"""The `CONSUMPTION_GROUNDED_IN_OPERATION` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _bare_identity, _cell, _items, _rows, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("CONSUMPTION_GROUNDED_IN_OPERATION")
def _consumption_grounded_in_operation(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A step consuming nothing must invoke an operation that takes nothing.

    `STEP_CONSUMES_UNDECLARED_INPUT` holds every named field to the published surface and skips the
    em-dash, which is the half that says a step hands the operation nothing at all. Nine steps in
    the corpus declare it, and until now the claim was unexamined: a `READ` consuming `—` addresses
    no key, and the operation receives null for the one input it has.

    Grounded in the operation's published `input`, so the dash is admissible exactly when there is
    nothing to hand over — `NOW` and `SELECT` take none, and both are in the corpus.

    CS steps only, for the reason the binding check gives: on a transform step the column carries
    domain-side names against the transform's own formals, so comparing them reports a defect where
    a mapping exists.
    """
    observed = doc.observed.get(rule.params["observation"]) or []
    if not observed:
        return [(
            _at(_where(rule)),
            "no capability surface was observed — whether a step hands an operation nothing cannot "
            "be checked against operations nobody published",
        )]

    inputs = {(_bare_identity(str(c.get("capability"))), op.upper()): list(spec.get("input") or [])
              for c in observed if isinstance(c, dict)
              for op, spec in (c.get("operations") or {}).items()}

    out = []
    for i, row in _rows(doc, rule):
        if _cell(row, rule.params["kind_column"]) != rule.params["kind_value"]:
            continue
        operation = _cell(row, "Operation").upper()
        declared = inputs.get((_bare_identity(_cell(row, rule.params["capability_column"])), operation))
        if not declared:
            continue
        if _items(row, rule.params["column"]):
            continue
        out.append((
            _at(_where(rule), i),
            rule.params["detail"].format(
                operation=operation,
                accepts=", ".join(sorted(declared)),
            ),
        ))
    return out
