# Change Seed — book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p0
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_03_catalog
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
    rationale: The catalog exists and works. It declares six moments it announces and announces none of them, against a rule the business set when the function was established.
  business_vocabulary:
  - term: Work
    definition: Something the library carries, independent of any particular edition of it.
  - term: Book
    definition: An edition of a work.
  - term: Physical copy
    definition: One copy of a book, on a shelf.
  - term: Bibliographic information
    definition: What the library publishes about a book.
  - term: Retirement
    definition: Taking a book or a copy out of service, without removing what is known about it.
  - term: Reinstatement
    definition: Returning a retired book or copy to service.
  - term: Moment
    definition: Something the catalog announces because the business declared it matters.
  requested_outcomes:
  - outcome: Each of the six declared moments is announced when the act it names completes.
  - outcome: That they are announced is checked, so the silence cannot return unnoticed.
  known_facts:
  - fact: The business decided the catalog announces the moments that matter.
    certainty: HIGH
  - fact: 'Six moments are declared: a work registered, a book registered, a physical copy registered, bibliographic information updated, a book retired, a physical copy retired.'
    certainty: HIGH
  - fact: A moment is announced when the act it names has completed, and not before.
    certainty: HIGH
  - fact: A refusal announces nothing. Nothing happened that anyone need be told about.
    certainty: HIGH
  - fact: Reinstatement is silent. The catalog performs it, records it, and announces nothing.
    certainty: HIGH
  - fact: The six declared moments are the complete set. No seventh is added by this change.
    certainty: HIGH
  - fact: An announcement carries which thing it concerns and when it occurred, and nothing further.
    certainty: HIGH
  - fact: Nobody is expected to hear these announcements today. The moment exists for the record.
    certainty: HIGH
  - fact: The catalog does not go back and announce moments that occurred before this change.
    certainty: HIGH
  - fact: This is a defect, not a new requirement.
    certainty: HIGH
  system_beliefs:
  - belief: The catalog declares six moments and announces none of them.
    why_it_matters: The whole of this change.
    verification_goal: Confirm the six are declared, and establish whether anything refers to any of them.
  - belief: The catalog performs registration, correction, retirement and reinstatement, each as its own act.
    why_it_matters: Each declared moment must attach to the act it names.
    verification_goal: Confirm which acts the catalog performs.
  - belief: Nothing checks whether a declared moment is ever announced.
    why_it_matters: Explains how the silence went unnoticed and says what the check must add.
    verification_goal: Establish whether any rule relates a declared moment to an announcement of it.
  - belief: Reinstatement has no declared moment of its own.
    why_it_matters: The business has ruled it silent; if a moment exists, the ruling and the system disagree.
    verification_goal: Confirm no moment is declared for reinstatement.
  assumptions:
  - assumption: Each declared moment corresponds to exactly one act the catalog performs.
    basis: The six are named after acts the catalog is known to perform.
  constraints:
  - constraint: Nothing a caller sends or is told back changes. This is invisible from outside.
    source: Business author
  - constraint: No moment is added and none is removed. The six are the complete set.
    source: Business author
  - constraint: Nothing outside the catalog is touched.
    source: Business author
  business_invariants:
  - invariant: A declared moment is announced when the act it names completes.
  - invariant: A refused act announces nothing.
  - invariant: An announcement carries which thing it concerns and when it occurred.
  - invariant: A recorded moment is never changed or removed.
  lifecycle_states:
  - object: Book
    state: In service
    meaning: The library carries it.
  - object: Book
    state: Retired
    meaning: Taken out of service; what is known about it is kept.
  - object: Physical copy
    state: In service
    meaning: On the shelf.
  - object: Physical copy
    state: Retired
    meaning: Taken out of service.
  business_events:
  - event: A work was registered
    when_it_occurs: When the library first carries a work
    significance: The library can show when it began carrying it.
  - event: A book was registered
    when_it_occurs: When an edition of a work is registered
    significance: The library can show when the edition entered the catalog.
  - event: A physical copy was registered
    when_it_occurs: When a copy is put on a shelf
    significance: The library can show when the copy became available.
  - event: Bibliographic information was updated
    when_it_occurs: When what the library publishes about a book is corrected
    significance: The library can show when the record changed.
  - event: A book was retired
    when_it_occurs: When an edition is taken out of service
    significance: The library can show when it stopped carrying it.
  - event: A physical copy was retired
    when_it_occurs: When a copy is taken out of service
    significance: The library can show when the copy left the shelf.
  authority_boundaries:
  - business_object: Work, book and physical copy
    authoritative_owner: catalog
  - business_object: Bibliographic information
    authoritative_owner: catalog
  - business_object: The moments the catalog announces
    authoritative_owner: catalog
  out_of_scope:
  - item: What any listener does with an announcement
    reason: The catalog announces the moment; who attends to it is a later question.
  - item: Whether the six are the right six
    reason: They are the moments the business already declared.
  - item: A moment for reinstatement
    reason: The business has ruled reinstatement silent.
  - item: Anything about what the catalog holds or how it is searched
    reason: Only the announcing is touched.
  - item: Anything outside the catalog
    reason: No other subdomain is touched.
  - item: Moments that occurred before this change
    reason: The record is added to and never rewritten.
  governance_scope:
  - scope_item: catalog
    relationship: MODIFIED
  clarification_requests: []
  acceptance_criteria:
  - criterion: Registering a work announces that a work was registered.
  - criterion: Registering a book announces that a book was registered.
  - criterion: Registering a physical copy announces that a physical copy was registered.
  - criterion: Correcting bibliographic information announces that it was updated.
  - criterion: Retiring a book announces that a book was retired.
  - criterion: Retiring a physical copy announces that a physical copy was retired.
  - criterion: A refused act announces nothing.
  - criterion: Reinstating a book or a copy announces nothing.
  - criterion: Each announcement carries which thing it concerns and when it occurred.
  identity_and_sameness:
  - business_object: Moment
    identified_by: The act it names
    two_are_the_same_when: They name the same act of the catalog.
  lifecycle_transitions:
  - object: Book
    from_state: In service
    to_state: Retired
    triggered_by: The library retiring it.
    cascade: A moment is announced. Nothing else follows.
  - object: Book
    from_state: Retired
    to_state: In service
    triggered_by: The library reinstating it.
    cascade: NONE. Reinstatement is silent.
  - object: Physical copy
    from_state: In service
    to_state: Retired
    triggered_by: The library retiring it.
    cascade: A moment is announced. Nothing else follows.
  - object: Physical copy
    from_state: Retired
    to_state: In service
    triggered_by: The library reinstating it.
    cascade: NONE. Reinstatement is silent.
  operation_refusals:
  - operation: Announcing a moment
    refused_when: The act it names did not complete
    business_reason: A moment names something that happened; announcing one for an act that failed would state something untrue.
  authority_deferrals:
  - business_object: What a listener does with an announcement
    deferred_to: A later change
    until: The business decides who is told and how.
```

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

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
