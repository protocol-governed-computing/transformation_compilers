# Design Intent: [domain] / [subdomain]

## Machine

```yaml
document:
  phase: p7
  domain: <domain>
  subdomain: <subdomain>
  cr: <change>
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
  # approval: {gate: ..., rule_set: ..., state: APPROVED} — when the gate closes
registers:
  design_resolution:
  - decision: null
    business_fact: null
    resolution: null
    source_finding: null
  existing_inventory:
  - fqdn: null
    action: null
    summary: null
    reason: null
    source_finding: null
  new_artifacts:
  - capability: null
    family: null
    code: null
    summary: null
    owner_subdomain: null
    status: null
    source_finding: null
  rb_declarations:
  - rb_code: null
    binds_wf: null
    cs_bindings: null
    storage_structure: null
    source_finding: null
  execution_topology:
  - workflow: null
    node: null
    runs: null
    node_type: null
    routing: null
    source_finding: null
  cc_composition:
  - cc_code: null
    step: null
    step_name: null
    capability: null
    kind: null
    operation: null
    store: null
    consumes: null
    produces: null
    routing: null
    interpreted_by: null
    semantic_status: null
    interface: null
  step_bindings:
  - owner: null
    step: null
    direction: null
    field: null
    bound_to: null
    source_finding: null
  interface_fields:
  - artifact: null
    direction: null
    field: null
    type: null
    format: null
    required: null
    default: null
    meaning: null
  implementation_bindings:
  - ct_code: null
    callable: null
    operation: null
    kind: null
    purity: null
    refusal: null
    source_finding: null
  vocabulary_extensions:
  - vocabulary_code: null
    extends: null
    group: null
    casing: null
    value: null
    meaning: null
    source_finding: null
  runtime_policies:
  - rb_code: null
    capability: null
    key: null
    value: null
    source_finding: null
  artifact_properties:
  - artifact: null
    property: null
    value: null
    source_finding: null
  structure_stores:
  - store_name: null
    storage_type: null
    proposed_path: null
    used_by: null
    source_finding: null
  transport_bindings:
  - artifact: null
    direction: null
    operation: null
    handler_kind: null
    handler_target: null
    field: null
    bound_to: null
    required: null
    source_finding: null
  artifact_summary:
  - action: null
    subdomain: null
    count: null
    artifacts: null
  generation_provenance:
  - artifact: null
    generator: null
    generator_sources: null
    source_finding: null
  declared_reach:
  - act: null
    consults: null
    source_finding: null
  refusal_discharge:
  - operation: null
    refused_when: null
    act: null
    step: null
    outcome: null
    source_finding: null
  refusal_deferrals:
  - operation: null
    refused_when: null
    deferred_to: null
    until: null
    source_finding: null
  refusal_governance_discharge:
  - operation: null
    refused_when: null
    phase: null
    governing_rule: null
    source_finding: null
  molecule_steps:
  - ct_code: null
    step: null
    kind: null
    target: null
    over: null
    iterator: null
    emits: null
    source_finding: null
  molecule_step_bindings:
  - ct_code: null
    step: null
    role: null
    field: null
    bound_to: null
    source_finding: null
  test_cases:
  - ct_code: null
    case: null
    expected_outcome: null
    source_finding: null
  test_case_values:
  - ct_code: null
    case: null
    role: null
    field: null
    value: null
    source_finding: null
  withdrawn_facts:
  - artifact: null
    fact: null
    reason: null
    source_finding: null
```

## Document Contract

**This artifact is a structured register document — not a narrative.** P7 assigns the **binding
FQDNs** the rest of the build depends on. The worker emits register ROWS; a deterministic renderer
owns the document and a structural oracle validates the codes BEFORE a human reviews.

VALID OUTPUT:
- Populated registers (every required register below)
- Binding FQDNs in `code` / `rb_code` / `binds_wf` / `storage_structure` columns, each
  well-formed (`domain::PREFIX_NAME_V<n>`) and assigned EXACTLY ONCE
- Business-language capability descriptions in the `capability` column

