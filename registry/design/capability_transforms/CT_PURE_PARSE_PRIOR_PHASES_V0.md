# CT_PURE_PARSE_PRIOR_PHASES_V0

## 1. Intent

Parse the upstream phase documents a phase is judged against, keyed by the phase that produced each.

Nine phases hand work forward through `gov_projection`, and every rule until now judged a single
document. That is sufficient while a defect lives inside one register. It stops being sufficient at
a handoff: a phase that quietly drops an upstream commitment is well formed read alone, and wrong
read as a pipeline. Seeing that requires both documents open, which requires the upstream one
parsed.

---

## 2. Why the whole mapping in one call

A capability contract is a fixed pipeline. It has no iteration, so a step that parsed one prior
could never parse two, and a phase reading two upstream documents would need a differently shaped
contract from one reading one.

Taking the whole mapping and returning the whole mapping puts the only iteration inside a pure
transform, where it costs nothing and observes nothing. The contract shape then stops depending on
how many priors a phase happens to read.

---

## 3. It parses; it does not judge

Whether a handoff was preserved is declared in the calling phase's rule set and evaluated by
`CT_PURE_EVALUATE_RULES_V0`. This transform reports what each upstream document contains. An empty
mapping is a legitimate input meaning no upstream document was supplied — the rules decide whether
that is a defect, and for a phase that declares a cross-phase rule it is one.

---

## Machine

```yaml
fqdn: transformation::CT_PURE_PARSE_PRIOR_PHASES_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: design
core:
  summary: Parse the upstream phase documents a phase is judged against
  refusal: never
  description: |
    Parses each supplied prior with the same reader the judged document uses, so a cross-phase rule
    and a same-phase rule cannot disagree about what a register contains. Raises CTExecutionError
    when the mapping or an entry is not the declared shape; the runtime maps any CT exception to
    VIOLATION.
  inputs:
    prior_texts:
      type: object
      required: true
      description: |
        Phase id → full text of that phase's document, supplied by the calling workflow. Empty when
        the caller handed over no upstream document; a rule that needs one then reports that it
        could not be checked rather than passing silently.
  outputs:
    priors:
      type: object
      required: true
      description: Phase id → parsed document as header, sections and registers
      structure: transformation::STRUCTURE_PHASE_PRIORS_V0
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_PARSE_PRIOR_PHASES
  implementation:
    module: transformation.implementation.capability_transforms.atoms.ct_pure_parse_prior_phases_v0
    callable: execute
```
