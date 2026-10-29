# A delivered replacement stays spent when its successor is superseded

## The change

A `replaces` answer stays in a ledger once delivered. Re-deriving the ledger must not apply it
again. The route recognized a delivered replacement by the design of record's lineage: the operation's
workflow `supersedes` the first workflow the answer names.

That held for one change only. A design of record names one predecessor per artifact. When ai_governance's
cr_05 superseded `WF_RECLAIM_LICENSE_V0` with `_V1`, `_V1` named `_V0` as its predecessor, and the
record that `_V0` had replaced `WF_AUTO_RECLAIM_V0` left the design of record. Re-deriving the
ledger then refused `replaces: [auto reclaim]` as naming a workflow the composition does not hold.

This change reads the replacements already made from the retirement ledger as well as the design's
lineage, and follows each to its last version:

- `compose.delivered()` builds each predecessor's chain of successors from
  `retired_identities.yaml` (`superseded_by`) and the design's `supersedes`. A `replaces` answer is
  spent when the operation's workflow is on the chain of the first workflow it names.
- `tc phase derive design` takes `--retired <ledger>`. `derive_build.sh`, `derive_deliver.sh` and
  `tc phase derive seal` pass the workspace's retirement ledger.
- A `replaces` answer that names a workflow neither held nor replaced is still refused.

## Re-derived

Each test ledger re-derives its domain's design of record unchanged. ai_governance's ledger now
holds cr_05's answer.