INVALID OUTPUT:
- Narrative summaries / reasoning essays replacing registers
- A binding FQDN referenced anywhere (topology, RB) but absent from `new_artifacts`
- Two spellings of the same capability (a typo is a SECOND immutable artifact, not a synonym)

A register with nothing to state is `[]`, declared empty. A register left `null` states nothing,
and a required register that states nothing is refused.

---

### Binding-FQDN discipline (the oracle enforces these)

- **Well-formed:** every assigned code is `domain::PREFIX_NAME_V<n>` (PREFIX ∈ WF/IN/RB/CC/CT/EV/
  STRUCTURE; explicit `_V0`).
- **One canonical FQDN per capability — assign it ONCE, reuse the EXACT string everywhere**
  (topology, pipelines, RB, summary). A binding FQDN is immutable: a spelling/term variant of the
  same concept (e.g. `GENESIS` vs `GENEISIS`) silently creates a SECOND, permanently-misnamed
  artifact. Spell domain terms exactly.
- **Referenced ⇒ declared:** every NEW code that appears in `execution_topology` or
  `rb_declarations` MUST appear as a row in `new_artifacts`. CTs and EVs are first-class new
  artifacts — never implicit.
- **Genuinely new:** an assigned `new_artifacts` code MUST NOT already exist in the snapshot
  (the oracle collision-checks via grounding). Existing artifacts go in `existing_inventory`.
- **Reconciled:** the NEW counts in `artifact_summary` MUST equal the rows of `new_artifacts`.

### Data-to-decision closure (the oracle enforces these)

P7 does not merely assign artifacts. It assigns the **behavioural interpretation path** from a
capability's output, through a decision, to a workflow transition. A design that names every
artifact correctly and leaves that path unstated is admissible and still cannot work.

- **No implicit truthiness.** `exists`, `matched`, `authorized` and every other boolean a capability
  returns is an **observation**, never a decision. A step that reads external state cannot drive
  business routing directly.
- **A step branches on what its operation answers, or says what produced the rest.** Every
  operation publishes its `result_status_values`. A `CS` step routing on one of those — a registry
  claim exiting on `ALREADY_EXISTS`, a read exiting on `NOT_FOUND` — is routing on the store's own
  answer, and interprets nothing. A step routing on anything else MUST name the transform that
  produces that outcome (`Interpreted By`) and the outcome itself (`Semantic Status`).
- **`—` in either column is a declaration, not a blank.** It says the step's output is data and the
  branches are the operation's own. It is the right answer for most steps and refused wherever the
  routing names an outcome the operation cannot produce.
- **`Store` and `Consumes` take the same dash and it says something different in each.** In `Store`
  it declares that the step addresses no store, which is true exactly when its capability keeps no
  records — a clock and every transform. In `Consumes` it declares that the step hands the operation
  nothing, which is true exactly when the operation takes no input. Both are checked against what the
  composition publishes, so a storage step addressing nothing and a read consuming nothing are each
  refused where they read as a design that works.
- **Routing closure.** Every workflow branch is backed by the whole chain:

```
CS result  →  CT interpretation  →  semantic outcome  →  WF transition
```

> **Raw capability observations never determine workflow behaviour directly.**

An interpretation transform expresses its decision the only way the execution contract allows: a
`CT` step yields `SUCCESS` when it returns and `VIOLATION` when it raises. A transform that returns
a boolean for both answers has interpreted nothing, however it is named — which is why a transform
named here must declare `refusal: raises` in §9.

### Capability Composition discipline (the oracle enforces these)

`cc_composition` declares the second half of Design Intent: WHAT each new CC is composed of. Workflow
topology (§5) says how CCs route to one another; composition says what is *inside* each CC. It is
**declarative, not procedural** — you declare the governed capabilities the CC is built from and how
data flows between them; you never write code, JSON, JSONPath, or an implementation.

- **CT/CS only.** Each composition step is a Capability Transform (`CT`, pure compute, zero side
  effects) or a Capability Side Effect (`CS`, the only place external state changes) — never a CC, WF,
  or IN. A CC composes *capabilities*, not other CCs.
- **Codes verbatim.** Every `Capability` cell is a CT/CS binding FQDN copied verbatim from
  `new_artifacts` (NEW) or a grounded `existing_inventory` artifact (REUSE) — same immutability rule
  as every binding FQDN. A composition code absent from both registers is a defect.
