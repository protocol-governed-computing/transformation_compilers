# Stage 8 — Authoring Mandate: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p8
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_02_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '2'
    code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '3'
    code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '4'
    code: book_library_mgmt::EV_WORK_REGISTERED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '2'
    step: '5'
    code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - wave: '2'
    step: '6'
    code: book_library_mgmt::CC_RESOLVE_WORK_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - wave: '2'
    step: '7'
    code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '3'
    step: '8'
    code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '4'
    step: '9'
    code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    - book_library_mgmt::CC_RESOLVE_WORK_V0
    - book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
  critical_path:
  - position: '1'
    code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
  - position: '2'
    code: book_library_mgmt::CC_RESOLVE_WORK_V0
  - position: '3'
    code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
  mandate_artifact_summary:
  - action: NEW
    count: '9'
    description: 3 CT, 1 EV, 3 CC, 1 IN, 1 WF — every identity Stage 7 assigned
  - action: EXTEND
    count: '7'
    description: STRUCTURE_CATALOG_STORAGE_V0, RB_CATALOG_BINDINGS_V0, WF_REGISTER_BOOK_V0, CC_REGISTER_BOOK_V0, CC_VALIDATE_BOOK_SUBMISSION_V0, CC_SEARCH_CATALOG_V0 and CC_ASSEMBLE_BOOK_DETAILS_V0 — amended in place, never authored, because each identity already exists in the composition
  field_declarations:
  - code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_WORK_REGISTERED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RESOLVE_WORK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    subdomain_field: catalog
  - code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  new_capabilities:
  - code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    purpose: Form the single key the registry claims for a work from its title and author, so that two registrations describing the same work resolve to one work
    inputs: title:string, author:string
    outputs: work_key:string
  - code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    purpose: Select the records matching stated criteria and return none when none match, so an edition the library holds no copies of can still be described
    inputs: source:array, filter:object
    outputs: extracted:array
  - code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    purpose: Group records by the value of a named attribute, so a search can answer once per work rather than once per matching edition
    inputs: source:array, attribute:string
    outputs: grouped:array
  new_intents:
  - code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    purpose: Admit a request to register a further edition of a work the catalog already holds
    workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    inputs: staff_credentials:object, authorization_rules:array, staff_id:string, title:string, author:string, publication_year:string, subject:array, edition_fields:object, edition_schema:object, work_fields:object, work_schema:object
  cross_subdomain_notes:
  - code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    note: Reused unchanged. Reads whether the staff member is authorized from what the caller supplies and grants nothing; deciding who is authorized remains a dependency gap owned by the staff function. The operations this change adds reach it first, as every existing operation does.
  - code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    note: Extended, not authored. Gains the WORKS store and the WORK_IDENTITY_REGISTRY store. Both are written only by contracts of this subdomain, and no contract of another subdomain reads or writes either.
  - code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    note: Extended, not authored. Binds the new workflow to the same three substrates and the same storage declaration the catalog already uses; no new substrate is required.
  - code: book_library_mgmt::WF_REGISTER_BOOK_V0
    note: Extended, not authored. Gains one node — the work claim — placed after validation and before every other claim, so every claim still precedes every write.
  - code: book_library_mgmt::CC_REGISTER_BOOK_V0
    note: Extended, not authored. The edition record it assembles now carries the key of the work the edition belongs to; its composition is otherwise unchanged.
  - code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    note: Extended, not authored. Validates the work's identifying attributes alongside the edition's, before any identity is claimed.
  - code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    note: Extended, not authored. Gains a grouping step after its selection step; the records it selects and the terms it accepts are unchanged.
  - code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    note: Extended, not authored. Gains a read of the work record, so a retrieval carries the work the edition belongs to without a second lookup.
  - code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    note: Writes only into stores this subdomain declares. Its claim yields ALREADY_EXISTS when the work is already held, and the registration routes that onward rather than refusing — the one claim in this subdomain whose second attempt is not a refusal.
```

Eight artifacts are scheduled — the eight the design assigns identities to. The seven the design
extends are not build steps: their identities already exist in the composition, and scheduling one
would mandate authoring an artifact that is already there. They are recorded in §3 and §7 instead.

---

## 1. Build Order

Four waves: the transforms and the business moment first, since nothing they need is authored here;
then the contracts that compose them; then the entry point; then the workflow that routes between
them. `CC_REGISTER_ADDITIONAL_EDITION_V0` depends on no new artifact — every capability it composes
is one the composition already carries.

---

## 2. Critical Path

The longest chain runs through the work key: the transform that forms it, the contract that resolves
a work by it, and the workflow that cannot be built until that contract exists.

---

## 3. Artifact Summary

---

## 4. Subdomain Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | p7_design_intent_book_library_mgmt_catalog_v0.md | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring (authoring tier) | per build_order | PENDING |

---

## gov_projection — Governed Handoff to Artifact Authoring

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 7 | new_artifacts · existing_inventory · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · structure_stores · artifact_summary |
| **Emits** → Artifact Authoring | build_order · critical_path · mandate_artifact_summary · field_declarations · new_capabilities · new_intents · cross_subdomain_notes |
