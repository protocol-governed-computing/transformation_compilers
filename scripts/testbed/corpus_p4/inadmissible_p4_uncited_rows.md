# Business Model — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
document:
  phase: p4
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_01_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Authorized staff member
    role: Performs every catalog operation, and judges when a record is obsolete
    authority_class: Operator
    source_finding: null
  - actor: Library
    role: Owns the physical copies the catalog describes, and assigns each copy its barcode
    authority_class: Owner
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - actor: Staff function
    role: Decides which staff are authorized; not part of this change
    authority_class: Deferred authority
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  bm_entities:
  - entity: Book
    description: A published material the library catalogs — the general term for anything it catalogs
    store_model: One durable record per book, addressed by title, author and publication year together, updatable in place, carrying its own state
    source_finding: {phase: p2, register: entities, key: Book}
  - entity: Physical Copy
    description: An individual copy the library owns, belonging to exactly one book
    store_model: One durable record per copy, addressed by its barcode, naming the one book it belongs to, carrying its own state
    source_finding: {phase: p2, register: entities, key: Physical Copy}
  resources:
  - resource: Book records
    description: The catalog's authoritative description of every book, held by CS_MUTABLE_JSON_V0
    source_finding: {phase: p2, register: resource_register, key: Book}
  - resource: Physical copy records
    description: The catalog's authoritative record of every copy the library owns
    source_finding: {phase: p2, register: entities, key: Physical Copy}
  - resource: Catalog audit trail
    description: The catalog's own durable record of every operation performed against it
    source_finding: {phase: p3, register: analysis_findings, row: 1}
  events:
  - event: Book registered
    trigger: Authorized staff register a new book together with its first physical copy
    lifecycle_meaning: A book enters the catalog and acquires its authoritative record
    source_finding: {phase: p1, register: business_events, key: Book Registered}
  - event: Physical copy registered
    trigger: Authorized staff register a further copy against a registered book
    lifecycle_meaning: The library records another copy it owns
    source_finding: {phase: p1, register: business_events, key: Physical Copy Registered}
  - event: Bibliographic information updated
    trigger: Authorized staff update a registered book's information
    lifecycle_meaning: The authoritative description of a book changes
    source_finding: {phase: p1, register: business_events, key: Bibliographic Information Updated}
  - event: Book retired
    trigger: Authorized staff retire a book record judged obsolete
    lifecycle_meaning: The record is no longer to be used, and is excluded from search
    source_finding: {phase: p1, register: business_events, key: Book Retired}
  - event: Physical copy retired
    trigger: Authorized staff retire a copy that is lost or damaged
    lifecycle_meaning: The library no longer holds that copy
    source_finding: {phase: p1, register: business_events, key: Physical Copy Retired}
  relationships:
  - subject: Physical copy
    verb: belongs to
    object: Book
    capability_need: Record a copy against exactly one registered book
    source_finding: {phase: p1, register: business_invariants, key: each physical copy belongs to exactly one book}
  - subject: Book
    verb: is identified by
    object: Title, author and publication year
    capability_need: Refuse a registration whose three identifying attributes match a registered book
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - subject: Physical copy
    verb: is identified by
    object: Barcode
    capability_need: Refuse a copy registration whose barcode is already owned
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - subject: Authorized staff member
    verb: performs
    object: Catalog operation
    capability_need: Confirm the staff member is authorized before any operation
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - subject: Catalog operation
    verb: is recorded in
    object: Catalog audit trail
    capability_need: Record every performed operation durably in the catalog's own trail
    source_finding: {phase: p1, register: business_invariants, key: every business operation is traceable and auditable}
  - subject: Book
    verb: carries
    object: Subject
    capability_need: Select registered books by the subject or title staff search for
    source_finding: {phase: p1, register: known_facts, key: staff search the catalog by subject or by title}
  capability_graph:
  - capability: Hold a book record durably and update it in place
    source_finding: {phase: p3, register: authoring_decisions, key: Hold a book record durably and update it in place}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Hold a physical copy record durably and update it in place
    source_finding: {phase: p3, register: authoring_decisions, key: Hold a physical copy record durably and update it in place}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Enforce that one book exists per title, author and publication year
    source_finding: {phase: p3, register: authoring_decisions, key: 'Enforce that one book exists per title, author and publication year'}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Enforce that one physical copy exists per barcode
    source_finding: {phase: p3, register: authoring_decisions, key: Enforce that one physical copy exists per barcode}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Assemble a catalog record from supplied values
    source_finding: {phase: p3, register: authoring_decisions, key: Assemble a catalog record from supplied values}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Confirm a catalog record carries its required fields
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm a catalog record carries its required fields}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Select the catalog records matching stated criteria
    source_finding: {phase: p3, register: authoring_decisions, key: Select the catalog records matching stated criteria}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Confirm the parameters supplied to a catalog operation satisfy their declared rules
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm the parameters supplied to a catalog operation satisfy their declared rules}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Append an entry to an append-only trail
    source_finding: {phase: p3, register: authoring_decisions, key: Append an entry to an append-only trail}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Record a performed catalog operation in the catalog's audit trail
    source_finding: {phase: p3, register: authoring_decisions, key: Record a performed catalog operation in the catalog's audit trail}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: Nothing in the composition satisfies it.
  - capability: Declare the stores the catalog owns
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the stores the catalog owns}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: Nothing in the composition satisfies it.
  - capability: Bind the catalog's operations to the stores and mechanisms they use
    source_finding: {phase: p3, register: authoring_decisions, key: Bind the catalog's operations to the stores and mechanisms they use}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: Nothing in the composition satisfies it.
  - capability: A library staff actor whose authorization a catalog operation binds
    source_finding: {phase: p3, register: authoring_decisions, key: A library staff actor whose authorization a catalog operation binds}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: Nothing in the composition satisfies it.
  - capability: Confirm the staff member performing an operation is authorized
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm the staff member performing an operation is authorized}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: Nothing in the composition satisfies it.
  - capability: Register a book together with its first physical copy
    source_finding: {phase: p3, register: authoring_decisions, key: Register a book together with its first physical copy}
    status: CRITICAL
    gap_register_entry: GAP-06
    notes: Nothing in the composition satisfies it.
  - capability: Register a further physical copy against a registered book
    source_finding: {phase: p3, register: authoring_decisions, key: Register a further physical copy against a registered book}
    status: CRITICAL
    gap_register_entry: GAP-07
    notes: Nothing in the composition satisfies it.
  - capability: Update a book's bibliographic information
    source_finding: {phase: p3, register: authoring_decisions, key: Update a book's bibliographic information}
    status: CRITICAL
    gap_register_entry: GAP-08
    notes: Nothing in the composition satisfies it.
  - capability: Retire a book record
    source_finding: {phase: p3, register: authoring_decisions, key: Retire a book record}
    status: CRITICAL
    gap_register_entry: GAP-09
    notes: Nothing in the composition satisfies it.
  - capability: Retire a physical copy
    source_finding: {phase: p3, register: authoring_decisions, key: Retire a physical copy}
    status: CRITICAL
    gap_register_entry: GAP-10
    notes: Nothing in the composition satisfies it.
  - capability: Return a retired book record to the registered state
    source_finding: {phase: p3, register: authoring_decisions, key: Return a retired book record to the registered state}
    status: CRITICAL
    gap_register_entry: GAP-11
    notes: Nothing in the composition satisfies it.
  - capability: Return a retired physical copy to the registered state
    source_finding: {phase: p3, register: authoring_decisions, key: Return a retired physical copy to the registered state}
    status: CRITICAL
    gap_register_entry: GAP-12
    notes: Nothing in the composition satisfies it.
  - capability: Read every book record so that a search can select among them by content
    source_finding: {phase: p3, register: authoring_decisions, key: Read every book record so that a search can select among them by content}
    status: CRITICAL
    gap_register_entry: GAP-17
    notes: 'Owned by platform: an existing mechanism amended to publish records.'
  - capability: Search the catalog by subject or title, excluding retired books
    source_finding: {phase: p3, register: authoring_decisions, key: 'Search the catalog by subject or title, excluding retired books'}
    status: CRITICAL
    gap_register_entry: GAP-13
    notes: Nothing in the composition satisfies it.
  - capability: Retrieve a book's complete details with the copies the library holds
    source_finding: {phase: p3, register: authoring_decisions, key: Retrieve a book's complete details with the copies the library holds}
    status: CRITICAL
    gap_register_entry: GAP-14
    notes: Nothing in the composition satisfies it.
  - capability: A governed entry point for each catalog operation
    source_finding: {phase: p3, register: authoring_decisions, key: A governed entry point for each catalog operation}
    status: CRITICAL
    gap_register_entry: GAP-15
    notes: Nothing in the composition satisfies it.
  - capability: A business moment for each of the five catalog events
    source_finding: {phase: p3, register: authoring_decisions, key: A business moment for each of the five catalog events}
    status: CRITICAL
    gap_register_entry: GAP-16
    notes: Nothing in the composition satisfies it.
  dependency_graph:
  - from: catalog
    to: capability_side_effects::CS_MUTABLE_JSON_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Durable record storage}
  - from: catalog
    to: capability_side_effects::CS_REGISTRY_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Uniqueness}
  - from: catalog
    to: capability_side_effects::CS_APPENDONLY_JSONL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Append-only trail}
  - from: catalog
    to: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Record assembly}
  - from: catalog
    to: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Record shape validation}
  - from: catalog
    to: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Record selection}
  - from: catalog
    to: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Parameter validation}
  - from: catalog
    to: staff
    dependency_type: data read
    pps_status: GAP
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  constraint_register:
  - number: '1'
    constraint: Each physical copy belongs to exactly one book.
    source_finding: {phase: p3, register: analysis_findings, row: 99}
    source: invariant
  - number: '2'
    constraint: Each book the library holds has exactly one authoritative record.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '3'
    constraint: Each physical copy the library owns has exactly one authoritative record.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '4'
    constraint: No two registered books share the same title, author and publication year.
    source_finding: {phase: p1, register: business_invariants, row: 4}
    source: invariant
  - number: '5'
    constraint: A book carries at least one subject.
    source_finding: {phase: p1, register: business_invariants, row: 5}
    source: invariant
  - number: '6'
    constraint: No two physical copies the library owns share the same barcode.
    source_finding: {phase: p1, register: business_invariants, row: 6}
    source: invariant
  - number: '7'
    constraint: Every business operation performed against the catalog is traceable and auditable.
    source_finding: {phase: p1, register: business_invariants, row: 7}
    source: invariant
  - number: '8'
    constraint: Only authorized staff perform catalog operations.
    source_finding: {phase: p1, register: business_invariants, row: 8}
    source: invariant
  - number: '9'
    constraint: Capabilities deferred to future change requests must not be designed into this solution.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: governance rule
  - number: '10'
    constraint: A physical copy may never be recorded against more than one book.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: business policy
  - number: '11'
    constraint: The catalog must not import the records staff maintain manually today.
    source_finding: {phase: p1, register: constraints, row: 5}
    source: business policy
  - number: '12'
    constraint: The catalog appends only to a store it owns; it never writes into another subdomain's store.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    source: governance rule
  - number: '13'
    constraint: A record's state is held as data on the record, because retirement is reversible in both directions.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
    source: domain knowledge
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Record a performed catalog operation in the catalog's audit trail}
    capability: Record a performed catalog operation in the catalog's audit trail
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the stores the catalog owns}
    capability: Declare the stores the catalog owns
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Bind the catalog's operations to the stores and mechanisms they use}
    capability: Bind the catalog's operations to the stores and mechanisms they use
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: A library staff actor whose authorization a catalog operation binds}
    capability: A library staff actor whose authorization a catalog operation binds
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm the staff member performing an operation is authorized}
    capability: Confirm the staff member performing an operation is authorized
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, key: Register a book together with its first physical copy}
    capability: Register a book together with its first physical copy
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, key: Register a further physical copy against a registered book}
    capability: Register a further physical copy against a registered book
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-08
    source_finding: {phase: p3, register: authoring_decisions, key: Update a book's bibliographic information}
    capability: Update a book's bibliographic information
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-09
    source_finding: {phase: p3, register: authoring_decisions, key: Retire a book record}
    capability: Retire a book record
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-10
    source_finding: {phase: p3, register: authoring_decisions, key: Retire a physical copy}
    capability: Retire a physical copy
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-11
    source_finding: {phase: p3, register: authoring_decisions, key: Return a retired book record to the registered state}
    capability: Return a retired book record to the registered state
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-12
    source_finding: {phase: p3, register: authoring_decisions, key: Return a retired physical copy to the registered state}
    capability: Return a retired physical copy to the registered state
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-13
    source_finding: {phase: p3, register: authoring_decisions, key: 'Search the catalog by subject or title, excluding retired books'}
    capability: Search the catalog by subject or title, excluding retired books
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-14
    source_finding: {phase: p3, register: authoring_decisions, key: Retrieve a book's complete details with the copies the library holds}
    capability: Retrieve a book's complete details with the copies the library holds
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-15
    source_finding: {phase: p3, register: authoring_decisions, key: A governed entry point for each catalog operation}
    capability: A governed entry point for each catalog operation
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-16
    source_finding: {phase: p3, register: authoring_decisions, key: A business moment for each of the five catalog events}
    capability: A business moment for each of the five catalog events
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-17
    source_finding: {phase: p3, register: authoring_decisions, key: Read every book record so that a search can select among them by content}
    capability: Read every book record so that a search can select among them by content
    owner_subdomain: platform
    resolution: EXTEND
  design_decisions:
  - number: '1'
    decision: The catalog is a new subdomain, a peer of the nine other project functions, rather than an extension of anything existing.
    source_finding: {phase: p3, register: placement_decision}
    rationale: Nothing in the composition carries the project's namespace or manages a library catalog, so there is no boundary to extend.
    constraints_imposed: The catalog owns its records exclusively; the nine remaining functions stay adjacent and untouched.
  - number: '2'
    decision: The catalog owns its audit composition and its own append-only audit store, reusing only the append-only mechanism beneath them.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    rationale: A subdomain owns its stores exclusively, and library traceability must not depend on agent-governance semantics. Decided by the business owner.
    constraints_imposed: Two artifacts are authored rather than one reused; no catalog operation writes into another subdomain's store.
  - number: '3'
    decision: Uniqueness on a book is enforced by reusing the registry with a key formed from title, author and publication year.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
    rationale: Register-if-absent gives an atomic guarantee, and forming the key is a catalog business rule rather than a change to a side effect nineteen artifacts depend on. Decided by the business owner.
    constraints_imposed: The composite key is stated by the catalog; the registry itself is read, never modified.
  - number: '4'
    decision: A record's state is data on the record, not the store it occupies.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
    rationale: Retirement is reversible, so a record must move from registered to retired and back without moving between stores.
    constraints_imposed: The record store must support update in place; state is never implied by location.
  - number: '5'
    decision: Search and retrieval are audited but raise no business event.
    source_finding: {phase: p1, register: business_events, key: Book Registered}
    rationale: Every operation must be traceable, while an event is a moment another function may react to, and nothing reacts to a read.
    constraints_imposed: Five business moments are authored, not seven; the audit trail records all nine operations.
  - number: '6'
    decision: Registering a book registers its first physical copy in the same operation.
    source_finding: {phase: p1, register: known_facts, key: registering a book requires at least one physical copy}
    rationale: A book is never registered without a copy, so the two records come into existence together.
    constraints_imposed: Registering a book raises one business moment, not two; a registration offering no copy is refused.
  - number: '7'
    decision: Retirement never cascades in either direction.
    source_finding: {phase: p1, register: lifecycle_transitions, row: 2}
    rationale: Staff retire each record explicitly; nothing happens in the catalog that a staff member did not do.
    constraints_imposed: No derived state change exists to design, and the audit trail needs no staff-versus-system distinction.
  - number: '8'
    decision: Authorization is read on every operation and granted nowhere in this change.
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
    rationale: The catalog requires staff to be authorized; deciding who is authorized belongs to the staff function, which a future change request introduces.
    constraints_imposed: The catalog authors an authorization read and no authorization grant; the dependency on the staff function is that peer's gap.
  - number: '9'
    decision: Subject is free text, so no value-set validation applies.
    source_finding: {phase: p3, register: analysis_findings, row: 6}
    rationale: The business chose free text. Decided by the business owner.
    constraints_imposed: One fewer reuse candidate; search by kind is only as consistent as what staff type.
  - number: '10'
    decision: Search excludes retired books while retrieval serves them.
    source_finding: {phase: p3, register: analysis_findings, row: 4}
    rationale: A retired record must stay auditable and retrievable without appearing as current stock.
    constraints_imposed: Both read paths select by stated criteria, with the record's state as one of them.
  - number: '11'
    decision: The durable-record mechanism is extended to publish records, rather than the catalog keeping a second copy of every book for searching.
    source_finding: {phase: p3, register: analysis_findings, row: 7}
    rationale: The implementation already returned records and only the declaration withheld them; a projection store would duplicate every book and need syncing on every update, retirement and reinstatement. Decided by the business owner.
    constraints_imposed: One additive operation on a platform side effect; the catalog holds no second copy of a book.
  authoring_scope:
  - capability: Record a performed catalog operation in the catalog's audit trail
    gap_register_ref: GAP-01
  - capability: Declare the stores the catalog owns
    gap_register_ref: GAP-02
  - capability: Bind the catalog's operations to the stores and mechanisms they use
    gap_register_ref: GAP-03
  - capability: A library staff actor whose authorization a catalog operation binds
    gap_register_ref: GAP-04
  - capability: Confirm the staff member performing an operation is authorized
    gap_register_ref: GAP-05
  - capability: Register a book together with its first physical copy
    gap_register_ref: GAP-06
  - capability: Register a further physical copy against a registered book
    gap_register_ref: GAP-07
  - capability: Update a book's bibliographic information
    gap_register_ref: GAP-08
  - capability: Retire a book record
    gap_register_ref: GAP-09
  - capability: Retire a physical copy
    gap_register_ref: GAP-10
  - capability: Return a retired book record to the registered state
    gap_register_ref: GAP-11
  - capability: Return a retired physical copy to the registered state
    gap_register_ref: GAP-12
  - capability: Search the catalog by subject or title, excluding retired books
    gap_register_ref: GAP-13
  - capability: Retrieve a book's complete details with the copies the library holds
    gap_register_ref: GAP-14
  - capability: A governed entry point for each catalog operation
    gap_register_ref: GAP-15
  - capability: A business moment for each of the five catalog events
    gap_register_ref: GAP-16
```

> P4 consolidates Stages 1 to 3 and introduces nothing. Every row below is a faithful consolidation. What is wrong with each is where it says it was consolidated from.

This document consolidates Stages 1 to 3. It re-litigates nothing and introduces no design: every
row carries the prior-stage finding it came from, and every capability Stage 3 committed appears in
the capability graph exactly as Stage 3 stated it.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

---

## 2. Capability Graph (capability_graph)

---

## 3. Dependency Graph (dependency_graph)

The dependency on the staff function is a gap owned by that peer, not by this change: the catalog
reads whether a staff member is authorized and never decides it.

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

| Read every book record so that a search can select among them by content | GAP-17 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Circulation | A project function; this change request is limited to catalog only |
| Patron | A project function, and patron management is declared excluded from this release |
| Staff | A project function; it is where deciding who is authorized is deferred to |
| Reservations | Declared excluded from this release |
| Acquisitions | Declared excluded from this release |
| Inventory | A project function; inventory reconciliation is declared excluded from this release |
| Notifications | A project function; this change request is limited to catalog only |
| Policy | A project function; this change request is limited to catalog only |
| Reporting | A project function; this change request is limited to catalog only |
| Borrowing | Declared excluded from this release |
| Fines | Declared excluded from this release |
| Import of the records staff maintain manually today | The catalog starts empty |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 3 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
