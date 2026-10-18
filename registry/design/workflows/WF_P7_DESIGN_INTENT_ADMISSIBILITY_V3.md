# WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3

## Generated Artifact

This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and
the copy is never corrected directly: where this artifact and its generator disagree, this
artifact is stale, and an edit here lasts until whoever next runs the emission.

- **Generator:** `transformation.design.emit:emit_rule_sets`
- **Generator sources** — one generator together, never separately:
  - `registry/schema/REGISTER_SCHEMA_P7_V0.json`
  - `registry/design/vocabulary/VOCAB_DESIGN_REGISTER_TERMS_V0.md`
  - `registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V1.md`

To change what this phase judges, amend a source and invoke the generator.
`tc phase emit --check` refuses a build in which the two disagree.

---

## 1. Intent

Phase 7 of the change pipeline: decide whether an offered Design Intent register is admissible.

P7 answers HOW, and it is where identity becomes binding. Stage 5 assigned provisional codes and
Stage 6 placed capabilities in subdomains; this phase turns those into domain-qualified FQDNs that
later phases, the compiler and the runtime all use verbatim. **Gate 1 closes here** — the dossier is
reviewed as a body before any mandate may be drafted.

---

## 2. The one rule that runs backwards

Every earlier phase cites artifacts that exist, and is wrong when a citation fails to resolve. This
phase assigns identities that *will* exist, and is wrong when one **does**. A code colliding with
something already in the composition is not a new artifact — it is a silent redefinition of an old
one, and nothing downstream would notice.

So this workflow grounds for the opposite reason every other grounded phase does: not to confirm a
citation, but to refuse a name already taken. A collision check that could not see the composition
would admit every colliding name, so an unobserved composition is itself the finding.

## 3. Immutability discipline

A binding FQDN is assigned once and reused as the exact same string everywhere. A spelling variant
of the same concept does not read as a synonym; it creates a second, permanently misnamed artifact.
Every code referenced in the topology, in a runtime binding, or in a composition must therefore be
declared — as new here, or as an existing artifact carried over. A reference to neither is a name
nobody owns.

---

## Machine

