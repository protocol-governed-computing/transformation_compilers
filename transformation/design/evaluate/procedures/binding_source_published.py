"""The `BINDING_SOURCE_PUBLISHED` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _bare_identity, _cell, _rows, _source, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("BINDING_SOURCE_PUBLISHED")
def _binding_source_published(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """An output binding must read a field its step's operation actually publishes.

    A step names its outputs in the contract's own vocabulary — `staff_record`, `book_details` — and
    the binding says where each comes from. The *name* is the design's to choose; the *source* is
    not. `capability_result.value` is a claim about what the operation yields, and only the
    composition can settle it.

    **This would not have caught the authorization defect**, and that is worth stating plainly.
    `authorized` was bound to `capability_result.exists`, and `EXISTS` does publish `exists` — the
    binding was structurally perfect and semantically wrong, because the question asked was whether
    a record existed when the question meant was whether a person was entitled. No structural rule
    reaches that. What this catches is a source that does not exist at all: a fabricated field, a
    typo, or a binding left pointing at an operation that has since changed its surface.
    """
    observation = rule.params["observation"]
    published = doc.observed.get(observation) or []
    if not published:
        return [(
            _at(_where(rule)),
            "no capability surface was observed — a binding source cannot be checked against "
            "operations nobody published",
        )]

    surface: dict[str, dict[str, set[str]]] = {}
    for entry in published:
        if not isinstance(entry, dict):
            continue
        surface[str(entry.get("capability"))] = {
            op: {str(f) for f in (spec.get("output") or [])}
            for op, spec in (entry.get("operations") or {}).items()
        }

    # Which capability and operation each CS step invokes, addressed the way a binding addresses it.
    steps: dict[tuple[Locator, str], tuple[Locator, str]] = {}
    composition = doc.register(rule.params["step_register"])
    if composition and composition.table:
        for row in composition.table.rows:
            if _cell(row, "Kind") != "CS":
                continue
            steps[(_bare_identity(_cell(row, "CC Code")), _cell(row, "Step Name"))] = (
                _cell(row, "Capability"), _cell(row, "Operation"))

    out = []
    prefix = "capability_result."
    for i, row in _rows(doc, rule):
        if _cell(row, "Direction") != "OUTPUT":
            continue
        bound = _source(row)
        if not bound.startswith(prefix):
            continue
        step = steps.get((_bare_identity(_cell(row, "Owner")), _cell(row, "Step")))
        if step is None:
            continue                      # a CT step, or a workflow node — a different surface
        capability, operation = step
        declared = surface.get(capability, {}).get(operation)
        if declared is None:
            continue                      # the operation itself is another rule's business
        field = bound[len(prefix):].split(".")[0]
        if field not in declared:
            out.append((
                _at(_where(rule), i),
                f"{operation} on {capability.split('::')[-1]} publishes {sorted(declared)}, "
                f"not {field!r} — a binding cannot read a field the operation never yields",
            ))
    return out
