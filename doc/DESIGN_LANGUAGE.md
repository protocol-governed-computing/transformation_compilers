# The Design Language

This document specifies the language the design compiler judges: the form of a phase document, the
register schema that declares its shape, the rules a schema declares, and how they are evaluated.
An evaluator that implements what is written here judges a phase document as the design compiler
does, without reading the compiler's code.

What the rules realise is declared in the platform's governance surface: the lifecycle invariants
under `lifecycle::CONSTITUTION_CHANGE_MGMT_V0`. A named procedure that realises a property of the
composition rather than of design is specified here, by a statement (§6.2).

---

## 1. The phase document

A phase document is Markdown with one `## Machine` section. The section holds one fenced YAML block,
opened by a line `` ```yaml `` and closed by a line `` ``` `` that starts at column 0. An indented
fence inside a value closes nothing. Everything outside the block is prose, and no rule reads prose.

The block holds two keys:

- `document`: the header. It states what the document is and the rule set it was authored under:
  - `phase`: the phase, `p0` to `p8`;
  - `domain` and `subdomain`: what the change is to. A change to two subdomains lists both;
  - `cr`: the change;
  - `rule_set`: the `$id` of the register schema the document was authored under;
  - `approval`, in a gated phase: `{gate, rule_set, state}`, the gate a person closed, the `$id` it
    was closed under, and `APPROVED`, `MIGRATED` or `RECONFIRMED`.
- `registers`: one key per register the phase declares.

A document carries no lifecycle status. Its standing is its verdict.

A register's value is one of four things:

| Value | Means |
|---|---|
| a list of rows | the register states these rows |
| `[]` | the register is declared empty |
| `null` | the register is present and states nothing |
| a string | a text-only register |

A register absent from the block is missing. Missing, declared empty and stating nothing are three
different statements, and rules tell them apart.

A row is a mapping from column key to value. A column key is the column's title in `snake_case`;
`#` is keyed `number`. A value is text, or `null` when the row says there is nothing to state,
unless the schema types the column:

| Column type | Value |
|---|---|
| list | a list of names |
| routing | a mapping from outcome to target |
| interface | `{in: {…}, out: {…}}`, each a mapping from the capability's name to the design's |
| binding | a path string, `{literal: v}`, or `{generated: true}` (§1.2) |
| citation | a citation (§1.1), a list of several, or `null` for none |
| test value | any YAML value; a row that leaves the column out states no value |
| typed value | any YAML value: an interface field's default, an artifact property's value |

### 1.1 Citations

A citation names where a row came from:

| Form | Cites |
|---|---|
| `{phase: p2, register: gaps, row: 1}` | a row by its ordinal |
| `{phase: p4, register: gap_register, key: GAP-05}` | a row by what it says |
| `{phase: p3, register: placement_decision}` | a whole register |
| `{artifact: <identity>}` | an artifact in the pinned composition |
| `{source: human}` | a ruling only a human can make |

A citation without `phase` cites this document. The seed is `phase: p0`.


### 1.2 Values construction renders

A value construction renders is stated in one of these forms, and in no other. No form is read out of
text: a value means what its YAML type says.

| Form | Where | Renders as |
|---|---|---|
| a path, `payload.title` | a step's binding | the runtime's binding expression, `$.payload.title`. A path starts at `payload`, `results`, `inputs`, `capability_result` or `result_status`; in a molecule also at `iterator` or `accumulator` |
| a path, `surface.record.grounds` | a boundary's binding | the path, as written |
| `${input.KEY}` | a boundary's binding | the token, as written: the boundary substitutes it |
| `{literal: v}` | any binding | `v`, of its own type: `30`, `false`, `[a, b]`, `""` |
| `{generated: true}` | any binding | the word `generated`; the generator its owner names supplies the value |
| a typed value | a default, a property value | itself: `30` is a number, `false` a flag, `'30'` text |

