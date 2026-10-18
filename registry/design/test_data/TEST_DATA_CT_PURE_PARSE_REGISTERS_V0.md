# TEST_DATA_CT_PURE_PARSE_REGISTERS_V0

## 1. Intent

A phase document is read into its header, its prose sections and its registers, adding and deciding nothing.

---

## Machine

```yaml
fqdn: transformation::TEST_DATA_CT_PURE_PARSE_REGISTERS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: design
target: transformation::CT_PURE_PARSE_REGISTERS_V0
cases:
- case_id: reads_header_registers_and_sections
  expected_outcome: SUCCESS
  bindings:
    document_text: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain:\
      \ d\n  subdomain: s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n\
      \  out_of_scope:\n  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n\
      ```\n\n## 12. Out of Scope\n\nNothing else.\n"
  expected:
    header:
      phase: p0
      domain: d
      subdomain: s
      cr: c
      rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
    sections:
    - number: 12
      title: Out of Scope
      text: '

        Nothing else.'
    registers:
    - id: out_of_scope
      value:
      - item: Fines
        reason: Not in this release.
    - id: clarification_requests
      value: null
```
