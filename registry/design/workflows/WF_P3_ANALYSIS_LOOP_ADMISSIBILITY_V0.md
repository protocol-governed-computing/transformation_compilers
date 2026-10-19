# WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0

## Generated Artifact

This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and
the copy is never corrected directly: where this artifact and its generator disagree, this
artifact is stale, and an edit here lasts until whoever next runs the emission.

- **Generator:** `transformation.design.emit:emit_rule_sets`
- **Generator sources** — one generator together, never separately:
  - `registry/schema/REGISTER_SCHEMA_P3_V0.json`
  - `registry/design/vocabulary/VOCAB_DESIGN_REGISTER_TERMS_V0.md`
  - `registry/design/capability_contracts/CC_JUDGE_AGAINST_COMPOSITION_V0.md`

To change what this phase judges, amend a source and invoke the generator.
`tc phase emit --check` refuses a build in which the two disagree.

---

## 1. Intent

Phase 3 of the change pipeline: decide whether an offered Analysis Loop register is admissible.

P3 is the first phase that **decides**. P0 reorganizes, P1 classifies, P2 discovers; P3 resolves
the extend-vs-new question P2 deferred and commits every capability to REUSE, EXTEND or
AUTHOR_NEW.

---

## 2. Why this workflow observes twice

P2 asks whether a cited identity exists, and the artifact list answers it. A phase that decides
asks a further question — may this artifact be offered to this change request at all — and that is
a property of the domain that owns it, declared by that domain.

So this workflow composes `CC_JUDGE_AGAINST_COMPOSITION_V0`: the artifact list resolves identities,
the composition summary carries each domain's declared reuse visibility, and the two answer
different questions. A domain declaring no visibility is a hard failure, not a permissive default —
absence would otherwise mean "search everything", which is the inference the declaration exists to
prevent.

**The declaration bounds the search space; it never makes the decision.** Which artifacts are
reused, extended or newly authored stays with the author, per artifact, against evidence.

---

## 3. Why it also reads P2

P3's verification pass exists to re-ground every prior result against the composition rather than
inherit it. Whether it actually covered them is not a property of this register: a pass over two of
P2's three belief results reads as complete, and the third was inherited silently.

So this workflow takes `prior_texts` and is judged against P2 as well as against the composition. A
result nobody re-verified is a finding, and so is one re-verified under a claim P2 never made — the
citation would otherwise lend a substitution provenance it does not have.

---

## Machine

```yaml
fqdn: transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: design

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered Analysis Loop register is admissible
  actor_context: transformation::AC_REGISTER_AUTHOR_V0

  start_node: IN_ANALYSIS_LOOP_SUBMITTED_V0

  nodes:
    IN_ANALYSIS_LOOP_SUBMITTED_V0:
      type: IN
      code: IN_ANALYSIS_LOOP_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_AGAINST_COMPOSITION_V0
        NACK: EXIT_REJECTED

    CC_JUDGE_AGAINST_COMPOSITION_V0:
      type: CC
      code: CC_JUDGE_AGAINST_COMPOSITION_V0
      inputs:
        document_text: $.payload.register_text
        prior_texts: $.payload.prior_texts
        rule_set:
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
          intent: a phase document states its phase, its domain and subdomain, its change, and the rule set it
            was authored under
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
              oneOf: *id001
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
              oneOf: *id001
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
            known_registers: *id002
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
            detail: decision records no alternatives examined — 'I searched and found nothing' is credible only
              with the search shown
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
            detail: verification records no evidence — grounding is not inherited, so a re-check that cites nothing
              did not happen
          intent: an overturned answer is marked with what overturned it, never erased
        - id: SATURATION_CRITERIA_INCOMPLETE
          identity: transformation.schemas.REGISTER_SCHEMA_P3_V0#/allOf/6
          check: TABLE_HAS_ROWS
          register: saturation
          params:
            minimum: 5
          intent: analysis is saturated only against every declared criterion; a claim resting on fewer is the
            gap the criteria exist to close
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
