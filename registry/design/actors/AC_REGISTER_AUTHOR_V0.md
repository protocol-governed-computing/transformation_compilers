# AC_REGISTER_AUTHOR_V0

## 1. Intent

The person accountable for a phase register's content, from P1 onward.

`AC_SEED_AUTHOR_V0` is P0's actor and is named for the seed specifically. A register is a different
document with a different obligation — the seed author states business content, a register author
restates it under traceability — so the accountability is declared separately rather than stretched
to cover both.

The naming asymmetry is worth noting: had P0's actor been named for *phase authorship* rather than
for the seed, one artifact would have served both. Renaming it now would mean a new version of a
sealed artifact, which is not worth it for a name; the two actors coexist and the lesson applies to
later phases, which reuse this one.

---

## Machine

```yaml
fqdn: transformation::AC_REGISTER_AUTHOR_V0
artifact_kind: ACTOR
version: v0
governed_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0
authority: pgc.platform
concern: design
core:
  summary: Author of record for a phase register
  description: The human accountable for the content of a register offered to a dossier phase.
  type: human
  attributes:
    role:
      type: string
      required: true
```
