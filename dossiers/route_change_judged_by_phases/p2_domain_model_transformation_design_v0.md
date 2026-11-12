# Stage 2 — Domain Model — transformation / design

## Machine

```yaml
document:
  phase: p2
  domain: transformation
  subdomain: design
  cr: route_change_judged_by_phases
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Route change
    description: A change to the doctrine, the ledger schema, the catalog or a building block of the derive route.
    store_model: One dossier per route change, kept in the repository as evidence and never in the composition.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: Seal
    description: The record that the derive route as it stands is the one a route change left.
    store_model: An ordered list of seals, oldest first, carried with the derive route and never edited.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - entity: Phase verdict
    description: Whether a phase document is admissible against the documents before it, by a named rule set.
    store_model: Recorded on the seal it decided, one per phase from the seed to governance intent.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 4}
  entity_attributes:
  - entity: Route change
    attribute: Pin
    meaning: The composition the route change is designed against, whose sealed rule sets judge it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, row: 6}
  - entity: Seal
    attribute: Phase verdicts
    meaning: The verdict of each phase from the seed to governance intent, and the rule set that gave it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  business_processes:
  - process: Seal a route change
    initiator: The person who authors the dossier
    outcome: The derive route as the change left it may derive designs.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  process_steps:
  - process: Seal a route change
    step: '1'
    action: Refuse when the dossier lacks a phase document from the seed to governance intent
    record_produced: A refusal, and no seal
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Seal a route change
    step: '2'
    action: Judge each phase document against the documents before it, by the rule sets sealed in the composition the dossier pins
    record_produced: One phase verdict per phase
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Seal a route change
    step: '3'
    action: Refuse when any phase verdict is inadmissible
    record_produced: A refusal, and no seal
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Seal a route change
    step: '4'
    action: Record the seal with every phase verdict
    record_produced: A seal
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  belief_verification:
  - belief: The composition already holds the phase workflows that judge each phase from the seed to governance intent.
    result: VERIFIED
    evidence: The composition holds transformation::WF_P0_SEED_ADMISSIBILITY_V0 and transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0, and a judging workflow for every phase between them.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The lifecycle's governance already states that a change whose deliverable is authored is complete at governance intent.
    result: NOT_FOUND
    evidence: lifecycle::CONSTITUTION_CHANGE_MGMT_V0 states that each phase answers one question and that governance intent says where a change is owned. The ruling that an authored change is complete there is stated in the repository's account of a change, not in the composition.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  pps_baseline_fqdns:
  - capability: Judging a seed
    fqdn: transformation::WF_P0_SEED_ADMISSIBILITY_V0
    what_it_does: Judges a seed by the rule set sealed for the seed phase.
    fit: EXACT
    cannot_do: It judges one document; it does not decide whether a route change may be sealed.
  - capability: Judging governance intent
    fqdn: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
    what_it_does: Judges a governance intent against the business intent and the seed before it.
    fit: EXACT
    cannot_do: It judges one document; it does not decide whether a route change may be sealed.
  - capability: Governing the change lifecycle
    fqdn: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
    what_it_does: States the principles every dossier is judged by.
    fit: PARTIAL
    cannot_do: It does not state that an authored change is complete at governance intent.
  gaps:
  - gap: Nothing refuses a route change whose dossier is not judged by the phases.
    severity: MAJOR
    impact: A change that reaches every domain is held to less than a change to one domain.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 3}
  - gap: A seal records no phase verdict.
    severity: MINOR
    impact: A seal cannot show which rule sets admitted its route change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  architectural_observations:
  - observation: Every phase a route change needs is already judged by a workflow the composition holds, so the change adds no judging of its own.
    evidence: transformation::WF_P0_SEED_ADMISSIBILITY_V0 · transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  discovery_concerns:
  - concern: The ruling that an authored change is complete at governance intent is not in the composition, so this change relies on the repository's statement of it.
    evidence: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  open_questions: []
```

Every row cites the change-request row it models.

---

## 1. Business Entities

---

## 2. Business Processes

---

## 3. Belief Verification — THE SPINE (fill this register FIRST)

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3
