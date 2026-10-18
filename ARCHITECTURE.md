# Architecture — `transformation_compilers`

This document describes what this repository is, what it owns, and what it must never do. It is
written to be read before any code, and assumes no prior familiarity with Protocol-Governed
Computing.

For the big picture — what PGC is and how the repositories compose — see
**https://github.com/protocol-governed-computing**.

---

## 1. What this repo is

This is how the system **changes**. Everything else in the composition governs what the system does;
this governs how it becomes something else.

> A change begins as a sentence someone in the business says, and ends as artefacts that compile.
> This repository is the graded path between those two things, and it refuses to let a step be
> skipped.

It holds two compilers. The first drives a problem statement through gated phases until it becomes
an **authoring mandate** — a design complete enough to build from. The second measures whether that
mandate actually determines the artefacts it schedules, and then writes them.

**What this repo is not.** It is not a project-management tool, not a document generator, and not
part of the running system. It executes before a snapshot exists, its output is authored artefacts a
human approves, and its only reader is the person driving the change.

## 2. Where it sits

```
                    ┌──────────────────────────────────────────┐
                    │  transformation      ← YOU ARE HERE      │
   a business       │                                          │     artefacts
   problem  ───────▶│   design/   problem  → mandate           │───▶  in a domain
   in prose         │   build/    mandate  → artefacts         │      repository
                    └──────────────────┬───────────────────────┘             │
                                       │ reads facts about                   │
                                       │ the current system                  ▼
                              snapshot_inspector              compiler → assembler
                                       ▲                                     │
                                       └──────── sealed snapshot ◀───────────┘
```

Note the loop. The mandate is judged against the snapshot the system currently *is*; the artefacts it
produces are compiled into the snapshot the system will *become*. **Evolution is never greenfield**
— even a brand-new domain compiles against a normative closure that already exists.

That is not a philosophical point. The pipeline's distinguishing logic — whether to reuse or extend,
where something belongs, who owns it, whether meaning was preserved — is only meaningful against a
baseline. A greenfield run leaves all of it unevaluated *while reporting success*.

## 3. The central idea: the language widens as you descend

The distinction that explains every design choice in this repository:

```
   PHASE                     VOCABULARY ADMITTED               so that…

   p0  change seed      ┐
   p1  change request   │
   p2  domain model     ├──▶  business language only     the business can read and
   p3  analysis loop    │                                correct its own problem
   p4  business model   ┘
   ─────────────────────────────────────────────────────────────────────────────
   p5  business intent  ────▶  + provisional names       WHAT must be true
   p6  governance intent ───▶  + placement               WHERE it belongs
   p7  design intent    ────▶  + bindings, paths, FQDNs  HOW it is realised
   p8  authoring mandate ───▶  + build order             IN WHAT ORDER
```

Each phase admits a strictly wider vocabulary than the one before, and **nothing may be said early
that belongs late**. A problem statement containing a module path has already decided the design
before anyone examined the problem — and the phase's rule set refuses it. Nine phases, 992 declared
rules, all of them checkable.

Three gates are human, and only three: **Gate 0** after p0, where the business confirms the seed says
what it meant; **Design Approval** after p7; and **Mandate Approval** after p8, at which point the
dossier is locked. A change to the governance surface ends at p6: constitutions and vocabularies are
authored, not constructed, so it has no design for construction to read.

### Why two compilers rather than one

They are separate **because they fail differently**:

| | failure reads as | fixed by |
|---|---|---|
| **Design Compiler** | *the mandate is incomplete or contradictory* | re-authoring a register |
| **Construction Compiler** | *the mandate was valid and did not determine an artefact* | amending the design language |

Different people fix those, and merging the compilers would blur the two into "it didn't work".

## 4. Everything that decides is data

Nothing a phase decides lives in code. A reader can learn every rule without opening a Python file.

**A phase document carries its facts as data.** It is Markdown with one `## Machine` block. The block
holds a header naming the phase, the change and the rule set it is written for, and the registers as
lists of typed rows. Prose sits around the block and explains it; nothing reads the prose.

