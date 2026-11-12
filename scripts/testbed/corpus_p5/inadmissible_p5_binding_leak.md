# Business Intent — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
document:
  phase: p5
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_01_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The catalog governs the library's authoritative description of what it holds: each bibliographic
    work it has cataloged and each physical copy it owns. It exists because those records are kept by
    hand today, which produces inconsistent descriptions, duplicate entries and difficulty locating
    materials. It owns the description of the collection and the operations that maintain it; it does
    not govern who borrows the collection, what is ordered, or what is owed.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: REFINED
    refinement: States what the subdomain owns and the three functions it does not govern.
  subdomain_purposes:
  - subdomain: catalog
    purpose: Governs the library's authoritative description of what it holds — the works it has cataloged and the physical copies it owns.
    source_finding: {phase: p1, register: cr_type, row: 1}
  scope_boundary:
  - capability: Register a book
    status: IN_SCOPE
    notes: Authored this change request
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Register a physical copy against one work
    status: IN_SCOPE
    notes: Authored this change request
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Update bibliographic information
    status: IN_SCOPE
    notes: Authored this change request
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Retire an obsolete record
    status: IN_SCOPE
    notes: Authored this change request
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Search the catalog
    status: IN_SCOPE
    notes: Authored this change request
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Retrieve complete book details
    status: IN_SCOPE
    notes: Authored this change request
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Record that a catalog operation was performed
    status: IN_SCOPE
    notes: Authored this change request
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Confirm the staff member is authorized
    status: IN_SCOPE
    notes: Authored this change request
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Declare the stores this subdomain owns
    status: IN_SCOPE
    notes: Authored this change request
    source_finding: {phase: p4, register: authoring_scope, key: GAP-09}
  - capability: Grant staff authorization
    status: DEFERRED
    notes: Owned by patron, which is not in this release
    source_finding: {phase: p4, register: gap_register, key: GAP-10}
  - capability: Borrowing, reservations, fines, acquisitions, inventory reconciliation
    status: DEFERRED
    notes: Declared out of scope by the business author
    source_finding: {phase: p1, register: out_of_scope, row: 1}
  business_objects:
  - store_name: Bibliographic work record
    record_model: MUTABLE_STATE
    business_rationale: The library requires a single authoritative record for each work
    source_finding: {phase: p4, register: bm_entities, key: Bibliographic work}
  - store_name: Physical copy record
    record_model: MUTABLE_STATE
    business_rationale: The library requires a single authoritative record for each copy it owns
    source_finding: {phase: p4, register: bm_entities, key: Physical copy}
  - store_name: Catalog operation record
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Appended at $.payload.operation for every completed call
    source_finding: {phase: p4, register: bm_entities, key: Operation record}
  identity_semantics:
  - store_name: Bibliographic work record
    identity_field: Work identifier
    source: UNRESOLVED
    uniqueness_rule: Two registrations describing the same published title are the same work and must not produce two records
    cross_subdomain_relationship: None
    source_finding: {phase: p2, register: entity_attributes, key: Bibliographic Work identity}
  - store_name: Physical copy record
    identity_field: Copy identifier
    source: Assigned by the library when the copy is registered
    uniqueness_rule: Each owned copy is distinct even when several copies describe one work
    cross_subdomain_relationship: Names exactly one bibliographic work record
    source_finding: {phase: p2, register: entity_attributes, key: Physical Copy identity}
  - store_name: Catalog operation record
    identity_field: Operation sequence
    source: Assigned on append
    uniqueness_rule: Each performed operation appends exactly one record
    cross_subdomain_relationship: Names the staff member who performed it
    source_finding: {phase: p4, register: bm_entities, key: Operation record}
  invariants:
  - invariant: Each physical copy belongs to exactly one bibliographic work
    business_reason: A copy the library owns describes one published title; a copy belonging to two would make the collection uncountable
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - invariant: Each work and each copy has exactly one authoritative record
    business_reason: The library requires one place to look, which is the whole point of the change
    source_finding: {phase: p4, register: constraint_register, row: 2}
  - invariant: Every business operation performed is traceable and auditable
    business_reason: The library must be able to account afterwards for what staff did to the catalog
    source_finding: {phase: p4, register: constraint_register, row: 3}
  - invariant: Only authorized staff perform catalog operations
    business_reason: The catalog is the library's authoritative description and may not be altered by anyone
    source_finding: {phase: p4, register: constraint_register, row: 4}
  - invariant: A retired record is never offered as current
    business_reason: A record retired for being obsolete would mislead if it kept appearing in results
    source_finding: {phase: p4, register: design_decisions, row: 5}
  actions:
  - action: Register
    object: Bibliographic work record
    trigger: Authorized staff register a new book
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register a book}
  - action: Register
    object: Physical copy record
    trigger: Authorized staff register a copy
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register a physical copy against one work}
  - action: Update
    object: Bibliographic work record
    trigger: Authorized staff update a registered work
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Update bibliographic information}
  - action: Retire
    object: Bibliographic work record
    trigger: Authorized staff retire an obsolete record
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Retire an obsolete record}
  - action: Search
    object: Bibliographic work record
    trigger: Authorized staff search for materials
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Search the catalog}
  - action: Retrieve
    object: Bibliographic work record
    trigger: Authorized staff request complete details
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Retrieve complete book details}
  - action: Append
    object: Catalog operation record
    trigger: Any catalog operation completes
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Record that a catalog operation was performed}
  provisional_codes:
  - subdomain: catalog
    provisional_code: AC_LIBRARY_STAFF_V0
    family: AC
    summary: The authorized staff member who performs a catalog operation
    source_finding: {phase: p4, register: actors, key: Authorized staff member}
  - subdomain: catalog
    provisional_code: IN_REGISTER_BOOK_V0
    family: IN
    summary: A request to register a new book
    source_finding: {phase: p4, register: capability_graph, key: Register a book}
  - subdomain: catalog
    provisional_code: IN_REGISTER_PHYSICAL_COPY_V0
    family: IN
    summary: A request to register a copy against a work
    source_finding: {phase: p4, register: capability_graph, key: Register a physical copy against one work}
  - subdomain: catalog
    provisional_code: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    family: IN
    summary: A request to update a registered work
    source_finding: {phase: p4, register: capability_graph, key: Update bibliographic information}
  - subdomain: catalog
    provisional_code: IN_RETIRE_CATALOG_RECORD_V0
    family: IN
    summary: A request to retire an obsolete record
    source_finding: {phase: p4, register: capability_graph, key: Retire an obsolete record}
  - subdomain: catalog
    provisional_code: IN_SEARCH_CATALOG_V0
    family: IN
    summary: A request to locate materials
    source_finding: {phase: p4, register: capability_graph, key: Search the catalog}
  - subdomain: catalog
    provisional_code: IN_RETRIEVE_BOOK_DETAILS_V0
    family: IN
    summary: A request for the complete details of a book
    source_finding: {phase: p4, register: capability_graph, key: Retrieve complete book details}
  - subdomain: catalog
    provisional_code: WF_REGISTER_BOOK_V0
    family: WF
    summary: Registering a book, end to end
    source_finding: {phase: p4, register: capability_graph, key: Register a book}
  - subdomain: catalog
    provisional_code: WF_REGISTER_PHYSICAL_COPY_V0
    family: WF
    summary: Registering a copy against exactly one work
    source_finding: {phase: p4, register: capability_graph, key: Register a physical copy against one work}
  - subdomain: catalog
    provisional_code: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    family: WF
    summary: Updating the description of a registered work
    source_finding: {phase: p4, register: capability_graph, key: Update bibliographic information}
  - subdomain: catalog
    provisional_code: WF_RETIRE_CATALOG_RECORD_V0
    family: WF
    summary: Retiring a record so it is no longer current
    source_finding: {phase: p4, register: capability_graph, key: Retire an obsolete record}
  - subdomain: catalog
    provisional_code: WF_SEARCH_CATALOG_V0
    family: CC
    summary: Searching the catalog and recording that it happened
    source_finding: {phase: p4, register: capability_graph, key: Search the catalog}
  - subdomain: catalog
    provisional_code: WF_RETRIEVE_BOOK_DETAILS_V0
    family: WF
    summary: Assembling a work with the copies belonging to it
    source_finding: {phase: p4, register: capability_graph, key: Retrieve complete book details}
  - subdomain: catalog
    provisional_code: CC_CONFIRM_STAFF_AUTHORIZED_V0
    family: CC
    summary: Confirm the staff member may perform catalog operations
    source_finding: {phase: p4, register: capability_graph, key: Confirm the staff member is authorized}
  - subdomain: catalog
    provisional_code: catalog::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0
    family: CC
    summary: Record a work as the catalog's authoritative description of it
    source_finding: {phase: p4, register: capability_graph, key: Register a book}
  - subdomain: catalog
    provisional_code: CC_REGISTER_PHYSICAL_COPY_V0
    family: CC
    summary: Record a copy against exactly one work
    source_finding: {phase: p4, register: capability_graph, key: Register a physical copy against one work}
  - subdomain: catalog
    provisional_code: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    family: CC
    summary: Replace the descriptive content of a work's record
    source_finding: {phase: p4, register: capability_graph, key: Update bibliographic information}
  - subdomain: catalog
    provisional_code: CC_RETIRE_CATALOG_RECORD_V0
    family: CC
    summary: Mark a record retired so it is no longer offered as current
    source_finding: {phase: p4, register: capability_graph, key: Retire an obsolete record}
  - subdomain: catalog
    provisional_code: CC_SEARCH_CATALOG_V0
    family: CC
    summary: Select the current records matching the staff member's terms
    source_finding: {phase: p4, register: capability_graph, key: Search the catalog}
  - subdomain: catalog
    provisional_code: CC_ASSEMBLE_BOOK_DETAILS_V0
    family: CC
    summary: Assemble a work's record with the copies belonging to it
    source_finding: {phase: p4, register: capability_graph, key: Retrieve complete book details}
  - subdomain: catalog
    provisional_code: CC_APPEND_CATALOG_OPERATION_V0
    family: CC
    summary: Append a durable account of a performed catalog operation
    source_finding: {phase: p4, register: capability_graph, key: Record that a catalog operation was performed}
  cross_subdomain_refs:
  - cc_code: capability_side_effects::CS_MUTABLE_JSON_V0
    defined_in: capability_side_effects
    role: Holds a catalog record that can be updated in place
    source_finding: {phase: p4, register: dependency_graph, key: catalog to CS_MUTABLE_JSON}
  - cc_code: workload::CS_APPENDONLY_JSONL_V0
    defined_in: capability_side_effects
    role: Appends a durable account of a performed operation
    source_finding: {phase: p4, register: dependency_graph, key: catalog to CS_APPENDONLY_JSONL}
```

> P5 states the irreducible WHAT. It is the first phase to name what this change will build, using
> provisional codes — what to build, never where it will live. Placement is Stage 6's decision and
> binding identity is Stage 7's.

---

## 1. Subdomain Purpose

### Purpose of every subdomain this change touches

## 2. Scope Boundary

## 3. Business Objects

## 4. Identity Semantics

## 5. Business Invariants

## 6. Business Actions

## 7. Provisional Artifact Codes

## 8. Cross-Subdomain References
