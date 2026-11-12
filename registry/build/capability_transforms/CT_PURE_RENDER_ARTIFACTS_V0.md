# CT_PURE_RENDER_ARTIFACTS_V0

## Machine

```yaml
fqdn: transformation::CT_PURE_RENDER_ARTIFACTS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: build
core:
  summary: Render every artifact a mandate schedules from the design that determines it
  refusal: raises
  inputs:
    design_registers:
      type: array
      required: true
    mandate_registers:
      type: array
      required: true
  outputs:
    artifacts:
      type: array
      required: true
    documents:
      type: array
      required: true
    artifact_count:
      type: integer
      required: true
    sources:
      type: object
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_RENDER_ARTIFACTS
  implementation:
    module: transformation.implementation.capability_transforms.atoms.ct_pure_render_artifacts_v0
    callable: execute
```

---

## Intent

Render every artifact a mandate schedules from the design that determines it
