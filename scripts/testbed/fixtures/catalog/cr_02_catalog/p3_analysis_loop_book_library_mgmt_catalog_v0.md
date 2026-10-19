# Stage 3 — Analysis Loop: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p3
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_02_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: The existing record is identified by title, author and publication year, and two records differing only in publication year are already two records. The catalog therefore already distinguishes editions, and no identity has to change.
    impact: The change adds the work above the existing record instead of redefining it; no existing identity, record or operation is redefined.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 forms one key from title, author and publication_year; book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 claims it
  - question_id: Q2
    finding: Uniqueness in this composition is claimed through a registry keyed on one value, and a key is formed by a pure transform before it is claimed. A work's key of title and author can be formed and claimed the same way.
    impact: The work's identity needs no new mechanism, only a new key and a new claim step.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_side_effects::CS_REGISTRY_V0 publishes REGISTER, RESOLVE and EXISTS; book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 is the worked precedent
  - question_id: Q3
    finding: The transform that forms the edition key is depended on by 23 artifacts and forms a three-attribute key. Making it also form a two-attribute key would change a transform every catalog operation reaches.
    impact: The work key is formed by a new transform rather than by widening the existing one.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: si.topology.impact impacted_count 23 for book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
  - question_id: Q4
    finding: Selecting records by stated criteria exists as a pure transform; grouping the selected records by an attribute they share does not.
    impact: Work-level search needs a grouping transform that the composition does not carry.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0 selects and returns records; no transform in the composition groups them
  - question_id: Q5
    finding: The search and retrieval steps are each reached by one workflow and one entry point, and their own consumer closure is the subdomain rather than the composition.
    impact: Changing what they return disturbs nothing outside the catalog.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: si.topology.impact impacted_namespaces book_library_mgmt only for book_library_mgmt::CC_SEARCH_CATALOG_V0 and book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
  - question_id: Q6
    finding: A physical copy is recorded against one record and claims its own barcode, so a copy already belongs to exactly one edition.
    impact: Copies are untouched by this change — no decision, no extension, no new artifact.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
  - question_id: Q7
    finding: The subdomain declares its own stores and binds its own workflows to them, and the binding declaration is referenced by nine artifacts within the subdomain and none outside it.
    impact: A store for works is declared and bound in the subdomain's own declarations, and the blast radius stays inside the catalog.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: si.artifact.refs ref_count 9 for book_library_mgmt::RB_CATALOG_BINDINGS_V0, all within book_library_mgmt
  - question_id: Q8
    finding: book_library_mgmt declares its reuse visibility as business, so the previous change's own artifacts are legitimate candidates for this one.
    impact: Reuse and extension of the catalog's artifacts are permitted rather than assumed.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: si.snapshot.summary reuse_visibility book_library_mgmt business
  - question_id: Q9
    finding: Whether any record was written under the previous change cannot be established from the composition; a snapshot declares stores and paths and does not carry their contents.
    impact: The existing-records promise is carried forward as a criterion execution must settle, not as a design question.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 declares five paths and no contents; no inspection operation reads a store
  - question_id: Q10
    finding: Registration already claims two identities and writes two records, in an order established so that every claim precedes every write.
    impact: A work claim is placed among the claims, before any write, rather than appended to the operation.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
  verification_results:
  - item: The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: 'Re-read against the pinned composition: book_library_mgmt carries 43 artifacts and declares compiler version 4, alongside five other domains'
  - item: The catalog is believed to hold bibliographic records and physical copies of library materials.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: 'Re-read book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0: five stores, of which BOOKS and PHYSICAL_COPIES hold the records, one append-only trail and two registries'
  - item: A book is believed to be identified by title, author and publication year.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: 'Re-read book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0: inputs title, author, publication_year; output one identity_key claimed by book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0'
  - item: A physical copy is believed to belong to exactly one book.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: Re-read book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; no path records a copy against more than one record
  - item: The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: 'Re-counted against the composition: nine workflows and nine entry points in book_library_mgmt, each reaching book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 first'
  - item: A retired record is believed to be reinstatable.
    origin: {phase: p2, register: belief_verification, row: 6}
    result: CONFIRMED
    evidence: Re-read book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0, reached through their own entry points
  - item: Records written under the previous change are believed to exist and to be readable.
    origin: {phase: p2, register: belief_verification, row: 7}
    result: CONFIRMED
    evidence: 'The result stands and is re-grounded: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 declares paths and no contents, and no inspection operation in the composition reads a store. The belief remains unresolvable from a snapshot, which is a fact about where it can be settled, not a defect in the belief'
  - item: Durable records are written, read, selected and updated in place through a declared side effect.
    origin: {phase: p2, register: pps_baseline_fqdns, key: durable record store}
    result: CONFIRMED
    evidence: Re-read capability_side_effects::CS_MUTABLE_JSON_V0; impacted_count 46 across ai_governance, book_library_mgmt and workload
  - item: Uniqueness is claimed through a registry keyed on a single value.
    origin: {phase: p2, register: pps_baseline_fqdns, key: uniqueness registry}
    result: CONFIRMED
    evidence: Re-read capability_side_effects::CS_REGISTRY_V0; impacted_count 43 across ai_governance and book_library_mgmt
  - item: Selecting records by stated criteria exists as a pure transform, and grouping them does not.
    origin: {phase: p2, register: architectural_observations, row: 5}
    result: CONFIRMED
    evidence: Re-read capability_transforms::CT_PURE_FILTER_RECORDS_V0; impacted_count 33, and the composition carries no grouping transform
  dependency_discoveries:
  - dependency: Durable record storage for works
    type: side effect
    disposition: REUSE
    evidence: capability_side_effects::CS_MUTABLE_JSON_V0
  - dependency: Uniqueness claim for a work's identity
    type: side effect
    disposition: REUSE
    evidence: capability_side_effects::CS_REGISTRY_V0
  - dependency: The work identity key, formed from title and author
    type: transform
    disposition: AUTHOR_NEW
    evidence: No transform in the composition forms a two-attribute key; book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 forms the three-attribute edition key
  - dependency: Grouping selected records by an attribute they share
    type: transform
    disposition: AUTHOR_NEW
    evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0 selects and does not group
  - dependency: The store declaration that must carry the work stores
    type: structure
    disposition: EXISTING
    evidence: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0, impacted_count 10
  - dependency: The binding declaration that must bind the work stores
    type: runtime binding
    disposition: EXISTING
    evidence: book_library_mgmt::RB_CATALOG_BINDINGS_V0, ref_count 9
  - dependency: The registration step that must claim the work
    type: contract
    disposition: EXISTING
    evidence: book_library_mgmt::CC_REGISTER_BOOK_V0, impacted_count 22
  - dependency: The search step whose answer must be grouped by work
    type: contract
    disposition: EXISTING
    evidence: book_library_mgmt::CC_SEARCH_CATALOG_V0, impacted_count 31
  - dependency: The retrieval step that must carry a work summary
    type: contract
    disposition: EXISTING
    evidence: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0, impacted_count 31
  - dependency: The authorization check every catalog operation reaches first
    type: contract
    disposition: REUSE
    evidence: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
  - dependency: The audit step every catalog operation reaches last
    type: contract
    disposition: REUSE
    evidence: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
  - dependency: Copy registration and barcode uniqueness
    type: contract
    disposition: REUSE
    evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0, unchanged by this change
  - dependency: Retirement and reinstatement of an edition
    type: contract
    disposition: REUSE
    evidence: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
  impact_analysis:
  - artifact: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    impact_scope: book_library_mgmt
    consumer_count: '10'
    evidence: si.topology.impact impacted_count 10, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 1
  - artifact: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    impact_scope: book_library_mgmt
    consumer_count: '9'
    evidence: si.topology.impact impacted_count 9, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 9
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    impact_scope: book_library_mgmt
    consumer_count: '22'
    evidence: si.topology.impact impacted_count 22, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2
  - artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
    impact_scope: book_library_mgmt
    consumer_count: '31'
    evidence: si.topology.impact impacted_count 31, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    impact_scope: book_library_mgmt
    consumer_count: '31'
    evidence: si.topology.impact impacted_count 31, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    impact_scope: book_library_mgmt
    consumer_count: '22'
    evidence: si.topology.impact impacted_count 22, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    impact_scope: book_library_mgmt
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 1
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    impact_scope: book_library_mgmt
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 1
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    impact_scope: book_library_mgmt
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 1
  - artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    impact_scope: book_library_mgmt
    consumer_count: '23'
    evidence: si.topology.impact impacted_count 23, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2 — examined and not widened
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    impact_scope: book_library_mgmt
    consumer_count: '20'
    evidence: si.topology.impact impacted_count 20, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2 — read as precedent, not changed
  - artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    impact_scope: ai_governance, book_library_mgmt, workload
    consumer_count: '46'
    evidence: si.topology.impact impacted_count 46, impacted_namespaces ai_governance, book_library_mgmt and workload; si.artifact.refs ref_count 14 — reused as-is
  - artifact: capability_side_effects::CS_REGISTRY_V0
    impact_scope: ai_governance, book_library_mgmt
    consumer_count: '43'
    evidence: si.topology.impact impacted_count 43, impacted_namespaces ai_governance and book_library_mgmt; si.artifact.refs ref_count 10 — reused as-is
  - artifact: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    impact_scope: book_library_mgmt
    consumer_count: '33'
    evidence: si.topology.impact impacted_count 33, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2 — examined and not extended
  - artifact: book_library_mgmt::WF_SEARCH_CATALOG_V0
    impact_scope: none
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
  - artifact: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    impact_scope: none
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    impact_scope: none
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
  authoring_decisions:
  - capability: Hold a work record durably and update it in place
    decision: REUSE
    rationale: A work record is written, read and updated in place exactly as an edition record is, and the declared mechanism is read rather than modified.
    alternatives_checked: capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is; capability_side_effects::CS_APPENDONLY_JSONL_V0 was examined and rejected because a work record must be updated, not only appended.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
  - capability: Enforce that one work exists per title and author
    decision: REUSE
    rationale: Register-if-absent gives the atomic uniqueness a work identity needs, and the key formed from two attributes is a catalog business rule rather than a change to the mechanism.
    alternatives_checked: capability_side_effects::CS_REGISTRY_V0 reused with a two-attribute key, exactly as the edition key uses it with three; book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 was examined as the worked precedent and claims a different key against a different store.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
  - capability: Form the identifying key of a work from its title and author
    decision: AUTHOR_NEW
    rationale: The work's key is a different business key from the edition's, and the transform that forms the edition key is reached by every catalog operation. Widening it would change the identity of the existing record to serve a new one.
    alternatives_checked: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 was examined and rejected — it forms a three-attribute key and 23 artifacts depend on it; capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 was examined and rejected because assembling a record applies no identity rule.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
  - capability: Claim a work's identity so that two registrations of one work do not produce two works
    decision: AUTHOR_NEW
    rationale: Nothing in the composition claims a work. The claim is a governed step of its own, composed the way the edition claim is composed, against the work's own registry store.
    alternatives_checked: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 was examined and rejected — it claims the edition key against the edition registry; capability_side_effects::CS_REGISTRY_V0 is reused beneath the new step rather than replaced.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
  - capability: Resolve the work an edition belongs to
    decision: AUTHOR_NEW
    rationale: Registering an additional edition must name an existing work and receive its record; no step in the composition answers which work a title and author denote.
    alternatives_checked: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 was examined and rejected — it resolves an edition by its own three-attribute key and cannot answer for a work.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
  - capability: Group selected records by an attribute they share
    decision: AUTHOR_NEW
    rationale: Work-level search returns one result per work, which requires grouping the matching editions. Selection and grouping are different operations on the same records.
    alternatives_checked: capability_transforms::CT_PURE_FILTER_RECORDS_V0 was examined and rejected — it selects records by criteria and returns them ungrouped; capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 was examined and rejected because it assembles one record rather than relating several.
    source_finding: {phase: p3, register: analysis_findings, row: 4}
  - capability: Declare the stores the catalog owns
    decision: EXTEND
    rationale: The catalog owns its stores and must now own two more — one holding work records and one claiming work identities. The declaration is the subdomain's own and its consumers are all within it.
    alternatives_checked: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 extended with the work stores; authoring a second storage declaration for the same subdomain was examined and rejected because a subdomain declares its stores once.
    source_finding: {phase: p3, register: analysis_findings, row: 7}
  - capability: Bind the catalog's workflows to the stores they use
    decision: EXTEND
    rationale: The new stores must be reachable by the workflows that read and write them, and binding is declared once per subdomain.
    alternatives_checked: book_library_mgmt::RB_CATALOG_BINDINGS_V0 extended with the work stores; a second binding declaration was examined and rejected for the same reason as the storage declaration.
    source_finding: {phase: p3, register: analysis_findings, row: 7}
  - capability: Register an edition of a work the catalog does not yet hold
    decision: EXTEND
    rationale: The existing registration already confirms authorization, validates, claims two identities, writes two records and audits. It gains a work claim among the claims, before any write, and changes in no other way.
    alternatives_checked: book_library_mgmt::CC_REGISTER_BOOK_V0 extended; authoring a separate registration was examined and rejected because two registrations for one act would duplicate every refusal the existing one enforces.
    source_finding: {phase: p3, register: analysis_findings, row: 10}
  - capability: Validate that a registration carries what a work and an edition require
    decision: EXTEND
    rationale: Validation already runs before any claim and knows the edition's attributes; it must also confirm what a work requires.
    alternatives_checked: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 extended; capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 was examined and is reused beneath it rather than replacing it.
    source_finding: {phase: p3, register: analysis_findings, row: 10}
  - capability: Register an additional edition of an existing work
    decision: AUTHOR_NEW
    rationale: This is the operation the change exists to add. It resolves an existing work rather than creating one, and claims only the edition, so it is a different business operation from registering a work.
    alternatives_checked: book_library_mgmt::CC_REGISTER_BOOK_V0 was examined and rejected — it creates the work and requires a first copy, neither of which an additional edition does; book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 was examined and rejected because a further edition is not a further copy.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
  - capability: Search the catalog and answer at the level of the work
    decision: EXTEND
    rationale: 'The existing search already selects registered records by subject or title and excludes retired ones. What changes is the shape of the answer: the matching editions are grouped under their work. Its consumers are one workflow and one entry point, both within the subdomain.'
    alternatives_checked: book_library_mgmt::CC_SEARCH_CATALOG_V0 extended; authoring a second search was examined and rejected because two searches would leave staff choosing which one answers their question.
    source_finding: {phase: p3, register: analysis_findings, row: 5}
  - capability: Retrieve an edition's complete details with a summary of its work
    decision: EXTEND
    rationale: Retrieval already assembles an edition and the physical copies of it; it gains the work summary so the work's title need not be looked up separately.
    alternatives_checked: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 extended; authoring a separate work retrieval was examined and rejected because the business asked for one retrieval carrying a summary, not a second operation.
    source_finding: {phase: p3, register: analysis_findings, row: 5}
  - capability: Admit a request to register an additional edition of an existing work
    decision: AUTHOR_NEW
    rationale: A new business operation is reached through its own entry point, which declares what a caller must supply — the work it belongs to and the edition's own attributes.
    alternatives_checked: book_library_mgmt::IN_REGISTER_BOOK_V0 was examined and rejected — it admits a registration that creates a work and requires a first copy.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
  - capability: Recognise the moment a work enters the catalog
    decision: AUTHOR_NEW
    rationale: The catalog declares a business moment for each thing that enters it, and a work entering is a moment nothing currently declares.
    alternatives_checked: book_library_mgmt::EV_BOOK_REGISTERED_V0 was examined and rejected — it names an edition entering the catalog, which continues to be its own moment.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
  - capability: Confirm the staff member performing an operation is authorized
    decision: REUSE
    rationale: Every catalog operation reaches the same check first, and the operations this change adds do the same.
    alternatives_checked: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 satisfies it as-is.
    source_finding: {phase: p3, register: analysis_findings, row: 10}
  - capability: Record every performed operation in the catalog's audit trail
    decision: REUSE
    rationale: The trail records whatever operation it is handed, including the ones this change adds.
    alternatives_checked: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 satisfies it as-is.
    source_finding: {phase: p3, register: analysis_findings, row: 10}
  - capability: Register a physical copy against exactly one edition
    decision: REUSE
    rationale: A copy already belongs to exactly one record, and that record is an edition. Nothing about copies changes.
    alternatives_checked: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 satisfy it as-is.
    source_finding: {phase: p3, register: analysis_findings, row: 6}
  - capability: Retire and reinstate an edition independently of the work's other editions
    decision: REUSE
    rationale: Retirement is declared on the existing record and cascades to nothing, which is exactly what retiring one edition requires.
    alternatives_checked: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 satisfy it as-is.
    source_finding: {phase: p3, register: analysis_findings, row: 6}
  - capability: Update an edition's bibliographic information
    decision: REUSE
    rationale: The update already refuses a change that would duplicate another record, and duplication remains an edition-level rule.
    alternatives_checked: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 satisfies it as-is.
    source_finding: {phase: p3, register: analysis_findings, row: 6}
  placement_decision:
  - decision: EXTEND
    subdomain: catalog
    rationale: The work is the abstraction above the record the catalog already holds, it is identified by attributes the catalog already stores, and every operation it touches is one the catalog already owns. Placing it in a subdomain of its own would split one authoritative description of the library's holdings across two owners.
    source_finding: {phase: p3, register: analysis_findings, row: 7}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: 'The six CRITICAL gaps carried from Stage 2 each resolve to a committed decision: the work entity and its store to REUSE of capability_side_effects::CS_MUTABLE_JSON_V0, its identity to a new key transform and a new claim step, grouping to a new transform, and search, retrieval and registration to extensions of book_library_mgmt::CC_SEARCH_CATALOG_V0, book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 and book_library_mgmt::CC_REGISTER_BOOK_V0'
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: Stage 2 carried none, and all ten findings in this stage are CLOSED
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: The thirteen dependencies were established in one pass against book_library_mgmt::RB_CATALOG_BINDINGS_V0 and the substrate side effects; re-reading them surfaced no further dependency
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: All ten items re-grounded and CONFIRMED, including the seventh belief whose unresolvability from a snapshot is itself confirmed against book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
    status: SATISFIED
    evidence: Every finding in this stage is OBSERVED. The Stage 2 rows that were INFERRED concern the work, which no artifact yet expresses; each is carried forward as a committed AUTHOR_NEW decision rather than left as a suspicion
```

Every decision here is taken against a subdomain the pipeline itself authored, so the reuse question
is asked of the previous change's own output rather than of the substrate alone. Impact counts are
read from the composition, never estimated.

---

## 1. Analysis Findings

---

## 2. Mandatory Verification Pass

---

## 3. Dependency Discoveries

---

## 4. Impact Analysis

Every impacted namespace is book_library_mgmt's own except for the two substrate side effects, which
are reused unchanged and gain a consumer rather than losing one.

---

## 5. Authoring Decisions

---

## 6. Subdomain Placement Decision

---

## 7. Saturation Assessment

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · assumptions · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · constraints |
| **Consumes** ← Stage 2 | belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