`scripts/testbed/render_vectors_test.py` pins each form.
---

## 2. The register schema

Each phase declares its document's shape in a register schema: a JSON Schema (draft 2020-12) file
with an `$id`, `transformation.schemas.REGISTER_SCHEMA_P<n>_V<k>`. The meta-schema
`SCHEMA_REGISTER_SCHEMA_V0` closes the surface: a keyword the evaluator does not implement is
refused when the schema is read, so a schema never says more than is enforced.

A schema declares:

- **Registers**, under `properties.registers.properties`. A table register is an array of rows; a
  text register is a string. `minItems: 1` means the register may not be empty. `x-section` names the
  document section it sits in. `x-business-language` names the columns that must hold business
  prose, or `true` for every column but the citing ones.
- **Columns**, under each register's `items.properties`. A column has a `title`, the type of its
  value (§1), and optionally `x-vocab: {artifact, group}`, a group of a `VOCABULARY` artifact its
  value must belong to. A vocabulary is referenced, never copied. A type several columns share is
  declared once under `$defs` and named by `$ref`.
- **The handoff**: `x-consumes` and `x-emits`, and `x-priors`, the earlier phases a document is
  judged against.
- **Observations**: `x-observations`, the inspection operations whose results the procedures read,
  each under the key it is read by.
- **Declared rules**: `allOf`, an ordered list (§4).

Which schema judges which phase is declared once, in
`transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0`. A row there names a phase, its schema's
`$id`, the workflow its rule set is sealed into, and the template its documents are authored from.
A procedure parameter written `{"x-dispatch": <field>}` reads as that field of every phase, keyed by
phase, so a schema never copies the dispatch. One written `{"x-vocab": {artifact, group}}` reads as
that vocabulary group's entries, so a schema never copies a vocabulary.

### 2.1 Rule identity

Every rule has an identity: its schema's `$id`, `#`, and a JSON Pointer to where the rule is
declared. No two rules of a rule set share one.

- A declared rule is the entry it decodes from: `#/allOf/<i>`.
- A derived rule (§3) is the keyword it expands, where the schema has one: `minLength`,
  `minItems`, `items/required`, `x-business-language`, or a column's `x-vocab`. A header rule is
  `/properties/document/required`, or the field's `const`, `pattern` or declaration.
- A derived rule with no keyword of its own is named after the declaration it derives from, followed
  by `x-derived/<check>`. A register's base is `/properties/registers/properties/<register>`; a
  column's is that, followed by `/items/properties/<key>`.

### 2.2 Closure

The rule sets close over the governance they realise:

- every `x-realises` names an invariant the design constitution,
  `lifecycle::CONSTITUTION_CHANGE_MGMT_V0`, names, or a statement in §6.2;
- every invariant that constitution names is realised by some rule. A derived rule realises what its
  check states: the citation checks realise `ROW_PROVENANCE_CITED`, and the business-language check
  `PHASE_SPEAKS_ITS_RUNG`;
- every check kind is used, and every rule's kind exists;
- every template names exactly its schema's registers, with the same columns;
- every rule set is the last revision its schema records (§2.3).

### 2.3 Effectivity

A rule set is named by its schema's `$id`. A change to the rules declares its own effectivity:

- **A change that can alter a prior document's admissibility is retroactive.** It takes a new `$id`:
  a new schema file, named in the dispatch, whose revisions start again at 1.
- **Any other change is a revision.** `x-revisions` lists them, oldest first, each as
  `{revision, retroactive: false, change, digest}`. `tc phase revise` records one.
- **The digest** is the SHA-256 of the rule set the schema expands into, in order, each rule read as
  its `id`, `identity`, `check`, `register`, `params` and `intent`.
- **A rule set whose digest is not its last revision's is refused,** as `REVISION_UNRECORDED`, by
  the emission and by the closure check. It is never sealed.

