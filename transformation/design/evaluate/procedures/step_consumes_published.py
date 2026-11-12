"""The `STEP_CONSUMES_PUBLISHED` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _cell, _items, _rows, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("STEP_CONSUMES_PUBLISHED")
def _step_consumes_published(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A step must hand its operation fields the operation accepts.

    The mirror of `BINDING_SOURCE_PUBLISHED`, and the half that was missing. That rule asks whether a
    binding *reads* a field the operation yields; nothing asked whether a step *hands* the operation a
    field it takes.

    The gap was not hypothetical. CR-1's catalog search declared a `LIST` step consuming `filter`,
    and `LIST` declares no inputs at all — it returns every key in the store. The design was
    admissible over 92 rules, constructed, and validated by an acceptance criterion that read "staff
    can search the catalog and locate a registered material", against a search that ignored the
    search terms entirely.

    CS steps only. A CT step declares its binding explicitly in `Interface`, where the transform's
    formals are named on both sides and a different rule governs the mapping.
    """
    observation = rule.params["observation"]
    published = doc.observed.get(observation) or []
    if not published:
        return [(
            _at(_where(rule)),
            "no capability surface was observed — a step's inputs cannot be checked against "
            "operations nobody published",
        )]

    accepted: dict[str, dict[str, set[str]]] = {}
    for entry in published:
        if not isinstance(entry, dict):
            continue
        accepted[str(entry.get("capability"))] = {
            op: {str(f) for f in (spec.get("input") or [])}
            for op, spec in (entry.get("operations") or {}).items()
        }

    out = []
    for i, row in _rows(doc, rule):
        if _cell(row, "Kind") != "CS":
            continue
        capability, operation = _cell(row, "Capability"), _cell(row, "Operation")
        declared = accepted.get(capability, {}).get(operation)
        if declared is None:
            continue                      # the operation itself is another rule's business
        for field in _items(row, "Consumes"):
            if not field or field == "—":
                continue
            if field not in declared:
                out.append((
                    _at(_where(rule), i),
                    f"{operation} on {capability.split('::')[-1]} accepts "
                    f"{sorted(declared) or 'no input'}, not {field!r} — a step cannot hand an "
                    f"operation a field it does not take",
                ))
    return out
