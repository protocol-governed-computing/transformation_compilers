# STRUCTURE_FIGURE_OF_MERIT_POLICY_V1

## 1. Intent

What a phase document loses a star for, and how much.

The figure of merit is **not** the verdict. Admissibility is decided by a phase's rule set and by
nothing else; this policy says how good an artifact is once judged. The two axes are independent in
both directions: an admissible document can rate poorly because it carries declared open questions,
and an inadmissible one can rate well because a single misspelled citation is fatal to
admissibility while costing little in quality. Collapsing them would make the rating a second,
softer gate, which a governed pipeline must not have.

Scoring is **deduction-based**: every artifact begins at the maximum and loses ground only against
declared evidence. Nothing has to earn its stars, so an artifact is presumed excellent until
something objective says otherwise — and every star lost names the reason it was lost.

## 2. Why this is declared rather than coded

What is deducted, and why it matters, is governance. Only *how* the arithmetic runs is
implementation. Holding the weights in Python would make the quality bar a property of a build
tool — unversioned, unreadable from the composition, and changeable without a governed act.

Changing a weight is therefore a change to this artifact, and a change to this artifact is a new
version like any other.

## 3. What a cell value can be, and what scores it

Three categories, and only the middle one belongs in a `rows` term:

| Category | Example | Admissible? | Scored here? |
|----------|---------|-------------|--------------|
| A valid value | `Result = VERIFIED` | Yes | No — nothing is wrong with it |
| A **governed hole** | `Result = INSUFFICIENT_EVIDENCE` | Yes | **Yes** — the legal alternative to guessing, surfaced rather than rejected |
| An **admission violation** | a cell reading `UNRESOLVED`; a clarification still `Blocking = YES` | **No** | No — a rule already refused it |

A governed hole is the only one this policy has business scoring. The first needs no deduction. The
third is already refused by a rule, and scoring it as well **double-counts one defect**: the
document loses a star through `finding` for the rule that fired, and loses a second through
`open_hole` for the cell that fired it. A reader comparing two documents then sees a gap that
measures how many ways the same cell was counted.

**V0 scored four admission violations this way.** `Identity Field`, `Uniqueness Rule` and `Source`
reading `UNRESOLVED` became inadmissible under `REGISTER_CELL_UNRESOLVED`, and a clarification
`Blocking = YES` became inadmissible under `BLOCKING_CLARIFICATION_OUTSTANDING`. The last was
redundant even before that rule existed: a row present in `clarification_requests` is already
counted by the register term above it, so one blocking question cost two stars for one fact. All
four are removed here.

The rule is general, not a list: **when a rule begins refusing a value, the `rows` term that scored
it comes out of this policy in the same change.** Admission decides whether a document may enter the
pipeline; the figure of merit compares the documents that entered. A term for something admission
forbids describes a document that cannot exist as an admissible one, and is measured twice in the
one case it can still appear — the inadmissible document that is rated anyway.

## 4. Deductions

| Deduction | Weight | What it catches |
|-----------|--------|-----------------|
| `identity_unresolved` | 2 | A citation that resolves to nothing really in the composition — a misspelling or a wrong namespace. Weighted double because a wrong identity propagates: every later phase reads it as established fact. |
| `register_incomplete` | 1 | A declared register that did not arrive intact. |
| `finding` | 1 | Any remaining rule finding. |
| `open_hole` | 1 | A declared governed hole — an open question carried in a register whose content is open questions, or a cell whose value states that the phase could not settle it. Not a defect, and never an admission violation. |

---

## Machine

```yaml
fqdn: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
artifact_kind: STRUCTURE
version: V1
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: transformation
supersedes: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V0

core:
  summary: Deterministic figure of merit for a phase document — deduction-based, 0 to 5
  maximum: 5
  minimum: 0
  deductions:
  - id: identity_unresolved
    label: Identity unresolved
    weight: 2
    findings:
    - BASELINE_IDENTITY_UNRESOLVED
    - VERIFIED_BELIEF_IDENTITY_UNRESOLVED
    - CITED_ALTERNATIVE_UNRESOLVED
    - DEPENDENCY_IDENTITY_UNRESOLVED
  - id: register_incomplete
    label: Register incomplete
    weight: 1
    findings:
    - REGISTER_MISSING
    - REGISTER_EMPTY
    - REGISTER_COLUMN_MISSING
  - id: finding
    label: Findings
    weight: 1
    remaining_findings: true
  - id: open_hole
    label: Open questions
    weight: 1
    rows:
      registers:
      - open_questions
      - clarification_requests
      columns:
        Resolution Status:
        - OPEN
        Status:
        - NOT_SATISFIED
        Result:
        - INSUFFICIENT_EVIDENCE
```

---

## 5. No convergence deduction

A phase is deterministic and single-shot: there is no worker loop, so convergence is *undefined*
rather than *failed*, and undefined convergence is not penalised. No deduction names it, because a
term nothing could ever trip would read as a check.
