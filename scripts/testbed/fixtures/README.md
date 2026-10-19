# Fixtures

Phase documents shaped like dossiers, kept as test fixtures. They are maintained against the current
rule set, so a complete chain is admissible today. That is what proves the rule sets, the projection
and the runtime wiring still work.

| Folder | What it is |
|---|---|
| `catalog/cr_01_catalog` … `cr_05_catalog` | A P0–P8 chain for the book catalog, and four changes after it |
| `transformation/founding_design_bootstrap` | P0–P2 for the transformation module's phases |

## What consumes these

| Script | What it takes |
|---|---|
| `build_payloads.py` | every phase document, as runtime payloads |
| `build_fixtures.py` | `cr_01_catalog`, as the base its negative corpus is derived from |
| `differential.py` | `cr_01_catalog`, `cr_03_catalog` and `founding_design_bootstrap`, driving the transforms directly |
| `effectivity_test.py` | `cr_01_catalog`'s P7, judged under each rule set |
| `projection_test.py` | the P0s, asserting each P1 is what the projection emits |
| `priors.py` | every seed, so a later phase can be handed the documents before it |

## Maintaining them

When a rule or a template changes and these go inadmissible, fix them. That is what they are for.
A fixture is not a design of record: the composition's designs are in each root's `design/`.
