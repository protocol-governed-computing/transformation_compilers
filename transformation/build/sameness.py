"""
Whether an amendment keeps an artifact's meaning, by the rules the platform declares.

A change of meaning is a new identity (`4c` ID-5, `4e` SU-11); a change of how a declaration is
written keeps the one it has. Construction compared an amendment with what it amends only for the
facts it would lose, so an amendment that added or altered a fact was built under the old identity,
and every change of the last cycle was. This compares the whole declaration.

What carries no meaning is not decided here. The platform declares it in
`artifact::VOCAB_DECLARATION_REPRESENTATION_V0`: the parts that only explain, the lists read as
sets, the parts that name another artifact, and the rules a comparison applies. This module applies
exactly those rules, and refuses to compare when the declaration names one it does not apply — a
comparison that skipped a declared rule would call a change of wording a change of meaning, or the
reverse, without saying so.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from inspector import api as inspector_api

DECLARATION = "artifact::VOCAB_DECLARATION_REPRESENTATION_V0"

# The rules this module applies. The declaration must name exactly these.
APPLIED = frozenset({"explanation_only_as_text", "reference_to_declared_successor"})

MACHINE = re.compile(r"```yaml\n(.*?)```", re.S)


class Uncomparable(ValueError):
    """The declaration cannot be read, or names a rule this comparison does not apply."""


@dataclass(frozen=True)
class Declaration:
    documentation: frozenset[str]
    unordered: frozenset[str]
    reference: frozenset[str]
    reference_keyed: frozenset[str]

    @classmethod
    def from_frontmatter(cls, fm: dict) -> "Declaration":
        if fm.get("superseded_by"):
            raise Uncomparable(f"{DECLARATION} is stood down by {fm['superseded_by']}; construction "
                               f"reads it by exact identity and must be re-pointed to its successor")

        def group(name: str) -> frozenset[str]:
            entries = (fm.get(name) or {}).get("entries") if isinstance(fm.get(name), dict) else None
            if not entries:
                raise Uncomparable(f"{DECLARATION} declares no '{name}' entries")
            return frozenset(entries)

        rules = group("sameness_rules")
        if rules != APPLIED:
            raise Uncomparable(
                f"{DECLARATION} declares the comparison rules {sorted(rules)}; construction applies "
                f"{sorted(APPLIED)}. A comparison that does not apply what the platform declares "
                f"cannot say whether meaning changed")
        return cls(group("documentation"), group("unordered"), group("reference"),
                   group("reference_keyed"))


def read(snapshot_root: Path) -> Declaration:
    """The platform's declaration, read from the composition by its exact identity."""
    status, result = inspector_api.query("si.artifact.show", {"artifact": DECLARATION},
                                         str(snapshot_root))
    if status != "SUCCESS":
        raise Uncomparable(f"{DECLARATION} is not in the composition at {snapshot_root}")
    return Declaration.from_frontmatter(canonical(result).get("frontmatter") or {})


def canonical(show_result: dict) -> dict:
    """The canonical record `si.artifact.show` returns, as a mapping."""
    record = show_result.get("canonical") or {}
    return record if isinstance(record, dict) else {}


def machine(text: str) -> dict:
    found = MACHINE.search(text)
    return (yaml.safe_load(found.group(1)) or {}) if found else {}


def _is_text(value: Any) -> bool:
    return isinstance(value, str) or (
        isinstance(value, list) and all(isinstance(v, str) for v in value))


def _repointed(value: Any, successor: dict[str, str]) -> Any:
    """A reference value with each name this design replaces read as its declared successor."""
    if isinstance(value, str):
        return successor.get(value, value)
    if isinstance(value, list):
        return [_repointed(v, successor) for v in value]
    if isinstance(value, dict):
        return {successor.get(k, k): _repointed(v, successor) for k, v in value.items()}
    return value


