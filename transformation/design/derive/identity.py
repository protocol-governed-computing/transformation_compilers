"""Which identity each derived artifact takes, decided by meaning (`transformation.build.sameness`).

A derived design names every artifact of its domain. Compared with what the composition holds:
- an artifact the composition holds, rendered with the same meaning, keeps its identity. The
  design amends it (EXTEND);
- one rendered with a changed meaning takes the next version never used, in the composition, the
  published release or the retirement ledger. So does one that names it: the successor's name is
  part of its meaning. It names its predecessor in `supersedes`, and the
  predecessor is replaced (REPLACE);
- one the composition does not hold is new;
- one the composition holds that an operation `replaces`, by the ledger's answer, is replaced by
  that operation's workflow or entrance. An artifact supersedes one predecessor, so of several
  the first named is replaced and the rest are retired;
- one the composition holds and the design no longer names is retired. A retirement is recorded:
  the build deletes it and writes the entry the retirement ledger takes.

The comparison renders the spliced dossier exactly as construction will, carries forward what no
register states, and applies the platform's declaration of what carries no meaning. Construction
compares the result again when it emits, so a wrong decision here is refused there.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from inspector import api as inspector_api
from transformation.build import sameness
from transformation.build.completeness import carry_forward
from transformation.build.render import implementation_namespace, render_all
from transformation.design.derive.splice import short
from transformation.design.read import read_seed
from transformation.machine_block import machine_yaml

VERSION = re.compile(r"^(?P<stem>.+)_V(?P<n>\d+)$")


def registers(dossier: Path, phase_key: str) -> dict:
    """A dossier phase document's registers, as the plain rows construction reads."""
    doc = read_seed(next(dossier.glob(f"{phase_key}_*.md")))
    out: dict[str, list[dict]] = {}
    for entry in doc.registers:
        block = doc.register(entry["id"])
        if block and block.table:
            out[entry["id"]] = block.table.rows
    return out


def namespace(domain_root: Path) -> str | None:
    """The implementation namespace the domain's build manifest declares, as construction reads it."""
    for path in sorted((domain_root / "registry").glob("**/STRUCTURE_BUILD_*_CONFIG_V*.md")):
        block = machine_yaml(path.read_text(encoding="utf-8"))
        if block is not None:
            return implementation_namespace(yaml.safe_load(block) or {})
    return None


def held(fqdn: str, snapshot: Path) -> dict | None:
    status, result = inspector_api.query("si.artifact.show", {"artifact": fqdn}, str(snapshot))
    if status != "SUCCESS":
        return None
    return sameness.machine(sameness.canonical(result).get("content", ""))


def listed(snapshot: Path) -> set[str]:
    status, result = inspector_api.query("si.artifact.list", {}, str(snapshot))
    return {e["artifact"] for e in result.get("artifacts", [])} if status == "SUCCESS" else set()


def used(snapshot: Path, release: Path | None, ledger: Path | None) -> set[str]:
    """Every identity ever used: live in the composition, published, or retired by record."""
    out = listed(snapshot)
    if release is not None and (release / "manifest.json").is_file():
        out |= listed(release)
    if ledger is not None and ledger.is_file():
        out |= {e["identity"] for e in (yaml.safe_load(ledger.read_text(encoding="utf-8")) or {}).get("retired") or []}
    return out


def next_version(fqdn: str, taken: set[str]) -> str:
    m = VERSION.match(fqdn)
    n = int(m["n"]) + 1
    while f"{m['stem']}_V{n}" in taken:
        n += 1
    return f"{m['stem']}_V{n}"


def decide(dossier: Path, snapshot: Path, domain_root: Path, baseline: list[str],
           release: Path | None = None, ledger: Path | None = None, replaces: dict | None = None) -> dict:
    """The identity each artifact of a spliced dossier takes. `baseline` is the domain's design of
    record's artifacts: what the composition holds of this domain. `replaces` maps what the ledger
    says an operation takes the place of to the artifact that does."""
    p7, p8 = registers(dossier, "p7"), registers(dossier, "p8")
    decl = sameness.read(snapshot)
    ns = domain_root.name + "::"
    rendered = render_all(p7, p8, namespace(domain_root))
    code_of = lambda a: ns + a["path"].rsplit("/", 1)[-1].removesuffix(".md")
    was = {code_of(a): held(code_of(a), snapshot) for a in rendered}
    was = {c: d for c, d in was.items() if d is not None}
    carry_forward(rendered, {short(c): d for c, d in was.items()})
    kept, changed, new = [], {}, []
    # A design names its artifacts in `new_artifacts`; what else renders (a transform's test data)
    # follows the artifact it belongs to.
    named = {r["code"] for r in p7.get("new_artifacts", [])}
    for a in rendered:
        code = code_of(a)
        if code not in named:
            continue
        if code not in was:
            new.append(code)
            continue
        places = sameness.differences(was[code], a["machine"], decl, {})
        if places:
            changed[code] = places
        else:
            kept.append(code)
    # A kept artifact that names a superseded one is compared again with the successors' names in
    # place, as construction compares it: a reference that follows its successor is the same
    # reference, and a name that is a place (a workflow's node key) is not. Repeat until none moves.
    taken = used(snapshot, release, ledger) | set(kept) | set(new)
    successor = {}
    by_code = {code_of(a): a for a in rendered}
    while True:
        for code in sorted(c for c in changed if c not in successor):
            successor[code] = next_version(code, taken)
            taken.add(successor[code])
        moved = {short(c): short(n) for c, n in successor.items()}
        follows = {**successor, **moved}
        cascade = {}
        for c in kept:
            renamed = renumber({"m": by_code[c]["machine"]}, moved)["m"]
            if renamed != by_code[c]["machine"]:
                places = sameness.differences(was[c], renamed, decl, follows)
                if places:
                    cascade[c] = places
        if not cascade:
            break
        for c, places in cascade.items():
            kept.remove(c)
            changed[c] = places
    derived = set(kept) | set(changed) | set(new)
    # An artifact supersedes one predecessor. Where an operation takes the place of several, the
    # first it names is its predecessor and the others are retired with no successor.
    replaced, succeeded = {}, set()
    for old, new in (replaces or {}).items():
        if old not in derived and new not in succeeded:
            replaced[old] = new
            succeeded.add(new)
    replaced = dict(sorted(replaced.items()))
    retired = sorted(c for c in baseline if c not in derived and c not in replaced)
    return {"kept": sorted(kept), "new": sorted(new),
            "superseded": {c: successor[c] for c in sorted(changed)},
            "changed_at": {c: len(p) for c, p in sorted(changed.items())},
            "replaced": replaced, "retired": retired}


def renumber(generated: dict, superseded: dict[str, str]) -> dict:
    """The derived rows with every superseded identity, full or short, named by its successor."""
    text = json.dumps(generated)
    for old, new in superseded.items():
        text = re.sub(rf"(?<![A-Z0-9_]){re.escape(short(old))}(?![A-Z0-9_])", short(new), text)
    return json.loads(text)
