"""The `STEP_OPERATION_PUBLISHED` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _cell, _rows, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("STEP_OPERATION_PUBLISHED")
def _step_operation_published(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A step must name an operation its capability actually offers.

    `STEP_CONSUMES_PUBLISHED` skips a step whose operation it cannot resolve, with the note that the
    operation is another rule's business. That rule did not exist, and its absence was not one gap
    but three: an unresolvable operation makes the consumes check, the binding-source check and this
    one all pass in silence, because each of them looks the operation up and finds nothing to
    compare against.

    What it cost: a design declared two clock reads as `READ` where the clock offers only `NOW`, and
    bound their results to a field called `now` where the operation publishes `timestamp`. Admissible
    over a hundred and thirty-four rules, one hundred per cent construction-complete, and refused by
    the compiler at S4 on an invariant the design layer had every fact needed to check.

    A capability absent from the surface is reported rather than skipped. A side effect is substrate
    a business change reuses and never authors, so one the composition does not publish is a name
    that resolves to nothing.
    """
    observation = rule.params["observation"]
    published = doc.observed.get(observation) or []
    if not published:
        return [(
            _at(_where(rule)),
            "no capability surface was observed — a step's operation cannot be checked against "
            "operations nobody published",
        )]

    offered = {
        str(entry.get("capability")): set(entry.get("operations") or {})
        for entry in published
        if isinstance(entry, dict)
    }

    out = []
    for i, row in _rows(doc, rule):
        if _cell(row, "Kind") != "CS":
            continue
        capability, operation = _cell(row, "Capability"), _cell(row, "Operation")
        if capability not in offered:
            out.append((_at(_where(rule), i),
                        f"{capability!r} publishes no capability surface — a side effect is reused, "
                        f"never authored, so one the composition does not carry names nothing"))
            continue
        if operation and operation not in offered[capability]:
            out.append((_at(_where(rule), i),
                        f"{capability} offers no operation {operation!r} — it publishes "
                        f"{', '.join(sorted(offered[capability])) or 'none'}"))
    return out