- **Data flow is logical, not wired.** `Consumes` / `Produces` name business/data fields (e.g.
  `proposed_block`, `content_hash`), connecting a CC's inputs to its steps and step-to-step. Concrete
  JSONPath wiring is construction (S8), not design.
- **Outcome coverage.** The outcomes the composition can yield MUST cover the CC's routing surface in
  `execution_topology` (§5): if topology routes the CC on `SUCCESS` and `ALREADY_EXISTS`, the
  composition must be able to produce both. The oracle cross-checks composition ⊇ topology surface.
- **CT purity.** A `CT` step may not appear where a side effect is required, and may never be a CS.

### Business-Language Rule

Only the `capability` column of `new_artifacts` is business language (name the need, not the
artifact). Every other column legitimately carries FQDNs / controlled tokens — that is where the
binding codes belong. Existing artifacts are cited by their real FQDN in `fqdn` / source columns.

---

## Stage Inputs — Questions for the Human

*Answer crisply before drafting. The right column states how the agent uses each answer.*

| # | Question for the Human | How the Agent Uses the Answer (Intent) |
|---|------------------------|----------------------------------------|
| 1 | For each open design decision carried from Stages 1–4: which concrete resolution (store shape, schema fields, algorithm, reuse-vs-new)? | Becomes `design_resolution`. Every row traces to a Business Model design decision; new decisions invented here are flagged. |
| 2 | Where an existing artifact partially fits: REUSE as-is, EXTEND it, or REPLACE it? | Fixes `existing_inventory` actions. REPLACE/EXTEND of shared artifacts affects other subdomains. |
| 3 | Do you approve the proposed store names, paths, and key fields? | Locks `structure_stores`. Storage topology is a governance concern — paths declared here, never hardcoded later. |
| 4 | Gate 1: do you approve the full dossier as the design basis? | Gate 1 approval authorizes Stage 7. Without it, no mandate may be drafted. |

**Agent execution rules for this stage (binding FQDNs are assigned here):**
- Every new artifact maps 1:1 to a Governance Intent outcome; every FQDN carries `_V<n>`.
- **Workflow nodes are IN, CC, EXIT/EXIT_SUCCESS only.** Sub-workflow invocation = gateway CC bound to `CS_WORKFLOW_GATEWAY_V0` (precedent: `CC_INVOKE_BLOCK_PROPOSAL_V0`). EV_ artifacts are emitted facts, never triggers.
- A store is written only by CCs of its owning subdomain. Writing CCs for peer stores are declared in the dependency-gap section with peer ownership.
- Before declaring a new CT or EV: check the existing inventory (the transform vocabulary and event set usually already contain the atom) — if reused, it belongs in `existing_inventory`, not `new_artifacts`.
- **Compose every new CC.** Each `family = CC` row in `new_artifacts` gets a `cc_composition` (§6): the ordered CT/CS steps it is built from + their data flow. Leaving a CC's composition unstated leaves construction a design decision — exactly the black box this stage exists to close.
- **Module path assignment (reference):** IN→`[repo].registry.[subdomain].intents`, WF→`.workflows`, CC→`.capability_contracts`, CT→`.capability_transforms`, RB→`.runtime_bindings`, STRUCTURE→`.structures`. A missing assignment is a build failure.

---

### Citing a prior row

Every row carries a `source_finding` naming where its content came from. A citation is a mapping:

- **a row of a register**, by ordinal or by key, in the phase that declared it:
  `{phase: p1, register: known_facts, row: 14}`. A citation that names no phase names this document;
- **an artifact already in the baseline**, by exact identity: `{artifact: blockchain::WF_REGISTER_ACTOR_V0}`;
- **a person**: `{source: human}`.

Several citations are a list. A row that cites nothing is `null`, and is refused where the register
requires provenance.

**A carried claim is carried verbatim.** Where a register restates a row an earlier phase declared —
a belief, an authoring decision, a capability — the text must match that row exactly. Tightening a
sentence while citing the row it came from is how a claim drifts from what was decided, so the rules
treat a tidier synonym as a new claim and refuse it. Cite it as it stands, or change it in the phase
that owns it.

