# Business Model: [domain] / [subdomain]

## Machine

```yaml
document:
  phase: p4
  domain: <domain>
  subdomain: <subdomain>
  cr: <change>
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: null
    role: null
    authority_class: null
    source_finding: null
  bm_entities:
  - entity: null
    description: null
    store_model: null
    source_finding: null
  resources:
  - resource: null
    description: null
    source_finding: null
  events:
  - event: null
    trigger: null
    lifecycle_meaning: null
    source_finding: null
  relationships:
  - subject: null
    verb: null
    object: null
    capability_need: null
    source_finding: null
  capability_graph:
  - capability: null
    source_finding: null
    status: null
    gap_register_entry: null
    notes: null
  dependency_graph:
  - from: null
    to: null
    dependency_type: null
    pps_status: null
    source_finding: null
  constraint_register:
  - number: null
    constraint: null
    source_finding: null
    source: null
  gap_register:
  - gap_code: null
    source_finding: null
    capability: null
    owner_subdomain: null
    resolution: null
  design_decisions:
  - number: null
    decision: null
    source_finding: null
    rationale: null
    constraints_imposed: null
  authoring_scope:
  - capability: null
    gap_register_ref: null
```

## Document Contract

**This artifact is a structured register document — not a narrative.**

VALID OUTPUT:
- Populated registers (every required register below)
- Existing artifact references by exact FQDN — only where a column explicitly permits it
- Business-language capability entries

INVALID OUTPUT:
- Narrative summaries
- Reasoning essays
- Executive summaries
- Free-form prose replacing required registers

A register with nothing to state is `[]`, declared empty. A register left `null` states nothing,
and a required register that states nothing is refused.

Narrative text does NOT satisfy register population requirements. A prose-only or empty
register is a structural defect, not brevity — the renderer rejects the document mechanically
before any human reviews it.

---

### Business-Language Rule

The following registers MUST NOT contain protocol artifact names or FQDNs:

- Discovery Summary (Actors / Entities / Resources / Events / Relationships)
- Capability Graph
- Gap Register

Capabilities are expressed in **business language only**. Naming solution artifacts here is a
design-leakage defect — protocol FQDNs are introduced at Stage 5 (provisional codes) and
Stage 7 (binding FQDNs), never in the Business Model.

VALID:
- Commit a validated block to the canonical chain
- Initialize the chain from a genesis state

INVALID:
- CC_COMMIT_BLOCK_TO_CHAIN_V0
- WF_RUN_GENESIS_BOOTSTRAP_WORKFLOW_V0

(The Dependency Graph and Authoring Scope MAY cite existing PPS artifacts by FQDN; the
Resolution column of the Gap Register names a disposition — NEW | REUSE | REPLACE — not an
artifact.)

**WHERE FQDNs GO.** When a row is grounded in an existing artifact, the FQDN goes ONLY in that
row's **Source Finding** column — NEVER in a content/description cell (Actor, Role, Entity,
Description, Capability, Subject / Verb / Object, Capability Need). Write the *business meaning* in
the content cell and let the FQDN in Source Finding carry the proof.
INVALID: `Capability Need = "block formation (CC_FORM_BLOCK_V0)"`.
VALID: `Capability Need = "form a block from a proposer and pending transactions"` ·
`Source Finding = artifact_source for blockchain::CC_FORM_BLOCK_V0`. The renderer rejects an FQDN
found in a content cell.

---

### Stage 4 execution rules

- This document **consolidates** Stages 1–3 — it does not re-litigate findings or introduce new design.
- **Every row traces to a prior-stage finding** (the Source Finding column). A row with no
  source is inadmissible — `CONCERN_TRACEABILITY_REQUIRED`.
- **Consistency check:** every CRITICAL row in the Capability Graph has a Gap Register entry
  with an owner subdomain; a capability that requires a NEW artifact in a peer subdomain is a
  GAP owned by that peer (dependency gap), never SATISFIED.
