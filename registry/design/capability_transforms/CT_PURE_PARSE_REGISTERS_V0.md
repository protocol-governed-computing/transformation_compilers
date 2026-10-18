# CT_PURE_PARSE_REGISTERS_V0

## 1. Intent

Read a phase document into the registers a rule set can be applied to.

**Phase-neutral by design.** Every phase document in the pipeline has the same shape — a Machine
block holding its `document` header and its registers, and prose sections around it — so every
phase parses the same way and differs only in which rule set it then applies. Every phase P0–P8 and
construction reuse this transform.

**What it returns is declared.** Each output names the structure its value conforms to:
`STRUCTURE_PHASE_HEADER_V0`, `STRUCTURE_PHASE_SECTIONS_V0` and `STRUCTURE_PHASE_REGISTERS_V0`. It
reads the Machine block, not the pipe tables.

`document_text` is the **document itself**, never a location to read. A pure CT may not touch the
filesystem — doing so would make the transform non-deterministic and unreplayable, and would put
I/O inside a transform. The caller reads the file and supplies its content, so the same text always
parses to the same registers.

This transform **reports what a document contains and judges nothing**. A malformed document yields
a partial structure rather than an error, because a parse failure would report a syntax problem
where the author needs a governance finding. Deciding admissibility belongs to the rule set.

---

## Machine

```yaml
fqdn: transformation::CT_PURE_PARSE_REGISTERS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: design
core:
  summary: Parse phase document text into structured registers
  refusal: never
  description: |
    Reads a phase document's Machine block into its header (the `document` mapping) and its
    registers (each by id, with its value as written), and its prose into numbered sections.

    Judges nothing: an absent register is simply absent from the result, and the rule set decides
    what that means.
  inputs:
    document_text:
      type: string
      required: true
      description: The full text of the phase document — never a path, never read from disk
  outputs:
    header:
      type: object
      required: true
      description: The Machine block's `document` mapping
      structure: transformation::STRUCTURE_PHASE_HEADER_V0
    sections:
      type: array
      required: true
      description: Ordered prose sections, each with its number, title and text
      structure: transformation::STRUCTURE_PHASE_SECTIONS_V0
    registers:
      type: array
      required: true
      description: Registers in the order written, each with its id and its value
      structure: transformation::STRUCTURE_PHASE_REGISTERS_V0
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_PARSE_REGISTERS
  implementation:
    module: transformation.implementation.capability_transforms.atoms.ct_pure_parse_registers_v0
    callable: execute
```
