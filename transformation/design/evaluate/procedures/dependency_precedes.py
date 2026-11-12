"""The `DEPENDENCY_PRECEDES` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _cell, _items, _rows, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("DEPENDENCY_PRECEDES")
def _dependency_precedes(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Everything a row depends on must be built before it.

    This is what makes a build order a *topological* sort rather than a list. A mandate whose steps
    are individually well formed but whose dependency is scheduled later is not a sequence anyone
    can execute — and the defect is invisible in either row alone.

    A dependency that is not itself a step is a prerequisite from outside this build (an artifact
    that already exists), which is legitimate and deliberately not reported here.
    """
    column = rule.params["column"]
    depends_column = rule.params["depends_column"]
    order_column = rule.params["order_column"]
    none_markers = {str(m).strip() for m in rule.params.get("none_markers", ["—", "-", "NONE", ""])}

    position: dict[str, int] = {}
    rows = []
    for i, row in _rows(doc, rule):
        code = _cell(row, column)
        step = _cell(row, order_column)
        try:
            step_number = int(step)
        except ValueError:
            continue
        if code:
            position[code] = step_number
        rows.append((i, code, step_number, _items(row, depends_column)))

    out = []
    for i, code, step_number, depends in rows:
        for part in depends:
            prerequisite = position.get(part)
            if prerequisite is None:
                continue          # built outside this mandate — legitimate
            if prerequisite >= step_number:
                out.append((
                    _at(_where(rule), i),
                    f"{code!r} is step {step_number} but depends on {part!r} at step "
                    f"{prerequisite} — a prerequisite scheduled later is not a build order",
                ))
    return out
