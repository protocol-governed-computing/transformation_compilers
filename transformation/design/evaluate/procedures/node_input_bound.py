"""The `NODE_INPUT_BOUND` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _composition_steps,
    _content_rows,
    _rows,
    _runs,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("NODE_INPUT_BOUND")
def _node_input_bound(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A workflow node must be handed every input its contract requires.

    A contract declares what it accepts; a workflow node declares what it is handed. Nothing checked
    that the second covered the first, so extending a contract to need a new input left its callers
    silently short — the contract was well formed, the workflow was well formed, and the value
    arrived as null at execution. Two contracts were extended that way in one change, and both
    designs were admissible over the full rule set and complete at 100%.

    Only required inputs are checked. An optional one absent is a declaration that the node does not
    supply it, which is what optional means.
    """
    topology = rule.params["topology_register"]
    fields = rule.params["fields_register"]

    declared: dict[str, set[str]] = {}
    for _, row in _content_rows(doc.register(fields)):
        if (_cell(row, "Direction").upper() != "INPUT"
                or _cell(row, "Required").upper() != "YES"):
            continue
        declared.setdefault(_bare_identity(_cell(row, "Artifact")), set()).add(_cell(row, "Field"))

    # A contract this design authors declares its interface above. One it *reuses* declares nothing —
    # the contract already exists, so there is nothing for the design to restate — and that silence
    # was read as "requires nothing". Every instance of this defect has been the same shape: a
    # workflow reusing another subdomain's contract and handing it nothing, admissible over the full
    # rule set, complete at 100%, and discovered only when the act ran and the contract received
    # nulls. Three of them in one change.
    #
    # Unioned rather than overridden. A design extending a contract states the input it adds while
    # the composition still requires the ones it had, and both must be bound; requiring too much is
    # a finding an author can answer, requiring too little is one nobody sees.
    #
    # Except where the design redeclares the contract whole. A contract whose steps the design
    # composes is authored again from this design, interface and all, so what it requires is what
    # the design declares — and an input the design withdraws is no longer required. Unioned, a
    # contract that stopped taking a rule from its caller was still read as requiring it, and the
    # only way to satisfy the rule was to hand the contract a value none of its steps read.
    redeclared = {owner for owner, _ in _composition_steps(doc, rule.params["composition_register"])}
    observation = rule.params.get("observation")
    for entry in (doc.observed.get(observation) or []) if observation else []:
        if not isinstance(entry, dict):
            continue
        if _bare_identity(str(entry.get("contract"))) in redeclared:
            continue
        required = {name for name, spec in (entry.get("inputs") or {}).items()
                    if isinstance(spec, dict) and spec.get("required")}
        if required:
            declared.setdefault(_bare_identity(str(entry.get("contract"))), set()).update(required)

    bound: dict[tuple[Locator, str], set[str]] = {}
    for _, row in _rows(doc, rule):
        if _cell(row, "Direction").upper() != "INPUT":
            continue
        key = (_bare_identity(_cell(row, "Owner")), _bare_identity(_cell(row, "Step")))
        bound.setdefault(key, set()).add(_cell(row, "Field"))

    out = []
    for i, row in _content_rows(doc.register(topology)):
        if _cell(row, "Node Type").upper() != "CC":
            continue
        workflow = _bare_identity(_cell(row, "Workflow"))
        node, contract = _bare_identity(_cell(row, "Node")), _runs(row)
        missing = sorted(declared.get(contract, set()) - bound.get((workflow, node), set()))
        named = node if node == contract else f"{node} ({contract})"
        for field in missing:
            out.append((
                _at(topology, i),
                f"{workflow} hands {named} no {field!r}, which that contract requires",
            ))
    return out
