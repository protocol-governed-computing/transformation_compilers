# Readiness for Assimilation

The derive route (`transformation/design/derive/`, `tc phase derive`) is assimilated into the Design
Compiler when every criterion below holds. It is a second route to the Design Compiler's outcome: a
design derived from a decision ledger, where the phases judge a design someone authored. Each criterion states its evidence and where it stands today. The
prototype's findings, briefs, owner answers and analysis are in git history at `3859bec`, under `decision_authoring_prototype/`.

## 1. The method generalizes

| # | Criterion | Evidence | Today |
|---|---|---|---|
| 1.1 | A block composer replaces the operation patterns | book and blockchain regenerate through it and pass every criterion they pass now | **holds**: `transformation/design/derive/compose.py`; book 23/23 and 27/27, blockchain 26/26, 6/6, 12/12 and 9/9, at 100% construction; one composition, `change_identity`, is still fitted |
| 1.2 | A held-out domain derives with no new block | ai_governance passes its 21 owner-answer criteria, or fails only on a declared platform gap | **holds**: 100% construction; 21/21, with the cap counted by the registry's declared COUNT; no new block; see `domains/ai_governance/FINDINGS_COMPOSER_RUN.md` in that history |
| 1.3 | The question catalog is closed for the three domains | every answer in the three ledgers fits a catalog question; the 5 ai_governance candidates are added or refused | **holds**: `transformation/design/derive/catalog.yaml`, 31 questions; all 5 candidates added, plus `values` and `sets` from the composer run and `replaces` from deciding identities; every ledger key names its question, and two questions are answered by the carried surface |
| 1.4 | Ledgers are written in the closed shape, not normalized by hand | a ledger schema refuses an answer outside its shape | **holds**: `transformation/design/derive/ledger_schema.yaml` and `check_ledger.py`; the three ledgers are admitted, 16 answers outside their shapes are refused, and `compose.py` refuses before deriving. The closed ledger has no open question or case yet |

## 2. It obeys the repository's rules

| # | Criterion | Today |
|---|---|---|
| 2.1 | It lives in `transformation/`, with absolute imports and no `sys.path` | **holds**: `transformation/design/derive/` (base, compose, ledger, splice, identity, seal, cli), run as `tc phase derive check \| meta \| selftest \| derive \| identities \| splice \| revise`; `scripts/derive_build.sh` builds a domain in scratch. The prototype folder keeps the ledgers, checks, findings and two analysis scripts |
| 2.2 | Every snapshot fact arrives through `inspector.api.query` | **holds**: the held artifacts, the composition's listing and the sameness declaration are read through the inspector; a design of record is read by `transformation.machine_block`, as every reader in the package reads one |
| 2.3 | Doctrine is a sealed rule set with a `$id`, revisions and a digest, and every result names it as `judged_by` | **holds**: the doctrine, the ledger schema and the catalog each carry a `$id` and `x-revisions` with digests (`seal.py`); a derivation is refused while one is not its last revision, and every derived design names all three under `_judged_by`. They are sealed in the package, not into a compiled artifact |
| 2.4 | Each doctrine rule cites what it realizes, as phase rules do | **holds**: every rule cites a lifecycle invariant, and `tc phase derive meta` checks each resolves in the composition. Six invariants were authored for the purpose (`INVARIANT_DERIVED_ACT_ORDERED_V0`, `_DERIVED_STORAGE_BY_NEED_V0`, `_DERIVED_INTERFACE_STATED_V0`, `_DERIVED_COMPONENT_SHARED_V0`, `_ACT_STATES_ITS_OWN_VALUES_V0`, `_REQUEST_CANNOT_WIDEN_RULES_V0`), named by `CONSTITUTION_CHANGE_MGMT_V0` under `applies_to: derived_design` |
| 2.5 | `sameness` decides identity: a change of meaning takes the next version, and a retirement is recorded | **holds**: `tc phase derive identities` renders the derived design as construction will and compares it with the composition. Same meaning is EXTEND; changed meaning takes the next unused version and supersedes its predecessor; an operation's `replaces` answer names the operation it takes the place of; what the ledger no longer derives is retired (RETIRE, new to the design language), with no successor. Construction's emit compares again and accepts all three domains. Deletions are written as retirement-ledger entries. Book keeps 23 and supersedes 18; blockchain keeps 13 and supersedes 9; ai_governance keeps 4, supersedes 14, replaces 3 and retires 20. The domain suites name the predecessors they were written against; `scripts/derive_suite.py` dispatches the successor each declares |

## 3. It is governed

| # | Criterion | Today |
|---|---|---|
| 3.1 | Every derived row traces to a ledger answer, a doctrine rule, or the carried surface, and an untraced row is refused | every row carries `_from`; nothing refuses an untraced one |
| 3.2 | Every ledger answer cites a seed or names the owner as its authority | book and blockchain cite seeds; ai_governance names the owner |
| 3.3 | The lifecycle states where the ledger sits: P1–P3 stay dialog for discovery changes; P4–P7 are derived; Gate 1 approves the ledger | decided in `ANALYSIS_LEDGER_VS_PHASES.md` (git history); not in the standard |
| 3.4 | Derived P1–P6 pass the phase rules, or the rules they replace are named | the derived design is judged by construction only |
| 3.5 | The carried-surface rule is in the standard: names fixed by data and callers are carried, and changing one is a migration the ledger states | prototype rule. Store, binding (RB) and entrance (IN) names are carried; store matching is heuristic |
| 3.6 | A doctrine or block change runs as its own dossier, and re-derives every domain's design of record | stated in `ARCHITECTURE_IMPACT.md` (git history); no dossier yet |

## 4. It is proven on every build

| # | Criterion | Today |
|---|---|---|
| 4.1 | Derivation is deterministic | book, blockchain and ai_governance each generate identical output twice |
| 4.2 | `regression.sh` runs the derive-and-build pipeline for each derived domain | **holds**: `--all` runs `derive_ledgers`, `derive_meta`, `derive_selftest` and `derive_<domain>` for the three domains, with their expected results in `expectations.yaml` |
| 4.3 | Construction completeness is 100% for every derived domain | book, blockchain and ai_governance at 100% |
| 4.4 | Each derived domain's criteria are written before its design | blockchain and ai_governance checks were; book's suites predate the method. That is history and stays a stated limit |

## 5. What it leaves behind is clean

| # | Criterion | Today |
|---|---|---|
| 5.1 | The platform gaps it found are resolved, or each is a declared refusal at admission | **resolved**: the count was never a platform gap (`CS_REGISTRY_V0` has declared COUNT since v1.0.0) — the composer lacked it, and now counts where the registry's entries are exactly the records counted; an empty answer resolved (`capability_transforms::CT_PURE_SELECT_RECORDS_V0`, used for any `nothing_found: empty`); retirement without a successor resolved (RETIRE) |
| 5.2 | Behavior the owners decided reaches the domains as numbered change requests, not as a derived design swapped in | none delivered; book's update rule and blockchain's listing, repeat registration and shared address wait |
| 5.3 | Defects found in today's designs are fixed or parked by name | parked in the handoff |

## The order to work in

1. Build the block composer (1.1). Done.
2. Run ai_governance through it (1.2). Done.
   Close the catalog and the ledger shape (1.3, 1.4). Done.
3. Then do the engineering in sections 2 and 4. Done. 2.5 needed a retirement without a successor,
   which the design language now states (RETIRE); 2.4 needed six lifecycle invariants, now authored.
4. Write the standard text last (3.3–3.6). It describes a design proven to hold.
