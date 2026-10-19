# Stage 8 — Authoring Mandate: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p8
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_05_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order: null
  critical_path: null
  mandate_artifact_summary:
  - action: EXTEND
    count: '26'
    description: The catalog's six rule-applying contracts, its ten acts and their ten gates, redeclared whole so that the catalog holds every rule it applies and checks what it records.
  field_declarations:
  - code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_SEARCH_CATALOG_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    subdomain_field: catalog
  - code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    subdomain_field: catalog
  new_capabilities:
  - code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    purpose: Confirm the staff member may perform catalog operations
    inputs: staff_credentials
    outputs: is_authorized
  - code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    purpose: Confirms a registration carries what a work and an edition require, before any identity is claimed
    inputs: work_fields, book_fields, barcode
    outputs: valid
  - code: book_library_mgmt::CC_REGISTER_BOOK_V0
    purpose: Validates, assembles and writes an edition record against the work it belongs to
    inputs: book_fields, identity_key
    outputs: book_record
  - code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    purpose: Assembles the edition record against a resolved work and writes it
    inputs: identity_key, edition_fields
    outputs: edition_record
  - code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    purpose: Record a copy against exactly one book
    inputs: identity_key, barcode, copy_fields
    outputs: book_record
  - code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    purpose: Changes a registered edition's descriptive content and refuses a change that would duplicate another edition
    inputs: identity_key, updated_fields
    outputs: book_record
  new_intents:
  - code: book_library_mgmt::IN_REGISTER_BOOK_V0
    purpose: A request to register a book together with its first physical copy
    workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    inputs: staff_credentials, title, author, publication_year, book_fields, barcode, copy_fields, staff_id
  - code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    purpose: The boundary that admits a request to register a further edition of a work the catalog already holds
    workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    inputs: staff_credentials, staff_id, title, author, publication_year, subject
  - code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    purpose: A request to register a further copy against a registered book
    workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    inputs: staff_credentials, identity_key, barcode, copy_fields, staff_id
  - code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    purpose: A request to change a registered book's description
    workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    inputs: staff_credentials, staff_id, identity_key, updated_fields
  - code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    purpose: A request to retire a book record judged obsolete
    workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    inputs: staff_credentials, identity_key, staff_id
  - code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    purpose: A request to return a retired book record to the registered state
    workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    inputs: staff_credentials, identity_key, staff_id
  - code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    purpose: A request to retire a lost or damaged copy
    workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    inputs: staff_credentials, barcode, staff_id
  - code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    purpose: A request to return a retired copy to the registered state
    workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    inputs: staff_credentials, barcode, staff_id
  - code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    purpose: A request for a book's complete details with the copies held
    workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    inputs: staff_credentials, identity_key, staff_id
  - code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    purpose: A request to locate material by subject or by title
    workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    inputs: staff_credentials, search_criteria, staff_id
  cross_subdomain_notes:
  - code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    note: Superseded and not in force; left unchanged. It still names the rules its contract no longer takes, which a superseded act may.
```

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Nothing is created, so nothing is scheduled: the twenty-six redeclared artifacts are authored
whole in their subdomain.

---

## 1. Build Order

---

## 2. Critical Path

---

## 3. Artifact Summary

---

## 4. Field Declarations

---

## 5. New Capabilities

---

## 6. New Intents

---

## 7. Cross-Subdomain Notes
