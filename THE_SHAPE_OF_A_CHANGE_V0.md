# The shape of a change

Re-deriving the wallet change from dev/5, knowing what the multi-subdomain path cost.

---

## 1. What actually broke, and it was not one thing

`cr_04_wallet` triggered three failures that look like one because they arrived together. They are
independent, they have different fixes, and conflating them is what produced three lifecycle dossiers
where two would have done.

| # | failure | trigger | what it cost |
|---|---|---|---|
| 1 | every rule reasoning about *the* subdomain was insufficient for two | the change spanned `wallet` and `identity` | 3 new rules, 2 template columns, a new register, P6 reaching back to P0, and **every dossier ever written went red** |
| 2 | a design can state a new artifact and cannot state an amended one | the change EXTENDs a build config | halted at 99.4%, `register_coverage` opened |
| 3 | a rule applies to every document that ever existed | (1) added rules | `rule_effectivity` opened, closed CRs unamendable-but-red |

**Failure 2 is not caused by failure 1.** This is the load-bearing observation and it decides whether
your ground rule is sufficient. Check it against the actual numbers, run just now:

```
Construction Completeness  99.4%  (468/471)
AMENDMENT NARROWS
    STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0    51 fact(s) lost
        .artifact_discovery.artifact_types[0..10]  …and 47 more
```

Every one of the 51 is on the **domain** build config. A wallet-only change that touches no other
subdomain still adds a subdomain to the domain, still EXTENDs that config, and still loses 51 facts.
So the single-subdomain rule does not unblock cr_04. It is worth doing anyway — see below — but not
for that reason.

---

## 2. Your rule, sharpened

> A change touches exactly one subdomain. Never do a cross-subdomain change.

It is worth having, in a form the pipeline can already enforce, and as a *write* rule rather than a
*touch* rule. **Not yet, though** — see §4A for why the sequencing matters more than the rule.

> **A change authors and amends only within its own subdomain. It may read across a boundary and
> never write across one.**

The write/read asymmetry matters. A wallet that cannot *see* identity is not a subdomain, it is an
island; the composition is a graph and pretending otherwise buys nothing. What must never happen is
wallet reaching into identity and changing it. That is the thing that made "the subdomain" plural.

**The pipeline is most of the way there already.** P6's stated discipline is *no cross-subdomain
writes*. P5 carries `cross_subdomain_refs` and P6 carries `cross_subdomain_deps` — both exist, both
model reading. What was missing was a rule holding P7's inventory to them:

```
CROSS_SUBDOMAIN_WRITE
  every row of new_artifacts is in this document's subdomain
  every existing_inventory row outside it has Action = REUSE or REVIEW, never EXTEND or REPLACE
```

One rule. It **replaces** `TOUCHED_SUBDOMAIN_WITHOUT_PURPOSE`, `TOUCHED_SUBDOMAIN_UNOWNED` and
`TOUCHED_SUBDOMAIN_AUTHORS_NOTHING`, and it makes the `Subdomain` column on `cr_type` and
`provisional_codes` and the whole `subdomain_purposes` register unnecessary — there is one subdomain,
it is in the document header, and its purpose is §1. P6 stops needing `PRIORS = ("p5", "p0")`.

Net: **one rule instead of three, no template columns, no new register, and none of the retroactive
breakage that cost this session two rollbacks.** That is the case for your instinct, and it is a good
one. It is a simplification, not merely a restriction.

### What wallet looks like under it

Two changes, in order, each single-subdomain:

- **CR-A `identity`** — split the deciding workflow into accept and reject, add rejection grounds,
  and publish what a consumer needs. Judged wholly within `identity`. One purpose, one owner, one
  authorship claim. Nothing about wallet appears in it, which is the test that it is a real change
  and not a wallet dependency wearing a disguise.
- **CR-B `wallet`** — authors the wallet subdomain and cites identity's published surface in
  `cross_subdomain_refs`. Reads, never writes.

