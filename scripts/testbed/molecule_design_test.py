"""Molecule design, in the design language.

A molecule is declared in P7 as its steps (`molecule_steps`) and what each step is handed
(`molecule_step_bindings`). Shown here: a loop over a molecule of two atoms renders to exactly the
source form the compiler lowers — a stream of steps, their bindings and one emission, and no
implementation — with every fact of it determined by the design; and each rule that holds a molecule
to being stated fires on a design built to trip it and stays silent on the one that keeps it.

Run:  python scripts/testbed/molecule_design_test.py
"""

from __future__ import annotations

import sys

import machine as probe
from transformation.build.provenance import of as provenance_of
from transformation.build.render import render_all, requirements
from transformation.design.evaluate import ParsedDocument
from transformation.design.oracle import evaluate
from transformation.design.rule_sets import RULE_SETS

rule_set = RULE_SETS["p7"].rule_set
from transformation.design.read import parse_text

D = "probe"
OFFER, CHOOSE = f"{D}::CT_IMPURE_OFFER_WORDS_V0", f"{D}::CT_PURE_CHOOSE_WORD_V0"
PASS, WRITE = f"{D}::CT_PASS_WRITE_ONE_WORD_V0", f"{D}::CT_WRITE_RESPONSE_V0"

NEW = [
    ("Offer words", OFFER), ("Choose a word", CHOOSE),
    ("Write one word", PASS), ("Write a response", WRITE),
]
IMPL = [  # code, callable, kind, purity
    (OFFER, "execute", "atom", "ct_impure"),
    (CHOOSE, "execute", "atom", "ct_pure"),
    (PASS, "", "molecule", "ct_impure"),
    (WRITE, "", "molecule", "ct_impure"),
]
STEPS = [  # molecule, step, kind, target, over, iterator, emits
    (PASS, "offered", "atom", OFFER, None, None, None),
    (PASS, "chosen", "atom", CHOOSE, None, None, "result"),
    (WRITE, "written", "loop", PASS, "inputs.positions", "position", "result"),
]
BINDINGS = [  # molecule, step, role, field, bound to
    (PASS, "offered", "INPUT", "position", "inputs.position"),
    (PASS, "chosen", "INPUT", "candidates", "results.offered.candidates"),
    (PASS, "chosen", "INPUT", "forbidden", "inputs.forbidden"),
    (PASS, "chosen", "INPUT", "text", "inputs.text"),
    (PASS, "chosen", "INPUT", "done", "inputs.done"),
    (WRITE, "written", "CARRY", "text", {"literal": ""}),
    (WRITE, "written", "CARRY", "done", {"literal": False}),
    (WRITE, "written", "INPUT", "position", "iterator"),
    (WRITE, "written", "INPUT", "text", "accumulator.text"),
    (WRITE, "written", "INPUT", "done", "accumulator.done"),
    (WRITE, "written", "INPUT", "forbidden", "inputs.forbidden"),
    (WRITE, "written", "UPDATE", "text", "results.text"),
    (WRITE, "written", "UPDATE", "done", "results.done"),
]


def _table(register: str, header: list[str], rows: list[tuple]) -> tuple[str, dict]:
    return probe.register(register, header, rows)


def design(impl=IMPL, steps=STEPS, bindings=BINDINGS) -> str:
    return probe.document(
        "Design Intent: probe / words",
        _table("new_artifacts", ["Capability", "Family", "Code", "Summary", "Owner Subdomain", "Status",
                                   "Source Finding"],
                 [(c, "CT", code, c, "words", "NEW", "human decision") for c, code in NEW]),
        _table("implementation_bindings", ["CT Code", "Callable", "Operation",
                                             "Kind", "Purity",
                                             "Refusal", "Source Finding"],
                 [(c, k, "op", kind, p, "never", "human decision") for c, k, kind, p in impl]),
        _table("molecule_steps", ["CT Code", "Step", "Kind", "Target", "Over",
                                    "Iterator", "Emits", "Source Finding"],
                 [(*s, "human decision") for s in steps]),
        _table("molecule_step_bindings", ["CT Code", "Step", "Role", "Field",
                                            "Bound To", "Source Finding"],
                 [(*b, "human decision") for b in bindings])
    )


