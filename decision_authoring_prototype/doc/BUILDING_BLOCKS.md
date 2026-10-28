# Building Blocks

The generator derives two domains from their ledgers. It does so with whole-operation patterns:
`register_with_first_child`, `update`, `decide`, `create_held` and eight others. Each pattern was
written for one domain's operations, and a third domain would need about six more. This document
replaces the patterns with a small vocabulary of building blocks, and tests it by re-expressing
every book and blockchain operation in it.

## Why patterns grow and blocks need not

A pattern bundles several decisions into one shape. `create_held` resolves a holder in another
part, requires a state, forms an identity, derives a value, pre-checks it, claims two identities,
writes a record and records a moment. A domain that needs any other combination needs another
pattern.

The same logic repeats across the patterns. Claiming an identity appears in six of them, and
pre-checking a claim in two. The patterns are compositions written out by hand. The blocks are what
they are composed of.

So this is a normalization. Each block appears once, and each ledger answer selects blocks. No
pattern has to anticipate which answers occur together.

## The vocabulary

A block is one step, realized by one platform capability. Each block answers with a fixed set of
statuses. A component is a sequence of blocks, and a workflow is a sequence of components.

| Block | Does | Realized by | Answers |
|---|---|---|---|
| `check` | refuses unless a rule holds | `VALIDATE_PARAMETER_RULES`, `VALIDATE_SET_MEMBERSHIP`, `VALIDATE_RECORD_STRUCTURE`, `COMPARE_EQUAL` | success, refusal |
| `form` | computes a value from others | a key transform, `GENERATE_ID`, a domain derive transform | success, refusal |
| `look up` | reads a value from a table the business states | `LOOKUP` | success, refusal |
| `resolve` | finds what an identity names | registry `RESOLVE` | found, not found, refusal, failure |
| `read` | reads a record | `READ` | found, not found, refusal, failure |
| `query` | answers the records matching criteria | `SELECT` with `SELECT`, `FILTER` or `GROUP` | success, failure |
| `claim` | takes an identity, refusing a held one | registry `REGISTER` | success, held, refusal, failure |
| `release` | gives an identity up | registry `DEREGISTER` | success, not found, refusal, failure |
| `write` | stores a new record, assembled from fixed and given values | `ASSEMBLE_RECORD`, `WRITE` | success, refusal, failure |
| `change` | sets named fields of a held record or records | `ASSEMBLE_RECORD`, `UPDATE`, `UPDATE_WHERE` | success, refusal, failure |
| `remove` | deletes a record | `DELETE` | success, not found, refusal, failure |
| `record` | appends a moment to a trail, timed when the trail holds a time | `NOW`, `ASSEMBLE_RECORD`, `APPEND` | success, refusal, failure |

Every block is an existing platform capability. None is new code.

Three operators compose blocks into workflows:

| Operator | Does |
|---|---|
| `then` | runs the next component on success; any other status ends the act refused (`failed_record_ends`) |
| `branch` | sends a named status to another path instead. A held claim can reuse the identity or take the repeat path; a refused check can take an alternative path |
| `end` | names an ending and the events it announces |

The doctrine decides how blocks group into components. A refusal must be its own component, because
a workflow reports its last component's status (`order`). A component that two operations share
is one component (`reuse`).

## Book, re-expressed

Every operation begins `check authorization`, and ends `record` and `end completed`. A read records
before it reads. These parts are left out below.

| Operation | Blocks |
|---|---|
| register book | check submission; resolve barcode, check free; form key, claim book; claim barcode; form work key, claim work (held → reuse), write work; form work key, write book; read book, write copy |
| register additional edition | check submission; form work key, resolve work, read work; form key, claim book; write book |
| register physical copy | resolve book; claim barcode; read book, write copy |
| update bibliographic information | resolve book; read book, form key, form work key, write-assemble, check complete; check identity unchanged (refused → claim path; success → write in place, end completed); claim book; claim work (held → reuse); write new, change copies (none matched → continue), remove old, release old |
| retire / reinstate book or copy | check the new state is admitted; change state where the current state matches |
| retrieve book details | read book; form work key; read work (not found → continue); query copies of the book |
| search catalog | query books: select registered, filter by criteria, group by work |

