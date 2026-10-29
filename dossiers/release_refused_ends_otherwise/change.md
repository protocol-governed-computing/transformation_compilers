# A refused release ends where the owner says

## The change

A change that releases an identity asks the identity's registry to release it. The registry may
refuse. Until this change, the ledger had no way to say where the operation then ends. Every refusal
ended it as rejected.

ai_governance's owner decided otherwise, in its cr_02. A reclaim the registry refuses ends as still
active: the license stays assigned, and no revocation is announced. When cr_04 derived the reclaim,
the decision's behavior held, but its ending did not. The reclaim ended at `EXIT_REJECTED`.

This change adds one answer, `release_refused`, to the ledger:

- **Schema (revision 7).** `release_refused: otherwise` is admitted on a change that `releases` an
  identity and names an `otherwise` ending. Any other value, or the answer without both of those, is
  refused.
- **Catalog (revision 6).** The question `release_refused`: per change that releases an identity,
  where the operation ends when the registry refuses the release.
- **Composer.** The release step's `VIOLATION`, the registry's refusal, routes to the `otherwise`
  ending. A `BACKEND_ERROR`, a store that cannot be written, still ends the act refused, as the
  doctrine's `failed_record_ends` requires. The release comes before any write, so nothing has
  changed when the operation ends there.
- **Self-test.** Two new cases: the answer without `releases`, and a value other than `otherwise`.

Without the answer, every derivation is as it was.

## Re-derived

No test ledger states the answer when this route is sealed, so each design of record re-derives
unchanged. ai_governance's cr_05 states it and delivers it.
