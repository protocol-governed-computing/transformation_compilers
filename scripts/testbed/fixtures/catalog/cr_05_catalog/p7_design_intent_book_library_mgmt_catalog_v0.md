# Stage 7 — Design Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p7
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_05_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Each rule is held by the step that applies it
    business_fact: A rule the caller supplies is a rule the caller can widen
    resolution: The confirming contract holds the library's authorization rules; the checking contracts hold the book, work and edition descriptions
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: Each check is followed by a rule refusing when it found anything
    business_fact: An incomplete registration is refused
    resolution: The submission check refuses on both its checks' violations; the book record, the edition record and the correction each gain a rule step requiring none
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: What each registration checks is the record it writes
    business_fact: A check of a supplied copy judges nothing that is written
    resolution: Each registration act hands its submission check the fields it records
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: The register act records the subject where callers send it
    business_fact: Every present caller sends it inside the book details
    resolution: The recorded book's subject is bound from the supplied book details
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - decision: A copy's registered state and a correction's state are the catalog's own
    business_fact: A copy is registered as registered; a correction does not change state
    resolution: The copy contract writes REGISTERED; the correction writes the state it read and checks the corrected record
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - decision: The gates stop requiring what the catalog holds and what no act reads
    business_fact: A gate requiring an unread field refuses a correct request
    resolution: Every gate drops the rules; the book gate its description; the edition gate its descriptions and supplied details
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - decision: Records made before this change are left as they are
    business_fact: The record is added to and never rewritten
    resolution: No migration, backfill or repair step is designed
    source_finding: {phase: p4, register: design_decisions, row: 7}
  existing_inventory:
  - fqdn: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    action: EXTEND
    summary: Confirm the staff member may perform catalog operations
    reason: It takes its rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    action: EXTEND
    summary: Confirms a registration carries what a work and an edition require, before any identity is claimed
    reason: It takes its descriptions from the request and refuses nothing its checks find.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: book_library_mgmt::CC_REGISTER_BOOK_V0
    action: EXTEND
    summary: Validates, assembles and writes an edition record against the work it belongs to
    reason: It takes its description from the request and ignores what its check finds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    action: EXTEND
    summary: Assembles the edition record against a resolved work and writes it
    reason: It takes its description from the request and ignores what its check finds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    action: EXTEND
    summary: Record a copy against exactly one book
    reason: It records the copy in the state the request gives.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: EXTEND
    summary: Changes a registered edition's descriptive content and refuses a change that would duplicate another edition
    reason: It writes the state the request gives and checks no description.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    action: EXTEND
    summary: The governed sequence that registers a work, its first edition and that edition's first physical copy
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    action: EXTEND
    summary: The governed sequence that registers a further edition of a work the library already holds
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - fqdn: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    action: EXTEND
    summary: The governed sequence that registers a further physical copy of an edition
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    action: EXTEND
    summary: Corrects what the library publishes about a registered book
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - fqdn: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    action: EXTEND
    summary: The governed sequence that takes a book out of service
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - fqdn: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    action: EXTEND
    summary: Returning a retired book record to the registered state
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - fqdn: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    action: EXTEND
    summary: The governed sequence that takes a physical copy out of service
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - fqdn: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    action: EXTEND
    summary: Returning a retired copy to the registered state
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - fqdn: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    action: EXTEND
    summary: Assembling a book with the copies the library holds of it
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - fqdn: book_library_mgmt::WF_SEARCH_CATALOG_V0
    action: EXTEND
    summary: Searching by subject or title, excluding retired books
    reason: It binds the rules from the request.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  - fqdn: book_library_mgmt::IN_REGISTER_BOOK_V0
    action: EXTEND
    summary: A request to register a book together with its first physical copy
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 17}
  - fqdn: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    action: EXTEND
    summary: The boundary that admits a request to register a further edition of a work the catalog already holds
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 18}
  - fqdn: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    action: EXTEND
    summary: A request to register a further copy against a registered book
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 19}
  - fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    action: EXTEND
    summary: A request to change a registered book's description
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 20}
  - fqdn: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    action: EXTEND
    summary: A request to retire a book record judged obsolete
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 21}
  - fqdn: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    action: EXTEND
    summary: A request to return a retired book record to the registered state
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 22}
  - fqdn: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    action: EXTEND
    summary: A request to retire a lost or damaged copy
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 23}
  - fqdn: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    action: EXTEND
    summary: A request to return a retired copy to the registered state
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 24}
  - fqdn: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    action: EXTEND
    summary: A request for a book's complete details with the copies held
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 25}
  - fqdn: book_library_mgmt::IN_SEARCH_CATALOG_V0
    action: EXTEND
    summary: A request to locate material by subject or by title
    reason: It requires the rules the catalog now holds.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 26}
  - fqdn: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 27}
  - fqdn: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 28}
  - fqdn: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 29}
  - fqdn: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 30}
  - fqdn: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 31}
  - fqdn: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 32}
  - fqdn: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 33}
  - fqdn: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 34}
  - fqdn: book_library_mgmt::CC_RESOLVE_WORK_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 35}
  - fqdn: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 36}
  - fqdn: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 37}
  - fqdn: book_library_mgmt::CC_SEARCH_CATALOG_V0
    action: REUSE
    summary: ''
    reason: Run by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 38}
  - fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: REUSE
    summary: ''
    reason: Superseded and not in force; named by its successor, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: REUSE
    summary: ''
    reason: Superseded and not in force; named by its successor, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    action: REUSE
    summary: ''
    reason: Binds every catalog act, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::AC_LIBRARY_STAFF_V0
    action: REUSE
    summary: ''
    reason: The actor every catalog act runs as, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    action: REUSE
    summary: ''
    reason: Announced by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::EV_BOOK_REGISTERED_V0
    action: REUSE
    summary: ''
    reason: Announced by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::EV_BOOK_RETIRED_V0
    action: REUSE
    summary: ''
    reason: Announced by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    action: REUSE
    summary: ''
    reason: Announced by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    action: REUSE
    summary: ''
    reason: Announced by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::EV_WORK_REGISTERED_V0
    action: REUSE
    summary: ''
    reason: Announced by an act this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    action: REUSE
    summary: ''
    reason: Run by a contract this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    action: REUSE
    summary: ''
    reason: Run by a contract this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    action: REUSE
    summary: ''
    reason: Run by a contract this change redeclares, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 3}
  - fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    action: REUSE
    summary: ''
    reason: Run by a contract this change redeclares, unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    action: REUSE
    summary: ''
    reason: Run by a contract this change redeclares, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 1}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    action: REUSE
    summary: ''
    reason: Run by a contract this change redeclares, unchanged.
    source_finding: {phase: p6, register: cross_subdomain_deps, row: 2}
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    action: REUSE
    summary: ''
    reason: Holds the catalog's records, unchanged.
    source_finding: {phase: p6, register: storage_governance, row: 1}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    action: REUSE
    summary: ''
    reason: Holds the catalog's records, unchanged.
    source_finding: {phase: p6, register: storage_governance, row: 1}
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    action: REUSE
    summary: ''
    reason: Holds the catalog's records, unchanged.
    source_finding: {phase: p6, register: storage_governance, row: 1}
  new_artifacts: null
  rb_declarations:
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_BOOK_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - rb_code: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    binds_wf: book_library_mgmt::WF_SEARCH_CATALOG_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  execution_topology:
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::IN_REGISTER_BOOK_V0
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      ALREADY_EXISTS: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_BOOK_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_REGISTER_BOOK_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_BOOK_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_RESOLVE_WORK_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_RESOLVE_WORK_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - workflow: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - workflow: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - workflow: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - workflow: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - workflow: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - workflow: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 14}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - workflow: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: book_library_mgmt::IN_SEARCH_CATALOG_V0
    runs: ''
    node_type: IN
    routing:
      ACK: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
      NACK: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
      VIOLATION: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: book_library_mgmt::CC_SEARCH_CATALOG_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: book_library_mgmt::CC_SEARCH_CATALOG_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: EXIT_COMPLETED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  - workflow: book_library_mgmt::WF_SEARCH_CATALOG_V0
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 16}
  cc_composition:
  - cc_code: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    step: '1'
    step_name: confirm_authorization
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - is_authorized
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
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
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
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
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
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
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
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
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '3'
    step_name: refuse_incomplete_record
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '4'
    step_name: assemble_book_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - fields
    produces:
    - book_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: book_record
  - cc_code: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: '5'
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
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '1'
    step_name: validate_edition_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: VALIDATE_RECORD_STRUCTURE
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '2'
    step_name: refuse_incomplete_record
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '3'
    step_name: assemble_edition_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - fields
    produces:
    - edition_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: edition_record
  - cc_code: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: '4'
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
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
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
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        value: book_record
        result_status: result_status
  - cc_code: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    step: '2'
    step_name: assemble_copy_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: ASSEMBLE_RECORD
    store: null
    consumes:
    - fields
    produces:
    - copy_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
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
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
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
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        value: book_record
        result_status: result_status
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '2'
    step_name: form_updated_identity_key
    capability: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    kind: CT
    operation: FORM_BOOK_IDENTITY_KEY
    store: null
    consumes:
    - title
    - author
    - publication_year
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
    - left
    - right
    produces:
    - identity_unchanged
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        left: left
        right: right
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
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
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
    - fields
    produces:
    - updated_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: updated_record
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '6'
    step_name: check_corrected_record
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: VALIDATE_RECORD_STRUCTURE
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '7'
    step_name: refuse_incomplete_correction
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: VALIDATE_PARAMETER_RULES
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: '8'
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
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  step_bindings:
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
        subject: $.payload.book_fields.subject
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: author
    bound_to: payload.author
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    direction: INPUT
    field: work_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: author
    bound_to: payload.author
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: publication_year
    bound_to: payload.publication_year
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
        subject: $.payload.book_fields.subject
        state: REGISTERED
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_BOOK_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_BOOK_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    bound_to: payload.copy_fields
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_BOOK
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_BOOK
        staff_id: $.payload.staff_id
        subject: $.payload.title
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
        subject: $.payload.subject
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_fields
    bound_to:
      literal:
        title: $.payload.title
        author: $.payload.author
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_RESOLVE_WORK_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_RESOLVE_WORK_V0
    direction: INPUT
    field: author
    bound_to: payload.author
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_RESOLVE_WORK_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: title
    bound_to: payload.title
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: author
    bound_to: payload.author
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    direction: INPUT
    field: publication_year
    bound_to: payload.publication_year
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: identity_key
    bound_to: results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0'}
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
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_ADDITIONAL_EDITION
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_ADDITIONAL_EDITION
        staff_id: $.payload.staff_id
        subject: $.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0'}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    bound_to: payload.copy_fields
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0'}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REGISTER_PHYSICAL_COPY
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REGISTER_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0'}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0'}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: updated_fields
    bound_to: payload.updated_fields
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0'}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: UPDATE_BIBLIOGRAPHIC_INFORMATION
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: UPDATE_BIBLIOGRAPHIC_INFORMATION
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0'}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETIRE_BOOK_RECORD
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETIRE_BOOK_RECORD
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REINSTATE_BOOK_RECORD
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REINSTATE_BOOK_RECORD
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0'}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETIRE_PHYSICAL_COPY
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETIRE_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    bound_to: payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: REINSTATE_PHYSICAL_COPY
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: REINSTATE_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: identity_key
    bound_to: payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0'}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    direction: INPUT
    field: copy_criteria
    bound_to:
      literal:
        identity_key: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0'}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: RETRIEVE_BOOK_DETAILS
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: RETRIEVE_BOOK_DETAILS
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    bound_to: payload.staff_credentials
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0'}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_SEARCH_CATALOG_V0
    direction: INPUT
    field: search_criteria
    bound_to: payload.search_criteria
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_SEARCH_CATALOG_V0'}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: staff_id
    bound_to: payload.staff_id
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: operation
    bound_to:
      literal: SEARCH_CATALOG
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
  - owner: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    direction: INPUT
    field: record
    bound_to:
      literal:
        operation: SEARCH_CATALOG
        staff_id: $.payload.staff_id
        subject: $.payload.search_criteria
    source_finding: {phase: p7, register: execution_topology, key: 'book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0'}
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
    bound_to:
      literal:
      - field: staff_id
        op: not_null
      - field: authorized
        op: eq
        value: true
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
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
        publication_year:
          required: true
          type: integer
        subject:
          required: true
          type: array
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_book_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
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
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
    source_finding: {phase: p7, register: cc_composition, key: validate_work_fields}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: validate_work_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: validate_work_fields}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: require_submission_complete
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        barcode: $.inputs.barcode
        subject: $.inputs.book_fields.subject
        book_violations: $.results.validate_book_fields.violations
        work_violations: $.results.validate_work_fields.violations
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
      - field: book_violations
        op: eq
        value: []
      - field: work_violations
        op: eq
        value: []
    source_finding: {phase: p7, register: cc_composition, key: require_submission_complete}
  - owner: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    step: require_submission_complete
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: require_submission_complete}
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
    step: validate_book_fields
    direction: INPUT
    field: record
    bound_to: inputs.book_fields
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: validate_book_fields
    direction: INPUT
    field: schema
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
        publication_year:
          required: true
          type: integer
        subject:
          required: true
          type: array
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: validate_book_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: validate_book_fields}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: refuse_incomplete_record
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.validate_book_fields.violations
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_record}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: refuse_incomplete_record
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_record}
  - owner: book_library_mgmt::CC_REGISTER_BOOK_V0
    step: refuse_incomplete_record
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_record}
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
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
        publication_year:
          required: true
          type: integer
        subject:
          required: true
          type: array
    source_finding: {phase: p7, register: cc_composition, key: validate_edition_fields}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: validate_edition_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: validate_edition_fields}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: refuse_incomplete_record
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.validate_edition_fields.violations
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_record}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: refuse_incomplete_record
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_record}
  - owner: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    step: refuse_incomplete_record
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_record}
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
        state: REGISTERED
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
        state: $.results.read_book_record.book_record.state
        work_key: $.results.read_book_record.book_record.work_key
    source_finding: {phase: p7, register: cc_composition, key: assemble_updated_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: assemble_updated_record
    direction: OUTPUT
    field: updated_record
    bound_to: capability_result.record
    source_finding: {phase: p7, register: cc_composition, key: assemble_updated_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: check_corrected_record
    direction: INPUT
    field: record
    bound_to: results.assemble_updated_record.updated_record
    source_finding: {phase: p7, register: cc_composition, key: check_corrected_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: check_corrected_record
    direction: INPUT
    field: schema
    bound_to:
      literal:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
        publication_year:
          required: true
          type: integer
        subject:
          required: true
          type: array
    source_finding: {phase: p7, register: cc_composition, key: check_corrected_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: check_corrected_record
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
    source_finding: {phase: p7, register: cc_composition, key: check_corrected_record}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: refuse_incomplete_correction
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.check_corrected_record.violations
        subject: $.results.assemble_updated_record.updated_record.subject
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_correction}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: refuse_incomplete_correction
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
      - field: subject
        op: neq
        value: []
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_correction}
  - owner: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    step: refuse_incomplete_correction
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
    source_finding: {phase: p7, register: cc_composition, key: refuse_incomplete_correction}
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
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: title
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: author
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: ''
    meaning: publication year
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: ''
    meaning: book fields
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: barcode
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: copy_fields
    type: object
    required: 'YES'
    default: ''
    meaning: copy fields
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: title
    type: string
    required: 'YES'
    default: ''
    meaning: title
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: author
    type: string
    required: 'YES'
    default: ''
    meaning: author
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: publication_year
    type: integer
    required: 'YES'
    default: ''
    meaning: publication year
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: subject
    type: array
    required: 'YES'
    default: ''
    meaning: subject
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: identity key
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: barcode
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    type: object
    required: 'YES'
    default: ''
    meaning: copy fields
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: identity key
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    direction: INPUT
    field: updated_fields
    type: object
    required: 'YES'
    default: ''
    meaning: updated fields
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: identity key
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: identity key
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: barcode
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: barcode
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: identity key
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: search_criteria
    type: object
    required: 'YES'
    default: ''
    meaning: search criteria
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    direction: INPUT
    field: staff_id
    type: string
    required: 'YES'
    default: ''
    meaning: staff id
  - artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: INPUT
    field: staff_credentials
    type: object
    required: 'YES'
    default: ''
    meaning: staff credentials
  - artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    direction: OUTPUT
    field: is_authorized
    type: boolean
    required: 'YES'
    default: ''
    meaning: is authorized
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: work_fields
    type: object
    required: 'YES'
    default: ''
    meaning: work fields
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: ''
    meaning: book fields
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'NO'
    default: ''
    meaning: barcode
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: ''
    meaning: valid
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: book_fields
    type: object
    required: 'YES'
    default: ''
    meaning: book fields
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: identity key
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: ''
    meaning: book record
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: identity key
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: INPUT
    field: edition_fields
    type: object
    required: 'YES'
    default: ''
    meaning: edition fields
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    direction: OUTPUT
    field: edition_record
    type: object
    required: 'YES'
    default: ''
    meaning: edition record
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: identity key
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: barcode
    type: string
    required: 'YES'
    default: ''
    meaning: barcode
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: INPUT
    field: copy_fields
    type: object
    required: 'YES'
    default: ''
    meaning: copy fields
  - artifact: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: ''
    meaning: book record
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: identity_key
    type: string
    required: 'YES'
    default: ''
    meaning: identity key
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: INPUT
    field: updated_fields
    type: object
    required: 'YES'
    default: ''
    meaning: updated fields
  - artifact: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    direction: OUTPUT
    field: book_record
    type: object
    required: 'YES'
    default: ''
    meaning: book record
  implementation_bindings: null
  vocabulary_extensions: null
  runtime_policies: null
  artifact_properties:
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_WORK_REGISTERED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    property: supersedes
    value:
    - book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BOOK_RETIRED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 13}
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    property: supersedes
    value:
    - book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 20}
  structure_stores: null
  transport_bindings: null
  artifact_summary:
  - action: EXTEND
    subdomain: catalog
    count: '26'
    artifacts: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0, book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0, book_library_mgmt::CC_REGISTER_BOOK_V0, book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::WF_SEARCH_CATALOG_V0, book_library_mgmt::IN_REGISTER_BOOK_V0, book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1, book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0, book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0, book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0, book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0, book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0, book_library_mgmt::IN_SEARCH_CATALOG_V0
  generation_provenance: null
  declared_reach: null
  refusal_discharge:
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Any catalog operation
    refused_when: The person performing it is not authorized staff
    act: book_library_mgmt::WF_SEARCH_CATALOG_V0
    step: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Registering a book
    refused_when: It lacks what the library says a book must contain
    act: book_library_mgmt::WF_REGISTER_BOOK_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Registering a further edition
    refused_when: It lacks what the library says an edition must contain
    act: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    step: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    outcome: VIOLATION
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  refusal_deferrals: null
  refusal_governance_discharge: null
  molecule_steps: null
  molecule_step_bindings: null
  test_cases: null
  test_case_values: null
  withdrawn_facts:
  - artifact: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    fact: .core.inputs.authorization_rules
    reason: The contract holds the library's rules itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_SEARCH_CATALOG_V0
    fact: .core.nodes.CC_CONFIRM_STAFF_AUTHORIZED_V0.inputs.authorization_rules
    reason: The confirming contract no longer takes the rules.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_REINSTATE_BOOK_RECORD_V0
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_REINSTATE_PHYSICAL_COPY_V0
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
    fact: .core.inputs.authorization_rules
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    fact: .core.inputs.book_schema
    reason: The contract holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    fact: .core.inputs.work_schema
    reason: The contract holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
    fact: .core.inputs.book_schema
    reason: The contract holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.inputs.edition_schema
    reason: The contract holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    fact: .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.book_schema
    reason: The check holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    fact: .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.work_schema
    reason: The check holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    fact: .core.nodes.CC_REGISTER_BOOK_V0.inputs.book_schema
    reason: The contract holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
    fact: .core.inputs.book_schema
    reason: The gate no longer requires what the catalog holds.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.book_schema
    reason: The check holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.nodes.CC_VALIDATE_BOOK_SUBMISSION_V0.inputs.work_schema
    reason: The check holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.nodes.CC_REGISTER_ADDITIONAL_EDITION_V0.inputs.edition_schema
    reason: The contract holds its description itself.
    source_finding: {phase: p6, register: boundary_rules, row: 1}
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.inputs.edition_schema
    reason: The gate no longer requires what the catalog holds or no act reads.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.inputs.work_schema
    reason: The gate no longer requires what the catalog holds or no act reads.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.inputs.edition_fields
    reason: The gate no longer requires what the catalog holds or no act reads.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
  - artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    fact: .core.inputs.work_fields
    reason: The gate no longer requires what the catalog holds or no act reads.
    source_finding: {phase: p6, register: boundary_rules, row: 6}
```

Every binding names a field the capability declares, read from the pinned baseline
`34c8a0e8a3f2f1b90956edd08d0d878a10347fbc058348049f8348ce0d5b8a95`.

Nothing new is authored. Twenty-six artifacts the catalog already holds are redeclared whole: six
contracts hold their rules and descriptions and refuse on what they find, ten acts stop passing rules
along and check what they record, and ten gates stop requiring what the catalog holds.

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

The routing of every act is unchanged. What changes is what each node is handed, in §7.

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
