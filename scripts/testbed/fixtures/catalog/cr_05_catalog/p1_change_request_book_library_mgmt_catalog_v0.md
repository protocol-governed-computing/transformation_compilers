# Stage 1 — Change Request: Clarification & Fact Capture: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p1
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_05_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: catalog
    classification: MODIFY
    rationale: The catalog is built. It applies its rules as each request states them rather than holding them itself, registers what its own check found incomplete, and checks a copy of the book rather than the book it records. Nothing is added to what the catalog does; its own rules are made to hold however it is reached.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Authorized staff
    definition: A library staff member permitted to perform catalog operations.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Staff credentials
    definition: What a request presents about the person performing it.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Description
    definition: What the library says a book, a work or a further edition must contain.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Business rule
    definition: 'Something the library decided about the catalog: who may perform an operation, and what a book, a work or a further edition must contain.'
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  requested_outcomes:
  - outcome: The catalog holds the rules that decide who is authorized to perform a catalog operation, and refuses anyone they do not admit, whatever the request says.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: The catalog holds what a book, a work and a further edition must contain, and refuses a registration that does not meet it.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: The catalog checks the book, work or edition it records, not a copy supplied beside it.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: The catalog registers a physical copy as registered, whatever state the request gives it.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: Every correct request from authorized staff is admitted, with the same outcome as today.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  known_facts:
  - fact: Only authorized staff perform catalog operations.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: The catalog does not decide who is authorized; it requires that they are.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: A book's bibliographic information is its title, author, publication year and subject.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A book carries at least one subject.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: The catalog records a publication year as a number.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: A work names its title and author.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: A further edition is described as a book is.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: A registration that does not meet the library's description is refused.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: What a request says about the catalog's rules is ignored, not refused; it is not part of the request.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: A physical copy's registration leads to registered, whatever the request carries.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: Every rule of the catalog's own is held by the catalog.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: The library adds to its record and does not rewrite it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  system_beliefs:
  - belief: Every catalog operation confirms the person performing it is authorized, against rules the request supplies.
    why_it_matters: 'This is the hole the library most needs closed: a request supplying no rules is confirmed whoever sends it.'
    verification_goal: Establish where each operation reads its authorization rules from.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds.
    why_it_matters: A check nothing acts on refuses nothing.
    verification_goal: Establish what each registration does with what its check finds.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: The catalog checks a copy of the book supplied beside it, not the book it records.
    why_it_matters: A check of the wrong thing would judge something other than what is written, even if it refused.
    verification_goal: Establish what each check reads, and what each registration writes.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: The descriptions a book, a work and a further edition are checked against come from the request.
    why_it_matters: A request supplying an empty description has nothing checked against it.
    verification_goal: Establish where each description is read from.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: A physical copy is registered in whatever state the request gives it.
    why_it_matters: A copy was registered already retired.
    verification_goal: Establish where a copy's registered state comes from.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  assumptions: []
  constraints:
  - constraint: Every correct request from authorized staff is admitted, with the same outcome as today.
    source: Business author
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: Records made under a request's own rules stay as they were made.
    source: Business author — the record is added to, never rewritten.
    source_finding: {phase: p0, register: constraints, row: 2}
  business_invariants:
  - invariant: No catalog operation is performed by anyone the library has not authorized.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No book, work or further edition is registered without what the library says it must contain.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: What the catalog checks is what it records.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No physical copy is registered in any state but registered.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: A business rule of the catalog's is held by the catalog, and no request changes it.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: A refusal changes no record.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  lifecycle_states:
  - object: Physical copy
    state: Registered
    meaning: On the shelf and in service. The only state a copy is registered in.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Physical copy
    state: Retired
    meaning: Taken out of service; unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  business_events:
  - event: A work was registered
    when_it_occurs: When authorized staff register a complete book
    significance: Unchanged by this change.
    source_finding: {phase: p0, register: business_events, row: 1}
  authority_boundaries:
  - business_object: The rules a catalog operation's staff credentials are judged by
    authoritative_owner: Catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: What a book, a work and a further edition must contain
    authoritative_owner: Catalog
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Which staff are authorized
    authoritative_owner: The staff function
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  out_of_scope:
  - item: Who a caller is, and whether the credentials a request presents are genuine
    reason: The catalog holds the rules credentials are judged by; it does not authenticate them.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Which staff are authorized
    reason: That belongs to the staff function.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Loans, members and every function other than the catalog
    reason: Not this change.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Records already in the catalog
    reason: The library adds to its record and does not rewrite it.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  governance_scope:
  - scope_item: catalog
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  clarification_requests: []
  acceptance_criteria:
  - criterion: A catalog operation requested by anyone the library has not authorized is refused, whatever rules the request states, and no record changes.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: A book, a work or a further edition missing what the library says it must contain is refused, whatever description the request states, and nothing is registered by it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: What the catalog checks for a registration is what it records.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: A physical copy is registered as registered, whatever state the request gives it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: A request stating rules of its own is judged by the catalog's rules, and is not refused for stating them.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: Every correct request from authorized staff is admitted, with the same outcome as before this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Records made before this change are unchanged by it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  identity_and_sameness: []
  lifecycle_transitions:
  - object: Physical copy
    from_state: Does not exist
    to_state: Registered
    triggered_by: Authorized staff registering it
    cascade: Unchanged by this change.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  operation_refusals:
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    business_reason: Only authorized staff perform catalog operations.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Registering a book
    refused_when: It lacks what the library says a book must contain
    business_reason: The library said the parts are required.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Registering a further edition
    refused_when: It lacks what the library says an edition must contain
    business_reason: The library said the parts are required.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  authority_deferrals:
  - business_object: Which staff are authorized
    deferred_to: The staff function
    until: Always; it is not the catalog's to decide.
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
