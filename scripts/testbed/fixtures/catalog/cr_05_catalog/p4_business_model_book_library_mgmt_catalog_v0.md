# Stage 4 — Business Model: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p4
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_05_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Authorized staff
    role: Performs catalog operations.
    authority_class: Internal staff
    source_finding: {phase: p1, register: known_facts, row: 1}
  - actor: The staff function
    role: Decides which staff are authorized.
    authority_class: Adjacent subdomain
    source_finding: {phase: p1, register: known_facts, row: 2}
  - actor: The catalog
    role: Holds the library's records, and now every rule it applies to them.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  bm_entities:
  - entity: The Book
    description: Title, author, publication year, subject and state.
    store_model: One keyed store, one record per book, unchanged.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: The Physical Copy
    description: One copy of a book, and its state.
    store_model: One keyed store, one record per barcode, unchanged.
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: The Catalog's Rules
    description: Who may perform a catalog operation, and what a book, a work and a further edition must contain.
    store_model: Held by the catalog steps that apply them. Held by nothing today.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  resources: []
  events:
  - event: NONE IDENTIFIED
    trigger: This change recognises no new moment.
    lifecycle_meaning: The moments the catalog announces are unchanged.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: The catalog
    verb: refuses
    object: anyone the library has not authorized
    capability_need: Refuse anyone the library has not authorized
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse anyone the library has not authorized}
  - subject: The catalog
    verb: refuses
    object: a registration missing what it must contain
    capability_need: Refuse a registration the catalog finds incomplete
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse a registration the catalog finds incomplete}
  - subject: The catalog
    verb: records
    object: a copy as registered
    capability_need: Register a copy as registered
    source_finding: {phase: p3, register: authoring_decisions, key: Register a copy as registered}
  capability_graph:
  - capability: Refuse anyone the library has not authorized
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse anyone the library has not authorized}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: The confirming step holds the library's rules.
  - capability: Refuse a registration the catalog finds incomplete
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse a registration the catalog finds incomplete}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: A rule following each check refuses on what it found.
  - capability: Hold what a book, a work and a further edition must contain
    source_finding: {phase: p3, register: authoring_decisions, key: 'Hold what a book, a work and a further edition must contain'}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: The checking contracts hold their descriptions.
  - capability: Check what the catalog records
    source_finding: {phase: p3, register: authoring_decisions, key: Check what the catalog records}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: Each registration act checks the record it writes.
  - capability: Record the subject callers supply
    source_finding: {phase: p3, register: authoring_decisions, key: Record the subject callers supply}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: The register act reads the subject where callers send it.
  - capability: Register a copy as registered
    source_finding: {phase: p3, register: authoring_decisions, key: Register a copy as registered}
    status: CRITICAL
    gap_register_entry: GAP-06
    notes: The copy contract writes the state itself.
  - capability: Keep a corrected record's state, and check it against the book description
    source_finding: {phase: p3, register: authoring_decisions, key: 'Keep a corrected record''s state, and check it against the book description'}
    status: CRITICAL
    gap_register_entry: GAP-07
    notes: The correction keeps the state and refuses a record that fails the description.
  - capability: Admit a request without the rules the catalog holds
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a request without the rules the catalog holds}
    status: CRITICAL
    gap_register_entry: GAP-08
    notes: The gates stop requiring what the catalog holds and what no act reads.
  dependency_graph:
  - from: catalog
    to: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    dependency_type: platform transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Refusing on a list of rules}
  - from: catalog
    to: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    dependency_type: platform transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Checking a record's structure}
  - from: catalog
    to: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    dependency_type: platform transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Assembling a record from fields}
  - from: catalog
    to: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Confirming staff}
  - from: catalog
    to: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Checking a submission}
  - from: catalog
    to: book_library_mgmt::CC_REGISTER_BOOK_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Recording a book}
  - from: catalog
    to: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Recording an edition}
  - from: catalog
    to: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Recording a copy}
  - from: catalog
    to: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Correcting a record}
  constraint_register:
  - number: '1'
    constraint: Every correct request from authorized staff is admitted, with the same outcome as today.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: The business author
  - number: '2'
    constraint: Records made under a request's own rules stay as they were made.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: The business author
  - number: '3'
    constraint: What a request says about the catalog's rules is ignored, not refused.
    source_finding: {phase: p1, register: known_facts, row: 9}
    source: The business author
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse anyone the library has not authorized}
    capability: Refuse anyone the library has not authorized
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse a registration the catalog finds incomplete}
    capability: Refuse a registration the catalog finds incomplete
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: 'Hold what a book, a work and a further edition must contain'}
    capability: Hold what a book, a work and a further edition must contain
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: Check what the catalog records}
    capability: Check what the catalog records
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, key: Record the subject callers supply}
    capability: Record the subject callers supply
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, key: Register a copy as registered}
    capability: Register a copy as registered
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, key: 'Keep a corrected record''s state, and check it against the book description'}
    capability: Keep a corrected record's state, and check it against the book description
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-08
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a request without the rules the catalog holds}
    capability: Admit a request without the rules the catalog holds
    owner_subdomain: catalog
    resolution: EXTEND
  - gap_code: GAP-09
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
    capability: Establish who a caller is
    owner_subdomain: outside the catalog
    resolution: DEFERRED
  design_decisions:
  - number: '1'
    decision: Each rule is held by the step that applies it, as a fixed value.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
    rationale: A rule written where it is applied holds for every act that composes the step, and no request can widen it.
    constraints_imposed: Nothing may hand the catalog a rule the catalog holds.
  - number: '2'
    decision: Each check is followed by a rule refusing when it found anything.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
    rationale: The platform check stays a reporter, as ruled; the catalog's contract decides.
    constraints_imposed: A check's report is consumed, never left unread.
  - number: '3'
    decision: What each registration checks is the record it writes.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: A check of a supplied copy judges something other than what is recorded.
    constraints_imposed: No registration checks a copy supplied beside the record.
  - number: '4'
    decision: The register act records the subject where callers send it.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: Every present caller sends it there, and every book recorded today lacks one.
    constraints_imposed: No present caller changes what it sends.
  - number: '5'
    decision: A copy's registered state and a correction's state are the catalog's own.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
    rationale: There is one state a copy is registered in, and a correction does not change state.
    constraints_imposed: No request sets a registered copy's or a corrected book's state.
  - number: '6'
    decision: The gates stop requiring what the catalog holds and what no act reads.
    source_finding: {phase: p3, register: analysis_findings, key: Q8}
    rationale: A gate requiring an unread field refuses a correct request for its absence.
    constraints_imposed: Every field an act reads stays required where it was.
  - number: '7'
    decision: Records made before this change are left as they are.
    source_finding: {phase: p3, register: analysis_findings, key: Q10}
    rationale: The record is added to and never rewritten.
    constraints_imposed: No migration, backfill or repair step may be authored.
  authoring_scope:
  - capability: Refuse anyone the library has not authorized
    gap_register_ref: GAP-01
  - capability: Refuse a registration the catalog finds incomplete
    gap_register_ref: GAP-02
  - capability: Hold what a book, a work and a further edition must contain
    gap_register_ref: GAP-03
  - capability: Check what the catalog records
    gap_register_ref: GAP-04
  - capability: Record the subject callers supply
    gap_register_ref: GAP-05
  - capability: Register a copy as registered
    gap_register_ref: GAP-06
  - capability: Keep a corrected record's state, and check it against the book description
    gap_register_ref: GAP-07
  - capability: Admit a request without the rules the catalog holds
    gap_register_ref: GAP-08
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. Every capability that changes
is an extension of one the catalog already has: each step keeps doing what it does, and holds the
rule it applies instead of being handed it.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

## 2. Capability Graph (capability_graph)

## 3. Dependency Graph (dependency_graph)

## 4. Constraint Register (constraint_register)

## 5. Gap Register (gap_register)

## 6. Design Decisions (design_decisions)

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Establish who a caller is | GAP-09. The credentials a request presents are its own; the catalog holds the rules they are judged by and does not authenticate them. |
| Records made under a request's own rules | Declined by the business: the record is added to and never rewritten. |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | PENDING |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · constraints · business_invariants · authority_boundaries · out_of_scope |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · pps_baseline_fqdns |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
