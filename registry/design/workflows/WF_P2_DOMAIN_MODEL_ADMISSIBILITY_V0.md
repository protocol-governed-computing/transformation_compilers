# WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0

## Generated Artifact

This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and
the copy is never corrected directly: where this artifact and its generator disagree, this
artifact is stale, and an edit here lasts until whoever next runs the emission.

- **Generator:** `transformation.design.emit:emit_rule_sets`
- **Generator sources** — one generator together, never separately:
  - `registry/schema/REGISTER_SCHEMA_P2_V0.json`
  - `registry/design/vocabulary/VOCAB_DESIGN_REGISTER_TERMS_V0.md`
  - `registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V0.md`

To change what this phase judges, amend a source and invoke the generator.
`tc phase emit --check` refuses a build in which the two disagree.

---

## 1. Intent

Phase 2 of the change pipeline: decide whether an offered Domain Model register is admissible.

P2 is the first phase that **looks**. P0 and P1 judge a document against itself — structure,
vocabulary, traceability — and can reach a verdict without knowing anything about the system. P2
cannot: a register claiming an artifact already exists is making a claim about the assembled
composition, and only observation settles it.

So this workflow composes `CC_JUDGE_AGAINST_SNAPSHOT_V0` rather than `CC_JUDGE_DOCUMENT_V0`. The
difference is one governed observation step, bound to the snapshot this workflow executes from.

---

## 2. The first handoff this pipeline checks

P2 is also the first phase judged against the document it was handed. P1 declares what the author
believes the system already provides; P2's spine resolves each of those beliefs, and until now
nothing established that the two registers were about the same beliefs.

A dropped belief is invisible from either side. P1 never sees P2. P2's register is well formed with
two rows or with three. The defect exists only in the gap, so the rule needs both documents — which
is why this workflow takes `prior_texts` alongside the register it judges.

---

## 3. Grounding, and what it deliberately does not flag

Cited identities are classified against the observed composition by the identity-preserving
taxonomy: exact, typo-alias, wrong-domain, proposed-new, fabrication. Only a misspelling or a
wrong namespace is reported.

An identity absent from the baseline is **not** a finding. Every change request that designs
anything proposes identities that do not exist yet, and proposed-new cannot be told from fabricated
without the CR's declared new artifacts — which arrive at P7. Counting what was not found would
reject every correct dossier for doing its job.

---

## Machine

```yaml
fqdn: transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: design

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Domain Model register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_DOMAIN_MODEL_SUBMITTED_V0

  nodes:
    IN_DOMAIN_MODEL_SUBMITTED_V0:
      type: IN
      code: IN_DOMAIN_MODEL_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_AGAINST_SNAPSHOT_V0
        NACK: EXIT_REJECTED

    CC_JUDGE_AGAINST_SNAPSHOT_V0:
      type: CC
      code: CC_JUDGE_AGAINST_SNAPSHOT_V0
      inputs:
        document_text: $.payload.register_text
        prior_texts: $.payload.prior_texts
        rule_set:
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
          intent: a phase document states its phase, its domain and subdomain, its change, and the rule set it
            was authored under
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
              oneOf: &id001
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
            known_registers: &id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
            detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask it
              as a clarification, do not hedge it in a register'
          intent: an unanswered question left in a register reads as decided to every later phase
      next:
        SUCCESS: EXIT_JUDGED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
        NOT_FOUND: EXIT_REJECTED

    EXIT_JUDGED:
      type: EXIT
      status: SUCCESS

    EXIT_REJECTED:
      type: EXIT
      status: VIOLATION
```
