"""The `UNRESOLVED_MARKER_ABSENT` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


# A cell that declares the question unanswered rather than answering it. Matched at the head of a
# cell, so `UNRESOLVED — whether an edition is a Book` fires and a sentence that merely mentions an
# unresolved question does not. `PENDING` is deliberately absent: in a projection table it means
# scheduled, not unknown.
GOVERNED_HOLE_MARKERS = (
    "UNRESOLVED",
    "UNDECIDED",
    "UNKNOWN",
    "TBD",
    "TBC",
    "TO BE DETERMINED",
    "TO BE DECIDED",
    "TO BE CONFIRMED",
    "NOT YET DECIDED",
    "OPEN QUESTION",
    "???",
)


@check("UNRESOLVED_MARKER_ABSENT")
def _unresolved_marker_absent(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """No register may hedge a cell instead of stating it.

    Document-wide rather than per-register: a hole can open in any cell of any register, and a rule
    that had to name the columns in advance would only ever catch the holes someone had already
    seen. The registers where an open question is the content — a clarification register, a gap
    register — are declared exempt by the phase that owns them.

    An unanswered question is not a value. Left in a register it is *determined* as far as every
    later phase can tell, which is how a design whose central business question was never settled
    reached execution reporting admissible at every gate.
    """
    out = []
    exempt = {r.lower() for r in rule.params.get("exempt", ())}
    markers = tuple(m.upper() for m in rule.params.get("markers", GOVERNED_HOLE_MARKERS))
    for entry in doc.registers:
        register_id = str(entry.get("id") or "")
        rows = entry.get("value")
        if register_id.lower() in exempt or not isinstance(rows, list):
            continue
        for i, row in enumerate(rows, start=1):
            for column, raw in (row.items() if isinstance(row, dict) else ()):
                if not isinstance(raw, str):
                    continue
                value = raw.strip().strip("*_`").upper()
                marker = next((m for m in markers if value.startswith(m)), None)
                if marker:
                    out.append(
                        (
                            _at(register_id, i),
                            rule.params["detail"].format(marker=marker, column=column),
                        )
                    )
    return out
