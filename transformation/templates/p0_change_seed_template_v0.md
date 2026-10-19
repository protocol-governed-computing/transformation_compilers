# P0 — Change Seed

## Machine

```yaml
document:
  phase: p0
  domain: <domain>
  subdomain: <subdomain>
  cr: <change>
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
  # approval: {gate: ..., rule_set: ..., state: APPROVED} — when the gate closes
registers:
  subdomain_purpose: null
  cr_type:
  - subdomain: null
    classification: null
    rationale: null
  business_vocabulary:
  - term: null
    definition: null
  requested_outcomes:
  - outcome: null
  known_facts:
  - fact: null
    certainty: null
  system_beliefs:
  - belief: null
    why_it_matters: null
    verification_goal: null
  assumptions:
  - assumption: null
    basis: null
  constraints:
  - constraint: null
    source: null
  business_invariants:
  - invariant: null
  lifecycle_states:
  - object: null
    state: null
    meaning: null
  business_events:
  - event: null
    when_it_occurs: null
    significance: null
  authority_boundaries:
  - business_object: null
    authoritative_owner: null
  out_of_scope:
  - item: null
    reason: null
  governance_scope:
  - scope_item: null
    relationship: null
  clarification_requests:
  - question: null
    why_needed: null
    blocking: null
    owner: null
  acceptance_criteria:
  - criterion: null
  identity_and_sameness:
  - business_object: null
    identified_by: null
    two_are_the_same_when: null
  lifecycle_transitions:
  - object: null
    from_state: null
    to_state: null
    triggered_by: null
    cascade: null
  operation_refusals:
  - operation: null
    refused_when: null
    business_reason: null
  authority_deferrals:
  - business_object: null
    deferred_to: null
    until: null
```

## Document Contract

**Before authoring a seed, ask whether this is a new change at all.** If its subject touches an
artifact a dossier still in flight declares, it is not a new change request — it belongs to that
dossier, whose problem statement is revisited and re-authored from P0. A change request is expensive
and re-authoring one is cheap, and two in-flight dossiers declaring one artifact are two designs of
record where each silently reverts the other. Only a subject touching nothing another in-flight
dossier declares gets a seed of its own.

**Input:** `0_business_problem_statement.md` — free-form business prose, written by a person.
**Output:** this document — the same content, reorganized into governed registers.

P0 **reorganizes; it does not decide.** Everything a register asserts must be traceable to a
sentence in the problem statement. Everything the problem statement leaves unsaid becomes a
Clarification Request — never a filled-in guess.

INVALID OUTPUT:
- business content the problem statement does not contain
- any artifact code, FQDN or capability name (no design at this rung)
- a Clarification answered by the author rather than asked
- a System Belief promoted into a Known Fact

A register with nothing to state is `[]`, declared empty. A register left `null` states nothing,
and a required register that states nothing is refused.

**Gate 0** — a person confirms the seed says what they meant, before any governed phase consumes it.

### A platform seed states a platform problem

A change to the platform is stated in the platform's own terms — an act, a subdomain, a record, a
capability — and never in the terms of a business domain that happens to be in the composition. A
platform is a **composition**: the domains present today are selected, another profile selects
others, and a problem statement that only reads as a problem when one particular domain exists has
made itself true of one composition rather than of the platform.

Name the instance anyway. An instance is what shows the problem occurred rather than being
anticipated, and it is the difference between a requirement and a worry. **Mark it as an instance**:
state the problem generically first, then give the case, and say plainly that the domain it comes
from is one the platform does not require and a later composition may not contain.

This applies to `p0_business_problem_statement.md` and to the seed. It does *not* apply to the
grounding phases — P2 verifies beliefs against a real composition and must cite exact identities,
because a generic citation grounds nothing.

---

### The three-way split (the heart of P0)

P0 exists to keep three kinds of statement from contaminating one another, because every later
phase treats them differently:

| Register | Nature | Authoritative | What P2 does with it |
|----------|--------|---------------|----------------------|
| §4 Known Facts | business truths | the human | takes as given |
| §5 System Beliefs | suspicions about what exists | nobody yet | verifies against the snapshot |
| §14 Clarification Requests | open questions | unanswered | must ask, never guess |

A belief recorded as a fact is never verified. A question recorded as a fact is answered by
invention. Both failures are silent, and both originate here.

---

### Elicitation — questions for the human, and what each answer is used for

