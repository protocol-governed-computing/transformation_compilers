## Response Style

Keep responses under ~400 output tokens. Prefer terse bullet summaries over prose narration. When a full document is needed, Write it to a file instead of printing it in chat.

## Document Authoring Rules

- Never include internal review notes, meta-scaffolding, work-order framing, cross-reference stubs, or 'Status:' metadata in deliverable docs or figures.
- Do not add dates to papers or appendices.
- An 'outline' means a clean reader-facing outline of the paper, not an execution plan.

# Transformation Compiler (PGC) — Architectural Rules

## What this repo is

The **governed Change Request → Protocol Artifact pipeline**, and it holds **two compilers**:

| Compiler | Transforms | Code | Registry | Subdomain |
|---|---|---|---|---|
| **Design Compiler** | problem → design | `transformation/design/` | `registry/design/` | `design` |
| **Construction Compiler** | design → protocol artifacts | `transformation/build/` | `registry/build/` | `build` |

A problem statement in business language is driven through gated phases into an **Authoring
Mandate**; construction then materializes the artifacts that mandate schedules. It began as a rehost
of RI-0's `pgs_change_mgmt`.

**The two are separate compilers because they fail differently.** A *design failure* is "the mandate
is incomplete or contradictory" — caught by a phase's rule set, fixed by re-authoring a register. A
*construction failure* is "the mandate was valid and did not uniquely determine an artifact" —
caught by Construction Completeness, fixed by amending the design language. Merging them would blur
two failure classes that different people fix, which is the distinction the split exists to keep.

The repo is named for what it holds, the two compilers. The lifecycle they serve keeps its own name:
the compiled domain is `transformation`, its artifacts are `transformation::…`, and the import
package is `transformation`. No identity is named after the repository.

- **Org:** `protocol-governed-computing`. **Repo:** `transformation_compilers`. **PyPI:**
  `pgc-transformation`.
- **Import package:** `transformation` — no `pgc_`/`protocol_` prefix inside; the org provides the
  namespace. Sibling convention: `protocol_compiler` → `compiler`, `snapshot_inspector` →
  `inspector`.
- Joins the release model at **release 4**; carries no earlier tag, correctly.

**Governed by `THE_SHAPE_OF_A_CHANGE_V0.md`, `doc/DESIGN_LANGUAGE.md` and
`doc/CONSTRUCTION_MAPPING.md`. Read them before writing code.** The language standard says what a
phase document is and how its rules are declared and evaluated; the mapping standard says how each
register field becomes an artifact field. The rulings that govern the module are restated here and
in the two standards.

## Build-time tool — CLI only

**No TI/TE boundary contract. No Operation Identity. Not reachable over transport.**

A boundary contract governs a *runtime* surface — a sealed snapshot serving a caller it does not
control. This tool is the other end of the lifecycle: it runs before a snapshot exists, its output
is authored artifacts a human gates, and its only reader is the person driving the change. An
Operation Identity would assert it is part of the executable composition, which is exactly what
"dossiers are evidence, not artifacts" exists to prevent. Transport stays reserved for `si.*`
inspection and runtime execution.

## The baseline is pinned

Validation runs against a **named, frozen snapshot**, never "the current snapshot". The pin is the
`baseline.json` beside the dossier: its `snapshot_id`, the domains it holds and its artifact count.

**A pin lives with its CR, not with this repo** — a CR dossier belongs to the domain it changes, so
its pin is `<domain>/cr_dossiers/cr_NN_<subject>/baseline.json`. A run that observes a different
`snapshot_id` **fails before executing a phase** — no phase may proceed against an unpinned or
mismatched baseline. Each CR pins the composition its predecessor produced.

Rebaselining is a deliberate, reviewed act: re-pin the id, re-approve the affected registers.
Never a silent drift — otherwise a regression is indistinguishable from a rebuild.

**A CR pins the composition without its own output.**
- The pin is the composition the change is designed *against*, never one that already holds what
  the change emits. For a domain's first CR that means without the domain.
- Pinned against a build that contains it, every `NEW` row the dossier declares reads as
  `*_ALREADY_EXISTS`, and P7 and P8 are refused.
- This bites the moment a CR is emitted and the default build picks it up. `assemble.sh` includes
  every domain with source, so the working `snapshot/` stops being a valid pin for that CR.

