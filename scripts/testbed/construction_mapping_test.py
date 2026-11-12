"""The construction mapping standard against construction itself.

`doc/CONSTRUCTION_MAPPING.md` states every field construction writes, by kind, with its provenance
class. This renders every design of record the acceptance harness reads, collects the same from what
construction emits (`build/mapping.py`), and requires the two to be one set. A field the standard
does not state, or one it states that construction no longer writes, fails the run.

Run:  python scripts/testbed/construction_mapping_test.py
Exit: 0 when the standard and construction agree, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import construction_acceptance as ca
from transformation.build.mapping import inventory

REPO = Path(__file__).resolve().parents[2]
STANDARD = REPO / "doc" / "CONSTRUCTION_MAPPING.md"
CELL = re.compile(r"`([^`]*)`")


def stated() -> set[tuple[str, str, str, str]]:
    """`(kind, field, class, governed by)` as the standard's tables state them."""
    text = STANDARD.read_text(encoding="utf-8")
    kinds = re.findall(r"^`artifact_kind: ([A-Z_]+)`$", text, re.M)
    out: set[tuple[str, str, str, str]] = set()
    kind = None
    text = text[text.index("\n## 2."):]
    for line in text.splitlines():
        found = re.match(r"^`artifact_kind: ([A-Z_]+)`$", line)
        if found:
            kind = found.group(1)
            continue
        if line.startswith("## 3."):
            break
        if not line.startswith("| `"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        field = CELL.match(cells[0]).group(1)
        if kind is None:
            # The table every artifact shares: `| field | kinds | class | source |`.
            named = kinds if cells[1] == "every" else [k.strip() for k in cells[1].split(",")]
            out |= {(k, field, cells[2], "") for k in named}
        else:
            governed = CELL.match(cells[2]).group(1) if cells[2] else ""
            out.add((kind, field, cells[1], governed))
    return out


def emitted() -> set[tuple[str, str, str, str]]:
    """What construction writes over every design of record."""
    out: set[tuple[str, str, str, str]] = set()
    for root, _ in ca.DOMAINS:
        design = root / "design"
        out |= inventory(ca.registers(next(design.glob("p7_*.md"))),
                         ca.registers(next(design.glob("p8_*.md"))))
    return out


def main() -> int:
    standard, construction = stated(), emitted()
    unstated = sorted(construction - standard)
    unwritten = sorted(standard - construction)
    for row in unstated:
        print(f"  UNSTATED   {' | '.join(row)}")
    for row in unwritten:
        print(f"  UNWRITTEN  {' | '.join(row)}")
    if unstated or unwritten:
        print(f"\nCONSTRUCTION MAPPING FAILED — {len(unstated)} field(s) construction writes and the "
              f"standard does not state, {len(unwritten)} it states and construction does not write")
        return 1
    print(f"CONSTRUCTION MAPPING PASSED — {len(standard)} fields over "
          f"{len({k for k, *_ in standard})} kinds, stated as construction writes them")
    return 0


if __name__ == "__main__":
    sys.exit(main())
