# RB_TRANSFORMATION_BINDINGS_V0

## 1. Intent

Runtime bindings for the transformation phase pipeline.

Phases that judge a document alone bind nothing: they read text supplied to them and return a
verdict, persisting nothing.

From P2 onward a phase must *observe* the composition to ground what a register claims, and that is
a side effect — the same query answers differently against different compositions. It is bound here
to `{{snapshot_root}}`: **the snapshot the workflow is executing from**, not one a caller names. A
workflow that could be pointed at a different composition would report confidently about the wrong
one, and its evidence would be worthless.

Nothing here is writable. The observation capability is read-only by construction, so a phase
cannot alter the composition it is reasoning about.

---

## Machine

```yaml
fqdn: transformation::RB_TRANSFORMATION_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
authority: pgc.platform
concern: design
parameters:
- snapshot_root
core:
  summary: Runtime bindings for the transformation phase pipeline
  description: Binds read-only observation of the executing composition. No storage, no writes.
  bindings:
    capability_side_effects::CS_SNAPSHOT_QUERY_V0:
      policy:
        snapshot_root: "{{snapshot_root}}"


extensions:
  notes:
    - This artifact performs no discovery and no inference.
    - The observed snapshot is the one the workflow runs inside, never one supplied by a caller.
    - No binding here can write; observation cannot disturb what it observes.
```
