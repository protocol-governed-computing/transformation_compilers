"""The `OUTCOME_GROUNDED_IN_OPERATION` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from typing import Any

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _routing,
    _rows,
    _value,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


def _routing_outcomes(routing: Any) -> set[str]:
    """The outcomes a routing branches on, compared as the surface publishes them: upper-cased."""
    return {outcome.upper() for outcome in _routing(routing)}


@check("OUTCOME_GROUNDED_IN_OPERATION")
def _outcome_grounded_in_operation(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A step may only branch on an outcome its operation answers, or name what produced the rest.

    This is the data-to-decision closure, and until now it was asked as "is the cell filled?" —
    which an em-dash satisfies. Every `Interpreted By` and `Semantic Status` cell in every design
    in the corpus is an em-dash, so the discipline the template states had never once bound a
    design, while two rules reported it satisfied 62 times.

    The em-dash is a declaration, and what it declares is that the step's output is data: the
    branches are the operation's own statuses, and nothing had to interpret anything to reach them.
    That is true of all 62 — a registry claim exits on `ALREADY_EXISTS` because the registry says
    so, and a read exits on `NOT_FOUND` for the same reason. Requiring an interpretation there
    would demand a transform to restate what the store already answered.

    So the question is not whether the step reads. It is whether the design routes on an outcome
    the operation cannot produce. `exists` bound to `authorized` was exactly that: a branch named
    for a decision, on a step whose operation answers only SUCCESS and VIOLATION, with nothing in
    between to turn one into the other. `result_status_values` is published per operation, so the
    check needs no fact the composition does not already carry.

    An operation that does not resolve at all is `STEP_NAMES_UNPUBLISHED_OPERATION`'s finding, and
    reporting it here as well would say one thing twice.
    """
    observed = doc.observed.get(rule.params["observation"]) or []
    if not observed:
        return [(
            _at(_where(rule)),
            "no capability surface was observed — whether a step branches on an outcome its "
            "operation answers cannot be checked against operations nobody published",
        )]

    answers = {(_bare_identity(str(c.get("capability"))), op.upper()):
               {str(s).upper() for s in (spec.get("result_status_values") or [])}
               for c in observed if isinstance(c, dict)
               for op, spec in (c.get("operations") or {}).items()}

    none_markers = {str(m).strip() for m in rule.params.get("none_markers", ["—", "-", "NONE", ""])}
    column = rule.params["column"]

    out = []
    for i, row in _rows(doc, rule):
        if _cell(row, rule.params["kind_column"]).upper() != rule.params["kind_value"]:
            continue
        operation = _cell(row, "Operation").upper()
        declared = answers.get((_bare_identity(_cell(row, "Capability")), operation))
        if declared is None:
            continue
        named = _routing_outcomes(_value(row, rule.params["routing_column"]))
        status = _cell(row, rule.params["status_column"])
        if status not in none_markers:
            named.add(status.upper())
        undeclared = sorted(named - declared)
        if not undeclared or _cell(row, column) not in none_markers:
            continue
        out.append((
            _at(_where(rule), i),
            rule.params["detail"].format(
                outcomes=", ".join(undeclared),
                operation=operation,
                answers=", ".join(sorted(declared)) or "nothing",
            ),
        ))
    return out