The cost is honest and should be stated: **CR-A is designed without its consumer in the room.** You
will get identity's interface slightly wrong and CR-C will fix it. That is the normal condition of
publishing an interface and it is cheaper than the alternative, which is what we just paid.

### What it does not fix

The build config. Which is next.

---

## 3. The reframe: the axis is not subdomains, it is author versus amend

Sort every defect of this session by whether the change was **authoring** something new or
**amending** something that existed.

Authoring is well served. The design language states a new artifact completely; construction renders
it; completeness measures it; `NEW_CODE_ALREADY_EXISTS` stops a collision. Every green number in the
suite is an authoring number.

Amending is barely served at all:

- an EXTEND is rendered **whole** and replaces its predecessor, so a design must restate every fact
  the artifact carries — and 51 of the build config's facts have no register at any shape;
- the narrowing check exists because a design that fails to restate silently deletes;
- `PROVISIONAL_CODE_NEVER_BOUND` needed a `union` clause because an extended code must appear in
  `existing_inventory` and must not appear in `new_artifacts`;
- `cr_04`'s last undetermined facts are `subdomain` on an amended workflow and `extends` on a base
  vocabulary — facts the authoring path supplies implicitly and the amending path cannot state.

Five separate patches, one cause. **The design language was built to author and retrofitted to
amend.** Your worry that the architecture will not survive the next problem is, I think, exactly
this: the next problem will also be an amendment, and it will need a sixth patch.

---

## 4. Four moves, cheapest first

### A — one subdomain per change (§2) — **held, deliberately**

One rule replacing three, and still worth having. It is nonetheless **not** the next move, and B's
result is the reason: it does not solve the build-config failure, and adopting it now would let a
complexity constraint stand in for a fix to the author-versus-amend defect underneath. A ban that
makes the defect harder to reach also makes it easier to leave in place. Revisit once amendability is
settled and A can be judged on its own merits rather than as relief.

### B — the domain build config is generated, not amended — **DONE**

Delivered. What the run showed, which was sharper than this section originally argued:

- **`build_manifest` already reproduces the artifact in the repo exactly** — 0 governed differences
  against `blockchain`, and 0 against `book_library_mgmt` independently. Declaring it generated
  re-expresses nothing; it stops pretending a design authored it.
- **The only subdomain-bearing field in the whole manifest is one prose sentence** in the summary.
  Nothing in the compiler's read path varies by subdomain, so the pre-flight rule *"adding a
  subdomain always amends the build config"* was true and irrelevant.
- **cr_04 hand-stated 14 `artifact_properties` rows for it, and one was fabricated** —
  `core.subdomain: wallet`, a field the artifact does not carry and the generator does not produce.
  The design invented a fact to satisfy a register that should never have been asked to hold it.
- **It is a class, not a one-off.** Six domain build configs in the snapshot share the shape. The two
  `structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V*` are hand-authored governance surface and stay
  authored.

Measured effect on cr_04:

```
                    before          after
completeness        99.4%           99.6%
required facts      471             447        24 derived facts stopped being the design's to state
narrowing           51 lost         none       the artifact is no longer amended
undetermined        3               2
```

And the acceptance harness went from **51/52 to 52/52**, because the manifest it had always reported
as "rendered nothing" is now compared against the generator's output. That comparison is what keeps
the claim honest: if `build_manifest` ever stops deriving what the composition holds, a design naming
it as its generator is pointing at something that does not produce the artifact.

**One design flaw surfaced by running it.** The agreement gate refused cr_04, correctly by its own
logic and wrongly in fact. The phase workflows derive from a template and a rule module, so a
disagreement is a stale copy *now* and the build must refuse. The build manifest derives from the
mandate, so before that mandate is built the artifact necessarily differs from what the design
determines — and that difference **is the change**. Refusing it would refuse every design that
touches a generated artifact, which is the opposite of the point. A generator now declares
`derived_from_design`; those are reported as PENDING at `construction check` and enforced at
`construction emit`, which refuses anything still disagreeing after the generator has run.