| Question | Declared intent |
|----------|-----------------|
| What does this subdomain govern, and why does it exist? | §0 Subdomain Purpose — the one narrative no compiled artifact can derive; consumed downstream, never rediscovered |
| Is this new, an extension, a modification, or a retirement? | §1 CR Type — P1 records the classification and its rationale |
| Which business terms carry governed meaning here? | §2 Business Vocabulary — every later phase reads meaning from this register |
| What must be true at close for this change to have succeeded? | §3 Requested Outcomes — P4 consolidates, P5 turns them into declared behaviour |
| What does the business authoritatively decide or require? | §4 Known Facts — taken as given; never re-litigated |
| What do you believe already exists? | §5 System Beliefs — P2 verification targets, each needing a Verification Goal |
| What are you assuming without having established it? | §6 Assumptions — surfaced so a later phase can overturn them explicitly |
| What is non-negotiable? | §7 Constraints — bound the design space at P5 and P6 |
| What must always be true, regardless of state? | §8 Business Invariants — P5 turns these into declared invariants |
| What states does each core object move through? | §9 Lifecycle States — P2 confirms them against the model |
| Which moments must the domain recognise? | §10 Business Events — P5 derives events from these |
| Who is authoritative for each business object? | §11 Authority Boundaries — P6 turns ownership into placement |
| What is deliberately *not* in this change? | §12 Out of Scope — what makes later CRs governed evolution rather than retrofitted scope |
| Which subdomains does this touch, and how? | §13 Governance Scope — P6 reads placement from this |
| What could you not answer? | §14 Clarification Requests — asked, never guessed |
| How will you know it worked, without looking inside? | §15 Acceptance Criteria — business-observable, testable without runtime internals |
| What identifies each object, and when are two of them the same thing? | §16 Identity and Sameness — P2 grounds identity in the model, P5 turns sameness into a declared rule |
| What moves an object between states, and what does *not* follow from it? | §17 Lifecycle Transitions — P5 declares the transitions; a cascade nobody asked for is invented behaviour |
| When must an operation refuse? | §18 Operation Refusals — P5 turns a refusal into declared behaviour rather than an unhandled path |
| Which authority is deliberately left to a later change? | §19 Authority Deferrals — P6 must not place what this change does not own |

An unanswered question is an open gap, never licence to assume.

---

## 0. Subdomain Purpose

*The one irreducible business narrative no compiled artifact can derive: what this subdomain
governs and why it exists. Stated once here, at the source; consumed downstream, never
rediscovered.*

Register `subdomain_purpose` in the Machine block.

## 1. CR Type

Register `cr_type` in the Machine block.

## 2. Business Vocabulary

Register `business_vocabulary` in the Machine block.

## 3. Requested Outcomes

Register `requested_outcomes` in the Machine block.

## 4. Known Facts — Business Truths

Register `known_facts` in the Machine block.

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

Register `system_beliefs` in the Machine block.

## 6. Assumptions

Register `assumptions` in the Machine block.

## 7. Constraints

Register `constraints` in the Machine block.

## 8. Business Invariants

Register `business_invariants` in the Machine block.

## 9. Lifecycle States

Register `lifecycle_states` in the Machine block.

## 10. Business Events

Register `business_events` in the Machine block.

## 11. Authority Boundaries

Register `authority_boundaries` in the Machine block.

## 12. Out of Scope

Register `out_of_scope` in the Machine block.

## 13. Governance Scope

Register `governance_scope` in the Machine block.

## 14. Clarification Requests

Register `clarification_requests` in the Machine block.

## 15. Acceptance Criteria

Register `acceptance_criteria` in the Machine block.

## 16. Identity and Sameness

*What identifies each business object, and the business rule that decides when two of them are the
same thing. A domain that cannot say when two records describe one object cannot prevent a duplicate,
and "a single authoritative record" is unverifiable.*

Register `identity_and_sameness` in the Machine block.

## 17. Lifecycle Transitions

*What moves an object from one state to another, and what does **not** follow from it. The Cascade
column is the register's reason for existing: a transition that triggers nothing must say so, because
otherwise a later phase is free to invent the cascade the business never asked for.*

Register `lifecycle_transitions` in the Machine block.

## 18. Operation Refusals

*When an operation must refuse, and the business reason. A refusal the business requires and the seed
omits becomes, downstream, an unhandled path that silently succeeds.*

Register `operation_refusals` in the Machine block.

## 19. Authority Deferrals

*Authority this change deliberately does not take, and where it is expected to land. Distinct from
§11: an owner named there is owned **now**, and a deferral recorded as an owner is placement P6 will
perform against a function that does not exist.*

Register `authority_deferrals` in the Machine block.

---

## gov_projection — Governed Handoff to Stage 1

*Governed, lossless, identity-preserving. Every register is forwarded — Stage 1 never re-discovers
what the seed established. Emit keys match the register ids above exactly.*

| Direction | Registers |
|-----------|-----------|
| **Consumes** ← the human | business problem statement |
| **Emits** | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
