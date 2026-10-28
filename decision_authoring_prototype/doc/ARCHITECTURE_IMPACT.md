# Architecture Impact — Decision Authoring in `transformation_compilers`

This document states what changes in this repository if decision authoring is adopted. It is
measured against `ARCHITECTURE.md` and its thirteen rules.

## 0. The open work this answers

The repository already names this gap. In `CLAUDE.md`: "Making generation a governed step, or
making the design language small enough to write by hand, is open work." CLM's P7 was written by
generator scripts from P5 and P6, and the rules admitted it as if typed by hand. Decision authoring
does both:

- it makes generation the governed step;
- it makes the language a person writes small, about 115 lines for this domain.

## 1. The shape: a third compiler, between the two

```
   today      p0 ─ p1 … p6 ─ p7 (authored) ─ p8 ─▶ Construction ─▶ artefacts
                    Design Compiler judges each

   proposed   p0 ─ LEDGER (authored) ─▶ Derivation ─▶ p1 … p7 (projected) ─ p8 ─▶ Construction
                    Ledger check judges it     Design Compiler judges the projections, unchanged
```

There are three compilers, because they fail in three different ways:

| | Failure reads as | Fixed by |
|---|---|---|
| **Ledger check** (new) | A question is unanswered, or an answer does not fit its shape | The owner answers |
| **Derivation** (new) | The ledger is complete, but no pattern or transform realizes an answer | Amending the pattern library or the transform inventory |
| **Design Compiler** | A projected phase breaks a rule | A defect in derivation, never re-authoring |
| **Construction Compiler** | The mandate does not determine an artefact | Amending the design language |

The prototype hit the first, second and fourth in this run: open questions, the unrealized empty
search, and the construction check.

## 2. How the thirteen rules apply

| Rule | Effect |
|---|---|
| 1. Vocabulary widens as you descend | **Strengthened.** A person authors only business vocabulary. The widening to bindings, paths and FQDNs happens in one deterministic step, so a person cannot say HOW at all. |
| 2. Rules are declared, not coded | **The prototype violates it.** Doctrine and patterns are Python. They must become data: a sealed derivation rule set, each rule citing the invariant it realizes, like a register schema. |
| 3. A verdict names its rule set | Extended. A derivation names the catalog revision and the doctrine revision that produced it. An approval stands only under both. |
| 4. Pinned baseline | Unchanged. Derivation reads the pinned composition: which components exist to reuse, and which transforms are held. |
| 5. Facts only through the inspector | **The prototype violates it.** It reads the baseline P7 file for the carried transforms. Derivation needs inspector operations for a domain's components and transforms. |
| 6, 7. Dossiers are evidence and live with their domain | Unchanged. A change dossier holds a ledger delta, a derived P7 and a trace. |
| 8. Decisions are deterministic | **A natural fit.** A worker may conduct the interview and draft answers. The catalog decides what must be asked, and derivation decides HOW. No step depends on a worker. |
| 9. Completeness below 100 is refused | Gains a twin: an unanswered or unrealized ledger entry is refused before derivation runs. |
| 10. One live version | **The prototype does not handle it yet.** It kept `_V0` on components whose meaning changed (search, the four transitions). Derivation must consult `sameness` and emit the next version with `supersedes`. |
| 11. Phases, never stages | Unchanged. The ledger is not a phase. Projections are phases. |
| 12. No transport | Unchanged. CLI only. |
| Import rules | **The prototype violates them.** `compare.py`, `splice.py` and the probes manipulate `sys.path`. Inside `transformation/derive/` they would use absolute `transformation.*` imports and `inspector.api` only. |
| 13. One producer | **Applies to P7.** Once derived, P7 is never corrected by hand. A disagreement means the copy is stale. The ledger plus the doctrine is the only producer. |

## 3. What the repository gains

```
transformation/
    derive/                     the Derivation compiler (new)
        ledger.py               read and check a ledger against its schema
        catalog.py              the question catalog: which questions follow from the answers so far
        patterns.py             apply declared patterns; no doctrine in code
        project.py              render P1 to P6 as projections, and P7 as derived
        trace.py                cite, per P7 row, the answer or rule it came from
registry/
    schema/REGISTER_SCHEMA_LEDGER_V0.json    answer shapes, closed (the strict format)
    derivation/                 doctrine and patterns as data, sealed, each citing an invariant
cli.py                          tc ledger check · tc ledger derive · tc ledger trace
```

The platform gains invariants in `software_governance/registry/lifecycle/`. The prototype found
each of these as doctrine:

- every design row traces to a decision or a declared rule;
- no refusal after a refusable claim;
- a refusal is a status, not a route;
- a read is trailed before it answers.

These are platform invariants, because a domain cannot author one.

The inspector gains the operations derivation needs: a domain's components with their interfaces,
and its held transforms.

## 4. What stays

- **The Design Compiler and its 992 rules.** They judge the projected P1 to P7 unchanged. This is
  the safety net while derivation is new. It also measures whether a projection is substance or
  ceremony. A phase whose projection never fails a rule is a candidate to retire later.
- **The Construction Compiler, sameness and emission.**
- **Gate 0** (the seed) and **Mandate Approval** (P8).

## 5. What moves

- **Design Approval becomes Decision Approval.** A person approves the ledger delta and reads the
  derived diff with its trace. The person no longer reviews a body of HOW.
- **Designs of record.** A domain's source of record becomes its ledger in `<domain>/design/`. P7 of
  record becomes generated, as P7 is already generated from the registry today.
- **The prototype splits.** Engine, catalog and doctrine go to `transformation/derive/` and
  `registry/derivation/`. Each domain's ledger goes to that domain's `design/`, through a dossier.

## 6. Order of work

1. **A strict ledger schema.** `tc ledger check` refuses an answer outside its shape. This ends
   the hand normalization.
2. **Doctrine as data.** Move the order, storage, naming, interface, binding and reuse rules out of
   Python into `registry/derivation/`, sealed.
3. **Inspector operations.** Remove derivation's reads of P7 files.
4. **Versioning through `sameness`.**
5. **A second domain** (`ai_governance`). Measure how many patterns carry over unchanged.
6. **Projections of P1 to P6.** Run the Design Compiler on them.
7. **Adopt for `book_library_mgmt`** through a change dossier that also fixes the four defects.

Steps 1 to 4 bring the prototype within the repository's own rules. Step 5 decides whether to
continue. Step 6 keeps governance whole. Step 7 is the first real use.
