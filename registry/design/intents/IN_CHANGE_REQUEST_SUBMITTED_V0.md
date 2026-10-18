# IN_CHANGE_REQUEST_SUBMITTED_V0

## 1. Intent

A Change Request register is offered to P1 for judgement.

`register_text` is the document itself. The driver reads the file; nothing downstream touches the
filesystem, which is what makes a verdict reproducible — the same rule established at P0 and
carried forward unchanged.

---

## Machine

```yaml
fqdn: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: design

core:
  summary: Offer a Change Request register for admissibility judgement
  workflow: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0

  inputs:
    register_text:
      type: string
      required: true
      description: Full text of the P1 register — supplied by the driver, never read downstream
    prior_texts:
      type: object
      required: true
      description: |
        Phase id → full text of the upstream document — p0 carries the seed this register restates. Supplied by the
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
