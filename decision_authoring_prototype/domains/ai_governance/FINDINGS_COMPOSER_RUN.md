# Findings — `ai_governance` Through the Block Composer

The held-out test asked whether a third domain derives without new operation patterns, and the
answer was no: it needed about six. The block composer replaced the patterns. This run asks the
same question of the composer: does ai_governance derive with no new block?

## The answer

Yes. The domain derives from `ledger.yaml` with the twelve blocks the design names, and no others.
It passes every owner-answer criterion except those the registry's missing count decides.

| Measure | Result |
|---|---|
| Construction completeness | 100% (1,849 of 1,849 facts) |
| Artifacts derived | 58: 27 CC, 9 EV, 7 WF, 7 IN, 3 AC, 2 STRUCTURE, 2 RB, 1 CT |
| Compile, assemble | pass; composition conformance passes |
| Owner-answer criteria | 17 of 21 |
| With the cap count stood in | 21 of 21 |
| Derivation | deterministic |
| Book and blockchain, rerun | generated output unchanged; every criterion they passed still passes |

## The four failures have one cause

The registry has a `count` in its code but declares no COUNT operation. So "under the cap" is not
realized, and the composer reports it as unrealized. Without it, a second employee is provisioned
at the cap. Three later criteria then fail on that employee's state, not on their own:

- a user without a license is denied: the employee now holds one;
- a reclaimed license no longer counts against the cap: the employee is refused a second license;
- an enterprise user may use a premium tool: the employee holds a standard license.

A probe that stood in only the refused provision passed all 21. The probe ran in scratch; the
checks are unchanged.

## What the six patterns became

Each shape the held-out test called a new pattern is now composer support for an answer. None
needed a block the design did not name.

| Held-out "pattern" | Answer in the ledger | Blocks the composer selects |
|---|---|---|
| Set a business value | `identity: {fixed: current}` | check, write at a fixed key; no claim |
| Record a fact about a thing | `sets`, `holds` | resolve, read; change where the record holds; a clock value from `form` |
| Refuse, recording and announcing a denial | `checks`, `on_refusal` | each refusal ends at a node that runs the part's `record` with its reason |
| End one of two ways on a condition | `when`, `otherwise` | form (the carried inactivity transform); a refusal ends where `otherwise` says |
| Look up what a value grants, with rules | `look_up: {contains}` or `{rules_on}` | look up, then check against what it answered |
| More than one actor | `actors`, `actor` per operation | none; rendering only |

`look up` was always one of the twelve blocks. This is the first domain whose answers select it.

The composer also gained:

- an identity generated from several fields;
- a part's trail read only from that part's components;
- only the transforms a component invokes are carried;
- the P8 entrances rebuilt from the derived design.

## What the composer decided that no answer states

- A refused claim is a refusal like any other, so an operation with `on_refusal` records and
  announces it. Its reason, `LICENSE_ALREADY_HELD`, is named by the composer.
- A check that the platform cannot realize gets no denial node, so nothing routes to an empty end.

## What this run leaves open

- **The registry count** is still a parked platform gap (readiness 5.1).
- **The entrance name.** The derived design names the governance request
  `IN_GOVERN_AGENT_ACTION_V0`. Today's is `IN_AGENT_ACTION_REQUESTED_V0`. Callers dispatch the
  workflow, whose name is carried, so no criterion sees it. The carried-surface rule should still
  carry the entrance's name.
- **An unused value.** The action's `request_identity` is formed, and nothing records it.
- **The domain's own suite.** `routing_closure` dispatches `WF_PROVISION_AI_LICENSING_V0`, which
  the owner's answers replaced. It fails by design, as expected before the run.
- **The composer grew.** `compose.py` went from 789 to 1,010 lines for these answers. The growth is
  in answer shapes, not blocks, but it is growth. The question catalog needs the shapes added
  (readiness 1.3).
