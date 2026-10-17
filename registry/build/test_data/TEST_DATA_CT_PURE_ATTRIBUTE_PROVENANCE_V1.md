# TEST_DATA_CT_PURE_ATTRIBUTE_PROVENANCE_V1

## 1. Intent

A leaf the renderer supplied is attributed to the renderer, and every other leaf to the design.

---

## Machine

```yaml
fqdn: transformation::TEST_DATA_CT_PURE_ATTRIBUTE_PROVENANCE_V1
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: build
target: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
cases:
- case_id: attributes_a_supplied_layer_to_the_renderer
  expected_outcome: SUCCESS
  bindings:
    rendered:
    - path: registry/s/layers/STRUCTURE_S_STORAGE_V0.md
      domain: STRUCTURE_S_STORAGE_V0
      machine:
        fqdn: STRUCTURE_S_STORAGE_V0
        artifact_kind: STRUCTURE
        version: v0
        governed_by: structure::CONSTITUTION_STRUCTURE_V0
        authority: pgc.platform
        concern: s
        core:
          summary: The stores the subdomain owns
          layer: DOMAINS
          domain: STRUCTURE_S_STORAGE_V0
          subdomain: s
          entity_stores: {}
    sources:
      STRUCTURE_S_STORAGE_V0:
        core.layer:
        - supplied_by_renderer
        - ''
  expected:
    provenance:
      STRUCTURE_S_STORAGE_V0.fqdn: stated_by_design
      STRUCTURE_S_STORAGE_V0.artifact_kind: stated_by_design
      STRUCTURE_S_STORAGE_V0.version: stated_by_design
      STRUCTURE_S_STORAGE_V0.governed_by: stated_by_design
      STRUCTURE_S_STORAGE_V0.authority: stated_by_design
      STRUCTURE_S_STORAGE_V0.concern: stated_by_design
      STRUCTURE_S_STORAGE_V0.core.summary: stated_by_design
      STRUCTURE_S_STORAGE_V0.core.layer: supplied_by_renderer
      STRUCTURE_S_STORAGE_V0.core.domain: stated_by_design
      STRUCTURE_S_STORAGE_V0.core.subdomain: stated_by_design
      STRUCTURE_S_STORAGE_V0.core.entity_stores: stated_by_design
    governing_artifacts: {}
```
