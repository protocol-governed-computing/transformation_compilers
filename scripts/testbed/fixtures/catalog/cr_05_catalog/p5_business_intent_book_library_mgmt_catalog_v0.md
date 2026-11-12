# Stage 5 — Business Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p5
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_05_catalog
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
    refinement: ''
  subdomain_purposes:
  - subdomain: catalog
    purpose: Governs what the library knows about its books, and now holds every rule it applies to them.
    source_finding: {phase: p4, register: bm_entities, key: The Catalog's Rules}
  scope_boundary:
  - capability: Refuse anyone the library has not authorized
    status: IN_SCOPE
    notes: The confirming step holds the library's rules; every act composes it.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Refuse a registration the catalog finds incomplete
    status: IN_SCOPE
    notes: A rule following each check refuses on what it found.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Hold what a book, a work and a further edition must contain
    status: IN_SCOPE
    notes: The checking contracts hold their descriptions.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Check what the catalog records
    status: IN_SCOPE
    notes: Each registration act checks the record it writes.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Record the subject callers supply
    status: IN_SCOPE
    notes: The register act reads the subject where callers send it.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Register a copy as registered
    status: IN_SCOPE
    notes: The copy contract writes the state itself.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Keep a corrected record's state, and check it against the book description
    status: IN_SCOPE
    notes: The correction keeps the state and refuses a record that fails the description.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Admit a request without the rules the catalog holds
    status: IN_SCOPE
    notes: The gates stop requiring what the catalog holds and what no act reads; nothing a caller sends needs to change.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Establish who a caller is
    status: DEFERRED
    notes: The credentials a request presents stay its own.
    source_finding: {phase: p4, register: authoring_scope, key: Establish who a caller is}
  - capability: Records made under a request's own rules
    status: DEFERRED
    notes: Declined by the business; the record is added to and never rewritten.
    source_finding: {phase: p4, register: authoring_scope, key: Records made under a request's own rules}
  business_objects:
  - store_name: Book record
    record_model: MUTABLE_STATE
    business_rationale: 'Unchanged by this change, and named because what may be written into it changes: only a book meeting the description, with the subject callers supply, and a correction only with the state the record has.'
    source_finding: {phase: p4, register: bm_entities, key: The Book}
  - store_name: Copy record
    record_model: MUTABLE_STATE
    business_rationale: Unchanged by this change, and named because a copy is written only as registered.
    source_finding: {phase: p4, register: bm_entities, key: The Physical Copy}
  identity_semantics:
  - store_name: Book record
    identity_field: Title, author and publication year
    source: Supplied by staff registering the book
    uniqueness_rule: No two registered books share them; unchanged by this change.
    cross_subdomain_relationship: None
    source_finding: {phase: p4, register: bm_entities, key: The Book}
  - store_name: Copy record
    identity_field: Barcode
    source: Supplied by staff registering the copy
    uniqueness_rule: No two copies share a barcode; unchanged by this change.
    cross_subdomain_relationship: None
    source_finding: {phase: p4, register: bm_entities, key: The Physical Copy}
  invariants:
  - invariant: No catalog operation is performed by anyone the library has not authorized.
    business_reason: Only authorized staff perform catalog operations.
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: No book, work or further edition is registered without what the library says it must contain.
    business_reason: The library said the parts are required.
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: What the catalog checks is what it records.
    business_reason: A check of anything else judges nothing that is written.
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: No physical copy is registered in any state but registered.
    business_reason: There is one state a copy is registered in.
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - invariant: A business rule of the catalog's is held by the catalog, and no request changes it.
    business_reason: A business rule the caller supplies is a business rule the caller can widen.
    source_finding: {phase: p1, register: business_invariants, row: 5}
  - invariant: A refusal changes no record.
    business_reason: A refused request leaves the catalog as it found it.
    source_finding: {phase: p1, register: business_invariants, row: 6}
  actions:
  - action: Refuse
    object: A request from anyone the library has not authorized
    trigger: Any catalog request
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Refuse anyone the library has not authorized}
  - action: Refuse
    object: A book, work or further edition lacking what it must contain
    trigger: A registration
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Refuse a registration the catalog finds incomplete}
  - action: Register
    object: A copy, as registered
    trigger: A copy registration
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register a copy as registered}
  - action: Correct
    object: A book's bibliographic information, keeping its state
    trigger: A correction
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: 'Keep a corrected record''s state, and check it against the book description'}
  provisional_codes: null
  cross_subdomain_refs: []
```

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Invariants

---

## 6. Actions

---

## 7. Provisional Codes

---

## 8. Cross-Subdomain References

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
