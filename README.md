# transformation_compilers

**The governed Change Request → Protocol Artifact pipeline**, and it holds **two compilers**.

| Compiler | Transforms | Code | Registry |
|---|---|---|---|
| **Design** | problem → design | `transformation/design/` | `registry/design/` |
| **Construction** | design → protocol artifacts | `transformation/build/` | `registry/build/` |

They are two because they fail differently. A *design* failure is a mandate that is incomplete or
contradictory, and a phase's rule set catches it. A *construction* failure is a mandate that was
valid and did not uniquely determine an artifact — only the thing that renders can expose that, and
the repair amends the design language rather than one register. Merging them would blur two failure
classes that different layers repair.

The repository is named for the two compilers it holds. The lifecycle keeps its name: the domain,
the `transformation::` namespace and the import package are all `transformation`, and the PyPI
package is `pgc-transformation`. **`transformation` is not a third compiler.** Every rule it enforces is
declared as data.

A change begins as a plain-language problem statement and is driven through gated phases into an
**Authoring Mandate** — a complete, reviewable dossier — *before* any protocol artifact is written.
Only after the mandate is approved are artifacts authored, and the protocol compiler then governs
their admissibility.

```
problem statement → P0 → Gate 0 → seed → dossier P1..P7 → Gate 1 → P8 → Gate 2
     → construction → authored artifacts
     → protocol_compiler S1..S9 → snapshot_assembler → conformance → runtime → trace
```

This pipeline is measured in **phases (P0–P8)**; `protocol_compiler` is measured in **stages
(S1–S9)**. A dossier has phases, a compilation has stages, and nothing uses one word for the other,
so every piece of evidence says which pipeline produced it.

## How a phase judges a document

- **A phase document carries its facts as data.** Each is Markdown with one `## Machine` YAML block:
  a header naming the phase, the change and the rule set it is written for, then the registers as
  lists of typed rows. Prose around the block explains it, and nothing reads the prose.
- **A phase's rules are its register schema**, `registry/schema/REGISTER_SCHEMA_P<n>_V0.json`.
  Shape is JSON Schema. Relations between registers and phases are four annotations. What neither
  can state is a named procedure, one small module each. Every rule cites the platform invariant it
  realises, under `lifecycle::` in `software_governance`.
- **A verdict names the rule set that judged it.** The rules are sealed into each phase's workflow.
  `--rules sealed` (the default) judges by the rule set sealed in the composition, and
  `--rules declared` by the working tree's schema. A change to a rule is a recorded revision.
- **An artifact lives in one version.** A change of meaning takes the next version and names its
  predecessor in `supersedes`. The predecessor is deleted and recorded in the workspace ledger.
- **Every transform is proven by vectors** — a `TEST_DATA` artifact stating, case by case, what it is
  handed and what it must return.

`ARCHITECTURE.md` explains why; `doc/DESIGN_LANGUAGE.md` states each mechanism precisely.

## Install

```bash
pip install pgc-transformation
```

Once installed:

```bash
tc --help
```

## Build-time tool

`transformation` is **CLI only** — no TI/TE boundary contract, no Operation Identity, not
reachable over transport. A boundary contract governs a runtime surface served from a sealed
snapshot; this tool runs *before* a snapshot exists, its output is authored artifacts a human
gates, and its only reader is the person driving the change.

```bash
tc phase list                              # phases this build governs
tc phase check --phase p0 <seed.md>        # structural oracle — ADMISSIBLE / INADMISSIBLE
tc phase check --phase p1 <register.md>
tc phase check --phase p2 <register.md> --snapshot <root>   # grounds against the composition
tc phase check ... --rules declared        # judge by the working tree's schema, not the sealed set
tc phase template --phase p1               # the required section structure
tc phase rules --phase p1                  # the declared rule set
tc phase project <prior.md> --phase p1 --out <doc.md>       # phases that decide nothing

tc phase meta                              # do the rule sets themselves hold?
tc phase emit --snapshot $W/snapshot --check   # are the sealed workflows current?
tc phase revise p7 --change "<what, why>"  # record a rule change as a revision of its schema
tc phase diff p7 --from <pin snapshot>     # the rules that differ from a pin's, by rule identity

tc baseline show --snapshot <root>                 # the composition present, as a pin
tc baseline verify <pin.json> --snapshot <root>
tc baseline approve <pin.json> --phase p2 --by <who>

tc construction check <dossier> --snapshot <root>   # does the design determine its artifacts?
tc construction emit  <dossier> --root <domain>     # render them, at 100% or not at all
```

Two of these judge the pipeline rather than a dossier. `tc phase meta` asserts that every declared
rule can run and every implemented mechanism is declared — if that correspondence breaks, a verdict
over a document is meaningless, because a rule that cannot run reports green over a subject it never
evaluated. `tc phase emit --check` asserts the sealed copy of a rule set still agrees with the
generator that produces it; a rule added after a workflow was emitted once left 52 rules sealed
against 55 declared, and every run reported confidently on the smaller set. Both belong in a build.

