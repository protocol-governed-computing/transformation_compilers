# Domain Model — transformation / phases

## Machine

```yaml
document:
  phase: p2
  domain: transformation
  subdomain: phases
  cr: new_subdomain
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Seed
    description: The business problem statement reorganized into fixed registers.
    store_model: Held as a document outside the composition; never stored as protocol state.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_vocabulary, key: Seed}
  - entity: Rule Set
    description: The declared conditions deciding whether a document is admissible.
    store_model: Carried as declared input on the phase workflow, sealed with it.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_vocabulary, key: Rule Set}
  - entity: Verdict
    description: 'The outcome of applying a rule set: admissible or inadmissible.'
    store_model: Returned by the phase; not persisted.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_vocabulary, key: Verdict}
  - entity: Finding
    description: One recorded failure of one rule.
    store_model: Returned within the verdict; not persisted.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_vocabulary, key: Finding}
  - entity: Author of Record
    description: The person accountable for a document's content.
    store_model: An actor identity bound by the phase workflow.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, key: Author of Record}
  entity_attributes:
  - entity: Verdict
    attribute: admissibility
    meaning: Whether the document may proceed to the next phase.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - entity: Verdict
    attribute: rules evaluated
    meaning: How many rules were applied — every rule, always.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - entity: Finding
    attribute: rule
    meaning: The rule that produced the finding.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - entity: Rule Set
    attribute: active version
    meaning: The declared rules currently deciding admissibility.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: lifecycle_states, key: Rule Set}
  - entity: Rule Set
    attribute: sealed copy
    meaning: The rules as carried in the phase's own compiled artifact, generated from the declaration rather than typed.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 14}
  - entity: Seed
    attribute: carried form
    meaning: The whole document, travelling with the request as text rather than as a location to be read.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 16}
  - entity: Verdict
    attribute: reproducibility
    meaning: A verdict is reproducible from what was judged, which is why nothing is read from a location at judging time.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 17}
  business_processes:
  - process: Judge a document
    initiator: The author of record offering it
    outcome: A verdict, with every failed rule reported, over the document text it was handed
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Accept at a gate
    initiator: The gate reviewer
    outcome: The document may be consumed by the next phase
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_events, key: Seed Accepted}
  process_steps:
  - process: Judge a document
    step: '1'
    action: Read the document into its registers
    record_produced: The registers
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Judge a document
    step: '2'
    action: Apply every declared rule
    record_produced: The findings
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - process: Judge a document
    step: '3'
    action: Reach a verdict
    record_produced: The verdict
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_invariants, row: 1}
  belief_verification:
  - belief: No capability in the current composition decides seed admissibility.
    result: NOT_FOUND
    evidence: No capability produces an admissibility verdict; the only governed call in the domain is transformation::CC_JUDGE_DOCUMENT_V0, authored by this CR.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: A capability for declaring pure, deterministic transforms already exists.
    result: VERIFIED
    evidence: capability_transforms::CT_PURE_COMPARE_EQUAL_V0, capability_transforms::CT_PURE_EXTRACT_V0
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: A capability for declaring governed calls already exists, and forbids orchestration logic inside them.
    result: VERIFIED
    evidence: transformation::CC_JUDGE_DOCUMENT_V0 composes steps in a pipeline; chaining inside a call is forbidden and enforced at compile time.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: A workflow form already exists that composes governed calls as a fixed graph without iteration.
    result: VERIFIED
    evidence: transformation::WF_P0_SEED_ADMISSIBILITY_V0, transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: An actor form already exists for recording accountability.
    result: VERIFIED
    evidence: transformation::AC_SEED_AUTHOR_V0, transformation::AC_GATE_REVIEWER_V0, transformation::AC_REGISTER_AUTHOR_V0
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - belief: A form for declaring rules as data, separate from the mechanism that enforces them, already exists.
    result: NOT_FOUND
    evidence: No declaration form carries rules applied to a document; the rule set travels as declared workflow input instead.
    source_finding: {phase: p1, register: system_beliefs, row: 6}
  - belief: Vocabulary extension is restricted to specific declared categories.
    result: VERIFIED
    evidence: Vocabulary extension contributes only to the categories a reserving declaration marks extensible; no other category admits domain entries.
    source_finding: {phase: p1, register: system_beliefs, row: 7}
  - belief: The platform's existing content is largely infrastructure rather than business capability.
    result: VERIFIED
    evidence: The composition is dominated by constitutions, invariants and transport contracts; capability_side_effects::CS_MUTABLE_JSON_V0 and capability_transforms::CT_PURE_EXTRACT_V0 are among the few reusable mechanisms.
    source_finding: {phase: p1, register: system_beliefs, row: 8}
  pps_baseline_fqdns:
  - capability: Snapshot observation
    fqdn: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    what_it_does: Reads an assembled snapshot through the governed inspection surface.
    fit: EXACT
    cannot_do: Nothing — it is read-only by construction.
  - capability: Mutable JSON store
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    what_it_does: Key-addressable JSON state with last-write-wins.
    fit: MISMATCH
    cannot_do: The phases persist nothing; no store is needed.
  - capability: Judge a document
    fqdn: transformation::CC_JUDGE_DOCUMENT_V0
    what_it_does: Parses a document and evaluates a declared rule set against it.
    fit: PARTIAL
    cannot_do: It observes nothing, so it cannot ground a claim about the composition.
  - capability: Author of record
    fqdn: transformation::AC_REGISTER_AUTHOR_V0
    what_it_does: The human accountable for a register's content.
    fit: EXACT
    cannot_do: Nothing.
  gaps:
  - gap: No governed call grounds a claim against the composition.
    severity: CRITICAL
    impact: A phase that verifies beliefs cannot be built from what exists; judging alone is not grounding.
    evidence_status: NOT_FOUND
    source_finding: {phase: p2, register: belief_verification, key: A capability for declaring governed calls}
  - gap: No declaration form carries rules applied to a document.
    severity: MEDIUM
    impact: The rule set travels as declared workflow input, which is sound but is not a reusable form.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: system_beliefs, row: 6}
  architectural_observations:
  - observation: 'Judging and grounding are separable concerns: one reads a document, the other reads the composition.'
    evidence: transformation::CC_JUDGE_DOCUMENT_V0 performs the first and binds nothing.
    evidence_status: VERIFIED
    source_finding: {phase: p2, register: gaps, key: No governed call grounds a claim}
  - observation: 'Observation is a side effect, not a transform: the same query answers differently against different compositions.'
    evidence: capability_side_effects::CS_SNAPSHOT_QUERY_V0 is declared read-only with a bound subject.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: constraints, key: A verdict must be reproducible}
  - observation: A rule set held in the artifact that applies it can be compared against its declaration, so the two cannot drift unnoticed.
    evidence: The seed settles that the sealed copy is generated rather than typed and that the two are compared on every run; nothing in the composition holds a rule set apart from the workflow that applies it.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 15}
  - observation: A phase handed the document itself observes nothing at judging time beyond what it was given.
    evidence: transformation::CC_JUDGE_DOCUMENT_V0 parses a document and evaluates a declared rule set against it, and observes nothing; the seed settles that the document travels with the request.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 16}
  discovery_concerns:
  - concern: Grounding is only meaningful against the composition the document was written about; against an unrelated snapshot every citation looks like new design.
    evidence: The identity taxonomy cannot separate proposed-new from fabricated without the CR's declared new artifacts.
    severity: MEDIUM
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: constraints, key: A verdict must be reproducible}
  open_questions:
  - question: Should the pipeline's own domain be excluded from reuse search when a business change request runs?
    category: scope
    why_it_matters: A library change request must not be offered a pipeline mechanism as a reuse candidate.
    source_finding: {phase: p2, register: gaps, key: No governed call grounds a claim}
```

> P2 verifies the semantic model inherited from P1 against the compiled snapshot. It discovers
> facts; it does not decide. Every belief P1 recorded gets a result, and `NOT_FOUND` is a final
> answer — absence is a finding, not a reason to keep searching.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions for Stage 3