A verdict names the rule set that rendered it as `judged_by`: the `$id` its rules carry in their
identities, the digest, and the revision that records the digest. It also names the rule set the
document was authored under, when that differs.

An approval is given under one `$id`. Under that `$id` it stands confirmed. Under any other it stands
unconfirmed until a person re-confirms it. A revision never unconfirms an approval, because it
alters no document's admissibility.

`tc phase diff` names the rules that differ between two rule sets, by identity: added, removed and
changed.

---

## 3. Rules derived from shape

Every schema expands into these rules. The header rules come first, from `properties.document`.
Then come these rules, in this order, for each register the schema declares. None needs an entry in
`allOf`.

| Finding | Refuses |
|---|---|
| `HEADER_FIELD_MISSING` | a header that does not state a required field |
| `HEADER_FIELD_MISMATCH` | a `phase` other than the schema's, or a `rule_set` of another phase |
| `HEADER_FIELD_NOT_OF_TYPE` | a stated header field not of its declared form, such as an approval in no declared state |
| `REGISTER_MISSING` | a declared register absent from the block |
| `REGISTER_EMPTY` | a text register with no text, or a register declared non-empty with no rows |
| `REGISTER_COLUMN_MISSING` | a row lacking a required column |
| `CELL_NOT_IN_VOCABULARY` | a value outside its column's vocabulary group |
| `CELL_NOT_OF_TYPE` | a value that is not of its column's type |
| `DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE` | an artifact code in a business-language column |
| `ROW_WITHOUT_SOURCE_FINDING` | a row whose citation is `null` or absent |
| `SOURCE_FINDING_UNRESOLVED` | a row none of whose citations names a register the phase may cite, the seed, a ruling or an artifact |
| `CITATION_ORDINAL_UNRESOLVED` | a citation naming a row past the end of the register it names |

Each derived rule's identity is given in §2.1.

A citation is resolved in the phase it names, or in this document when it names none. A register
in a prior that was not supplied is not read, and is not reported.

---

## 4. Declared rules

`allOf` is an ordered list. One entry is one rule, and the order is part of the rule set's meaning:
a sealed rule set is compared as a list.

Every entry carries:

- `x-finding`: the finding `code` an author reads, the rule's `intent`, and its `detail` text when it
  has one. A code is shared by every rule that finds the same kind of defect.
- `x-register`: the register it governs, unless it is about the whole document.
- `x-realises`: the invariant it realises, or the statement that specifies it. Required of every
  annotation and procedure.
- `x-columns`: the titles of columns it names that the register does not declare, which must be
  absent.

An entry states one of three things: a constraint (§4.1), an annotation (§5), or a procedure (§6).

### 4.1 Constraints

A constraint is written in this subset of JSON Schema, and nothing else:

| Keyword | Where | States |
|---|---|---|
| `minItems` | entry | the register has at least this many rows |
| `maxItems` | entry | the register has at most this many rows |
| `items.properties.<k>.minLength: 1` | entry | the column states a value |
| `items.properties.<k>.pattern` | entry | a text value in the column matches the pattern |
| `items.properties.<k>.not.pattern` | entry | no text value in the columns contains the pattern |
| `items.required` | entry | every row carries the column |
| `items.not.required` | entry | no row carries the column |
| `items.not.properties.<k>.const` | entry | no row holds this value in the column |
| `items.if` / `items.then` | entry | the constraint in `then` binds only the rows `if` selects, by `const` or `enum` on one column |

A pattern constrains text. A typed value, or a cell stating nothing, is not matched. A pattern is
anchored at the start of the value.

### 4.2 From a failing keyword to a finding

A constraint that fails yields one finding per row it fails on, or one for the register. The finding
carries the entry's code and intent. Its place is the register and the row. Its detail is the entry's
`detail`, with `{value}` replaced by the failing value, or `{token}` by the matched text, where the
detail names it.

---

## 5. Annotations

An annotation relates rows to other rows. It carries a `mode` and the `params` the mode reads.