`tc construction check` measures **determinacy** before anything is written: the fraction of the
facts the artifacts require that the design determines. Below 100% nothing is emitted, because a
generator choosing a value it was not given is a generator inventing one.

## The two loops

`$W` is the workspace root holding the sibling repos.

**After editing a dossier's P7 or P8** — skipping a step leaves the snapshot describing a design that
no longer exists:

```bash
D=$W/business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog

tc construction check $D --snapshot $W/snapshot
tc construction emit  $D --root $W/business_domains/book_library_mgmt

python $W/transformation_compilers/scripts/testbed/construction_acceptance.py
$W/protocol_compiler/compile_domain.sh $W/business_domains/book_library_mgmt
PGC_SNAPSHOT_PROFILE=GOVERNANCE_SURFACE_PROFILE_V0 $W/snapshot_assembler/assemble.sh
```

`--snapshot` is required whenever a design amends, replaces or re-points anything; without it
`check` and `emit` refuse. **A change of meaning is a new identity.** Each amendment — rendered, or
generated and previewed before it is written — is compared with the artifact the composition holds,
by the platform's declaration in `artifact::VOCAB_DECLARATION_REPRESENTATION_V1`: explanation is
ignored where it is text, a list declared unordered is a set, and a reference re-pointed to the
declared successor of what it named is the same reference. Any other difference is refused, and the
design authors a successor and `REPLACE`s the artifact instead. P7 refuses a withdrawal for the same
reason. A `REPOINT` row rewrites, in an artifact the design otherwise leaves alone, the names of what
the design replaces; every live artifact naming a replaced one must be `REPLACE`d, `EXTEND`ed or
`REPOINT`ed by the design, read from `si.artifact.refs`. Descriptions no register can state are
carried from the document being replaced, by `check` when it measures and by `emit` when it writes.

**Transforms carry their cases.** P7's `test_cases` and `test_case_values` state what a transform is
handed and what it must answer; construction renders them as `TEST_DATA` beside the transform, and
the runtime's conformance runs them. **A generated artifact is reached, not written:** a design names
its generator in `generation_provenance`, and `emit` invokes it. A domain's build manifest is one.

Construction run as a governed workflow writes into `data/`, never into the domain. **Promotion is a
separate, deliberate act**, and `tc construction emit` is that act.
A `tc construction build` CLI existed once and was removed, because it duplicated a governed path
with an ungoverned one.

A new capability transform is a protocol artifact *and* a Python implementation. Construction renders
the first; the second is hand-authored at
`business_domains/<domain>/implementation/capability_transforms/atoms/<code_lower>.py` with a
callable `execute(inputs, context)` raising `CTExecutionError`. A CT whose module is missing returns
nothing and its contract yields `VIOLATION` — while every check above still passes.

**After changing a phase's rule set** — the rules are declared in the phase's register schema,
`registry/schema/REGISTER_SCHEMA_P<n>_V0.json`, and *sealed* into that phase's workflow artifact.
Record the change as a revision first (`tc phase revise`). Editing
the declaration alone leaves `tc phase check` and the governed workflow evaluating different rule
sets:

```bash
tc phase emit --snapshot $W/snapshot --check           # names the drifted phase
python $W/transformation_compilers/scripts/emit_rule_sets.py --snapshot $W/snapshot   # re-seal
$W/protocol_compiler/compile_domain.sh $W/transformation_compilers
PGC_SNAPSHOT_PROFILE=GOVERNANCE_SURFACE_PROFILE_V0 $W/snapshot_assembler/assemble.sh
python $W/transformation_compilers/scripts/testbed/build_fixtures.py
python $W/transformation_compilers/scripts/testbed/build_payloads.py
```

Fixtures and payloads are **derived from the live dossier** — never hand-edit one; change the dossier
or the mutator in `build_fixtures.py`. A derived fixture cannot go stale silently, because the
derivation raises rather than producing a wrong one.

The fast inner loop is `python scripts/testbed/differential.py`, which drives the capability
transforms directly. It proves the rule sets and the check logic and nothing about workflow wiring;
`scripts/testbed/e2e_phases_test.py` boots the assembled snapshot and proves the wiring. Neither
substitutes for the other — a workflow that bound `$.capability_result.header` across nodes passed
the differential and failed immediately under the runtime.

From P1 a phase also needs its **priors**, or the handoff between phases goes unchecked:
P1←p0 · P2←p1 · P3←p2 · P4←p3 · **P5←p0** · P6←p5+p0 · P7←p5+p6+p0 · P8←p7. Each schema declares
its own in `x-priors`. P5 reads the seed, not P4: the
subdomain purpose is authored once at P0, has no register to travel in through P1–P4, and reappears
at P5.

## Why "transformation", not "change management"

