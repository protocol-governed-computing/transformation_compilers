# Stage 6 — Governance Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p6
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_03_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Announcing the three moments registering a book completes
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-1}
  - capability: Announcing the moment each remaining act completes
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - capability: Attaching the moment naming a registered work to the act that claims its identity
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    source_finding: {phase: p4, register: capability_graph, row: 3}
  - capability: Announcing an ordered sequence at one ending
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: workflow::CONSTITUTION_WORKFLOW_V0
    source_finding: {phase: p4, register: capability_graph, row: 4}
  - capability: A moment naming a reinstatement
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - capability: Refusing a declared moment that nothing announces
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #2'}
  - capability: A moment announced per member of a collection
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #3'}
  storage_governance: []
  cross_subdomain_deps: []
  pps_artifacts_requiring_action:
  - fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    current_status: Admits a work, its first edition and that edition's first physical copy, and announces none of the three.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-1}
  - fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    current_status: Registers a further edition of a work the library already holds, and announces nothing.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - fqdn: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    current_status: Registers a further copy of an edition, and announces nothing.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    current_status: Corrects what the library publishes about a book, and announces nothing.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - fqdn: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    current_status: Takes a book out of service, and announces nothing.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - fqdn: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    current_status: Takes a physical copy out of service, and announces nothing.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - fqdn: book_library_mgmt::EV_WORK_REGISTERED_V0
    current_status: Declares the moment a work enters the catalog. Referenced by nothing.
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, row: 2}
  - fqdn: book_library_mgmt::EV_BOOK_REGISTERED_V0
    current_status: Declares the moment a book enters the catalog. Referenced by nothing.
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, row: 2}
  - fqdn: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    current_status: Declares the moment a physical copy enters the catalog. Referenced by nothing.
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, row: 2}
  - fqdn: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    current_status: Declares the moment a book's published details are corrected. Referenced by nothing.
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, row: 2}
  - fqdn: book_library_mgmt::EV_BOOK_RETIRED_V0
    current_status: Declares the moment a book leaves service. Referenced by nothing.
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, row: 2}
  - fqdn: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    current_status: Declares the moment a physical copy leaves service. Referenced by nothing.
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, row: 2}
  - fqdn: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    current_status: Returns a book to service. The business declares no moment for it, so it announces nothing and this change leaves it alone.
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - fqdn: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    current_status: Returns a physical copy to service. The same.
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - fqdn: book_library_mgmt::AC_LIBRARY_STAFF_V0
    current_status: The actor every catalog act runs as. Unchanged by this change, and carried unchanged by every act it re-renders.
    action: REUSE
    source_finding: {phase: p4, register: actors, row: 2}
  boundary_rules:
  - rule_name: AN_ACT_ANNOUNCES_WHAT_IT_COMPLETED
    statement: An act announces every moment it completed, or the business has no account of what happened. A moment that occurred and was not announced cannot be told apart afterwards from one that never occurred.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - rule_name: A_MOMENT_BELONGS_TO_THE_ACT_THAT_COMPLETES_IT
    statement: A moment is attached to the act that completes it, never to one that merely touches the same records.
    source_finding: {phase: p4, register: constraint_register, row: 2}
  - rule_name: THE_BUSINESS_IS_NOT_RESHAPED_TO_SUIT_THE_PLATFORM
    statement: The library registers a book once, as one act. It is not split into three so that each part may announce one moment.
    source_finding: {phase: p4, register: constraint_register, row: 3}
  - rule_name: ONLY_DECLARED_MOMENTS_ARE_ANNOUNCED
    statement: Only moments the business already declared are announced; a moment authored to fill a gap in an account is business content nobody decided.
    source_finding: {phase: p4, register: constraint_register, row: 4}
  - rule_name: THE_ORDER_ANNOUNCED_IS_THE_ORDER_COMPLETED
    statement: Where an act announces several, they are announced in the order the business completes them. The order is normative and a reader of the account sees it.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  governance_outcome:
  - capability: Announcing the three moments registering a book completes
    owner_subdomain: catalog
    source_finding: {phase: p4, register: gap_register, key: GAP-1}
  - capability: Announcing the moment each remaining act completes
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
| Authority class | reuse existing — an act announces what it completed; no new actor type |
| Governing constitutions | `workflow::CONSTITUTION_WORKFLOW_V0`, `event::CONSTITUTION_EVENT_V0`, `fb.constitution::CONSTITUTION_GOVERNANCE_V0` |

Every act and every moment belongs to catalog already. What changes is what its acts state about
what they did, declared in the acts themselves. No subdomain is created.

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

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