```yaml
document:
  phase: p3
  domain: transformation
  cr: new_subdomain
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: 'S2 gaps #1'
    finding: Judging a document is three mechanisms …
    evidence_status: OBSERVED
    resolution_status: CLOSED
```

**A phase's rules are its register schema.** Each phase has one JSON Schema in `registry/schema/`.
Shape — presence, required cells, patterns, vocabularies — is plain JSON Schema. Relations between
registers and with earlier phases are four annotations: a key, a reference, a carriage from a prior
phase, and a grounding against the composition. What neither can state is a named procedure, one
small module each. Every rule cites the platform invariant it realises:

```json
{
  "x-register": "known_facts",
  "x-finding": {
    "code": "SEED_ROW_NOT_CARRIED",
    "intent": "P0 reorganizes and P1 restates; neither may drop what the business said"
  },
  "x-realises": "lifecycle::INVARIANT_UPSTREAM_COMMITMENT_CARRIED_V0",
  "x-carriage": {"mode": "present_by_key",
                 "params": {"prior_phase": "p0", "prior_register": "known_facts",
                            "prior_key_column": "Fact", "key_column": "Fact"}}
}
```

**The invariants live on the platform.** A domain cannot author an invariant or a constitution, so
the lifecycle's governance is `software_governance/registry/lifecycle/`:
`CONSTITUTION_CHANGE_MGMT_V1`, `CONSTITUTION_CONSTRUCTION_V1`, and the invariants they name. This
repository keeps the code that enforces them.

**A rule set is sealed, and a verdict names it.** A phase's rules are expanded from its schema and
sealed into that phase's workflow. A document names the rule set it was written for; a verdict names
the rule set that judged it, with its revision. A change to a rule is recorded as a revision of its
schema. An approval given under one rule set stands unconfirmed under another until a person
re-confirms it.

## 5. What it owns, and what it must never do

**It owns:**

- **the register schemas** — what each phase's document must contain and what it may not say yet;
- **the evaluator** — the deterministic judge that renders a verdict on a document;
- **the pinned baseline** — the named, frozen snapshot every claim is verified against;
- **construction completeness** — the measurement of whether a design determines its artefacts;
- **sameness** — whether an amendment keeps an artefact's meaning, by the rules the platform declares;
- **emission** — writing the artefacts a mandate schedules into the domain that owns them.

**It must never:**

- **reach into the compiler.** Every fact about a snapshot arrives through the inspector's query
  interface. If a phase needs a fact the inspector does not publish, the answer is a **new inspection
  operation** — never a private index built from compiler internals. Building this repository without
  a compiler import is the acceptance test for that whole separation.
- **be reachable over transport.** No boundary contract, no operation identity, CLI only. An
  operation identity would assert this tool is part of the executable composition, which is exactly
  what "dossiers are evidence, not artefacts" exists to prevent.
- **put a dossier in a snapshot.** A dossier describes a change to a composition; it is not part of
  one.
- **own the dossiers it judges.** A dossier lives with the domain it changes, in that domain's
  repository. The pipeline judges; it does not collect.
- **let a decision be non-deterministic.** A worker may *draft* prose into a register. The schema,
  the evaluator, the gates and the mandate *decide*, and they are deterministic. No phase may depend
  on a worker existing.

## 6. Try it — watch a document be judged

Two commands, no prior knowledge. First, see the pipeline itself:

```bash
cd transformation_compilers
tc phase list
```

Every phase prints what it is for, how many rules it declares, what vocabulary it admits, its one
governing rule, and its gate. Now judge a real document — the book catalog's change request, kept
as a test fixture — against phase 1's 193 rules:

```bash
F=scripts/testbed/fixtures/catalog/cr_01_catalog
tc phase check --phase p1 --snapshot ../snapshot $F/p1_change_request_book_library_mgmt_catalog_v0.md
```

