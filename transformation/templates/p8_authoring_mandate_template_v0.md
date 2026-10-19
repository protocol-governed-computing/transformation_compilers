# Authoring Mandate: [domain] / [subdomain]

## Machine

```yaml
document:
  phase: p8
  domain: <domain>
  subdomain: <subdomain>
  cr: <change>
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
  # approval: {gate: ..., rule_set: ..., state: APPROVED} — when the gate closes
registers:
  build_order:
  - wave: null
    step: null
    code: null
    action: null
    subdomain: null
    depends_on: null
  critical_path:
  - position: null
    code: null
  mandate_artifact_summary:
  - action: null
    count: null
    description: null
  field_declarations:
  - code: null
    subdomain_field: null
  new_capabilities:
  - code: null
    purpose: null
    inputs: null
    outputs: null
  new_intents:
  - code: null
    purpose: null
    workflow: null
    inputs: null
  cross_subdomain_notes:
  - code: null
    note: null
```

## Document Contract

**This artifact is a structured register document — not a narrative.** S7 is mechanical: it
re-orders the artifacts Stage 7 already assigned into a build sequence. The worker emits register
ROWS; a deterministic renderer owns the document; a cross-stage oracle checks the codes against the
Stage 7 registers.

VALID OUTPUT:
- Populated registers (every required register below)
- Every `code` cell a binding FQDN copied VERBATIM from a Stage 7 register

INVALID OUTPUT:
- Narrative summaries replacing registers
- A code not present in the Stage 7 `new_artifacts` / `existing_inventory` registers
- A non-contiguous `step` sequence (a gap means a silently dropped artifact)

---

### Mandate discipline (the oracle enforces these)

- **No design here.** S7 adds nothing and drops nothing — it ORDERS what Stage 7 assigned. No new
  codes, no new actions.
- **Copy every code VERBATIM from the Stage 7 registers** — never re-type, re-spell, or introduce
  a code. A binding FQDN is immutable; re-typing one (even a transposed letter) mints a second,
  permanently-misnamed artifact. Every code in this mandate MUST appear in a Stage 7 register
  (`new_artifacts` for NEW, `existing_inventory` for REPLACE/EXTEND).
- **Reconcile:** the NEW / REPLACE / EXTEND counts in `mandate_artifact_summary` MUST equal Stage
  P7's `artifact_summary`. `step` numbering is contiguous from 1.

---

## Stage Inputs — Questions for the Human

| # | Question for the Human | How the Agent Uses the Answer (Intent) |
|---|------------------------|----------------------------------------|
| 1 | Gate 2: approve this mandate, locking the dossier before authoring begins? | Gate 2 freezes scope. After it, any departure is an Approved Deviation in the Stage 8 manifest — never a silent change. |
| 2 | Any sequencing constraints beyond the dependency graph (e.g., author a risky artifact first)? | Adjusts `wave` ordering without changing the dependency-derived topological order. |

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

## 1. Build Dependency Order

*Topological sort of Stage 7's `new_artifacts` over the dependencies in `execution_topology` /
`rb_declarations`. ONE row per artifact to AUTHOR — `action` ∈ NEW / REPLACE / EXTEND only. A
REUSE / existing dependency is NOT authored: reference it in `depends_on`, never as its own row.
`step` is the GLOBAL execution order, contiguous from 1 across all waves; `wave` groups parallel
work. `code` is copied verbatim from a Stage 7 register; `depends_on` lists prerequisite codes (or `—`).*

Register `build_order` in the Machine block.

---

## 2. Critical Path

*The longest sequential dependency chain, in order. Each `code` is a build_order step on the
critical path.*

Register `critical_path` in the Machine block.

---

## 3. Artifact Summary

*Authoring action counts, for Stage 8 input. Reconciles against Stage 7 `artifact_summary`.*

Register `mandate_artifact_summary` in the Machine block.

---

## 4. Subdomain Field Declarations

*The `subdomain` field for every WF / CC / EV / RB artifact — governs trace routing and data-store
path resolution. `code` is copied verbatim from a Stage 7 register.*

*Scheduled **and amended** alike. An artifact this change extends or replaces is never a build step,
so nothing in the build order names it, and a workflow whose subdomain went undeclared rendered an
empty one while every rule passed. The artifact already sits in a subdomain; this states which,
because construction has no view of the composition to read it from.*

Register `field_declarations` in the Machine block.

---

## 5. New Capabilities

*New CT/capability declarations — **business intent only**. `Code` is a binding FQDN from a Stage 7 `new_artifacts` row; `Purpose` is business language; `Inputs`/`Outputs` are typed fields written `name:type` (comma-separated, e.g. `block:object`). The Construction Compiler realizes these into candidate CT contracts — it derives ALL protocol realization (purity, governing constitution, machine/implementation binding). You declare only intent. Nothing new → leave empty.*

Register `new_capabilities` in the Machine block.

---

## 6. New Intents

*New IN (ingress) declarations — **business intent only**. `Code` is a binding FQDN from `new_artifacts`; `Purpose` is business language; `Workflow` is the WF this intent admits into (a design decision — the FQDN); `Inputs` is the typed payload written `name:type` (comma-separated — only what ARRIVES at the intent boundary). The Construction Compiler realizes these into candidate IN contracts. Nothing new → leave empty.*

Register `new_intents` in the Machine block.

---

## 7. Cross-Subdomain Notes

*Artifacts that make cross-subdomain calls (permitted) or would write cross-subdomain (forbidden — must be a peer-owned dependency-gap CC). Audit only.*

Register `cross_subdomain_notes` in the Machine block.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | design_intent_[subdomain]_v0.md | GATE 1 APPROVED |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring (authoring tier) | per build_order | PENDING |
| Stage 8 — Authoring Manifest | post-authoring | PENDING |

---

## gov_projection — Governed Handoff to Artifact Authoring

*The bounded inputs and emit keys mirror the engine's gov_projection schema exactly
(`contracts/gov_projection.py`). S7 consumes all five Stage 7 registers and emits the four the
authoring step builds from. Emit keys match the register ids above exactly.*

| Direction | Registers |
|-----------|-----------|
| **Consumes** ← p7 | new_artifacts · existing_inventory · rb_declarations · execution_topology · artifact_summary |
| **Emits** | build_order · critical_path · mandate_artifact_summary · field_declarations |
