# STRUCTURE_PHASE_HEADER_V0

## 1. Intent

A phase document states what it is in the `document` mapping of its Machine block: its phase,
domain, subdomain, change request and rule set, and an approval where the phase has a gate. The
parser carries that mapping as written. A scalar is read as text; a field holding structure, such as
a list of subdomains or an approval, is kept as it is. Which fields a phase requires, and their
values, are the register schema's to judge, so this structure states only the form.

## 2. How it is read

`core.json_schema` is a JSON Schema. A capability transform's field names this structure
with `structure`, and the field's value conforms to the schema. `$id` is the structure's own
identity.

---

## Machine

```yaml
fqdn: transformation::STRUCTURE_PHASE_HEADER_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: transformation
core:
  summary: 'A phase document''s header: its Machine block''s `document` mapping, as parsed'
  json_schema:
    $schema: https://json-schema.org/draft/2020-12/schema
    $id: transformation::STRUCTURE_PHASE_HEADER_V0
    type: object
    additionalProperties:
      type:
      - string
      - array
      - object
```
