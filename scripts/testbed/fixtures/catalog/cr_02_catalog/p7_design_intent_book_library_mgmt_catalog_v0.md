# Design Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p7
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_02_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: The record the previous change calls a book is an edition; the work is added above it
    business_fact: Editions of one work share a title and an author and differ by publication year
    resolution: No existing identity changes. A work store and a work identity registry are added, and the edition record gains the key of the work it belongs to
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: The work's identity is formed by a new transform
    business_fact: The edition key transform is reached by every catalog operation and 23 artifacts depend on it
    resolution: A second transform forms the work key from title and author; the two are independent and neither can alter the other
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: The work is claimed through the same registry mechanism the edition is claimed through
    business_fact: Register-if-absent gives the atomic uniqueness a work identity needs
    resolution: A registry store claims the work key; a claim that finds the key already held yields ALREADY_EXISTS, which the registration treats as the work having been found rather than as a refusal
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: The work store and the work identity registry are declared in the catalog's own storage declaration
    business_fact: A subdomain declares its stores once and binds them once
    resolution: Both stores are added to the existing storage declaration and reached through the existing runtime binding
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: Registering an edition of a new work extends the existing registration; registering an additional edition is a new operation
    business_fact: The existing registration creates the work and requires a first copy; an additional edition does neither
    resolution: The existing workflow gains a work claim before its claims; a second workflow resolves an existing work and claims only the edition
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: The work claim is placed among the existing claims, before any write
    business_fact: A refused registration must leave nothing behind
    resolution: The work claim runs after validation and before the edition and barcode claims, so every claim still precedes every write
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - decision: Search is extended rather than duplicated, and answers at the level of the work
    business_fact: Two searches would leave staff choosing which one answers their question
    resolution: The existing search gains a grouping step after its selection step; the search terms and the records it selects are unchanged
    source_finding: {phase: p4, register: design_decisions, row: 7}
  - decision: Retrieval stays edition retrieval and carries a summary of the work
    business_fact: The business asked for one retrieval carrying a summary, not a second operation
    resolution: The existing retrieval gains a read of the work record; the edition and its copies are assembled as before
    source_finding: {phase: p4, register: design_decisions, row: 8}
  - decision: A work is never retired
    business_fact: A work whose editions are all retired is simply that
    resolution: No retirement operation names the work, and no routing reaches the work store from a retirement
    source_finding: {phase: p4, register: design_decisions, row: 9}
  existing_inventory:
  - fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    action: EXTEND
    summary: Declares the stores the catalog owns and the paths they occupy
    reason: Gains the work record store and the work identity registry alongside the five stores the catalog already owns
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0'}
  - fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    action: EXTEND
    summary: Binds the catalog's workflows to the stores and mechanisms they use
    reason: Binds the new workflow to the same substrates and the same storage declaration the catalog already uses
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::RB_CATALOG_BINDINGS_V0'}
  - fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    action: EXTEND
    summary: Registers a work with its first edition and that edition's first physical copy
    reason: 'Gains one node: the work claim, placed after validation and before every other claim'
    source_finding: {phase: p6, register: ownership, key: Register an edition of a work the catalog does not yet hold}
  - fqdn: book_library_mgmt::CC_REGISTER_BOOK_V0
    action: EXTEND
    summary: Validates, assembles and writes an edition record against the work it belongs to
    reason: The edition record it assembles now carries the key of the work the edition belongs to
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::CC_REGISTER_BOOK_V0'}
  - fqdn: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    action: EXTEND
    summary: Confirms a registration carries what a work and an edition require, before any identity is claimed
    reason: Confirms the submission carries what a work requires as well as what an edition requires
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0'}
  - fqdn: book_library_mgmt::CC_SEARCH_CATALOG_V0
    action: EXTEND
    summary: Selects the registered editions matching a subject or title and groups them under their work
    reason: Groups the matching editions under the work they belong to, so the answer is one result per work
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::CC_SEARCH_CATALOG_V0'}
  - fqdn: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    action: EXTEND
    summary: Assembles an edition, the physical copies of it, and the record of the work it belongs to
    reason: Reads the work record so the retrieval carries a summary of the work the edition belongs to
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0'}
  - fqdn: book_library_mgmt::AC_LIBRARY_STAFF_V0
    action: REUSE
    summary: ''
    reason: The actor every catalog workflow runs as, including the one this change adds — authorization is read from what the caller supplies and granted nowhere
    source_finding: {phase: p6, register: ownership, key: Confirm the staff member performing an operation is authorized}
  - fqdn: book_library_mgmt::IN_REGISTER_BOOK_V0
    action: REUSE
    summary: ''
    reason: The registration's entry point is unchanged — what a caller supplies is what it supplied before, and only the sequence it starts gains a node
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::CC_REGISTER_BOOK_V0'}
  - fqdn: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    action: REVIEW
    summary: ''
    reason: Examined and deliberately not widened; it continues to form the edition key from three attributes
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0'}
  - fqdn: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    action: REUSE
    summary: ''
    reason: Claims the edition's identity unchanged, and is the precedent the work claim follows
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0'}
  - fqdn: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    action: REUSE
    summary: ''
    reason: Every operation this change adds reaches it first, as every existing operation does
    source_finding: {phase: p6, register: ownership, key: Confirm the staff member performing an operation is authorized}
  - fqdn: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    action: REUSE
    summary: ''
    reason: Records the operations this change adds into the trail it already appends to
    source_finding: {phase: p6, register: ownership, key: Record every performed operation in the catalog's audit trail}
  - fqdn: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    action: REUSE
    summary: ''
    reason: A copy already belongs to exactly one record, and that record is an edition
    source_finding: {phase: p6, register: ownership, key: Register a physical copy against exactly one edition}
  - fqdn: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    action: REUSE
    summary: ''
    reason: Barcode uniqueness is unaffected by the work abstraction
    source_finding: {phase: p6, register: ownership, key: Register a physical copy against exactly one edition}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    action: REUSE
    summary: ''
    reason: Holds the work record as it holds the edition and copy records
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    action: REUSE
    summary: ''
    reason: Claims the work key as it claims the edition key and the barcode
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    action: REUSE
    summary: ''
    reason: Appends the operations this change adds to the catalog's trail
    source_finding: {phase: p6, register: storage_governance, key: An unamendable trail of every operation performed}
  - fqdn: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    action: REVIEW
    summary: ''
    reason: Examined and not extended; it selects records and the grouping is a separate transform
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_transforms::CT_PURE_FILTER_RECORDS_V0'}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: ''
    reason: Assembles the work record as it assembles the edition and copy records
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every work the library has catalogued}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    action: REUSE
    summary: ''
    reason: Confirms a submission carries the fields its schema declares, for the work as for the edition
    source_finding: {phase: p6, register: ownership, key: Validate that a registration carries what a work and an edition require}
  - fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    action: REUSE
    summary: ''
    reason: Compares two values for equality, unchanged — the update uses it to confirm an edition's identity did not change
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    action: REUSE
    summary: ''
    reason: Turns a validation result into a refusal, unchanged
    source_finding: {phase: p6, register: ownership, key: Validate that a registration carries what a work and an edition require}
  - fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: EXTEND
    summary: Changes a registered edition's descriptive content and refuses a change that would duplicate another edition
    reason: The record it writes back now carries the work the edition belongs to, which it previously dropped
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0'}
  new_artifacts:
  - capability: Form the identifying key of a work from its title and author
    family: CT
    code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    summary: Forms the single key claimed for a work from its title and author
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_FORM_WORK_IDENTITY_KEY_V0}
  - capability: Select records matching criteria, answering none when none match
    family: CT
    code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    summary: Selects the records matching stated criteria and returns none when none match
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_SELECT_RECORDS_V0}
  - capability: Group selected records by an attribute they share
    family: CT
    code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    summary: Groups records by the value of a named attribute, returning one group per distinct value
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CT_PURE_GROUP_RECORDS_V0}
  - capability: Claim a work's identity so that two registrations of one work do not produce two works
    family: CC
    code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    summary: Forms the work key, claims it, and writes the work record when the claim is new
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CLAIM_WORK_IDENTITY_V0}
  - capability: Resolve the work an edition belongs to
    family: CC
    code: book_library_mgmt::CC_RESOLVE_WORK_V0
    summary: Forms the work key, resolves it against the registry, and reads the work record it names
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_RESOLVE_WORK_V0}
  - capability: Register an additional edition of an existing work
    family: CC
    code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    summary: Assembles the edition record against a resolved work and writes it
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_REGISTER_ADDITIONAL_EDITION_V0}
  - capability: Admit a request to register an additional edition of an existing work
    family: IN
    code: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    summary: A request to register a further edition of a work the catalog already holds
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_REGISTER_ADDITIONAL_EDITION_V0}
  - capability: Register an additional edition of an existing work
    family: WF
    code: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    summary: The governed sequence that registers a further edition of an existing work
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_REGISTER_ADDITIONAL_EDITION_V0}
  - capability: Recognise the moment a work enters the catalog
    family: EV
    code: book_library_mgmt::EV_WORK_REGISTERED_V0
    summary: The moment a work enters the catalog, created by the edition that evidences it
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: EV_WORK_REGISTERED_V0}
  rb_declarations:
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every work the library has catalogued}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_BOOK_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: An atomic claim on each work's identity}
  execution_topology:
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_REGISTER_ADDITIONAL_EDITION_V0}
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
    source_finding: {phase: p7, register: new_artifacts, key: CC_RESOLVE_WORK_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_REGISTER_ADDITIONAL_EDITION_V0}
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
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::IN_REGISTER_BOOK_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: WF_REGISTER_BOOK_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      ALREADY_EXISTS: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CLAIM_WORK_IDENTITY_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_BOOK_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_CLAIM_COPY_BARCODE_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_REGISTER_BOOK_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_REGISTER_BOOK_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: existing_inventory, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REGISTER_BOOK_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REGISTER_BOOK_V0}
  cc_composition:
  - cc_code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: '1'
    step_name: form_work_key
    capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    kind: CT
    operation: FORM_WORK_IDENTITY_KEY
    store: null
    consumes:
    - title
    - author
    produces:
    - work_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
      out:
        work_key: work_key
  - cc_code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: '2'
    step_name: claim_work
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: WORK_IDENTITY_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    routing:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: ALREADY_EXISTS
    interface: null
  - cc_code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: '3'
    step_name: assemble_work_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - work_fields
    produces:
    - work_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: work_fields
      out:
        record: work_record
  - cc_code: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: '4'
    step_name: write_work_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: WORKS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: '1'
    step_name: form_work_key
    capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    kind: CT
    operation: FORM_WORK_IDENTITY_KEY
    store: null
    consumes:
    - title
    - author
    produces:
    - work_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
      out:
        work_key: work_key
  - cc_code: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: '2'
    step_name: resolve_work_claim
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: WORK_IDENTITY_REGISTRY
    consumes:
    - key_or_address
    produces:
    - target_ref
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: '3'
    step_name: read_work_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: WORKS
    consumes:
    - key
    produces:
    - value
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '1'
    step_name: validate_edition_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: VALIDATE_RECORD_STRUCTURE
    store: null
    consumes:
    - edition_fields
    - edition_schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: edition_fields
        schema: edition_schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '2'
    step_name: assemble_edition_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - edition_fields
    produces:
    - edition_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: edition_fields
      out:
        record: edition_record
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '3'
    step_name: write_edition_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: BOOKS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '1'
    step_name: form_work_key
    capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    kind: CT
    operation: FORM_WORK_IDENTITY_KEY
    store: null
    consumes:
    - title
    - author
    produces:
    - work_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
      out:
        work_key: work_key
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '2'
    step_name: validate_book_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: VALIDATE_RECORD_STRUCTURE
    store: null
    consumes:
    - book_fields
    - book_schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: book_fields
        schema: book_schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '3'
    step_name: assemble_book_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - book_fields
    produces:
    - book_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: book_fields
      out:
        record: book_record
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '4'
    step_name: write_book_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: BOOKS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: '1'
    step_name: validate_book_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: VALIDATE_RECORD_STRUCTURE
    store: null
    consumes:
    - book_fields
    - book_schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: book_fields
        schema: book_schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: '2'
    step_name: validate_work_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: VALIDATE_RECORD_STRUCTURE
    store: null
    consumes:
    - work_fields
    - work_schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: work_fields
        schema: work_schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: '3'
    step_name: require_submission_complete
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - barcode
    - book_fields
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: barcode
        rules: rules
      out:
        valid: valid
  - cc_code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: '1'
    step_name: select_book_records
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: SELECT
    store: BOOKS
    consumes: null
    produces:
    - records
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: '2'
    step_name: select_matching_books
    capability: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    kind: CT
    operation: FILTER_RECORDS
    store: null
    consumes:
    - records
    - search_criteria
    produces:
    - matching_books
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: records
        filter: search_criteria
      out:
        extracted: matching_books
  - cc_code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: '3'
    step_name: group_editions_by_work
    capability: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    kind: CT
    operation: GROUP_RECORDS
    store: null
    consumes:
    - matching_books
    - group_by
    produces:
    - matching_works
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: matching_books
        attribute: group_by
      out:
        grouped: matching_works
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '1'
    step_name: read_book_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: BOOKS
    consumes:
    - key
    produces:
    - value
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '2'
    step_name: form_work_key
    capability: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    kind: CT
    operation: FORM_WORK_IDENTITY_KEY
    store: null
    consumes:
    - title
    - author
    produces:
    - work_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
      out:
        work_key: work_key
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '3'
    step_name: read_work_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: WORKS
    consumes:
    - key
    produces:
    - value
    routing:
      SUCCESS: continue
      NOT_FOUND: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '4'
    step_name: select_copy_records
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: SELECT
    store: PHYSICAL_COPIES
    consumes: null
    produces:
    - records
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: '5'
    step_name: select_copies_of_book
    capability: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    kind: CT
    operation: SELECT_RECORDS
    store: null
    consumes:
    - records
    - copy_criteria
    produces:
    - copies_held
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: records
        filter: copy_criteria
      out:
        extracted: copies_held
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '1'
    step_name: read_book_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: BOOKS
    consumes:
    - key
    produces:
    - book_record
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: NOT_FOUND
    interface: null
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '2'
    step_name: form_updated_identity_key
    capability: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    kind: CT
    operation: FORM_BOOK_IDENTITY_KEY
    store: null
    consumes:
    - updated_fields
    produces:
    - updated_identity_key
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        title: title
        author: author
        publication_year: publication_year
      out:
        identity_key: updated_identity_key
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '3'
    step_name: compare_identity
    capability: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    kind: CT
    operation: COMPARE_EQUAL
    store: null
    consumes:
    - identity_key
    - updated_identity_key
    produces:
    - identity_unchanged
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        left: identity_key
        right: updated_identity_key
      out:
        is_equal: identity_unchanged
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '4'
    step_name: require_identity_unchanged
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - identity_unchanged
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: identity_unchanged
        rules: rules
      out:
        valid: valid
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '5'
    step_name: assemble_updated_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - updated_fields
    produces:
    - updated_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: updated_fields
      out:
        record: updated_record
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '6'
    step_name: write_updated_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: BOOKS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  step_bindings:
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: form_work_key
    direction: INPUT
    field: title
    bound_to: inputs.title
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: form_work_key
    direction: INPUT
    field: author
    bound_to: inputs.author
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: form_work_key
    direction: OUTPUT
    field: work_key
    bound_to: capability_result.work_key
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: INPUT
    field: key
    bound_to: results.form_work_key.work_key
    source_finding: {phase: p7, register: cc_composition, key: claim_work}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
    source_finding: {phase: p7, register: cc_composition, key: claim_work}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: INPUT
    field: target_ref
    bound_to:
      literal: WORKS
    source_finding: {phase: p7, register: cc_composition, key: claim_work}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
    source_finding: {phase: p7, register: cc_composition, key: claim_work}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: claim_work
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: claim_work}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: assemble_work_record
    direction: INPUT
    field: fields
    bound_to: inputs.work_fields
    source_finding: {phase: p7, register: cc_composition, key: assemble_work_record}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: assemble_work_record
    direction: OUTPUT
    field: work_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_work_record}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: write_work_record
    direction: INPUT
    field: key
    bound_to: results.form_work_key.work_key
    source_finding: {phase: p7, register: cc_composition, key: write_work_record}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: write_work_record
    direction: INPUT
    field: value
    bound_to: results.assemble_work_record.work_record
    source_finding: {phase: p7, register: cc_composition, key: write_work_record}
  - owner: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    step: write_work_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_work_record}
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: form_work_key
    direction: INPUT
    field: title
    bound_to: inputs.title
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: form_work_key
    direction: INPUT
    field: author
    bound_to: inputs.author
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: form_work_key
    direction: OUTPUT
    field: work_key
    bound_to: capability_result.work_key
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: resolve_work_claim
    direction: INPUT
    field: key_or_address
    bound_to: results.form_work_key.work_key
    source_finding: {phase: p7, register: cc_composition, key: resolve_work_claim}
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: resolve_work_claim
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
    source_finding: {phase: p7, register: cc_composition, key: resolve_work_claim}
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: resolve_work_claim
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: resolve_work_claim}
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: read_work_record
    direction: INPUT
    field: key
    bound_to: results.form_work_key.work_key
    source_finding: {phase: p7, register: cc_composition, key: read_work_record}
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: read_work_record
    direction: OUTPUT
    field: work_record
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_work_record}
  - owner: book_library_mgmt::CC_RESOLVE_WORK_V0
    step: read_work_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_work_record}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: validate_edition_fields
    direction: INPUT
    field: record
    bound_to: inputs.edition_fields
    source_finding: {phase: p7, register: cc_composition, key: validate_edition_fields}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: validate_edition_fields
    direction: INPUT
    field: schema
    bound_to: inputs.edition_schema
    source_finding: {phase: p7, register: cc_composition, key: validate_edition_fields}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: validate_edition_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: validate_edition_fields}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: assemble_edition_record
    direction: INPUT
    field: fields
    bound_to: inputs.edition_fields
    source_finding: {phase: p7, register: cc_composition, key: assemble_edition_record}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: assemble_edition_record
    direction: OUTPUT
    field: edition_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_edition_record}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: write_edition_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: write_edition_record}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: write_edition_record
    direction: INPUT
    field: value
    bound_to: results.assemble_edition_record.edition_record
    source_finding: {phase: p7, register: cc_composition, key: write_edition_record}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: write_edition_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_edition_record}
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_book_records
    direction: OUTPUT
    field: records
    bound_to: capability_result.records
    source_finding: {phase: p7, register: cc_composition, key: select_book_records}
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_book_records
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: select_book_records}
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_matching_books
    direction: INPUT
    field: source
    bound_to: results.select_book_records.records
    source_finding: {phase: p7, register: cc_composition, key: select_matching_books}
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_matching_books
    direction: INPUT
    field: filter
    bound_to: inputs.search_criteria
    source_finding: {phase: p7, register: cc_composition, key: select_matching_books}
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: select_matching_books
    direction: OUTPUT
    field: matching_books
    bound_to: capability_result.extracted
    source_finding: {phase: p7, register: cc_composition, key: select_matching_books}
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: group_editions_by_work
    direction: INPUT
    field: source
    bound_to: results.select_matching_books.matching_books
    source_finding: {phase: p7, register: cc_composition, key: group_editions_by_work}
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: group_editions_by_work
    direction: INPUT
    field: attribute
    bound_to:
      literal: work_key
    source_finding: {phase: p7, register: cc_composition, key: group_editions_by_work}
  - owner: book_library_mgmt::CC_SEARCH_CATALOG_V0
    step: group_editions_by_work
    direction: OUTPUT
    field: matching_works
    bound_to: capability_result.grouped
    source_finding: {phase: p7, register: cc_composition, key: group_editions_by_work}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: OUTPUT
    field: value
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: form_work_key
    direction: INPUT
    field: title
    bound_to: results.read_book_record.value.title
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: form_work_key
    direction: INPUT
    field: author
    bound_to: results.read_book_record.value.author
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: form_work_key
    direction: OUTPUT
    field: work_key
    bound_to: capability_result.work_key
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_work_record
    direction: INPUT
    field: key
    bound_to: results.form_work_key.work_key
    source_finding: {phase: p7, register: cc_composition, key: read_work_record}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_work_record
    direction: OUTPUT
    field: work_record
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_work_record}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copy_records
    direction: OUTPUT
    field: records
    bound_to: capability_result.records
    source_finding: {phase: p7, register: cc_composition, key: select_copy_records}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copies_of_book
    direction: INPUT
    field: source
    bound_to: results.select_copy_records.records
    source_finding: {phase: p7, register: cc_composition, key: select_copies_of_book}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copies_of_book
    direction: INPUT
    field: filter
    bound_to: inputs.copy_criteria
    source_finding: {phase: p7, register: cc_composition, key: select_copies_of_book}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copies_of_book
    direction: OUTPUT
    field: copies_held
    bound_to: capability_result.extracted
    source_finding: {phase: p7, register: cc_composition, key: select_copies_of_book}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_work_fields
    direction: INPUT
    field: record
    bound_to: inputs.work_fields
    source_finding: {phase: p7, register: cc_composition, key: validate_work_fields}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_work_fields
    direction: INPUT
    field: schema
    bound_to: inputs.work_schema
    source_finding: {phase: p7, register: cc_composition, key: validate_work_fields}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_work_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: validate_work_fields}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: form_work_key
    direction: INPUT
    field: title
    bound_to: inputs.book_fields.title
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: form_work_key
    direction: INPUT
    field: author
    bound_to: inputs.book_fields.author
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: form_work_key
    direction: OUTPUT
    field: work_key
    bound_to: capability_result.work_key
    source_finding: {phase: p7, register: cc_composition, key: form_work_key}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: assemble_book_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        title: $.inputs.book_fields.title
        author: $.inputs.book_fields.author
        publication_year: $.inputs.book_fields.publication_year
        subject: $.inputs.book_fields.subject
        state: $.inputs.book_fields.state
        work_key: $.results.form_work_key.work_key
    source_finding: {phase: p7, register: cc_composition, key: assemble_book_record}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: assemble_book_record
    direction: OUTPUT
    field: book_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_book_record}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
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
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: CC_RESOLVE_WORK_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: author
    bound_to: payload.author
    source_finding: {phase: p7, register: execution_topology, key: CC_RESOLVE_WORK_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_BOOK_IDENTITY_V0}
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
    step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
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
    field: edition_fields
    bound_to:
      literal:
        identity_key: $.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
        subject: $.payload.subject
        state: REGISTERED
        work_key: $.results.CC_RESOLVE_WORK_V0.work_key
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_ADDITIONAL_EDITION_V0}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
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
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_WORK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: author
    bound_to: payload.author
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_WORK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: work_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_WORK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_schema
    bound_to:
      literal:
        required:
        - title
        - author
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
        subject: $.payload.subject
        state: REGISTERED
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_BOOK_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_fields
    bound_to: payload.book_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_schema
    bound_to: payload.book_schema
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: author
    bound_to: payload.author
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: publication_year
    bound_to: payload.publication_year
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_BOOK_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_schema
    bound_to: payload.book_schema
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_BOOK_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_COPY_BARCODE_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    bound_to: payload.copy_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_BOOK
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_BOOK
        staff_id: $.payload.staff_id
        subject: $.payload.title
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_book_fields
    direction: INPUT
    field: record
    bound_to: inputs.book_fields
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_book_fields
    direction: INPUT
    field: schema
    bound_to: inputs.book_schema
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_book_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: require_submission_complete
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        barcode: $.inputs.barcode
        subject: $.inputs.book_fields.subject
    source_finding: {phase: p7, register: cc_composition, key: require_submission_complete}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: require_submission_complete
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: barcode
        op: neq
        value: ''
      - field: subject
        op: neq
        value: []
    source_finding: {phase: p7, register: cc_composition, key: require_submission_complete}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: require_submission_complete
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_submission_complete}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: validate_book_fields
    direction: INPUT
    field: record
    bound_to: inputs.book_fields
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: validate_book_fields
    direction: INPUT
    field: schema
    bound_to: inputs.book_schema
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: validate_book_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: write_book_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: write_book_record}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: write_book_record
    direction: INPUT
    field: value
    bound_to: results.assemble_book_record.book_record
    source_finding: {phase: p7, register: cc_composition, key: write_book_record}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: write_book_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_book_record}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: OUTPUT
    field: book_record
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copy_records
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: select_copy_records}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copies_of_book
    direction: INPUT
    field: source
    bound_to: results.select_copy_records.records
    source_finding: {phase: p7, register: cc_composition, key: select_copies_of_book}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copies_of_book
    direction: INPUT
    field: filter
    bound_to: inputs.copy_criteria
    source_finding: {phase: p7, register: cc_composition, key: select_copies_of_book}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: select_copies_of_book
    direction: OUTPUT
    field: copies_held
    bound_to: capability_result.extracted
    source_finding: {phase: p7, register: cc_composition, key: select_copies_of_book}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: read_book_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: read_book_record
    direction: OUTPUT
    field: book_record
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: read_book_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: form_updated_identity_key
    direction: INPUT
    field: title
    bound_to: inputs.updated_fields.title
    source_finding: {phase: p7, register: cc_composition, key: form_updated_identity_key}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: form_updated_identity_key
    direction: INPUT
    field: author
    bound_to: inputs.updated_fields.author
    source_finding: {phase: p7, register: cc_composition, key: form_updated_identity_key}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: form_updated_identity_key
    direction: INPUT
    field: publication_year
    bound_to: inputs.updated_fields.publication_year
    source_finding: {phase: p7, register: cc_composition, key: form_updated_identity_key}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: form_updated_identity_key
    direction: OUTPUT
    field: updated_identity_key
    bound_to: capability_result.identity_key
    source_finding: {phase: p7, register: cc_composition, key: form_updated_identity_key}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: compare_identity
    direction: INPUT
    field: left
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: compare_identity}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: compare_identity
    direction: INPUT
    field: right
    bound_to: results.form_updated_identity_key.updated_identity_key
    source_finding: {phase: p7, register: cc_composition, key: compare_identity}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: compare_identity
    direction: OUTPUT
    field: identity_unchanged
    bound_to: capability_result.is_equal
    source_finding: {phase: p7, register: cc_composition, key: compare_identity}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: require_identity_unchanged
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        identity_unchanged: $.results.compare_identity.identity_unchanged
    source_finding: {phase: p7, register: cc_composition, key: require_identity_unchanged}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: require_identity_unchanged
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: identity_unchanged
        op: eq
        value: true
    source_finding: {phase: p7, register: cc_composition, key: require_identity_unchanged}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: require_identity_unchanged
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_identity_unchanged}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: assemble_updated_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        title: $.inputs.updated_fields.title
        author: $.inputs.updated_fields.author
        publication_year: $.inputs.updated_fields.publication_year
        subject: $.inputs.updated_fields.subject
        state: $.inputs.updated_fields.state
        work_key: $.results.read_book_record.book_record.work_key
    source_finding: {phase: p7, register: cc_composition, key: assemble_updated_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: assemble_updated_record
    direction: OUTPUT
    field: updated_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_updated_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: write_updated_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: write_updated_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: write_updated_record
    direction: INPUT
    field: value
    bound_to: results.assemble_updated_record.updated_record
    source_finding: {phase: p7, register: cc_composition, key: write_updated_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: write_updated_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_updated_record}
  interface_fields:
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The title of the work the edition belongs to, and of the edition itself
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The author of the work the edition belongs to
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: publication_year
    type: string
    required: 'YES'
    default: ''
    meaning: The year that distinguishes this edition from the work's other editions
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: subject
    type: array
    required: 'YES'
    default: ''
    meaning: What kind of material the edition is, as free text
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The edition's descriptive content as submitted
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The fields an edition record is required to carry
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: work_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The work's identifying attributes as submitted
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: work_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The fields a work record is required to carry
  - artifact: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The work's title, compared without regard to letter case or repeated spacing
  - artifact: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The work's author, compared the same way
  - artifact: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    direction: OUTPUT
    field: work_key
    type: string
    required: 'YES'
    default: ''
    meaning: The single key claimed for the work
  - artifact: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    direction: INPUT
    field: source
    type: array
    required: 'YES'
    default: ''
    meaning: The records to select from
  - artifact: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    direction: INPUT
    field: filter
    type: object
    required: 'YES'
    default: ''
    meaning: The criteria a record must match on every key
  - artifact: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    direction: OUTPUT
    field: extracted
    type: array
    required: 'YES'
    default: ''
    meaning: The records that matched, possibly none
  - artifact: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    direction: INPUT
    field: source
    type: array
    required: 'YES'
    default: ''
    meaning: The records to group
  - artifact: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    direction: INPUT
    field: attribute
    type: string
    required: 'YES'
    default: ''
    meaning: The attribute whose value decides which group a record belongs to
  - artifact: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    direction: OUTPUT
    field: grouped
    type: array
    required: 'YES'
    default: ''
    meaning: One group per distinct value, each carrying the records that share it
  - artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The work's title
  - artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The work's author
  - artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: work_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The work record's content, written when the claim is new
  - artifact: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: OUTPUT
    field: work_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key claimed for the work, whether the claim was new or already held
  - artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The title of the work to resolve
  - artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The author of the work to resolve
  - artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: OUTPUT
    field: work_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key of the work that was resolved
  - artifact: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: OUTPUT
    field: work_record
    type: object
    required: 'NO'
    default: ''
    meaning: The work record the key names, when the work exists
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The edition's claimed identity, which is the key its record occupies
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The edition record's content, including the key of the work it belongs to
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The fields an edition record is required to carry
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: OUTPUT
    field: edition_record
    type: object
    required: 'YES'
    default: ''
    meaning: The edition record as written
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The work's identifying attributes, validated alongside the edition's
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The fields a work record is required to carry
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the submission may proceed to be claimed and written
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: ''
    meaning: The edition's authoritative record, carrying the key of the work it belongs to
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The edition record's content, now including the key of the work it belongs to
  - artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
    direction: OUTPUT
    field: matching_works
    type: array
    required: 'YES'
    default: ''
    meaning: One entry per matching work, each carrying the editions of it that matched
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: OUTPUT
    field: work_record
    type: object
    required: 'YES'
    default: ''
    meaning: The record of the work the edition belongs to — its title and author — so the work need not be looked up separately
  - artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
    direction: ATTRIBUTE
    field: work_key
    type: string
    required: 'YES'
    default: ''
    meaning: The work that entered the catalog
  - artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
    direction: ATTRIBUTE
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The work's title
  - artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
    direction: ATTRIBUTE
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The work's author
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The book's bibliographic information
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The fields a book record must carry, as the rules its structure is validated against
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'NO'
    default: ''
    meaning: The barcode the library assigned to the copy, when the registration carries one — an additional edition of an existing work does not
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The fields a book record must carry, as the rules its structure is validated against
  - artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
    direction: INPUT
    field: search_criteria
    type: object
    required: 'YES'
    default: ''
    meaning: What staff are searching by, and the states to include
  - artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
    direction: OUTPUT
    field: matching_books
    type: array
    required: 'YES'
    default: ''
    meaning: The registered books matching what was searched for
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: copy_criteria
    type: object
    required: 'YES'
    default: ''
    meaning: Which copies belong to the book being retrieved
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: ''
    meaning: The book's authoritative record
  - artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: OUTPUT
    field: copies_held
    type: array
    required: 'YES'
    default: ''
    meaning: The copies the library holds of the book
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: updated_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The changed bibliographic information
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: ''
    meaning: The book's authoritative record
  implementation_bindings:
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    callable: execute
    operation: PURE_FORM_WORK_IDENTITY_KEY
    kind: atom
    purity: ct_pure
    refusal: never
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_FORM_WORK_IDENTITY_KEY_V0}
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    callable: execute
    operation: PURE_SELECT_RECORDS
    kind: atom
    purity: ct_pure
    refusal: never
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_SELECT_RECORDS_V0}
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    callable: execute
    operation: PURE_GROUP_RECORDS
    kind: atom
    purity: ct_pure
    refusal: never
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_GROUP_RECORDS_V0}
  vocabulary_extensions: null
  runtime_policies:
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p7, register: rb_declarations, key: RB_CATALOG_BINDINGS_V0}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p7, register: rb_declarations, key: RB_CATALOG_BINDINGS_V0}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p7, register: rb_declarations, key: RB_CATALOG_BINDINGS_V0}
  artifact_properties:
  - artifact: book_library_mgmt::EV_WORK_REGISTERED_V0
    property: type
    value: BUSINESS_MOMENT
    source_finding: {phase: p5, register: provisional_codes, key: EV_WORK_REGISTERED_V0}
  structure_stores:
  - store_name: WORKS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: book_library_mgmt/catalog/works.json
    used_by: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every work the library has catalogued}
  - store_name: WORK_IDENTITY_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: book_library_mgmt/catalog/work_identity_registry.jsonl
    used_by: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    source_finding: {phase: p6, register: storage_governance, key: An atomic claim on each work's identity}
  - store_name: BOOKS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: book_library_mgmt/catalog/books.json
    used_by: book_library_mgmt::CC_REGISTER_BOOK_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  - store_name: PHYSICAL_COPIES
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: book_library_mgmt/catalog/physical_copies.json
    used_by: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every physical copy the library owns}
  - store_name: CATALOG_OPERATIONS
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: book_library_mgmt/catalog/catalog_operations.jsonl
    used_by: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    source_finding: {phase: p6, register: storage_governance, key: A trail of performed operations that cannot be amended}
  - store_name: BOOK_IDENTITY_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: book_library_mgmt/catalog/book_identity_registry.jsonl
    used_by: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    source_finding: {phase: p6, register: storage_governance, key: 'A claim on each book''s identity, held once'}
  - store_name: COPY_BARCODE_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: book_library_mgmt/catalog/copy_barcode_registry.jsonl
    used_by: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    source_finding: {phase: p6, register: storage_governance, key: 'A claim on each copy''s barcode, held once'}
  transport_bindings: []
  artifact_summary:
  - action: NEW
    subdomain: catalog
    count: '8'
    artifacts: 1 IN, 1 WF, 3 CC, 2 CT, 1 EV
  - action: EXTEND
    subdomain: catalog
    count: '7'
    artifacts: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0, book_library_mgmt::RB_CATALOG_BINDINGS_V0, book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_SEARCH_CATALOG_V0, book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
  generation_provenance: []
  declared_reach: []
  test_cases:
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    case: forms_normalized_key
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    case: selects_matching_records
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    case: groups_by_attribute
    expected_outcome: SUCCESS
    source_finding: {source: human}
  test_case_values:
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: title
    value: The Odyssey
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: author
    value: Homer
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: EXPECTED
    field: work_key
    value: the odyssey|homer
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    case: selects_matching_records
    role: INPUT
    field: source
    value:
    - author: Homer
      title: Iliad
    - author: Virgil
      title: Aeneid
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    case: selects_matching_records
    role: INPUT
    field: filter
    value:
      author: Homer
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
    case: selects_matching_records
    role: EXPECTED
    field: extracted
    value:
    - author: Homer
      title: Iliad
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    case: groups_by_attribute
    role: INPUT
    field: source
    value:
    - work: w1
      edition: 1
    - work: w2
      edition: 1
    - work: w1
      edition: 2
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    case: groups_by_attribute
    role: INPUT
    field: attribute
    value: work
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
    case: groups_by_attribute
    role: EXPECTED
    field: grouped
    value:
    - key: w1
      records:
      - work: w1
        edition: 1
      - work: w1
        edition: 2
    - key: w2
      records:
      - work: w2
        edition: 1
    source_finding: {source: human}
  withdrawn_facts: null
```

Eight artifacts are authored and six existing ones are extended. The extended six carry identities
the composition already holds, so they are inventoried rather than assigned — a design that assigned
them again would create a second artifact under the same name.

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

## 15. Artifact Summary

---

## 16. Generation Provenance

*Every artifact this design schedules or amends is authored: construction renders each from the
registers above and it is its own source of truth. Nothing here is reached by invoking a
generator.*

---

## 17. Declared Reach

---

## 23. Test Cases

---

## 24. Test Case Values

---

## 25. Withdrawn Facts

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | p5_business_intent_book_library_mgmt_catalog_v0.md | COMPLETE |
| Stage 6 — Governance Intent | p6_governance_intent_book_library_mgmt_catalog_v0.md | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
| Stage 8 — Authoring Mandate | Pending | — |

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes |
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary |
