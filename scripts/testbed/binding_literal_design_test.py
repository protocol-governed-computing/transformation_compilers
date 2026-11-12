"""Binding literals — one meaning for a literal, and a statement for a value a generator writes.

The rooting rule read a quoted value, a qualified identity and a number as literals; the form rules
refused all three. A dotted operation name had no spelling both admitted, so no design could
redeclare a contract that observes the composition. And a value a generator writes — the rule set a
phase workflow hands its judge — had no statement at all. Shown here: every literal form passes
every rule that judges a binding, in a step binding and in a molecule binding; `generated` passes
where its owner is listed as generated and is refused where it is not; and what was refused before
for being no form at all is refused still. A literal is stated as `{literal: v}` and the generator's
value as `{generated: true}`, so neither is ever read out of a path.

Run:  python scripts/testbed/binding_literal_design_test.py
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
WF, CC, CT = f"{D}::WF_OBSERVE_V0", f"{D}::CC_OBSERVE_V0", f"{D}::CT_PURE_PROBE_V0"
HELD = {"BINDING_SOURCE_UNROOTED", "BINDING_SOURCE_MALFORMED", "MOLECULE_BINDING_SOURCE_MALFORMED",
        "GENERATED_SOURCE_WITHOUT_GENERATOR"}
RULES = [r for r in rule_set() if r.id in HELD]

LITERALS = [{"literal": v} for v in ("si.artifact.list", "si.store.list", 3, -1.5,
                                      "transformation::CC_JUDGE_V0", "accepted", {}, [], "")]
GENERATED = {"generated": True}


def _table(register: str, header: list[str], rows: list[tuple]) -> tuple[str, dict]:
    return machine.register(register, header, rows)


def design(step_sources=(), molecule_sources=(), generated_owner=None) -> str:
    provenance = [(generated_owner, "probe.emit:emit", "probe/rules.py", "human decision")] \
        if generated_owner else []
    return machine.document(
        "Design Intent: probe / literals",
        _table("step_bindings", ["Owner", "Step", "Direction", "Field", "Bound To", "Source Finding"],
                 [(o, "observe", "INPUT", f"field_{i}", s, "human decision")
                  for i, (o, s) in enumerate(step_sources)]),
        _table("molecule_step_bindings", ["CT Code", "Step", "Role", "Field", "Bound To", "Source Finding"],
                 [(CT, "probe", "INPUT", f"field_{i}", s, "human decision")
                  for i, s in enumerate(molecule_sources)]),
        _table("generation_provenance", ["Artifact", "Generator", "Generator Sources", "Source Finding"],
                 provenance)
    )


def fired(text: str) -> list[str]:
    header, sections, registers = parse_text(text)
    doc = ParsedDocument(header=header, sections=sections, registers=registers, raw=text, path="probe")
    return sorted(f.code for f in evaluate(doc, RULES).findings)


def test_every_literal_form_passes_in_a_step_binding():
    assert fired(design(step_sources=[(CC, s) for s in LITERALS])) == []


def test_every_literal_form_passes_in_a_molecule_binding():
    assert fired(design(molecule_sources=LITERALS)) == []


def test_references_pass_as_before():
    sources = ["payload.register_text", "inputs.document_text", "results.parse.registers"]
    assert fired(design(step_sources=[(CC, s) for s in sources])) == []


def test_a_generated_value_passes_where_its_owner_is_generated():
    assert fired(design(step_sources=[(WF, GENERATED)], generated_owner=WF)) == []


def test_a_generated_value_is_refused_where_its_owner_is_not_generated():
    assert fired(design(step_sources=[(WF, GENERATED)])) == ["GENERATED_SOURCE_WITHOUT_GENERATOR"]
    assert fired(design(step_sources=[(WF, GENERATED)], generated_owner=CC)) == \
        ["GENERATED_SOURCE_WITHOUT_GENERATOR"]


def test_the_word_itself_as_a_literal_is_not_generated():
    assert fired(design(step_sources=[(WF, {"literal": "generated"})])) == []


def test_what_is_no_form_at_all_is_refused_still():
    assert fired(design(step_sources=[(CC, "the rule set the generator seals")])) == \
        ["BINDING_SOURCE_MALFORMED"]
    assert fired(design(step_sources=[(CC, "si.artifact.list")])) == \
        ["BINDING_SOURCE_MALFORMED", "BINDING_SOURCE_UNROOTED"]
    assert fired(design(molecule_sources=["the rule set the generator seals"])) == \
        ["MOLECULE_BINDING_SOURCE_MALFORMED"]


def test_construction_renders_a_literal_as_the_value_it_states():
    """A literal renders as the value it states, and a path as the runtime's expression for it."""
    from transformation.build.render import _binding
    for literal in LITERALS:
        assert _binding(literal) == literal["literal"], literal
    assert _binding(GENERATED) == "generated"
    assert _binding("payload.register_text") == "$.payload.register_text"


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
