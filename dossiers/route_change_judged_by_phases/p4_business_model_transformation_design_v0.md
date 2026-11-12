# Stage 4 — Business Model — transformation / design

## Machine

```yaml
document:
  phase: p4
  domain: transformation
  subdomain: design
  cr: route_change_judged_by_phases
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Author of a route change
    role: Writes the dossier of a route change and asks for its seal
    authority_class: Operator
    source_finding: {phase: p2, register: business_processes, row: 1}
  bm_entities:
  - entity: Route change
    description: A change to the doctrine, the ledger schema, the catalog or a building block of the derive route.
    store_model: One dossier per route change, kept in the repository as evidence and never in the composition.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: Seal
    description: The record that the derive route as it stands is the one a route change left.
    store_model: An ordered list of seals, oldest first, carried with the derive route and never edited.
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: Phase verdict
    description: Whether a phase document is admissible against the documents before it, by a named rule set.
    store_model: Recorded on the seal it decided, one per phase from the seed to governance intent.
    source_finding: {phase: p2, register: entities, row: 3}
  resources: []
  events:
  - event: Route change sealed
    trigger: When every phase document of the dossier is admissible and the seal is recorded
    lifecycle_meaning: The derive route as the change left it may derive designs.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: Seal
    verb: records
    object: Phase verdict
    capability_need: Show which rule sets admitted a route change
    source_finding: {phase: p2, register: entity_attributes, row: 2}
  capability_graph:
  - capability: Refusing a seal unless every phase document is admissible
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    status: GAP
    gap_register_entry: GAP-01
    notes: Authored in the derive route, which calls the judging workflows as they are declared.
  - capability: Recording each phase verdict on the seal
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    status: GAP
    gap_register_entry: GAP-02
    notes: Authored in the derive route, which alone writes seals.
  dependency_graph:
  - from: transformation
    to: transformation::WF_P0_SEED_ADMISSIBILITY_V0
    dependency_type: judgement
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 1}
  - from: transformation
    to: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
    dependency_type: judgement
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 2}
  constraint_register:
  - number: '1'
    constraint: A route is in force only when a seal records it.
    source_finding: {phase: p1, register: business_invariants, row: 1}
    source: invariant
  - number: '2'
    constraint: A seal judged by the phases records an admissible verdict for every phase from the seed to governance intent.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '3'
    constraint: No seal without verdicts follows a seal with them.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '4'
    constraint: A sealed dossier is never judged again against a later composition.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: constraint
  - number: '5'
    constraint: The rule sets that judge a dossier are the ones sealed in the composition it pins.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: constraint
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    capability: Refusing a seal unless every phase document is admissible
    owner_subdomain: design
    resolution: AUTHOR_NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    capability: Recording each phase verdict on the seal
    owner_subdomain: design
    resolution: AUTHOR_NEW
  design_decisions:
  - number: '1'
    decision: Design stays the subdomain it is; the change extends it.
    source_finding: {phase: p3, register: placement_decision, row: 1}
    rationale: The derive route belongs to Design, and judging its changes uses the phases Design already holds.
    constraints_imposed: The judging workflows are called as they are declared.
  authoring_scope:
  - capability: Refusing a seal unless every phase document is admissible
    gap_register_ref: GAP-01
  - capability: Recording each phase verdict on the seal
    gap_register_ref: GAP-02
```

Consolidated from the analysis. Every row cites what it consolidates.

---

## 1. Discovery Summary

---

## 2. Capability Graph (capability_graph)

---

## 3. Dependency Graph (dependency_graph)

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)