---

## 1. Design Decisions Resolution

*The Design Decisions Register populated throughout Stages 1–4 — resolved here. Each row traces to a Business Model design decision (`source_finding`).*

Register `design_resolution` in the Machine block.

---

## 2. Artifact Inventory — Existing Artifacts

*All existing PPS artifacts touched by this CR. Action ∈ REPLACE | REUSE | EXTEND | REPOINT | REVIEW. `fqdn` is the existing artifact, cited by exact FQDN.*

**An `EXTEND` is a whole redeclaration, not a delta.** Construction renders an amended artifact from
this design alone and the result replaces its predecessor, so every register that describes it must
describe it *as it will be* — every store the declaration carries, every field the contract accepts
and returns, every node the workflow runs — not only the parts this change adds. A design that
states the delta renders an artifact with the rest deleted, and reports 100% completeness while
doing it, because completeness asks whether the design's own claims are determined and never what
the composition already holds.

*The word invites the wrong reading and the reading is expensive: it produced a storage declaration
carrying two stores where five existed. **An `EXTEND` keeps the artifact's meaning.** Construction
compares each amendment with the artifact the composition holds, by the platform's declaration of
what carries no meaning, and refuses any difference it does not excuse: a fact added, altered or
removed. A change of meaning is a new identity — a new artifact that the old one is `REPLACE`d by.*

*A `REPOINT` is an artifact that names one this design replaces. Construction rewrites each such
name in it to the replaced artifact's declared successor and changes nothing else; the artifact
keeps its identity. Every live artifact that names one this design replaces is `REPLACE`d,
`EXTEND`ed or `REPOINT`ed here, or construction refuses the design and names it.*

*`Summary` states what the artifact **is**, where `Reason` states why this change touches it. It is
required for an `EXTEND`, because a rendered artifact without its summary is one this change
silently emptied. A `REUSE`, `REPOINT` or `REVIEW` row is not rendered and may leave it blank.*

Register `existing_inventory` in the Machine block.

---

## 3. Artifact Family Mapping — New Artifacts

*Each Governance Outcome capability mapped to an artifact family with a binding FQDN assigned.
`capability` is business language; `code` is the binding FQDN; `family` is the execution concern;
`owner_subdomain` is the owning subdomain; `source_finding` traces to the S6 ownership / S4 gap.*

Register `new_artifacts` in the Machine block.

---

## 4. Runtime Binding (RB) Declarations

*One RB per WF. The RB declares which CS substrates the WF requires and which storage structure resolves store paths. An undeclared CS binding is a runtime failure. `cs_bindings` may list several CS FQDNs (comma-separated).*

Register `rb_declarations` in the Machine block.

---

## 5. Execution Topology

*The DAG flattened to one row per node, in execution order, per workflow. `node` is an IN/CC binding
FQDN or a terminal (EXIT / EXIT_SUCCESS).*

*`routing` states the outcome→target edges as **edges, not prose**: `STATUS -> target` entries
separated by `;`, where STATUS is a business status name (ACK, NACK, SUCCESS, NOT_FOUND,
ALREADY_EXISTS, DENIED, VIOLATION, BACKEND_ERROR) and target is a node of this same workflow or a
terminal. `SUCCESS -> CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED`. A description of
where control goes is not a routing declaration — it names no node, and construction cannot resolve
it.*

*`runs` is optional, and blank means the node is its own contract: the node is named by the CC's code,
as above. A workflow that runs one contract at several places, each handed its own values, names
each place with a key and states the contract it runs in `runs`. A key is unique within its
workflow. Routing targets, step bindings and discharges name the key; the contract's interface and
reach are read from `runs`. `NOT_FOUND -> RECORD_UNKNOWN_BORROWER` routes to a keyed node whose
`runs` is `CC_RECORD_REFUSAL_V0`, and a second key in the same workflow may run that contract too.*

Register `execution_topology` in the Machine block.

---

## 6. Capability Composition

