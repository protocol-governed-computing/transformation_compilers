"""The `STEP_INPUTS_BOUND` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _composition_steps,
    _content_rows,
    _items,
    _rows,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("STEP_INPUTS_BOUND")
def _step_inputs_bound(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Every input a step consumes must be bound to something.

    A composition says what a step hands its capability; the bindings say where each value comes
    from. Nothing checked that the second covered the first, so a step could declare it consumes
    `key, target_cs, target_ref`, bind only `key`, and be well formed twice over. The capability
    then received two nulls and wrote a row keyed on nothing — `{"key": null}` in a registry whose
    whole purpose is that the key is the identity.

    This is `NODE_INPUT_BOUND` one level down: that rule holds a workflow to the contract it calls,
    this one holds a contract to the capability it calls.
    """
    composition = rule.params["composition_register"]
    bound: dict[tuple[Locator, str], set[str]] = {}
    for _, row in _rows(doc, rule):
        if _cell(row, "Direction").upper() != "INPUT":
            continue
        key = (_bare_identity(_cell(row, "Owner")), _cell(row, "Step"))
        bound.setdefault(key, set()).add(_cell(row, "Field"))

    # A step input the contract itself declares under the same name needs no binding row: the
    # runtime passes it through by name, and the catalog relies on it throughout. Only a name the
    # contract neither declares nor binds arrives as a null.
    passed_through: dict[str, set[str]] = {}
    fields = doc.register(rule.params["fields_register"])
    if fields is not None and fields.table is not None:
        for _, row in _content_rows(fields):
            if _cell(row, "Direction").upper() == "INPUT":
                passed_through.setdefault(_bare_identity(_cell(row, "Artifact")), set()).add(
                    _cell(row, "Field"))

    # A value an earlier step of the same contract produced under that name is also satisfied: the
    # runtime chains by name within a contract, which is how the catalog feeds `records` from a
    # read into a select without a binding row for it.
    produced: dict[str, set[str]] = {}
    for (owner, _), row in _composition_steps(doc, composition).items():
        produced.setdefault(owner, set()).update(_items(row, "Produces"))

    # Only side-effect steps are checked. `Consumes` on a CS step names the operation's own inputs
    # — `STEP_CONSUMES_UNDECLARED_INPUT` holds it to the published surface — so an unbound one
    # provably arrives null. On a transform step the column is unenforced, and the tested designs
    # use domain-side names there while the bindings use the transform's, so comparing them would
    # report a defect where a mapping exists. Transform steps become checkable once a transform's
    # contract can be observed; until then this asserts only what it can know.
    out: list[tuple[Locator, str]] = []
    for (owner, step), row in sorted(_composition_steps(doc, composition).items()):
        if _cell(row, "Kind").upper() != "CS":
            continue
        satisfied = (bound.get((owner, step), set()) | passed_through.get(owner, set())
                     | produced.get(owner, set()))
        for field in sorted(set(_items(row, "Consumes")) - satisfied):
            out.append((_at(composition, f"{owner}/{step}"),
                        f"consumes {field!r} and binds it to nothing — the capability receives "
                        f"no value for it"))
    return out
