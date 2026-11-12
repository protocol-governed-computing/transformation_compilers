"""The `DISCHARGE_OUTCOME_REFUSES` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _at,
    _cell,
    _routing,
    _rows,
    _topology,
    _value,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("DISCHARGE_OUTCOME_REFUSES")
def _discharge_outcome_refuses(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """The outcome a discharge names must route to an ending that refuses.

    The separate claim, and the one the other kind cannot make: a step may report exactly the
    outcome the register names and route it onward to the next step. The act then completes, having
    performed the operation the business said it refuses, and every cell of the discharge row was
    accurate.

    A refusing ending is one the topology types `EXIT`; a completing one is typed `EXIT_SUCCESS`.
    The type is what is read, never the node's name — a name is a convention anybody can break by
    calling an exit something reassuring, and `EXIT_REJECTED` is a spelling rather than a
    declaration.

    A row this rule cannot resolve is left to `DISCHARGE_GROUNDED_IN_TOPOLOGY`, which is the rule
    that says so.
    """
    topology = _topology(doc, rule)
    act_column = rule.params.get("act_column", "Act")
    step_column = rule.params.get("step_column", "Step")
    outcome_column = rule.params.get("outcome_column", "Outcome")
    routing_column = rule.params.get("routing_column", "Routing")
    type_column = rule.params.get("type_column", "Node Type")
    refusing = rule.params.get("refusing_type", "EXIT")

    out = []
    for i, row in _rows(doc, rule):
        act = _cell(row, act_column)
        step = _cell(row, step_column)
        outcome = _cell(row, outcome_column)
        node = topology.get((act, step))
        if node is None:
            continue
        destination = _routing(_value(node, routing_column)).get(outcome)
        if not destination:
            continue
        ending = topology.get((act, destination))
        if ending is None:
            out.append((
                _at(_where(rule), i),
                f"{outcome!r} routes to {destination!r} and {act.split('::')[-1]} declares no such "
                f"node — an ending the topology does not state is one nothing can be said about",
            ))
            continue
        node_type = _cell(ending, type_column).strip().upper()
        if node_type != refusing:
            out.append((
                _at(_where(rule), i),
                f"{outcome!r} routes to {destination!r}, typed {node_type or 'nothing'} — a "
                f"discharge must reach an ending typed {refusing}, and this one does not refuse",
            ))
    return out
