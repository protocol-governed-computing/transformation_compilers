# Stage 2 — Domain Model Discovery: book_library_mgmt / catalog

## Machine

```yaml
document:
  phase: p2
  domain: book_library_mgmt
  subdomain: catalog
  cr: cr_03_catalog
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Work
    description: Something the library carries, independent of any edition.
    store_model: Held by the catalog.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: Book
    description: An edition of a work.
    store_model: Held by the catalog.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: Physical copy
    description: One copy of a book, on a shelf.
    store_model: Held by the catalog.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - entity: Moment
    description: Something the catalog announces because the business declared it matters.
    store_model: Declared, and referred to by nothing.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 7}
  entity_attributes:
  - entity: Moment
    attribute: What it names
    meaning: The act whose completion it announces.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_events, row: 1}
  - entity: Moment
    attribute: Whether it is announced
    meaning: Whether anything in the composition refers to it.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - entity: Book
    attribute: State
    meaning: Whether it is in service or retired.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: lifecycle_states, row: 1}
  - entity: Physical copy
    attribute: State
    meaning: Whether it is in service or retired.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: lifecycle_states, row: 3}
  business_processes:
  - process: Registering a work, a book or a physical copy
    initiator: The library
    outcome: The thing is held by the catalog.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - process: Correcting bibliographic information
    initiator: The library
    outcome: What the library publishes is changed.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - process: Retiring a book or a physical copy
    initiator: The library
    outcome: The thing is out of service; what is known about it is kept.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - process: Reinstating a book or a physical copy
    initiator: The library
    outcome: The thing is back in service.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - process: Announcing a moment
    initiator: The completion of the act it names
    outcome: Nothing. No act announces anything today.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  process_steps:
  - process: Announcing a moment
    step: '1'
    action: Complete the act the moment names.
    record_produced: The act's own record.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 3}
  - process: Announcing a moment
    step: '2'
    action: Announce the moment, carrying which thing it concerns and when.
    record_produced: The announcement.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 7}
  belief_verification:
  - belief: The catalog declares six moments and announces none of them.
    result: VERIFIED
    evidence: Six are declared — `book_library_mgmt::EV_WORK_REGISTERED_V0`, `EV_BOOK_REGISTERED_V0`, `EV_PHYSICAL_COPY_REGISTERED_V0`, `EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0`, `EV_BOOK_RETIRED_V0`, `EV_PHYSICAL_COPY_RETIRED_V0`. Each reports a reference count of zero, and no workflow in the domain announces anything at all.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The catalog performs registration, correction, retirement and reinstatement, each as its own act.
    result: VERIFIED
    evidence: Ten workflows are held for this subdomain, including registration of a book, an additional edition and a physical copy; correction of bibliographic information; retirement and reinstatement of both a book record and a physical copy.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: Nothing checks whether a declared moment is ever announced.
    result: VERIFIED
    evidence: No rule relates a declared moment to a reference to it. The six have been declared and silent since the subdomain was built, and nothing has reported a fault.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: Reinstatement has no declared moment of its own.
    result: VERIFIED
    evidence: Two workflows reinstate, and neither a book reinstated nor a copy reinstated appears among the six declared moments. The business's ruling that reinstatement is silent and the composition agree.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  pps_baseline_fqdns:
  - capability: Registers a book
    fqdn: book_library_mgmt::WF_REGISTER_BOOK_V0
    what_it_does: Registers an edition of a work.
    fit: PARTIAL
    cannot_do: Announces nothing.
  - capability: Registers an additional edition
    fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
    what_it_does: Registers a further edition of a work already carried.
    fit: PARTIAL
    cannot_do: Announces nothing.
  - capability: Registers a physical copy
    fqdn: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
    what_it_does: Puts a copy on a shelf.
    fit: PARTIAL
    cannot_do: Announces nothing.
  - capability: Corrects bibliographic information
    fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
    what_it_does: Changes what the library publishes about a book.
    fit: PARTIAL
    cannot_do: Announces nothing.
  - capability: Retires a book
    fqdn: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
    what_it_does: Takes an edition out of service.
    fit: PARTIAL
    cannot_do: Announces nothing.
  - capability: Retires a physical copy
    fqdn: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
    what_it_does: Takes a copy out of service.
    fit: PARTIAL
    cannot_do: Announces nothing.
  - capability: Reinstates a book
    fqdn: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
    what_it_does: Returns an edition to service.
    fit: EXACT
    cannot_do: Nothing; the business has ruled reinstatement silent.
  - capability: Reinstates a physical copy
    fqdn: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
    what_it_does: Returns a copy to service.
    fit: EXACT
    cannot_do: Nothing; the business has ruled reinstatement silent.
  - capability: Declares that a work was registered
    fqdn: book_library_mgmt::EV_WORK_REGISTERED_V0
    what_it_does: Names the moment.
    fit: PARTIAL
    cannot_do: Is referred to by nothing and is therefore never announced.
  - capability: Declares that a book was registered
    fqdn: book_library_mgmt::EV_BOOK_REGISTERED_V0
    what_it_does: Names the moment.
    fit: PARTIAL
    cannot_do: The same.
  - capability: Declares that a physical copy was registered
    fqdn: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
    what_it_does: Names the moment.
    fit: PARTIAL
    cannot_do: The same.
  - capability: Declares that bibliographic information was updated
    fqdn: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    what_it_does: Names the moment.
    fit: PARTIAL
    cannot_do: The same.
  - capability: Declares that a book was retired
    fqdn: book_library_mgmt::EV_BOOK_RETIRED_V0
    what_it_does: Names the moment.
    fit: PARTIAL
    cannot_do: The same.
  - capability: Declares that a physical copy was retired
    fqdn: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    what_it_does: Names the moment.
    fit: PARTIAL
    cannot_do: The same.
  gaps:
  - gap: No act announces any moment.
    severity: CRITICAL
    impact: The whole of this change. Six declared moments are silent.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - gap: Nothing checks that a declared moment is announced.
    severity: CRITICAL
    impact: The silence returned unnoticed once and would again.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - gap: The moment naming a registered work has no single act that plainly produces it.
    severity: OPEN QUESTION
    impact: Registration of a book and of an additional edition both concern works; which announces a work registered is not evident from the composition.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: assumptions, row: 1}
  architectural_observations:
  - observation: A declared moment that nothing refers to is indistinguishable, from the outside, from a moment the business never declared.
    evidence: Reference count of zero on all six.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - observation: This is the same defect a different domain was found to have, in the same shape and for the same reason.
    evidence: Six moments here; three in the identity function of another domain, all silent, none checked.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - observation: Every act this change touches already exists and needs no new capability. Only where each act ends is changed.
    evidence: Ten workflows held for this subdomain, all performing their acts today.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - observation: The business's ruling and the composition agree that reinstatement is silent, so this change removes a question rather than answering one.
    evidence: Two reinstatement workflows, no declared moment for either.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  discovery_concerns:
  - concern: The business believed the catalog announced six moments and it announced none. Nothing reported a fault, because nothing checks.
    evidence: Reference count of zero on all six, and no announcement anywhere in the domain.
    severity: CRITICAL
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - concern: Two acts register something that concerns a work, and only one moment names a work registered. Attaching it to the wrong act would announce something untrue.
    evidence: Registration of a book and of an additional edition both exist.
    severity: MAJOR
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: assumptions, row: 1}
  open_questions:
  - question: Which act announces that a work was registered — registering a book, or registering an additional edition?
    category: business
    why_it_matters: A moment attached to the wrong act announces something untrue.
    source_finding: {phase: p1, register: assumptions, row: 1}
```

Every belief carried from Stage 1 was grounded against the pinned snapshot through the inspection
interface. What was searched is recorded, not only what was found.

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
