# Design Intent — book_library_mgmt / catalog (deliberately inadmissible fixture)

## Machine

```yaml
document:
  phase: p8
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_01_catalog
registers:
  design_resolution: |2

    ---
  existing_inventory:
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    action: REVIEW
    summary: Writes, reads, selects, lists, updates in place and deletes durable records
    reason: Extended with an operation that publishes the records themselves, so a search can select among them by content; the implementation behind it already returned them.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    action: ADOPT
    summary: ''
    reason: Register-if-absent gives the atomic claim duplicate prevention needs, on a key the catalog forms.
    source_finding: {phase: p6, register: ownership, key: Claim a value once so a second claim on it fails}
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    action: REUSE
    summary: ''
    reason: Appends an entry to a trail that cannot be amended.
    source_finding: {phase: p6, register: ownership, key: Append an entry to a trail that cannot be amended}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: ''
    reason: Assembles a durable record from supplied values.
    source_finding: {phase: p6, register: ownership, key: Assemble a durable record from supplied values}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    action: REUSE
    summary: ''
    reason: Confirms a record carries the fields its contract declares.
    source_finding: {phase: p6, register: ownership, key: Confirm a record carries the fields its contract declares}
  - fqdn: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    action: REUSE
    summary: ''
    reason: Selects the records matching stated criteria, and interprets a read of the store into a decision.
    source_finding: {phase: p6, register: ownership, key: Select the records matching stated criteria}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    action: REUSE
    summary: ''
    reason: Confirms supplied parameters satisfy declared rules, and interprets a read into a decision.
    source_finding: {phase: p6, register: ownership, key: Confirm supplied parameters satisfy declared rules}
  - fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    action: REUSE
    summary: ''
    reason: Decides whether the identity an update would produce is the identity the book already has.
    source_finding: {phase: p6, register: ownership, key: Confirm supplied parameters satisfy declared rules}
  new_artifacts:
  - capability: The authorized staff member who performs a catalog operation
    family: AC
    code: book_library_mgmt::AC_LIBRARY_STAFF_V0
    summary: The actor whose authorization every catalog operation binds
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: AC_LIBRARY_STAFF_V0}
  - capability: A request to register a book together with its first physical copy
    family: IN
    code: book_library_mgmt::IN_REGISTER_BOOK_V0
    summary: A request to register a book together with its first physical copy
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_REGISTER_BOOK_V0}
  - capability: A request to register a further copy against a registered book
    family: IN
    code: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    summary: A request to register a further copy against a registered book
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_REGISTER_PHYSICAL_COPY_V0}
  - capability: A request to change a registered book's description
    family: IN
    code: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    summary: A request to change a registered book's description
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - capability: A request to retire a book record judged obsolete
    family: IN
    code: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    summary: A request to retire a book record judged obsolete
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_RETIRE_BOOK_RECORD_V0}
  - capability: A request to retire a lost or damaged copy
    family: IN
    code: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    summary: A request to retire a lost or damaged copy
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_RETIRE_PHYSICAL_COPY_V0}
  - capability: A request to return a retired book record to the registered state
    family: IN
    code: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    summary: A request to return a retired book record to the registered state
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_REINSTATE_BOOK_RECORD_V0}
  - capability: A request to return a retired copy to the registered state
    family: IN
    code: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    summary: A request to return a retired copy to the registered state
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_REINSTATE_PHYSICAL_COPY_V0}
  - capability: A request to locate material by subject or by title
    family: IN
    code: book_library_mgmt::IN_SEARCH_CATALOG_V0
    summary: A request to locate material by subject or by title
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_SEARCH_CATALOG_V0}
  - capability: A request for a book's complete details with the copies held
    family: IN
    code: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    summary: A request for a book's complete details with the copies held
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: IN_RETRIEVE_BOOK_DETAILS_V0}
  - capability: Registering a book and its first copy, end to end
    family: WF
    code: book_library_mgmt::WF_REGISTER_BOOK_V0
    summary: Registering a book and its first copy, end to end
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_REGISTER_BOOK_V0}
  - capability: Registering a further copy against a registered book
    family: WF
    code: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    summary: Registering a further copy against a registered book
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_REGISTER_PHYSICAL_COPY_V0}
  - capability: Changing a book's description without making it a duplicate
    family: WF
    code: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    summary: Changing a book's description without making it a duplicate
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - capability: Retiring a book record, leaving its copies untouched
    family: WF
    code: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    summary: Retiring a book record, leaving its copies untouched
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_RETIRE_BOOK_RECORD_V0}
  - capability: Retiring a copy, leaving the book record untouched
    family: WF
    code: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    summary: Retiring a copy, leaving the book record untouched
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_RETIRE_PHYSICAL_COPY_V0}
  - capability: Returning a retired book record to the registered state
    family: WF
    code: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    summary: Returning a retired book record to the registered state
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_REINSTATE_BOOK_RECORD_V0}
  - capability: Returning a retired copy to the registered state
    family: WF
    code: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    summary: Returning a retired copy to the registered state
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_REINSTATE_PHYSICAL_COPY_V0}
  - capability: Searching by subject or title, excluding retired books
    family: WF
    code: book_library_mgmt::WF_SEARCH_CATALOG_V0
    summary: Searching by subject or title, excluding retired books
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_SEARCH_CATALOG_V0}
  - capability: Assembling a book with the copies the library holds of it
    family: WF
    code: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    summary: Assembling a book with the copies the library holds of it
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: WF_RETRIEVE_BOOK_DETAILS_V0}
  - capability: Confirm the staff member may perform catalog operations
    family: CC
    code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    summary: Confirm the staff member may perform catalog operations
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - capability: Judge a registration admissible before anything is claimed or written
    family: CC
    code: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    summary: Validate a book submission is complete
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_REGISTER_BOOK_V0}
  - capability: Resolve a registered book's identity without claiming it
    family: CC
    code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    summary: Resolve a registered book's identity key
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - capability: Claim a book's identity so a second registration of the same book is refused
    family: CC
    code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    summary: Claim a book's identity so a second registration of the same book is refused
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - capability: Claim a copy's barcode so a second copy carrying it is refused
    family: CC
    code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    summary: Claim a copy's barcode so a second copy carrying it is refused
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_CLAIM_COPY_BARCODE_V0}
  - capability: Record a book's bibliographic information as the catalog's authoritative description
    family: CC
    code: book_library_mgmt::CC_REGISTER_BOOK_V0
    summary: Record a book's bibliographic information as the catalog's authoritative description
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_REGISTER_BOOK_V0}
  - capability: Record a copy against exactly one book
    family: CC
    code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    summary: Record a copy against exactly one book
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - capability: Replace a book's descriptive content in place
    family: CC
    code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    summary: Replace a book's descriptive content in place
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - capability: Mark a book record retired so it is no longer offered as current
    family: CC
    code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    summary: Mark a book record retired so it is no longer offered as current
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_RETIRE_BOOK_RECORD_V0}
  - capability: Mark a copy retired so the library no longer holds it
    family: CC
    code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    summary: Mark a copy retired so the library no longer holds it
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_RETIRE_PHYSICAL_COPY_V0}
  - capability: Mark a retired book record registered again
    family: CC
    code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    summary: Mark a retired book record registered again
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_REINSTATE_BOOK_RECORD_V0}
  - capability: Mark a retired copy registered again
    family: CC
    code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    summary: Mark a retired copy registered again
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_REINSTATE_PHYSICAL_COPY_V0}
  - capability: Select the registered books matching a subject or title, excluding retired ones
    family: CC
    code: book_library_mgmt::CC_SEARCH_CATALOG_V0
    summary: Select the registered books matching a subject or title, excluding retired ones
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_SEARCH_CATALOG_V0}
  - capability: Assemble a book's record with the copies recorded against it
    family: CC
    code: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    summary: Assemble a book's record with the copies recorded against it
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_ASSEMBLE_BOOK_DETAILS_V0}
  - capability: Append a durable account of a performed operation to the catalog's own trail
    family: CC
    code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    summary: Append a durable account of a performed operation to the catalog's own trail
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p5, register: provisional_codes, key: CC_APPEND_CATALOG_OPERATION_V0}
  - capability: Form one identity key from a book's title, author and publication year
    family: CT
    code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    summary: Forms the single key the registry claims from the three identifying attributes
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p3, register: authoring_decisions, key: 'Enforce that one book exists per title, author and publication year'}
  - capability: A book entered the catalog and acquired its authoritative record
    family: EV
    code: book_library_mgmt::EV_BOOK_REGISTERED_V0
    summary: A book entered the catalog and acquired its authoritative record
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p4, register: events, key: Book registered}
  - capability: The library recorded another copy it owns
    family: EV
    code: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    summary: The library recorded another copy it owns
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p4, register: events, key: Physical copy registered}
  - capability: The authoritative description of a book changed
    family: EV
    code: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    summary: The authoritative description of a book changed
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p4, register: events, key: Bibliographic information updated}
  - capability: A book record is no longer to be used
    family: EV
    code: book_library_mgmt::EV_BOOK_RETIRED_V0
    summary: A book record is no longer to be used
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p4, register: events, key: Book retired}
  - capability: The library no longer holds that copy
    family: EV
    code: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    summary: The library no longer holds that copy
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p4, register: events, key: Physical copy retired}
  - capability: Bind the catalog's operations to the stores and mechanisms they use
    family: RB
    code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    summary: Binds every catalog workflow to the mechanisms and stores it uses
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p6, register: ownership, key: Record a performed catalog operation in the catalog's audit trail}
  - capability: Declare the stores the catalog owns
    family: STRUCTURE
    code: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    summary: Declares the five stores the catalog owns and the paths they occupy
    owner_subdomain: catalog
    status: NEW
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  rb_declarations:
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_BOOK_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_SEARCH_CATALOG_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every book the library catalogs}
  execution_topology:
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::IN_REGISTER_BOOK_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_REGISTER_BOOK_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_VALIDATE_BOOK_SUBMISSION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_REGISTER_BOOK_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_REGISTER_BOOK_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_BOOK_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CLAIM_COPY_BARCODE_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_CATALOG_OPERATION_V0}
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
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_REGISTER_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CLAIM_COPY_BARCODE_V0}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REGISTER_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REGISTER_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CLAIM_BOOK_IDENTITY_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_RETIRE_BOOK_RECORD_V0}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RETIRE_BOOK_RECORD_V0}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RETIRE_BOOK_RECORD_V0}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RETIRE_BOOK_RECORD_V0}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_RETIRE_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_RETIRE_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RETIRE_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RETIRE_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_REINSTATE_BOOK_RECORD_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_REINSTATE_BOOK_RECORD_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REINSTATE_BOOK_RECORD_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REINSTATE_BOOK_RECORD_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_REINSTATE_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_REINSTATE_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REINSTATE_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_REINSTATE_PHYSICAL_COPY_V0}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: book_library_mgmt::IN_SEARCH_CATALOG_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_SEARCH_CATALOG_V0}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: book_library_mgmt::CC_SEARCH_CATALOG_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_SEARCH_CATALOG_V0}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_SEARCH_CATALOG_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_SEARCH_CATALOG_V0}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_SEARCH_CATALOG_V0}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: IN_RETRIEVE_BOOK_DETAILS_V0}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_ASSEMBLE_BOOK_DETAILS_V0}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p7, register: new_artifacts, key: CC_APPEND_CATALOG_OPERATION_V0}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: EXIT_COMPLETED
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RETRIEVE_BOOK_DETAILS_V0}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
    source_finding: {phase: p7, register: execution_topology, key: WF_RETRIEVE_BOOK_DETAILS_V0}
  cc_composition:
  - cc_code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    step: '1'
    step_name: confirm_authorization
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - staff_credentials
    - authorization_rules
    produces:
    - is_authorized
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: staff_credentials
        rules: authorization_rules
      out:
        valid: is_authorized
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
  - cc_code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: '1'
    step_name: form_identity_key
    capability: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    kind: CT
    operation: FORM_BOOK_IDENTITY_KEY
    store: null
    consumes:
    - title
    - author
    - publication_year
    produces:
    - identity_key
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
        identity_key: identity_key
  - cc_code: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: '2'
    step_name: claim_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: BOOK_IDENTITY_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: ALREADY_EXISTS
    interface: null
  - cc_code: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    step: '1'
    step_name: resolve_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: BOOK_IDENTITY_REGISTRY
    consumes:
    - key_or_address
    produces:
    - target_ref
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: '1'
    step_name: claim_barcode
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: COPY_BARCODE_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: ALREADY_EXISTS
    interface: null
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
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
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '2'
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
    step: '3'
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
  - cc_code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
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
  - cc_code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: '2'
    step_name: assemble_copy_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - copy_fields
    produces:
    - copy_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: copy_fields
      out:
        record: copy_record
  - cc_code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: '3'
    step_name: write_copy_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: PHYSICAL_COPIES
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
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: records
        filter: search_criteria
      out:
        extracted: matching_books
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
    - book_record
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
    step: '3'
    step_name: select_copies_of_book
    capability: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    kind: CT
    operation: FILTER_RECORDS
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
  - cc_code: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: '1'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: PHYSICAL_COPIES
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: '1'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: PHYSICAL_COPIES
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: '1'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: BOOKS
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: '1'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: BOOKS
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  - cc_code: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: '1'
    step_name: append_operation
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: CATALOG_OPERATIONS
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - record_id
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface: null
  step_bindings:
  - owner: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: INPUT
    field: parameters
    bound_to: inputs.staff_credentials
    source_finding: {phase: p7, register: cc_composition, key: confirm_authorization}
  - owner: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: INPUT
    field: rules
    bound_to: inputs.authorization_rules
    source_finding: {phase: p7, register: cc_composition, key: confirm_authorization}
  - owner: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    step: confirm_authorization
    direction: OUTPUT
    field: is_authorized
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: confirm_authorization}
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
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: title
    bound_to: inputs.title
    source_finding: {phase: p7, register: cc_composition, key: form_identity_key}
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: author
    bound_to: inputs.author
    source_finding: {phase: p7, register: cc_composition, key: form_identity_key}
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: form_identity_key
    direction: INPUT
    field: publication_year
    bound_to: inputs.publication_year
    source_finding: {phase: p7, register: cc_composition, key: form_identity_key}
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: form_identity_key
    direction: OUTPUT
    field: identity_key
    bound_to: capability_result.identity_key
    source_finding: {phase: p7, register: cc_composition, key: form_identity_key}
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: key
    bound_to: results.form_identity_key.identity_key
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: INPUT
    field: target_ref
    bound_to:
      literal: BOOKS
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    step: claim_identity
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: claim_identity}
  - owner: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    step: resolve_identity
    direction: INPUT
    field: key_or_address
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: resolve_identity}
  - owner: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    step: resolve_identity
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
    source_finding: {phase: p7, register: cc_composition, key: resolve_identity}
  - owner: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    step: resolve_identity
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: resolve_identity}
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: INPUT
    field: key
    bound_to: inputs.barcode
    source_finding: {phase: p7, register: cc_composition, key: claim_barcode}
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
    source_finding: {phase: p7, register: cc_composition, key: claim_barcode}
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: INPUT
    field: target_ref
    bound_to:
      literal: PHYSICAL_COPIES
    source_finding: {phase: p7, register: cc_composition, key: claim_barcode}
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
    source_finding: {phase: p7, register: cc_composition, key: claim_barcode}
  - owner: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    step: claim_barcode
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: claim_barcode}
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
    source_finding: {phase: p7, register: cc_composition, key: assemble_book_record}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: assemble_book_record
    direction: OUTPUT
    field: book_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_book_record}
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
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: read_book_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: read_book_record
    direction: OUTPUT
    field: book_record
    bound_to: capability_result.value
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: read_book_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: assemble_copy_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
        barcode: $.inputs.barcode
        state: $.inputs.copy_fields.state
    source_finding: {phase: p7, register: cc_composition, key: assemble_copy_record}
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: assemble_copy_record
    direction: OUTPUT
    field: copy_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_copy_record}
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: write_copy_record
    direction: INPUT
    field: key
    bound_to: inputs.barcode
    source_finding: {phase: p7, register: cc_composition, key: write_copy_record}
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: write_copy_record
    direction: INPUT
    field: value
    bound_to: results.assemble_copy_record.copy_record
    source_finding: {phase: p7, register: cc_composition, key: write_copy_record}
  - owner: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: write_copy_record
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: write_copy_record}
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
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: INPUT
    field: key
    bound_to: inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: read_book_record}
  - owner: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    step: read_book_record
    direction: OUTPUT
    field: book_record
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
    step: select_copy_records
    direction: OUTPUT
    field: records
    bound_to: capability_result.records
    source_finding: {phase: p7, register: cc_composition, key: select_copy_records}
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
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        barcode: $.inputs.barcode
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: REGISTERED
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        barcode: $.inputs.barcode
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: RETIRED
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: REGISTERED
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        identity_key: $.inputs.identity_key
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: RETIRED
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to:
      literal: $.result_status
    source_finding: {phase: p7, register: cc_composition, key: set_record_state}
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: record
    bound_to: inputs.record
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: stream_id
    bound_to:
      literal: CATALOG_OPERATIONS
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: INPUT
    field: actor_id
    bound_to: inputs.staff_id
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: OUTPUT
    field: record_id
    bound_to: capability_result.record_id
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
  - owner: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    step: append_operation
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
    source_finding: {phase: p7, register: cc_composition, key: append_operation}
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
    field: book_fields
    bound_to: payload.book_fields
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
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_CLAIM_COPY_BARCODE_V0}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    bound_to: payload.copy_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_REGISTER_PHYSICAL_COPY_V0}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_PHYSICAL_COPY
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_RESOLVE_BOOK_IDENTITY_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: updated_fields
    bound_to: payload.updated_fields
    source_finding: {phase: p7, register: execution_topology, key: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: UPDATE_BIBLIOGRAPHIC_INFORMATION
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: UPDATE_BIBLIOGRAPHIC_INFORMATION
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_RETIRE_BOOK_RECORD_V0}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETIRE_BOOK_RECORD
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETIRE_BOOK_RECORD
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_RETIRE_PHYSICAL_COPY_V0}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETIRE_PHYSICAL_COPY
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETIRE_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_REINSTATE_BOOK_RECORD_V0}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REINSTATE_BOOK_RECORD
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REINSTATE_BOOK_RECORD
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_REINSTATE_PHYSICAL_COPY_V0}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REINSTATE_PHYSICAL_COPY
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REINSTATE_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_SEARCH_CATALOG_V0
    direction: INPUT
    field: search_criteria
    bound_to: payload.search_criteria
    source_finding: {phase: p7, register: execution_topology, key: CC_SEARCH_CATALOG_V0}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: SEARCH_CATALOG
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: SEARCH_CATALOG
        staff_id: $.payload.staff_id
        subject: $.payload.search_criteria
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    bound_to: payload.authorization_rules
    source_finding: {phase: p7, register: execution_topology, key: CC_CONFIRM_STAFF_AUTHORIZED_V0}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_ASSEMBLE_BOOK_DETAILS_V0}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: copy_criteria
    bound_to:
      literal:
        identity_key: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_ASSEMBLE_BOOK_DETAILS_V0}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETRIEVE_BOOK_DETAILS
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETRIEVE_BOOK_DETAILS
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: CC_APPEND_CATALOG_OPERATION_V0}
  interface_fields:
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The title the book is published under
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The author the book is published under
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: ''
    meaning: The year this edition was published
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The book's bibliographic information
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: book_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The fields a book record must carry, as the rules its structure is validated against
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: copy_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The copy's recorded detail
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The copy's recorded detail
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The title the book is published under
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The author the book is published under
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: ''
    meaning: The year this edition was published
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: updated_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The changed bibliographic information
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: search_criteria
    type: object
    required: 'YES'
    default: ''
    meaning: What staff are searching by, and the states to include
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: Who is performing the operation, as the catalog receives it
  - artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: authorization_rules
    type: array
    required: 'YES'
    default: ''
    meaning: The rules the staff member's credentials are checked against
  - artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: OUTPUT
    field: is_authorized
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the staff member may perform catalog operations
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
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: ''
    meaning: Whether the submission may proceed to be claimed and written
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The title the book is published under
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The author the book is published under
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: ''
    meaning: The year this edition was published
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: ''
    meaning: Where the claimed key resolves to
  - artifact: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    direction: OUTPUT
    field: target_ref
    type: string
    required: 'YES'
    default: ''
    meaning: Where the registered key resolves to
  - artifact: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: ''
    meaning: Where the claimed key resolves to
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The book's bibliographic information
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_schema
    type: object
    required: 'YES'
    default: ''
    meaning: The fields a book record must carry, as the rules its structure is validated against
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: ''
    meaning: The book's authoritative record
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    type: object
    required: 'YES'
    default: ''
    meaning: The copy's recorded detail
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: ''
    meaning: The book's authoritative record
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
  - artifact: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: ''
    meaning: How many records the state change matched and updated
  - artifact: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: ''
    meaning: How many records the state change matched and updated
  - artifact: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: ''
    meaning: How many records the state change matched and updated
  - artifact: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: ''
    meaning: How many records the state change matched and updated
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
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    type: object
    required: 'YES'
    default: ''
    meaning: The account of the performed operation
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    type: string
    required: 'YES'
    default: ''
    meaning: operation
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: OUTPUT
    field: record_id
    type: string
    required: 'YES'
    default: ''
    meaning: The identity of the appended trail entry
  - artifact: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: ''
    meaning: The entry's position in the trail
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The title the book is published under
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The author the book is published under
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: ''
    meaning: The year this edition was published
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::EV_BOOK_REGISTERED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    direction: OUTPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::EV_BOOK_RETIRED_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::EV_BOOK_RETIRED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    direction: OUTPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: The barcode the library assigned to the copy
  - artifact: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    direction: OUTPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member recorded against the operation in the audit trail
  - artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: The title the book is published under
  - artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: The author the book is published under
  - artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: ''
    meaning: The year this edition was published
  - artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    direction: OUTPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: The key formed from a book's title, author and publication year
  - artifact: book_library_mgmt::AC_LIBRARY_STAFF_V0
    direction: ATTRIBUTE
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: The staff member's identity as the library knows it
  - artifact: book_library_mgmt::AC_LIBRARY_STAFF_V0
    direction: ATTRIBUTE
    field: authorized
    type: boolean
    required: 'NO'
    default: false
    meaning: Whether the staff member may perform catalog operations; decided by the staff function, read here
  implementation_bindings:
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    callable: execute
    operation: PURE_FORM_BOOK_IDENTITY_KEY
    kind: atom
    purity: ct_pure
    refusal: never
    source_finding: {phase: p7, register: new_artifacts, key: CT_PURE_FORM_BOOK_IDENTITY_KEY_V0}
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
  - artifact: book_library_mgmt::AC_LIBRARY_STAFF_V0
    property: type
    value: UNRESOLVED
    source_finding: {phase: p5, register: provisional_codes, key: AC_LIBRARY_STAFF_V0}
  structure_stores:
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
  artifact_summary: null
  generation_provenance: []
  declared_reach: []
  refusal_discharge:
  - operation: Register a book
    refused_when: Its title, author and publication year match a registered book.
    act: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    outcome: ALREADY_EXISTS
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Register a book
    refused_when: No physical copy is offered with it.
    act: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Register a book
    refused_when: It carries no subject.
    act: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Register a physical copy
    refused_when: The book it names is not registered.
    act: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    outcome: NOT_FOUND
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Register a physical copy
    refused_when: Its barcode matches a copy the library already owns.
    act: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    outcome: ALREADY_EXISTS
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: Update bibliographic information
    refused_when: The changed title, author and publication year would match another registered book.
    act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    act: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    act: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    act: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    act: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    act: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    act: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    act: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Any catalog operation
    refused_when: The staff member performing it is not authorized.
    act: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  refusal_deferrals: []
  refusal_governance_discharge: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    expected_outcome: SUCCESS
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: refuses_blank_title
    expected_outcome: VIOLATION
    source_finding: {source: human}
  test_case_values:
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: title
    value: THE ODYSSEY
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: author
    value: Homer
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: INPUT
    field: publication_year
    value: 1614
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: forms_normalized_key
    role: EXPECTED
    field: identity_key
    value: the odyssey|homer|1614
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: refuses_blank_title
    role: INPUT
    field: title
    value: ' '
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: refuses_blank_title
    role: INPUT
    field: author
    value: Homer
    source_finding: {source: human}
  - ct_code: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    case: refuses_blank_title
    role: INPUT
    field: publication_year
    value: 1614
    source_finding: {source: human}
  withdrawn_facts: null
```

> The design below is the admissible document's. What is wrong is the shape it is carried in.

Every binding names a field the capability declares, read from the pinned baseline
`41dd01fb1bc94d57c645f5c7fee1f96a7c4f147c98fa5104a6249ce9e6ea4a1d`.

---

## 1. Design Decisions Resolution

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

Every status this design routes on — ACK, NACK, SUCCESS, NOT_FOUND, ALREADY_EXISTS, DENIED, VIOLATION,
BACKEND_ERROR — is already admitted, so no vocabulary is extended.

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

*Every artifact this design schedules is authored: construction renders it from the registers
above and it is its own source of truth. Nothing here is reached by invoking a generator.*

---

## 17. Declared Reach

---

## 18. Refusal Discharge

---

## 19. Refusal Deferrals

---

## 20. Refusal — Governance-Surface Discharge

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

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
