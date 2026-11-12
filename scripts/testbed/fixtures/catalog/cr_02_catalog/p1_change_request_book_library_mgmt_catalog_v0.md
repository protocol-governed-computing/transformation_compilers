# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p1
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_02_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: catalog
    classification: EXTEND_SUBDOMAIN
    rationale: The change extends the existing catalog function of the existing book_library_mgmt project. It introduces no new library function, adds the Work above the records the previous change established, and withdraws no capability staff have today.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: book_library_mgmt
    definition: The existing project governing the library of books, across ten functions of which catalog is one.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Catalog
    definition: The function holding the library's authoritative description of the materials it holds.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Work
    definition: A published work, recognizable as one thing across the editions in which it is published, identified by its title and author.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Edition
    definition: A publication of a work, identified by its title, author and publication year; editions of one work share a title and an author and differ by publication year. The record the previous change calls a Book is an edition.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Book
    definition: The name the previous change gives to what this change calls an edition.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Edition Summary
    definition: Enough of a description of a work's editions, carried in a search result, for staff to choose the edition they mean.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Work Summary
    definition: A short description of the work an edition belongs to, carried in that edition's retrieval so the work's title need not be looked up separately.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: Bibliographic Information
    definition: An edition's descriptive content, as established by the previous change.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Bibliographic Accuracy
    definition: The catalog describing what the library holds as it actually is, which creating separate book records for editions of one work compromises.
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  - term: Physical Copy
    definition: An individual copy the library owns, belonging to exactly one edition.
    source_finding: {phase: p0, register: business_vocabulary, row: 10}
  - term: Existing Catalog Record
    definition: A catalog record written under the previous governed change, before this one.
    source_finding: {phase: p0, register: business_vocabulary, row: 11}
  - term: Authorized Staff
    definition: A library staff member permitted to perform catalog operations.
    source_finding: {phase: p0, register: business_vocabulary, row: 12}
  - term: Business Operation
    definition: An action performed against the catalog that must be traceable and auditable.
    source_finding: {phase: p0, register: business_vocabulary, row: 13}
  - term: Capability Loss
    definition: An operation withdrawn from staff or a record made unreachable; what this change promises will not happen, as distinct from a behavior deliberately extended.
    source_finding: {phase: p0, register: business_vocabulary, row: 14}
  requested_outcomes:
  - outcome: The catalog can represent a published work that exists in more than one edition.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: Authorized staff can register additional editions of an existing work.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: Authorized staff can search the catalog and receive one result per matching work rather than one per edition.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: Authorized staff can choose the edition they mean from a search result and retrieve that edition's complete details.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: No capability staff have today is withdrawn and no existing record becomes unreachable.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: Records written under the previous governed change remain valid and continue to function without recreation or migration.
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - outcome: Every business operation remains traceable and auditable.
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  known_facts:
  - fact: This change extends the existing book_library_mgmt system.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: 'The overall project scope continues to cover ten library functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: This change extends the existing catalog function and introduces no new library function.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: The purpose of the change is to allow the catalog to represent a published work that exists in more than one edition.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: Many published works exist in multiple editions.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: Editions of one work differ in publication date, publisher, format or content revision while remaining recognizably the same work.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: The current catalog cannot distinguish editions without creating separate book records or compromising bibliographic accuracy.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: The current catalog adequately manages books, physical copies and basic bibliographic information.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: As the collection grows, staff increasingly meet situations that cannot be represented accurately within the current model.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: The record the previous change calls a Book is an edition, and always was; the library did not discover this until it met a work published more than once.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: What this change adds is the Work, the abstraction above the existing record.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: No existing record is redefined, no existing operation is withdrawn, and nothing already catalogued needs recreating.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: An edition is identified by its title, author and publication year — the identity the previous change already established.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: Editions of one work share a title and an author and differ by publication year.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: The identity of title, author and publication year distinguishes editions today and continues to; it was never an identity for the work.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: A work is identified by its title and author.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  - fact: Two works are the same work when their titles and authors match.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 17}
  - fact: A physical copy belongs to exactly one edition, exactly as it belongs to exactly one book today.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 18}
  - fact: Multiple editions do not share physical copies.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 19}
  - fact: Retiring an edition is what retiring a book is today, it cascades to nothing, and an edition may be retired independently of the work's other editions.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 20}
  - fact: A work is not retired; a work whose editions are all retired is simply that.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 21}
  - fact: The first edition creates the work; a work is never registered without an edition, exactly as a book is never registered without a copy.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 22}
  - fact: A search returns one result per matching work, carrying enough of a summary of that work's editions for staff to choose the edition they mean.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 23}
  - fact: Three near-identical results for one work is what the library is trying to stop seeing.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 24}
  - fact: 'Retrieval stays edition retrieval: staff select an edition and receive that edition''s complete details and the physical copies of it, together with a short summary of the work it belongs to.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 25}
  - fact: Each existing catalog record is an edition, grouped under the work its title and author name.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 26}
  - fact: No migration is required; existing records remain valid as written.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 27}
  - fact: A record written before this change is an edition of a work with one edition.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 28}
  - fact: No capability is lost and no existing record becomes unreachable.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 29}
  - fact: 'Search and retrieval are deliberately extended: search groups its results by work, and retrieval carries a summary of the work.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 30}
  - fact: Every other existing operation behaves as it does today.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 31}
  - fact: The promise of no regression is a promise that nothing is lost, not that nothing changes.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 32}
  - fact: Registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete details are the capabilities that must survive this change.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 33}
  - fact: Every business operation shall remain traceable and auditable.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 34}
  - fact: The promise that existing records remain valid is about records written under the previous change and read under this one, and is not satisfied by the catalog merely continuing to compile.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 35}
  - fact: A record written before this change must still be found by search, retrieved in full, updated, retired and reinstated.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 36}
  - fact: Multiple identifiers, a governed subject taxonomy, digital resources and images are further catalog needs the library has, each excluded from this change because each rests on the edition question and could not be settled before it was.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 37}
  - fact: Different publishers, distributors or historical editions may assign different ISBN values to the same publication, and the catalog currently assumes a single identifying value.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 38}
  - fact: What an ISBN identifies — a work, an edition or a printing — is not answerable until an edition is defined.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 39}
  - fact: The library wishes to organize its collection using a governed taxonomy rather than unrestricted subject text, for consistency of cataloging and more accurate searching and reporting.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 40}
  - fact: Library collections increasingly include electronic editions, supplementary downloadable material, publisher resources and external reference links, which staff require the ability to associate with catalog records without changing the circulation model.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 41}
  - fact: Staff require the ability to associate one or more images, such as cover images or scanned illustrations, with catalog records.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 42}
  - fact: Each deferred need is a governed change of its own, in the order the business chooses.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 43}
  - fact: Circulation, patron management, reservations, acquisitions, inventory management, notifications, reporting and staff authorization are excluded from this release, except where existing catalog behavior depends upon them.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 44}
  - fact: The remaining project functions are named, planned, and outside the scope of this governed extension.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 45}
  system_beliefs:
  - belief: The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change.
    why_it_matters: The change is classified EXTEND_SUBDOMAIN on that basis; if the catalog is not present, this is not an extension.
    verification_goal: Confirm the pinned composition carries the book_library_mgmt catalog.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The catalog is believed to hold bibliographic records and physical copies of library materials.
    why_it_matters: 'The change rests on what the existing record describes: the claim that a Book record is already an edition is a claim about those records.'
    verification_goal: Confirm what the catalog's records describe in the pinned composition.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: A book is believed to be identified by title, author and publication year.
    why_it_matters: The whole shape of this change follows from that identity being the edition's and not the work's. If the composition identifies a book differently, editions are not already distinguished.
    verification_goal: Confirm how the composition identifies a book.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: A physical copy is believed to belong to exactly one book.
    why_it_matters: It is what makes a copy already a copy of an edition, with no change to copies at all.
    verification_goal: Confirm what a physical copy is registered against in the composition.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details.
    why_it_matters: These are the capabilities that must survive; the claim that nothing is lost cannot be tested against capabilities that do not exist as believed.
    verification_goal: Confirm which catalog operations the composition provides.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  - belief: A retired record is believed to be reinstatable.
    why_it_matters: The existing-records promise requires a record written before this change to be retired and reinstated after it.
    verification_goal: Confirm whether the composition provides reinstatement.
    source_finding: {phase: p0, register: system_beliefs, row: 6}
  - belief: Records written under the previous change are believed to exist and to be readable.
    why_it_matters: The existing-records promise is about data, and is unfalsifiable if no such data exists.
    verification_goal: Confirm that records written by the previous catalog capability can be read.
    source_finding: {phase: p0, register: system_beliefs, row: 7}
  assumptions:
  - assumption: The ten project functions and the deferred catalog needs are named to establish future scope, not to be governed by this change.
    basis: The statement names them and declares each excluded from this change.
    source_finding: {phase: p0, register: assumptions, row: 1}
  constraints:
  - constraint: No capability staff have today may be withdrawn and no existing record may become unreachable.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: Existing catalog records must remain valid without recreation or migration, demonstrated against records written under the previous change.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: Only search and retrieval may be extended; every other existing operation must behave as it does today.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: Multiple identifiers, governed subject taxonomy, digital resources and images must not be designed into this change.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 4}
  - constraint: Every business operation must remain traceable and auditable.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 5}
  business_invariants:
  - invariant: Each edition belongs to exactly one work.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: Each physical copy belongs to exactly one edition.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: No two works share the same title and author.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No two editions of a work share the same publication year.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: Every work has at least one edition.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: A record written under the previous change remains valid and usable without recreation.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: Every business operation performed against the catalog is traceable and auditable.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  - invariant: The catalog describes what the library holds without compromising bibliographic accuracy.
    source_finding: {phase: p0, register: business_invariants, row: 8}
  lifecycle_states:
  - object: Work
    state: Registered
    meaning: The work has been registered with its first edition and the catalog holds its authoritative record.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Edition
    state: Registered
    meaning: The edition has been registered against exactly one work; this is what the previous change calls a registered book.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Edition
    state: Retired
    meaning: The edition's record has been judged obsolete and is no longer to be used; this is what the previous change calls a retired book, and staff may return it to Registered.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: Physical Copy
    state: Registered
    meaning: The copy has been registered against exactly one edition.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  - object: Physical Copy
    state: Retired
    meaning: The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered.
    source_finding: {phase: p0, register: lifecycle_states, row: 5}
  business_events:
  - event: Work Registered
    when_it_occurs: When authorized staff register an edition of a work the catalog does not yet hold.
    significance: A work enters the catalog, created by the edition that evidences it.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: Edition Registered
    when_it_occurs: When authorized staff register an additional edition of an existing work.
    significance: The catalog records a further edition of a work it already holds.
    source_finding: {phase: p0, register: business_events, row: 2}
  authority_boundaries:
  - business_object: Work record
    authoritative_owner: Catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: Edition record
    authoritative_owner: Catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Physical copy record
    authoritative_owner: Catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: Existing catalog records
    authoritative_owner: Catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  - business_object: The judgement that an edition is obsolete
    authoritative_owner: Authorized staff
    source_finding: {phase: p0, register: authority_boundaries, row: 5}
  out_of_scope:
  - item: Multiple identifiers
    reason: A further catalog need, deferred to a governed change of its own; what an ISBN identifies could not be answered until an edition was defined.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Governed subject taxonomy
    reason: A further catalog need, deferred to a governed change of its own.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Digital resources
    reason: A further catalog need, deferred to a governed change of its own.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Images
    reason: A further catalog need, deferred to a governed change of its own.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: Retirement of a work
    reason: A work is not retired; a work whose editions are all retired is simply that.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  - item: Migration of existing records
    reason: No migration is required; existing records remain valid as written.
    source_finding: {phase: p0, register: out_of_scope, row: 6}
  - item: Circulation
    reason: Excluded from this release, except where existing catalog behavior depends upon it.
    source_finding: {phase: p0, register: out_of_scope, row: 7}
  - item: Patron management
    reason: Excluded from this release, except where existing catalog behavior depends upon it.
    source_finding: {phase: p0, register: out_of_scope, row: 8}
  - item: Reservations
    reason: Excluded from this release, except where existing catalog behavior depends upon it.
    source_finding: {phase: p0, register: out_of_scope, row: 9}
  - item: Acquisitions
    reason: Excluded from this release, except where existing catalog behavior depends upon it.
    source_finding: {phase: p0, register: out_of_scope, row: 10}
  - item: Inventory management
    reason: Excluded from this release, except where existing catalog behavior depends upon it.
    source_finding: {phase: p0, register: out_of_scope, row: 11}
  - item: Notifications
    reason: Excluded from this release, except where existing catalog behavior depends upon it.
    source_finding: {phase: p0, register: out_of_scope, row: 12}
  - item: Reporting
    reason: Excluded from this release, except where existing catalog behavior depends upon it.
    source_finding: {phase: p0, register: out_of_scope, row: 13}
  - item: Staff authorization
    reason: Excluded from this release, except where existing catalog behavior depends upon it.
    source_finding: {phase: p0, register: out_of_scope, row: 14}
  - item: Policy
    reason: A project function, adjacent to this change and outside its scope.
    source_finding: {phase: p0, register: out_of_scope, row: 15}
  governance_scope:
  - scope_item: catalog
    relationship: EXTENDED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: circulation
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 2}
  - scope_item: patron
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 3}
  - scope_item: staff
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 4}
  - scope_item: reservations
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 5}
  - scope_item: acquisitions
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 6}
  - scope_item: inventory
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 7}
  - scope_item: notifications
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 8}
  - scope_item: policy
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 9}
  - scope_item: reporting
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 10}
  clarification_requests: null
  acceptance_criteria:
  - criterion: Authorized staff can register an edition of a work the catalog does not yet hold, and the catalog then holds one work with one edition.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: Authorized staff can register an additional edition of an existing work, and it is recorded against that work only.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: A registration whose title, author and publication year match a registered edition is refused.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Two editions sharing a title and an author, differing by publication year, are grouped under one work.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: A search for a work with three editions returns one result, not three.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: A search result carries enough of a summary of the work's editions for staff to choose the edition they mean.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Authorized staff can select an edition from a search result and retrieve that edition's complete details and the physical copies of it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: A retrieval carries a summary of the work the edition belongs to, so the work's title need not be looked up separately.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: Authorized staff can register a physical copy against an edition, and it is recorded against that edition only.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: Authorized staff can retire an edition, and the work's other editions are unaffected.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: Authorized staff can return a retired edition to the registered state.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  - criterion: Registering a physical copy behaves as it did before this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 12}
  - criterion: Updating bibliographic information behaves as it did before this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 13}
  - criterion: Retiring a record behaves as it did before this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 14}
  - criterion: A record written under the previous change is found by search after this change, without having been recreated or migrated.
    source_finding: {phase: p0, register: acceptance_criteria, row: 15}
  - criterion: A record written under the previous change is retrieved in full after this change, without having been recreated or migrated.
    source_finding: {phase: p0, register: acceptance_criteria, row: 16}
  - criterion: A record written under the previous change can be updated after this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 17}
  - criterion: A record written under the previous change can be retired after this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 18}
  - criterion: A record written under the previous change can be reinstated after this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 19}
  - criterion: A record written under the previous change appears as an edition of a work with one edition.
    source_finding: {phase: p0, register: acceptance_criteria, row: 20}
  - criterion: No operation staff had before this change has been withdrawn.
    source_finding: {phase: p0, register: acceptance_criteria, row: 21}
  - criterion: Every business operation performed against the extended catalog can be traced and audited afterwards.
    source_finding: {phase: p0, register: acceptance_criteria, row: 22}
  identity_and_sameness:
  - business_object: Work
    identified_by: Its title and author together.
    two_are_the_same_when: Their titles and authors match.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: Edition
    identified_by: Its title, author and publication year together, as the previous change established.
    two_are_the_same_when: Their publication year matches and their titles and authors match.
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  - business_object: Physical Copy
    identified_by: The barcode the library assigns to it.
    two_are_the_same_when: Their barcodes match.
    source_finding: {phase: p0, register: identity_and_sameness, row: 3}
  lifecycle_transitions:
  - object: Work
    from_state: null
    to_state: Registered
    triggered_by: Authorized staff register an edition of a work the catalog does not yet hold.
    cascade: None beyond the first edition being registered with it.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Edition
    from_state: null
    to_state: Registered
    triggered_by: Authorized staff register an edition against a work, existing or created by this registration.
    cascade: None — the work's other editions are unaffected.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  - object: Edition
    from_state: Registered
    to_state: Retired
    triggered_by: Authorized staff judge the edition's record obsolete and retire it.
    cascade: None — the work's other editions and the edition's physical copies are unaffected.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 3}
  - object: Edition
    from_state: Retired
    to_state: Registered
    triggered_by: Authorized staff return the retired edition to the registered state.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 4}
  - object: Physical Copy
    from_state: null
    to_state: Registered
    triggered_by: Authorized staff register the copy against a registered edition.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 5}
  - object: Physical Copy
    from_state: Registered
    to_state: Retired
    triggered_by: Authorized staff retire a copy that is lost or damaged.
    cascade: None — the edition is unaffected, including when it is the last copy.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 6}
  - object: Physical Copy
    from_state: Retired
    to_state: Registered
    triggered_by: Authorized staff return the retired copy to the registered state.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 7}
  operation_refusals:
  - operation: Register an edition
    refused_when: Its title, author and publication year match a registered edition.
    business_reason: That identity identifies an edition; the edition already exists, and a further copy is what staff register instead.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Register an edition
    refused_when: No work is named and none is created with it.
    business_reason: Every edition belongs to exactly one work.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Register a work
    refused_when: No edition is offered with it.
    business_reason: The first edition creates the work; a work is never registered without an edition.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Register a physical copy
    refused_when: The edition it names is not registered.
    business_reason: Each physical copy belongs to exactly one edition.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Retire a work
    refused_when: Always.
    business_reason: A work is not retired; a work whose editions are all retired is simply that.
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    business_reason: Only authorized staff may perform catalog operations.
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  authority_deferrals:
  - business_object: Identifiers assigned to a publication, including multiple ISBN values
    deferred_to: A follow-on governed change for identifiers
    until: This change defines an edition.
    source_finding: {phase: p0, register: authority_deferrals, row: 1}
  - business_object: A governed subject taxonomy
    deferred_to: A follow-on governed change for taxonomy
    until: The business chooses to take it up.
    source_finding: {phase: p0, register: authority_deferrals, row: 2}
  - business_object: Digital resources associated with catalog records
    deferred_to: A follow-on governed change for digital resources
    until: The business chooses to take it up.
    source_finding: {phase: p0, register: authority_deferrals, row: 3}
  - business_object: Images associated with catalog records
    deferred_to: A follow-on governed change for images
    until: The business chooses to take it up.
    source_finding: {phase: p0, register: authority_deferrals, row: 4}
  - business_object: Which staff are authorized
    deferred_to: The staff function
    until: A future governed change introduces staff authorization.
    source_finding: {phase: p0, register: authority_deferrals, row: 5}
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
