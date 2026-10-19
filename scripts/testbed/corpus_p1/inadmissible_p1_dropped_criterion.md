# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p1
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_01_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: catalog
    classification: NEW_SUBDOMAIN
    rationale: book_library_mgmt is proposed as a new project, and the library requires a governed catalog management capability it maintains manually today. It extends nothing that exists.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: book_library_mgmt
    definition: The project governing the library of books, across ten functions of which catalog is the first.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Catalog
    definition: The function holding the library's authoritative description of the materials it holds.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Book
    definition: A published material the library catalogs, identified by its title, author and publication year. The general term for anything the library catalogs, including published materials that are not books.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Bibliographic Information
    definition: 'A book''s descriptive content: title, author, publication year and subject.'
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Subject
    definition: What kind of book it is, stated as free text; what staff search on when looking for material rather than for a known title.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Physical Copy
    definition: An individual copy the library owns, belonging to exactly one book, identified by its barcode.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Barcode
    definition: The identifier the library assigns to a physical copy, which distinguishes that copy from every other copy the library owns.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: Catalog Record
    definition: The single authoritative record for one book or one physical copy.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Book Details
    definition: 'The complete description of a registered book: its bibliographic information and the physical copies the library holds of it.'
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  - term: Obsolete Record
    definition: A catalog record the library has determined is no longer to be used.
    source_finding: {phase: p0, register: business_vocabulary, row: 10}
  - term: Authorized Staff
    definition: A library staff member permitted to perform catalog operations.
    source_finding: {phase: p0, register: business_vocabulary, row: 11}
  - term: Business Operation
    definition: An action performed against the catalog that must be traceable and auditable.
    source_finding: {phase: p0, register: business_vocabulary, row: 12}
  requested_outcomes:
  - outcome: A single authoritative record exists for each book the library holds.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: A single authoritative record exists for each physical copy the library owns.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: Authorized staff can register new books, register physical copies, update bibliographic information, retire obsolete records, search the catalog, and retrieve complete book details.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: Catalog descriptions are consistent and duplicate entries no longer occur.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: Materials can be located by what kind of book they are, without the difficulty the manual catalog produces.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: Every business operation performed against the catalog is traceable and auditable.
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  known_facts:
  - fact: The proposed name of the project is book_library_mgmt.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: 'The project scope covers ten functions: catalog, circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy, reporting.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: The scope of this change request is limited to the catalog function only.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A community library maintains thousands of books and other published materials.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: '"Book" is the general term for anything the library catalogs, including published materials that are not books.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: Catalog records are maintained manually today.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: Manual maintenance produces inconsistent descriptions, duplicate entries, and difficulty locating materials.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: The library requires a governed catalog management capability providing a single authoritative record for each book and each physical copy it owns.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: A book's bibliographic information is its title, author, publication year and subject.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: A book carries at least one subject and may carry several.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: Subject says what kind of book it is, and is what staff search on when looking for material rather than for a known title.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: A book's subject is free text; the library maintains no list of permitted subjects.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: Staff search the catalog by subject or by title.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: A search returns the bibliographic information of each matching registered book, and nothing about its physical copies.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: Title, author and publication year together identify a book.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: Title and author are compared without regard to letter case or repeated spacing; case and spacing do not change which book is meant.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  - fact: Each physical copy belongs to exactly one book.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 17}
  - fact: Registering a book requires at least one physical copy; a book is never registered without a copy.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 18}
  - fact: Each physical copy carries a barcode the library assigns, which identifies that copy among all the copies the library owns.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 19}
  - fact: A physical copy may be retired on its own, when it is lost or damaged.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 20}
  - fact: A physical copy may be registered against a retired book.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 21}
  - fact: A catalog record is never deleted; retirement is the only way a record leaves use.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 22}
  - fact: Authorized staff may return a retired book record or a retired physical copy to the registered state.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 23}
  - fact: An update to bibliographic information may change the title, author or publication year.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 24}
  - fact: An update is refused when the changed title, author and publication year would match another registered book.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 25}
  - fact: 'No retirement follows automatically from another: retiring a book does not retire its copies, and retiring the last copy does not retire the book.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 26}
  - fact: A registration whose title, author and publication year match a registered book is refused, because the book already exists.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 27}
  - fact: A retired book is excluded from search results, and its details remain retrievable.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 28}
  - fact: Retrieving complete book details returns the book's bibliographic information and the physical copies the library holds of it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 29}
  - fact: The catalog does not manage which staff are authorized; it requires staff to be authorized.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 30}
  - fact: Deciding who is authorized belongs to the staff function, which governs library employees.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 31}
  - fact: Patrons are library users, not employees, and the patron function does not decide staff authorization.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 32}
  - fact: Only authorized staff may perform catalog operations.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 33}
  - fact: Every business operation must be traceable and auditable.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 34}
  - fact: The catalog starts empty; the records staff maintain manually today are not imported by this change.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 35}
  - fact: 'The operations required of the catalog are: register a new book, register a physical copy, update bibliographic information, retire an obsolete record, search the catalog, retrieve complete book details.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 36}
  - fact: Borrowing, reservations, fines, patron management, acquisitions and inventory reconciliation are excluded from this release.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 37}
  - fact: The excluded capabilities are expected to be introduced through future governed change requests.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 38}
  - fact: The excluded capabilities must not be designed into the initial solution.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 39}
  system_beliefs:
  - belief: book_library_mgmt does not appear to be part of the current software baseline.
    why_it_matters: The change is classified NEW_SUBDOMAIN on that basis; if the project already exists, this is an extension and its scope is different.
    verification_goal: Confirm no artifact in the pinned composition carries the book_library_mgmt namespace.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: No capability in the current composition manages a library catalog.
    why_it_matters: This change exists to fill that gap; if such a capability exists, the change becomes a reuse or an extension.
    verification_goal: Confirm nothing in the composition registers, describes, searches or retires a catalog record.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  assumptions:
  - assumption: '"Thousands of books" describes the size of the collection and states no performance requirement.'
    basis: Confirmed by the business author; the statement names no performance target.
    source_finding: {phase: p0, register: assumptions, row: 1}
  - assumption: The library is treated as a single collection; no branch or location distinction is required.
    basis: Confirmed by the business author; the statement names no branch or location.
    source_finding: {phase: p0, register: assumptions, row: 2}
  - assumption: The nine remaining project functions are named to establish future scope, not to be governed by this change.
    basis: Confirmed by the business author; the statement limits this change request to catalog only.
    source_finding: {phase: p0, register: assumptions, row: 3}
  constraints:
  - constraint: Capabilities deferred to future change requests must not be designed into this solution.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: Only authorized staff may perform catalog operations.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: Every business operation must leave a record that can be traced and audited.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: A physical copy may never be recorded against more than one book.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 4}
  - constraint: The catalog must not import the records staff maintain manually today.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 5}
  business_invariants:
  - invariant: Each physical copy belongs to exactly one book.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: Each book the library holds has exactly one authoritative record.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: Each physical copy the library owns has exactly one authoritative record.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No two registered books share the same title, author and publication year.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: A book carries at least one subject.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: No two physical copies the library owns share the same barcode.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: No catalog record is ever deleted.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  - invariant: Every business operation performed against the catalog is traceable and auditable.
    source_finding: {phase: p0, register: business_invariants, row: 8}
  - invariant: Only authorized staff perform catalog operations.
    source_finding: {phase: p0, register: business_invariants, row: 9}
  lifecycle_states:
  - object: Book
    state: Registered
    meaning: The book has been registered and the catalog holds its authoritative record.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Book
    state: Retired
    meaning: The record has been judged obsolete and is no longer to be used; the book is excluded from search, its details remain retrievable, and staff may return it to Registered.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Physical Copy
    state: Registered
    meaning: The copy has been registered against exactly one book.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: Physical Copy
    state: Retired
    meaning: The copy has been lost or damaged and is no longer held by the library; staff may return it to Registered.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  business_events:
  - event: Book Registered
    when_it_occurs: When authorized staff register a new book with its first physical copy.
    significance: A book enters the catalog and acquires its authoritative record.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: Physical Copy Registered
    when_it_occurs: When authorized staff register a further copy against a registered book.
    significance: The library records another copy it owns.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: Bibliographic Information Updated
    when_it_occurs: When authorized staff update a registered book's bibliographic information.
    significance: The authoritative description of a book changes.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: Book Retired
    when_it_occurs: When authorized staff retire a book record judged obsolete.
    significance: The record is no longer to be used.
    source_finding: {phase: p0, register: business_events, row: 4}
  - event: Physical Copy Retired
    when_it_occurs: When authorized staff retire a copy that is lost or damaged.
    significance: The library no longer holds that copy.
    source_finding: {phase: p0, register: business_events, row: 5}
  authority_boundaries:
  - business_object: Book record
    authoritative_owner: Catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: Physical copy record
    authoritative_owner: Catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Bibliographic information
    authoritative_owner: Catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: The judgement that a record is obsolete
    authoritative_owner: Authorized staff
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  out_of_scope:
  - item: Circulation
    reason: A project function; this change request is limited to catalog only.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Patron
    reason: A project function; this change request is limited to catalog only, and patron management is declared excluded from this release.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Staff
    reason: A project function; this change request is limited to catalog only, and it is where deciding who is authorized is deferred to.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Reservations
    reason: A project function, declared excluded from this release; expected through a future governed change request.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: Acquisitions
    reason: A project function, declared excluded from this release; expected through a future governed change request.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  - item: Inventory
    reason: A project function; inventory reconciliation is declared excluded from this release.
    source_finding: {phase: p0, register: out_of_scope, row: 6}
  - item: Notifications
    reason: A project function; this change request is limited to catalog only.
    source_finding: {phase: p0, register: out_of_scope, row: 7}
  - item: Policy
    reason: A project function; this change request is limited to catalog only.
    source_finding: {phase: p0, register: out_of_scope, row: 8}
  - item: Reporting
    reason: A project function; this change request is limited to catalog only.
    source_finding: {phase: p0, register: out_of_scope, row: 9}
  - item: Borrowing
    reason: Declared excluded from this release; expected through a future governed change request.
    source_finding: {phase: p0, register: out_of_scope, row: 10}
  - item: Fines
    reason: Declared excluded from this release; expected through a future governed change request.
    source_finding: {phase: p0, register: out_of_scope, row: 11}
  - item: Import of the records staff maintain manually today
    reason: The catalog starts empty.
    source_finding: {phase: p0, register: out_of_scope, row: 12}
  governance_scope:
  - scope_item: catalog
    relationship: CREATED
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
  - criterion: Authorized staff can register a new book with at least one physical copy, and the catalog then holds exactly one record for it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: A registration whose title, author and publication year match a registered book is refused, and the reason states that the book already exists.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: A registration offering no physical copy is refused.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: A registration carrying no subject is refused.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Authorized staff can register a further physical copy against a registered book, and it is recorded against that book only.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: Authorized staff can update a registered book's bibliographic information, and a later retrieval returns the updated version.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Authorized staff can retire a book record, and its physical copies are unaffected.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: Authorized staff can retire a physical copy, and the book record is unaffected, including when it is the last copy.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: Authorized staff can search by subject and locate registered books of that kind.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: Authorized staff can search by title and locate a registered book by name.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: A search returns the bibliographic information of each matching book and nothing about its physical copies.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  - criterion: A retired book does not appear in search results, and its details can still be retrieved.
    source_finding: {phase: p0, register: acceptance_criteria, row: 12}
  - criterion: Authorized staff can retrieve the complete details of a registered book, including the physical copies the library holds of it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 13}
  - criterion: Authorized staff can register a physical copy against a retired book.
    source_finding: {phase: p0, register: acceptance_criteria, row: 14}
  - criterion: Authorized staff can return a retired book record to the registered state, and it appears in search again.
    source_finding: {phase: p0, register: acceptance_criteria, row: 15}
  - criterion: Authorized staff can return a retired physical copy to the registered state.
    source_finding: {phase: p0, register: acceptance_criteria, row: 16}
  - criterion: An update that would make a book's title, author and publication year match another registered book is refused.
    source_finding: {phase: p0, register: acceptance_criteria, row: 17}
  - criterion: A copy registration whose barcode matches a copy the library already owns is refused.
    source_finding: {phase: p0, register: acceptance_criteria, row: 18}
  - criterion: A staff member who is not authorized cannot perform any catalog operation.
    source_finding: {phase: p0, register: acceptance_criteria, row: 19}
  identity_and_sameness:
  - business_object: Book
    identified_by: Its title, author and publication year together.
    two_are_the_same_when: Their publication year matches and their titles and authors match without regard to letter case or repeated spacing.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: Physical Copy
    identified_by: The barcode the library assigns to it.
    two_are_the_same_when: Their barcodes match.
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  lifecycle_transitions:
  - object: Book
    from_state: null
    to_state: Registered
    triggered_by: Authorized staff register the book together with its first physical copy.
    cascade: None beyond the first copy being registered with it.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Book
    from_state: Registered
    to_state: Retired
    triggered_by: Authorized staff judge the record obsolete and retire it.
    cascade: None — the book's physical copies are unaffected.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  - object: Book
    from_state: Retired
    to_state: Registered
    triggered_by: Authorized staff return the retired book record to the registered state.
    cascade: None — the book's physical copies are unaffected.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 3}
  - object: Physical Copy
    from_state: null
    to_state: Registered
    triggered_by: Authorized staff register the copy against a registered book.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 4}
  - object: Physical Copy
    from_state: Registered
    to_state: Retired
    triggered_by: Authorized staff retire a copy that is lost or damaged.
    cascade: None — the book record is unaffected, including when it is the last copy.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 5}
  - object: Physical Copy
    from_state: Retired
    to_state: Registered
    triggered_by: Authorized staff return the retired copy to the registered state.
    cascade: None — the book record is unaffected.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 6}
  operation_refusals:
  - operation: Register a book
    refused_when: Its title, author and publication year match a registered book.
    business_reason: The catalog holds one record per book; the book already exists, and a further copy is what staff register instead.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Register a book
    refused_when: No physical copy is offered with it.
    business_reason: A book is never registered without at least one copy.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Register a book
    refused_when: It carries no subject.
    business_reason: A book carries at least one subject, and subject is what staff search on.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Register a physical copy
    refused_when: The book it names is not registered.
    business_reason: Each physical copy belongs to exactly one book.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Register a physical copy
    refused_when: Its barcode matches a copy the library already owns.
    business_reason: A barcode identifies one copy; no two copies share one.
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: Update bibliographic information
    refused_when: The changed title, author and publication year would match another registered book.
    business_reason: Title, author and publication year identify a book; an update must not make one book a duplicate of another.
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    business_reason: Only authorized staff may perform catalog operations.
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  authority_deferrals:
  - business_object: Which staff are authorized
    deferred_to: The staff function, which governs library employees
    until: A future governed change request introduces the staff function.
    source_finding: {phase: p0, register: authority_deferrals, row: 1}
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
