# AC_SEED_AUTHOR_V0

## 1. Intent

The person accountable for a seed's content.

A seed is a faithful rewrite of a business problem statement, and someone must answer for whether it
says what the business meant. Declaring that as an actor makes authorship a property of the
composition rather than a convention: the pipeline cannot run without one, and no automated drafter
can occupy this role.

---

## Machine

```yaml
fqdn: transformation::AC_SEED_AUTHOR_V0
artifact_kind: ACTOR
version: v0
governed_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0
authority: pgc.platform
concern: design
core:
  summary: Author of record for a seed
  description: The human accountable for the content of a seed offered to the seed phase.
  type: human
  attributes:
    role:
      type: string
      required: true
```
