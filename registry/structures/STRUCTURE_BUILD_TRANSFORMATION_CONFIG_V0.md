# STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0

## 1. Intent

Build-time manifest for the `transformation` domain — the governed change pipeline itself.

---

## Machine

```yaml
fqdn: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: transformation
structure_scope: transformation
reuse_visibility: platform_service
core:
  summary: Build-time STRUCTURE manifest (transformation pipeline domain scope)
  description: 'Compiles the transformation domain''s own artifacts (WF/IN/CC/CT/AC/RB/STRUCTURE),
    resolving governance and platform capability references against the imported compiled governance
    surface. Emits only transformation artifacts. Self-describing: declares its own source layer and
    namespace rule additively.

    '
layer_definitions:
  TRANSFORMATION:
    domain_subpath: registry
    registry_module: transformation.registry
    implementation_namespace: transformation.implementation.capability_transforms.atoms
    layer_category: domain
identity_rules:
- match: transformation.registry
  namespace: transformation
artifact_discovery:
  search_layers:
  - TRANSFORMATION
  import_surface:
    domain: platform
  artifact_types:
  - WF
  - IN
  - CC
  - CT
  - AC
  - RB
  - STRUCTURE
  - VOCAB
  - TEST_DATA
output_configuration:
  root: snapshot
  artifacts:
    layer: PROTOCOL_BUILD_ROOT
    subpath: compiled/canonical
  vocabulary_projection_path:
    layer: GOVERNANCE
    subpath: compiled/vocabulary
  tokenized_projection_path:
    layer: GOVERNANCE
    subpath: compiled/tokenized
  evidence_projection_path:
    layer: GOVERNANCE
    subpath: compiled/evidence
  trust_attestation_path:
    layer: GOVERNANCE
    subpath: compiled/trust
  layer_outputs:
    TRANSFORMATION:
      layer: TRANSFORMATION
      subpath: compiled/canonical
  bootstrap_search_roots:
  - layer: GOVERNANCE
    subpath: structure/structures
  conformance:
    layer: GOVERNANCE
    subpath: compiled/transform_conformance
build_phases:
- phase: discover
  description: Discover transformation artifacts via STRUCTURE
- phase: parse
  description: Parse artifacts into canonical machine form
- phase: normalize
  description: Resolve references (transformation + imported governance surface)
- phase: validate
  description: Validate artifacts using compiler schema rules
- phase: assert
  description: Evaluate cross-artifact invariants
- phase: materialize
  description: Emit deterministic compiled artifacts (transformation scope only)
  target: compiled/artifacts/
```
