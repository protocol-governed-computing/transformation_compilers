# The derive route, sealed whole

## The change

The derive route decides a design from three sealed documents and from its building blocks: the
doctrine, the ledger schema, the catalog, and the modules of `transformation/design/derive/`. Before
this change, each document recorded its own revisions. The modules recorded nothing. A change to a
building block changed every derived design, and nothing refused it.

This change seals the route whole:

- `seal.route_now()` takes the digest of every file of the route: each module of the package and
  each sealed document.
- `route_seals.yaml` in the package records each seal. A seal names the route change's dossier, the
  digest of every file as the change left it, and what re-deriving each ledger gave.
- A derivation is refused unless a seal records the route as it stands. `judged_by` names that seal
  beside the three documents.
- `tc phase derive seal <dossier> --snapshot … --change …` records a seal. It refuses a dossier
  outside `dossiers/`, a dossier with no `change.md`, and a route a seal already records. It
  re-derives every ledger in `testbed/ledgers/` against its domain's design of record and records the
  identity outcome of each.
- `tc phase derive meta` refuses an unsealed route, and a seal whose dossier is missing from the
  repository.

## What this seal covers

This is the route's first seal. It covers the route as commit `23f0c0d` left it, with this change
added. That route was built across readiness sections 1 to 5, before a route change had to run as
a dossier. Those earlier changes are recorded in git and in `doc/ASSIMILATION_READINESS.md`, not
in a dossier of their own.

## Re-derived

Each ledger re-derives its domain's design of record unchanged: book 57 kept, blockchain 44 and
ai_governance 59. `route_seals.yaml` records the outcome of each.
