"""The `STEP_INTERFACE_CONFORMS` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _cell, _interface_map, _rows, _value, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("STEP_INTERFACE_CONFORMS")
def _step_interface_conforms(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A transform step must hand its transform the inputs that transform declares.

    The side-effect half of this has been checked since `STEP_CONSUMES_UNDECLARED_INPUT`, because
    the capability surface published side effects. It published no transforms, so a design could
    name `rules` where the transform declares `schema`, or read `validation_status` where it
    answers `violations`, and pass every rule at full Construction Completeness. Four contracts in
    one change request did exactly that, and every one of them failed at execution.

    Read from the **Interface** column rather than `Consumes`, because that column states the
    mapping instead of leaving it to be inferred: `in: source=matching_books` says the transform's
    `source` is fed by the design's `matching_books`, and only the left half is the transform's to
    declare. `Consumes` carries the capability's names on a side-effect step and the design's on a
    transform step, so holding a transform to it would report a defect on every design that renames
    anything.
    """
    observed = {t["transform"]: t for t in
                (doc.observed.get(rule.params["observation"]) or [])
                if isinstance(t, dict) and t.get("transform")}
    if not observed:
        # Reported, not skipped. Returning nothing here made this rule pass in silence through the
        # compiled path for as long as it existed, because the contract that judges a document
        # passed the capability surface and not the transform surface. A rule that cannot see its
        # subject has not checked it, and saying so is the difference between the two.
        return [(
            _at(_where(rule)),
            "no transform surface was observed — a step's interface cannot be checked against "
            "transforms nobody published",
        )]

    out: list[tuple[Locator, str]] = []
    for index, row in _rows(doc, rule):
        if _cell(row, "Kind").upper() != "CT":
            continue
        contract = observed.get(_cell(row, "Capability"))
        if contract is None:
            continue
        where = _at(_where(rule), index)
        interface = _value(row, "Interface")
        supplied = _interface_map(interface, "in")
        produced = _interface_map(interface, "out")

        for name in sorted(set(supplied) - set(contract["inputs"])):
            out.append((where, f"hands {_cell(row, 'Capability').split('::')[-1]} an input "
                               f"{name!r} it does not declare — it accepts "
                               f"{', '.join(sorted(contract['inputs'])) or 'nothing'}"))
        for name in sorted(set(produced) - set(contract["outputs"])):
            out.append((where, f"reads {name!r} from "
                               f"{_cell(row, 'Capability').split('::')[-1]}, which answers "
                               f"{', '.join(contract['outputs']) or 'nothing'}"))
        required = {n for n, spec in contract["inputs"].items() if spec.get("required")}
        for name in sorted(required - set(supplied)):
            out.append((where, f"supplies no {name!r}, which "
                               f"{_cell(row, 'Capability').split('::')[-1]} requires"))
    return out
