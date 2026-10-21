# VOCAB_DESIGN_REGISTER_TERMS_V0

## Machine

```yaml
fqdn: transformation::VOCAB_DESIGN_REGISTER_TERMS_V0
artifact_kind: VOCABULARY
version: v0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: design
extends: ''
artifact_family:
  casing: UPPER_SNAKE
  entries:
  - AC
  - IN
  - WF
  - CC
  - CT
  - EV
  - RB
  - VOCAB
  - STRUCTURE
  - TI
  - TE
approval_state:
  casing: UPPER_SNAKE
  entries:
  - APPROVED
  - MIGRATED
  - RECONFIRMED
belief_result:
  casing: UPPER_SNAKE
  entries:
  - VERIFIED
  - NOT_FOUND
  - INSUFFICIENT_EVIDENCE
certainty:
  casing: UPPER_SNAKE
  entries:
  - HIGH
  - MEDIUM
  - LOW
clarification_owner:
  casing: UPPER_SNAKE
  entries:
  - HUMAN
  - SNAPSHOT
  - GOVERNANCE
classification:
  casing: UPPER_SNAKE
  entries:
  - NEW_SUBDOMAIN
  - EXTEND_SUBDOMAIN
  - MODIFY
  - DEPRECATE
composition_kind:
  casing: UPPER_SNAKE
  entries:
  - CT
  - CS
dependency_disposition:
  casing: UPPER_SNAKE
  entries:
  - EXISTING
  - EXTEND
  - REUSE
  - AUTHOR_NEW
  - INVESTIGATE
dependency_status:
  casing: UPPER_SNAKE
  entries:
  - SATISFIED
  - GAP
evidence_status:
  casing: UPPER_SNAKE
  entries:
  - OBSERVED
  - INFERRED
  - OPEN
expected_outcome:
  casing: UPPER_SNAKE
  entries:
  - SUCCESS
  - VIOLATION
field_direction:
  casing: UPPER_SNAKE
  entries:
  - INPUT
  - OUTPUT
fit:
  casing: UPPER_SNAKE
  entries:
  - EXACT
  - PARTIAL
  - MISMATCH
gap_resolution:
  casing: UPPER_SNAKE
  entries:
  - REPLACE
  - EXTEND
  - NEW
handler_kind:
  casing: UPPER_SNAKE
  entries:
  - WF_INVOCATION
  - SNAPSHOT_READ
interface_direction:
  casing: UPPER_SNAKE
  entries:
  - INPUT
  - OUTPUT
  - ATTRIBUTE
inventory_action:
  casing: UPPER_SNAKE
  entries:
  - REPLACE
  - REUSE
  - EXTEND
  - REPOINT
  - REVIEW
molecule_binding_role:
  casing: UPPER_SNAKE
  entries:
  - INPUT
  - CARRY
  - UPDATE
node_type:
  casing: UPPER_SNAKE
  entries:
  - IN
  - CC
  - EXIT
  - EXIT_SUCCESS
ownership_disposition:
  casing: UPPER_SNAKE
  entries:
  - OWNED
  - SATISFIED
  - DEFERRED
placement_decision:
  casing: UPPER_SNAKE
  entries:
  - NEW_SUBDOMAIN
  - EXTEND
pps_action:
  casing: UPPER_SNAKE
  entries:
  - REPLACE
  - REVIEW
  - REUSE
  - EXTEND
purpose_disposition:
  casing: UPPER_SNAKE
  entries:
  - INHERITED
  - REFINED
record_model:
  casing: UPPER_SNAKE
  entries:
  - MUTABLE_STATE
  - APPEND_ONLY_JOURNAL
  - IDENTITY_REGISTRY
  - HYBRID
resolution_status:
  casing: UPPER_SNAKE
  entries:
  - CLOSED
  - OPEN
reuse_decision:
  casing: UPPER_SNAKE
  entries:
  - REUSE
  - EXTEND
  - AUTHOR_NEW
saturation_status:
  casing: UPPER_SNAKE
  entries:
  - SATISFIED
  - NOT_SATISFIED
scope_relationship:
  casing: UPPER_SNAKE
  entries:
  - CREATED
  - EXTENDED
  - MODIFIED
  - DEPRECATED
  - ADJACENT
scope_status:
  casing: UPPER_SNAKE
  entries:
  - IN_SCOPE
  - DEFERRED
storage_type:
  casing: UPPER_SNAKE
  names_kind: CAPABILITY_SIDE_EFFECT
  entries:
  - CS_APPENDONLY_JSONL_V0
  - CS_MUTABLE_JSON_V0
  - CS_REGISTRY_V0
test_value_role:
  casing: UPPER_SNAKE
  entries:
  - INPUT
  - EXPECTED
  - ASSERT
  - RECORDED
transport_direction:
  casing: UPPER_SNAKE
  entries:
  - INGRESS
  - EGRESS
verification_result:
  casing: UPPER_SNAKE
  entries:
  - CONFIRMED
  - OVERTURNED
yes_no:
  casing: UPPER_SNAKE
  entries:
  - 'YES'
  - 'NO'
```

---

## Intent

The closed sets a phase document's registers draw on. Each register schema names the group a
column takes its values from, and nothing restates a group's entries.
