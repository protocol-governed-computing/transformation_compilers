# The shape of a change

What a change request may write, how it changes what already exists, and where the lifecycle's
authority over a change ends.

---

## 1. A change writes within its own subdomain

> **A change authors and amends only within its own subdomain. It may read across a boundary, and it
> never writes across one.**

The asymmetry is the point. A subdomain that cannot read another is not isolated. It is isolated
*and* duplicating, because the composition is a graph. What must never happen is one subdomain
reaching into another and changing it.

The pipeline holds the rule in three places:

- P5 carries `cross_subdomain_refs` and P6 carries `cross_subdomain_deps`. Both model reading.
- P5 and P6 refuse a touched subdomain with no purpose, no owner, or nothing authored
  (`TOUCHED_SUBDOMAIN_*`).
- P7 refuses a write across the boundary:

```
CROSS_SUBDOMAIN_WRITE
  every row of new_artifacts is in this document's subdomain
  every existing_inventory row outside it has Action = REUSE or REVIEW, never EXTEND or REPLACE
```

A change that needs another subdomain to publish something is two changes. The first is judged
wholly within the publishing subdomain. The second cites what was published and writes only its
own. The first is designed without its consumer in the room, so a later change may correct the
interface. That is the normal condition of publishing an interface.

## 2. Authoring and amending are different acts

Authoring states a new artifact completely. Construction renders it, completeness measures it, and
`NEW_CODE_ALREADY_EXISTS` stops a collision.

Amending is harder to state. An `EXTEND` is rendered **whole** and replaces its predecessor, so a
design must restate every fact the artifact carries. A design that fails to restate a fact deletes it
silently, which is why construction refuses an amendment that narrows what it replaces. An amended
artifact that changes meaning takes a new identity and names its predecessor in `supersedes`.

## 3. A derived artifact is generated, not amended

An artifact derived from the composition — a domain's build manifest is the example — is declared
generated. The design names its generator and states none of its facts. A register is never asked to
hold a fact no designer decides.

- **The generator reproduces the artifact exactly.** Construction acceptance compares what the
  registry holds with what the generator produces. If the generator ever stops deriving what the
  composition holds, a design naming it points at something that does not produce the artifact.
- **The difference is the change.** Before a mandate is built, a generated artifact necessarily
  differs from what the design determines. A generator therefore declares `derived_from_design`:
  `construction check` reports such an artifact as PENDING, and `construction emit` refuses anything
  still disagreeing after the generator has run.
- **Founding is not amending.** A design declares provenance for a generated artifact it amends. An
  artifact that does not yet exist cannot be amended, so its first emission is part of founding the
  domain. `construction emit` invokes the generator for it rather than writing a file, so one
  producer owns it from the first copy.

The platform's own build configurations are hand-authored governance surface, and they stay authored.

## 4. A document is judged by the rules its pin seals

Each phase's rule set is sealed inside the phase workflow in the snapshot a dossier pins. So the pin
names the rule set. `tc phase check` judges a document by the rule set sealed in its pinned
snapshot, the same copy the runtime reads. A new rule therefore reaches no completed dossier, and a
completed dossier is never re-pinned forward. A dossier in flight may re-pin, and re-pinning
changes its rules mid-change, as it changes everything else the pin names.

---

## 5. Ruling — the governance surface is authored, not constructed

**The pipeline's authority over a governance-surface change ends at P6.** A person writes a
constitution, an invariant or a schema under a governed dossier. A mandate does not schedule it, and
construction does not render it. A dossier whose deliverables are governance artifacts is therefore
**complete at P6**, not halted before P7.

### Why this is a boundary and not a gap

A design authors an artifact by giving it a family. The families are
`AC IN WF CC CT EV RB VOCAB STRUCTURE TI TE`, with `CS` present as substrate a change reuses and
never writes. There is no family for a constitution or an invariant, and the renderer has a builder
for each of the eleven and for nothing else.

That absence is not something missing. **A constitution's content is argument.** It says what must
hold and why the alternative was rejected. A register that determined it would have to carry the
argument, which makes the register the constitution and the document its rendering. The design
language exists to make an artifact's *content* derivable from declared facts. Where the content is
the reasoning, there is nothing to derive it from.