*The inside of each new CC: the ordered CT/CS steps it is composed of and how data flows between
them. Declarative, not procedural — governed capabilities + data flow, never code or JSONPath. One
row per (CC, step), in execution order. `capability` is a CT/CS binding FQDN (verbatim from
`new_artifacts` or `existing_inventory`); `consumes`/`produces` name logical data fields. The
outcomes the composition can yield must cover the CC's routing surface in `execution_topology` (§5).
`Interface` (CT steps) is the **explicit invocation binding** — how this step's CC-local fields bind
to the invoked capability's declared FORMAL parameters, so a reusable CT keeps its own vocabulary and
the CC keeps its business vocabulary. Syntax: `in: <ct_formal>=<cc_local>, …; out: <ct_output>=<cc_local>, …`
(e.g. `in: left=predecessor_hash, right=current_head; out: is_equal=is_match`). CS steps leave it blank.*

Register `cc_composition` in the Machine block.

---

## 7. Step Bindings

*What each workflow node and each contract step is handed, and where its results go. A step whose
bindings are undeclared is one construction must invent bindings for, and an invented binding is a
design decision taken outside the gate.*

*`owner` is the workflow or capability contract; `step` is its node or step name. A workflow node
takes INPUT bindings only; a contract step takes both, because its outputs are named for later steps
and for the contract's own surface.*

*`bound_to` is declarative, never an expression: `payload.<field>` names a field of the starting
intent, `<node>.<field>` names an earlier node's output in this same workflow, and a bare literal is
a constant the design fixes (an operation name, a status). Rendering that into `$.payload.x` is
construction's business — the design states the source, not the syntax.*

*A literal is a single word, a qualified identity (`domain::CODE_V0`), a number, or a value opening
with a quote, bracket or brace. A value with a dot in it is written quoted — `"si.artifact.list"` —
or it reads as a reference. Every rule that judges a binding reads a literal this way.*

*`generated` is reserved. It states that the generator of the binding's owner determines the value,
as a phase workflow's sealed rule set is, and it is admitted only for an owner §16 lists as
generated. A design that means the word itself writes it quoted.*

Register `step_bindings` in the Machine block.

---

## 8. Interface Fields

*Every typed field an artifact declares, whichever family it belongs to. An intent's inputs, a
capability contract's inputs and outputs, a transform's inputs and outputs, and an actor's
attributes are one shape — (artifact, direction, field, type) — and they were all unexpressible for
the same reason: the language could describe a capability but never a field of one.*

*`direction` ∈ INPUT | OUTPUT | ATTRIBUTE. `required` ∈ YES | NO. `default` is stated only when the
field has one; a field with no default and `required: NO` is simply absent when not supplied.*

Register `interface_fields` in the Machine block.

---

## 9. Implementation Bindings

*Where a transform's code lives. A CT is the one family whose artifact points outside the
composition, and the module path is a governance concern for the same reason a store path is: it is
declared once, at design time, never discovered later.*

*`operation` is the CT's declared operation name; `purity` ∈ ct_pure | ct_impure; `kind` ∈ atom |
molecule.*

*A molecule has no module and no callable: its steps are its specification, and §21 declares them.
Leave both cells blank for a molecule. Every atom names both.*

*`refusal` says how the transform expresses a judgement about its subject: `raises` refuses, which
the execution contract reads as VIOLATION; `returns` yields the judgement as an output, so the step
succeeds whatever it found; `never` judges nothing. It is about the subject, never the inputs —
every transform raises on a missing input, so that would make the fact uniform and therefore empty.
A transform named as an interpretation must declare `raises`, because a judgement the step cannot
fail on is a branch nothing reaches.*

Register `implementation_bindings` in the Machine block.

---

## 10. Vocabulary Extensions

*Business status names this change adds, and the vocabulary they extend. A workflow that routes on
`DENIED` needs `DENIED` to exist; the routing surface and the vocabulary that admits it are declared
together or the composition compiles with a status nothing recognizes.*

*`Extends` is required and the none marker is an answer. A vocabulary that builds on nothing is a
base vocabulary, which is a decision; left blank it is indistinguishable from a design that never
settled the question, and both render the same empty field.*

Register `vocabulary_extensions` in the Machine block.

---

## 11. Runtime Policies

