# Change Request — transformation / phases

## Machine

```yaml
document:
  phase: p1
  domain: transformation
  subdomain: phases
  cr: new_subdomain
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: phases
    classification: INVENTED_SUBDOMAIN
    rationale: The pipeline that decides which changes are admissible is a distinct concern from the capabilities it admits, and needs its own governance boundary. It extends nothing that exists.
    source_finding: {phase: p0, register: cr_type}
  business_vocabulary:
  - term: Phase
    definition: One governed step of the change pipeline, with declared inputs, outputs and rules.
    source_finding: null
  - term: Seed
    definition: The business problem statement reorganized into fixed registers, and the only input later phases accept.
    source_finding: I remembered it
  - term: Seed Phase
    definition: 'The first phase: it turns a person''s problem statement into a seed.'
    source_finding: {phase: p0, register: business_vocabulary}
  - term: Rule Set
    definition: The declared set of conditions that decide whether a seed is admissible. Governance, not implementation.
    source_finding: {phase: p0, register: business_vocabulary}
  - term: Check Mechanism
    definition: A means of performing one kind of condition test. Implementation; carries no judgement about what should be tested.
    source_finding: {phase: p0, register: business_vocabulary}
  - term: Verdict
    definition: 'The outcome of applying the rule set to a seed: admissible or inadmissible. There is no partial pass.'
    source_finding: {phase: p0, register: business_vocabulary}
  - term: Finding
    definition: One recorded failure of one rule, naming the rule, where it failed, and why that matters.
    source_finding: {phase: p0, register: business_vocabulary}
  - term: Gate
    definition: A point where a person accepts responsibility before the pipeline continues.
    source_finding: {phase: p0, register: business_vocabulary}
  - term: Author of Record
    definition: The person accountable for a seed's content.
    source_finding: {phase: p0, register: business_vocabulary}
  - term: Business Truth
    definition: Something the business authoritatively decides or requires.
    source_finding: {phase: p0, register: business_vocabulary}
  - term: System Belief
    definition: Something believed about what already exists, which must be verified rather than assumed.
    source_finding: {phase: p0, register: business_vocabulary}
  - term: Clarification
    definition: An open question that must be asked and never guessed.
    source_finding: {phase: p0, register: business_vocabulary}
  requested_outcomes:
  - outcome: Establish the seed phase as a governed capability of the platform, with its rules readable from the composition rather than from a build tool.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: Produce a verdict for any offered seed, reporting every rule the seed failed rather than stopping at the first failure.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: 'Record accountability: a person is the author of record for a seed, and a person confirms at the gate that it says what they meant.'
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  known_facts:
  - fact: The change pipeline must be governed the same way the capabilities it admits are governed.
    certainty: MAYBE
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: The seed phase reorganizes a problem statement; it never decides business content.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: A seed is either admissible or inadmissible; there is no partial pass and no warning tier.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: Every rule is applied to every seed; evaluation does not stop at the first failure.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: The rule set is governance and must be readable from the composition and versioned as declared behaviour.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: A check mechanism is implementation and may live in code, provided it carries no judgement about what should be tested.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: A person is the author of record for a seed, and a person confirms it at the gate.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: The seed phase may not add business content the problem statement does not contain.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: The seed phase may not resolve an open question by guessing.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: The seed phase may not assign any design.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: The seed phase may not promote a System Belief into a Business Truth.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: Changing the rule set requires the same governed change process as any other declared behaviour.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: This change establishes the seed phase and its rule set only.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: The rule set is carried sealed inside the phase's own compiled artifact, alongside the workflow that applies it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: The sealed rule set is generated from the declaration rather than typed, and the two are compared on every run.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: A phase receives the seed as text, the whole document travelling with the request.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: A verdict must be reproducible from what was judged, so a phase is never handed a location to read.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  system_beliefs:
  - belief: No capability in the current composition decides seed admissibility.
    why_it_matters: This CR exists to fill that gap; if such a capability exists, the CR scope changes.
    verification_goal: Confirm no existing capability produces a seed verdict.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: A capability for declaring pure, deterministic transforms already exists.
    why_it_matters: The check mechanisms are pure transforms and should reuse it rather than author a new form.
    verification_goal: Identify the governing declaration for pure capability transforms and its purity obligations.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: A capability for declaring governed calls already exists, and forbids orchestration logic inside them.
    why_it_matters: Determines whether a rule can be a governed call or must be data the phase evaluates.
    verification_goal: Identify the governing declaration for capability contracts and what it forbids.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: A workflow form already exists that composes governed calls as a fixed graph without iteration.
    why_it_matters: Determines how the phase applies many rules to many registers.
    verification_goal: Identify the workflow declaration and confirm whether iteration is available to it.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: An actor form already exists for recording accountability.
    why_it_matters: The author of record and the gate reviewer are actors.
    verification_goal: Identify the actor declaration and how a workflow binds one.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  - belief: A form for declaring rules as data, separate from the mechanism that enforces them, already exists.
    why_it_matters: If so, the rule set should reuse it rather than invent a carrier.
    verification_goal: Identify how existing rules are declared apart from their enforcement, and whether that form fits a rule set applied to a document.
    source_finding: {phase: p0, register: system_beliefs, row: 6}
  - belief: Vocabulary extension is restricted to specific declared categories.
    why_it_matters: Determines whether the controlled vocabularies of the seed may be declared as vocabulary.
    verification_goal: Identify what may be extended as vocabulary and what may not.
    source_finding: {phase: p0, register: system_beliefs, row: 7}
  - belief: The platform's existing content is largely infrastructure rather than business capability.
    why_it_matters: Establishes what this subdomain can legitimately reuse.
    verification_goal: Identify which existing capabilities are reuse candidates for a pipeline subdomain.
    source_finding: {phase: p0, register: system_beliefs, row: 8}
  assumptions:
  - assumption: The seed template's section structure is stable and will not change while this CR is in flight.
    basis: It is fixed by the reference elicitation already in use.
    source_finding: {phase: p0, register: assumptions}
  - assumption: A person can supply every register by hand, so the pipeline never depends on an automated drafter.
    basis: Stated release constraint.
    source_finding: {phase: p0, register: assumptions}
  constraints:
  - constraint: What is checked, and why, must be readable from the composition; only how a check runs may live in code.
    source: Business policy
    source_finding: {phase: p0, register: constraints}
  - constraint: The pipeline is reachable only from a local command line, not over any network boundary.
    source: Business policy
    source_finding: {phase: p0, register: constraints}
  - constraint: Dossiers are evidence about a composition and must never become part of one.
    source: Business policy
    source_finding: {phase: p0, register: constraints}
  - constraint: 'A verdict must be reproducible: the same seed and the same rule set always give the same verdict.'
    source: Business policy
    source_finding: {phase: p0, register: constraints}
  business_invariants:
  - invariant: A seed has exactly one verdict, enforced by CT_PURE_EVALUATE_RULES_V0.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: Every rule in the rule set is applied to every seed offered to the phase.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: An inadmissible seed carries at least one finding, and an admissible seed carries none.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: Every finding names the rule that produced it.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: Every seed has exactly one author of record.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: The same seed and rule set always produce the same verdict.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: A seed that has not passed the gate is never consumed by a later phase.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  lifecycle_states:
  - object: Seed
    state: Drafted
    meaning: Reorganized from a problem statement; not yet judged.
    source_finding: {phase: p0, register: lifecycle_states}
  - object: Seed
    state: Admissible
    meaning: The rule set found no findings.
    source_finding: {phase: p0, register: lifecycle_states}
  - object: Seed
    state: Inadmissible
    meaning: At least one finding was recorded; the seed cannot proceed.
    source_finding: {phase: p0, register: lifecycle_states}
  - object: Seed
    state: Accepted
    meaning: A person confirmed at the gate that it says what they meant.
    source_finding: {phase: p0, register: lifecycle_states}
  - object: Rule Set
    state: Active
    meaning: The declared rules currently deciding admissibility.
    source_finding: {phase: p0, register: lifecycle_states}
  - object: Rule Set
    state: Superseded
    meaning: Replaced by a later version through a governed change.
    source_finding: {phase: p0, register: lifecycle_states}
  business_events:
  - event: Seed Offered
    when_it_occurs: When a seed is submitted to the phase for judgement.
    significance: The phase has something to decide about.
    source_finding: {phase: p0, register: business_events}
  - event: Verdict Reached
    when_it_occurs: When the rule set has been applied in full.
    significance: The seed's admissibility is established and recorded.
    source_finding: {phase: p0, register: business_events}
  - event: Seed Accepted
    when_it_occurs: When a person confirms the seed at the gate.
    significance: Accountability is recorded and later phases may consume it.
    source_finding: {phase: p0, register: business_events}
  - event: Seed Rejected
    when_it_occurs: When a verdict is inadmissible, or a person declines at the gate.
    significance: The change does not proceed, and the cause is recorded.
    source_finding: {phase: p0, register: business_events}
  authority_boundaries:
  - business_object: Problem Statement
    authoritative_owner: The person who wrote it
    source_finding: {phase: p0, register: authority_boundaries}
  - business_object: Seed content
    authoritative_owner: The author of record
    source_finding: {phase: p0, register: authority_boundaries}
  - business_object: Rule Set
    authoritative_owner: Phases
    source_finding: {phase: p0, register: authority_boundaries}
  - business_object: Verdict
    authoritative_owner: Phases
    source_finding: {phase: p0, register: authority_boundaries}
  - business_object: Finding
    authoritative_owner: Phases
    source_finding: {phase: p0, register: authority_boundaries}
  - business_object: Gate acceptance
    authoritative_owner: The gate reviewer
    source_finding: {phase: p0, register: authority_boundaries}
  out_of_scope:
  - item: The remaining phases of the pipeline.
    reason: This change establishes the seed phase only; the rest arrive as later change requests.
    source_finding: {phase: p0, register: out_of_scope}
  - item: Automated drafting of a seed.
    reason: The pipeline must not depend on it; it may be added later behind the same rules.
    source_finding: {phase: p0, register: out_of_scope}
  - item: Reachability over any network boundary.
    reason: The pipeline is build-time and local only.
    source_finding: {phase: p0, register: out_of_scope}
  - item: Rules that require reading an existing composition.
    reason: The seed phase judges a document alone; composition-aware rules belong to later phases.
    source_finding: {phase: p0, register: out_of_scope}
  - item: Deciding which parts of a composition may be reused by a later change.
    reason: A property of the analysis phase, not the seed phase.
    source_finding: {phase: p0, register: out_of_scope}
  governance_scope:
  - scope_item: phases
    relationship: INVENTED
    source_finding: {phase: p0, register: governance_scope}
  - scope_item: capability_transforms
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope}
  - scope_item: capability_contracts
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope}
  - scope_item: workflow
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope}
  - scope_item: intent
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope}
  - scope_item: runtime_binding
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope}
  - scope_item: governance
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope}
  clarification_requests: []
  acceptance_criteria:
  - criterion: A person can offer a seed to the phase and receive a verdict of admissible or inadmissible.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: An inadmissible seed reports every rule it failed, not only the first.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: The rules deciding admissibility can be read from the composition without reading any code.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Offering the same seed twice produces the same verdict.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: A seed records exactly one author of record, and a gate acceptance records the person who gave it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: A seed that fails the gate is not consumed by any later phase.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  identity_and_sameness: null
  lifecycle_transitions: null
  operation_refusals: null
  authority_deferrals: null
```

The P1 register. Every row restates content from the accepted seed and cites the finding it came
from; P1 classifies and traces, it does not add. Business language only — nothing here gets a code.

---

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---
