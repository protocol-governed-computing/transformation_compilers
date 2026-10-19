"""The `DISCHARGE_GROUNDED_IN_TOPOLOGY` procedure (DESIGN_LANGUAGE §6)."""

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


@check("DISCHARGE_GROUNDED_IN_TOPOLOGY")
def _discharge_grounded_in_topology(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A stated discharge must name a step the act really has, and an outcome that step reports.

    A register read only for presence documents intent and enforces nothing. The seed says the
    business refuses an operation under a condition; this register says where that refusal happens;
    and until something holds the second to the first, a design may name a step no act has and be
    admissible for saying so — which is a refusal that stops nothing, written in the language of one
    that does.

    Act, step and outcome are checked together and reported once. They are three cells of one claim:
    a step that is not in the act has no outcomes to check, and splitting the claim across rules
    would report a single wrong row two or three times over.

    The topology is the design's own, read from the same document. No composition fact is observed —
    a design is judged on whether it is internally answerable, and an act it is authoring exists
    nowhere else yet.
    """
    topology = _topology(doc, rule)
    act_column = rule.params.get("act_column", "Act")
    step_column = rule.params.get("step_column", "Step")
    outcome_column = rule.params.get("outcome_column", "Outcome")
    routing_column = rule.params.get("routing_column", "Routing")

    out = []
    for i, row in _rows(doc, rule):
        act = _cell(row, act_column)
        step = _cell(row, step_column)
        outcome = _cell(row, outcome_column)
        if not act or not step or not outcome:
            # An empty cell is `CELL_NOT_EMPTY`'s finding. Grounding a blank would report the same
            # omission a second time, in worse words.
            continue
        node = topology.get((act, step))
        if node is None:
            out.append((
                _at(_where(rule), i),
                f"{step!r} is no step of {act} — the discharge names a place in an act that has "
                f"no such place, so nothing carries the refusal out",
            ))
            continue
        reported = _routing(_value(node, routing_column))
        if outcome not in reported:
            known = ", ".join(sorted(reported)) or "nothing"
            out.append((
                _at(_where(rule), i),
                f"{step.split('::')[-1]} does not report {outcome!r} — it reports {known}, and a "
                f"discharge on an outcome the step never returns never happens",
            ))
    return out
