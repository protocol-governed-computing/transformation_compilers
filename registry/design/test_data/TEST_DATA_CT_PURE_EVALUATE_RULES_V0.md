# TEST_DATA_CT_PURE_EVALUATE_RULES_V0

## 1. Intent

A rule set is applied whole: a failed rule is reported with its identity, place, detail and intent, and a document failing none is admissible.

---

## Machine

```yaml
fqdn: transformation::TEST_DATA_CT_PURE_EVALUATE_RULES_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: design
target: transformation::CT_PURE_EVALUATE_RULES_V0
cases:
- case_id: finds_an_absent_register
  expected_outcome: SUCCESS
  bindings:
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
    document_text: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain:\
      \ d\n  subdomain: s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n\
      \  out_of_scope:\n  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n\
      ```\n\n## 12. Out of Scope\n\nNothing else.\n"
    rule_set:
    - id: REGISTER_MISSING
      identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/cr_type/x-derived/TABLE_PRESENT
      check: TABLE_PRESENT
      register: cr_type
      intent: a declared register must be present and readable as rows
    observed: {}
    priors: {}
  expected:
    verdict: INADMISSIBLE
    findings:
    - code: REGISTER_MISSING
      rule: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/cr_type/x-derived/TABLE_PRESENT
      locator:
        register: cr_type
        row: null
        field: null
      detail: declared register is absent from the document
      intent: a declared register must be present and readable as rows
    rules_evaluated: 1
- case_id: admits_a_present_register
  expected_outcome: SUCCESS
  bindings:
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
    document_text: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain:\
      \ d\n  subdomain: s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n\
      \  out_of_scope:\n  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n\
      ```\n\n## 12. Out of Scope\n\nNothing else.\n"
    rule_set:
    - id: REGISTER_MISSING
      identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/out_of_scope/x-derived/TABLE_PRESENT
      check: TABLE_PRESENT
      register: out_of_scope
      intent: a declared register must be present and readable as rows
    observed: {}
    priors: {}
  expected:
    verdict: ADMISSIBLE
    findings: []
    rules_evaluated: 1
```
