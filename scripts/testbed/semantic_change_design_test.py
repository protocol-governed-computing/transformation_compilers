"""Semantic change — a change of meaning is a new identity, and a replacement accounts for its reach.

Construction compared an amendment with what it amends only for the facts it would lose, skipped
even that without the composition, and let a design withdraw facts; every change of the last cycle
changed meaning under an old identity. It now compares the whole declaration by the platform's
declaration of what carries no meaning, refuses an amendment it cannot compare, and refuses a
withdrawal. A design may re-point a reference to what it replaces, and every live referrer of a
replaced or retired artifact must be replaced, retired, amended or re-pointed by the design. A
retirement takes away an artifact with no successor; construction never deletes it. Inspection answers who
refers to an artifact from the composition's record of references.

Run:  python scripts/testbed/semantic_change_design_test.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from inspector import api as inspector_api

import machine
from transformation.build import sameness
from transformation.build.generators import Context
from transformation.cli import _meaning_refusals
from transformation.design.evaluate import ParsedDocument
from transformation.design.oracle import evaluate
from transformation.design.rule_sets import RULE_SETS

rule_set = RULE_SETS["p7"].rule_set
from transformation.design.read import parse_text

SNAPSHOT = Path(__file__).resolve().parents[3] / "snapshot"

DECL = sameness.Declaration(
    documentation=frozenset({"summary", "description"}),
    unordered=frozenset({"allowed", "consults"}),
    reference=frozenset({"governed_by", "consults", "workflow", "code"}),
    reference_keyed=frozenset({"bindings"}),
)
SUCCESSOR = {"probe::RB_OLD_V0": "probe::RB_NEW_V0", "RB_OLD_V0": "RB_NEW_V0"}
WAS = {"governed_by": "workflow::CONSTITUTION_WORKFLOW_V0", "summary": "Decides",
       "core": {"description": "Old words", "allowed": ["SUCCESS", "VIOLATION"],
                "consults": ["probe::RB_OLD_V0"], "steps": [{"step": "a", "op": "READ"}]}}


def _now(**core) -> dict:
    return {**WAS, "core": {**WAS["core"], **core}}


# --- the comparison ----------------------------------------------------------------------------

def test_wording_and_the_order_of_a_set_keep_meaning():
    now = {**_now(description="New words", allowed=["VIOLATION", "SUCCESS"]), "summary": "Judges"}
    assert sameness.differences(WAS, now, DECL, {}) == []


def test_an_added_altered_or_removed_fact_changes_meaning():
    assert sameness.differences(WAS, _now(extra=1), DECL, {}) == ["core.extra"]
    assert sameness.differences(WAS, _now(steps=[{"step": "a", "op": "WRITE"}]), DECL, {}) == \
        ["core.steps[a].op"]
    assert sameness.differences(WAS, _now(allowed=["SUCCESS"]), DECL, {}) == ["core.allowed"]


def test_explanation_holding_data_carries_meaning():
    assert sameness.differences(_now(description={"layers": 2}), _now(description={"layers": 3}),
                                DECL, {}) == ["core.description.layers"]


def test_a_reference_to_the_declared_successor_is_the_same_reference():
    now = _now(consults=["probe::RB_NEW_V0"])
    assert sameness.differences(WAS, now, DECL, {}) == ["core.consults"]
    assert sameness.differences(WAS, now, DECL, SUCCESSOR) == []


def test_a_successor_outside_a_reference_part_still_changes_meaning():
    was, now = _now(note="probe::RB_OLD_V0"), _now(note="probe::RB_NEW_V0")
    assert sameness.differences(was, now, DECL, SUCCESSOR) == ["core.note"]


# --- the declaration ---------------------------------------------------------------------------

DECLARED = {"documentation": {"entries": ["summary"]}, "unordered": {"entries": ["allowed"]},
            "reference": {"entries": ["governed_by"]}, "reference_keyed": {"entries": ["bindings"]},
            "sameness_rules": {"entries": sorted(sameness.APPLIED)}}


def test_a_declared_rule_the_comparison_does_not_apply_refuses_the_comparison():
    rules = {"entries": sorted(sameness.APPLIED) + ["order_of_steps_ignored"]}
    try:
        sameness.Declaration.from_frontmatter({**DECLARED, "sameness_rules": rules})
    except sameness.Uncomparable as exc:
        assert "order_of_steps_ignored" in str(exc)
    else:
        raise AssertionError("a comparison ran without a rule the platform declares")



def test_the_composition_declares_exactly_the_rules_construction_applies():
    assert sameness.read(SNAPSHOT).reference


# --- a re-point --------------------------------------------------------------------------------

DOC = """# IN_PROBE_V0

Starts WF_OLD_V0, which names probe::RB_OLD_V0 in its prose.

## Machine

