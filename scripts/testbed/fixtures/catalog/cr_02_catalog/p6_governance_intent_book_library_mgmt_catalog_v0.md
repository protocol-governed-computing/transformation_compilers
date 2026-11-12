# Stage 6 — Governance Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p6
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_02_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Form the identifying key of a work from its title and author
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Form the identifying key of a work from its title and author}
  - capability: Claim a work's identity so that two registrations of one work do not produce two works
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Claim a work's identity so that two registrations of one work do not produce two works}
  - capability: Resolve the work an edition belongs to
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Resolve the work an edition belongs to}
  - capability: Group selected records by an attribute they share
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Group selected records by an attribute they share}
  - capability: Declare the stores the catalog owns
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Declare the stores the catalog owns}
  - capability: Bind the catalog's workflows to the stores they use
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Bind the catalog's workflows to the stores they use}
  - capability: Register an edition of a work the catalog does not yet hold
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Register an edition of a work the catalog does not yet hold}
  - capability: Validate that a registration carries what a work and an edition require
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Validate that a registration carries what a work and an edition require}
  - capability: Register an additional edition of an existing work
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Register an additional edition of an existing work}
  - capability: Search the catalog and answer at the level of the work
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Search the catalog and answer at the level of the work}
  - capability: Retrieve an edition's complete details with a summary of its work
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Retrieve an edition's complete details with a summary of its work}
  - capability: Admit a request to register an additional edition of an existing work
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Admit a request to register an additional edition of an existing work}
  - capability: Recognise the moment a work enters the catalog
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Recognise the moment a work enters the catalog}
  - capability: Hold a record durably and update it in place
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    source_finding: {phase: p4, register: capability_graph, key: Hold a work record durably and update it in place}
  - capability: Claim an identity atomically so that a second claim cannot succeed unnoticed
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_REGISTRY_V0
    source_finding: {phase: p4, register: capability_graph, key: Enforce that one work exists per title and author}
  - capability: Confirm the staff member performing an operation is authorized
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    source_finding: {phase: p4, register: capability_graph, key: Confirm the staff member performing an operation is authorized}
  - capability: Record every performed operation in the catalog's audit trail
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    source_finding: {phase: p4, register: capability_graph, key: Record every performed operation in the catalog's audit trail}
  - capability: Register a physical copy against exactly one edition
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    source_finding: {phase: p4, register: capability_graph, key: Register a physical copy against exactly one edition}
  - capability: Retire and reinstate an edition independently of the work's other editions
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    source_finding: {phase: p4, register: capability_graph, key: Retire and reinstate an edition independently of the work's other editions}
  - capability: Update an edition's bibliographic information
    owner_subdomain: catalog
    disposition: SATISFIED
    existing_artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    source_finding: {phase: p4, register: capability_graph, key: Update an edition's bibliographic information}
  - capability: Deciding which staff are authorized
    owner_subdomain: staff
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Deciding which staff are authorized}
  - capability: Multiple identifiers for one publication
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Multiple identifiers for one publication}
  - capability: A governed subject taxonomy
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: A governed subject taxonomy}
  - capability: Digital resources associated with catalog records
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Digital resources associated with catalog records}
  - capability: Images associated with catalog records
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Images associated with catalog records}
  storage_governance:
  - storage_need: A durable record of every work the library has catalogued
    purpose: The library requires one authoritative description per work, correctable in place, so that several editions can be said to be editions of one thing
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, key: Work record}
  - storage_need: An atomic claim on each work's identity
    purpose: Two registrations describing the same work must resolve to one work, and only a claim taken at the moment of registration can guarantee it
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, key: Work identity registry}
  - storage_need: A durable record of every edition the library holds
    purpose: 'Unchanged from the previous change: one authoritative description per edition, correctable in place and carrying its own registered-or-retired state'
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, key: Edition record}
  - storage_need: A durable record of every physical copy the library owns
    purpose: 'Unchanged from the previous change: one authoritative record per copy, each naming the one edition it belongs to'
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, key: Physical copy record}
  - storage_need: An unamendable trail of every operation performed
    purpose: 'Unchanged from the previous change: an operation that has been performed cannot be un-performed, so its record is never amended'
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, key: Catalog audit trail}
  - storage_need: An atomic claim on each edition's identity
    purpose: 'Unchanged from the previous change: no two editions share a title, author and publication year'
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, key: Edition identity registry}
  - storage_need: An atomic claim on each copy's barcode
    purpose: 'Unchanged from the previous change: no two copies the library owns share a barcode'
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, key: Copy barcode registry}
  cross_subdomain_deps:
  - dependency: Read whether a staff member is authorized to perform catalog operations
    direction: catalog → staff
    existing_artifact: ''
    status: GAP
    source_finding: {phase: p4, register: dependency_graph, key: catalog → staff}
  pps_artifacts_requiring_action:
  - fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    current_status: Declares the five stores the catalog owns; every consumer is inside the subdomain
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-05}
  - fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    current_status: Binds the catalog's workflows to the stores they use; referenced by nine artifacts, all within the subdomain
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-06}
  - fqdn: book_library_mgmt::CC_REGISTER_BOOK_V0
    current_status: Registers a record together with its first copy, claiming two identities before any write
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-07}
  - fqdn: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    current_status: Confirms a registration carries what a record requires, before any claim
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-08}
  - fqdn: book_library_mgmt::CC_SEARCH_CATALOG_V0
    current_status: Selects registered records by subject or title and excludes retired ones
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-10}
  - fqdn: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    current_status: Assembles one record with the physical copies of it
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-11}
  - fqdn: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    current_status: Forms the three-attribute key every catalog operation reaches; 23 artifacts depend on it
    action: REVIEW
    source_finding: {phase: p3, register: authoring_decisions, key: Form the identifying key of a work from its title and author}
  - fqdn: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    current_status: Claims the edition's identity; read as the precedent the work claim follows
    action: REVIEW
    source_finding: {phase: p3, register: authoring_decisions, key: Claim a work's identity so that two registrations of one work do not produce two works}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    current_status: Declared and in use by ai_governance, book_library_mgmt and workload
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    current_status: Declared and in use by ai_governance and book_library_mgmt
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - fqdn: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    current_status: Selects records by stated criteria; examined and not extended
    action: REVIEW
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_transforms::CT_PURE_FILTER_RECORDS_V0'}
  boundary_rules:
  - rule_name: CATALOG_OWNS_ITS_STORES
    statement: Every store the catalog reads or writes is declared by the catalog, including the two this change adds, and no catalog operation writes into a store another subdomain owns.
    source_finding: {phase: p3, register: analysis_findings, row: 7}
  - rule_name: AUTHORIZATION_IS_READ_NEVER_GRANTED
    statement: The catalog confirms a staff member is authorized on every operation, including the ones this change adds, and grants authorization nowhere.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - rule_name: EVERY_CLAIM_PRECEDES_EVERY_WRITE
    statement: A registration claims every identity it needs — the work, the edition and the barcode — before it writes any record, so a refused registration leaves nothing behind.
    source_finding: {phase: p4, register: constraint_register, row: 12}
  - rule_name: EDITION_IDENTITY_IS_NOT_WIDENED
    statement: The key that identifies an existing record is not changed to serve the work; the work's key is formed independently and the two cannot alter each other.
    source_finding: {phase: p4, register: constraint_register, row: 13}
  - rule_name: NO_CAPABILITY_IS_WITHDRAWN
    statement: Every operation staff had before this change remains reachable and every existing record remains findable; search and retrieval are extended in the shape of their answers and in nothing else.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - rule_name: A_WORK_IS_NEVER_RETIRED
    statement: Retirement is declared on the edition and on the copy; a work whose editions are all retired is simply that, and no cascade reaches it.
    source_finding: {phase: p4, register: constraint_register, row: 11}
  governance_outcome:
  - capability: Form the identifying key of a work from its title and author
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Form the identifying key of a work from its title and author}
  - capability: Claim a work's identity so that two registrations of one work do not produce two works
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Claim a work's identity so that two registrations of one work do not produce two works}
  - capability: Resolve the work an edition belongs to
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Resolve the work an edition belongs to}
  - capability: Group selected records by an attribute they share
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Group selected records by an attribute they share}
  - capability: Declare the stores the catalog owns
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Declare the stores the catalog owns}
  - capability: Bind the catalog's workflows to the stores they use
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Bind the catalog's workflows to the stores they use}
  - capability: Register an edition of a work the catalog does not yet hold
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Register an edition of a work the catalog does not yet hold}
  - capability: Validate that a registration carries what a work and an edition require
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Validate that a registration carries what a work and an edition require}
  - capability: Register an additional edition of an existing work
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Register an additional edition of an existing work}
  - capability: Search the catalog and answer at the level of the work
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Search the catalog and answer at the level of the work}
  - capability: Retrieve an edition's complete details with a summary of its work
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Retrieve an edition's complete details with a summary of its work}
  - capability: Admit a request to register an additional edition of an existing work
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Admit a request to register an additional edition of an existing work}
  - capability: Recognise the moment a work enters the catalog
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Recognise the moment a work enters the catalog}
```

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

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
