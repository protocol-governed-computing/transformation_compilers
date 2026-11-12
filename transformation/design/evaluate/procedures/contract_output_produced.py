"""The `CONTRACT_OUTPUT_PRODUCED` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _content_rows,
    _rows,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("CONTRACT_OUTPUT_PRODUCED")
def _contract_output_produced(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A contract's declared output must name a value one of its steps surfaces.

    Surfaced, not consumed: a step's OUTPUT binding carries the *domain* name a value takes when it
    leaves the step, while the composition's `Produces` column carries the capability's own name for
    it. `read_work_record` produces `value` and surfaces it as `work_record`, and a contract
    declaring `work_record` is exactly right. Reading the wrong one of those two reports a defect on
    every correct contract that renames anything.

    Declaring an output no step surfaces gives every caller a name that resolves to nothing — the
    contract is well formed, the caller is well formed, and the value arrives absent.
    """
    surfaced: dict[str, set[str]] = {}
    owners: set[str] = set()
    bindings = doc.register(rule.params["bindings_register"])
    if bindings is not None and bindings.table is not None:
        for _, row in _content_rows(bindings):
            owner = _bare_identity(_cell(row, "Owner"))
            owners.add(owner)
            if _cell(row, "Direction").upper() == "OUTPUT":
                surfaced.setdefault(owner, set()).add(_cell(row, "Field"))

    out: list[tuple[Locator, str]] = []
    for i, row in _rows(doc, rule):
        artifact = _bare_identity(_cell(row, "Artifact"))
        if artifact not in owners or _cell(row, "Direction").upper() != "OUTPUT":
            continue
        field = _cell(row, "Field")
        if field and field not in surfaced.get(artifact, set()):
            out.append((_at(_where(rule), i),
                        f"{artifact} declares output {field!r}, which no step of it surfaces — "
                        f"its steps surface {', '.join(sorted(surfaced.get(artifact, set()))) or 'nothing'}"))
    return out