*The per-capability configuration a runtime binding carries. `dispatcher.py` resolves
`rb_policy[rb][capability]["policy"]` at execution, so this is what an RB *is* — the workflow that
binds it is a separate fact, declared on the workflow in §4.*

*A capability listed in `rb_declarations` with no row here binds with an empty policy, which is a
declaration that it needs no configuration rather than an omission.*

Register `runtime_policies` in the Machine block.

---

## 12. Artifact Properties

*Scalar facts a family declares that no other register carries — an actor's `type` today. A property
that recurs across families has stopped being family-specific and earns its own register; this one
exists so that a single scalar does not.*

*`emit.<ending>` names the moments an act announces at that ending, which completes the act. An act
that refuses may announce the refusal itself, and nothing else: an ending typed `EXIT` announces only
moments this register declares `moment` = `refusal`. Whether a moment is a refusal is read from that
declaration, never from its name.*

Register `artifact_properties` in the Machine block.

---

## 13. STRUCTURE Stores

*New entity stores. `storage_type` selects the CS substrate — a store a capability claims keys in is a registry store, which the composition already carries examples of; `proposed_path` is the declared store path (governance concern — never hardcoded later); `used_by` names the writing CC (its owning subdomain only).*

Register `structure_stores` in the Machine block.

---

## 14. Transport Bindings

*What a boundary contract publishes and how it maps across the boundary. An ingress declares the
operation identity a caller names, what dispatches it, and how the canonical input becomes the
workflow payload; an egress declares how a result surface becomes the fields a caller reads. One row
per mapped field, so a mapping is checkable rather than a blob. An egress field is owed; `required:
false` declares one the response omits when the result carries nothing for it.*

Register `transport_bindings` in the Machine block.

## 15. Artifact Summary

*Artifact count by action type, for Stage 7 input. The oracle reconciles: the NEW counts here MUST equal the rows of `new_artifacts`. `artifacts` lists the codes for that action.*

Register `artifact_summary` in the Machine block.

---

## 16. Generation Provenance

*How an artifact is **reached**. Every other register says what an artifact must become; this one
says what determines it, and it is the only register that can describe an artifact nobody types.*

*An artifact listed here is produced by invoking its generator, and construction never writes it —
two producers of one truth drift, and the drift is silent until something reads the stale one. The
generator is authoritative: where the artifact and the generator disagree, the artifact is stale, and
the build refuses rather than reporting on a copy.*

*`Generator` is what construction invokes, as `module:callable`, and it must be importable from the
composition rather than reached as a script. `Generator Sources` names everything the emission reads
— a template and the declaration read with it are **one** generator, and naming either alone permits
regenerating from a stale pairing.*

*The artifact is still scheduled as an artifact. A design does not schedule a generator: the artifact
is what enters the composition and what conformance judges, and a mandate scheduling a generator
schedules something that never appears in a snapshot.*

Register `generation_provenance` in the Machine block.

---

## 17. Declared Reach

*The bindings an act **consults** — the records another subdomain of its own domain owns, which this
act reads and never writes. Ownership is §4 and is exactly one; reach is here and may be several,
and the two are separate registers rather than one with a column telling them apart, because a
column would put them a typo apart with nothing between them but the rule that reads it.*

*`Act` is the workflow's binding FQDN; `Consults` names the binding, comma-separated for several,
and **never the records behind it**. Which records a binding covers is the owning subdomain's own
declaration, and restating it here is a second copy kept by someone other than whoever answers for
it. The rules read the composition for that half.*

*Every declared reach is used by a read the act performs, and every read the act's own binding does
not cover is declared here. Neither half is a rule alone: the first permits a reserve, the second
permits a silent reach.*

*An act that reads only what it owns declares none, which is most acts.*

Register `declared_reach` in the Machine block.

---

## 18. Refusal Discharge

*What carries out an operation the business said it refuses. The seed states the refusal and the
condition; this register states the act, the step and the outcome that stop it — and it is the only
place a design says so, because a refusal nothing discharges is a refusal in prose.*

*`Operation` and `Refused When` are the seed's own wording, taken from its `operation_refusals`
register: the pair identifies which declared refusal this row answers, and a row naming a pair the
seed does not state is answering for a refusal nobody approved.*

