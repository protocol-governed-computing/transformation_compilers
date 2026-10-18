# STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0

## 1. Intent

Each design phase P0–P8 is judged by one register schema, sealed into one workflow, and authored
from one template. This structure states that dispatch once. The design compiler reads it to load a
phase's schema, to emit its rule set into its workflow, and to name the workflows a design may cite.

## 2. What a row states

| Field | Meaning |
|---|---|
| `phase` | The phase identity, `p0` to `p8`. |
| `schema` | The `$id` of the register schema the phase is judged by. |
| `workflow` | The admissibility workflow its rule set is sealed into. |
| `template` | The template a document of the phase is authored from. |
| `rung` | The vocabulary class the phase adds on the purity ladder. |
| `purpose`, `question`, `key_rule` | What the phase is for, the question it answers, and the rule an author keeps. |
| `gate` | The human gate that closes the phase, or `null` where none does. |

A phase's order in `phases` is its order in the pipeline. The phase after a phase is the next row.

## 3. Why this is declared rather than coded

The dispatch was two Python tables. One named each phase's schema file and template. The other named
the workflow each rule set is sealed into. A third copy, the workflows a design may cite, was written
into the P7 register schema by hand. Three copies of one fact drift. Here it is stated once, and
changing it is a new version of this structure.

---

## Machine

```yaml
fqdn: transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: transformation

core:
  summary: Which register schema, workflow and template each design phase dispatches to
  phases:
  - phase: p0
    schema: transformation.schemas.REGISTER_SCHEMA_P0_V0
    workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V0
    template: p0_change_seed_template_v0.md
    rung: business_language
    purpose: change seed
    question: What does the business want, stated in its own words?
    key_rule: Faithful rewrite only — no content added, no clarification resolved, no design assigned
    gate: Gate 0 — the human confirms the seed says what they meant
  - phase: p1
    schema: transformation.schemas.REGISTER_SCHEMA_P1_V0
    workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
    template: p1_change_request_template_v0.md
    rung: business_language
    purpose: change request
    question: Classification · Problem · Outcome · Known Facts · Deferrals
    key_rule: Business language only; baseline claims verified against the snapshot, never memory
    gate: null
  - phase: p2
    schema: transformation.schemas.REGISTER_SCHEMA_P2_V0
    workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0
    template: p2_domain_model_template_v0.md
    rung: business_language
    purpose: domain model
    question: Entities · Processes · Baseline fit · Gaps
    key_rule: Record what was searched, not only what was found
    gate: null
  - phase: p3
    schema: transformation.schemas.REGISTER_SCHEMA_P3_V0
    workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0
    template: p3_analysis_loop_template_v0.md
    rung: business_language
    purpose: analysis loop
    question: How is each gap resolved, iterated to Discovery Saturation?
    key_rule: Every answer carries evidence; overturned answers are marked, never erased
    gate: null
  - phase: p4
    schema: transformation.schemas.REGISTER_SCHEMA_P4_V0
    workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0
    template: p4_business_model_template_v0.md
    rung: business_language
    purpose: business model
    question: What is the canonical consolidation every later phase projects from?
    key_rule: Consolidation, not re-litigation
    gate: null
  - phase: p5
    schema: transformation.schemas.REGISTER_SCHEMA_P5_V0
    workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0
    template: p5_business_intent_template_v0.md
    rung: provisional_codes
    purpose: business intent
    question: WHAT — behaviour, objects, identity, invariants, actions
    key_rule: Provisional capability names are admissible; no bindings, no paths
    gate: null
  - phase: p6
    schema: transformation.schemas.REGISTER_SCHEMA_P6_V0
    workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
    template: p6_governance_intent_template_v0.md
    rung: placement
    purpose: governance intent
    question: WHERE — domain and subdomain, ownership, dependencies
    key_rule: No new artifact codes; cross-subdomain writes forbidden
    gate: null
  - phase: p7
    schema: transformation.schemas.REGISTER_SCHEMA_P7_V0
    workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    template: p7_design_intent_template_v0.md
    rung: binding_fqdns
    purpose: design intent
    question: HOW — FQDNs, topology, schemas, stores, module paths, runtime bindings
    key_rule: The full dossier is reviewed as a body
    gate: Gate 1 — Design Approval
  - phase: p8
    schema: transformation.schemas.REGISTER_SCHEMA_P8_V0
    workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0
    template: p8_authoring_mandate_template_v0.md
    rung: build_order
    purpose: authoring mandate
    question: IN WHAT ORDER — topologically sorted build waves
    key_rule: Mechanical derivation; must reconcile with p7 exactly
    gate: Gate 2 — Mandate Approval; the dossier is locked
```
