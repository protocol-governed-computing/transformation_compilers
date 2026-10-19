"""The `ENTRANCE_SUPPLIES_GATE` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _bare_identity, _cell, _content_rows, _rows
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("ENTRANCE_SUPPLIES_GATE")
def _entrance_supplies_gate(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """An entrance must supply everything the gate of the workflow it invokes requires.

    `NODE_INPUT_BOUND` holds a workflow to its contracts; nothing held an entrance to the gate it
    reaches. A design that stops an entrance sending a field its workflow does not read, and leaves
    the gate that still requires the field as it is, has every request through the entrance refused
    at admission — admissible over every rule, complete at 100%, found by the first request.

    The gate is the workflow's `IN` node where the design states the topology, and otherwise the
    intent the composition declares for that workflow. What the gate requires is what the design
    declares where it declares the gate's interface — a gate the design redeclares is authored again
    from it — and what the composition's gate requires otherwise.
    """
    topology = rule.params["topology_register"]
    fields = rule.params["fields_register"]

    supplied: dict[str, tuple[str, set[str]]] = {}
    for _, row in _rows(doc, rule):
        if (_cell(row, "Direction").upper() != "INGRESS"
                or _cell(row, "Handler Kind").upper() != "WF_INVOCATION"):
            continue
        entrance = _bare_identity(_cell(row, "Artifact"))
        workflow = _bare_identity(_cell(row, "Handler Target"))
        field = _cell(row, "Field").split(".", 1)[0]
        supplied.setdefault(entrance, (workflow, set()))[1].add(field)

    gates: dict[str, str] = {}
    for _, row in _content_rows(doc.register(topology)):
        if _cell(row, "Node Type").upper() == "IN":
            gates[_bare_identity(_cell(row, "Workflow"))] = _bare_identity(_cell(row, "Node"))

    declared: dict[str, set[str]] = {}
    for _, row in _content_rows(doc.register(fields)):
        if _cell(row, "Direction").upper() != "INPUT":
            continue
        artifact = _bare_identity(_cell(row, "Artifact"))
        required = declared.setdefault(artifact, set())
        if _cell(row, "Required").upper() == "YES":
            required.add(_cell(row, "Field"))

    observed: dict[str, set[str]] = {}
    for entry in doc.observed.get(rule.params["observation"]) or []:
        if not isinstance(entry, dict):
            continue
        intent = _bare_identity(str(entry.get("intent")))
        observed[intent] = {name for name, spec in (entry.get("inputs") or {}).items()
                            if isinstance(spec, dict) and spec.get("required")}
        gates.setdefault(_bare_identity(str(entry.get("workflow"))), intent)

    out = []
    for entrance, (workflow, fields_sent) in sorted(supplied.items()):
        gate = gates.get(workflow)
        if gate is None:
            continue
        required = declared[gate] if gate in declared else observed.get(gate, set())
        for field in sorted(required - fields_sent):
            out.append((
                _at(rule.register, entrance),
                f"{entrance} invokes {workflow}, whose gate {gate} requires {field!r} — the entrance "
                f"does not supply it, so every request through it is refused at admission",
            ))
    return out
