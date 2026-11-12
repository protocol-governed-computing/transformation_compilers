# Stage 5 — Business Intent — transformation / design

## Machine

```yaml
document:
  phase: p5
  domain: transformation
  subdomain: design
  cr: route_change_judged_by_phases
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Design subdomain governs how a change to a composition becomes a design: the phases that judge
    a design someone authored, and the derive route that derives one from an owner's answers. This
    change governs how the derive route itself is changed.
  purpose_provenance:
  - source: Change seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: null
  subdomain_purposes:
  - subdomain: design
    purpose: Design judges every change to the derive route by the phases, from the seed to governance intent, before it seals it.
    source_finding: {phase: p0, register: cr_type, row: 1}
  scope_boundary:
  - capability: Refusing a seal unless every phase document is admissible
    status: IN_SCOPE
    notes: A route change is sealed only when its dossier is admissible from the seed to governance intent
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - capability: Recording each phase verdict on the seal
    status: IN_SCOPE
    notes: The seal names each verdict and the rule set that gave it
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - capability: Refusing a seal without verdicts after a seal with them
    status: IN_SCOPE
    notes: Earlier seals stay as history; later ones carry verdicts
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - capability: Judging a route change past governance intent
    status: DEFERRED
    notes: Nothing in a route change is constructed
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - capability: Judging a sealed dossier again against a later composition
    status: DEFERRED
    notes: A dossier is judged against the composition it pins
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  business_objects:
  - store_name: Seal journal
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: A seal is written once, when its route change is admitted, and never edited, so the journal shows every route the derive route has been.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  identity_semantics:
  - store_name: Seal journal
    identity_field: Dossier
    source: The route change's dossier
    uniqueness_rule: Two seals are the same when they record the same route.
    cross_subdomain_relationship: None
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  invariants:
  - invariant: A route is in force only when a seal records it.
    business_reason: A route no seal records was changed outside a dossier.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: A seal judged by the phases records an admissible verdict for every phase from the seed to governance intent.
    business_reason: A route change reaches every domain, and is held to the same phases as any other change.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: No seal without verdicts follows a seal with them.
    business_reason: Once route changes are judged by the phases, none may skip them.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  actions:
  - action: Seal a route change
    object: route change
    trigger: Requested by the author of the route change
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  provisional_codes: []
  cross_subdomain_refs: []
```

Every row cites the seed row it states.

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References
