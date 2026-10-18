"""The `STORE_GROUNDED_IN_CAPABILITY` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _bare_identity, _cell, _items, _rows, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("STORE_GROUNDED_IN_CAPABILITY")
def _store_grounded_in_capability(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A step names a store when its capability keeps one, and does not when it does not.

    `Store` is the third em-dash column in the step register and the only one no check read at all:
    88 of 155 steps in the corpus declare `—` there, and the column reached the register-columns
    check and stopped. So both halves were unstated — a storage step that named nothing, and a
    clock step that named a store — and neither could be told from a step that was right.

    The dash is the same kind of declaration `Interpreted By`'s is: it says this step addresses no
    store. What decides whether that is true is the design language's own list of the capabilities
    that keep named stores, the `storage_type` group a store's declaration is already drawn from. A
    capability's `category` cannot decide it: a capability that persists beneath a root its binding
    declares is `storage` and addresses no named store. A capability transform keeps
    none by being one.

    An unknown capability is `COMPOSITION_STEP_UNDECLARED`'s finding and an unknown operation is
    `STEP_NAMES_UNPUBLISHED_OPERATION`'s; neither is restated here.
    """
    observed = doc.observed.get(rule.params["observation"]) or []
    if not observed:
        return [(
            _at(_where(rule)),
            "no capability surface was observed — whether a step addresses a store cannot be "
            "checked against capabilities nobody published",
        )]

    store_keeping = {_bare_identity(str(c)) for c in rule.params["store_keeping"]}
    storage, known = set(), set()
    for entry in observed:
        if not isinstance(entry, dict):
            continue
        if entry.get("capability") is not None:
            identity = _bare_identity(str(entry["capability"]))
            known.add(identity)
            if identity in store_keeping:
                storage.add(identity)
        elif entry.get("transform") is not None:
            known.add(_bare_identity(str(entry["transform"])))

    out = []
    for i, row in _rows(doc, rule):
        capability = _bare_identity(_cell(row, rule.params["capability_column"]))
        if capability not in known:
            continue
        keeps_records = capability in storage
        if bool(_items(row, rule.params["column"])) == keeps_records:
            continue
        detail = rule.params["detail_missing"] if keeps_records else rule.params["detail_spurious"]
        out.append((_at(_where(rule), i), detail.format(capability=capability)))
    return out
