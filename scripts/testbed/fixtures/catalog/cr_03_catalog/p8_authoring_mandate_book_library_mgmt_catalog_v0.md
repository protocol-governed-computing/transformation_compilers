# Stage 8 — Authoring Mandate: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p8
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_03_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order: []
  critical_path: []
  mandate_artifact_summary:
  - action: EXTEND
    count: '6'
    description: The six acts that complete a declared moment, each re-rendered whole so that it announces what it completed. One of them announces three.
  - action: NEW
    count: '0'
    description: The change authors no artifact. All six moments were declared long ago and referenced by nothing; what was missing was the acts saying they had completed them.
  field_declarations:
  - code: book_library_mgmt::WF_REGISTER_BOOK_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    subdomain_field: catalog
  - code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    subdomain_field: catalog
  new_capabilities: []
  new_intents: []
  cross_subdomain_notes: []
```

Mechanical. Stage 7's assignments re-ordered into a build sequence; nothing added, nothing dropped.

---

## 1. Build Dependency Order

---

## 2. Critical Path

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

## Gate 2 — Mandate Approval

**Gate 2 closes here**, and it freezes scope before authoring begins. After it, any departure is an
Approved Deviation recorded in the authoring manifest — never a silent change.

**Status: CLOSED.** Approved by the business author against the composition `9c2c693d882e…`, the one
`baseline.json` pins, after Construction Completeness read 100% on all six acts.

What is frozen is six acts and what each announces. The acts are re-rendered whole from the design,
which is what an EXTEND means, so nothing about them is edited in place and the announcements arrive
with the rendering. **A moment announced by editing a built artifact is outside this mandate** — and
so is a moment the business never declared, which is why neither reinstatement act is here.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 7 — Design Intent | Inventory, topology, bindings, announcements | COMPLETE |
| Stage 8 — Authoring Mandate | This document | PENDING GATE 2 APPROVAL |
