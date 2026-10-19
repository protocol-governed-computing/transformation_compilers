# Governance Intent — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
document:
  phase: p6
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_01_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Register a book together with its first physical copy
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Register a further physical copy against a registered book
    owner_subdomain: catalog
    disposition: SHARED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Update a book's bibliographic information
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Retire a book record
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Retire a physical copy
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-09}
  - capability: Return a retired book record to the registered state
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-10}
  - capability: Return a retired physical copy to the registered state
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-11}
  - capability: Search the catalog by subject or title
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-12}
  - capability: Retrieve a book's complete details with the copies held
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-13}
  - capability: Confirm the staff member performing an operation is authorized
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Record every performed catalog operation in the catalog's own audit trail
    owner_subdomain: catalog
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Read every book record so that a search can select among them by content
    owner_subdomain: platform
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-17}
  - capability: Hold a durable record that can be read, listed and updated in place
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Hold a book record durably and update it in place}
  - capability: Claim a value once so a second claim on it fails
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: ''
    source_finding: {phase: p3, register: authoring_decisions, key: 'Enforce that one book exists per title, author and publication year'}
  - capability: Append an entry to a trail that cannot be amended
    owner_subdomain: platform
    disposition: UNRESOLVED
    existing_artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Append an entry to an append-only trail}
  - capability: Assemble a durable record from supplied values
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Assemble a catalog record from supplied values}
  - capability: Confirm a record carries the fields its contract declares
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm a catalog record carries its required fields}
  - capability: Select the records matching stated criteria
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Select the catalog records matching stated criteria}
  - capability: Confirm supplied parameters satisfy declared rules
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm the parameters supplied to a catalog operation satisfy their declared rules}
  - capability: Deciding which staff are authorized
    owner_subdomain: staff
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  - capability: Deleting a catalog record
    owner_subdomain: catalog
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p1, register: business_invariants, row: 9}
  storage_governance: null
  cross_subdomain_deps:
  - dependency: Read whether a staff member is authorized to perform catalog operations
    direction: catalog → staff
    existing_artifact: ''
    status: SATISFIED
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  pps_artifacts_requiring_action:
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    current_status: Declared and in use by ai_governance and workload
    action: EXTEND
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    current_status: Declared and in use by ai_governance
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    current_status: Declared and in use by ai_governance
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_side_effects::CS_APPENDONLY_JSONL_V0'}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    current_status: Declared, no current consumer
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    current_status: Declared, no current consumer
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - fqdn: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    current_status: Declared, no current consumer
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_transforms::CT_PURE_FILTER_RECORDS_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    current_status: Declared and in use by ai_governance
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0'}
  boundary_rules:
  - rule_name: CATALOG_OWNS_ITS_STORES
    statement: Every store the catalog reads or writes is declared by the catalog, and no catalog operation writes into a store another subdomain owns.
    source_finding: {phase: p4, register: constraint_register, row: 12}
  - rule_name: AUTHORIZATION_IS_READ_NEVER_GRANTED
    statement: The catalog confirms a staff member is authorized on every operation and grants authorization nowhere.
    source_finding: {phase: p4, register: design_decisions, row: 8}
  - rule_name: NO_RECORD_IS_DELETED
    statement: No catalog operation removes a record. Retirement is the only way a record leaves use, and it is reversible.
    source_finding: {phase: p1, register: business_invariants, row: 9}
  - rule_name: STATE_IS_DATA_ON_THE_RECORD
    statement: A record's registered-or-retired state is held as data on the record, never implied by which store it occupies.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - rule_name: RETIREMENT_NEVER_CASCADES
    statement: Retiring a book leaves its copies untouched and retiring the last copy leaves the book registered; no state change is derived from another.
    source_finding: {phase: p4, register: design_decisions, row: 7}
  - rule_name: EVERY_OPERATION_IS_APPENDED
    statement: Every performed catalog operation appends one entry to the catalog's own trail, including searches and retrievals.
    source_finding: {phase: p1, register: business_invariants, row: 7}
  - rule_name: READS_RAISE_NO_EVENT
    statement: Searching and retrieving are audited but recognise no business moment, because nothing reacts to a read.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  governance_outcome:
  - capability: Register a book together with its first physical copy
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Register a book together with its first physical copy}
  - capability: Register a further physical copy against a registered book
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Register a further physical copy against a registered book}
  - capability: Update a book's bibliographic information
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Update a book's bibliographic information}
  - capability: Retire a book record
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Retire a book record}
  - capability: Retire a physical copy
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Retire a physical copy}
  - capability: Return a retired book record to the registered state
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Return a retired book record to the registered state}
  - capability: Return a retired physical copy to the registered state
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Return a retired physical copy to the registered state}
  - capability: Search the catalog by subject or title
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Search the catalog by subject or title}
  - capability: Retrieve a book's complete details with the copies held
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Retrieve a book's complete details with the copies held}
  - capability: Confirm the staff member performing an operation is authorized
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Confirm the staff member performing an operation is authorized}
  - capability: Record every performed catalog operation in the catalog's own audit trail
    owner_subdomain: catalog
    source_finding: {phase: p6, register: ownership, key: Record every performed catalog operation in the catalog's own audit trail}
```

> Every register below is present and correctly shaped. Each is missing the one cell that carries the decision the phase exists to record, or hedges it.

---

## Domain Placement

| Field | Value |
| --- | --- |
| Domain | `book_library_mgmt` |
| Primary subdomain | `catalog` — NEW — declared by this CR |
| Authority class | new actor type: the authorized library staff member |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

The catalog stands alone rather than nesting under an existing subdomain because nothing in the
composition describes what a library holds: there is no boundary to extend, and the nine remaining
project functions do not exist yet to nest beneath. A new actor type is required because the one
business actor in the composition names another subdomain's employee and asserts no authorization to
perform catalog operations.

---

## 1. Subdomain Boundary — Ownership

Eleven capabilities are owned by the catalog and authored by this change. Seven are satisfied by
mechanisms the platform already declares, reused as-is. Two are deferred: one to a function that does
not exist yet, and one that will never exist because a record is never deleted.

---

## 2. Storage Governance Requirements

Every store named here is owned by the catalog and written only by the catalog's own operations.

---

## 3. Cross-Subdomain Dependency Declaration

The catalog reads authorization and never grants it, so the capability that decides who is authorized
is a gap owned by the staff function rather than work this change performs. No catalog operation
writes into a store another subdomain owns, and no capability contract from another subdomain is
called.

---

## 4. PPS Artifacts Requiring Action

Every artifact is read, never modified, so no consumer of any of them is affected by this change.

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
