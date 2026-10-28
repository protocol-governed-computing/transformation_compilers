"""The rule sets the decision compiler applies, sealed: an `$id`, revisions and a digest.

The doctrine, the ledger schema and the question catalog each decide what a derived design is, so
each is sealed as a phase's rule set is (`transformation.design.effectivity`). Its digest is taken
over the document without its revisions. A change records a revision with the digest it produced
(`tc decision revise`), and a derivation is refused while a document's digest is not its last
revision's. Every derived design names the three as `judged_by`.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

import yaml

from inspector import api as inspector_api

HERE = Path(__file__).parent
SEALED = {"doctrine": HERE / "doctrine.yaml", "ledger_schema": HERE / "ledger_schema.yaml",
          "catalog": HERE / "catalog.yaml"}
REVISIONS = re.compile(r"^x-revisions:.*\Z", re.MULTILINE | re.DOTALL)


class Unsealed(ValueError):
    """A sealed document's content is not the content its last revision records."""


def load(name: str) -> dict[str, Any]:
    return yaml.safe_load(SEALED[name].read_text(encoding="utf-8"))


def digest(doc: dict[str, Any]) -> str:
    body = {k: v for k, v in doc.items() if k != "x-revisions"}
    text = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def unrecorded(name: str) -> str | None:
    """Why a document is not its last recorded revision, or None when it is."""
    doc = load(name)
    revisions = doc.get("x-revisions") or []
    if not revisions:
        return f"{doc['$id']} records no revision"
    actual = digest(doc)
    if revisions[-1]["digest"] != actual:
        return (f"{doc['$id']} digests to {actual}, but its last revision ({revisions[-1]['revision']}) "
                f"records {revisions[-1]['digest']} — a change records a revision (`tc decision revise`)")
    return None


def judged_by() -> dict[str, dict[str, Any]]:
    """The sealed documents a derivation applies. Refused when any is not its last revision."""
    out = {}
    for name in SEALED:
        why = unrecorded(name)
        if why:
            raise Unsealed(why)
        doc = load(name)
        out[name] = {"id": doc["$id"], "revision": doc["x-revisions"][-1]["revision"], "digest": digest(doc)}
    return out


def revise(name: str, change: str) -> dict[str, Any]:
    """Record a revision of one sealed document, with the digest its content now has."""
    path, doc = SEALED[name], load(name)
    revisions = list(doc.get("x-revisions") or [])
    actual = digest(doc)
    if revisions and revisions[-1]["digest"] == actual:
        raise Unsealed(f"{doc['$id']} revision {revisions[-1]['revision']} already records {actual}")
    revisions.append({"revision": len(revisions) + 1, "change": change, "digest": actual})
    block = yaml.safe_dump({"x-revisions": revisions}, sort_keys=False, allow_unicode=True, width=100)
    text = path.read_text(encoding="utf-8")
    text = REVISIONS.sub(lambda _: block, text) if REVISIONS.search(text) else text.rstrip("\n") + "\n\n" + block
    path.write_text(text, encoding="utf-8")
    return revisions[-1]


def doctrine_closure(snapshot_root: Path) -> list[str]:
    """Why the doctrine's citations do not close, or nothing when they do.

    Every rule cites what it realizes: invariants the composition holds, or `none` with the reason
    no invariant states it. A cited invariant that does not resolve is refused, as is a rule that
    cites nothing and gives no reason.
    """
    out = []
    for name, rule in load("doctrine")["rules"].items():
        cited = rule.get("realizes")
        if cited == "none":
            if not rule.get("unstated_because"):
                out.append(f"{name}: realizes none, and gives no reason")
            continue
        if not cited:
            out.append(f"{name}: cites nothing it realizes")
            continue
        for fqdn in cited:
            status, _ = inspector_api.query("si.artifact.show", {"artifact": fqdn}, str(snapshot_root))
            if status != "SUCCESS" or "::INVARIANT_" not in fqdn:
                out.append(f"{name}: cites {fqdn}, which is not an invariant the composition holds")
    return out
