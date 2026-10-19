# Change Seed — book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p0
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_05_catalog
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
    rationale: The catalog is built. It applies its rules as each request states them rather than holding them itself, registers what its own check found incomplete, and checks a copy of the book rather than the book it records. Nothing is added to what the catalog does; its own rules are made to hold however it is reached.
  business_vocabulary:
  - term: Authorized staff
    definition: A library staff member permitted to perform catalog operations.
  - term: Staff credentials
    definition: What a request presents about the person performing it.
  - term: Description
    definition: What the library says a book, a work or a further edition must contain.
  - term: Business rule
    definition: 'Something the library decided about the catalog: who may perform an operation, and what a book, a work or a further edition must contain.'
  requested_outcomes:
  - outcome: The catalog holds the rules that decide who is authorized to perform a catalog operation, and refuses anyone they do not admit, whatever the request says.
  - outcome: The catalog holds what a book, a work and a further edition must contain, and refuses a registration that does not meet it.
  - outcome: The catalog checks the book, work or edition it records, not a copy supplied beside it.
  - outcome: The catalog registers a physical copy as registered, whatever state the request gives it.
  - outcome: Every correct request from authorized staff is admitted, with the same outcome as today.
  known_facts:
  - fact: Only authorized staff perform catalog operations.
    certainty: HIGH
  - fact: The catalog does not decide who is authorized; it requires that they are.
    certainty: HIGH
  - fact: A book's bibliographic information is its title, author, publication year and subject.
    certainty: HIGH
  - fact: A book carries at least one subject.
    certainty: HIGH
  - fact: The catalog records a publication year as a number.
    certainty: HIGH
  - fact: A work names its title and author.
    certainty: HIGH
  - fact: A further edition is described as a book is.
    certainty: HIGH
  - fact: A registration that does not meet the library's description is refused.
    certainty: HIGH
  - fact: What a request says about the catalog's rules is ignored, not refused; it is not part of the request.
    certainty: HIGH
  - fact: A physical copy's registration leads to registered, whatever the request carries.
    certainty: HIGH
  - fact: Every rule of the catalog's own is held by the catalog.
    certainty: HIGH
  - fact: The library adds to its record and does not rewrite it.
    certainty: HIGH
  system_beliefs:
  - belief: Every catalog operation confirms the person performing it is authorized, against rules the request supplies.
    why_it_matters: 'This is the hole the library most needs closed: a request supplying no rules is confirmed whoever sends it.'
    verification_goal: Establish where each operation reads its authorization rules from.
  - belief: The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds.
    why_it_matters: A check nothing acts on refuses nothing.
    verification_goal: Establish what each registration does with what its check finds.
  - belief: The catalog checks a copy of the book supplied beside it, not the book it records.
    why_it_matters: A check of the wrong thing would judge something other than what is written, even if it refused.
    verification_goal: Establish what each check reads, and what each registration writes.
  - belief: The descriptions a book, a work and a further edition are checked against come from the request.
    why_it_matters: A request supplying an empty description has nothing checked against it.
    verification_goal: Establish where each description is read from.
  - belief: A physical copy is registered in whatever state the request gives it.
    why_it_matters: A copy was registered already retired.
    verification_goal: Establish where a copy's registered state comes from.
  assumptions: []
  constraints:
  - constraint: Every correct request from authorized staff is admitted, with the same outcome as today.
    source: Business author
  - constraint: Records made under a request's own rules stay as they were made.
    source: Business author — the record is added to, never rewritten.
  business_invariants:
  - invariant: No catalog operation is performed by anyone the library has not authorized.
  - invariant: No book, work or further edition is registered without what the library says it must contain.
  - invariant: What the catalog checks is what it records.
  - invariant: No physical copy is registered in any state but registered.
  - invariant: A business rule of the catalog's is held by the catalog, and no request changes it.
  - invariant: A refusal changes no record.
  lifecycle_states:
  - object: Physical copy
    state: Registered
    meaning: On the shelf and in service. The only state a copy is registered in.
  - object: Physical copy
    state: Retired
    meaning: Taken out of service; unchanged by this change.
  business_events:
  - event: A work was registered
    when_it_occurs: When authorized staff register a complete book
    significance: Unchanged by this change.
  authority_boundaries:
  - business_object: The rules a catalog operation's staff credentials are judged by
    authoritative_owner: Catalog
  - business_object: What a book, a work and a further edition must contain
    authoritative_owner: Catalog
  - business_object: Which staff are authorized
    authoritative_owner: The staff function
  out_of_scope:
  - item: Who a caller is, and whether the credentials a request presents are genuine
    reason: The catalog holds the rules credentials are judged by; it does not authenticate them.
  - item: Which staff are authorized
    reason: That belongs to the staff function.
  - item: Loans, members and every function other than the catalog
    reason: Not this change.
  - item: Records already in the catalog
    reason: The library adds to its record and does not rewrite it.
  governance_scope:
  - scope_item: catalog
    relationship: MODIFIED
  clarification_requests: []
  acceptance_criteria:
  - criterion: A catalog operation requested by anyone the library has not authorized is refused, whatever rules the request states, and no record changes.
  - criterion: A book, a work or a further edition missing what the library says it must contain is refused, whatever description the request states, and nothing is registered by it.
  - criterion: What the catalog checks for a registration is what it records.
  - criterion: A physical copy is registered as registered, whatever state the request gives it.
  - criterion: A request stating rules of its own is judged by the catalog's rules, and is not refused for stating them.
  - criterion: Every correct request from authorized staff is admitted, with the same outcome as before this change.
  - criterion: Records made before this change are unchanged by it.
  identity_and_sameness: []
  lifecycle_transitions:
  - object: Physical copy
    from_state: Does not exist
    to_state: Registered
    triggered_by: Authorized staff registering it
    cascade: Unchanged by this change.
  operation_refusals:
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    business_reason: Only authorized staff perform catalog operations.
  - operation: Registering a book
    refused_when: It lacks what the library says a book must contain
    business_reason: The library said the parts are required.
  - operation: Registering a further edition
    refused_when: It lacks what the library says an edition must contain
    business_reason: The library said the parts are required.
  authority_deferrals:
  - business_object: Which staff are authorized
    deferred_to: The staff function
    until: Always; it is not the catalog's to decide.
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
