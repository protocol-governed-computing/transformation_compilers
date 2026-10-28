# Findings — Blind Ledger Run of `blockchain`

An LLM author wrote a ledger from two files: the ledger format and `LEDGER_BRIEF_BLOCKCHAIN.md`. It
saw no design, no seed, no census and no owner answer. Its ledger is
`LEDGER_BRIEF_RUN_BLOCKCHAIN.yaml`.

## Result

| Measure | Book | Blockchain |
|---|---:|---:|
| Lines | 245 | 762 |
| Answers | 24 | 38 |
| Open questions | 9 | 15 |
| Cases | 17 | 33 |
| New question types | 0 | 12 |

The ledger addresses all 32 census decisions. Fifteen are left fully or partly open. The author
made no decision without a basis in the brief or a disclosed inference. It added one operation the
brief implies and the baseline lacks: showing one actor.

## The catalog fell short

The book catalog has fourteen question types. The author needed twelve more. They fall into three
groups.

**Questions the catalog should gain.** Each states a real business decision that no question
asked.

| Question | What it asks |
|---|---|
| `parts` | which part of the business owns each thing and act |
| `required_when` | a field required by one act and optional for another |
| `allowed_values` | a named set of values, and the subset that may be created |
| `derived_value` | a value computed from supplied material, by a named rule |
| `on_repeat` | a duplicate that succeeds, what it records, and what it announces |
| `reads_other_part` | another part's records an act reads, and never writes |
| `public_acts` | the acts offered from outside |
| `entrance_turns_away` | what an entrance may refuse, and what it tells the caller |
| `outcome_classes` | the answers a caller can receive, and which are kept apart |

**A question that splits in two.** `value_source` covers a default when a value is absent, a value
fixed by the business, and a time set by the clock. The default is a decision. The other two are
doctrine.

**Doctrine restated as answers.** `request_cannot_override` and `on_record_failure` restate rules
every act follows. The author answered them because the brief stated them as requirements. They
are the content of three of the four corrective change requests: cr_05, cr_06 and cr_07.

The lesson is about the brief and the catalog, not the author. Doctrine belongs in the catalog as
fixed rules the author sees and cannot answer. A brief should state only what the business decides.

## Why so many open questions

Fifteen open questions have three causes.

**The brief left them out.** Four come from my brief, not from the business.

- The announcements of accept, reject and wallet creation. The seeds name all three events.
- The public names of the offered acts. Today's design names them.
- How the acts not offered from outside are reached.

**The baseline decided them silently.** Ten are real gaps that today's design filled without a
recorded decision.

- Who counts as an authority, and what proves it without a login. The seeds defer it. The design
  records whatever authority the request names, and checks nothing.
- Who may list or show actors, and what showing an unknown actor answers.
- Whether a contact address is normalized. The design compares it exactly.
- The exact form of a wallet's identity.
- A key that is not a key, and two holders supplying the same key.
- Whether an empty list is empty or refused.
- Whether a refused act leaves a moment on the trail. The design leaves none.

**The brief holds a conflict.** A registration with no name is refused by the act, and turned
away by the entrance. The author asked which answer the caller hears. Today's design does both: the
entrance turns it away, and the act would refuse it if reached directly.

## What this shows

- **The format holds for a second domain.** No answer needed a design term. Every gap surfaced as
  an open question or a new question type, not as an invented rule.
- **The catalog does not.** It covered one domain and needs about ten more question types for a
  second. That is the risk named in the phase-split analysis: discovery finds the questions a
  catalog lacks. Here an author found them, which is the cheap case.
- **The blind run finds what the baseline never decided.** The book run found five defects in its design.
  Blockchain finds ten silent decisions, and one of them is the trust model: anyone may name
  themselves an authority.

## The owner's answers

All fifteen are answered in `LEDGER_OWNER_ANSWERS_BLOCKCHAIN.yaml`. The seeds answer the four the
brief left out. The owner answered the other eleven.

- Six keep today's behavior and now stand as recorded decisions: the authority, contact-address
  comparison, the wallet identity's form, an unreadable key, a refusal's trail, and which answer a
  caller hears for a missing name. The trust model stays deferred: a decision records the authority
  the request names, and nothing checks it.
- Listing is reached from inside only, with no check. The author's "show actor" is dropped, because
  listing by state covers what the business asked.
- Two change behavior. Listing a state with no actors answers with an empty list. A wallet whose
  key gives an address another wallet already holds is refused.

The checks gained a criterion for each change. Today's design fails the second: two people
supplying the same key both get a wallet, at one address.

## Next

1. Move doctrine into the catalog as fixed rules, and drop it from the ledger.
2. Extend the generator for the new question types, and keep the book run passing.
