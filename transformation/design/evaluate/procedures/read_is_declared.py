"""The `READ_IS_DECLARED` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _act_stores,
    _at,
    _bare_identity,
    _binding_stores,
    _cell,
    _content_rows,
    _declared_reach,
    _store_keys,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


def _own_binding(doc: ParsedDocument, rule) -> dict[str, str]:
    """`act -> the binding it owns`, from the declarations that bind one to each workflow."""
    out: dict[str, str] = {}
    block = doc.register(rule.params["rb_register"])
    for _, row in _content_rows(block) if block is not None else []:
        out[_bare_identity(_cell(row, "Binds WF"))] = _bare_identity(_cell(row, "RB Code"))
    return out


@check("READ_IS_DECLARED")
def _read_is_declared(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """An act reads nothing it did not declare a reach to.

    The other half. A step addressing records that neither the act's own binding nor any reach it
    declared covers is reaching, and the design does not say so — which is exactly the state the
    blocked change was in, and it was invisible until the act ran.

    An act whose own binding does not resolve is left alone: what it owns is undecided, so what it
    reaches cannot be told apart from it.
    """
    observed = doc.observed.get(rule.params["observation"]) or []
    if not observed:
        return [(_at(_where(rule)),
                 "no store surface was observed — whether an act reads what it declared cannot be "
                 "checked against stores nobody published")]

    covers = _binding_stores(observed)
    reads = _act_stores(doc, rule, _store_keys(observed))
    reach = _declared_reach(doc, rule)

    out = []
    for act, owned in sorted(_own_binding(doc, rule).items()):
        if owned not in covers:
            continue
        permitted = set(covers[owned])
        for binding in reach.get(act, set()):
            permitted |= covers.get(binding, set())
        for store in sorted(reads.get(act, set()) - permitted):
            out.append((
                _at(_where(rule), act),
                rule.params["detail"].format(store=store, binding=owned),
            ))
    return out
