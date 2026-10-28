# Findings — The Whole Domain from the Ledger

The front end now derives all of `book_library_mgmt`'s P7 from the ledger: ten operations across
works, books and copies. The result runs through the unchanged pipeline.

## Result

| Measure | Result |
|---|---|
| Ledger (`ledger.yaml`) | 115 lines |
| Baseline P7 | 4,595 lines, 603 register rows |
| Derived rows identical to the baseline | 512 |
| Changed / baseline only / derived only | 24 / 38 / 32 |
| Derived rows traced | 411 ledger, 140 doctrine, 17 carried, **0 untraced** |
| Construction check | **100.0%** (1916/1916 determined, 57 artifacts) |
| Compile | 1 succeeded, 0 failed; transform conformance 4 proven, 0 refused |
| Side assembly | composition conformance passed, round-trip OK |
| Execution validation | **23/23** and **27/27** criteria hold |

Reproduce with `engine/run_pipeline.sh book_library_mgmt <scratch dir>`. It derives, splices, checks, emits, compiles,
assembles and runs both validations in the scratch directory. The probes are
`probes/probe_catalog.py <snapshot>`.

"Carried" means the code-backed transforms (key formation, select, group), their implementation
bindings and their test cases. The ledger decides what they compute. It does not author their
code.

## Behavior: probes against both snapshots

| Probe | Current snapshot | Derived design |
|---|---|---|
| Search for a retired book, no state given | SUCCESS, 1 match | VIOLATION, 0 matches |
| Search, caller asks for `state: RETIRED` | SUCCESS, 1 match | VIOLATION, 0 matches |
| Retire an already-retired book | SUCCESS | VIOLATION |
| Search that matches nothing | VIOLATION | VIOLATION (unrealized, see below) |
| Register a book with a barcode already owned | ALREADY_EXISTS | VIOLATION |
| Then the same book with a free barcode | **ALREADY_EXISTS, book never held** | SUCCESS, held |
| Register a book whose request says `state: RETIRED` | REGISTERED | REGISTERED |
| Copy barcode reused after a refused registration | ALREADY_EXISTS | SUCCESS |

The derived design holds every stated criterion. It also closes four defects in the current
design:

1. **Search shows retired books** unless the caller filters them out. This was the parked search
   gap.
2. **A book refused for a duplicate barcode loses its identity for good.** This is new. The book
   identity is claimed before the barcode, and nothing releases it. The library can never
   register that edition again.
3. **A copy refused for an unknown book loses its barcode for good.** This was found in step 4.
4. **Retiring an already-retired book or copy succeeds** and is trailed twice.

The `state: RETIRED` probe is not a defect. The workflow's literal fixes the state before the
component reads it.

## What changed in the design, and why

| Change | Source |
|---|---|
| `CC_REQUIRE_COPY_BARCODE_FREE_V0` pre-checks the barcode before any claim; claim order book, copy, work | doctrine `order` (defect 2) |
| Precondition before claim in copy registration | doctrine `order` (defect 3) |
| `CC_REGISTER_ADDITIONAL_EDITION_V0` removed; both registrations use `CC_REGISTER_BOOK_V0` | doctrine `reuse` |
| `CC_REGISTER_BOOK_V0` no longer re-validates what `CC_VALIDATE_BOOK_SUBMISSION_V0` already checked | doctrine `order` (validate once) |
| Search keeps only registered books before the caller's criteria | ledger `always_exclude` (defect 1) |
| From-state filters on all four transitions | owner's decision (defect 4) |
| Two reinstatement events | owner's answer |
| Trail subject for register-book is the identity key, not the title | owner's answer |
| `copy_fields` dropped: required, never read | no ledger entry |
| `copy_criteria` moves from a workflow literal into the details component | doctrine `interface` |
| Smaller differences: output naming, an optional field, step numbers | doctrine `interface` |

## Doctrine the domain taught

Each of these came from a failure in this run. None was designed in advance.

- **A workflow answers with its last component.** With the trail last, search and retrieval
  returned empty surfaces, and six criteria failed. A read is trailed before it reads. The
  baseline's order looked arbitrary, but it is a runtime constraint.
- **A workflow reports its last component's status.** A pre-check that routed SUCCESS to
  rejection ended the run rejected but reported SUCCESS. A refusal must be a component that
  returns VIOLATION. Routing alone is not enough.
