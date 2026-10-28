# Readiness for Assimilation

The prototype is ready to join `transformation_compilers` as its third compiler when every
criterion below holds. Each criterion states its evidence and where it stands today.

## 1. The method generalizes

| # | Criterion | Evidence | Today |
|---|---|---|---|
| 1.1 | A block composer replaces the operation patterns | book and blockchain regenerate through it and pass every criterion they pass now | **holds**: `engine/compose.py`; book 23/23 and 27/27, blockchain 26/26, 6/6, 12/12 and 8/9, at 100% construction; one composition, `change_identity`, is still fitted |
| 1.2 | A held-out domain derives with no new block | ai_governance passes its 21 owner-answer criteria, or fails only on a declared platform gap | **holds**: 100% construction; 17/21, and the four failures follow from the registry count, a declared gap (21/21 with it stood in); no new block; see `domains/ai_governance/FINDINGS_COMPOSER_RUN.md` |
| 1.3 | The question catalog is closed for the three domains | every answer in the three ledgers fits a catalog question; the 5 ai_governance candidates are added or refused | 23 types; 5 candidates open; the composer run added answer shapes (`checks`, `on_refusal`, `sets`, `when`, `look_up`, a fixed identity) the catalog does not yet hold |
| 1.4 | Ledgers are written in the closed shape, not normalized by hand | a ledger schema refuses an answer outside its shape | no schema; ledgers transcribed by hand |

## 2. It obeys the repository's rules

| # | Criterion | Today |
|---|---|---|
| 2.1 | It lives in `transformation/`, with absolute imports and no `sys.path` | outside the package; uses `sys.path` |
| 2.2 | Every snapshot fact arrives through `inspector.api.query` | reads P7 and P8 files directly |
| 2.3 | Doctrine is a sealed rule set with a `$id`, revisions and a digest, and every result names it as `judged_by` | `doctrine.yaml` is data; it is neither sealed nor versioned |
| 2.4 | Each doctrine rule cites what it realizes, as phase rules do | no citations |
| 2.5 | `sameness` decides identity: a change of meaning takes the next version, and a retirement is recorded | changed components keep `_V0` |

## 3. It is governed

| # | Criterion | Today |
|---|---|---|
| 3.1 | Every derived row traces to a ledger answer, a doctrine rule, or the carried surface, and an untraced row is refused | every row carries `_from`; nothing refuses an untraced one |
| 3.2 | Every ledger answer cites a seed or names the owner as its authority | book and blockchain cite seeds; ai_governance names the owner |
| 3.3 | The lifecycle states where the ledger sits: P1–P3 stay dialog for discovery changes; P4–P7 are derived; Gate 1 approves the ledger | decided in `ANALYSIS_LEDGER_VS_PHASES.md`; not in the standard |
| 3.4 | Derived P1–P6 pass the phase rules, or the rules they replace are named | the derived design is judged by construction only |
| 3.5 | The carried-surface rule is in the standard: names fixed by data and callers are carried, and changing one is a migration the ledger states | prototype rule; store matching is heuristic |
| 3.6 | A doctrine or block change runs as its own dossier, and re-derives every domain's design of record | stated in `ARCHITECTURE_IMPACT.md`; no dossier yet |

## 4. It is proven on every build

| # | Criterion | Today |
|---|---|---|
| 4.1 | Derivation is deterministic | book, blockchain and ai_governance each generate identical output twice |
| 4.2 | `regression.sh` runs the derive-and-build pipeline for each derived domain | run by hand |
| 4.3 | Construction completeness is 100% for every derived domain | book, blockchain and ai_governance at 100% |
| 4.4 | Each derived domain's criteria are written before its design | blockchain and ai_governance checks were; book's suites predate the method |

## 5. What it leaves behind is clean

| # | Criterion | Today |
|---|---|---|
| 5.1 | The platform gaps it found are resolved, or each is a declared refusal at admission | empty-answer filter and registry count parked |
| 5.2 | Behavior the owners decided reaches the domains as numbered change requests, not as a derived design swapped in | none delivered; book's update rule and blockchain's listing, repeat registration and shared address wait |
| 5.3 | Defects found in today's designs are fixed or parked by name | parked in the handoff |

## The order to work in

1. Build the block composer (1.1). Done.
2. Run ai_governance through it (1.2). Done; the registry count stays a declared gap (5.1).
3. Then do the engineering in sections 2 and 4. It is mechanical once the design is stable.
4. Write the standard text last (3.3–3.6). It describes a design proven to hold.
