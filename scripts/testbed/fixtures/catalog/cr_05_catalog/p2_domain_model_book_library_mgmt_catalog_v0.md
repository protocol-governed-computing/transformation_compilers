# Stage 2 — Domain Model Verification: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p2
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_05_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: The Book
    description: 'What the library records about a book: its title, author, publication year, subject and state.'
    store_model: One keyed store, one record per book, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 3}
  - entity: The Physical Copy
    description: One copy of a book on the library's shelves, and its state.
    store_model: One keyed store, one record per barcode, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: lifecycle_states, row: 1}
  - entity: The Staff Credentials
    description: What a request presents about the person performing it.
    store_model: Carried by each request; the catalog stores none.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: The Catalog's Rules
    description: Who may perform a catalog operation, and what a book, a work and a further edition must contain.
    store_model: Held nowhere in the catalog today. Each travels with the request that is judged by it.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  entity_attributes:
  - entity: The Book
    attribute: Title
    meaning: Part of what identifies a book. Required.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 3}
  - entity: The Book
    attribute: Author
    meaning: Part of what identifies a book. Required.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 3}
  - entity: The Book
    attribute: Publication Year
    meaning: Part of what identifies a book, recorded as a number. Required.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 5}
  - entity: The Book
    attribute: Subject
    meaning: What kind of book it is. At least one.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 4}
  - entity: The Physical Copy
    attribute: State
    meaning: Registered or retired.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: lifecycle_states, row: 1}
  business_processes:
  - process: Perform any catalog operation
    initiator: Authorized staff
    outcome: The operation proceeds for authorized staff; anyone else is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Register a book, a further edition or a copy
    initiator: Authorized staff
    outcome: A complete registration is recorded; an incomplete one is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  process_steps:
  - process: Perform any catalog operation
    step: '1'
    action: Confirm the person performing it is authorized staff.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - process: Register a book, a further edition or a copy
    step: '1'
    action: Check the registration against what it must contain.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - process: Register a book, a further edition or a copy
    step: '2'
    action: Record the book, the edition or the copy, and record that it happened.
    record_produced: The record, and a moment on the operation trail.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  belief_verification:
  - belief: Every catalog operation confirms the person performing it is authorized, against rules the request supplies.
    result: VERIFIED
    evidence: 'All ten catalog acts in force bind `authorization_rules` from the payload into book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, whose one step judges the request''s `staff_credentials` against them, and each act''s gate requires the field. Run directly: staff presenting `authorized: false` are refused under the library''s rules and registered a book when the request sent an empty list of rules. That book is held like any other.'
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds.
    result: VERIFIED
    evidence: 'book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 run capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and publish its violations; nothing reads them. The submission check''s only refusal is a rule on the barcode and the supplied subject. Run directly: a book whose supplied details lacked everything but a title was registered.'
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: The catalog checks a copy of the book supplied beside it, not the book it records.
    result: VERIFIED
    evidence: The submission check reads `book_fields` from the payload. The act records a book built from the request's top-level title, author, year and subject. Every caller sends the subject inside `book_fields` and never at the top level, so every book registered through the library's own exercise is recorded with no subject — the defect cr_04_catalog found and set aside.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: The descriptions a book, a work and a further edition are checked against come from the request.
    result: VERIFIED
    evidence: 'book_library_mgmt::WF_REGISTER_BOOK_V0 binds `book_schema`, and book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 binds `edition_schema` and `work_schema`, from the payload; both gates require them. The register act writes its work description as a literal, but in a shape the structure check does not read, so it checks nothing. Run directly: an empty `book_schema` let an incomplete book through.'
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: A physical copy is registered in whatever state the request gives it.
    result: VERIFIED
    evidence: 'book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 assembles the copy''s `state` from the request''s `copy_fields`. Run directly: a copy registered with the state RETIRED is held retired.'
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  pps_baseline_fqdns:
  - capability: Confirming staff are authorized
    fqdn: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    what_it_does: Judges the request's staff credentials against a list of rules.
    fit: PARTIAL
    cannot_do: It holds no rule of its own; the rules come from the request.
  - capability: Checking a book submission
    fqdn: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    what_it_does: Checks supplied book and work details against descriptions, and refuses a blank barcode or an empty supplied subject.
    fit: PARTIAL
    cannot_do: It refuses nothing its checks find, checks the supplied copy rather than the recorded book, and takes its descriptions from the request.
  - capability: Recording a book
    fqdn: book_library_mgmt::CC_REGISTER_BOOK_V0
    what_it_does: Checks the book against a description, then records it.
    fit: PARTIAL
    cannot_do: It ignores what its check finds and takes the description from the request.
  - capability: Recording a further edition
    fqdn: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    what_it_does: Checks the edition against a description, then records it.
    fit: PARTIAL
    cannot_do: It ignores what its check finds and takes the description from the request.
  - capability: Recording a copy
    fqdn: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    what_it_does: Records a copy of a registered book.
    fit: PARTIAL
    cannot_do: It records the copy in whatever state the request gives.
  - capability: Correcting a record
    fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    what_it_does: Refuses a correction that would change a book's identity, then writes the corrected record.
    fit: PARTIAL
    cannot_do: It writes the state the request gives, and checks the corrected record against no description.
  - capability: Book registration act
    fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    what_it_does: Confirms staff, checks, claims identities and barcode, records book and copy, and records the operation.
    fit: PARTIAL
    cannot_do: It binds the rules and the description from the request, and reads the subject where no caller sends it.
  - capability: Edition registration act
    fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    what_it_does: Confirms staff, checks, resolves the work and records the edition.
    fit: PARTIAL
    cannot_do: It binds the rules and both descriptions from the request.
  - capability: Copy registration act
    fqdn: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    what_it_does: Confirms staff, claims the barcode and records the copy.
    fit: PARTIAL
    cannot_do: It binds the rules from the request.
  - capability: Correction act
    fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    what_it_does: Confirms staff, resolves the book and writes the correction.
    fit: PARTIAL
    cannot_do: It binds the rules from the request.
  - capability: Book retirement act
    fqdn: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    what_it_does: Confirms staff and retires a book record.
    fit: PARTIAL
    cannot_do: It binds the rules from the request.
  - capability: Book reinstatement act
    fqdn: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    what_it_does: Confirms staff and reinstates a book record.
    fit: PARTIAL
    cannot_do: It binds the rules from the request.
  - capability: Copy retirement act
    fqdn: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    what_it_does: Confirms staff and retires a copy.
    fit: PARTIAL
    cannot_do: It binds the rules from the request.
  - capability: Copy reinstatement act
    fqdn: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    what_it_does: Confirms staff and reinstates a copy.
    fit: PARTIAL
    cannot_do: It binds the rules from the request.
  - capability: Retrieval act
    fqdn: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    what_it_does: Confirms staff and returns a book's details.
    fit: PARTIAL
    cannot_do: It binds the rules from the request.
  - capability: Search act
    fqdn: book_library_mgmt::WF_SEARCH_CATALOG_V0
    what_it_does: Confirms staff and searches the catalog.
    fit: PARTIAL
    cannot_do: It binds the rules from the request.
  - capability: Rule check
    fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    what_it_does: Refuses parameters that fail a given list of rules.
    fit: EXACT
    cannot_do: Nothing; it can refuse on a check's violations, as another domain already does.
  - capability: Structure check
    fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    what_it_does: Reports every way a record fails a description.
    fit: PARTIAL
    cannot_do: It reports and never refuses. Refusing on what it reports is the calling contract's business (ruled for v5).
  - capability: Holding the rules in the contract
    fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    what_it_does: Holds its description as a literal and refuses on what its check finds.
    fit: EXACT
    cannot_do: Nothing; it is the precedent this change follows.
  gaps:
  - gap: The catalog holds none of its own rules; each comes with the request it judges.
    severity: CRITICAL
    impact: Anyone can perform any catalog operation by sending no rules.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: A registration the catalog finds incomplete is registered anyway.
    severity: MAJOR
    impact: A book can be held without what the library says it must contain.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: What the catalog checks is not what it records.
    severity: MAJOR
    impact: Every registered book is recorded without its subject, and a check that refused would judge the wrong thing.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: A copy is registered in the state the request gives.
    severity: MINOR
    impact: A copy can enter the catalog already retired.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  architectural_observations:
  - observation: The catalog has no entrance that supplies its rules, so every caller states them.
    evidence: No transport ingress targets a catalog act; the library's own exercise supplies the rules in every request.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - observation: Identity closed the same hole by holding its rules in the contracts that apply them.
    evidence: blockchain::CC_VALIDATE_REGISTRATION_V0 holds its description and refuses on its violations.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 19}
  - observation: The gates require the rule fields, so holding the rules in the catalog changes every gate.
    evidence: Each of the ten gates in force requires `authorization_rules`; two also require descriptions.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  discovery_concerns:
  - concern: A correction writes the state the request gives.
    evidence: 'Run directly: a correction set a registered book to SUSPENDED, a state the library does not have, bypassing retirement and reinstatement. Put to the business author, who answered that a correction keeps the record''s state.'
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 6}
  - concern: A correction is not checked against what a book must contain.
    evidence: 'Run directly: a correction left a book with no subject. Put to the business author, who answered that a corrected record meets the book description.'
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 6}
  - concern: The register act's work description checks nothing.
    evidence: It is written as a list of required names, a shape the structure check does not read, so every work passes. Covered by the catalog holding what a work must contain.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - concern: The book's recorded subject is read where no caller sends it.
    evidence: Put to the business author, who answered that the act records the subject where callers send it, inside the book's supplied details.
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - concern: The credentials a request presents are its own.
    evidence: 'Holding the rules closes rule-widening; a caller presenting `authorized: true` is still admitted. Who a caller is lies outside this change.'
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: out_of_scope, row: 1}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition. What is
verified here is where each of the catalog's rules is read from, and what the catalog does with what
its checks find. The catalog has no transport entrance: every caller invokes its acts directly, so
each belief about behaviour was established by running the acts directly against the pinned
composition, on a scratch data root, as any caller would.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