- **State-lifecycle completeness:** every state-lifecycle concern surfaced in Stage 3
  (creation, transition, immutability, persistence, cryptographic linkage, …) MUST appear in
  the Constraint Register OR the Design Decisions register before this stage can complete.

---

### Citing a prior row

Every row carries a `source_finding` naming where its content came from. A citation is a mapping:

- **a row of a register**, by ordinal or by key, in the phase that declared it:
  `{phase: p1, register: known_facts, row: 14}`. A citation that names no phase names this document;
- **an artifact already in the baseline**, by exact identity: `{artifact: blockchain::WF_REGISTER_ACTOR_V0}`;
- **a person**: `{source: human}`.

Several citations are a list. A row that cites nothing is `null`, and is refused where the register
requires provenance.

**A carried claim is carried verbatim.** Where a register restates a row an earlier phase declared —
a belief, an authoring decision, a capability — the text must match that row exactly. Tightening a
sentence while citing the row it came from is how a claim drifts from what was decided, so the rules
treat a tidier synonym as a new claim and refuse it. Cite it as it stands, or change it in the phase
that owns it.

---

## 1. Discovery Summary

*Produced by Stages 1–3 (Input Elicitation → Domain Model Discovery → Analysis Loop). This section is the accumulated output of convergence — do not edit it to make it "cleaner." It is a record of what analysis discovered, not a polished narrative.*

Register `actors` in the Machine block.
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|

Register `bm_entities` in the Machine block.
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|

Register `resources` in the Machine block.
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|

Register `events` in the Machine block.
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|

*A relationship implies a capability. Name that capability as a **business need** in Capability
Need (business language — no artifact names). If an existing or candidate artifact is relevant,
cite its FQDN in **Source Finding** only — never in the Capability Need cell.*

Register `relationships` in the Machine block.
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|

---

## 2. Capability Graph (capability_graph)

*Every capability discovered during Analysis Loop. CRITICAL = must author this CR. ADVISORY = should author. SATISFIED = exists in PPS. Capability column is business language — no FQDNs.*

> **Release boundary.** A capability deferred in `out_of_scope` (S1 §12) is NOT part of this CR — do
> not list it here in any status, and never promote it to a CRITICAL gap. The oracle drops governed
> coverage for a capability row that names a deferred item.

Register `capability_graph` in the Machine block.

---

## 3. Dependency Graph (dependency_graph)

*Cross-subdomain dependencies discovered. Declared dependencies constrain authoring order. Existing PPS artifacts MAY be cited by FQDN here.*

Register `dependency_graph` in the Machine block.

---

## 4. Constraint Register (constraint_register)

*Non-negotiable rules discovered during analysis. Each constraint has a business source.*

Register `constraint_register` in the Machine block.

---

## 5. Gap Register (gap_register)

*All CRITICAL gaps. Each gap must be resolved before authoring begins. Capability is business language; Resolution is a disposition, not an artifact name.*

Register `gap_register` in the Machine block.

---

## 6. Design Decisions (design_decisions)

*Decisions accumulated during Stages 1–3 that constrain Design Intent. Each decision locks in an architectural choice.*

Register `design_decisions` in the Machine block.

---

## 7. Authoring Scope (authoring_scope)

*What is IN this CR vs. FUTURE CR. This is the governance boundary decision that filters the Business Model into the Business Intent.*

Register `authoring_scope` in the Machine block.
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | PENDING |

---

## gov_projection — Governed Handoff to Stage 5

*Governed, lossless, identity-preserving (defined in Stage 0 / field manual §4.7). Every identity and concern in a **Consumes** field reappears in the corresponding **Emits** field transform-free, unless explicitly deferred with a recorded reason; no field is dropped silently. Emit keys match the register ids above exactly.*

*S4 is the hub — it consolidates Stages 1–3. The bounded inputs below mirror the engine's
gov_projection schema exactly (`contracts/gov_projection.py`).*

| Direction | Registers |
|-----------|-----------|
| **Consumes** ← p3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
