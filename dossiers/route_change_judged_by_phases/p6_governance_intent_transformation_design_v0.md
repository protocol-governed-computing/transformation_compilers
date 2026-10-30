# Stage 6 — Governance Intent — transformation / design

## Machine

```yaml
document:
  phase: p6
  domain: transformation
  subdomain: design
  cr: route_change_judged_by_phases
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Refusing a seal unless every phase document is admissible
    owner_subdomain: design
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 1}
  - capability: Recording each phase verdict on the seal
    owner_subdomain: design
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 2}
  - capability: Refusing a seal without verdicts after a seal with them
    owner_subdomain: design
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 3}
  - capability: Judging a route change past governance intent
    owner_subdomain: design
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 4}
  - capability: Judging a sealed dossier again against a later composition
    owner_subdomain: design
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 5}
  storage_governance:
  - storage_need: A journal of seals
    purpose: A seal is written once, when its route change is admitted, and never edited, so the journal shows every route the derive route has been.
    subdomain: design
    source_finding: {phase: p5, register: business_objects, row: 1}
  cross_subdomain_deps: []
  pps_artifacts_requiring_action: []
  boundary_rules:
  - rule_name: DESIGN_OWNS_ITS_SEALS
    statement: Only the derive route writes a seal, and only when every phase document of the route change's dossier is admissible.
    source_finding: {phase: p5, register: subdomain_purposes, row: 1}
  governance_outcome:
  - capability: Refusing a seal unless every phase document is admissible
    owner_subdomain: design
    source_finding: {phase: p6, register: ownership, key: Refusing a seal unless every phase document is admissible}
  - capability: Recording each phase verdict on the seal
    owner_subdomain: design
    source_finding: {phase: p6, register: ownership, key: Recording each phase verdict on the seal}
  - capability: Refusing a seal without verdicts after a seal with them
    owner_subdomain: design
    source_finding: {phase: p6, register: ownership, key: Refusing a seal without verdicts after a seal with them}
```

A route change authors code and sealed documents, which construction does not render, so this
dossier is complete at governance intent.

---

## 1. Subdomain Boundary — Ownership

---

## 2. Storage Governance Requirements

---

## 3. Cross-Subdomain Dependency Declaration

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome
