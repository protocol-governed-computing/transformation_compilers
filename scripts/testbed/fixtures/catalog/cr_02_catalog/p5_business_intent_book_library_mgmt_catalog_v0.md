# Stage 5 — Business Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p5
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_02_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Catalog subdomain governs the library's authoritative description of what it holds: one record
    for each work the library has catalogued, one for each edition in which that work is published, and
    one for each physical copy it owns. It establishes the authority to say what the library has and how
    its holdings relate — a work exists in the collection because the catalog says so, an edition belongs
    to that work because the catalog records it that way, and a copy is a copy of one edition for the
    same reason. It manages the lifecycle of editions and copies from registration through retirement
    and back, and it records every operation performed against it so that any change to the library's
    description of itself can be traced afterwards. It exists because a work published more than once
    cannot be described accurately by a catalog that knows only editions, which is what the library had.
    It does not govern who borrows the collection, what is ordered, who the library's patrons are, or
    which staff are authorized.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: REFINED
    refinement: 'The seed states the change — that the record the previous change calls a book is an edition and that the work is added above it. This states the subdomain that results: the three records it holds, the authority it establishes over how they relate, the lifecycle it manages, and the four functions it does not govern. Nothing here contradicts the seed; what it adds is the standing description rather than the narrative of the change.'
  scope_boundary:
  - capability: Form the identifying key of a work from its title and author
    status: IN_SCOPE
    notes: A different business key from the edition's; the edition key is not widened
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Claim a work's identity so that two registrations of one work do not produce two works
    status: IN_SCOPE
    notes: Claimed atomically, as the edition's identity is
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Resolve the work an edition belongs to
    status: IN_SCOPE
    notes: Answers which work a title and author denote
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Group selected records by an attribute they share
    status: IN_SCOPE
    notes: Selection already exists; grouping does not
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Declare the stores the catalog owns
    status: IN_SCOPE
    notes: Extended with the work store and the work identity registry
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Bind the catalog's workflows to the stores they use
    status: IN_SCOPE
    notes: Extended so the new stores are reachable
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Register an edition of a work the catalog does not yet hold
    status: IN_SCOPE
    notes: Gains a work claim among the claims, before any write
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Validate that a registration carries what a work and an edition require
    status: IN_SCOPE
    notes: Runs before any claim, as it does today
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Register an additional edition of an existing work
    status: IN_SCOPE
    notes: The operation this change exists to add
    source_finding: {phase: p4, register: authoring_scope, key: GAP-09}
  - capability: Search the catalog and answer at the level of the work
    status: IN_SCOPE
    notes: Search terms unchanged; one result per matching work
    source_finding: {phase: p4, register: authoring_scope, key: GAP-10}
  - capability: Retrieve an edition's complete details with a summary of its work
    status: IN_SCOPE
    notes: Retrieval stays edition retrieval
    source_finding: {phase: p4, register: authoring_scope, key: GAP-11}
  - capability: Admit a request to register an additional edition of an existing work
    status: IN_SCOPE
    notes: A new operation is reached through its own entry point
    source_finding: {phase: p4, register: authoring_scope, key: GAP-12}
  - capability: Recognise the moment a work enters the catalog
    status: IN_SCOPE
    notes: The catalog declares a moment for each thing that enters it
    source_finding: {phase: p4, register: authoring_scope, key: GAP-13}
  - capability: Multiple identifiers for one publication
    status: DEFERRED
    notes: What an identifier identifies could not be answered until an edition was defined
    source_finding: {phase: p4, register: authoring_scope, key: Deferred}
  - capability: A governed subject taxonomy
    status: DEFERRED
    notes: A further catalog need, deferred to a change of its own
    source_finding: {phase: p4, register: authoring_scope, key: Deferred}
  - capability: Digital resources associated with catalog records
    status: DEFERRED
    notes: A further catalog need, deferred to a change of its own
    source_finding: {phase: p4, register: authoring_scope, key: Deferred}
  - capability: Images associated with catalog records
    status: DEFERRED
    notes: A further catalog need, deferred to a change of its own
    source_finding: {phase: p4, register: authoring_scope, key: Deferred}
  - capability: Deciding which staff are authorized
    status: DEFERRED
    notes: Belongs to the staff function, which a future change introduces
    source_finding: {phase: p4, register: authoring_scope, key: Deferred}
  business_objects:
  - store_name: Work record
    record_model: MUTABLE_STATE
    business_rationale: The library needs one place that says which works it holds; a work's description is corrected in place rather than re-registered
    source_finding: {phase: p4, register: bm_entities, key: Work}
  - store_name: Work identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Two registrations describing the same work must not produce two works, and only an atomic claim can guarantee that
    source_finding: {phase: p4, register: resources, key: The work identity registry}
  - store_name: Edition record
    record_model: MUTABLE_STATE
    business_rationale: 'Unchanged from the previous change: an edition''s description is corrected in place and its state moves both ways'
    source_finding: {phase: p4, register: bm_entities, key: Edition}
  - store_name: Physical copy record
    record_model: MUTABLE_STATE
    business_rationale: 'Unchanged from the previous change: a copy''s state moves both ways on the same record'
    source_finding: {phase: p4, register: bm_entities, key: Physical Copy}
  - store_name: Catalog audit trail
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: 'Unchanged from the previous change: an operation that has been performed cannot be un-performed, so its record is never amended'
    source_finding: {phase: p4, register: bm_entities, key: Business Operation}
  - store_name: Edition identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: 'Unchanged from the previous change: no two editions share a title, author and publication year'
    source_finding: {phase: p4, register: constraint_register, row: 9}
  - store_name: Copy barcode registry
    record_model: IDENTITY_REGISTRY
    business_rationale: 'Unchanged from the previous change: no two copies share a barcode'
    source_finding: {phase: p4, register: constraint_register, row: 7}
  identity_semantics:
  - store_name: Work record
    identity_field: Title and author together
    source: Supplied by the staff member registering the first edition of the work
    uniqueness_rule: Two registrations carrying the same title and author describe the same work, and the second names the work that exists rather than creating another
    cross_subdomain_relationship: None
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - store_name: Work identity registry
    identity_field: The key formed from title and author
    source: Formed by the catalog from the two identifying attributes
    uniqueness_rule: The key is claimed once; a second claim on it resolves to the work already registered rather than refusing
    cross_subdomain_relationship: None
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - store_name: Edition record
    identity_field: Title, author and publication year together
    source: Supplied by the staff member registering the edition
    uniqueness_rule: Two registrations carrying the same title, author and publication year describe the same edition, and the second is refused
    cross_subdomain_relationship: Names exactly one work record
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - store_name: Physical copy record
    identity_field: Barcode
    source: Assigned by the library and supplied when the copy is registered
    uniqueness_rule: Two records carrying the same barcode describe the same copy, and the second is refused
    cross_subdomain_relationship: Names exactly one edition record
    source_finding: {phase: p1, register: identity_and_sameness, row: 3}
  - store_name: Catalog audit trail
    identity_field: Append position
    source: Assigned when the entry is appended
    uniqueness_rule: Each performed operation appends exactly one entry, and no entry is amended or removed
    cross_subdomain_relationship: Names the staff member who performed the operation
    source_finding: {phase: p4, register: bm_entities, key: Business Operation}
  - store_name: Edition identity registry
    identity_field: The key formed from title, author and publication year
    source: Formed by the catalog, unchanged from the previous change
    uniqueness_rule: The key is claimed once; a second claim on it fails and the registration is refused
    cross_subdomain_relationship: None
    source_finding: {phase: p4, register: constraint_register, row: 9}
  - store_name: Copy barcode registry
    identity_field: Barcode
    source: Assigned by the library
    uniqueness_rule: The barcode is claimed once; a second claim on it fails and the copy registration is refused
    cross_subdomain_relationship: None
    source_finding: {phase: p4, register: constraint_register, row: 7}
  invariants:
  - invariant: Each edition belongs to exactly one work
    business_reason: An edition is a publication of one published work; an edition recorded against two works would make the collection's description untrue
    source_finding: {phase: p4, register: constraint_register, row: 6}
  - invariant: Each physical copy belongs to exactly one edition
    business_reason: A copy the library owns is a copy of one publication, which is what a staff member holds when they hold it
    source_finding: {phase: p4, register: constraint_register, row: 7}
  - invariant: No two works share the same title and author
    business_reason: The library needs one place that says which works it holds, and two records for one work would defeat the grouping this change exists to provide
    source_finding: {phase: p4, register: constraint_register, row: 8}
  - invariant: No two editions of a work share the same publication year
    business_reason: Editions are told apart by when they were published, so two carrying the same year cannot be told apart at all
    source_finding: {phase: p4, register: constraint_register, row: 9}
  - invariant: Every work has at least one edition
    business_reason: A work enters the catalog because the library holds a publication of it; a work with no edition describes nothing the library has
    source_finding: {phase: p4, register: constraint_register, row: 10}
  - invariant: A work is never retired
    business_reason: A work whose editions are all retired is simply that, and retiring the work would hide editions whose details must remain retrievable
    source_finding: {phase: p4, register: constraint_register, row: 11}
  - invariant: Every claim precedes every write in a registration
    business_reason: A registration that is refused must leave nothing behind, including a work nobody asked for
    source_finding: {phase: p4, register: constraint_register, row: 12}
  - invariant: A record written under the previous change remains valid and usable without recreation
    business_reason: The library's existing catalogue is the collection; a change that required it to be rebuilt would be a new catalogue, not an extension
    source_finding: {phase: p4, register: constraint_register, row: 2}
  - invariant: Every business operation performed against the catalog is traceable and auditable
    business_reason: The library must be able to say afterwards who changed its description of itself, and how
    source_finding: {phase: p4, register: constraint_register, row: 5}
  - invariant: Only authorized staff perform catalog operations
    business_reason: The catalog is the library's authoritative description of its holdings and is not open to alteration by anyone who asks
    source_finding: {phase: p4, register: constraint_register, row: 1}
  actions:
  - action: Register
    object: A work and its first edition, with that edition's first copy
    trigger: Authorized staff register an edition of a work the catalog does not yet hold
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register an edition of a work the catalog does not yet hold}
  - action: Register
    object: An additional edition of an existing work
    trigger: Authorized staff register a further edition of a work the catalog already holds
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register an additional edition of an existing work}
  - action: Register
    object: A physical copy of an edition
    trigger: Authorized staff register a further copy against a registered edition
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register a physical copy against exactly one edition}
  - action: Update
    object: An edition's bibliographic information
    trigger: Authorized staff change a registered edition's description
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Update an edition's bibliographic information}
  - action: Retire
    object: An edition record or a physical copy
    trigger: Authorized staff judge the record obsolete, or the copy lost or damaged
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Retire and reinstate an edition independently of the work's other editions}
  - action: Reinstate
    object: A retired edition record or physical copy
    trigger: Authorized staff return the record to the registered state
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Retire and reinstate an edition independently of the work's other editions}
  - action: Search
    object: The catalog, answering at the level of the work
    trigger: Authorized staff search by subject or title
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Search the catalog and answer at the level of the work}
  - action: Retrieve
    object: An edition's complete details, with a summary of its work
    trigger: Authorized staff select an edition and ask for everything about it
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Retrieve an edition's complete details with a summary of its work}
  - action: Associate
    object: An identifier, a taxonomy term, a digital resource or an image with a record
    trigger: A future governed change takes the need up
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Deferred}
  provisional_codes:
  - provisional_code: IN_REGISTER_ADDITIONAL_EDITION_V0
    family: IN
    summary: A request to register a further edition of a work the catalog already holds
    source_finding: {phase: p5, register: actions, key: Register}
  - provisional_code: WF_REGISTER_ADDITIONAL_EDITION_V0
    family: WF
    summary: The governed sequence that registers a further edition of an existing work
    source_finding: {phase: p5, register: actions, key: Register}
  - provisional_code: CC_REGISTER_ADDITIONAL_EDITION_V0
    family: CC
    summary: Resolves the named work, claims the edition's identity, writes the edition record and records the operation
    source_finding: {phase: p4, register: gap_register, key: GAP-09}
  - provisional_code: CC_CLAIM_WORK_IDENTITY_V0
    family: CC
    summary: Claims a work's identity so that two registrations of one work do not produce two works
    source_finding: {phase: p4, register: gap_register, key: GAP-02}
  - provisional_code: CC_RESOLVE_WORK_V0
    family: CC
    summary: Answers which work a title and author denote, and returns the work already registered
    source_finding: {phase: p4, register: gap_register, key: GAP-03}
  - provisional_code: CC_REGISTER_BOOK_V0
    family: CC
    summary: 'Extended: claims the work alongside the edition and the barcode, before any record is written'
    source_finding: {phase: p4, register: gap_register, key: GAP-07}
  - provisional_code: CC_VALIDATE_BOOK_SUBMISSION_V0
    family: CC
    summary: 'Extended: confirms a registration carries what a work requires as well as what an edition requires'
    source_finding: {phase: p4, register: gap_register, key: GAP-08}
  - provisional_code: CC_SEARCH_CATALOG_V0
    family: CC
    summary: 'Extended: groups the matching editions under the work they belong to and answers one result per work'
    source_finding: {phase: p4, register: gap_register, key: GAP-10}
  - provisional_code: CC_ASSEMBLE_BOOK_DETAILS_V0
    family: CC
    summary: 'Extended: carries a summary of the work the edition belongs to alongside the edition and its copies'
    source_finding: {phase: p4, register: gap_register, key: GAP-11}
  - provisional_code: CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    family: CT
    summary: Forms the single key claimed for a work from its title and author
    source_finding: {phase: p4, register: gap_register, key: GAP-01}
  - provisional_code: CT_PURE_SELECT_RECORDS_V0
    family: CT
    summary: Selects the records matching stated criteria and returns none when none match, so an edition the library holds no copies of can still be described
    source_finding: {phase: p4, register: gap_register, key: GAP-11}
  - provisional_code: CT_PURE_GROUP_RECORDS_V0
    family: CT
    summary: Groups selected records by an attribute they share, so a search can answer once per work
    source_finding: {phase: p4, register: gap_register, key: GAP-04}
  - provisional_code: EV_WORK_REGISTERED_V0
    family: EV
    summary: The moment a work enters the catalog
    source_finding: {phase: p4, register: gap_register, key: GAP-13}
  - provisional_code: STRUCTURE_CATALOG_STORAGE_V0
    family: STRUCTURE
    summary: 'Extended: declares the work record store and the work identity registry alongside the stores the catalog already owns'
    source_finding: {phase: p4, register: gap_register, key: GAP-05}
  - provisional_code: RB_CATALOG_BINDINGS_V0
    family: RB
    summary: 'Extended: binds the work store and the work identity registry to the workflows that read and write them'
    source_finding: {phase: p4, register: gap_register, key: GAP-06}
  cross_subdomain_refs: null
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
| Stage 4 — Business Model | p4_business_model_book_library_mgmt_catalog_v0.md | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | capability_graph · gap_register · constraint_register · design_decisions · authoring_scope · bm_entities · actors · events |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