**How to take such a pin.** Take it with one side assembly, not by stashing and switching branches.
Name every compiled root except the domain's in `PGC_SOURCE_ROOTS`, and write the result aside with
`PGC_SNAPSHOT_OUT`:

```
PGC_SNAPSHOT_PROFILE=GOVERNANCE_SURFACE_PROFILE_V0 \
PGC_SOURCE_ROOTS=<every */snapshot/compiled root but the CR's domain, ':'-separated> \
PGC_SNAPSHOT_OUT=<scratch dir> ./snapshot_assembler/assemble.sh
tc baseline show --snapshot <scratch dir> > <dossier>/baseline.json
```

Then run the phase checks with `--snapshot <scratch dir>`.
- The assembler refuses a domain that has source but no compiled output, so the narrower set is
  always the one named, never one arrived at by accident.
- The side assembly's id is the composition's identity. It equals the pin exactly when nothing
  outside the CR has changed, which makes it the test for whether a pin is still current.

**A re-authored dossier is the exception.** When a dossier is re-authored against a composition
holding its own earlier output, its rows move to `EXTEND`, as described below. That is re-authoring,
chosen deliberately. It is not a pin taken from the wrong build.

## Why "transformation", not "change management"

**PGC evolution is never greenfield.** Every change transforms an existing composition: even a new
domain compiles against the platform's normative closure and composes into a snapshot that already
exists. The name states what the tool does.

This is not naming taste — it is the testability property. The pipeline's distinguishing logic
(REUSE / EXTEND decisions, placement, ownership, semantic preservation, roundtrip equivalence) is
meaningful only against a baseline. A greenfield run leaves all of it unevaluated while reporting
success, which is the vacuity failure this codebase has hit repeatedly.

## Snapshot access — the rule this repo exists to honour

**Every snapshot fact arrives through `inspector.api.query(operation, params, snapshot_root)`.**

A consumer that reaches into compiler internals and builds its own indexes is what
`snapshot_inspector` exists to remove.

- **MUST NOT import `compiler.*`**, or any compiler internal, ever.
- If a phase needs a fact the inspector does not publish, the answer is a **new `si.` operation** —
  not a reach into the compiler.
- Building this repo without a `compiler.*` import is the acceptance test for the inspection work.

## Phases, not stages

The transformation compiler is measured in **phases P0–P8**; `protocol_compiler` is measured in
**stages S1–S9**. Two words keep every piece of evidence clear about which pipeline produced it.
The rule is mechanical: a dossier has phases, a compilation has stages, and no document, path, register field
or identifier uses one word for the other.

**P0 is the seed phase**: human-authored business prose
(`0_business_problem_statement.md`) is faithfully rewritten into a template-conformant seed
(`0_seed_business_problem_statement.md`), which is what P1 consumes. P0 reorganizes; it must never
add business content, invent design, resolve a Clarification, or promote a System Belief to a
Business Truth. Gate 0 is a human confirming the seed says what they meant.

## The phase document

A phase document is Markdown with one `## Machine` YAML block. The block holds a `document` header,
`{phase, domain, subdomain, cr, rule_set}` plus `approval` on gated phases, and the `registers`. A
register is a list of rows keyed `snake_case`: `[]` declares it empty, `null` states nothing. Values
are typed: routing as a mapping, interfaces as `{in, out}`, a binding as a path, `{literal: v}` or
`{generated: true}`. A citation is a mapping naming the phase, register and row or key it cites.
The reader splits prose from the block and parses YAML. It applies no convention, and reads no table.

## Rules are declared, not coded

- **Each phase's rules are its register schema**, `registry/schema/REGISTER_SCHEMA_P<n>_V0.json`.
  Shape is JSON Schema keywords. Relations are four annotations (`x-key`, `x-reference`,
  `x-carriage`, `x-grounding`). What neither can state is a named procedure, one module each under
  `design/evaluate/procedures/`. A procedure parameter may name a vocabulary group with
  `{"x-vocab": {artifact, group}}` or a dispatched field with `{"x-dispatch": field}`; both resolve
  when the rule is sealed.
