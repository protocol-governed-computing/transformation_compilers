# Stage 1 — Change Request: Clarification & Fact Capture: [domain] / [subdomain]

## Machine

```yaml
document:
  phase: p1
  domain: <domain>
  subdomain: <subdomain>
  cr: <change>
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: null
    classification: null
    rationale: null
    source_finding: null
  business_vocabulary:
  - term: null
    definition: null
    source_finding: null
  requested_outcomes:
  - outcome: null
    source_finding: null
  known_facts:
  - fact: null
    certainty: null
    source_finding: null
  system_beliefs:
  - belief: null
    why_it_matters: null
    verification_goal: null
    source_finding: null
  assumptions:
  - assumption: null
    basis: null
    source_finding: null
  constraints:
  - constraint: null
    source: null
    source_finding: null
  business_invariants:
  - invariant: null
    source_finding: null
  lifecycle_states:
  - object: null
    state: null
    meaning: null
    source_finding: null
  business_events:
  - event: null
    when_it_occurs: null
    significance: null
    source_finding: null
  authority_boundaries:
  - business_object: null
    authoritative_owner: null
    source_finding: null
  out_of_scope:
  - item: null
    reason: null
    source_finding: null
  governance_scope:
  - scope_item: null
    relationship: null
    source_finding: null
  clarification_requests:
  - question: null
    why_needed: null
    blocking: null
    owner: null
    source_finding: null
  acceptance_criteria:
  - criterion: null
    source_finding: null
  identity_and_sameness:
  - business_object: null
    identified_by: null
    two_are_the_same_when: null
    source_finding: null
  lifecycle_transitions:
  - object: null
    from_state: null
    to_state: null
    triggered_by: null
    cascade: null
    source_finding: null
  operation_refusals:
  - operation: null
    refused_when: null
    business_reason: null
    source_finding: null
  authority_deferrals:
  - business_object: null
    deferred_to: null
    until: null
    source_finding: null
```

> **S1 interrogates; it does not author.** It captures *what is requested*, the *business
> semantics* (vocabulary, invariants, lifecycle states, business events, authority boundaries),
> *what the business definitively holds true*, *what the human believes the system already
> provides* (a hypothesis, not a fact), *what is assumed*, *what constrains*, and — most
> importantly — *what must be clarified before proceeding*. S1 is the primary human↔agent
> interaction stage: the agent does not guess, it asks. Implementation is deliberately out of view
> (S1 discovers, S2 models, S3 decides) — no design options, architectures, capability candidates,
> workflows, or artifact names appear here.

---

## Document Contract

**This artifact is a structured register document — not a narrative.** No Problem Statement /
Background / Business Need / Goals prose (those invite speculation). Capture facts and requests
as registers.

VALID OUTPUT:
- Populated registers (every required register)
- Business-language statements; existing artifacts cited by FQDN ONLY in a Source Finding cell

INVALID OUTPUT:
- Narrative prose replacing registers; design options; recommended architecture; capability /
  workflow / artifact candidates (all premature at S1)

A register with nothing to state is `[]`, declared empty. A register left `null` states nothing,
and a required register that states nothing is refused.

---

### The three-way split (the heart of S1)

S1's job is to keep three kinds of statement from contaminating one another — the separation
that prevents semantic drift downstream:

- **Business Truth** (§4 Known Facts) — what the business *authoritatively decides or requires*.
  The human owns these. They do not require snapshot inspection. Certainty is HIGH unless the
  human is genuinely unsure. Example: *"initial supply shall be 1,000,000 BachiCoin."*
- **System Belief** (§5 Existing-System Beliefs) — what the human *believes the system already
  provides*. The human is NOT authoritative here; the snapshot is. These are **discovery targets**
  the agent grounds in Stage 2, each with a **Verification Goal** — never asserted as fact at S1.
  Example: *"a consensus loop that proposes blocks may already exist."*
- **Clarification** (§14) — an unresolved question the agent must ask rather than guess, tagged
  with its **Owner** (who can answer: HUMAN, SNAPSHOT, or GOVERNANCE).

