# Findings — `ai_governance` as the Held-Out Test

The book and blockchain runs fitted the generator to two domains. This run asked one question:
does a third domain derive from a ledger with few or no new patterns? The run closes with an
answer, and without deriving the domain.

## The answer

No. Even with ai_governance's logic kept as simple as it is today, the generator would need about
six new patterns:

| Pattern | Where the domain needs it |
|---|---|
| Set a business value | the license cap |
| Record a fact about a thing | training completed, a use of a license |
| Refuse, recording and announcing a denial | provisioning |
| End one of two ways on a measured condition | reclaim: 30 days unused, or still active |
| Look up what a value grants, with rules per entry | a tier's tools, and each tool's parameter rules |
| More than one actor | employee, system, agent, governor |

The blind author reached the same list from the business side. It needed five question types the
catalog lacks, and four of them match patterns above: `on_refusal`, `outcome_condition`, `grants`
and `value_rules`. The fifth, `refusal_order`, asks for the check order that the format says an
author may override but gives no question for.

## What held, and what grew

| Holds across three domains | Grows with each domain |
|---|---|
| The ledger format | Patterns: book 9, blockchain 4 more, ai_governance about 6 more |
| The doctrine | Question types: 14, then 9 more, now 5 more |
| The carried surface | |
| Blind authors make no unauthorized rule | |

This run tested the doctrine harder than the others. The blind author cited doctrine wherever the
brief restated it, and answered none of it. In the blockchain run, the author had answered three
doctrine rules as questions.

## Why the run stops here

Building the six patterns would fit the generator to a third domain. That is the outcome the held
out test exists to rule out, and it would not change the answer.

ai_governance was also built as a regression fixture, with simplifying assumptions. The census
found gaps that come from those assumptions, not from the generator. Chasing them would test the
fixture.

## The work this run produced

| File | What it holds |
|---|---|
| `FINDINGS_DECISION_LEDGER_CENSUS.md` | 20 decisions in 2,707 P7 values; no business statement exists for them; six gaps in today's design |
| `LEDGER_OWNER_ANSWERS_AI_GOVERNANCE.yaml` | 14 owner answers: the business holds its own facts and rules |
| `LEDGER_BRIEF_AI_GOVERNANCE.md` | the brief written from those answers |
| `checks/execution_validation_owner_answers.py` | 21 criteria; today's design holds 4 |
| `LEDGER_BRIEF_RUN_AI_GOVERNANCE.yaml` | the blind ledger: 72 answers, 17 open, 31 cases, 765 lines |

The owner answers stay on record and are not realized. Three requirements in the brief were my
inferences, not the owner's: a second registration of an employee is refused, setting the cap
again replaces it, and no license is provisioned before a cap is set.

## Open items the run found

- **The platform cannot count.** The cap needs a count of active licenses. The license registry
  counts internally but declares no COUNT operation, and no transform returns a list's length.
  This sits beside the parked empty-answer filter.
- **Reclaim against doctrine.** cr_02 ended a reclaim the registry refuses as "still active".
  `failed_record_ends` ends such an act refused, as blockchain's cr_06 did. The owner should rule
  which holds, or whether "still active" means refused with the license still assigned.
- **Tier names disagree.** Licenses are standard or enterprise, but the premium tool's rule
  requires the parameter `tier: premium`. The owner kept today's tables.
- **Licensing trusts the request.** The cap, the count, training, dates and the license identity
  all come from the request. This is the known leak of `cap`, `threshold_days` and
  `days_inactive`, and still the top domain fix.
- **The parts are not connected.** Agent governance reads a license store no act writes.

## What this means for incorporation

Whole-operation patterns do not generalize. Sealing them into dev/19 would freeze two domains' fit
and make every new domain a governed platform change.

The next design step is a small vocabulary of building blocks: claim, resolve, require, derive,
record, set, look up, and decide on a condition. A domain's operations would be composed from these
blocks, as the ledger's answers dictate. A new domain then adds answers, not code. The test of that
design is to re-express book and blockchain's operations in it. Only if they need no new block is
ai_governance the held-out test again.