### 5.1 `x-key`

| Mode | States |
|---|---|
| `unique` | no two rows carry the same value in the key's columns, compared on the bare identity |
| `contiguous` | the key's numbers run from 1 without a gap |

### 5.2 `x-reference`

| Mode | States |
|---|---|
| `resolves` | each value in the column names a row of the target register, optionally only for rows a gate selects |
| `covers` | each row of the target register is named by some row here |

### 5.3 `x-carriage`

Carriage relates this document to a register of a prior phase.

| Mode | States |
|---|---|
| `present_by_key` | each prior row reappears here, matched on its key columns |
| `confined` | each row here appears in the prior register |
| `cited` | each prior row is cited by some row here |
| `matches_cited` | a row citing a prior row states what that row stated |
| `identities_covered` | each identity the prior declares appears here |
| `prose` | the prior's text register is carried here |

A prior that was not supplied is reported once, as unchecked. A register missing from a supplied
prior is reported as the prior's defect.

### 5.4 `x-grounding`

Grounding relates the document to the pinned composition.

| Mode | States |
|---|---|
| `exists` | each identity the column claims exists in the composition |
| `absent` | each identity the column declares new does not |
| `reuse_eligible` | each reuse candidate comes from a domain that permits reuse |

---

## 6. Procedures

A procedure is a named check the general language cannot state as one rule:
`x-procedure: {name, params}`. Each is specified outside the code that runs it.

### 6.1 Specified by an invariant

| Procedure | Realises |
|---|---|
| `DISCHARGE_GROUNDED_IN_TOPOLOGY` | `BUSINESS_REFUSAL_DISCHARGED` |
| `DISCHARGE_OUTCOME_REFUSES` | `BUSINESS_REFUSAL_DISCHARGED` |
| `GOVERNING_RULE_IN_SEALED_SET` | `BUSINESS_REFUSAL_DISCHARGED` |
| `EMISSION_GROUNDED_IN_ENDING` | `ANNOUNCEMENT_FROM_COMPLETING_ENDING` |
| `READ_IS_DECLARED` | `REACH_DECLARED_AND_USED` |
| `REACH_IS_USED` | `REACH_DECLARED_AND_USED` |
| `DEPENDENCY_PRECEDES` | `BUILD_ORDER_TOPOLOGICAL` |
| `STEP_BINDINGS_MATCH_INTERFACE` | `DESIGN_NAMES_RESOLVE` |
| `CONTRACT_OUTPUT_PRODUCED` | `DESIGN_NAMES_RESOLVE` |
| `CELL_PREFIXED_BY_COLUMN` | `DESIGN_NAMES_RESOLVE` |
| `IMPLEMENTATION_MODULE_CONFORMS` | `DESIGN_NAMES_RESOLVE` |
| `UNRESOLVED_MARKER_ABSENT` | `NO_QUESTION_LEFT_OPEN` |

Each invariant is `lifecycle::INVARIANT_<name>_V0`.

### 6.2 Specified by a statement

These check properties of the composition a design will produce. Two anticipate a refusal the
protocol pipeline already makes. Twelve check a property nothing in the protocol pipeline refuses:
the design compiler is their only enforcement, until the protocol declares them.

#### STEP_OPERATION_PUBLISHED

A step names an operation its capability offers. A capability absent from the composition's
surface is reported, not skipped. The compiler refuses the same step at S4.

#### TOPOLOGY_ROUTE_RESOLVES

Every routing target is a node of the same workflow, or an ending. A target is a node's key, not a
contract. A route to a place the design does not redeclare resolves against the composition's
workflow. The build refuses an unresolved route when it verifies the dispatch.

#### BINDING_SOURCE_REACHABLE

A source rooted at another node names a node the workflow runs.

#### BINDING_SOURCE_PUBLISHED

An output binding reads a field the step's operation publishes.

#### STEP_INTERFACE_CONFORMS