**PGC evolution is never greenfield.** Every change is a transformation of an existing composition:
a new domain still compiles against the platform's normative closure and composes into a snapshot
that already exists. The name states what the tool does; `change_mgmt` named the process around it.

That property is also what makes the tool testable. Its distinguishing logic — REUSE / EXTEND
decisions, placement, ownership, semantic preservation, roundtrip equivalence — is meaningful only
against a baseline. A greenfield run exercises none of it.

## Relationship to the rest of the toolchain

```
protocol_compiler       source      → compiled projections
snapshot_assembler      projections → assembled snapshot
protocol_runtime        snapshot    → execution
snapshot_inspector      snapshot    → inspection
transformation           problem     → change request → authoring mandate   (this repo)
```

Every snapshot fact this pipeline needs arrives through
`inspector.api.query(operation, params, snapshot_root)`. It imports nothing from `compiler.*` and
builds no index of its own: a fact the inspector does not publish becomes a new `si.` operation.

## Validation is pinned

Runs are validated against a **named, frozen snapshot**, never "the current snapshot" — every
register a snapshot-reading phase emits encodes facts about one specific composition. A run that
observes a different `snapshot_id` fails before any phase executes.

Rebaselining is deliberate and has two halves. `tc baseline verify` proves the composition is the
one named; `tc baseline approve` records that someone re-read the registers asserting facts about
it. Which registers a phase owes is derived from its rule set — a register rests on a snapshot fact
exactly when a rule governing it consults an observation. The approval lives in the pin, so re-pinning
drops it: an approval is against one composition and survives no other.

## Documents

- `THE_SHAPE_OF_A_CHANGE_V0.md` — when a subject is a new change request and when it is the
  same one re-authored, and which artifacts a governance change may amend.
- `doc/DESIGN_LANGUAGE.md` — what a phase document is, and how each phase's rules are declared,
  sealed and evaluated.
- `doc/CONSTRUCTION_MAPPING.md` — how each register field becomes an artifact field, and under
  which provenance class.
- `registry/schema/` — the register schemas. **These are the authority**: registers, columns,
  controlled vocabularies, optionality and every rule are declared there. The templates in
  `transformation/templates/` are checked against them.

---

## The package family

| Package | Repository | Role |
|---|---|---|
| `pgc-compiler` | `protocol_compiler` | declarations → compiled projections |
| `pgc-assembler` | `snapshot_assembler` | projections → sealed snapshot |
| `pgc-runtime` | `protocol_runtime` | snapshot → governed execution |
| `pgc-inspector` | `snapshot_inspector` | snapshot → read-only inspection |
| `pgc-transformation` | `transformation_compilers` | change request → protocol artifacts |
| `pgc-governance` | `software_governance` | the governance surface and its capability implementations |
| `pgc-workloads` | `conformance_workloads` | the workloads that make conformance observable |
| `pgc-domains` | `business_domains` | the business domain implementations the composed snapshot binds |

`pip install protocol-governed-computing` brings in the whole family.

**Installing the toolchain is one of two steps.** The compiler resolves the governance surface from
`PGC_PLATFORM_ROOT` — fail-hard, cwd-independent, zero inference — so the *declarations* come from a
repository you point at, never from a wheel. A registry inside a package would be a second governance
surface competing with the repository's, and a build could then be governed by a stale copy.

```bash
git clone https://github.com/protocol-governed-computing/software_governance
export PGC_PLATFORM_ROOT=$PWD/software_governance
pgc            # reports what is installed and whether the anchor resolves
```

`PGC_DOMAIN_ROOTS` names an additional domain contributing its own `registry/structures` — the
directory that *directly contains* it, not the repository above it; pointing one level too high is a
silent no-op. `PGC_SNAPSHOT_PROFILES` is the directory holding snapshot profiles, required by the
assembler and the runtime alike.

**Where a build writes is declared, not supplied.** Each build configuration names its root in
`output_configuration.root`, and every layer's output consolidates there. The compiler does not read
`PGC_SNAPSHOT_ROOT`; the runtime does, with its own meaning — the assembled snapshot to execute.

`PGC_BUILD_ROOT` is accepted and reported and **nothing reads it**.

The full sequence, with the repositories it needs, is in
[`pgc_install`](https://github.com/protocol-governed-computing/pgc_install).

**Versioning.** Two schemes, and the published version follows the second.

- **Internal** — each repository's `VERSION` file, a monotonic composition ordinal. PGC versions the
  composition rather than each repo: they release together and the governance closure forces lockstep,
  so the ordinal names which composition a repo belongs to. Development happens on `dev/<N>` and each
  cycle is tagged `release-<N>`. This is not published.
- **Public** — `PUBLIC_VERSION`, tagged on every component repository. The platform is at **`v5`**.

**The published version is the public one: `v5` is `5.0.0`.** The standard the packages implement is a
separate artifact on its own track and is not this number.

The standard these packages implement is published separately: https://doi.org/10.5281/zenodo.22150616
