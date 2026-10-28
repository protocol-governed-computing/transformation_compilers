# Findings — Step 4, the Copy Family

The front end derives the copy family's P7 rows from the ledger. The derived rows are compared
with the same rows of the baseline P7.

## What was built

| File | Role |
|---|---|
| `history/ledger_copy_family.yaml` | The copy family in closed shapes. It was normalized by hand from the authored ledger and the owner's answers. |
| `history/ledger_to_p7.py` | The front end: two operation patterns (`create`, `transition`), shared components and five doctrine rules |
| `engine/p7_slice.py` | Cuts a family's rows out of a P7 |
| `engine/compare.py` | Diffs derived rows against the baseline slice. Prose summaries are excluded. |
| `history/generated_copy_family.json` | The derived rows |

Reproduce from `transformation_compilers/decision_authoring_prototype/domains/book_library_mgmt/`:

```
python history/ledger_to_p7.py history/ledger_copy_family.yaml > history/generated_copy_family.json
python ../../engine/compare.py <baseline P7> history/generated_copy_family.json CC_CLAIM_COPY_BARCODE_V0
```

## Result

| | Rows |
|---|---:|
| Identical to the baseline | 95 |
| Changed | 7 |
| Baseline only | 14 |
| Derived only | 11 |
| Derived rows traced to a ledger entry | 79 |
| Derived rows traced to a doctrine rule | 34 |
| Derived rows with no trace | 0 |

The ledger section for the family is about 60 lines. The baseline slice is 116 rows.

Every difference has one of four causes:

| Cause | Changed | Baseline only | Derived only | Source |
|---|---:|---:|---:|---|
| A. The barcode claim moves after the book check | 5 | 11 | 6 | doctrine `order`; a defect in the baseline |
| B. The unused `copy_fields` input is dropped | | 3 | | no ledger entry; a defect in the baseline |
| C. Retire and reinstate require the starting state | 2 | | | ledger precondition, inferred; the owner must confirm |
| D. Reinstatement announces an event | | | 5 | owner's answer |

### A. A refused registration consumes its barcode (a defect, confirmed by a probe)

The baseline claims the barcode in `CC_CLAIM_COPY_BARCODE_V0` before `CC_REGISTER_PHYSICAL_COPY_V0`
checks that the book exists. A probe against the current snapshot showed the effect:

```
copy BC-X vs unknown book    NOT_FOUND
copy BC-X vs real book       ALREADY_EXISTS   (no copy record written)
```

The refused registration leaves the claim behind, so the barcode can never be used again.
Doctrine `order` checks the precondition before the claim. The derived design folds the claim into
the registering component, between the book read and the write. This removes one artifact.

### B. `copy_fields` is required and never read

The request and the component both require `copy_fields`. No step reads it, because the copy
record is assembled from `identity_key`, `barcode` and a fixed state. This is why "a copy is
registered as registered, whatever state the request gives it" holds. Nothing in the ledger asks
for the field, so the derived design does not carry it.

### C. Retiring an already-retired copy succeeds

The probe showed `retire already-retired copy → SUCCESS`, with a second trail entry. The derived
filter adds the starting state (`state: REGISTERED` for retire, `RETIRED` for reinstate). A
transition from the wrong state then matches nothing and is refused. This came from an inference
by the blind author. The owner has not confirmed it.

### D. Reinstatement announces an event

This comes from the owner's answer. The derived design adds `EV_PHYSICAL_COPY_REINSTATED_V0` and
its emit property.

## One miss in the doctrine

The first run left out `format: date-time` on event timestamps. The baseline holds it. The
doctrine `interface` now includes it. This is the kind of gap the pattern library will keep
showing until it covers the platform's conventions.

## Limits

- **The ledger was normalized by hand.** The authored ledger mixes prose into answer values, for
  example "the book is registered or retired". The format's shapes were not closed enough for a
  machine to read. Format V1 needs a schema for each answer shape.
- **The rows are compared, not run.** The derived rows have not been spliced into a P7, validated
  by the Design Compiler, built, or executed. Step 5 does that.
- **Names partly follow the baseline.** Doctrine `naming` (head noun, role noun) was chosen to fit
  the baseline's codes. A second domain tests whether it holds.
- **One family.** The patterns cover create and transition. Search, update, retrieve and the
  work/edition operations need four more patterns: validate, form key, filter/group and assemble
  details.

## Revision: shared components are reused, not folded

The first version folded the barcode claim into the registering component. The splice showed that
`WF_REGISTER_BOOK_V0` also uses `CC_CLAIM_COPY_BARCODE_V0` and `CC_REGISTER_PHYSICAL_COPY_V0`, so
the fold would have changed a workflow outside the family. The `create` pattern now keeps the claim
as its own component. It puts the precondition before the claim by reusing the book's existing
`CC_RESOLVE_BOOK_IDENTITY_V0`.

| | Rows |
|---|---:|
| Identical to the baseline | 110 |
| Changed / baseline only / derived only | 3 / 3 / 7 |
| Derived rows with no trace | 0 |

The remaining 13 differences:

- **Precondition before claim.** One routing change and one new node in
  `WF_REGISTER_PHYSICAL_COPY_V0`, plus one binding. Doctrine `order`.
- **`copy_fields` dropped.** Three rows. The splice also drops the matching binding in
  `WF_REGISTER_BOOK_V0`.
- **From-state filters.** Two rows. The owner confirmed this decision: a transition from the
  wrong state is refused.
- **Reinstatement event.** Five rows. This is the owner's answer.

## Step 5 — spliced, constructed, compiled, assembled, run

Everything ran in the scratch space. The domain repositories and the working snapshot were not
touched.

1. `engine/splice.py` replaced the family's rows in copies of the domain's P7 and P8.
2. `tc construction check` gave **Construction Completeness 100.0%** (1942/1942 determined,
   56 artifacts). The baseline gives 1922/1922 and 55 artifacts.
3. `tc construction emit` wrote the artifacts into a copy of the domain.
4. `compile_domain.sh` built it (1 succeeded, 0 failed). Transform conformance showed 4 proven
   and 0 refused.
5. A side assembly with the other compiled roots passed composition conformance and the
   round-trip check.
6. Both execution validations ran against the side snapshot: **23/23** and **27/27** criteria
   hold.
7. The probe (`probes/probe_copy_family.py`) was run against both snapshots:

| Probe | Current snapshot | Derived design |
|---|---|---|
| Copy registered against an unknown book | NOT_FOUND | NOT_FOUND |
| Then the same barcode against a real book | ALREADY_EXISTS, no record written | **SUCCESS**, record written |
| Retire an unknown copy | VIOLATION | VIOLATION |
| Retire an already-retired copy | SUCCESS, trailed twice | **VIOLATION** |

The derived design keeps every stated criterion and fixes both defects.

### Findings from the run

- **Register-book has the same orphan-claim shape.** It claims the book identity, then the
  barcode. A duplicate barcode leaves the book identity claimed with no book written. A general
  rule should hold: after the first claim that can be refused, nothing may refuse. Otherwise
  claims need compensation. This belongs in doctrine `order`.
- **Emit rewrites every artifact's formatting.** The emitted registry differs from the hand-kept
  one in files the design did not change. Section order and an "Intent" heading differ. The
  difference is presentation, but it makes a registry diff noisy.
- **Summaries are prose the ledger does not yet carry.** The derived summaries ("Retire a
  physical copy") replace the authored ones. The ledger's `about` text, or an explicit summary
  answer, should supply them.