The same is true one step down. An invariant states what may never happen, and its worth is in the
statement, not in a field a generator could fill.

### What the pipeline still governs

Everything except the rendering, which is most of it:

- **P0–P6 are not optional.** The problem, the beliefs and their verification, the gaps, the
  capabilities, the invariants, the ownership and the boundary rules all apply. A governance change
  is judged exactly as any other change is judged, up to the point where an artifact would be
  rendered.
- **The dossier is the record of authority.** A clause that appears in a constitution with no
  dossier behind it is an ungoverned change.
- **The domain half is an ordinary change request.** Where a governance change enables something in
  a business domain, that half has families, is designed at P7 and is constructed. The platform half
  being authored does not make the domain half authored.

### What it costs

Delivery of a governance artifact is not mechanically reproducible from its dossier. Construction
acceptance cannot re-render it and compare, so nothing catches a document that drifts from the design
that argued for it. That is the price of the ruling, and it is accepted. The alternative is a
generator inventing the argument, and an argument nobody made is worse than one nobody re-derived.

### Gates and identity

- **Gate 1 is at P6 for a governance change.** The gate that reviews a dossier as a body belongs at
  the end of the dossier, and for a governance change the end is P6. Phases 0 through 6 are presented
  as a body, and approval authorizes the authoring of the clauses and rules the dossier argues for.
- **Gate 2 has no subject.** Gate 2 locks a mandate before artifact authoring begins. A change that
  schedules no artifacts drafts no mandate and has nothing to lock. Gate 1 being the last word
  carries what Gate 2 protects for a domain change: scope frozen before anyone writes an artifact.
  The P6 template carries the gate and says so.
- **"Complete at P6" means the phases are exhausted and the gate is presented.** Approval remains the
  reviewer's act. A dossier that has reached P6 is approvable, not approved.
- **Identity assignment is ungoverned for these artifacts.** P7 assigns a binding FQDN and
  collision-checks it against the composition. Whoever writes a new invariant under a P6-terminal
  dossier names it. This is deliberate.
- **Nothing re-renders and compares.** Drift between a governance clause and the dossier that argued
  for it is caught by reading, or not at all.

### The rule that holds it

`AMENDED_ARTIFACT_NOT_AUTHORABLE` — a design may not name, as an artifact it amends, one whose family
it cannot author. `REUSE` and `REVIEW` are unaffected: reading a constitution and citing it are what
every design does. What is refused is `EXTEND` or `REPLACE` on a family the renderer has no builder
for, which would schedule a governing document to be rewritten from registers that never held its
content.

---

## 6. Ruling — a change that never entered the composition is deleted, not superseded

Supersession is a claim about two things that both existed. A change request that never became part
of anything has no successor relationship to record.

**The test is delivery, not lifecycle position.** A change request that never entered the delivered
composition — never pinned, never released, owning nothing that survives — is deleted. Marking it
superseded would assert a lineage that does not exist. It would also leave a complete dossier on disk
whose gates read CLOSED and whose design claims to be the whole declaration of an artifact it no
longer describes. That is not a record. It is a hazard a reader can act on.

**Being built once, or executed once, does not keep it.** What decides is whether any of it survives
in the composition that matters. Where a later change has re-emitted the same artifacts, nothing of
the earlier one survives.

**With one condition:**

> A change request that never entered the delivered composition leaves no trace on deletion —
> **provided nothing cites it.** Where something does, re-ground the citation first, then delete.

A dossier can be evidence for another dossier while delivering nothing itself. A deletion can break
that evidence quietly: a verified belief grounded on a path that is no longer there is worse than the
dossier it pointed at. Re-ground it on something that survives and says the same thing, then delete.

**Why this is the right boundary.** Keeping every dossier ever authored accumulates records faster
than the changes they describe, and each one looks live until a reader opens it. In-flight work may
be consolidated and re-authored so that one artifact has one design of record.

**What this does not license.** A delivered change is never deleted, however wrong it turned out to
be. Its artifacts are in a composition somebody ran, and its dossier is the evidence of an approval
that happened. Correcting it is a new change request.
