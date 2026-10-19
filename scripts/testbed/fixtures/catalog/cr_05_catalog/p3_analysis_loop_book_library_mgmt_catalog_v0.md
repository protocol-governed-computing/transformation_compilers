# Stage 3 — Analysis Loop: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p3
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_05_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: 'Every act confirms its staff against rules the request hands it, and the rules every caller sends are the library''s: the credentials name a staff member, and they are authorized. Written in the confirming contract, the rules hold for every act that composes it, and no request can widen them.'
    impact: The confirming contract holds the rules as a literal. The ten acts stop binding them, and the ten gates stop requiring them.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 is composed by all ten acts in force; every caller in the library's exercise sends `staff_id not_null` and `authorized eq true`; run directly with no rules, unauthorized staff registered a book
  - question_id: Q2
    finding: Four checks report and nothing acts on the report. A rule step requiring the violations to be empty, following each check, turns each report into a refusal, as identity and another domain already do.
    impact: The submission check, the book record, the edition record and the correction each refuse on what their check finds. The platform check stays a reporter, as ruled for v5.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 publish violations nothing reads; blockchain::CC_VALIDATE_REGISTRATION_V0 follows the same check with a rule requiring none
  - question_id: Q3
    finding: The descriptions a book, a work and a further edition are checked against are fixed values of the library's, and can be written where they are used. The book description is its title, author and year as text, text and a number, and its subject as a list; a further edition is described as a book is; a work names its title and author.
    impact: The contracts that check hold their descriptions as literals; the two registration acts stop binding them and their gates stop requiring them. The malformed work description the register act wrote is replaced by the contract's own.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'Every caller in the library''s exercise sends the same book description; book_library_mgmt::WF_REGISTER_BOOK_V0 writes `work_schema` as `required: [title, author]`, which capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 reads as no requirement at all'
  - question_id: Q4
    finding: The submission check reads the book details the request supplies beside the book; the registration records a book the act builds from the request's own fields. Checking the book the act builds — the one it records — makes what is checked what is recorded.
    impact: Each registration act hands its submission check the record it will write, not the supplied copy.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::WF_REGISTER_BOOK_V0 binds the check's `book_fields` from the payload and the record's from the request's top-level fields; book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0 does the same with `edition_fields` and `work_fields`
  - question_id: Q5
    finding: The book the register act records reads its subject where no caller sends it, so every book registered through the library's exercise is recorded without one. Callers send the subject inside the book details they supply.
    impact: The register act records the subject from the supplied book details, as the author answered. Checked as recorded, every present registration passes.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::WF_REGISTER_BOOK_V0 binds `subject` from `$.payload.subject`; the library's exercise sends it only in `book_fields.subject`; cr_04_catalog P3 Q1 recorded the same and set it aside
  - question_id: Q6
    finding: A copy is recorded in the state the request gives it, in both acts that register copies, because the copy contract assembles its state from the request.
    impact: The copy contract writes the state REGISTERED as its own value.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 is composed by book_library_mgmt::WF_REGISTER_BOOK_V0 and book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0; run directly, a copy registered RETIRED is held retired
  - question_id: Q7
    finding: A correction writes the state the request gives it and is checked against no description, so it can set a state the library does not have or leave a book with no subject.
    impact: The correction writes the state the record already has, and checks the corrected record against the book description, refusing a record without a subject.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 assembles `state` from `updated_fields.state`; run directly, a correction set SUSPENDED and an empty subject; the author answered both
  - question_id: Q8
    finding: Every gate in force requires the authorization rules, and two require descriptions and supplied copies no act will read. A gate that requires what no act reads refuses a request for lacking something nobody uses.
    impact: The ten gates stop requiring the rules; the book gate stops requiring the description; the edition gate stops requiring its descriptions and its supplied edition and work details. What every act does read stays required.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: The ten intents in force each require `authorization_rules`; book_library_mgmt::IN_REGISTER_BOOK_V0 requires `book_schema`; book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 requires `edition_schema`, `work_schema`, `edition_fields` and `work_fields`
  - question_id: Q9
    finding: The credentials a request presents are its own. Holding the rules stops a request from widening them; a request presenting credentials that say it is authorized is still admitted.
    impact: Recorded and carried; who a caller is lies outside this change.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 out_of_scope #1'
  - question_id: Q10
    finding: Records made under a request's own rules stay as they were made, including every book recorded without a subject.
    impact: No repair, no backfill.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 constraints #2'
  verification_results:
  - item: Every catalog operation confirms the person performing it is authorized, against rules the request supplies.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1 and Q8
  - item: The catalog checks a book, a work and a further edition against what each must contain, and registers them whatever the check finds.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q2
  - item: The catalog checks a copy of the book supplied beside it, not the book it records.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q4 and Q5
  - item: The descriptions a book, a work and a further edition are checked against come from the request.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q3 and Q8
  - item: A physical copy is registered in whatever state the request gives it.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: Resolved in Q6
  - item: The catalog holds none of its own rules; each comes with the request it judges.
    origin: {phase: p2, register: gaps, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1 through Q3
  - item: A registration the catalog finds incomplete is registered anyway.
    origin: {phase: p2, register: gaps, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q2
  - item: What the catalog checks is not what it records.
    origin: {phase: p2, register: gaps, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q4 and Q5
  - item: A copy is registered in the state the request gives.
    origin: {phase: p2, register: gaps, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q6
  - item: A correction writes the state the request gives.
    origin: {phase: p2, register: discovery_concerns, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q7, per the author's answer
  - item: A correction is not checked against what a book must contain.
    origin: {phase: p2, register: discovery_concerns, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q7, per the author's answer
  - item: The register act's work description checks nothing.
    origin: {phase: p2, register: discovery_concerns, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q3
  - item: The book's recorded subject is read where no caller sends it.
    origin: {phase: p2, register: discovery_concerns, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q5, per the author's answer
  - item: The credentials a request presents are its own.
    origin: {phase: p2, register: discovery_concerns, row: 5}
    result: CONFIRMED
    evidence: Carried in Q9; outside this change
  dependency_discoveries:
  - dependency: Checking a record's structure
    type: Platform transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, unchanged
  - dependency: Refusing on a list of rules
    type: Platform transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, unchanged
  - dependency: Assembling a record from fields
    type: Platform transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, unchanged
  - dependency: Confirming staff
    type: Capability contract
    disposition: EXTEND
    evidence: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 holds its rules
  - dependency: Checking a submission
    type: Capability contract
    disposition: EXTEND
    evidence: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 holds its descriptions and refuses on violations
  - dependency: Recording a book
    type: Capability contract
    disposition: EXTEND
    evidence: book_library_mgmt::CC_REGISTER_BOOK_V0 holds its description and refuses on violations
  - dependency: Recording an edition
    type: Capability contract
    disposition: EXTEND
    evidence: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 holds its description and refuses on violations
  - dependency: Recording a copy
    type: Capability contract
    disposition: EXTEND
    evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 writes its state itself
  - dependency: Correcting a record
    type: Capability contract
    disposition: EXTEND
    evidence: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 keeps the state and checks the corrected record
  - dependency: The ten acts
    type: Workflows
    disposition: EXTEND
    evidence: Every act in force stops binding the rules; the two registration acts check what they record and the register act records the supplied subject
  - dependency: The ten gates
    type: Intents
    disposition: EXTEND
    evidence: Every gate in force stops requiring the rules, and the two registration gates what no act reads
  - dependency: The superseded correction
    type: Workflow and intent
    disposition: EXISTING
    evidence: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 and its intent are superseded and not in force; unchanged
  impact_analysis:
  - artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    impact_scope: Amended — holds its rules
    consumer_count: '22'
    evidence: si.topology.impact impacted_count 22
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    impact_scope: Amended — holds its descriptions, refuses on violations
    consumer_count: '23'
    evidence: si.topology.impact impacted_count 23
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    impact_scope: Amended — holds its description, refuses on violations
    consumer_count: '28'
    evidence: si.topology.impact impacted_count 28
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    impact_scope: Amended — holds its description, refuses on violations
    consumer_count: '27'
    evidence: si.topology.impact impacted_count 27
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    impact_scope: Amended — writes the state itself
    consumer_count: '29'
    evidence: si.topology.impact impacted_count 29
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    impact_scope: Amended — keeps the state, checks the corrected record
    consumer_count: '24'
    evidence: si.topology.impact impacted_count 24
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    impact_scope: Amended — stops binding rules, checks and records the supplied subject
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    impact_scope: Amended — stops binding rules, checks what it records
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    impact_scope: Amended — stops binding rules
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    impact_scope: Amended — stops binding rules
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    impact_scope: Amended — stops binding rules
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    impact_scope: Amended — stops binding rules
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    impact_scope: Amended — stops binding rules
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    impact_scope: Amended — stops binding rules
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    impact_scope: Amended — stops binding rules
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::WF_SEARCH_CATALOG_V0
    impact_scope: Amended — stops binding rules
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    impact_scope: Amended — stops requiring rules and description
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    impact_scope: Amended — stops requiring rules, descriptions and supplied details
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    impact_scope: Amended — stops requiring rules
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    impact_scope: Amended — stops requiring rules
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    impact_scope: Amended — stops requiring rules
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    impact_scope: Amended — stops requiring rules
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    impact_scope: Amended — stops requiring rules
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    impact_scope: Amended — stops requiring rules
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    impact_scope: Amended — stops requiring rules
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    impact_scope: Amended — stops requiring rules
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  authoring_decisions:
  - capability: Refuse anyone the library has not authorized
    decision: EXTEND
    rationale: The confirming step holds the library's rules, so every act that composes it holds them.
    alternatives_checked: 'Holding the rules in each act was checked and rejected: ten acts would carry ten copies of one rule.'
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - capability: Refuse a registration the catalog finds incomplete
    decision: EXTEND
    rationale: A rule following each check refuses when it found anything, as identity does.
    alternatives_checked: 'Making the platform check refuse was rejected by ruling: a check that decides can no longer be used only to report.'
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  - capability: Hold what a book, a work and a further edition must contain
    decision: EXTEND
    rationale: The checking contracts hold their descriptions as literals.
    alternatives_checked: 'Holding them in the acts was checked and rejected: the descriptions belong to the checks, and both registration acts compose the same submission check.'
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  - capability: Check what the catalog records
    decision: EXTEND
    rationale: Each registration act hands its check the record it writes.
    alternatives_checked: 'Checking the supplied copy as well was checked and rejected: a second check of the wrong thing adds nothing.'
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - capability: Record the subject callers supply
    decision: EXTEND
    rationale: The register act reads the subject where callers send it.
    alternatives_checked: 'Requiring it at the top level was rejected by the author: every present caller would change.'
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  - capability: Register a copy as registered
    decision: EXTEND
    rationale: The copy contract writes the state itself, for both acts that register copies.
    alternatives_checked: 'Checking the requested state was rejected: there is one state a copy is registered in, so there is nothing to check, only something to write.'
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
  - capability: Keep a corrected record's state, and check it against the book description
    decision: EXTEND
    rationale: The correction writes the state the record has, and refuses a corrected record that fails the book description or has no subject.
    alternatives_checked: 'Refusing a correction that names a state was checked and rejected: a request''s extra words are ignored, not refused.'
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - capability: Admit a request without the rules the catalog holds
    decision: EXTEND
    rationale: Every gate stops requiring the rules, and the registration gates what no act reads.
    alternatives_checked: 'Leaving the gates as they are was checked and rejected: a gate requiring what nothing reads refuses a correct request for its absence.'
    source_finding: {phase: p3, register: analysis_findings, key: Q8}
  placement_decision:
  - decision: EXTEND
    subdomain: catalog
    rationale: Every rule held here is the catalog's own, and every step that changes belongs to the catalog. Nothing moves and no other subdomain changes.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: 'The one CRITICAL gap resolves to a committed decision: the confirming step holds the library''s rules'
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: All ten findings are CLOSED. The three questions Stage 2 raised were answered by the business author
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: A second pass read every act and every gate in force, not only those the change request names, and added the gates' unread requirements; a third pass over what each act writes found nothing further
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: All fourteen items re-grounded and CONFIRMED
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
    status: SATISFIED
    evidence: Every finding is OBSERVED; five were established by running the acts against the pinned composition
```

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: where each of the catalog's rules is held, and what the
catalog checks against what it records. Every act and every gate was read, not only those the change
request names, because the catalog's rules reach every one of them.

---

## 1. Analysis Findings

## 2. Verification Results

## 3. Dependency Discoveries

## 4. Impact Analysis

## 5. Authoring Decisions

## 6. Placement Decision

## 7. Saturation Assessment
