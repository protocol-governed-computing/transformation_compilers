"""Vector design — the design language's half of software_governance/dossiers/transform_conformance (held at the v5 tag).

A transform's proof is declared in P7 as its cases (`test_cases`) and what each case hands the
transform and expects back (`test_case_values`). Shown here: construction renders a transform's cases
as its vector, beside it, in the shape `SCHEMA_TEST_DATA_V0` admits — including a molecule's recorded
results and a shape assertion — with every fact of it determined by the design; a design without cases
declares no vector layer; and each rule that holds a design to proving its transforms fires on a design
built to trip it and stays silent on the one that keeps it.

Run:  python scripts/testbed/vector_design_test.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

import machine
from transformation.build.provenance import of as provenance_of
from transformation.build.render import build_manifest, render_all, requirements
from transformation.design.evaluate import ParsedDocument
from transformation.design.oracle import evaluate
from transformation.design.rule_sets import RULE_SETS

rule_set = RULE_SETS["p7"].rule_set
from transformation.design.read import parse_text

D = "probe"
OFFER, WRITE = f"{D}::CT_IMPURE_OFFER_WORDS_V0", f"{D}::CT_WRITE_RESPONSE_V0"
NEW = [("Offer words", OFFER), ("Write a response", WRITE)]
CASES = [  # transform, case, outcome
    (OFFER, "offers_candidates", "SUCCESS"),
    (WRITE, "writes_three_words", "SUCCESS"),
    (WRITE, "refuses_without_positions", "VIOLATION"),
]
VALUES = [  # transform, case, role, field, value
    (OFFER, "offers_candidates", "INPUT", "position", 1),
    (OFFER, "offers_candidates", "ASSERT", "candidates", {"mode": "property", "type": "non_zero"}),
    (WRITE, "writes_three_words", "INPUT", "positions", [1, 2, 3]),
    (WRITE, "writes_three_words", "RECORDED", "written[0]/offered", {"candidates": ["the"]}),
    (WRITE, "writes_three_words", "RECORDED", "written[1]/offered", {"candidates": ["balance"]}),
    (WRITE, "writes_three_words", "RECORDED", "written[2]/offered", {"candidates": ["holds"]}),
    (WRITE, "writes_three_words", "EXPECTED", "result", {"text": "the balance holds", "done": False}),
    (WRITE, "refuses_without_positions", "INPUT", "positions", ""),
]
AMENDED = f"{D}::CT_PURE_CHOOSE_WORD_V0"


def _table(register: str, header: list[str], rows: list[tuple]) -> tuple[str, dict]:
    return machine.register(register, header, rows)


def design(cases=CASES, values=VALUES, amended=()) -> str:
    return machine.document(
        "Design Intent: probe / words",
        _table("new_artifacts", ["Capability", "Family", "Code", "Summary", "Owner Subdomain", "Status",
                                   "Source Finding"],
                 [(c, "CT", code, c, "words", "NEW", "human decision") for c, code in NEW]),
        _table("existing_inventory", ["FQDN", "Action", "Summary",
                                        "Reason", "Source Finding"],
                 [(a, "EXTEND", "Chooses a word", "Amended", "human decision") for a in amended]),
        _table("test_cases", ["CT Code", "Case", "Expected Outcome", "Source Finding"],
                 [(*c, "human decision") for c in cases]),
        _table("test_case_values", ["CT Code", "Case", "Role", "Field",
                                      "Value", "Source Finding"],
                 [(*v, "human decision") for v in values])
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
# The vector rules: every finding a transform's test cases and their values can raise.
HELD = {"AMENDED_TRANSFORM_WITHOUT_VECTOR", "TEST_CASE_NAME_MALFORMED",
        "TEST_CASE_TRANSFORM_UNDECLARED", "TEST_CASE_UNNAMED", "TEST_VALUE_CASE_UNDECLARED",
        "TEST_VALUE_EMPTY", "TEST_VALUE_WITHOUT_FIELD",
        "TRANSFORM_WITHOUT_VECTOR"}
# The declaration the compiler validates a vector against, read as a file: this repo never imports the
# compiler, and the schema is the platform's declaration rather than the compiler's code.
SCHEMA = json.loads((Path(__file__).resolve().parents[3]
                     / "software_governance/registry/schema/SCHEMA_TEST_DATA_V0.json").read_text())
RULES = [r for r in rule_set() if r.id in HELD or (
    r.id == "CELL_NOT_IN_VOCABULARY" and r.register in ("test_cases", "test_case_values"))]


def fired(text: str) -> list[str]:
    return sorted(f.code for f in evaluate(parsed(text), RULES).findings)


def vector(code: str) -> dict:
    return next(a for a in render_all(registers(design()), MANDATE)
                if a["machine"]["fqdn"] == f"{D}::TEST_DATA_{code.split('::')[1]}")


def test_a_transform_s_cases_render_as_its_vector_beside_it():
    rendered = vector(WRITE)
    assert rendered["path"] == "registry/words/test_data/TEST_DATA_CT_WRITE_RESPONSE_V0.md"
    m = rendered["machine"]
    assert (m["artifact_kind"], m["version"], m["target"]) == ("TEST_DATA", "V0", WRITE)
    assert m["governed_by"] == "conformance::CONSTITUTION_TEST_DATA_V0"
    written, refused = m["cases"]
    assert written == {
        "case_id": "writes_three_words", "expected_outcome": "SUCCESS",
        "bindings": {"positions": [1, 2, 3]},
        "expected": {"result": {"text": "the balance holds", "done": False}},
        "recorded": {f"written[{i}]/offered": {"candidates": [w]}
                     for i, w in enumerate(["the", "balance", "holds"])},
    }
    assert refused == {"case_id": "refuses_without_positions", "expected_outcome": "VIOLATION",
                       "bindings": {"positions": ""}}
    offered = vector(OFFER)["machine"]["cases"][0]
    assert offered["assertions"] == {"candidates": {"mode": "property", "type": "non_zero"}}


def test_every_rendered_vector_is_one_the_platform_admits():
    for code in (OFFER, WRITE):
        errors = [e.message for e in Draft202012Validator(SCHEMA).iter_errors(vector(code)["machine"])]
        assert errors == [], (code, errors)


def test_every_fact_of_a_vector_is_determined_by_the_design():
    undetermined = [(c, p) for c, p, ok in requirements(registers(design()), MANDATE,
                                                  provenance_of(render_all(registers(design()), MANDATE)))
                    if not ok and c.startswith("TEST_DATA_")]
    assert undetermined == [], undetermined


def test_a_design_with_cases_declares_its_vector_layer_and_one_without_does_not():
    with_cases = build_manifest(registers(design()), MANDATE)
    assert "TEST_DATA" in with_cases["artifact_discovery"]["artifact_types"]
    assert with_cases["output_configuration"]["conformance"]["subpath"] == "compiled/transform_conformance"
    without = build_manifest(registers(design(cases=[], values=[])), MANDATE)
    assert "TEST_DATA" not in without["artifact_discovery"]["artifact_types"]
    assert "conformance" not in without["output_configuration"]


def test_a_well_formed_vector_design_passes_every_rule():
    assert fired(design()) == [], fired(design())


def test_each_rule_fires_on_the_defect_it_names():
    cases = {
        "TRANSFORM_WITHOUT_VECTOR": design(cases=CASES[1:], values=VALUES[2:]),
        "AMENDED_TRANSFORM_WITHOUT_VECTOR": design(amended=[AMENDED]),
        "TEST_CASE_TRANSFORM_UNDECLARED": design(cases=[*CASES, (f"{D}::CT_NONE_V0", "orphan", "SUCCESS")]),
        "TEST_CASE_UNNAMED": design(cases=[*CASES, (WRITE, "", "SUCCESS")]),
        "TEST_CASE_NAME_MALFORMED": design(cases=[*CASES, (WRITE, "Writes-Words", "SUCCESS")]),
        "TEST_VALUE_CASE_UNDECLARED": design(values=[*VALUES, (WRITE, "nowhere", "INPUT", "x", "1")]),
        "TEST_VALUE_WITHOUT_FIELD": design(values=[*VALUES, (WRITE, "writes_three_words", "INPUT", "", "1")]),
        "TEST_VALUE_EMPTY": design(values=[*VALUES, (WRITE, "writes_three_words", "INPUT", "seed", machine.ABSENT)]),
        "CELL_NOT_IN_VOCABULARY": design(values=[*VALUES, (WRITE, "writes_three_words", "OUTPUT", "x", "1")]),
    }
    for rule, text in cases.items():
        assert rule in fired(text), (rule, fired(text))
    unshown = (HELD | {"CELL_NOT_IN_VOCABULARY"}) - set(cases)
    assert not unshown, f"rules never shown to fire: {sorted(unshown)}"
    amended_with_case = design(amended=[AMENDED], cases=[*CASES, (AMENDED, "chooses", "SUCCESS")])
    assert "AMENDED_TRANSFORM_WITHOUT_VECTOR" not in fired(amended_with_case)



def test_a_manifest_is_generated_for_an_amendment_and_declares_its_root():
    # A change that schedules nothing but states cases for transforms it redeclares still needs its
    # domain to compile them; and every manifest declares where it writes (A10).
    amending = registers(design())
    amending["existing_inventory"] = [{"fqdn": "probe::CT_PURE_PROBE_V0", "action": "EXTEND"}]
    manifest = build_manifest(amending, {"build_order": [], "field_declarations": MANDATE["field_declarations"]})
    assert manifest is not None and "TEST_DATA" in manifest["artifact_discovery"]["artifact_types"], manifest
    assert manifest["output_configuration"]["root"] == "snapshot", manifest["output_configuration"]
    assert build_manifest({}, {"build_order": []}) is None
    # The manifest describes the domain: a subdomain the change does not touch is still named.
    held = build_manifest(amending, {"build_order": [], "field_declarations": MANDATE["field_declarations"]},
                          ("untouched",))
    assert "untouched" in held["core"]["description"], held["core"]["description"]

def test_an_emitted_amendment_keeps_the_descriptions_it_replaces():
    # `check` measures an amendment with its predecessor's descriptions carried forward; emit must
    # write it the same way, reading the document it replaces, or what was measured is not written.
    import tempfile
    from transformation.build.completeness import carry_forward
    from transformation.build.render import render_document
    from transformation.cli import _predecessors

    rendered = render_all(registers(design()), MANDATE)
    target = next(a for a in rendered if a["path"].endswith("CT_WRITE_RESPONSE_V0.md"))
    prior = {**target["machine"], "core": {**target["machine"]["core"], "description": "Kept."}}
    with tempfile.TemporaryDirectory() as root:
        path = Path(root) / target["path"]
        path.parent.mkdir(parents=True)
        path.write_text(render_document({"machine": prior}), encoding="utf-8")
        carry_forward(rendered, _predecessors(rendered, Path(root)))
    assert target["machine"]["core"].get("description") == "Kept.", target["machine"]["core"]


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