def parsed(text: str) -> ParsedDocument:
    header, sections, registers = parse_text(text)
    return ParsedDocument(header=header, sections=sections, registers=registers, raw=text, path="probe")


def registers(text: str) -> dict[str, list[dict]]:
    doc = parsed(text)
    return {e["id"]: doc.register(e["id"]).table.rows for e in doc.registers
            if doc.register(e["id"]) and doc.register(e["id"]).table}


MANDATE = {"build_order": [{"code": code} for _, code in NEW],
           "field_declarations": [{"code": code, "subdomain_field": "words"} for _, code in NEW]}

# The rules a molecule is held to: the molecule rules, the two kind rules,
# and the vocabulary the template declares for a binding's role.
# The molecule rules: every finding a molecule's steps and bindings can raise.
MOLECULE_RULES = {"LOOP_COLLECTION_UNROOTED", "LOOP_FIELDS_OUTSIDE_LOOP", "LOOP_UPDATE_NOT_FROM_RESULT",
                  "LOOP_WITHOUT_COLLECTION", "LOOP_WITHOUT_ITERATOR", "MOLECULE_BINDING_SOURCE_MALFORMED",
                  "MOLECULE_BINDING_STEP_UNDECLARED", "MOLECULE_BINDING_WITHOUT_SOURCE",
                  "MOLECULE_EMITS_TWICE", "MOLECULE_STEP_KIND_UNKNOWN",
                  "MOLECULE_STEP_OWNER_NOT_MOLECULE", "MOLECULE_STEP_TARGET_UNDECLARED", "MOLECULE_STEP_UNNAMED",
                  "MOLECULE_STEP_WITHOUT_KIND", "MOLECULE_STEP_WITHOUT_TARGET", "MOLECULE_WITHOUT_EMISSION",
                  "MOLECULE_WITHOUT_STEPS"}
HELD = MOLECULE_RULES | {"IMPLEMENTATION_WITHOUT_KIND", "IMPLEMENTATION_KIND_UNKNOWN"}
RULES = [r for r in rule_set() if r.id in HELD or (
    r.id == "CELL_NOT_IN_VOCABULARY" and r.register in ("molecule_steps", "molecule_step_bindings",
                                                        "implementation_bindings"))]


def fired(text: str) -> list[str]:
    return sorted(f.code for f in evaluate(parsed(text), RULES).findings)


def machine(code: str) -> dict:
    return next(a["machine"] for a in render_all(registers(design()), MANDATE) if a["machine"]["fqdn"] == code)


def test_a_loop_over_a_molecule_renders_the_form_the_compiler_lowers():
    write = machine(WRITE)["machine"]
    assert "implementation" not in write
    assert write["emit"] == {"result": "written"}
    assert write["atom_stream"] == [{
        "kind": "loop", "molecule": PASS, "as": "written",
        "over": "$.inputs.positions", "iterator": "position",
        "accumulator": {"text": "", "done": False},
        "inputs": {"position": "$.iterator", "text": "$.accumulator.text",
                   "done": "$.accumulator.done", "forbidden": "$.inputs.forbidden"},
        "update_accumulator": {"text": "$.results.text", "done": "$.results.done"},
    }]
    passed = machine(PASS)["machine"]
    assert passed["emit"] == {"result": "chosen"}
    offered, chosen = passed["atom_stream"]
    assert offered == {"kind": "atom", "atom": OFFER, "as": "offered",
                       "with": {"position": "$.inputs.position"}}
    assert chosen["with"]["candidates"] == "$.results.offered.candidates"
    assert machine(OFFER)["machine"]["implementation"]["callable"] == "execute"


def test_each_transform_is_governed_by_the_constitution_its_kind_and_purity_place_it_under():
    assert machine(WRITE)["governed_by"] == machine(PASS)["governed_by"] == \
        "capability_transforms::CONSTITUTION_MOLECULES_V0"
    assert machine(OFFER)["governed_by"] == "capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0"
    assert machine(CHOOSE)["governed_by"] == "capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0"


