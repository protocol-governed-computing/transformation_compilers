"""End-to-end phase check — every phase through the real runtime.

The differential (`differential.py`) drives the capability transforms directly. It proves the rule
sets and the check logic, and it proves nothing about IN/WF/CC wiring, node input bindings, or
routing — because it never boots a snapshot or dispatches a workflow.

That gap is not theoretical. A workflow that bound `$.capability_result.header` across nodes passed
the differential and failed the moment it ran through `protocol_runtime`: workflow nodes read the
intent payload, not a previous node's result. Only executing the compiled workflow catches that
class of defect.

So this script executes each phase through the runtime, one case per line, and asserts the
expected verdict and finding count. Adding a phase is an entry in `CASES` — the runbook stays one
line however many phases exist.

Run:  python scripts/testbed/e2e_phases.py [snapshot_root]
Exit: 0 if every case matched, 1 otherwise.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent

# Domain CT/CS implementations are imported by declared module path at execution. Their roots are
# env-provisioned — the runtime never manipulates sys.path — so a suite that drives the runtime has
# to provision them the way `run.sh` does. P2 is the first phase to need this: it binds a capability
# whose host lives in the governance surface.
for _root in (WORKSPACE / "software_governance", WORKSPACE / "conformance_workloads",
              WORKSPACE / "business_domains", REPO):
    if str(_root) not in sys.path:
        sys.path.insert(0, str(_root))

from runtime import api
from meta_test import assert_consistent
from transformation.design.emit import workflow_fqdn
from transformation.design.rule_sets import RULE_SETS
from transformation.design.merit import Merit, load_policy, rate
PAYLOADS = REPO / "testbed" / "phases" / "test_payloads"

# phase, workflow, payload file, expected verdict, expected rule ids, expected rules evaluated,
# expected figure of merit.
#
# The rating is asserted, not just printed. A figure of merit nobody checks drifts into decoration:
# it would keep reporting a number while the thing it measures changed underneath it. Note that the
# two axes move independently — every admissible CR-1 document rates 4/5 because it carries a
# declared open question, which is a governed hole rather than a defect.
#
# The expectation names the rules that must fire, not how many. A finding *count* is a weak
# assertion: seven entirely different rules firing satisfies "7 findings", and the suite reports OK
# over the wrong behaviour. Naming them catches a rule that stops working even when another starts
# firing in its place.
#
# Both an admissible and an inadmissible case per phase: a suite that only runs the passing case
# proves transport, not governance.
# Which workflow judges each phase, and how many rules it seals, are read from the phases rather
# than restated: a version or a count copied here goes stale the moment a rule is added or a
# workflow replaced, and the suite then fails on the copy instead of on behaviour. The assertion
# keeps its force — the runtime must evaluate every declared rule, never a subset.
WF = {p.upper(): workflow_fqdn(p) for p in RULE_SETS}
RULES = {p.upper(): len(module.rule_set()) for p, module in RULE_SETS.items()}

CASES = [
    ("P0", WF["P0"],
     "01_admissible_seed.json", "ADMISSIBLE", [], RULES["P0"], 5),
    ("P0", WF["P0"],
     "02_admissible_reference.json", "ADMISSIBLE", [], RULES["P0"], 5),
    ("P0", WF["P0"],
     "03_inadmissible_seven_violations.json", "INADMISSIBLE", [
         "BELIEF_STATED_AS_FACT",
         "BELIEF_WITHOUT_VERIFICATION_GOAL",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "HEADER_FIELD_MISMATCH",
     ], RULES["P0"], 4),
    ("P0", WF["P0"],
     "04_inadmissible_structural.json", "INADMISSIBLE", ["REGISTER_MISSING"] * 5, RULES["P0"], 4),
    ("P0", WF["P0"],
     "05_inadmissible_truncated.json", "INADMISSIBLE", ["REGISTER_MISSING"] * 12, RULES["P0"], 4),
    # The seed's five remaining rules. `BELIEF_CARRIES_CERTAINTY` is the truth/belief split enforced
    # structurally: a Certainty column on system_beliefs would make them facts, so the rule refuses
    # the column rather than any value in it.
    ("P0", WF["P0"],
     "68_inadmissible_malformed_seed.json", "INADMISSIBLE", [
         "BELIEF_CARRIES_CERTAINTY",
         "HEADER_FIELD_MISSING",
         "REGISTER_CELL_UNRESOLVED",
         "REGISTER_COLUMN_MISSING",
         "REGISTER_EMPTY",
     ], RULES["P0"], 3),
    ("P1", WF["P1"],
     "06_p1_admissible_register.json", "ADMISSIBLE", [], RULES["P1"], 5),
    ("P1", WF["P1"],
     "07_p1_inadmissible_register.json", "INADMISSIBLE", [
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "ROW_WITHOUT_SOURCE_FINDING",
         # The leak and the loss are one edit seen from two sides: naming a transform inside a
         # business invariant also stops the row restating the invariant the seed declared. The
         # fixture was cut for the first defect years before the second rule existed.
         "SEED_ROW_NOT_CARRIED",
         # The second is the assumption this fixture inherits from the change request it was cut
         # from, reworded there from "register structure" to "section structure".
         "SEED_ROW_NOT_CARRIED",
         # Both mutations are additions as well as losses: a reworded row states something the seed
         # does not, which is the half of the contract confinement governs.
         "ROW_NOT_IN_SEED",
         "ROW_NOT_IN_SEED",
         # `I remembered it` is no citation at all, so its type refuses it (rebuild M3.3b-1).
         "CELL_NOT_OF_TYPE",
     ], RULES["P1"], 4),
    # P1's remaining ten. The clarification pair is the phase's own gate: a change request carrying
    # an unanswered blocking question is not a change request yet, and one only the business can
    # answer cannot be closed by anyone reading the document.
    ("P1", WF["P1"],
     "69_p1_inadmissible_outstanding_clarifications.json", "INADMISSIBLE", [
         "BLOCKING_CLARIFICATION_OUTSTANDING",
         "BUSINESS_CLARIFICATION_OUTSTANDING",
         "CITATION_ORDINAL_UNRESOLVED",
         # One ordinal rule resolves every citation, the seed's included (rebuild M3.4a-2).
         "CITATION_ORDINAL_UNRESOLVED",
         "BUSINESS_CLARIFICATION_OUTSTANDING",
     ], RULES["P1"], 3),
    # Six SEED_ROW_NOT_CARRIED and one ROW_NOT_IN_SEED are the cost of the shape defects, not extra
    # ones: emptying cr_type and dropping the events table strands every seed row they carried. An
    # earlier cut of this fixture dropped the `Certainty` column instead and fired
    # CELL_NOT_IN_VOCABULARY thirty-nine times — the check was right and the fixture was unreadable.
    ("P1", WF["P1"],
     "70_p1_inadmissible_malformed_document.json", "INADMISSIBLE", [
         "HEADER_FIELD_MISSING",
         "HEADER_FIELD_MISMATCH",
         "REGISTER_CELL_UNRESOLVED",
         "REGISTER_EMPTY",
         "REGISTER_MISSING",
         "ROW_NOT_IN_SEED",
     ] + ["SEED_ROW_NOT_CARRIED"] * 6 + ["REGISTER_COLUMN_MISSING"] * 12, RULES["P1"], 3),
    ("P2", WF["P2"],
     "08_p2_admissible_register.json", "ADMISSIBLE", [], RULES["P2"], 4),
    # Grounding: a misspelled identity and a right-code/wrong-namespace one are defects; an
    # identity simply absent from the baseline is proposed-new and correctly goes unflagged.
    ("P2", WF["P2"],
     "09_p2_inadmissible_register.json", "INADMISSIBLE", [
         "BASELINE_IDENTITY_UNRESOLVED",
         "BASELINE_IDENTITY_UNRESOLVED",
     ], RULES["P2"], 2),
    # CR-1 — the same three phases over a business subject. CR-0 is the pipeline authoring its own
    # domain, so it grounds every claim against artifacts this repo also wrote; the catalog CR
    # grounds against a composition it contributed nothing to, which is the harder case.
    ("P0", WF["P0"],
     "10_p0_admissible_catalog_seed.json", "ADMISSIBLE", [], RULES["P0"], 5),
    ("P1", WF["P1"],
     "11_p1_admissible_catalog_register.json", "ADMISSIBLE", [], RULES["P1"], 5),
    ("P2", WF["P2"],
     "12_p2_admissible_catalog_register.json", "ADMISSIBLE", [], RULES["P2"], 5),
    # The rules must bite on business content, not only on documents about the pipeline. A
    # misspelled identity and a right-code/wrong-namespace one are defects; design leaking into a
    # business-language cell is a third. An identity merely absent from the baseline stays
    # unflagged — that is proposed-new, which is what a CR is for.
    ("P2", WF["P2"],
     "13_p2_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "BASELINE_IDENTITY_UNRESOLVED",
         "BASELINE_IDENTITY_UNRESOLVED",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
     ], RULES["P2"], 2),
    # P2's remaining thirteen. `BELIEF_RESTATED_FROM_P1` is the sharpest of them: the citation is
    # carried forward correctly and the claim underneath it is quietly changed, so the substitution
    # inherits a provenance it never had.
    ("P2", WF["P2"],
     "71_p2_inadmissible_unverified_beliefs.json", "INADMISSIBLE", [
         "BELIEF_RESTATED_FROM_P1",
         "BELIEF_WITHOUT_EVIDENCE",
         "CITATION_ORDINAL_UNRESOLVED",
         "ROW_WITHOUT_SOURCE_FINDING",
         "SOURCE_FINDING_UNRESOLVED",
         "VERIFIED_BELIEF_IDENTITY_UNRESOLVED",
     ], RULES["P2"], 2),
    ("P2", WF["P2"],
     "72_p2_inadmissible_malformed_document.json", "INADMISSIBLE", [
         # Dropping the Evidence column takes the evidence with it, so both verification rows
         # report a result resting on nothing.
         "BELIEF_WITHOUT_EVIDENCE",
         "BELIEF_WITHOUT_EVIDENCE",
         "CELL_NOT_IN_VOCABULARY",
         "HEADER_FIELD_MISSING",
         "HEADER_FIELD_MISMATCH",
         "REGISTER_CELL_UNRESOLVED",
         "REGISTER_EMPTY",
         "REGISTER_MISSING",
     ] + ["REGISTER_COLUMN_MISSING"] * 2, RULES["P2"], 3),
    # P3 decides, so it observes twice: the artifact list resolves identities, the composition
    # summary carries what each domain declares about being reused. The inadmissible case offers a
    # business CR a pipeline capability and a conformance workload — a confusion that is invisible
    # in the document and only a declaration can settle.
    ("P3", WF["P3"],
     "14_p3_admissible_catalog_register.json", "ADMISSIBLE", [], RULES["P3"], 5),
    ("P3", WF["P3"],
     "15_p3_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "REUSE_CANDIDATE_NOT_ELIGIBLE",
         "REUSE_CANDIDATE_NOT_ELIGIBLE",
     ], RULES["P3"], 4),
    # Three documents demonstrating all 21 rules P3 declares, the phase that decides what is reused
    # and what is built.
    ("P3", WF["P3"],
     "62_p3_inadmissible_uncited_rows.json", "INADMISSIBLE", [
         "CITATION_ORDINAL_UNRESOLVED",
         "CITED_ALTERNATIVE_UNRESOLVED",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "ROW_WITHOUT_SOURCE_FINDING",
         "SOURCE_FINDING_UNRESOLVED",
     ], RULES["P3"], 2),
    ("P3", WF["P3"],
     "63_p3_inadmissible_unreasoned_decisions.json", "INADMISSIBLE", [
         # `UNRESOLVED` as a Decision is two defects on one cell: outside the vocabulary, and a
         # question hedged where the phase exists to settle it.
         "CELL_NOT_IN_VOCABULARY",
         "DECISION_WITHOUT_ALTERNATIVES",
         "DECISION_WITHOUT_RATIONALE",
         "IMPACT_WITHOUT_EVIDENCE",
         "REGISTER_CELL_UNRESOLVED",
         "SATURATION_CLAIMED_WITHOUT_EVIDENCE",
         "VERIFICATION_WITHOUT_EVIDENCE",
     ], RULES["P3"], 4),
    # Emptying the verification register is one edit and two rules: the register asserts nothing,
    # and the two beliefs P2 handed over go un-reverified. That is the same defect stated at two
    # altitudes — the shape, and the commitment the shape was carrying.
    ("P3", WF["P3"],
     "64_p3_inadmissible_malformed_document.json", "INADMISSIBLE", [
         "BELIEF_RESULT_NOT_REVERIFIED",
         "BELIEF_RESULT_NOT_REVERIFIED",
         "HEADER_FIELD_MISSING",
         "HEADER_FIELD_MISMATCH",
         "REGISTER_EMPTY",
         "REGISTER_MISSING",
         "SATURATION_CRITERIA_INCOMPLETE",
     ] + ["REGISTER_COLUMN_MISSING"] * 9, RULES["P3"], 3),
    # P4 consolidates: its defects live between registers, where every register is individually
    # well formed and the document as a whole asserts something untrue. The admissible case is the
    # corpus's only 5/5 — a consolidation carries no open questions of its own, because P3
    # resolved them.
    ("P4", WF["P4"],
     "16_p4_admissible_catalog_register.json", "ADMISSIBLE", [], RULES["P4"], 5),
    ("P4", WF["P4"],
     "17_p4_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "DEPENDENCY_IDENTITY_UNRESOLVED",
         "GAP_ENTRY_UNDECLARED",
         "GAP_WITHOUT_OWNER",
         "SCOPE_GAP_UNDECLARED",
     ], RULES["P4"], 2),
    # Three documents taking P4 from 5 demonstrated rules to all 18 it declares. P4 consolidates
    # Stages 1 to 3 and introduces nothing, so its defects are consolidation defects: a row that
    # cites the wrong place, a row that traces to no evidence, a document mis-shaped.
    #
    # The malformed case needed a fix before it could be written. `TABLE_HAS_COLUMNS` matched a
    # required column by prefix against any header, so `Source Finding` satisfied a required
    # `Source` — nine registers across six phases could lose a column and report clean. Matches are
    # now consumed once, exact before prefix.
    ("P4", WF["P4"],
     "65_p4_inadmissible_uncited_rows.json", "INADMISSIBLE", [
         "CITATION_ORDINAL_UNRESOLVED",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "ROW_WITHOUT_SOURCE_FINDING",
         "SOURCE_FINDING_UNRESOLVED",
     ], RULES["P4"], 4),
    ("P4", WF["P4"],
     "66_p4_inadmissible_untraced_consolidation.json", "INADMISSIBLE", [
         "CRITICAL_WITHOUT_GAP_ENTRY",
         "DECISION_WITHOUT_RATIONALE",
         "REGISTER_CELL_UNRESOLVED",
         "REGISTER_EMPTY",
         "SCOPE_WITHOUT_GAP_REFERENCE",
     ], RULES["P4"], 3),
    ("P4", WF["P4"],
     "67_p4_inadmissible_malformed_document.json", "INADMISSIBLE", [
         "HEADER_FIELD_MISSING",
         "HEADER_FIELD_MISMATCH",
         "REGISTER_MISSING",
     ] + ["REGISTER_COLUMN_MISSING"] * 13, RULES["P4"], 3),
    # P5 is the first rung up the purity ladder, and its two rules pull opposite ways: a
    # provisional code must NOT be namespaced, while a borrowed capability MUST be — one names
    # what this change creates, the other what it leans on.
    ("P5", WF["P5"],
     "18_p5_admissible_catalog_register.json", "ADMISSIBLE", [], RULES["P5"], 5),
    ("P5", WF["P5"],
     "19_p5_inadmissible_catalog_register.json", "INADMISSIBLE", [
         "BINDING_LEAKED_INTO_INTENT",
         "CROSS_SUBDOMAIN_REF_UNRESOLVED",
         "PROVISIONAL_CODE_ALREADY_BOUND",
         "PROVISIONAL_CODE_MALFORMED",
         "PROVISIONAL_FAMILY_MISMATCH",
         "PROVISIONAL_FAMILY_MISMATCH",
         # The fixture declares an identity Source it cannot derive as `UNRESOLVED`. A hole nothing
         # forces closed is how a design whose central
         # identity question was never settled reached execution admissible at every gate.
         "REGISTER_CELL_UNRESOLVED",
     # 4/5, not 3/5, since the merit policy stopped scoring the `UNRESOLVED` identity cell it now
     # refuses. One defect, one deduction: the rule that fired it.
     ], RULES["P5"], 4),
    # Four documents that take P5 from 6 demonstrated rules to all 24 it declares. They are grouped
    # by kind of authoring failure rather than one rule per file: an author who miscites one row
    # miscites several, and a document wrong in one way is the realistic subject. Each still names
    # every rule it must fire, so a rule that stops working is still caught alone.
    #
    # Two of the eighteen could not be reached at first, and both were the phase's doing rather than
    # the document's. `DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE` was keyed on the template author's
    # spelling of a column — `business_reason` against a row held under `Business Reason` — so the
    # scoped form of the flag emitted a rule that could not fire, at P3, P5, P6 and P7.
    # `CITATION_ORDINAL_UNRESOLVED` resolves an ordinal inside the prior a citation names, and every
    # P5 document cites S1/S2/S4 while P5 receives only p0 — so it is silent on every citation a
    # real document carries, and only one naming S0 reaches it.
    ("P5", WF["P5"],
     "54_p5_inadmissible_uncited_rows.json", "INADMISSIBLE", [
         "CITATION_ORDINAL_UNRESOLVED",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "ROW_WITHOUT_SOURCE_FINDING",
         "SOURCE_FINDING_UNRESOLVED",
     ], RULES["P5"], 4),
    ("P5", WF["P5"],
     "55_p5_inadmissible_hollow_registers.json", "INADMISSIBLE", [
         "CELL_NOT_IN_VOCABULARY",
         "IDENTITY_WITHOUT_UNIQUENESS_RULE",
         "INVARIANT_WITHOUT_BUSINESS_REASON",
         "REFINEMENT_NOT_STATED",
         "REGISTER_EMPTY",
     ], RULES["P5"], 3),
    ("P5", WF["P5"],
     "56_p5_inadmissible_malformed_document.json", "INADMISSIBLE", [
         "HEADER_FIELD_MISSING",
         "HEADER_FIELD_MISMATCH",
         "PURPOSE_PROVENANCE_NOT_SINGULAR",
         "REGISTER_MISSING",
     ] + ["REGISTER_COLUMN_MISSING"] * 10, RULES["P5"], 3),
    ("P5", WF["P5"],
     "57_p5_inadmissible_untouched_subdomain.json", "INADMISSIBLE", [
         "EVENT_CODE_NOT_PAST_PARTICIPLE",
         "PURPOSE_NOT_CARRIED_FROM_SEED",
         "TOUCHED_SUBDOMAIN_AUTHORS_NOTHING",
         "TOUCHED_SUBDOMAIN_WITHOUT_PURPOSE",
     ], RULES["P5"], 4),
    # P6 draws lines, and the ladder does not simply accumulate: P5 requires provisional codes,
    # P6 forbids them. Each rung admits its own vocabulary rather than everything below it.
    ("P6", WF["P6"],
     "20_p6_admissible_catalog_register.json", "ADMISSIBLE", [], RULES["P6"], 5),
    ("P6", WF["P6"],
     "21_p6_inadmissible_catalog_register.json", "INADMISSIBLE", [
         # A provisional code where a capability belongs unplaces the capability P5 named and
         # dangles the outcome row that restates it — one edit, three rules.
         "DEPENDENCY_DIRECTION_MALFORMED",
         # The same edit also leaks a design identity into `ownership`'s business-language column,
         # which this fixture has done since it was written and nothing reported: the rule was
         # keyed on the column name the template author typed rather than the one the row is held
         # under. It fires now. The document did not change; the rule started working.
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "IN_SCOPE_CAPABILITY_UNPLACED",
         "OUTCOME_CAPABILITY_UNPLACED",
         "PROVISIONAL_CODE_IN_PLACEMENT",
     ], RULES["P6"], 4),
    # Four documents taking P6 from 5 demonstrated rules to 21 of the 22 it declares.
    #
    # The grounding pair needed a *classified* defect rather than any absent identity.
    # `CITED_ARTIFACTS_RESOLVE` deliberately does not flag a well-formed identity simply missing
    # from the baseline — that is proposed-new, which every CR is full of — so a fabricated name
    # like `CS_MUTABLE_JSON_STORE_V0` is silently admitted and proves nothing. What it does flag is
    # a right-code/wrong-namespace citation, which is what these use.
    ("P6", WF["P6"],
     "58_p6_inadmissible_uncited_rows.json", "INADMISSIBLE", [
         "CITATION_ORDINAL_UNRESOLVED",
         "EXISTING_ARTIFACT_UNRESOLVED",
         "PPS_ACTION_IDENTITY_UNRESOLVED",
         "ROW_WITHOUT_SOURCE_FINDING",
         "SOURCE_FINDING_UNRESOLVED",
     ], RULES["P6"], 4),
    ("P6", WF["P6"],
     "59_p6_inadmissible_hollow_registers.json", "INADMISSIBLE", [
         # `UNRESOLVED` in a Disposition cell is two defects at once: it is not in the vocabulary,
         # and it hedges a decision the phase exists to record. Both rules fire on the one cell.
         "CELL_NOT_IN_VOCABULARY",
         "CELL_NOT_IN_VOCABULARY",
         "DEPENDENCY_SATISFIED_WITHOUT_ARTIFACT",
         "REGISTER_CELL_UNRESOLVED",
         "REGISTER_EMPTY",
         "SATISFIED_WITHOUT_EXISTING_ARTIFACT",
     ], RULES["P6"], 3),
    ("P6", WF["P6"],
     "60_p6_inadmissible_malformed_document.json", "INADMISSIBLE", [
         "HEADER_FIELD_MISSING",
         "HEADER_FIELD_MISMATCH",
         "REGISTER_MISSING",
         "STORAGE_CODE_IN_PLACEMENT",
     ] + ["REGISTER_COLUMN_MISSING"] * 11, RULES["P6"], 3),
    ("P6", WF["P6"],
     "61_p6_inadmissible_unowned_subdomain.json", "INADMISSIBLE", [
         "TOUCHED_SUBDOMAIN_UNOWNED",
     ], RULES["P6"], 4),
    # P7 assigns binding identity, and one of its rules runs backwards: every other grounded phase
    # is wrong when a citation fails to resolve, this one is wrong when a NEW code *does*. A
    # collision is not a new artifact but a silent redefinition of an old one.
    # Judged against the design-time baseline — the composition CR-1 was designed against, not the
    # one containing its own output. Getting this wrong makes every assigned identity collide.
    ("P7", WF["P7"],
     "22_p7_admissible_catalog_register.json", "ADMISSIBLE", [], RULES["P7"], 5, "design"),
    ("P7", WF["P7"],
     "23_p7_inadmissible_catalog_register.json", "INADMISSIBLE", [
         # The fixture renames an authored artifact, which leaves the renamed one traceable to no
         # provisional code — the reverse direction of the P5 closure, firing on the same edit.
         "AUTHORED_ARTIFACT_WITHOUT_INTENT",
         "BINDING_STEP_OWNER_UNDECLARED",
         "BINDING_STEP_OWNER_UNDECLARED",
         "BINDING_STEP_OWNER_UNDECLARED",
         "BINDING_STEP_OWNER_UNDECLARED",
         "BINDING_STEP_OWNER_UNDECLARED",
         "COMPOSITION_CC_UNDECLARED",
         "COMPOSITION_CC_UNDECLARED",
         "CONTRACT_WITHOUT_COMPOSITION",
         "INTERFACE_ARTIFACT_UNDECLARED",
         "INTERFACE_ARTIFACT_UNDECLARED",
         "NEW_CODE_MALFORMED",
         "PROVISIONAL_CODE_NEVER_BOUND",
         "STORE_WITHOUT_PROPOSED_PATH",
         "TOPOLOGY_NODE_UNDECLARED",
         "TOPOLOGY_NODE_UNDECLARED",
         # The misspelled node leaves the route into the correct spelling with nowhere to go.
         "TOPOLOGY_ROUTE_UNRESOLVED",
     ], RULES["P7"], 4, "design"),
    # P8 is the only phase judged on row *order*. Every rule before it decides a row on its own; a
    # mandate can be made entirely of well-formed rows and still be unexecutable, because a dropped
    # step and a prerequisite scheduled too late exist between rows rather than in any one of them.
    # CR-1's authored mandate, judged against its own design. It does not reconcile: one artifact
    # P7 declared is scheduled nowhere, which every other P8 rule passes because the step sequence
    # stays contiguous over a hole that was never a step. Kept as authored — the finding is the
    # evidence, and rewriting the dossier to make the suite green would delete it.
    # P7 is the biggest rule set in the pipeline — 80 rules over 21 registers — and its defects are
    # binding defects: a step that names an operation nothing publishes, a field bound to a source no
    # node produces, an artifact inventoried on the wrong side of the new/existing line.
    ("P7", WF["P7"],
     "77_p7_inadmissible_malformed_document.json", "INADMISSIBLE", [
         "CELL_NOT_IN_VOCABULARY",
         "HEADER_FIELD_MISSING",
         "HEADER_FIELD_MISMATCH",
         "REGISTER_CELL_UNRESOLVED",
         "REGISTER_EMPTY",
         "REGISTER_MISSING",
     ], RULES["P7"], 3),
    ("P7", WF["P7"],
     "78_p7_inadmissible_uncomposed_steps.json", "INADMISSIBLE", [
         # An em-dash in `Interpreted By` declares that the step's branches are the operation's
         # own statuses. Routing on one the operation cannot answer, with the em-dash still
         # there, is exactly what the observation pair exists to catch.
         "INTERPRETATION_TRANSFORM_CANNOT_REFUSE",
         "INTERPRETATION_TRANSFORM_CANNOT_REFUSE",
         "INTERPRETATION_TRANSFORM_UNDECLARED",
         "OBSERVATION_WITHOUT_INTERPRETATION",
         "OBSERVATION_WITHOUT_SEMANTIC_STATUS",
         "STEP_BINDING_NOT_IN_INTERFACE",
         "STEP_CONSUMES_NOTHING_FROM_OPERATION_WITH_INPUT",
         "STEP_CONSUMES_UNDECLARED_INPUT",
         "STEP_INPUT_UNBOUND",
         "STEP_INTERFACE_NOT_CONFORMANT",
         "STEP_INTERFACE_NOT_CONFORMANT",
         "STEP_NAMES_UNPUBLISHED_OPERATION",
         "STORE_UNGROUNDED_IN_CAPABILITY",
     ], RULES["P7"], 4),
    ("P7", WF["P7"],
     "79_p7_inadmissible_unbuildable_artifacts.json", "INADMISSIBLE", [
         "ARTIFACT_HAS_TWO_GENERATORS",
         "GENERATED_ARTIFACT_UNDECLARED",
         "GENERATOR_SOURCES_UNNAMED",
         "GENERATOR_UNNAMED",
         "GENERATOR_UNREACHABLE",
         "IMPLEMENTATION_CALLABLE_UNCONVENTIONAL",
         "IMPLEMENTATION_REFUSAL_UNKNOWN",
         "IMPLEMENTATION_WITHOUT_REFUSAL",
         "VOCABULARY_WITHOUT_EXTENDS",
     ], RULES["P7"], 4),
    ("P7", WF["P7"],
     "80_p7_inadmissible_unbound_fields.json", "INADMISSIBLE", [
         # BINDING_SOURCE_UNREACHABLE only sees a binding whose Owner is a workflow — a
         # contract-owned step binding is skipped by construction, so the unreachable source
         # has to be planted on a WF-owned row to reach it at all.
         "BINDING_READS_UNPUBLISHED_FIELD",
         "BINDING_SOURCE_UNREACHABLE",
         "BINDING_WITHOUT_SOURCE",
         "CONTRACT_OUTPUT_UNPRODUCED",
     ], RULES["P7"], 4),
    ("P7", WF["P7"],
     "81_p7_inadmissible_unbound_topology.json", "INADMISSIBLE", [
         "RB_BINDS_UNDECLARED_WORKFLOW",
         "RB_CODE_UNDECLARED",
         "TOPOLOGY_ROUTE_UNRESOLVED",
         "TOPOLOGY_WORKFLOW_UNDECLARED",
         "WORKFLOW_WITHOUT_RUNTIME_BINDING",
     ], RULES["P7"], 4),
    ("P7", WF["P7"],
     "82_p7_inadmissible_miscounted_inventory.json", "INADMISSIBLE", [
         # The added EV row is one edit with four consequences: the moment is named in a tense
         # that is not past, no intent admits it, and three composed steps now name a code the
         # design never assigned.
         "AMENDED_ARTIFACT_NOT_AUTHORABLE",
         "AUTHORED_ARTIFACT_WITHOUT_INTENT",
         "COMPOSITION_STEP_UNDECLARED",
         "COMPOSITION_STEP_UNDECLARED",
         "COMPOSITION_STEP_UNDECLARED",
         "EVENT_CODE_NOT_PAST_PARTICIPLE",
         "EXISTING_INVENTORY_UNRESOLVED",
         "REPLACED_ARTIFACT_NOT_AUTHORABLE",
         "REPLACED_ARTIFACT_WITHOUT_SUCCESSOR",
     ], RULES["P7"], 4),
    ("P7", WF["P7"],
     "83_p7_inadmissible_uncited_rows.json", "INADMISSIBLE", [
         "CITATION_ORDINAL_UNRESOLVED",
         "DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
         "ROW_WITHOUT_SOURCE_FINDING",
         "SOURCE_FINDING_UNRESOLVED",
     ], RULES["P7"], 4),
    # Reach. A subdomain owns what it holds, and the three rules that say so had never been reached
    # because no dossier in the workspace populates `declared_reach`. They are document-local after
    # all — what was missing was the right *kind* of identifier: `Consults` names a runtime binding,
    # not a store, and `Store` names a store by its bare name, not its key.
    ("P7", WF["P7"],
     "84_p7_inadmissible_undeclared_reach.json", "INADMISSIBLE", [
         "CROSS_SUBDOMAIN_WRITE",
         "DECLARED_REACH_UNUSED",
         # Routing a catalog workflow into another subdomain's contract also hands that contract
         # nothing: three of its declared inputs arrive unbound. One edit, two boundaries crossed.
         "NODE_INPUT_UNBOUND",
         "NODE_INPUT_UNBOUND",
         "NODE_INPUT_UNBOUND",
         "TOPOLOGY_NODE_UNDECLARED",
     ], RULES["P7"], 4),
    ("P8", WF["P8"],
     "24_p8_admissible_catalog_mandate.json", "ADMISSIBLE", [], RULES["P8"], 5, "design"),
    ("P8", WF["P8"],
     "25_p8_inadmissible_catalog_mandate.json", "INADMISSIBLE", [
         "BUILD_STEPS_NOT_CONTIGUOUS",
         "DEPENDENCY_SCHEDULED_LATER",
         "DESIGNED_ARTIFACT_NOT_SCHEDULED",
     ], RULES["P8"], 4, "design"),
    # P8's remaining fifteen. The mandate is the last gate before authoring, so its defects are
    # schedule defects: an order that cannot be built, an entry that says nothing actionable, and a
    # document mis-shaped.
    ("P8", WF["P8"],
     "73_p8_inadmissible_unbuildable_schedule.json", "INADMISSIBLE", [
         "BUILD_CODE_ALREADY_EXISTS",
         "BUILD_CODE_MALFORMED",
         "CRITICAL_PATH_NOT_CONTIGUOUS",
         "CRITICAL_PATH_NOT_CONTIGUOUS",
         "CRITICAL_PATH_NOT_CONTIGUOUS",
         "CRITICAL_PATH_NOT_IN_BUILD_ORDER",
         "DESIGNED_ARTIFACT_NOT_SCHEDULED",
         "DESIGNED_ARTIFACT_NOT_SCHEDULED",
         "SCHEDULED_ARTIFACT_NOT_DESIGNED",
         "SCHEDULED_ARTIFACT_NOT_DESIGNED",
         "SCHEDULED_ARTIFACT_UNPLACED",
         "SCHEDULED_ARTIFACT_UNPLACED",
     ], RULES["P8"], 4, "design"),
    ("P8", WF["P8"],
     "74_p8_inadmissible_hollow_mandate.json", "INADMISSIBLE", [
         "CAPABILITY_WITHOUT_PURPOSE",
         "CELL_NOT_IN_VOCABULARY",
         "INTENT_WITHOUT_WORKFLOW",
         "REGISTER_CELL_UNRESOLVED",
         "REGISTER_EMPTY",
     ], RULES["P8"], 3, "design"),
    ("P8", WF["P8"],
     "75_p8_inadmissible_malformed_document.json", "INADMISSIBLE", [
         "HEADER_FIELD_MISSING",
         "HEADER_FIELD_MISMATCH",
         "REGISTER_MISSING",
     ] + ["REGISTER_COLUMN_MISSING"] * 4, RULES["P8"], 3, "design"),
    # Cut from cr_02 rather than cr_01, because cr_01's P7 declares no EXTEND row and the rule is
    # gated on one — the artifact this mandate forgets to place has to be an artifact the design
    # actually amends. It is also the only P8 case that is not book_library_mgmt cr_01.
    ("P8", WF["P8"],
     "76_p8_inadmissible_unplaced_amendment.json", "INADMISSIBLE", [
         # An amended artifact is not a scheduled one — the mandate never orders it built — so only
         # the amendment rule sees it missing. That is the distinction the two rules exist to draw.
         "AMENDED_ARTIFACT_UNPLACED",
     ], RULES["P8"], 4, "design"),
    # The first two cases whose defect is in neither document. Each register is correct read alone
    # — the P2 resolves every belief it lists, the P3 re-verifies every item it names — and the
    # pipeline is wrong anyway, because a commitment was lost between them. Nothing in the suite
    # before these could fail for a reason that lives in a handoff.
    ("P2", WF["P2"],
     "26_p2_inadmissible_dropped_belief.json", "INADMISSIBLE", [
         "BELIEF_NOT_CARRIED_FROM_P1",
     ], RULES["P2"], 4),
    ("P3", WF["P3"],
     "27_p3_inadmissible_restated_result.json", "INADMISSIBLE", [
         "BELIEF_RESULT_RESTATED_FROM_P2",
     ], RULES["P3"], 4),
    # Reconciliation, both directions. A mandate scheduling everything the design declared is the
    # corpus's only fully reconciled one; the second schedules an identity no phase ever designed,
    # which reads as an ordinary well-formed row.
    ("P8", WF["P8"],
     "29_p8_inadmissible_undesigned_artifact.json", "INADMISSIBLE", [
         "SCHEDULED_ARTIFACT_NOT_DESIGNED",
     ], RULES["P8"], 4, "design"),
    # The two edges at the ends of the pipeline. Neither defect is visible in the document that
    # carries it: a change request missing an acceptance criterion is a well-formed change request,
    # and a design that never binds a provisional code is a complete design.
    ("P1", WF["P1"],
     "30_p1_inadmissible_dropped_criterion.json", "INADMISSIBLE", [
         "SEED_ROW_NOT_CARRIED",
     ], RULES["P1"], 4),
    ("P7", WF["P7"],
     "31_p7_inadmissible_unbound_code.json", "INADMISSIBLE", [
         "INTERFACE_ARTIFACT_UNDECLARED",
         "INTERFACE_ARTIFACT_UNDECLARED",
         "PROVISIONAL_CODE_NEVER_BOUND",
     ], RULES["P7"], 4, "design"),
    # The last two handoffs. P4's consolidation loses a decision P3 committed to; P7 drops a reused
    # artifact P6 declared a dependency satisfied by. The second fires two rules on one edit — an
    # artifact that is inventoried is also composed, so removing it is visible from both directions.
    # Only the cross-phase rule would fire for a dependency satisfied by an artifact the design
    # never referenced at all.
    ("P4", WF["P4"],
     "32_p4_inadmissible_dropped_decision.json", "INADMISSIBLE", [
         "AUTHORING_DECISION_NOT_CONSOLIDATED",
     ], RULES["P4"], 4),
    ("P7", WF["P7"],
     "33_p7_inadmissible_dropped_reuse.json", "INADMISSIBLE", [
         "COMPOSITION_STEP_UNDECLARED",
     ], RULES["P7"], 4, "design"),
    # The defect that reached execution: a source naming a place execution does not offer. Every
    # layer beneath read it as a literal and reported success — the design rules are the only place
    # it can be refused, because a binding determined to be a literal is still determined and
    # construction completeness stays at 100%.
    ("P7", WF["P7"],
     "36_p7_inadmissible_unrooted_source.json", "INADMISSIBLE", [
         "BINDING_SOURCE_UNROOTED",
         # A source that names no root is also not a form the runtime resolves, so both rules
         # fire. They are different statements: one says the reference escapes the declared
         # roots, the other that it is not a reference the runtime can follow at all.
         "BINDING_SOURCE_MALFORMED",
     ], RULES["P7"], 4, "design"),
    # A store whose name advertises a format its capability does not write. Nothing below the design
    # can catch it: the runtime opens the path it is handed and never reads the suffix.
    ("P7", WF["P7"],
     "37_p7_inadmissible_store_path.json", "INADMISSIBLE", [
         "STORE_PATH_FORMAT_MISMATCH",
     ], RULES["P7"], 4, "design"),
    # The other face of reconciliation: an artifact the design declared that the mandate schedules
    # nowhere. CR-1's own mandate carried this defect until the dossier was completed, so the
    # corpus has to carry it now — it is the one the P7↔P8 rule was built for.
    ("P8", WF["P8"],
     "35_p8_inadmissible_dropped_artifact.json", "INADMISSIBLE", [
         "DESIGNED_ARTIFACT_NOT_SCHEDULED",
     ], RULES["P8"], 4, "design"),
    ("P0", WF["P0"],
     "38_p0_inadmissible_blocking_clarification.json", "INADMISSIBLE",
     # The fixture's question is HUMAN-owned as well as blocking, so both closures fire. They are
     # different refusals: one says the author declared the answer necessary before the next phase,
     # the other says only the business can give it whatever the author declared.
     ["BLOCKING_CLARIFICATION_OUTSTANDING", "BUSINESS_CLARIFICATION_OUTSTANDING"], RULES["P0"], 3, "design"),
    ("P6", WF["P6"],
     "34_p6_inadmissible_unplaced_scope.json", "INADMISSIBLE", [
         "IN_SCOPE_CAPABILITY_UNPLACED",
         "OUTCOME_CAPABILITY_UNPLACED",
     ], RULES["P6"], 4),
    # The five probes. Each new rule is authored against a corpus in which no document stated a
    # discharge, so each would report clean on its first run while checking nothing. One probe per
    # rule, each built to fail it, is what turns a clean report into evidence.
    ("P7", WF["P7"],
     "39_p7_inadmissible_refusal_unaccounted.json", "INADMISSIBLE", [
         "REFUSAL_UNACCOUNTED",
     ], RULES["P7"], 4, "design"),
    ("P7", WF["P7"],
     "40_p7_inadmissible_discharge_undeclared.json", "INADMISSIBLE", [
         "DISCHARGE_UNDECLARED_REFUSAL",
     ], RULES["P7"], 4, "design"),
    ("P7", WF["P7"],
     "41_p7_inadmissible_deferral_undeclared.json", "INADMISSIBLE", [
         "DEFERRAL_UNDECLARED_REFUSAL",
     ], RULES["P7"], 4, "design"),
    ("P7", WF["P7"],
     "42_p7_inadmissible_discharge_ungrounded.json", "INADMISSIBLE", [
         "DISCHARGE_NOT_IN_TOPOLOGY",
     ], RULES["P7"], 4, "design"),
    # Every cell of the row is accurate and the act completes anyway — the defect no rule reading
    # the register alone can see.
    ("P7", WF["P7"],
     "43_p7_inadmissible_discharge_completes.json", "INADMISSIBLE", [
         "DISCHARGE_DOES_NOT_REFUSE",
     ], RULES["P7"], 4, "design"),
    # The emission guard. Nothing read an `emit.` property before it: six acts announced eight
    # moments and no rule looked at one. Three probes, because the guard makes three claims — the
    # ending exists, it completes, and the moment is declared.
    ("P7", WF["P7"],
     "44_p7_inadmissible_emission_unknown_ending.json", "INADMISSIBLE", [
         "EMISSION_NOT_FROM_COMPLETING_ENDING",
     ], RULES["P7"], 4, "design"),
    # The ending exists and refuses. The moment would state something that did not happen.
    ("P7", WF["P7"],
     "45_p7_inadmissible_emission_from_refusal.json", "INADMISSIBLE", [
         "EMISSION_NOT_FROM_COMPLETING_ENDING",
     ], RULES["P7"], 4, "design"),
    ("P7", WF["P7"],
     "46_p7_inadmissible_emission_undeclared_event.json", "INADMISSIBLE", [
         "EMITTED_EVENT_UNDECLARED",
     ], RULES["P7"], 4, "design"),
    # The governance-surface discharge. A refusal carried out by a rule of the pipeline rather than
    # by a step of the domain's own acts — cr_03's, and the third of the three forms.
    ("P7", WF["P7"],
     "47_p7_inadmissible_governance_undeclared_refusal.json", "INADMISSIBLE", [
         "GOVERNANCE_DISCHARGE_UNDECLARED_REFUSAL",
     ], RULES["P7"], 4, "design"),
    ("P7", WF["P7"],
     "48_p7_inadmissible_governing_rule_unnamed.json", "INADMISSIBLE", [
         "GOVERNING_RULE_UNNAMED",
     ], RULES["P7"], 4, "design"),
    # A stage number where a phase belongs — the collision the phase column exists to prevent.
    ("P7", WF["P7"],
     "49_p7_inadmissible_governing_rule_phase.json", "INADMISSIBLE", [
         "GOVERNING_RULE_PHASE_MALFORMED",
     ], RULES["P7"], 4, "design"),
    # Grounding the citation. A register naming a rule nobody resolves documents intent and
    # enforces nothing, which is the failure the refusal work exists to end.
    ("P7", WF["P7"],
     "50_p7_inadmissible_governing_rule_not_in_force.json", "INADMISSIBLE", [
         "GOVERNING_RULE_NOT_IN_FORCE",
     ], RULES["P7"], 4, "design"),
    # Right rule, wrong phase — 15 rule identifiers are declared by more than one phase, so an
    # identifier without its phase names nine rules and resolves against whichever came first.
    ("P7", WF["P7"],
     "51_p7_inadmissible_governing_rule_wrong_phase.json", "INADMISSIBLE", [
         "GOVERNING_RULE_NOT_IN_FORCE",
     ], RULES["P7"], 4, "design"),
    # Issue 23, both ways round. No document in the corpus had ever populated the deferral register,
    # so a rule requiring its owner would have reported clean while checking nothing — and nothing
    # would have shown that a well-formed deferral is accepted either.
    ("P7", WF["P7"],
     "52_p7_admissible_deferral_owned.json", "ADMISSIBLE", [], RULES["P7"], 5, "design"),
    ("P7", WF["P7"],
     "53_p7_inadmissible_deferral_unowned.json", "INADMISSIBLE", [
         "DEFERRAL_OWNER_UNNAMED",
     ], RULES["P7"], 4, "design"),
]


PHASE_TEMPLATE = {"P0": "p0", "P1": "p1", "P2": "p2", "P3": "p3", "P4": "p4", "P5": "p5", "P6": "p6", "P7": "p7", "P8": "p8"}


def merit_of(surface: dict, payload: dict, phase: str, policy: dict) -> Merit:
    """The figure of merit for a judged document.

    Derived here rather than returned by the workflow: admissibility is what the composition
    decides, and quality is a read over the result. A runtime that scored its own output would be
    asserting an opinion the snapshot never declared.
    """
    from transformation.design.oracle import Verdict, Finding
    from transformation.design.read import parse_text

    verdict = Verdict(
        verdict=surface.get("verdict"),
        seed="",
        rules_evaluated=surface.get("rules_evaluated") or 0,
        findings=[
            Finding(code=f["code"], rule=f["rule"], locator=f["locator"],
                    detail=f.get("detail", ""), intent=f.get("intent", ""))
            for f in (surface.get("findings") or [])
        ],
    )
    text = payload.get("register_text") or payload.get("seed_text") or ""
    from transformation.design.evaluate import ParsedDocument
    header, sections, registers = parse_text(text)
    doc = ParsedDocument(header=header, sections=sections, registers=registers, raw=text, path="")
    return rate(verdict, doc, policy)


# A CR's dossier is judged against the composition it was DESIGNED against, never against one that
# already contains its own output. CR-1's design assigns 23 identities; once those are built, every
# one of them collides — correctly, and fatally for any attempt to re-validate the design.
#
# The baseline does not need archiving. Snapshots are dispensable and reassembled at will, so the
# design-time composition is *reproduced* on demand from the same compiled domains minus the one
# the CR authored — cheaper than storing it, and it cannot go stale *provided the reproduction is
# actually re-run*. Caching it under /tmp keyed on nothing is what makes it go stale: a P8 rule was
# added and compiled, and three cases were judged against a baseline still carrying the previous
# sealed rule set, reporting "30 rules evaluated" against 32 declared. Reproduction is now
# conditional on the sources being no newer than the cache.
# Build output, beside the rest: `regression.sh --all` clears `traces/` before it rebuilds, so the
# reproduction never outlives the compiled domains it was assembled from.
DESIGN_BASELINE = WORKSPACE / "traces" / "design_baseline"

# The business domain CR-1 cites as its neighbour, frozen at the revision CR-1 was designed against.
# The corpus cites that domain's artifacts as they were then; read from the live domain, every
# delivery to it would reach into these fixtures. It is built once from git, beside the baseline.
FROZEN_DOMAIN, FROZEN_REVISION = "ai_governance", "36bc62a"
FROZEN = WORKSPACE / "traces" / "design_baseline_sources" / f"{FROZEN_DOMAIN}_{FROZEN_REVISION}"

DESIGN_BASELINE_ROOTS = [
    WORKSPACE / "software_governance",
    WORKSPACE / "conformance_workloads" / "workloads" / "collatz",
    FROZEN / FROZEN_DOMAIN,
    WORKSPACE / "snapshot_inspector",
    REPO,
]


def _frozen_domain() -> None:
    """Build the frozen neighbour from git, once: its source at the revision, compiled against the
    platform with its own transforms ahead of the working tree's."""
    import os
    import shutil
    import subprocess

    if (FROZEN / FROZEN_DOMAIN / "snapshot" / "compiled").is_dir():
        return
    shutil.rmtree(FROZEN, ignore_errors=True)
    FROZEN.mkdir(parents=True)
    archive = subprocess.run(["git", "-C", str(WORKSPACE / "business_domains"), "archive", FROZEN_REVISION,
                              FROZEN_DOMAIN], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", str(FROZEN)], input=archive, check=True)
    shutil.rmtree(FROZEN / FROZEN_DOMAIN / "snapshot" / "compiled", ignore_errors=True)
    env = {**os.environ, "PGC_IMPL_ROOTS": ":".join(
        str(r) for r in (FROZEN, WORKSPACE / "software_governance", WORKSPACE / "conformance_workloads",
                         WORKSPACE / "business_domains"))}
    done = subprocess.run([str(WORKSPACE / "protocol_compiler" / "compile_domain.sh"), str(FROZEN / FROZEN_DOMAIN)],
                          env=env, capture_output=True, text=True)
    if done.returncode:
        shutil.rmtree(FROZEN, ignore_errors=True)
        raise SystemExit(f"design baseline: {FROZEN_DOMAIN} at {FROZEN_REVISION} did not compile\n"
                         + "\n".join((done.stdout + done.stderr).splitlines()[-20:]))


def _baseline_is_stale() -> bool:
    """Whether any source domain has been recompiled since the baseline was reproduced.

    A cached snapshot is only a reproduction while its inputs have not moved. Checking `is_file()`
    alone answers "was this ever built", which is a different question and the one that let a stale
    composition judge a freshly compiled rule set.
    """
    _frozen_domain()
    manifest = DESIGN_BASELINE / "manifest.json"
    if not manifest.is_file():
        return True
    built_at = manifest.stat().st_mtime
    for root in DESIGN_BASELINE_ROOTS:
        compiled = root / "snapshot" / "compiled"
        if any(f.stat().st_mtime > built_at for f in compiled.rglob("*.json")):
            return True
    return False


def design_baseline() -> str:
    """The composition CR-1 was designed against, reproduced whenever its sources have moved."""
    if _baseline_is_stale():
        import os
        import shutil
        import subprocess

        # Reassembling over a populated directory would leave the previous reproduction's artifacts
        # behind, which is the same staleness one level down.
        shutil.rmtree(DESIGN_BASELINE, ignore_errors=True)
        roots = ":".join(str(r / "snapshot" / "compiled") for r in DESIGN_BASELINE_ROOTS)
        # PGC_SNAPSHOT_PROFILE is named, not defaulted: a snapshot must name the profile it
        # claims (1b §11), and assemble.sh has no default because none is privileged (6a §11).
        env = {**os.environ,
               "PGC_SOURCE_ROOTS": roots,
               "PGC_SNAPSHOT_OUT": str(DESIGN_BASELINE),
               "PGC_SNAPSHOT_PROFILE": "GOVERNANCE_SURFACE_PROFILE_V0"}
        # The assembler's own words are the diagnosis: a bare exit status hid why it refused.
        done = subprocess.run([str(WORKSPACE / "snapshot_assembler" / "assemble.sh")],
                              env=env, capture_output=True, text=True)
        if done.returncode:
            raise SystemExit(f"design baseline: assembly refused (exit {done.returncode})\n"
                             + "\n".join((done.stdout + done.stderr).splitlines()[-20:]))
    return str(DESIGN_BASELINE)


def main() -> int:
    # Before any case runs: a rule that cannot run would make every expected finding count below a
    # statement about a rule set that was never fully applied.
    assert_consistent()
    # The reproduced baseline, not the workspace snapshot on disk. A phase's rule set travels *in*
    # the workflow the runtime executes, so the composition a case runs against decides which rules
    # it is judged by — and the assembled snapshot at the workspace root is reassembled by hand.
    # It had fallen one rule behind, so P5 was judged by 78 rules while it declared 79, and the case
    # reported a confident verdict over a rule set that was never applied. `design_baseline()`
    # rebuilds itself whenever a source domain is recompiled, which makes that impossible. An
    # explicit root is still honoured, for judging a document against a composition on purpose.
    snapshot_root = sys.argv[1] if len(sys.argv) > 1 else design_baseline()
    data_root = str(REPO.parent / "data" / "transformation")
    # The deduction weights are governance, read from the composition like the rule sets.
    policy = load_policy(snapshot_root)

    phases = sorted({c[0] for c in CASES})
    print(f"e2e phases — {len(CASES)} case(s) across {len(phases)}: {', '.join(phases)}")
    print(f"  snapshot {snapshot_root}\n")

    failures = 0
    for case in CASES:
        phase, wf, payload_file, want_verdict, want_rule_ids, want_rules, want_rating = case[:7]
        # A case may name the composition it is judged against; most use the live snapshot.
        case_snapshot = design_baseline() if len(case) > 7 and case[7] == "design" else snapshot_root
        path = PAYLOADS / payload_file
        if not path.is_file():
            print(f"  MISSING  {phase}  {payload_file} — run scripts/testbed/build_payloads.py")
            failures += 1
            continue

        payload = json.loads(path.read_text(encoding="utf-8"))
        result = api.run_workflow(
            wf_fqdn=wf, payload=payload, snapshot_root=case_snapshot, data_root=data_root
        )

        verdict = result.surface.get("verdict")
        fired = sorted(f["code"] for f in (result.surface.get("findings") or []))
        expected = sorted(want_rule_ids)
        rules = result.surface.get("rules_evaluated")

        # A workflow that judges a document correctly still completes successfully: an inadmissible
        # verdict is a governed outcome, not an execution failure. Status VIOLATION would mean the
        # phase itself is broken.
        problems = []
        if result.status != "SUCCESS":
            problems.append(f"status {result.status}")
        if verdict != want_verdict:
            problems.append(f"verdict {verdict} != {want_verdict}")
        if fired != expected:
            # Compared as multisets, not as sets. Membership tests alone report nothing when a rule
            # fires twice against one expected occurrence — the lists differ, `missing` and
            # `unexpected` both come back empty, and the case prints OK over a real change in what
            # the phase found. That is how a second SEED_ROW_NOT_CARRIED went unreported here.
            fired_counts, expected_counts = Counter(fired), Counter(expected)
            missing = sorted((expected_counts - fired_counts).elements())
            unexpected = sorted((fired_counts - expected_counts).elements())
            if missing:
                problems.append(f"rules that did not fire: {missing}")
            if unexpected:
                problems.append(f"rules that fired unexpectedly: {unexpected}")
        if rules != want_rules:
            problems.append(f"rules evaluated {rules} != {want_rules}")

        # The runtime returns the verdict, not the rating: the figure of merit is a read over the
        # judged document, and re-deriving it here keeps the runtime free of a quality opinion.
        merit = merit_of(result.surface, payload, phase, policy)
        if merit.rating != want_rating:
            problems.append(f"figure of merit {merit.rating}/5 != {want_rating}/5")

        # PASS/FAIL, not the verdict. ADMISSIBLE and INADMISSIBLE are both correct outcomes — half
        # these cases exist to be refused — so printing the verdict in the result column invited
        # reading a governed refusal as a broken test. What this line reports is whether the case
        # matched what it declared, and the verdict appears below only when it did not.
        print(
            f"  {'PASS' if not problems else 'FAIL'}  {phase}  {payload_file:<40} "
            f"{len(fired):>2} finding(s)  {rules} rules  "
            f"{merit.stars} {merit.rating}/{merit.maximum}"
        )
        if problems:
            failures += 1
            print(f"          verdict {verdict}; {'; '.join(problems)}")

    print()
    if failures:
        print(f"E2E FAILED — {failures} of {len(CASES)} case(s) did not match")
        return 1
    print(f"E2E PASSED — {len(CASES)} case(s), every phase executed through the runtime")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
