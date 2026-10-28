# Findings — Decision Ledger Census of `ai_governance`

Step 1 of `PLAN_DECISION_LEDGER_AUTHORING.md`, run on the third domain. This domain is the held-out
test: the generator should derive it from a ledger with few or no new patterns.

```
python engine/census.py ../../business_domains/ai_governance/design/p7_*.md domains/ai_governance/census_profile.yaml
```

## Result

The census itself passes, with no value left unaccounted for. The domain's P7 holds 2,707 values.

| Class | Leaves | Share |
|---|---:|---:|
| Decision | 448 | 16.5% |
| Case | 131 | 4.8% |
| Mechanical | 2,128 | 78.6% |
| Unaccounted | 0 | — |

The decision share is the highest of the three domains. Two maps carry it: the tools each license
tier allows, and the parameter rules of each tool. Both are business tables written into the design
as literals.

## No business statement exists for what the domain does

The domain has two change requests, both deleted with their dossiers in `5d405b8`. Neither states
what the domain does.

- **cr_01** adds test cases to three checks. It changes no behavior.
- **cr_02** repairs a routing defect in reclaim, and a parameter result nothing wrote.

The behavior itself came from RI-0 by migration. RI-0 holds no business statement for it either.
Its only dossier is for `agent_admission`, the fork this workspace deleted. So the decisions below
can be read from P7, but none of them can cite a seed. The book and blockchain ledgers each cited
one for every answer.

## The decisions P7 encodes

These are inferred from the design. No business author has stated them.

**Agent governance**

| # | Decision |
|---:|---|
| 1 | An agent's proposed action is judged before any tool runs |
| 2 | The checks run in order: well formed, tool declared, user licensed, tier covers tool, parameters valid |
| 3 | Three tools exist: read a record, provision a standard license, provision a premium license |
| 4 | The tiers: none reads; standard also provisions standard; enterprise provisions both |
| 5 | A license must be active |
| 6 | Each tool declares parameter rules |
| 7 | Four denial reasons, one per failed check |
| 8 | Every outcome is audited; an authorized action is also registered |
| 9 | Two events, authorized and denied, and what each carries |
| 10 | Request and action identities carry the prefixes `AREQ` and `AGOV` |
| 11 | A user's tier and status are read from license facts |

**AI licensing**

| # | Decision |
|---:|---|
| 12 | Operations: provision, deny a provision, reclaim |
| 13 | Actors: an employee requests; the system denies and reclaims |
| 14 | A license needs training complete |
| 15 | A license needs fewer assigned than the cap |
| 16 | A license is reclaimed when unused for the threshold of days or more |
| 17 | A reclaim the registry refuses leaves the license assigned (cr_02) |
| 18 | Events: provisioned, denied, revoked, and what each carries |
| 19 | The reason a cap refusal gives: `CAP_REACHED` |
| 20 | Four further events are declared: employee registered, cap set, training completed, usage recorded |

## What the census found in today's design

Each item needs the owner before a ledger is written.

1. **Licensing takes every fact and rule from the request.** The cap, the count already assigned,
   whether training is complete, the last day of use, today's date, the threshold and even the new
   license's identity all arrive in the payload. A caller can obtain a license by stating that
   training is complete and nothing is assigned. This is the `rules_held` doctrine violation that
   blockchain's cr_05 repaired, and it is the known leak of `cap`, `threshold_days` and
   `days_inactive`.
2. **The cap and the threshold have no value anywhere.** No seed or literal states them. Only the
   caller does.
3. **The two parts are not connected.** Agent governance reads a user's tier from a license-facts
   store that no act writes; the regression seeds it by hand. Provisioning writes a registry that
   agent governance never reads.
4. **Four events are never announced.** No act emits employee registered, cap set, training
   completed or usage recorded, and no act records training or usage.
5. **Deny provision is its own act**, taking the reason from the caller. Provisioning already
   denies when a check fails.
6. **One actor is unused.** Nothing names the enterprise runtime.

## The domain has no acceptance suite

The book and blockchain runs were judged by suites written from their seeds. Here the regression
dispatches one happy path per part, and `testbed/routing_closure` holds 4 criteria. The rest of
the behavior has no criteria. The held-out test needs criteria written before any design is
generated, as the blockchain checks were.

## What this means for the held-out test

The generator test still stands: can a ledger drive this domain with few new patterns? But
authoring cannot run as it did for book and blockchain, because there is no business statement to
cite. The owner has to supply the authority, either as a short business statement or as answers
to these findings.
