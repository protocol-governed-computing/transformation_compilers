# Stage 8 — Authoring Mandate: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p8
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_01_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::RB_CATALOG_BINDINGS_V0
  - wave: '1'
    step: '2'
    code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '3'
    code: book_library_mgmt::AC_LIBRARY_STAFF_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '4'
    code: book_library_mgmt::EV_BOOK_REGISTERED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '5'
    code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '6'
    code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '7'
    code: book_library_mgmt::EV_BOOK_RETIRED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '1'
    step: '8'
    code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '2'
    step: '9'
    code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
  - wave: '2'
    step: '10'
    code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    - capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
  - wave: '2'
    step: '11'
    code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    - capability_side_effects::CS_REGISTRY_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '12'
    code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_side_effects::CS_REGISTRY_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '13'
    code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_side_effects::CS_REGISTRY_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '14'
    code: book_library_mgmt::CC_REGISTER_BOOK_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '15'
    code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '17'
    code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '18'
    code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '19'
    code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '20'
    code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '21'
    code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_transforms::CT_PURE_FILTER_RECORDS_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '22'
    code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_transforms::CT_PURE_FILTER_RECORDS_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '2'
    step: '23'
    code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - wave: '3'
    step: '24'
    code: book_library_mgmt::IN_REGISTER_BOOK_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '3'
    step: '25'
    code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '3'
    step: '26'
    code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '3'
    step: '27'
    code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '3'
    step: '28'
    code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '3'
    step: '29'
    code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '3'
    step: '30'
    code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '3'
    step: '31'
    code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '3'
    step: '32'
    code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    action: NEW
    subdomain: catalog
    depends_on: null
  - wave: '4'
    step: '33'
    code: book_library_mgmt::WF_REGISTER_BOOK_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_REGISTER_BOOK_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    - book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    - book_library_mgmt::CC_REGISTER_BOOK_V0
    - book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    - book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
  - wave: '4'
    step: '34'
    code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    - book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
  - wave: '4'
    step: '35'
    code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    - book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
  - wave: '4'
    step: '36'
    code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - book_library_mgmt::EV_BOOK_RETIRED_V0
  - wave: '4'
    step: '37'
    code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
  - wave: '4'
    step: '38'
    code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
  - wave: '4'
    step: '39'
    code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
  - wave: '4'
    step: '40'
    code: book_library_mgmt::WF_SEARCH_CATALOG_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_SEARCH_CATALOG_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_SEARCH_CATALOG_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '4'
    step: '41'
    code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    - book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    - book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - wave: '5'
    step: '42'
    code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    action: NEW
    subdomain: catalog
    depends_on:
    - book_library_mgmt::WF_REGISTER_BOOK_V0
    - book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    - book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    - book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    - book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    - book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    - book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    - book_library_mgmt::WF_SEARCH_CATALOG_V0
    - book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    - book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  critical_path:
  - position: '1'
    code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - position: '2'
    code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
  - position: '3'
    code: book_library_mgmt::WF_REGISTER_BOOK_V0
  - position: '4'
    code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
  mandate_artifact_summary:
  - action: NEW
    count: '40'
    description: 1 AC, 9 IN, 9 WF, 13 CC, 1 CT, 5 EV, 1 RB, 1 STRUCTURE — every identity Stage 7 assigned
  - action: EXTEND
    count: '1'
    description: capability_side_effects::CS_MUTABLE_JSON_V0 gains an operation that publishes records; authored in the platform, not scheduled here
  field_declarations:
  - code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::AC_LIBRARY_STAFF_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BOOK_REGISTERED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_BOOK_RETIRED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_SEARCH_CATALOG_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    subdomain_field: catalog
  new_capabilities:
  - code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    purpose: Form the single key the registry claims from a book's three identifying attributes, so that a second registration of the same book is refused
    inputs: title:string, author:string, publication_year:integer
    outputs: identity_key:string
  new_intents:
  - code: book_library_mgmt::IN_REGISTER_BOOK_V0
    purpose: Admit a request to register a book together with its first physical copy
    workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    inputs: staff_credentials:object, authorization_rules:array, title:string, author:string, publication_year:integer, book_fields:object, book_schema:object, barcode:string, copy_fields:object, staff_id:string
  - code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    purpose: Admit a request to register a further copy against a registered book
    workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    inputs: staff_credentials:object, authorization_rules:array, identity_key:string, barcode:string, copy_fields:object, staff_id:string
  - code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    purpose: Admit a request to change a registered book's description
    workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    inputs: staff_credentials:object, authorization_rules:array, title:string, author:string, publication_year:integer, updated_fields:object, staff_id:string
  - code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    purpose: Admit a request to retire a book record judged obsolete
    workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    inputs: staff_credentials:object, authorization_rules:array, identity_key:string, staff_id:string
  - code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    purpose: Admit a request to retire a lost or damaged copy
    workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    inputs: staff_credentials:object, authorization_rules:array, barcode:string, staff_id:string
  - code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    purpose: Admit a request to return a retired book record to the registered state
    workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    inputs: staff_credentials:object, authorization_rules:array, identity_key:string, staff_id:string
  - code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    purpose: Admit a request to return a retired copy to the registered state
    workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    inputs: staff_credentials:object, authorization_rules:array, barcode:string, staff_id:string
  - code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    purpose: Admit a request to locate material by subject or by title
    workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    inputs: staff_credentials:object, authorization_rules:array, search_criteria:object, staff_id:string
  - code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    purpose: Admit a request for a book's complete details with the copies held
    workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    inputs: staff_credentials:object, authorization_rules:array, identity_key:string, staff_id:string
  cross_subdomain_notes:
  - code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    note: Reads whether the staff member is authorized from what the caller supplies, and grants nothing. Deciding who is authorized is a dependency gap owned by the staff function, which a future change request introduces. No store of authorized staff is declared here.
  - code: capability_side_effects::CS_MUTABLE_JSON_V0
    note: 'Extended by this change with an operation that publishes records. A platform artifact amended by a business change request: additive, so none of its twelve consumers is affected, and authored in the platform repository rather than scheduled in this mandate.'
```

The forty artifacts Stage 7 designed, scheduled in dependency order. Nothing is added here and nothing
is dropped: the mandate orders the build, it does not decide it.

---

## 1. Build Dependency Order

Wave 1 depends on nothing: the store declaration, the identity transform, the actor and the five
business moments. Wave 2 composes the thirteen capability contracts over those and over the platform
mechanisms reused as-is. Wave 3 declares the nine entry points. Wave 4 wires the nine workflows, each
over its own entry point, its contracts and the moments it recognises. Wave 5 is the runtime binding,
which binds every workflow and therefore comes last.

The platform's `capability_side_effects::CS_MUTABLE_JSON_V0` is extended, not authored, so it is
not a step here — it already exists in the composition, and a mandate schedules only what does not.
It is recorded in §3 and §7.

---

## 2. Critical Path

The longest chain runs store declaration → identity claim → the registration workflow → the runtime
binding. Nothing in the catalog can be exercised until that chain is complete.

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

No catalog artifact writes into a store another subdomain owns.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | p7_design_intent_book_library_mgmt_catalog_v0.md | GATE 1 APPROVED |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
| Artifact Authoring | per build_order | PENDING |
