# Stage 4 — Business Model: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p4
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_04_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Catalog
    role: States what each of its operations needs, and decides whether a request may proceed.
    authority_class: Declaring — what an operation requires is the catalog's own account of what it does.
    source_finding: {phase: p1, register: authority_boundaries, row: 1}
  - actor: Library staff
    role: Make the requests the catalog admits or turns away.
    authority_class: Acting — unchanged by this change.
    source_finding: {phase: p2, register: entities, row: 2}
  - actor: The library's authorisation rules
    role: Decide who may perform each operation.
    authority_class: Deciding — stated separately from what an operation needs, and untouched.
    source_finding: {phase: p2, register: belief_verification, row: 4}
  bm_entities:
  - entity: Operation
    description: Something a librarian asks the catalog to do.
    store_model: Ten are declared for this subdomain, each with a boundary and a workflow.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: Requirement
    description: Something an operation states a request must supply.
    store_model: Declared at the operation's boundary, as a name and the form the value takes.
    source_finding: {phase: p2, register: entities, row: 3}
  - entity: Use
    description: A step of the operation reading something the request supplied.
    store_model: Declared in the operation's own steps.
    source_finding: {phase: p2, register: entities, row: 4}
  - entity: Request
    description: One asking, with what the librarian supplied.
    store_model: Not held; it is what arrives at the boundary.
    source_finding: {phase: p2, register: entities, row: 2}
  resources:
  - resource: The three boundaries being corrected
    description: Registering a further edition, correcting bibliographic information, and registering a work.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
  - resource: The seven boundaries that already agree
    description: Registering a physical copy, retiring and reinstating a book record and a physical copy, retrieving book details, and searching the catalog.
    source_finding: {phase: p2, register: architectural_observations, row: 1}
  - resource: The library's end-to-end exercise of the catalog
    description: Registering a work, adding two further editions, correcting a legacy record. Stops today at the second edition.
    source_finding: {phase: p3, register: verification_results, row: 6}
  - resource: The four statements of a publication year's form
    description: Three boundaries and the description supplied with each request. Three say number; one says word.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
  events:
  - event: A request was admitted
    trigger: A librarian supplying what the operation needs
    lifecycle_meaning: The operation proceeds and the catalog changes.
    source_finding: {phase: p1, register: business_events, row: 1}
  - event: A request was turned away
    trigger: Something the operation needs being missing or in the wrong form
    lifecycle_meaning: The librarian is told before anything happened, and the catalog is unchanged.
    source_finding: {phase: p1, register: business_events, row: 2}
  - event: A correct request was turned away
    trigger: A boundary requiring something its operation does not use, or requiring it in a form the catalog does not hold
    lifecycle_meaning: The state this change ends. It is the present state of two of the ten operations.
    source_finding: {phase: p1, register: lifecycle_states, row: 3}
  - event: A request was admitted that the operation could not carry out
    trigger: A boundary requiring less than its operation reads
    lifecycle_meaning: Latent in registering a work; the failure appears part-way through instead of at the boundary.
    source_finding: {phase: p2, register: gaps, row: 3}
  relationships:
  - subject: Operation
    verb: requires
    object: Requirement
    capability_need: Admitting a request to register a further edition.
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
  - subject: Operation
    verb: requires
    object: Requirement
    capability_need: Admitting a request to correct bibliographic information.
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
  - subject: Operation
    verb: requires
    object: Requirement
    capability_need: Admitting a request to register a work — deferred; the requirement it lacks is one every present caller sends elsewhere.
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
  - subject: Operation
    verb: uses
    object: Requirement
    capability_need: Agreement between what an operation requires and what its steps read.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
  capability_graph:
  - capability: Admitting a request to register a further edition
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    status: CRITICAL
    gap_register_entry: GAP-1
    notes: Turns away every correct request today; the library's exercise stops here.
  - capability: Admitting a request to correct bibliographic information
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    status: CRITICAL
    gap_register_entry: GAP-2
    notes: Turns away every correction today.
  - capability: Admitting a request to register a work
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    status: DEFERRED
    gap_register_entry: ''
    notes: A real defect of the same kind, read in the other direction. Correcting it moves a caller, which this change's seed forbids.
  - capability: Deciding who may perform an operation
    source_finding: {phase: p3, register: dependency_discoveries, row: 3}
    status: SATISFIED
    gap_register_entry: ''
    notes: Declared uniformly across all ten operations and untouched.
  - capability: The three operations
    source_finding: {phase: p3, register: authoring_decisions, row: 4}
    status: SATISFIED
    gap_register_entry: ''
    notes: No step is added, removed or rebound; each operation is correct.
  - capability: Holding what the catalog knows
    source_finding: {phase: p3, register: dependency_discoveries, row: 4}
    status: SATISFIED
    gap_register_entry: ''
    notes: Six stores, unchanged; no held record is migrated or revalidated.
  dependency_graph:
  - from: catalog
    to: catalog
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 2}
  - from: catalog
    to: intent
    dependency_type: data read
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 1}
  - from: catalog
    to: structure
    dependency_type: data read
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 4}
  constraint_register:
  - number: '1'
    constraint: An operation requires only what it uses, and uses only what it requires.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
    source: governance rule
  - number: '2'
    constraint: Nothing about who may perform an operation changes.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: governance rule
  - number: '3'
    constraint: The records the catalog already holds are not migrated, rewritten or revalidated.
    source_finding: {phase: p1, register: constraints, row: 3}
    source: governance rule
  - number: '4'
    constraint: A publication year is stated as a number wherever an operation asks for one.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: governance rule
  - number: '5'
    constraint: No correct request becomes harder to make.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    source: governance rule
  - number: '6'
    constraint: The form of a detail the catalog holds is settled by no artifact, so agreement among the statements of it is the only authority available.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
    source: domain knowledge
  gap_register:
  - gap_code: GAP-1
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    capability: Admitting a request to register a further edition
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-2
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    capability: Admitting a request to correct bibliographic information
    owner_subdomain: catalog
    resolution: EXTEND
  design_decisions:
  - number: '1'
    decision: Registering a further edition states the publication year as a number.
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    rationale: Three of the four statements of the form say number, and every year the library supplies is a number.
    constraints_imposed: Rules out changing the operation to accept a word, and rules out leaving the form to whichever statement is read first.
  - number: '2'
    decision: Correcting bibliographic information withdraws the title, the author and the publication year.
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    rationale: No step of the correction reads any of the three, and a correction that restates the fields it leaves alone is not a correction.
    constraints_imposed: Rules out making the operation read them to justify requiring them.
  - number: '3'
    decision: Registering a work is not corrected here.
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    rationale: The act reads the subject at the top of the request and every present caller sends it nested inside the details of the book, so requiring it makes every present request fail. Constraint 5 forbids exactly that.
    constraints_imposed: Rules out correcting a boundary whose correction moves a caller, and fixes that the defect is deferred intact rather than dropped.
  - number: '4'
    decision: No step of any of the three operations changes.
    source_finding: {phase: p3, register: authoring_decisions, row: 4}
    rationale: What each operation does is correct; it is the boundary above it that is wrong.
    constraints_imposed: Rules out rewriting the operations, and confines the change to three declarations.
  - number: '5'
    decision: The change is one act over three boundaries, not three unrelated corrections.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
    rationale: All three break one invariant, read in both directions; stating it one-sidedly is what let the third survive.
    constraints_imposed: Rules out completing the change with two of the three corrected.
  authoring_scope:
  - capability: Admitting a request to register a further edition
    gap_register_ref: GAP-1
  - capability: Admitting a request to correct bibliographic information
    gap_register_ref: GAP-2
```

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

---

## 2. Capability Graph (capability_graph)

---

## 3. Dependency Graph (dependency_graph)

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Admitting a request to register a work | The act reads the subject at the top of the request and every present caller sends it nested inside the details of the book. Requiring it moves the boundary and every caller together, which this change's seed forbids. Its own CR, where both move at once. |
| Comparing what an operation requires against what it uses | Nothing performs it in the composition. Whether it belongs to this subdomain or to the platform is not this change's to settle. |
| Declaring the form of a detail the catalog holds | The store declares paths and no forms. Giving the catalog an authority over forms is a larger change than bringing one boundary into agreement with three statements. |
| The operations of subdomains and domains other than the catalog | Each is its own business, and the same comparison reports findings elsewhere that were not examined here. |
