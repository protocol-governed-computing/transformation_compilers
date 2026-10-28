# Findings — Decision Ledger Census of `blockchain`

Step 1 of `PLAN_DECISION_LEDGER_AUTHORING.md`, run on the second domain. The census classifies
every leaf value in the baseline P7 registers and lists the distinct human decisions they encode.

Run it with:

```
python engine/census.py ../../business_domains/blockchain/design/p7_*.md domains/blockchain/census_profile.yaml
```

`census.py` now reads a per-domain profile. Run with `book_library_mgmt`'s profile, it reproduces
that domain's census exactly.

## Result

The gate passes. The domain rests on 32 decisions. Its P7 holds 2,424 leaf values.

| Class | Leaves | Share |
|---|---:|---:|
| Decision | 296 | 12.2% |
| Case | 26 | 1.1% |
| Mechanical | 2,102 | 86.7% |
| Unaccounted | 0 | — |

One decision costs about 9 decision leaves, and about 76 leaves of P7 overall. The book domain
cost about 12 and 119. Blockchain has fewer operations, and each one is smaller.

| Register | Decision | Case | Mechanical |
|---|---:|---:|---:|
| `interface_fields` | 154 | | 410 |
| `step_bindings` | 79 | | 512 |
| `transport_bindings` | 26 | | 157 |
| `new_artifacts` | 24 | | 166 |
| `vocabulary_extensions` | 8 | | 48 |
| `cc_composition` | 1 | | 469 |
| `execution_topology` | | | 160 |
| `test_cases`, `test_case_values` | | 26 | |
| other registers | 4 | | 180 |

Two registers are new to the census. In `transport_bindings`, the public name of an offered act
is a decision, and every other leaf follows from the request. In `vocabulary_extensions`, each
value the business named is a decision.

## The decisions

The seeds of all seven change requests are in git, deleted with the dossiers in `5d405b8`. Each
decision below cites the seed that states it.

| # | Decision | Seed |
|---:|---|---|
| 1 | Identity says who an actor is and whether the business trusts them | cr_01 |
| 2 | Operations: register, accept, reject | cr_01 |
| 3 | The actor is a participant acting for themselves | cr_01 |
| 4 | An actor carries a name, a contact address and two preferences | cr_01 |
| 5 | Preference defaults: currency BACHI, language English | cr_01 |
| 6 | An actor is identified by their contact address | cr_01 |
| 7 | A registration requires a name and a contact address | cr_01, cr_05 |
| 8 | A repeated registration is the same actor, a new occurrence, resets nothing, and the first details prevail | cr_01 |
| 9 | States: unverified, accepted, rejected; a new actor is unverified | cr_01 |
| 10 | A decision is made only about an unverified actor | cr_01, cr_05 |
| 11 | A decision is an acceptance or a rejection, nothing else | cr_01, cr_05 |
| 12 | A decision needs a registration that exists | cr_01 |
| 13 | A decision names its authority | cr_01 |
| 14 | No one decides about themselves | cr_01, cr_05 |
| 15 | A rejection states grounds; an acceptance may | cr_01 |
| 16 | A decision changes only state, authority and grounds | cr_03 |
| 17 | The trail records every registration and decision, with authority and grounds | cr_01 |
| 18 | Events: registered, accepted, rejected, and what each carries | cr_01, cr_04 |
| 19 | The business can list rejected actors | cr_01 |
| 20 | The acts offered from outside, and their public names | cr_02 |
| 21 | An entrance turns away only a request it cannot read | cr_02 |
| 22 | A caller is told one of three things, and turned away differs from decided against | cr_02 |
| 23 | No account or login is required | cr_02 |
| 24 | A wallet goes only to a person identity holds and has accepted | cr_04 |
| 25 | One person holds one wallet | cr_04 |
| 26 | A wallet's identity is formed from its holder, with the prefix `wal` | cr_04, cr_07 |
| 27 | The address is derived from key material supplied to the business | cr_04 |
| 28 | A new wallet holds zero, in BACHI, classified DEFAULT, and is active | cr_04, cr_07 |
| 29 | Classifications: default, private, business, savings | cr_04 |
| 30 | Wallet states: active, inactive, closed; only creation is built | cr_04 |
| 31 | The trail records a wallet's creation and its holder | cr_04 |
| 32 | Wallet reads identity's records and never writes them | cr_04 |

