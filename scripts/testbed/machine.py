"""Write a phase document for a probe: a title, and its registers in a Machine block.

The design tests build small documents to trip one rule and leave the rest silent. They state a
register as its column titles and its rows, and this writes it in the form the reader reads: a list
of rows, each a mapping from column key to value. A value is written as given, so a probe states a
list, a routing or a binding as the structure it is. An empty register is declared empty, `[]`,
unless `declared_empty` is false, which leaves it stating nothing, `null`. A cell given as `ABSENT`
is left out of its row.
"""
from __future__ import annotations

from typing import Iterable

from transformation.design.project import dump
from transformation.design.schema import column_key


ABSENT = object()


def register(register_id: str, columns: list[str], rows: Iterable[tuple],
             declared_empty: bool = True) -> tuple[str, list | None]:
    """One register: each row as a mapping from column key to value. A row shorter than the columns
    leaves the rest empty."""
    keys = [column_key(c) for c in columns]
    body = [{k: v for k, v in zip(keys, [*row, *[""] * (len(keys) - len(row))][: len(keys)])
             if v is not ABSENT} for row in rows]
    if not body:
        return register_id, [] if declared_empty else None
    return register_id, body


def document(title: str, *registers: tuple[str, list | None], header: dict | None = None,
             prose: str = "") -> str:
    """The document text: title, Machine block, then any prose. `header` is the `document` mapping."""
    block: dict = {}
    if header:
        block["document"] = dict(header)
    block["registers"] = dict(registers)
    return f"# {title}\n\n## Machine\n\n```yaml\n{dump(block)}```\n" + (f"\n{prose}\n" if prose else "")
