# TEST_DATA_CT_PURE_RENDER_ARTIFACTS_V0

## 1. Intent

The artifacts a mandate schedules are rendered from the design, with the renderer's record of anything it supplied; a mandate scheduling nothing is refused.

---

## Machine

```yaml
fqdn: transformation::TEST_DATA_CT_PURE_RENDER_ARTIFACTS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: build
target: transformation::CT_PURE_RENDER_ARTIFACTS_V0
cases:
- case_id: renders_the_actor_a_mandate_schedules
  expected_outcome: SUCCESS
  bindings:
    design_registers:
    - id: new_artifacts
      value:
      - capability: Reader
        family: AC
        code: AC_READER_V0
        summary: A reader of the catalog
        owner_subdomain: s
        status: NEW
        source_finding:
          source: human
    - id: artifact_properties
      value:
      - artifact: AC_READER_V0
        property: type
        value: human
        source_finding:
          source: human
    - id: interface_fields
      value:
      - artifact: AC_READER_V0
        direction: ATTRIBUTE
        field: role
        type: string
        required: 'YES'
        default: null
        meaning: What the reader does
    mandate_registers:
    - id: build_order
      value:
      - wave: '1'
        code: AC_READER_V0
    - id: field_declarations
      value:
      - code: AC_READER_V0
        subdomain_field: s
  expected:
    artifacts:
    - path: registry/s/actors/AC_READER_V0.md
      domain: AC_READER_V0
      machine:
        fqdn: AC_READER_V0
        artifact_kind: ACTOR
        version: v0
        governed_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0
        authority: pgc.platform
        concern: s
        core:
          summary: A reader of the catalog
          type: human
          attributes:
            role:
              type: string
              required: true
    documents:
    - path: registry/s/actors/AC_READER_V0.md
      text: "# AC_READER_V0\n\n## Machine\n\n```yaml\nfqdn: AC_READER_V0\nartifact_kind: ACTOR\nversion:\
        \ v0\ngoverned_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0\nauthority: pgc.platform\nconcern: s\n\
        core:\n  summary: A reader of the catalog\n  type: human\n  attributes:\n    role:\n      type:\
        \ string\n      required: true\n```\n\n---\n\n## Intent\n\nA reader of the catalog\n"
    artifact_count: 1
    sources:
      AC_READER_V0: {}
- case_id: refuses_a_mandate_scheduling_nothing
  expected_outcome: VIOLATION
  bindings:
    design_registers:
    - id: new_artifacts
      value:
      - capability: Reader
        family: AC
        code: AC_READER_V0
        summary: A reader of the catalog
        owner_subdomain: s
        status: NEW
        source_finding:
          source: human
    - id: artifact_properties
      value:
      - artifact: AC_READER_V0
        property: type
        value: human
        source_finding:
          source: human
    - id: interface_fields
      value:
      - artifact: AC_READER_V0
        direction: ATTRIBUTE
        field: role
        type: string
        required: 'YES'
        default: null
        meaning: What the reader does
    mandate_registers:
    - id: build_order
      value: []
    - id: field_declarations
      value: []
```
