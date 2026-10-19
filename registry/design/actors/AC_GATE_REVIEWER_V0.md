# AC_GATE_REVIEWER_V0

## 1. Intent

The person who confirms at a gate that a seed says what they meant.

An admissible verdict is a structural result: it establishes that the seed is well formed, never
that it is correct. Only a person can accept that, so the gate has a declared human actor and the
acceptance is recorded against them.

---

## Machine

```yaml
fqdn: transformation::AC_GATE_REVIEWER_V0
artifact_kind: ACTOR
version: v0
governed_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0
authority: pgc.platform
concern: design
core:
  summary: Human reviewer at a pipeline gate
  description: The human who accepts or declines a seed at Gate 0 after a verdict is reached.
  type: human
  attributes:
    role:
      type: string
      required: true
```