- **After the first claim that can refuse, nothing else may refuse.** Every later claim is
  pre-checked. Claims have no compensation.
- **Shared components constrain patterns.** `CC_CLAIM_COPY_BARCODE_V0` and
  `CC_REGISTER_PHYSICAL_COPY_V0` serve two workflows. A pattern that reshapes a component for one
  workflow breaks the other.

## Unrealized decision

The owner decided that an empty search returns an empty result. No available transform realizes
it. `CT_PURE_FILTER_RECORDS_V0` supports the presence criteria the search needs, but it refuses
an empty result. `CT_PURE_SELECT_RECORDS_V0` answers empty, but it cannot test presence. The
generator records this as `_unrealized` and does not invent a substitute. Realizing it needs one
transform change, which is a governed change to the code-backed inventory.

## Limits

- **Normalized by hand.** The ledger in closed shapes was transcribed from the authored ledger.
  Format V1 needs a schema per answer shape.
- **The patterns are fitted to one domain.** There are ten operations and nine patterns. Some
  patterns name the domain's own things (`book`, `work`), notably `validate`,
  `register_with_first_child` and `details`. A second domain would show how much of this
  generalizes.
- **Prose summaries are generated placeholders.** They replace the authored summaries in the
  emitted artifacts.
- **Event emission is unconditional.** "Work registered (when new)" cannot be stated, so
  register-book announces a work even when it reuses one. The current design does the same.
- **Emit reformats every artifact.** A registry diff against the hand-kept files is noisy.

## P0's update rule restored

cr_01's P0 says an update may change the title, author or publication year, and is refused only
when the result duplicates another registered book. P1 to P5 carried that rule. The P7 of record
refuses any identity change. The owner chose P0's rule. Recording it in the ledger surfaced two
decisions P0 left open, and the owner answered both:

- **The work.** An edition whose title or author changes moves to the work they name. The work is
  created if it is new. This replaces the earlier answer that a correction never moves an edition.
- **The old identity.** It is freed. The copies follow to the new identity. The trail and past
  events keep the old identity as history.

### What derivation did with them

The update operation now has two paths, and every refusal comes before the first write:

```
resolve → prepare (read, form new key, form work key, assemble, validate)
        → identity unchanged? ── yes → write in place ─────────────────────────┐
                                 no  → claim new identity (duplicate refuses)    │
                                       → claim work (reuse or create)            │
                                       → re-key: write new record, move copies,  │
                                         remove old record, release old claim ──→ trail
```

`CC_CONFIRM_BOOK_IDENTITY_UNCHANGED_V0`, `CC_WRITE_CORRECTED_BOOK_RECORD_V0` and
`CC_REKEY_BOOK_V0` are new. Construction first measured 99.9%: two write-only components declared
no output. Doctrine `interface` now requires one, and construction is back to **100%**
(2076/2076, 60 artifacts). Both validations hold, **23/23** and **27/27**.

### Probes (`probes/probe_update.py`)

| Probe | Current snapshot | Derived design |
|---|---|---|
| Correct the subject only | SUCCESS | SUCCESS |
| Correct the Odyssey into the Iliad (a duplicate) | VIOLATION | ALREADY_EXISTS; nothing changes |
| Correct the Odyssey's year | **VIOLATION** (P0 allows it) | SUCCESS; key moves to `…1615` |
| — its copy follows | — | BC-1 names the new key |
| — the old identity is free: register the 1614 Odyssey again | ALREADY_EXISTS | SUCCESS |
| Retitle the Iliad (its work changes) | VIOLATION | SUCCESS; the new work is created and held |

### Notes

- **A drift the phase rules passed.** The narrowing entered at P7 in cr_01 and stayed through five
  changes. No rule compares P7's behavior with a P5 note. Execution check 17 cannot tell the two
  rules apart, because its case is both a duplicate and an identity change.
- **A missing event.** A retitled edition can create a work, but no "work registered" event is
  announced for it. Conditional emission cannot be stated, which was already noted above.
- **Versioning not applied.** `CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0` changed meaning and keeps
  `_V0`. Versioning through `sameness` is step 4 of `ARCHITECTURE_IMPACT.md`.