- **Every rule cites what it realises,** a `lifecycle::INVARIANT_…` or a statement in
  `DESIGN_LANGUAGE.md` §6.2. `tc phase meta` checks the closure.
- **A rule set is sealed into its phase workflow.** `tc phase emit --check` refuses sealed rules that
  differ from the schema unless a revision records the difference (`tc phase revise`).
- **A document, a verdict and an approval name the rule set that judged them.** A verdict reports
  `judged_by`: the schema `$id`, its revision and digest. An approval given under one `$id` stands
  unconfirmed under any other until a person re-confirms it.

## One live version per artifact

- **Meaning decides identity.** `transformation.build.sameness` compares two declarations by the
  rules `artifact::VOCAB_DECLARATION_REPRESENTATION_V0` declares. Same meaning keeps the identity.
  Changed meaning takes the next version never used, in the release, the live tree or the ledger,
  and names its predecessor in `supersedes`.
- **The predecessor is deleted, not kept.** Every deletion is recorded in
  `.github/process/retired_identities.yaml` with who decided and why. A deleted name is never reused.
  History is held by the release tag, the ledger, `supersedes` and git.
- **`single_instance_check` holds it:** no artifact name is live in two versions.
- **A workflow node's key is the live name of the contract it runs.** No node key spells a deleted
  version, even as a place.
- **Published identity is checked against the last release only.** Construction is stricter: it
  refuses any amendment that changes meaning, published or not, so a changed act takes its next
  version even when its current one was never released.

## Every transform carries test vectors

A capability transform is proven by a `TEST_DATA_<CT>` artifact: `target` names the transform, and
`cases` state what each case hands it and what it must return. `cases` is a data part
(`VOCAB_DECLARATION_REPRESENTATION_V0`), so a value written as a full name there is a value, not a
reference. The build manifest names `TEST_DATA` and `VOCAB`, so `compile_domain.sh` proves every
transform at each compile. P7 refuses a transform without cases.

A field that holds a structured value names its shape: `structure: transformation::STRUCTURE_…`, a
STRUCTURE whose `core.json_schema` is a JSON Schema. A full-name `$ref` is refused, so a structure
restates the parts it contains.

## Governance lives on the platform

A domain build cannot author an INVARIANT or a CONSTITUTION. So the lifecycle's governance is in
`software_governance/registry/lifecycle/`: `CONSTITUTION_CHANGE_MGMT_V0` for the design pipeline,
`CONSTITUTION_CONSTRUCTION_V0` for construction, and their `lifecycle::INVARIANT_…_V0`. An
invariant's `enforced_by` is prose, because a platform artifact cannot name a domain artifact. This
repository keeps the code and the tool domain: both compilers, the CLI, the transform
implementations, the phase and construction workflows, the judging contracts, intents and bindings.

## Designs of record

Every designed root carries one P7 and one P8 of record in `<root>/design/`: this repo's in
`design/`, each business domain's and the Collatz workload's in theirs. `python -m
transformation.record` writes them from the registry; `scripts/write_baseline_designs.py` writes all
of them, and its `--check` refuses a design the registry no longer generates.
`construction_acceptance.py` renders each and compares it with the registry.

A design of record is read by construction. It is not a phase document a rule set judges: it has no
P0 to P6 to cite. Every change after it is a dossier, judged in full, and once the change is built
the design of record is regenerated. The platform and the inspection surface carry none: the
platform's governance kinds are ones the design language cannot state, and the inspection contracts
are generated from their declaration.

## Determinism — where it applies, and where it cannot

A phase may use a non-deterministic worker. PGC stays deterministic and fail-hard:

- **Governed and deterministic:** the register schema, the structural oracle, the gates, the
  mandate. These decide admissibility.
- **Assistive and non-deterministic:** a worker drafting prose to populate a register.

A non-deterministic *drafter* behind a deterministic oracle and a human gate is coherent. A
non-deterministic *decision* inside a governed pipeline is not. Build the deterministic core first,
driven by hand-authored problem statements and registers; attach a worker only once the oracle is
proven. **No phase may depend on a worker existing** — P0's input is human-authored by definition.

Test fixtures pin the **register rows and the oracle verdict**, never authored prose — worker
output is not byte-reproducible, and a fixture that diffs it will be deleted within a week.

## Validation criteria are designed, not written after the build

