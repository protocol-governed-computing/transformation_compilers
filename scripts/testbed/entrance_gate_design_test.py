"""An entrance supplies what its gate requires — B25.

A design that stops an entrance sending a field its workflow does not read, and reuses the
workflow's gate, which still requires it, has every request through the entrance refused at
admission, with every phase admitting the design and construction at 100%. Shown here: the rule
fires on that shape; stays silent once the design redeclares the gate without the field; stays
silent while the entrance still supplies it; and reads the gate from the design's topology when the
design states one.

Run:  python scripts/testbed/entrance_gate_design_test.py
"""

from __future__ import annotations

import sys

import machine
from transformation.design.evaluate import ParsedDocument
from transformation.design.oracle import evaluate
from transformation.design.rule_sets import RULE_SETS

rule_set = RULE_SETS["p7"].rule_set
from transformation.design.read import parse_text

# The observation the rule under test reads, as its schema entry names it.
INTENT_OBSERVATION = "si.capability.surface#intents"
D = "probe"
RULE = [r for r in rule_set() if r.id == "ENTRANCE_UNDERSUPPLIES_GATE"]
PINNED = {INTENT_OBSERVATION: [{"intent": f"{D}::IN_REGISTERED_V0", "workflow": "WF_REGISTER_V0",
                                "inputs": {"record": {"required": True},
                                           "schema": {"required": True}}}]}


def _table(register: str, header: list[str], rows: list[tuple]) -> tuple[str, dict]:
    return machine.register(register, header, rows)


def design(sent=("record.name", "record.address"), gate_fields=(), topology=(),
           gate=f"{D}::IN_REGISTERED_V0") -> str:
    return machine.document(
        "Design Intent: probe / entrance",
        _table("transport_bindings", ["Artifact", "Direction", "Operation", "Handler Kind",
                                        "Handler Target", "Field", "Bound To", "Source Finding"],
                 [(f"{D}::TI_REGISTER_V0", "INGRESS", "probe.register", "WF_INVOCATION",
                   f"{D}::WF_REGISTER_V0", f, "${input.x}", "human decision") for f in sent]),
        _table("interface_fields", ["Artifact", "Direction", "Field", "Type", "Required", "Default",
                                      "Meaning"],
                 [(gate, "INPUT", f, "object", "YES", "", f) for f in gate_fields]),
        _table("execution_topology", ["Workflow", "Node", "Node Type", "Routing", "Source Finding"],
                 [(f"{D}::WF_REGISTER_V0", n, "IN", "ACK -> EXIT_SUCCESS", "human decision")
                  for n in topology])
    )


def fired(text: str) -> list[str]:
    header, sections, registers = parse_text(text)
    doc = ParsedDocument(header=header, sections=sections, registers=registers, raw=text, path="probe",
                         observed=PINNED)
    return [f.code for f in evaluate(doc, RULE).findings]


def test_an_entrance_that_stops_supplying_what_a_reused_gate_requires_is_refused():
    assert fired(design()) == ["ENTRANCE_UNDERSUPPLIES_GATE"], fired(design())


def test_a_gate_redeclared_without_the_field_is_satisfied():
    assert fired(design(gate_fields=("record",))) == []


def test_an_entrance_still_supplying_the_field_is_satisfied():
    assert fired(design(sent=("record.name", "schema.name"))) == []


def test_the_gate_the_design_names_is_the_one_held():
    # The topology names a different gate. Declared requiring only `record`, the entrance satisfies
    # it; declared requiring `token`, it does not — either way the composition's gate is not asked.
    other = f"{D}::IN_OTHER_V0"
    satisfied = design(topology=(other,), gate_fields=("record",), gate=other)
    short = design(topology=(other,), gate_fields=("token",), gate=other)
    assert fired(satisfied) == [], fired(satisfied)
    assert fired(short) == ["ENTRANCE_UNDERSUPPLIES_GATE"], fired(short)


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except Exception as exc:  # report every test, then fail the run
            failed += 1
            print(f"  FAIL  {name}: {exc!r}"[:1500])
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
