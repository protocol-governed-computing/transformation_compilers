"""The `TOPOLOGY_ROUTE_RESOLVES` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _normalise,
    _routing,
    _rows,
    _value,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("TOPOLOGY_ROUTE_RESOLVES")
def _topology_route_resolves(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Every routing target is a node of the same workflow.

    A target is a key, not a contract: once a contract runs at several places, naming the contract
    no longer says which one control reaches.

    A design that amends a workflow declares the places it changes, not every place the workflow
    has, so a route to an unchanged place resolves against the composition. Without an observation
    only the design's own rows count, and such a route is reported rather than assumed.
    """
    exempt = tuple(rule.params.get("exempt_prefixes") or ())
    rows = list(_rows(doc, rule))
    composed: dict[tuple[Locator, str], set[str]] = {}
    observation = rule.params.get("observation")
    for entry in (doc.observed.get(observation) or []) if observation else []:
        composed[(entry["domain"], entry["wf_code"])] = set(entry["nodes"])
    nodes: dict[str, set[str]] = {}
    for _, row in rows:
        cell = _normalise(_cell(row, "Workflow"))
        workflow = _bare_identity(cell)
        domain = cell.split("::", 1)[0] if "::" in cell else ""
        nodes.setdefault(workflow, set(composed.get((domain, workflow), ()))).add(
            _bare_identity(_cell(row, "Node")))
    out = []
    for i, row in rows:
        workflow = _bare_identity(_cell(row, "Workflow"))
        for outcome, target in _routing(_value(row, "Routing")).items():
            bare = _bare_identity(target)
            if not bare or bare.startswith(exempt) or bare in nodes[workflow]:
                continue
            out.append((
                _at(_where(rule), i),
                f"{outcome} routes to {target!r}, which is no node of {workflow}",
            ))
    return out