**Founding versus amending.** cr_01's manifest could not be declared the same way: it does not exist
in the composition cr_01 was designed against, so an `existing_inventory` EXTEND row would correctly
fail `EXISTING_INVENTORY_UNRESOLVED`. That gives the rule rather than a workaround — *a design
declares provenance for a generated artifact it amends; an artifact that does not yet exist cannot be
amended, and its first emission is part of founding the domain.* `construction emit` invokes the
generator for it rather than writing a file, so one producer owns it from the first copy.

**The residual, for the reassessment.** Exactly two undetermined facts remain, and both are
amendment expressiveness on genuinely authored artifacts: `subdomain` on the amended
`WF_REGISTER_ACTOR_V0`, and `extends` on a base vocabulary. No further derived-configuration
artifacts are implicated. That is the first branch, and it says the next problem is amendability —
not coverage, and not subdomain span.

### C — judge a document through the composition it pins

`rule_effectivity` is framed as a new capability. I think it is a plumbing bug.

Every dossier already pins a snapshot in `baseline.json`. **Every phase's rule set is already sealed
inside the workflow artifact in that snapshot** — that is what `generated_artifacts` just made
enforceable. So the pin already names the rule set. Nothing else is needed.

But `tc phase check` reads `RULE_SETS[phase_key]` — the Python declaration in the working tree —
while the runtime reads the sealed copy from the snapshot. Two paths, two answers, and the one people
run interactively is the one that ignores the pin.

Make `tc phase check` read its rule set from the pinned snapshot and retroactivity is gone, with no
new register, no new vocabulary, and no new doctrine. "A completed CR is never re-pinned forward" is
already the rule; it simply was not being applied to rules because nobody noticed the pin covered
them.

Residual: a dossier in flight legitimately re-pins, and re-pinning changes the rules mid-change. That
is correct and already how the snapshot pin behaves.

### D — artifacts are immutable, and change by supersession

This is the answer to *will it stand up to the next one*. A, B and C make amendment rarer and
cheaper. D removes it.

Every artifact header in the composition already carries `Supersedes: NONE`. The field is there and
nothing uses it. The proposal is to use it:

> A change never amends an artifact. It authors the next version, which supersedes the previous one.

`WF_REGISTER_ACTOR_V0` is not extended; `WF_REGISTER_ACTOR_V1` is authored, whole, by the authoring
path that already works. What falls away:

- the narrowing check — nothing is replaced, so nothing can be narrowed;
- `register_coverage`'s premise — a design never amends, so "can a design state an amendment" stops
  being a question;
- the `union` clause in `PROVISIONAL_CODE_NEVER_BOUND` and the `Action = EXTEND` special cases;
- the "an EXTEND is a whole redeclaration, not a delta" warning in the P7 template, which exists
  because the word invites the wrong reading and has already cost a storage declaration.

And it is what the rest of the platform already does. Snapshots are immutable. Generated artifacts are
never corrected in place. A pin is never re-pinned forward. **The canonical artifact is the one
mutable thing in a system whose entire thesis is immutability**, and that is not a coincidence with
the fact that amendment is where the design language keeps failing.

#### The cascade, which is the real objection

If `IN_ACTOR_REGISTRATION_V0` names `WF_REGISTER_ACTOR_V0`, superseding the workflow forces a new
intent, and so on up the spine. A leaf change bumps the branch. That objection kills naive
supersession.

The resolution is to move the version from the reference to the composition:

- an artifact's **logical identity** is `domain::FAMILY_NAME`; its **version** is `_V<n>`;
- a reference names the logical identity;
- **the assembler binds each reference to the highest non-superseded version and seals the resolved
  version into the snapshot.**

The cascade disappears — only the changed artifact gets a new version — and the snapshot still records
exactly which versions composed, because it is sealed resolved. That is the snapshot's existing job.

This is a genuine governance act, not a refactor: `NAMESPACE_MODEL.md` says identity is exact, and
this splits it into logical identity plus composition-time version. It belongs in `standards` as a
ruling, with the compiler and assembler following. **Do not start it as a side effect of a domain
change.** It is the one item on this list that deserves its own change and its own gate.

