# Plan — Generating a Second Domain

The generator derives `book_library_mgmt` from its ledger. This plan extends it to derive
`blockchain` from a ledger written in the same format. The book domain must still derive, build and
pass after every step.

## What blockchain needs that book does not

| Need | Book today | Blockchain |
|---|---|---|
| Parts | one subdomain | identity and wallet, each with its own stores, trail and bindings |
| Actor | staff, authorized by credentials | a participant acting for themselves; no authorization step |
| Public entrance | none | entrances for three acts, with answer classes |
| Reading another part | none | wallet reads identity's actors and never writes them |
| Derived values | key formation only | an address from a key; an identity from the holder |
| A repeat that succeeds | refused or reused | a repeated registration records its details and announces its own event |
| Field required by one act | none | grounds, required to reject and optional to accept |
| Values the business fixes | state only | a new wallet's balance, currency, classification and state |
| Defaults | none | preferred currency and language |
| Time on the trail | no clock step | read from the clock, on every moment |

## A rule the plan rests on: the published surface is carried

The blockchain suites read stores by path and records by field. They send requests in today's
shape, and the browser client does too. A design that renamed a store would orphan the data already
on disk. A design that reshaped a request would break every caller.

So the generator carries three things from the baseline instead of deriving them:

- **store names and paths;**
- **request shapes** of every act and entrance;
- **the keys of trail records.**

These are facts about the existing composition, not decisions. The ledger can change one only by
saying so, and the change is then a migration the owner decides. The book run already carried its
code-backed transforms the same way.

The rule is general. It holds for any domain that already exists, which is every domain, because
evolution is never greenfield.

## Steps

Each step ends with the book pipeline passing and its `generated.json` unchanged, unless the step
says otherwise.

1. **Doctrine becomes data.** Move the doctrine rules out of the module docstring into
   `engine/doctrine.yaml`, each with a name and a statement. Add the three the blind run restated as
   answers: an act states its own values, a request cannot widen a rule, and a failed record ends
   the act. Rows keep citing `doctrine:<name>`. Update `LEDGER_FORMAT_V0.md`: the catalog gains the
   nine question types, and doctrine is listed as fixed rules the author reads but does not answer.

2. **Parts.** The ledger gains `parts:`. Each part has its own things, operations, trail and
   announcements. One part yields today's output. The book ledger is read as one part, unchanged.

3. **Carried surface.** Read the baseline's store names and paths, request fields and trail record
   keys, and use them where the ledger names the same thing. Rows cite `carried:surface`.

4. **Actor modes.** `authorization: none` drops the authorization step and the credential fields.
   Book keeps `staff`.

5. **New patterns**, one at a time, each with a probe before the whole domain is tried:
   - `register` with `on_repeat`: claim the identity; on a repeat, record the submitted details and
     announce the repeat event; the actor is unchanged.
   - `decide`: a transition guarded by state, the self-decision rule and `required_when`, changing
     only the fields `invariant_on_change` lists.
   - `list`: select by a caller-named state; an empty list is an answer.
   - `create` with `reads_other_part`, `derived_value` and fixed values: resolve the holder in the
     other part, require the accepted state, derive the identity and the address, claim both, write
     the record, trail it.

6. **Reading another part.** A pattern that reads another part's store emits `declared_reach` and
   binds that part's resolution, and never a write to it.

7. **Trail time.** A doctrine rule that every moment carries the clock's time. Book's output
   changes here. This is the one deliberate change to book, and its suites must still pass.

8. **Offering.** `public_acts`, `entrance_turns_away` and `outcome_classes` render TI and TE
   artifacts and `transport_bindings`. An entrance requires what the act requires, so a request
   missing a detail is turned away before the act runs.

9. **Blockchain ledger.** Normalize the blind run and the owner answers into
   `domains/blockchain/ledger.yaml`, in closed shapes, each value citing its source.

10. **Whole domain.** Run `run_pipeline.sh blockchain`. The target is 100% construction, every
    criterion in the three domain suites, and all nine checks of the owner's answers. Then rerun
    book.

## What could stop it

- **Construction may lack a form for one of the new needs.** If the design language cannot state
  something, I stop and report it. I do not work around it.
- **The routing-closure suite reads the trace.** It expects an act to stop at the step whose record
  failed. Doctrine already ends a component on any failed status, so it should hold.
- **A domain-wide splice.** Blockchain has two parts. `splice.py` replaces whole registers, and the
  P8 rebuild must cover both parts. This is untested.

## Files

| File | Change |
|---|---|
| `engine/generate_domain.py` | parts, carried surface, actor modes, five patterns, reach, offering |
| `engine/doctrine.yaml` | new: the doctrine rules as data |
| `engine/splice.py` | the new registers and two parts, if needed |
| `doc/LEDGER_FORMAT_V0.md` | the nine question types; doctrine as fixed rules |
| `domains/blockchain/ledger.yaml` | new |
| `domains/blockchain/probes/` | new: one probe per pattern |
| `domains/blockchain/FINDINGS_STEP5_WHOLE_DOMAIN.md` | new: the result |
| `domains/book_library_mgmt/generated.json` | regenerated; changes only at step 7 |

Nothing outside `decision_authoring_prototype/` changes.