```yaml
fqdn: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V3
supersedes: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V2
artifact_kind: WORKFLOW
version: v3
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: design

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Design Intent register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_DESIGN_INTENT_SUBMITTED_V0

  nodes:
    IN_DESIGN_INTENT_SUBMITTED_V0:
      type: IN
      code: IN_DESIGN_INTENT_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_AGAINST_SNAPSHOT_V1
        NACK: EXIT_REJECTED

    CC_JUDGE_AGAINST_SNAPSHOT_V1:
      type: CC
      code: CC_JUDGE_AGAINST_SNAPSHOT_V1
      inputs:
        document_text: $.payload.register_text
        prior_texts: $.payload.prior_texts
        rule_set:
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
          intent: a phase document states its phase, its domain and subdomain, its change, and the rule set it
            was authored under
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              The governance surface is authored, not constructed: cite it with REUSE or REVIEW, and deliver the
              change by authoring it'
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
            detail: a binding identity is immutable, so a spelling variant is a second artifact rather than a
              synonym
          intent: every node in the topology runs an identity this design actually assigned
        - id: TOPOLOGY_NODE_REPEATED
          identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/7
          check: COLUMN_VALUES_UNIQUE
          register: execution_topology
          params:
            columns:
            - Workflow
            - Node
            detail: '{0} names {1} again (first at row {first}) — a node that runs a contract twice needs a key
              for each place, and `Runs` naming the contract'
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
            detail: branches on {outcomes}, which {operation} does not answer — it answers {answers}. An outcome
              the store cannot produce comes from an interpretation, and this step names none, so the branch is
              a decision nothing makes
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
            detail: routes on {outcomes} and declares no semantic status — {operation} answers {answers}, so the
              outcome routed on is an interpretation's, and the workflow branch it feeds has nothing declared
              to route on
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
            detail_spurious: names a store on {capability}, which keeps none — the step addresses records that
              capability has no way to hold
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
            detail: declares a reach to {binding} and reads nothing it covers — that binding answers for {stores},
              and no step this act runs addresses any of them. A permission granted for nothing is one whose purpose
              nobody reviewed
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
            detail: reads {store}, which {binding} does not cover and no declared reach names — the act reaches
              records another part of the business owns and its design does not say so, which is invisible until
              the act runs
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
            detail: vocabulary says nothing about what it extends — a base vocabulary declares that with the none
              marker, because an empty cell and an omission render the same thing
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
          intent: a transform is the one family that points outside the composition; the path is designed, not
            discovered
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
            detail: transform declares no kind — whether it runs an implementation or a stream of steps decides
              every other rule this row is held to
          intent: a transform says whether it is an atom or a molecule
        - id: IMPLEMENTATION_KIND_UNKNOWN
          identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/40
          check: CELL_MATCHES
          register: implementation_bindings
          params:
            column: Kind
            pattern: ^(atom|molecule)$
            detail: kind is {value!r}; a transform is an atom, which runs an implementation, or a molecule, which
              runs its declared steps, and the schema admits nothing else
          intent: kind is one of the two the runtime can run
        - id: IMPLEMENTATION_WITHOUT_REFUSAL
          identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/41
          check: CELL_NOT_EMPTY
          register: implementation_bindings
          params:
            column: Refusal
            detail: transform declares no refusal — whether a judgement is raised or returned is the one fact
              that says if a step routing on it can ever fail, and both look the same from outside
          intent: a transform says how it expresses a judgement about its subject
        - id: IMPLEMENTATION_REFUSAL_UNKNOWN
          identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/42
          check: CELL_MATCHES
          register: implementation_bindings
          params:
            column: Refusal
            pattern: ^(raises|returns|never)$
            detail: refusal is {value!r}; a transform raises its judgement, returns it, or makes none, and the
              schema admits nothing else
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
            detail: callable is {value!r}; every transform in the composition is entered through `execute`, and
              a loader given another name finds nothing
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
            detail: '{value!r} names a store CS_MUTABLE_JSON_V0 keeps, and CS_MUTABLE_JSON_V0 writes .json — a
              store''s name must not advertise a format its capability does not write'
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
            detail: '{value!r} names a store CS_REGISTRY_V0 keeps, and CS_REGISTRY_V0 writes .jsonl — a store''s
              name must not advertise a format its capability does not write'
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
            detail: '{value!r} names a store CS_APPENDONLY_JSONL_V0 keeps, and CS_APPENDONLY_JSONL_V0 writes .jsonl
              — a store''s name must not advertise a format its capability does not write'
          intent: a store is named for the format its capability actually writes
        - id: BINDING_SOURCE_UNROOTED
          identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/49
          check: CELL_MATCHES
          register: step_bindings
          params:
            column: Bound To
            pattern: ^(?:(?:payload|inputs|results|capability_result)\..+|result_status|(?!(?:payload|inputs|results|capability_result)$)[^.]*|.*::.*|-?[0-9]+(?:\.[0-9]+)?)$
            detail: '{value!r} is not rooted in a scope execution offers — a source names a field under one of
              payload, inputs, results, capability_result, or is result_status'
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
            detail: output binds {value!r}, which is not a form the runtime resolves — an output is written to
              capability_result.<field> or result_status; an input reads inputs.<field>, payload.<field>, results.<step>.<field>,
              or is a literal
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
            detail: input binds {value!r}, which is not a form the runtime resolves — an output is written to
              capability_result.<field> or result_status; an input reads inputs.<field>, payload.<field>, results.<step>.<field>,
              or is a literal
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
            detail: provenance is stated about an artifact this design neither authors nor carries over — a generator
              for something nothing schedules produces nothing
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
            detail: binds a generated value, and its owner names no generator — a generator determines only what
              the design says it does
          intent: a value is declared generated only where the design names its generator
        - id: GENERATOR_UNNAMED
          identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/62
          check: CELL_NOT_EMPTY
          register: generation_provenance
          params:
            column: Generator
            detail: artifact is declared generated and names no generator — construction has nothing to invoke
              and no way to reach it
          intent: a generated artifact names what produces it
        - id: GENERATOR_UNREACHABLE
          identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/63
          check: CELL_MATCHES
          register: generation_provenance
          params:
            column: Generator
            pattern: ^[a-z_][a-z0-9_]*(?:\.[a-z_][a-z0-9_]*)*:[a-z_][a-z0-9_]*$
            detail: generator {value!r} must be module:callable — construction imports its generator and a script
              it can only shell out to is one nothing governs
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
            detail: names no owner — a refusal handed on to nobody is a refusal dropped in language that sounds
              like a plan
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
          intent: the governance surface is cited for a refusal the business declared, never for one it did not
        - id: GOVERNING_RULE_PHASE_MALFORMED
          identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/70
          check: CELL_MATCHES
          register: refusal_governance_discharge
          params:
            column: Phase
            pattern: ^p[0-8]$
            detail: '{value!r} is not a phase — a rule is named by its phase and its identifier together, written
              p0 through p8, because an identifier alone names nine rules'
          intent: a cited rule is located in the phase whose rule set holds it
        - id: GOVERNING_RULE_UNNAMED
          identity: transformation.schemas.REGISTER_SCHEMA_P7_V0#/allOf/71
          check: CELL_NOT_EMPTY
          register: refusal_governance_discharge
          params:
            column: Governing Rule
            detail: cites no rule — a refusal said to be carried out by the governance surface and naming nothing
              there is prose, and prose refuses nothing
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
          intent: a moment is announced from an ending the act has, and one that completes it — or, for a moment
            declared a refusal, one that refuses it
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
            detail: step kind is {value!r}; a step runs an atom, a molecule once, or a molecule once per member
              of a collection, and the compiler lowers nothing else
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
            detail: '{value} emits a second value, first at row {first} — a molecule yields exactly one, and two
              leave a caller to guess which it was handed'
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
            detail: source is {value!r}; a molecule binding reads inputs.<field>, results.<step>.<field>, iterator,
              accumulator.<field>, or is a literal
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
            detail: a carried value is updated from {value!r}; it is taken from what the pass produced, results.<field>,
              or the loop carries forward something no pass computed
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
            detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask it
              as a clarification, do not hedge it in a register'
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
