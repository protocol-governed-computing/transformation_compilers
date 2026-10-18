# CC_CONSTRUCT_ARTIFACTS_V0

## 1. Intent

Construct protocol artifacts from an approved design and mandate.

---

## 2. The gate is a step, not a convention

The pipeline measures before it renders, and the measurement **refuses**. A design below the
threshold never reaches the renderer, so "construction only runs on a design that determines its
output" is enforced by the composition rather than by a rule someone remembers.

This is why measuring and rendering are separate steps over the same derivation. One transform doing
both would have to choose between reporting a score and refusing.

**The refusal cannot carry its own name, and that is the CT status limit.** A transform has exactly
two outcomes — SUCCESS on return, VIOLATION on raise — so an under-determined design and a broken
construction reach the caller as the same status. An earlier draft of this contract declared
`UNDER_DETERMINED` in its surface and routed on it; nothing could ever produce it, which made it
dead routing and the vocabulary that declared it vacuous. That is the same defect this pipeline
found in `CC_REGISTER_PHYSICAL_COPY_V0`, reproduced immediately in the artifact written to govern
the finding. The refusal is distinguishable in the raised message, not in the status.

---

## 3. Both documents, parsed the same way

A design and a mandate are parsed by the same transform the phases use. Construction reading
documents through its own parser would let it disagree with the oracle that admitted them about what
a register contains.

---

## 4. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CT_PURE_PARSE_REGISTERS_V1 | CT | Parse the design |
| 2 | CT_PURE_PARSE_REGISTERS_V1 | CT | Parse the mandate |
| 3 | CT_PURE_MEASURE_COMPLETENESS_V0 | CT | Gate |
| 4 | CT_PURE_RENDER_ARTIFACTS_V0 | CT | Render |

---

## Machine

```yaml
fqdn: transformation::CC_CONSTRUCT_ARTIFACTS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: build
core:
  summary: Measure a design, refuse it if under-determined, and render the artifacts it schedules
  inputs:
    design_text:
      type: string
      required: true
    mandate_text:
      type: string
      required: true
    threshold:
      type: number
      required: true
  outputs:
    artifacts:
      type: array
    documents:
      type: array
    artifact_count:
      type: integer
    completeness:
      type: number
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: parse_design
    transform: transformation::CT_PURE_PARSE_REGISTERS_V1
    inputs:
      document_text: $.inputs.design_text
    outputs: {}
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit

  - step: parse_mandate
    transform: transformation::CT_PURE_PARSE_REGISTERS_V1
    inputs:
      document_text: $.inputs.mandate_text
    outputs: {}
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit

  # Rendering now precedes the gate, and the gate is unchanged in what it protects. The measure tests
  # where each value came from, and only the renderer knows — it is the thing that put it there. So
  # the renderer runs, reports one source per leaf, and the gate reads the origins derived from them.
  #
  # Nothing is written before the gate. Rendering is pure and produces a shape in memory; persistence
  # is a separate contract and still runs only on a design the gate admitted. What the gate stops is
  # a construction being *written* from a design that does not determine it, and it still does.
  - step: render_artifacts
    transform: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    inputs:
      design_registers: $.results.parse_design.capability_result.registers
      mandate_registers: $.results.parse_mandate.capability_result.registers
    outputs:
      artifacts: $.capability_result.artifacts
      documents: $.capability_result.documents
      artifact_count: $.capability_result.artifact_count
      sources: $.capability_result.sources
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit

  # One origin per leaf: stated by the design, governed elsewhere, carried from the predecessor, or
  # supplied by the renderer. Only the last is a fact nobody accounted for.
  - step: attribute_provenance
    transform: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    inputs:
      rendered: $.results.render_artifacts.capability_result.artifacts
      sources: $.results.render_artifacts.capability_result.sources
    outputs:
      provenance: $.capability_result.provenance
      governing_artifacts: $.capability_result.governing_artifacts
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit

  # The gate. A design that does not determine its artifacts stops here and nothing is written —
  # refusal is the transform raising, which the runtime surfaces as UNDER_DETERMINED.
  - step: require_determined
    transform: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    inputs:
      design_registers: $.results.parse_design.capability_result.registers
      mandate_registers: $.results.parse_mandate.capability_result.registers
      threshold: $.inputs.threshold
      provenance: $.results.attribute_provenance.capability_result.provenance
    outputs:
      completeness: $.capability_result.completeness
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
extensions:
  description: The Construction lifecycle's single governed capability
```
