# Change Seed — blockchain / chain

## Machine

```yaml
document:
  phase: p0
  domain: blockchain
  subdomain: chain
  cr: blockchain_chain_v0
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  subdomain_purpose: |2

    The Chain subdomain maintains the official blockchain ledger. It records every block that has been
    accepted by the network and preserves the complete history of the blockchain from the beginning.
    Other subdomains decide which blocks should be accepted, but the Chain subdomain is responsible for
    maintaining the authoritative record once that decision has been made. This authoritative ledger is
    the foundation that the rest of the blockchain system relies on.
  cr_type:
  - subdomain: chain
    classification: INVENTED_SUBDOMAIN
    rationale: The canonical ledger is a distinct concern from block proposal and needs its own governance boundary; it is not an extension of an existing subdomain.
  business_vocabulary:
  - term: Chain
    definition: Implemented by CT_COMMIT_BLOCK_V0. The authoritative, ordered, append-only ledger of committed blocks.
  - term: Block
    definition: A unit of the ledger produced by a proposer and recorded on the chain; carries the transactions of its round.
  - term: Proposed Block
    definition: A block produced by a proposer in the consensus loop, not yet committed and not yet authoritative.
  - term: Commit
    definition: 'To make a proposed block part of the canonical chain: its content is hashed as its signature, it is linked to its predecessor, and it is recorded as canonical. Commit is irreversible.'
  - term: Genesis Block
    definition: The chain's first block. It has the same form as any block and contains the first system transaction — a mint crediting the mint wallet — performed by the Genesis Actor.
  - term: Bootstrap
    definition: The one-time genesis sequence that establishes the initial chain and supply, before the consensus loop runs.
  - term: Genesis Actor
    definition: The special, permanent actor that receives the initial minted supply at bootstrap and owns the mint wallet thereafter.
  - term: Proposer
    definition: The validator selected to produce a block in a given round.
  - term: BachiCoin
    definition: The system's unit of value; the supply is a closed monetary system.
  requested_outcomes:
  - outcome: Establish a closed, canonical chain that commits proposer-produced blocks to an authoritative, append-only record.
  - outcome: Bootstrap the chain from a genesis block that mints the initial supply to a Genesis Actor before the consensus loop runs.
  - outcome: For this increment, commit all proposed blocks directly to the chain, with attestation and finalization deferred to future iterations.
  known_facts:
  - fact: A canonical chain is required as the authoritative record of committed blocks.
    certainty: PROBABLY
  - fact: A genesis bootstrap is required, and must occur before consensus execution begins.
    certainty: HIGH
  - fact: The genesis block shall mint an initial supply of 1,000,000 BachiCoin.
    certainty: HIGH
  - fact: The initial supply shall be assigned to a Genesis Actor, which is permanent and owns the mint wallet.
    certainty: HIGH
  - fact: Minting occurs only during genesis bootstrap; no minting and no burning occur in this release.
    certainty: HIGH
  - fact: For this development increment, all proposer-produced blocks are committed to the chain.
    certainty: HIGH
  - fact: Attestation and finalization are intentionally deferred to a future iteration.
    certainty: HIGH
  - fact: Consensus proposes; the chain records and is the authoritative source of committed history.
    certainty: HIGH
  - fact: In this release, the chain commits every proposed block without additional validation.
    certainty: HIGH
  - fact: On commit, a block and its contained transactions become authoritative and immutable.
    certainty: HIGH
  - fact: Wallet balances are derived from committed transactions and reconciled on the chain after commit; the chain does not maintain independent balance state.
    certainty: HIGH
  system_beliefs:
  - belief: The current implementation does not yet provide a chain that commits proposed blocks.
    why_it_matters: This CR exists to fill that gap; if a commit capability already exists, the CR scope changes.
    verification_goal: Confirm no existing capability commits proposed blocks to a ledger.
  - belief: A consensus loop already exists that proposes blocks and drives slot processing.
    why_it_matters: The chain commits exactly the blocks this loop proposes — its upstream producer.
    verification_goal: Identify the governing workflows, their producers, the records emitted, and the owning subdomain.
  - belief: There is a block-proposal capability.
    why_it_matters: Defines the input the chain commit consumes.
    verification_goal: ''
  - belief: A validator registry already exists.
    why_it_matters: Validators feed proposer selection upstream of the chain.
    verification_goal: Identify where validators are registered and how proposer selection reads it.
  - belief: A wallet capability already exists.
    why_it_matters: Genesis mints the initial supply to the mint wallet held by the Genesis Actor.
    verification_goal: Identify the wallet capability and how a balance or mint is recorded.
  - belief: A transaction capability already exists.
    why_it_matters: Part of the pipeline from actor to wallet to transaction to mempool.
    verification_goal: Identify the transaction capability and its place in that pipeline.
  - belief: A mempool already exists.
    why_it_matters: Transactions queue there before block formation.
    verification_goal: Identify the mempool store and how transactions queue before a block is formed.
  - belief: An orchestration subdomain already exists.
    why_it_matters: Drives slot processing and the consensus loop.
    verification_goal: Identify the orchestration driver and what it invokes.
  - belief: 'Adjacent subdomains exist: identity, wallet, transaction, mempool, consensus, orchestration.'
    why_it_matters: Establishes the neighbourhood the new chain subdomain plugs into.
    verification_goal: Confirm each named subdomain exists and note its owning boundary.
  assumptions:
  - assumption: All proposed blocks are good and are committed as finalized, with no rejection path this increment.
    basis: Incremental-development decision; attestation and finalization deferred.
  constraints:
  - constraint: Closed monetary system — no supply enters or leaves except by the system's own rules.
    source: Business policy
  - constraint: The chain is immutable — a committed block cannot be altered or removed.
    source: Business policy
  - constraint: Genesis supply is fixed at 1,000,000 BachiCoin, minted to the Genesis Actor at bootstrap.
    source: Business policy
  business_invariants:
  - invariant: Exactly one genesis block exists per chain.
  - invariant: Genesis executes exactly once at bootstrap and is never replayed.
  - invariant: Total supply is conserved and equals 1,000,000 BachiCoin.
  - invariant: A committed block is immutable — it never changes or disappears.
  - invariant: Every committed block has exactly one predecessor, except the genesis block.
  - invariant: A block cannot be committed twice.
  - invariant: The canonical chain is the authoritative source of committed history; a proposed block is not authoritative until committed.
  lifecycle_states:
  - object: Chain
    state: Uninitialized
    meaning: No genesis block yet; the chain is not established.
  - object: Chain
    state: Active
    meaning: Genesis created; the chain accepts and commits blocks.
  - object: Block
    state: Proposed
    meaning: Produced by a proposer; not yet committed and not authoritative.
  - object: Block
    state: Committed
    meaning: Recorded in the canonical chain; immutable and authoritative.
  - object: Genesis Block
    state: Created Once
    meaning: The single first block, established at bootstrap; permanent.
  business_events:
  - event: Genesis Created
    when_it_occurs: Once, at bootstrap, before the consensus loop runs.
    significance: Establishes the chain and the initial monetary state.
  - event: Block Proposed
    when_it_occurs: When a proposer produces a block in a round.
    significance: A candidate block exists; not yet authoritative.
  - event: Block Committed
    when_it_occurs: When a proposed block is committed to the canonical chain.
    significance: The block and its transactions become authoritative and immutable.
  - event: Balance Reconciled
    when_it_occurs: After a block is committed, when wallet balances are recomputed from the committed transactions.
    significance: Wallet balances become consistent with the canonical committed history.
  authority_boundaries:
  - business_object: Proposed Block
    authoritative_owner: Consensus
  - business_object: Committed Block
    authoritative_owner: Chain
  - business_object: Committed History
    authoritative_owner: Chain
  - business_object: Monetary Supply
    authoritative_owner: Genesis at bootstrap, then Chain
  - business_object: Wallet Balance
    authoritative_owner: Chain, derived by reconciliation from committed transactions rather than owned as independent state
  out_of_scope:
  - item: The attestation step of the proof-of-stake progression.
    reason: Deferred to a future iteration; all proposed blocks treated as good this increment.
  - item: The finalization step of the proof-of-stake progression.
    reason: Deferred to a future iteration; proposed blocks committed directly.
  - item: Fork resolution.
    reason: Not part of this release; the chain commits every proposed block.
  - item: Chain reorganization.
    reason: Not part of this release; committed history is immutable.
  - item: Slashing.
    reason: Validator penalties are out of scope this release.
  - item: Rewards.
    reason: Validator and proposer rewards are out of scope this release.
  governance_scope:
  - scope_item: chain
    relationship: INVENTED
  - scope_item: consensus_pos
    relationship: ADJACENT
  - scope_item: orchestration
    relationship: ADJACENT
  - scope_item: wallet
    relationship: ADJACENT
  - scope_item: transaction
    relationship: ADJACENT
  - scope_item: mempool
    relationship: ADJACENT
  - scope_item: identity
    relationship: ADJACENT
  clarification_requests: []
  acceptance_criteria:
  - criterion: The chain begins with a genesis block that records the assignment of the initial 1,000,000 BachiCoin supply to the Genesis Actor.
  - criterion: Blocks accepted by the chain appear in the authoritative ledger in proposal order.
  - criterion: A block recorded in the ledger never changes or disappears.
  - criterion: The total recorded supply on the ledger is 1,000,000 BachiCoin, held initially by the Genesis Actor.
  - criterion: Once committed, a block and its contained transactions are treated as authoritative.
  identity_and_sameness: null
  lifecycle_transitions: null
  operation_refusals: null
  authority_deferrals: null
```

The reference subject, an elicitation for `blockchain/chain` organized into the seed's registers. It is here because it was authored independently of this template: a
template that only fits the document it was derived from proves nothing.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals
