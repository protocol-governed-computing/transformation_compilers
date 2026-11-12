# Stage 1 — Change Request: Clarification & Fact Capture: transformation / design

## Machine

```yaml
document:
  phase: p1
  domain: transformation
  subdomain: design
  cr: route_change_judged_by_phases
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: design
    classification: MODIFY
    rationale: The route already runs a change as its own dossier and seals it; this change adds the judgement of that dossier by the phases, and authors no artifact into the subdomain.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Derive Route
    definition: The way the Design subdomain derives a design from an owner's answers, decided by its doctrine, its ledger schema, its catalog and its building blocks.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Route Change
    definition: A change to the doctrine, the ledger schema, the catalog or a building block of the derive route.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Seal
    definition: The record that the derive route as it stands is the one a route change left, kept with the dossier that made it.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Phase Verdict
    definition: Whether a phase document is admissible against the documents before it, by a named rule set.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  requested_outcomes:
  - outcome: A route change is sealed only when its dossier carries the seed, the change request, the domain model, the analysis, the business model, the business intent and the governance intent, each admissible.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: Each seal records the verdict of every phase and the rule set that gave it.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: Once one seal carries verdicts, every later seal carries them too.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  known_facts:
  - fact: A change to the derive route changes every design the route derives, for every domain at once.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: Today a route change runs as its own dossier, holding a note that says what changed and why.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: Today nothing judges a route change's dossier.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A change whose deliverable is authored, not constructed, runs the phases from the seed to governance intent and is complete there.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: The derive route's rules and code are written by a person, and construction renders none of them.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: A phase document is judged by the rule set sealed in the composition its dossier pins.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: Seals recorded before this change carry a note and no verdicts, and they stay as they are.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: This change is itself a route change, and the first judged by the phases.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  system_beliefs:
  - belief: The composition already holds the phase workflows that judge each phase from the seed to governance intent.
    why_it_matters: A route change can be judged only by phases the composition already carries.
    verification_goal: Confirm the composition holds a judging workflow for each phase from the seed to governance intent.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The lifecycle's governance already states that a change whose deliverable is authored is complete at governance intent.
    why_it_matters: The change relies on that ruling rather than making a new one.
    verification_goal: Confirm the lifecycle's governance states the ruling.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  assumptions: []
  constraints:
  - constraint: A sealed dossier is never judged again against a later composition.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: The rule sets that judge a dossier are the ones sealed in the composition it pins.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 2}
  business_invariants:
  - invariant: A route is in force only when a seal records it.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: A seal judged by the phases records an admissible verdict for every phase from the seed to governance intent.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: No seal without verdicts follows a seal with them.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  lifecycle_states:
  - object: Route Change
    state: Proposed
    meaning: Its dossier is being written, and no seal records it.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Route Change
    state: Sealed
    meaning: A seal records it, with an admissible verdict for every phase.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  business_events:
  - event: Route Change Sealed
    when_it_occurs: When every phase document of the dossier is admissible and the seal is recorded.
    significance: The derive route as the change left it may derive designs.
    source_finding: {phase: p0, register: business_events, row: 1}
  authority_boundaries:
  - business_object: Route Change
    authoritative_owner: The person who authors the dossier
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: Phase Verdict
    authoritative_owner: Design
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Seal
    authoritative_owner: Design
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  out_of_scope:
  - item: Judging a route change past governance intent.
    reason: Nothing in a route change is constructed.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Judging a sealed dossier again against a later composition.
    reason: A dossier is judged against the composition it pins.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Changing what the derive route derives.
    reason: This change governs how the route is changed, not what it does.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  governance_scope:
  - scope_item: design
    relationship: EXTENDED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: lifecycle
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 2}
  clarification_requests: []
  acceptance_criteria:
  - criterion: A route change whose dossier lacks a phase document from the seed to governance intent is refused its seal.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: A route change whose phase document is inadmissible is refused its seal.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: A sealed route change records the verdict of every phase and the rule set that gave it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: A seal without verdicts after a seal with them is refused.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  identity_and_sameness: null
  lifecycle_transitions: null
  operation_refusals:
  - operation: Seal a route change
    refused_when: Its dossier lacks a phase document from the seed to governance intent, or one is inadmissible.
    business_reason: A route change reaches every domain, and is held to the same phases as any other change.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  authority_deferrals: null
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
