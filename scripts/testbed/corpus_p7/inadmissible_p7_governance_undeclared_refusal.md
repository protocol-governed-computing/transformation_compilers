# Stage 7 — Design Intent: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p7
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_03_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Registering a book announces three moments at one ending.
    business_fact: An act announces every moment it completed.
    resolution: §12 declares three `emit.EXIT_COMPLETED` rows against `WF_REGISTER_BOOK_V0`. Construction renders them as an ordered sequence; the platform seals that order and the runtime keeps it.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - decision: The order announced is the order the business completes them.
    business_fact: The order is normative and a reader of the account sees it.
    resolution: The rows are read in document order — the work, then the book, then the physical copy — which is the order the act claims each identity.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - decision: Each remaining act announces the one moment it completes.
    business_fact: An act announces every moment it completed.
    resolution: One `emit` row each. A sequence of one renders as a single name, which is what every act announcing elsewhere in the composition carries.
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - decision: Reinstatement announces nothing.
    business_fact: Only moments the business already declared are announced.
    resolution: Neither reinstatement act appears here. The business declares no moment for a reinstatement, and authoring one would be business content this design does not own.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  existing_inventory:
  - fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    action: EXTEND
    summary: The governed sequence that registers a work, its first edition and that edition's first physical copy
    reason: Announces the moments it completes, where it announced nothing. Everything else about it is restated unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    action: EXTEND
    summary: The governed sequence that registers a further edition of a work the library already holds
    reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 2}
  - fqdn: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    action: EXTEND
    summary: The governed sequence that registers a further physical copy of an edition
    reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 3}
  - fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: EXTEND
    summary: The governed sequence that corrects what the library publishes about a book
    reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 4}
  - fqdn: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    action: EXTEND
    summary: The governed sequence that takes a book out of service
    reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 5}
  - fqdn: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    action: EXTEND
    summary: The governed sequence that takes a physical copy out of service
    reason: Announces the moment it completes, where it announced nothing. Everything else about it is restated unchanged.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 6}
  - fqdn: book_library_mgmt::AC_LIBRARY_STAFF_V0
    action: REUSE
    summary: The actor whose authorization every catalog operation binds
    reason: The actor every catalog act runs as. An EXTEND re-renders an act whole, so the design must state the actor it carries or the re-rendered act would carry none.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 15}
  - fqdn: book_library_mgmt::EV_WORK_REGISTERED_V0
    action: REUSE
    summary: ''
    reason: The moment announced by the act that completes it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 7}
  - fqdn: book_library_mgmt::EV_BOOK_REGISTERED_V0
    action: REUSE
    summary: ''
    reason: The moment announced by the act that completes it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 8}
  - fqdn: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    action: REUSE
    summary: ''
    reason: The moment announced by the act that completes it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 9}
  - fqdn: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    action: REUSE
    summary: ''
    reason: The moment announced by the act that completes it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 10}
  - fqdn: book_library_mgmt::EV_BOOK_RETIRED_V0
    action: REUSE
    summary: ''
    reason: The moment announced by the act that completes it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 11}
  - fqdn: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    action: REUSE
    summary: ''
    reason: The moment announced by the act that completes it.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 12}
  - fqdn: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_REGISTER_BOOK_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_RESOLVE_WORK_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_RETIRE_PHYSICAL_COPY_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::IN_REGISTER_BOOK_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::IN_REGISTER_PHYSICAL_COPY_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::IN_RETIRE_BOOK_RECORD_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::IN_RETIRE_PHYSICAL_COPY_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  - fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    action: REUSE
    summary: ''
    reason: Named by an act this change extends; unchanged, and restated because an EXTEND is a whole redeclaration.
    source_finding: {phase: p6, register: pps_artifacts_requiring_action, row: 1}
  new_artifacts: []
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
    binds_wf: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    source_finding: {phase: p6, register: storage_governance, key: A durable record of every work the library has catalogued}
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
  execution_topology:
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
  cc_composition: []
  step_bindings:
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
  interface_fields: []
  implementation_bindings: []
  vocabulary_extensions: []
  runtime_policies: []
  artifact_properties:
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_WORK_REGISTERED_V0
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - artifact: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BOOK_REGISTERED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - artifact: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - artifact: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - artifact: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_BOOK_RETIRED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - artifact: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    property: emit.EXIT_COMPLETED
    value:
    - book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  structure_stores: []
  transport_bindings: []
  artifact_summary:
  - action: EXTEND
    subdomain: catalog
    count: '6'
    artifacts: book_library_mgmt::WF_REGISTER_BOOK_V0, book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0, book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0, book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0, book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0, book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
  - action: NEW
    subdomain: catalog
    count: '0'
    artifacts: ''
  generation_provenance: []
  declared_reach: []
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge:
  - operation: Announcing a moment
    refused_when: The act it names did not complete
    phase: p7
    governing_rule: EMISSION_NOT_FROM_COMPLETING_ENDING
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Announcing a moment
    refused_when: The moment was already announced once
    phase: p7
    governing_rule: EMISSION_NOT_FROM_COMPLETING_ENDING
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  molecule_steps: []
  molecule_step_bindings: []
  test_cases: []
  test_case_values: []
  withdrawn_facts: null
```

HOW. Binding FQDNs are assigned here; business facts and placement decisions are not repeated.

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

## Gate 1 — Design Approval

**Gate 1 closes here.** Stages 0 through 7 are presented for review as a body — a unified review of
the complete design, not a per-stage approval. Approval authorizes Stage 8, the Authoring Mandate.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`9c2c693d882e…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the amendment of the six acts §2 marks EXTEND, each re-rendered whole
from this design, and nothing else.

One row of §2 was added before this closure and is the reason it is worth naming: the design
inventoried the six acts and the six moments and not the actor those acts run as. Every act carries
`book_library_mgmt::AC_LIBRARY_STAFF_V0` in the composition, and an EXTEND re-renders an act whole
from the design — so a design silent about the actor re-renders six acts with none. Construction
Completeness refused the design at 98.2% and named the missing fact six times. The row states what
was always true and changes no decision this dossier took.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | Ownership, artifacts requiring action | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
