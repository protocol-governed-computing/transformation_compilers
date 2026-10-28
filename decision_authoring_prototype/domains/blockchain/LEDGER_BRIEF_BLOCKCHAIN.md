# Brief — Blockchain Identity and Wallets

What the blockchain project requires of identity and wallets. Identity says who an actor is and
whether the business trusts them. Wallet says where a person the business has accepted holds
value.

## Registering

- A person registers themselves with a name and a contact address, and is admitted unverified.
- A registration may also state a preferred currency and a preferred language. A person who states
  none prefers BACHI and English.
- A registration with no name, or no contact address, is refused. No actor exists afterwards.
- A registration is held unverified, whatever state the request gives it.
- An actor is identified by their contact address. The same address registered twice is one actor,
  with two registrations shown against them.
- A repeated registration does not fail and does not reset a decision. The details the actor was
  first admitted with prevail.
- A repeated registration records the details it submitted, and the actor is unchanged by them.
- A repeated registration is announced as a registration again, distinct from a first
  registration.

## Deciding

- An authority records a decision about a registered person: an acceptance or a rejection, and
  nothing else.
- A decision about a person who never registered is refused.
- A person is decided about once. A decision about a person already accepted or rejected is
  refused, and no record changes.
- A decision names the authority that made it.
- A person never decides about themselves. Such a decision is refused.
- A rejection states its grounds. A rejection stating no grounds is refused. An acceptance may
  state grounds.
- A decision changes the person's state, the authority and the grounds, and nothing else. An
  accepted or rejected person keeps the name and preferences they registered with.
- An accepted actor is shown as accepted, with the deciding authority and the time. A rejected
  actor is shown as rejected, with the authority, the grounds and the time.
- A rejected actor cannot be read as accepted by any means.

## Finding actors

- The business can list the actors in a given state. Listing the rejected shows exactly the
  rejected actors.

## Wallets

- A person the business has accepted asks for a wallet, supplying the public key it is made from.
- A wallet for a person who never registered is refused. A wallet for a person who is unverified
  or rejected is refused, and none is recorded for them.
- One person holds one wallet. A person who already holds one is refused a second.
- A new wallet is held by the accepted person. It holds a balance of zero, in BACHI, classified
  DEFAULT, and is active, whatever the request states.
- The business names four classifications: default, private, business and savings. Only default
  wallets are created.
- A wallet's identity is formed from its holder and carries the business's prefix, `wal`, whatever
  the request states.
- A wallet's address is formed from the supplied public key the way an Ethereum address is: the
  last 20 bytes of the key's Keccak-256 hash. The same key always gives the same address, with or
  without its `0x` prefix and `04` tag.
- Wallet reads identity's records to learn whether a person is accepted. It never writes them.
  Every wallet act leaves identity's records exactly as they were, including a refused one.

## The public entrance

- Registering, accepting and rejecting are offered from outside, each under a public name. A
  request naming any other act is turned away.
- The entrance turns a request away only when it cannot read it: a detail is missing or not in the
  form asked for. It tells the caller which detail.
- A caller is told one of three things: the act was done, it was turned away, or something went
  wrong inside the business. A request turned away and a request the business decided against are
  told apart.
- No caller needs an account or a login.
- Everything the business decides is decided by the act, not the entrance.

## Rules and values the business holds

- A request that states rules of its own is judged by the business's rules. It is not refused for
  stating them.
- A request cannot widen who may be decided about, which decisions are allowed, the
  self-decision rule or the grounds rule.
- Every act records its own moment on its own trail, whatever moment or trail the request names.
  A registration claims the contact address wherever the request says it sits.

## Records

- Every registration, decision and wallet creation is recorded as a moment with the time it
  happened. Two moments at different times carry different times.
- No act changes or removes a moment already recorded.
- Every wallet has exactly one creation moment.
- When a record an act needs cannot be read or written, the act ends refused. Nothing after that
  point happens, and nothing is recorded by it.
