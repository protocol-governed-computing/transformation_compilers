# Stage 3 — Analysis Loop: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p3
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_01_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: 'S2 discovery_concerns #1'
    finding: The only composed audit step belongs to another subdomain and appends into that subdomain's store, so reusing it would breach a subdomain's exclusive ownership of its stores. The catalog owns its audit composition and its own append-only store, and reuses the append-only mechanism beneath them.
    impact: Two artifacts authored rather than one reused; library traceability stays independent of agent-governance semantics.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0 binds capability_side_effects::CS_APPENDONLY_JSONL_V0 and writes through ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1; si.artifact.refs reports 7 direct references, all ai_governance. Decided by the business owner.
  - question_id: 'S2 discovery_concerns #2'
    finding: The available uniqueness mechanism keys on a single value while a book is identified by title, author and publication year together. The registry is reused with a key formed from the three attributes; forming that key is a catalog business rule, not a change to the registry.
    impact: Duplicate prevention keeps an atomic register-if-absent guarantee; no side effect is modified, so nothing that depends on the registry is disturbed.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_side_effects::CS_REGISTRY_V0 publishes REGISTER, RESOLVE, EXISTS, COUNT, DEREGISTER; si.topology.impact reports 19 impacted artifacts across ai_governance. Decided by the business owner.
  - question_id: 'S2 discovery_concerns #3'
    finding: Because a record moves from retired back to registered, state must be held as data on the record rather than implied by the store it occupies.
    impact: The record store must support update in place, which the available durable-record mechanism does.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_side_effects::CS_MUTABLE_JSON_V0 publishes WRITE, READ, LIST, EXISTS, UPDATE_WHERE, DELETE, DELETE_MANY.
  - question_id: 'S2 discovery_concerns #4'
    finding: Search excludes retired books while retrieval does not, so the same records are read under two rules. Selection by stated criteria covers both, with the state as one criterion.
    impact: No separate mechanism is needed for the two read paths.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0 selects records matching stated criteria.
  - question_id: 'S2 discovery_concerns #5'
    finding: The one business actor available names an employee of another subdomain and asserts no authorization, so the catalog authors its own actor and its own authorization check while deciding who is authorized remains deferred.
    impact: One actor and one check authored; the catalog reads authorization and never grants it.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: ai_governance::AC_EMPLOYEE_V1 exists and carries no authorization assertion; si.topology.impact reports 0 impacted artifacts.
  - question_id: 'S2 gaps #7'
    finding: Subject is free text, so no value-set validation applies and search by kind is only as consistent as what staff type.
    impact: One fewer reuse candidate; nothing further to author.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: The business owner stated subject is free text; capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 therefore serves no requested outcome.
  - question_id: S2 business_processes Search the catalog
    finding: 'Searching by subject or title needs the book records themselves, and the durable-record mechanism publishes only keys: LIST declares no input and yields keys, UPDATE_WHERE filters but only in order to update, and no operation returns records by content. The mechanism is extended with an operation that publishes the records, which the implementation behind it already produced.'
    impact: One additive operation on a platform side effect; the selection stays with the catalog, which is where the criteria are business knowledge.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_side_effects::CS_MUTABLE_JSON_V0 publishes LIST with input [] and output [result_status, keys]; si.topology.impact reports 12 impacted artifacts. Decided by the business owner.
  - question_id: S1 constraints — business policy limits
    finding: No limit on copies per book, no retention period on retired records and no limit on subjects per book were stated. Nothing further constrains the design.
    impact: No constraint rows are added at Stage 4 beyond those Stage 1 carried.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: Confirmed by the business owner at this stage.
  verification_results:
  - item: book_library_mgmt does not appear to be part of the current software baseline.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: 'Re-read at this stage: si.artifact.list for domain book_library_mgmt returns nothing, and si.snapshot.summary reports five domains — ai_governance, inspection, platform, transformation, workload — over 292 artifacts.'
  - item: No capability in the current composition manages a library catalog.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: 'Re-read at this stage: si.vocab.search returns no identity for book, copy, barcode, subject or title; si.store.list reports five declared stores, none holding library records.'
  - item: Durable records can be held, read, listed and updated in place by a declared side effect.
    origin: {phase: p2, register: architectural_observations, row: 2}
    result: CONFIRMED
    evidence: capability_side_effects::CS_MUTABLE_JSON_V0 publishes WRITE, READ, LIST, EXISTS, UPDATE_WHERE, DELETE, DELETE_MANY.
  - item: Uniqueness is available as a declared side effect, keyed on a single value.
    origin: {phase: p2, register: architectural_observations, row: 3}
    result: CONFIRMED
    evidence: capability_side_effects::CS_REGISTRY_V0 publishes REGISTER, RESOLVE, EXISTS, COUNT, DEREGISTER — one key per registration.
  - item: Pure transforms exist for assembling a record, validating its shape and selecting records by criteria.
    origin: {phase: p2, register: architectural_observations, row: 4}
    result: CONFIRMED
    evidence: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and capability_transforms::CT_PURE_FILTER_RECORDS_V0 are carried by the composition's artifact index.
  - item: A business subdomain declares its own stores and binds its own workflows to them.
    origin: {phase: p2, register: architectural_observations, row: 1}
    result: CONFIRMED
    evidence: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1 declares that subdomain's stores; ai_governance::RB_LICENSE_BINDINGS_V1 binds its surface.
  dependency_discoveries:
  - dependency: capability_side_effects::CS_MUTABLE_JSON_V0
    type: Durable record storage
    disposition: REUSE
    evidence: Publishes update in place, which reinstatement requires.
  - dependency: capability_side_effects::CS_REGISTRY_V0
    type: Uniqueness
    disposition: REUSE
    evidence: Publishes register-if-absent, keyed on one value formed from the three identifying attributes.
  - dependency: capability_side_effects::CS_APPENDONLY_JSONL_V0
    type: Append-only trail
    disposition: REUSE
    evidence: Publishes APPEND and GET_ALL; si.topology.impact reports 21 impacted artifacts.
  - dependency: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    type: Record assembly
    disposition: REUSE
    evidence: Assembles a durable record from supplied values; 0 impacted artifacts.
  - dependency: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    type: Record shape validation
    disposition: REUSE
    evidence: Confirms a record carries its declared fields; 0 impacted artifacts.
  - dependency: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    type: Record selection
    disposition: REUSE
    evidence: Selects records matching stated criteria; 0 impacted artifacts.
  - dependency: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    type: Parameter validation
    disposition: REUSE
    evidence: Confirms supplied parameters satisfy declared rules; si.topology.impact reports 7 impacted artifacts.
  - dependency: The catalog's own append-only audit store
    type: Store declaration
    disposition: AUTHOR_NEW
    evidence: No store in the composition holds catalog records or catalog audit entries.
  - dependency: The catalog's own audit composition
    type: Governed operation step
    disposition: AUTHOR_NEW
    evidence: The only composed audit step writes through another subdomain's store declaration.
  - dependency: A library staff actor
    type: Business actor
    disposition: AUTHOR_NEW
    evidence: ai_governance::AC_EMPLOYEE_V1 names another subdomain's employee and asserts no authorization.
  - dependency: Nine catalog operations, their entry points and their business moments
    type: Governed operation surface
    disposition: AUTHOR_NEW
    evidence: Semantic vocabulary search returns no library identity of any kind.
  impact_analysis:
  - artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    impact_scope: ai_governance, workload
    consumer_count: '12'
    evidence: si.topology.impact impacted_count 12, impacted_namespaces ai_governance and workload; si.artifact.refs ref_count 4
  - artifact: capability_side_effects::CS_REGISTRY_V0
    impact_scope: ai_governance
    consumer_count: '19'
    evidence: si.topology.impact impacted_count 19, impacted_namespaces ai_governance; si.artifact.refs ref_count 6
  - artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
    impact_scope: ai_governance
    consumer_count: '21'
    evidence: si.topology.impact impacted_count 21, impacted_namespaces ai_governance; si.artifact.refs ref_count 5
  - artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    impact_scope: none
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
  - artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    impact_scope: none
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
  - artifact: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    impact_scope: none
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
  - artifact: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    impact_scope: ai_governance
    consumer_count: '7'
    evidence: si.topology.impact impacted_count 7, impacted_namespaces ai_governance; si.artifact.refs ref_count 1
  - artifact: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    impact_scope: ai_governance
    consumer_count: '9'
    evidence: si.topology.impact impacted_count 9, impacted_namespaces ai_governance; si.artifact.refs ref_count 7 — examined and not reused
  - artifact: ai_governance::AC_EMPLOYEE_V1
    impact_scope: none
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0 — examined and not reused
  authoring_decisions:
  - capability: Hold a book record durably and update it in place
    decision: REUSE
    rationale: Records must be written, read, listed and updated in place, and state must move both ways on the same record. The declared mechanism does exactly this and is read, not modified.
    alternatives_checked: capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is; capability_side_effects::CS_APPENDONLY_JSONL_V0 was examined and rejected because an append-only trail cannot update a record in place.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
  - capability: Hold a physical copy record durably and update it in place
    decision: REUSE
    rationale: The same durability and in-place update the book record needs, for a record addressed by barcode.
    alternatives_checked: capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
  - capability: Enforce that one book exists per title, author and publication year
    decision: REUSE
    rationale: Register-if-absent gives an atomic uniqueness guarantee. A key formed from the three identifying attributes is a catalog business rule, so nothing about the mechanism changes and nothing depending on it is disturbed.
    alternatives_checked: capability_side_effects::CS_REGISTRY_V0 reused with a composite key; extending it to accept multi-attribute keys was examined and rejected as a change to a side effect 19 artifacts depend on. Decided by the business owner.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
  - capability: Enforce that one physical copy exists per barcode
    decision: REUSE
    rationale: A barcode is a single value, so the registry's own key is the business key with no convention added.
    alternatives_checked: capability_side_effects::CS_REGISTRY_V0 satisfies it as-is.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
  - capability: Assemble a catalog record from supplied values
    decision: REUSE
    rationale: Assembling a durable record from supplied values carries no catalog meaning and is already a pure transform.
    alternatives_checked: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 satisfies it as-is.
    source_finding: {phase: p2, register: architectural_observations, row: 4}
  - capability: Confirm a catalog record carries its required fields
    decision: REUSE
    rationale: Shape validation against a declared contract is mechanism, not business rule; which fields a book requires is stated by the catalog's own contract.
    alternatives_checked: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 satisfies it as-is.
    source_finding: {phase: p2, register: architectural_observations, row: 4}
  - capability: Select the catalog records matching stated criteria
    decision: REUSE
    rationale: Search and retrieval read the same records under different criteria, including the record's state, which selection by stated criteria covers.
    alternatives_checked: capability_transforms::CT_PURE_FILTER_RECORDS_V0 satisfies it as-is.
    source_finding: {phase: p3, register: analysis_findings, row: 4}
  - capability: Confirm the parameters supplied to a catalog operation satisfy their declared rules
    decision: REUSE
    rationale: Parameter validation is mechanism; the rules are declared by the catalog's own operations.
    alternatives_checked: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 satisfies it as-is.
    source_finding: {phase: p2, register: pps_baseline_fqdns, key: Parameter rule validation}
  - capability: Append an entry to an append-only trail
    decision: REUSE
    rationale: The mechanism beneath an audit trail carries no domain meaning and is already declared.
    alternatives_checked: capability_side_effects::CS_APPENDONLY_JSONL_V0 satisfies it as-is.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
  - capability: Record a performed catalog operation in the catalog's audit trail
    decision: AUTHOR_NEW
    rationale: The catalog owns its traceability, so that library auditing does not depend on another subdomain's semantics or write into a store that subdomain owns. The mechanism beneath it is reused.
    alternatives_checked: 'ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0 was examined and rejected: it writes through ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1, and a subdomain owns its stores exclusively. Extending it was rejected as making a licensing artifact depend on library meaning. Decided by the business owner.'
    source_finding: {phase: p3, register: analysis_findings, row: 1}
  - capability: Declare the stores the catalog owns
    decision: AUTHOR_NEW
    rationale: A subdomain declares its own stores; the catalog needs a book store, a copy store and an audit trail of its own.
    alternatives_checked: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1 was examined as the worked form and rejected as another subdomain's declaration.
    source_finding: {phase: p2, register: architectural_observations, row: 1}
  - capability: Bind the catalog's operations to the stores and mechanisms they use
    decision: AUTHOR_NEW
    rationale: Bindings name one subdomain's surface and cannot be shared across subdomains.
    alternatives_checked: ai_governance::RB_LICENSE_BINDINGS_V1 was examined as the worked form and rejected as another subdomain's bindings.
    source_finding: {phase: p2, register: architectural_observations, row: 1}
  - capability: A library staff actor whose authorization a catalog operation binds
    decision: AUTHOR_NEW
    rationale: Every operation is refused unless the staff member is authorized, and nothing existing asserts that authorization.
    alternatives_checked: 'ai_governance::AC_EMPLOYEE_V1 was examined and rejected: it names another subdomain''s employee and asserts no authorization.'
    source_finding: {phase: p3, register: analysis_findings, row: 5}
  - capability: Confirm the staff member performing an operation is authorized
    decision: AUTHOR_NEW
    rationale: The catalog reads authorization on every operation; deciding who is authorized stays deferred to the staff function.
    alternatives_checked: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0 was examined and rejected as a licensing eligibility rule, not an authorization read.
    source_finding: {phase: p3, register: analysis_findings, row: 5}
  - capability: Register a book together with its first physical copy
    decision: AUTHOR_NEW
    rationale: No capability in the composition registers a book; the operation carries the catalog's own refusals and identity rule.
    alternatives_checked: ai_governance::CC_WRITE_LICENSE_V0 was examined as the worked form of a governed operation pipeline and rejected as licensing semantics.
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - capability: Register a further physical copy against a registered book
    decision: AUTHOR_NEW
    rationale: Nothing existing records a copy against a book, and the operation carries the barcode uniqueness and existence refusals.
    alternatives_checked: ai_governance::CC_WRITE_LICENSE_V0 was examined as the worked form and rejected as licensing semantics.
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - capability: Update a book's bibliographic information
    decision: AUTHOR_NEW
    rationale: Nothing existing updates a catalog record, and the operation carries the refusal that an update must not make one book a duplicate of another.
    alternatives_checked: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0 was examined as an in-place update of a governed record and rejected as licensing semantics.
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - capability: Retire a book record
    decision: AUTHOR_NEW
    rationale: Nothing existing retires a catalog record, and retirement must leave the book's copies untouched.
    alternatives_checked: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0 was examined as the worked form of withdrawing a governed record and rejected as licensing semantics.
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - capability: Retire a physical copy
    decision: AUTHOR_NEW
    rationale: Nothing existing retires a copy, and retirement must leave the book record untouched even when it was the last copy.
    alternatives_checked: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0 was examined as the worked form and rejected as licensing semantics.
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - capability: Return a retired book record to the registered state
    decision: AUTHOR_NEW
    rationale: Reinstatement is a business transition the composition has no counterpart for, and it must leave the book's copies untouched.
    alternatives_checked: ai_governance::CC_WRITE_LICENSE_V0 was examined as the worked form of restoring a governed record and rejected as licensing semantics.
    source_finding: {phase: p1, register: lifecycle_transitions, row: 3}
  - capability: Return a retired physical copy to the registered state
    decision: AUTHOR_NEW
    rationale: The same transition for a copy, leaving the book record untouched.
    alternatives_checked: ai_governance::CC_WRITE_LICENSE_V0 was examined as the worked form and rejected as licensing semantics.
    source_finding: {phase: p1, register: lifecycle_transitions, row: 6}
  - capability: Read every book record so that a search can select among them by content
    decision: EXTEND
    rationale: The records must be published before anything can select among them by content. The operation is additive, so no consumer of the mechanism is affected, and the implementation behind it already returned records — only the declaration was keys-only.
    alternatives_checked: capability_side_effects::CS_MUTABLE_JSON_V0 is extended with an operation that publishes records; its LIST was examined and rejected as keys-only, and its UPDATE_WHERE as filtering only in order to update. Decided by the business owner.
    source_finding: {phase: p3, register: analysis_findings, row: 7}
  - capability: Search the catalog by subject or title, excluding retired books
    decision: AUTHOR_NEW
    rationale: Nothing existing searches a catalog; the operation states the criteria and the exclusion, and reuses record selection beneath.
    alternatives_checked: capability_transforms::CT_PURE_FILTER_RECORDS_V0 is reused as the mechanism; no composed search operation exists to reuse.
    source_finding: {phase: p3, register: analysis_findings, row: 4}
  - capability: Retrieve a book's complete details with the copies the library holds
    decision: AUTHOR_NEW
    rationale: Nothing existing reads a book with its copies, and retrieval must serve retired books as well as registered ones.
    alternatives_checked: ai_governance::CC_RESOLVE_LICENSE_V0 was examined as the worked form of a governed read and rejected as licensing semantics.
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - capability: A governed entry point for each catalog operation
    decision: AUTHOR_NEW
    rationale: Each operation is requested through its own governed entry point, and none exists for any catalog operation.
    alternatives_checked: ai_governance::IN_PROVISION_LICENSE_V0 was examined as the worked form and rejected as a licensing request.
    source_finding: {phase: p2, register: pps_baseline_fqdns, key: Business entry point}
  - capability: A business moment for each of the five catalog events
    decision: AUTHOR_NEW
    rationale: Five business moments are declared and none is recognised anywhere in the composition.
    alternatives_checked: ai_governance::EV_LICENSE_PROVISIONED_V1 was examined as the worked form and rejected as a licensing moment.
    source_finding: {phase: p1, register: business_events, key: Book Registered}
  placement_decision:
  - decision: NEW_SUBDOMAIN
    subdomain: catalog
    rationale: The composition carries no artifact in the book_library_mgmt namespace and nothing that manages a library catalog, so there is no subdomain to extend. The catalog is the first of ten functions the project will govern, and the remaining nine are declared adjacent rather than touched.
    source_finding:
    - {phase: p2, register: belief_verification, row: 1}
    - {phase: p1, register: governance_scope, row: 1}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: 'All six CRITICAL gaps carried from Stage 2 have an authoring decision: records, operations, actor, business moments, composite uniqueness and the catalog''s own audit trail.'
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: 'Stage 2 carried one open question, on whether subject is a declared value set; the business owner answered that subject is free text, and it is closed as S3 analysis_findings #6.'
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: The dependency register closed at eleven entries — seven reused, four authored — and re-reading the composition at this stage surfaced no further dependency.
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: Six items re-verified against the composition, all CONFIRMED, none OVERTURNED.
  - criterion: Every INFERRED finding promoted, accepted or carried forward with a reason
    status: SATISFIED
    evidence: Stage 2 carried two INFERRED concerns — that state must be held as data, and that search and retrieval read under different rules. Both are re-grounded here as OBSERVED against the published operations of the mechanisms concerned.
```

Every decision below is grounded in the pinned baseline
`41dd01fb1bc94d57c645f5c7fee1f96a7c4f147c98fa5104a6249ce9e6ea4a1d`, re-read at this stage rather
than inherited from Stage 2. Two compromises could not be settled by evidence and were decided by the
business owner: how the catalog satisfies traceability, and how uniqueness on a three-attribute
identity is enforced.

---

## 1. Analysis Findings

---

## 2. Mandatory Verification Pass

---

## 3. Dependency Discoveries

---

## 4. Impact Analysis

Every reused artifact is read, never modified, so this change adds consumers and disturbs none of the
counts above.

---

## 5. Authoring Decisions

---

## 6. Subdomain Placement Decision

---

## 7. Saturation Assessment

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
