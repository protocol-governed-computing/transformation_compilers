# Change Seed — transformation / phases

## Machine

```yaml
document:
  phase: p0
  domain: transformation
  subdomain: phases
  cr: new_subdomain
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Phases subdomain governs how a proposed change to a composition is carried from a person's
    problem statement to a decision about whether it may proceed. It owns the pipeline itself: what each
    phase consumes and produces, which rules decide admissibility, and who is accountable at each gate.
    Other parts of the platform govern what a composition contains; this subdomain governs how a
    composition is allowed to change.
  cr_type:
  - subdomain: design
    classification: NEW_SUBDOMAIN
    rationale: The pipeline that decides which changes are admissible is a distinct concern from the capabilities it admits, and needs its own governance boundary. It extends nothing that exists.
  business_vocabulary:
  - term: Phase
    definition: One governed step of the change pipeline, with declared inputs, outputs and rules.
  - term: Seed
    definition: The business problem statement reorganized into fixed registers, and the only input later phases accept.
  - term: Seed Phase
    definition: 'The first phase: it turns a person''s problem statement into a seed.'
  - term: Rule Set
    definition: The declared set of conditions that decide whether a seed is admissible. Governance, not implementation.
  - term: Check Mechanism
    definition: A means of performing one kind of condition test. Implementation; carries no judgement about what should be tested.
  - term: Verdict
    definition: 'The outcome of applying the rule set to a seed: admissible or inadmissible. There is no partial pass.'
  - term: Finding
    definition: One recorded failure of one rule, naming the rule, where it failed, and why that matters.
  - term: Gate
    definition: A point where a person accepts responsibility before the pipeline continues.
  - term: Author of Record
    definition: The person accountable for a seed's content.
  - term: Business Truth
    definition: Something the business authoritatively decides or requires.
  - term: System Belief
    definition: Something believed about what already exists, which must be verified rather than assumed.
  - term: Clarification
    definition: An open question that must be asked and never guessed.
  requested_outcomes:
  - outcome: Establish the seed phase as a governed capability of the platform, with its rules readable from the composition rather than from a build tool.
  - outcome: Produce a verdict for any offered seed, reporting every rule the seed failed rather than stopping at the first failure.
  - outcome: 'Record accountability: a person is the author of record for a seed, and a person confirms at the gate that it says what they meant.'
  known_facts:
  - fact: The change pipeline must be governed the same way the capabilities it admits are governed.
    certainty: HIGH
  - fact: The seed phase reorganizes a problem statement; it never decides business content.
    certainty: HIGH
  - fact: A seed is either admissible or inadmissible; there is no partial pass and no warning tier.
    certainty: HIGH
  - fact: Every rule is applied to every seed; evaluation does not stop at the first failure.
    certainty: HIGH
  - fact: The rule set is governance and must be readable from the composition and versioned as declared behaviour.
    certainty: HIGH
  - fact: A check mechanism is implementation and may live in code, provided it carries no judgement about what should be tested.
    certainty: HIGH
  - fact: A person is the author of record for a seed, and a person confirms it at the gate.
    certainty: HIGH
  - fact: The seed phase may not add business content the problem statement does not contain.
    certainty: HIGH
  - fact: The seed phase may not resolve an open question by guessing.
    certainty: HIGH
  - fact: The seed phase may not assign any design.
    certainty: HIGH
  - fact: The seed phase may not promote a System Belief into a Business Truth.
    certainty: HIGH
  - fact: Changing the rule set requires the same governed change process as any other declared behaviour.
    certainty: HIGH
  - fact: This change establishes the seed phase and its rule set only.
    certainty: HIGH
  - fact: The rule set is carried sealed inside the phase's own compiled artifact, alongside the workflow that applies it.
    certainty: HIGH
  - fact: The sealed rule set is generated from the declaration rather than typed, and the two are compared on every run.
    certainty: HIGH
  - fact: A phase receives the seed as text, the whole document travelling with the request.
    certainty: HIGH
  - fact: A verdict must be reproducible from what was judged, so a phase is never handed a location to read.
    certainty: HIGH
  system_beliefs:
  - belief: No capability in the current composition decides seed admissibility.
    why_it_matters: This CR exists to fill that gap; if such a capability exists, the CR scope changes.
    verification_goal: Confirm no existing capability produces a seed verdict.
  - belief: A capability for declaring pure, deterministic transforms already exists.
    why_it_matters: The check mechanisms are pure transforms and should reuse it rather than author a new form.
    verification_goal: Identify the governing declaration for pure capability transforms and its purity obligations.
  - belief: A capability for declaring governed calls already exists, and forbids orchestration logic inside them.
    why_it_matters: Determines whether a rule can be a governed call or must be data the phase evaluates.
    verification_goal: Identify the governing declaration for capability contracts and what it forbids.
  - belief: A workflow form already exists that composes governed calls as a fixed graph without iteration.
    why_it_matters: Determines how the phase applies many rules to many registers.
    verification_goal: Identify the workflow declaration and confirm whether iteration is available to it.
  - belief: An actor form already exists for recording accountability.
    why_it_matters: The author of record and the gate reviewer are actors.
    verification_goal: Identify the actor declaration and how a workflow binds one.
  - belief: A form for declaring rules as data, separate from the mechanism that enforces them, already exists.
    why_it_matters: If so, the rule set should reuse it rather than invent a carrier.
    verification_goal: Identify how existing rules are declared apart from their enforcement, and whether that form fits a rule set applied to a document.
  - belief: Vocabulary extension is restricted to specific declared categories.
    why_it_matters: Determines whether the controlled vocabularies of the seed may be declared as vocabulary.
    verification_goal: Identify what may be extended as vocabulary and what may not.
  - belief: The platform's existing content is largely infrastructure rather than business capability.
    why_it_matters: Establishes what this subdomain can legitimately reuse.
    verification_goal: Identify which existing capabilities are reuse candidates for a pipeline subdomain.
  assumptions:
  - assumption: The seed template's register structure is stable and will not change while this CR is in flight.
    basis: It is fixed by the reference elicitation already in use.
  - assumption: A person can supply every register by hand, so the pipeline never depends on an automated drafter.
    basis: Stated release constraint.
  constraints:
  - constraint: What is checked, and why, must be readable from the composition; only how a check runs may live in code.
    source: Business policy
  - constraint: The pipeline is reachable only from a local command line, not over any network boundary.
    source: Business policy
  - constraint: Dossiers are evidence about a composition and must never become part of one.
    source: Business policy
  - constraint: 'A verdict must be reproducible: the same seed and the same rule set always give the same verdict.'
    source: Business policy
  business_invariants:
  - invariant: A seed has exactly one verdict.
  - invariant: Every rule in the rule set is applied to every seed offered to the phase.
  - invariant: An inadmissible seed carries at least one finding, and an admissible seed carries none.
  - invariant: Every finding names the rule that produced it.
  - invariant: Every seed has exactly one author of record.
  - invariant: The same seed and rule set always produce the same verdict.
  - invariant: A seed that has not passed the gate is never consumed by a later phase.
  lifecycle_states:
  - object: Seed
    state: Drafted
    meaning: Reorganized from a problem statement; not yet judged.
  - object: Seed
    state: Admissible
    meaning: The rule set found no findings.
  - object: Seed
    state: Inadmissible
    meaning: At least one finding was recorded; the seed cannot proceed.
  - object: Seed
    state: Accepted
    meaning: A person confirmed at the gate that it says what they meant.
  - object: Rule Set
    state: Active
    meaning: The declared rules currently deciding admissibility.
  - object: Rule Set
    state: Superseded
    meaning: Replaced by a later version through a governed change.
  business_events:
  - event: Seed Offered
    when_it_occurs: When a seed is submitted to the phase for judgement.
    significance: The phase has something to decide about.
  - event: Verdict Reached
    when_it_occurs: When the rule set has been applied in full.
    significance: The seed's admissibility is established and recorded.
  - event: Seed Accepted
    when_it_occurs: When a person confirms the seed at the gate.
    significance: Accountability is recorded and later phases may consume it.
  - event: Seed Rejected
    when_it_occurs: When a verdict is inadmissible, or a person declines at the gate.
    significance: The change does not proceed, and the cause is recorded.
  authority_boundaries:
  - business_object: Problem Statement
    authoritative_owner: The person who wrote it
  - business_object: Seed content
    authoritative_owner: The author of record
  - business_object: Rule Set
    authoritative_owner: Phases
  - business_object: Verdict
    authoritative_owner: Phases
  - business_object: Finding
    authoritative_owner: Phases
  - business_object: Gate acceptance
    authoritative_owner: The gate reviewer
  out_of_scope:
  - item: The remaining phases of the pipeline.
    reason: This change establishes the seed phase only; the rest arrive as later change requests.
  - item: Automated drafting of a seed.
    reason: The pipeline must not depend on it; it may be added later behind the same rules.
  - item: Reachability over any network boundary.
    reason: The pipeline is build-time and local only.
  - item: Rules that require reading an existing composition.
    reason: The seed phase judges a document alone; composition-aware rules belong to later phases.
  - item: Deciding which parts of a composition may be reused by a later change.
    reason: A property of the analysis phase, not the seed phase.
  governance_scope:
  - scope_item: phases
    relationship: CREATED
  - scope_item: capability_transforms
    relationship: ADJACENT
  - scope_item: capability_contracts
    relationship: ADJACENT
  - scope_item: workflow
    relationship: ADJACENT
  - scope_item: intent
    relationship: ADJACENT
  - scope_item: runtime_binding
    relationship: ADJACENT
  - scope_item: governance
    relationship: ADJACENT
  clarification_requests: []
  acceptance_criteria:
  - criterion: A person can offer a seed to the phase and receive a verdict of admissible or inadmissible.
  - criterion: An inadmissible seed reports every rule it failed, not only the first.
  - criterion: The rules deciding admissibility can be read from the composition without reading any code.
  - criterion: Offering the same seed twice produces the same verdict.
  - criterion: A seed records exactly one author of record, and a gate acceptance records the person who gave it.
  - criterion: A seed that fails the gate is not consumed by any later phase.
  identity_and_sameness: null
  lifecycle_transitions: null
  operation_refusals: null
  authority_deferrals: null
```

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

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

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals
