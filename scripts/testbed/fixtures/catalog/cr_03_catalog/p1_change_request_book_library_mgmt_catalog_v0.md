# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p1
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_03_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: catalog
    classification: MODIFY
    rationale: The catalog exists and works. It declares six moments it announces and announces none of them, against a rule the business set when the function was established.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Work
    definition: Something the library carries, independent of any particular edition of it.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Book
    definition: An edition of a work.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Physical copy
    definition: One copy of a book, on a shelf.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Bibliographic information
    definition: What the library publishes about a book.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Retirement
    definition: Taking a book or a copy out of service, without removing what is known about it.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Reinstatement
    definition: Returning a retired book or copy to service.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Moment
    definition: Something the catalog announces because the business declared it matters.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  requested_outcomes:
  - outcome: Each of the six declared moments is announced when the act it names completes.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: That they are announced is checked, so the silence cannot return unnoticed.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  known_facts:
  - fact: The business decided the catalog announces the moments that matter.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: 'Six moments are declared: a work registered, a book registered, a physical copy registered, bibliographic information updated, a book retired, a physical copy retired.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: A moment is announced when the act it names has completed, and not before.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A refusal announces nothing. Nothing happened that anyone need be told about.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: Reinstatement is silent. The catalog performs it, records it, and announces nothing.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: The six declared moments are the complete set. No seventh is added by this change.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: An announcement carries which thing it concerns and when it occurred, and nothing further.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: Nobody is expected to hear these announcements today. The moment exists for the record.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: The catalog does not go back and announce moments that occurred before this change.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: This is a defect, not a new requirement.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  system_beliefs:
  - belief: The catalog declares six moments and announces none of them.
    why_it_matters: The whole of this change.
    verification_goal: Confirm the six are declared, and establish whether anything refers to any of them.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The catalog performs registration, correction, retirement and reinstatement, each as its own act.
    why_it_matters: Each declared moment must attach to the act it names.
    verification_goal: Confirm which acts the catalog performs.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: Nothing checks whether a declared moment is ever announced.
    why_it_matters: Explains how the silence went unnoticed and says what the check must add.
    verification_goal: Establish whether any rule relates a declared moment to an announcement of it.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: Reinstatement has no declared moment of its own.
    why_it_matters: The business has ruled it silent; if a moment exists, the ruling and the system disagree.
    verification_goal: Confirm no moment is declared for reinstatement.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  assumptions:
  - assumption: Each declared moment corresponds to exactly one act the catalog performs.
    basis: The six are named after acts the catalog is known to perform.
    source_finding: {phase: p0, register: assumptions, row: 1}
  constraints:
  - constraint: Nothing a caller sends or is told back changes. This is invisible from outside.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: No moment is added and none is removed. The six are the complete set.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: Nothing outside the catalog is touched.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 3}
  business_invariants:
  - invariant: A declared moment is announced when the act it names completes.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: A refused act announces nothing.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: An announcement carries which thing it concerns and when it occurred.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: A recorded moment is never changed or removed.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  lifecycle_states:
  - object: Book
    state: In service
    meaning: The library carries it.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Book
    state: Retired
    meaning: Taken out of service; what is known about it is kept.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Physical copy
    state: In service
    meaning: On the shelf.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: Physical copy
    state: Retired
    meaning: Taken out of service.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  business_events:
  - event: A work was registered
    when_it_occurs: When the library first carries a work
    significance: The library can show when it began carrying it.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: A book was registered
    when_it_occurs: When an edition of a work is registered
    significance: The library can show when the edition entered the catalog.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: A physical copy was registered
    when_it_occurs: When a copy is put on a shelf
    significance: The library can show when the copy became available.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: Bibliographic information was updated
    when_it_occurs: When what the library publishes about a book is corrected
    significance: The library can show when the record changed.
    source_finding: {phase: p0, register: business_events, row: 4}
  - event: A book was retired
    when_it_occurs: When an edition is taken out of service
    significance: The library can show when it stopped carrying it.
    source_finding: {phase: p0, register: business_events, row: 5}
  - event: A physical copy was retired
    when_it_occurs: When a copy is taken out of service
    significance: The library can show when the copy left the shelf.
    source_finding: {phase: p0, register: business_events, row: 6}
  authority_boundaries:
  - business_object: Work, book and physical copy
    authoritative_owner: catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: Bibliographic information
    authoritative_owner: catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: The moments the catalog announces
    authoritative_owner: catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  out_of_scope:
  - item: What any listener does with an announcement
    reason: The catalog announces the moment; who attends to it is a later question.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Whether the six are the right six
    reason: They are the moments the business already declared.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: A moment for reinstatement
    reason: The business has ruled reinstatement silent.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Anything about what the catalog holds or how it is searched
    reason: Only the announcing is touched.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: Anything outside the catalog
    reason: No other subdomain is touched.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  - item: Moments that occurred before this change
    reason: The record is added to and never rewritten.
    source_finding: {phase: p0, register: out_of_scope, row: 6}
  governance_scope:
  - scope_item: catalog
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  clarification_requests: []
  acceptance_criteria:
  - criterion: Registering a work announces that a work was registered.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: Registering a book announces that a book was registered.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: Registering a physical copy announces that a physical copy was registered.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Correcting bibliographic information announces that it was updated.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Retiring a book announces that a book was retired.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: Retiring a physical copy announces that a physical copy was retired.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: A refused act announces nothing.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: Reinstating a book or a copy announces nothing.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: Each announcement carries which thing it concerns and when it occurred.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  identity_and_sameness:
  - business_object: Moment
    identified_by: The act it names
    two_are_the_same_when: They name the same act of the catalog.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  lifecycle_transitions:
  - object: Book
    from_state: In service
    to_state: Retired
    triggered_by: The library retiring it.
    cascade: A moment is announced. Nothing else follows.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Book
    from_state: Retired
    to_state: In service
    triggered_by: The library reinstating it.
    cascade: NONE. Reinstatement is silent.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  - object: Physical copy
    from_state: In service
    to_state: Retired
    triggered_by: The library retiring it.
    cascade: A moment is announced. Nothing else follows.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 3}
  - object: Physical copy
    from_state: Retired
    to_state: In service
    triggered_by: The library reinstating it.
    cascade: NONE. Reinstatement is silent.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 4}
  operation_refusals:
  - operation: Announcing a moment
    refused_when: The act it names did not complete
    business_reason: A moment names something that happened; announcing one for an act that failed would state something untrue.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  authority_deferrals:
  - business_object: What a listener does with an announcement
    deferred_to: A later change
    until: The business decides who is told and how.
    source_finding: {phase: p0, register: authority_deferrals, row: 1}
```

Projected from the change seed. Every row is the seed's own, cited to the section it was said in.
S1 interrogates and does not author.

---

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
