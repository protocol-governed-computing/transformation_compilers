# IN_CONSTRUCTION_REQUESTED_V0

## 1. Intent

Offer an approved design and mandate for construction.

Gate 1 approved the design and Gate 2 froze the mandate; this is the request to build from them.
Both documents travel in the payload rather than being read from a path, for the same reason a
phase document does: a governed capability reads what it is handed, and a capability that opened a
file would make its result depend on a filesystem the composition cannot see.

---

## Machine

```yaml
fqdn: transformation::IN_CONSTRUCTION_REQUESTED_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: build

core:
  summary: Offer an approved design and mandate for construction
  workflow: WF_CONSTRUCT_ARTIFACTS_V0

  inputs:
    design_text:
      type: string
      required: true
      description: Full text of the P7 design intent
    mandate_text:
      type: string
      required: true
      description: Full text of the P8 authoring mandate
    threshold:
      type: number
      required: true
      description: Minimum Construction Completeness required to build
    author_of_record:
      type: string
      required: true
      description: Identity of the person accountable for the construction

  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
