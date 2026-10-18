# WF_P0_SEED_ADMISSIBILITY_V0

## Generated Artifact

This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and
the copy is never corrected directly: where this artifact and its generator disagree, this
artifact is stale, and an edit here lasts until whoever next runs the emission.

- **Generator:** `transformation.design.emit:emit_rule_sets`
- **Generator sources** — one generator together, never separately:
  - `registry/schema/REGISTER_SCHEMA_P0_V0.json`
  - `registry/design/vocabulary/VOCAB_DESIGN_REGISTER_TERMS_V0.md`
  - `registry/design/capability_contracts/CC_JUDGE_DOCUMENT_V0.md`

To change what this phase judges, amend a source and invoke the generator.
`tc phase emit --check` refuses a build in which the two disagree.

---

## 1. Intent

Phase 0 of the change pipeline: decide whether an offered seed is admissible.

The workflow composes one reused governed call — judge a document — and carries the **rule set
itself** as declared node input. That is the point of this artifact. The rules deciding
admissibility are compiled, sealed, versioned and readable from the composition through ordinary
artifact inspection; they are not configuration, not code, and not editable outside a governed
change.

The mechanisms hold no policy. Reading the evaluator tells you how a check runs. Reading this
workflow tells you what is governed. Later phases reuse the same mechanisms and declare their own
rule sets here, in their own workflow.

---

## 2. Verdict, not exception

`INADMISSIBLE` is a normal outcome. A seed that fails the rule set has been correctly judged, not
incorrectly executed. `VIOLATION` is reserved for a rule naming a check kind the evaluator does not
implement — a defect in the rule set, not in the seed.

---

## 3. Beliefs are refused by pattern

A belief asserted as fact is refused by a pattern the register schema declares on the `Belief`
column, not by a check written for it alone. The rule refuses the same rows.

---

## Machine

```yaml
fqdn: transformation::WF_P0_SEED_ADMISSIBILITY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: design

runtime_binding: transformation::RB_TRANSFORMATION_BINDINGS_V0
subdomain: design
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Decide whether an offered seed is admissible
  actor_context: transformation::AC_SEED_AUTHOR_V0

  start_node: IN_SEED_SUBMITTED_V0

  nodes:
    IN_SEED_SUBMITTED_V0:
      type: IN
      code: IN_SEED_SUBMITTED_V0
      next:
        ACK: CC_JUDGE_DOCUMENT_V0
        NACK: EXIT_REJECTED

    CC_JUDGE_DOCUMENT_V0:
      type: CC
      code: CC_JUDGE_DOCUMENT_V0
      inputs:
        document_text: $.payload.seed_text
        # P0's input is human prose, not a phase document — there is no upstream register.
        prior_texts: {}
        rule_set:
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
          intent: a phase document states its phase, its domain and subdomain, its change, and the rule set it
            was authored under
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
            detail: belief is asserted, not suspected ({token!r}) — state it as a belief or move it to Known Facts
          intent: P0 must not promote a System Belief to a Known Fact
        - id: REGISTER_CELL_UNRESOLVED
          identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/allOf/3
          check: UNRESOLVED_MARKER_ABSENT
          params:
            exempt:
            - clarification_requests
            detail: '{column!r} declares the question unanswered ({marker}) rather than answering it — ask it
              as a clarification, do not hedge it in a register'
          intent: an unanswered question left in a register reads as decided to every later phase
        - id: BLOCKING_CLARIFICATION_OUTSTANDING
          identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/allOf/4
          check: ROW_ABSENT_WHEN
          register: clarification_requests
          params:
            column: Blocking
            value: 'YES'
            detail: a blocking clarification is unanswered — resolve it with the named owner and fold the answer
              into the document before any phase consumes it
          intent: a blocking question the next phase never sees is answered by invention
        - id: BUSINESS_CLARIFICATION_OUTSTANDING
          identity: transformation.schemas.REGISTER_SCHEMA_P0_V0#/allOf/5
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