A transform step hands its transform only the inputs the transform declares, and reads only the
outputs it answers, as the step's interface maps them.

#### NODE_INPUT_BOUND

A workflow node is handed every input its contract requires. An optional input left unbound is a
declaration that the node does not supply it.

#### ENTRANCE_SUPPLIES_GATE

An entrance supplies every field the gate of the workflow it invokes requires. The gate is the
workflow's `IN` node where the design states the topology, and otherwise the intent the composition
declares for it.

#### STEP_INPUTS_BOUND

Every input a step consumes is bound.

#### STEP_CONSUMES_PUBLISHED

A side-effect step hands its operation only fields the operation accepts.

#### CONSUMPTION_GROUNDED_IN_OPERATION

A side-effect step that consumes nothing invokes an operation that takes no input.

#### STORE_GROUNDED_IN_CAPABILITY

A step names a store exactly when its capability keeps records.

#### CROSS_SUBDOMAIN_REACH_READ_ONLY

An act reaching into another subdomain only reads what that subdomain holds. Whether an operation
writes is read from the operation's published `effect`, never from its name.

#### OUTCOME_GROUNDED_IN_OPERATION

A step branches only on outcomes its operation answers, or names the transform that interprets
the observation and the status that interpretation yields.

#### INTERPRETATION_TRANSFORM_REFUSES

A transform named to interpret an observation can refuse it: it raises, rather than returning its
judgement as a value.

---

## 7. Findings and verdict

A finding carries:

- `code`: the kind of defect, shared by every rule that finds it;
- `rule`: the identity of the rule that found it (§2.1);
- `locator`: where it is, as `{register, row, field}`. `row` is the row's ordinal, or the key a row
  is named by where the rule reads named places. `field` is the key of the column the rule is about.
  What the finding cannot place is `null`. A finding about the header has the register `document`
  and the field it is about; one about the whole document has the register `document` and no field;
- `detail`: what is wrong, in the author's terms;
- `intent`: why the rule exists.

A document is `ADMISSIBLE` when no rule finds anything, and `INADMISSIBLE` otherwise.

---

## 8. Evaluation semantics

- **Every rule is evaluated,** in its sealed order. There is no short-circuit and no warning tier.
  An author needs the whole finding set, and a rule that never runs cannot be trusted.
- **The rule set is always supplied.** An evaluator has no default rule set: a default would judge
  one phase's document by another phase's rules.
- **An unknown rule kind fails the evaluation.** A rule skipped reports nothing over a subject
  nobody judged.
- **Emptiness is declared, never inferred.** `[]` and `null` are statements; an absent register is a
  finding.
- **An unsupplied prior differs from a missing register.** The first is the caller's omission and is
  reported as an unchecked handoff. The second is the upstream author's defect.
- **The composition is observed, never read directly.** Every fact about the pinned composition
  arrives through the inspection interface, as the observations the schema declares.

---

## 9. The derive route

The derive route derives a P7 design intent from a decision ledger. It is the Design Compiler's
second route to a design. The phases judge a design that a person writes. The derive route composes
a design from typed business answers. `tc phase derive` runs it, and `transformation/design/derive/`
holds it.

### 9.1 Where the ledger sits

The ledger replaces the authored P4 to P7. It leaves P0 and the discovery phases in human hands.

| Phase | With the ledger |
|---|---|
| P0 | Authored, unchanged. The seed is the brief the owner answers from. The route also projects a seed from the ledger (§9.6). |
| P1 to P3 | Discovery, in dialog. It ends in ledger answers, and in a new question type when the catalog lacks one. |
| P4 to P6 | Held by the ledger's closed shapes: the consolidation, the WHAT and the WHERE. |
| P7 | Derived. |
| P8 | Unchanged. The route splices the derived design into the mandate. |

A person approves the ledger at the P7 gate. The gate sees the ledger, the derived design and the
trace from one to the other. The gate approves decisions, not the rows derived from them.