A dossier proves its design determines its artifacts. It does not prove the composition does what
the business asked for, and only execution does that.
- A domain's execution validation dispatches real workflows against a fresh data root, one
  criterion per acceptance criterion.
- It is part of the change, not an afterthought to it.

**The criteria come from P0, and they are settled at design time.**
- Draw each criterion from the seed's acceptance criteria and `operation_refusals`, in the seed's
  own words, while P7 is being written.
- A criterion written after the build is written by someone who has watched the system behave, and
  it drifts toward what the system does.
- CLM's suite was written that way. One criterion expected a response a rule stopped to keep its
  partial words. The seed says the model "gives no response". The system was right and the check
  was wrong, and only rereading P0 told the two apart.

**Two readings are required before a criterion is accepted:**
- **the criterion against P0.** Does it say what the business said, no more and no less?
- **a failure against P0 before the design.** When a criterion fails, first ask whether the
  criterion misread the seed. Only then treat the failure as a defect in the design or the platform.

**Run one workflow as soon as artifacts exist.**
- A happy-path dispatch right after emit is the cheapest execution evidence there is.
- It is not a substitute for the suite. It catches what every phase check passes over: they read
  the declarations, and a defect in how declarations are sealed is invisible to them.
- CLM's routing collision passed P2–P8 at 100% construction completeness. The first dispatch found
  it.

**This is doctrine and nothing enforces it.** No template has a register for validation criteria,
and no rule checks one against P0. Until one does, this section is the check.

## A dossier is admitted on what it says, not on how it was written

The phase checks admit a document. They do not see how it was produced. CLM's P7 — 47 topology rows
and 280 bindings — and its P8 were written by generator scripts from P5 and P6, and every rule
admitted them exactly as it would have admitted the same text typed by hand.

**This is a stated limit, not a loophole to close quietly.** A generated dossier is permitted.
- **Keep its generator as evidence,** exactly as it ran: commit it with the dossier it wrote. Once
  the dossier is delivered, git holds the generator and the working tree does not. Only
  `transformation.record` stays, because designs of record are regenerated whenever a registry
  changes.
- **Say it was generated** in the dossier.
- **A generator is not a design authority.** Where it infers something no register states, the
  construction completeness measure is what catches it, and 100% is still required.

Making generation a governed step, or making the design language small enough to write by hand, is
open work.

## Dossiers are evidence, not artifacts

A dossier describes a change to a composition; it is not part of one. Dossiers **must not** enter
the snapshot as artifacts, and generated dossiers are gitignored. Authored dossiers are tracked.

**A delivered dossier's content is never edited.** A completed dossier is never re-judged against
today's composition: its pin names the composition it was designed against, and that composition
has moved on.

## Dossier layout

**A dossier lives with the domain it changes**, in that domain's repo — never centralized here. The
pipeline judges dossiers, it does not own them.

**Every domain transforms, so every domain repo may carry dossiers.** `platform` is the unspoken
genesis domain and is a domain like any other: it evolves, and its evolution is governed by the same
phases. So `software_governance`, `snapshot_inspector`, `conformance_workloads` and `transformation`
each hold their own, alongside the business domains. A change to the platform is not exempt from the
lifecycle for being foundational — being foundational is the argument for governing it.

**A business domain's dossiers are change requests and are numbered; a base-code domain's are not.**
A change to platform or base code is managed by git, so `cr_NN_` says nothing true about it and reads
as a sequence that does not exist. `cr_dossiers/cr_NN_<subject>/` is the business-domain form;
`dossiers/<subject>/` is every other domain's. The `CR:` header field remains in every dossier of
both kinds, because P1 *is* the Change Request phase whatever domain it runs against — the term is
the phase model's, not a claim about who raised it.

```
<business domain>/cr_dossiers/cr_NN_<subject>/   authored, tracked
<any other domain>/dossiers/<subject>/           authored, tracked
dossiers/<domain>/<subdomain>/                   generated, gitignored

  baseline.json                         the snapshot this CR is validated against
  p0_business_problem_statement.md      human-authored input
  p0_seed_<domain>_<subdomain>_v0.md    the seed
  p1_change_request_<...>_v0.md         one phase document: prose around one `## Machine` block
  ...                                   one document per phase reached, p0 to p8
