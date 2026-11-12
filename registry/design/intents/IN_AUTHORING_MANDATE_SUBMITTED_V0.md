# IN_AUTHORING_MANDATE_SUBMITTED_V0

## 1. Intent

An Authoring Mandate is offered to P8 for judgement.

The register arrives as text, as at every phase. What it will be judged *against* — the assembled
composition — is not supplied here: it is bound by the runtime binding to the snapshot the workflow
executes from. A caller can offer a document; it cannot choose the reality the document is checked
against.

---

## Machine

```yaml
fqdn: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: design

core:
  summary: Offer an Authoring Mandate for admissibility judgement
  workflow: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0

  inputs:
    register_text:
      type: string
      required: true
      description: Full text of the P8 mandate — supplied by the driver, never read downstream
    prior_texts:
      type: object
      required: true
      description: |
        Phase id → full text of the upstream document — p7 carries the design whose assigned
        identities this mandate schedules. Supplied by the driver alongside the mandate itself: a
        mandate is a derivation of a design, and it can only be checked against the design.
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
