# Stage 5 — Business Intent: book_library_mgmt / catalog

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

    The catalog governs the library's authoritative description of what it holds: one record for each book
    it catalogs, and one for each physical copy it owns. It establishes the authority to state what the
    library has — a book exists in the collection because the catalog says so, and a copy belongs to
    exactly one book because the catalog records it that way. It manages the lifecycle of both records
    from registration through retirement and back, and it records every operation performed against it so
    that any change to the library's description of itself can be traced afterwards. It exists because
    those records are maintained by hand today, which produces inconsistent descriptions, duplicate
    entries and difficulty locating materials. It does not govern who borrows the collection, what is
    ordered, who the library's patrons are, or which staff are authorized.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: REFINED
    refinement: States the authority the subdomain establishes — a book exists in the collection because the catalog says so — the lifecycle it manages from registration through retirement and back, and the four functions it explicitly does not govern. The seed states what the catalog is for and why it exists; none of these four additions contradicts it.
  subdomain_purposes:
  - subdomain: catalog
    purpose: Governs the library's authoritative description of what it holds — one record per book it catalogs and one per physical copy it owns — and the lifecycle of both from registration through retirement and back.
    source_finding: {phase: p1, register: cr_type, row: 1}
  scope_boundary:
  - capability: Register a book together with its first physical copy
    status: IN_SCOPE
    notes: A book is never registered without a copy
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Register a further physical copy against a registered book
    status: IN_SCOPE
    notes: Refused if the barcode is already owned or the book is not registered
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Update a book's bibliographic information
    status: IN_SCOPE
    notes: Refused if the change would make the book a duplicate of another
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Retire a book record
    status: IN_SCOPE
    notes: Leaves the book's copies untouched
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Retire a physical copy
    status: IN_SCOPE
    notes: Leaves the book record untouched, including when it was the last copy
    source_finding: {phase: p4, register: authoring_scope, key: GAP-09}
  - capability: Return a retired book record to the registered state
    status: IN_SCOPE
    notes: Reinstatement is explicit, never derived
    source_finding: {phase: p4, register: authoring_scope, key: GAP-10}
  - capability: Return a retired physical copy to the registered state
    status: IN_SCOPE
    notes: Reinstatement is explicit, never derived
    source_finding: {phase: p4, register: authoring_scope, key: GAP-11}
  - capability: Search the catalog by subject or title
    status: IN_SCOPE
    notes: Retired books are excluded from results
    source_finding: {phase: p4, register: authoring_scope, key: GAP-12}
  - capability: Retrieve a book's complete details with the copies held
    status: IN_SCOPE
    notes: Serves retired books as well as registered ones
    source_finding: {phase: p4, register: authoring_scope, key: GAP-13}
  - capability: Confirm the staff member performing an operation is authorized
    status: IN_SCOPE
    notes: The catalog reads authorization; it never grants it
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Record every performed catalog operation in the catalog's own audit trail
    status: IN_SCOPE
    notes: The catalog owns the trail it appends to
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Read every book record so that a search can select among them by content
    status: IN_SCOPE
    notes: An existing mechanism amended to publish records; owned by platform, not by the catalog
    source_finding: {phase: p4, register: authoring_scope, key: GAP-17}
  - capability: Deciding which staff are authorized
    status: DEFERRED
    notes: Belongs to the staff function, which a future change request introduces
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  - capability: Deleting a catalog record
    status: DEFERRED
    notes: 'Not deferred but excluded: a record is never deleted, so no capability is authored for it'
    source_finding: {phase: p1, register: business_invariants, row: 9}
  - capability: Importing the records staff maintain manually today
    status: DEFERRED
    notes: The catalog starts empty
    source_finding: {phase: p1, register: out_of_scope, key: Import of the records staff maintain manually today}
  - capability: Circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy and reporting
    status: DEFERRED
    notes: The nine remaining project functions, adjacent and untouched
    source_finding: {phase: p1, register: governance_scope, row: 2}
  business_objects:
  - store_name: Book record
    record_model: MUTABLE_STATE
    business_rationale: The library requires one authoritative record per book, its bibliographic information is correctable, and its state moves from registered to retired and back on the same record
    source_finding: {phase: p4, register: bm_entities, key: Book}
  - store_name: Physical copy record
    record_model: MUTABLE_STATE
    business_rationale: The library requires one authoritative record per copy it owns, and a copy's state moves both ways on the same record
    source_finding: {phase: p4, register: bm_entities, key: Physical Copy}
  - store_name: Catalog audit trail
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence
    source_finding: {phase: p4, register: resources, key: Catalog audit trail}
  - store_name: Book identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Duplicate prevention needs an atomic claim on a book's identity at the moment of registration
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - store_name: Copy barcode registry
    record_model: IDENTITY_REGISTRY
    business_rationale: No two copies the library owns may share a barcode, and the claim must hold at the moment of registration
    source_finding: {phase: p1, register: business_invariants, row: 6}
  identity_semantics:
  - store_name: Book record
    identity_field: Title, author and publication year together
    source: Supplied by the staff member registering the book
    uniqueness_rule: Two registrations carrying the same publication year, and the same title and author without regard to letter case or repeated spacing, describe the same book, and the second is refused
    cross_subdomain_relationship: None
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - store_name: Physical copy record
    identity_field: Barcode
    source: Assigned by the library and supplied when the copy is registered
    uniqueness_rule: Two records carrying the same barcode describe the same copy, and the second is refused
    cross_subdomain_relationship: Names exactly one book record
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - store_name: Catalog audit trail
    identity_field: Append position
    source: Assigned when the entry is appended
    uniqueness_rule: Each performed operation appends exactly one entry, and no entry is amended or removed
    cross_subdomain_relationship: Names the staff member who performed the operation
    source_finding: {phase: p4, register: resources, key: Catalog audit trail}
  - store_name: Book identity registry
    identity_field: The key formed from title, author and publication year
    source: Formed by the catalog, comparing title and author without regard to letter case or repeated spacing
    uniqueness_rule: The key is claimed once; a second claim on it fails and the registration is refused
    cross_subdomain_relationship: None
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - store_name: Copy barcode registry
    identity_field: Barcode
    source: Assigned by the library
    uniqueness_rule: The barcode is claimed once; a second claim on it fails and the copy registration is refused
    cross_subdomain_relationship: None
    source_finding: {phase: p1, register: business_invariants, row: 6}
  invariants:
  - invariant: Each physical copy belongs to exactly one book
    business_reason: A copy the library owns is a copy of one published thing; a copy recorded against two books would make the collection's description untrue
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: Each book the library holds has exactly one authoritative record
    business_reason: The library needs one place that says what it holds, which is the whole point of a governed catalog
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: Each physical copy the library owns has exactly one authoritative record
    business_reason: Two records for one copy would make the library's count of what it owns unreliable
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: No two registered books share the same title, author and publication year
    business_reason: Duplicate entries are the pain this change exists to remove
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - invariant: A book carries at least one subject
    business_reason: Subject is what staff search on when looking for material rather than a known title, so a book with none could not be found that way
    source_finding: {phase: p1, register: business_invariants, row: 5}
  - invariant: No two physical copies the library owns share the same barcode
    business_reason: A barcode is how staff name one copy among several of the same book, including when retiring one
    source_finding: {phase: p1, register: business_invariants, row: 6}
  - invariant: Every business operation performed against the catalog is traceable and auditable
    business_reason: The library must be able to account afterwards for every change to its description of itself
    source_finding: {phase: p1, register: business_invariants, row: 7}
  - invariant: Only authorized staff perform catalog operations
    business_reason: The catalog is the library's authoritative record, and an unauthorized change to it would not be authoritative
    source_finding: {phase: p1, register: business_invariants, row: 8}
  - invariant: No catalog record is ever deleted
    business_reason: Retirement is the only way a record leaves use; a deleted record would leave its audit trail pointing at nothing
    source_finding: {phase: p1, register: business_invariants, row: 9}
  - invariant: A registered book always has at the moment of registration at least one physical copy
    business_reason: The library catalogs what it holds, and a book it holds no copy of is not a holding
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  actions:
  - action: Register
    object: Book, with its first physical copy
    trigger: An authorized staff member registers a book the library has acquired
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register a book together with its first physical copy}
  - action: Register
    object: Physical copy
    trigger: An authorized staff member records a further copy of a registered book
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register a further physical copy against a registered book}
  - action: Update
    object: Book's bibliographic information
    trigger: An authorized staff member corrects or changes a book's description
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Update a book's bibliographic information}
  - action: Retire
    object: Book record
    trigger: An authorized staff member judges the record obsolete
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Retire a book record}
  - action: Retire
    object: Physical copy
    trigger: A copy is lost or damaged
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Retire a physical copy}
  - action: Reinstate
    object: Book record
    trigger: An authorized staff member returns a retired book to use
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Return a retired book record to the registered state}
  - action: Reinstate
    object: Physical copy
    trigger: An authorized staff member returns a retired copy to use
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Return a retired physical copy to the registered state}
  - action: Search
    object: Catalog
    trigger: An authorized staff member looks for material by subject or by title
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: 'Search the catalog by subject or title, excluding retired books'}
  - action: Retrieve
    object: Book's complete details
    trigger: An authorized staff member asks what the library holds of one book
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Retrieve a book's complete details with the copies the library holds}
  - action: Delete
    object: Book record or physical copy
    trigger: Never — no trigger exists, because a record is never deleted
    status: DEFERRED
    source_finding: {phase: p1, register: business_invariants, row: 9}
  provisional_codes:
  - subdomain: catalog
    provisional_code: AC_LIBRARY_STAFF_V0
    family: AC
    summary: The authorized staff member who performs a catalog operation
    source_finding: {phase: p4, register: actors, key: Authorized staff member}
  - subdomain: catalog
    provisional_code: IN_REGISTER_BOOK_V0
    family: IN
    summary: A request to register a book together with its first physical copy
    source_finding: {phase: p5, register: actions, key: Register}
  - subdomain: catalog
    provisional_code: IN_REGISTER_PHYSICAL_COPY_V0
    family: IN
    summary: A request to register a further copy against a registered book
    source_finding: {phase: p5, register: actions, key: Register}
  - subdomain: catalog
    provisional_code: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    family: IN
    summary: A request to change a registered book's description
    source_finding: {phase: p5, register: actions, key: Update}
  - subdomain: catalog
    provisional_code: IN_RETIRE_BOOK_RECORD_V0
    family: IN
    summary: A request to retire a book record judged obsolete
    source_finding: {phase: p5, register: actions, key: Retire}
  - subdomain: catalog
    provisional_code: IN_RETIRE_PHYSICAL_COPY_V0
    family: IN
    summary: A request to retire a lost or damaged copy
    source_finding: {phase: p5, register: actions, key: Retire}
  - subdomain: catalog
    provisional_code: IN_REINSTATE_BOOK_RECORD_V0
    family: IN
    summary: A request to return a retired book record to the registered state
    source_finding: {phase: p5, register: actions, key: Reinstate}
  - subdomain: catalog
    provisional_code: IN_REINSTATE_PHYSICAL_COPY_V0
    family: IN
    summary: A request to return a retired copy to the registered state
    source_finding: {phase: p5, register: actions, key: Reinstate}
  - subdomain: catalog
    provisional_code: IN_SEARCH_CATALOG_V0
    family: IN
    summary: A request to locate material by subject or by title
    source_finding: {phase: p5, register: actions, key: Search}
  - subdomain: catalog
    provisional_code: IN_RETRIEVE_BOOK_DETAILS_V0
    family: IN
    summary: A request for a book's complete details with the copies held
    source_finding: {phase: p5, register: actions, key: Retrieve}
  - subdomain: catalog
    provisional_code: WF_REGISTER_BOOK_V0
    family: WF
    summary: Registering a book and its first copy, end to end
    source_finding: {phase: p4, register: capability_graph, key: Register a book together with its first physical copy}
  - subdomain: catalog
    provisional_code: WF_REGISTER_PHYSICAL_COPY_V0
    family: WF
    summary: Registering a further copy against a registered book
    source_finding: {phase: p4, register: capability_graph, key: Register a further physical copy against a registered book}
  - subdomain: catalog
    provisional_code: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    family: WF
    summary: Changing a book's description without making it a duplicate
    source_finding: {phase: p4, register: capability_graph, key: Update a book's bibliographic information}
  - subdomain: catalog
    provisional_code: WF_RETIRE_BOOK_RECORD_V0
    family: WF
    summary: Retiring a book record, leaving its copies untouched
    source_finding: {phase: p4, register: capability_graph, key: Retire a book record}
  - subdomain: catalog
    provisional_code: WF_RETIRE_PHYSICAL_COPY_V0
    family: WF
    summary: Retiring a copy, leaving the book record untouched
    source_finding: {phase: p4, register: capability_graph, key: Retire a physical copy}
  - subdomain: catalog
    provisional_code: WF_REINSTATE_BOOK_RECORD_V0
    family: WF
    summary: Returning a retired book record to the registered state
    source_finding: {phase: p4, register: capability_graph, key: Return a retired book record to the registered state}
  - subdomain: catalog
    provisional_code: WF_REINSTATE_PHYSICAL_COPY_V0
    family: WF
    summary: Returning a retired copy to the registered state
    source_finding: {phase: p4, register: capability_graph, key: Return a retired physical copy to the registered state}
  - subdomain: catalog
    provisional_code: WF_SEARCH_CATALOG_V0
    family: WF
    summary: Searching by subject or title, excluding retired books, and recording that it happened
    source_finding: {phase: p4, register: capability_graph, key: 'Search the catalog by subject or title, excluding retired books'}
  - subdomain: catalog
    provisional_code: WF_RETRIEVE_BOOK_DETAILS_V0
    family: WF
    summary: Assembling a book with the copies the library holds of it
    source_finding: {phase: p4, register: capability_graph, key: Retrieve a book's complete details with the copies the library holds}
  - subdomain: catalog
    provisional_code: CC_CONFIRM_STAFF_AUTHORIZED_V0
    family: CC
    summary: Confirm the staff member may perform catalog operations
    source_finding: {phase: p4, register: capability_graph, key: Confirm the staff member performing an operation is authorized}
  - subdomain: catalog
    provisional_code: CC_CLAIM_BOOK_IDENTITY_V0
    family: CC
    summary: Claim a book's identity so a second registration of the same book is refused
    source_finding: {phase: p4, register: capability_graph, key: 'Enforce that one book exists per title, author and publication year'}
  - subdomain: catalog
    provisional_code: CC_CLAIM_COPY_BARCODE_V0
    family: CC
    summary: Claim a copy's barcode so a second copy carrying it is refused
    source_finding: {phase: p4, register: capability_graph, key: Enforce that one physical copy exists per barcode}
  - subdomain: catalog
    provisional_code: CC_REGISTER_BOOK_V0
    family: CC
    summary: Record a book's bibliographic information as the catalog's authoritative description of it
    source_finding: {phase: p4, register: capability_graph, key: Register a book together with its first physical copy}
  - subdomain: catalog
    provisional_code: CC_REGISTER_PHYSICAL_COPY_V0
    family: CC
    summary: Record a copy against exactly one book
    source_finding: {phase: p4, register: capability_graph, key: Register a further physical copy against a registered book}
  - subdomain: catalog
    provisional_code: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    family: CC
    summary: Replace a book's descriptive content, refusing a change that duplicates another book
    source_finding: {phase: p4, register: capability_graph, key: Update a book's bibliographic information}
  - subdomain: catalog
    provisional_code: CC_RETIRE_BOOK_RECORD_V0
    family: CC
    summary: Mark a book record retired so it is no longer offered as current
    source_finding: {phase: p4, register: capability_graph, key: Retire a book record}
  - subdomain: catalog
    provisional_code: CC_RETIRE_PHYSICAL_COPY_V0
    family: CC
    summary: Mark a copy retired so the library no longer holds it
    source_finding: {phase: p4, register: capability_graph, key: Retire a physical copy}
  - subdomain: catalog
    provisional_code: CC_REINSTATE_BOOK_RECORD_V0
    family: CC
    summary: Mark a retired book record registered again
    source_finding: {phase: p4, register: capability_graph, key: Return a retired book record to the registered state}
  - subdomain: catalog
    provisional_code: CC_REINSTATE_PHYSICAL_COPY_V0
    family: CC
    summary: Mark a retired copy registered again
    source_finding: {phase: p4, register: capability_graph, key: Return a retired physical copy to the registered state}
  - subdomain: catalog
    provisional_code: CC_SEARCH_CATALOG_V0
    family: CC
    summary: Select the registered books matching a subject or title, excluding retired ones
    source_finding: {phase: p4, register: capability_graph, key: 'Search the catalog by subject or title, excluding retired books'}
  - subdomain: catalog
    provisional_code: CC_ASSEMBLE_BOOK_DETAILS_V0
    family: CC
    summary: Assemble a book's record with the copies recorded against it
    source_finding: {phase: p4, register: capability_graph, key: Retrieve a book's complete details with the copies the library holds}
  - subdomain: catalog
    provisional_code: CC_APPEND_CATALOG_OPERATION_V0
    family: CC
    summary: Append a durable account of a performed operation to the catalog's own audit trail
    source_finding: {phase: p4, register: capability_graph, key: Record a performed catalog operation in the catalog's audit trail}
  - subdomain: catalog
    provisional_code: CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    family: CT
    summary: Forms the single key claimed for a book from its title, author and publication year
    source_finding: {phase: p4, register: gap_register, key: GAP-06}
  - subdomain: catalog
    provisional_code: CC_VALIDATE_BOOK_SUBMISSION_V0
    family: CC
    summary: Confirms a registration carries what a book record requires, before any identity is claimed
    source_finding: {phase: p4, register: gap_register, key: GAP-06}
  - subdomain: catalog
    provisional_code: CC_RESOLVE_BOOK_IDENTITY_V0
    family: CC
    summary: Resolves a registered book by its identifying key, so an update names the book independently of the attributes it changes
    source_finding: {phase: p4, register: gap_register, key: GAP-08}
  - subdomain: catalog
    provisional_code: EV_BOOK_REGISTERED_V0
    family: EV
    summary: The moment a book enters the catalog
    source_finding: {phase: p4, register: gap_register, key: GAP-16}
  - subdomain: catalog
    provisional_code: EV_PHYSICAL_COPY_REGISTERED_V0
    family: EV
    summary: The moment the library records another copy it owns
    source_finding: {phase: p4, register: gap_register, key: GAP-16}
  - subdomain: catalog
    provisional_code: EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    family: EV
    summary: The moment a book's authoritative description changes
    source_finding: {phase: p4, register: gap_register, key: GAP-16}
  - subdomain: catalog
    provisional_code: EV_BOOK_RETIRED_V0
    family: EV
    summary: The moment a book record is judged obsolete
    source_finding: {phase: p4, register: gap_register, key: GAP-16}
  - subdomain: catalog
    provisional_code: EV_PHYSICAL_COPY_RETIRED_V0
    family: EV
    summary: The moment the library no longer holds a copy
    source_finding: {phase: p4, register: gap_register, key: GAP-16}
  - subdomain: catalog
    provisional_code: RB_CATALOG_BINDINGS_V0
    family: RB
    summary: Binds the catalog's operations to the stores and mechanisms they use
    source_finding: {phase: p4, register: gap_register, key: GAP-03}
  - subdomain: catalog
    provisional_code: STRUCTURE_CATALOG_STORAGE_V0
    family: STRUCTURE
    summary: Declares the stores the catalog owns and the paths they occupy
    source_finding: {phase: p4, register: gap_register, key: GAP-02}
  cross_subdomain_refs: null
```

---

## 1. Subdomain Purpose

### Purpose of every subdomain this change touches

---

## 2. Scope Boundary

---

## 3. Business Objects

No record is ever deleted. Retirement is the only way a record leaves use, and it is reversible, which
is why both record stores hold state as data rather than by which store a record occupies.

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

No capability contract from another subdomain is referenced. The catalog reuses declared mechanisms —
durable records, uniqueness, an append-only trail and four pure transforms — and composes them itself,
so that no catalog operation depends on another subdomain's semantics or writes into its stores.

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