A statement about current system state is a **System Belief**, never a Known Fact. A business
decision is a **Known Fact**, never a System Belief. When you would guess either, raise a
**Clarification** instead.

### The business-semantics model (what S3 consumes to eliminate guesswork)

Six registers together form the human-authoritative semantic model so downstream stages discover
topology *in service of* meaning, not the reverse: **Business Vocabulary** (§2, the objects),
**Business Invariants** (§8, what must always hold), **Lifecycle States** (§9, the states an
object moves through), **Business Events** (§10, the moments that matter), and **Authority
Boundaries** (§11, who is authoritative for each object — the transition that drives S3's
REUSE-vs-AUTHOR_NEW calls). A NEW_SUBDOMAIN CR is incomplete without these.

---

### Business-Language Rule

Every CONTENT/DESCRIPTION cell is a business-language statement — NO protocol artifact names,
FQDNs, workflow/capability/intent/event names, or register bindings (those arrive at Stage 5+).
If a fact is supported by an existing artifact, cite that FQDN ONLY in the row's `source_finding`
(evidence) column — never in the statement itself.

VALID: "the running system already registers validators"  
INVALID: "WF_REGISTER_VALIDATOR_V0 exists"

---

### Stage 1 execution rules

- **Vocabulary first.** Every domain term the CR depends on (§2) is defined in business language
  before it is used — definitions are governed evidence, not implicit knowledge.
- **Truths ≠ Beliefs ≠ Requests.** Business Truths (§4) are human-authoritative decisions/
  requirements. System Beliefs (§5) are unverified hypotheses about what exists → discovery
  targets. Requested Outcomes (§3) are what the requester wants. Never merge them.
- **Known Facts are business truths only.** A claim about what the system currently does is a
  System Belief (§5), not a Known Fact — even if the human is confident.
- **Every System Belief carries a Verification Goal** — what Stage 2 must establish to confirm or
  refute it — so grounding is scoped to this CR, not the whole domain inventory.
- **State the business semantics explicitly** (§8–§11): invariants, lifecycle states, events, and
  authority boundaries are human-authoritative business truths, not implementation. S3 uses them
  to eliminate competing designs.
- **Every fact carries a certainty** (HIGH | MEDIUM | LOW). A belief you could not verify is a
  Clarification request — not a HIGH fact.
- **Every clarification carries an Owner.** Do not ask the human what only the snapshot can answer
  (Owner = SNAPSHOT) — route it to discovery instead.
- **Every row carries a `source_finding`** (human statement, seed answer ref, or grounded FQDN).
- **When you would guess, ask instead.** Anything not established becomes a
  `clarification_requests` row, not an assumption silently carried forward.

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

## 1. CR Type

*The classification of this change.*

Register `cr_type` in the Machine block.

---

## 2. Business Vocabulary

*Every domain term this CR depends on, defined in business language. Governed definitions become
first-class evidence — they prevent every downstream stage from re-inferring what the human
already means. Define the term, not its implementation.*

Register `business_vocabulary` in the Machine block.

---

## 3. Requested Outcomes

*What the requester wants to be true at close — business outcomes, not solutions.*

Register `requested_outcomes` in the Machine block.

---

## 4. Known Facts — Business Truths

*Only statements the human is authoritative about: business decisions and requirements. NOT
statements about what the system currently provides (those are §5 System Beliefs). Certainty
∈ HIGH | MEDIUM | LOW; source is the human (or an explicit human-cited authority).*

Register `known_facts` in the Machine block.

---

## 5. Existing-System Beliefs — Requiring Verification

*What the human BELIEVES the system already provides — hypotheses, not facts. The human is not
authoritative here; the snapshot is. Each row is a Stage-2 discovery target: `Why It Matters`
scopes the grounding to this CR, and `Verification Goal` states what Stage 2 must establish to
confirm or refute the belief (governing workflow(s), producers, emitted records, ownership).*

Register `system_beliefs` in the Machine block.

---

## 6. Assumptions