*`Act` is the workflow's binding FQDN and `Step` is a step of that workflow, both resolved against
§5. `Outcome` is one the step reports, and it must route to a node typed `EXIT` — an ending that
refuses. An outcome routing anywhere else does not stop the operation, however plainly this register
says it does.*

*A refusal this change does not carry out belongs in §19, not here and not nowhere.*

Register `refusal_discharge` in the Machine block.

---

## 19. Refusal Deferrals

*A refusal the business declared and this design does not discharge, with the owner who will. The
two registers are read together for coverage and apart for everything else: a discharge names a
place in the topology, a deferral names a person and a condition, and one table holding both would
leave half its cells empty on every row — where a blank meaning "not applicable" is indistinguishable
from one meaning "unanswered".*

*`Deferred To` is who owns it and must not be blank; a deferral with no owner is a refusal dropped
in language that sounds like a plan. `Until` is the condition that ends the deferral.*

Register `refusal_deferrals` in the Machine block.

---

## 20. Refusal — Governance-Surface Discharge

*A refusal carried out by the design language itself, rather than by a step of this domain's own
acts. The business refuses an operation; no act performs it and none omits it; what refuses it is a
rule of the pipeline, which makes the declaration inadmissible before anything runs.*

*Three places a declared refusal can be carried out, and a design states each in its own register:
§18 when an act is attempted and refuses, §19 when someone else will carry it out later, and here
when the governance surface refuses the declaration outright. A fourth case — the domain simply
never offering the operation — is stated nowhere yet.*

*`Phase` is the phase whose rule set holds the rule, written `p0` through `p8` — the phase spelling,
never a stage number. It is required and not inferred: rule identifiers are **not** unique across
phases — every derived one, `REGISTER_MISSING`
among them, is declared by all nine — so a rule named without its phase names nine different rules.*

*`Governing Rule` is the rule's identifier, never a check kind. A check kind is a mechanism and can
be bound to any register with any parameters; it says how a check runs and cannot say what is
governed. The rule is the binding, and the binding is what refuses.*

*The rule must be **active in that phase's sealed rule set** — in the composition this design is
pinned to, not in somebody's working tree. Two consequences worth meeting here rather than
discovering later. **A design cannot discharge a refusal by citing a rule its own change is adding**:
the rule does not exist in the pinned composition, and the citation resolves to nothing. And
**resolution is not coverage** — that the cited rule exists and is enforced is checkable; that it
actually refuses the condition stated in `Refused When` is not, and it is what Gate 1 is reading for.*

Register `refusal_governance_discharge` in the Machine block.

---

## 21. Molecule Steps

*The inside of each molecule: the steps it runs, in order. A molecule is a transform made of other
transforms, and it exists so that a computation of several decisions is declared as those decisions
rather than hidden in one implementation. One row per (molecule, step), in execution order.*

*`Step` is the symbol the step's result is known by, and later steps read it as
`results.<step>.<field>`. `Kind` is `atom` for a transform with an implementation, `molecule` for a
molecule run once, and `loop` for a molecule run once per member of a collection. `Target` is the
transform the step runs, by binding FQDN, declared in `new_artifacts` or carried in
`existing_inventory`.*

*`Over` and `Iterator` are a loop's alone. `Over` names the collection, as `inputs.<field>`, and
`Iterator` is the name each member is handed to the body under. A loop runs its body once per member,
every time; a loop whose work is finished says so in the values it carries, and the passes that
remain change nothing.*

*`Emits` names the one value the molecule yields and is written on the step that produces it — on
exactly one row per molecule, and `—` on every other. Where the emitting step is not deterministic,
the molecule is refused: its results are offered to a deterministic step, never decided by one.*

Register `molecule_steps` in the Machine block.

---

## 22. Molecule Step Bindings

*What each molecule step is handed, and what a loop carries from one pass to the next. One row per
field, as §7 is for contract steps.*

*`Role` says which of three things a row is. `INPUT` is a field the step is handed — for a loop, a
field its body is handed on each pass. `CARRY` is a value a loop carries between passes, with the
value it starts from. `UPDATE` is where a carried value is taken from after each pass, read from the
body's result.*

