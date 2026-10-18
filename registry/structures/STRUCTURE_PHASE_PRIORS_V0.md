# STRUCTURE_PHASE_PRIORS_V0

## 1. Intent

A phase that preserves an upstream commitment is handed the upstream documents. Each is parsed by
the reader the judged document uses, so a cross-phase rule and a same-phase rule read a register
alike. The key is the phase id; the value is that document's header, sections and registers, each
in the form `STRUCTURE_PHASE_HEADER_V0`, `STRUCTURE_PHASE_SECTIONS_V0` and
`STRUCTURE_PHASE_REGISTERS_V0` state. The forms are written out here, not referenced: a JSON Schema
`$ref` is not a reference the platform declares.

## 2. How it is read

`core.json_schema` is a JSON Schema. A capability transform's field names this structure
with `structure`, and the field's value conforms to the schema. `$id` is the structure's own
identity.

---

## Machine

```yaml
fqdn: transformation::STRUCTURE_PHASE_PRIORS_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: transformation
core:
  summary: The upstream phase documents a phase is judged against, parsed, by phase id
  json_schema:
    $schema: https://json-schema.org/draft/2020-12/schema
    $id: transformation::STRUCTURE_PHASE_PRIORS_V0
    type: object
    additionalProperties:
      type: object
      additionalProperties: false
      required:
      - header
      - sections
      - registers
      properties:
        header:
          type: object
          additionalProperties:
            type:
            - string
            - array
            - object
        sections:
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
        registers:
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
