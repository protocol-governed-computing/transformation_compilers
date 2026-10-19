# WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0

## Generated Artifact

This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and
the copy is never corrected directly: where this artifact and its generator disagree, this
artifact is stale, and an edit here lasts until whoever next runs the emission.

- **Generator:** `transformation.design.emit:emit_rule_sets`
- **Generator sources** — one generator together, never separately:
  - `registry/schema/REGISTER_SCHEMA_P6_V0.json`
  - `registry/design/vocabulary/VOCAB_DESIGN_REGISTER_TERMS_V0.md`
  - `registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V0.md`

To change what this phase judges, amend a source and invoke the generator.
`tc phase emit --check` refuses a build in which the two disagree.

---

## 1. Intent

Phase 6 of the change pipeline: decide whether an offered Governance Intent register is admissible.

P6 answers WHERE — which subdomain owns each capability, which owns each store, and what crosses a
boundary. It is the phase that draws lines.

---

## 2. The ladder does not simply accumulate

Stage 5 requires provisional artifact codes; this stage forbids them. That looks like a step
backwards and is not: each rung admits its *own* vocabulary rather than everything below it. P6's
vocabulary is placement, so a capability here is named in business language and placed in a
subdomain. A row naming a provisional code has answered a question this stage is not asking and
pre-empted one Stage 7 owns.

Existing artifacts stay citable by exact FQDN at every rung, because citing what already exists is
observation rather than design — which is why this workflow grounds.

## 3. What ownership exclusivity means here

A store is written only by capabilities of the subdomain that owns it. When a change needs a peer's
store written, the writing capability belongs to that peer and is declared as a dependency gap.
That is not visible in any single cell, so what is checked is the discipline that makes it
visible: a dependency states its direction, a satisfied one names the artifact that satisfies it,
and every capability in the outcome was placed in the ownership register first.

---

## Machine

```yaml
fqdn: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: design

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Governance Intent register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_GOVERNANCE_INTENT_SUBMITTED_V0

  nodes:
    IN_GOVERNANCE_INTENT_SUBMITTED_V0:
      type: IN
      code: IN_GOVERNANCE_INTENT_SUBMITTED_V0
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
          identity: transformation.schemas.REGISTER_SCHEMA_P6_V0#/properties/document/required
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
            detail: capability is SATISFIED but names no existing artifact — a claim that something already covers
              this needs the something
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

    EXIT_REJECTED:
      type: EXIT
```
