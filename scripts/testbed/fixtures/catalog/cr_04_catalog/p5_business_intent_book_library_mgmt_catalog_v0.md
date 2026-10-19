# Stage 5 — Business Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p5
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_04_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Catalog subdomain governs what the library knows about its books: the works it carries, the
    editions of those works, and the physical copies on its shelves. It holds one record for each, the
    state that says whether each is in service or retired, and the details the library publishes about
    them. It records each thing being registered, its details being corrected, and its being retired or
    reinstated, and it announces the moments the business declared matter. It does not govern who borrows
    a book, what a borrower may do, or what the library charges.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: The seed's paragraph, word for word. This phase adds nothing to it.
  subdomain_purposes:
  - subdomain: catalog
    purpose: Governs what the library knows about its books — the works it carries, their editions, and the physical copies on its shelves — and states what each of its operations needs from the person performing it.
    source_finding: {phase: p1, register: cr_type, row: 1}
  scope_boundary:
  - capability: Admitting a request to register a further edition
    status: IN_SCOPE
    notes: The publication year is stated as a number, as the other three statements of its form already say.
    source_finding: {phase: p4, register: authoring_scope, row: 1}
  - capability: Admitting a request to correct bibliographic information
    status: IN_SCOPE
    notes: The title, the author and the publication year are withdrawn; no step reads them. A boundary is stated whole, so withdrawing a requirement authors a successor rather than amending the boundary to say less than it said.
    source_finding: {phase: p4, register: authoring_scope, row: 2}
  - capability: Admitting a request to register a work
    status: DEFERRED
    notes: The act reads the subject at the top of the request and every present caller sends it nested inside the details of the book. Requiring it moves the boundary and every caller together, which this change's seed forbids.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - capability: Comparing what an operation requires against what it uses
    status: DEFERRED
    notes: Nothing performs it in the composition. Whether it belongs to this subdomain or to the platform is not this change's to settle.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - capability: Declaring the form of a detail the catalog holds
    status: DEFERRED
    notes: The store declares paths and no forms. Giving the catalog an authority over forms is a larger change than bringing one boundary into agreement with three statements.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #2'}
  - capability: The operations of subdomains and domains other than the catalog
    status: DEFERRED
    notes: Each is its own business, and the same comparison reports findings elsewhere that were not examined here.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #3'}
  business_objects: []
  identity_semantics: []
  invariants:
  - invariant: An operation requires only what it uses, and uses only what it requires.
    business_reason: A requirement no step reads turns away correct requests and admits nothing extra; a use no requirement covers admits a request the operation then cannot carry out. Both are one disagreement between two statements of one fact, and stating the rule in only one direction is what let the third defect survive discovery of the first two.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - invariant: Nothing about who may perform an operation changes.
    business_reason: The three things that decide who may act are stated separately from what an operation needs, appear in all ten operations, and are read by no step of any of them. Restating what an operation needs cannot reach them, and a change that quietly did would be a relaxation rather than a correction.
    source_finding: {phase: p4, register: constraint_register, row: 2}
  - invariant: The records the catalog already holds are not migrated, rewritten or revalidated.
    business_reason: What is wrong is what a request must supply, not what the catalog knows. A record registered before this change is as good afterwards.
    source_finding: {phase: p4, register: constraint_register, row: 3}
  - invariant: A publication year is stated as a number wherever an operation asks for one.
    business_reason: The catalog displays a year as a number and every request the library makes supplies one, so a librarian who types the year they see is turned away by the only boundary that disagrees.
    source_finding: {phase: p4, register: constraint_register, row: 4}
  - invariant: No correct request becomes harder to make.
    business_reason: This is what the ruling against gaining requirements was for, and it decided the shape of this change. Requiring the subject looked like it added nothing a requester was not already sending; the requester sends it nested inside the details of the book and the act reads it at the top of the request, so requiring it makes every present request fail. The ruling holds and the correction is deferred.
    source_finding: {phase: p4, register: constraint_register, row: 5}
  - invariant: The form of a detail the catalog holds is settled by no artifact, so agreement among the statements of it is the only authority available.
    business_reason: There is nothing to defer to. The store declares six paths and no forms, so the correction rests on three statements agreeing and the data agreeing with them, which is weaker than a declaration and is what exists.
    source_finding: {phase: p4, register: constraint_register, row: 6}
  actions:
  - action: Admit a request to register a further edition
    object: Request
    trigger: A librarian registering a further edition of a held work.
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, row: 1}
  - action: Admit a request to correct bibliographic information
    object: Request
    trigger: A librarian correcting the details of a held record.
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, row: 2}
  - action: Admit a request to register a work
    object: Request
    trigger: A librarian registering a work the library does not yet carry.
    status: DEFERRED
    source_finding: {phase: p4, register: capability_graph, row: 3}
  - action: Turn away a request that does not supply what the operation needs
    object: Request
    trigger: Something the operation needs being absent or in the wrong form.
    status: IN_SCOPE
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  provisional_codes:
  - subdomain: catalog
    provisional_code: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    family: IN
    summary: The boundary that admits a correction, requiring the record named and the details being changed and nothing else
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - subdomain: catalog
    provisional_code: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    family: WF
    summary: The act that corrects a held record, admitted by the successor boundary. Its steps are those of the act it supersedes
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  cross_subdomain_refs: []
```

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

### Purpose of every subdomain this change touches

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | Capability graph, gaps, design decisions, authoring scope | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |
