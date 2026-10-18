# CC_JUDGE_AGAINST_COMPOSITION_V0

## 1. Intent

Judge a phase document against a declared rule set, the artifacts the composition publishes, what
each domain declares about itself, **and the upstream phase documents it was handed**.

---

## 2. Why a second observation

`CC_JUDGE_AGAINST_SNAPSHOT_V0` observes the artifact list, which answers *does this identity
exist*. That is the whole question while a phase is discovering what is there.

A phase that **decides** asks a further one: *may this artifact be offered to this change request
at all?* That is not a property of the artifact — it is a property of the domain that owns it, and
a domain declares it. So this contract gathers the composition summary as well, and the two
observations answer different questions: one resolves an identity, the other bounds the search
space an identity may be drawn from.

Both remain separate contracts. A phase that only discovers should not acquire an observation it
does not use, and folding the two would make P2 depend on a declaration it never reads.

---

## 3. Why it also reads upstream documents

A decision is made against what earlier phases committed to, and until now nothing checked that
those commitments survived the handoff. P3's verification pass exists to re-ground every prior
result rather than inherit it; whether it covered them is a question about two documents, and no
amount of reading this one settles it.

Priors are parsed as one mapping in one step. This contract is a fixed pipeline with no iteration,
so the number of upstream documents a phase reads must not change the contract's shape.

---

## 4. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CT_PURE_PARSE_REGISTERS_V0 | CT | Parse |
| 2 | CT_PURE_PARSE_PRIOR_PHASES_V0 | CT | Parse priors |
| 3 | CS_SNAPSHOT_QUERY_V0 | CS | QUERY (si.artifact.list) |
| 4 | CS_SNAPSHOT_QUERY_V0 | CS | QUERY (si.snapshot.summary) |
| 5 | CT_PURE_EVALUATE_RULES_V0 | CT | Evaluate |

---

## Machine

```yaml
fqdn: transformation::CC_JUDGE_AGAINST_COMPOSITION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: design
core:
  summary: Parse a phase document and its priors, observe the composition and its declarations, and judge them together
  inputs:
    document_text:
      type: string
      required: true
    prior_texts:
      type: object
      required: true
      description: |
        Phase id → full text of the upstream document. Empty when the caller handed none over; the
        rule set decides whether that is a defect, and for a phase declaring a cross-phase rule it
        is one.
    rule_set:
      type: array
      required: true
  outputs:
    verdict:
      type: string
    findings:
      type: array
    rules_evaluated:
      type: integer
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    - NOT_FOUND
    on_input_failure: VIOLATION
  pipeline:
  - step: parse_registers
    transform: transformation::CT_PURE_PARSE_REGISTERS_V0
    inputs:
      document_text: $.inputs.document_text
    outputs: {}
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit

  - step: parse_priors
    transform: transformation::CT_PURE_PARSE_PRIOR_PHASES_V0
    inputs:
      prior_texts: $.inputs.prior_texts
    outputs: {}
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit

  # Observation is a governed capability, never an ad hoc read. The snapshot observed is the one
  # this workflow executes from, bound by the runtime binding rather than named by a caller.
  - step: observe_composition
    side_effect: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    op: QUERY
    inputs:
      operation: si.artifact.list
      params: {}
    outputs: {}
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit

  - step: observe_declarations
    side_effect: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    op: QUERY
    inputs:
      operation: si.snapshot.summary
      params: {}
    outputs: {}
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit

  - step: evaluate_rules
    transform: transformation::CT_PURE_EVALUATE_RULES_V0
    inputs:
      header: $.results.parse_registers.capability_result.header
      sections: $.results.parse_registers.capability_result.sections
      registers: $.results.parse_registers.capability_result.registers
      document_text: $.inputs.document_text
      rule_set: $.inputs.rule_set
      # Keyed by the operation that produced it, so a rule can say which observation it relied on.
      observed:
        si.artifact.list: $.results.observe_composition.capability_result.result.artifacts
        si.snapshot.summary: $.results.observe_declarations.capability_result.result.reuse_visibility
      # Keyed by the phase that produced it, for the same reason.
      priors: $.results.parse_priors.capability_result.priors
    outputs:
      verdict: $.capability_result.verdict
      findings: $.capability_result.findings
      rules_evaluated: $.capability_result.rules_evaluated
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
extensions:
  description: Grounds a phase document against the composition and the declarations of the domains within it
```