```yaml
fqdn: probe::IN_PROBE_V0
core:
  workflow: WF_OLD_V0
  consults: [probe::RB_OLD_V0]
```
"""


def test_a_re_point_rewrites_names_in_the_machine_block_only():
    out = sameness.repoint(DOC, {**SUCCESSOR, "WF_OLD_V0": "WF_NEW_V0"}, DECL)
    assert "workflow: WF_NEW_V0" in out and "[probe::RB_NEW_V0]" in out, out
    assert out.startswith(DOC.split("```yaml")[0]), "prose was rewritten"


def test_yaml_in_the_prose_is_not_the_machine_block():
    # A declaration may show YAML in its prose before its machine block, as an example.
    doc = """# STRUCTURE_PROBE_V0

```yaml
example: not the declaration
```

## Machine

```yaml
fqdn: probe::STRUCTURE_PROBE_V0
note: "a value may carry ``` backticks"
```
"""
    assert sameness.machine(doc) == {"fqdn": "probe::STRUCTURE_PROBE_V0",
                                     "note": "a value may carry ``` backticks"}


def test_a_re_point_leaves_a_place_label_and_its_route_alone():
    doc = """## Machine

```yaml
fqdn: probe::WF_V0
core:
  nodes:
    CC_OLD_V0:
      code: CC_OLD_V0
      next: {SUCCESS: EXIT_DONE}
    IN_V0:
      next: {ACK: CC_OLD_V0}
```
"""
    successor = {"probe::CC_OLD_V0": "probe::CC_NEW_V0", "CC_OLD_V0": "CC_NEW_V0"}
    out = sameness.machine(sameness.repoint(doc, successor, DECL))
    nodes = out["core"]["nodes"]
    assert nodes["CC_OLD_V0"]["code"] == "CC_NEW_V0", nodes
    assert nodes["IN_V0"]["next"]["ACK"] == "CC_OLD_V0", nodes
    assert sameness.differences(sameness.machine(doc), out, DECL, successor) == []


# --- the design phase --------------------------------------------------------------------------

def _doc(action: str, withdrawal: bool, fqdn: str = "probe::CC_DECIDE_V0") -> ParsedDocument:
    text = machine.document(
        "Design Intent: probe / semantic change",
        machine.register("existing_inventory",
                         ["FQDN", "Action", "Summary", "Reason",
                          "Source Finding"],
                         [(fqdn, action, "Decides", "Amended", "human decision")]),
        machine.register("withdrawn_facts", ["Artifact", "Fact", "Reason", "Source Finding"],
                         [("probe::CC_DECIDE_V0", ".core.inputs.allowed_set", "Gone", "human decision")]
                         if withdrawal else [], declared_empty=False),
    )
    header, sections, registers = parse_text(text)
    return ParsedDocument(header=header, sections=sections, registers=registers, raw=text,
                          path="probe", observed={})


def _findings(doc: ParsedDocument, *ids: str) -> list[str]:
    return [f.code for f in evaluate(doc, [r for r in rule_set() if r.id in ids]).findings]


def test_a_design_may_re_point():
    assert _findings(_doc("REPOINT", False), "CELL_NOT_IN_VOCABULARY") == []


def test_a_design_may_retire():
    assert _findings(_doc("RETIRE", False), "CELL_NOT_IN_VOCABULARY") == []


def test_a_design_retires_only_what_it_could_author():
    assert _findings(_doc("RETIRE", False), "RETIRED_ARTIFACT_NOT_AUTHORABLE") == []
    assert _findings(_doc("RETIRE", False, "workflow::CONSTITUTION_WORKFLOW_V0"),
                     "RETIRED_ARTIFACT_NOT_AUTHORABLE") == ["RETIRED_ARTIFACT_NOT_AUTHORABLE"]


def test_a_withdrawal_is_refused():
    assert _findings(_doc("EXTEND", False), "WITHDRAWAL_IS_A_CHANGE_OF_MEANING") == []
    assert _findings(_doc("EXTEND", True), "WITHDRAWAL_IS_A_CHANGE_OF_MEANING") == \
        ["WITHDRAWAL_IS_A_CHANGE_OF_MEANING"]


# --- construction ------------------------------------------------------------------------------

def _p7(*rows: tuple[str, str]) -> dict:
    return {"existing_inventory": [{"fqdn": f, "action": a} for f, a in rows]}


def test_an_amendment_without_the_composition_is_refused():
    p7 = _p7(("transformation::AC_REGISTER_AUTHOR_V0", "EXTEND"))
    refusals = _meaning_refusals(p7, {}, None, Context(p7=p7, p8={}))
    assert len(refusals) == 1 and "--snapshot" in refusals[0], refusals


def test_a_design_touching_nothing_needs_no_composition():
    p7 = _p7(("transformation::AC_REGISTER_AUTHOR_V0", "REUSE"))
    assert _meaning_refusals(p7, {}, None, Context(p7=p7, p8={})) == []


def test_a_replacement_names_every_referrer_it_leaves_unaccounted():
    p7 = _p7(("transformation::AC_REGISTER_AUTHOR_V0", "REPLACE"))
    refusals = _meaning_refusals(p7, {}, SNAPSHOT, Context(p7=p7, p8={}, snapshot_root=SNAPSHOT))
    assert len(refusals) == 9 and all("still names it" in r for r in refusals), refusals


