# WF_CONSTRUCT_ARTIFACTS_V0

## 1. Intent

The Construction lifecycle, executed as a governed workflow.

Every other stage of the pipeline is a composition the snapshot seals and the runtime executes.
Construction was ordinary Python called by a testbed — which meant the one step that *creates*
artifacts was the one step nothing governed.

---

## 2. Why this is not P9

P0–P8 judge documents and emit verdicts. This consumes P7 and P8 and emits artifacts. Numbering it
would blur the two failure classes the lifecycle split exists to separate: a **P8 failure** is "the
mandate is incomplete or contradictory", a **construction failure** is "the mandate was valid and
did not uniquely determine an artifact". Those are caught by different mechanisms and fixed by
different people.

So Construction is a lifecycle stage alongside compilation and execution, and this workflow is its
entry point.

---

## 3. The refusal is a composition, not a convention

A convention that construction "should" only run on a complete design is a convention. A step that
refuses is a composition: an under-determined design stops at the gate and never reaches the
renderer, so zero artifacts are emitted rather than twenty-five approximations.

What the surface **cannot** say is which kind of refusal it was. A transform yields SUCCESS on
return and VIOLATION on raise and nothing else, so a design that does not determine its artifacts
and a construction that is broken arrive as the same status. The exit is named `EXIT_REFUSED`
because refusal is overwhelmingly the likelier cause, and the reason travels in the raised message.
Distinguishing them at the status would need the CT surface to widen, which is a platform change and
not this workflow's to make.

---

## Machine

```yaml
fqdn: transformation::WF_CONSTRUCT_ARTIFACTS_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: build

runtime_binding: transformation::RB_CONSTRUCTION_BINDINGS_V0
subdomain: build
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Construct protocol artifacts from an approved design and mandate
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_CONSTRUCTION_REQUESTED_V0

  nodes:
    IN_CONSTRUCTION_REQUESTED_V0:
      type: IN
      code: IN_CONSTRUCTION_REQUESTED_V0
      next:
        ACK: CC_CONSTRUCT_ARTIFACTS_V0
        NACK: EXIT_REJECTED

    CC_CONSTRUCT_ARTIFACTS_V0:
      type: CC
      code: CC_CONSTRUCT_ARTIFACTS_V0
      inputs:
        design_text: $.payload.design_text
        mandate_text: $.payload.mandate_text
        threshold: $.payload.threshold
      next:
        SUCCESS: CC_PERSIST_ARTIFACTS_V0
        VIOLATION: EXIT_REFUSED
        BACKEND_ERROR: EXIT_REJECTED

    CC_PERSIST_ARTIFACTS_V0:
      type: CC
      code: CC_PERSIST_ARTIFACTS_V0
      inputs:
        documents: $.results.CC_CONSTRUCT_ARTIFACTS_V0.documents
      next:
        SUCCESS: EXIT_CONSTRUCTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED

    EXIT_CONSTRUCTED:
      type: EXIT

    EXIT_REFUSED:
      type: EXIT

    EXIT_REJECTED:
      type: EXIT
```
