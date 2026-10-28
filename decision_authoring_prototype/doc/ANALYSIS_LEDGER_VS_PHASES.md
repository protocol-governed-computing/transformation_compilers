# Ledger Authoring and the Transformation Lifecycle

This document assumes ledger authoring works, and asks what it changes in the lifecycle.

## Phase by phase

| Phase | Today | With the ledger |
|---|---|---|
| P0 change seed | The business's own words. Gate 0: the human confirms the seed. | **Unchanged.** The seed is the brief the ledger is answered from. |
| P1 change request | Classification, problem, outcome, known facts, deferrals | **Absorbed.** Deferrals become open questions. Classification and outcome become the ledger delta's header. |
| P2 domain model | Entities, processes, baseline fit, gaps | **Absorbed.** `things` and `operations` hold entities and processes. Unanswered questions hold the gaps. The generator's reuse of components holds the baseline fit. |
| P3 analysis loop | Gap resolution with evidence, to saturation | **Becomes the interview.** The question catalog asks, the owner answers, and `decided_by` carries the authority. Saturation means no question the catalog asks is left unanswered. |
| P4 business model | Canonical consolidation | **The ledger is the consolidation.** |
| P5 business intent | WHAT: objects, identity, invariants, actions | **The ledger's closed shapes.** This phase maps most directly. |
| P6 governance intent | WHERE: domain, subdomain, ownership | **The ledger header plus doctrine.** Cross-subdomain placement would need questions the catalog does not yet ask. |
| P7 design intent | HOW: 4,595 hand-kept lines. Gate 1: design approval. | **Derived.** The front end emits it, and every row cites a ledger entry or a doctrine rule. |
| P8 authoring mandate | Mechanical build order. Gate 2. | **Unchanged.** It was already mechanical. |

So P7 is short-circuited outright. P1 to P6 are not skipped. Their work moves into one interview,
and the ledger is its only output.

## Should P1 to P6 still run behind the scenes?

The phase rules depend on them. P7 alone has 283 rules, and many cite upstream phases, for
example refusal discharge against P0. The prototype ran only the construction check, which needs
no upstream phase. A ledger path that skips P1 to P6 silently loses those checks.

There are two options:

1. **Render P1 to P6 from the ledger as projections.** Each is generated and reviewable. None is
   authored. The phase rules keep running unchanged, and the dossier keeps its shape for audit
   and for every gate. The cost is that a projection checked against rules written for authored
   documents can fail on form rather than substance.
2. **Replace the phase rules with ledger rules.** Every question is answered or open. Every
   answer names its authority. Every P7 row traces to an answer or a doctrine rule. This is
   cleaner, but it is a rewrite of the transformation standard.

The recommendation is option 1 first, because it changes no governance. Move to option 2 only
where a projection proves to be ceremony.

## What changes

| | Today | Ledger |
|---|---|---|
| What a person authors | P0 to P7; P7 is 4,595 lines in PGC vocabulary | P0, plus about 115 lines of answers in domain words |
| Unit of review | A design document, judged as a body | A decision, with its authority |
| Gate 1 approves | The full P7 | The ledger, plus the generated diff and its trace |
| A change is | A dossier re-authored P0 to P8 | A ledger delta. P7 and its diff follow mechanically. |
| Where an unstated behavior goes | Into P7, silently | Nowhere: it is an open question, and admission refuses it |
| Authority for HOW | Each P7 author | The pattern library and doctrine, shared by every domain |

## What the prototype showed the current lifecycle misses

The current design passed every phase, construction at 100%, and 50 execution criteria. The
ledger path still found:

- four behavioral defects, confirmed by probes: search shows retired books; two cases where a
  refused registration permanently consumes an identity; and retiring something already retired
  succeeds;
- two places where a summary claims what the registers do not encode: search exclusion, and the
  update rule's wording;
- one dead required input (`copy_fields`);
- nine decisions the domain's own criteria never state.

The cause is structural. P7 is hand-written HOW, and the checks verify structure and closure.
They do not check that a stated intent is encoded. The ledger closes that gap by construction:
HOW is derived from decisions, so a decision cannot be stated and then left unencoded.

## What it costs

- **A new design authority.** `tc construction check` exists because "a generator that invents
  design is a second, ungoverned design authority." The ledger front end is such a generator. Its
  doctrine and patterns must be governed like the Construction Compiler: sealed, versioned, and
  conformance-tested against domains. Otherwise the problem has only moved.
- **Defects in the doctrine spread.** A wrong rule is wrong in every domain at once. The
  correction spreads the same way, as the four fixes did here.
- **Expressiveness.** Closed shapes and a fixed pattern library will not cover every design. An
  escape hatch is needed: a hand-written P7 fragment for one component, clearly marked, that is
  still checked.
- **Lost narrative.** P2 and P3 record what was searched and why an answer was overturned. A
  ledger answer records only the result and its authority, unless the interview log is kept.

## Is it worth pursuing?

Yes, for three reasons the prototype supports with evidence:

1. **Load.** One domain fell from 4,595 lines of PGC vocabulary to about 115 lines of decisions,
   and the behavior was preserved: 23/23 and 27/27 criteria hold.
2. **Correctness.** The ledger path found defects that the full lifecycle passed. These are
   failures of hand-written HOW, which is what the ledger removes.
3. **Fit with the thesis.** PGC's claim is that authority is established before execution. The
   ledger makes authority explicit for each decision (`decided_by`). P7 cannot express that. It
   is also the natural home for the parked decision-accounting design.

Three things are not yet shown, and each could still sink it:

- **Generality.** The patterns are fitted to one domain. The second domain is the test.
- **Governance of the generator.** Doctrine must be sealed and checked the way construction is.
- **Human authorship.** Both blind authors were LLMs. One human author is needed before any
  claim about cognitive load.