```

Phase prefix is `p0..p8`, never `1_..8_` — filenames carry the phase/stage discipline too.
The Machine block's registers are the test assertion; the prose never is.

## When a change is a new CR, and when it is the same one re-authored

**A change request is expensive; re-authoring one is cheap.** Raising a second dossier for something
that belongs to the first is what makes the lifecycle bureaucratic rather than governing, and it
creates a hazard: an EXTEND is a whole redeclaration, so two in-flight dossiers each declaring one
artifact are two designs of record, neither complete, and emitting either silently reverts the other.
Nothing refuses that — construction compares an amendment against its *own* pinned baseline,
where the other change's additions do not yet exist.

**The test is artifact overlap, not judgement.** Read it from **P6's
`pps_artifacts_requiring_action`**, which every dossier carries and which enumerates exactly what the
change acts on. Not P7's `new_artifacts` and `existing_inventory`: those refine the same set, and a
governance change terminal at P6 has no P7 at all — anchoring the test there makes it unreadable for
precisely the dossiers most likely to overlap. So:

| the new subject | disposition |
|---|---|
| touches an artifact a dossier **in flight** declares | **child — do not raise a CR.** Revisit that dossier's problem statement and re-author it from P0 |
| touches an artifact a **delivered** dossier declares | **new CR.** It is a correction to delivered work, and a delivered dossier is never edited |
| touches nothing another dossier declares | **sibling.** Independent, raise it, work it in any order |

A child has no separation of concerns from its parent by definition — its subject is inside the
parent's. A sibling has one, which is what makes it workable alone.

**What re-authoring costs, stated so it is chosen and not stumbled into.** The parent's problem
statement grows, and every phase is re-judged. Where the parent's own artifacts are already in the
composition, re-pinning turns its `NEW` rows into `EXTEND` — the dossier stops recording that it
authored them, and only git remembers. That erosion accumulates across re-authorings.

**A defect that blocks an in-flight dossier is fixed in sequence, not as a child.** When a dossier
cannot pass a phase because the pinned rule set or construction is wrong, the fix cannot ride inside
it: the dossier is judged by the composition it is pinned to, and its own fix is not in that
composition yet. So the parent is parked at its last admissible phase, the fix runs as its own
dossier and is delivered, and the parent re-pins against the composition the fix produced. Its new
identities then shift past the fix's. This is not the overlap the child rule guards against: the two
are never in flight together, so there is never more than one design of record for an artifact.
`rule_effectivity` waited this way on `binding_literals` and `quoted_literals`.

**This is doctrine and nothing enforces it.** It should be a rule: a dossier whose P7 names an
artifact another in-flight dossier declares is a child, and refused. That rule would refuse the
second dossier at P7, before any consolidation is needed. Until it exists, this paragraph is the
only thing standing between the two, which is exactly the failure mode this repo keeps finding.

## Import rules (MANDATORY)

- Absolute, fully-qualified from `transformation.*`. No relative imports.
- **`inspector.api` is the only cross-repo import** — the inspection interface. No `compiler.*`,
  no `assembler.*`, no `runtime.*`, no `pgs_*`, no domain imports.
- No `sys.path` manipulation; roots are env-provisioned.
- No dynamic imports, reflection, or filesystem-based discovery.

## Workflow rules (MANDATORY)

Diagnose → plan → **get approval before multi-file changes.** Present the complete file list first;
one coherent change set, not scattered edits.

## Environment

Build against the workspace venv (`protocol-governed-computing/.venv`), never RI-0's. Three things
must hold: the active interpreter is that venv, every PGC package imports, and **no `pgs_*` package
is reachable** — a reachable one is a clean-break violation even when nothing imports it.

```bash
python -c "import sys, importlib.util as u
print(sys.prefix)
print([m for m in ('transformation','inspector') if u.find_spec(m)])
print('pgs_ reachable:', bool(u.find_spec('pgs_compiler')))"
```

Expected: the workspace `.venv`, both packages found, and `pgs_ reachable: False`.

## One-line summary

Problem statement → governed dossier → authoring mandate; snapshot facts only through
`inspector.api.query`; deterministic oracle and gates, assistive workers; **evolution is never
greenfield**, so validation is a change *sequence*, never a single build.
