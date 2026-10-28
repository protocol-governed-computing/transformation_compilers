# Dossier Comparison — Phase Dossiers and Decision Dossiers

This document compares the `book_library_mgmt` catalog's real change history with what the same
history would be under decision authoring. The real dossiers are kept as fixtures in
`scripts/testbed/fixtures/catalog/cr_01_catalog` to `cr_05_catalog`.

## 1. Naming

| Compiler | Transforms | Status |
|---|---|---|
| **Decision Compiler** | decisions → design (P1 to P7, derived) | new |
| **Design Compiler** | judges each phase document against its rule set | kept; its input becomes derived |
| **Construction Compiler** | design → artifacts | unchanged |

"Decision Compiler" names its input, as the other two do. It compiles a ledger of decisions, the
way construction compiles a design. "Derivation" is what it does, not what it is.

## 2. The real history: five dossiers, 25,191 lines

| CR | What it changed | P0 statement | P1–P6 | P7 | P8 | Total |
|---|---|---:|---:|---:|---:|---:|
| cr_01 | founded the catalog | 113 (seed 397) | 2,861 | 3,762 | 570 | 7,703 |
| cr_02 | works above editions | 135 (seed 449) | 2,849 | 2,617 | 218 | 6,268 |
| cr_03 | the six events were declared and never announced | 75 (seed 236) | 1,263 | 1,255 | 92 | 2,921 |
| cr_04 | boundaries demanded fields no step read | 53 (seed 235) | 1,418 | 778 | 111 | 2,595 |
| cr_05 | rules were taken from the request, so a caller could authorize itself | 89 (seed 201) | 1,785 | 3,456 | 173 | 5,704 |

Business authors wrote 465 lines of problem statements. Everything else, about 24,700 lines, is the
phase dossier.

**Three of the five changes repaired defects in hand-written HOW.** None of them was a new
business requirement:

- cr_03: events declared but never emitted;
- cr_04: inputs required and never read;
- cr_05: rules supplied by the caller.

These are the same classes the prototype found still present today: `copy_fields` is required and
never read, and search criteria are supplied by the caller. A derived design cannot produce them.
Doctrine always wires an announced event to its emit, never declares an input no step reads, and
binds every rule as a literal. Under decision authoring, cr_03 to cr_05 (11,220 lines) would not
have been needed.

## 3. A decision dossier

```
cr_NN_<subject>/
  baseline.json                         the pinned composition                     unchanged
  p0_business_problem_statement.md      the business's words                       unchanged, human
  p0_seed_<...>.md                      the faithful rewrite; Gate 0               unchanged
  ledger_delta.yaml                     the decisions this change makes            NEW, the only authored design
  interview.md                          questions asked, answers overturned        NEW, evidence (replaces P3's narrative)
  derived/                              written by the Decision Compiler, frozen at delivery
    p1_ … p6_<...>.md                   projections of the ledger                  judged by the Design Compiler
    p7_design_intent_<...>.md           derived HOW                                judged; Gate 1 reads its diff
    trace.json                          each P7 row → ledger answer or doctrine rule
    verdict.json                        catalog and doctrine revisions; open; unrealized
  p8_authoring_mandate_<...>.md         mechanical; Gate 2                         unchanged
```

What each element answers:

| Element | Question | Who |
|---|---|---|
| P0 statement and seed | What does the business want, in its words? | business author; Gate 0 |
| `ledger_delta.yaml` | What did the business decide, and who had the authority? | owner, through the interview |
| `interview.md` | What was asked, and what changed its answer? | the interviewer (may be a worker) |
| `derived/` | What design follows, and why each part of it? | Decision Compiler; Design Compiler judges |
| Gate 1 | Do these decisions, and this diff, say what we meant? | owner |

### The same history as decision dossiers

| CR | Ledger delta |
|---|---|
| cr_01 | about 70 lines: actor, book, copy, eight operations, trail, events, cases from P0 §3 |
| cr_02 | about 40 lines: `work` added; a `register additional edition` operation; search groups by work; a question on records written before the change |
| cr_03–cr_05 | none. The defects are not derivable. |
| today's four defects | none. The current derivation already avoids them. |

Problem statements stay at their 465 lines. Authored design falls from about 24,700 lines to about
115.

## 4. Nuances

### 4.1 The ledger must cite the seed, or it can contradict it

The prototype ledger was written from the testbed criteria, not from P0. Checking it against
cr_01's P0 exposed a contradiction:

- **P0 §3:** "An update to bibliographic information may change the title, author or publication
  year. The update is refused when the changed title, author and publication year would match
  another registered book."
- **P1 to P5** carry that rule. P5's note reads: "Refused if the change would make the book a
  duplicate of another."
- **P7** encodes something else: `compare_identity` and `require_identity_unchanged` refuse *any*
  change to title, author or year.

The 992 phase rules passed the narrowing. Execution check 17 cannot tell the two rules apart.
Asked in the interview, the owner chose P7's rule, which is the opposite of what P0 says.

So each ledger answer should cite the seed statement it settles. `tc ledger check` should then refuse
an answer that contradicts its citation, unless the answer is marked as an amendment of the seed.

### 4.2 Records written before a change

cr_02 had to promise that a record written before works existed would still be found, retrieved,
updated, retired and reinstated. The prototype passed those criteria by luck: derivation forms the
work key from title and author instead of reading a stored one. The catalog needs a question for
it: "existing records — compatible as written, migrated, or refused?"

### 4.3 Delivered dossiers are frozen, and doctrine moves

A delivered dossier is never edited. Its derived design must be frozen together with the doctrine
revision that produced it. When doctrine changes, every domain's derived design of record changes
with it. That is a platform-wide change, and it needs its own dossier. Components whose meaning
shifts take their next version through `sameness`. A doctrine change is the most consequential
change in the system, and it should be governed as one.

### 4.4 What a human stops doing

The P3 baseline search ("what can be reused, what was examined and rejected") moves from the author
to the Decision Compiler, which queries the inspector. The author no longer records
`alternatives_checked`. The trace records which existing component was reused.

### 4.5 What is lost, and kept on purpose

- **P2 and P3 narrative.** The interview log keeps what was asked and what was overturned.
- **Expressiveness.** A design no pattern covers needs a marked, hand-written fragment, checked by
  the Design Compiler as P7 is today.
- **Gate 1's object.** The owner approves decisions and reads a diff. Nobody reviews the full HOW
  unless the trace shows a doctrine row they do not recognise.
