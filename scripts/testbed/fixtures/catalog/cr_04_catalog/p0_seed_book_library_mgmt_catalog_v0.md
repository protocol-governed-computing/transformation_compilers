# Change Seed — book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p0
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_04_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Catalog subdomain governs what the library knows about its books: the works it carries, the
    editions of those works, and the physical copies on its shelves. It holds one record for each, the
    state that says whether each is in service or retired, and the details the library publishes about
    them. It records each thing being registered, its details being corrected, and its being retired or
    reinstated, and it announces the moments the business declared matter. It does not govern who borrows
    a book, what a borrower may do, or what the library charges.
  cr_type:
  - subdomain: catalog
    classification: MODIFY
    rationale: Two operations state that they need things they do not use, and one states a publication year in a form the catalog does not hold it in. Correct requests are turned away. What each operation needs is restated to match what it does.
  business_vocabulary:
  - term: Operation
    definition: Something a librarian asks the catalog to do.
  - term: Request
    definition: One asking, with what the librarian supplied.
  - term: Admission
    definition: The catalog deciding whether a request may proceed.
  - term: Requirement
    definition: Something an operation states a request must supply.
  - term: Correction
    definition: Changing some details of a record the catalog already holds.
  - term: Further edition
    definition: Another edition of a work the library already carries.
  - term: Publication year
    definition: The year an edition was published, which the catalog holds as a number.
  requested_outcomes:
  - outcome: Registering a further edition asks for the publication year in the form the catalog holds it.
  - outcome: Correcting bibliographic information asks for the record and the changes, and nothing it does not use.
  - outcome: A correct request for either operation is admitted.
  - outcome: Every requirement an operation states is something that operation uses.
  - outcome: Who may perform each operation, and what they must be authorised to do, is unchanged.
  known_facts:
  - fact: The catalog holds a publication year as a number, wherever it holds one.
    certainty: HIGH
  - fact: Registering a work for the first time asks for the publication year as a number.
    certainty: HIGH
  - fact: Registering a further edition of that same work asks for it as text.
    certainty: HIGH
  - fact: A correction names the record it corrects and supplies the fields it changes.
    certainty: HIGH
  - fact: A correction does not restate the fields it leaves alone; that is what makes it a correction.
    certainty: HIGH
  - fact: Correcting bibliographic information asks for the title, author and publication year of the record.
    certainty: HIGH
  - fact: The steps that carry out a correction read the record named and the changed fields, and read none of those three.
    certainty: HIGH
  - fact: A requirement an operation does not use turns away correct requests and admits nothing extra.
    certainty: HIGH
  - fact: A librarian correcting the subject headings of a record is turned away for not resupplying its title.
    certainty: HIGH
  - fact: The library's end-to-end exercise of the catalog fails at both operations today.
    certainty: HIGH
  - fact: Both failures are the boundary behaving correctly on a wrong statement.
    certainty: HIGH
  - fact: Nothing compared what an operation asks for against what it uses, for as long as the boundary admitted everything.
    certainty: HIGH
  system_beliefs:
  - belief: Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number.
    why_it_matters: One half of the change.
    verification_goal: Confirm both statements, and confirm which form the catalog records.
  - belief: Correcting bibliographic information asks for three details it does not use.
    why_it_matters: The other half.
    verification_goal: Confirm the three, and confirm no step of the correction reads them.
  - belief: No other catalog operation asks for something it does not use.
    why_it_matters: Says whether this is two instances or a pattern across the subdomain.
    verification_goal: Establish, for every catalog operation, what it asks for and what it uses.
  - belief: Who may perform each operation is stated separately from what the operation needs.
    why_it_matters: Decides whether restating requirements can affect authorisation.
    verification_goal: Confirm the two are separate statements.
  - belief: The details a correction changes are supplied together, as the changed fields.
    why_it_matters: Decides whether removing three requirements loses anything.
    verification_goal: Confirm the changed fields carry the details being corrected.
  assumptions:
  - assumption: A librarian supplies a publication year the way the catalog displays it.
    basis: The catalog holds and shows it as a number.
  - assumption: The two operations were written from a third, and the requirements were carried across without being reconsidered.
    basis: Registering a work needs the title, author and year; correcting a record does not, and asks for all three.
  constraints:
  - constraint: Every requirement an operation keeps is one that operation uses.
    source: Business author
  - constraint: Nothing about who may perform an operation changes.
    source: Business author
  - constraint: The records the catalog already holds are not migrated, rewritten or revalidated.
    source: Business author
  - constraint: A publication year is a number, in every operation that names one.
    source: Business author
  - constraint: No operation gains a requirement in this change.
    source: Business author
  business_invariants:
  - invariant: An operation requires only what it uses.
  - invariant: A publication year is stated as a number wherever an operation asks for one.
  - invariant: A correction requires the record it corrects and the changes it makes.
  - invariant: A correct request is admitted.
  - invariant: What an operation requires is stated separately from who may perform it.
  lifecycle_states:
  - object: Request
    state: Admitted
    meaning: The catalog accepted it and the operation proceeds.
  - object: Request
    state: Turned away
    meaning: The catalog refused it before anything happened.
  - object: Request
    state: Correct and turned away
    meaning: Everything the operation needs was supplied and it was refused anyway. This is the state this change ends.
  business_events:
  - event: A request was admitted
    when_it_occurs: When a librarian supplied what the operation needs
    significance: The operation proceeds and the catalog changes.
  - event: A request was turned away
    when_it_occurs: When something the operation needs was missing or in the wrong form
    significance: The librarian is told before anything happened, and the catalog is unchanged.
  authority_boundaries:
  - business_object: What each catalog operation requires
    authoritative_owner: The catalog subdomain
  - business_object: The form a publication year takes
    authoritative_owner: The catalog subdomain
  - business_object: Who may perform a catalog operation
    authoritative_owner: The library's authorisation rules
  - business_object: Whether a request is admitted
    authoritative_owner: The catalog boundary
  out_of_scope:
  - item: Who may perform any catalog operation
    reason: A separate statement, unchanged by this.
  - item: The records the catalog already holds
    reason: No held record changes; only what a new request must supply.
  - item: Operations of subdomains other than the catalog
    reason: Each subdomain's own change.
  - item: Whether the boundary should determine admission at all
    reason: Settled; the boundary does what it always declared.
  governance_scope:
  - scope_item: catalog
    relationship: MODIFIED
  clarification_requests: []
  acceptance_criteria:
  - criterion: Registering a further edition of a held work, with the publication year as a number, is admitted and the edition is registered.
  - criterion: Correcting the subject headings of a held record, naming the record and the changes only, is admitted and the record is corrected.
  - criterion: The library's end-to-end exercise of the catalog completes, with every criterion holding.
  - criterion: A request omitting something either operation still needs is turned away.
  - criterion: A librarian not authorised for either operation is refused exactly as today.
  - criterion: No catalog operation requires anything it does not use.
  identity_and_sameness:
  - business_object: Record
    identified_by: The identity the catalog holds it under
    two_are_the_same_when: Two requests name the same identity.
  - business_object: Requirement
    identified_by: The operation that states it and the thing it asks for
    two_are_the_same_when: One operation asks for one thing once.
  - business_object: Publication year
    identified_by: The year itself
    two_are_the_same_when: Two are the same year, however either was supplied.
  lifecycle_transitions:
  - object: Request
    from_state: Correct and turned away
    to_state: Admitted
    triggered_by: The operation stating only what it uses.
    cascade: The operation proceeds as it always would have. Nothing about the catalog's records changes.
  - object: Request
    from_state: Admitted
    to_state: Turned away
    triggered_by: Something the operation needs being absent.
    cascade: The catalog is unchanged and the librarian is told.
  operation_refusals:
  - operation: Registering a further edition
    refused_when: The publication year is not supplied
    business_reason: The catalog holds an edition by the work it belongs to and the year it was published, so an edition without a year cannot be placed.
  - operation: Correcting bibliographic information
    refused_when: The record to correct is not named
    business_reason: A correction with no subject changes nothing, and the catalog would not know what to change.
  - operation: Correcting bibliographic information
    refused_when: No changed fields are supplied
    business_reason: A correction that changes nothing is not a correction.
  authority_deferrals:
  - business_object: What operations of other subdomains require
    deferred_to: Each subdomain
    until: That subdomain raises the change that needs it.
```

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

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
