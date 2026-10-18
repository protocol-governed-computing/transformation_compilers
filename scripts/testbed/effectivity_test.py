"""Rule effectivity — what judged a document, and whether a change to the rules was declared.

- every phase's rule set is the last revision its schema records, and `judged_by` names it;
- a rule set changed without a revision is refused, and names no revision;
- the header rules refuse a document that does not state what it is, or names another phase's rules;
- an approval stands confirmed under the rule set it was given under, and unconfirmed under another;
- the difference between two rule sets is named rule by rule.

Run:  python scripts/testbed/effectivity_test.py
Exit: 0 when every case holds, 1 otherwise.
"""

from __future__ import annotations

import sys
from dataclasses import replace
from pathlib import Path

from transformation.design import effectivity
from transformation.design.oracle import evaluate
from transformation.design.read import read_seed
from transformation.design.rule_sets import RULE_SETS

REPO = Path(__file__).resolve().parents[2]
DOCUMENT = REPO / "scripts/testbed/fixtures/catalog/cr_01_catalog/p7_design_intent_book_library_mgmt_catalog_v0.md"
P7 = RULE_SETS["p7"]
CURRENT = P7.shape.schema_id
APPROVAL = {"gate": "Gate 1 — Design Approval", "rule_set": CURRENT, "state": "APPROVED"}

failures = 0


def case(name: str, holds: bool, detail: object = "") -> None:
    global failures
    failures += not holds
    print(f"  {'PASS' if holds else 'FAIL'}  {name}" + ("" if holds else f"\n          {detail}"))


def header_findings(**fields) -> list[tuple[str, object]]:
    """The header findings for the fixture document with its header fields replaced."""
    doc = read_seed(DOCUMENT)
    doc.header = {k: v for k, v in {**doc.header, **fields}.items() if v is not None}
    rules = [r for r in P7.rule_set() if r.id.startswith("HEADER_")]
    return [(f.code, f.locator["field"]) for f in evaluate(doc, rules).findings]


def main() -> int:
    print("revisions")
    for phase_id, phase in RULE_SETS.items():
        rules = phase.rule_set()
        judged = effectivity.judged_by(rules, phase.shape)
        case(f"{phase_id} is its schema's last revision", effectivity.unrecorded(phase.shape, rules) is None
             and judged["revision"] == phase.shape.revisions[-1]["revision"], judged)
    rules = P7.rule_set()
    changed = [replace(rules[0], intent=rules[0].intent + " (changed)")] + rules[1:]
    case("a rule changed without a revision is refused", effectivity.unrecorded(P7.shape, changed) is not None)
    case("and names no revision", effectivity.judged_by(changed, P7.shape)["revision"] is None)
    case("judged_by names the schema its rules carry", effectivity.judged_by(rules, P7.shape)["schema"] == CURRENT)

    print("header")
    case("a document stating its header has no header finding", header_findings() == [], header_findings())
    case("a document naming no rule set is refused",
         header_findings(rule_set=None) == [("HEADER_FIELD_MISSING", "rule_set")], header_findings(rule_set=None))
    case("a document of another phase is refused",
         header_findings(phase="p6") == [("HEADER_FIELD_MISMATCH", "phase")], header_findings(phase="p6"))
    other = "transformation.schemas.REGISTER_SCHEMA_P6_V0"
    case("a document naming another phase's rules is refused",
         header_findings(rule_set=other) == [("HEADER_FIELD_MISMATCH", "rule_set")], header_findings(rule_set=other))
    case("a well-formed approval is admitted", header_findings(approval=APPROVAL) == [],
         header_findings(approval=APPROVAL))
    bad = {**APPROVAL, "state": "SIGNED"}
    case("an approval in no declared state is refused",
         header_findings(approval=bad) == [("HEADER_FIELD_NOT_OF_TYPE", "approval")], header_findings(approval=bad))

    print("approvals")
    standing = effectivity.approval_standing({"approval": APPROVAL}, CURRENT)
    case("an approval under the current rule set is confirmed", standing["standing"] == "confirmed", standing)
    later = CURRENT.replace("_V0", "_V1")
    standing = effectivity.approval_standing({"approval": APPROVAL}, later)
    case("under a later rule set it stands unconfirmed", standing["standing"] == "unconfirmed", standing)
    case("a document with no approval has no standing", effectivity.approval_standing({}, CURRENT) is None)

    print("difference")
    diff = effectivity.difference(rules, changed[:-1] + [replace(rules[-1], identity=rules[-1].identity + "x")])
    case("names the changed, removed and added rules by identity",
         diff == {"added": [rules[-1].identity + "x"], "removed": [rules[-1].identity],
                  "changed": [rules[0].identity]}, diff)
    case("two identical rule sets differ in nothing",
         effectivity.difference(rules, rules) == {"added": [], "removed": [], "changed": []})

    if failures:
        print(f"\nEFFECTIVITY FAILED — {failures} case(s)")
        return 1
    print(f"\nEFFECTIVITY PASSED — {len(RULE_SETS)} rule sets at their recorded revision; header, approval "
          f"and difference cases hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
