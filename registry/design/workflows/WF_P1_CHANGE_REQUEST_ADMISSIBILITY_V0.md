# WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0

## Generated Artifact

This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and
the copy is never corrected directly: where this artifact and its generator disagree, this
artifact is stale, and an edit here lasts until whoever next runs the emission.

- **Generator:** `transformation.design.emit:emit_rule_sets`
- **Generator sources** — one generator together, never separately:
  - `registry/schema/REGISTER_SCHEMA_P1_V0.json`
  - `registry/design/vocabulary/VOCAB_DESIGN_REGISTER_TERMS_V0.md`
  - `registry/design/capability_contracts/CC_JUDGE_DOCUMENT_V0.md`

To change what this phase judges, amend a source and invoke the generator.
`tc phase emit --check` refuses a build in which the two disagree.

---

## 1. Intent

Phase 1 of the change pipeline: decide whether an offered Change Request register is admissible.

This workflow **authors no new mechanism**. It composes the same governed call P0 uses — judge a
document against a declared rule set — and differs only in the rule set it carries. That is the
generalization the pipeline was designed for: phases share mechanisms and differ in declared data.

---

## 2. What P1 adds over P0

P0 governs a seed, where business content enters. P1 governs the register that restates it, so P1
can check something P0 cannot: **traceability**. Every row must cite the seed finding it came from,
in a parseable form. An uncited row is content the phase invented, which is precisely what P1 must
not do.

The rule set below is **derived from the vendored template**
(`templates/p1_change_request_template_v0.md`), which declares the fifteen registers, their columns,
their inline controlled vocabularies, which may be empty, and which hold business language. Only the
document header — which belongs to no register — is declared by hand.

Traceability follows from the register schema: every register carrying a `Source Finding` column
gets a `ROW_WITHOUT_SOURCE_FINDING` and a `SOURCE_FINDING_UNRESOLVED` rule, so a register added later
is traced automatically rather than left as a hole where invention is silently permitted.

---

## 3. Citations are mappings

A citation is a mapping naming what it cites — `{phase: p0, register: known_facts, row: 14}` — not
a string read by pattern. A citation that is not one is refused by its type, a row that cites nothing
says `null` and is refused for it, and the rules that resolve a citation read the mapping.

---

## Machine

```yaml
fqdn: transformation::WF_P1_CHANGE_REQUEST_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: design

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Change Request register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_CHANGE_REQUEST_SUBMITTED_V0

  nodes:
    IN_CHANGE_REQUEST_SUBMITTED_V0:
      type: IN
      code: IN_CHANGE_REQUEST_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_DOCUMENT_V0
        NACK: EXIT_REJECTED

    CC_JUDGE_DOCUMENT_V0:
      type: CC
      code: CC_JUDGE_DOCUMENT_V0
      inputs:
        document_text: $.payload.register_text
        prior_texts: $.payload.prior_texts
        rule_set:
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
          intent: a phase document states its phase, its domain and subdomain, its change, and the rule set it
            was authored under
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
              oneOf: *id001
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
            known_registers: *id002
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
            detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask it
              as a clarification, do not hedge it in a register'
          intent: an unanswered question left in a register reads as decided to every later phase
        - id: BLOCKING_CLARIFICATION_OUTSTANDING
          identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/35
          check: ROW_ABSENT_WHEN
          register: clarification_requests
          params:
            column: Blocking
            value: 'YES'
            detail: a blocking clarification is unanswered — resolve it with the named owner and fold the answer
              into the document before any phase consumes it
          intent: a blocking question the next phase never sees is answered by invention
        - id: BUSINESS_CLARIFICATION_OUTSTANDING
          identity: transformation.schemas.REGISTER_SCHEMA_P1_V0#/allOf/36
          check: ROW_ABSENT_WHEN
          register: clarification_requests
          params:
            column: Owner
            value: HUMAN
            detail: only the business can answer this — ask it, fold the answer into the problem statement, and
              re-author the seed rather than carrying the question forward
          intent: a business question that outlives the seed is answered downstream by inference
      next:
        SUCCESS: EXIT_JUDGED
        VIOLATION: EXIT_REJECTED

    EXIT_JUDGED:
      type: EXIT
      status: SUCCESS

    EXIT_REJECTED:
      type: EXIT
      status: VIOLATION
```