## Four of seven change requests are doctrine, not decisions

Four seeds add no business decision. Each repairs how hand-written P7 realized a decision already
made.

| Change | What it repaired | Doctrine that prevents it |
|---|---|---|
| cr_03 | A decision overwrote the actor's record and lost their name and preferences | A transition changes only what the decision names |
| cr_05 | Rules came from the request, so a caller could widen them | A rule is a literal of the act; a request carries only domain fields |
| cr_06 | An act carried on past a failed record | A failed record ends the act |
| cr_07 | The trail, the moment and the wallet's values came from the request | An act states its own values |

The book domain showed the same pattern: three of five changes repaired hand-written HOW. A
generator that applies the doctrine would have made none of these four changes necessary.
`engine/generate_domain.py` already applies all four rules. A transition updates only its state.
Rules, trails, states and stored values are literals of the act. Every status other than success
ends a component unless a pattern routes it on. The blockchain run will confirm this.

## Where P7 and the seeds disagree

These need the owner before a ledger is written. Each is a candidate defect, not a confirmed one.

1. **A wallet is requested separately.** cr_04 says a wallet follows acceptance and is not
   something a person asks for. P7 offers a separate wallet act whose request carries the key
   material. The seed also says the key material is supplied to the business, and does not say
   when or by whom.
2. **Asking again for a wallet.** cr_04 says asking again changes nothing. Its refusals list says
   a person who already holds a wallet is refused. P7 refuses. The seed holds both readings.
3. **No way to list rejected actors.** cr_01 asks for it. P7 has no reading act. The test suite
   lists them by reading the store directly, so the criterion passes without the business being
   able to ask.
4. **A repeated registration's details.** cr_01 says the differing details are recorded with the
   occurrence. P7's registration occurrence records only its name and the address.
5. **The "registered again" event.** cr_01 names it as a business event. P7 has no such event.

The owner answered all five, in `LEDGER_OWNER_ANSWERS_BLOCKCHAIN.yaml`. The separate wallet
request stays, and so does the refusal of a second wallet. A reading act lists actors by state. A
repeated registration records the details it submitted, and announces its own event. Three of the
five change today's design.

## What the catalog lacks

The book catalog covers decisions 1 to 19 and 24 to 31. Three groups need new question types:

- **Offering (20 to 23).** Which acts are public, under what name, what an entrance may refuse,
  and how answers are classed. Today these are TI and TE rows. Most of them follow from the act,
  so the questions are few.
- **Reach (32).** Which other subdomain's records an act reads. This is the cross-subdomain
  question. A generator can derive the reach from decision 24, so it may need no question at all.
- **Supplied material (27).** A value the business derives from what the caller supplies, by a
  rule the business names. The book domain had none.

## What this predicts for the next steps

- The ledger should be about 32 answers and five owner questions.
- The generator needs new patterns for the transport boundary, a cross-subdomain precondition and
  a derived value. It needs no new doctrine rule.
- The engine's book run must still pass after each of those changes.

## The brief

`LEDGER_BRIEF_BLOCKCHAIN.md` states the requirements in business words, for an author who has not
seen the design. It draws on the 44 criteria of the three test suites, the seeds and the owner's
answers. It names no artifact, store or step.

Three of its requirements have no check yet, because the owner's answers added them:

- listing actors by state;
- a repeated registration recording the details it submitted;
- a repeated registration announced as a registration again.

They need criteria, written from the brief before any design is generated.
