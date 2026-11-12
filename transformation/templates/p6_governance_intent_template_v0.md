# Governance Intent: [domain] / [subdomain]

## Machine

```yaml
document:
  phase: p6
  domain: <domain>
  subdomain: <subdomain>
  cr: <change>
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: null
    owner_subdomain: null
    disposition: null
    existing_artifact: null
    source_finding: null
  storage_governance:
  - storage_need: null
    purpose: null
    subdomain: null
    source_finding: null
  cross_subdomain_deps:
  - dependency: null
    direction: null
    existing_artifact: null
    status: null
    source_finding: null
  pps_artifacts_requiring_action:
  - fqdn: null
    current_status: null
    action: null
    source_finding: null
  boundary_rules:
  - rule_name: null
    statement: null
    source_finding: null
  governance_outcome:
  - capability: null
    owner_subdomain: null
    source_finding: null
```

## Document Contract

**This artifact is a structured register document — not a narrative.** S6 declares the WHERE:
subdomain ownership, storage governance, cross-subdomain dependencies, and existing artifacts
needing action. The worker emits register ROWS; a deterministic renderer owns the document.

VALID OUTPUT:
- Populated registers (every required register below)
- Business-language capability / dependency / storage descriptions
- Existing artifacts cited by exact FQDN in evidence / artifact columns

INVALID OUTPUT:
- Narrative summaries replacing registers
- A provisional or invented artifact code in a content column (see the discipline below)

A register with nothing to state is `[]`, declared empty. A register left `null` states nothing,
and a required register that states nothing is refused.

---

### Governance discipline

- **NO provisional artifact codes in this stage** (per the Purity line above). A NEW capability is
  named in **business language** (e.g. "create the genesis block at bootstrap"); ownership names the
  owning **subdomain** namespace, never an invented artifact code like `CC_CREATE_GENESIS_BLOCK_V0`.
  Existing artifacts are still cited by their real FQDN (in `evidence` / `existing_artifact` / `fqdn`
  columns). Provisional codes were assigned at Stage 5; binding FQDNs are assigned at Stage 7.
- **Cross-subdomain writes are forbidden — no exceptions.** A store is written only by CCs of its
  owning subdomain. If this CR's process requires writing a peer's store, the writing CC is owned by
  that peer (a dependency gap declared in `cross_subdomain_deps`, Status = GAP).
- Cross-subdomain capability calls and data reads ARE permitted — declare each with explicit
  direction in `cross_subdomain_deps`.

---

## Stage Inputs — Questions for the Human

| # | Question for the Human | How the Agent Uses the Answer (Intent) |
|---|------------------------|----------------------------------------|
| 1 | Does this capability stand as its own subdomain, or extend an existing one — and why? | Sets Domain Placement (below). Subdomain existence is a governance topology declaration, never derived from the snapshot. |
| 2 | Under what authority class do these operations execute (existing ENDUSER/SYSTEM, or a new actor type)? | A new actor type expands CR scope; reuse must be stated explicitly. |
| 3 | For each capability that touches a peer subdomain: who should OWN it? | Drives `ownership` + `cross_subdomain_deps`. A capability that writes a peer's store MUST be owned by that peer. |
| 4 | Which boundary rules are non-negotiable for this subdomain? | Becomes `boundary_rules`, the invariants conformance tests will enforce. |

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `[domain]` |
| Primary subdomain | `[subdomain]` — [NEW — declared by this CR / EXISTING] |
| Authority class | [reuse existing ENDUSER/SYSTEM / new actor type: name] |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

*State the placement rationale in one or two sentences: if declaring a new subdomain, why it stands alone rather than nesting under an existing one.*

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

## 1. Subdomain Boundary — Ownership

*Every capability this CR needs, and who OWNS it. Disposition ∈ OWNED (this subdomain authors it) | SATISFIED (an existing artifact covers it — cite the FQDN in Evidence) | DEFERRED (future CR). `capability` is business language; `owner_subdomain` is a subdomain namespace, never an artifact code.*

Register `ownership` in the Machine block.

---

## 2. Storage Governance Requirements

*What persistent storage the subdomain requires, as a governance requirement — NOT store names or paths (those are Stage 7). Business language only.*

Register `storage_governance` in the Machine block.

---

## 3. Cross-Subdomain Dependency Declaration

*Cross-subdomain calls/reads (permitted) and dependency gaps (a peer must author a capability for this CR). `dependency` is business language; `direction` is `this_subdomain → peer`; `existing_artifact` cites an existing FQDN when reused. Status ∈ SATISFIED (reuse existing) | GAP (new, owned by the peer).*

Register `cross_subdomain_deps` in the Machine block.

---

### A platform change acts only on the platform

A platform dossier may **cite** a domain artifact — as a belief verified at P2, as impact at P3, as
what was observed in the composition it was validated against. It may not **act** on one. A domain
artifact in §3 or §4 is a platform change scheduling work inside a domain it does not own, and a
dependency declared *from* a platform subdomain *to* a business one points the arrow backwards: a
capability does not depend on the domains that reach it.

The distinction is what makes a platform dossier age. A composition selects its domains; a citation
becomes history when one is not selected, and a scheduled action becomes a claim on something that
is not there.

---

## 4. PPS Artifacts Requiring Action

*Existing PPS artifacts that must be reviewed or replaced as part of this CR. `fqdn` is the existing artifact. Action ∈ REPLACE | REVIEW | REUSE | EXTEND — Stage 7's inventory already admits EXTEND, and an
artifact amended to admit a case it did not is extended at both rungs or at neither.*

Register `pps_artifacts_requiring_action` in the Machine block.

---

## 5. Governance Boundary Rules

*Non-negotiable boundary rules for this subdomain — each a governance invariant, not an implementation detail.*

Register `boundary_rules` in the Machine block.

---

## 6. Governance Outcome

*Capabilities requiring protocol realization (Stage 7 assigns the artifact family + binding FQDN). Business language; organized by owning subdomain.*

Register `governance_outcome` in the Machine block.

---

## Gate 1 — Design Approval, where a change ends here

**A governance-surface change closes Gate 1 at this stage.** The governance surface is authored, not
constructed, so such a dossier is terminal at P6 — and the gate that reviews a dossier as a body
belongs at the end of the dossier, wherever that end is. The full dossier (Stages 0–6) is presented
for review as a body, and approval authorizes the authoring of the clauses and rules it argues for.

**Gate 2 has no subject here and does not apply.** It exists to lock a mandate before artifact
authoring begins; a change that schedules no artifacts has no mandate to lock. What Gate 2 protects
for a domain change — that scope is frozen before anyone writes an artifact — is carried by Gate 1
being the last word rather than the second-to-last.

**For a change that continues to P7, this section is not used.** Gate 1 closes there, as it always
has, over a dossier that includes a design.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | business_model_[subdomain]_v0.md | COMPLETE |
| Stage 5 — Business Intent | business_intent_[subdomain]_v0.md | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
| Stage 7 — Design Intent | Pending | — |

---

## gov_projection — Governed Handoff to Stage 7

*The bounded inputs and emit keys mirror the engine's gov_projection schema exactly
(`contracts/gov_projection.py`). Domain Placement, Boundary Rules (§5), and Governance Outcome (§6)
are this stage's record; the four emit registers cross to Stage 7. Emit keys match the register ids
above exactly.*

| Direction | Registers |
|-----------|-----------|
| **Consumes** ← p5, p0 | scope_boundary · invariants · cross_subdomain_refs |
| **Emits** | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action |
