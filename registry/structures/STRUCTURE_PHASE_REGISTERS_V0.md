# STRUCTURE_PHASE_REGISTERS_V0

## 1. Intent

Each register of a document's Machine block, in the order written, addressed by its id. Its value
is what the document states: a list of rows, a text, `[]` declared empty, or `null` stating nothing.
A row is a mapping keyed `snake_case`. The register schema the document's rule set is drawn from
types each row; this structure states only the form every register shares.

## 2. How it is read

`core.json_schema` is a JSON Schema. A capability transform's field names this structure
with `structure`, and the field's value conforms to the schema. `$id` is the structure's own
identity.

---

## Machine

```yaml
fqdn: transformation::STRUCTURE_PHASE_REGISTERS_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: transformation
core:
  summary: A phase document's registers, by id, each with its value as written
  json_schema:
    $schema: https://json-schema.org/draft/2020-12/schema
    $id: transformation::STRUCTURE_PHASE_REGISTERS_V0
    type: array
    items:
      type: object
      additionalProperties: false
      required:
      - id
      - value
      properties:
        id:
          type: string
        value:
          type:
          - array
          - string
          - 'null'
```