def test_every_fact_of_a_molecule_is_determined_by_the_design():
    undetermined = [(c, p) for c, p, ok in requirements(registers(design()), MANDATE,
                                                  provenance_of(render_all(registers(design()), MANDATE)))
                    if not ok and ("atom_stream" in p or "emit" in p)]
    assert undetermined == [], undetermined


def test_a_well_formed_molecule_design_passes_every_rule():
    assert fired(design()) == [], fired(design())


def test_each_rule_fires_on_the_defect_it_names():
    cases = {
        "MOLECULE_WITHOUT_STEPS": design(steps=STEPS[2:]),
        "MOLECULE_STEP_OWNER_NOT_MOLECULE": design(steps=[*STEPS, (OFFER, "x", "atom", CHOOSE, None, None, None)]),
        "MOLECULE_STEP_TARGET_UNDECLARED": design(steps=[STEPS[0], (PASS, "chosen", "atom", f"{D}::CT_NONE_V0", None, None, "result"), STEPS[2]]),
        "LOOP_WITHOUT_COLLECTION": design(steps=[*STEPS[:2], (WRITE, "written", "loop", PASS, "", "position", "result")]),
        "LOOP_COLLECTION_UNROOTED": design(steps=[*STEPS[:2], (WRITE, "written", "loop", PASS, "results.chosen.words", "position", "result")]),
        "LOOP_WITHOUT_ITERATOR": design(steps=[*STEPS[:2], (WRITE, "written", "loop", PASS, "inputs.positions", "", "result")]),
        "LOOP_FIELDS_OUTSIDE_LOOP": design(steps=[(PASS, "offered", "atom", OFFER, "inputs.positions", None, None), *STEPS[1:]]),
        "MOLECULE_WITHOUT_EMISSION": design(steps=[*STEPS[:2], (WRITE, "written", "loop", PASS, "inputs.positions", "position", None)]),
        "MOLECULE_EMITS_TWICE": design(steps=[(PASS, "offered", "atom", OFFER, None, None, "offered"), *STEPS[1:]]),
        "MOLECULE_BINDING_STEP_UNDECLARED": design(bindings=[*BINDINGS, (PASS, "nowhere", "INPUT", "x", "inputs.x")]),
        "MOLECULE_BINDING_WITHOUT_SOURCE": design(bindings=[*BINDINGS, (PASS, "chosen", "INPUT", "x", "")]),
        "MOLECULE_BINDING_SOURCE_MALFORMED": design(bindings=[*BINDINGS, (PASS, "chosen", "INPUT", "x", "$.inputs.x")]),
        "LOOP_UPDATE_NOT_FROM_RESULT": design(bindings=[*BINDINGS[:-1], (WRITE, "written", "UPDATE", "done", "accumulator.done")]),
        "IMPLEMENTATION_WITHOUT_KIND": design(impl=[*IMPL[:3], (WRITE, "", "", "ct_impure")]),
        "MOLECULE_STEP_KIND_UNKNOWN": design(steps=[*STEPS[:2], (WRITE, "written", "repeat", PASS, "inputs.positions", "position", "result")]),
        "MOLECULE_STEP_WITHOUT_KIND": design(steps=[*STEPS[:2], (WRITE, "written", "", PASS, None, None, "result")]),
        "MOLECULE_STEP_UNNAMED": design(steps=[(PASS, "", "atom", OFFER, None, None, None), *STEPS[1:]]),
        "MOLECULE_STEP_WITHOUT_TARGET": design(steps=[(PASS, "offered", "atom", "", None, None, None), *STEPS[1:]]),
        "IMPLEMENTATION_KIND_UNKNOWN": design(impl=[*IMPL[:3], (WRITE, "", "compound", "ct_impure")]),
        "CELL_NOT_IN_VOCABULARY": design(bindings=[*BINDINGS, (WRITE, "written", "SEED", "x", "1")]),
    }
    for rule, text in cases.items():
        assert rule in fired(text), (rule, fired(text))
    unshown = (HELD | {"CELL_NOT_IN_VOCABULARY"}) - set(cases)
    assert not unshown, f"rules never shown to fire: {sorted(unshown)}"


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except Exception as exc:  # report every test, then fail the run
            failed += 1
            print(f"  FAIL  {name}: {exc!r}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
