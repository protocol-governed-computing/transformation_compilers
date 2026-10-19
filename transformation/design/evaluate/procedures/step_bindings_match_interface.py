"""The `STEP_BINDINGS_MATCH_INTERFACE` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _composition_steps,
    _interface_map,
    _rows,
    _value,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("STEP_BINDINGS_MATCH_INTERFACE")
def _step_bindings_match_interface(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A binding may only name a field the step's Interface declares.

    The Interface states what the step hands its capability and reads back; the bindings say where
    each of those comes from. `STEP_INTERFACE_CONFORMS` holds the Interface to the capability's real
    contract, so a binding naming a field the Interface does not carry is bound to a capability
    input that does not exist — checked at one remove, and until now not at all. A first attempt to
    give an occurrence its time bound `occurred_at` on a transform that accepts only `fields`, and
    passed every rule.

    Only steps that declare an Interface are checked. A side-effect step leaves the column empty
    because its `Consumes`/`Produces` already name the operation's own fields, and
    `STEP_CONSUMES_UNDECLARED_INPUT` holds those to the published surface.
    """
    declared: dict[tuple[Locator, str], tuple[set[str], set[str]]] = {}
    for (owner, step), row in _composition_steps(doc, rule.params["composition_register"]).items():
        interface = _value(row, "Interface")
        if not isinstance(interface, dict) or not interface:
            continue
        # An input binds the capability's own name for the value — the left of `in: record=record`.
        # An output binds the *design's* name for it, the right of `out: record=book_record`, because
        # that is the name the value carries once it leaves the step. The two directions read
        # opposite halves of the same column, and a check reading one half for both reports a defect
        # on every step that renames its result.
        declared[(owner, step)] = (set(_interface_map(interface, "in")),
                                   set(_interface_map(interface, "out").values()))

    out: list[tuple[Locator, str]] = []
    for index, row in _rows(doc, rule):
        key = (_bare_identity(_cell(row, "Owner")), _cell(row, "Step"))
        if key not in declared:
            continue
        direction = _cell(row, "Direction").upper()
        allowed = declared[key][0] if direction == "INPUT" else declared[key][1]
        field = _cell(row, "Field")
        if field and field not in allowed:
            out.append((_at(_where(rule), index),
                        f"binds {field!r} on {key[1]}, which its interface does not carry — it "
                        f"declares {', '.join(sorted(allowed)) or 'nothing'} in that direction"))
    return out
