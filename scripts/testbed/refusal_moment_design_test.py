"""Refusal moments — an act that refuses may announce the refusal, and nothing else.

A moment names something that happened, so it is announced from an ending that completes the act. A
refusal is itself something that happened: a business that records every refused request may need
to announce the refusal from the ending that refuses. Shown here: a refusing ending announcing a
moment the design declares a refusal is admissible; the same ending announcing an undeclared moment,
or a declared one alongside an undeclared one, is refused; and a completing ending is unaffected.

Run:  python scripts/testbed/refusal_moment_design_test.py
"""

from __future__ import annotations

import sys

import machine
from transformation.design.evaluate import ParsedDocument
from transformation.design.oracle import evaluate
from transformation.design.rule_sets import RULE_SETS

rule_set = RULE_SETS["p7"].rule_set
from transformation.design.read import parse_text

D = "probe"
WF, REFUSED, DONE = f"{D}::WF_SUBMIT_V0", f"{D}::EV_REFUSED_V0", f"{D}::EV_DONE_V0"
RULES = [r for r in rule_set() if r.id == "EMISSION_NOT_FROM_COMPLETING_ENDING"]


def _table(register: str, header: list[str], rows: list[tuple]) -> tuple[str, dict]:
    return machine.register(register, header, rows)


def design(properties) -> str:
    return machine.document(
        "Design Intent: probe / moments",
        _table("execution_topology", ["Workflow", "Node", "Node Type", "Routing", "Source Finding"], [
            (WF, "EXIT_SUCCESS", "EXIT_SUCCESS", "—", "human decision"),
            (WF, "EXIT_REFUSED", "EXIT", "—", "human decision")]),
        _table("artifact_properties", ["Artifact", "Property", "Value", "Source Finding"],
                 [(*p, "human decision") for p in properties])
    )


def fired(properties) -> list[str]:
    header, sections, registers = parse_text(design(properties))
    doc = ParsedDocument(header=header, sections=sections, registers=registers, raw="", path="probe")
    return [f.code for f in evaluate(doc, RULES).findings]


DECLARED = (REFUSED, "moment", "refusal")


def test_a_refusing_ending_announces_a_declared_refusal():
    assert fired([DECLARED, (WF, "emit.EXIT_REFUSED", REFUSED)]) == []


def test_a_refusing_ending_announcing_an_undeclared_moment_is_refused():
    assert fired([(WF, "emit.EXIT_REFUSED", REFUSED)]) == ["EMISSION_NOT_FROM_COMPLETING_ENDING"]


def test_a_refusal_does_not_carry_another_moment_with_it():
    assert fired([DECLARED, (WF, "emit.EXIT_REFUSED", f"{REFUSED}, {DONE}")]) == \
        ["EMISSION_NOT_FROM_COMPLETING_ENDING"]


def test_a_completing_ending_is_unaffected():
    assert fired([(WF, "emit.EXIT_SUCCESS", DONE)]) == []


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
