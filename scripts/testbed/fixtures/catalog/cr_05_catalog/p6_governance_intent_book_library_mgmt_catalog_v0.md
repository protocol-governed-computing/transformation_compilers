# Stage 6 — Governance Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p6
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_05_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Refuse anyone the library has not authorized
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Refuse anyone the library has not authorized}
  - capability: Refuse a registration the catalog finds incomplete
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Refuse a registration the catalog finds incomplete}
  - capability: Hold what a book, a work and a further edition must contain
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: 'Hold what a book, a work and a further edition must contain'}
  - capability: Check what the catalog records
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Check what the catalog records}
  - capability: Record the subject callers supply
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Record the subject callers supply}
  - capability: Register a copy as registered
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Register a copy as registered}
  - capability: Keep a corrected record's state, and check it against the book description
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: 'Keep a corrected record''s state, and check it against the book description'}
  - capability: Admit a request without the rules the catalog holds
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Admit a request without the rules the catalog holds}
  - capability: Establish who a caller is
    owner_subdomain: outside the catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Establish who a caller is}
  - capability: Records made under a request's own rules
    owner_subdomain: nowhere; the business declines to rewrite them
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Records made under a request's own rules}
  storage_governance:
  - storage_need: A durable record of every book, with its bibliographic information and state
    purpose: 'Unchanged by this change, and named because what may be written into it changes: a book only as described, with its subject, and a correction only with the state the record has'
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, key: Book record}
  - storage_need: A durable record of every physical copy and its state
    purpose: Unchanged by this change, and named because a copy is written only as registered
    subdomain: catalog
    source_finding: {phase: p5, register: business_objects, key: Copy record}
  cross_subdomain_deps:
  - dependency: Refusing on a list of rules
    direction: catalog -> platform
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0'}
  - dependency: Checking a record's structure
    direction: catalog -> platform
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - dependency: Assembling a record from fields
    direction: catalog -> platform
    existing_artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0'}
  pps_artifacts_requiring_action:
  - fqdn: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    current_status: Present; takes its rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: Confirming staff}
  - fqdn: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    current_status: Present; takes its descriptions from the request and refuses nothing its checks find
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: Checking a submission}
  - fqdn: book_library_mgmt::CC_REGISTER_BOOK_V0
    current_status: Present; takes its description from the request and ignores what its check finds
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: Recording a book}
  - fqdn: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    current_status: Present; takes its description from the request and ignores what its check finds
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: Recording an edition}
  - fqdn: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    current_status: Present; records the copy in the state the request gives
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: Recording a copy}
  - fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    current_status: Present; writes the state the request gives and checks no description
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: Correcting a record}
  - fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::WF_SEARCH_CATALOG_V0
    current_status: Present; binds the rules from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::IN_REGISTER_BOOK_V0
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::IN_SEARCH_CATALOG_V0
    current_status: Present; requires the rules the catalog will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten gates}
  - fqdn: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_RESOLVE_WORK_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  - fqdn: book_library_mgmt::CC_SEARCH_CATALOG_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The ten acts}
  boundary_rules:
  - rule_name: A_RULE_IS_HELD_WHERE_IT_IS_APPLIED
    statement: Each of the catalog's rules is a fixed value of the step that applies it. No act and no request hands the catalog a rule.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - rule_name: A_CHECK_THAT_FINDS_REFUSES
    statement: A check's report is consumed by a rule that refuses when it found anything. The platform check reports; the catalog decides.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: WHAT_IS_CHECKED_IS_WHAT_IS_RECORDED
    statement: Each registration checks the record it writes, never a copy supplied beside it.
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - rule_name: THE_SUBJECT_IS_THE_ONE_SUPPLIED
    statement: The register act records the subject where callers send it.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - rule_name: STATE_IS_THE_CATALOGS
    statement: A copy is registered as registered, and a correction keeps the state the record has.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - rule_name: A_GATE_REQUIRES_WHAT_IS_READ
    statement: A gate requires what its act reads, and nothing the catalog holds or no act reads.
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - rule_name: THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN
    statement: Records made before this change are left as they are.
    source_finding: {phase: p4, register: design_decisions, row: 7}
  governance_outcome:
  - capability: Refuse anyone the library has not authorized
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Refuse anyone the library has not authorized}
  - capability: Refuse a registration the catalog finds incomplete
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Refuse a registration the catalog finds incomplete}
  - capability: Hold what a book, a work and a further edition must contain
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: 'Hold what a book, a work and a further edition must contain'}
  - capability: Check what the catalog records
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Check what the catalog records}
  - capability: Record the subject callers supply
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Record the subject callers supply}
  - capability: Register a copy as registered
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Register a copy as registered}
  - capability: Keep a corrected record's state, and check it against the book description
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: 'Keep a corrected record''s state, and check it against the book description'}
  - capability: Admit a request without the rules the catalog holds
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Admit a request without the rules the catalog holds}
```

Placement of rules. Nothing moves and nothing is added: every step that changes already belongs to
the catalog. What is placed here is each of the catalog's rules, with the step that applies it, so
that the catalog holds them however it is reached.

---

## 1. Ownership

---

## 2. Storage Governance

---

## 3. Cross-Subdomain Dependencies

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
