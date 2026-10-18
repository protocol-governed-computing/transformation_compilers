# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p1
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_04_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: catalog
    classification: MODIFY
    rationale: Two operations state that they need things they do not use, and one states a publication year in a form the catalog does not hold it in. Correct requests are turned away. What each operation needs is restated to match what it does.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Operation
    definition: Something a librarian asks the catalog to do.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Request
    definition: One asking, with what the librarian supplied.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Admission
    definition: The catalog deciding whether a request may proceed.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Requirement
    definition: Something an operation states a request must supply.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Correction
    definition: Changing some details of a record the catalog already holds.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Further edition
    definition: Another edition of a work the library already carries.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Publication year
    definition: The year an edition was published, which the catalog holds as a number.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  requested_outcomes:
  - outcome: Registering a further edition asks for the publication year in the form the catalog holds it.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: Correcting bibliographic information asks for the record and the changes, and nothing it does not use.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: A correct request for either operation is admitted.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: Every requirement an operation states is something that operation uses.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: Who may perform each operation, and what they must be authorised to do, is unchanged.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  known_facts:
  - fact: The catalog holds a publication year as a number, wherever it holds one.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: Registering a work for the first time asks for the publication year as a number.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: Registering a further edition of that same work asks for it as text.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A correction names the record it corrects and supplies the fields it changes.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: A correction does not restate the fields it leaves alone; that is what makes it a correction.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: Correcting bibliographic information asks for the title, author and publication year of the record.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: The steps that carry out a correction read the record named and the changed fields, and read none of those three.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: A requirement an operation does not use turns away correct requests and admits nothing extra.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: A librarian correcting the subject headings of a record is turned away for not resupplying its title.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: The library's end-to-end exercise of the catalog fails at both operations today.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: Both failures are the boundary behaving correctly on a wrong statement.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: Nothing compared what an operation asks for against what it uses, for as long as the boundary admitted everything.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  system_beliefs:
  - belief: Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number.
    why_it_matters: One half of the change.
    verification_goal: Confirm both statements, and confirm which form the catalog records.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: Correcting bibliographic information asks for three details it does not use.
    why_it_matters: The other half.
    verification_goal: Confirm the three, and confirm no step of the correction reads them.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: No other catalog operation asks for something it does not use.
    why_it_matters: Says whether this is two instances or a pattern across the subdomain.
    verification_goal: Establish, for every catalog operation, what it asks for and what it uses.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: Who may perform each operation is stated separately from what the operation needs.
    why_it_matters: Decides whether restating requirements can affect authorisation.
    verification_goal: Confirm the two are separate statements.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: The details a correction changes are supplied together, as the changed fields.
    why_it_matters: Decides whether removing three requirements loses anything.
    verification_goal: Confirm the changed fields carry the details being corrected.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  assumptions:
  - assumption: A librarian supplies a publication year the way the catalog displays it.
    basis: The catalog holds and shows it as a number.
    source_finding: {phase: p0, register: assumptions, row: 1}
  - assumption: The two operations were written from a third, and the requirements were carried across without being reconsidered.
    basis: Registering a work needs the title, author and year; correcting a record does not, and asks for all three.
    source_finding: {phase: p0, register: assumptions, row: 2}
  constraints:
  - constraint: Every requirement an operation keeps is one that operation uses.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: Nothing about who may perform an operation changes.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: The records the catalog already holds are not migrated, rewritten or revalidated.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: A publication year is a number, in every operation that names one.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 4}
  - constraint: No operation gains a requirement in this change.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 5}
  business_invariants:
  - invariant: An operation requires only what it uses.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: A publication year is stated as a number wherever an operation asks for one.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: A correction requires the record it corrects and the changes it makes.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: A correct request is admitted.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: What an operation requires is stated separately from who may perform it.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  lifecycle_states:
  - object: Request
    state: Admitted
    meaning: The catalog accepted it and the operation proceeds.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Request
    state: Turned away
    meaning: The catalog refused it before anything happened.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Request
    state: Correct and turned away
    meaning: Everything the operation needs was supplied and it was refused anyway. This is the state this change ends.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  business_events:
  - event: A request was admitted
    when_it_occurs: When a librarian supplied what the operation needs
    significance: The operation proceeds and the catalog changes.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: A request was turned away
    when_it_occurs: When something the operation needs was missing or in the wrong form
    significance: The librarian is told before anything happened, and the catalog is unchanged.
    source_finding: {phase: p0, register: business_events, row: 2}
  authority_boundaries:
  - business_object: What each catalog operation requires
    authoritative_owner: The catalog subdomain
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: The form a publication year takes
    authoritative_owner: The catalog subdomain
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Who may perform a catalog operation
    authoritative_owner: The library's authorisation rules
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: Whether a request is admitted
    authoritative_owner: The catalog boundary
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  out_of_scope:
  - item: Who may perform any catalog operation
    reason: A separate statement, unchanged by this.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: The records the catalog already holds
    reason: No held record changes; only what a new request must supply.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Operations of subdomains other than the catalog
    reason: Each subdomain's own change.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Whether the boundary should determine admission at all
    reason: Settled; the boundary does what it always declared.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  governance_scope:
  - scope_item: catalog
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  clarification_requests: []
  acceptance_criteria:
  - criterion: Registering a further edition of a held work, with the publication year as a number, is admitted and the edition is registered.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: Correcting the subject headings of a held record, naming the record and the changes only, is admitted and the record is corrected.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: The library's end-to-end exercise of the catalog completes, with every criterion holding.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: A request omitting something either operation still needs is turned away.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: A librarian not authorised for either operation is refused exactly as today.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: No catalog operation requires anything it does not use.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  identity_and_sameness:
  - business_object: Record
    identified_by: The identity the catalog holds it under
    two_are_the_same_when: Two requests name the same identity.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: Requirement
    identified_by: The operation that states it and the thing it asks for
    two_are_the_same_when: One operation asks for one thing once.
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  - business_object: Publication year
    identified_by: The year itself
    two_are_the_same_when: Two are the same year, however either was supplied.
    source_finding: {phase: p0, register: identity_and_sameness, row: 3}
  lifecycle_transitions:
  - object: Request
    from_state: Correct and turned away
    to_state: Admitted
    triggered_by: The operation stating only what it uses.
    cascade: The operation proceeds as it always would have. Nothing about the catalog's records changes.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Request
    from_state: Admitted
    to_state: Turned away
    triggered_by: Something the operation needs being absent.
    cascade: The catalog is unchanged and the librarian is told.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  operation_refusals:
  - operation: Registering a further edition
    refused_when: The publication year is not supplied
    business_reason: The catalog holds an edition by the work it belongs to and the year it was published, so an edition without a year cannot be placed.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Correcting bibliographic information
    refused_when: The record to correct is not named
    business_reason: A correction with no subject changes nothing, and the catalog would not know what to change.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Correcting bibliographic information
    refused_when: No changed fields are supplied
    business_reason: A correction that changes nothing is not a correction.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  authority_deferrals:
  - business_object: What operations of other subdomains require
    deferred_to: Each subdomain
    until: That subdomain raises the change that needs it.
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
