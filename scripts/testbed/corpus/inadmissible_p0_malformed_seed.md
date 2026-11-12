# Change Seed — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
document:
  phase: p0
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_01_catalog
registers:
  subdomain_purpose: ''
  cr_type:
  - subdomain: catalog
    classification: NEW_SUBDOMAIN
  business_vocabulary:
  - term: book_library_mgmt
    definition: The project governing the library of books, across ten functions of which catalog is the first.
  - term: Catalog
    definition: The function holding the library's authoritative description of the materials it holds.
  - term: Book
    definition: A published material the library catalogs, identified by its title, author and publication year. The general term for anything the library catalogs, including published materials that are not books.
  - term: Bibliographic Information
    definition: 'A book''s descriptive content: title, author, publication year and subject.'
  - term: Subject
    definition: What kind of book it is, stated as free text; what staff search on when looking for material rather than for a known title.
  - term: Physical Copy
    definition: An individual copy the library owns, belonging to exactly one book, identified by its barcode.
  - term: Barcode
    definition: The identifier the library assigns to a physical copy, which distinguishes that copy from every other copy the library owns.
  - term: Catalog Record
    definition: The single authoritative record for one book or one physical copy.
  - term: Book Details
    definition: 'The complete description of a registered book: its bibliographic information and the physical copies the library holds of it.'
  - term: Obsolete Record
    definition: A catalog record the library has determined is no longer to be used.
  - term: Authorized Staff
    definition: A library staff member permitted to perform catalog operations.
  - term: Business Operation
    definition: An action performed against the catalog that must be traceable and auditable.
  requested_outcomes:
  - outcome: A single authoritative record exists for each book the library holds.
  - outcome: A single authoritative record exists for each physical copy the library owns.
  - outcome: Authorized staff can register new books, register physical copies, update bibliographic information, retire obsolete records, search the catalog, and retrieve complete book details.
  - outcome: Catalog descriptions are consistent and duplicate entries no longer occur.
  - outcome: Materials can be located by what kind of book they are, without the difficulty the manual catalog produces.
  - outcome: Every business operation performed against the catalog is traceable and auditable.
  known_facts:
  - fact: The proposed name of the project is book_library_mgmt.
    certainty: HIGH
  - fact: 'The project scope covers ten functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting.'
    certainty: HIGH
  - fact: The scope of this change request is limited to the catalog function only.
    certainty: HIGH
  - fact: A community library maintains thousands of books and other published materials.
    certainty: HIGH
  - fact: '"Book" is the general term for anything the library catalogs, including published materials that are not books.'
    certainty: HIGH
  - fact: Catalog records are maintained manually today.
    certainty: HIGH
  - fact: Manual maintenance produces inconsistent descriptions, duplicate entries, and difficulty locating materials.
    certainty: HIGH
  - fact: The library requires a governed catalog management capability providing a single authoritative record for each book and each physical copy it owns.
    certainty: HIGH
  - fact: A book's bibliographic information is its title, author, publication year and subject.
    certainty: HIGH
  - fact: A book carries at least one subject and may carry several.
    certainty: HIGH
  - fact: Subject says what kind of book it is, and is what staff search on when looking for material rather than for a known title.
    certainty: HIGH
  - fact: A book's subject is free text; the library maintains no list of permitted subjects.
    certainty: HIGH
  - fact: Staff search the catalog by subject or by title.
    certainty: HIGH
  - fact: A search returns the bibliographic information of each matching registered book, and nothing about its physical copies.
    certainty: HIGH
  - fact: Title, author and publication year together identify a book.
    certainty: HIGH
  - fact: Title and author are compared without regard to letter case or repeated spacing; case and spacing do not change which book is meant.
    certainty: HIGH
  - fact: UNRESOLVED
    certainty: HIGH
  - fact: Registering a book requires at least one physical copy; a book is never registered without a copy.
    certainty: HIGH
  - fact: Each physical copy carries a barcode the library assigns, which identifies that copy among all the copies the library owns.
    certainty: HIGH
  - fact: A physical copy may be retired on its own, when it is lost or damaged.
    certainty: HIGH
  - fact: A physical copy may be registered against a retired book.
    certainty: HIGH
  - fact: A catalog record is never deleted; retirement is the only way a record leaves use.
    certainty: HIGH
  - fact: Authorized staff may return a retired book record or a retired physical copy to the registered state.
    certainty: HIGH
  - fact: An update to bibliographic information may change the title, author or publication year.
    certainty: HIGH
  - fact: An update is refused when the changed title, author and publication year would match another registered book.
    certainty: HIGH
  - fact: 'No retirement follows automatically from another: retiring a book does not retire its copies, and retiring the last copy does not retire the book.'
    certainty: HIGH
  - fact: A registration whose title, author and publication year match a registered book is refused, because the book already exists.
    certainty: HIGH
  - fact: A retired book is excluded from search results, and its details remain retrievable.
    certainty: HIGH
  - fact: Retrieving complete book details returns the book's bibliographic information and the physical copies the library holds of it.
    certainty: HIGH
  - fact: The catalog does not manage which staff are authorized; it requires staff to be authorized.
    certainty: HIGH
  - fact: Deciding who is authorized belongs to the staff function, which governs library employees.
    certainty: HIGH
  - fact: Patrons are library users, not employees, and the patron function does not decide staff authorization.
    certainty: HIGH
  - fact: Only authorized staff may perform catalog operations.
    certainty: HIGH
  - fact: Every business operation must be traceable and auditable.
    certainty: HIGH
  - fact: The catalog starts empty; the records staff maintain manually today are not imported by this change.
    certainty: HIGH
  - fact: 'The operations required of the catalog are: register a new book, register a physical copy, update bibliographic information, retire an obsolete record, search the catalog, retrieve complete book details.'
    certainty: HIGH
  - fact: Borrowing, reservations, fines, patron management, acquisitions and inventory reconciliation are excluded from this release.
    certainty: HIGH
  - fact: The excluded capabilities are expected to be introduced through future governed change requests.
    certainty: HIGH
  - fact: The excluded capabilities must not be designed into the initial solution.
    certainty: HIGH
  system_beliefs:
  - belief: book_library_mgmt does not appear to be part of the current software baseline.
    why_it_matters: The change is classified NEW_SUBDOMAIN on that basis; if the project already exists, this is an extension and its scope is different.
    certainty: MEDIUM
    verification_goal: Confirm no artifact in the pinned composition carries the book_library_mgmt namespace.
  - belief: No capability in the current composition manages a library catalog.
    why_it_matters: This change exists to fill that gap; if such a capability exists, the change becomes a reuse or an extension.
    certainty: HIGH
    verification_goal: Confirm nothing in the composition registers, describes, searches or retires a catalog record.
  assumptions:
  - assumption: '"Thousands of books" describes the size of the collection and states no performance requirement.'
    basis: Confirmed by the business author; the statement names no performance target.
  - assumption: The library is treated as a single collection; no branch or location distinction is required.
    basis: Confirmed by the business author; the statement names no branch or location.
  - assumption: The nine remaining project functions are named to establish future scope, not to be governed by this change.
    basis: Confirmed by the business author; the statement limits this change request to catalog only.
  constraints:
  - constraint: Capabilities deferred to future change requests must not be designed into this solution.
    source: Business policy
  - constraint: Only authorized staff may perform catalog operations.
    source: Business policy
  - constraint: Every business operation must leave a record that can be traced and audited.
    source: Business policy
  - constraint: A physical copy may never be recorded against more than one book.
    source: Business policy
  - constraint: The catalog must not import the records staff maintain manually today.
    source: Business policy
  business_invariants:
  - invariant: Each physical copy belongs to exactly one book.
  - invariant: Each book the library holds has exactly one authoritative record.
  - invariant: Each physical copy the library owns has exactly one authoritative record.
  - invariant: No two registered books share the same title, author and publication year.
  - invariant: A book carries at least one subject.
  - invariant: No two physical copies the library owns share the same barcode.
  - invariant: No catalog record is ever deleted.
  - invariant: Every business operation performed against the catalog is traceable and auditable.
  - invariant: Only authorized staff perform catalog operations.
  lifecycle_states:
  - object: Book
    state: Registered
    meaning: The book has been registered and the catalog holds its authoritative record.
  - object: Book
    state: Retired
    meaning: The record has been judged obsolete and is no longer to be used; the book is excluded from search, its details remain retrievable, and staff may return it to Registered.
  - object: Physical Copy
    state: Registered
    meaning: The copy has been registered against exactly one book.
  - object: Physical Copy
    state: Retired
    meaning: The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered.
  business_events:
  - event: Book Registered
    when_it_occurs: When authorized staff register a new book with its first physical copy.
    significance: A book enters the catalog and acquires its authoritative record.
  - event: Physical Copy Registered
    when_it_occurs: When authorized staff register a further copy against a registered book.
    significance: The library records another copy it owns.
  - event: Bibliographic Information Updated
    when_it_occurs: When authorized staff update a registered book's bibliographic information.
    significance: The authoritative description of a book changes.
  - event: Book Retired
    when_it_occurs: When authorized staff retire a book record judged obsolete.
    significance: The record is no longer to be used.
  - event: Physical Copy Retired
    when_it_occurs: When authorized staff retire a copy that is lost or damaged.
    significance: The library no longer holds that copy.
  authority_boundaries:
  - business_object: Book record
    authoritative_owner: Catalog
  - business_object: Physical copy record
    authoritative_owner: Catalog
  - business_object: Bibliographic information
    authoritative_owner: Catalog
  - business_object: The judgement that a record is obsolete
    authoritative_owner: Authorized staff
  out_of_scope:
  - item: Circulation
    reason: A project function; this change request is limited to catalog only.
  - item: Patron
    reason: A project function; this change request is limited to catalog only, and patron management is declared excluded from this release.
  - item: Staff
    reason: A project function; this change request is limited to catalog only, and it is where deciding who is authorized is deferred to.
  - item: Reservations
    reason: A project function, declared excluded from this release; expected through a future governed change request.
  - item: Acquisitions
    reason: A project function, declared excluded from this release; expected through a future governed change request.
  - item: Inventory
    reason: A project function; inventory reconciliation is declared excluded from this release.
  - item: Notifications
    reason: A project function; this change request is limited to catalog only.
  - item: Policy
    reason: A project function; this change request is limited to catalog only.
  - item: Reporting
    reason: A project function; this change request is limited to catalog only.
  - item: Borrowing
    reason: Declared excluded from this release; expected through a future governed change request.
  - item: Fines
    reason: Declared excluded from this release; expected through a future governed change request.
  - item: Import of the records staff maintain manually today
    reason: The catalog starts empty.
  governance_scope:
  - scope_item: catalog
    relationship: CREATED
  - scope_item: circulation
    relationship: ADJACENT
  - scope_item: patron
    relationship: ADJACENT
  - scope_item: staff
    relationship: ADJACENT
  - scope_item: reservations
    relationship: ADJACENT
  - scope_item: acquisitions
    relationship: ADJACENT
  - scope_item: inventory
    relationship: ADJACENT
  - scope_item: notifications
    relationship: ADJACENT
  - scope_item: policy
    relationship: ADJACENT
  - scope_item: reporting
    relationship: ADJACENT
  clarification_requests: null
  acceptance_criteria:
  - criterion: Authorized staff can register a new book with at least one physical copy, and the catalog then holds exactly one record for it.
  - criterion: A registration whose title, author and publication year match a registered book is refused, and the reason states that the book already exists.
  - criterion: A registration offering no physical copy is refused.
  - criterion: A registration carrying no subject is refused.
  - criterion: Authorized staff can register a further physical copy against a registered book, and it is recorded against that book only.
  - criterion: Authorized staff can update a registered book's bibliographic information, and a later retrieval returns the updated version.
  - criterion: Authorized staff can retire a book record, and its physical copies are unaffected.
  - criterion: Authorized staff can retire a physical copy, and the book record is unaffected, including when it is the last copy.
  - criterion: Authorized staff can search by subject and locate registered books of that kind.
  - criterion: Authorized staff can search by title and locate a registered book by name.
  - criterion: A search returns the bibliographic information of each matching book and nothing about its physical copies.
  - criterion: A retired book does not appear in search results, and its details can still be retrieved.
  - criterion: Authorized staff can retrieve the complete details of a registered book, including the physical copies the library holds of it.
  - criterion: Authorized staff can register a physical copy against a retired book.
  - criterion: Authorized staff can return a retired book record to the registered state, and it appears in search again.
  - criterion: Authorized staff can return a retired physical copy to the registered state.
  - criterion: An update that would make a book's title, author and publication year match another registered book is refused.
  - criterion: A copy registration whose barcode matches a copy the library already owns is refused.
  - criterion: A staff member who is not authorized cannot perform any catalog operation.
  - criterion: Every catalog operation performed can be traced and audited afterwards.
  identity_and_sameness:
  - business_object: Book
    identified_by: Its title, author and publication year together.
    two_are_the_same_when: Their publication year matches and their titles and authors match without regard to letter case or repeated spacing.
  - business_object: Physical Copy
    identified_by: The barcode the library assigns to it.
    two_are_the_same_when: Their barcodes match.
  lifecycle_transitions:
  - object: Book
    from_state: null
    to_state: Registered
    triggered_by: Authorized staff register the book together with its first physical copy.
    cascade: None beyond the first copy being registered with it.
  - object: Book
    from_state: Registered
    to_state: Retired
    triggered_by: Authorized staff judge the record obsolete and retire it.
    cascade: None — the book's physical copies are unaffected.
  - object: Book
    from_state: Retired
    to_state: Registered
    triggered_by: Authorized staff return the retired book record to the registered state.
    cascade: None — the book's physical copies are unaffected.
  - object: Physical Copy
    from_state: null
    to_state: Registered
    triggered_by: Authorized staff register the copy against a registered book.
    cascade: None.
  - object: Physical Copy
    from_state: Registered
    to_state: Retired
    triggered_by: Authorized staff retire a copy that is lost or damaged.
    cascade: None — the book record is unaffected, including when it is the last copy.
  - object: Physical Copy
    from_state: Retired
    to_state: Registered
    triggered_by: Authorized staff return the retired copy to the registered state.
    cascade: None — the book record is unaffected.
  operation_refusals:
  - operation: Register a book
    refused_when: Its title, author and publication year match a registered book.
    business_reason: The catalog holds one record per book; the book already exists, and a further copy is what staff register instead.
  - operation: Register a book
    refused_when: No physical copy is offered with it.
    business_reason: A book is never registered without at least one copy.
  - operation: Register a book
    refused_when: It carries no subject.
    business_reason: A book carries at least one subject, and subject is what staff search on.
  - operation: Register a physical copy
    refused_when: The book it names is not registered.
    business_reason: Each physical copy belongs to exactly one book.
  - operation: Register a physical copy
    refused_when: Its barcode matches a copy the library already owns.
    business_reason: A barcode identifies one copy; no two copies share one.
  - operation: Update bibliographic information
    refused_when: The changed title, author and publication year would match another registered book.
    business_reason: Title, author and publication year identify a book; an update must not make one book a duplicate of another.
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    business_reason: Only authorized staff may perform catalog operations.
  authority_deferrals:
  - business_object: Which staff are authorized
    deferred_to: The staff function, which governs library employees
    until: A future governed change request introduces the staff function.
```

> The business content below is the admissible seed's. What is wrong is the shape it is carried in — and one register answers a question by declaring it unanswered.

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
