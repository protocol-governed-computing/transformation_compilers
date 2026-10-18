"""Regenerate the inadmissible corpus fixtures from CR-1's dossier.

A fixture is an admissible document with a named defect introduced. Hand-authoring one freezes a
copy of the dossier at the moment it was cut, and the copy rots: amending P7 left every P7 fixture
missing four registers, and the P8 order fixture had been written in a `catalog::` namespace the
dossier stopped using long before.

So a fixture is declared as *the defect*, not as a file. The document is the current dossier, and
the transformation states what is wrong with it, as edits to the rows of its Machine block — which is also the only readable form, because a
reader wants to know what a fixture proves, not to diff two hundred lines to find out.

Every negative catalog fixture is derived this way. The five that were still hand-authored went stale
the moment the dossier was replaced: a P4 fixture judged against a new P3 reported twenty-six
unconsolidated decisions, and a P1 fixture judged against a new seed reported a hundred and forty-two
findings. A derived fixture cannot drift from the dossier it is cut from.

Run:  python scripts/testbed/build_fixtures.py
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

import machine

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
# Fixtures maintained against the current rule set. See `fixtures/README.md`.
CR_01 = REPO / "scripts/testbed/fixtures/catalog/cr_01_catalog"
MACHINE = re.compile(r"## Machine\s*\n+```yaml\n(.*?)\n```", re.S)
CORPUS = REPO / "scripts/testbed"

P0 = CR_01 / "p0_seed_book_library_mgmt_catalog_v0.md"
P1 = CR_01 / "p1_change_request_book_library_mgmt_catalog_v0.md"
P2 = CR_01 / "p2_domain_model_book_library_mgmt_catalog_v0.md"
P3 = CR_01 / "p3_analysis_loop_book_library_mgmt_catalog_v0.md"
P4 = CR_01 / "p4_business_model_book_library_mgmt_catalog_v0.md"
P6 = CR_01 / "p6_governance_intent_book_library_mgmt_catalog_v0.md"
P7 = CR_01 / "p7_design_intent_book_library_mgmt_catalog_v0.md"
P8 = CR_01 / "p8_authoring_mandate_book_library_mgmt_catalog_v0.md"


class Rows:
    """A document's registers, edited row by row. Each edit names the row it changes by what the row
    says, and refuses unless exactly one row says it — a fixture whose anchor has gone stale fails
    here rather than quietly introducing no defect."""

    def __init__(self, text: str):
        self.text = text
        self.block = yaml.safe_load(MACHINE.search(text).group(1))

    def find(self, register: str, **says) -> int:
        rows = self.block["registers"][register] or []
        found = [i for i, row in enumerate(rows) if all(row.get(k) == v for k, v in says.items())]
        if len(found) != 1:
            raise SystemExit(f"expected exactly one {register} row saying {says}, found {len(found)}")
        return found[0]

    def drop(self, register: str, **says) -> "Rows":
        del self.block["registers"][register][self.find(register, **says)]
        return self

    def set(self, register: str, says: dict, **changes) -> "Rows":
        self.block["registers"][register][self.find(register, **says)].update(changes)
        return self

    def after(self, register: str, says: dict, row: dict) -> "Rows":
        self.block["registers"][register].insert(self.find(register, **says) + 1, row)
        return self

    def add(self, register: str, row: dict) -> "Rows":
        self.block["registers"][register] = [*(self.block["registers"][register] or []), row]
        return self

    def __str__(self) -> str:
        body = MACHINE.search(self.text)
        return self.text[:body.start(1)] + machine.dump(self.block).rstrip("\n") + self.text[body.end(1):]


NS = "book_library_mgmt::"


def p0_blocking_clarification(t: Rows) -> Rows:
    """A question the seed asks, marked blocking, and handed on unanswered.

    CR-1's author answered every clarification, so the register is empty and the defect has to be
    introduced rather than removed. It is the one seed defect that cannot be seen by reading the
    register alone: the row is well-formed, in vocabulary, and says the next phase must not proceed.
    """
    return t.add("clarification_requests", {
        "question": "Does a physical copy belong to the book or to the library branch holding it?",
        "why_needed": "Registration cannot be designed until a copy's owner is settled.",
        "blocking": "YES", "owner": "HUMAN"})


def p1_dropped_criterion(t: Rows) -> Rows:
    """An acceptance criterion the seed declared and the change request drops."""
    return t.drop("acceptance_criteria",
                  criterion="Every catalog operation performed can be traced and audited afterwards.")


def p2_grounding(t: Rows) -> Rows:
    """A misspelled identity, a right-code/wrong-namespace one, and design in a business cell."""
    return (t.set("pps_baseline_fqdns", {"fqdn": "capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0"},
                  fqdn="capability_transforms::CT_PURE_ASEMBLE_RECORD_V0")
             .set("pps_baseline_fqdns", {"capability": "Record shape validation"},
                  fqdn="ai_governance::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0")
             .set("gaps", {"gap": "Nothing in the composition holds a book record or a copy record."},
                  gap="Nothing in the composition holds a book record, so CC_REGISTER_BOOK_V0 must be authored."))


def p2_dropped_belief(t: Rows) -> Rows:
    """A Stage-1 belief the domain model never verifies."""
    return t.drop("belief_verification",
                  belief="No capability in the current composition manages a library catalog.")


def p3_ineligible_reuse(t: Rows) -> Rows:
    """Candidates offered to a business change request from domains that permit no reuse."""
    return t.set("authoring_decisions",
                 {"alternatives_checked": "capability_side_effects::CS_REGISTRY_V0 satisfies it as-is.",
                  "source_finding": {"phase": "p3", "register": "analysis_findings", "row": 2}},
                 alternatives_checked="transformation::CT_PURE_PARSE_REGISTERS_V1 and "
                                      "workload::EV_CONJECTURE_EVALUATED_V0 were offered as candidates.")


def p3_restated_result(t: Rows) -> Rows:
    """A re-verification that cites one belief and addresses another."""
    return t.set("verification_results", {"origin": {"phase": "p2", "register": "belief_verification", "row": 1}},
                 item="The catalog has no records of its own to verify.")


def p4_consolidation(t: Rows) -> Rows:
    """A dangling gap reference, an unowned gap, a scope row pointing nowhere, a bad dependency."""
    return (t.set("dependency_graph", {"from": "catalog", "to": "capability_side_effects::CS_MUTABLE_JSON_V0"},
                  to="capability_side_effects::CS_MUTABLE_JSN_V0")
             .set("capability_graph", {"capability": "Retire a book record"}, gap_register_entry="GAP-99")
             .set("gap_register", {"gap_code": "GAP-01"}, owner_subdomain="")
             .set("authoring_scope", {"gap_register_ref": "GAP-13"}, gap_register_ref="GAP-98"))


def p4_dropped_decision(t: Rows) -> Rows:
    """A capability P3 committed that the consolidation never carries."""
    return t.drop("capability_graph",
                  capability="Retrieve a book's complete details with the copies the library holds")


def p6_placement(t: Rows) -> Rows:
    """A malformed dependency direction, and an in-scope capability placed under a code."""
    return (t.set("cross_subdomain_deps",
                  {"dependency": "Read whether a staff member is authorized to perform catalog operations"},
                  direction="staff and catalog both")
             .set("ownership", {"capability": "Search the catalog by subject or title"},
                  capability="CC_SEARCH_CATALOG_V0"))


def p6_unplaced_scope(t: Rows) -> Rows:
    """A capability P5 declared in scope that the placement phase never mentions."""
    return t.drop("ownership", capability="Retire a physical copy")


def p7_collision(t: Rows) -> Rows:
    """A code with no namespace, a node that resolves to nothing, and a store nobody can locate."""
    return (t.set("new_artifacts", {"code": f"{NS}CC_SEARCH_CATALOG_V0"}, code="CC_SEARCH_UNQUALIFIED_V0")
             .set("execution_topology", {"workflow": f"{NS}WF_REGISTER_BOOK_V0", "node": f"{NS}CC_REGISTER_BOOK_V0"},
                  node=f"{NS}CC_REGISTR_BOOK_V0")
             .set("structure_stores", {"store_name": "BOOKS"}, proposed_path=""))


def p7_unbound_code(t: Rows) -> Rows:
    """A provisional code P5 declared that this design never binds."""
    return t.drop("new_artifacts", code=f"{NS}AC_LIBRARY_STAFF_V0")


def p7_dropped_reuse(t: Rows) -> Rows:
    """A reused artifact dropped from the inventory, leaving a step bound to nothing.

    `SATISFIED_DEPENDENCY_NOT_INVENTORIED` cannot be proven against this dossier: it reads P6's
    `cross_subdomain_deps` Existing Artifact column, and this CR's only cross-subdomain dependency is
    the staff authorization GAP, which names no artifact by design. The rule is therefore uncovered —
    recorded rather than papered over with a fixture that does not exercise it.
    """
    return t.drop("existing_inventory", fqdn="capability_side_effects::CS_APPENDONLY_JSONL_V0")


def p7_unrooted_source(t: Rows) -> Rows:
    """A cross-step source with its root dropped — the defect that reached execution.

    `results.assemble_book_record.book_record` names a prior step's output; `assemble_book_record.
    book_record` names nothing, and every layer below reads it as a literal string. The renderer
    emitted it verbatim, the compiler accepted it, and the runtime handed the store its own binding
    text as the book. Nothing refused it: construction completeness was 100%, because a binding
    determined to be a literal is still determined.
    """
    return t.set("step_bindings", {"bound_to": "results.assemble_book_record.book_record"},
                 bound_to="assemble_book_record.book_record")


def p7_store_path_mismatch(t: Rows) -> Rows:
    """A registry store named for a format its capability does not write.

    `CS_REGISTRY_V0` writes JSON Lines; `.json` advertises a document that could never be parsed as
    one. It compiled, ran, and cost nothing until the first tool that tried to read the store.
    """
    return t.set("structure_stores", {"store_name": "BOOK_IDENTITY_REGISTRY"},
                 proposed_path="book_library_mgmt/catalog/book_identity_registry.json")


def p8_broken_order(t: Rows) -> Rows:
    """A dropped step, a prerequisite scheduled late, and a critical path through neither.

    A build_order row is found by the code it schedules, never by its step number: every artifact
    inserted into an earlier wave renumbers everything after it.
    """
    return (t.drop("build_order", code=f"{NS}CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0")
             .set("build_order", {"code": f"{NS}STRUCTURE_CATALOG_STORAGE_V0"},
                  depends_on=[f"{NS}RB_CATALOG_BINDINGS_V0"]))


def p8_undesigned_artifact(t: Rows) -> Rows:
    """A row the mandate invented, which no phase ever designed."""
    anchor = t.block["registers"]["build_order"][t.find("build_order", code=f"{NS}RB_CATALOG_BINDINGS_V0")]
    return (t.after("build_order", {"code": f"{NS}RB_CATALOG_BINDINGS_V0"},
                    {"wave": anchor["wave"], "step": str(int(anchor["step"]) + 1),
                     "code": f"{NS}CC_ARCHIVE_CATALOG_RECORD_V0", "action": "NEW", "subdomain": "catalog",
                     "depends_on": None})
             .after("field_declarations", {"code": f"{NS}RB_CATALOG_BINDINGS_V0"},
                    {"code": f"{NS}CC_ARCHIVE_CATALOG_RECORD_V0", "subdomain_field": "catalog"}))


def p8_dropped_artifact(t: Rows) -> Rows:
    """An artifact P7 declared that the mandate schedules nowhere.

    The last step is the one to drop: removing any earlier one would break step contiguity as well,
    and two findings for one edit would make the reconciliation rule hard to see. Removed from the
    field declarations too, so the placement rule does not fire in the reconciliation rule's place.
    """
    # A mandate that dropped an artifact would not go on routing its critical path through it —
    # leaving the path row fires CRITICAL_PATH_NOT_IN_BUILD_ORDER instead of the reconciliation rule.
    return (t.drop("build_order", code=f"{NS}RB_CATALOG_BINDINGS_V0")
             .drop("field_declarations", code=f"{NS}RB_CATALOG_BINDINGS_V0")
             .drop("critical_path", code=f"{NS}RB_CATALOG_BINDINGS_V0"))


FIXTURES = [
    ("corpus/inadmissible_p0_blocking_clarification.md", P0, p0_blocking_clarification),
    ("corpus_p1/inadmissible_p1_dropped_criterion.md", P1, p1_dropped_criterion),
    ("corpus_p2/inadmissible_p2_catalog_register.md", P2, p2_grounding),
    ("corpus_p2/inadmissible_p2_dropped_belief.md", P2, p2_dropped_belief),
    ("corpus_p3/inadmissible_p3_ineligible_reuse.md", P3, p3_ineligible_reuse),
    ("corpus_p3/inadmissible_p3_restated_result.md", P3, p3_restated_result),
    ("corpus_p4/inadmissible_p4_broken_consolidation.md", P4, p4_consolidation),
    ("corpus_p4/inadmissible_p4_dropped_decision.md", P4, p4_dropped_decision),
    ("corpus_p6/inadmissible_p6_unplaced.md", P6, p6_placement),
    ("corpus_p6/inadmissible_p6_unplaced_scope.md", P6, p6_unplaced_scope),
    ("corpus_p7/inadmissible_p7_collision.md", P7, p7_collision),
    ("corpus_p7/inadmissible_p7_unbound_code.md", P7, p7_unbound_code),
    ("corpus_p7/inadmissible_p7_dropped_reuse.md", P7, p7_dropped_reuse),
    ("corpus_p7/inadmissible_p7_unrooted_source.md", P7, p7_unrooted_source),
    ("corpus_p7/inadmissible_p7_store_path.md", P7, p7_store_path_mismatch),
    ("corpus_p8/inadmissible_p8_broken_order.md", P8, p8_broken_order),
    ("corpus_p8/inadmissible_p8_undesigned_artifact.md", P8, p8_undesigned_artifact),
    ("corpus_p8/inadmissible_p8_dropped_artifact.md", P8, p8_dropped_artifact),
]


def main() -> int:
    for name, source, transform in FIXTURES:
        (CORPUS / name).write_text(str(transform(Rows(source.read_text(encoding="utf-8")))), encoding="utf-8")
        print(f"  {name:<52} <- {source.name}  [{transform.__name__}]")
    print(f"\n{len(FIXTURES)} fixture(s) derived from the dossier")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
