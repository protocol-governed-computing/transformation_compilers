# Stage 4 — Business Model: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p4
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_03_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Catalog
    role: Performs the acts, and states what each of them completed.
    authority_class: Declaring — an announcement is the act's own account of what it did.
    source_finding: {phase: p1, register: cr_type, row: 1}
  - actor: Library staff
    role: Perform the acts the catalog admits.
    authority_class: Acting — unchanged by this change.
    source_finding: {phase: p2, register: actors, row: 1}
  - actor: The platform
    role: Seals the moments an act announces, in order, and announces each when the act reaches its ending.
    authority_class: Enabling — the capability this change waited for.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  bm_entities:
  - entity: Moment
    description: Something the business declares occurred, stated by the act that completed it.
    store_model: Six are declared; none is announced.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: Act
    description: Something the catalog does as one unit, which completes or is refused.
    store_model: Nine, each admitted by its own intent.
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: Announcement
    description: What an act states at its ending about the moments it completed.
    store_model: None exists anywhere in this subdomain.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  resources:
  - resource: The six declared moments
    description: Registered work, registered book, registered physical copy, updated bibliographic information, retired book, retired physical copy. Referenced by nothing.
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - resource: The act that completes three
    description: Registering a book admits a work, its first edition and that edition's first physical copy.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  - resource: The capability the platform now holds
    description: An ordered sequence announced at one ending, a repeat refused, an announcement that cannot be made reported.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  events:
  - event: An act announced what it completed
    trigger: An act reaching an ending it declares announcements for
    lifecycle_meaning: The business has an account of what happened, which it has never had.
    source_finding: {phase: p1, register: business_events, row: 1}
  - event: A declared moment stayed silent
    trigger: An act completing a moment and stating nothing
    lifecycle_meaning: The state this change ends; it is the present state of every act.
    source_finding: {phase: p2, register: belief_verification, row: 1}
  relationships:
  - subject: Act
    verb: announces
    object: Moment
    capability_need: Announcing the three moments registering a book completes.
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
  - subject: Act
    verb: announces
    object: Moment
    capability_need: Announcing the moment each remaining act completes.
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
  - subject: Catalog
    verb: attaches
    object: Moment
    capability_need: Attaching the moment naming a registered work to the act that claims its identity.
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
  capability_graph:
  - capability: Announcing the three moments registering a book completes
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    status: CRITICAL
    gap_register_entry: GAP-1
    notes: The act this dossier halted for; three moments at one ending.
  - capability: Announcing the moment each remaining act completes
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    status: CRITICAL
    gap_register_entry: GAP-2
    notes: Five acts, one moment each — a sequence of one.
  - capability: Attaching the moment naming a registered work to the act that claims its identity
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    status: SATISFIED
    gap_register_entry: ''
    notes: 'The composition decides it: one act claims the work, the other resolves it.'
  - capability: Announcing an ordered sequence at one ending
    source_finding: {phase: p3, register: dependency_discoveries, row: 1}
    status: SATISFIED
    gap_register_entry: ''
    notes: The platform states the model, holds it, seals the order and keeps it.
  dependency_graph:
  - from: catalog
    to: workflow
    dependency_type: data read
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 1}
  - from: catalog
    to: event
    dependency_type: data read
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 2}
  - from: catalog
    to: catalog
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 3}
  constraint_register:
  - number: '1'
    constraint: An act announces every moment it completed, or the business has no account of what happened.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: governance rule
  - number: '2'
    constraint: A moment is attached to the act that completes it, never to one that merely touches the same records.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
    source: governance rule
  - number: '3'
    constraint: The business is not reshaped to suit what the platform could express.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: governance rule
  - number: '4'
    constraint: Only moments the business already declared are announced.
    source_finding: {phase: p3, register: verification_results, row: 4}
    source: governance rule
  - number: '5'
    constraint: A limitation paid in silence produces no account at all, and no check anywhere notices.
    source_finding: {phase: p2, register: belief_verification, row: 3}
    source: domain knowledge
  gap_register:
  - gap_code: GAP-1
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    capability: Announcing the three moments registering a book completes
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-2
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    capability: Announcing the moment each remaining act completes
    owner_subdomain: catalog
    resolution: EXTEND
  design_decisions:
  - number: '1'
    decision: Registering a book announces three moments at one ending.
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    rationale: The act completes all three and is the only act that does.
    constraints_imposed: Rules out announcing one and leaving two silent, and rules out splitting the act.
  - number: '2'
    decision: 'The order announced is the order the business completes them: the work, then the book, then the physical copy.'
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
    rationale: The order is normative and a reader of the account sees it; the business's own order is the one that reads correctly.
    constraints_imposed: Fixes the order in the design rather than leaving it to how the composition was sealed.
  - number: '3'
    decision: Each remaining act announces the one moment it completes.
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    rationale: Five acts complete one moment each and can say so; a sequence of one is what the platform already ran.
    constraints_imposed: Rules out leaving any declared moment silent.
  - number: '4'
    decision: Reinstatement announces nothing.
    source_finding: {phase: p3, register: verification_results, row: 4}
    rationale: The business declared no moment for it, and this change announces only moments the business already declared.
    constraints_imposed: Rules out authoring a moment to fill a gap the business has not stated.
  authoring_scope:
  - capability: Announcing the three moments registering a book completes
    gap_register_ref: GAP-1
  - capability: Announcing the moment each remaining act completes
    gap_register_ref: GAP-2
```

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

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

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| A moment naming a reinstatement | The business has declared none; authoring one here would invent business content. |
| Refusing a declared moment that nothing announces | Its own question, and answering it here would refuse moments that are correct today. |
| A moment announced per member of a collection | A different shape; this change announces a known few, named where the act is designed. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