```
INADMISSIBLE  [p1]
  [SEED_ROW_NOT_CARRIED] system_beliefs: p0 was not supplied — this handoff is unchecked, and an
  unchecked handoff looks identical to a preserved one
  …
  34 finding(s) over 193 rules
```

The document is fine. **The check is incomplete**, and it says so rather than passing. Supply the
phase it descends from and run it again:

```bash
tc phase check --phase p1 --snapshot ../snapshot \
    --prior p0=$F/p0_seed_book_library_mgmt_catalog_v0.md <same document>
```

```
ADMISSIBLE  [p1]
  0 finding(s) over 193 rules
  judged by transformation.schemas.REGISTER_SCHEMA_P1_V0 revision 1 (the rule set sealed in ../snapshot)
  Figure of Merit   ★★★★★ 5/5
  Ready for P2      YES
```

### What just happened, and why it is the whole idea

The 34 findings were not complaints about content. They were **refusals to certify a handoff nobody
could see** — every row that claims to carry something forward from p0 was unverifiable without p0.
A pipeline that had shrugged and passed would have produced exactly the same verdict for a document
that quietly dropped half its problem statement.

Notice that the verdict names the rule set that judged it, and that it is not a boolean.
`ADMISSIBLE` is the gate; the **figure of merit** is a separate judgement of quality. Admissibility
and excellence are different questions, and conflating them makes one of them useless.

### Then look at the other end

```bash
tc baseline show --snapshot ../snapshot
tc construction check <a dossier with a p7>
```

`baseline show` prints the composition as a pin — an identity hash, an artefact count, the domains
present. `construction check` measures whether a design determines its artefacts, and the default
threshold is **100**:

> A fact the design does not state is a fact the generator would have to invent, and a generator that
> invents design is a second, ungoverned design authority.

Anything below 100 is a refusal, not a warning.

## 7. The baseline is pinned, and stays pinned

Validation never runs against "the current snapshot". It runs against a **named, frozen** one, and a
run that observes a different identity **fails before executing a phase**.

**The pin lives with the change, not with this repository** — each dossier carries its own, and each
change pins the composition its predecessor produced. A completed change is never re-pinned forward:
approving a register against a composition that arrived later asserts a re-reading of facts the build
already settled. An in-flight change is different and may legitimately re-pin.

Rebaselining is a deliberate, reviewed act — re-pin the identity, re-approve the affected registers.
Never a silent drift, because otherwise **a regression is indistinguishable from a rebuild**.

## 8. One live version, and proof for every transform

**An artefact lives in one version.** Whether a change keeps an artefact's meaning is decided by
`sameness`, by the rules `artifact::VOCAB_DECLARATION_REPRESENTATION_V1` declares. A change that keeps
it keeps the identity. A change of meaning takes the next version never used and names its
predecessor in `supersedes`. The predecessor is deleted, and the deletion is recorded in the
workspace ledger with who decided it and why. A deleted name is never reused. History is held by the
release tags, the ledger and git, not by old versions left in the tree.

**Every transform this module owns is proven by vectors.** A `TEST_DATA` artefact names the
transform it tests and states, case by case, what the transform is handed and what it must return.
The domain build runs them. Phase 7 refuses a design whose new transform has no cases.

## 9. Phases, never stages

A dossier has **phases** (p0–p8). A compilation has **stages** (S1–S9). No document, path, register
field or identifier uses one word for the other.

This looks like pedantry and is not. The earlier implementation numbered its dossier phases S1–S7,
colliding with the compiler's own S1–S9, and every piece of evidence became ambiguous about which
pipeline produced it. A word that names two things names neither.

## 10. Layout

