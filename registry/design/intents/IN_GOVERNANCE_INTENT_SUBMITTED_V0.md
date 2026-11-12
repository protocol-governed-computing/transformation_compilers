# IN_GOVERNANCE_INTENT_SUBMITTED_V0

## 1. Intent

A Governance Intent register is offered to P6 for judgement.

The register arrives as text, as at every phase. What it will be judged *against* — the assembled
composition — is not supplied here: it is bound by the runtime binding to the snapshot the workflow
executes from. A caller can offer a document; it cannot choose the reality the document is checked
against.

---

## Machine

```yaml
fqdn: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: design

core:
  summary: Offer a Governance Intent register for admissibility judgement
  workflow: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0

  inputs:
    register_text:
      type: string
      required: true
      description: Full text of the P6 register — supplied by the driver, never read downstream
    prior_texts:
      type: object
      required: true
      description: |
        Phase id → full text of the upstream document — p5 carries the scope this placement must
        cover and the capabilities it borrows across a subdomain boundary. Supplied by the driver
        alongside the register itself: a handoff is checked by reading both documents, and an
        absent prior is reported as an unchecked handoff rather than passed over.
    author_of_record:
      type: string
      required: true
      description: Identity of the person accountable for the register's content

  outcomes:
    ACK:
      description: Register accepted for judgement
    NACK:
      description: Register not accepted for judgement
```
