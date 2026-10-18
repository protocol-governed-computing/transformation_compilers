# Design Intent — transformation / design, build

## Machine

```yaml
document:
  phase: p7
  domain: transformation
  subdomain:
  - design
  - build
  cr: genesis
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Two subdomains
    business_fact: The phases and construction fail differently and are fixed by different people.
    resolution: Design holds the phases, their reading and evaluating capabilities and their rules; build
      holds construction and uses design only to read a document.
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - decision: One mechanism, nine rule sets
    business_fact: The phases differ only by their rules.
    resolution: One reading capability, one evaluating capability and three judging contracts serve all
      nine phases. Each phase workflow carries its rule set, generated from its register schema.
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - decision: The founding change is judged by its own rules
    business_fact: The composition it is designed against holds none of the pipeline.
    resolution: This design is judged by the rules it declares, each naming the platform invariant it
      realises.
    source_finding:
      phase: p4
      register: design_decisions
      row: 3
  - decision: Construction writes through the platform
    business_fact: Writing carries no pipeline meaning.
    resolution: Construction reuses the platform's text persistence beneath a root its binding declares.
    source_finding:
      phase: p4
      register: design_decisions
      row: 4
  existing_inventory:
  - fqdn: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    action: REUSE
    summary: Observes an assembled composition read-only through the inspection surface
    reason: Reused as it stands; read, never modified.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      key: capability_side_effects::CS_SNAPSHOT_QUERY_V0
  - fqdn: capability_side_effects::CS_TEXT_ARTIFACT_V0
    action: REUSE
    summary: Persists rendered artifacts as text documents beneath a declared root
    reason: Reused as it stands; read, never modified.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      key: capability_side_effects::CS_TEXT_ARTIFACT_V0
  - fqdn: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    action: REUSE
    summary: Runtime execution configuration
    reason: Reused as it stands; read, never modified.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      key: execution::STRUCTURE_RUNTIME_EXECUTION_V0
  - fqdn: lifecycle::CONSTITUTION_CHANGE_MGMT_V1
    action: REUSE
    summary: States the pipeline as phases and names the invariants the design compiler enforces
    reason: Reused as it stands; read, never modified.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      key: lifecycle::CONSTITUTION_CHANGE_MGMT_V1
  - fqdn: lifecycle::CONSTITUTION_CONSTRUCTION_V1
    action: REUSE
    summary: States the invariants construction enforces
    reason: Reused as it stands; read, never modified.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      key: lifecycle::CONSTITUTION_CONSTRUCTION_V1
  new_artifacts:
  - capability: Build an approved mandate
    family: CC
    code: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    summary: Measure a design, refuse it if under-determined, and render the artifacts it schedules
    owner_subdomain: build
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Build an approved mandate
  - capability: Build an approved mandate
    family: CC
    code: transformation::CC_PERSIST_ARTIFACTS_V0
    summary: Write a rendered construction beneath the root its runtime binding declares
    owner_subdomain: build
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Build an approved mandate
  - capability: Render, measure and attribute the artifacts a mandate schedules
    family: CT
    code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    summary: Report, for each leaf of a rendered artifact, whether the design stated it, a constitution
      governs it, or the renderer supplied it
    owner_subdomain: build
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - capability: Render, measure and attribute the artifacts a mandate schedules
    family: CT
    code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    summary: Measure Construction Completeness and refuse a design that does not determine its artifacts
    owner_subdomain: build
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - capability: Render, measure and attribute the artifacts a mandate schedules
    family: CT
    code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    summary: Render every artifact a mandate schedules from the design that determines it
    owner_subdomain: build
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - capability: Build an approved mandate
    family: IN
    code: transformation::IN_CONSTRUCTION_REQUESTED_V0
    summary: Offer an approved design and mandate for construction
    owner_subdomain: build
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Build an approved mandate
  - capability: Build an approved mandate
    family: RB
    code: transformation::RB_CONSTRUCTION_BINDINGS_V0
    summary: Runtime bindings for the construction lifecycle
    owner_subdomain: build
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Build an approved mandate
  - capability: Build an approved mandate
    family: VOCAB
    code: transformation::VOCAB_FACT_PROVENANCE_V0
    summary: Where a value construction wrote came from
    owner_subdomain: build
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Build an approved mandate
  - capability: Build an approved mandate
    family: WF
    code: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    summary: Construct protocol artifacts from an approved design and mandate
    owner_subdomain: build
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Build an approved mandate
  - capability: The author of record and the reviewer
    family: AC
    code: transformation::AC_GATE_REVIEWER_V0
    summary: Human reviewer at a pipeline gate
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The author of record and the reviewer
  - capability: The author of record and the reviewer
    family: AC
    code: transformation::AC_REGISTER_AUTHOR_V0
    summary: Author of record for a phase register
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The author of record and the reviewer
  - capability: The author of record and the reviewer
    family: AC
    code: transformation::AC_SEED_AUTHOR_V0
    summary: Author of record for a seed
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The author of record and the reviewer
  - capability: Judge a phase document, with and without the composition and earlier documents
    family: CC
    code: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    summary: Parse a phase document and its priors, observe the composition and its declarations, and
      judge them together
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Judge a phase document, with and without the composition and earlier documents
  - capability: Judge a phase document, with and without the composition and earlier documents
    family: CC
    code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    summary: Parse a phase document and its priors, observe the composition, and judge them together
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Judge a phase document, with and without the composition and earlier documents
  - capability: Judge a phase document, with and without the composition and earlier documents
    family: CC
    code: transformation::CC_JUDGE_DOCUMENT_V0
    summary: Parse a phase document and judge it against a declared rule set
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Judge a phase document, with and without the composition and earlier documents
  - capability: Apply every rule of a phase and report each failure
    family: CT
    code: transformation::CT_PURE_EVALUATE_RULES_V1
    summary: Evaluate a declared rule set against parsed registers
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - capability: Read the earlier phase documents a phase must agree with
    family: CT
    code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    summary: Parse the upstream phase documents a phase is judged against
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read the earlier phase documents a phase must agree with
  - capability: Read a phase document into its registers
    family: CT
    code: transformation::CT_PURE_PARSE_REGISTERS_V1
    summary: Parse phase document text into structured registers
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read a phase document into its registers
  - capability: The nine phases, each with its rules and its entry point
    family: IN
    code: transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    summary: Offer an Analysis Loop register for admissibility judgement
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: IN
    code: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    summary: Offer an Authoring Mandate for admissibility judgement
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: IN
    code: transformation::IN_BUSINESS_INTENT_SUBMITTED_V1
    summary: Offer a Business Intent register for admissibility judgement
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: IN
    code: transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    summary: Offer a Business Model register for admissibility judgement
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: IN
    code: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    summary: Offer a Change Request register for admissibility judgement
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: IN
    code: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    summary: Offer a Design Intent register for admissibility judgement
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: IN
    code: transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    summary: Offer a Domain Model register for admissibility judgement
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: IN
    code: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    summary: Offer a Governance Intent register for admissibility judgement
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: IN
    code: transformation::IN_SEED_SUBMITTED_V0
    summary: Offer a seed document for admissibility judgement
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: RB
    code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    summary: Runtime bindings for the transformation phase pipeline
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: VOCAB
    code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    summary: The controlled terms the phase registers are written in
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: WF
    code: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    summary: Decide whether an offered seed is admissible
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: WF
    code: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    summary: Decide whether an offered Change Request register is admissible
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: WF
    code: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    summary: Decide whether an offered Domain Model register is admissible
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: WF
    code: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    summary: Decide whether an offered Analysis Loop register is admissible
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: WF
    code: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    summary: Decide whether an offered Business Model register is admissible
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: WF
    code: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    summary: Decide whether an offered Business Intent register is admissible
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: WF
    code: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    summary: Decide whether an offered Governance Intent register is admissible
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: WF
    code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    summary: Decide whether an offered Design Intent register is admissible
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: WF
    code: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    summary: Decide whether an offered Authoring Mandate is admissible
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: STRUCTURE
    code: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V1
    summary: Build-time STRUCTURE manifest (transformation pipeline domain scope)
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: STRUCTURE
    code: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
    summary: Deterministic figure of merit for a phase document — deduction-based, 0 to 5
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_FINDINGS_V0
    summary: 'The rules a phase document failed: each one''s code, identity, place, detail and intent'
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_HEADER_V0
    summary: 'A phase document''s header: its Machine block''s `document` mapping, as parsed'
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_PRIORS_V0
    summary: The upstream phase documents a phase is judged against, parsed, by phase id
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_REGISTERS_V0
    summary: A phase document's registers, by id, each with its value as written
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_SECTIONS_V0
    summary: A phase document's prose sections, in order, as parsed
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  - capability: The nine phases, each with its rules and its entry point
    family: STRUCTURE
    code: transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
    summary: Which register schema, workflow and template each design phase dispatches to
    owner_subdomain: design
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: The nine phases, each with its rules and its entry point
  rb_declarations:
  - rb_code: transformation::RB_CONSTRUCTION_BINDINGS_V0
    binds_wf: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    cs_bindings:
    - capability_side_effects::CS_TEXT_ARTIFACT_V0
    storage_structure: transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V1
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_CONSTRUCTION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  execution_topology:
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: transformation::IN_CONSTRUCTION_REQUESTED_V0
    node_type: IN
    routing:
      ACK: transformation::CC_CONSTRUCT_ARTIFACTS_V0
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    node_type: CC
    routing:
      SUCCESS: transformation::CC_PERSIST_ARTIFACTS_V0
      VIOLATION: EXIT_REFUSED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: transformation::CC_PERSIST_ARTIFACTS_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_CONSTRUCTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: EXIT_CONSTRUCTED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    node: transformation::IN_SEED_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_DOCUMENT_V0
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P0_SEED_ADMISSIBILITY_V1
  - workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    node: transformation::CC_JUDGE_DOCUMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P0_SEED_ADMISSIBILITY_V1
  - workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    node: EXIT_JUDGED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P0_SEED_ADMISSIBILITY_V1
  - workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P0_SEED_ADMISSIBILITY_V1
  - workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    node: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_DOCUMENT_V0
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
  - workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    node: transformation::CC_JUDGE_DOCUMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
  - workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    node: EXIT_JUDGED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
  - workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
  - workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    node: transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
  - workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    node: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
  - workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
  - workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
  - workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    node: transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
  - workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    node: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
  - workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
  - workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
  - workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    node: transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
  - workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    node: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
  - workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
  - workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
  - workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    node: transformation::IN_BUSINESS_INTENT_SUBMITTED_V1
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
  - workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    node: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
  - workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
  - workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
  - workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    node: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
  - workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    node: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
  - workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
  - workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    node: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    node: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
  - workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    node: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
  - workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    node: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
  - workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
  - workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
  cc_composition:
  - cc_code: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: '1'
    step_name: parse_design
    capability: transformation::CT_PURE_PARSE_REGISTERS_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - document_text
    produces: []
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        document_text: document_text
      out: {}
  - cc_code: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: '2'
    step_name: parse_mandate
    capability: transformation::CT_PURE_PARSE_REGISTERS_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - document_text
    produces: []
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        document_text: document_text
      out: {}
  - cc_code: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: '3'
    step_name: render_artifacts
    capability: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - design_registers
    - mandate_registers
    produces:
    - artifacts
    - documents
    - artifact_count
    - sources
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        design_registers: design_registers
        mandate_registers: mandate_registers
      out:
        artifacts: artifacts
        documents: documents
        artifact_count: artifact_count
        sources: sources
  - cc_code: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: '4'
    step_name: attribute_provenance
    capability: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - rendered
    - sources
    produces:
    - provenance
    - governing_artifacts
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        rendered: rendered
        sources: sources
      out:
        provenance: provenance
        governing_artifacts: governing_artifacts
  - cc_code: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: '5'
    step_name: require_determined
    capability: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - design_registers
    - mandate_registers
    - threshold
    - provenance
    produces:
    - completeness
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        design_registers: design_registers
        mandate_registers: mandate_registers
        threshold: threshold
        provenance: provenance
      out:
        completeness: completeness
  - cc_code: transformation::CC_PERSIST_ARTIFACTS_V0
    step: '1'
    step_name: write_artifacts
    capability: capability_side_effects::CS_TEXT_ARTIFACT_V0
    kind: CS
    operation: WRITE_ALL
    store: null
    consumes:
    - documents
    produces:
    - written
    - paths
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        documents: documents
      out:
        written: written
        paths: paths
  - cc_code: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: '1'
    step_name: parse_registers
    capability: transformation::CT_PURE_PARSE_REGISTERS_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - document_text
    produces: []
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        document_text: document_text
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: '2'
    step_name: parse_priors
    capability: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - prior_texts
    produces: []
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        prior_texts: prior_texts
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: '3'
    step_name: observe_composition
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    kind: CS
    operation: QUERY
    store: null
    consumes:
    - operation
    - params
    produces: []
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        operation: operation
        params: params
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: '4'
    step_name: observe_declarations
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    kind: CS
    operation: QUERY
    store: null
    consumes:
    - operation
    - params
    produces: []
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        operation: operation
        params: params
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: '5'
    step_name: evaluate_rules
    capability: transformation::CT_PURE_EVALUATE_RULES_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - header
    - sections
    - registers
    - document_text
    - rule_set
    - observed
    - priors
    produces:
    - verdict
    - findings
    - rules_evaluated
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        header: header
        sections: sections
        registers: registers
        document_text: document_text
        rule_set: rule_set
        observed: observed
        priors: priors
      out:
        verdict: verdict
        findings: findings
        rules_evaluated: rules_evaluated
  - cc_code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: '1'
    step_name: parse_registers
    capability: transformation::CT_PURE_PARSE_REGISTERS_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - document_text
    produces: []
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        document_text: document_text
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: '2'
    step_name: parse_priors
    capability: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - prior_texts
    produces: []
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        prior_texts: prior_texts
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: '3'
    step_name: observe_composition
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    kind: CS
    operation: QUERY
    store: null
    consumes:
    - operation
    - params
    produces: []
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        operation: operation
        params: params
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: '4'
    step_name: observe_capabilities
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    kind: CS
    operation: QUERY
    store: null
    consumes:
    - operation
    - params
    produces: []
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        operation: operation
        params: params
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: '5'
    step_name: observe_reuse_visibility
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    kind: CS
    operation: QUERY
    store: null
    consumes:
    - operation
    - params
    produces: []
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        operation: operation
        params: params
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: '6'
    step_name: observe_store_list
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    kind: CS
    operation: QUERY
    store: null
    consumes:
    - operation
    - params
    produces: []
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        operation: operation
        params: params
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: '7'
    step_name: observe_rule_set_list
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    kind: CS
    operation: QUERY
    store: null
    consumes:
    - operation
    - params
    produces: []
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        operation: operation
        params: params
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: '8'
    step_name: observe_behavior_logic_list
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    kind: CS
    operation: QUERY
    store: null
    consumes:
    - operation
    - params
    produces: []
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        operation: operation
        params: params
      out: {}
  - cc_code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: '9'
    step_name: evaluate_rules
    capability: transformation::CT_PURE_EVALUATE_RULES_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - header
    - sections
    - registers
    - document_text
    - rule_set
    - observed
    - priors
    produces:
    - verdict
    - findings
    - rules_evaluated
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        header: header
        sections: sections
        registers: registers
        document_text: document_text
        rule_set: rule_set
        observed: observed
        priors: priors
      out:
        verdict: verdict
        findings: findings
        rules_evaluated: rules_evaluated
  - cc_code: transformation::CC_JUDGE_DOCUMENT_V0
    step: '1'
    step_name: parse_registers
    capability: transformation::CT_PURE_PARSE_REGISTERS_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - document_text
    produces: []
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        document_text: document_text
      out: {}
  - cc_code: transformation::CC_JUDGE_DOCUMENT_V0
    step: '2'
    step_name: parse_priors
    capability: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - prior_texts
    produces: []
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        prior_texts: prior_texts
      out: {}
  - cc_code: transformation::CC_JUDGE_DOCUMENT_V0
    step: '3'
    step_name: evaluate_rules
    capability: transformation::CT_PURE_EVALUATE_RULES_V1
    kind: CT
    operation: null
    store: null
    consumes:
    - header
    - sections
    - registers
    - document_text
    - rule_set
    - observed
    - priors
    produces:
    - verdict
    - findings
    - rules_evaluated
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        header: header
        sections: sections
        registers: registers
        document_text: document_text
        rule_set: rule_set
        observed: observed
        priors: priors
      out:
        verdict: verdict
        findings: findings
        rules_evaluated: rules_evaluated
  step_bindings:
  - owner: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    step: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: INPUT
    field: design_text
    bound_to: payload.design_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    step: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: INPUT
    field: mandate_text
    bound_to: payload.mandate_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    step: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: INPUT
    field: threshold
    bound_to: payload.threshold
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    step: transformation::CC_PERSIST_ARTIFACTS_V0
    direction: INPUT
    field: documents
    bound_to: results.CC_CONSTRUCT_ARTIFACTS_V0.documents
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    step: transformation::CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: document_text
    bound_to: payload.seed_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P0_SEED_ADMISSIBILITY_V1
  - owner: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    step: transformation::CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: prior_texts
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P0_SEED_ADMISSIBILITY_V1
  - owner: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    step: transformation::CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P0_SEED_ADMISSIBILITY_V1
  - owner: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    step: transformation::CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
  - owner: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    step: transformation::CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
  - owner: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    step: transformation::CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
  - owner: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
  - owner: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
  - owner: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
  - owner: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
  - owner: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
  - owner: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
  - owner: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
  - owner: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
  - owner: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
  - owner: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
  - owner: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
  - owner: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
  - owner: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
  - owner: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
  - owner: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
  - owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
  - owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
  - owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
  - owner: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
  - owner: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
  - owner: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    step: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: parse_design
    direction: INPUT
    field: document_text
    bound_to: inputs.design_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: parse_mandate
    direction: INPUT
    field: document_text
    bound_to: inputs.mandate_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: INPUT
    field: design_registers
    bound_to: results.parse_design.capability_result.registers
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: INPUT
    field: mandate_registers
    bound_to: results.parse_mandate.capability_result.registers
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: OUTPUT
    field: artifacts
    bound_to: capability_result.artifacts
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: OUTPUT
    field: documents
    bound_to: capability_result.documents
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: OUTPUT
    field: artifact_count
    bound_to: capability_result.artifact_count
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: OUTPUT
    field: sources
    bound_to: capability_result.sources
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: attribute_provenance
    direction: INPUT
    field: rendered
    bound_to: results.render_artifacts.capability_result.artifacts
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: attribute_provenance
    direction: INPUT
    field: sources
    bound_to: results.render_artifacts.capability_result.sources
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: attribute_provenance
    direction: OUTPUT
    field: provenance
    bound_to: capability_result.provenance
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: attribute_provenance
    direction: OUTPUT
    field: governing_artifacts
    bound_to: capability_result.governing_artifacts
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: INPUT
    field: design_registers
    bound_to: results.parse_design.capability_result.registers
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: INPUT
    field: mandate_registers
    bound_to: results.parse_mandate.capability_result.registers
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: INPUT
    field: threshold
    bound_to: inputs.threshold
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: INPUT
    field: provenance
    bound_to: results.attribute_provenance.capability_result.provenance
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: OUTPUT
    field: completeness
    bound_to: capability_result.completeness
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_CONSTRUCT_ARTIFACTS_V0
  - owner: transformation::CC_PERSIST_ARTIFACTS_V0
    step: write_artifacts
    direction: INPUT
    field: documents
    bound_to: inputs.documents
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_PERSIST_ARTIFACTS_V0
  - owner: transformation::CC_PERSIST_ARTIFACTS_V0
    step: write_artifacts
    direction: OUTPUT
    field: written
    bound_to: capability_result.written
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_PERSIST_ARTIFACTS_V0
  - owner: transformation::CC_PERSIST_ARTIFACTS_V0
    step: write_artifacts
    direction: OUTPUT
    field: paths
    bound_to: capability_result.paths
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_PERSIST_ARTIFACTS_V0
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: parse_registers
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: parse_priors
    direction: INPUT
    field: prior_texts
    bound_to: inputs.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: observe_composition
    direction: INPUT
    field: operation
    bound_to:
      literal: si.artifact.list
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: observe_composition
    direction: INPUT
    field: params
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: observe_declarations
    direction: INPUT
    field: operation
    bound_to:
      literal: si.snapshot.summary
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: observe_declarations
    direction: INPUT
    field: params
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: header
    bound_to: results.parse_registers.capability_result.header
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: sections
    bound_to: results.parse_registers.capability_result.sections
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: registers
    bound_to: results.parse_registers.capability_result.registers
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: rule_set
    bound_to: inputs.rule_set
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: observed
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: priors
    bound_to: results.parse_priors.capability_result.priors
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: OUTPUT
    field: verdict
    bound_to: capability_result.verdict
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: OUTPUT
    field: findings
    bound_to: capability_result.findings
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: OUTPUT
    field: rules_evaluated
    bound_to: capability_result.rules_evaluated
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_COMPOSITION_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: parse_registers
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: parse_priors
    direction: INPUT
    field: prior_texts
    bound_to: inputs.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_composition
    direction: INPUT
    field: operation
    bound_to:
      literal: si.artifact.list
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_composition
    direction: INPUT
    field: params
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_capabilities
    direction: INPUT
    field: operation
    bound_to:
      literal: si.capability.surface
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_capabilities
    direction: INPUT
    field: params
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_reuse_visibility
    direction: INPUT
    field: operation
    bound_to:
      literal: si.snapshot.summary
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_reuse_visibility
    direction: INPUT
    field: params
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_store_list
    direction: INPUT
    field: operation
    bound_to:
      literal: si.store.list
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_store_list
    direction: INPUT
    field: params
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_rule_set_list
    direction: INPUT
    field: operation
    bound_to:
      literal: si.rule_set.list
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_rule_set_list
    direction: INPUT
    field: params
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_behavior_logic_list
    direction: INPUT
    field: operation
    bound_to:
      literal: si.behavior_logic.list
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_behavior_logic_list
    direction: INPUT
    field: params
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: header
    bound_to: results.parse_registers.capability_result.header
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: sections
    bound_to: results.parse_registers.capability_result.sections
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: registers
    bound_to: results.parse_registers.capability_result.registers
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: rule_set
    bound_to: inputs.rule_set
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: observed
    bound_to:
      generated: true
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: priors
    bound_to: results.parse_priors.capability_result.priors
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: OUTPUT
    field: verdict
    bound_to: capability_result.verdict
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: OUTPUT
    field: findings
    bound_to: capability_result.findings
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: OUTPUT
    field: rules_evaluated
    bound_to: capability_result.rules_evaluated
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_AGAINST_SNAPSHOT_V1
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: parse_registers
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: parse_priors
    direction: INPUT
    field: prior_texts
    bound_to: inputs.prior_texts
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: header
    bound_to: results.parse_registers.capability_result.header
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: sections
    bound_to: results.parse_registers.capability_result.sections
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: registers
    bound_to: results.parse_registers.capability_result.registers
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: rule_set
    bound_to: inputs.rule_set
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: observed
    bound_to:
      literal: {}
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: priors
    bound_to: results.parse_priors.capability_result.priors
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: OUTPUT
    field: verdict
    bound_to: capability_result.verdict
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: OUTPUT
    field: findings
    bound_to: capability_result.findings
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: OUTPUT
    field: rules_evaluated
    bound_to: capability_result.rules_evaluated
    source_finding:
      phase: p7
      register: new_artifacts
      key: CC_JUDGE_DOCUMENT_V0
  interface_fields:
  - artifact: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: INPUT
    field: design_text
    type: string
    required: 'YES'
    default: null
    meaning: design text
  - artifact: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: INPUT
    field: mandate_text
    type: string
    required: 'YES'
    default: null
    meaning: mandate text
  - artifact: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: INPUT
    field: threshold
    type: number
    required: 'YES'
    default: null
    meaning: threshold
  - artifact: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: OUTPUT
    field: artifacts
    type: array
    required: 'NO'
    default: null
    meaning: artifacts
  - artifact: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: OUTPUT
    field: documents
    type: array
    required: 'NO'
    default: null
    meaning: documents
  - artifact: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: OUTPUT
    field: artifact_count
    type: integer
    required: 'NO'
    default: null
    meaning: artifact count
  - artifact: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    direction: OUTPUT
    field: completeness
    type: number
    required: 'NO'
    default: null
    meaning: completeness
  - artifact: transformation::CC_PERSIST_ARTIFACTS_V0
    direction: INPUT
    field: documents
    type: array
    required: 'YES'
    default: null
    meaning: documents
  - artifact: transformation::CC_PERSIST_ARTIFACTS_V0
    direction: OUTPUT
    field: written
    type: integer
    required: 'NO'
    default: null
    meaning: written
  - artifact: transformation::CC_PERSIST_ARTIFACTS_V0
    direction: OUTPUT
    field: paths
    type: array
    required: 'NO'
    default: null
    meaning: paths
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    direction: INPUT
    field: rendered
    type: array
    required: 'YES'
    default: null
    meaning: rendered
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    direction: INPUT
    field: sources
    type: object
    required: 'YES'
    default: null
    meaning: sources
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    direction: OUTPUT
    field: provenance
    type: object
    required: 'YES'
    default: null
    meaning: provenance
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    direction: OUTPUT
    field: governing_artifacts
    type: object
    required: 'YES'
    default: null
    meaning: governing artifacts
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: INPUT
    field: design_registers
    type: array
    required: 'YES'
    default: null
    meaning: design registers
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: INPUT
    field: mandate_registers
    type: array
    required: 'YES'
    default: null
    meaning: mandate registers
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: INPUT
    field: threshold
    type: number
    required: 'YES'
    default: null
    meaning: threshold
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: INPUT
    field: provenance
    type: object
    required: 'YES'
    default: null
    meaning: provenance
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: OUTPUT
    field: completeness
    type: number
    required: 'YES'
    default: null
    meaning: completeness
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: OUTPUT
    field: determined
    type: integer
    required: 'YES'
    default: null
    meaning: determined
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: OUTPUT
    field: required
    type: integer
    required: 'YES'
    default: null
    meaning: required
  - artifact: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    direction: OUTPUT
    field: undetermined
    type: array
    required: 'YES'
    default: null
    meaning: undetermined
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: INPUT
    field: design_registers
    type: array
    required: 'YES'
    default: null
    meaning: design registers
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: INPUT
    field: mandate_registers
    type: array
    required: 'YES'
    default: null
    meaning: mandate registers
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: OUTPUT
    field: artifacts
    type: array
    required: 'YES'
    default: null
    meaning: artifacts
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: OUTPUT
    field: documents
    type: array
    required: 'YES'
    default: null
    meaning: documents
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: OUTPUT
    field: artifact_count
    type: integer
    required: 'YES'
    default: null
    meaning: artifact count
  - artifact: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    direction: OUTPUT
    field: sources
    type: object
    required: 'YES'
    default: null
    meaning: sources
  - artifact: transformation::IN_CONSTRUCTION_REQUESTED_V0
    direction: INPUT
    field: design_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P7 design intent
  - artifact: transformation::IN_CONSTRUCTION_REQUESTED_V0
    direction: INPUT
    field: mandate_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P8 authoring mandate
  - artifact: transformation::IN_CONSTRUCTION_REQUESTED_V0
    direction: INPUT
    field: threshold
    type: number
    required: 'YES'
    default: null
    meaning: Minimum Construction Completeness required to build
  - artifact: transformation::IN_CONSTRUCTION_REQUESTED_V0
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the construction
  - artifact: transformation::AC_GATE_REVIEWER_V0
    direction: ATTRIBUTE
    field: role
    type: string
    required: 'YES'
    default: gate_reviewer
    meaning: role
  - artifact: transformation::AC_REGISTER_AUTHOR_V0
    direction: ATTRIBUTE
    field: role
    type: string
    required: 'YES'
    default: register_author
    meaning: role
  - artifact: transformation::AC_SEED_AUTHOR_V0
    direction: ATTRIBUTE
    field: role
    type: string
    required: 'YES'
    default: seed_author
    meaning: role
  - artifact: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: INPUT
    field: document_text
    type: string
    required: 'YES'
    default: null
    meaning: document text
  - artifact: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: Phase id → full text of the upstream document. Empty when the caller handed none over; the
      rule set decides whether that is a defect, and for a phase declaring a cross-phase rule it is one.
  - artifact: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: INPUT
    field: rule_set
    type: array
    required: 'YES'
    default: null
    meaning: rule set
  - artifact: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: OUTPUT
    field: verdict
    type: string
    required: 'NO'
    default: null
    meaning: verdict
  - artifact: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: OUTPUT
    field: findings
    type: array
    required: 'NO'
    default: null
    meaning: findings
  - artifact: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: OUTPUT
    field: rules_evaluated
    type: integer
    required: 'NO'
    default: null
    meaning: rules evaluated
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    type: string
    required: 'YES'
    default: null
    meaning: document text
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: Phase id → full text of the upstream document. Empty when this phase reads none; the rule
      set decides whether that is a defect, and for a phase declaring a cross-phase rule it is one.
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    type: array
    required: 'YES'
    default: null
    meaning: rule set
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: OUTPUT
    field: verdict
    type: string
    required: 'NO'
    default: null
    meaning: verdict
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: OUTPUT
    field: findings
    type: array
    required: 'NO'
    default: null
    meaning: findings
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: OUTPUT
    field: rules_evaluated
    type: integer
    required: 'NO'
    default: null
    meaning: rules evaluated
  - artifact: transformation::CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: document_text
    type: string
    required: 'YES'
    default: null
    meaning: document text
  - artifact: transformation::CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: 'Phase id → full text of the upstream document. Empty when this phase reads none — which
      for P0 is permanent: its input is human prose, not a phase document, so there is no upstream register
      to preserve and never will be.'
  - artifact: transformation::CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: rule_set
    type: array
    required: 'YES'
    default: null
    meaning: rule set
  - artifact: transformation::CC_JUDGE_DOCUMENT_V0
    direction: OUTPUT
    field: verdict
    type: string
    required: 'NO'
    default: null
    meaning: verdict
  - artifact: transformation::CC_JUDGE_DOCUMENT_V0
    direction: OUTPUT
    field: findings
    type: array
    required: 'NO'
    default: null
    meaning: findings
  - artifact: transformation::CC_JUDGE_DOCUMENT_V0
    direction: OUTPUT
    field: rules_evaluated
    type: integer
    required: 'NO'
    default: null
    meaning: rules evaluated
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: INPUT
    field: header
    type: object
    required: 'YES'
    default: null
    meaning: The document's header, as parsed
    structure: transformation::STRUCTURE_PHASE_HEADER_V0
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: INPUT
    field: sections
    type: array
    required: 'YES'
    default: null
    meaning: Parsed document sections
    structure: transformation::STRUCTURE_PHASE_SECTIONS_V0
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: INPUT
    field: registers
    type: array
    required: 'YES'
    default: null
    meaning: Parsed registers, addressed by id — how a rule locates what it governs
    structure: transformation::STRUCTURE_PHASE_REGISTERS_V0
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: INPUT
    field: document_text
    type: string
    required: 'YES'
    default: null
    meaning: The original document text, for whole-document rules
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: INPUT
    field: rule_set
    type: array
    required: 'YES'
    default: null
    meaning: The declared rules deciding admissibility — supplied by the calling workflow
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: INPUT
    field: observed
    type: object
    required: 'YES'
    default: null
    meaning: Facts gathered about the composition, keyed by the inspection operation that produced each.
      Empty for a phase that judges a document alone; a phase that grounds claims fills it from a governed
      inspection capability. A rule needing an observation that is absent reports that it could not be
      checked rather than passing silently.
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: INPUT
    field: priors
    type: object
    required: 'YES'
    default: null
    meaning: The upstream phase documents this one is judged against, parsed, keyed by phase id. Empty
      for a phase judged on its own document; a phase that preserves an upstream commitment fills it from
      the priors the caller handed over. A cross-phase rule whose prior is absent reports that the handoff
      is unchecked rather than passing silently — an unchecked handoff and a preserved one are otherwise
      indistinguishable.
    structure: transformation::STRUCTURE_PHASE_PRIORS_V0
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: OUTPUT
    field: verdict
    type: string
    required: 'YES'
    default: null
    meaning: ADMISSIBLE when no rule failed, INADMISSIBLE otherwise
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: OUTPUT
    field: findings
    type: array
    required: 'YES'
    default: null
    meaning: One entry per failed rule, naming the rule, where it failed, and why it matters
    structure: transformation::STRUCTURE_PHASE_FINDINGS_V0
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    direction: OUTPUT
    field: rules_evaluated
    type: integer
    required: 'YES'
    default: null
    meaning: How many rules were applied — every rule in the set, always
  - artifact: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: Phase id → full text of that phase's document, supplied by the calling workflow. Empty when
      the caller handed over no upstream document; a rule that needs one then reports that it could not
      be checked rather than passing silently.
  - artifact: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    direction: OUTPUT
    field: priors
    type: object
    required: 'YES'
    default: null
    meaning: Phase id → parsed document as header, sections and registers
    structure: transformation::STRUCTURE_PHASE_PRIORS_V0
  - artifact: transformation::CT_PURE_PARSE_REGISTERS_V1
    direction: INPUT
    field: document_text
    type: string
    required: 'YES'
    default: null
    meaning: The full text of the phase document — never a path, never read from disk
  - artifact: transformation::CT_PURE_PARSE_REGISTERS_V1
    direction: OUTPUT
    field: header
    type: object
    required: 'YES'
    default: null
    meaning: The Machine block's `document` mapping
    structure: transformation::STRUCTURE_PHASE_HEADER_V0
  - artifact: transformation::CT_PURE_PARSE_REGISTERS_V1
    direction: OUTPUT
    field: sections
    type: array
    required: 'YES'
    default: null
    meaning: Ordered prose sections, each with its number, title and text
    structure: transformation::STRUCTURE_PHASE_SECTIONS_V0
  - artifact: transformation::CT_PURE_PARSE_REGISTERS_V1
    direction: OUTPUT
    field: registers
    type: array
    required: 'YES'
    default: null
    meaning: Registers in the order written, each with its id and its value
    structure: transformation::STRUCTURE_PHASE_REGISTERS_V0
  - artifact: transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    direction: INPUT
    field: register_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P3 register — supplied by the driver, never read downstream
  - artifact: transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: 'Phase id → full text of the upstream document — p2 carries the domain model whose belief
      results this register re-verifies. Supplied by the driver alongside the register itself: a handoff
      is checked by reading both documents, and an absent prior is reported as an unchecked handoff rather
      than passed over.'
  - artifact: transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the register's content
  - artifact: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    direction: INPUT
    field: register_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P8 mandate — supplied by the driver, never read downstream
  - artifact: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: 'Phase id → full text of the upstream document — p7 carries the design whose assigned identities
      this mandate schedules. Supplied by the driver alongside the mandate itself: a mandate is a derivation
      of a design, and it can only be checked against the design.'
  - artifact: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the register's content
  - artifact: transformation::IN_BUSINESS_INTENT_SUBMITTED_V1
    direction: INPUT
    field: register_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P5 register — supplied by the driver, never read downstream
  - artifact: transformation::IN_BUSINESS_INTENT_SUBMITTED_V1
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: 'Phase id → full text of the upstream document — p0 carries the subdomain purpose this register
      restates. Supplied by the driver alongside the register itself: a handoff is checked by reading
      both documents, and an absent prior is reported as an unchecked handoff rather than passed over.'
  - artifact: transformation::IN_BUSINESS_INTENT_SUBMITTED_V1
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the register's content
  - artifact: transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    direction: INPUT
    field: register_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P4 register — supplied by the driver, never read downstream
  - artifact: transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: 'Phase id → full text of the upstream document — p3 carries the authoring decisions this
      model consolidates. Supplied by the driver alongside the register itself: a handoff is checked by
      reading both documents, and an absent prior is reported as an unchecked handoff rather than passed
      over.'
  - artifact: transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the register's content
  - artifact: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    direction: INPUT
    field: register_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P1 register — supplied by the driver, never read downstream
  - artifact: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: 'Phase id → full text of the upstream document — p0 carries the seed this register restates.
      Supplied by the driver alongside the register itself: a handoff is checked by reading both documents,
      and an absent prior is reported as an unchecked handoff rather than passed over.'
  - artifact: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the register's content
  - artifact: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    direction: INPUT
    field: register_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P7 register — supplied by the driver, never read downstream
  - artifact: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: 'Phase id → full text of each upstream document — p5 carries the provisional codes this design
      binds, p6 the cross-subdomain dependencies it must inventory as reuse. Supplied by the driver alongside
      the register itself: a handoff is checked by reading both documents, and an absent prior is reported
      as an unchecked handoff rather than passed over.'
  - artifact: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the register's content
  - artifact: transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    direction: INPUT
    field: register_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P2 register — supplied by the driver, never read downstream
  - artifact: transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: 'Phase id → full text of the upstream document — p1 carries the change request whose System
      Beliefs this register resolves. Supplied by the driver alongside the register itself: a handoff
      is checked by reading both documents, and an absent prior is reported as an unchecked handoff rather
      than passed over.'
  - artifact: transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the register's content
  - artifact: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    direction: INPUT
    field: register_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the P6 register — supplied by the driver, never read downstream
  - artifact: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    direction: INPUT
    field: prior_texts
    type: object
    required: 'YES'
    default: null
    meaning: 'Phase id → full text of the upstream document — p5 carries the scope this placement must
      cover and the capabilities it borrows across a subdomain boundary. Supplied by the driver alongside
      the register itself: a handoff is checked by reading both documents, and an absent prior is reported
      as an unchecked handoff rather than passed over.'
  - artifact: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the register's content
  - artifact: transformation::IN_SEED_SUBMITTED_V0
    direction: INPUT
    field: seed_text
    type: string
    required: 'YES'
    default: null
    meaning: Full text of the seed document — supplied by the driver, never read downstream
  - artifact: transformation::IN_SEED_SUBMITTED_V0
    direction: INPUT
    field: author_of_record
    type: string
    required: 'YES'
    default: null
    meaning: Identity of the person accountable for the seed's content
  implementation_bindings:
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    callable: execute
    operation: ATTRIBUTE_PROVENANCE
    kind: atom
    purity: ct_pure
    refusal: returns
    source_finding:
      phase: p7
      register: new_artifacts
      key: CT_PURE_ATTRIBUTE_PROVENANCE_V1
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    callable: execute
    operation: PURE_MEASURE_COMPLETENESS
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding:
      phase: p7
      register: new_artifacts
      key: CT_PURE_MEASURE_COMPLETENESS_V0
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    callable: execute
    operation: PURE_RENDER_ARTIFACTS
    kind: atom
    purity: ct_pure
    refusal: raises
    source_finding:
      phase: p7
      register: new_artifacts
      key: CT_PURE_RENDER_ARTIFACTS_V0
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    callable: execute
    operation: PURE_EVALUATE_RULES
    kind: atom
    purity: ct_pure
    refusal: returns
    source_finding:
      phase: p7
      register: new_artifacts
      key: CT_PURE_EVALUATE_RULES_V1
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    callable: execute
    operation: PURE_PARSE_PRIOR_PHASES
    kind: atom
    purity: ct_pure
    refusal: never
    source_finding:
      phase: p7
      register: new_artifacts
      key: CT_PURE_PARSE_PRIOR_PHASES_V1
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    callable: execute
    operation: PURE_PARSE_REGISTERS
    kind: atom
    purity: ct_pure
    refusal: never
    source_finding:
      phase: p7
      register: new_artifacts
      key: CT_PURE_PARSE_REGISTERS_V1
  vocabulary_extensions:
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: stated_by_design
    meaning: stated_by_design
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_FACT_PROVENANCE_V0
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: governed_elsewhere
    meaning: governed_elsewhere
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_FACT_PROVENANCE_V0
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: carried_from_predecessor
    meaning: carried_from_predecessor
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_FACT_PROVENANCE_V0
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: supplied_by_renderer
    meaning: supplied_by_renderer
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_FACT_PROVENANCE_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: AC
    meaning: AC
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: IN
    meaning: IN
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: WF
    meaning: WF
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: CC
    meaning: CC
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: CT
    meaning: CT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: EV
    meaning: EV
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: RB
    meaning: RB
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: VOCAB
    meaning: VOCAB
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: STRUCTURE
    meaning: STRUCTURE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: TI
    meaning: TI
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: TE
    meaning: TE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: approval_state
    casing: UPPER_SNAKE
    value: APPROVED
    meaning: APPROVED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: approval_state
    casing: UPPER_SNAKE
    value: MIGRATED
    meaning: MIGRATED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: approval_state
    casing: UPPER_SNAKE
    value: RECONFIRMED
    meaning: RECONFIRMED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: belief_result
    casing: UPPER_SNAKE
    value: VERIFIED
    meaning: VERIFIED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: belief_result
    casing: UPPER_SNAKE
    value: NOT_FOUND
    meaning: NOT_FOUND
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: belief_result
    casing: UPPER_SNAKE
    value: INSUFFICIENT_EVIDENCE
    meaning: INSUFFICIENT_EVIDENCE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: certainty
    casing: UPPER_SNAKE
    value: HIGH
    meaning: HIGH
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: certainty
    casing: UPPER_SNAKE
    value: MEDIUM
    meaning: MEDIUM
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: certainty
    casing: UPPER_SNAKE
    value: LOW
    meaning: LOW
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: clarification_owner
    casing: UPPER_SNAKE
    value: HUMAN
    meaning: HUMAN
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: clarification_owner
    casing: UPPER_SNAKE
    value: SNAPSHOT
    meaning: SNAPSHOT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: clarification_owner
    casing: UPPER_SNAKE
    value: GOVERNANCE
    meaning: GOVERNANCE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: classification
    casing: UPPER_SNAKE
    value: NEW_SUBDOMAIN
    meaning: NEW_SUBDOMAIN
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: classification
    casing: UPPER_SNAKE
    value: EXTEND_SUBDOMAIN
    meaning: EXTEND_SUBDOMAIN
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: classification
    casing: UPPER_SNAKE
    value: MODIFY
    meaning: MODIFY
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: classification
    casing: UPPER_SNAKE
    value: DEPRECATE
    meaning: DEPRECATE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: composition_kind
    casing: UPPER_SNAKE
    value: CT
    meaning: CT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: composition_kind
    casing: UPPER_SNAKE
    value: CS
    meaning: CS
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: EXISTING
    meaning: EXISTING
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: REUSE
    meaning: REUSE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: AUTHOR_NEW
    meaning: AUTHOR_NEW
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: INVESTIGATE
    meaning: INVESTIGATE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_status
    casing: UPPER_SNAKE
    value: SATISFIED
    meaning: SATISFIED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_status
    casing: UPPER_SNAKE
    value: GAP
    meaning: GAP
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: evidence_status
    casing: UPPER_SNAKE
    value: OBSERVED
    meaning: OBSERVED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: evidence_status
    casing: UPPER_SNAKE
    value: INFERRED
    meaning: INFERRED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: evidence_status
    casing: UPPER_SNAKE
    value: OPEN
    meaning: OPEN
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: expected_outcome
    casing: UPPER_SNAKE
    value: SUCCESS
    meaning: SUCCESS
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: expected_outcome
    casing: UPPER_SNAKE
    value: VIOLATION
    meaning: VIOLATION
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: field_direction
    casing: UPPER_SNAKE
    value: INPUT
    meaning: INPUT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: field_direction
    casing: UPPER_SNAKE
    value: OUTPUT
    meaning: OUTPUT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: fit
    casing: UPPER_SNAKE
    value: EXACT
    meaning: EXACT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: fit
    casing: UPPER_SNAKE
    value: PARTIAL
    meaning: PARTIAL
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: fit
    casing: UPPER_SNAKE
    value: MISMATCH
    meaning: MISMATCH
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: gap_resolution
    casing: UPPER_SNAKE
    value: REPLACE
    meaning: REPLACE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: gap_resolution
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: gap_resolution
    casing: UPPER_SNAKE
    value: NEW
    meaning: NEW
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: handler_kind
    casing: UPPER_SNAKE
    value: WF_INVOCATION
    meaning: WF_INVOCATION
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: handler_kind
    casing: UPPER_SNAKE
    value: SNAPSHOT_READ
    meaning: SNAPSHOT_READ
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: interface_direction
    casing: UPPER_SNAKE
    value: INPUT
    meaning: INPUT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: interface_direction
    casing: UPPER_SNAKE
    value: OUTPUT
    meaning: OUTPUT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: interface_direction
    casing: UPPER_SNAKE
    value: ATTRIBUTE
    meaning: ATTRIBUTE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: REPLACE
    meaning: REPLACE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: REUSE
    meaning: REUSE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: REPOINT
    meaning: REPOINT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: REVIEW
    meaning: REVIEW
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: molecule_binding_role
    casing: UPPER_SNAKE
    value: INPUT
    meaning: INPUT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: molecule_binding_role
    casing: UPPER_SNAKE
    value: CARRY
    meaning: CARRY
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: molecule_binding_role
    casing: UPPER_SNAKE
    value: UPDATE
    meaning: UPDATE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: node_type
    casing: UPPER_SNAKE
    value: IN
    meaning: IN
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: node_type
    casing: UPPER_SNAKE
    value: CC
    meaning: CC
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: node_type
    casing: UPPER_SNAKE
    value: EXIT
    meaning: EXIT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: node_type
    casing: UPPER_SNAKE
    value: EXIT_SUCCESS
    meaning: EXIT_SUCCESS
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: ownership_disposition
    casing: UPPER_SNAKE
    value: OWNED
    meaning: OWNED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: ownership_disposition
    casing: UPPER_SNAKE
    value: SATISFIED
    meaning: SATISFIED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: ownership_disposition
    casing: UPPER_SNAKE
    value: DEFERRED
    meaning: DEFERRED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: placement_decision
    casing: UPPER_SNAKE
    value: NEW_SUBDOMAIN
    meaning: NEW_SUBDOMAIN
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: placement_decision
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: pps_action
    casing: UPPER_SNAKE
    value: REPLACE
    meaning: REPLACE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: pps_action
    casing: UPPER_SNAKE
    value: REVIEW
    meaning: REVIEW
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: pps_action
    casing: UPPER_SNAKE
    value: REUSE
    meaning: REUSE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: pps_action
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: purpose_disposition
    casing: UPPER_SNAKE
    value: INHERITED
    meaning: INHERITED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: purpose_disposition
    casing: UPPER_SNAKE
    value: REFINED
    meaning: REFINED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: record_model
    casing: UPPER_SNAKE
    value: MUTABLE_STATE
    meaning: MUTABLE_STATE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: record_model
    casing: UPPER_SNAKE
    value: APPEND_ONLY_JOURNAL
    meaning: APPEND_ONLY_JOURNAL
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: record_model
    casing: UPPER_SNAKE
    value: IDENTITY_REGISTRY
    meaning: IDENTITY_REGISTRY
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: record_model
    casing: UPPER_SNAKE
    value: HYBRID
    meaning: HYBRID
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: resolution_status
    casing: UPPER_SNAKE
    value: CLOSED
    meaning: CLOSED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: resolution_status
    casing: UPPER_SNAKE
    value: OPEN
    meaning: OPEN
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: reuse_decision
    casing: UPPER_SNAKE
    value: REUSE
    meaning: REUSE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: reuse_decision
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: reuse_decision
    casing: UPPER_SNAKE
    value: AUTHOR_NEW
    meaning: AUTHOR_NEW
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: saturation_status
    casing: UPPER_SNAKE
    value: SATISFIED
    meaning: SATISFIED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: saturation_status
    casing: UPPER_SNAKE
    value: NOT_SATISFIED
    meaning: NOT_SATISFIED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: CREATED
    meaning: CREATED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: EXTENDED
    meaning: EXTENDED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: MODIFIED
    meaning: MODIFIED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: DEPRECATED
    meaning: DEPRECATED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: ADJACENT
    meaning: ADJACENT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_status
    casing: UPPER_SNAKE
    value: IN_SCOPE
    meaning: IN_SCOPE
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_status
    casing: UPPER_SNAKE
    value: DEFERRED
    meaning: DEFERRED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: storage_type
    casing: UPPER_SNAKE
    value: CS_APPENDONLY_JSONL_V0
    meaning: CS_APPENDONLY_JSONL_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: storage_type
    casing: UPPER_SNAKE
    value: CS_MUTABLE_JSON_V0
    meaning: CS_MUTABLE_JSON_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: storage_type
    casing: UPPER_SNAKE
    value: CS_REGISTRY_V0
    meaning: CS_REGISTRY_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: test_value_role
    casing: UPPER_SNAKE
    value: INPUT
    meaning: INPUT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: test_value_role
    casing: UPPER_SNAKE
    value: EXPECTED
    meaning: EXPECTED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: test_value_role
    casing: UPPER_SNAKE
    value: ASSERT
    meaning: ASSERT
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: test_value_role
    casing: UPPER_SNAKE
    value: RECORDED
    meaning: RECORDED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: transport_direction
    casing: UPPER_SNAKE
    value: INGRESS
    meaning: INGRESS
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: transport_direction
    casing: UPPER_SNAKE
    value: EGRESS
    meaning: EGRESS
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: verification_result
    casing: UPPER_SNAKE
    value: CONFIRMED
    meaning: CONFIRMED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: verification_result
    casing: UPPER_SNAKE
    value: OVERTURNED
    meaning: OVERTURNED
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: yes_no
    casing: UPPER_SNAKE
    value: 'YES'
    meaning: 'YES'
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: yes_no
    casing: UPPER_SNAKE
    value: 'NO'
    meaning: 'NO'
    source_finding:
      phase: p7
      register: new_artifacts
      key: VOCAB_DESIGN_REGISTER_TERMS_V0
  runtime_policies:
  - rb_code: transformation::RB_CONSTRUCTION_BINDINGS_V0
    capability: capability_side_effects::CS_TEXT_ARTIFACT_V0
    key: root
    value: '{{module_data_root}}/construction'
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_CONSTRUCTION_BINDINGS_V0
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    key: snapshot_root
    value: '{{snapshot_root}}'
    source_finding:
      phase: p7
      register: new_artifacts
      key: RB_TRANSFORMATION_BINDINGS_V0
  artifact_properties:
  - artifact: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_CONSTRUCT_ARTIFACTS_V0
  - artifact: transformation::AC_GATE_REVIEWER_V0
    property: type
    value: human
    source_finding:
      phase: p7
      register: new_artifacts
      key: AC_GATE_REVIEWER_V0
  - artifact: transformation::AC_REGISTER_AUTHOR_V0
    property: type
    value: human
    source_finding:
      phase: p7
      register: new_artifacts
      key: AC_REGISTER_AUTHOR_V0
  - artifact: transformation::AC_SEED_AUTHOR_V0
    property: type
    value: human
    source_finding:
      phase: p7
      register: new_artifacts
      key: AC_SEED_AUTHOR_V0
  - artifact: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    property: actor_context
    value: transformation::AC_SEED_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P0_SEED_ADMISSIBILITY_V1
  - artifact: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
  - artifact: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
  - artifact: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
  - artifact: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
  - artifact: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
  - artifact: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
  - artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
  - artifact: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
    source_finding:
      phase: p7
      register: new_artifacts
      key: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
  - artifact: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
    property: maximum
    value: 5
    source_finding:
      phase: p7
      register: new_artifacts
      key: STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
  - artifact: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
    property: minimum
    value: 0
    source_finding:
      phase: p7
      register: new_artifacts
      key: STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
  - artifact: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
    property: deductions
    value:
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
    source_finding:
      phase: p7
      register: new_artifacts
      key: STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
  - artifact: transformation::STRUCTURE_PHASE_FINDINGS_V0
    property: json_schema
    value:
      $schema: https://json-schema.org/draft/2020-12/schema
      $id: transformation::STRUCTURE_PHASE_FINDINGS_V0
      type: array
      items:
        type: object
        additionalProperties: false
        required:
        - code
        - rule
        - locator
        - detail
        - intent
        properties:
          code:
            type: string
          rule:
            type: string
          locator:
            type: object
            additionalProperties: false
            required:
            - register
            - row
            - field
            properties:
              register:
                type:
                - string
                - 'null'
              row:
                type:
                - integer
                - string
                - 'null'
              field:
                type:
                - string
                - 'null'
          detail:
            type: string
          intent:
            type: string
    source_finding:
      phase: p7
      register: new_artifacts
      key: STRUCTURE_PHASE_FINDINGS_V0
  - artifact: transformation::STRUCTURE_PHASE_HEADER_V0
    property: json_schema
    value:
      $schema: https://json-schema.org/draft/2020-12/schema
      $id: transformation::STRUCTURE_PHASE_HEADER_V0
      type: object
      additionalProperties:
        type:
        - string
        - array
        - object
    source_finding:
      phase: p7
      register: new_artifacts
      key: STRUCTURE_PHASE_HEADER_V0
  - artifact: transformation::STRUCTURE_PHASE_PRIORS_V0
    property: json_schema
    value:
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
    source_finding:
      phase: p7
      register: new_artifacts
      key: STRUCTURE_PHASE_PRIORS_V0
  - artifact: transformation::STRUCTURE_PHASE_REGISTERS_V0
    property: json_schema
    value:
      $schema: https://json-schema.org/draft/2020-12/schema
      $id: transformation::STRUCTURE_PHASE_REGISTERS_V0
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
    source_finding:
      phase: p7
      register: new_artifacts
      key: STRUCTURE_PHASE_REGISTERS_V0
  - artifact: transformation::STRUCTURE_PHASE_SECTIONS_V0
    property: json_schema
    value:
      $schema: https://json-schema.org/draft/2020-12/schema
      $id: transformation::STRUCTURE_PHASE_SECTIONS_V0
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
    source_finding:
      phase: p7
      register: new_artifacts
      key: STRUCTURE_PHASE_SECTIONS_V0
  - artifact: transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
    property: phases
    value:
    - phase: p0
      schema: transformation.schemas.REGISTER_SCHEMA_P0_V0
      workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V1
      template: p0_change_seed_template_v0.md
      rung: business_language
      purpose: change seed
      question: What does the business want, stated in its own words?
      key_rule: Faithful rewrite only — no content added, no clarification resolved, no design assigned
      gate: Gate 0 — the human confirms the seed says what they meant
    - phase: p1
      schema: transformation.schemas.REGISTER_SCHEMA_P1_V0
      workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
      template: p1_change_request_template_v0.md
      rung: business_language
      purpose: change request
      question: Classification · Problem · Outcome · Known Facts · Deferrals
      key_rule: Business language only; baseline claims verified against the snapshot, never memory
      gate: null
    - phase: p2
      schema: transformation.schemas.REGISTER_SCHEMA_P2_V0
      workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
      template: p2_domain_model_template_v0.md
      rung: business_language
      purpose: domain model
      question: Entities · Processes · Baseline fit · Gaps
      key_rule: Record what was searched, not only what was found
      gate: null
    - phase: p3
      schema: transformation.schemas.REGISTER_SCHEMA_P3_V0
      workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
      template: p3_analysis_loop_template_v0.md
      rung: business_language
      purpose: analysis loop
      question: How is each gap resolved, iterated to Discovery Saturation?
      key_rule: Every answer carries evidence; overturned answers are marked, never erased
      gate: null
    - phase: p4
      schema: transformation.schemas.REGISTER_SCHEMA_P4_V0
      workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
      template: p4_business_model_template_v0.md
      rung: business_language
      purpose: business model
      question: What is the canonical consolidation every later phase projects from?
      key_rule: Consolidation, not re-litigation
      gate: null
    - phase: p5
      schema: transformation.schemas.REGISTER_SCHEMA_P5_V0
      workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
      template: p5_business_intent_template_v0.md
      rung: provisional_codes
      purpose: business intent
      question: WHAT — behaviour, objects, identity, invariants, actions
      key_rule: Provisional capability names are admissible; no bindings, no paths
      gate: null
    - phase: p6
      schema: transformation.schemas.REGISTER_SCHEMA_P6_V0
      workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
      template: p6_governance_intent_template_v0.md
      rung: placement
      purpose: governance intent
      question: WHERE — domain and subdomain, ownership, dependencies
      key_rule: No new artifact codes; cross-subdomain writes forbidden
      gate: null
    - phase: p7
      schema: transformation.schemas.REGISTER_SCHEMA_P7_V0
      workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
      template: p7_design_intent_template_v0.md
      rung: binding_fqdns
      purpose: design intent
      question: HOW — FQDNs, topology, schemas, stores, module paths, runtime bindings
      key_rule: The full dossier is reviewed as a body
      gate: Gate 1 — Design Approval
    - phase: p8
      schema: transformation.schemas.REGISTER_SCHEMA_P8_V0
      workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
      template: p8_authoring_mandate_template_v0.md
      rung: build_order
      purpose: authoring mandate
      question: IN WHAT ORDER — topologically sorted build waves
      key_rule: Mechanical derivation; must reconcile with p7 exactly
      gate: Gate 2 — Mandate Approval; the dossier is locked
    source_finding:
      phase: p7
      register: new_artifacts
      key: STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: NEW
    subdomain: design
    count: '37'
    artifacts: transformation::AC_GATE_REVIEWER_V0, transformation::AC_REGISTER_AUTHOR_V0, transformation::AC_SEED_AUTHOR_V0,
      transformation::CC_JUDGE_AGAINST_COMPOSITION_V1, transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1, transformation::CC_JUDGE_DOCUMENT_V0,
      transformation::CT_PURE_EVALUATE_RULES_V1, transformation::CT_PURE_PARSE_PRIOR_PHASES_V1, transformation::CT_PURE_PARSE_REGISTERS_V1,
      transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0, transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0,
      transformation::IN_BUSINESS_INTENT_SUBMITTED_V1, transformation::IN_BUSINESS_MODEL_SUBMITTED_V0,
      transformation::IN_CHANGE_REQUEST_SUBMITTED_V0, transformation::IN_DESIGN_INTENT_SUBMITTED_V0, transformation::IN_DOMAIN_MODEL_SUBMITTED_V0,
      transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0, transformation::IN_SEED_SUBMITTED_V0, transformation::RB_TRANSFORMATION_BINDINGS_V0,
      transformation::VOCAB_DESIGN_REGISTER_TERMS_V0, transformation::WF_P0_SEED_ADMISSIBILITY_V1, transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1,
      transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2, transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2,
      transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2, transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2,
      transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2, transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3,
      transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2, transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V1,
      transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1, transformation::STRUCTURE_PHASE_FINDINGS_V0,
      transformation::STRUCTURE_PHASE_HEADER_V0, transformation::STRUCTURE_PHASE_PRIORS_V0, transformation::STRUCTURE_PHASE_REGISTERS_V0,
      transformation::STRUCTURE_PHASE_SECTIONS_V0, transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
  - action: NEW
    subdomain: build
    count: '9'
    artifacts: transformation::CC_CONSTRUCT_ARTIFACTS_V0, transformation::CC_PERSIST_ARTIFACTS_V0, transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1,
      transformation::CT_PURE_MEASURE_COMPLETENESS_V0, transformation::CT_PURE_RENDER_ARTIFACTS_V0, transformation::IN_CONSTRUCTION_REQUESTED_V0,
      transformation::RB_CONSTRUCTION_BINDINGS_V0, transformation::VOCAB_FACT_PROVENANCE_V0, transformation::WF_CONSTRUCT_ARTIFACTS_V0
  generation_provenance:
  - artifact: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - artifact: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry/structures/STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md
    - registry/schema/
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  declared_reach: []
  refusal_discharge: []
  refusal_deferrals:
  - operation: Continue past a gate
    refused_when: The document is inadmissible or not approved.
    deferred_to: The reviewer at each gate
    until: 'Never: outside the module''s scope. Approval is a person''s act. The module records it on
      the document and reports it in every check, and the reviewer refuses to continue without it.'
    source_finding:
      phase: p0
      register: operation_refusals
      row: 1
  - operation: Build a mandate
    refused_when: The mandate has not been approved.
    deferred_to: The person driving the change
    until: 'Never: outside the module''s scope. Construction refuses a mandate that does not determine
      its artifacts. Whether an approved mandate is built is the decision of the person driving the change.'
    source_finding:
      phase: p0
      register: operation_refusals
      row: 2
  - operation: Judge a document
    refused_when: The composition it is designed against is not the one it names.
    deferred_to: The person driving the change, through the baseline check
    until: 'Never: outside the module''s scope. `tc baseline verify` checks the pin before a phase is
      run, and a composition cannot judge whether it is itself the one a document names.'
    source_finding:
      phase: p0
      register: operation_refusals
      row: 3
  refusal_governance_discharge: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    case: attributes_a_supplied_layer_to_the_renderer
    expected_outcome: SUCCESS
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    expected_outcome: SUCCESS
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_design_that_leaves_facts_undetermined
    expected_outcome: VIOLATION
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_value_its_provenance_attributes_to_the_renderer
    expected_outcome: VIOLATION
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    expected_outcome: SUCCESS
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: refuses_a_mandate_scheduling_nothing
    expected_outcome: VIOLATION
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    expected_outcome: SUCCESS
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    expected_outcome: SUCCESS
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_each_prior_by_phase
    expected_outcome: SUCCESS
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read the earlier phase documents a phase must agree with
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_no_prior_when_none_is_handed_over
    expected_outcome: SUCCESS
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read the earlier phase documents a phase must agree with
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    case: reads_header_registers_and_sections
    expected_outcome: SUCCESS
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read a phase document into its registers
  test_case_values:
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    case: attributes_a_supplied_layer_to_the_renderer
    role: INPUT
    field: rendered
    value:
    - path: registry/s/layers/STRUCTURE_S_STORAGE_V0.md
      domain: STRUCTURE_S_STORAGE_V0
      machine:
        fqdn: STRUCTURE_S_STORAGE_V0
        artifact_kind: STRUCTURE
        version: v0
        governed_by: structure::CONSTITUTION_STRUCTURE_V0
        authority: pgc.platform
        concern: s
        core:
          summary: The stores the subdomain owns
          layer: DOMAINS
          domain: STRUCTURE_S_STORAGE_V0
          subdomain: s
          entity_stores: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    case: attributes_a_supplied_layer_to_the_renderer
    role: INPUT
    field: sources
    value:
      STRUCTURE_S_STORAGE_V0:
        core.layer:
        - supplied_by_renderer
        - ''
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    case: attributes_a_supplied_layer_to_the_renderer
    role: EXPECTED
    field: provenance
    value:
      STRUCTURE_S_STORAGE_V0.fqdn: stated_by_design
      STRUCTURE_S_STORAGE_V0.artifact_kind: stated_by_design
      STRUCTURE_S_STORAGE_V0.version: stated_by_design
      STRUCTURE_S_STORAGE_V0.governed_by: stated_by_design
      STRUCTURE_S_STORAGE_V0.authority: stated_by_design
      STRUCTURE_S_STORAGE_V0.concern: stated_by_design
      STRUCTURE_S_STORAGE_V0.core.summary: stated_by_design
      STRUCTURE_S_STORAGE_V0.core.layer: supplied_by_renderer
      STRUCTURE_S_STORAGE_V0.core.domain: stated_by_design
      STRUCTURE_S_STORAGE_V0.core.subdomain: stated_by_design
      STRUCTURE_S_STORAGE_V0.core.entity_stores: stated_by_design
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    case: attributes_a_supplied_layer_to_the_renderer
    role: EXPECTED
    field: governing_artifacts
    value: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: INPUT
    field: design_registers
    value:
    - id: new_artifacts
      value:
      - capability: Reader
        family: AC
        code: AC_READER_V0
        summary: A reader of the catalog
        owner_subdomain: s
        status: NEW
        source_finding:
          source: human
    - id: artifact_properties
      value:
      - artifact: AC_READER_V0
        property: type
        value: human
        source_finding:
          source: human
    - id: interface_fields
      value:
      - artifact: AC_READER_V0
        direction: ATTRIBUTE
        field: role
        type: string
        required: 'YES'
        default: null
        meaning: What the reader does
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: INPUT
    field: mandate_registers
    value:
    - id: build_order
      value:
      - wave: '1'
        code: AC_READER_V0
    - id: field_declarations
      value:
      - code: AC_READER_V0
        subdomain_field: s
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: INPUT
    field: threshold
    value: 100.0
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: INPUT
    field: provenance
    value: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: EXPECTED
    field: completeness
    value: 100.0
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: EXPECTED
    field: determined
    value: 10
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: EXPECTED
    field: required
    value: 10
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: EXPECTED
    field: undetermined
    value: []
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_design_that_leaves_facts_undetermined
    role: INPUT
    field: design_registers
    value:
    - id: new_artifacts
      value:
      - capability: Storage
        family: STRUCTURE
        code: STRUCTURE_S_STORAGE_V0
        summary: The stores the subdomain owns
        owner_subdomain: s
        status: NEW
        source_finding:
          source: human
    - id: structure_stores
      value: []
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_design_that_leaves_facts_undetermined
    role: INPUT
    field: mandate_registers
    value:
    - id: build_order
      value:
      - wave: '1'
        code: STRUCTURE_S_STORAGE_V0
    - id: field_declarations
      value:
      - code: STRUCTURE_S_STORAGE_V0
        subdomain_field: s
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_design_that_leaves_facts_undetermined
    role: INPUT
    field: threshold
    value: 100.0
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_design_that_leaves_facts_undetermined
    role: INPUT
    field: provenance
    value: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_value_its_provenance_attributes_to_the_renderer
    role: INPUT
    field: design_registers
    value:
    - id: new_artifacts
      value:
      - capability: Reader
        family: AC
        code: AC_READER_V0
        summary: A reader of the catalog
        owner_subdomain: s
        status: NEW
        source_finding:
          source: human
    - id: artifact_properties
      value:
      - artifact: AC_READER_V0
        property: type
        value: human
        source_finding:
          source: human
    - id: interface_fields
      value:
      - artifact: AC_READER_V0
        direction: ATTRIBUTE
        field: role
        type: string
        required: 'YES'
        default: null
        meaning: What the reader does
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_value_its_provenance_attributes_to_the_renderer
    role: INPUT
    field: mandate_registers
    value:
    - id: build_order
      value:
      - wave: '1'
        code: AC_READER_V0
    - id: field_declarations
      value:
      - code: AC_READER_V0
        subdomain_field: s
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_value_its_provenance_attributes_to_the_renderer
    role: INPUT
    field: threshold
    value: 100.0
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_value_its_provenance_attributes_to_the_renderer
    role: INPUT
    field: provenance
    value:
      AC_READER_V0.core.type: supplied_by_renderer
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    role: INPUT
    field: design_registers
    value:
    - id: new_artifacts
      value:
      - capability: Reader
        family: AC
        code: AC_READER_V0
        summary: A reader of the catalog
        owner_subdomain: s
        status: NEW
        source_finding:
          source: human
    - id: artifact_properties
      value:
      - artifact: AC_READER_V0
        property: type
        value: human
        source_finding:
          source: human
    - id: interface_fields
      value:
      - artifact: AC_READER_V0
        direction: ATTRIBUTE
        field: role
        type: string
        required: 'YES'
        default: null
        meaning: What the reader does
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    role: INPUT
    field: mandate_registers
    value:
    - id: build_order
      value:
      - wave: '1'
        code: AC_READER_V0
    - id: field_declarations
      value:
      - code: AC_READER_V0
        subdomain_field: s
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    role: EXPECTED
    field: artifacts
    value:
    - path: registry/s/actors/AC_READER_V0.md
      domain: AC_READER_V0
      machine:
        fqdn: AC_READER_V0
        artifact_kind: ACTOR
        version: v0
        governed_by: governance::CONSTITUTION_GOVERNANCE_V0
        authority: pgc.platform
        concern: s
        core:
          summary: A reader of the catalog
          type: human
          attributes:
            role:
              type: string
              required: true
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    role: EXPECTED
    field: documents
    value:
    - path: registry/s/actors/AC_READER_V0.md
      text: "# AC_READER_V0\n\n## Machine\n\n```yaml\nfqdn: AC_READER_V0\nartifact_kind: ACTOR\nversion:\
        \ v0\ngoverned_by: governance::CONSTITUTION_GOVERNANCE_V0\nauthority: pgc.platform\nconcern: s\n\
        core:\n  summary: A reader of the catalog\n  type: human\n  attributes:\n    role:\n      type:\
        \ string\n      required: true\n```\n\n---\n\n## Intent\n\nA reader of the catalog\n"
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    role: EXPECTED
    field: artifact_count
    value: 1
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    role: EXPECTED
    field: sources
    value:
      AC_READER_V0: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: refuses_a_mandate_scheduling_nothing
    role: INPUT
    field: design_registers
    value:
    - id: new_artifacts
      value:
      - capability: Reader
        family: AC
        code: AC_READER_V0
        summary: A reader of the catalog
        owner_subdomain: s
        status: NEW
        source_finding:
          source: human
    - id: artifact_properties
      value:
      - artifact: AC_READER_V0
        property: type
        value: human
        source_finding:
          source: human
    - id: interface_fields
      value:
      - artifact: AC_READER_V0
        direction: ATTRIBUTE
        field: role
        type: string
        required: 'YES'
        default: null
        meaning: What the reader does
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: refuses_a_mandate_scheduling_nothing
    role: INPUT
    field: mandate_registers
    value:
    - id: build_order
      value: []
    - id: field_declarations
      value: []
    source_finding:
      phase: p6
      register: governance_outcome
      key: Render, measure and attribute the artifacts a mandate schedules
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: header
    value:
      phase: p0
      domain: d
      subdomain: s
      cr: c
      rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: sections
    value:
    - number: 12
      title: Out of Scope
      text: '

        Nothing else.'
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: registers
    value:
    - id: out_of_scope
      value:
      - item: Fines
        reason: Not in this release.
    - id: clarification_requests
      value: null
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: document_text
    value: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain: d\n  subdomain:\
      \ s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n  out_of_scope:\n\
      \  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n```\n\n## 12.\
      \ Out of Scope\n\nNothing else.\n"
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: rule_set
    value:
    - id: REGISTER_MISSING
      identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/cr_type/x-derived/TABLE_PRESENT
      check: TABLE_PRESENT
      register: cr_type
      intent: a declared register must be present and readable as rows
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: observed
    value: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: priors
    value: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: EXPECTED
    field: verdict
    value: INADMISSIBLE
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: EXPECTED
    field: findings
    value:
    - code: REGISTER_MISSING
      rule: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/cr_type/x-derived/TABLE_PRESENT
      locator:
        register: cr_type
        row: null
        field: null
      detail: declared register is absent from the document
      intent: a declared register must be present and readable as rows
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: EXPECTED
    field: rules_evaluated
    value: 1
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: header
    value:
      phase: p0
      domain: d
      subdomain: s
      cr: c
      rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: sections
    value:
    - number: 12
      title: Out of Scope
      text: '

        Nothing else.'
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: registers
    value:
    - id: out_of_scope
      value:
      - item: Fines
        reason: Not in this release.
    - id: clarification_requests
      value: null
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: document_text
    value: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain: d\n  subdomain:\
      \ s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n  out_of_scope:\n\
      \  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n```\n\n## 12.\
      \ Out of Scope\n\nNothing else.\n"
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: rule_set
    value:
    - id: REGISTER_MISSING
      identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/out_of_scope/x-derived/TABLE_PRESENT
      check: TABLE_PRESENT
      register: out_of_scope
      intent: a declared register must be present and readable as rows
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: observed
    value: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: priors
    value: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: EXPECTED
    field: verdict
    value: ADMISSIBLE
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: EXPECTED
    field: findings
    value: []
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: EXPECTED
    field: rules_evaluated
    value: 1
    source_finding:
      phase: p6
      register: governance_outcome
      key: Apply every rule of a phase and report each failure
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_each_prior_by_phase
    role: INPUT
    field: prior_texts
    value:
      p0: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain: d\n  subdomain:\
        \ s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n  out_of_scope:\n\
        \  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n```\n\n##\
        \ 12. Out of Scope\n\nNothing else.\n"
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read the earlier phase documents a phase must agree with
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_each_prior_by_phase
    role: EXPECTED
    field: priors
    value:
      p0:
        header:
          phase: p0
          domain: d
          subdomain: s
          cr: c
          rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
        sections:
        - number: 12
          title: Out of Scope
          text: '

            Nothing else.'
        registers:
        - id: out_of_scope
          value:
          - item: Fines
            reason: Not in this release.
        - id: clarification_requests
          value: null
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read the earlier phase documents a phase must agree with
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_no_prior_when_none_is_handed_over
    role: INPUT
    field: prior_texts
    value: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read the earlier phase documents a phase must agree with
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_no_prior_when_none_is_handed_over
    role: EXPECTED
    field: priors
    value: {}
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read the earlier phase documents a phase must agree with
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    case: reads_header_registers_and_sections
    role: INPUT
    field: document_text
    value: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain: d\n  subdomain:\
      \ s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n  out_of_scope:\n\
      \  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n```\n\n## 12.\
      \ Out of Scope\n\nNothing else.\n"
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read a phase document into its registers
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    case: reads_header_registers_and_sections
    role: EXPECTED
    field: header
    value:
      phase: p0
      domain: d
      subdomain: s
      cr: c
      rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read a phase document into its registers
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    case: reads_header_registers_and_sections
    role: EXPECTED
    field: sections
    value:
    - number: 12
      title: Out of Scope
      text: '

        Nothing else.'
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read a phase document into its registers
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    case: reads_header_registers_and_sections
    role: EXPECTED
    field: registers
    value:
    - id: out_of_scope
      value:
      - item: Fines
        reason: Not in this release.
    - id: clarification_requests
      value: null
    source_finding:
      phase: p6
      register: governance_outcome
      key: Read a phase document into its registers
  withdrawn_facts: null
```

HOW the change is built — identities, topology, compositions, bindings and interfaces. Every register
that describes an artifact was read from the live registry by
`scripts/genesis/p7_design_intent.py`; the design decisions and the refusal
deferrals are stated by hand. The three deferrals are the module's scope, not open work: approving a
gate, approving a mandate and confirming a pin are acts of the people driving a change.

---

## 1. Design Decisions Resolution

## 2. Existing Inventory

## 3. New Artifacts

## 4. Runtime Bindings

## 5. Execution Topology

## 6. Capability Contract Composition

### Step Bindings

## 7. Interface Fields

## 8. Implementation Bindings

## 9. Vocabulary Extensions

## 10. Runtime Policies

## 11. Artifact Properties

## 12. Structure Stores

## 13. Transport Bindings

## 14. Artifact Summary

## 15. Generation Provenance

## 16. Declared Reach

## 17. Refusal Discharge

### Refusal Deferrals

### Refusal Governance Discharge

## 18. Molecule Steps

### Molecule Step Bindings

## 19. Test Cases

### Test Case Values

## 20. Withdrawn Facts
