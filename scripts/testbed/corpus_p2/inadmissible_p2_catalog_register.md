# Stage 2 — Domain Model Verification: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p2
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_01_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Book
    description: A published material the library catalogs — the general term for anything it catalogs, including materials that are not books.
    store_model: One durable record per book, addressed by its title, author and publication year together, updatable in place, and markable retired and registered again.
    evidence_status: INFERRED
    source_finding:
    - {phase: p1, register: business_vocabulary, key: Book}
    - {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Physical Copy
    description: An individual copy the library owns, belonging to exactly one book.
    store_model: One durable record per copy, addressed by its barcode, naming the single book it belongs to, and markable retired and registered again.
    evidence_status: INFERRED
    source_finding:
    - {phase: p1, register: business_vocabulary, key: Physical Copy}
    - {phase: p1, register: identity_and_sameness, row: 2}
  entity_attributes:
  - entity: Book
    attribute: Title
    meaning: The title the book is published under; part of what identifies it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: 'a book''s bibliographic information is title, author, publication year and subject'}
  - entity: Book
    attribute: Author
    meaning: The author the book is published under; part of what identifies it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: bibliographic information}
  - entity: Book
    attribute: Publication Year
    meaning: The year this edition was published; part of what identifies it, and what distinguishes one edition from another.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Book
    attribute: Subject
    meaning: What kind of book it is. A book carries at least one and may carry several.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: a book carries at least one subject and may carry several}
  - entity: Book
    attribute: State
    meaning: Whether the book is registered or retired.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_states, key: Book}
  - entity: Physical Copy
    attribute: Barcode
    meaning: The identifier the library assigns to this copy; what identifies it among all copies the library owns.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - entity: Physical Copy
    attribute: Book
    meaning: The single book this copy belongs to.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: each physical copy belongs to exactly one book}
  - entity: Physical Copy
    attribute: State
    meaning: Whether the copy is registered or retired.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_states, key: Physical Copy}
  business_processes:
  - process: Register a book
    initiator: Authorized staff
    outcome: The catalog holds one authoritative record for the book, and one for the physical copy registered with it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Book Registered}
  - process: Register a physical copy
    initiator: Authorized staff
    outcome: The catalog holds one authoritative record for a further copy of a registered book.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Physical Copy Registered}
  - process: Update bibliographic information
    initiator: Authorized staff
    outcome: The book's authoritative description reflects the change, or the update is refused for making the book a duplicate of another.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Bibliographic Information Updated}
  - process: Retire a book record
    initiator: Authorized staff
    outcome: The book record is retired, excluded from search, still retrievable, and its copies unaffected.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Book Retired}
  - process: Retire a physical copy
    initiator: Authorized staff
    outcome: The copy record is retired and the book record is unaffected, including when it was the last copy.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Physical Copy Retired}
  - process: Reinstate a book record
    initiator: Authorized staff
    outcome: The retired book record is registered again and appears in search.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 3}
  - process: Reinstate a physical copy
    initiator: Authorized staff
    outcome: The retired copy record is registered again.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 6}
  - process: Search the catalog
    initiator: Authorized staff
    outcome: The bibliographic information of each registered book matching the subject or title searched for.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: staff search the catalog by subject or by title}
  - process: Retrieve complete book details
    initiator: Authorized staff
    outcome: The book's bibliographic information and the physical copies the library holds of it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: retrieving complete book details returns the bibliographic information and the copies}
  process_steps:
  - process: Register a book
    step: '1'
    action: Confirm the staff member is authorized to perform catalog operations
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Register a book
    step: '2'
    action: Confirm at least one physical copy is offered with the book
    record_produced: A completeness decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - process: Register a book
    step: '3'
    action: Confirm the book carries at least one subject
    record_produced: A completeness decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 3}
  - process: Register a book
    step: '4'
    action: Confirm no registered book already carries this title, author and publication year
    record_produced: A sameness decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Register a book
    step: '5'
    action: Record the book's bibliographic information as its authoritative record, registered
    record_produced: The book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: each book has exactly one authoritative record}
  - process: Register a book
    step: '6'
    action: Record the offered copy against the book, registered
    record_produced: The physical copy record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: registering a book requires at least one physical copy}
  - process: Register a book
    step: '7'
    action: Record that the book was registered
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: every business operation is traceable and auditable}
  - process: Register a physical copy
    step: '1'
    action: Confirm the staff member is authorized to perform catalog operations
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Register a physical copy
    step: '2'
    action: Confirm the book the copy names is registered in the catalog
    record_produced: An existence decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 4}
  - process: Register a physical copy
    step: '3'
    action: Confirm no copy the library owns already carries this barcode
    record_produced: A sameness decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 5}
  - process: Register a physical copy
    step: '4'
    action: Record the copy against that book, registered
    record_produced: The physical copy record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: each copy has exactly one authoritative record}
  - process: Register a physical copy
    step: '5'
    action: Record that the copy was registered
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - process: Update bibliographic information
    step: '1'
    action: Confirm the staff member is authorized to perform catalog operations
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Update bibliographic information
    step: '2'
    action: Confirm the changed title, author and publication year would not match another registered book
    record_produced: A sameness decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 6}
  - process: Update bibliographic information
    step: '3'
    action: Record the changed bibliographic information as the book's authoritative description
    record_produced: The updated book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Bibliographic Information Updated}
  - process: Update bibliographic information
    step: '4'
    action: Record that the book's information was updated
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - process: Retire a book record
    step: '1'
    action: Confirm the staff member is authorized to perform catalog operations
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Retire a book record
    step: '2'
    action: Record the book record as retired, leaving its copies as they are
    record_produced: The retired book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 2}
  - process: Retire a book record
    step: '3'
    action: Record that the book was retired
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - process: Retire a physical copy
    step: '1'
    action: Confirm the staff member is authorized to perform catalog operations
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Retire a physical copy
    step: '2'
    action: Record the copy as retired, leaving the book record as it is
    record_produced: The retired copy record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 5}
  - process: Retire a physical copy
    step: '3'
    action: Record that the copy was retired
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - process: Reinstate a book record
    step: '1'
    action: Confirm the staff member is authorized to perform catalog operations
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Reinstate a book record
    step: '2'
    action: Record the retired book record as registered again
    record_produced: The registered book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 3}
  - process: Reinstate a book record
    step: '3'
    action: Record that the book was returned to the registered state
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - process: Reinstate a physical copy
    step: '1'
    action: Confirm the staff member is authorized to perform catalog operations
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Reinstate a physical copy
    step: '2'
    action: Record the retired copy as registered again
    record_produced: The registered copy record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 6}
  - process: Reinstate a physical copy
    step: '3'
    action: Record that the copy was returned to the registered state
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - process: Search the catalog
    step: '1'
    action: Confirm the staff member is authorized to perform catalog operations
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Search the catalog
    step: '2'
    action: Select the registered books whose subject or title matches what was searched for, excluding retired books
    record_produced: The matching set
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: a retired book is excluded from search results}
  - process: Search the catalog
    step: '3'
    action: Return the bibliographic information of each matching book, and nothing about its copies
    record_produced: The search result
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: a search returns the bibliographic information of each matching book}
  - process: Search the catalog
    step: '4'
    action: Record that the catalog was searched
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - process: Retrieve complete book details
    step: '1'
    action: Confirm the staff member is authorized to perform catalog operations
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Retrieve complete book details
    step: '2'
    action: Read the book's authoritative record, whether registered or retired
    record_produced: The book record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: a retired book's details remain retrievable}
  - process: Retrieve complete book details
    step: '3'
    action: Read the physical copies recorded against that book
    record_produced: The copies held
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: complete details return the copies the library holds}
  - process: Retrieve complete book details
    step: '4'
    action: Record that the book's details were retrieved
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  belief_verification:
  - belief: book_library_mgmt does not appear to be part of the current software baseline.
    result: NOT_FOUND
    evidence: The composition declares five domains — ai_governance, inspection, platform, transformation, workload — and its artifact index carries no identity in the book_library_mgmt namespace.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: No capability in the current composition manages a library catalog.
    result: NOT_FOUND
    evidence: 'Semantic vocabulary search returns no identity for book, library, copy, subject, title or barcode. The only identities matching catalog are inspection::TI_SI_CATALOG_V0 and inspection::TE_SI_CATALOG_V0, which publish the list of snapshot-inspection operations and carry no library meaning. No declared store holds library records: the five declared stores belong to ai_governance and workload.'
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  pps_baseline_fqdns:
  - capability: Uniqueness registry
    fqdn: capability_side_effects::CS_REGISTRY_V0
    what_it_does: Registers a key, resolves it, reports whether it exists, counts and deregisters.
    fit: PARTIAL
    cannot_do: It enforces uniqueness on one key; a book is identified by title, author and publication year together, and the composite is not a key it forms.
  - capability: Durable record store
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    what_it_does: Writes, reads, lists, updates in place and deletes durable records.
    fit: EXACT
    cannot_do: It holds whatever it is given; it enforces no identity, no state and no authorization.
  - capability: Append-only trail
    fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    what_it_does: Appends an entry and returns the whole trail.
    fit: EXACT
    cannot_do: It appends what it is handed; it does not decide which operations must be recorded.
  - capability: Audit composition
    fqdn: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    what_it_does: Composes the recording of a performed action into an append-only store.
    fit: PARTIAL
    cannot_do: It carries agent-governance semantics and appends to another subdomain's store; a subdomain owns its stores exclusively.
  - capability: Record shape validation
    fqdn: ai_governance::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    what_it_does: Confirms a record carries the fields its contract declares.
    fit: EXACT
    cannot_do: It does not know which fields a book or a copy requires.
  - capability: Record assembly
    fqdn: capability_transforms::CT_PURE_ASEMBLE_RECORD_V0
    what_it_does: Assembles a durable record from supplied values.
    fit: EXACT
    cannot_do: It applies no identity rule and decides no sameness.
  - capability: Record selection
    fqdn: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    what_it_does: Selects the records matching stated criteria.
    fit: EXACT
    cannot_do: It knows nothing of registered and retired, so exclusion of retired books must be stated as criteria.
  - capability: Parameter rule validation
    fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    what_it_does: Confirms supplied parameters satisfy declared rules.
    fit: EXACT
    cannot_do: It carries no catalog rule of its own.
  - capability: Business actor
    fqdn: ai_governance::AC_EMPLOYEE_V1
    what_it_does: Declares a business actor whose identity an operation binds.
    fit: PARTIAL
    cannot_do: It names an employee of another subdomain and asserts no authorization to perform catalog operations.
  - capability: Business entry point
    fqdn: ai_governance::IN_PROVISION_LICENSE_V0
    what_it_does: Declares the governed entry point through which a business operation is requested.
    fit: EXACT
    cannot_do: It admits a licensing request, not a catalog operation.
  - capability: Governed operation pipeline
    fqdn: ai_governance::CC_WRITE_LICENSE_V0
    what_it_does: Composes one business operation as an ordered pipeline of governed steps.
    fit: EXACT
    cannot_do: It carries licensing semantics; the catalog's operations must be authored.
  - capability: Subdomain storage declaration
    fqdn: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
    what_it_does: Declares the stores a business subdomain owns and the paths they occupy.
    fit: EXACT
    cannot_do: It declares another subdomain's stores.
  - capability: Runtime binding declaration
    fqdn: ai_governance::RB_LICENSE_BINDINGS_V1
    what_it_does: Binds a subdomain's workflows to the stores and policies they use.
    fit: EXACT
    cannot_do: It binds another subdomain's surface.
  - capability: Business moment
    fqdn: ai_governance::EV_LICENSE_PROVISIONED_V1
    what_it_does: Declares a business moment the domain recognises when an operation completes.
    fit: EXACT
    cannot_do: It names a licensing moment, not a catalog one.
  gaps:
  - gap: Nothing in the composition holds a book record, so CC_REGISTER_BOOK_V0 must be authored.
    severity: CRITICAL
    impact: Every requested outcome depends on a durable authoritative record per book and per copy; the store mechanisms exist, the catalog's own stores do not.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: No capability registers a book, registers a copy, updates bibliographic information, retires a record, reinstates a record, searches, or retrieves book details.
    severity: CRITICAL
    impact: The nine business processes have no counterpart in the composition and must all be authored.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: No actor exists for library staff, and none asserts authorization to perform catalog operations.
    severity: CRITICAL
    impact: Every operation is refused unless the staff member is authorized, and there is nothing to bind that decision to.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - gap: No business moment exists for a book or copy being registered, updated, retired or reinstated.
    severity: CRITICAL
    impact: Five business events are declared and none is recognised anywhere in the composition.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_events, key: Book Registered}
  - gap: Uniqueness on a composite of title, author and publication year has no counterpart in the composition.
    severity: CRITICAL
    impact: Duplicate prevention is the business problem this change exists to solve, and the registry available enforces uniqueness on a single key.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - gap: No audit trail belongs to the catalog; the only audit composition belongs to another subdomain.
    severity: CRITICAL
    impact: Every operation must be traceable, and a subdomain owns its stores exclusively.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_invariants, key: every business operation is traceable and auditable}
  - gap: Subject is free text, so searching by kind of book is only as consistent as what staff type into it.
    severity: MINOR
    impact: 'Noted, not modelled: the business has chosen free text, and no value-set validation applies.'
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, key: a book's subject is free text}
  - gap: Deciding which staff are authorized is deferred to the staff function, which does not exist.
    severity: MINOR
    impact: 'Noted, not modelled: the catalog reads authorization and never grants it.'
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  architectural_observations:
  - observation: A business subdomain in this composition declares its own stores and binds its own workflows to them, so a new subdomain has a worked precedent for owning its records.
    evidence: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1 · ai_governance::RB_LICENSE_BINDINGS_V1
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - observation: Durable records that are written, read, listed and updated in place are available as a declared side effect, as is an append-only trail.
    evidence: capability_side_effects::CS_MUTABLE_JSON_V0 · capability_side_effects::CS_APPENDONLY_JSONL_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - observation: Uniqueness is available as a declared side effect, keyed on a single value.
    evidence: capability_side_effects::CS_REGISTRY_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - observation: Pure transforms already exist for assembling a record, validating its shape, and selecting records by criteria.
    evidence: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 · capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 · capability_transforms::CT_PURE_FILTER_RECORDS_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - observation: Recording a performed action into an append-only trail is already composed as a governed step, within another subdomain.
    evidence: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - observation: 'The composition carries no business vocabulary for a library: no identity claims book, library, copy, subject, title or barcode.'
    evidence: inspection::TI_SI_CATALOG_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  discovery_concerns:
  - concern: The only composed audit step belongs to another subdomain, so satisfying traceability by reusing it would cross a subdomain's ownership of its own stores.
    evidence: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0 · ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - concern: The available uniqueness mechanism is keyed on one value while a book is identified by three attributes together, so duplicate prevention needs a stated key rather than a direct reuse.
    evidence: capability_side_effects::CS_REGISTRY_V0
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - concern: Reinstatement means a record's state moves both ways, so state must be held as data on the record rather than implied by which store it is in.
    evidence: capability_side_effects::CS_MUTABLE_JSON_V0
    severity: MAJOR
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 3}
  - concern: Search must exclude retired books while retrieval must not, so the same records are read under two different rules.
    evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    severity: MINOR
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: a retired book is excluded from search results}
  - concern: The one business actor available names an employee of another subdomain and asserts no authorization, so authorization has nothing to bind to until the staff function exists.
    evidence: ai_governance::AC_EMPLOYEE_V1
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  open_questions: null
```

Every claim about what exists is grounded in the pinned baseline
`41dd01fb1bc94d57c645f5c7fee1f96a7c4f147c98fa5104a6249ce9e6ea4a1d` — 292 artifacts across
ai_governance, inspection, platform, transformation, workload — read through the inspection interface.
The semantic model is inherited from Stage 1 and confirmed here, never re-derived.

---

## 1. Business Entities

### Entity Attributes

---

## 2. Business Processes

### Process Steps

---

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