*Things taken as true WITHOUT full evidence — each with its basis. If an assumption is
load-bearing and unverified, prefer raising a clarification request instead.*

Register `assumptions` in the Machine block.

---

## 7. Constraints

*Non-negotiable rules the change must honor (monetary, governance, regulatory, immutability, …).*

Register `constraints` in the Machine block.

---

## 8. Business Invariants

*Properties that must ALWAYS hold true of the domain — business truths stated as invariants, not
implementation rules. S3 uses these to eliminate competing designs (a design that violates an
invariant is inadmissible). Each is a single, testable business statement.*

Register `business_invariants` in the Machine block.

---

## 9. Lifecycle States

*The states each core business object moves through, in business language. S3 uses these to scope
the state transitions a design must support (and the ones it must not). One row per object-state.*

Register `lifecycle_states` in the Machine block.

---

## 10. Business Events

*The business moments that matter — the events the domain must recognize. Stated in business
language (not artifact/event-code names). One row per event.*

Register `business_events` in the Machine block.

---

## 11. Authority Boundaries

*Who is authoritative for each core business object — and where authority transitions. S3 uses
these to drive REUSE-vs-AUTHOR_NEW: an authority handoff (e.g. proposed→committed) is exactly the
boundary a design must respect. State the owner in business terms, not artifact names.*

Register `authority_boundaries` in the Machine block.

---

## 12. Out of Scope

*Explicitly excluded from this CR — deferred to future CRs. State the release boundary
explicitly so downstream stages do not chase future-state architecture.*

Register `out_of_scope` in the Machine block.

---

## 13. Governance Scope

*Which governance concerns this CR touches, in business terms (not artifact bindings). Each scope
item declares its `Relationship` to this CR — what the CR does to/with that boundary.*

Register `governance_scope` in the Machine block.

---

## 14. Clarification Requests

*The keystone register: the agent does NOT guess — it asks. Every unresolved uncertainty that
could change the design is a row here. Blocking ∈ YES (cannot proceed until answered) | NO.
Owner ∈ HUMAN (only the requester can answer) | SNAPSHOT (discovery answers it in Stage 2) |
GOVERNANCE (a governance/topology decision). Do not ask the human a SNAPSHOT question.*

Register `clarification_requests` in the Machine block.

---

## 15. Acceptance Criteria

*How the requester will judge the CR satisfied at close — the S8 acceptance boundary. Each
criterion must be business-observable: testable by a business reviewer without inspecting runtime
internals.*

Register `acceptance_criteria` in the Machine block.

---

## 16. Identity and Sameness

*What identifies each business object, and when two of them are the same thing. S3 eliminates any
design that cannot enforce the sameness rule; S5 declares it as behaviour.*

Register `identity_and_sameness` in the Machine block.

---

## 17. Lifecycle Transitions

*What moves an object between states, and what does not follow from it. A transition whose Cascade is
declared as none forbids a later phase from inventing one.*

Register `lifecycle_transitions` in the Machine block.

---

## 18. Operation Refusals

*When an operation must refuse, and why in business terms. S5 declares each refusal; an omitted
refusal becomes a path that succeeds when the business requires it to fail.*

Register `operation_refusals` in the Machine block.

---

## 19. Authority Deferrals

*Authority this CR does not take, and where it is expected to land. S6 places only what §11 owns
now; a deferral here keeps it from placing what does not yet exist.*

Register `authority_deferrals` in the Machine block.

---

## gov_projection — Governed Handoff to Stage 2

*Governed, lossless, identity-preserving (Stage 0 / field manual §4.7). Emit keys match the
register ids above exactly. Business Vocabulary, Truths, Invariants, Lifecycle States, Events and
Authority Boundaries cross as authoritative business semantics; System Beliefs cross as Stage-2
discovery targets (verified, never trusted). Blocking clarification requests are resolved by the
human at the S1 gate before Stage 2 proceeds.*

| Direction | Registers |
|-----------|-----------|
| **Consumes** ← p0 | human elicitation answers (the seed) |
| **Emits** | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