## Blockchain, re-expressed

| Operation | Blocks |
|---|---|
| register actor | check submission; claim address (held → repeat path); write actor; record moment, end completed. Repeat path: record moment with the submitted details, end repeated |
| accept actor | resolve, read actor; check not self, check outcome, change state and decided fields where the state is unverified; record moment |
| reject actor | check grounds stated; then as accept |
| list actors | record moment; query actors by state |
| create wallet | resolve, read actor (another part); check accepted; form address; resolve address, check free; form identity, claim identity; claim address; write wallet; record moment |

Every book and blockchain operation is a sequence of the twelve blocks and three operators. Neither
domain needs a block beyond them.

## ai_governance, prospectively

The held-out run closed because the domain needed about six new patterns. Expressed in blocks, they
are compositions, except for one:

| What the domain needed | In blocks |
|---|---|
| set a business value (the cap) | write at a fixed key |
| record a fact (training, a use) | change; record |
| refuse while recording a denial | branch each refused check to: record denial, end denied |
| end one of two ways on a condition (reclaim) | check inactive (refused → end still active); release; change state; record; end reclaimed |
| look up what a tier grants, with rules per tool | look up tools for tier, check membership; look up rules for tool, check parameters |
| more than one actor | a ledger answer per operation, not a block |
| count the licenses assigned | **no block.** The registry counts internally, but declares no operation for it |

So ai_governance needs no new block, only one missing platform capability. That capability sits
beside the empty answer, which the platform now gives (`CT_PURE_SELECT_RECORDS_V0`).

## What the ledger's questions select

| Question | Selects |
|---|---|
| `actor` | check authorization, or none |
| `required`, `required_when` | check submission, or check a field stated |
| `identity` | form key, claim; on duplicate: refuse, reuse (branch), or repeat (branch) |
| `precondition` | resolve, read, check |
| `states`, `invariant_on_change` | change, guarded by check state |
| `derived_value` | form |
| `allowed_values`, `grants`, `value_rules` | check, look up |
| `query_excludes`, `query_returns`, `nothing_found` | query |
| `reads_other_part` | resolve and read in that part; declared reach |
| `on_repeat`, `on_refusal`, `outcome_condition` | branch, end |
| `trail` | record |
| `announces` | end |

## As built

`transformation/decision/compose.py` is the composer. It replaces the twelve patterns, which are deleted.
`transformation/decision/base.py` keeps only the shared base: steps, components, stores, the carried
surface and rendering. The ledgers no longer name a pattern. Each operation says what it `does`
(`create`, `change`, `read` or `query`) and to which things, and its other answers select the
blocks.

| Measure | Patterns | Composer |
|---|---:|---:|
| Engine lines (generator and base) | 1,213 | 1,279 (composer 789, base 490); 1,516 after ai_governance (composer 1,010, base 506) |
| Operation patterns | 12 | 0 |
| Book: construction facts, artifacts | 2,076, 60 | 2,151, 57 |
| Blockchain: construction facts, artifacts | 1,332, 46 | 1,303, 44 |
| ai_governance: construction facts, artifacts | none | 1,849, 58 |

The composer is not smaller than the patterns it replaces. It is general: no method of it names an
operation of either domain.

Two compositions differ from the patterns, and both are simpler:

- **A change guards its state in the write.** It changes the record only where the current state
  matches, instead of reading the state and checking it first. One component serves every change
  of one thing from one state, so accept and reject share it.
- **A claim forms its own identity.** Forming the wallet's identity is a step of claiming it, as
  forming a book's key already was.

One composition is still fitted: a change that may change identity (`change_identity`). It
composes blocks only, but its order of blocks is written for one shape of answer.
`on_identity_change` should select those blocks the way the other questions do.

ai_governance, held out from both, derives with the same twelve blocks. Its answers select `look up`
for the first time. The composer grew for new answer shapes, not new blocks: named checks, a
refusal that records and announces, a fixed identity, facts set on a record, and a condition with
another ending. `domains/ai_governance/FINDINGS_COMPOSER_RUN.md` has the detail.