*`Bound To` is declarative: `inputs.<field>` names a field the molecule is handed, `results.<step>.<field>`
an earlier step's result, `iterator` the member a loop pass is on, `accumulator.<field>` a carried
value as it stands, `results.<field>` (in an `UPDATE`) the body's result, and a bare literal a
constant the design fixes.*

Register `molecule_step_bindings` in the Machine block.

---

## 23. Test Cases

*The proof each transform this design authors or amends carries: stated inputs, and what the transform
must produce from them. A transform's implementation lives outside the composition, so the composition
can vouch for its declaration and never for its code; its cases are run against it exactly as sealed,
in the build that supplies it, on every build (`conformance::CONSTITUTION_TEST_DATA_V2`). One row per case.*

*Every transform in `new_artifacts`, and every transform amended in `existing_inventory`, has at least
one case — a transform authored without one is refused here, because this is the one place a new
transform can be told from one that already exists. Construction renders a transform's cases as its
vector, `TEST_DATA_<transform code>`, beside the transform; the vector is not listed in `new_artifacts`.*

*`Expected Outcome` is `SUCCESS`, or `VIOLATION` for a case the transform must refuse.*

Register `test_cases` in the Machine block.

---

## 24. Test Case Values

*What each case hands the transform and what it expects back. One row per value.*

*`Role` says what a row is. `INPUT` is a field the transform is handed. `EXPECTED` is an output the
transform must yield, compared exactly. `ASSERT` is an output whose value cannot be stated, with the
form it must take — `{mode: property, type: non_zero}` — which is how a step that is not deterministic
is proven on its own. `RECORDED` is, for a molecule, the result a non-deterministic step is recorded as
having produced: `Field` is the step's path as the runtime addresses it — `written[3]/offered` is the
step `offered` on the fourth pass of the loop `written` — and the case runs with that result
substituted, never running the step.*

*`Value` is a literal, written as YAML: `3`, `"The Odyssey"`, `[1, 2]`, `{candidates: [a, b]}`. A
case expecting `SUCCESS` states every output the transform declares, as `EXPECTED` or `ASSERT`, and
nothing else; a case expecting `VIOLATION` states none.*

Register `test_case_values` in the Machine block.

---

## 25. Withdrawn Facts

*A withdrawal is a change of meaning. An amendment keeps the artifact's meaning, so it can withdraw
nothing: a fact removed from an artifact is a new artifact that the old one is `REPLACE`d by. This
register is kept so that what a design may cite does not change, and it must be empty — a row here
is refused.*

Register `withdrawn_facts` in the Machine block.

---

## Gate 1 — Design Approval

**Gate 1 closes here.** The full dossier (Stages 0–7) is presented for review as a body. Any
prior-stage artifact amended during the Stage 6–7 session is included. This is a unified review of
the complete design, not a per-stage approval. Gate 1 approval authorizes Stage 7 — Authoring
Mandate. Gate 2 (after Stage 7) locks the full dossier before artifact authoring begins.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | change_request_[subdomain]_v0.md | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | business_model_[subdomain]_v0.md | COMPLETE |
| Stage 5 — Business Intent | business_intent_[subdomain]_v0.md | COMPLETE |
| Stage 6 — Governance Intent | governance_intent_[subdomain]_v0.md | COMPLETE — APPROVED |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
| Stage 8 — Authoring Mandate | Pending | — |
| Stage 8 — Authoring Manifest | Pending | — |

---

## gov_projection — Governed Handoff to Stage 7

*The bounded inputs and emit keys mirror the engine's gov_projection schema exactly
(`contracts/gov_projection.py`). P7 is the binding stage — it consumes the full design context
(S2 attribute/step data, S4 gaps/decisions, S5 intent + provisional codes, S6 placement) and emits
the five registers S7 builds from, plus `cc_composition` which the S8 Build Sheet assembles. Emit
keys match the register ids above exactly.*

| Direction | Registers |
|-----------|-----------|
| **Consumes** ← p5, p6, p0 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action |
| **Emits** | cc_composition · generation_provenance |