def _leaves(value: Any, path: str, key: str, decl: Declaration, out: dict,
            successor: dict[str, str] | None, under: bool) -> None:
    """Every fact that carries meaning, addressed by where it sits.

    `successor`, when given, re-points the references of the declaration being read, so a reference
    to what a design replaces compares equal to one naming its successor.
    """
    if isinstance(value, dict):
        for k, item in value.items():
            if k in decl.documentation and _is_text(item):
                continue
            if successor is not None and k in decl.reference_keyed and isinstance(item, dict):
                item = {successor.get(name, name): inner for name, inner in item.items()}
            _leaves(item, f"{path}.{k}", k, decl, out, successor, under or k in decl.reference)
    elif isinstance(value, list):
        if key in decl.unordered:
            members = [_repointed(v, successor) if (successor is not None and under) else v
                       for v in value]
            out[path] = ("set", frozenset(json.dumps(m, sort_keys=True, default=str)
                                          for m in members))
            return
        for index, item in enumerate(value):
            ident = next((item[k] for k in ("step", "code", "name")
                          if isinstance(item, dict) and item.get(k)), index)
            _leaves(item, f"{path}[{ident}]", key, decl, out, successor, under)
    else:
        if successor is not None and under and isinstance(value, str):
            value = successor.get(value, value)
        out[path] = ("value", value)


def differences(was: dict, now: dict, decl: Declaration, successor: dict[str, str]) -> list[str]:
    """The places where `now` means something `was` did not.

    `successor` maps each artifact this design replaces, by full name and by short code, to its one
    declared successor. A reference re-pointed along it is the same reference; nothing else is
    excused but what the platform declares.
    """
    as_was: dict = {}
    repointed: dict = {}
    after: dict = {}
    _leaves(was, "", "", decl, as_was, None, False)
    _leaves(was, "", "", decl, repointed, successor, False)
    _leaves(now, "", "", decl, after, None, False)
    # A reference may stay as it was or follow its successor; whether a live artifact may still
    # name what a design replaces is the reach check's to answer, not this one's.
    places = set(as_was) | set(repointed) | set(after)
    return sorted(p.lstrip(".") for p in places
                  if after.get(p) != as_was.get(p) and after.get(p) != repointed.get(p))


def successors(supersessions: dict[str, tuple[str, list[str]]]) -> dict[str, str]:
    """Each replaced artifact's one declared successor, by full name and by short code."""
    out: dict[str, str] = {}
    for retired, named in supersessions.values():
        if len(named) != 1:
            continue
        out[retired] = named[0]
        out[retired.split("::")[-1]] = named[0].split("::")[-1]
    return out


def _raw_leaves(value: Any, path: str, decl: Declaration, under: bool, out: dict) -> None:
    """Every leaf as written, with whether it sits at or beneath a reference part."""
    if isinstance(value, dict):
        for k, item in value.items():
            _raw_leaves(item, f"{path}.{k}", decl, under or k in decl.reference, out)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _raw_leaves(item, f"{path}[{index}]", decl, under, out)
    else:
        out[path] = (value, under)


def _moves_only_a_reference(was: dict, now: dict, decl: Declaration) -> bool:
    before: dict = {}
    after: dict = {}
    _raw_leaves(was, "", decl, False, before)
    _raw_leaves(now, "", decl, False, after)
    if set(before) != set(after):
        return False  # a key was renamed: a place, a route or a field, never a reference value
    changed = [p for p in after if after[p][0] != before[p][0]]
    return bool(changed) and all(after[p][1] for p in changed)


def repoint(text: str, successor: dict[str, str], decl: Declaration) -> str:
    """A document with each name this design replaces rewritten to its successor, where it is a
    reference and nowhere else.

    Rewritten as text, one occurrence at a time, so the document keeps its layout and its prose. An
    occurrence is kept only when the one value it changes sits at or beneath a declared reference
    part. A workflow names a contract it runs by short code in `code`, and labels the place it runs
    it in, and routes to that place, by the same spelling; the label and the route are not
    references, and rewriting them would rename a place rather than re-point it.
    """
    found = MACHINE.search(text)
    if not found:
        return text
    block = found.group(1)
    for old, new in sorted(successor.items(), key=lambda kv: -len(kv[0])):
        pattern = re.compile(rf"(?<![A-Za-z0-9_:]){re.escape(old)}(?![A-Za-z0-9_])")
        at = 0
        while (hit := pattern.search(block, at)) is not None:
            candidate = block[:hit.start()] + new + block[hit.end():]
            if _moves_only_a_reference(yaml.safe_load(block) or {},
                                       yaml.safe_load(candidate) or {}, decl):
                block, at = candidate, hit.start() + len(new)
            else:
                at = hit.end()
    return text[:found.start(1)] + block + text[found.end(1):]
