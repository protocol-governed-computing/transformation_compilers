# Stage 5 — Business Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p5
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_03_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Catalog subdomain governs what the library knows about its books: the works it carries, the
    editions of those works, and the physical copies on its shelves. It holds one record for each, the
    state that says whether each is in service or retired, and the details the library publishes about
    them. It records each thing being registered, its details being corrected, and its being retired or
    reinstated, and it announces the moments the business declared matter. It does not govern who borrows
    a book, what a borrower may do, or what the library charges.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: The seed's paragraph, word for word. This phase adds nothing to it.
  subdomain_purposes:
  - subdomain: catalog
    purpose: Governs what the library knows about its books — the works it carries, their editions, and the physical copies on its shelves.
    source_finding: {phase: p1, register: cr_type, row: 1}
  scope_boundary:
  - capability: Announcing the three moments registering a book completes
    status: IN_SCOPE
    notes: The act this change halted for.
    source_finding: {phase: p4, register: authoring_scope, row: 1}
  - capability: Announcing the moment each remaining act completes
    status: IN_SCOPE
    notes: Five acts, one moment each.
    source_finding: {phase: p4, register: authoring_scope, row: 2}
  - capability: A moment naming a reinstatement
    status: DEFERRED
    notes: The business has declared none; authoring one here would invent business content.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - capability: Refusing a declared moment that nothing announces
    status: DEFERRED
    notes: Its own question, and answering it here would refuse moments that are correct today.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #2'}
  - capability: A moment announced per member of a collection
    status: DEFERRED
    notes: A different shape; this change announces a known few, named where the act is designed.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #3'}
  business_objects: []
  identity_semantics: []
  invariants:
  - invariant: An act announces every moment it completed, or the business has no account of what happened.
    business_reason: An act that completes three moments and states one leaves two things that occurred with nothing saying so, and nobody reading the account afterwards can tell the difference between a moment that did not happen and one nobody announced.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - invariant: A moment is attached to the act that completes it, never to one that merely touches the same records.
    business_reason: Registering an additional edition reads the work it attaches to; announcing a work registered there would state that something happened which happened earlier and elsewhere.
    source_finding: {phase: p4, register: constraint_register, row: 2}
  - invariant: The business is not reshaped to suit what the platform could express.
    business_reason: The library registers a book once, as one act. Splitting it into three so that each could announce one moment would change what the business does in order to make it describable.
    source_finding: {phase: p4, register: constraint_register, row: 3}
  - invariant: Only moments the business already declared are announced.
    business_reason: A moment authored to fill a gap in an account is business content invented by whoever noticed the gap, rather than something the business decided occurred.
    source_finding: {phase: p4, register: constraint_register, row: 4}
  - invariant: A limitation paid in silence produces no account at all, and no check anywhere notices.
    business_reason: Faced with announcing one of three moments, this subdomain announced none — so the cost of the limitation was not a wrong account but the absence of one, and nothing anywhere reported a fault.
    source_finding: {phase: p4, register: constraint_register, row: 5}
  actions:
  - action: Announce the three moments registering a book completes
    object: Announcement
    trigger: A book being registered.
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, row: 1}
  - action: Announce the moment each remaining act completes
    object: Announcement
    trigger: Any of the five acts completing.
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, row: 2}
  provisional_codes: []
  cross_subdomain_refs: []
```

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

### Purpose of every subdomain this change touches

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | Capability graph, gaps, design decisions, authoring scope | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |
