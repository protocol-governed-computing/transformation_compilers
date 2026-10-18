# Design Intent — transformation, baseline

## Machine

```yaml
document:
  phase: p7
  domain: transformation
  subdomain:
  - build
  - design
  - transformation
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution: []
  existing_inventory: []
  new_artifacts:
  - family: CC
    code: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    summary: Measure a design, refuse it if under-determined, and render the artifacts it schedules
    owner_subdomain: build
    status: NEW
  - family: CC
    code: transformation::CC_PERSIST_ARTIFACTS_V0
    summary: Write a rendered construction beneath the root its runtime binding declares
    owner_subdomain: build
    status: NEW
  - family: CT
    code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    summary: Report, for each leaf of a rendered artifact, whether the design stated it, a constitution
      governs it, or the renderer supplied it
    owner_subdomain: build
    status: NEW
  - family: CT
    code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    summary: Measure Construction Completeness and refuse a design that does not determine its artifacts
    owner_subdomain: build
    status: NEW
  - family: CT
    code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    summary: Render every artifact a mandate schedules from the design that determines it
    owner_subdomain: build
    status: NEW
  - family: IN
    code: transformation::IN_CONSTRUCTION_REQUESTED_V0
    summary: Offer an approved design and mandate for construction
    owner_subdomain: build
    status: NEW
  - family: RB
    code: transformation::RB_CONSTRUCTION_BINDINGS_V0
    summary: Runtime bindings for the construction lifecycle
    owner_subdomain: build
    status: NEW
  - family: VOCAB
    code: transformation::VOCAB_FACT_PROVENANCE_V0
    summary: ''
    owner_subdomain: build
    status: NEW
  - family: WF
    code: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    summary: Construct protocol artifacts from an approved design and mandate
    owner_subdomain: build
    status: NEW
  - family: AC
    code: transformation::AC_GATE_REVIEWER_V0
    summary: Human reviewer at a pipeline gate
    owner_subdomain: design
    status: NEW
  - family: AC
    code: transformation::AC_REGISTER_AUTHOR_V0
    summary: Author of record for a phase register
    owner_subdomain: design
    status: NEW
  - family: AC
    code: transformation::AC_SEED_AUTHOR_V0
    summary: Author of record for a seed
    owner_subdomain: design
    status: NEW
  - family: CC
    code: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    summary: Parse a phase document and its priors, observe the composition and its declarations, and
      judge them together
    owner_subdomain: design
    status: NEW
  - family: CC
    code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    summary: Parse a phase document and its priors, observe the composition, and judge them together
    owner_subdomain: design
    status: NEW
  - family: CC
    code: transformation::CC_JUDGE_DOCUMENT_V0
    summary: Parse a phase document and judge it against a declared rule set
    owner_subdomain: design
    status: NEW
  - family: CT
    code: transformation::CT_PURE_EVALUATE_RULES_V1
    summary: Evaluate a declared rule set against parsed registers
    owner_subdomain: design
    status: NEW
  - family: CT
    code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    summary: Parse the upstream phase documents a phase is judged against
    owner_subdomain: design
    status: NEW
  - family: CT
    code: transformation::CT_PURE_PARSE_REGISTERS_V1
    summary: Parse phase document text into structured registers
    owner_subdomain: design
    status: NEW
  - family: IN
    code: transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    summary: Offer an Analysis Loop register for admissibility judgement
    owner_subdomain: design
    status: NEW
  - family: IN
    code: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    summary: Offer an Authoring Mandate for admissibility judgement
    owner_subdomain: design
    status: NEW
  - family: IN
    code: transformation::IN_BUSINESS_INTENT_SUBMITTED_V1
    summary: Offer a Business Intent register for admissibility judgement
    owner_subdomain: design
    status: NEW
  - family: IN
    code: transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    summary: Offer a Business Model register for admissibility judgement
    owner_subdomain: design
    status: NEW
  - family: IN
    code: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    summary: Offer a Change Request register for admissibility judgement
    owner_subdomain: design
    status: NEW
  - family: IN
    code: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    summary: Offer a Design Intent register for admissibility judgement
    owner_subdomain: design
    status: NEW
  - family: IN
    code: transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    summary: Offer a Domain Model register for admissibility judgement
    owner_subdomain: design
    status: NEW
  - family: IN
    code: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    summary: Offer a Governance Intent register for admissibility judgement
    owner_subdomain: design
    status: NEW
  - family: IN
    code: transformation::IN_SEED_SUBMITTED_V0
    summary: Offer a seed document for admissibility judgement
    owner_subdomain: design
    status: NEW
  - family: RB
    code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    summary: Runtime bindings for the transformation phase pipeline
    owner_subdomain: design
    status: NEW
  - family: VOCAB
    code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    summary: ''
    owner_subdomain: design
    status: NEW
  - family: WF
    code: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    summary: Decide whether an offered seed is admissible
    owner_subdomain: design
    status: NEW
  - family: WF
    code: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    summary: Decide whether an offered Change Request register is admissible
    owner_subdomain: design
    status: NEW
  - family: WF
    code: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    summary: Decide whether an offered Domain Model register is admissible
    owner_subdomain: design
    status: NEW
  - family: WF
    code: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    summary: Decide whether an offered Analysis Loop register is admissible
    owner_subdomain: design
    status: NEW
  - family: WF
    code: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    summary: Decide whether an offered Business Model register is admissible
    owner_subdomain: design
    status: NEW
  - family: WF
    code: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    summary: Decide whether an offered Business Intent register is admissible
    owner_subdomain: design
    status: NEW
  - family: WF
    code: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    summary: Decide whether an offered Governance Intent register is admissible
    owner_subdomain: design
    status: NEW
  - family: WF
    code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    summary: Decide whether an offered Design Intent register is admissible
    owner_subdomain: design
    status: NEW
  - family: WF
    code: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    summary: Decide whether an offered Authoring Mandate is admissible
    owner_subdomain: design
    status: NEW
  - family: STRUCTURE
    code: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
    summary: Deterministic figure of merit for a phase document — deduction-based, 0 to 5
    owner_subdomain: transformation
    status: NEW
  - family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_FINDINGS_V0
    summary: 'The rules a phase document failed: each one''s code, identity, place, detail and intent'
    owner_subdomain: transformation
    status: NEW
  - family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_HEADER_V0
    summary: 'A phase document''s header: its Machine block''s `document` mapping, as parsed'
    owner_subdomain: transformation
    status: NEW
  - family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_PRIORS_V0
    summary: The upstream phase documents a phase is judged against, parsed, by phase id
    owner_subdomain: transformation
    status: NEW
  - family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_REGISTERS_V0
    summary: A phase document's registers, by id, each with its value as written
    owner_subdomain: transformation
    status: NEW
  - family: STRUCTURE
    code: transformation::STRUCTURE_PHASE_SECTIONS_V0
    summary: A phase document's prose sections, in order, as parsed
    owner_subdomain: transformation
    status: NEW
  - family: STRUCTURE
    code: transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
    summary: Which register schema, workflow and template each design phase dispatches to
    owner_subdomain: transformation
    status: NEW
  rb_declarations:
  - rb_code: transformation::RB_CONSTRUCTION_BINDINGS_V0
    binds_wf: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    cs_bindings:
    - capability_side_effects::CS_TEXT_ARTIFACT_V0
    storage_structure: null
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: null
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: null
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: null
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: null
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: null
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: null
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: null
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: null
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    binds_wf: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    cs_bindings:
    - capability_side_effects::CS_SNAPSHOT_QUERY_V0
    storage_structure: null
  execution_topology:
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: IN_CONSTRUCTION_REQUESTED_V0
    node_type: IN
    routing:
      ACK: CC_CONSTRUCT_ARTIFACTS_V0
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: CC_CONSTRUCT_ARTIFACTS_V0
    node_type: CC
    routing:
      SUCCESS: CC_PERSIST_ARTIFACTS_V0
      VIOLATION: EXIT_REFUSED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: CC_PERSIST_ARTIFACTS_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_CONSTRUCTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: EXIT_CONSTRUCTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: EXIT_REFUSED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    node: IN_SEED_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: CC_JUDGE_DOCUMENT_V0
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    node: CC_JUDGE_DOCUMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
  - workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    node: IN_CHANGE_REQUEST_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: CC_JUDGE_DOCUMENT_V0
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    node: CC_JUDGE_DOCUMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
  - workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    node: IN_DOMAIN_MODEL_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    node: CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
  - workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    node: IN_ANALYSIS_LOOP_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: CC_JUDGE_AGAINST_COMPOSITION_V1
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    node: CC_JUDGE_AGAINST_COMPOSITION_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
  - workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    node: IN_BUSINESS_MODEL_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    node: CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
  - workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    node: IN_BUSINESS_INTENT_SUBMITTED_V1
    node_type: IN
    routing:
      ACK: CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    node: CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
  - workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    node: IN_GOVERNANCE_INTENT_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    node: CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
  - workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    node: IN_DESIGN_INTENT_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    node: CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    node: IN_AUTHORING_MANDATE_SUBMITTED_V0
    node_type: IN
    routing:
      ACK: CC_JUDGE_AGAINST_SNAPSHOT_V1
      NACK: EXIT_REJECTED
  - workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    node: CC_JUDGE_AGAINST_SNAPSHOT_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_JUDGED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
  - workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    node: EXIT_JUDGED
    node_type: EXIT
    routing: null
  - workflow: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
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
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: parse_design
    direction: INPUT
    field: document_text
    bound_to: inputs.design_text
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: parse_mandate
    direction: INPUT
    field: document_text
    bound_to: inputs.mandate_text
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: INPUT
    field: design_registers
    bound_to: results.parse_design.capability_result.registers
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: INPUT
    field: mandate_registers
    bound_to: results.parse_mandate.capability_result.registers
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: OUTPUT
    field: artifacts
    bound_to: capability_result.artifacts
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: OUTPUT
    field: documents
    bound_to: capability_result.documents
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: OUTPUT
    field: artifact_count
    bound_to: capability_result.artifact_count
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: render_artifacts
    direction: OUTPUT
    field: sources
    bound_to: capability_result.sources
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: attribute_provenance
    direction: INPUT
    field: rendered
    bound_to: results.render_artifacts.capability_result.artifacts
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: attribute_provenance
    direction: INPUT
    field: sources
    bound_to: results.render_artifacts.capability_result.sources
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: attribute_provenance
    direction: OUTPUT
    field: provenance
    bound_to: capability_result.provenance
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: attribute_provenance
    direction: OUTPUT
    field: governing_artifacts
    bound_to: capability_result.governing_artifacts
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: INPUT
    field: design_registers
    bound_to: results.parse_design.capability_result.registers
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: INPUT
    field: mandate_registers
    bound_to: results.parse_mandate.capability_result.registers
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: INPUT
    field: threshold
    bound_to: inputs.threshold
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: INPUT
    field: provenance
    bound_to: results.attribute_provenance.capability_result.provenance
  - owner: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    step: require_determined
    direction: OUTPUT
    field: completeness
    bound_to: capability_result.completeness
  - owner: transformation::CC_PERSIST_ARTIFACTS_V0
    step: write_artifacts
    direction: INPUT
    field: documents
    bound_to: inputs.documents
  - owner: transformation::CC_PERSIST_ARTIFACTS_V0
    step: write_artifacts
    direction: OUTPUT
    field: written
    bound_to: capability_result.written
  - owner: transformation::CC_PERSIST_ARTIFACTS_V0
    step: write_artifacts
    direction: OUTPUT
    field: paths
    bound_to: capability_result.paths
  - owner: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    step: CC_CONSTRUCT_ARTIFACTS_V0
    direction: INPUT
    field: design_text
    bound_to: payload.design_text
  - owner: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    step: CC_CONSTRUCT_ARTIFACTS_V0
    direction: INPUT
    field: mandate_text
    bound_to: payload.mandate_text
  - owner: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    step: CC_CONSTRUCT_ARTIFACTS_V0
    direction: INPUT
    field: threshold
    bound_to: payload.threshold
  - owner: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    step: CC_PERSIST_ARTIFACTS_V0
    direction: INPUT
    field: documents
    bound_to: results.CC_CONSTRUCT_ARTIFACTS_V0.documents
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: parse_registers
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: parse_priors
    direction: INPUT
    field: prior_texts
    bound_to: inputs.prior_texts
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: observe_composition
    direction: INPUT
    field: operation
    bound_to:
      literal: si.artifact.list
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: observe_composition
    direction: INPUT
    field: params
    bound_to:
      literal: {}
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: observe_declarations
    direction: INPUT
    field: operation
    bound_to:
      literal: si.snapshot.summary
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: observe_declarations
    direction: INPUT
    field: params
    bound_to:
      literal: {}
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: header
    bound_to: results.parse_registers.capability_result.header
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: sections
    bound_to: results.parse_registers.capability_result.sections
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: registers
    bound_to: results.parse_registers.capability_result.registers
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: rule_set
    bound_to: inputs.rule_set
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: observed
    bound_to:
      literal:
        si.artifact.list: $.results.observe_composition.capability_result.result.artifacts
        si.snapshot.summary: $.results.observe_declarations.capability_result.result.reuse_visibility
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: INPUT
    field: priors
    bound_to: results.parse_priors.capability_result.priors
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: OUTPUT
    field: verdict
    bound_to: capability_result.verdict
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: OUTPUT
    field: findings
    bound_to: capability_result.findings
  - owner: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    step: evaluate_rules
    direction: OUTPUT
    field: rules_evaluated
    bound_to: capability_result.rules_evaluated
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: parse_registers
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: parse_priors
    direction: INPUT
    field: prior_texts
    bound_to: inputs.prior_texts
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_composition
    direction: INPUT
    field: operation
    bound_to:
      literal: si.artifact.list
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_composition
    direction: INPUT
    field: params
    bound_to:
      literal: {}
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_capabilities
    direction: INPUT
    field: operation
    bound_to:
      literal: si.capability.surface
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_capabilities
    direction: INPUT
    field: params
    bound_to:
      literal: {}
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_reuse_visibility
    direction: INPUT
    field: operation
    bound_to:
      literal: si.snapshot.summary
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_reuse_visibility
    direction: INPUT
    field: params
    bound_to:
      literal: {}
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_store_list
    direction: INPUT
    field: operation
    bound_to:
      literal: si.store.list
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_store_list
    direction: INPUT
    field: params
    bound_to:
      literal: {}
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_rule_set_list
    direction: INPUT
    field: operation
    bound_to:
      literal: si.rule_set.list
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_rule_set_list
    direction: INPUT
    field: params
    bound_to:
      literal: {}
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_behavior_logic_list
    direction: INPUT
    field: operation
    bound_to:
      literal: si.behavior_logic.list
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: observe_behavior_logic_list
    direction: INPUT
    field: params
    bound_to:
      literal: {}
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: header
    bound_to: results.parse_registers.capability_result.header
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: sections
    bound_to: results.parse_registers.capability_result.sections
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: registers
    bound_to: results.parse_registers.capability_result.registers
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: rule_set
    bound_to: inputs.rule_set
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: observed
    bound_to:
      literal:
        si.artifact.list: $.results.observe_composition.capability_result.result.artifacts
        si.behavior_logic.list: $.results.observe_behavior_logic_list.capability_result.result.workflows
        si.capability.surface: $.results.observe_capabilities.capability_result.result.capabilities
        si.capability.surface#contracts: $.results.observe_capabilities.capability_result.result.contracts
        si.capability.surface#intents: $.results.observe_capabilities.capability_result.result.intents
        si.capability.surface#transforms: $.results.observe_capabilities.capability_result.result.transforms
        si.rule_set.list: $.results.observe_rule_set_list.capability_result.result.carriers
        si.snapshot.summary: $.results.observe_reuse_visibility.capability_result.result.reuse_visibility
        si.store.list: $.results.observe_store_list.capability_result.result.stores
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: INPUT
    field: priors
    bound_to: results.parse_priors.capability_result.priors
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: OUTPUT
    field: verdict
    bound_to: capability_result.verdict
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: OUTPUT
    field: findings
    bound_to: capability_result.findings
  - owner: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    step: evaluate_rules
    direction: OUTPUT
    field: rules_evaluated
    bound_to: capability_result.rules_evaluated
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: parse_registers
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: parse_priors
    direction: INPUT
    field: prior_texts
    bound_to: inputs.prior_texts
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: header
    bound_to: results.parse_registers.capability_result.header
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: sections
    bound_to: results.parse_registers.capability_result.sections
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: registers
    bound_to: results.parse_registers.capability_result.registers
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: document_text
    bound_to: inputs.document_text
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: rule_set
    bound_to: inputs.rule_set
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: observed
    bound_to:
      literal: {}
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: INPUT
    field: priors
    bound_to: results.parse_priors.capability_result.priors
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: OUTPUT
    field: verdict
    bound_to: capability_result.verdict
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: OUTPUT
    field: findings
    bound_to: capability_result.findings
  - owner: transformation::CC_JUDGE_DOCUMENT_V0
    step: evaluate_rules
    direction: OUTPUT
    field: rules_evaluated
    bound_to: capability_result.rules_evaluated
  - owner: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    step: CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: document_text
    bound_to: payload.seed_text
  - owner: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    step: CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: prior_texts
    bound_to:
      literal: {}
  - owner: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    step: CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: rule_set
    bound_to:
      literal:
      - id: HEADER_FIELD_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/document/required
        check: HEADER_FIELD_PRESENT
        params:
          fields:
          - phase
          - domain
          - subdomain
          - cr
          - rule_set
        intent: a phase document states its phase, its domain and subdomain, its change, and the rule
          set it was authored under
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/document/properties/phase/const
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - phase
          pattern: ^p0$
        intent: a document's phase is the phase whose rules judge it
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/document/properties/domain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: domain
          type:
            type: string
            minLength: 1
        intent: a document's domain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/document/properties/subdomain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: subdomain
          type:
            type:
            - string
            - array
            items:
              type: string
            minLength: 1
            minItems: 1
        intent: a document's subdomain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/document/properties/cr
        check: HEADER_FIELD_OF_TYPE
        params:
          field: cr
          type:
            type: string
            minLength: 1
        intent: a document's cr takes its declared form
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/document/properties/rule_set/pattern
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - rule_set
          pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P0_V[0-9]+$
        intent: a document's rule_set names a rule set of its own phase
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/document/properties/approval
        check: HEADER_FIELD_OF_TYPE
        params:
          field: approval
          type:
            type: object
            required:
            - gate
            - rule_set
            - state
            additionalProperties: false
            properties:
              gate:
                type: string
                minLength: 1
              rule_set:
                type: string
                pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P0_V[0-9]+$
              state:
                enum:
                - APPROVED
                - MIGRATED
                - RECONFIRMED
        intent: a document's approval takes its declared form
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/subdomain_purpose/minLength
        check: SECTION_HAS_TEXT
        register: subdomain_purpose
        params:
          detail: narrative register is empty — it states nothing
        intent: a narrative register carries the context nothing downstream can rederive
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/cr_type/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: cr_type
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/cr_type/items/required
        check: TABLE_HAS_COLUMNS
        register: cr_type
        params:
          columns:
          - Subdomain
          - Classification
          - Rationale
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/cr_type/minItems
        check: TABLE_HAS_ROWS
        register: cr_type
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/cr_type/items/properties/classification/x-vocab
        check: CELL_IN_VOCABULARY
        register: cr_type
        params:
          column: Classification
          vocabulary:
          - NEW_SUBDOMAIN
          - EXTEND_SUBDOMAIN
          - MODIFY
          - DEPRECATE
        intent: Classification is a controlled vocabulary declared by the template
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/cr_type/x-business-language
        check: CELL_TOKEN_ABSENT
        register: cr_type
        params:
          columns:
          - Subdomain
          - Classification
          - Rationale
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_vocabulary/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: business_vocabulary
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_vocabulary/items/required
        check: TABLE_HAS_COLUMNS
        register: business_vocabulary
        params:
          columns:
          - Term
          - Definition
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_vocabulary/minItems
        check: TABLE_HAS_ROWS
        register: business_vocabulary
        intent: an empty required register asserts nothing
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_vocabulary/x-business-language
        check: CELL_TOKEN_ABSENT
        register: business_vocabulary
        params:
          columns:
          - Term
          - Definition
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/requested_outcomes/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: requested_outcomes
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/requested_outcomes/items/required
        check: TABLE_HAS_COLUMNS
        register: requested_outcomes
        params:
          columns:
          - Outcome
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/requested_outcomes/minItems
        check: TABLE_HAS_ROWS
        register: requested_outcomes
        intent: an empty required register asserts nothing
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/requested_outcomes/x-business-language
        check: CELL_TOKEN_ABSENT
        register: requested_outcomes
        params:
          columns:
          - Outcome
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/known_facts/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: known_facts
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/known_facts/items/required
        check: TABLE_HAS_COLUMNS
        register: known_facts
        params:
          columns:
          - Fact
          - Certainty
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/known_facts/minItems
        check: TABLE_HAS_ROWS
        register: known_facts
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/known_facts/items/properties/certainty/x-vocab
        check: CELL_IN_VOCABULARY
        register: known_facts
        params:
          column: Certainty
          vocabulary:
          - HIGH
          - MEDIUM
          - LOW
        intent: Certainty is a controlled vocabulary declared by the template
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/known_facts/x-business-language
        check: CELL_TOKEN_ABSENT
        register: known_facts
        params:
          columns:
          - Fact
          - Certainty
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/system_beliefs/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: system_beliefs
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/system_beliefs/items/required
        check: TABLE_HAS_COLUMNS
        register: system_beliefs
        params:
          columns:
          - Belief
          - Why It Matters
          - Verification Goal
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/system_beliefs/minItems
        check: TABLE_HAS_ROWS
        register: system_beliefs
        intent: an empty required register asserts nothing
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/system_beliefs/x-business-language
        check: CELL_TOKEN_ABSENT
        register: system_beliefs
        params:
          columns:
          - Belief
          - Why It Matters
          - Verification Goal
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/assumptions/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: assumptions
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/assumptions/items/required
        check: TABLE_HAS_COLUMNS
        register: assumptions
        params:
          columns:
          - Assumption
          - Basis
        intent: downstream phases read these columns by name
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/assumptions/x-business-language
        check: CELL_TOKEN_ABSENT
        register: assumptions
        params:
          columns:
          - Assumption
          - Basis
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/constraints/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: constraints
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/constraints/items/required
        check: TABLE_HAS_COLUMNS
        register: constraints
        params:
          columns:
          - Constraint
          - Source
        intent: downstream phases read these columns by name
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/constraints/x-business-language
        check: CELL_TOKEN_ABSENT
        register: constraints
        params:
          columns:
          - Constraint
          - Source
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_invariants/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: business_invariants
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_invariants/items/required
        check: TABLE_HAS_COLUMNS
        register: business_invariants
        params:
          columns:
          - Invariant
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_invariants/minItems
        check: TABLE_HAS_ROWS
        register: business_invariants
        intent: an empty required register asserts nothing
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_invariants/x-business-language
        check: CELL_TOKEN_ABSENT
        register: business_invariants
        params:
          columns:
          - Invariant
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/lifecycle_states/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: lifecycle_states
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/lifecycle_states/items/required
        check: TABLE_HAS_COLUMNS
        register: lifecycle_states
        params:
          columns:
          - Object
          - State
          - Meaning
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/lifecycle_states/minItems
        check: TABLE_HAS_ROWS
        register: lifecycle_states
        intent: an empty required register asserts nothing
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/lifecycle_states/x-business-language
        check: CELL_TOKEN_ABSENT
        register: lifecycle_states
        params:
          columns:
          - Object
          - State
          - Meaning
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_events/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: business_events
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_events/items/required
        check: TABLE_HAS_COLUMNS
        register: business_events
        params:
          columns:
          - Event
          - When It Occurs
          - Significance
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_events/minItems
        check: TABLE_HAS_ROWS
        register: business_events
        intent: an empty required register asserts nothing
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/business_events/x-business-language
        check: CELL_TOKEN_ABSENT
        register: business_events
        params:
          columns:
          - Event
          - When It Occurs
          - Significance
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/authority_boundaries/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: authority_boundaries
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/authority_boundaries/items/required
        check: TABLE_HAS_COLUMNS
        register: authority_boundaries
        params:
          columns:
          - Business Object
          - Authoritative Owner
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/authority_boundaries/minItems
        check: TABLE_HAS_ROWS
        register: authority_boundaries
        intent: an empty required register asserts nothing
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/authority_boundaries/x-business-language
        check: CELL_TOKEN_ABSENT
        register: authority_boundaries
        params:
          columns:
          - Business Object
          - Authoritative Owner
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/out_of_scope/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: out_of_scope
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/out_of_scope/items/required
        check: TABLE_HAS_COLUMNS
        register: out_of_scope
        params:
          columns:
          - Item
          - Reason
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/out_of_scope/minItems
        check: TABLE_HAS_ROWS
        register: out_of_scope
        intent: an empty required register asserts nothing
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/out_of_scope/x-business-language
        check: CELL_TOKEN_ABSENT
        register: out_of_scope
        params:
          columns:
          - Item
          - Reason
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/governance_scope/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: governance_scope
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/governance_scope/items/required
        check: TABLE_HAS_COLUMNS
        register: governance_scope
        params:
          columns:
          - Scope Item
          - Relationship
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/governance_scope/minItems
        check: TABLE_HAS_ROWS
        register: governance_scope
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/governance_scope/items/properties/relationship/x-vocab
        check: CELL_IN_VOCABULARY
        register: governance_scope
        params:
          column: Relationship
          vocabulary:
          - CREATED
          - EXTENDED
          - MODIFIED
          - DEPRECATED
          - ADJACENT
        intent: Relationship is a controlled vocabulary declared by the template
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/governance_scope/x-business-language
        check: CELL_TOKEN_ABSENT
        register: governance_scope
        params:
          columns:
          - Scope Item
          - Relationship
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/clarification_requests/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: clarification_requests
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/clarification_requests/items/required
        check: TABLE_HAS_COLUMNS
        register: clarification_requests
        params:
          columns:
          - Question
          - Why Needed
          - Blocking
          - Owner
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/clarification_requests/items/properties/blocking/x-vocab
        check: CELL_IN_VOCABULARY
        register: clarification_requests
        params:
          column: Blocking
          vocabulary:
          - 'YES'
          - 'NO'
        intent: Blocking is a controlled vocabulary declared by the template
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/clarification_requests/items/properties/owner/x-vocab
        check: CELL_IN_VOCABULARY
        register: clarification_requests
        params:
          column: Owner
          vocabulary:
          - HUMAN
          - SNAPSHOT
          - GOVERNANCE
        intent: Owner is a controlled vocabulary declared by the template
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/clarification_requests/x-business-language
        check: CELL_TOKEN_ABSENT
        register: clarification_requests
        params:
          columns:
          - Question
          - Why Needed
          - Blocking
          - Owner
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/acceptance_criteria/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: acceptance_criteria
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/acceptance_criteria/items/required
        check: TABLE_HAS_COLUMNS
        register: acceptance_criteria
        params:
          columns:
          - Criterion
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/acceptance_criteria/minItems
        check: TABLE_HAS_ROWS
        register: acceptance_criteria
        intent: an empty required register asserts nothing
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/acceptance_criteria/x-business-language
        check: CELL_TOKEN_ABSENT
        register: acceptance_criteria
        params:
          columns:
          - Criterion
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/identity_and_sameness/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: identity_and_sameness
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/identity_and_sameness/items/required
        check: TABLE_HAS_COLUMNS
        register: identity_and_sameness
        params:
          columns:
          - Business Object
          - Identified By
          - Two Are The Same When
        intent: downstream phases read these columns by name
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/identity_and_sameness/x-business-language
        check: CELL_TOKEN_ABSENT
        register: identity_and_sameness
        params:
          columns:
          - Business Object
          - Identified By
          - Two Are The Same When
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/lifecycle_transitions/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: lifecycle_transitions
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/lifecycle_transitions/items/required
        check: TABLE_HAS_COLUMNS
        register: lifecycle_transitions
        params:
          columns:
          - Object
          - From State
          - To State
          - Triggered By
          - Cascade
        intent: downstream phases read these columns by name
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/lifecycle_transitions/x-business-language
        check: CELL_TOKEN_ABSENT
        register: lifecycle_transitions
        params:
          columns:
          - Object
          - From State
          - To State
          - Triggered By
          - Cascade
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/operation_refusals/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: operation_refusals
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/operation_refusals/items/required
        check: TABLE_HAS_COLUMNS
        register: operation_refusals
        params:
          columns:
          - Operation
          - Refused When
          - Business Reason
        intent: downstream phases read these columns by name
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/operation_refusals/x-business-language
        check: CELL_TOKEN_ABSENT
        register: operation_refusals
        params:
          columns:
          - Operation
          - Refused When
          - Business Reason
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/authority_deferrals/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: authority_deferrals
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/authority_deferrals/items/required
        check: TABLE_HAS_COLUMNS
        register: authority_deferrals
        params:
          columns:
          - Business Object
          - Deferred To
          - Until
        intent: downstream phases read these columns by name
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/properties/registers/properties/authority_deferrals/x-business-language
        check: CELL_TOKEN_ABSENT
        register: authority_deferrals
        params:
          columns:
          - Business Object
          - Deferred To
          - Until
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: BELIEF_CARRIES_CERTAINTY
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/allOf/0
        check: COLUMN_ABSENT
        register: system_beliefs
        params:
          column: Certainty
          detail: beliefs must not carry a Certainty column — that would make them facts
        intent: the truth/belief split is what P2 verification depends on
      - id: BELIEF_WITHOUT_VERIFICATION_GOAL
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/allOf/1
        check: CELL_NOT_EMPTY
        register: system_beliefs
        params:
          column: Verification Goal
          detail: every belief must state what P2 has to establish
        intent: an unverifiable belief silently becomes an assumption
      - id: BELIEF_STATED_AS_FACT
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/allOf/2
        check: CELL_TOKEN_ABSENT
        register: system_beliefs
        params:
          columns:
          - Belief
          pattern: (?i)^(?:there is|there are|the system provides|the system has|it is confirmed|confirmed:)(?=\s)
          detail: belief is asserted, not suspected ({token!r}) — state it as a belief or move it to Known
            Facts
        intent: P0 must not promote a System Belief to a Known Fact
      - id: REGISTER_CELL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/allOf/3
        check: UNRESOLVED_MARKER_ABSENT
        params:
          exempt:
          - clarification_requests
          detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask
            it as a clarification, do not hedge it in a register'
        intent: an unanswered question left in a register reads as decided to every later phase
      - id: BLOCKING_CLARIFICATION_OUTSTANDING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/allOf/4
        check: ROW_ABSENT_WHEN
        register: clarification_requests
        params:
          column: Blocking
          value: 'YES'
          detail: a blocking clarification is unanswered — resolve it with the named owner and fold the
            answer into the document before any phase consumes it
        intent: a blocking question the next phase never sees is answered by invention
      - id: BUSINESS_CLARIFICATION_OUTSTANDING
        identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/allOf/5
        check: ROW_ABSENT_WHEN
        register: clarification_requests
        params:
          column: Owner
          value: HUMAN
          detail: only the business can answer this — ask it, fold the answer into the problem statement,
            and re-author the seed rather than carrying the question forward
        intent: a business question that outlives the seed is answered downstream by inference
  - owner: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    step: CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
  - owner: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    step: CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
  - owner: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    step: CC_JUDGE_DOCUMENT_V0
    direction: INPUT
    field: rule_set
    bound_to:
      literal:
      - id: HEADER_FIELD_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/document/required
        check: HEADER_FIELD_PRESENT
        params:
          fields:
          - phase
          - domain
          - subdomain
          - cr
          - rule_set
        intent: a phase document states its phase, its domain and subdomain, its change, and the rule
          set it was authored under
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/document/properties/phase/const
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - phase
          pattern: ^p1$
        intent: a document's phase is the phase whose rules judge it
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/document/properties/domain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: domain
          type:
            type: string
            minLength: 1
        intent: a document's domain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/document/properties/subdomain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: subdomain
          type:
            type:
            - string
            - array
            items:
              type: string
            minLength: 1
            minItems: 1
        intent: a document's subdomain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/document/properties/cr
        check: HEADER_FIELD_OF_TYPE
        params:
          field: cr
          type:
            type: string
            minLength: 1
        intent: a document's cr takes its declared form
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/document/properties/rule_set/pattern
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - rule_set
          pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P1_V[0-9]+$
        intent: a document's rule_set names a rule set of its own phase
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/cr_type/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: cr_type
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/cr_type/items/required
        check: TABLE_HAS_COLUMNS
        register: cr_type
        params:
          columns:
          - Subdomain
          - Classification
          - Rationale
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/cr_type/minItems
        check: TABLE_HAS_ROWS
        register: cr_type
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/cr_type/items/properties/classification/x-vocab
        check: CELL_IN_VOCABULARY
        register: cr_type
        params:
          column: Classification
          vocabulary:
          - NEW_SUBDOMAIN
          - EXTEND_SUBDOMAIN
          - MODIFY
          - DEPRECATE
        intent: Classification is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/cr_type/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: cr_type
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/cr_type/x-business-language
        check: CELL_TOKEN_ABSENT
        register: cr_type
        params:
          columns:
          - Subdomain
          - Classification
          - Rationale
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/cr_type/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: cr_type
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/cr_type/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: cr_type
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/cr_type/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: cr_type
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_vocabulary/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: business_vocabulary
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_vocabulary/items/required
        check: TABLE_HAS_COLUMNS
        register: business_vocabulary
        params:
          columns:
          - Term
          - Definition
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_vocabulary/minItems
        check: TABLE_HAS_ROWS
        register: business_vocabulary
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_vocabulary/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: business_vocabulary
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_vocabulary/x-business-language
        check: CELL_TOKEN_ABSENT
        register: business_vocabulary
        params:
          columns:
          - Term
          - Definition
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_vocabulary/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: business_vocabulary
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_vocabulary/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: business_vocabulary
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_vocabulary/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: business_vocabulary
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/requested_outcomes/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: requested_outcomes
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/requested_outcomes/items/required
        check: TABLE_HAS_COLUMNS
        register: requested_outcomes
        params:
          columns:
          - Outcome
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/requested_outcomes/minItems
        check: TABLE_HAS_ROWS
        register: requested_outcomes
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/requested_outcomes/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: requested_outcomes
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/requested_outcomes/x-business-language
        check: CELL_TOKEN_ABSENT
        register: requested_outcomes
        params:
          columns:
          - Outcome
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/requested_outcomes/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: requested_outcomes
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/requested_outcomes/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: requested_outcomes
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/requested_outcomes/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: requested_outcomes
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/known_facts/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: known_facts
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/known_facts/items/required
        check: TABLE_HAS_COLUMNS
        register: known_facts
        params:
          columns:
          - Fact
          - Certainty
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/known_facts/minItems
        check: TABLE_HAS_ROWS
        register: known_facts
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/known_facts/items/properties/certainty/x-vocab
        check: CELL_IN_VOCABULARY
        register: known_facts
        params:
          column: Certainty
          vocabulary:
          - HIGH
          - MEDIUM
          - LOW
        intent: Certainty is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/known_facts/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: known_facts
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/known_facts/x-business-language
        check: CELL_TOKEN_ABSENT
        register: known_facts
        params:
          columns:
          - Fact
          - Certainty
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/known_facts/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: known_facts
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/known_facts/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: known_facts
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/known_facts/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: known_facts
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/system_beliefs/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: system_beliefs
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/system_beliefs/items/required
        check: TABLE_HAS_COLUMNS
        register: system_beliefs
        params:
          columns:
          - Belief
          - Why It Matters
          - Verification Goal
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/system_beliefs/minItems
        check: TABLE_HAS_ROWS
        register: system_beliefs
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/system_beliefs/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: system_beliefs
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/system_beliefs/x-business-language
        check: CELL_TOKEN_ABSENT
        register: system_beliefs
        params:
          columns:
          - Belief
          - Why It Matters
          - Verification Goal
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/system_beliefs/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: system_beliefs
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/system_beliefs/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: system_beliefs
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/system_beliefs/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: system_beliefs
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/assumptions/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: assumptions
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/assumptions/items/required
        check: TABLE_HAS_COLUMNS
        register: assumptions
        params:
          columns:
          - Assumption
          - Basis
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/assumptions/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: assumptions
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/assumptions/x-business-language
        check: CELL_TOKEN_ABSENT
        register: assumptions
        params:
          columns:
          - Assumption
          - Basis
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/assumptions/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: assumptions
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/assumptions/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: assumptions
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/assumptions/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: assumptions
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/constraints/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: constraints
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/constraints/items/required
        check: TABLE_HAS_COLUMNS
        register: constraints
        params:
          columns:
          - Constraint
          - Source
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/constraints/minItems
        check: TABLE_HAS_ROWS
        register: constraints
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/constraints/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: constraints
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/constraints/x-business-language
        check: CELL_TOKEN_ABSENT
        register: constraints
        params:
          columns:
          - Constraint
          - Source
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/constraints/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: constraints
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/constraints/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: constraints
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/constraints/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: constraints
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_invariants/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: business_invariants
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_invariants/items/required
        check: TABLE_HAS_COLUMNS
        register: business_invariants
        params:
          columns:
          - Invariant
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_invariants/minItems
        check: TABLE_HAS_ROWS
        register: business_invariants
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_invariants/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: business_invariants
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_invariants/x-business-language
        check: CELL_TOKEN_ABSENT
        register: business_invariants
        params:
          columns:
          - Invariant
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_invariants/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: business_invariants
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_invariants/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: business_invariants
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_invariants/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: business_invariants
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_states/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: lifecycle_states
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_states/items/required
        check: TABLE_HAS_COLUMNS
        register: lifecycle_states
        params:
          columns:
          - Object
          - State
          - Meaning
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_states/minItems
        check: TABLE_HAS_ROWS
        register: lifecycle_states
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_states/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: lifecycle_states
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_states/x-business-language
        check: CELL_TOKEN_ABSENT
        register: lifecycle_states
        params:
          columns:
          - Object
          - State
          - Meaning
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_states/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: lifecycle_states
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_states/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: lifecycle_states
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_states/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: lifecycle_states
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_events/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: business_events
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_events/items/required
        check: TABLE_HAS_COLUMNS
        register: business_events
        params:
          columns:
          - Event
          - When It Occurs
          - Significance
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_events/minItems
        check: TABLE_HAS_ROWS
        register: business_events
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_events/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: business_events
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_events/x-business-language
        check: CELL_TOKEN_ABSENT
        register: business_events
        params:
          columns:
          - Event
          - When It Occurs
          - Significance
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_events/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: business_events
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_events/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: business_events
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/business_events/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: business_events
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_boundaries/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: authority_boundaries
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_boundaries/items/required
        check: TABLE_HAS_COLUMNS
        register: authority_boundaries
        params:
          columns:
          - Business Object
          - Authoritative Owner
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_boundaries/minItems
        check: TABLE_HAS_ROWS
        register: authority_boundaries
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_boundaries/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: authority_boundaries
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_boundaries/x-business-language
        check: CELL_TOKEN_ABSENT
        register: authority_boundaries
        params:
          columns:
          - Business Object
          - Authoritative Owner
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_boundaries/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: authority_boundaries
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_boundaries/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: authority_boundaries
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_boundaries/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: authority_boundaries
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/out_of_scope/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: out_of_scope
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/out_of_scope/items/required
        check: TABLE_HAS_COLUMNS
        register: out_of_scope
        params:
          columns:
          - Item
          - Reason
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/out_of_scope/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: out_of_scope
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/out_of_scope/x-business-language
        check: CELL_TOKEN_ABSENT
        register: out_of_scope
        params:
          columns:
          - Item
          - Reason
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/out_of_scope/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: out_of_scope
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/out_of_scope/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: out_of_scope
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/out_of_scope/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: out_of_scope
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/governance_scope/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: governance_scope
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/governance_scope/items/required
        check: TABLE_HAS_COLUMNS
        register: governance_scope
        params:
          columns:
          - Scope Item
          - Relationship
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/governance_scope/minItems
        check: TABLE_HAS_ROWS
        register: governance_scope
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/governance_scope/items/properties/relationship/x-vocab
        check: CELL_IN_VOCABULARY
        register: governance_scope
        params:
          column: Relationship
          vocabulary:
          - CREATED
          - EXTENDED
          - MODIFIED
          - DEPRECATED
          - ADJACENT
        intent: Relationship is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/governance_scope/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: governance_scope
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/governance_scope/x-business-language
        check: CELL_TOKEN_ABSENT
        register: governance_scope
        params:
          columns:
          - Scope Item
          - Relationship
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/governance_scope/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: governance_scope
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/governance_scope/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: governance_scope
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/governance_scope/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: governance_scope
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/clarification_requests/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: clarification_requests
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/clarification_requests/items/required
        check: TABLE_HAS_COLUMNS
        register: clarification_requests
        params:
          columns:
          - Question
          - Why Needed
          - Blocking
          - Owner
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/clarification_requests/items/properties/blocking/x-vocab
        check: CELL_IN_VOCABULARY
        register: clarification_requests
        params:
          column: Blocking
          vocabulary:
          - 'YES'
          - 'NO'
        intent: Blocking is a controlled vocabulary declared by the template
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/clarification_requests/items/properties/owner/x-vocab
        check: CELL_IN_VOCABULARY
        register: clarification_requests
        params:
          column: Owner
          vocabulary:
          - HUMAN
          - SNAPSHOT
          - GOVERNANCE
        intent: Owner is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/clarification_requests/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: clarification_requests
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/clarification_requests/x-business-language
        check: CELL_TOKEN_ABSENT
        register: clarification_requests
        params:
          columns:
          - Question
          - Why Needed
          - Blocking
          - Owner
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/clarification_requests/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: clarification_requests
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/clarification_requests/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: clarification_requests
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/clarification_requests/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: clarification_requests
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/acceptance_criteria/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: acceptance_criteria
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/acceptance_criteria/items/required
        check: TABLE_HAS_COLUMNS
        register: acceptance_criteria
        params:
          columns:
          - Criterion
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/acceptance_criteria/minItems
        check: TABLE_HAS_ROWS
        register: acceptance_criteria
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/acceptance_criteria/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: acceptance_criteria
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/acceptance_criteria/x-business-language
        check: CELL_TOKEN_ABSENT
        register: acceptance_criteria
        params:
          columns:
          - Criterion
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/acceptance_criteria/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: acceptance_criteria
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/acceptance_criteria/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: acceptance_criteria
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/acceptance_criteria/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: acceptance_criteria
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/identity_and_sameness/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: identity_and_sameness
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/identity_and_sameness/items/required
        check: TABLE_HAS_COLUMNS
        register: identity_and_sameness
        params:
          columns:
          - Business Object
          - Identified By
          - Two Are The Same When
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/identity_and_sameness/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: identity_and_sameness
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/identity_and_sameness/x-business-language
        check: CELL_TOKEN_ABSENT
        register: identity_and_sameness
        params:
          columns:
          - Business Object
          - Identified By
          - Two Are The Same When
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/identity_and_sameness/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: identity_and_sameness
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/identity_and_sameness/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: identity_and_sameness
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/identity_and_sameness/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: identity_and_sameness
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_transitions/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: lifecycle_transitions
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_transitions/items/required
        check: TABLE_HAS_COLUMNS
        register: lifecycle_transitions
        params:
          columns:
          - Object
          - From State
          - To State
          - Triggered By
          - Cascade
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_transitions/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: lifecycle_transitions
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_transitions/x-business-language
        check: CELL_TOKEN_ABSENT
        register: lifecycle_transitions
        params:
          columns:
          - Object
          - From State
          - To State
          - Triggered By
          - Cascade
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_transitions/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: lifecycle_transitions
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_transitions/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: lifecycle_transitions
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/lifecycle_transitions/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: lifecycle_transitions
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/operation_refusals/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: operation_refusals
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/operation_refusals/items/required
        check: TABLE_HAS_COLUMNS
        register: operation_refusals
        params:
          columns:
          - Operation
          - Refused When
          - Business Reason
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/operation_refusals/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: operation_refusals
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/operation_refusals/x-business-language
        check: CELL_TOKEN_ABSENT
        register: operation_refusals
        params:
          columns:
          - Operation
          - Refused When
          - Business Reason
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/operation_refusals/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: operation_refusals
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/operation_refusals/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: operation_refusals
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/operation_refusals/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: operation_refusals
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_deferrals/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: authority_deferrals
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_deferrals/items/required
        check: TABLE_HAS_COLUMNS
        register: authority_deferrals
        params:
          columns:
          - Business Object
          - Deferred To
          - Until
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_deferrals/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: authority_deferrals
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_deferrals/x-business-language
        check: CELL_TOKEN_ABSENT
        register: authority_deferrals
        params:
          columns:
          - Business Object
          - Deferred To
          - Until
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_deferrals/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: authority_deferrals
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_deferrals/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: authority_deferrals
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/properties/registers/properties/authority_deferrals/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: authority_deferrals
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/0
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: system_beliefs
        params:
          prior_phase: p0
          prior_register: system_beliefs
          prior_key_column: Belief
          key_column: Belief
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/1
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: requested_outcomes
        params:
          prior_phase: p0
          prior_register: requested_outcomes
          prior_key_column: Outcome
          key_column: Outcome
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/2
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: business_invariants
        params:
          prior_phase: p0
          prior_register: business_invariants
          prior_key_column: Invariant
          key_column: Invariant
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/3
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: acceptance_criteria
        params:
          prior_phase: p0
          prior_register: acceptance_criteria
          prior_key_column: Criterion
          key_column: Criterion
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/4
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: known_facts
        params:
          prior_phase: p0
          prior_register: known_facts
          prior_key_column: Fact
          key_column: Fact
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/5
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: business_vocabulary
        params:
          prior_phase: p0
          prior_register: business_vocabulary
          prior_key_column: Term
          key_column: Term
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/6
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: constraints
        params:
          prior_phase: p0
          prior_register: constraints
          prior_key_column: Constraint
          key_column: Constraint
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/7
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: assumptions
        params:
          prior_phase: p0
          prior_register: assumptions
          prior_key_column: Assumption
          key_column: Assumption
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/8
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: business_events
        params:
          prior_phase: p0
          prior_register: business_events
          prior_key_column: Event
          key_column: Event
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/9
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: authority_boundaries
        params:
          prior_phase: p0
          prior_register: authority_boundaries
          prior_key_column: Business Object
          key_column: Business Object
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/10
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: out_of_scope
        params:
          prior_phase: p0
          prior_register: out_of_scope
          prior_key_column: Item
          key_column: Item
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/11
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: governance_scope
        params:
          prior_phase: p0
          prior_register: governance_scope
          prior_key_column: Scope Item
          key_column: Scope Item
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/12
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: identity_and_sameness
        params:
          prior_phase: p0
          prior_register: identity_and_sameness
          prior_key_column: Business Object
          key_column: Business Object
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/13
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: authority_deferrals
        params:
          prior_phase: p0
          prior_register: authority_deferrals
          prior_key_column: Business Object
          key_column: Business Object
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/14
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: lifecycle_states
        params:
          prior_phase: p0
          prior_register: lifecycle_states
          prior_key_column:
          - Object
          - State
          key_column:
          - Object
          - State
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/15
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: lifecycle_transitions
        params:
          prior_phase: p0
          prior_register: lifecycle_transitions
          prior_key_column:
          - Object
          - From State
          - To State
          key_column:
          - Object
          - From State
          - To State
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: SEED_ROW_NOT_CARRIED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/16
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: operation_refusals
        params:
          prior_phase: p0
          prior_register: operation_refusals
          prior_key_column:
          - Operation
          - Refused When
          key_column:
          - Operation
          - Refused When
        intent: P0 reorganizes and P1 restates; neither may drop what the business said
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/17
        check: ROWS_CONFINED_TO_PRIOR
        register: system_beliefs
        params:
          prior_phase: p0
          prior_register: system_beliefs
          prior_key_column: Belief
          key_column: Belief
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/18
        check: ROWS_CONFINED_TO_PRIOR
        register: requested_outcomes
        params:
          prior_phase: p0
          prior_register: requested_outcomes
          prior_key_column: Outcome
          key_column: Outcome
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/19
        check: ROWS_CONFINED_TO_PRIOR
        register: business_invariants
        params:
          prior_phase: p0
          prior_register: business_invariants
          prior_key_column: Invariant
          key_column: Invariant
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/20
        check: ROWS_CONFINED_TO_PRIOR
        register: acceptance_criteria
        params:
          prior_phase: p0
          prior_register: acceptance_criteria
          prior_key_column: Criterion
          key_column: Criterion
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/21
        check: ROWS_CONFINED_TO_PRIOR
        register: known_facts
        params:
          prior_phase: p0
          prior_register: known_facts
          prior_key_column: Fact
          key_column: Fact
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/22
        check: ROWS_CONFINED_TO_PRIOR
        register: business_vocabulary
        params:
          prior_phase: p0
          prior_register: business_vocabulary
          prior_key_column: Term
          key_column: Term
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/23
        check: ROWS_CONFINED_TO_PRIOR
        register: constraints
        params:
          prior_phase: p0
          prior_register: constraints
          prior_key_column: Constraint
          key_column: Constraint
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/24
        check: ROWS_CONFINED_TO_PRIOR
        register: assumptions
        params:
          prior_phase: p0
          prior_register: assumptions
          prior_key_column: Assumption
          key_column: Assumption
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/25
        check: ROWS_CONFINED_TO_PRIOR
        register: business_events
        params:
          prior_phase: p0
          prior_register: business_events
          prior_key_column: Event
          key_column: Event
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/26
        check: ROWS_CONFINED_TO_PRIOR
        register: authority_boundaries
        params:
          prior_phase: p0
          prior_register: authority_boundaries
          prior_key_column: Business Object
          key_column: Business Object
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/27
        check: ROWS_CONFINED_TO_PRIOR
        register: out_of_scope
        params:
          prior_phase: p0
          prior_register: out_of_scope
          prior_key_column: Item
          key_column: Item
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/28
        check: ROWS_CONFINED_TO_PRIOR
        register: governance_scope
        params:
          prior_phase: p0
          prior_register: governance_scope
          prior_key_column: Scope Item
          key_column: Scope Item
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/29
        check: ROWS_CONFINED_TO_PRIOR
        register: identity_and_sameness
        params:
          prior_phase: p0
          prior_register: identity_and_sameness
          prior_key_column: Business Object
          key_column: Business Object
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/30
        check: ROWS_CONFINED_TO_PRIOR
        register: authority_deferrals
        params:
          prior_phase: p0
          prior_register: authority_deferrals
          prior_key_column: Business Object
          key_column: Business Object
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/31
        check: ROWS_CONFINED_TO_PRIOR
        register: lifecycle_states
        params:
          prior_phase: p0
          prior_register: lifecycle_states
          prior_key_column:
          - Object
          - State
          key_column:
          - Object
          - State
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/32
        check: ROWS_CONFINED_TO_PRIOR
        register: lifecycle_transitions
        params:
          prior_phase: p0
          prior_register: lifecycle_transitions
          prior_key_column:
          - Object
          - From State
          - To State
          key_column:
          - Object
          - From State
          - To State
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: ROW_NOT_IN_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/33
        check: ROWS_CONFINED_TO_PRIOR
        register: operation_refusals
        params:
          prior_phase: p0
          prior_register: operation_refusals
          prior_key_column:
          - Operation
          - Refused When
          key_column:
          - Operation
          - Refused When
        intent: P1 interrogates and restates; business content enters at P0 or not at all
      - id: REGISTER_CELL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/34
        check: UNRESOLVED_MARKER_ABSENT
        params:
          exempt:
          - clarification_requests
          detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask
            it as a clarification, do not hedge it in a register'
        intent: an unanswered question left in a register reads as decided to every later phase
      - id: BLOCKING_CLARIFICATION_OUTSTANDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/35
        check: ROW_ABSENT_WHEN
        register: clarification_requests
        params:
          column: Blocking
          value: 'YES'
          detail: a blocking clarification is unanswered — resolve it with the named owner and fold the
            answer into the document before any phase consumes it
        intent: a blocking question the next phase never sees is answered by invention
      - id: BUSINESS_CLARIFICATION_OUTSTANDING
        identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/36
        check: ROW_ABSENT_WHEN
        register: clarification_requests
        params:
          column: Owner
          value: HUMAN
          detail: only the business can answer this — ask it, fold the answer into the problem statement,
            and re-author the seed rather than carrying the question forward
        intent: a business question that outlives the seed is answered downstream by inference
  - owner: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
  - owner: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
  - owner: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      literal:
      - id: HEADER_FIELD_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/document/required
        check: HEADER_FIELD_PRESENT
        params:
          fields:
          - phase
          - domain
          - subdomain
          - cr
          - rule_set
        intent: a phase document states its phase, its domain and subdomain, its change, and the rule
          set it was authored under
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/document/properties/phase/const
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - phase
          pattern: ^p2$
        intent: a document's phase is the phase whose rules judge it
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/document/properties/domain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: domain
          type:
            type: string
            minLength: 1
        intent: a document's domain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/document/properties/subdomain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: subdomain
          type:
            type:
            - string
            - array
            items:
              type: string
            minLength: 1
            minItems: 1
        intent: a document's subdomain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/document/properties/cr
        check: HEADER_FIELD_OF_TYPE
        params:
          field: cr
          type:
            type: string
            minLength: 1
        intent: a document's cr takes its declared form
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/document/properties/rule_set/pattern
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - rule_set
          pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P2_V[0-9]+$
        intent: a document's rule_set names a rule set of its own phase
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entities/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: entities
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entities/items/required
        check: TABLE_HAS_COLUMNS
        register: entities
        params:
          columns:
          - Entity
          - Description
          - Store Model
          - Evidence Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entities/minItems
        check: TABLE_HAS_ROWS
        register: entities
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entities/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: entities
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entities/x-business-language
        check: CELL_TOKEN_ABSENT
        register: entities
        params:
          columns:
          - Entity
          - Description
          - Store Model
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entities/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: entities
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entities/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: entities
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entities/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: entities
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entity_attributes/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: entity_attributes
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entity_attributes/items/required
        check: TABLE_HAS_COLUMNS
        register: entity_attributes
        params:
          columns:
          - Entity
          - Attribute
          - Meaning
          - Evidence Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entity_attributes/minItems
        check: TABLE_HAS_ROWS
        register: entity_attributes
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entity_attributes/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: entity_attributes
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entity_attributes/x-business-language
        check: CELL_TOKEN_ABSENT
        register: entity_attributes
        params:
          columns:
          - Entity
          - Attribute
          - Meaning
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entity_attributes/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: entity_attributes
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entity_attributes/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: entity_attributes
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/entity_attributes/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: entity_attributes
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/business_processes/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: business_processes
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/business_processes/items/required
        check: TABLE_HAS_COLUMNS
        register: business_processes
        params:
          columns:
          - Process
          - Initiator
          - Outcome
          - Evidence Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/business_processes/minItems
        check: TABLE_HAS_ROWS
        register: business_processes
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/business_processes/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: business_processes
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/business_processes/x-business-language
        check: CELL_TOKEN_ABSENT
        register: business_processes
        params:
          columns:
          - Process
          - Initiator
          - Outcome
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/business_processes/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: business_processes
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/business_processes/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: business_processes
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/business_processes/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: business_processes
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/process_steps/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: process_steps
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/process_steps/items/required
        check: TABLE_HAS_COLUMNS
        register: process_steps
        params:
          columns:
          - Process
          - 'Step #'
          - Action
          - Record Produced
          - Evidence Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/process_steps/minItems
        check: TABLE_HAS_ROWS
        register: process_steps
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/process_steps/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: process_steps
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/process_steps/x-business-language
        check: CELL_TOKEN_ABSENT
        register: process_steps
        params:
          columns:
          - Process
          - 'Step #'
          - Action
          - Record Produced
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/process_steps/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: process_steps
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/process_steps/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: process_steps
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/process_steps/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: process_steps
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/belief_verification/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: belief_verification
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/belief_verification/items/required
        check: TABLE_HAS_COLUMNS
        register: belief_verification
        params:
          columns:
          - Belief
          - Result
          - Evidence
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/belief_verification/minItems
        check: TABLE_HAS_ROWS
        register: belief_verification
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/belief_verification/items/properties/result/x-vocab
        check: CELL_IN_VOCABULARY
        register: belief_verification
        params:
          column: Result
          vocabulary:
          - VERIFIED
          - NOT_FOUND
          - INSUFFICIENT_EVIDENCE
        intent: Result is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/belief_verification/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: belief_verification
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/belief_verification/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: belief_verification
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/belief_verification/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: belief_verification
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/belief_verification/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: belief_verification
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/pps_baseline_fqdns/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: pps_baseline_fqdns
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/pps_baseline_fqdns/items/required
        check: TABLE_HAS_COLUMNS
        register: pps_baseline_fqdns
        params:
          columns:
          - Capability
          - FQDN
          - What It Does
          - Fit
          - Cannot Do
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/pps_baseline_fqdns/minItems
        check: TABLE_HAS_ROWS
        register: pps_baseline_fqdns
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/pps_baseline_fqdns/items/properties/fit/x-vocab
        check: CELL_IN_VOCABULARY
        register: pps_baseline_fqdns
        params:
          column: Fit
          vocabulary:
          - EXACT
          - PARTIAL
          - MISMATCH
        intent: Fit is a controlled vocabulary declared by the template
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/gaps/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: gaps
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/gaps/items/required
        check: TABLE_HAS_COLUMNS
        register: gaps
        params:
          columns:
          - Gap
          - Severity
          - Impact
          - Evidence Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/gaps/minItems
        check: TABLE_HAS_ROWS
        register: gaps
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/gaps/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: gaps
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/gaps/x-business-language
        check: CELL_TOKEN_ABSENT
        register: gaps
        params:
          columns:
          - Gap
          - Severity
          - Impact
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/gaps/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: gaps
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/gaps/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: gaps
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/gaps/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: gaps
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/architectural_observations/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: architectural_observations
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/architectural_observations/items/required
        check: TABLE_HAS_COLUMNS
        register: architectural_observations
        params:
          columns:
          - Observation
          - Evidence
          - Evidence Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/architectural_observations/minItems
        check: TABLE_HAS_ROWS
        register: architectural_observations
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/architectural_observations/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: architectural_observations
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/architectural_observations/x-business-language
        check: CELL_TOKEN_ABSENT
        register: architectural_observations
        params:
          columns:
          - Observation
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/architectural_observations/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: architectural_observations
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/architectural_observations/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: architectural_observations
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/architectural_observations/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: architectural_observations
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/discovery_concerns/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: discovery_concerns
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/discovery_concerns/items/required
        check: TABLE_HAS_COLUMNS
        register: discovery_concerns
        params:
          columns:
          - Concern
          - Evidence
          - Severity
          - Evidence Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/discovery_concerns/minItems
        check: TABLE_HAS_ROWS
        register: discovery_concerns
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/discovery_concerns/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: discovery_concerns
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/discovery_concerns/x-business-language
        check: CELL_TOKEN_ABSENT
        register: discovery_concerns
        params:
          columns:
          - Concern
          - Severity
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/discovery_concerns/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: discovery_concerns
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/discovery_concerns/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: discovery_concerns
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/discovery_concerns/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: discovery_concerns
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/open_questions/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: open_questions
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/open_questions/items/required
        check: TABLE_HAS_COLUMNS
        register: open_questions
        params:
          columns:
          - Question
          - Category
          - Why It Matters
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/open_questions/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: open_questions
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/open_questions/x-business-language
        check: CELL_TOKEN_ABSENT
        register: open_questions
        params:
          columns:
          - Question
          - Category
          - Why It Matters
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/open_questions/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: open_questions
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/open_questions/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: open_questions
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/properties/registers/properties/open_questions/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: open_questions
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: BASELINE_IDENTITY_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/allOf/0
        check: CITED_ARTIFACTS_RESOLVE
        register: pps_baseline_fqdns
        params:
          column: FQDN
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
          detail_missing: baseline row names no artifact identity
        intent: the baseline register records what already exists, so every row must be observable
      - id: VERIFIED_BELIEF_IDENTITY_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/allOf/1
        check: CITED_ARTIFACTS_RESOLVE
        register: belief_verification
        params:
          column: Evidence
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
          only_when_column: Result
          only_when_value: VERIFIED
        intent: a belief grounded on an identity must be grounded on one that is really there
      - id: BELIEF_WITHOUT_EVIDENCE
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/allOf/2
        check: CELL_NOT_EMPTY
        register: belief_verification
        params:
          column: Evidence
          detail: belief has a result but records nothing about how it was reached
        intent: a result without evidence is an assertion, not a verification
      - id: BELIEF_NOT_CARRIED_FROM_P1
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/allOf/3
        check: PRIOR_ROWS_CITED
        register: belief_verification
        params:
          prior_phase: p1
          prior_register: system_beliefs
          prior_key_column: Belief
          citation_column: Source Finding
        intent: a belief nobody carried forward is forgotten, not resolved
      - id: BELIEF_RESTATED_FROM_P1
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/allOf/4
        check: PRIOR_ROW_MATCHES_CITED
        register: belief_verification
        params:
          prior_phase: p1
          prior_register: system_beliefs
          prior_key_column: Belief
          key_column: Belief
          citation_column: Source Finding
        intent: a verification must resolve the belief it cites, not a substitute for it
      - id: REGISTER_CELL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P2_V0#/allOf/5
        check: UNRESOLVED_MARKER_ABSENT
        params:
          exempt:
          - gaps
          - open_questions
          - discovery_concerns
          detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask
            it as a clarification, do not hedge it in a register'
        intent: an unanswered question left in a register reads as decided to every later phase
  - owner: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
  - owner: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
  - owner: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_COMPOSITION_V1
    direction: INPUT
    field: rule_set
    bound_to:
      literal:
      - id: HEADER_FIELD_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/document/required
        check: HEADER_FIELD_PRESENT
        params:
          fields:
          - phase
          - domain
          - subdomain
          - cr
          - rule_set
        intent: a phase document states its phase, its domain and subdomain, its change, and the rule
          set it was authored under
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/document/properties/phase/const
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - phase
          pattern: ^p3$
        intent: a document's phase is the phase whose rules judge it
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/document/properties/domain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: domain
          type:
            type: string
            minLength: 1
        intent: a document's domain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/document/properties/subdomain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: subdomain
          type:
            type:
            - string
            - array
            items:
              type: string
            minLength: 1
            minItems: 1
        intent: a document's subdomain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/document/properties/cr
        check: HEADER_FIELD_OF_TYPE
        params:
          field: cr
          type:
            type: string
            minLength: 1
        intent: a document's cr takes its declared form
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/document/properties/rule_set/pattern
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - rule_set
          pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P3_V[0-9]+$
        intent: a document's rule_set names a rule set of its own phase
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/analysis_findings/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: analysis_findings
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/analysis_findings/items/required
        check: TABLE_HAS_COLUMNS
        register: analysis_findings
        params:
          columns:
          - Question Id
          - Finding
          - Impact
          - Evidence Status
          - Confidence
          - Resolution Status
          - Evidence
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/analysis_findings/minItems
        check: TABLE_HAS_ROWS
        register: analysis_findings
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/analysis_findings/items/properties/evidence_status/x-vocab
        check: CELL_IN_VOCABULARY
        register: analysis_findings
        params:
          column: Evidence Status
          vocabulary:
          - OBSERVED
          - INFERRED
          - OPEN
        intent: Evidence Status is a controlled vocabulary declared by the template
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/analysis_findings/items/properties/confidence/x-vocab
        check: CELL_IN_VOCABULARY
        register: analysis_findings
        params:
          column: Confidence
          vocabulary:
          - HIGH
          - MEDIUM
          - LOW
        intent: Confidence is a controlled vocabulary declared by the template
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/analysis_findings/items/properties/resolution_status/x-vocab
        check: CELL_IN_VOCABULARY
        register: analysis_findings
        params:
          column: Resolution Status
          vocabulary:
          - CLOSED
          - OPEN
        intent: Resolution Status is a controlled vocabulary declared by the template
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/verification_results/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: verification_results
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/verification_results/items/required
        check: TABLE_HAS_COLUMNS
        register: verification_results
        params:
          columns:
          - Item
          - Origin
          - Result
          - Evidence
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/verification_results/minItems
        check: TABLE_HAS_ROWS
        register: verification_results
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/verification_results/items/properties/result/x-vocab
        check: CELL_IN_VOCABULARY
        register: verification_results
        params:
          column: Result
          vocabulary:
          - CONFIRMED
          - OVERTURNED
        intent: Result is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/verification_results/items/properties/origin/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: verification_results
        params:
          column: Origin
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Origin carries structure, and its value must take the declared form
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/dependency_discoveries/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: dependency_discoveries
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/dependency_discoveries/items/required
        check: TABLE_HAS_COLUMNS
        register: dependency_discoveries
        params:
          columns:
          - Dependency
          - Type
          - Disposition
          - Evidence
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/dependency_discoveries/minItems
        check: TABLE_HAS_ROWS
        register: dependency_discoveries
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/dependency_discoveries/items/properties/disposition/x-vocab
        check: CELL_IN_VOCABULARY
        register: dependency_discoveries
        params:
          column: Disposition
          vocabulary:
          - EXISTING
          - EXTEND
          - REUSE
          - AUTHOR_NEW
          - INVESTIGATE
        intent: Disposition is a controlled vocabulary declared by the template
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/impact_analysis/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: impact_analysis
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/impact_analysis/items/required
        check: TABLE_HAS_COLUMNS
        register: impact_analysis
        params:
          columns:
          - Artifact
          - Impact Scope
          - Consumer Count
          - Evidence
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/impact_analysis/minItems
        check: TABLE_HAS_ROWS
        register: impact_analysis
        intent: an empty required register asserts nothing
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/authoring_decisions/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: authoring_decisions
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/authoring_decisions/items/required
        check: TABLE_HAS_COLUMNS
        register: authoring_decisions
        params:
          columns:
          - Capability
          - Decision
          - Rationale
          - Alternatives Checked
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/authoring_decisions/minItems
        check: TABLE_HAS_ROWS
        register: authoring_decisions
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/authoring_decisions/items/properties/decision/x-vocab
        check: CELL_IN_VOCABULARY
        register: authoring_decisions
        params:
          column: Decision
          vocabulary:
          - REUSE
          - EXTEND
          - AUTHOR_NEW
        intent: Decision is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/authoring_decisions/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: authoring_decisions
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/authoring_decisions/x-business-language
        check: CELL_TOKEN_ABSENT
        register: authoring_decisions
        params:
          columns:
          - Capability
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/authoring_decisions/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: authoring_decisions
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/authoring_decisions/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: authoring_decisions
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/authoring_decisions/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: authoring_decisions
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/placement_decision/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: placement_decision
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/placement_decision/items/required
        check: TABLE_HAS_COLUMNS
        register: placement_decision
        params:
          columns:
          - Decision
          - Subdomain
          - Rationale
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/placement_decision/minItems
        check: TABLE_HAS_ROWS
        register: placement_decision
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/placement_decision/items/properties/decision/x-vocab
        check: CELL_IN_VOCABULARY
        register: placement_decision
        params:
          column: Decision
          vocabulary:
          - NEW_SUBDOMAIN
          - EXTEND
        intent: Decision is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/placement_decision/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: placement_decision
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/placement_decision/x-business-language
        check: CELL_TOKEN_ABSENT
        register: placement_decision
        params:
          columns:
          - Subdomain
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/placement_decision/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: placement_decision
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/placement_decision/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: placement_decision
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/placement_decision/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: placement_decision
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/saturation/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: saturation
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/saturation/items/required
        check: TABLE_HAS_COLUMNS
        register: saturation
        params:
          columns:
          - Criterion
          - Status
          - Evidence
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/saturation/minItems
        check: TABLE_HAS_ROWS
        register: saturation
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/saturation/items/properties/status/x-vocab
        check: CELL_IN_VOCABULARY
        register: saturation
        params:
          column: Status
          vocabulary:
          - SATISFIED
          - NOT_SATISFIED
        intent: Status is a controlled vocabulary declared by the template
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/properties/registers/properties/saturation/x-business-language
        check: CELL_TOKEN_ABSENT
        register: saturation
        params:
          columns:
          - Criterion
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REUSE_CANDIDATE_NOT_ELIGIBLE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/0
        check: REUSE_CANDIDATE_ELIGIBLE
        register: authoring_decisions
        params:
          column: Alternatives Checked
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.snapshot.summary
          artifact_observation: si.artifact.list
          eligible:
          - substrate
          - business
        intent: a change request may only be offered candidates from a domain that permits reuse
      - id: DECISION_WITHOUT_ALTERNATIVES
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/1
        check: CELL_NOT_EMPTY
        register: authoring_decisions
        params:
          column: Alternatives Checked
          detail: decision records no alternatives examined — 'I searched and found nothing' is credible
            only with the search shown
        intent: a committed decision shows the search that produced it
      - id: DECISION_WITHOUT_RATIONALE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/2
        check: CELL_NOT_EMPTY
        register: authoring_decisions
        params:
          column: Rationale
          detail: decision states no rationale — a classification without a reason is an assertion
        intent: every decision traces to a grounded reason
      - id: CITED_ALTERNATIVE_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/3
        check: CITED_ARTIFACTS_RESOLVE
        register: authoring_decisions
        params:
          column: Alternatives Checked
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
        intent: an alternative examined must be one that really exists
      - id: IMPACT_WITHOUT_EVIDENCE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/4
        check: CELL_NOT_EMPTY
        register: impact_analysis
        params:
          column: Evidence
          detail: impact row carries no evidence — consumer counts are observed, never estimated
        intent: impact is mechanically captured, never summarised from memory
      - id: VERIFICATION_WITHOUT_EVIDENCE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/5
        check: CELL_NOT_EMPTY
        register: verification_results
        params:
          column: Evidence
          detail: verification records no evidence — grounding is not inherited, so a re-check that cites
            nothing did not happen
        intent: an overturned answer is marked with what overturned it, never erased
      - id: SATURATION_CRITERIA_INCOMPLETE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/6
        check: TABLE_HAS_ROWS
        register: saturation
        params:
          minimum: 5
        intent: analysis is saturated only against every declared criterion; a claim resting on fewer
          is the gap the criteria exist to close
      - id: SATURATION_CLAIMED_WITHOUT_EVIDENCE
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/7
        check: CELL_NOT_EMPTY
        register: saturation
        params:
          column: Evidence
          detail: criterion is asserted satisfied with nothing to show for it
        intent: saturation is demonstrated, not declared
      - id: BELIEF_RESULT_NOT_REVERIFIED
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/8
        check: PRIOR_ROWS_CITED
        register: verification_results
        params:
          prior_phase: p2
          prior_register: belief_verification
          prior_key_column: Belief
          citation_column: Origin
        intent: a result nobody re-verified was inherited, and grounding is not inherited
      - id: BELIEF_RESULT_RESTATED_FROM_P2
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/9
        check: PRIOR_ROW_MATCHES_CITED
        register: verification_results
        params:
          prior_phase: p2
          prior_register: belief_verification
          prior_key_column: Belief
          key_column: Item
          citation_column: Origin
        intent: a re-verification must address the result it cites, not a substitute for it
      - id: REGISTER_CELL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/10
        check: UNRESOLVED_MARKER_ABSENT
        params:
          exempt: []
          detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask
            it as a clarification, do not hedge it in a register'
        intent: an unanswered question left in a register reads as decided to every later phase
  - owner: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
  - owner: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
  - owner: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      literal:
      - id: HEADER_FIELD_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/document/required
        check: HEADER_FIELD_PRESENT
        params:
          fields:
          - phase
          - domain
          - subdomain
          - cr
          - rule_set
        intent: a phase document states its phase, its domain and subdomain, its change, and the rule
          set it was authored under
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/document/properties/phase/const
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - phase
          pattern: ^p4$
        intent: a document's phase is the phase whose rules judge it
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/document/properties/domain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: domain
          type:
            type: string
            minLength: 1
        intent: a document's domain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/document/properties/subdomain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: subdomain
          type:
            type:
            - string
            - array
            items:
              type: string
            minLength: 1
            minItems: 1
        intent: a document's subdomain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/document/properties/cr
        check: HEADER_FIELD_OF_TYPE
        params:
          field: cr
          type:
            type: string
            minLength: 1
        intent: a document's cr takes its declared form
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/document/properties/rule_set/pattern
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - rule_set
          pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P4_V[0-9]+$
        intent: a document's rule_set names a rule set of its own phase
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/actors/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: actors
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/actors/items/required
        check: TABLE_HAS_COLUMNS
        register: actors
        params:
          columns:
          - Actor
          - Role
          - Authority Class
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/actors/minItems
        check: TABLE_HAS_ROWS
        register: actors
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/actors/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: actors
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/actors/x-business-language
        check: CELL_TOKEN_ABSENT
        register: actors
        params:
          columns:
          - Actor
          - Role
          - Authority Class
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/actors/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: actors
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/actors/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: actors
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/actors/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: actors
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/bm_entities/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: bm_entities
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/bm_entities/items/required
        check: TABLE_HAS_COLUMNS
        register: bm_entities
        params:
          columns:
          - Entity
          - Description
          - Store Model
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/bm_entities/minItems
        check: TABLE_HAS_ROWS
        register: bm_entities
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/bm_entities/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: bm_entities
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/bm_entities/x-business-language
        check: CELL_TOKEN_ABSENT
        register: bm_entities
        params:
          columns:
          - Entity
          - Description
          - Store Model
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/bm_entities/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: bm_entities
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/bm_entities/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: bm_entities
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/bm_entities/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: bm_entities
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/resources/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: resources
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/resources/items/required
        check: TABLE_HAS_COLUMNS
        register: resources
        params:
          columns:
          - Resource
          - Description
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/resources/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: resources
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/resources/x-business-language
        check: CELL_TOKEN_ABSENT
        register: resources
        params:
          columns:
          - Resource
          - Description
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/resources/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: resources
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/resources/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: resources
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/resources/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: resources
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/events/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: events
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/events/items/required
        check: TABLE_HAS_COLUMNS
        register: events
        params:
          columns:
          - Event
          - Trigger
          - Lifecycle Meaning
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/events/minItems
        check: TABLE_HAS_ROWS
        register: events
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/events/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: events
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/events/x-business-language
        check: CELL_TOKEN_ABSENT
        register: events
        params:
          columns:
          - Event
          - Trigger
          - Lifecycle Meaning
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/events/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: events
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/events/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: events
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/events/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: events
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/relationships/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: relationships
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/relationships/items/required
        check: TABLE_HAS_COLUMNS
        register: relationships
        params:
          columns:
          - Subject
          - Verb
          - Object
          - Capability Need
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/relationships/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: relationships
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/relationships/x-business-language
        check: CELL_TOKEN_ABSENT
        register: relationships
        params:
          columns:
          - Subject
          - Verb
          - Object
          - Capability Need
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/relationships/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: relationships
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/relationships/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: relationships
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/relationships/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: relationships
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/capability_graph/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: capability_graph
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/capability_graph/items/required
        check: TABLE_HAS_COLUMNS
        register: capability_graph
        params:
          columns:
          - Capability
          - Source Finding
          - Status
          - Gap Register Entry
          - Notes
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/capability_graph/minItems
        check: TABLE_HAS_ROWS
        register: capability_graph
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/capability_graph/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: capability_graph
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/capability_graph/x-business-language
        check: CELL_TOKEN_ABSENT
        register: capability_graph
        params:
          columns:
          - Capability
          - Status
          - Gap Register Entry
          - Notes
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/capability_graph/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: capability_graph
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/capability_graph/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: capability_graph
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/capability_graph/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: capability_graph
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/dependency_graph/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: dependency_graph
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/dependency_graph/items/required
        check: TABLE_HAS_COLUMNS
        register: dependency_graph
        params:
          columns:
          - From
          - To
          - Dependency Type
          - PPS Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/dependency_graph/minItems
        check: TABLE_HAS_ROWS
        register: dependency_graph
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/dependency_graph/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: dependency_graph
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/dependency_graph/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: dependency_graph
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/dependency_graph/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: dependency_graph
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/dependency_graph/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: dependency_graph
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/constraint_register/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: constraint_register
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/constraint_register/items/required
        check: TABLE_HAS_COLUMNS
        register: constraint_register
        params:
          columns:
          - '#'
          - Constraint
          - Source Finding
          - Source
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/constraint_register/minItems
        check: TABLE_HAS_ROWS
        register: constraint_register
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/constraint_register/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: constraint_register
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/constraint_register/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: constraint_register
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/constraint_register/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: constraint_register
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/constraint_register/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: constraint_register
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/gap_register/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: gap_register
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/gap_register/items/required
        check: TABLE_HAS_COLUMNS
        register: gap_register
        params:
          columns:
          - Gap Code
          - Source Finding
          - Capability
          - Owner Subdomain
          - Resolution
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/gap_register/minItems
        check: TABLE_HAS_ROWS
        register: gap_register
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/gap_register/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: gap_register
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/gap_register/x-business-language
        check: CELL_TOKEN_ABSENT
        register: gap_register
        params:
          columns:
          - Gap Code
          - Capability
          - Owner Subdomain
          - Resolution
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/gap_register/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: gap_register
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/gap_register/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: gap_register
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/gap_register/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: gap_register
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/design_decisions/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: design_decisions
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/design_decisions/items/required
        check: TABLE_HAS_COLUMNS
        register: design_decisions
        params:
          columns:
          - '#'
          - Decision
          - Source Finding
          - Rationale
          - Constraints Imposed
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/design_decisions/minItems
        check: TABLE_HAS_ROWS
        register: design_decisions
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/design_decisions/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: design_decisions
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/design_decisions/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: design_decisions
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/design_decisions/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: design_decisions
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/design_decisions/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: design_decisions
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/authoring_scope/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: authoring_scope
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/authoring_scope/items/required
        check: TABLE_HAS_COLUMNS
        register: authoring_scope
        params:
          columns:
          - Capability
          - Gap Register Ref
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/properties/registers/properties/authoring_scope/minItems
        check: TABLE_HAS_ROWS
        register: authoring_scope
        intent: an empty required register asserts nothing
      - id: CRITICAL_WITHOUT_GAP_ENTRY
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/allOf/0
        check: CELL_NOT_EMPTY
        register: capability_graph
        params:
          column: Gap Register Entry
          only_when_column: Status
          only_when_value: CRITICAL
          detail: capability is CRITICAL but names no gap — work this change request must do has nowhere
            to be tracked
        intent: every capability that must be authored is a declared gap
      - id: GAP_ENTRY_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/allOf/1
        check: CELL_RESOLVES_IN_REGISTER
        register: capability_graph
        params:
          column: Gap Register Entry
          target_register: gap_register
          target_column: Gap Code
          only_when_column: Status
          only_when_value: CRITICAL
          detail: a consolidation may only point at what it consolidated
        intent: a capability points only at a gap the document itself declares
      - id: GAP_WITHOUT_OWNER
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/allOf/2
        check: CELL_NOT_EMPTY
        register: gap_register
        params:
          column: Owner Subdomain
          detail: gap names no owning subdomain — an unowned gap is nobody's work
        intent: every gap has a subdomain accountable for closing it
      - id: SCOPE_WITHOUT_GAP_REFERENCE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/allOf/3
        check: CELL_NOT_EMPTY
        register: authoring_scope
        params:
          column: Gap Register Ref
          detail: in-scope capability references no gap — scope must trace to evidence
        intent: what this change request builds traces to a declared gap, not to intent
      - id: SCOPE_GAP_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/allOf/4
        check: CELL_RESOLVES_IN_REGISTER
        register: authoring_scope
        params:
          column: Gap Register Ref
          target_register: gap_register
          target_column: Gap Code
          detail: a consolidation may only point at what it consolidated
        intent: scope points only at a gap the document itself declares
      - id: DEPENDENCY_IDENTITY_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/allOf/5
        check: CITED_ARTIFACTS_RESOLVE
        register: dependency_graph
        params:
          column: To
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
        intent: a dependency on an existing artifact must be one that really exists
      - id: DECISION_WITHOUT_RATIONALE
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/allOf/6
        check: CELL_NOT_EMPTY
        register: design_decisions
        params:
          column: Rationale
          detail: design decision states no rationale — a decision without a reason cannot be reviewed
        intent: a consolidated decision carries the reasoning that produced it
      - id: AUTHORING_DECISION_NOT_CONSOLIDATED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/allOf/7
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: capability_graph
        params:
          prior_phase: p3
          prior_register: authoring_decisions
          prior_key_column: Capability
          key_column: Capability
        intent: a capability P3 decided and P4 never consolidated is dropped, not deferred
      - id: REGISTER_CELL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P4_V0#/allOf/8
        check: UNRESOLVED_MARKER_ABSENT
        params:
          exempt:
          - gap_register
          detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask
            it as a clarification, do not hedge it in a register'
        intent: an unanswered question left in a register reads as decided to every later phase
  - owner: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
  - owner: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
  - owner: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      literal:
      - id: HEADER_FIELD_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/document/required
        check: HEADER_FIELD_PRESENT
        params:
          fields:
          - phase
          - domain
          - subdomain
          - cr
          - rule_set
        intent: a phase document states its phase, its domain and subdomain, its change, and the rule
          set it was authored under
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/document/properties/phase/const
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - phase
          pattern: ^p5$
        intent: a document's phase is the phase whose rules judge it
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/document/properties/domain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: domain
          type:
            type: string
            minLength: 1
        intent: a document's domain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/document/properties/subdomain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: subdomain
          type:
            type:
            - string
            - array
            items:
              type: string
            minLength: 1
            minItems: 1
        intent: a document's subdomain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/document/properties/cr
        check: HEADER_FIELD_OF_TYPE
        params:
          field: cr
          type:
            type: string
            minLength: 1
        intent: a document's cr takes its declared form
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/document/properties/rule_set/pattern
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - rule_set
          pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P5_V[0-9]+$
        intent: a document's rule_set names a rule set of its own phase
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/subdomain_purpose/minLength
        check: SECTION_HAS_TEXT
        register: subdomain_purpose
        params:
          detail: narrative register is empty — it states nothing
        intent: a narrative register carries the context nothing downstream can rederive
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/purpose_provenance/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: purpose_provenance
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/purpose_provenance/items/required
        check: TABLE_HAS_COLUMNS
        register: purpose_provenance
        params:
          columns:
          - Source
          - Disposition
          - Refinement
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/purpose_provenance/minItems
        check: TABLE_HAS_ROWS
        register: purpose_provenance
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/purpose_provenance/items/properties/disposition/x-vocab
        check: CELL_IN_VOCABULARY
        register: purpose_provenance
        params:
          column: Disposition
          vocabulary:
          - INHERITED
          - REFINED
        intent: Disposition is a controlled vocabulary declared by the template
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/purpose_provenance/x-business-language
        check: CELL_TOKEN_ABSENT
        register: purpose_provenance
        params:
          columns:
          - Refinement
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/subdomain_purposes/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: subdomain_purposes
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/subdomain_purposes/items/required
        check: TABLE_HAS_COLUMNS
        register: subdomain_purposes
        params:
          columns:
          - Subdomain
          - Purpose
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/subdomain_purposes/minItems
        check: TABLE_HAS_ROWS
        register: subdomain_purposes
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/subdomain_purposes/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: subdomain_purposes
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/subdomain_purposes/x-business-language
        check: CELL_TOKEN_ABSENT
        register: subdomain_purposes
        params:
          columns:
          - Purpose
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/subdomain_purposes/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: subdomain_purposes
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/subdomain_purposes/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: subdomain_purposes
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/subdomain_purposes/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: subdomain_purposes
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/scope_boundary/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: scope_boundary
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/scope_boundary/items/required
        check: TABLE_HAS_COLUMNS
        register: scope_boundary
        params:
          columns:
          - Capability
          - Status
          - Notes
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/scope_boundary/minItems
        check: TABLE_HAS_ROWS
        register: scope_boundary
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/scope_boundary/items/properties/status/x-vocab
        check: CELL_IN_VOCABULARY
        register: scope_boundary
        params:
          column: Status
          vocabulary:
          - IN_SCOPE
          - DEFERRED
        intent: Status is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/scope_boundary/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: scope_boundary
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/scope_boundary/x-business-language
        check: CELL_TOKEN_ABSENT
        register: scope_boundary
        params:
          columns:
          - Capability
          - Notes
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/scope_boundary/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: scope_boundary
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/scope_boundary/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: scope_boundary
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/scope_boundary/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: scope_boundary
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/business_objects/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: business_objects
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/business_objects/items/required
        check: TABLE_HAS_COLUMNS
        register: business_objects
        params:
          columns:
          - Store Name
          - Record Model
          - Business Rationale
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/business_objects/items/properties/record_model/x-vocab
        check: CELL_IN_VOCABULARY
        register: business_objects
        params:
          column: Record Model
          vocabulary:
          - MUTABLE_STATE
          - APPEND_ONLY_JOURNAL
          - IDENTITY_REGISTRY
          - HYBRID
        intent: Record Model is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/business_objects/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: business_objects
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/business_objects/x-business-language
        check: CELL_TOKEN_ABSENT
        register: business_objects
        params:
          columns:
          - Store Name
          - Business Rationale
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/business_objects/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: business_objects
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/business_objects/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: business_objects
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/business_objects/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: business_objects
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/identity_semantics/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: identity_semantics
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/identity_semantics/items/required
        check: TABLE_HAS_COLUMNS
        register: identity_semantics
        params:
          columns:
          - Store Name
          - Identity Field
          - Source
          - Uniqueness Rule
          - Cross-Subdomain Relationship
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/identity_semantics/minItems
        check: TABLE_HAS_ROWS
        register: identity_semantics
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/identity_semantics/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: identity_semantics
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/identity_semantics/x-business-language
        check: CELL_TOKEN_ABSENT
        register: identity_semantics
        params:
          columns:
          - Identity Field
          - Source
          - Uniqueness Rule
          - Cross-Subdomain Relationship
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/identity_semantics/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: identity_semantics
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/identity_semantics/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: identity_semantics
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/identity_semantics/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: identity_semantics
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/invariants/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: invariants
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/invariants/items/required
        check: TABLE_HAS_COLUMNS
        register: invariants
        params:
          columns:
          - Invariant
          - Business Reason
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/invariants/minItems
        check: TABLE_HAS_ROWS
        register: invariants
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/invariants/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: invariants
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/invariants/x-business-language
        check: CELL_TOKEN_ABSENT
        register: invariants
        params:
          columns:
          - Invariant
          - Business Reason
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/invariants/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: invariants
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/invariants/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: invariants
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/invariants/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: invariants
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/actions/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: actions
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/actions/items/required
        check: TABLE_HAS_COLUMNS
        register: actions
        params:
          columns:
          - Action
          - Object
          - Trigger
          - Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/actions/minItems
        check: TABLE_HAS_ROWS
        register: actions
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/actions/items/properties/status/x-vocab
        check: CELL_IN_VOCABULARY
        register: actions
        params:
          column: Status
          vocabulary:
          - IN_SCOPE
          - DEFERRED
        intent: Status is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/actions/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: actions
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/actions/x-business-language
        check: CELL_TOKEN_ABSENT
        register: actions
        params:
          columns:
          - Object
          - Trigger
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/actions/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: actions
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/actions/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: actions
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/actions/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: actions
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/provisional_codes/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: provisional_codes
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/provisional_codes/items/required
        check: TABLE_HAS_COLUMNS
        register: provisional_codes
        params:
          columns:
          - Subdomain
          - Provisional Code
          - Family
          - Summary
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/provisional_codes/items/properties/family/x-vocab
        check: CELL_IN_VOCABULARY
        register: provisional_codes
        params:
          column: Family
          vocabulary:
          - AC
          - IN
          - WF
          - CC
          - CT
          - EV
          - RB
          - VOCAB
          - STRUCTURE
          - TI
          - TE
        intent: Family is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/provisional_codes/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: provisional_codes
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/provisional_codes/x-business-language
        check: CELL_TOKEN_ABSENT
        register: provisional_codes
        params:
          columns:
          - Summary
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/provisional_codes/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: provisional_codes
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/provisional_codes/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: provisional_codes
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/provisional_codes/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: provisional_codes
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/cross_subdomain_refs/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: cross_subdomain_refs
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/cross_subdomain_refs/items/required
        check: TABLE_HAS_COLUMNS
        register: cross_subdomain_refs
        params:
          columns:
          - CC Code
          - Defined In
          - Role
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/cross_subdomain_refs/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: cross_subdomain_refs
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/cross_subdomain_refs/x-business-language
        check: CELL_TOKEN_ABSENT
        register: cross_subdomain_refs
        params:
          columns:
          - Role
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/cross_subdomain_refs/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: cross_subdomain_refs
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/cross_subdomain_refs/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: cross_subdomain_refs
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/properties/registers/properties/cross_subdomain_refs/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: cross_subdomain_refs
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: PURPOSE_PROVENANCE_NOT_SINGULAR
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/0
        check: TABLE_ROW_COUNT
        register: purpose_provenance
        params:
          maximum: 1
          detail: the register answers one question — whether this phase inherited the seed's purpose
            or refined it — and two rows are two answers to it
        intent: a register owing one answer may not carry several
      - id: PURPOSE_NOT_CARRIED_FROM_SEED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/1
        check: PRIOR_PROSE_CARRIED
        register: purpose_provenance
        params:
          prior_phase: p0
          prior_register: subdomain_purpose
          prose_register: subdomain_purpose
          column: Disposition
          inherited_value: INHERITED
          detail: the purpose is declared INHERITED and does not match the seed's — inherit it word for
            word, or declare REFINED and say what this phase adds
        intent: the one narrative no artifact can derive is authored once and never quietly replaced
      - id: REFINEMENT_NOT_STATED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/2
        check: CELL_NOT_EMPTY
        register: purpose_provenance
        params:
          column: Refinement
          only_when_column: Disposition
          only_when_value: REFINED
          detail: a refined purpose must state what it adds that the seed did not say; silence here is
            the silent replacement this register exists to prevent
        intent: superseding upstream content is allowed, doing it without saying so is not
      - id: TOUCHED_SUBDOMAIN_WITHOUT_PURPOSE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/3
        check: PRIOR_IDENTITIES_COVERED
        register: subdomain_purposes
        params:
          prior_phase: p0
          prior_register: cr_type
          prior_column: Subdomain
          column: Subdomain
          require: prior_in_here
        intent: every subdomain a change touches has its purpose stated
      - id: TOUCHED_SUBDOMAIN_AUTHORS_NOTHING
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/4
        check: PRIOR_IDENTITIES_COVERED
        register: provisional_codes
        params:
          prior_phase: p0
          prior_register: cr_type
          prior_column: Subdomain
          column: Subdomain
          require: prior_in_here
          prior_only_when_column: Classification
          prior_only_when_values:
          - NEW_SUBDOMAIN
          - EXTEND_SUBDOMAIN
        intent: a subdomain a change authors into names the artifacts it authors
      - id: PROVISIONAL_CODE_ALREADY_BOUND
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/5
        check: CELL_TOKEN_ABSENT
        register: provisional_codes
        params:
          columns:
          - Provisional Code
          pattern: '::'
          detail: '{token!r} in {column!r} — a provisional code carrying a namespace has already been
            placed, and placement is Stage 7''s decision'
        intent: a provisional code names what to build, never where it will live
      - id: PROVISIONAL_CODE_MALFORMED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/6
        check: CELL_MATCHES
        register: provisional_codes
        params:
          column: Provisional Code
          pattern: ^(?:AC|IN|WF|CC|CT|EV|RB|VOCAB|STRUCTURE|TI|TE)_[A-Z0-9_]+_V\d+$
          detail: provisional code must be FAMILY_NAME_V<n> with no namespace
        intent: a provisional code is readable as a family, a name and a version
      - id: PROVISIONAL_FAMILY_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/7
        check: CELL_PREFIXED_BY_COLUMN
        register: provisional_codes
        params:
          column: Provisional Code
          prefix_column: Family
        intent: a code and the family it is filed under agree
      - id: CROSS_SUBDOMAIN_REF_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/8
        check: CITED_ARTIFACTS_RESOLVE
        register: cross_subdomain_refs
        params:
          column: CC Code
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
        intent: a capability borrowed from elsewhere must be one that really exists
      - id: BINDING_LEAKED_INTO_INTENT
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/9
        check: CELL_TOKEN_ABSENT
        register: business_objects
        params:
          columns:
          - Store Name
          - Record Model
          - Business Rationale
          pattern: \$\.[A-Za-z_]|/[a-z_]+/|\b[0-9a-f]{16,}\b
          detail: '{token!r} in {column!r} — a path, a binding expression or a hash is an implementation
            decision, and Stage 7 owns those'
        intent: intent says what must be true, never how it is wired
      - id: INVARIANT_WITHOUT_BUSINESS_REASON
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/10
        check: CELL_NOT_EMPTY
        register: invariants
        params:
          column: Business Reason
          detail: invariant states no business reason — a rule without one is a technical constraint and
            belongs elsewhere
        intent: every invariant is answerable to the business, not to the design
      - id: IDENTITY_WITHOUT_UNIQUENESS_RULE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/11
        check: CELL_NOT_EMPTY
        register: identity_semantics
        params:
          column: Uniqueness Rule
          detail: identity declares no uniqueness rule — what a duplicate means is irreducible business
            knowledge the compiler cannot infer
        intent: identity semantics are stated, never inferred from field names
      - id: EVENT_CODE_NOT_PAST_PARTICIPLE
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/12
        check: CELL_MATCHES
        register: provisional_codes
        params:
          column: Provisional Code
          pattern: ^(?:[a-z][a-z0-9_.]*::)?EV_[A-Z0-9_]+ED_V\d+$
          only_when_column: Family
          only_when_value: EV
          detail: '{value!r} does not name a moment that has happened — an event code reads EV_<subject>_<participle>,
            as EV_ACTOR_REGISTERED_V0 does'
        intent: an event names an occurrence, and a code in the imperative names an operation
      - id: REGISTER_CELL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/13
        check: UNRESOLVED_MARKER_ABSENT
        params:
          exempt: []
          detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask
            it as a clarification, do not hedge it in a register'
        intent: an unanswered question left in a register reads as decided to every later phase
  - owner: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
  - owner: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
  - owner: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      literal:
      - id: HEADER_FIELD_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/document/required
        check: HEADER_FIELD_PRESENT
        params:
          fields:
          - phase
          - domain
          - subdomain
          - cr
          - rule_set
        intent: a phase document states its phase, its domain and subdomain, its change, and the rule
          set it was authored under
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/document/properties/phase/const
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - phase
          pattern: ^p6$
        intent: a document's phase is the phase whose rules judge it
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/document/properties/domain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: domain
          type:
            type: string
            minLength: 1
        intent: a document's domain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/document/properties/subdomain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: subdomain
          type:
            type:
            - string
            - array
            items:
              type: string
            minLength: 1
            minItems: 1
        intent: a document's subdomain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/document/properties/cr
        check: HEADER_FIELD_OF_TYPE
        params:
          field: cr
          type:
            type: string
            minLength: 1
        intent: a document's cr takes its declared form
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/document/properties/rule_set/pattern
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - rule_set
          pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P6_V[0-9]+$
        intent: a document's rule_set names a rule set of its own phase
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/ownership/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: ownership
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/ownership/items/required
        check: TABLE_HAS_COLUMNS
        register: ownership
        params:
          columns:
          - Capability
          - Owner Subdomain
          - Disposition
          - Existing Artifact
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/ownership/minItems
        check: TABLE_HAS_ROWS
        register: ownership
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/ownership/items/properties/disposition/x-vocab
        check: CELL_IN_VOCABULARY
        register: ownership
        params:
          column: Disposition
          vocabulary:
          - OWNED
          - SATISFIED
          - DEFERRED
        intent: Disposition is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/ownership/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: ownership
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/ownership/x-business-language
        check: CELL_TOKEN_ABSENT
        register: ownership
        params:
          columns:
          - Capability
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/ownership/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: ownership
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/ownership/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: ownership
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/ownership/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: ownership
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/storage_governance/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: storage_governance
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/storage_governance/items/required
        check: TABLE_HAS_COLUMNS
        register: storage_governance
        params:
          columns:
          - Storage Need
          - Purpose
          - Subdomain
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/storage_governance/minItems
        check: TABLE_HAS_ROWS
        register: storage_governance
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/storage_governance/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: storage_governance
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/storage_governance/x-business-language
        check: CELL_TOKEN_ABSENT
        register: storage_governance
        params:
          columns:
          - Storage Need
          - Purpose
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/storage_governance/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: storage_governance
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/storage_governance/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: storage_governance
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/storage_governance/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: storage_governance
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/cross_subdomain_deps/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: cross_subdomain_deps
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/cross_subdomain_deps/items/required
        check: TABLE_HAS_COLUMNS
        register: cross_subdomain_deps
        params:
          columns:
          - Dependency
          - Direction
          - Existing Artifact
          - Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/cross_subdomain_deps/items/properties/status/x-vocab
        check: CELL_IN_VOCABULARY
        register: cross_subdomain_deps
        params:
          column: Status
          vocabulary:
          - SATISFIED
          - GAP
        intent: Status is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/cross_subdomain_deps/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: cross_subdomain_deps
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/cross_subdomain_deps/x-business-language
        check: CELL_TOKEN_ABSENT
        register: cross_subdomain_deps
        params:
          columns:
          - Dependency
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/cross_subdomain_deps/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: cross_subdomain_deps
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/cross_subdomain_deps/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: cross_subdomain_deps
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/cross_subdomain_deps/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: cross_subdomain_deps
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/pps_artifacts_requiring_action/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: pps_artifacts_requiring_action
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/pps_artifacts_requiring_action/items/required
        check: TABLE_HAS_COLUMNS
        register: pps_artifacts_requiring_action
        params:
          columns:
          - FQDN
          - Current Status
          - Action
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/pps_artifacts_requiring_action/items/properties/action/x-vocab
        check: CELL_IN_VOCABULARY
        register: pps_artifacts_requiring_action
        params:
          column: Action
          vocabulary:
          - REPLACE
          - REVIEW
          - REUSE
          - EXTEND
        intent: Action is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/pps_artifacts_requiring_action/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: pps_artifacts_requiring_action
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/pps_artifacts_requiring_action/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: pps_artifacts_requiring_action
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/pps_artifacts_requiring_action/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: pps_artifacts_requiring_action
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/pps_artifacts_requiring_action/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: pps_artifacts_requiring_action
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/boundary_rules/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: boundary_rules
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/boundary_rules/items/required
        check: TABLE_HAS_COLUMNS
        register: boundary_rules
        params:
          columns:
          - Rule Name
          - Statement
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/boundary_rules/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: boundary_rules
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/boundary_rules/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: boundary_rules
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/boundary_rules/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: boundary_rules
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/boundary_rules/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: boundary_rules
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/governance_outcome/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: governance_outcome
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/governance_outcome/items/required
        check: TABLE_HAS_COLUMNS
        register: governance_outcome
        params:
          columns:
          - Capability
          - Owner Subdomain
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/governance_outcome/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: governance_outcome
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/governance_outcome/x-business-language
        check: CELL_TOKEN_ABSENT
        register: governance_outcome
        params:
          columns:
          - Capability
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/governance_outcome/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: governance_outcome
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/governance_outcome/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: governance_outcome
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/registers/properties/governance_outcome/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: governance_outcome
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: PROVISIONAL_CODE_IN_PLACEMENT
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/0
        check: CELL_TOKEN_ABSENT
        register: ownership
        params:
          columns:
          - Capability
          - Owner Subdomain
          pattern: \b(?:STRUCTURE|TEST_DATA|VOCAB|AC|IN|WF|CC|CT|CS|RB|EV|TI|TE)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} in {column!r} — this stage places capabilities in subdomains; naming an artifact
            answers a question Stage 7 owns'
        intent: placement names a subdomain, never an artifact
      - id: STORAGE_CODE_IN_PLACEMENT
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/1
        check: CELL_TOKEN_ABSENT
        register: storage_governance
        params:
          columns:
          - Storage Need
          - Purpose
          - Subdomain
          pattern: \b(?:STRUCTURE|TEST_DATA|VOCAB|AC|IN|WF|CC|CT|CS|RB|EV|TI|TE)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} in {column!r} — a storage need is business language, not an artifact'
        intent: a store is described by what it holds, not by what will write it
      - id: SATISFIED_WITHOUT_EXISTING_ARTIFACT
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/2
        check: CELL_NOT_EMPTY
        register: ownership
        params:
          column: Existing Artifact
          only_when_column: Disposition
          only_when_value: SATISFIED
          detail: capability is SATISFIED but names no existing artifact — a claim that something already
            covers this needs the something
        intent: a satisfied capability names what satisfies it
      - id: EXISTING_ARTIFACT_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/3
        check: CITED_ARTIFACTS_RESOLVE
        register: ownership
        params:
          column: Existing Artifact
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
        intent: an artifact said to cover a capability must be one that really exists
      - id: PPS_ACTION_IDENTITY_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/4
        check: CITED_ARTIFACTS_RESOLVE
        register: pps_artifacts_requiring_action
        params:
          column: FQDN
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
        intent: an artifact this change will act on must be one the composition carries
      - id: DEPENDENCY_DIRECTION_MALFORMED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/5
        check: CELL_MATCHES
        register: cross_subdomain_deps
        params:
          column: Direction
          pattern: ^[a-z][a-z0-9_]*\s*(?:->|→)\s*[a-z][a-z0-9_]*$
          detail: direction {value!r} must read `this_subdomain -> peer` — a boundary has two sides
        intent: a dependency states which way it crosses the boundary
      - id: DEPENDENCY_SATISFIED_WITHOUT_ARTIFACT
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/6
        check: CELL_NOT_EMPTY
        register: cross_subdomain_deps
        params:
          column: Existing Artifact
          only_when_column: Status
          only_when_value: SATISFIED
          detail: dependency is SATISFIED but names no existing artifact — an unsatisfied dependency declared
            satisfied is how a gap goes missing
        intent: a satisfied dependency names the artifact that satisfies it
      - id: OUTCOME_CAPABILITY_UNPLACED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/7
        check: CELL_RESOLVES_IN_REGISTER
        register: governance_outcome
        params:
          column: Capability
          target_register: ownership
          target_column: Capability
        intent: the outcome restates placement, it does not introduce it
      - id: IN_SCOPE_CAPABILITY_UNPLACED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/8
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: ownership
        params:
          prior_phase: p5
          prior_register: scope_boundary
          prior_key_column: Capability
          key_column: Capability
          prior_only_when_column: Status
          prior_only_when_value: IN_SCOPE
        intent: a capability declared in scope and given no owner is in nobody's scope
      - id: BORROWED_CAPABILITY_NOT_DECLARED_CROSSING
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/9
        check: PRIOR_IDENTITIES_COVERED
        register: cross_subdomain_deps
        params:
          prior_phase: p5
          prior_register: cross_subdomain_refs
          prior_column: CC Code
          column: Existing Artifact
          require: prior_in_here
        intent: a capability borrowed across a subdomain boundary is a dependency, declared as one
      - id: TOUCHED_SUBDOMAIN_UNOWNED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/10
        check: PRIOR_IDENTITIES_COVERED
        register: ownership
        params:
          prior_phase: p0
          prior_register: cr_type
          prior_column: Subdomain
          column: Owner Subdomain
          require: prior_in_here
        intent: every subdomain a change touches has its owner declared
      - id: REGISTER_CELL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/allOf/11
        check: UNRESOLVED_MARKER_ABSENT
        params:
          exempt: []
          detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask
            it as a clarification, do not hedge it in a register'
        intent: an unanswered question left in a register reads as decided to every later phase
  - owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
  - owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
  - owner: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      literal:
      - id: HEADER_FIELD_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/document/required
        check: HEADER_FIELD_PRESENT
        params:
          fields:
          - phase
          - domain
          - subdomain
          - cr
          - rule_set
        intent: a phase document states its phase, its domain and subdomain, its change, and the rule
          set it was authored under
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/document/properties/phase/const
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - phase
          pattern: ^p7$
        intent: a document's phase is the phase whose rules judge it
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/document/properties/domain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: domain
          type:
            type: string
            minLength: 1
        intent: a document's domain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/document/properties/subdomain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: subdomain
          type:
            type:
            - string
            - array
            items:
              type: string
            minLength: 1
            minItems: 1
        intent: a document's subdomain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/document/properties/cr
        check: HEADER_FIELD_OF_TYPE
        params:
          field: cr
          type:
            type: string
            minLength: 1
        intent: a document's cr takes its declared form
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/document/properties/rule_set/pattern
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - rule_set
          pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P7_V[0-9]+$
        intent: a document's rule_set names a rule set of its own phase
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/document/properties/approval
        check: HEADER_FIELD_OF_TYPE
        params:
          field: approval
          type:
            type: object
            required:
            - gate
            - rule_set
            - state
            additionalProperties: false
            properties:
              gate:
                type: string
                minLength: 1
              rule_set:
                type: string
                pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P7_V[0-9]+$
              state:
                enum:
                - APPROVED
                - MIGRATED
                - RECONFIRMED
        intent: a document's approval takes its declared form
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/design_resolution/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: design_resolution
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/design_resolution/items/required
        check: TABLE_HAS_COLUMNS
        register: design_resolution
        params:
          columns:
          - Decision
          - Business Fact
          - Resolution
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/design_resolution/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: design_resolution
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/design_resolution/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: design_resolution
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/design_resolution/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: design_resolution
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/design_resolution/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: design_resolution
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/existing_inventory/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: existing_inventory
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/existing_inventory/items/required
        check: TABLE_HAS_COLUMNS
        register: existing_inventory
        params:
          columns:
          - FQDN
          - Action
          - Summary
          - Reason
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/existing_inventory/minItems
        check: TABLE_HAS_ROWS
        register: existing_inventory
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/existing_inventory/items/properties/action/x-vocab
        check: CELL_IN_VOCABULARY
        register: existing_inventory
        params:
          column: Action
          vocabulary:
          - REPLACE
          - REUSE
          - EXTEND
          - REPOINT
          - REVIEW
        intent: Action is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/existing_inventory/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: existing_inventory
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/existing_inventory/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: existing_inventory
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/existing_inventory/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: existing_inventory
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/existing_inventory/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: existing_inventory
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/new_artifacts/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: new_artifacts
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/new_artifacts/items/required
        check: TABLE_HAS_COLUMNS
        register: new_artifacts
        params:
          columns:
          - Capability
          - Family
          - Code
          - Summary
          - Owner Subdomain
          - Status
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/new_artifacts/items/properties/family/x-vocab
        check: CELL_IN_VOCABULARY
        register: new_artifacts
        params:
          column: Family
          vocabulary:
          - AC
          - IN
          - WF
          - CC
          - CT
          - EV
          - RB
          - VOCAB
          - STRUCTURE
          - TI
          - TE
        intent: Family is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/new_artifacts/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: new_artifacts
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/new_artifacts/x-business-language
        check: CELL_TOKEN_ABSENT
        register: new_artifacts
        params:
          columns:
          - Capability
          pattern: \b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b
          detail: '{token!r} appears in business-language column {column!r} — this register states business
            meaning, not design'
        intent: business registers name no compiled artifact
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/new_artifacts/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: new_artifacts
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/new_artifacts/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: new_artifacts
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/new_artifacts/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: new_artifacts
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/rb_declarations/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: rb_declarations
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/rb_declarations/items/required
        check: TABLE_HAS_COLUMNS
        register: rb_declarations
        params:
          columns:
          - RB Code
          - Binds WF
          - CS Bindings
          - Storage Structure
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/rb_declarations/minItems
        check: TABLE_HAS_ROWS
        register: rb_declarations
        intent: an empty required register asserts nothing
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/rb_declarations/items/properties/cs_bindings/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: rb_declarations
        params:
          column: CS Bindings
          type:
            type:
            - array
            - 'null'
            items:
              type: string
        intent: CS Bindings carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/rb_declarations/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: rb_declarations
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/rb_declarations/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: rb_declarations
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/rb_declarations/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: rb_declarations
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/rb_declarations/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: rb_declarations
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/execution_topology/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: execution_topology
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/execution_topology/items/required
        check: TABLE_HAS_COLUMNS
        register: execution_topology
        params:
          columns:
          - Workflow
          - Node
          - Node Type
          - Routing
          - Source Finding
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/execution_topology/minItems
        check: TABLE_HAS_ROWS
        register: execution_topology
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/execution_topology/items/properties/node_type/x-vocab
        check: CELL_IN_VOCABULARY
        register: execution_topology
        params:
          column: Node Type
          vocabulary:
          - IN
          - CC
          - EXIT
          - EXIT_SUCCESS
        intent: Node Type is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/execution_topology/items/properties/routing/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: execution_topology
        params:
          column: Routing
          type:
            type:
            - object
            - 'null'
            additionalProperties:
              type: string
        intent: Routing carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/execution_topology/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: execution_topology
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/execution_topology/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: execution_topology
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/execution_topology/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: execution_topology
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/execution_topology/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: execution_topology
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/cc_composition/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: cc_composition
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/cc_composition/items/required
        check: TABLE_HAS_COLUMNS
        register: cc_composition
        params:
          columns:
          - CC Code
          - Step
          - Step Name
          - Capability
          - Kind
          - Operation
          - Store
          - Consumes
          - Produces
          - Routing
          - Interpreted By
          - Semantic Status
          - Interface
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/cc_composition/items/properties/kind/x-vocab
        check: CELL_IN_VOCABULARY
        register: cc_composition
        params:
          column: Kind
          vocabulary:
          - CT
          - CS
        intent: Kind is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/cc_composition/items/properties/consumes/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: cc_composition
        params:
          column: Consumes
          type:
            type:
            - array
            - 'null'
            items:
              type: string
        intent: Consumes carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/cc_composition/items/properties/produces/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: cc_composition
        params:
          column: Produces
          type:
            type:
            - array
            - 'null'
            items:
              type: string
        intent: Produces carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/cc_composition/items/properties/routing/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: cc_composition
        params:
          column: Routing
          type:
            type:
            - object
            - 'null'
            additionalProperties:
              type: string
        intent: Routing carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/cc_composition/items/properties/interface/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: cc_composition
        params:
          column: Interface
          type:
            type:
            - object
            - 'null'
            additionalProperties: false
            properties:
              in:
                type: object
                additionalProperties:
                  type: string
              out:
                type: object
                additionalProperties:
                  type: string
        intent: Interface carries structure, and its value must take the declared form
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/step_bindings/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: step_bindings
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/step_bindings/items/required
        check: TABLE_HAS_COLUMNS
        register: step_bindings
        params:
          columns:
          - Owner
          - Step
          - Direction
          - Field
          - Bound To
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/step_bindings/items/properties/direction/x-vocab
        check: CELL_IN_VOCABULARY
        register: step_bindings
        params:
          column: Direction
          vocabulary:
          - INPUT
          - OUTPUT
        intent: Direction is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/step_bindings/items/properties/bound_to/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: step_bindings
        params:
          column: Bound To
          type:
            oneOf:
            - type: 'null'
            - type: string
            - type: object
              required:
              - literal
              additionalProperties: false
              properties:
                literal: {}
            - type: object
              required:
              - generated
              additionalProperties: false
              properties:
                generated:
                  const: true
        intent: Bound To carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/step_bindings/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: step_bindings
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/step_bindings/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: step_bindings
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/step_bindings/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: step_bindings
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/step_bindings/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: step_bindings
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/interface_fields/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: interface_fields
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/interface_fields/items/required
        check: TABLE_HAS_COLUMNS
        register: interface_fields
        params:
          columns:
          - Artifact
          - Direction
          - Field
          - Type
          - Required
          - Default
          - Meaning
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/interface_fields/items/properties/direction/x-vocab
        check: CELL_IN_VOCABULARY
        register: interface_fields
        params:
          column: Direction
          vocabulary:
          - INPUT
          - OUTPUT
          - ATTRIBUTE
        intent: Direction is a controlled vocabulary declared by the template
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/interface_fields/items/properties/required/x-vocab
        check: CELL_IN_VOCABULARY
        register: interface_fields
        params:
          column: Required
          vocabulary:
          - 'YES'
          - 'NO'
        intent: Required is a controlled vocabulary declared by the template
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/implementation_bindings/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: implementation_bindings
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/implementation_bindings/items/required
        check: TABLE_HAS_COLUMNS
        register: implementation_bindings
        params:
          columns:
          - CT Code
          - Callable
          - Operation
          - Kind
          - Purity
          - Refusal
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/implementation_bindings/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: implementation_bindings
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/implementation_bindings/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: implementation_bindings
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/implementation_bindings/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: implementation_bindings
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/implementation_bindings/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: implementation_bindings
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/vocabulary_extensions/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: vocabulary_extensions
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/vocabulary_extensions/items/required
        check: TABLE_HAS_COLUMNS
        register: vocabulary_extensions
        params:
          columns:
          - Vocabulary Code
          - Extends
          - Group
          - Casing
          - Value
          - Meaning
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/vocabulary_extensions/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: vocabulary_extensions
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/vocabulary_extensions/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: vocabulary_extensions
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/vocabulary_extensions/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: vocabulary_extensions
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/vocabulary_extensions/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: vocabulary_extensions
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/runtime_policies/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: runtime_policies
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/runtime_policies/items/required
        check: TABLE_HAS_COLUMNS
        register: runtime_policies
        params:
          columns:
          - RB Code
          - Capability
          - Key
          - Value
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/runtime_policies/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: runtime_policies
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/runtime_policies/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: runtime_policies
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/runtime_policies/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: runtime_policies
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/runtime_policies/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: runtime_policies
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_properties/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: artifact_properties
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_properties/items/required
        check: TABLE_HAS_COLUMNS
        register: artifact_properties
        params:
          columns:
          - Artifact
          - Property
          - Value
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_properties/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: artifact_properties
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_properties/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: artifact_properties
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_properties/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: artifact_properties
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_properties/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: artifact_properties
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/structure_stores/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: structure_stores
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/structure_stores/items/required
        check: TABLE_HAS_COLUMNS
        register: structure_stores
        params:
          columns:
          - Store Name
          - Storage Type
          - Proposed Path
          - Used By
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/structure_stores/items/properties/storage_type/x-vocab
        check: CELL_IN_VOCABULARY
        register: structure_stores
        params:
          column: Storage Type
          vocabulary:
          - CS_APPENDONLY_JSONL_V0
          - CS_MUTABLE_JSON_V0
          - CS_REGISTRY_V0
        intent: Storage Type is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/structure_stores/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: structure_stores
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/structure_stores/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: structure_stores
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/structure_stores/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: structure_stores
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/structure_stores/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: structure_stores
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: transport_bindings
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/items/required
        check: TABLE_HAS_COLUMNS
        register: transport_bindings
        params:
          columns:
          - Artifact
          - Direction
          - Operation
          - Handler Kind
          - Handler Target
          - Field
          - Bound To
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/items/properties/direction/x-vocab
        check: CELL_IN_VOCABULARY
        register: transport_bindings
        params:
          column: Direction
          vocabulary:
          - INGRESS
          - EGRESS
        intent: Direction is a controlled vocabulary declared by the template
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/items/properties/handler_kind/x-vocab
        check: CELL_IN_VOCABULARY
        register: transport_bindings
        params:
          column: Handler Kind
          vocabulary:
          - WF_INVOCATION
          - SNAPSHOT_READ
        intent: Handler Kind is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/items/properties/bound_to/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: transport_bindings
        params:
          column: Bound To
          type:
            oneOf:
            - type: 'null'
            - type: string
            - type: object
              required:
              - literal
              additionalProperties: false
              properties:
                literal: {}
            - type: object
              required:
              - generated
              additionalProperties: false
              properties:
                generated:
                  const: true
        intent: Bound To carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/items/properties/required/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: transport_bindings
        params:
          column: Required
          type:
            type:
            - boolean
            - 'null'
        intent: Required carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: transport_bindings
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: transport_bindings
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: transport_bindings
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/transport_bindings/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: transport_bindings
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_summary/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: artifact_summary
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_summary/items/required
        check: TABLE_HAS_COLUMNS
        register: artifact_summary
        params:
          columns:
          - Action
          - Subdomain
          - Count
          - Artifacts
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_summary/minItems
        check: TABLE_HAS_ROWS
        register: artifact_summary
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/artifact_summary/items/properties/action/x-vocab
        check: CELL_IN_VOCABULARY
        register: artifact_summary
        params:
          column: Action
          vocabulary:
          - REPLACE
          - EXTEND
          - NEW
        intent: Action is a controlled vocabulary declared by the template
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/generation_provenance/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: generation_provenance
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/generation_provenance/items/required
        check: TABLE_HAS_COLUMNS
        register: generation_provenance
        params:
          columns:
          - Artifact
          - Generator
          - Generator Sources
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/generation_provenance/items/properties/generator_sources/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: generation_provenance
        params:
          column: Generator Sources
          type:
            type:
            - array
            - 'null'
            items:
              type: string
        intent: Generator Sources carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/generation_provenance/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: generation_provenance
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/generation_provenance/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: generation_provenance
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/generation_provenance/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: generation_provenance
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/generation_provenance/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: generation_provenance
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/declared_reach/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: declared_reach
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/declared_reach/items/required
        check: TABLE_HAS_COLUMNS
        register: declared_reach
        params:
          columns:
          - Act
          - Consults
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/declared_reach/items/properties/consults/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: declared_reach
        params:
          column: Consults
          type:
            type:
            - array
            - 'null'
            items:
              type: string
        intent: Consults carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/declared_reach/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: declared_reach
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/declared_reach/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: declared_reach
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/declared_reach/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: declared_reach
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/declared_reach/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: declared_reach
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_discharge/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: refusal_discharge
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_discharge/items/required
        check: TABLE_HAS_COLUMNS
        register: refusal_discharge
        params:
          columns:
          - Operation
          - Refused When
          - Act
          - Step
          - Outcome
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_discharge/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: refusal_discharge
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_discharge/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: refusal_discharge
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_discharge/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: refusal_discharge
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_discharge/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: refusal_discharge
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_deferrals/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: refusal_deferrals
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_deferrals/items/required
        check: TABLE_HAS_COLUMNS
        register: refusal_deferrals
        params:
          columns:
          - Operation
          - Refused When
          - Deferred To
          - Until
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_deferrals/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: refusal_deferrals
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_deferrals/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: refusal_deferrals
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_deferrals/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: refusal_deferrals
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_deferrals/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: refusal_deferrals
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_governance_discharge/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: refusal_governance_discharge
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_governance_discharge/items/required
        check: TABLE_HAS_COLUMNS
        register: refusal_governance_discharge
        params:
          columns:
          - Operation
          - Refused When
          - Phase
          - Governing Rule
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_governance_discharge/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: refusal_governance_discharge
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_governance_discharge/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: refusal_governance_discharge
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_governance_discharge/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: refusal_governance_discharge
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/refusal_governance_discharge/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: refusal_governance_discharge
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_steps/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: molecule_steps
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_steps/items/required
        check: TABLE_HAS_COLUMNS
        register: molecule_steps
        params:
          columns:
          - CT Code
          - Step
          - Kind
          - Target
          - Over
          - Iterator
          - Emits
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_steps/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: molecule_steps
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_steps/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: molecule_steps
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_steps/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: molecule_steps
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_steps/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: molecule_steps
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_step_bindings/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: molecule_step_bindings
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_step_bindings/items/required
        check: TABLE_HAS_COLUMNS
        register: molecule_step_bindings
        params:
          columns:
          - CT Code
          - Step
          - Role
          - Field
          - Bound To
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_step_bindings/items/properties/role/x-vocab
        check: CELL_IN_VOCABULARY
        register: molecule_step_bindings
        params:
          column: Role
          vocabulary:
          - INPUT
          - CARRY
          - UPDATE
        intent: Role is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_step_bindings/items/properties/bound_to/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: molecule_step_bindings
        params:
          column: Bound To
          type:
            oneOf:
            - type: 'null'
            - type: string
            - type: object
              required:
              - literal
              additionalProperties: false
              properties:
                literal: {}
            - type: object
              required:
              - generated
              additionalProperties: false
              properties:
                generated:
                  const: true
        intent: Bound To carries structure, and its value must take the declared form
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_step_bindings/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: molecule_step_bindings
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_step_bindings/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: molecule_step_bindings
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_step_bindings/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: molecule_step_bindings
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/molecule_step_bindings/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: molecule_step_bindings
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_cases/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: test_cases
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_cases/items/required
        check: TABLE_HAS_COLUMNS
        register: test_cases
        params:
          columns:
          - CT Code
          - Case
          - Expected Outcome
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_cases/items/properties/expected_outcome/x-vocab
        check: CELL_IN_VOCABULARY
        register: test_cases
        params:
          column: Expected Outcome
          vocabulary:
          - SUCCESS
          - VIOLATION
        intent: Expected Outcome is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_cases/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: test_cases
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_cases/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: test_cases
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_cases/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: test_cases
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_cases/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: test_cases
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_case_values/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: test_case_values
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_case_values/items/required
        check: TABLE_HAS_COLUMNS
        register: test_case_values
        params:
          columns:
          - CT Code
          - Case
          - Role
          - Field
          - Value
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_case_values/items/properties/role/x-vocab
        check: CELL_IN_VOCABULARY
        register: test_case_values
        params:
          column: Role
          vocabulary:
          - INPUT
          - EXPECTED
          - ASSERT
          - RECORDED
        intent: Role is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_case_values/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: test_case_values
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_case_values/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: test_case_values
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_case_values/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: test_case_values
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/test_case_values/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: test_case_values
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/withdrawn_facts/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: withdrawn_facts
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/withdrawn_facts/items/required
        check: TABLE_HAS_COLUMNS
        register: withdrawn_facts
        params:
          columns:
          - Artifact
          - Fact
          - Reason
          - Source Finding
        intent: downstream phases read these columns by name
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/withdrawn_facts/items/properties/source_finding/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: withdrawn_facts
        params:
          column: Source Finding
          type:
            oneOf:
            - type: 'null'
            - type: object
              required:
              - register
              additionalProperties: false
              properties:
                phase:
                  type: string
                  pattern: ^p[0-8]$
                register:
                  type: string
                  pattern: ^[a-z][a-z0-9_]*$
                row:
                  type: integer
                key:
                  type: string
                  minLength: 1
              not:
                required:
                - row
                - key
            - type: object
              required:
              - artifact
              additionalProperties: false
              properties:
                artifact:
                  type: string
                  pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
            - type: object
              required:
              - source
              additionalProperties: false
              properties:
                source:
                  const: human
            - type: array
              minItems: 2
              items:
                oneOf:
                - type: object
                  required:
                  - register
                  additionalProperties: false
                  properties:
                    phase:
                      type: string
                      pattern: ^p[0-8]$
                    register:
                      type: string
                      pattern: ^[a-z][a-z0-9_]*$
                    row:
                      type: integer
                    key:
                      type: string
                      minLength: 1
                  not:
                    required:
                    - row
                    - key
                - type: object
                  required:
                  - artifact
                  additionalProperties: false
                  properties:
                    artifact:
                      type: string
                      pattern: ^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$
                - type: object
                  required:
                  - source
                  additionalProperties: false
                  properties:
                    source:
                      const: human
        intent: Source Finding carries structure, and its value must take the declared form
      - id: ROW_WITHOUT_SOURCE_FINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/withdrawn_facts/items/properties/source_finding/x-derived/CITATION_PRESENT
        check: CITATION_PRESENT
        register: withdrawn_facts
        params:
          column: Source Finding
          detail: row cites no earlier finding — a phase restates its input, it does not add to it
        intent: an uncited row has no provenance in the dossier
      - id: SOURCE_FINDING_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/withdrawn_facts/items/properties/source_finding/x-derived/SOURCE_FINDING_RESOLVES
        check: SOURCE_FINDING_RESOLVES
        register: withdrawn_facts
        params:
          column: Source Finding
          known_registers:
          - acceptance_criteria
          - actions
          - actors
          - analysis_findings
          - architectural_observations
          - artifact_properties
          - artifact_summary
          - assumptions
          - authoring_decisions
          - authoring_scope
          - authority_boundaries
          - authority_deferrals
          - belief_verification
          - bm_entities
          - boundary_rules
          - build_order
          - business_events
          - business_invariants
          - business_objects
          - business_processes
          - business_vocabulary
          - capability_graph
          - cc_composition
          - clarification_requests
          - constraint_register
          - constraints
          - cr_type
          - critical_path
          - cross_subdomain_deps
          - cross_subdomain_notes
          - cross_subdomain_refs
          - declared_reach
          - dependency_discoveries
          - dependency_graph
          - design_decisions
          - design_resolution
          - discovery_concerns
          - entities
          - entity_attributes
          - events
          - execution_topology
          - existing_inventory
          - field_declarations
          - gap_register
          - gaps
          - generation_provenance
          - governance_outcome
          - governance_scope
          - identity_and_sameness
          - identity_semantics
          - impact_analysis
          - implementation_bindings
          - interface_fields
          - invariants
          - known_facts
          - lifecycle_states
          - lifecycle_transitions
          - mandate_artifact_summary
          - molecule_step_bindings
          - molecule_steps
          - new_artifacts
          - new_capabilities
          - new_intents
          - open_questions
          - operation_refusals
          - out_of_scope
          - ownership
          - placement_decision
          - pps_artifacts_requiring_action
          - pps_baseline_fqdns
          - process_steps
          - provisional_codes
          - purpose_provenance
          - rb_declarations
          - refusal_deferrals
          - refusal_discharge
          - refusal_governance_discharge
          - relationships
          - requested_outcomes
          - resources
          - runtime_policies
          - saturation
          - scope_boundary
          - step_bindings
          - storage_governance
          - structure_stores
          - subdomain_purpose
          - subdomain_purposes
          - system_beliefs
          - test_case_values
          - test_cases
          - transport_bindings
          - verification_results
          - vocabulary_extensions
          - withdrawn_facts
        intent: a citation must name something this phase can actually cite
      - id: CITATION_ORDINAL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/properties/registers/properties/withdrawn_facts/items/properties/source_finding/x-derived/CITED_ORDINAL_RESOLVES
        check: CITED_ORDINAL_RESOLVES
        register: withdrawn_facts
        params:
          column: Source Finding
        intent: an ordinal past the end of a register cites a finding that is not there
      - id: NEW_CODE_ALREADY_EXISTS
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/0
        check: CITED_ARTIFACTS_ABSENT
        register: new_artifacts
        params:
          column: Code
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
        intent: an identity assigned as new must not already name something else
      - id: NEW_CODE_MALFORMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/1
        check: CELL_MATCHES
        register: new_artifacts
        params:
          column: Code
          pattern: ^[a-z][a-z0-9_.]*::(?:STRUCTURE|TEST_DATA|VOCAB|AC|IN|WF|CC|CT|CS|RB|EV|TI|TE)_[A-Z0-9_]+_V\d+$
          detail: binding code {value!r} must be domain::FAMILY_NAME_V<n>
        intent: a binding identity is domain-qualified, family-prefixed and versioned
      - id: EXISTING_INVENTORY_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/2
        check: CITED_ARTIFACTS_RESOLVE
        register: existing_inventory
        params:
          column: FQDN
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
        intent: an artifact carried over from the composition must really be in it
      - id: AMENDED_ARTIFACT_NOT_AUTHORABLE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/3
        check: CELL_MATCHES
        register: existing_inventory
        params:
          column: FQDN
          pattern: ^[a-z][a-z0-9_.]*::(?:STRUCTURE|VOCAB|AC|IN|WF|CC|CT|RB|EV|TI|TE)_[A-Z0-9_]+_V\d+$
          only_when_column: Action
          only_when_value: EXTEND
          detail: 'amends {value!r}, whose family this design cannot author — an amended artifact is rendered
            whole, so this schedules a document to be rewritten from registers that never held its content.
            The governance surface is authored, not constructed: cite it with REUSE or REVIEW, and deliver
            the change by authoring it'
        intent: a design amends only what it could have authored
      - id: REPLACED_ARTIFACT_NOT_AUTHORABLE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/4
        check: CELL_MATCHES
        register: existing_inventory
        params:
          column: FQDN
          pattern: ^[a-z][a-z0-9_.]*::(?:STRUCTURE|VOCAB|AC|IN|WF|CC|CT|RB|EV|TI|TE)_[A-Z0-9_]+_V\d+$
          only_when_column: Action
          only_when_value: REPLACE
          detail: replaces {value!r}, whose family this design cannot author — a replacement is a rendering
            like any other. The governance surface is authored, not constructed
        intent: a design replaces only what it could have authored
      - id: TOPOLOGY_WORKFLOW_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/5
        check: CELL_RESOLVES_IN_REGISTER
        register: execution_topology
        params:
          column: Workflow
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
        intent: a workflow in the topology is one this design declared or carried over
      - id: TOPOLOGY_NODE_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/6
        check: CELL_RESOLVES_IN_REGISTER
        register: execution_topology
        params:
          column: Node
          prefer_column: Runs
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
          exempt_prefixes:
          - EXIT
          detail: a binding identity is immutable, so a spelling variant is a second artifact rather than
            a synonym
        intent: every node in the topology runs an identity this design actually assigned
      - id: TOPOLOGY_NODE_REPEATED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/7
        check: COLUMN_VALUES_UNIQUE
        register: execution_topology
        params:
          columns:
          - Workflow
          - Node
          detail: '{0} names {1} again (first at row {first}) — a node that runs a contract twice needs
            a key for each place, and `Runs` naming the contract'
        intent: a node names one place in its workflow
      - id: TOPOLOGY_ROUTE_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/8
        check: TOPOLOGY_ROUTE_RESOLVES
        register: execution_topology
        params:
          exempt_prefixes:
          - EXIT
          observation: si.behavior_logic.list
        intent: control reaches only a node the workflow declares or already has, or an ending
      - id: RB_BINDS_UNDECLARED_WORKFLOW
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/9
        check: CELL_RESOLVES_IN_REGISTER
        register: rb_declarations
        params:
          column: Binds WF
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
        intent: a runtime binding binds a workflow that exists in this design
      - id: RB_CODE_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/10
        check: CELL_RESOLVES_IN_REGISTER
        register: rb_declarations
        params:
          column: RB Code
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
        intent: a runtime binding is itself a declared artifact, never implicit
      - id: COMPOSITION_CC_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/11
        check: CELL_RESOLVES_IN_REGISTER
        register: cc_composition
        params:
          column: CC Code
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
        intent: a composition belongs to a capability contract this design declared
      - id: COMPOSITION_STEP_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/12
        check: CELL_RESOLVES_IN_REGISTER
        register: cc_composition
        params:
          column: Capability
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
        intent: a step invokes a capability that is declared new or carried over, never invented inline
      - id: OBSERVATION_WITHOUT_INTERPRETATION
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/13
        check: OUTCOME_GROUNDED_IN_OPERATION
        register: cc_composition
        params:
          column: Interpreted By
          kind_column: Kind
          kind_value: CS
          routing_column: Routing
          status_column: Semantic Status
          observation: si.capability.surface
          detail: branches on {outcomes}, which {operation} does not answer — it answers {answers}. An
            outcome the store cannot produce comes from an interpretation, and this step names none, so
            the branch is a decision nothing makes
        intent: an outcome the operation cannot answer names the transform that produces it
      - id: OBSERVATION_WITHOUT_SEMANTIC_STATUS
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/14
        check: OUTCOME_GROUNDED_IN_OPERATION
        register: cc_composition
        params:
          column: Semantic Status
          kind_column: Kind
          kind_value: CS
          routing_column: Routing
          status_column: Semantic Status
          observation: si.capability.surface
          detail: routes on {outcomes} and declares no semantic status — {operation} answers {answers},
            so the outcome routed on is an interpretation's, and the workflow branch it feeds has nothing
            declared to route on
        intent: an interpretation names the outcome it yields, closing the route
      - id: STORE_UNGROUNDED_IN_CAPABILITY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/15
        check: STORE_GROUNDED_IN_CAPABILITY
        register: cc_composition
        params:
          column: Store
          capability_column: Capability
          store_keeping:
          - CS_APPENDONLY_JSONL_V0
          - CS_MUTABLE_JSON_V0
          - CS_REGISTRY_V0
          observation: si.capability.surface
          detail_missing: names no store on {capability}, which keeps records — a storage step that addresses
            nothing is a read or a write with no subject
          detail_spurious: names a store on {capability}, which keeps none — the step addresses records
            that capability has no way to hold
        intent: a step addresses a store exactly when its capability keeps one
      - id: STEP_CONSUMES_NOTHING_FROM_OPERATION_WITH_INPUT
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/16
        check: CONSUMPTION_GROUNDED_IN_OPERATION
        register: cc_composition
        params:
          column: Consumes
          capability_column: Capability
          kind_column: Kind
          kind_value: CS
          observation: si.capability.surface
          detail: consumes nothing and invokes {operation}, which accepts {accepts} — the operation receives
            no value for what it takes, and the step reports success on having addressed nothing
        intent: a step consuming nothing invokes an operation that takes nothing
      - id: DECLARED_REACH_UNUSED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/17
        check: REACH_IS_USED
        register: declared_reach
        params:
          register: declared_reach
          topology_register: execution_topology
          composition_register: cc_composition
          observation: si.store.list
          contract_observation: si.capability.surface#contracts
          detail: declares a reach to {binding} and reads nothing it covers — that binding answers for
            {stores}, and no step this act runs addresses any of them. A permission granted for nothing
            is one whose purpose nobody reviewed
        intent: every reach an act declares is used by a read that act performs
      - id: UNDECLARED_REACH_READ
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/18
        check: READ_IS_DECLARED
        register: execution_topology
        params:
          register: declared_reach
          rb_register: rb_declarations
          topology_register: execution_topology
          composition_register: cc_composition
          observation: si.store.list
          contract_observation: si.capability.surface#contracts
          detail: reads {store}, which {binding} does not cover and no declared reach names — the act
            reaches records another part of the business owns and its design does not say so, which is
            invisible until the act runs
        intent: an act reads nothing it did not declare a reach to
      - id: CROSS_SUBDOMAIN_WRITE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/19
        check: CROSS_SUBDOMAIN_REACH_READ_ONLY
        register: execution_topology
        params:
          topology_register: execution_topology
          new_register: new_artifacts
          artifact_observation: si.artifact.list
          capability_observation: si.capability.surface
          contract_observation: si.capability.surface#contracts
        intent: an act reaching into another subdomain reads what it holds and never changes it
      - id: INTERPRETATION_TRANSFORM_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/20
        check: CELL_RESOLVES_IN_REGISTER
        register: cc_composition
        params:
          column: Interpreted By
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
          detail: an interpreting transform is an artifact like any other, declared or carried over
        intent: the transform that turns an observation into a decision is itself governed
      - id: VOCABULARY_WITHOUT_EXTENDS
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/21
        check: CELL_NOT_EMPTY
        register: vocabulary_extensions
        params:
          column: Extends
          detail: vocabulary says nothing about what it extends — a base vocabulary declares that with
            the none marker, because an empty cell and an omission render the same thing
        intent: a vocabulary states what it extends, or states that it extends nothing
      - id: STORE_WITHOUT_PROPOSED_PATH
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/22
        check: CELL_NOT_EMPTY
        register: structure_stores
        params:
          column: Proposed Path
          detail: store declares no proposed path — a store nobody can locate is not designed
        intent: a declared store says where it will live
      - id: SATISFIED_DEPENDENCY_NOT_INVENTORIED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/23
        check: PRIOR_IDENTITIES_COVERED
        register: existing_inventory
        params:
          prior_phase: p6
          prior_register: cross_subdomain_deps
          prior_column: Existing Artifact
          column: FQDN
          require: prior_in_here
        intent: a dependency declared satisfied by an existing artifact must be inventoried as reuse
      - id: PROVISIONAL_CODE_NEVER_BOUND
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/24
        check: PRIOR_IDENTITIES_COVERED
        register: new_artifacts
        params:
          prior_phase: p5
          prior_register: provisional_codes
          prior_column: Provisional Code
          column: Code
          require: prior_in_here
          match_on: bare_code
          union:
          - register: existing_inventory
            column: FQDN
            only_when_column: Action
            only_when_value: EXTEND
        intent: a capability the business asked for and the design never bound is declined, not deferred
      - id: AUTHORED_ARTIFACT_WITHOUT_INTENT
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/25
        check: PRIOR_IDENTITIES_COVERED
        register: new_artifacts
        params:
          prior_phase: p5
          prior_register: provisional_codes
          prior_column: Provisional Code
          column: Code
          require: here_in_prior
          match_on: bare_code
        intent: an artifact the design authors is one the business asked for, never one it invented
      - id: WORKFLOW_WITHOUT_TOPOLOGY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/26
        check: REGISTER_COVERS_REGISTER
        register: execution_topology
        params:
          source_register: new_artifacts
          source_column: Code
          column: Workflow
          only_when_column: Family
          only_when_value: WF
        intent: a workflow with no declared graph is a workflow construction would have to invent
      - id: WORKFLOW_WITHOUT_RUNTIME_BINDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/27
        check: REGISTER_COVERS_REGISTER
        register: rb_declarations
        params:
          source_register: new_artifacts
          source_column: Code
          column: Binds WF
          only_when_column: Family
          only_when_value: WF
        intent: a workflow with no runtime binding cannot resolve the capabilities it composes
      - id: CONTRACT_WITHOUT_COMPOSITION
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/28
        check: REGISTER_COVERS_REGISTER
        register: cc_composition
        params:
          source_register: new_artifacts
          source_column: Code
          column: CC Code
          only_when_column: Family
          only_when_value: CC
        intent: a capability contract with no declared pipeline specifies nothing to build
      - id: TRANSFORM_WITHOUT_IMPLEMENTATION
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/29
        check: REGISTER_COVERS_REGISTER
        register: implementation_bindings
        params:
          source_register: new_artifacts
          source_column: Code
          column: CT Code
          only_when_column: Family
          only_when_value: CT
        intent: a transform is the one family that points outside the composition; the path is designed,
          not discovered
      - id: REPLACED_ARTIFACT_WITHOUT_SUCCESSOR
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/30
        check: REGISTER_COVERS_REGISTER
        register: artifact_properties
        params:
          source_register: existing_inventory
          source_column: FQDN
          column: Value
          only_when_column: Action
          only_when_value: REPLACE
          covered_only_when_column: Property
          covered_only_when_value: supersedes
        intent: an artifact this design replaces is named by whatever supersedes it
      - id: VOCABULARY_WITHOUT_GROUP
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/31
        check: CELL_NOT_EMPTY
        register: vocabulary_extensions
        params:
          column: Group
          detail: vocabulary names no group for its values — the renderer would supply one, and it supplies
            the same one to every vocabulary whatever the values mean
        intent: a vocabulary states the group its values belong to
      - id: VOCABULARY_WITHOUT_CASING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/32
        check: CELL_NOT_EMPTY
        register: vocabulary_extensions
        params:
          column: Casing
          detail: vocabulary names no spelling for its values — the renderer would supply one, and a spelling
            its values do not have is refused by the platform that reads them
        intent: a vocabulary states the spelling its values take
      - id: VOCABULARY_WITHOUT_VALUES
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/33
        check: REGISTER_COVERS_REGISTER
        register: vocabulary_extensions
        params:
          source_register: new_artifacts
          source_column: Code
          column: Vocabulary Code
          only_when_column: Family
          only_when_value: VOCAB
        intent: a vocabulary that declares no value admits nothing
      - id: BINDING_STEP_OWNER_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/34
        check: CELL_RESOLVES_IN_REGISTER
        register: step_bindings
        params:
          column: Owner
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
        intent: a binding belongs to a workflow or contract this design declared
      - id: INTERFACE_ARTIFACT_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/35
        check: CELL_RESOLVES_IN_REGISTER
        register: interface_fields
        params:
          column: Artifact
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
        intent: a field belongs to an artifact this design declared
      - id: BINDING_READS_UNPUBLISHED_FIELD
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/36
        check: BINDING_SOURCE_PUBLISHED
        register: step_bindings
        params:
          step_register: cc_composition
          observation: si.capability.surface
        intent: a binding reads a field the operation yields, never one it was hoped would exist
      - id: STEP_NAMES_UNPUBLISHED_OPERATION
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/37
        check: STEP_OPERATION_PUBLISHED
        register: cc_composition
        params:
          observation: si.capability.surface
        intent: a step invokes an operation the capability offers, never one it was assumed to have
      - id: STEP_CONSUMES_UNDECLARED_INPUT
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/38
        check: STEP_CONSUMES_PUBLISHED
        register: cc_composition
        params:
          observation: si.capability.surface
        intent: a step hands an operation fields it accepts, never ones it was hoped would exist
      - id: IMPLEMENTATION_WITHOUT_KIND
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/39
        check: CELL_NOT_EMPTY
        register: implementation_bindings
        params:
          column: Kind
          detail: transform declares no kind — whether it runs an implementation or a stream of steps
            decides every other rule this row is held to
        intent: a transform says whether it is an atom or a molecule
      - id: IMPLEMENTATION_KIND_UNKNOWN
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/40
        check: CELL_MATCHES
        register: implementation_bindings
        params:
          column: Kind
          pattern: ^(atom|molecule)$
          detail: kind is {value!r}; a transform is an atom, which runs an implementation, or a molecule,
            which runs its declared steps, and the schema admits nothing else
        intent: kind is one of the two the runtime can run
      - id: IMPLEMENTATION_WITHOUT_REFUSAL
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/41
        check: CELL_NOT_EMPTY
        register: implementation_bindings
        params:
          column: Refusal
          detail: transform declares no refusal — whether a judgement is raised or returned is the one
            fact that says if a step routing on it can ever fail, and both look the same from outside
        intent: a transform says how it expresses a judgement about its subject
      - id: IMPLEMENTATION_REFUSAL_UNKNOWN
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/42
        check: CELL_MATCHES
        register: implementation_bindings
        params:
          column: Refusal
          pattern: ^(raises|returns|never)$
          detail: refusal is {value!r}; a transform raises its judgement, returns it, or makes none, and
            the schema admits nothing else
        intent: refusal is one of the three the composition can act on
      - id: INTERPRETATION_TRANSFORM_CANNOT_REFUSE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/43
        check: INTERPRETATION_TRANSFORM_REFUSES
        register: cc_composition
        params:
          column: Interpreted By
          status_column: Semantic Status
          observation: si.capability.surface#transforms
          design_register: implementation_bindings
          design_code_column: CT Code
          design_refusal_column: Refusal
        intent: an interpretation can fail, or the branch it feeds is unreachable
      - id: IMPLEMENTATION_CALLABLE_UNCONVENTIONAL
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/44
        check: CELL_MATCHES
        register: implementation_bindings
        params:
          column: Callable
          pattern: ^execute$
          detail: callable is {value!r}; every transform in the composition is entered through `execute`,
            and a loader given another name finds nothing
        intent: a transform is entered the one way every transform is entered
      - id: BINDING_WITHOUT_SOURCE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/45
        check: CELL_NOT_EMPTY
        register: step_bindings
        params:
          column: Bound To
          detail: field is bound to nothing — construction would have to choose a source
        intent: every declared input names where its value comes from
      - id: STORE_PATH_FORMAT_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/46
        check: CELL_MATCHES
        register: structure_stores
        params:
          column: Proposed Path
          pattern: ^.*\.json$
          only_when_column: Storage Type
          only_when_value: CS_MUTABLE_JSON_V0
          detail: '{value!r} names a store CS_MUTABLE_JSON_V0 keeps, and CS_MUTABLE_JSON_V0 writes .json
            — a store''s name must not advertise a format its capability does not write'
        intent: a store is named for the format its capability actually writes
      - id: STORE_PATH_FORMAT_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/47
        check: CELL_MATCHES
        register: structure_stores
        params:
          column: Proposed Path
          pattern: ^.*\.jsonl$
          only_when_column: Storage Type
          only_when_value: CS_REGISTRY_V0
          detail: '{value!r} names a store CS_REGISTRY_V0 keeps, and CS_REGISTRY_V0 writes .jsonl — a
            store''s name must not advertise a format its capability does not write'
        intent: a store is named for the format its capability actually writes
      - id: STORE_PATH_FORMAT_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/48
        check: CELL_MATCHES
        register: structure_stores
        params:
          column: Proposed Path
          pattern: ^.*\.jsonl$
          only_when_column: Storage Type
          only_when_value: CS_APPENDONLY_JSONL_V0
          detail: '{value!r} names a store CS_APPENDONLY_JSONL_V0 keeps, and CS_APPENDONLY_JSONL_V0 writes
            .jsonl — a store''s name must not advertise a format its capability does not write'
        intent: a store is named for the format its capability actually writes
      - id: BINDING_SOURCE_UNROOTED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/49
        check: CELL_MATCHES
        register: step_bindings
        params:
          column: Bound To
          pattern: ^(?:(?:payload|inputs|results|capability_result)\..+|result_status|(?!(?:payload|inputs|results|capability_result)$)[^.]*|.*::.*|-?[0-9]+(?:\.[0-9]+)?)$
          detail: '{value!r} is not rooted in a scope execution offers — a source names a field under
            one of payload, inputs, results, capability_result, or is result_status'
        intent: a source that names a place is rooted in one execution scope actually offers
      - id: NODE_INPUT_UNBOUND
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/50
        check: NODE_INPUT_BOUND
        register: step_bindings
        params:
          topology_register: execution_topology
          fields_register: interface_fields
          composition_register: cc_composition
          observation: si.capability.surface#contracts
        intent: a workflow hands a contract everything that contract says it requires
      - id: ENTRANCE_UNDERSUPPLIES_GATE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/51
        check: ENTRANCE_SUPPLIES_GATE
        register: transport_bindings
        params:
          topology_register: execution_topology
          fields_register: interface_fields
          observation: si.capability.surface#intents
        intent: an entrance supplies everything the gate it reaches requires
      - id: BINDING_SOURCE_UNREACHABLE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/52
        check: BINDING_SOURCE_REACHABLE
        register: step_bindings
        params:
          topology_register: execution_topology
          pattern: results\.([A-Za-z][A-Za-z0-9_.:]*?)\.
        intent: a source that names another node must name one this workflow reaches
      - id: STEP_INTERFACE_NOT_CONFORMANT
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/53
        check: STEP_INTERFACE_CONFORMS
        register: cc_composition
        params:
          observation: si.capability.surface#transforms
        intent: a transform handed an input it does not declare receives nothing under that name
      - id: STEP_BINDING_NOT_IN_INTERFACE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/54
        check: STEP_BINDINGS_MATCH_INTERFACE
        register: step_bindings
        params:
          composition_register: cc_composition
        intent: a binding outside the interface feeds a capability input that does not exist
      - id: STEP_INPUT_UNBOUND
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/55
        check: STEP_INPUTS_BOUND
        register: step_bindings
        params:
          composition_register: cc_composition
          fields_register: interface_fields
        intent: a capability handed no value for an input it declares receives a null
      - id: BINDING_SOURCE_MALFORMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/56
        check: CELL_MATCHES
        register: step_bindings
        params:
          column: Bound To
          pattern: ^(?:capability_result\.[A-Za-z_][A-Za-z0-9_]*|result_status)$
          only_when_column: Direction
          only_when_value: OUTPUT
          detail: output binds {value!r}, which is not a form the runtime resolves — an output is written
            to capability_result.<field> or result_status; an input reads inputs.<field>, payload.<field>,
            results.<step>.<field>, or is a literal
        intent: a reference the runtime cannot resolve is indistinguishable from one it can
      - id: BINDING_SOURCE_MALFORMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/57
        check: CELL_MATCHES
        register: step_bindings
        params:
          column: Bound To
          pattern: ^(?:inputs\.[A-Za-z_][A-Za-z0-9_.]*|payload\.[A-Za-z_][A-Za-z0-9_.]*|results\.[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z_][A-Za-z0-9_.]*|[\[{].*[\]}]|"[^"]*"|'[^']*'|-?[0-9]+(?:\.[0-9]+)?|[A-Za-z_][A-Za-z0-9_]*::[A-Za-z_][A-Za-z0-9_]*|[A-Za-z_][A-Za-z0-9_-]*)$
          only_when_column: Direction
          only_when_value: INPUT
          detail: input binds {value!r}, which is not a form the runtime resolves — an output is written
            to capability_result.<field> or result_status; an input reads inputs.<field>, payload.<field>,
            results.<step>.<field>, or is a literal
        intent: a reference the runtime cannot resolve is indistinguishable from one it can
      - id: CONTRACT_OUTPUT_UNPRODUCED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/58
        check: CONTRACT_OUTPUT_PRODUCED
        register: interface_fields
        params:
          bindings_register: step_bindings
        intent: a declared output no step emits gives every caller a name that resolves to nothing
      - id: GENERATED_ARTIFACT_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/59
        check: CELL_RESOLVES_IN_REGISTER
        register: generation_provenance
        params:
          column: Artifact
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
          detail: provenance is stated about an artifact this design neither authors nor carries over
            — a generator for something nothing schedules produces nothing
        intent: provenance belongs to an artifact the design actually declares
      - id: ARTIFACT_HAS_TWO_GENERATORS
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/60
        check: COLUMN_VALUES_UNIQUE
        register: generation_provenance
        params:
          column: Artifact
          detail: '{value} is generated twice, first at row {first} — an artifact has exactly one producer,
            and two producers of one truth drift'
        intent: one artifact, one producer, so agreement with the generator means something
      - id: GENERATED_SOURCE_WITHOUT_GENERATOR
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/61
        check: CELL_RESOLVES_IN_REGISTER
        register: step_bindings
        params:
          column: Owner
          only_when_column: Bound To
          only_when_value:
            generated: true
          target_registers:
          - generation_provenance
          target_column: Artifact
          detail: binds a generated value, and its owner names no generator — a generator determines only
            what the design says it does
        intent: a value is declared generated only where the design names its generator
      - id: GENERATOR_UNNAMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/62
        check: CELL_NOT_EMPTY
        register: generation_provenance
        params:
          column: Generator
          detail: artifact is declared generated and names no generator — construction has nothing to
            invoke and no way to reach it
        intent: a generated artifact names what produces it
      - id: GENERATOR_UNREACHABLE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/63
        check: CELL_MATCHES
        register: generation_provenance
        params:
          column: Generator
          pattern: ^[a-z_][a-z0-9_]*(?:\.[a-z_][a-z0-9_]*)*:[a-z_][a-z0-9_]*$
          detail: generator {value!r} must be module:callable — construction imports its generator and
            a script it can only shell out to is one nothing governs
        intent: a generator is invocable from the composition, not only by a person at a terminal
      - id: GENERATOR_SOURCES_UNNAMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/64
        check: CELL_NOT_EMPTY
        register: generation_provenance
        params:
          column: Generator Sources
          detail: generator names no sources — a template and the declaration read with it are one generator,
            and naming neither permits regenerating from a stale pairing
        intent: a generator is its sources together, so a change to either is a change to it
      - id: REFUSAL_UNACCOUNTED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/65
        check: PRIOR_ROWS_PRESENT_BY_KEY
        register: refusal_discharge
        params:
          prior_phase: p0
          prior_register: operation_refusals
          prior_key_column:
          - Operation
          - Refused When
          key_column:
          - Operation
          - Refused When
          registers:
          - refusal_discharge
          - refusal_deferrals
          - refusal_governance_discharge
        intent: every refusal the business declared is carried out here or owned by someone else
      - id: DISCHARGE_UNDECLARED_REFUSAL
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/66
        check: ROWS_CONFINED_TO_PRIOR
        register: refusal_discharge
        params:
          prior_phase: p0
          prior_register: operation_refusals
          prior_key_column:
          - Operation
          - Refused When
          key_column:
          - Operation
          - Refused When
        intent: a discharge answers a refusal the business declared, never one the design invented
      - id: DEFERRAL_UNDECLARED_REFUSAL
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/67
        check: ROWS_CONFINED_TO_PRIOR
        register: refusal_deferrals
        params:
          prior_phase: p0
          prior_register: operation_refusals
          prior_key_column:
          - Operation
          - Refused When
          key_column:
          - Operation
          - Refused When
        intent: a deferral hands on a refusal the business declared, never one nobody approved
      - id: DEFERRAL_OWNER_UNNAMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/68
        check: CELL_NOT_EMPTY
        register: refusal_deferrals
        params:
          column: Deferred To
          detail: names no owner — a refusal handed on to nobody is a refusal dropped in language that
            sounds like a plan
        intent: a deferred refusal names who will carry it out
      - id: GOVERNANCE_DISCHARGE_UNDECLARED_REFUSAL
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/69
        check: ROWS_CONFINED_TO_PRIOR
        register: refusal_governance_discharge
        params:
          prior_phase: p0
          prior_register: operation_refusals
          prior_key_column:
          - Operation
          - Refused When
          key_column:
          - Operation
          - Refused When
        intent: the governance surface is cited for a refusal the business declared, never for one it
          did not
      - id: GOVERNING_RULE_PHASE_MALFORMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/70
        check: CELL_MATCHES
        register: refusal_governance_discharge
        params:
          column: Phase
          pattern: ^p[0-8]$
          detail: '{value!r} is not a phase — a rule is named by its phase and its identifier together,
            written p0 through p8, because an identifier alone names nine rules'
        intent: a cited rule is located in the phase whose rule set holds it
      - id: GOVERNING_RULE_UNNAMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/71
        check: CELL_NOT_EMPTY
        register: refusal_governance_discharge
        params:
          column: Governing Rule
          detail: cites no rule — a refusal said to be carried out by the governance surface and naming
            nothing there is prose, and prose refuses nothing
        intent: a governance-surface discharge names the rule that refuses
      - id: GOVERNING_RULE_NOT_IN_FORCE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/72
        check: GOVERNING_RULE_IN_SEALED_SET
        register: refusal_governance_discharge
        params:
          observation: si.rule_set.list
          phase_workflows:
            p0: WF_P0_SEED_ADMISSIBILITY
            p1: WF_P1_CHANGE_REQUEST_ADMISSIBILITY
            p2: WF_P2_DOMAIN_MODEL_ADMISSIBILITY
            p3: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY
            p4: WF_P4_BUSINESS_MODEL_ADMISSIBILITY
            p5: WF_P5_BUSINESS_INTENT_ADMISSIBILITY
            p6: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY
            p7: WF_P7_DESIGN_INTENT_ADMISSIBILITY
            p8: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY
        intent: a rule said to carry out a refusal is really in force where the design is pinned
      - id: DISCHARGE_NOT_IN_TOPOLOGY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/73
        check: DISCHARGE_GROUNDED_IN_TOPOLOGY
        register: refusal_discharge
        intent: a discharge names a step the act has and an outcome that step reports
      - id: DISCHARGE_DOES_NOT_REFUSE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/74
        check: DISCHARGE_OUTCOME_REFUSES
        register: refusal_discharge
        intent: the outcome a discharge names stops the act rather than continuing it
      - id: EMISSION_NOT_FROM_COMPLETING_ENDING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/75
        check: EMISSION_GROUNDED_IN_ENDING
        register: artifact_properties
        params:
          property_prefix: emit.
          refusal_property: moment
          refusal_value: refusal
        intent: a moment is announced from an ending the act has, and one that completes it — or, for
          a moment declared a refusal, one that refuses it
      - id: EMITTED_EVENT_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/76
        check: CELL_RESOLVES_IN_REGISTER
        register: artifact_properties
        params:
          column: Value
          only_when_column: Property
          only_when_prefix: emit.
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
          detail: an announced moment must be an identity this design declares
        intent: an act announces a moment that exists, never one nothing declares
      - id: MOLECULE_WITHOUT_STEPS
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/77
        check: REGISTER_COVERS_REGISTER
        register: molecule_steps
        params:
          source_register: implementation_bindings
          source_column: CT Code
          column: CT Code
          only_when_column: Kind
          only_when_value: molecule
        intent: a molecule with no declared steps specifies nothing to run
      - id: MOLECULE_STEP_OWNER_NOT_MOLECULE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/78
        check: CELL_RESOLVES_IN_REGISTER
        register: molecule_steps
        params:
          column: CT Code
          target_register: implementation_bindings
          target_column: CT Code
          target_only_when_column: Kind
          target_only_when_value: molecule
          detail: steps belong to a transform this design declares a molecule
        intent: only a molecule has steps
      - id: MOLECULE_STEP_KIND_UNKNOWN
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/79
        check: CELL_MATCHES
        register: molecule_steps
        params:
          column: Kind
          pattern: ^(atom|molecule|loop)$
          detail: step kind is {value!r}; a step runs an atom, a molecule once, or a molecule once per
            member of a collection, and the compiler lowers nothing else
        intent: a step is one of the three the compiler lowers
      - id: MOLECULE_STEP_WITHOUT_KIND
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/80
        check: CELL_NOT_EMPTY
        register: molecule_steps
        params:
          column: Kind
          detail: step declares no kind — construction would have to choose how it runs
        intent: every step says how it runs
      - id: MOLECULE_STEP_TARGET_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/81
        check: CELL_RESOLVES_IN_REGISTER
        register: molecule_steps
        params:
          column: Target
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
          detail: a step runs a transform this design declares or carries over
        intent: a step runs something that exists
      - id: MOLECULE_STEP_WITHOUT_TARGET
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/82
        check: CELL_NOT_EMPTY
        register: molecule_steps
        params:
          column: Target
          detail: step runs nothing — construction would have to choose what
        intent: every step names the transform it runs
      - id: MOLECULE_STEP_UNNAMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/83
        check: CELL_NOT_EMPTY
        register: molecule_steps
        params:
          column: Step
          detail: step has no symbol — a result nothing can name is a result no later step can read
        intent: every step's result has a name later steps read it by
      - id: LOOP_WITHOUT_COLLECTION
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/84
        check: CELL_NOT_EMPTY
        register: molecule_steps
        params:
          column: Over
          only_when_column: Kind
          only_when_value: loop
          detail: loop names no collection — its passes would have no stated bound
        intent: a loop runs once per member of a collection the composition can see
      - id: LOOP_COLLECTION_UNROOTED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/85
        check: CELL_MATCHES
        register: molecule_steps
        params:
          column: Over
          pattern: ^inputs\.[A-Za-z_][A-Za-z0-9_.]*$
          only_when_column: Kind
          only_when_value: loop
          detail: loop runs over {value!r}; a loop's collection is a field the molecule is handed, inputs.<field>,
            so its length is fixed before the first pass and never by one
        intent: a loop's length never depends on the data it computes
      - id: LOOP_WITHOUT_ITERATOR
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/86
        check: CELL_NOT_EMPTY
        register: molecule_steps
        params:
          column: Iterator
          only_when_column: Kind
          only_when_value: loop
          detail: loop names no iterator — its body is handed a member under no name
        intent: a loop's body receives each member under a declared name
      - id: LOOP_FIELDS_OUTSIDE_LOOP
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/87
        check: CELL_MATCHES
        register: molecule_steps
        params:
          column: Over
          pattern: ^(?:—|-)$
          only_when_column: Kind
          only_when_values:
          - atom
          - molecule
          detail: a step that is not a loop names collection {value!r}, which nothing reads
        intent: a collection is stated where it bounds something
      - id: MOLECULE_WITHOUT_EMISSION
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/88
        check: REGISTER_COVERS_REGISTER
        register: molecule_steps
        params:
          source_register: implementation_bindings
          source_column: CT Code
          column: CT Code
          only_when_column: Kind
          only_when_value: molecule
          covered_present_column: Emits
        intent: a molecule yields a value, and says which step it comes from
      - id: MOLECULE_EMITS_TWICE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/89
        check: COLUMN_VALUES_UNIQUE
        register: molecule_steps
        params:
          column: CT Code
          only_when_present_column: Emits
          detail: '{value} emits a second value, first at row {first} — a molecule yields exactly one,
            and two leave a caller to guess which it was handed'
        intent: a molecule yields exactly one value
      - id: MOLECULE_BINDING_STEP_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/90
        check: CELL_RESOLVES_IN_REGISTER
        register: molecule_step_bindings
        params:
          column: Step
          target_register: molecule_steps
          target_column: Step
          detail: a binding belongs to a step this design declares
        intent: a binding hands a value to a step that exists
      - id: MOLECULE_BINDING_WITHOUT_SOURCE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/91
        check: CELL_NOT_EMPTY
        register: molecule_step_bindings
        params:
          column: Bound To
          detail: field is bound to nothing — construction would have to choose a source
        intent: every molecule binding names where its value comes from
      - id: MOLECULE_BINDING_SOURCE_MALFORMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/92
        check: CELL_MATCHES
        register: molecule_step_bindings
        params:
          column: Bound To
          pattern: ^(?:inputs\.[A-Za-z_][A-Za-z0-9_.]*|results\.[A-Za-z_][A-Za-z0-9_.]*|iterator|accumulator\.[A-Za-z_][A-Za-z0-9_.]*|[\[{].*[\]}]|"[^"]*"|'[^']*'|-?[0-9]+(?:\.[0-9]+)?|[A-Za-z_][A-Za-z0-9_]*::[A-Za-z_][A-Za-z0-9_]*|[A-Za-z_][A-Za-z0-9_-]*)$
          detail: source is {value!r}; a molecule binding reads inputs.<field>, results.<step>.<field>,
            iterator, accumulator.<field>, or is a literal
        intent: a reference the runtime cannot resolve is indistinguishable from one it can
      - id: LOOP_UPDATE_NOT_FROM_RESULT
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/93
        check: CELL_MATCHES
        register: molecule_step_bindings
        params:
          column: Bound To
          pattern: ^results\.[A-Za-z_][A-Za-z0-9_.]*$
          only_when_column: Role
          only_when_value: UPDATE
          detail: a carried value is updated from {value!r}; it is taken from what the pass produced,
            results.<field>, or the loop carries forward something no pass computed
        intent: what a loop carries forward is what each pass produced
      - id: WITHDRAWAL_IS_A_CHANGE_OF_MEANING
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/94
        check: TABLE_ROW_COUNT
        register: withdrawn_facts
        params:
          maximum: 0
          detail: a withdrawal changes what an artifact means — author its successor and REPLACE it instead
        intent: an amendment withdraws nothing; a change of meaning is a new identity
      - id: TRANSFORM_WITHOUT_VECTOR
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/95
        check: REGISTER_COVERS_REGISTER
        register: test_cases
        params:
          source_register: new_artifacts
          source_column: Code
          column: CT Code
          only_when_column: Family
          only_when_value: CT
        intent: a transform authored here enters the composition with its proof
      - id: AMENDED_TRANSFORM_WITHOUT_VECTOR
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/96
        check: REGISTER_COVERS_REGISTER
        register: test_cases
        params:
          source_register: existing_inventory
          source_column: FQDN
          column: CT Code
          only_when_column: Action
          only_when_value: EXTEND
          only_when_source_pattern: ^CT_
        intent: a transform this change amends is proven as it will be
      - id: TEST_CASE_TRANSFORM_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/97
        check: CELL_RESOLVES_IN_REGISTER
        register: test_cases
        params:
          column: CT Code
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
          detail: a case proves a transform this design declares or carries over
        intent: a case tests something that exists
      - id: TEST_CASE_UNNAMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/98
        check: CELL_NOT_EMPTY
        register: test_cases
        params:
          column: Case
          detail: case has no name — a failure nothing can name is one nobody can find
        intent: every case is named
      - id: TEST_CASE_NAME_MALFORMED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/99
        check: CELL_MATCHES
        register: test_cases
        params:
          column: Case
          pattern: ^[a-z][a-z0-9_]*$
          detail: case is named {value!r}; a case is named in lower case, words joined by underscores
        intent: a case name is a stable identifier
      - id: TEST_VALUE_CASE_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/100
        check: CELL_RESOLVES_IN_REGISTER
        register: test_case_values
        params:
          column: Case
          target_register: test_cases
          target_column: Case
          detail: a value belongs to a case this design declares
        intent: a value is handed to, or expected of, a case that exists
      - id: TEST_VALUE_WITHOUT_FIELD
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/101
        check: CELL_NOT_EMPTY
        register: test_case_values
        params:
          column: Field
          detail: value names no field — construction would have to choose one
        intent: every value names the field it is for
      - id: TEST_VALUE_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/102
        check: CELL_PRESENT
        register: test_case_values
        params:
          column: Value
          detail: value is not stated — write the literal; "" is the empty string and null is null
        intent: every value is stated
      - id: EVENT_CODE_NOT_PAST_PARTICIPLE
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/103
        check: CELL_MATCHES
        register: new_artifacts
        params:
          column: Code
          pattern: ^(?:[a-z][a-z0-9_.]*::)?EV_[A-Z0-9_]+ED_V\d+$
          only_when_column: Family
          only_when_value: EV
          detail: '{value!r} does not name a moment that has happened — an event code reads EV_<subject>_<participle>,
            as EV_ACTOR_REGISTERED_V0 does'
        intent: an event names an occurrence, and a code in the imperative names an operation
      - id: REGISTER_CELL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/104
        check: UNRESOLVED_MARKER_ABSENT
        params:
          exempt: []
          detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask
            it as a clarification, do not hedge it in a register'
        intent: an unanswered question left in a register reads as decided to every later phase
      - id: FIELD_STRUCTURE_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/105
        check: CELL_RESOLVES_IN_REGISTER
        register: interface_fields
        params:
          column: Structure
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
        intent: a field's structure names a STRUCTURE this design declares or carries over
      - id: WORKFLOW_ACTOR_UNDECLARED
        identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/106
        check: CELL_RESOLVES_IN_REGISTER
        register: artifact_properties
        params:
          column: Value
          only_when_column: Property
          only_when_value: actor_context
          target_registers:
          - new_artifacts
          - existing_inventory
          target_column: Code
          target_columns:
          - Code
          - FQDN
        intent: the actor a workflow runs as is one this design declares or carries over
  - owner: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: document_text
    bound_to: payload.register_text
  - owner: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: prior_texts
    bound_to: payload.prior_texts
  - owner: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    step: CC_JUDGE_AGAINST_SNAPSHOT_V1
    direction: INPUT
    field: rule_set
    bound_to:
      literal:
      - id: HEADER_FIELD_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/document/required
        check: HEADER_FIELD_PRESENT
        params:
          fields:
          - phase
          - domain
          - subdomain
          - cr
          - rule_set
        intent: a phase document states its phase, its domain and subdomain, its change, and the rule
          set it was authored under
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/document/properties/phase/const
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - phase
          pattern: ^p8$
        intent: a document's phase is the phase whose rules judge it
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/document/properties/domain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: domain
          type:
            type: string
            minLength: 1
        intent: a document's domain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/document/properties/subdomain
        check: HEADER_FIELD_OF_TYPE
        params:
          field: subdomain
          type:
            type:
            - string
            - array
            items:
              type: string
            minLength: 1
            minItems: 1
        intent: a document's subdomain takes its declared form
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/document/properties/cr
        check: HEADER_FIELD_OF_TYPE
        params:
          field: cr
          type:
            type: string
            minLength: 1
        intent: a document's cr takes its declared form
      - id: HEADER_FIELD_MISMATCH
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/document/properties/rule_set/pattern
        check: HEADER_FIELD_MATCHES
        params:
          fields:
          - rule_set
          pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P8_V[0-9]+$
        intent: a document's rule_set names a rule set of its own phase
      - id: HEADER_FIELD_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/document/properties/approval
        check: HEADER_FIELD_OF_TYPE
        params:
          field: approval
          type:
            type: object
            required:
            - gate
            - rule_set
            - state
            additionalProperties: false
            properties:
              gate:
                type: string
                minLength: 1
              rule_set:
                type: string
                pattern: ^transformation\.schemas\.REGISTER_SCHEMA_P8_V[0-9]+$
              state:
                enum:
                - APPROVED
                - MIGRATED
                - RECONFIRMED
        intent: a document's approval takes its declared form
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/build_order/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: build_order
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/build_order/items/required
        check: TABLE_HAS_COLUMNS
        register: build_order
        params:
          columns:
          - Wave
          - Step
          - Code
          - Action
          - Subdomain
          - Depends On
        intent: downstream phases read these columns by name
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/build_order/items/properties/action/x-vocab
        check: CELL_IN_VOCABULARY
        register: build_order
        params:
          column: Action
          vocabulary:
          - REPLACE
          - EXTEND
          - NEW
        intent: Action is a controlled vocabulary declared by the template
      - id: CELL_NOT_OF_TYPE
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/build_order/items/properties/depends_on/x-derived/CELL_OF_TYPE
        check: CELL_OF_TYPE
        register: build_order
        params:
          column: Depends On
          type:
            type:
            - array
            - 'null'
            items:
              type: string
        intent: Depends On carries structure, and its value must take the declared form
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/critical_path/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: critical_path
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/critical_path/items/required
        check: TABLE_HAS_COLUMNS
        register: critical_path
        params:
          columns:
          - Position
          - Code
        intent: downstream phases read these columns by name
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/mandate_artifact_summary/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: mandate_artifact_summary
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/mandate_artifact_summary/items/required
        check: TABLE_HAS_COLUMNS
        register: mandate_artifact_summary
        params:
          columns:
          - Action
          - Count
          - Description
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/mandate_artifact_summary/minItems
        check: TABLE_HAS_ROWS
        register: mandate_artifact_summary
        intent: an empty required register asserts nothing
      - id: CELL_NOT_IN_VOCABULARY
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/mandate_artifact_summary/items/properties/action/x-vocab
        check: CELL_IN_VOCABULARY
        register: mandate_artifact_summary
        params:
          column: Action
          vocabulary:
          - REPLACE
          - EXTEND
          - NEW
        intent: Action is a controlled vocabulary declared by the template
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/field_declarations/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: field_declarations
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/field_declarations/items/required
        check: TABLE_HAS_COLUMNS
        register: field_declarations
        params:
          columns:
          - Code
          - Subdomain Field
        intent: downstream phases read these columns by name
      - id: REGISTER_EMPTY
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/field_declarations/minItems
        check: TABLE_HAS_ROWS
        register: field_declarations
        intent: an empty required register asserts nothing
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/new_capabilities/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: new_capabilities
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/new_capabilities/items/required
        check: TABLE_HAS_COLUMNS
        register: new_capabilities
        params:
          columns:
          - Code
          - Purpose
          - Inputs
          - Outputs
        intent: downstream phases read these columns by name
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/new_intents/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: new_intents
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/new_intents/items/required
        check: TABLE_HAS_COLUMNS
        register: new_intents
        params:
          columns:
          - Code
          - Purpose
          - Workflow
          - Inputs
        intent: downstream phases read these columns by name
      - id: REGISTER_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/cross_subdomain_notes/x-derived/TABLE_PRESENT
        check: TABLE_PRESENT
        register: cross_subdomain_notes
        intent: a declared register must be present and readable as rows
      - id: REGISTER_COLUMN_MISSING
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/properties/registers/properties/cross_subdomain_notes/items/required
        check: TABLE_HAS_COLUMNS
        register: cross_subdomain_notes
        params:
          columns:
          - Code
          - Note
        intent: downstream phases read these columns by name
      - id: BUILD_STEPS_NOT_CONTIGUOUS
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/0
        check: COLUMN_SEQUENCE_CONTIGUOUS
        register: build_order
        params:
          column: Step
          start: 1
        intent: the build sequence is total and gapless, because a gap is a dropped artifact
      - id: DEPENDENCY_SCHEDULED_LATER
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/1
        check: DEPENDENCY_PRECEDES
        register: build_order
        params:
          column: Code
          depends_column: Depends On
          order_column: Step
        intent: everything a step depends on is built before it — this is what makes it a sort
      - id: BUILD_CODE_MALFORMED
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/2
        check: CELL_MATCHES
        register: build_order
        params:
          column: Code
          pattern: ^[a-z][a-z0-9_.]*::(?:STRUCTURE|TEST_DATA|VOCAB|AC|IN|WF|CC|CT|CS|RB|EV|TI|TE)_[A-Z0-9_]+_V\d+$
          detail: build code {value!r} must be a binding FQDN copied verbatim from Stage 7
        intent: a mandate orders binding identities, never re-typed approximations
      - id: BUILD_CODE_ALREADY_EXISTS
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/3
        check: CITED_ARTIFACTS_ABSENT
        register: build_order
        params:
          column: Code
          pattern: '[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+'
          observation: si.artifact.list
        intent: an artifact mandated for authoring must not already be in the composition
      - id: CRITICAL_PATH_NOT_IN_BUILD_ORDER
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/4
        check: CELL_RESOLVES_IN_REGISTER
        register: critical_path
        params:
          column: Code
          target_register: build_order
          target_column: Code
          detail: the critical path runs through steps the mandate schedules, not past them
        intent: the critical path is a path through this build order
      - id: CRITICAL_PATH_NOT_CONTIGUOUS
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/5
        check: COLUMN_SEQUENCE_CONTIGUOUS
        register: critical_path
        params:
          column: Position
          start: 1
        intent: a path is an ordered chain, not an unordered set of steps
      - id: CAPABILITY_WITHOUT_PURPOSE
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/6
        check: CELL_NOT_EMPTY
        register: new_capabilities
        params:
          column: Purpose
          detail: capability states no purpose — a builder needs to know what to build, not only its name
        intent: a mandated capability says what it is for
      - id: INTENT_WITHOUT_WORKFLOW
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/7
        check: CELL_NOT_EMPTY
        register: new_intents
        params:
          column: Workflow
          detail: intent names no workflow — an entry point that starts nothing cannot be authored
        intent: every mandated intent names the workflow it starts
      - id: DESIGNED_ARTIFACT_NOT_SCHEDULED
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/8
        check: PRIOR_IDENTITIES_COVERED
        register: build_order
        params:
          prior_phase: p7
          prior_register: new_artifacts
          prior_column: Code
          column: Code
          require: prior_in_here
        intent: an artifact the design declared and the mandate never schedules is not deferred, it is
          lost
      - id: SCHEDULED_ARTIFACT_NOT_DESIGNED
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/9
        check: PRIOR_IDENTITIES_COVERED
        register: build_order
        params:
          prior_phase: p7
          prior_register: new_artifacts
          prior_column: Code
          column: Code
          require: here_in_prior
        intent: a mandate orders the build; it does not get to add to it
      - id: SCHEDULED_ARTIFACT_UNPLACED
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/10
        check: REGISTER_COVERS_REGISTER
        register: field_declarations
        params:
          source_register: build_order
          source_column: Code
          column: Code
        intent: every artifact the mandate schedules declares the subdomain it is built into
      - id: AMENDED_ARTIFACT_UNPLACED
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/11
        check: PRIOR_IDENTITIES_COVERED
        register: field_declarations
        params:
          prior_phase: p7
          prior_register: existing_inventory
          prior_column: FQDN
          column: Code
          require: prior_in_here
          match_on: bare_code
          prior_only_when_column: Action
          prior_only_when_values:
          - EXTEND
          prior_only_when_prefixes:
          - AC_
          - IN_
          - WF_
          - CC_
          - CT_
          - EV_
          - RB_
          - VOCAB_
          - TI_
          - TE_
        intent: an artifact this change amends declares the subdomain it is placed in, as a scheduled
          one does
      - id: REGISTER_CELL_UNRESOLVED
        identity: transformation.schemas.REGISTER_SCHEMA_P8_V0#/allOf/12
        check: UNRESOLVED_MARKER_ABSENT
        params:
          exempt: []
          detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask
            it as a clarification, do not hedge it in a register'
        intent: an unanswered question left in a register reads as decided to every later phase
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
    default: null
    meaning: role
  - artifact: transformation::AC_REGISTER_AUTHOR_V0
    direction: ATTRIBUTE
    field: role
    type: string
    required: 'YES'
    default: null
    meaning: role
  - artifact: transformation::AC_SEED_AUTHOR_V0
    direction: ATTRIBUTE
    field: role
    type: string
    required: 'YES'
    default: null
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
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    callable: execute
    operation: PURE_MEASURE_COMPLETENESS
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    callable: execute
    operation: PURE_RENDER_ARTIFACTS
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    callable: execute
    operation: PURE_EVALUATE_RULES
    kind: atom
    purity: ct_pure
    refusal: returns
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    callable: execute
    operation: PURE_PARSE_PRIOR_PHASES
    kind: atom
    purity: ct_pure
    refusal: never
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    callable: execute
    operation: PURE_PARSE_REGISTERS
    kind: atom
    purity: ct_pure
    refusal: never
  vocabulary_extensions:
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: stated_by_design
    meaning: stated_by_design
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: governed_elsewhere
    meaning: governed_elsewhere
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: carried_from_predecessor
    meaning: carried_from_predecessor
  - vocabulary_code: transformation::VOCAB_FACT_PROVENANCE_V0
    extends: null
    group: fact_provenance
    casing: lower_snake
    value: supplied_by_renderer
    meaning: supplied_by_renderer
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: AC
    meaning: AC
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: IN
    meaning: IN
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: WF
    meaning: WF
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: CC
    meaning: CC
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: CT
    meaning: CT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: EV
    meaning: EV
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: RB
    meaning: RB
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: VOCAB
    meaning: VOCAB
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: STRUCTURE
    meaning: STRUCTURE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: TI
    meaning: TI
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: artifact_family
    casing: UPPER_SNAKE
    value: TE
    meaning: TE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: approval_state
    casing: UPPER_SNAKE
    value: APPROVED
    meaning: APPROVED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: approval_state
    casing: UPPER_SNAKE
    value: MIGRATED
    meaning: MIGRATED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: approval_state
    casing: UPPER_SNAKE
    value: RECONFIRMED
    meaning: RECONFIRMED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: belief_result
    casing: UPPER_SNAKE
    value: VERIFIED
    meaning: VERIFIED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: belief_result
    casing: UPPER_SNAKE
    value: NOT_FOUND
    meaning: NOT_FOUND
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: belief_result
    casing: UPPER_SNAKE
    value: INSUFFICIENT_EVIDENCE
    meaning: INSUFFICIENT_EVIDENCE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: certainty
    casing: UPPER_SNAKE
    value: HIGH
    meaning: HIGH
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: certainty
    casing: UPPER_SNAKE
    value: MEDIUM
    meaning: MEDIUM
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: certainty
    casing: UPPER_SNAKE
    value: LOW
    meaning: LOW
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: clarification_owner
    casing: UPPER_SNAKE
    value: HUMAN
    meaning: HUMAN
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: clarification_owner
    casing: UPPER_SNAKE
    value: SNAPSHOT
    meaning: SNAPSHOT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: clarification_owner
    casing: UPPER_SNAKE
    value: GOVERNANCE
    meaning: GOVERNANCE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: classification
    casing: UPPER_SNAKE
    value: NEW_SUBDOMAIN
    meaning: NEW_SUBDOMAIN
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: classification
    casing: UPPER_SNAKE
    value: EXTEND_SUBDOMAIN
    meaning: EXTEND_SUBDOMAIN
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: classification
    casing: UPPER_SNAKE
    value: MODIFY
    meaning: MODIFY
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: classification
    casing: UPPER_SNAKE
    value: DEPRECATE
    meaning: DEPRECATE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: composition_kind
    casing: UPPER_SNAKE
    value: CT
    meaning: CT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: composition_kind
    casing: UPPER_SNAKE
    value: CS
    meaning: CS
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: EXISTING
    meaning: EXISTING
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: REUSE
    meaning: REUSE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: AUTHOR_NEW
    meaning: AUTHOR_NEW
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_disposition
    casing: UPPER_SNAKE
    value: INVESTIGATE
    meaning: INVESTIGATE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_status
    casing: UPPER_SNAKE
    value: SATISFIED
    meaning: SATISFIED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: dependency_status
    casing: UPPER_SNAKE
    value: GAP
    meaning: GAP
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: evidence_status
    casing: UPPER_SNAKE
    value: OBSERVED
    meaning: OBSERVED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: evidence_status
    casing: UPPER_SNAKE
    value: INFERRED
    meaning: INFERRED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: evidence_status
    casing: UPPER_SNAKE
    value: OPEN
    meaning: OPEN
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: expected_outcome
    casing: UPPER_SNAKE
    value: SUCCESS
    meaning: SUCCESS
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: expected_outcome
    casing: UPPER_SNAKE
    value: VIOLATION
    meaning: VIOLATION
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: field_direction
    casing: UPPER_SNAKE
    value: INPUT
    meaning: INPUT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: field_direction
    casing: UPPER_SNAKE
    value: OUTPUT
    meaning: OUTPUT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: fit
    casing: UPPER_SNAKE
    value: EXACT
    meaning: EXACT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: fit
    casing: UPPER_SNAKE
    value: PARTIAL
    meaning: PARTIAL
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: fit
    casing: UPPER_SNAKE
    value: MISMATCH
    meaning: MISMATCH
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: gap_resolution
    casing: UPPER_SNAKE
    value: REPLACE
    meaning: REPLACE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: gap_resolution
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: gap_resolution
    casing: UPPER_SNAKE
    value: NEW
    meaning: NEW
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: handler_kind
    casing: UPPER_SNAKE
    value: WF_INVOCATION
    meaning: WF_INVOCATION
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: handler_kind
    casing: UPPER_SNAKE
    value: SNAPSHOT_READ
    meaning: SNAPSHOT_READ
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: interface_direction
    casing: UPPER_SNAKE
    value: INPUT
    meaning: INPUT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: interface_direction
    casing: UPPER_SNAKE
    value: OUTPUT
    meaning: OUTPUT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: interface_direction
    casing: UPPER_SNAKE
    value: ATTRIBUTE
    meaning: ATTRIBUTE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: REPLACE
    meaning: REPLACE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: REUSE
    meaning: REUSE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: REPOINT
    meaning: REPOINT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: inventory_action
    casing: UPPER_SNAKE
    value: REVIEW
    meaning: REVIEW
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: molecule_binding_role
    casing: UPPER_SNAKE
    value: INPUT
    meaning: INPUT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: molecule_binding_role
    casing: UPPER_SNAKE
    value: CARRY
    meaning: CARRY
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: molecule_binding_role
    casing: UPPER_SNAKE
    value: UPDATE
    meaning: UPDATE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: node_type
    casing: UPPER_SNAKE
    value: IN
    meaning: IN
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: node_type
    casing: UPPER_SNAKE
    value: CC
    meaning: CC
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: node_type
    casing: UPPER_SNAKE
    value: EXIT
    meaning: EXIT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: node_type
    casing: UPPER_SNAKE
    value: EXIT_SUCCESS
    meaning: EXIT_SUCCESS
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: ownership_disposition
    casing: UPPER_SNAKE
    value: OWNED
    meaning: OWNED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: ownership_disposition
    casing: UPPER_SNAKE
    value: SATISFIED
    meaning: SATISFIED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: ownership_disposition
    casing: UPPER_SNAKE
    value: DEFERRED
    meaning: DEFERRED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: placement_decision
    casing: UPPER_SNAKE
    value: NEW_SUBDOMAIN
    meaning: NEW_SUBDOMAIN
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: placement_decision
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: pps_action
    casing: UPPER_SNAKE
    value: REPLACE
    meaning: REPLACE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: pps_action
    casing: UPPER_SNAKE
    value: REVIEW
    meaning: REVIEW
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: pps_action
    casing: UPPER_SNAKE
    value: REUSE
    meaning: REUSE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: pps_action
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: purpose_disposition
    casing: UPPER_SNAKE
    value: INHERITED
    meaning: INHERITED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: purpose_disposition
    casing: UPPER_SNAKE
    value: REFINED
    meaning: REFINED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: record_model
    casing: UPPER_SNAKE
    value: MUTABLE_STATE
    meaning: MUTABLE_STATE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: record_model
    casing: UPPER_SNAKE
    value: APPEND_ONLY_JOURNAL
    meaning: APPEND_ONLY_JOURNAL
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: record_model
    casing: UPPER_SNAKE
    value: IDENTITY_REGISTRY
    meaning: IDENTITY_REGISTRY
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: record_model
    casing: UPPER_SNAKE
    value: HYBRID
    meaning: HYBRID
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: resolution_status
    casing: UPPER_SNAKE
    value: CLOSED
    meaning: CLOSED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: resolution_status
    casing: UPPER_SNAKE
    value: OPEN
    meaning: OPEN
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: reuse_decision
    casing: UPPER_SNAKE
    value: REUSE
    meaning: REUSE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: reuse_decision
    casing: UPPER_SNAKE
    value: EXTEND
    meaning: EXTEND
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: reuse_decision
    casing: UPPER_SNAKE
    value: AUTHOR_NEW
    meaning: AUTHOR_NEW
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: saturation_status
    casing: UPPER_SNAKE
    value: SATISFIED
    meaning: SATISFIED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: saturation_status
    casing: UPPER_SNAKE
    value: NOT_SATISFIED
    meaning: NOT_SATISFIED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: CREATED
    meaning: CREATED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: EXTENDED
    meaning: EXTENDED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: MODIFIED
    meaning: MODIFIED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: DEPRECATED
    meaning: DEPRECATED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_relationship
    casing: UPPER_SNAKE
    value: ADJACENT
    meaning: ADJACENT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_status
    casing: UPPER_SNAKE
    value: IN_SCOPE
    meaning: IN_SCOPE
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: scope_status
    casing: UPPER_SNAKE
    value: DEFERRED
    meaning: DEFERRED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: storage_type
    casing: UPPER_SNAKE
    value: CS_APPENDONLY_JSONL_V0
    meaning: CS_APPENDONLY_JSONL_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: storage_type
    casing: UPPER_SNAKE
    value: CS_MUTABLE_JSON_V0
    meaning: CS_MUTABLE_JSON_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: storage_type
    casing: UPPER_SNAKE
    value: CS_REGISTRY_V0
    meaning: CS_REGISTRY_V0
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: test_value_role
    casing: UPPER_SNAKE
    value: INPUT
    meaning: INPUT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: test_value_role
    casing: UPPER_SNAKE
    value: EXPECTED
    meaning: EXPECTED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: test_value_role
    casing: UPPER_SNAKE
    value: ASSERT
    meaning: ASSERT
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: test_value_role
    casing: UPPER_SNAKE
    value: RECORDED
    meaning: RECORDED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: transport_direction
    casing: UPPER_SNAKE
    value: INGRESS
    meaning: INGRESS
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: transport_direction
    casing: UPPER_SNAKE
    value: EGRESS
    meaning: EGRESS
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: verification_result
    casing: UPPER_SNAKE
    value: CONFIRMED
    meaning: CONFIRMED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: verification_result
    casing: UPPER_SNAKE
    value: OVERTURNED
    meaning: OVERTURNED
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: yes_no
    casing: UPPER_SNAKE
    value: 'YES'
    meaning: 'YES'
  - vocabulary_code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    extends: null
    group: yes_no
    casing: UPPER_SNAKE
    value: 'NO'
    meaning: 'NO'
  runtime_policies:
  - rb_code: transformation::RB_CONSTRUCTION_BINDINGS_V0
    capability: capability_side_effects::CS_TEXT_ARTIFACT_V0
    key: root
    value: '{{module_data_root}}/construction'
  - rb_code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    capability: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    key: snapshot_root
    value: '{{snapshot_root}}'
  artifact_properties:
  - artifact: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    property: supersedes
    value:
    - transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
  - artifact: transformation::RB_CONSTRUCTION_BINDINGS_V0
    property: parameters
    value:
    - module_data_root
  - artifact: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
  - artifact: transformation::AC_GATE_REVIEWER_V0
    property: description
    value: The human who accepts or declines a seed at Gate 0 after a verdict is reached.
  - artifact: transformation::AC_GATE_REVIEWER_V0
    property: type
    value: human
  - artifact: transformation::AC_REGISTER_AUTHOR_V0
    property: description
    value: The human accountable for the content of a register offered to a dossier phase.
  - artifact: transformation::AC_REGISTER_AUTHOR_V0
    property: type
    value: human
  - artifact: transformation::AC_SEED_AUTHOR_V0
    property: description
    value: The human accountable for the content of a seed offered to the seed phase.
  - artifact: transformation::AC_SEED_AUTHOR_V0
    property: type
    value: human
  - artifact: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    property: supersedes
    value:
    - transformation::CC_JUDGE_AGAINST_COMPOSITION_V0
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    property: supersedes
    value:
    - transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
  - artifact: transformation::CT_PURE_EVALUATE_RULES_V1
    property: supersedes
    value:
    - transformation::CT_PURE_EVALUATE_RULES_V0
  - artifact: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    property: supersedes
    value:
    - transformation::CT_PURE_PARSE_PRIOR_PHASES_V0
  - artifact: transformation::CT_PURE_PARSE_REGISTERS_V1
    property: supersedes
    value:
    - transformation::CT_PURE_PARSE_REGISTERS_V0
  - artifact: transformation::IN_BUSINESS_INTENT_SUBMITTED_V1
    property: supersedes
    value:
    - transformation::IN_BUSINESS_INTENT_SUBMITTED_V0
  - artifact: transformation::RB_TRANSFORMATION_BINDINGS_V0
    property: parameters
    value:
    - snapshot_root
  - artifact: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    property: supersedes
    value:
    - transformation::WF_P0_SEED_ADMISSIBILITY_V0
  - artifact: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    property: actor_context
    value: transformation::AC_SEED_AUTHOR_V0
  - artifact: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    property: supersedes
    value:
    - transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
  - artifact: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
  - artifact: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    property: supersedes
    value:
    - transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V1
  - artifact: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
  - artifact: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    property: supersedes
    value:
    - transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V1
  - artifact: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
  - artifact: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    property: supersedes
    value:
    - transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V1
  - artifact: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
  - artifact: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    property: supersedes
    value:
    - transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V1
  - artifact: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
  - artifact: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    property: supersedes
    value:
    - transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V1
  - artifact: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
  - artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    property: supersedes
    value:
    - transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
  - artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
  - artifact: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    property: supersedes
    value:
    - transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V1
  - artifact: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    property: actor_context
    value: transformation::AC_REGISTER_AUTHOR_V0
  - artifact: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
    property: supersedes
    value:
    - transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V0
  - artifact: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
    property: maximum
    value: 5
  - artifact: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1
    property: minimum
    value: 0
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
  structure_stores: []
  transport_bindings: []
  declared_reach: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    case: attributes_a_supplied_layer_to_the_renderer
    expected_outcome: SUCCESS
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    expected_outcome: SUCCESS
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_design_that_leaves_facts_undetermined
    expected_outcome: VIOLATION
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_value_its_provenance_attributes_to_the_renderer
    expected_outcome: VIOLATION
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    expected_outcome: SUCCESS
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: refuses_a_mandate_scheduling_nothing
    expected_outcome: VIOLATION
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    expected_outcome: SUCCESS
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    expected_outcome: SUCCESS
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_each_prior_by_phase
    expected_outcome: SUCCESS
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_no_prior_when_none_is_handed_over
    expected_outcome: SUCCESS
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    case: reads_header_registers_and_sections
    expected_outcome: SUCCESS
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
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    case: attributes_a_supplied_layer_to_the_renderer
    role: INPUT
    field: sources
    value:
      STRUCTURE_S_STORAGE_V0:
        core.layer:
        - supplied_by_renderer
        - ''
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
  - ct_code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1
    case: attributes_a_supplied_layer_to_the_renderer
    role: EXPECTED
    field: governing_artifacts
    value: {}
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
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: INPUT
    field: threshold
    value: 100.0
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: INPUT
    field: provenance
    value: {}
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: EXPECTED
    field: completeness
    value: 100.0
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: EXPECTED
    field: determined
    value: 10
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: EXPECTED
    field: required
    value: 10
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: admits_a_design_that_determines_its_artifact
    role: EXPECTED
    field: undetermined
    value: []
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
    - id: artifact_properties
      value:
      - artifact: STRUCTURE_S_STORAGE_V0
        property: layer
        value: DOMAINS
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
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_design_that_leaves_facts_undetermined
    role: INPUT
    field: threshold
    value: 100.0
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_design_that_leaves_facts_undetermined
    role: INPUT
    field: provenance
    value: {}
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
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_value_its_provenance_attributes_to_the_renderer
    role: INPUT
    field: threshold
    value: 100.0
  - ct_code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    case: refuses_a_value_its_provenance_attributes_to_the_renderer
    role: INPUT
    field: provenance
    value:
      AC_READER_V0.core.type: supplied_by_renderer
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
        governed_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0
        authority: pgc.platform
        concern: s
        core:
          summary: A reader of the catalog
          type: human
          attributes:
            role:
              type: string
              required: true
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    role: EXPECTED
    field: documents
    value:
    - path: registry/s/actors/AC_READER_V0.md
      text: "# AC_READER_V0\n\n## Machine\n\n```yaml\nfqdn: AC_READER_V0\nartifact_kind: ACTOR\nversion:\
        \ v0\ngoverned_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0\nauthority: pgc.platform\nconcern: s\n\
        core:\n  summary: A reader of the catalog\n  type: human\n  attributes:\n    role:\n      type:\
        \ string\n      required: true\n```\n\n---\n\n## Intent\n\nA reader of the catalog\n"
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    role: EXPECTED
    field: artifact_count
    value: 1
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: renders_the_actor_a_mandate_schedules
    role: EXPECTED
    field: sources
    value:
      AC_READER_V0: {}
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
  - ct_code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    case: refuses_a_mandate_scheduling_nothing
    role: INPUT
    field: mandate_registers
    value:
    - id: build_order
      value: []
    - id: field_declarations
      value: []
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
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: sections
    value:
    - number: 12
      title: Out of Scope
      text: '

        Nothing else.'
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
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: document_text
    value: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain: d\n  subdomain:\
      \ s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n  out_of_scope:\n\
      \  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n```\n\n## 12.\
      \ Out of Scope\n\nNothing else.\n"
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
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: observed
    value: {}
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: INPUT
    field: priors
    value: {}
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: EXPECTED
    field: verdict
    value: INADMISSIBLE
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
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: finds_an_absent_register
    role: EXPECTED
    field: rules_evaluated
    value: 1
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
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: sections
    value:
    - number: 12
      title: Out of Scope
      text: '

        Nothing else.'
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
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: document_text
    value: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain: d\n  subdomain:\
      \ s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n  out_of_scope:\n\
      \  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n```\n\n## 12.\
      \ Out of Scope\n\nNothing else.\n"
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
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: observed
    value: {}
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: INPUT
    field: priors
    value: {}
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: EXPECTED
    field: verdict
    value: ADMISSIBLE
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: EXPECTED
    field: findings
    value: []
  - ct_code: transformation::CT_PURE_EVALUATE_RULES_V1
    case: admits_a_present_register
    role: EXPECTED
    field: rules_evaluated
    value: 1
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_each_prior_by_phase
    role: INPUT
    field: prior_texts
    value:
      p0: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain: d\n  subdomain:\
        \ s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n  out_of_scope:\n\
        \  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n```\n\n##\
        \ 12. Out of Scope\n\nNothing else.\n"
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
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_no_prior_when_none_is_handed_over
    role: INPUT
    field: prior_texts
    value: {}
  - ct_code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V1
    case: reads_no_prior_when_none_is_handed_over
    role: EXPECTED
    field: priors
    value: {}
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    case: reads_header_registers_and_sections
    role: INPUT
    field: document_text
    value: "# Change Seed — d / s\n\n## Machine\n\n```yaml\ndocument:\n  phase: p0\n  domain: d\n  subdomain:\
      \ s\n  cr: c\n  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0\nregisters:\n  out_of_scope:\n\
      \  - item: Fines\n    reason: Not in this release.\n  clarification_requests: null\n```\n\n## 12.\
      \ Out of Scope\n\nNothing else.\n"
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
  - ct_code: transformation::CT_PURE_PARSE_REGISTERS_V1
    case: reads_header_registers_and_sections
    role: EXPECTED
    field: sections
    value:
    - number: 12
      title: Out of Scope
      text: '

        Nothing else.'
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
  generation_provenance:
  - artifact: transformation::CC_JUDGE_AGAINST_COMPOSITION_V1
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::WF_P0_SEED_ADMISSIBILITY_V1
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V1
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  - artifact: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
    generator: transformation.design.emit:emit_rule_sets
    generator_sources:
    - registry
  artifact_summary:
  - action: NEW
    subdomain: build
    count: '9'
    artifacts: transformation::CC_CONSTRUCT_ARTIFACTS_V0, transformation::CC_PERSIST_ARTIFACTS_V0, transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V1,
      transformation::CT_PURE_MEASURE_COMPLETENESS_V0, transformation::CT_PURE_RENDER_ARTIFACTS_V0, transformation::IN_CONSTRUCTION_REQUESTED_V0,
      transformation::RB_CONSTRUCTION_BINDINGS_V0, transformation::VOCAB_FACT_PROVENANCE_V0, transformation::WF_CONSTRUCT_ARTIFACTS_V0
  - action: NEW
    subdomain: design
    count: '29'
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
      transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V2
  - action: NEW
    subdomain: transformation
    count: '7'
    artifacts: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1, transformation::STRUCTURE_PHASE_FINDINGS_V0,
      transformation::STRUCTURE_PHASE_HEADER_V0, transformation::STRUCTURE_PHASE_PRIORS_V0, transformation::STRUCTURE_PHASE_REGISTERS_V0,
      transformation::STRUCTURE_PHASE_SECTIONS_V0, transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge: []
  withdrawn_facts: null
```

The design of record of `transformation`: every artifact its registry holds, stated in the design language.
Written by `python -m transformation.record` from the registry. Construction of this design and its
mandate reproduces the registry, and `construction_acceptance` asks whether it does. A change to
`transformation` is a dossier designed against the composition.
