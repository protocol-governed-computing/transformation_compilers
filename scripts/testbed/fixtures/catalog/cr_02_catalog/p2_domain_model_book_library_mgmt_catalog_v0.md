# Stage 2 — Domain Model Verification: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p2
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_02_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Work
    description: A published work, recognizable as one thing across the editions in which it is published.
    store_model: None — the composition holds no store for a work, and nothing groups records that describe one.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Edition
    description: A publication of a work, identified by title, author and publication year. The record the previous change calls a book is an edition.
    store_model: A durable record store keyed by the identifying attributes, holding one record per edition.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - entity: Physical Copy
    description: An individual copy the library owns, belonging to exactly one edition.
    store_model: A durable record store keyed by barcode, holding one record per copy.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - entity: Bibliographic Information
    description: An edition's descriptive content.
    store_model: Held within the edition's own record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - entity: Edition Summary
    description: Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean.
    store_model: None — search results carry one edition's bibliographic information and nothing about a work.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - entity: Work Summary
    description: A short description of the work an edition belongs to, carried in that edition's retrieval.
    store_model: None — retrieval carries the edition and its copies and nothing about a work.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - entity: Existing Catalog Record
    description: A catalog record written under the previous governed change, before this one.
    store_model: The same store the edition occupies; the composition declares the store, not its contents.
    evidence_status: INFERRED
    source_finding: {phase: p2, register: belief_verification, row: 7}
  - entity: Authorized Staff
    description: A library staff member permitted to perform catalog operations.
    store_model: None — the catalog requires authorization and does not decide it.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - entity: Business Operation
    description: An action performed against the catalog that must be traceable and auditable.
    store_model: An append-only trail holding one entry per performed operation.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  entity_attributes:
  - entity: Work
    attribute: Title
    meaning: The work's title, shared by every edition of it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Work
    attribute: Author
    meaning: The work's author, shared by every edition of it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Edition
    attribute: Title
    meaning: The edition's title, one of the three attributes that identify it.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Edition
    attribute: Author
    meaning: The edition's author, one of the three attributes that identify it.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Edition
    attribute: Publication Year
    meaning: The year of publication, the attribute that distinguishes one edition of a work from another.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Edition
    attribute: Subject
    meaning: What kind of material it is, stated as free text, and what staff search on.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - entity: Edition
    attribute: State
    meaning: Whether the edition's record is registered or retired.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 6}
  - entity: Edition
    attribute: Identifying Key
    meaning: The single value formed from title, author and publication year, claimed so that no two editions share it.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Physical Copy
    attribute: Barcode
    meaning: The identifier the library assigns to a copy, which distinguishes it from every other copy.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - entity: Physical Copy
    attribute: Edition Identity
    meaning: The edition the copy belongs to, recorded on the copy.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - entity: Physical Copy
    attribute: State
    meaning: Whether the copy's record is registered or retired.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 6}
  - entity: Business Operation
    attribute: Operation Record
    meaning: What was performed, by whom, against which record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  business_processes:
  - process: Register an edition of a work the catalog does not yet hold
    initiator: Authorized staff
    outcome: The work enters the catalog with its first edition and that edition's first copy.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Register an additional edition of an existing work
    initiator: Authorized staff
    outcome: A further edition is recorded against a work the catalog already holds.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Search the catalog
    initiator: Authorized staff
    outcome: One result per matching work, carrying enough of a summary of that work's editions to choose one.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Retrieve an edition's complete details
    initiator: Authorized staff
    outcome: The edition's bibliographic information, the physical copies of it, and a summary of the work it belongs to.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Register a physical copy
    initiator: Authorized staff
    outcome: A copy is recorded against exactly one edition.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - process: Update bibliographic information
    initiator: Authorized staff
    outcome: A registered edition's descriptive content changes.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Retire a record
    initiator: Authorized staff
    outcome: An edition or a copy is judged obsolete and is no longer to be used.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Reinstate a record
    initiator: Authorized staff
    outcome: A retired edition or copy returns to the registered state.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 6}
  process_steps:
  - process: Register an edition of a work the catalog does not yet hold
    step: '1'
    action: Confirm the staff member is authorized.
    record_produced: None
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Register an edition of a work the catalog does not yet hold
    step: '2'
    action: Validate the submission carries what an edition requires.
    record_produced: None
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Register an edition of a work the catalog does not yet hold
    step: '3'
    action: Claim the work, identified by title and author.
    record_produced: A work record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - process: Register an edition of a work the catalog does not yet hold
    step: '4'
    action: Claim the edition's identity, so no two editions share title, author and publication year.
    record_produced: An identity claim
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - process: Register an edition of a work the catalog does not yet hold
    step: '5'
    action: Claim the first copy's barcode.
    record_produced: A barcode claim
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - process: Register an edition of a work the catalog does not yet hold
    step: '6'
    action: Write the edition record and its first copy record.
    record_produced: An edition record and a copy record
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - process: Register an edition of a work the catalog does not yet hold
    step: '7'
    action: Record the operation in the audit trail.
    record_produced: An operation entry
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Register an additional edition of an existing work
    step: '1'
    action: Confirm the staff member is authorized.
    record_produced: None
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Register an additional edition of an existing work
    step: '2'
    action: Resolve the work the edition belongs to, by title and author.
    record_produced: None
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - process: Register an additional edition of an existing work
    step: '3'
    action: Claim the edition's identity, so no two editions of the work share a publication year.
    record_produced: An identity claim
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - process: Register an additional edition of an existing work
    step: '4'
    action: Write the edition record against the resolved work.
    record_produced: An edition record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Register an additional edition of an existing work
    step: '5'
    action: Record the operation in the audit trail.
    record_produced: An operation entry
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Search the catalog
    step: '1'
    action: Confirm the staff member is authorized.
    record_produced: None
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Search the catalog
    step: '2'
    action: Select the registered editions matching the stated subject or title, excluding retired ones.
    record_produced: None
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Search the catalog
    step: '3'
    action: Group the matching editions by the work they belong to.
    record_produced: None
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Search the catalog
    step: '4'
    action: Return one result per work, carrying a summary of its matching editions.
    record_produced: A search result
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Retrieve an edition's complete details
    step: '1'
    action: Confirm the staff member is authorized.
    record_produced: None
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Retrieve an edition's complete details
    step: '2'
    action: Read the named edition and the physical copies of it.
    record_produced: None
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - process: Retrieve an edition's complete details
    step: '3'
    action: Read a summary of the work the edition belongs to.
    record_produced: None
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Retrieve an edition's complete details
    step: '4'
    action: Return the edition, its copies and the work summary.
    record_produced: A retrieval result
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  belief_verification:
  - belief: The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change.
    result: VERIFIED
    evidence: The pinned composition declares six domains and carries forty-three artifacts in the book_library_mgmt namespace, among them book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 and book_library_mgmt::RB_CATALOG_BINDINGS_V0, which declare the subdomain's stores and bind its workflows to them.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The catalog is believed to hold bibliographic records and physical copies of library materials.
    result: VERIFIED
    evidence: 'book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 declares five stores: one for book records, one for physical copies, an append-only operations trail, and two uniqueness registries. book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 write the first two.'
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: A book is believed to be identified by title, author and publication year.
    result: VERIFIED
    evidence: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 forms one key from exactly those three attributes, and book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 claims that key so a second record carrying the same three is refused. book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 resolves a record by the same key.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: A physical copy is believed to belong to exactly one book.
    result: VERIFIED
    evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 records a copy against one book record, and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 claims its barcode so no two copies share one.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details.
    result: VERIFIED
    evidence: 'Nine workflows serve them: book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::WF_SEARCH_CATALOG_V0, book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0. Every one admits only an authorized staff member, through book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0.'
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - belief: A retired record is believed to be reinstatable.
    result: VERIFIED
    evidence: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0 return a retired record to the registered state, reached through book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0.
    source_finding: {phase: p1, register: system_beliefs, row: 6}
  - belief: Records written under the previous change are believed to exist and to be readable.
    result: INSUFFICIENT_EVIDENCE
    evidence: The composition declares the stores and the paths they occupy; it does not carry their contents. Whether any record was ever written is runtime state, and no inspection of a sealed snapshot can answer it. The belief is resolvable only by reading a store the previous change wrote.
    source_finding: {phase: p1, register: system_beliefs, row: 7}
  pps_baseline_fqdns:
  - capability: Catalog storage declaration
    fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    what_it_does: Declares the five stores the catalog owns and the paths they occupy.
    fit: PARTIAL
    cannot_do: It declares no store for a work, and no store in which the grouping of editions under a work could be held.
  - capability: Edition identity key
    fqdn: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    what_it_does: Forms one key from title, author and publication year.
    fit: EXACT
    cannot_do: It forms an edition's key; the work's key of title and author alone is not a key it forms.
  - capability: Edition identity claim
    fqdn: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    what_it_does: Claims the identifying key so that no two records share title, author and publication year.
    fit: EXACT
    cannot_do: It claims one edition; it neither claims a work nor relates two editions that share a title and an author.
  - capability: Edition identity resolution
    fqdn: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    what_it_does: Resolves a registered record by its identifying key.
    fit: EXACT
    cannot_do: It resolves one edition by its own key and cannot answer which work an edition belongs to.
  - capability: Register an edition
    fqdn: book_library_mgmt::CC_REGISTER_BOOK_V0
    what_it_does: Confirms authorization, validates the submission, claims identity and barcode, writes the record and its first copy, and records the operation.
    fit: PARTIAL
    cannot_do: It registers an edition standing alone; nothing in it claims or resolves the work the edition belongs to.
  - capability: Validate a submission
    fqdn: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    what_it_does: Confirms a registration carries what a record requires before anything is claimed or written.
    fit: PARTIAL
    cannot_do: It validates an edition's own attributes and knows nothing a work would require.
  - capability: Register a physical copy
    fqdn: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    what_it_does: Records a copy against one existing record and claims its barcode.
    fit: EXACT
    cannot_do: Nothing — a copy already belongs to exactly one edition, which is what this change requires of it.
  - capability: Barcode claim
    fqdn: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    what_it_does: Claims a copy's barcode so no two copies share one.
    fit: EXACT
    cannot_do: It is unaffected by the work abstraction.
  - capability: Search the catalog
    fqdn: book_library_mgmt::CC_SEARCH_CATALOG_V0
    what_it_does: Selects registered records matching a stated subject or title and excludes retired ones.
    fit: PARTIAL
    cannot_do: It returns one result per matching edition. It cannot group editions under the work they belong to, and returns three near-identical results where the library wants one.
  - capability: Retrieve complete details
    fqdn: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    what_it_does: Assembles one record's bibliographic information together with the physical copies of it.
    fit: PARTIAL
    cannot_do: It carries no summary of the work the record belongs to, so the work's title cannot be shown without a second lookup.
  - capability: Update bibliographic information
    fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    what_it_does: Changes a registered record's descriptive content and refuses a change that would duplicate another record.
    fit: EXACT
    cannot_do: It refuses duplication at the edition level, which is where this change leaves it.
  - capability: Retire a record
    fqdn: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    what_it_does: Retires one record and cascades to nothing.
    fit: EXACT
    cannot_do: It retires an edition, which is what this change requires; a work is not retired.
  - capability: Retire a physical copy
    fqdn: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    what_it_does: Retires one copy and leaves its record unaffected.
    fit: EXACT
    cannot_do: It is unaffected by the work abstraction.
  - capability: Reinstate a record
    fqdn: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    what_it_does: Returns a retired record to the registered state.
    fit: EXACT
    cannot_do: It is unaffected by the work abstraction.
  - capability: Reinstate a physical copy
    fqdn: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    what_it_does: Returns a retired copy to the registered state.
    fit: EXACT
    cannot_do: It is unaffected by the work abstraction.
  - capability: Audit the operation
    fqdn: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    what_it_does: Appends one performed operation to the catalog's own append-only trail.
    fit: EXACT
    cannot_do: It records whatever operation it is handed, including ones this change adds.
  - capability: Staff authorization check
    fqdn: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    what_it_does: Confirms the staff member performing an operation is authorized.
    fit: EXACT
    cannot_do: It requires authorization and does not decide it, which this change leaves unchanged.
  - capability: Catalog entry points
    fqdn: book_library_mgmt::IN_REGISTER_BOOK_V0
    what_it_does: Admits a registration request and declares what a caller must supply.
    fit: PARTIAL
    cannot_do: It admits an edition's attributes and names no work.
  - capability: Search entry point
    fqdn: book_library_mgmt::IN_SEARCH_CATALOG_V0
    what_it_does: Admits a search request stating a subject or a title.
    fit: EXACT
    cannot_do: It admits the search terms this change keeps; what changes is the shape of the answer.
  - capability: Retrieval entry point
    fqdn: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    what_it_does: Admits a request for one record's complete details.
    fit: PARTIAL
    cannot_do: It names the record to retrieve and carries nothing that would ask for the work.
  - capability: Runtime binding declaration
    fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    what_it_does: Binds the catalog's workflows to the stores and policies they use.
    fit: PARTIAL
    cannot_do: It binds the five stores that exist; a store for works would have to be bound here too.
  - capability: Business moments
    fqdn: book_library_mgmt::EV_BOOK_REGISTERED_V0
    what_it_does: Declares the moment a record enters the catalog.
    fit: PARTIAL
    cannot_do: It names the registration of an edition; the moment a work enters the catalog has no declaration.
  - capability: Durable record store
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    what_it_does: Writes, reads, selects, lists, updates in place and deletes durable records.
    fit: EXACT
    cannot_do: It holds whatever it is given; it enforces no identity and no grouping.
  - capability: Uniqueness registry
    fqdn: capability_side_effects::CS_REGISTRY_V0
    what_it_does: Registers a key, resolves it, and reports whether it exists.
    fit: EXACT
    cannot_do: It enforces uniqueness on one key; grouping editions under a work is not something it expresses.
  - capability: Record selection
    fqdn: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    what_it_does: Selects the records matching stated criteria.
    fit: PARTIAL
    cannot_do: It selects records; it does not group the selected records by an attribute they share.
  gaps:
  - gap: The catalog has no work — nothing in the composition represents the thing that several editions are editions of.
    severity: CRITICAL
    impact: 'Every outcome this change requests rests on it: an additional edition has nothing to be registered against, a search cannot group by it, and a retrieval cannot summarise it.'
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: No store holds a work, and the storage declaration has no place to put one.
    severity: CRITICAL
    impact: A work that is derived at read time and never recorded cannot be claimed, cannot be resolved, and cannot be shown to have exactly one authoritative record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: Nothing claims a work's identity of title and author, as the edition's identity of title, author and publication year is claimed.
    severity: CRITICAL
    impact: Without a claim, two registrations describing the same work would produce two works, and the invariant that no two works share a title and an author is unenforceable.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: Search returns one result per matching edition and cannot group its results by work.
    severity: CRITICAL
    impact: The requested outcome is one result per work carrying a summary of its editions; the existing search answers a different question.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - gap: Retrieval carries no summary of the work a record belongs to.
    severity: CRITICAL
    impact: Staff selecting an edition from a search result would have to look the work up separately, which is what carrying the summary exists to avoid.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - gap: Registering an edition neither resolves nor creates the work it belongs to.
    severity: CRITICAL
    impact: Registering an additional edition of an existing work is the change's central operation and has no path through the existing registration.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - gap: Records written under the previous change carry no work membership, and whether any such record exists cannot be established from the composition.
    severity: OPEN QUESTION
    impact: The promise that existing records remain valid without recreation is about data. It is not testable against a snapshot, only against a store the previous change wrote.
    evidence_status: INFERRED
    source_finding: {phase: p2, register: belief_verification, row: 7}
  - gap: No business moment is declared for a work entering the catalog.
    severity: MINOR
    impact: The moments this change adds would go unrecognised while the edition's own moments continue to be declared.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: Deciding which staff are authorized still belongs to a function that does not exist.
    severity: MINOR
    impact: Unchanged by this change, and deferred by the business to the staff function.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  architectural_observations:
  - observation: The record the previous change calls a book is identified by exactly the three attributes that identify an edition, and two records differing only in publication year are already two records. The existing catalog therefore already distinguishes editions, and what it has never had is the work above them.
    evidence: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 · book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - observation: A physical copy is recorded against one record and claims its own barcode, so a copy already belongs to exactly one edition and needs no change at all.
    evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 · book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - observation: Uniqueness in this composition is claimed through a registry keyed on one value, and the existing edition key is formed by a pure transform before it is claimed. A work's key of title and author could be formed and claimed the same way.
    evidence: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 · capability_side_effects::CS_REGISTRY_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - observation: Every catalog operation is composed as an ordered pipeline that confirms authorization first and records the operation last, so an operation this change adds has a worked shape to follow.
    evidence: book_library_mgmt::CC_REGISTER_BOOK_V0 · book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 · book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - observation: Selecting records by stated criteria is available as a pure transform, and grouping the selected records by an attribute they share is not.
    evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - observation: The subdomain owns its five stores and binds its own workflows to them, so a store for works would be declared and bound in the subdomain's own declarations.
    evidence: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 · book_library_mgmt::RB_CATALOG_BINDINGS_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - observation: Retirement is declared on the record the previous change calls a book and cascades to nothing, which is exactly what retiring an edition independently of a work's other editions requires.
    evidence: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 · book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 6}
  discovery_concerns:
  - concern: The promise that existing records remain valid without recreation cannot be verified at this stage at all. The composition declares stores and paths; it does not carry what is in them, and a snapshot has no way to say whether the previous change ever wrote a record. The promise is a claim about data, and only execution against a store the previous change wrote can settle it.
    evidence: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    severity: CRITICAL
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 7}
  - concern: The existing search is the one existing capability whose answer this change alters, and it is also the one every existing acceptance criterion about search was written against. Grouping its results by work changes the shape of what staff already receive, and the business has accepted that as an extension rather than a regression.
    evidence: book_library_mgmt::CC_SEARCH_CATALOG_V0
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - concern: The work an existing record belongs to is derivable from the record's own title and author, but deriving it at read time and recording it are different things. If a work is claimed, every record written before this change needs a claim it never made; if it is not, the work has no authoritative record.
    evidence: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    severity: MAJOR
    evidence_status: INFERRED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - concern: The registration this change extends already claims two identities and writes two records before it audits, and it was reordered during the previous change so that every claim precedes every write. Adding a work claim to it touches the sequence that ordering was established to protect.
    evidence: book_library_mgmt::CC_REGISTER_BOOK_V0 · book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition, and every other
register projects from those resolutions. This is the first change request whose baseline contains a
subdomain the pipeline itself built: what already exists here is the previous catalog change's own
output.

---

## 1. Business Entities

### Entity Attributes

---

## 2. Business Processes

### Process Steps

---

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