def test_a_route_to_a_place_is_not_a_referrer():
    # The parameter check routes to the place that records the action, so inspection reports it as
    # a referrer by NODE_NEXT; its declaration does not name the recording contract.
    target = "ai_governance::CC_RECORD_GOVERNED_ACTION_V0"
    p7 = _p7((target, "REPLACE"))
    refusals = _meaning_refusals(p7, {}, SNAPSHOT, Context(p7=p7, p8={}, snapshot_root=SNAPSHOT))
    assert refusals == [f"{target} is replaced and ai_governance::WF_GOVERN_AGENT_ACTION_V0 still "
                        f"names it — REPLACE, RETIRE, EXTEND or REPOINT "
                        f"ai_governance::WF_GOVERN_AGENT_ACTION_V0 in this design"], refusals


def test_a_retirement_names_every_referrer_it_leaves_unaccounted():
    target = "ai_governance::CC_RECORD_GOVERNED_ACTION_V0"
    p7 = _p7((target, "RETIRE"))
    refusals = _meaning_refusals(p7, {}, SNAPSHOT, Context(p7=p7, p8={}, snapshot_root=SNAPSHOT))
    assert refusals == [f"{target} is retired and ai_governance::WF_GOVERN_AGENT_ACTION_V0 still "
                        f"names it — REPLACE, RETIRE, EXTEND or REPOINT "
                        f"ai_governance::WF_GOVERN_AGENT_ACTION_V0 in this design"], refusals


def test_a_retired_referrer_is_accounted_for():
    # A replaced event, named by a contract the same design retires: the retirement accounts for it.
    event, contract = "ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0", "ai_governance::CC_RECORD_GOVERNED_ACTION_V0"
    replaced_only = _p7((event, "REPLACE"))
    before = _meaning_refusals(replaced_only, {}, SNAPSHOT,
                               Context(p7=replaced_only, p8={}, snapshot_root=SNAPSHOT))
    assert any(f"{event} is replaced and {contract} still names it" in r for r in before), before
    p7 = _p7((event, "REPLACE"), (contract, "RETIRE"))
    after = _meaning_refusals(p7, {}, SNAPSHOT, Context(p7=p7, p8={}, snapshot_root=SNAPSHOT))
    assert not any(f"and {contract} still names it" in r for r in after), after


def test_a_retired_transform_takes_its_test_data_with_it():
    target = "ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0"
    p7 = _p7((target, "RETIRE"))
    refusals = _meaning_refusals(p7, {}, SNAPSHOT, Context(p7=p7, p8={}, snapshot_root=SNAPSHOT))
    assert not any("TEST_DATA_CT_PURE_CHECK_QUOTA_AVAILABLE_V0" in r for r in refusals), refusals


def test_a_retirement_of_what_the_composition_does_not_hold_is_refused():
    p7 = _p7(("ai_governance::CC_NEVER_HELD_V0", "RETIRE"))
    refusals = _meaning_refusals(p7, {}, SNAPSHOT, Context(p7=p7, p8={}, snapshot_root=SNAPSHOT))
    assert refusals == ["ai_governance::CC_NEVER_HELD_V0 is retired and the composition does not "
                        "hold it"], refusals


def test_a_referrer_the_design_re_points_is_accounted_for():
    status, result = inspector_api.query(
        "si.artifact.refs", {"artifact": "transformation::AC_REGISTER_AUTHOR_V0"}, str(SNAPSHOT))
    referrers = sorted({r["fqdn"] for r in result["refs"]})
    p7 = _p7(("transformation::AC_REGISTER_AUTHOR_V0", "REPLACE"),
             *[(r, "REPOINT") for r in referrers])
    refusals = _meaning_refusals(p7, {}, SNAPSHOT, Context(p7=p7, p8={}, snapshot_root=SNAPSHOT))
    # No successor is declared, so each re-point names nothing it could move — and says so.
    assert refusals and all("names nothing this design replaces" in r for r in refusals), refusals
    assert not any("still names it" in r for r in refusals), refusals


# --- inspection --------------------------------------------------------------------------------

def test_inspection_reports_every_referrer_the_record_holds():
    # Counted from the canonical record itself, so the check follows the composition rather than a
    # size it once had.
    target = "workflow::CONSTITUTION_WORKFLOW_V0"
    held = {d["fqdn_id"] for d in (json.loads(p.read_text())
                                   for p in (SNAPSHOT / "canonical").rglob("*.json"))
            if d.get("fqdn_id") != target and target in (d.get("references") or [])}
    status, result = inspector_api.query("si.artifact.refs", {"artifact": target}, str(SNAPSHOT))
    assert status == "SUCCESS" and held and result["ref_count"] == len(held), \
        (result.get("ref_count"), len(held))


if __name__ == "__main__":
    if not (SNAPSHOT / "manifest.json").is_file():
        print("SKIP  no assembled snapshot")
        sys.exit(0)
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
