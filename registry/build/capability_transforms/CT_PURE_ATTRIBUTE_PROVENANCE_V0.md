# CT_PURE_ATTRIBUTE_PROVENANCE_V0

## 1. Intent

Report, for each leaf of every rendered artifact, where its value came from: the design stated it,
an artifact named in its governance fixes it, it was carried from the predecessor, or the renderer
supplied it. Only the renderer knows, because it put the value there, so this reads the renderer's
own record of what it supplied and attributes every other leaf to the design.

`rendered` is the list of artifacts the renderer produced, which is what the construction contract
hands it.

---

## Machine

```yaml
fqdn: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: build
core:
  summary: Report, for each leaf of a rendered artifact, whether the design stated it, a constitution
    governs it, or the renderer supplied it
  refusal: returns
  inputs:
    rendered:
      type: array
      required: true
    sources:
      type: object
      required: true
  outputs:
    provenance:
      type: object
      required: true
    governing_artifacts:
      type: object
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: ATTRIBUTE_PROVENANCE
  implementation:
    module: transformation.implementation.capability_transforms.atoms.ct_pure_attribute_provenance_v0
    callable: execute
```

---

## Intent

Report, for each leaf of a rendered artifact, whether the design stated it, a constitution governs it, or the renderer supplied it
