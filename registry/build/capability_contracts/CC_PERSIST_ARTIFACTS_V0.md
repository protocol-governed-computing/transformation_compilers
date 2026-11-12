# CC_PERSIST_ARTIFACTS_V0

## 1. Intent

Persist a rendered construction.

---

## 2. Why this is a separate contract

`CC_CONSTRUCT_ARTIFACTS_V0` binds nothing and observes nothing: it parses, measures and renders, and
the same design produces the same artifacts wherever it runs. That is what makes construction
testable — its output depends on its input and on nothing else.

Writing is a side effect. A contract that binds one is a different contract from one that binds
none, for the same reason `CC_JUDGE_AGAINST_SNAPSHOT_V0` is not `CC_JUDGE_DOCUMENT_V0`. Folding the
write into the pure pipeline would make rendering depend on a filesystem, and a construction that
could not be run without writing could not be measured without writing either.

So the purity boundary is a contract boundary, and it is visible in the workflow: one node renders,
the next node persists.

---

## 3. One operation, one construction

A capability contract is a fixed pipeline with no iteration, so the whole rendered set is written in
one call. The outcome that matters is the one that survives: either the construction was persisted
or it was not.

---

## Machine

```yaml
fqdn: transformation::CC_PERSIST_ARTIFACTS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: build
core:
  summary: Write a rendered construction beneath the root its runtime binding declares
  inputs:
    documents:
      type: array
      required: true
  outputs:
    written:
      type: integer
    paths:
      type: array
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: write_artifacts
    side_effect: capability_side_effects::CS_TEXT_ARTIFACT_V0
    op: WRITE_ALL
    inputs:
      documents: $.inputs.documents
    outputs:
      written: $.capability_result.written
      paths: $.capability_result.paths
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
extensions:
  description: The Construction lifecycle's only side effect
```
