# CC_JUDGE_DOCUMENT_V0

## 1. Intent

Judge a phase document against a declared rule set: read it into registers, then apply every rule
and report what failed.

Reused by every phase. Each phase supplies its own document and its own rule set; the mechanism is
the same one.

---

## 2. Rationale

Parsing and evaluating are two steps of one governed capability rather than two capabilities. A
workflow composes capability *calls*, and data does not flow between them — a node reads the intent
payload, not a previous node's result. Chaining belongs inside a contract's pipeline, where step two
reads step one through `$.results.parse_registers.*`.

Keeping the two transforms separate still matters: parsing judges nothing and evaluating knows
nothing about markdown, so each can be reused or replaced without disturbing the other.

Admissibility must be reproducible — the same document and the same rule set always give the same
verdict. The rule set arrives as an input rather than as embedded content, so what is governed can
be read from the composition without reading any code.

---

## 3. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CT_PURE_PARSE_REGISTERS_V0 | CT | Parse |
| 2 | CT_PURE_EVALUATE_RULES_V0 | CT | Evaluate |

---

## 4. Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| document_text | string | true | Full text of the phase document |
| rule_set | array | true | The declared rules deciding admissibility |

---

## 5. Outputs

| Field | Type | Description |
|-------|------|-------------|
| verdict | string | ADMISSIBLE or INADMISSIBLE |
| findings | array | One entry per failed rule |
| rules_evaluated | integer | Number of rules applied |

---

## 6. Result Status Contract

| Status | Condition |
|--------|-----------|
| SUCCESS | The rule set was applied in full and a verdict reached |
| VIOLATION | The input was unusable, or a rule named an unimplemented check kind |

---

## Machine

```yaml
fqdn: transformation::CC_JUDGE_DOCUMENT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: design
core:
  summary: Parse a phase document and judge it against a declared rule set
  inputs:
    document_text:
      type: string
      required: true
    prior_texts:
      type: object
      required: true
      description: |
        Phase id → full text of the upstream document. Empty when this phase reads none — which for
        P0 is permanent: its input is human prose, not a phase document, so there is no upstream
        register to preserve and never will be.
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
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  # Declares no outputs: registers are an intermediate, not a result of judging a document.
  # Every step's outputs mapping accumulates into the CC surface, so declaring them here would
  # publish the entire parsed document as an observable output of the phase. Step two reads the
  # raw result directly instead, which the dispatcher addresses as
  # $.results.<step_id>.capability_result.<field>.
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

  - step: evaluate_rules
    transform: transformation::CT_PURE_EVALUATE_RULES_V0
    inputs:
      header: $.results.parse_registers.capability_result.header
      sections: $.results.parse_registers.capability_result.sections
      registers: $.results.parse_registers.capability_result.registers
      document_text: $.inputs.document_text
      rule_set: $.inputs.rule_set
      # Judges a document alone — it binds no capability and observes nothing. Declared empty
      # rather than omitted: a rule needing an observation must find it absent, not undefined.
      observed: {}
      # Keyed by the phase that produced it, so a rule can say which handoff it relied on.
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
  description: Reads a phase document into registers and evaluates every declared rule against it
```