A change that needs a question the catalog lacks is a discovery change. It runs P1 to P3 and adds
the question type to the catalog. Any other change is a ledger delta.

The route projects every phase document from P0 to P6 (§9.6).

### 9.2 The ledger

A ledger holds answers in closed shapes (`ledger_schema.yaml`). Each shape names the catalog
question it answers (`catalog.yaml`). The route refuses an answer outside its shape. It never
interprets one.

- **Every answer cites its authority.** Its `from` names a seed, the brief or the owner.
- **An open question holds back what depends on it.** An `open` entry names a catalog question, the
  operation it is about and who it waits on. The route derives nothing for that operation, and
  admission refuses it.
- **A case states an outcome in domain words.** The route checks that it names an operation. It
  derives nothing from it.

### 9.3 Derivation

The route composes each operation from twelve building blocks, in the order the doctrine sets
(`doctrine.yaml`).

- **The doctrine is sealed.** The doctrine, the ledger schema and the catalog each carry an `$id`,
  revisions and a digest. The route refuses to derive while any of them differs from its last
  revision. Every derived design names all three as its `judged_by`.
- **Each doctrine rule realises an invariant.** Its `realizes` names a `lifecycle::` invariant that
  `CONSTITUTION_CHANGE_MGMT_V0` puts in force. `tc phase derive meta` checks that each resolves.
- **Every derived row traces.** A row's `_from` names a ledger answer, a doctrine rule or the
  carried surface. The route refuses a row that names no source, or a source that holds nothing.
- **Meaning decides identity.** The route compares each derived artifact with the one the composition
  holds, by `sameness`. An artifact with the same meaning keeps its identity (EXTEND). One with a
  changed meaning takes the next version never used, and supersedes its predecessor. An operation's
  `replaces` answer names the operation it takes the place of. An artifact the ledger no longer
  derives is retired (RETIRE).

### 9.4 The carried surface

A derived design keeps the names its callers and its data already use. The route carries:

- store names and paths;
- binding (RB) names;
- entrance (IN) names and request shapes;
- trail record keys;
- the output names a read returns.

The route matches a store by its exact name, by the words a registry holds, or as the part's one
trail.

A ledger changes a carried name only through an answer that states the change. Today one answer
does: `replaces`, for an operation. A ledger cannot yet rename a store or a field. Such a change is a
migration, and it runs as an authored dossier.

### 9.5 Changing the route

A change to the doctrine, the ledger schema, the catalog or a building block changes every derived
design at once.

- **A sealed document records a revision.** `tc phase derive revise` records it, with the digest it
  produced.
- **It runs as its own dossier,** `dossiers/<subject>/` of this repository, whose `change.md` says what
  changed and why.
- **The route is sealed whole.** `tc phase derive seal <dossier>` takes the digest of every module of
  `transformation/design/derive/` and every sealed document. It re-derives every ledger in
  `testbed/ledgers/` against its domain's design of record, and records both in the package's
  `route_seals.yaml` under the dossier's name.
  - Each re-derivation's outcome is recorded. An unchanged design of record keeps every artifact;
    a changed one is delivered as a change request.
- **A route no seal records derives nothing.** A derivation is refused, and `judged_by` names the seal
  it ran under. `tc phase derive meta` also refuses a seal whose dossier has no `change.md`.
- **The workspace regression builds each ledger** and compares the result with its expected outcome.

### 9.6 The phase documents

`tc phase derive project <ledger> <baseline> --design <generated.json> --snapshot <dir> --out <dir>`
writes the phase documents between the ledger and the design. `tc phase check` judges each one by the rule set that governs an authored
document of its phase. No rule is relaxed for a projection. A projection that fails a rule is a
fault in the projector.