```
transformation/
    cli.py                the command surface: phase · construction · baseline
    baseline.py           the pin, and verification against it
    design/               the Design Compiler
        read.py           a phase document: prose split from its Machine block
        schema.py expand.py declared.py   register schemas expanded into sealed rules
        evaluate/         the deterministic judge: keywords, four constructs, procedures/
        oracle.py rules.py rule_sets.py sealed.py   the rule set a phase is judged by
        effectivity.py    which rule set judged a document, and approval standing
        project.py merit.py meta.py   projection, figure of merit, closure
        emit.py           the generator behind the nine phase workflows
    build/                the Construction Compiler
        completeness.py   does this design determine its artefacts?
        render.py mapping.py   write them, as the construction mapping states
        generators.py     …except the ones that are reached, not written
        sameness.py       does an amendment keep its artefact's meaning?
    implementation/       the capability transforms the phase workflows run
    templates/            the required section structure, one per phase

registry/                 this repo's own artefacts — design/ and build/ are compiled
                          subdomains, like any domain's; schema/ holds the register schemas
design/                   this module's design of record: P7 and P8, generated from registry/
doc/                      the design language and the construction mapping
scripts/testbed/          the phase corpus, fixtures and the harnesses the regression runs
testbed/                  the payloads the runtime executes, and the routing closure
```

`registry/` deserves a second look: **this repository is itself a compiled domain.** The lifecycle
that governs change is declared in the same artefact language as the businesses it governs.

## 11. Rules this repo enforces

1. **Each phase admits a strictly wider vocabulary than the last**, and nothing may be said early
   that belongs late.
2. **Rules are declared, not coded.** A phase's rules are its register schema, and each rule cites the
   invariant it realises.
3. **A verdict names the rule set that judged it**, and an approval stands only under the rule set it
   was given under.
4. **A run fails before executing a phase** if the snapshot on disk is not the pinned baseline.
5. **Every snapshot fact arrives through the inspection interface.** No compiler import, ever.
6. **Dossiers are evidence, not artefacts** — they never enter a snapshot.
7. **A dossier lives with the domain it changes**, never centralised here.
8. **Decisions are deterministic**; only drafting may be assistive, and no phase depends on a worker.
9. **Construction completeness below 100 is a refusal**, because the gap would be filled by
   invention.
10. **An artefact lives in one version.** A change of meaning is a new version, and the old one is
    deleted by record.
11. **Phases are never called stages.**
12. **The tool has no transport surface.** CLI only.
13. **An artefact has one producer.** Where an artefact is generated, its generator is authoritative
    and the artefact is never corrected directly — a disagreement is proof the copy is stale, and the
    build refuses rather than reporting on it. Construction reaches such an artefact by invoking its
    generator, never by writing it.

## 12. How to know it works

```bash
tc phase meta --snapshot ../snapshot   # the rule sets checked against themselves
tc phase list                          # every phase, with its declared rule count
tc phase emit --check --snapshot ../snapshot   # every workflow against its schema
```

`phase meta` is the one to trust. It verifies the **rules themselves** rather than any document —
that every declared rule resolves to a check that exists, that every check is used, and that every
rule realises an invariant the platform declares. A good result reads:

```
CONSISTENT — 992 rules across 9 phases resolve against 57 check kinds
```

A pipeline whose rules are not themselves checkable is a pipeline that can quietly stop enforcing
something. Beyond that, the workspace regression drives a corpus of phase documents through every
phase, both directly and through the runtime, and compares each verdict and finding with what the
case expects. It pins **the register rows and the verdict — never authored prose.** Prose from a
drafter is not byte-reproducible, and a fixture that diffs it is deleted within a week.

The design of record is the last check. It states every artifact of this module in the design
language, and construction renders it back into the registry.

## 13. Where the architecture is explained

This document describes *this repository*. The architecture it realizes is developed in the papers
indexed at **https://github.com/protocol-governed-computing**:

- **An Architecture for Closed-Loop Governed Transformation** — the closest companion to this
  repository: why evolution must itself be governed, and what closes the loop.
- **Realizing the Normative Platform and Its Governed Transformation** — construction completeness,
  the baseline as a party to its own transformation, and what realization surfaced.
- **A Conceptual Model** — the artefact language a mandate ultimately schedules.
