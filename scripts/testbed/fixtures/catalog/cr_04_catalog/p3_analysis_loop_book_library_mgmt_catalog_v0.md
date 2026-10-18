# Stage 3 — Analysis Loop: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p3
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_04_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: '**OVERTURNED. Registering a work does not belong in this change.** This pass first ruled that it did, on the ground that requiring the subject makes no request harder because every request already supplies it. Executing the change against the library''s own exercise of the catalog falsified that ground: the caller supplies the subject nested inside the details of the book, and the act reads it at the top level of the request and rebuilds those details itself. No caller has ever sent it where the act reads it. Requiring it therefore makes every present request fail, which is precisely what the seed''s ruling against gaining requirements forbids.'
    impact: Returns the change to the two defects it was raised for. The third is real and is raised separately, where the boundary and the caller move together.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: '`WF_REGISTER_BOOK_V0` binds `book_fields` from `$.payload.subject`, `$.payload.title` and `$.payload.author`, ignoring the details the caller supplies. The library''s exercise sends the subject only inside those supplied details. Emitting the requirement turned that exercise from failing at the second edition to failing at the first registration.'
  - question_id: Q1a
    finding: '**The third defect stands, and its correction is not this change''s to make.** A boundary that admits a request its act cannot carry out is a defect by the same invariant as the other two, read in the other direction. Correcting it moves a requirement and a caller together, and the seed rules that no operation gains a requirement in this change.'
    impact: Defers the third defect intact rather than dropping it. It is raised where the caller may move with it.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: Requiring the subject is one requirement added; every present caller sends it elsewhere. Both facts are established, and they cannot both be honoured inside a change whose seed forbids the first.
  - question_id: Q2
    finding: '**One invariant covers all three defects, read in both directions.** Stage 1 stated that an operation requires only what it uses. Its converse — that an operation uses only what it requires — is the same statement of the same relation, and the third defect breaks it. Stating the invariant one-sidedly is what allowed the third defect to survive discovery of the first two.'
    impact: 'Fixes what the change asserts: agreement between the two statements, not the removal of surplus requirements.'
    evidence_status: INFERRED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: Of the subdomain's ten operations, seven agree exactly, one requires more than it uses, one uses more than it requires, and one requires a detail in the wrong form.
  - question_id: Q3
    finding: '**The form of a detail is settled by no artifact, so the change must settle it by agreement.** The store declares six paths and no forms. A publication year''s form is stated at three boundaries and in a description supplied with each request. Three of those four say number; one says word. There is no authority to defer to, only a majority and the data.'
    impact: 'Fixes how the first defect is corrected: the boundary is brought to the form the other three statements share, rather than to a form the catalog declares.'
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: '`book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0` declares stores and paths only. `IN_REGISTER_BOOK_V0` and `IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0` say number; `IN_REGISTER_ADDITIONAL_EDITION_V0` says word; every year in the library''s exercise of the catalog is a number.'
  - question_id: Q4
    finding: '**Nothing else in the subdomain changes.** Each of the three boundaries is reached by exactly one artifact — the workflow it admits — and by nothing else. No boundary is shared, no boundary is referenced by another domain, and correcting one reaches nothing beyond its own operation.'
    impact: Establishes that the change is three declarations and no cascade.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'Each of the three reports a consumer count of one: its own workflow.'
  verification_results:
  - item: Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: 'Re-read from the composition: one boundary says word, two say number, and the description supplied with each request says number.'
  - item: Correcting bibliographic information asks for three details it does not use.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: Eight required; five read across four steps. The title, the author and the publication year are read by no step.
  - item: No other catalog operation asks for something it does not use.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: Confirmed in the direction stated, and the opposite defect confirmed in registering a work. Both were re-derived from the compiled bindings rather than carried from Stage 2. What was overturned is not the defect but the claim that correcting it reached no caller.
  - item: Who may perform each operation is stated separately from what the operation needs.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: The same three things appear in all ten operations of the subdomain and are read by no step of any of them.
  - item: The details a correction changes are supplied together, as the changed fields.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: The correction's four steps read the record named and the changed details, and nothing else the request supplied.
  - item: Both failures break the library's own end-to-end exercise of the catalog.
    origin: {phase: p2, register: belief_verification, row: 6}
    result: CONFIRMED
    evidence: 'Re-run against the pinned composition: the exercise stops at the second edition, which is absent from the catalog when the exercise looks for it.'
  dependency_discoveries:
  - dependency: The three boundaries being corrected
    type: governance
    disposition: EXISTING
    evidence: All three are declared artifacts of this subdomain, each reached by one workflow.
  - dependency: The three operations themselves
    type: capability
    disposition: EXISTING
    evidence: All three already run and already read what they read. No step changes.
  - dependency: The decision about who may perform an operation
    type: governance
    disposition: EXISTING
    evidence: Declared uniformly across all ten operations and untouched by this change.
  - dependency: The catalog's stores
    type: data
    disposition: EXISTING
    evidence: Six stores, unchanged. No held record is migrated, rewritten or revalidated.
  - dependency: The comparison of what an operation requires against what it uses
    type: governance
    disposition: INVESTIGATE
    evidence: Nothing performs it in the composition. Whether it belongs to this subdomain or to the platform is not this change's to settle.
  impact_analysis:
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    impact_scope: The form of one requirement. Nothing else in the subdomain reads it.
    consumer_count: '1'
    evidence: 'Reported by the composition: its only consumer is `book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0`.'
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    impact_scope: Three requirements withdrawn. Nothing else in the subdomain reads it.
    consumer_count: '1'
    evidence: 'Reported by the composition: its only consumer is `book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0`.'
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    impact_scope: One requirement added, which the operation already reads.
    consumer_count: '1'
    evidence: 'Reported by the composition: its only consumer is `book_library_mgmt::WF_REGISTER_BOOK_V0`.'
  - artifact: The three workflows
    impact_scope: None. No step is added, removed or rebound.
    consumer_count: null
    evidence: Each reads exactly what it reads today; the change is to what the boundary above it states.
  - artifact: The catalog's six stores
    impact_scope: None.
    consumer_count: null
    evidence: No held record changes; the change is to what a new request must supply.
  - artifact: The library's end-to-end exercise of the catalog
    impact_scope: It completes, where today it stops at the second edition.
    consumer_count: null
    evidence: The exercise is the acceptance evidence, not a consumer of any artifact.
  authoring_decisions:
  - capability: Admitting a request to register a further edition
    decision: EXTEND
    rationale: The boundary is right about what it needs and wrong about the form one of them takes. Only the form changes.
    alternatives_checked: 'Changing the operation to accept a word was considered and rejected: three of the four statements of the form say number, and the data is numbers.'
    source_finding: {register: analysis_findings, row: 3}
  - capability: Admitting a request to correct bibliographic information
    decision: EXTEND
    rationale: Three requirements are withdrawn. The other five describe what the operation does.
    alternatives_checked: 'Making the operation read the three was considered and rejected: a correction that restates the fields it leaves alone is not a correction.'
    source_finding: {register: analysis_findings, row: 2}
  - capability: Admitting a request to register a work
    decision: REUSE
    rationale: Unchanged by this change. The requirement it lacks is one every present caller sends elsewhere, so adding it here would break every request the library makes.
    alternatives_checked: Adding the requirement was ruled and then overturned against the library's own exercise of the catalog; amending the callers alongside it was rejected as outside a change whose seed forbids gaining a requirement.
    source_finding: {register: analysis_findings, row: 1}
  - capability: The three operations
    decision: REUSE
    rationale: No step is added, removed or rebound. What each operation does is correct.
    alternatives_checked: 'Rewriting the operations was considered and rejected: it is the boundaries that are wrong.'
    source_finding: {register: analysis_findings, row: 4}
  placement_decision:
  - decision: EXTEND
    subdomain: catalog
    rationale: All three boundaries are declared by this subdomain, reached only by its own workflows, and reach nothing outside it.
    source_finding: {register: analysis_findings, row: 4}
  saturation:
  - criterion: The question Stage 2 left open is closed.
    status: SATISFIED
    evidence: 'Registering a work does not join the change. The ground for admitting it was overturned by execution: the constraint it appeared to break does reach it, because no present caller supplies the detail where the act reads it.'
  - criterion: Every belief Stage 2 verified was re-grounded.
    status: SATISFIED
    evidence: All six confirmed against the pinned composition and against the library's own exercise of the catalog; none overturned.
  - criterion: Every operation of the subdomain has been examined.
    status: SATISFIED
    evidence: All ten compared requirement by requirement against the steps that carry them. Three disagree; seven agree exactly. Two are corrected here and the third is deferred with its ground recorded.
  - criterion: The correction for each defect is determined.
    status: SATISFIED
    evidence: One form brought to the form the other three statements share, and three requirements withdrawn. The third defect is stated, deferred and unchanged.
  - criterion: Nothing outside the subdomain is reached.
    status: SATISFIED
    evidence: Each boundary has exactly one consumer, its own workflow. No store, no other subdomain and no other domain is touched.
```

The question Stage 2 left open, closed against the pinned composition; every belief it verified,
re-grounded rather than carried.

---

## 1. Analysis Findings

---

## 2. Mandatory Verification Pass

---

## 3. Dependency Discoveries

---

## 4. Impact Analysis

---

## 5. Authoring Decisions

---

## 6. Placement Decision

---

## 7. Discovery Saturation
