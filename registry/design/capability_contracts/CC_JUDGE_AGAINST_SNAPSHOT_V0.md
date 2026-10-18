# CC_JUDGE_AGAINST_SNAPSHOT_V0

## 1. Intent

Judge a phase document against a declared rule set, **against the composition it describes**, and
against the upstream phase documents it was handed.

Reused by every phase that grounds claims. Each supplies its own document and rule set; the
mechanism is the same one.

---

## 2. Why this is a separate contract

`CC_JUDGE_DOCUMENT_V0` judges a document alone and binds nothing. That is sufficient while a rule
is a property of what the register says about itself — structure, vocabulary, traceability.

It stops being sufficient the moment a register claims something already exists. That is a claim
about the assembled composition, and no amount of reading the document can settle it. Grounding
needs an observation, an observation is a side effect, and a contract that binds a side effect is a
different contract from one that binds none.

Both remain: a phase that grounds nothing should not acquire a capability it does not use, and a
contract that always observed would make every phase depend on a snapshot being present.

---

## 3. Why the prior parse does not fork the contract

Reading an upstream document is the other thing a rule may need from outside the document, and it
does **not** get its own contract. What forks a contract here is a side effect: an observation binds
a capability, and binding one is a commitment a phase that never observes should not make.

Parsing text the caller already supplied binds nothing and observes nothing. It is the same class of
step as parsing the judged document, which every contract already carries. Forking on it would give
three contracts six shapes and say nothing true about any of them.

So the step is unconditional, and a phase that reads no upstream document says so at the call site
by handing over an empty mapping. That is more inspectable than an absence: `prior_texts: {}` in a
compiled workflow is a declaration that this phase's handoff is ungoverned, and it is greppable.

---

## 4. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CT_PURE_PARSE_REGISTERS_V0 | CT | Parse |
| 2 | CT_PURE_PARSE_PRIOR_PHASES_V0 | CT | Parse priors |
| 3 | CS_SNAPSHOT_QUERY_V0 | CS | QUERY (si.artifact.list) |
| 4 | CS_SNAPSHOT_QUERY_V0 | CS | QUERY (si.capability.surface) |
| 5 | CT_PURE_EVALUATE_RULES_V0 | CT | Evaluate |

---

## 5. Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| document_text | string | true | Full text of the phase document |
| prior_texts | object | true | Phase id → text of the upstream document; empty when none is read |
| rule_set | array | true | The declared rules deciding admissibility |

---

## 6. Outputs

| Field | Type | Description |
|-------|------|-------------|
| verdict | string | ADMISSIBLE or INADMISSIBLE |
| findings | array | One entry per failed rule |
| rules_evaluated | integer | Number of rules applied |

---

## 7. Result Status Contract

| Status | Condition |
|--------|-----------|
| SUCCESS | The composition was observed, the rule set applied in full, and a verdict reached |
| VIOLATION | The input was unusable, or a rule named an unimplemented check kind |
| BACKEND_ERROR | The bound snapshot could not be read |

---

## Machine

```yaml
fqdn: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: design
core:
  summary: Parse a phase document and its priors, observe the composition, and judge them together
  inputs:
    document_text:
      type: string
      required: true
    prior_texts:
      type: object
      required: true
      description: |
        Phase id → full text of the upstream document. Empty when this phase reads none; the rule
        set decides whether that is a defect, and for a phase declaring a cross-phase rule it is one.
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

  # A third question of the same bound capability, not a new capability. What an operation declares
  # it yields is the only fact that separates a binding reading a real field from one reading a
  # field somebody hoped existed.
  - step: observe_capabilities
    side_effect: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    op: QUERY
    inputs:
      operation: si.capability.surface
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

  # What each domain declares about being drawn on. A phase deciding whether an artifact may be
  # reused needs the owning domain's own statement, and inferring relevance from a namespace is
  # reserved to the author. Declared by P3 and observed by nothing until the observed map was
  # generated, at which point the omission became a build failure instead of a quiet degradation.
  - step: observe_reuse_visibility
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

  - step: observe_store_list
    side_effect: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    op: QUERY
    inputs:
      operation: si.store.list
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
  - step: observe_rule_set_list
    side_effect: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    op: QUERY
    inputs:
      operation: si.rule_set.list
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
  - step: observe_behavior_logic_list
    side_effect: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    op: QUERY
    inputs:
      operation: si.behavior_logic.list
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
        si.behavior_logic.list: $.results.observe_behavior_logic_list.capability_result.result.workflows
        si.capability.surface: $.results.observe_capabilities.capability_result.result.capabilities
        si.capability.surface#contracts: $.results.observe_capabilities.capability_result.result.contracts
        si.capability.surface#intents: $.results.observe_capabilities.capability_result.result.intents
        si.capability.surface#transforms: $.results.observe_capabilities.capability_result.result.transforms
        si.rule_set.list: $.results.observe_rule_set_list.capability_result.result.carriers
        si.snapshot.summary: $.results.observe_reuse_visibility.capability_result.result.reuse_visibility
        si.store.list: $.results.observe_store_list.capability_result.result.stores
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
  description: Grounds a phase document against the composition it is executing within
```
