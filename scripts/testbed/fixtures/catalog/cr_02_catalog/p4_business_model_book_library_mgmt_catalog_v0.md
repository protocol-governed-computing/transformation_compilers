# Stage 4 — Business Model: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p4
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_02_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Authorized staff
    role: Performs every catalog operation, including the ones this change adds.
    authority_class: Authorized business actor
    source_finding: {phase: p1, register: authority_boundaries, key: The judgement that an edition is obsolete}
  - actor: The catalog
    role: Holds the authoritative record of every work, edition and physical copy.
    authority_class: Owning subdomain
    source_finding: {phase: p1, register: authority_boundaries, key: Work record}
  - actor: The business author
    role: Settles what an edition is and what identifies a work.
    authority_class: Business authority, outside the system
    source_finding: {phase: p1, register: authority_boundaries, key: Whether an edition is part of a Book or a catalog entity in its own right}
  bm_entities:
  - entity: Work
    description: A published work, recognizable as one thing across the editions in which it is published, identified by its title and author.
    store_model: A durable record store holding one record per work, and a registry claiming each work's identity.
    source_finding: {phase: p2, register: entities, key: Work}
  - entity: Edition
    description: A publication of a work, identified by title, author and publication year. The record the previous change calls a book is an edition.
    store_model: The existing durable record store, unchanged.
    source_finding: {phase: p2, register: entities, key: Edition}
  - entity: Physical Copy
    description: An individual copy the library owns, belonging to exactly one edition.
    store_model: The existing durable record store, unchanged.
    source_finding: {phase: p2, register: entities, key: Physical Copy}
  - entity: Bibliographic Information
    description: An edition's descriptive content.
    store_model: Held within the edition's own record.
    source_finding: {phase: p2, register: entities, key: Bibliographic Information}
  - entity: Edition Summary
    description: Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean.
    store_model: Assembled at read time; not stored.
    source_finding: {phase: p2, register: entities, key: Edition Summary}
  - entity: Work Summary
    description: A short description of the work an edition belongs to, carried in that edition's retrieval.
    store_model: Assembled at read time; not stored.
    source_finding: {phase: p2, register: entities, key: Work Summary}
  - entity: Existing Catalog Record
    description: A catalog record written under the previous governed change, before this one.
    store_model: The same store the edition occupies.
    source_finding: {phase: p2, register: entities, key: Existing Catalog Record}
  - entity: Business Operation
    description: An action performed against the catalog that must be traceable and auditable.
    store_model: The existing append-only trail, unchanged.
    source_finding: {phase: p2, register: entities, key: Business Operation}
  resources:
  - resource: The work store
    description: Holds one record per work the catalog knows.
    source_finding: {phase: p3, register: authoring_decisions, key: Hold a work record durably and update it in place}
  - resource: The work identity registry
    description: Claims each work's identity so two registrations of one work do not produce two works.
    source_finding: {phase: p3, register: authoring_decisions, key: Enforce that one work exists per title and author}
  events:
  - event: Work Registered
    trigger: Authorized staff register an edition of a work the catalog does not yet hold.
    lifecycle_meaning: A work enters the catalog, created by the edition that evidences it.
    source_finding: {phase: p1, register: business_events, row: 1}
  - event: Edition Registered
    trigger: Authorized staff register an additional edition of an existing work.
    lifecycle_meaning: The catalog records a further edition of a work it already holds.
    source_finding: {phase: p1, register: business_events, row: 2}
  relationships:
  - subject: Work
    verb: is published as
    object: Edition
    capability_need: Register an edition against the work it belongs to, creating the work when the catalog does not yet hold it
    source_finding: {phase: p3, register: authoring_decisions, key: Register an edition of a work the catalog does not yet hold}
  - subject: Edition
    verb: belongs to
    object: Work
    capability_need: Resolve the work a title and author denote, so a further edition can name it
    source_finding: {phase: p3, register: authoring_decisions, key: Resolve the work an edition belongs to}
  - subject: Physical Copy
    verb: is a copy of
    object: Edition
    capability_need: Register a copy against exactly one edition, unchanged from the previous change
    source_finding: {phase: p3, register: authoring_decisions, key: Register a physical copy against exactly one edition}
  - subject: Authorized staff
    verb: searches
    object: Work
    capability_need: Answer a search at the level of the work, carrying a summary of its editions
    source_finding: {phase: p3, register: authoring_decisions, key: Search the catalog and answer at the level of the work}
  - subject: Authorized staff
    verb: retrieves
    object: Edition
    capability_need: Return an edition's details, its copies, and a summary of the work it belongs to
    source_finding: {phase: p3, register: authoring_decisions, key: Retrieve an edition's complete details with a summary of its work}
  capability_graph:
  - capability: Hold a work record durably and update it in place
    source_finding: {phase: p3, register: authoring_decisions, key: Hold a work record durably and update it in place}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Enforce that one work exists per title and author
    source_finding: {phase: p3, register: authoring_decisions, key: Enforce that one work exists per title and author}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is with a two-attribute key, exactly as the edition key uses it with three.
  - capability: Form the identifying key of a work from its title and author
    source_finding: {phase: p3, register: authoring_decisions, key: Form the identifying key of a work from its title and author}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: The edition key transform is reached by every catalog operation and is not widened.
  - capability: Claim a work's identity so that two registrations of one work do not produce two works
    source_finding: {phase: p3, register: authoring_decisions, key: Claim a work's identity so that two registrations of one work do not produce two works}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: Composed the way the edition claim is composed, against the work's own registry store.
  - capability: Resolve the work an edition belongs to
    source_finding: {phase: p3, register: authoring_decisions, key: Resolve the work an edition belongs to}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: Nothing in the composition answers which work a title and author denote.
  - capability: Group selected records by an attribute they share
    source_finding: {phase: p3, register: authoring_decisions, key: Group selected records by an attribute they share}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: Selection exists; grouping does not.
  - capability: Declare the stores the catalog owns
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the stores the catalog owns}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: Extended with the work store and the work identity registry.
  - capability: Bind the catalog's workflows to the stores they use
    source_finding: {phase: p3, register: authoring_decisions, key: Bind the catalog's workflows to the stores they use}
    status: CRITICAL
    gap_register_entry: GAP-06
    notes: Extended so the new stores are reachable by the workflows that use them.
  - capability: Register an edition of a work the catalog does not yet hold
    source_finding: {phase: p3, register: authoring_decisions, key: Register an edition of a work the catalog does not yet hold}
    status: CRITICAL
    gap_register_entry: GAP-07
    notes: Gains a work claim among the claims, before any write.
  - capability: Validate that a registration carries what a work and an edition require
    source_finding: {phase: p3, register: authoring_decisions, key: Validate that a registration carries what a work and an edition require}
    status: CRITICAL
    gap_register_entry: GAP-08
    notes: Runs before any claim, as it does today.
  - capability: Register an additional edition of an existing work
    source_finding: {phase: p3, register: authoring_decisions, key: Register an additional edition of an existing work}
    status: CRITICAL
    gap_register_entry: GAP-09
    notes: The operation this change exists to add.
  - capability: Search the catalog and answer at the level of the work
    source_finding: {phase: p3, register: authoring_decisions, key: Search the catalog and answer at the level of the work}
    status: CRITICAL
    gap_register_entry: GAP-10
    notes: The search terms are unchanged; the shape of the answer is not.
  - capability: Retrieve an edition's complete details with a summary of its work
    source_finding: {phase: p3, register: authoring_decisions, key: Retrieve an edition's complete details with a summary of its work}
    status: CRITICAL
    gap_register_entry: GAP-11
    notes: Retrieval stays edition retrieval and gains the work summary.
  - capability: Admit a request to register an additional edition of an existing work
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a request to register an additional edition of an existing work}
    status: CRITICAL
    gap_register_entry: GAP-12
    notes: A new business operation is reached through its own entry point.
  - capability: Recognise the moment a work enters the catalog
    source_finding: {phase: p3, register: authoring_decisions, key: Recognise the moment a work enters the catalog}
    status: CRITICAL
    gap_register_entry: GAP-13
    notes: The catalog declares a moment for each thing that enters it.
  - capability: Confirm the staff member performing an operation is authorized
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm the staff member performing an operation is authorized}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is; the operations this change adds reach it first, as every other does.
  - capability: Record every performed operation in the catalog's audit trail
    source_finding: {phase: p3, register: authoring_decisions, key: Record every performed operation in the catalog's audit trail}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is; the trail records whatever operation it is handed.
  - capability: Register a physical copy against exactly one edition
    source_finding: {phase: p3, register: authoring_decisions, key: Register a physical copy against exactly one edition}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is; nothing about copies changes.
  - capability: Retire and reinstate an edition independently of the work's other editions
    source_finding: {phase: p3, register: authoring_decisions, key: Retire and reinstate an edition independently of the work's other editions}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is; retirement already cascades to nothing.
  - capability: Update an edition's bibliographic information
    source_finding: {phase: p3, register: authoring_decisions, key: Update an edition's bibliographic information}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is; duplication remains an edition-level rule.
  dependency_graph:
  - from: catalog
    to: capability_side_effects::CS_MUTABLE_JSON_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Durable record storage for works}
  - from: catalog
    to: capability_side_effects::CS_REGISTRY_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Uniqueness claim for a work's identity}
  - from: catalog
    to: capability_side_effects::CS_APPENDONLY_JSONL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The audit step every catalog operation reaches last}
  - from: catalog
    to: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    dependency_type: data read
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The store declaration that must carry the work stores}
  - from: catalog
    to: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    dependency_type: data read
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The binding declaration that must bind the work stores}
  - from: catalog
    to: book_library_mgmt::CC_REGISTER_BOOK_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The registration step that must claim the work}
  - from: catalog
    to: book_library_mgmt::CC_SEARCH_CATALOG_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The search step whose answer must be grouped by work}
  - from: catalog
    to: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The retrieval step that must carry a work summary}
  - from: catalog
    to: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The authorization check every catalog operation reaches first}
  - from: catalog
    to: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The audit step every catalog operation reaches last}
  - from: catalog
    to: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Copy registration and barcode uniqueness}
  - from: catalog
    to: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Retirement and reinstatement of an edition}
  - from: catalog
    to: staff
    dependency_type: capability call
    pps_status: GAP
    source_finding: {phase: p1, register: authority_deferrals, key: Which staff are authorized}
  constraint_register:
  - number: '1'
    constraint: No capability staff have today may be withdrawn and no existing record may become unreachable.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: governance rule
  - number: '2'
    constraint: Existing catalog records must remain valid without recreation or migration, demonstrated against records written under the previous change.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: governance rule
  - number: '3'
    constraint: Only search and retrieval may be extended; every other existing operation must behave as it does today.
    source_finding: {phase: p1, register: constraints, row: 3}
    source: governance rule
  - number: '4'
    constraint: Multiple identifiers, governed subject taxonomy, digital resources and images must not be designed into this change.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: governance rule
  - number: '5'
    constraint: Every business operation must remain traceable and auditable.
    source_finding: {phase: p1, register: constraints, row: 5}
    source: invariant
  - number: '6'
    constraint: Each edition belongs to exactly one work.
    source_finding: {phase: p1, register: business_invariants, row: 1}
    source: invariant
  - number: '7'
    constraint: Each physical copy belongs to exactly one edition.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '8'
    constraint: No two works share the same title and author.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '9'
    constraint: No two editions of a work share the same publication year.
    source_finding: {phase: p1, register: business_invariants, row: 4}
    source: invariant
  - number: '10'
    constraint: Every work has at least one edition.
    source_finding: {phase: p1, register: business_invariants, row: 5}
    source: invariant
  - number: '11'
    constraint: A work is not retired; a work whose editions are all retired is simply that.
    source_finding: {phase: p1, register: operation_refusals, key: Retire a work}
    source: domain knowledge
  - number: '12'
    constraint: Every claim precedes every write, so a refused registration changes nothing.
    source_finding: {phase: p3, register: analysis_findings, row: 10}
    source: domain knowledge
  - number: '13'
    constraint: The transform forming the edition key is not widened; the identity of the existing record does not change to serve a new one.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
    source: domain knowledge
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Form the identifying key of a work from its title and author}
    capability: Form the identifying key of a work from its title and author
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Claim a work's identity so that two registrations of one work do not produce two works}
    capability: Claim a work's identity so that two registrations of one work do not produce two works
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Resolve the work an edition belongs to}
    capability: Resolve the work an edition belongs to
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: Group selected records by an attribute they share}
    capability: Group selected records by an attribute they share
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the stores the catalog owns}
    capability: Declare the stores the catalog owns
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, key: Bind the catalog's workflows to the stores they use}
    capability: Bind the catalog's workflows to the stores they use
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, key: Register an edition of a work the catalog does not yet hold}
    capability: Register an edition of a work the catalog does not yet hold
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-08
    source_finding: {phase: p3, register: authoring_decisions, key: Validate that a registration carries what a work and an edition require}
    capability: Validate that a registration carries what a work and an edition require
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-09
    source_finding: {phase: p3, register: authoring_decisions, key: Register an additional edition of an existing work}
    capability: Register an additional edition of an existing work
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-10
    source_finding: {phase: p3, register: authoring_decisions, key: Search the catalog and answer at the level of the work}
    capability: Search the catalog and answer at the level of the work
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-11
    source_finding: {phase: p3, register: authoring_decisions, key: Retrieve an edition's complete details with a summary of its work}
    capability: Retrieve an edition's complete details with a summary of its work
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-12
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a request to register an additional edition of an existing work}
    capability: Admit a request to register an additional edition of an existing work
    owner_subdomain: catalog
    resolution: NEW
  - gap_code: GAP-13
    source_finding: {phase: p3, register: authoring_decisions, key: Recognise the moment a work enters the catalog}
    capability: Recognise the moment a work enters the catalog
    owner_subdomain: catalog
    resolution: NEW
  design_decisions:
  - number: '1'
    decision: The record the previous change calls a book is an edition; the work is added above it.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    rationale: The existing identity of title, author and publication year already distinguishes editions, so no existing identity, record or operation is redefined.
    constraints_imposed: No migration of existing records; no change to the edition's identity; a record written before this change is an edition of a work with one edition.
  - number: '2'
    decision: The work's identity is formed by a new transform rather than by widening the existing key transform.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
    rationale: The edition key transform is reached by every catalog operation and 23 artifacts depend on it.
    constraints_imposed: The two keys stay independent; a change to one cannot alter the other.
  - number: '3'
    decision: The work is claimed through the same registry mechanism the edition is claimed through.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
    rationale: Register-if-absent gives the atomic uniqueness a work identity needs, and the mechanism is read rather than modified.
    constraints_imposed: The work claim is atomic; two registrations of one work cannot produce two works.
  - number: '4'
    decision: The work store and the work identity registry are declared in the catalog's own storage declaration.
    source_finding: {phase: p3, register: analysis_findings, row: 7}
    rationale: A subdomain declares its stores once and binds them once, and every consumer of both declarations is inside the catalog.
    constraints_imposed: No second storage or binding declaration for this subdomain.
  - number: '5'
    decision: Registering an edition of a new work extends the existing registration; registering an additional edition is a new operation.
    source_finding: {phase: p3, register: authoring_decisions, key: Register an additional edition of an existing work}
    rationale: The existing registration creates the work and requires a first copy; an additional edition does neither.
    constraints_imposed: Two registration operations, each with its own entry point, sharing every refusal the existing one enforces.
  - number: '6'
    decision: The work claim is placed among the existing claims, before any write.
    source_finding: {phase: p3, register: analysis_findings, row: 10}
    rationale: The previous change established the order so that a refused registration leaves nothing behind.
    constraints_imposed: A refused registration still changes nothing, including the work.
  - number: '7'
    decision: Search is extended rather than duplicated, and answers at the level of the work.
    source_finding: {phase: p3, register: analysis_findings, row: 5}
    rationale: Two searches would leave staff choosing which one answers their question, and the existing search's consumers are one workflow and one entry point within the subdomain.
    constraints_imposed: The result shape changes; the search terms do not. Every existing record remains findable.
  - number: '8'
    decision: Retrieval stays edition retrieval and carries a summary of the work.
    source_finding: {phase: p1, register: known_facts, key: Retrieval stays edition retrieval}
    rationale: The business asked for one retrieval carrying a summary, not a second operation.
    constraints_imposed: No work-level retrieval operation in this change.
  - number: '9'
    decision: A work is not retired.
    source_finding: {phase: p1, register: operation_refusals, key: Retire a work}
    rationale: A work whose editions are all retired is simply that; retirement is declared on the edition and cascades to nothing.
    constraints_imposed: No work lifecycle beyond registered; no cascade from an edition's retirement to its work.
  authoring_scope:
  - capability: Form the identifying key of a work from its title and author
    gap_register_ref: GAP-01
  - capability: Claim a work's identity so that two registrations of one work do not produce two works
    gap_register_ref: GAP-02
  - capability: Resolve the work an edition belongs to
    gap_register_ref: GAP-03
  - capability: Group selected records by an attribute they share
    gap_register_ref: GAP-04
  - capability: Declare the stores the catalog owns
    gap_register_ref: GAP-05
  - capability: Bind the catalog's workflows to the stores they use
    gap_register_ref: GAP-06
  - capability: Register an edition of a work the catalog does not yet hold
    gap_register_ref: GAP-07
  - capability: Validate that a registration carries what a work and an edition require
    gap_register_ref: GAP-08
  - capability: Register an additional edition of an existing work
    gap_register_ref: GAP-09
  - capability: Search the catalog and answer at the level of the work
    gap_register_ref: GAP-10
  - capability: Retrieve an edition's complete details with a summary of its work
    gap_register_ref: GAP-11
  - capability: Admit a request to register an additional edition of an existing work
    gap_register_ref: GAP-12
  - capability: Recognise the moment a work enters the catalog
    gap_register_ref: GAP-13
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies: what is reused already exists, what is extended or authored is a declared gap.
Nothing is re-litigated and nothing new is decided.

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

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Multiple identifiers for one publication | A further catalog need, deferred to a governed change of its own; what an ISBN identifies could not be answered until an edition was defined. |
| A governed subject taxonomy | A further catalog need, deferred to a governed change of its own. |
| Digital resources associated with catalog records | A further catalog need, deferred to a governed change of its own. |
| Images associated with catalog records | A further catalog need, deferred to a governed change of its own. |
| Deciding which staff are authorized | Deferred to the staff function, which a future governed change introduces. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · business_invariants · constraints · authority_boundaries · business_events · out_of_scope · authority_deferrals |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · gaps · architectural_observations |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