Costs to name rather than discover: version proliferation with no garbage collection story; a
superseded STRUCTURE whose store paths moved leaves data behind the new version cannot read; and
`NEW_CODE_ALREADY_EXISTS` becomes a version check rather than an identity check, which is the same
rule at finer grain but is a rule edit.

---

## 5. What I would actually do

1. ~~**B — build config generated.**~~ **Done.** cr_04 at 99.6%, narrowing gone, acceptance 52/52,
   and GAP-3 exercised against a live dossier for the first time.
2. **Amendability**, which the residual now points at directly. Two facts, both on authored artifacts
   a design extends. Small enough to fix as registers and large enough to be worth asking first
   whether D removes the category.
3. **C — judge through the pinned snapshot.** Before the next template change, so the next one does
   not turn every closed dossier red again.
4. **D — supersession.** Open as a `standards` ruling. If the answer is yes, `register_coverage` is
   closed without being built.

**A is deliberately not on this list.** It is a useful complexity constraint and it did not solve the
build-config failure — this section originally had it second, and B's result is the argument against
that. A blanket cross-subdomain ban adopted now would be a workaround for an author-versus-amend
defect, and would take the pressure off fixing the defect. Revisit it once amendability is settled and
it can be judged on its own merits.

## 6. What I would not do

- **Do not forbid reading across a boundary.** A subdomain that cannot cite another is not isolated,
  it is isolated *and* duplicating. The rule is about writes.
- **Do not solve the build config by adding 51 registers.** That is `register_coverage` as currently
  scoped, and it would enlarge the design language to describe facts no designer decides.
- **Do not merge the three lifecycle dossiers** even though this note treats them as one cause. Their
  P0s each name the other two as out of scope, and that separation is what stopped this session's
  work from becoming a single unreviewable change. One cause, three deliveries.
- **Do not retrofit A or D onto closed dossiers.** They are evidence. C is what makes that
  sustainable, which is why C comes before the next template change and not after it.

---

## 7. Ruling — the governance surface is authored, not constructed

**The pipeline's authority over a governance-surface change ends at P6.** A constitution, an
invariant and a schema are written by a person under a governed dossier; they are not scheduled by a
mandate and not rendered by construction. A dossier whose deliverables are governance artifacts is
therefore **complete at P6**, not halted before P7.

### Why this is a boundary and not a gap

Three dossiers reached P6 and stopped, and the third made the reason legible. A design authors an
artifact by giving it a family, and the families are `AC IN WF CC CT EV RB VOCAB STRUCTURE TI TE`,
with `CS` present as substrate a change reuses and never writes. There is no family for a
constitution or an invariant, and the renderer has a builder for each of the eleven and for nothing
else.

That absence was read twice as something missing. It is not. **A constitution's content is
argument** — it says what must hold and why the alternative was rejected — and a register that
determined it would have to carry the argument, which makes the register the constitution and the
document its rendering. The design language exists to make an artifact's *content* derivable from
declared facts. Where the content is the reasoning, there is nothing to derive it from.

The same is true one step down. An invariant states what may never happen, and its worth is in the
statement, not in a field a generator could fill.

### What the pipeline still governs

Everything except the rendering, which is most of it:

- **P0–P6 are unchanged and are not optional.** The problem, the beliefs and their verification, the
  gaps, the capabilities, the invariants, the ownership and the boundary rules all apply. A
  governance change is judged exactly as any other change is judged, up to the point where an
  artifact would be rendered.
- **The dossier is the record of authority.** A clause that appears in a constitution with no dossier
  behind it is an ungoverned change, and that is now a statement with a place to point.
- **The domain half is an ordinary CR.** Where a governance change enables something in a business
  domain, that half has families, is designed at P7 and is constructed. The platform half being
  authored does not make the domain half authored.

### What it costs, stated