| Document | Projected from | Each row cites |
|---|---|---|
| P0 seed | the ledger | nothing: the seed is where the owner's answers enter |
| P1 change request | P0, by the existing P1 projection | the P0 row it restates |
| P2 domain model | P1, the baseline design, the derived design and the snapshot | the P1 row it models |
| P3 analysis loop | P2, and the identity decisions | the P2 row it resolves |
| P4 business model | P3 | the P3 row it consolidates |
| P5 business intent | P0 | the P0 row it restates |
| P6 governance intent | P5, and the baseline design for an existing binding | the P5 row it places |

- **The owner's words are carried, never rewritten.** The ledger states the domain's purpose, each
  part's purpose, why each thing is kept (`why`) and what is out of scope. The projection carries
  each one word for word.
- **Everything else is said from structure.** Identity, states, refusals, events and the trail
  become sentences. A sentence states only what its answer states.
- **A projected document proves the projection.** P5 cannot fail to carry P0's purpose, because it
  was built from it. The rules that catch a hand-made P5 still run, and changing a projected
  document makes them fire.
- **Discovery restates what the derivation observed.** P2 to P4 are projected after identities are
  decided. They name what the baseline holds, what is kept, changed, new or retired, and what each
  reused platform artifact is for and how far a change to it reaches, as the inspector reads it.
  `tc phase check` grounds every name against the snapshot. Business columns name artifacts in
  words; the codes go in the evidence.
- **An open question holds back its operation** in every document as in the design. The seed lists
  the operation as out of scope, with the question it waits on.

### 9.7 Delivering a change

`scripts/derive_deliver.sh <domain> <cr dir>` delivers a change the route designed. The change is a
dossier, `<domain>/cr_dossiers/cr_NN_<subject>/`, whose `ledger.yaml` is the decision. The script
pins `baseline.json`, derives P7 and P8, projects P0 to P6 and refuses to go on unless all seven are
admissible. It then checks construction, emits, deletes what the design superseded, replaced or
retired, records each deletion in `retired_identities.yaml`, repoints the domain's testbed and
client to successors, compiles, assembles and regenerates the design of record.

- **The criteria come first.** The change's `criteria.yaml` names the suites that hold its acceptance
  criteria. Delivery runs them against the composition the change is designed against, before it
  derives (`criteria_before.txt`), and refuses unless one fails there: criteria the composition
  already meets do not tell the change apart. After delivery every criterion must hold
  (`criteria_after.txt`). `scripts/criteria_run.py` dispatches each act the suite names to the
  version of it the composition holds. `scripts/criteria_before.sh` runs a delivered domain's
  criteria against the domain at an earlier revision.
- **One decision, one change.** A ledger that adopts the derived design keeps the behavior the
  design of record has, where the ledger can state it. Each later owner decision is its own change,
  a delta to the previous change's ledger.
- **What the ledger cannot state in its earlier form is named.** Adopting the route can correct
  behavior no ledger shape reproduces. The first change names each such correction.
- **A delivered domain is a fixed point.** The composer names artifacts at V0 and maps each to the
  version the design of record holds, with that version's lineage. It reads the trail's form from
  the design it wrote as well as from a hand-authored one. Re-deriving the last change's ledger
  keeps every artifact. Three rules keep this true:
  - A `replaces` answer is spent once delivered: the operation's workflow is on the chain of
    successors of the first workflow it names. The chain is read from the retirement ledger and the
    design's lineage, because a design of record names only each artifact's latest predecessor.
  - A new act's trail records the request fields its own chain binds, as it will once the act
    exists.
  - A suite dispatches the successors the derivation, the design's lineage and the retirement
    ledger declare, followed to the last version.
- **A domain may need only one change.** ai_governance's owner answers all follow from one ruling,
  that the business holds its own facts. The ledger cannot state the earlier design otherwise, so
  cr_04 delivers them together, and its delivery record names each difference.
- **Identity follows references as construction does.** A kept artifact is compared again with its
  successors' names in place. A reference that follows its successor keeps its meaning; a renamed
  place, such as a workflow node, does not.
