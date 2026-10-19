# Stage 2 — Domain Model Discovery: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p2
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_04_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Operation
    description: Something a librarian asks the catalog to do.
    store_model: Ten are declared for this subdomain, each with a boundary and a workflow.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: Request
    description: One asking, with what the librarian supplied.
    store_model: Not held; it is what arrives at the boundary.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: Requirement
    description: Something an operation states a request must supply.
    store_model: Declared at the operation's boundary, as a name and the form the value takes.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 4}
  - entity: Use
    description: A step of the operation reading something the request supplied.
    store_model: Declared in the operation's own steps, as a reference to the supplied value.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 7}
  - entity: Publication year
    description: The year an edition was published.
    store_model: Held in the catalog's book store. Its form is not declared anywhere the catalog owns; it is stated at each boundary and in the description supplied with each request, which say number in every case but one.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 7}
  - entity: Correction
    description: Changing some details of a record the catalog already holds.
    store_model: The record named, and the changed details supplied together.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 5}
  entity_attributes:
  - entity: Requirement
    attribute: Its name
    meaning: What the request must supply.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 4}
  - entity: Requirement
    attribute: The form it takes
    meaning: Whether the value is a number, a word, a list or a record.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 1}
  - entity: Requirement
    attribute: Whether it must be supplied
    meaning: All fifty-nine requirements across the subdomain's ten operations must be supplied; none is optional.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - entity: Publication year
    attribute: Its form at the boundary
    meaning: A number in two of the three operations that name it, and a word in the third.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 2}
  - entity: Publication year
    attribute: Its form in the record
    meaning: Not declared by the catalog. It is whatever the description supplied with the request says, which is a number in every request the library makes.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 1}
  - entity: Correction
    attribute: The record it names
    meaning: The identity the catalog holds the record under. Read by the operation's steps.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 4}
  - entity: Correction
    attribute: The details it changes
    meaning: Supplied together. Read by the operation's steps.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 4}
  business_processes:
  - process: Admitting a request
    initiator: The catalog boundary
    outcome: The request proceeds, or it is turned away before anything happened.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - process: Registering a further edition
    initiator: A librarian
    outcome: A further edition of a held work is registered.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Correcting bibliographic information
    initiator: A librarian
    outcome: What the library publishes about a record is changed.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Registering a work for the first time
    initiator: A librarian
    outcome: The work, its first edition and a copy are registered.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 2}
  - process: Comparing what an operation requires against what it uses
    initiator: Nobody, until now
    outcome: Nothing performed this while the boundary admitted everything.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 12}
  process_steps:
  - process: Admitting a request
    step: '1'
    action: Read what the operation states a request must supply.
    record_produced: Nothing.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 8}
  - process: Admitting a request
    step: '2'
    action: Turn the request away if anything stated is missing or in the wrong form.
    record_produced: The refusal, given to the librarian before anything happened.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: lifecycle_states, row: 2}
  - process: Registering a further edition
    step: '3'
    action: Read the eleven things the request supplied, including the publication year.
    record_produced: The edition and the work it belongs to.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 7}
  - process: Correcting bibliographic information
    step: '4'
    action: Read the record named and the details being changed.
    record_produced: The corrected record.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 4}
  - process: Correcting bibliographic information
    step: '5'
    action: Read the title, the author and the publication year the request also supplied.
    record_produced: Nothing. No step performs this.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 7}
  belief_verification:
  - belief: Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number.
    result: VERIFIED
    evidence: '`book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0` declares the publication year as a word. `book_library_mgmt::IN_REGISTER_BOOK_V0` declares it as a number, as does `book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0`. The description of a book that the library supplies with each request declares it a number, and every year in the library''s own exercise of the catalog is a number. Two of three boundaries, the supplied description and the data agree; the third does not.'
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: Correcting bibliographic information asks for three details it does not use.
    result: VERIFIED
    evidence: '`book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0` requires eight things. Its workflow has four steps, and across all four it reads five: the record named, the details being changed, and the three the boundary uses to decide who may perform the operation. The title, the author and the publication year are read by no step.'
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: No other catalog operation asks for something it does not use.
    result: NOT_FOUND
    evidence: 'All ten operations of the subdomain were compared, requirement by requirement, against the steps that carry them. **The belief holds in the direction Stage 1 meant it and fails in the other.** No operation but the correction requires something no step uses. But `book_library_mgmt::IN_REGISTER_BOOK_V0` has the opposite defect: its workflow reads the subject of the book and its boundary does not require it. The boundary therefore admits a request with no subject that the operation cannot then carry out. Whether any caller supplies the subject where the act reads it was not established at this stage.'
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: Who may perform each operation is stated separately from what the operation needs.
    result: VERIFIED
    evidence: Three of the eight things the correction requires — the credentials, the authorisation rules and the identity of the staff member — are consumed by the boundary's own decision about who may perform the operation, not by any step. They are present in every one of the subdomain's ten operations and are unaffected by what the operation does. Restating what an operation needs cannot reach them.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: The details a correction changes are supplied together, as the changed fields.
    result: VERIFIED
    evidence: The correction's steps read the changed details as one supplied thing, and read the record they belong to by its identity. Removing the title, the author and the publication year removes nothing a step reads.
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - belief: Both failures break the library's own end-to-end exercise of the catalog.
    result: VERIFIED
    evidence: 'Run against the pinned composition, the exercise stops at the second edition: the 1984 edition of the work being registered is absent from the catalog when the exercise looks for it. The first defect refuses it at the boundary, so the correction is never reached.'
    source_finding: {phase: p1, register: known_facts, row: 10}
  pps_baseline_fqdns:
  - capability: Admits a request to register a further edition
    fqdn: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    what_it_does: States the eleven things such a request must supply, and turns away a request that does not supply them.
    fit: MISMATCH
    cannot_do: States the publication year as a word. Turns away every request that supplies it the way the catalog holds it.
  - capability: Registers a further edition
    fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    what_it_does: Registers a further edition of a work already carried, reading all eleven things supplied.
    fit: EXACT
    cannot_do: Nothing. It uses everything its boundary requires; only the form of one requirement is wrong.
  - capability: Admits a request to correct bibliographic information
    fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    what_it_does: States the eight things such a request must supply.
    fit: MISMATCH
    cannot_do: Requires the title, the author and the publication year, which no step of the correction reads. Turns away a correction that does not resupply them.
  - capability: Corrects bibliographic information
    fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    what_it_does: Changes the details of a held record, reading the record named and the details being changed.
    fit: EXACT
    cannot_do: Nothing. It is the boundary above it that is wrong.
  - capability: Admits a request to register a work
    fqdn: book_library_mgmt::IN_REGISTER_BOOK_V0
    what_it_does: States the ten things such a request must supply.
    fit: PARTIAL
    cannot_do: Does not require the subject, which its workflow reads. Admits a request the operation cannot then carry out.
  - capability: Registers a work
    fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    what_it_does: Registers a work, its first edition and a copy, reading eleven things supplied.
    fit: EXACT
    cannot_do: Nothing; it reads one thing its boundary does not require.
  - capability: Holds what the catalog knows
    fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    what_it_does: Declares the six stores the catalog owns and the paths they occupy.
    fit: MISMATCH
    cannot_do: Declares no form for any detail it holds, so it cannot settle whether a publication year is a number. The description of a book is supplied with each request rather than declared once.
  gaps:
  - gap: Registering a further edition states the publication year in a form the catalog does not hold it in.
    severity: HIGH
    impact: Every correct request is turned away. The library's own exercise of the catalog stops here and never reaches the second defect.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - gap: Correcting bibliographic information requires three details no step reads.
    severity: HIGH
    impact: A correction that does not restate the fields it leaves alone is turned away, which is every correction.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - gap: Registering a work reads a detail its boundary does not require.
    severity: MEDIUM
    impact: The boundary admits a request with no subject that the operation then cannot carry out, so a declaration gap surfaces as a failure part-way through rather than as a refusal before anything happened. Whether any caller supplies the detail where the operation reads it was not established here.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - gap: Nothing compares what an operation requires against what it uses.
    severity: MEDIUM
    impact: All three defects were introduced without anything objecting, and stood undetected for as long as the boundary admitted everything.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 12}
  architectural_observations:
  - observation: The subdomain's operations are otherwise exact.
    evidence: Seven of the ten operations require precisely what their steps read, name for name. The defects are three, not a pattern across the subdomain.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - observation: The two defects are opposite in shape and were invisible for the same reason.
    evidence: One boundary requires more than its operation reads; another requires less. Both are a disagreement between two statements of one fact, and neither is visible from either statement alone.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 8}
  - observation: Who may perform an operation is declared uniformly and is untouched by this.
    evidence: The same three things appear in all ten operations and are consumed by the boundary rather than by any step. They are constant across operations that read nothing else in common.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: out_of_scope, row: 1}
  - observation: A form mismatch and a name mismatch are not found by the same means.
    evidence: Comparing names against what the steps read finds two of the three defects and cannot see the third. The publication year's form is wrong while its name is required and read, which no name-level comparison distinguishes.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 1}
  discovery_concerns:
  - concern: The defect discovered in registering a work is outside what Stage 1 scoped.
    evidence: Stage 1 named two operations and stated that no other asks for something it does not use. Discovery confirmed that and found a third operation with the opposite defect. It is in the same subdomain, of the same kind, and the change would be incomplete without it.
    severity: MEDIUM
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - concern: The form of a detail the catalog holds is declared nowhere the catalog owns.
    evidence: The store declares paths and no forms. The publication year's form is stated at three boundaries and in a description supplied with each request, and those four statements are the only ones there are. Three say number and one says word, and nothing compares them. The same disagreement could arise for any other detail.
    severity: MEDIUM
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 1}
  - concern: Whether the defects are confined to this domain is not established.
    evidence: Ten operations of this subdomain were compared. The same comparison across the whole composition reports findings in other domains, which are those domains' business and were not examined here.
    severity: LOW
    evidence_status: INSUFFICIENT_EVIDENCE
    source_finding: {phase: p1, register: out_of_scope, row: 3}
  open_questions:
  - question: Does registering a work belong in this change, or in its own?
    category: SCOPE
    why_it_matters: 'Discovery found a third defect in the same subdomain, of the opposite shape, that Stage 1 did not name. It is one requirement added rather than removed, which Stage 1 explicitly ruled out: no operation gains a requirement in this change. Either the constraint is relaxed for this one, or the defect is raised separately.'
    source_finding: {phase: p1, register: constraints, row: 5}
```

Every belief carried from Stage 1 was grounded against the pinned snapshot through the inspection
interface, and against the compiled dispatch the runtime actually reads. What was searched is
recorded, not only what was found. Where a belief came back narrower or wider than Stage 1 stated
it, the correction is recorded against the belief.

---

## 1. Business Entities

### Entity Attributes

---

## 2. Business Processes

### Process Steps

---

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gaps

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions
