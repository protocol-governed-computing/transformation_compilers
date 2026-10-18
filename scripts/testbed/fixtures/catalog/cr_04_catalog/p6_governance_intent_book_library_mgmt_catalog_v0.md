# Stage 6 — Governance Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p6
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_04_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Admitting a request to register a further edition
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-1}
  - capability: Admitting a request to correct bibliographic information
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - capability: Admitting a request to register a work
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - capability: The three operations
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    source_finding: {phase: p4, register: capability_graph, row: 5}
  - capability: Deciding who may perform an operation
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    source_finding: {phase: p4, register: capability_graph, row: 4}
  - capability: Holding what the catalog knows
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p4, register: capability_graph, row: 6}
  - capability: Comparing what an operation requires against what it uses
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - capability: Declaring the form of a detail the catalog holds
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #2'}
  - capability: The operations of subdomains and domains other than the catalog
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #3'}
  storage_governance: []
  cross_subdomain_deps: []
  pps_artifacts_requiring_action:
  - fqdn: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    current_status: Requires eleven things, all of which its operation reads, and states the publication year as a word where the other three statements of its form say number. Turns away every correct request.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-1}
  - fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    current_status: Requires eight things; its operation reads five. The title, the author and the publication year are read by no step, and their absence turns away every correction.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - fqdn: book_library_mgmt::IN_REGISTER_BOOK_V0
    current_status: 'Requires ten things; its operation reads eleven. The subject is read and not required, so a request without one is admitted and then cannot be carried out. Unchanged here: every present caller sends the subject nested inside the details of the book, so requiring it moves the boundary and the caller together.'
    action: REVIEW
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    current_status: Reads all eleven things its boundary requires. Correct as it stands.
    action: REUSE
    source_finding: {phase: p4, register: capability_graph, row: 5}
  - fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    current_status: Reads the record named and the details being changed, across four steps. Correct as it stands.
    action: REUSE
    source_finding: {phase: p4, register: capability_graph, row: 5}
  - fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    current_status: Reads eleven things, one of which its boundary does not require, and rebuilds the details of the book from what the request supplies at its top level rather than from the details the caller sends. Unchanged.
    action: REVIEW
    source_finding: {phase: p4, register: capability_graph, row: 5}
  - fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    current_status: Declares the six stores the catalog owns and the paths they occupy, and no form for any detail it holds. Unchanged by this change and named as the reason the form rests on agreement.
    action: REVIEW
    source_finding: {phase: p4, register: constraint_register, row: 6}
  boundary_rules:
  - rule_name: REQUIRES_ONLY_WHAT_IT_USES
    statement: An operation requires only what its steps read. A requirement no step reads turns away correct requests and admits nothing extra.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - rule_name: USES_ONLY_WHAT_IT_REQUIRES
    statement: An operation reads only what its boundary requires. A use no requirement covers admits a request the operation then cannot carry out, so a declaration gap surfaces part-way through instead of as a refusal before anything happened.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - rule_name: AUTHORITY_IS_UNTOUCHED
    statement: Nothing about who may perform an operation changes. The three things that decide it are stated separately, appear in all ten operations, and are read by no step of any of them.
    source_finding: {phase: p4, register: constraint_register, row: 2}
  - rule_name: HELD_RECORDS_ARE_NOT_DISTURBED
    statement: No record the catalog already holds is migrated, rewritten or revalidated. What is wrong is what a new request must supply, not what the catalog knows.
    source_finding: {phase: p4, register: constraint_register, row: 3}
  - rule_name: A_YEAR_IS_A_NUMBER
    statement: A publication year is stated as a number wherever an operation asks for one. The catalog displays a year as a number and every request the library makes supplies one.
    source_finding: {phase: p4, register: constraint_register, row: 4}
  - rule_name: NO_CORRECT_REQUEST_BECOMES_HARDER
    statement: No requirement is added where any present caller would then fail. This is what the ruling against gaining requirements was for, and it is what defers the third correction rather than permitting it.
    source_finding: {phase: p4, register: constraint_register, row: 5}
  - rule_name: AGREEMENT_IS_THE_ONLY_AUTHORITY
    statement: Where no artifact declares the form of a detail, the correction rests on agreement among the statements of it and on the data. That is weaker than a declaration and is what exists.
    source_finding: {phase: p4, register: constraint_register, row: 6}
  - rule_name: A_DEFERRAL_RECORDS_ITS_GROUND
    statement: The third boundary is deferred with the reason written down, not dropped. A defect nobody found and a defect deferred for a stated reason are different states, and only one of them is governed.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  governance_outcome:
  - capability: Admitting a request to register a further edition
    owner_subdomain: catalog
    source_finding: {phase: p4, register: gap_register, key: GAP-1}
  - capability: Admitting a request to correct bibliographic information
    owner_subdomain: catalog
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
```

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `book_library_mgmt` |
| Primary subdomain | `catalog` — EXISTING — modified by this CR |
| Authority class | reuse existing — a librarian requests, the catalog admits or turns away, the library's rules decide who may act; no new actor type |
| Governing constitutions | `intent::CONSTITUTION_INTENT_V0` |

What each catalog operation requires is the catalog's own account of what it does, so all three
corrections belong to the subdomain that declares them. Nothing new stands on its own; no artifact is
authored and no subdomain is created.

**No artifact outside this subdomain is touched.** Each of the three boundaries is reached by exactly
one artifact — the workflow it admits — and by nothing else. The three things that decide who may
perform an operation are read by no step of any of the subdomain's ten operations and are not
reached by restating what an operation needs.

---

## 1. Subdomain Boundary — Ownership

---

## 2. Storage Governance Requirements

---

## 3. Cross-Subdomain Dependency Declaration

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## Gate 1 — Design Approval
