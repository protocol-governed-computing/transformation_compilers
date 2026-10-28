# Findings — Whole `blockchain` Domain from Its Ledger

The generator derives the whole `blockchain` domain, both parts, from a 120-line ledger. The
unchanged pipeline builds it. Run it with:

```
engine/run_pipeline.sh blockchain <scratch dir>
```

## Result

| Measure | Result |
|---|---|
| Construction completeness | 100% (1,332 of 1,332 facts, 46 artifacts) |
| Compile and assembly | pass; composition conformance passed |
| `identity` suite | 26 of 26 criteria hold |
| `routing_closure` suite | 6 of 6 hold |
| `wallet` suite | 12 of 12 hold |
| Checks of the owner's answers | 8 of 9 hold; today's design holds 2 |
| Book domain, rerun | 100% construction, 23 of 23 and 27 of 27; generated design byte-identical |
| Determinism | generating twice gives identical output |

Every row cites its source:

| Source | Rows |
|---|---:|
| The ledger | 268 |
| Doctrine alone | 91 |
| The carried surface | 64 |
| The carried realization (the address transform and its cases) | 13 |

## What changed against today's design

The derived design keeps every behavior the suites check, and adds what the owner decided:

- **Listing actors by state.** A new act, reached from inside only.
- **A repeated registration records what it submitted**, and announces "actor registered again".
  It still counts as a registration on the trail, so the suite's count of two registrations holds.
- **Two wallets never share an address.** The address is pre-checked, then claimed, in a new
  registry. Today two people supplying one key both get a wallet at one address.
- **Four wallet classifications, not eight.** The seeds name default, private, business and
  savings. Today's vocabulary also holds investment, mint, burn and pool, which no seed names.

Fifteen components and requests were renamed by the naming doctrine and replaced. No store,
request shape, trail record or entrance changed, because they are carried.

## Unrealized

- **An empty list.** The owner decided that listing a state no actor is in answers empty. The
  platform's filter refuses an empty result, so the listing refuses. The book domain's empty
  search has the same cause. One platform transform fixes both.
- **Defaults on a direct request.** Preferred currency and language default to BACHI and English.
  The entrance supplies them, as today. No platform transform supplies a default, so a direct
  request that leaves one out records none.

## What the generator gained

- **Parts.** A ledger may have `parts`. Each gets its own stores, trail, bindings and structure. A
  ledger without parts is one part. The book ledger reads that way, and its output is unchanged.
- **The carried surface.** Store names and paths, request shapes, trail record keys and entrances
  are taken from the existing composition. A store is matched by its own name, a registry by the
  words of what it holds, and a trail by being the part's one append-only store.
- **A participant actor.** `authorization: none` drops the authorization step and credentials.
- **Four patterns.** Registration with a repeat, a decision, a listing, and creation for a holder
  another part keeps.
- **Reach.** An act that runs another part's component declares that it consults that part's
  bindings. A write into another part's records is reported as a conflict.
- **Offering and vocabulary.** Public acts carry their entrances. Allowed values render as
  vocabulary, in the shape the composition already declares.

## Where the plan changed

- **Step 7 was not needed.** The plan put a clock time on every trail moment, which would have
  changed the book domain's output. The trail store already stamps every entry's envelope with
  its time. A clock step is needed only where the trail record itself holds a time key, as
  identity's does. `own_values` covers it, and the book's output did not change.
- **One check was refit.** A listing's answer also carries the records its act read before
  filtering them. The first version of the check read the whole answer as text, so it saw every
  actor. It now asks that the answer hold one list naming exactly the expected actors. Today's
  design still fails it, because it has no listing.
- **The mandate gains new requests.** Construction reads a request's workflow from P8. The splice
  now adds a P8 entry for each request the derived design names that the mandate lacks.

## What this shows

- The ledger format and the doctrine held for a second domain once the catalog gained nine
  question types.
- The carried-surface rule did the work the suites required. Without it, renamed stores and
  reshaped requests would have failed most criteria while the design stayed correct.
- The generator is still a prototype. Its patterns are fitted to two domains, and it reads facts
  from P7 files rather than through `inspector.api`.
