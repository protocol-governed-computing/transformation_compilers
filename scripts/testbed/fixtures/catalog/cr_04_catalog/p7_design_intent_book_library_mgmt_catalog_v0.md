# Stage 7 — Design Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p7
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_04_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: The form the publication year takes at the boundary of registering a further edition
    business_fact: Three of the four statements of the form say number, and every year the library supplies is a number.
    resolution: '`publication_year` is declared `integer` in `book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0`, matching its two sibling boundaries.'
    source_finding: {phase: p6, register: boundary_rules, key: A_YEAR_IS_A_NUMBER}
  - decision: Which requirements a correction keeps
    business_fact: Its four steps read the record named and the details being changed, and nothing else the request supplied.
    resolution: '`book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1` is authored requiring the five its steps read, and supersedes `..._V0`. A boundary is rendered whole from the design, so a requirement is withdrawn by authoring the successor that does not carry it, never by amending the predecessor to say less than it said.'
    source_finding: {phase: p6, register: boundary_rules, key: REQUIRES_ONLY_WHAT_IT_USES}
  - decision: Whether registering a work is corrected here
    business_fact: Its steps read `subject` at the top of the request and rebuild the details of the book themselves; every present caller sends `subject` nested inside the details it supplies.
    resolution: '`book_library_mgmt::IN_REGISTER_BOOK_V0` is unchanged. Requiring `subject` moves the boundary and every caller together, and no caller moves inside this change.'
    source_finding: {phase: p6, register: boundary_rules, key: NO_CORRECT_REQUEST_BECOMES_HARDER}
  - decision: Whether any workflow changes
    business_fact: The three operations read exactly what they read today.
    resolution: No workflow, capability contract, capability transform, side effect or store is altered. Each of the three boundaries is re-rendered whole; the act it admits is restated unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - decision: Whether authority is reached
    business_fact: The three things that decide who may perform an operation are read by no step of any of the subdomain's ten operations.
    resolution: '`staff_credentials`, `authorization_rules` and `staff_id` are restated unchanged in all three boundaries, in the same form and with the same requiredness.'
    source_finding: {phase: p6, register: boundary_rules, key: AUTHORITY_IS_UNTOUCHED}
  existing_inventory:
  - fqdn: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    action: EXTEND
    summary: The boundary that admits a request to register a further edition of a work the catalog already holds
    reason: One requirement changes form; the other ten are restated unchanged, because an EXTEND re-renders the boundary whole.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: REPLACE
    summary: ''
    reason: Requires three things no step of its operation reads. Stood down and superseded, because withdrawing a requirement makes the boundary say less than it said, and an amendment may only say more.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: book_library_mgmt::IN_REGISTER_BOOK_V0
    action: REVIEW
    summary: The boundary that admits a request to register a work, its first edition and that edition's first physical copy
    reason: 'Requires ten things where its act reads eleven. Unchanged: the missing requirement is one every present caller sends nested inside the details of the book rather than where the act reads it.'
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    action: REUSE
    summary: The governed sequence that registers a further edition of a work already held
    reason: Reads all eleven things its boundary requires. Named because the boundary is its entry node and an EXTEND must state the act it admits.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: REPLACE
    summary: ''
    reason: Names the boundary being superseded as its entry. An act states the boundary that admits it, so a successor boundary means a successor act. Nothing consumes this act, so the substitution reaches nothing further.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    action: REVIEW
    summary: The governed sequence that registers a work, its first edition and that edition's first physical copy
    reason: Reads eleven things, one of which its boundary does not require, and rebuilds the details of the book from the top of the request. Unchanged, and named as the evidence that the third correction reaches a caller.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: book_library_mgmt::AC_LIBRARY_STAFF_V0
    action: REUSE
    summary: The actor whose authorization every catalog operation binds
    reason: The actor all three acts run as. Named because an EXTEND re-renders the boundary and the act it admits must state its actor.
    source_finding: {phase: p6, register: ownership, row: 5}
  - fqdn: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    action: REUSE
    summary: Decides whether the staff member may perform the operation
    reason: The first act of all three sequences, and what consumes the three authority requirements. Unchanged.
    source_finding: {phase: p6, register: ownership, row: 5}
  - fqdn: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    action: REUSE
    summary: Checks a submitted description against the schema supplied with it
    reason: Named by two of the three acts; what reads `publication_year` in the form the boundary declares.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    action: REUSE
    summary: Resolves the record a correction names
    reason: What reads `identity_key`, one of the five requirements the correction keeps.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: REUSE
    summary: Changes the details of a resolved record
    reason: What reads `updated_fields`, and what reads none of the three requirements withdrawn.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    action: REUSE
    summary: Records that a catalog operation occurred
    reason: The last act of all three sequences. Unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: book_library_mgmt::CC_RESOLVE_WORK_V0
    action: REUSE
    summary: Resolves the work a further edition attaches to
    reason: Named by the act that registers a further edition; unchanged, and restated because the boundary above it is re-rendered whole.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    action: REUSE
    summary: Claims the identity of an edition
    reason: Named by two of the three acts; what reads the title, the author and the publication year.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    action: REUSE
    summary: Registers a further edition against a resolved work
    reason: Named by the act that registers a further edition; unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    action: REUSE
    summary: Claims the identity of a work
    reason: Named by the act that registers a work; unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    action: REUSE
    summary: Claims the barcode of a physical copy
    reason: Named by the act that registers a work; unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: book_library_mgmt::CC_REGISTER_BOOK_V0
    action: REUSE
    summary: Registers an edition against a claimed identity
    reason: Named by the act that registers a work; what reads the subject the boundary now requires.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    action: REUSE
    summary: Puts a physical copy on a shelf
    reason: Named by the act that registers a work; unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    action: REUSE
    summary: Binds the catalog's acts to the capabilities and stores that carry them
    reason: Named because the three acts are bound through it; unchanged by this change.
    source_finding: {phase: p6, register: ownership, row: 6}
  - fqdn: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    action: REUSE
    summary: The moment the act announces when a correction completes
    reason: Announced at the act's successful ending. Unchanged, and named because an EXTEND re-renders the act whole and the announcement must be restated with it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    action: REVIEW
    summary: Declares the six stores the catalog owns and the paths they occupy
    reason: Declares no form for any detail it holds, which is why the form of a publication year rests on agreement rather than on a declaration. Unchanged by this change.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  new_artifacts:
  - capability: Admitting a request to correct bibliographic information
    family: IN
    code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    summary: A request to change a registered book's description
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 2}
  - capability: The three operations
    family: WF
    code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    summary: Corrects what the library publishes about a registered book
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p6, register: governance_outcome, row: 2}
  rb_declarations:
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    cs_bindings:
    - Unchanged
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: ownership, row: 6}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    cs_bindings:
    - Unchanged
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: ownership, row: 6}
  execution_topology:
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: IN_REGISTER_ADDITIONAL_EDITION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_RESOLVE_WORK_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_RESOLVE_WORK_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ADDITIONAL_EDITION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ADDITIONAL_EDITION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_ADDITIONAL_EDITION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REGISTER_ADDITIONAL_EDITION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REGISTER_ADDITIONAL_EDITION_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_RESOLVE_BOOK_IDENTITY_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  cc_composition: []
  step_bindings:
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_ADDITIONAL_EDITION
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_ADDITIONAL_EDITION
        staff_id: $.payload.staff_id
        subject: $.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: author
    bound_to: payload.author
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: publication_year
    bound_to: payload.publication_year
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_fields
    bound_to:
      literal:
        author: $.payload.author
        identity_key: $.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
        publication_year: $.payload.publication_year
        state: REGISTERED
        subject: $.payload.subject
        title: $.payload.title
        work_key: $.results.CC_RESOLVE_WORK_V0.work_key
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_ADDITIONAL_EDITION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_schema
    bound_to: payload.edition_schema
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_ADDITIONAL_EDITION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_ADDITIONAL_EDITION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: author
    bound_to: payload.author
    source_finding: {phase: p7, register: execution_topology, key: CC_RESOLVE_WORK_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: CC_RESOLVE_WORK_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_fields
    bound_to: payload.edition_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_schema
    bound_to: payload.edition_schema
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_fields
    bound_to: payload.work_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_schema
    bound_to: payload.work_schema
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: UPDATE_BIBLIOGRAPHIC_INFORMATION
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: UPDATE_BIBLIOGRAPHIC_INFORMATION
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_RESOLVE_BOOK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: updated_fields
    bound_to: payload.updated_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  interface_fields:
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: The credentials of the staff member making the request. Consumed by the decision about who may act.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: null
    meaning: The rules that decide whether this staff member may perform the operation.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: The staff member accountable for the request.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: null
    meaning: The title of the work the edition belongs to.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: null
    meaning: The author of the work the edition belongs to.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: null
    meaning: The year the edition was published. Stated as a number, as the catalog holds it and as both sibling boundaries declare it.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: subject
    type: array
    required: 'YES'
    default: null
    meaning: The subject headings of the edition.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_fields
    type: object
    required: 'YES'
    default: null
    meaning: The details of the edition being registered.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_schema
    type: object
    required: 'YES'
    default: null
    meaning: The description the edition is checked against.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: work_fields
    type: object
    required: 'YES'
    default: null
    meaning: The details of the work the edition is attached to.
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: work_schema
    type: object
    required: 'YES'
    default: null
    meaning: The description the work is checked against.
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: null
    meaning: The credentials of the staff member making the request. Consumed by the decision about who may act.
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: null
    meaning: The rules that decide whether this staff member may perform the operation.
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: null
    meaning: The staff member accountable for the request.
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: null
    meaning: The record being corrected.
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    direction: INPUT
    field: updated_fields
    type: object
    required: 'YES'
    default: null
    meaning: The details being changed. A correction supplies these and does not restate the fields it leaves alone.
  implementation_bindings: []
  vocabulary_extensions: []
  runtime_policies: []
  artifact_properties:
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    property: core.workflow
    value: WF_REGISTER_ADDITIONAL_EDITION_V0
    source_finding: {phase: p7, register: execution_topology, key: WF_REGISTER_ADDITIONAL_EDITION_V0}
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    property: core.workflow
    value: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    source_finding: {phase: p7, register: execution_topology, key: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    source_finding: {phase: p7, register: existing_inventory, key: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    property: supersedes
    value:
    - book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    source_finding: {phase: p7, register: existing_inventory, key: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    property: supersedes
    value:
    - book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    source_finding: {phase: p7, register: existing_inventory, key: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: EXTEND
    subdomain: catalog
    count: '1'
    artifacts: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
  - action: REPLACE
    subdomain: catalog
    count: '2'
    artifacts: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
  - action: NEW
    subdomain: catalog
    count: '2'
    artifacts: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
  generation_provenance: []
  declared_reach: []
  refusal_discharge:
  - operation: Registering a further edition
    refused_when: The publication year is not supplied
    act: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    outcome: NACK
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - operation: Correcting bibliographic information
    refused_when: The record to correct is not named
    act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    outcome: NACK
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - operation: Correcting bibliographic information
    refused_when: No changed fields are supplied
    act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    outcome: NACK
    source_finding: {phase: p1, register: operation_refusals, row: 3}
  refusal_deferrals: []
  refusal_governance_discharge: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases: []
  test_case_values: []
  withdrawn_facts: null
```

HOW it is built. FQDNs, topology, schemas and bindings. The full dossier is reviewed as a body.

---

## 1. Design Decisions Resolution

---

## 2. Artifact Inventory — Existing Artifacts

---

## 3. Artifact Family Mapping — New Artifacts

---

## 4. Runtime Binding (RB) Declarations

---

## 5. Execution Topology

---

## 6. Capability Composition

---

## 7. Step Bindings

---

## 8. Interface Fields

---

## 9. Implementation Bindings

---

## 10. Vocabulary Extensions

---

## 11. Runtime Policies

---

## 12. Artifact Properties

---

## 13. STRUCTURE Stores

---

## 14. Transport Bindings

---

## 15. Artifact Summary

---

## 16. Generation Provenance

---

## 17. Declared Reach

---

## 18. Refusal Discharge

---

## 19. Refusal Deferrals

---

## 20. Refusal Governance Discharge

---

## 21. Molecule Steps

---

## 22. Molecule Step Bindings

---

## 23. Test Cases

---

## 24. Test Case Values

---

## 25. Withdrawn Facts

---

## Gate 1 — Design Approval

**Gate 1 closes here.** Stages 0 through 7 are presented for review as a body — a unified review of
the complete design, not a per-stage approval. Approval authorizes Stage 8, the Authoring Mandate.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`10aa26e1582f…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the amendment of the one boundary §2 marks EXTEND, the authoring of
the successor boundary and successor act §3 declares, and the standing down of the two artifacts §2
marks REPLACE. It authorizes nothing else, and in particular it does not authorize requiring the
subject at the boundary that registers a work.

That third correction was designed, emitted and withdrawn, and the withdrawal is the reason this
closure differs from the one first written. The act reads the subject at the top of the request and
rebuilds the details of the book itself; every caller sends the subject nested inside the details it
supplies. Requiring it turned the library's own exercise of the catalog from failing at the second
edition to failing at the first registration. The defect is real and is deferred with its ground
recorded, to a change where the boundary and its callers move together.

The shape of §2 changed at this closure and the reason is worth naming. A boundary is rendered whole
from the design, so an amendment may say more than its predecessor and may never say less; withdrawing
three requirements no step reads is therefore a supersession, not an amendment. The act that named the
withdrawn boundary as its entry is superseded with it, because an act states the boundary that admits
it. Nothing consumes that act, so the substitution stops there.

One decision of §1 is worth naming at this closure, because it reads against a constraint the seed
states. The seed rules that no operation gains a requirement in this change. Registering a work
gains one. The approval takes the constraint to protect a requester rather than a declaration: the
act already reads the subject, and every request the library makes already supplies it, so no correct
request becomes harder to make. A requirement that asked for something new would not be permitted by
the same reading.
