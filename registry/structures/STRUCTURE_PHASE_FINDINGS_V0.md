# STRUCTURE_PHASE_FINDINGS_V0

## 1. Intent

One finding per failed rule. `code` names the kind of failure. `rule` is the failed rule's identity,
its register schema's `$id` and the JSON Pointer of the declaration, so the rule can be read where it
is declared. `locator` places the failure: the register, the row and the field, each `null` where the
rule is about something wider. `detail` says what was found, and `intent` why the rule exists.

## 2. How it is read

`core.json_schema` is a JSON Schema. A capability transform's field names this structure
with `structure`, and the field's value conforms to the schema. `$id` is the structure's own
identity.

---

## Machine

```yaml
fqdn: transformation::STRUCTURE_PHASE_FINDINGS_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: transformation
core:
  summary: 'The rules a phase document failed: each one''s code, identity, place, detail and intent'
  json_schema:
    $schema: https://json-schema.org/draft/2020-12/schema
    $id: transformation::STRUCTURE_PHASE_FINDINGS_V0
    type: array
    items:
      type: object
      additionalProperties: false
      required:
      - code
      - rule
      - locator
      - detail
      - intent
      properties:
        code:
          type: string
        rule:
          type: string
        locator:
          type: object
          additionalProperties: false
          required:
          - register
          - row
          - field
          properties:
            register:
              type:
              - string
              - 'null'
            row:
              type:
              - integer
              - string
              - 'null'
            field:
              type:
              - string
              - 'null'
        detail:
          type: string
        intent:
          type: string
```
