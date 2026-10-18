# IN_DESIGN_INTENT_SUBMITTED_V0

## 1. Intent

A Design Intent register is offered to P7 for judgement.

The register arrives as text, as at every phase. What it will be judged *against* — the assembled
composition — is not supplied here: it is bound by the runtime binding to the snapshot the workflow
executes from. A caller can offer a document; it cannot choose the reality the document is checked
against.

---

## Machine

```yaml
fqdn: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: design

core:
  summary: Offer a Design Intent register for admissibility judgement
  workflow: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0

  inputs:
    register_text:
      type: string
      required: true
      description: Full text of the P7 register — supplied by the driver, never read downstream
    prior_texts:
      type: object
      required: true
      description: |
        Phase id → full text of each upstream document — p5 carries the provisional codes this
        design binds, p6 the cross-subdomain dependencies it must inventory as reuse. Supplied by the
        driver alongside the register itself: a handoff is checked by reading both documents, and
        an absent prior is reported as an unchecked handoff rather than passed over.
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
