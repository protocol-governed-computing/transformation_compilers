"""The rule sets the derive route applies, sealed: an `$id`, revisions and a digest.

The doctrine, the ledger schema and the question catalog each decide what a derived design is, so
each is sealed as a phase's rule set is (`transformation.design.effectivity`). Its digest is taken
over the document without its revisions. A change records a revision with the digest it produced
(`tc phase derive revise`), and a derivation is refused while a document's digest is not its last
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


DOSSIERS = HERE.parents[2] / "dossiers"
ROUTE_SEALS = HERE / "route_seals.yaml"
CHANGE_FILE = "change.md"
PIN_FILE = "baseline.json"
# A route change authors code and sealed documents, which construction does not render, so its
# dossier is complete at P6 (THE_SHAPE_OF_A_CHANGE §5). Each phase's document, by its file prefix,
# and the phases it is judged against: the register schemas' `x-priors`.
PHASES = {"p0": "p0_seed_", "p1": "p1_change_request_", "p2": "p2_domain_model_", "p3": "p3_analysis_loop_",
          "p4": "p4_business_model_", "p5": "p5_business_intent_", "p6": "p6_governance_intent_"}
PRIORS = {"p0": [], "p1": ["p0"], "p2": ["p1"], "p3": ["p2"], "p4": ["p3"], "p5": ["p0"], "p6": ["p5", "p0"]}
SEALING = False   # set only while `tc phase derive seal` re-derives the ledgers under a new seal


class Unsealed(ValueError):
    """A sealed document's content is not the content its last revision records, or the route is not
    one a dossier sealed."""


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
                f"records {revisions[-1]['digest']} — a change records a revision (`tc phase derive revise`)")
    return None


# -- the route, sealed whole ---------------------------------------------------------------------
#
# The sealed documents decide part of a derived design; the building blocks, which are code, decide
# the rest. A route change, to either, runs as its own dossier, `dossiers/<subject>/`, whose
# `change.md` says what changed and why. `tc phase derive seal` records the change in
# `route_seals.yaml`: the digest of every file of the route as the change left it, and what
# re-deriving each ledger gave. A derivation is refused while the route is not one a seal records.

def route_files() -> list[Path]:
    """Every file that decides a derived design: the package's modules and its sealed documents."""
    return sorted([*HERE.glob("*.py"), *SEALED.values()])


def file_digest(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def route_now() -> dict[str, str]:
    return {p.name: file_digest(p) for p in route_files()}


def seals() -> list[dict[str, Any]]:
    """Every recorded seal of the route, oldest first."""
    if not ROUTE_SEALS.is_file():
        return []
    return (yaml.safe_load(ROUTE_SEALS.read_text(encoding="utf-8")) or {}).get("seals") or []


def route_unsealed() -> str | None:
    """Why the route as it stands is not one a seal records, or None when one does."""
    now, sealed = route_now(), seals()
    if any(s.get("route") == now for s in sealed):
        return None
    if not sealed:
        return "no seal records the derive route — a route change runs as its own dossier (`tc phase derive seal`)"
    last = sealed[-1]
    differs = sorted(f for f in set(now) | set(last["route"]) if now.get(f) != last["route"].get(f))
    return (f"the derive route was changed outside a dossier: {', '.join(differs)} "
            f"{'differs' if len(differs) == 1 else 'differ'} from the route "
            f"dossiers/{last['dossier']} sealed — a route change runs as its own dossier (`tc phase derive seal`)")


def route_in_force() -> dict[str, Any]:
    """The seal the route is. Refused when none is, unless a seal is being made."""
    why = route_unsealed()
    if why and not SEALING:
        raise Unsealed(why)
    now = route_now()
    dossier = next((s["dossier"] for s in seals() if s.get("route") == now), "being sealed")
    whole = hashlib.sha256(json.dumps(now, sort_keys=True).encode("utf-8")).hexdigest()
    return {"id": "the derive route", "revision": dossier, "digest": "sha256:" + whole}


def phase_documents(dossier: Path) -> dict[str, Path | None]:
    """The dossier's document for each phase P0 to P6, or None where it has none."""
    return {ph: next(iter(sorted(dossier.glob(f"{prefix}*.md"))), None) for ph, prefix in PHASES.items()}


def unsealed_dossiers() -> list[str]:
    """Seals whose dossier is missing from the repository or says nothing, and seals that skip the
    phases once a seal has been judged by them."""
    out = []
    judged = False
    for s in seals():
        judged = judged or bool(s.get("phases"))
        if judged and not s.get("phases"):
            out.append(f"seal of dossiers/{s['dossier']}: no phase verdicts, after a seal judged by the phases")
        if judged and any(v.get("verdict") != "ADMISSIBLE" for v in (s.get("phases") or {}).values()):
            out.append(f"seal of dossiers/{s['dossier']}: a phase document was not admissible")
    if not DOSSIERS.parent.joinpath("pyproject.toml").is_file():
        return out   # an installed package carries its seals, not the repository's dossiers
    for s in seals():
        d = DOSSIERS / s["dossier"]
        if s.get("phases"):
            missing = [ph for ph, doc in phase_documents(d).items() if doc is None]
            if missing:
                out.append(f"seal of dossiers/{s['dossier']}: the dossier has no {', '.join(missing)} document")
        elif not (d / CHANGE_FILE).is_file():
            out.append(f"seal of dossiers/{s['dossier']}: the dossier has no {CHANGE_FILE}")
    return out


def record_seal(dossier: str, change: str, rederived: dict[str, Any],
                phases: dict[str, Any] | None = None, pinned: str | None = None) -> dict[str, Any]:
    """Append a seal of the route as it stands. Refused when a seal already records it."""
    now = route_now()
    sealed = seals()
    if any(s.get("route") == now for s in sealed):
        raise Unsealed(f"a seal already records this route (dossiers/{next(s['dossier'] for s in sealed if s['route'] == now)})")
    entry = {"dossier": dossier, "change": change, "route": now, "rederived": rederived}
    if phases is not None:
        entry = {"dossier": dossier, "change": change, "pinned": pinned, "phases": phases, "route": now,
                 "rederived": rederived}
    head = ("# Seals of the derive route, oldest first. Written by `tc phase derive seal`; never edited.\n"
            "# Each records a route change's dossier, the digest of every file of the route as the change\n"
            "# left it, and what re-deriving each ledger gave. A derivation is refused unless one matches.\n")
    ROUTE_SEALS.write_text(head + yaml.safe_dump({"seals": sealed + [entry]}, sort_keys=False, allow_unicode=True,
                                                 width=100), encoding="utf-8")
    return entry


def judged_by() -> dict[str, dict[str, Any]]:
    """The sealed documents a derivation applies. Refused when any is not its last revision."""
    out = {}
    for name in SEALED:
        why = unrecorded(name)
        if why:
            raise Unsealed(why)
        doc = load(name)
        out[name] = {"id": doc["$id"], "revision": doc["x-revisions"][-1]["revision"], "digest": digest(doc)}
    out["route"] = route_in_force()
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
