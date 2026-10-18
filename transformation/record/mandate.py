"""A baseline P8: the authoring mandate for a baseline P7, derived from it and the registry.

A mandate orders the build and decides nothing. What is scheduled is P7's `new_artifacts`; what each
depends on is every full name its declaration holds that the design also schedules; the waves are
the longest path over those dependencies.
"""
from __future__ import annotations

import re
from typing import Any

FULL = re.compile(r"^[a-z_][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+$")
ORDER = ["STRUCTURE", "VOCAB", "AC", "EV", "CT", "CC", "IN", "WF", "RB", "TI", "TE"]


def _names(value: Any) -> list[str]:
    """Every full name a declaration holds, in the order it holds them."""
    if isinstance(value, str):
        return [value] if FULL.match(value) else []
    if isinstance(value, dict):
        return [n for v in value.values() for n in _names(v)]
    if isinstance(value, list):
        return [n for v in value for n in _names(v)]
    return []


def _fields(interface: list[dict], code: str, direction: str) -> str:
    return ", ".join(f"{f['field']}:{f['type']}" for f in interface
                     if f["artifact"] == code and f["direction"] == direction)


def p8(held: list[dict], p7: dict[str, Any]) -> dict[str, Any]:
    by_fqdn = {a["fqdn"]: a for a in held}
    new = p7["new_artifacts"]
    declared = [a["code"] for a in new]
    family = {a["code"]: a["family"] for a in new}
    owner = {a["code"]: a["owner_subdomain"] for a in new}
    summary = {a["code"]: a["summary"] for a in new}

    # A bare name in a workflow or contract is a name in the declaring domain.
    namespace = declared[0].split("::")[0] if declared else ""
    deps: dict[str, list[str]] = {}
    for code in declared:
        machine = {k: v for k, v in by_fqdn[code]["machine"].items()
                   if k not in ("fqdn", "supersedes", "superseded_by")}
        named = _names(machine)
        if family[code] == "WF":
            named += [f"{namespace}::{key}" for key in machine["core"]["nodes"]]
        deps[code] = [n for n in dict.fromkeys(named) if n in family and n != code]

    wave: dict[str, int] = {}

    def depth(code: str, seen: tuple = ()) -> int:
        if code not in wave:
            wave[code] = 1 + max((depth(d, seen + (code,)) for d in deps[code] if d not in seen),
                                 default=0)
        return wave[code]

    for code in declared:
        depth(code)
    ordered = sorted(declared, key=lambda c: (wave[c], ORDER.index(family[c]), declared.index(c)))

    path: list[str] = []
    if ordered:
        path = [max(ordered, key=lambda c: (wave[c], -ordered.index(c)))]
        while authored := [d for d in deps[path[-1]] if d not in path]:
            path.append(max(authored, key=lambda d: (wave[d], -declared.index(d))))
        path.reverse()

    counts = {f: sum(1 for c in declared if family[c] == f) for f in ORDER}
    interface = p7["interface_fields"]
    return {
        "build_order": [{"wave": str(wave[c]), "step": str(i), "code": c, "action": "NEW",
                         "subdomain": owner[c], "depends_on": deps[c] or None}
                        for i, c in enumerate(ordered, 1)],
        "critical_path": [{"position": str(i), "code": c} for i, c in enumerate(path, 1)],
        "mandate_artifact_summary": [{
            "action": "NEW", "count": str(len(declared)),
            "description": ", ".join(f"{n} {f}" for f, n in counts.items() if n)}],
        "field_declarations": [{"code": c, "subdomain_field": owner[c]} for c in ordered],
        "new_capabilities": [{"code": c, "purpose": summary[c],
                              "inputs": _fields(interface, c, "INPUT"),
                              "outputs": _fields(interface, c, "OUTPUT")}
                             for c in ordered if family[c] == "CT"],
        "new_intents": [{"code": c, "purpose": summary[c],
                         "workflow": by_fqdn[c]["machine"]["core"].get("workflow"),
                         "inputs": _fields(interface, c, "INPUT")}
                        for c in ordered if family[c] == "IN"],
        "cross_subdomain_notes": [],
    }
