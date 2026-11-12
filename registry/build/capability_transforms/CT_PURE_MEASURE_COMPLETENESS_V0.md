# CT_PURE_MEASURE_COMPLETENESS_V0

## Machine

```yaml
fqdn: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: build
core:
  summary: Measure Construction Completeness and refuse a design that does not determine its artifacts
  refusal: raises
  inputs:
    design_registers:
      type: array
      required: true
    mandate_registers:
      type: array
      required: true
    threshold:
      type: number
      required: true
    provenance:
      type: object
      required: true
  outputs:
    completeness:
      type: number
      required: true
    determined:
      type: integer
      required: true
    required:
      type: integer
      required: true
    undetermined:
      type: array
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_MEASURE_COMPLETENESS
  implementation:
    module: transformation.implementation.capability_transforms.atoms.ct_pure_measure_completeness_v0
    callable: execute
```

---

## Intent

Measure Construction Completeness and refuse a design that does not determine its artifacts
