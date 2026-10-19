"""The `CELL_PREFIXED_BY_COLUMN` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _cell, _rows, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("CELL_PREFIXED_BY_COLUMN")
def _cell_prefixed_by_column(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """One column must agree with another in the same row.

    A register that classifies its own rows can disagree with itself: a code named `CC_…` filed
    under family `WF` is well-formed in both cells and wrong as a pair. Checking each column against
    a fixed vocabulary cannot see it, because both values are individually legal.
    """
    column = rule.params["column"]
    prefix_column = rule.params["prefix_column"]
    separator = rule.params.get("separator", "_")

    out = []
    for i, row in _rows(doc, rule):
        value = _cell(row, column)
        prefix = _cell(row, prefix_column)
        if not value or not prefix:
            continue                             # emptiness is CELL_NOT_EMPTY's finding
        if not value.startswith(f"{prefix}{separator}"):
            out.append((
                _at(_where(rule), i),
                f"{value!r} does not agree with {prefix_column} {prefix!r} — "
                f"the row classifies itself two ways",
            ))
    return out