Delivery of a governance artifact is not mechanically reproducible from its dossier. Construction
acceptance cannot re-render it and compare, so nothing catches a document that drifts from the design
that argued for it. That is the price of the ruling and it is accepted: the alternative was a
generator inventing the argument, and an argument nobody made is worse than one nobody re-derived.

### What this ruling leaves open, and should not be read as settling

**Ruled: Gate 1 moves to P6 for a governance change.** The gate that reviews a dossier as a body
belongs at the end of the dossier, wherever that end is, and for a governance change the end is P6.
Stages 0 through 6 are presented as a body, and approval authorizes the authoring of the clauses and
rules the dossier argues for.

**Gate 2 does not follow it, because it has no subject.** Gate 2 locks a mandate before artifact
authoring begins; a change that schedules no artifacts drafts no mandate and has nothing to lock.
What it protects for a domain change — scope frozen before anyone writes an artifact — is carried
here by Gate 1 being the last word rather than the second-to-last. The P6 template carries the gate
and says so.

**"Complete at P6" therefore means the phases are exhausted and the gate is presented.** Approval
remains the reviewer's act: a dossier that has reached P6 is approvable, not approved.

**Identity assignment is ungoverned for these artifacts.** P7 assigns a binding FQDN and
collision-checks it against the composition; a new invariant authored under a P6-terminal dossier is
named by whoever writes it. This is a deliberate arrangement, not an oversight.

**Nothing re-renders and compares.** Construction acceptance can render a domain artifact from its
design and diff it against what the registry holds; a governance artifact has no such check, so drift
between the clause and the dossier that argued for it is caught by reading, or not at all.

### The rule that holds it

`AMENDED_ARTIFACT_NOT_AUTHORABLE` — a design may not name, as an artifact it amends, one whose family
it cannot author. `REUSE` and `REVIEW` are unaffected: reading a constitution and citing it are what
every design does. What is refused is `EXTEND` or `REPLACE` on a family the renderer has no builder
for, which would schedule a governing document to be rewritten from registers that never held its
content.

---

## 8. Ruling — a change that never entered the composition is deleted, not superseded

Supersession is a claim about two things that both existed. An artifact stood down by a successor is
marked rather than removed, because a composition that silently loses a file tells a later reader
nothing about why. That reasoning is sound and it does not reach a change request that never became
part of anything.

**The test is delivery, not lifecycle position.** A change request that never entered the delivered
composition — never pinned, never released, owning nothing that survives — has no successor
relationship to record. Marking it superseded asserts a lineage that does not exist, and leaves a
complete dossier on disk whose gates read CLOSED and whose design claims to be the whole declaration
of an artifact it no longer describes. That is not a record; it is a hazard a reader can act on.

**So it is deleted, and it leaves no trace.** Being built once, or executed once, does not qualify
it: what decides is whether any of it survives in the composition that matters. Where a later change
has re-emitted the same artifacts, nothing of the earlier one does.

**With one condition, which is the whole of the care this needs.**

> A change request that never entered the delivered composition leaves no trace on deletion —
> **provided nothing cites it.** Where something does, re-ground the citation first, then delete.

A dossier can be evidence for another dossier while delivering nothing itself. Evidence-value and
delivery-value are independent, and it is the first that a deletion can quietly break: a verified
belief grounded on a path that is no longer there is worse than the dossier it pointed at. Re-ground
it on something that survives and says the same thing, then delete freely.

**Why this is the right boundary.** The alternative — keeping every dossier that was ever authored —
accumulates records faster than the changes they describe, and each one looks live until a reader
opens it. In-flight work is allowed to be consolidated and re-authored precisely so that one artifact
has one design of record. A change absorbed into another has no separate story to tell, and keeping
it invites a reader to believe it does.

**What this does not license.** A delivered change is never deleted, however wrong it turned out to
be. Its artifacts are in a composition somebody ran, its dossier is the evidence of an approval that
happened, and correcting it is a new change request. The line is delivery, and it is not negotiable
in either direction.
