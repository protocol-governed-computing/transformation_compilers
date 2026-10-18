# Authoring Mandate — transformation, baseline

## Machine

```yaml
document:
  phase: p8
  domain: transformation
  subdomain:
  - build
  - design
  - transformation
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V0
    action: NEW
    subdomain: transformation
    depends_on: null
  - wave: '1'
    step: '2'
    code: transformation::STRUCTURE_PHASE_FINDINGS_V0
    action: NEW
    subdomain: transformation
    depends_on: null
  - wave: '1'
    step: '3'
    code: transformation::STRUCTURE_PHASE_HEADER_V0
    action: NEW
    subdomain: transformation
    depends_on: null
  - wave: '1'
    step: '4'
    code: transformation::STRUCTURE_PHASE_PRIORS_V0
    action: NEW
    subdomain: transformation
    depends_on: null
  - wave: '1'
    step: '5'
    code: transformation::STRUCTURE_PHASE_REGISTERS_V0
    action: NEW
    subdomain: transformation
    depends_on: null
  - wave: '1'
    step: '6'
    code: transformation::STRUCTURE_PHASE_SECTIONS_V0
    action: NEW
    subdomain: transformation
    depends_on: null
  - wave: '1'
    step: '7'
    code: transformation::VOCAB_FACT_PROVENANCE_V0
    action: NEW
    subdomain: build
    depends_on: null
  - wave: '1'
    step: '8'
    code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '9'
    code: transformation::AC_GATE_REVIEWER_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '10'
    code: transformation::AC_REGISTER_AUTHOR_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '11'
    code: transformation::AC_SEED_AUTHOR_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '12'
    code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    action: NEW
    subdomain: build
    depends_on: null
  - wave: '1'
    step: '13'
    code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    action: NEW
    subdomain: build
    depends_on: null
  - wave: '1'
    step: '14'
    code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    action: NEW
    subdomain: build
    depends_on: null
  - wave: '1'
    step: '15'
    code: transformation::CC_PERSIST_ARTIFACTS_V0
    action: NEW
    subdomain: build
    depends_on: null
  - wave: '1'
    step: '16'
    code: transformation::IN_CONSTRUCTION_REQUESTED_V0
    action: NEW
    subdomain: build
    depends_on: null
  - wave: '1'
    step: '17'
    code: transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '18'
    code: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '19'
    code: transformation::IN_BUSINESS_INTENT_SUBMITTED_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '20'
    code: transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '21'
    code: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '22'
    code: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '23'
    code: transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '24'
    code: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '25'
    code: transformation::IN_SEED_SUBMITTED_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '1'
    step: '26'
    code: transformation::RB_CONSTRUCTION_BINDINGS_V0
    action: NEW
    subdomain: build
    depends_on: null
  - wave: '1'
    step: '27'
    code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    action: NEW
    subdomain: design
    depends_on: null
  - wave: '2'
    step: '28'
    code: transformation::CT_PURE_EVALUATE_RULES_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::STRUCTURE_PHASE_HEADER_V0
    - transformation::STRUCTURE_PHASE_SECTIONS_V0
    - transformation::STRUCTURE_PHASE_REGISTERS_V0
    - transformation::STRUCTURE_PHASE_PRIORS_V0
    - transformation::STRUCTURE_PHASE_FINDINGS_V0
  - wave: '2'
    step: '29'
    code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::STRUCTURE_PHASE_PRIORS_V0
  - wave: '2'
    step: '30'
    code: transformation::CT_PURE_PARSE_REGISTERS_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::STRUCTURE_PHASE_HEADER_V0
    - transformation::STRUCTURE_PHASE_SECTIONS_V0
    - transformation::STRUCTURE_PHASE_REGISTERS_V0
  - wave: '3'
    step: '31'
    code: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    action: NEW
    subdomain: build
    depends_on:
    - transformation::CT_PURE_PARSE_REGISTERS_V0
    - transformation::CT_PURE_RENDER_ARTIFACTS_V0
    - transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    - transformation::CT_PURE_MEASURE_COMPLETENESS_V0
  - wave: '3'
    step: '32'
    code: transformation::CC_JUDGE_AGAINST_COMPOSITION_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::CT_PURE_PARSE_REGISTERS_V0
    - transformation::CT_PURE_PARSE_PRIOR_PHASES_V0
    - transformation::CT_PURE_EVALUATE_RULES_V0
  - wave: '3'
    step: '33'
    code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::CT_PURE_PARSE_REGISTERS_V0
    - transformation::CT_PURE_PARSE_PRIOR_PHASES_V0
    - transformation::CT_PURE_EVALUATE_RULES_V0
  - wave: '3'
    step: '34'
    code: transformation::CC_JUDGE_DOCUMENT_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::CT_PURE_PARSE_REGISTERS_V0
    - transformation::CT_PURE_PARSE_PRIOR_PHASES_V0
    - transformation::CT_PURE_EVALUATE_RULES_V0
  - wave: '4'
    step: '35'
    code: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    action: NEW
    subdomain: build
    depends_on:
    - transformation::RB_CONSTRUCTION_BINDINGS_V0
    - transformation::AC_REGISTER_AUTHOR_V0
    - transformation::IN_CONSTRUCTION_REQUESTED_V0
    - transformation::CC_CONSTRUCT_ARTIFACTS_V0
    - transformation::CC_PERSIST_ARTIFACTS_V0
  - wave: '4'
    step: '36'
    code: transformation::WF_P0_SEED_ADMISSIBILITY_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::RB_TRANSFORMATION_BINDINGS_V0
    - transformation::AC_SEED_AUTHOR_V0
    - transformation::IN_SEED_SUBMITTED_V0
    - transformation::CC_JUDGE_DOCUMENT_V0
  - wave: '4'
    step: '37'
    code: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::RB_TRANSFORMATION_BINDINGS_V0
    - transformation::AC_REGISTER_AUTHOR_V0
    - transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    - transformation::CC_JUDGE_DOCUMENT_V0
  - wave: '4'
    step: '38'
    code: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::RB_TRANSFORMATION_BINDINGS_V0
    - transformation::AC_REGISTER_AUTHOR_V0
    - transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    - transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
  - wave: '4'
    step: '39'
    code: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::RB_TRANSFORMATION_BINDINGS_V0
    - transformation::AC_REGISTER_AUTHOR_V0
    - transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    - transformation::CC_JUDGE_AGAINST_COMPOSITION_V0
  - wave: '4'
    step: '40'
    code: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::RB_TRANSFORMATION_BINDINGS_V0
    - transformation::AC_REGISTER_AUTHOR_V0
    - transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    - transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
  - wave: '4'
    step: '41'
    code: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::RB_TRANSFORMATION_BINDINGS_V0
    - transformation::AC_REGISTER_AUTHOR_V0
    - transformation::IN_BUSINESS_INTENT_SUBMITTED_V0
    - transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
  - wave: '4'
    step: '42'
    code: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::RB_TRANSFORMATION_BINDINGS_V0
    - transformation::AC_REGISTER_AUTHOR_V0
    - transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    - transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
  - wave: '4'
    step: '43'
    code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::RB_TRANSFORMATION_BINDINGS_V0
    - transformation::AC_REGISTER_AUTHOR_V0
    - transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    - transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
  - wave: '4'
    step: '44'
    code: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0
    action: NEW
    subdomain: design
    depends_on:
    - transformation::RB_TRANSFORMATION_BINDINGS_V0
    - transformation::AC_REGISTER_AUTHOR_V0
    - transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    - transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
  - wave: '5'
    step: '45'
    code: transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
    action: NEW
    subdomain: transformation
    depends_on:
    - transformation::WF_P0_SEED_ADMISSIBILITY_V0
    - transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
    - transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0
    - transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0
    - transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0
    - transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0
    - transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
    - transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    - transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0
  critical_path:
  - position: '1'
    code: transformation::STRUCTURE_PHASE_FINDINGS_V0
  - position: '2'
    code: transformation::CT_PURE_EVALUATE_RULES_V0
  - position: '3'
    code: transformation::CC_JUDGE_DOCUMENT_V0
  - position: '4'
    code: transformation::WF_P0_SEED_ADMISSIBILITY_V0
  - position: '5'
    code: transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
  mandate_artifact_summary:
  - action: NEW
    count: '45'
    description: 7 STRUCTURE, 2 VOCAB, 3 AC, 6 CT, 5 CC, 10 IN, 10 WF, 2 RB
  field_declarations:
  - code: transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V0
    subdomain_field: transformation
  - code: transformation::STRUCTURE_PHASE_FINDINGS_V0
    subdomain_field: transformation
  - code: transformation::STRUCTURE_PHASE_HEADER_V0
    subdomain_field: transformation
  - code: transformation::STRUCTURE_PHASE_PRIORS_V0
    subdomain_field: transformation
  - code: transformation::STRUCTURE_PHASE_REGISTERS_V0
    subdomain_field: transformation
  - code: transformation::STRUCTURE_PHASE_SECTIONS_V0
    subdomain_field: transformation
  - code: transformation::VOCAB_FACT_PROVENANCE_V0
    subdomain_field: build
  - code: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
    subdomain_field: design
  - code: transformation::AC_GATE_REVIEWER_V0
    subdomain_field: design
  - code: transformation::AC_REGISTER_AUTHOR_V0
    subdomain_field: design
  - code: transformation::AC_SEED_AUTHOR_V0
    subdomain_field: design
  - code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    subdomain_field: build
  - code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    subdomain_field: build
  - code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    subdomain_field: build
  - code: transformation::CC_PERSIST_ARTIFACTS_V0
    subdomain_field: build
  - code: transformation::IN_CONSTRUCTION_REQUESTED_V0
    subdomain_field: build
  - code: transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    subdomain_field: design
  - code: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    subdomain_field: design
  - code: transformation::IN_BUSINESS_INTENT_SUBMITTED_V0
    subdomain_field: design
  - code: transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    subdomain_field: design
  - code: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    subdomain_field: design
  - code: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    subdomain_field: design
  - code: transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    subdomain_field: design
  - code: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    subdomain_field: design
  - code: transformation::IN_SEED_SUBMITTED_V0
    subdomain_field: design
  - code: transformation::RB_CONSTRUCTION_BINDINGS_V0
    subdomain_field: build
  - code: transformation::RB_TRANSFORMATION_BINDINGS_V0
    subdomain_field: design
  - code: transformation::CT_PURE_EVALUATE_RULES_V0
    subdomain_field: design
  - code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V0
    subdomain_field: design
  - code: transformation::CT_PURE_PARSE_REGISTERS_V0
    subdomain_field: design
  - code: transformation::CC_CONSTRUCT_ARTIFACTS_V0
    subdomain_field: build
  - code: transformation::CC_JUDGE_AGAINST_COMPOSITION_V0
    subdomain_field: design
  - code: transformation::CC_JUDGE_AGAINST_SNAPSHOT_V0
    subdomain_field: design
  - code: transformation::CC_JUDGE_DOCUMENT_V0
    subdomain_field: design
  - code: transformation::WF_CONSTRUCT_ARTIFACTS_V0
    subdomain_field: build
  - code: transformation::WF_P0_SEED_ADMISSIBILITY_V0
    subdomain_field: design
  - code: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
    subdomain_field: design
  - code: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0
    subdomain_field: design
  - code: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0
    subdomain_field: design
  - code: transformation::WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0
    subdomain_field: design
  - code: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0
    subdomain_field: design
  - code: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
    subdomain_field: design
  - code: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    subdomain_field: design
  - code: transformation::WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0
    subdomain_field: design
  - code: transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0
    subdomain_field: transformation
  new_capabilities:
  - code: transformation::CT_PURE_ATTRIBUTE_PROVENANCE_V0
    purpose: Report, for each leaf of a rendered artifact, whether the design stated it, a constitution
      governs it, or the renderer supplied it
    inputs: rendered:array, sources:object
    outputs: provenance:object, governing_artifacts:object
  - code: transformation::CT_PURE_MEASURE_COMPLETENESS_V0
    purpose: Measure Construction Completeness and refuse a design that does not determine its artifacts
    inputs: design_registers:array, mandate_registers:array, threshold:number, provenance:object
    outputs: completeness:number, determined:integer, required:integer, undetermined:array
  - code: transformation::CT_PURE_RENDER_ARTIFACTS_V0
    purpose: Render every artifact a mandate schedules from the design that determines it
    inputs: design_registers:array, mandate_registers:array
    outputs: artifacts:array, documents:array, artifact_count:integer, sources:object
  - code: transformation::CT_PURE_EVALUATE_RULES_V0
    purpose: Evaluate a declared rule set against parsed registers
    inputs: header:object, sections:array, registers:array, document_text:string, rule_set:array, observed:object,
      priors:object
    outputs: verdict:string, findings:array, rules_evaluated:integer
  - code: transformation::CT_PURE_PARSE_PRIOR_PHASES_V0
    purpose: Parse the upstream phase documents a phase is judged against
    inputs: prior_texts:object
    outputs: priors:object
  - code: transformation::CT_PURE_PARSE_REGISTERS_V0
    purpose: Parse phase document text into structured registers
    inputs: document_text:string
    outputs: header:object, sections:array, registers:array
  new_intents:
  - code: transformation::IN_CONSTRUCTION_REQUESTED_V0
    purpose: Offer an approved design and mandate for construction
    workflow: WF_CONSTRUCT_ARTIFACTS_V0
    inputs: design_text:string, mandate_text:string, threshold:number, author_of_record:string
  - code: transformation::IN_ANALYSIS_LOOP_SUBMITTED_V0
    purpose: Offer an Analysis Loop register for admissibility judgement
    workflow: WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0
    inputs: register_text:string, prior_texts:object, author_of_record:string
  - code: transformation::IN_AUTHORING_MANDATE_SUBMITTED_V0
    purpose: Offer an Authoring Mandate for admissibility judgement
    workflow: WF_P8_AUTHORING_MANDATE_ADMISSIBILITY_V0
    inputs: register_text:string, prior_texts:object, author_of_record:string
  - code: transformation::IN_BUSINESS_INTENT_SUBMITTED_V0
    purpose: Offer a Business Intent register for admissibility judgement
    workflow: WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0
    inputs: register_text:string, prior_texts:object, author_of_record:string
  - code: transformation::IN_BUSINESS_MODEL_SUBMITTED_V0
    purpose: Offer a Business Model register for admissibility judgement
    workflow: WF_P4_BUSINESS_MODEL_ADMISSIBILITY_V0
    inputs: register_text:string, prior_texts:object, author_of_record:string
  - code: transformation::IN_CHANGE_REQUEST_SUBMITTED_V0
    purpose: Offer a Change Request register for admissibility judgement
    workflow: WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
    inputs: register_text:string, prior_texts:object, author_of_record:string
  - code: transformation::IN_DESIGN_INTENT_SUBMITTED_V0
    purpose: Offer a Design Intent register for admissibility judgement
    workflow: WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    inputs: register_text:string, prior_texts:object, author_of_record:string
  - code: transformation::IN_DOMAIN_MODEL_SUBMITTED_V0
    purpose: Offer a Domain Model register for admissibility judgement
    workflow: WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0
    inputs: register_text:string, prior_texts:object, author_of_record:string
  - code: transformation::IN_GOVERNANCE_INTENT_SUBMITTED_V0
    purpose: Offer a Governance Intent register for admissibility judgement
    workflow: WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
    inputs: register_text:string, prior_texts:object, author_of_record:string
  - code: transformation::IN_SEED_SUBMITTED_V0
    purpose: Offer a seed document for admissibility judgement
    workflow: WF_P0_SEED_ADMISSIBILITY_V0
    inputs: seed_text:string, author_of_record:string
  cross_subdomain_notes: []
```

The 45 artifacts of `transformation`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
