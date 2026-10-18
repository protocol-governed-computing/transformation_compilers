# WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0

## Generated Artifact

This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and
the copy is never corrected directly: where this artifact and its generator disagree, this
artifact is stale, and an edit here lasts until whoever next runs the emission.

- **Generator:** `transformation.design.emit:emit_rule_sets`
- **Generator sources** — one generator together, never separately:
  - `registry/schema/REGISTER_SCHEMA_P5_V0.json`
  - `registry/design/vocabulary/VOCAB_DESIGN_REGISTER_TERMS_V0.md`
  - `registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V0.md`

To change what this phase judges, amend a source and invoke the generator.
`tc phase emit --check` refuses a build in which the two disagree.

---

## 1. Intent

Phase 5 of the change pipeline: decide whether an offered Business Intent register is admissible.

P5 states the irreducible WHAT — purpose, scope, objects, identity, invariants, actions — and is
the first phase to name what the change will build.

---

## 2. The purity ladder, and the rule pair it produces

Every phase before this one is business language only. P5 admits *provisional* artifact codes,
because naming what you intend to build is how intent becomes specific. It still may not admit a
*binding*: a domain-qualified FQDN, a JSONPath, a module path belong to Stage 7, and a phase
reaching for them would decide placement before governance intent exists.

So this phase forbids a namespace in one register and requires one in another:

- `provisional_codes` must not be namespaced — a code carrying a domain has already been placed
- `cross_subdomain_refs` must cite exact, resolvable identities, because those artifacts already
  exist, and citing what exists is observation rather than design

One register names what this change will create; the other names what it will lean on. That is why
this workflow grounds: only the composition can settle whether a borrowed capability is really
there.

---

## Machine

```yaml
fqdn: transformation::WF_P5_BUSINESS_INTENT_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: design

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Business Intent register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_BUSINESS_INTENT_SUBMITTED_V0

  nodes:
    IN_BUSINESS_INTENT_SUBMITTED_V0:
      type: IN
      code: IN_BUSINESS_INTENT_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_AGAINST_SNAPSHOT_V0
        NACK: EXIT_REJECTED

    CC_JUDGE_AGAINST_SNAPSHOT_V0:
      type: CC
      code: CC_JUDGE_AGAINST_SNAPSHOT_V0
      inputs:
        document_text: $.payload.register_text
        # P4 hands this phase its consolidation, and P5 transforms it rather than restating
        # it: `scope_boundary` is a fresh in/out judgement carrying deferrals P4 never had,
        # and no other register receives `capability_graph`. There is no row-level obligation
        # there to check, so none is declared against P4.
        #
        # The seed is a different matter. The subdomain purpose is authored once at P0 and has
        # no register to travel in between, so this is where it reappears — and until the
        # handoff was checked, it reappeared as a second author's paragraph.
        prior_texts: $.payload.prior_texts
        rule_set:
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
          intent: a phase document states its phase, its domain and subdomain, its change, and the rule set it
            was authored under
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
            detail: the register answers one question — whether this phase inherited the seed's purpose or refined
              it — and two rows are two answers to it
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
            detail: the purpose is declared INHERITED and does not match the seed's — inherit it word for word,
              or declare REFINED and say what this phase adds
          intent: the one narrative no artifact can derive is authored once and never quietly replaced
        - id: REFINEMENT_NOT_STATED
          identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/2
          check: CELL_NOT_EMPTY
          register: purpose_provenance
          params:
            column: Refinement
            only_when_column: Disposition
            only_when_value: REFINED
            detail: a refined purpose must state what it adds that the seed did not say; silence here is the silent
              replacement this register exists to prevent
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
            detail: '{token!r} in {column!r} — a provisional code carrying a namespace has already been placed,
              and placement is Stage 7''s decision'
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
            detail: '{token!r} in {column!r} — a path, a binding expression or a hash is an implementation decision,
              and Stage 7 owns those'
          intent: intent says what must be true, never how it is wired
        - id: INVARIANT_WITHOUT_BUSINESS_REASON
          identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/10
          check: CELL_NOT_EMPTY
          register: invariants
          params:
            column: Business Reason
            detail: invariant states no business reason — a rule without one is a technical constraint and belongs
              elsewhere
          intent: every invariant is answerable to the business, not to the design
        - id: IDENTITY_WITHOUT_UNIQUENESS_RULE
          identity: transformation.schemas.REGISTER_SCHEMA_P5_V0#/allOf/11
          check: CELL_NOT_EMPTY
          register: identity_semantics
          params:
            column: Uniqueness Rule
            detail: identity declares no uniqueness rule — what a duplicate means is irreducible business knowledge
              the compiler cannot infer
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
