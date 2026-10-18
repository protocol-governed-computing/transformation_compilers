# TEST_DATA_CT_PURE_MEASURE_COMPLETENESS_V0

## 1. Intent

A design determining every fact its artifacts need is admitted; one leaving facts undetermined is refused.

---

## Machine

```yaml
fqdn: transformation::TEST_DATA_CT_PURE_MEASURE_COMPLETENESS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: build
target: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
cases:
- case_id: admits_a_design_that_determines_its_artifact
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
    threshold: 100.0
    provenance: {}
  expected:
    completeness: 100.0
    determined: 10
    required: 10
    undetermined: []
- case_id: refuses_a_design_that_leaves_facts_undetermined
  expected_outcome: VIOLATION
  bindings:
    design_registers:
    - id: new_artifacts
      value:
      - capability: Storage
        family: STRUCTURE
        code: STRUCTURE_S_STORAGE_V0
        summary: The stores the subdomain owns
        owner_subdomain: s
        status: NEW
        source_finding:
          source: human
    - id: structure_stores
      value: []
    - id: artifact_properties
      value:
      - artifact: STRUCTURE_S_STORAGE_V0
        property: layer
        value: DOMAINS
    mandate_registers:
    - id: build_order
      value:
      - wave: '1'
        code: STRUCTURE_S_STORAGE_V0
    - id: field_declarations
      value:
      - code: STRUCTURE_S_STORAGE_V0
        subdomain_field: s
    threshold: 100.0
    provenance: {}
- case_id: refuses_a_value_its_provenance_attributes_to_the_renderer
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
      value:
      - wave: '1'
        code: AC_READER_V0
    - id: field_declarations
      value:
      - code: AC_READER_V0
        subdomain_field: s
    threshold: 100.0
    provenance:
      AC_READER_V0.core.type: supplied_by_renderer
```
