# STRUCTURE_PHASE_SECTIONS_V0

## 1. Intent

The prose of a phase document outside its Machine block, cut at its headings. A section has the
number its heading carries, or `null` for an unnumbered heading, its title, and its text. Prose is
read, never judged as structure: the registers carry what a rule checks.

## 2. How it is read

`core.json_schema` is a JSON Schema. A capability transform's field names this structure
with `structure`, and the field's value conforms to the schema. `$id` is the structure's own
identity.

---

## Machine

```yaml
fqdn: transformation::STRUCTURE_PHASE_SECTIONS_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: transformation
core:
  summary: A phase document's prose sections, in order, as parsed
  json_schema:
    $schema: https://json-schema.org/draft/2020-12/schema
    $id: transformation::STRUCTURE_PHASE_SECTIONS_V0
    type: array
    items:
      type: object
      additionalProperties: false
      required:
      - number
      - title
      - text
      properties:
        number:
          type:
          - integer
          - 'null'
        title:
          type: string
        text:
          type: string
```
