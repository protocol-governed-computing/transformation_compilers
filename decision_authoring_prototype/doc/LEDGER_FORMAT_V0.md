# Decision Ledger Format V0

Step 2 of `PLAN_DECISION_LEDGER_AUTHORING.md`.

## Principle

The author answers questions. The author never chooses a category, a family or a register.

The front end owns a catalog of typed questions. It asks only the questions that the answers so
far make relevant. Each answer has a fixed shape, and that shape determines which P7 content the
front end derives from it. The author's file holds the answers and nothing else.

## The author's file

```yaml
domain: book_library_mgmt
purpose: >
  Library staff keep the catalog of the books the library holds and the copies it owns.

answers:
  - ask: identity
    about: edition
    answer:
      same_when: [title, author, publication_year]
      normalized: true
      on_duplicate: refuse
    decided_by: catalog owner

  - ask: query_excludes
    about: search catalog
    answer:
      always_exclude: {state: retired}
      caller_may_override: false
    decided_by: catalog owner

  - ask: nothing_found
    about: search catalog
    open: true          # unanswered: dependent behavior is refused at admission

cases:
  - when: search catalog
    given: {"The Odyssey": retired}
    request: {title: "The Odyssey"}
    then: returns nothing
    because: retired books are not offered
```

The file has three kinds of entry:

- **Answer.** `ask` names a question in the catalog, `about` names its subject in the author's
  words, `answer` gives its shape, and `decided_by` names the authority.
- **Open question.** `open: true` with no `answer`. The front end emits no P7 for the behavior
  that depends on it, and admission refuses that behavior.
- **Case.** Given a state, a request produces an outcome, with a reason. It is written in domain
  words with no field paths.

No entry names a PGC family, code or register.

## The question catalog

The census of `book_library_mgmt` sorted its 34 decisions into nine groups. Each group becomes one
or more typed questions. The right-hand column is the content the front end derives. The author
never sees it.

| Question | Asked when | Answer shape | Derives |
|---|---|---|---|
| `purpose` | always | one sentence | domain, subdomain |
| `operations` | always | list of named operations | WF, IN, entry topology |
| `actor` | per operation | who, and what authorizes them | AC, authorization step, rule literal |
| `things` | always | named things and how they relate | stores, structure, references |
| `required` | per thing | fields with type and requirement | IN fields, schema literals, validation step |
| `identity` | per thing | fields, normalization, on-duplicate | key CT, registry store, claim step |
| `states` | per thing with a lifecycle | states, and which operation moves between them | state literals, transition steps |
| `precondition` | per operation | what must already exist or hold | resolve step, refusal routing |
| `invariant_on_change` | per updating operation | what may not change | compare step, rule literal |
| `query_excludes` | per reading operation | fixed exclusions, caller override | fixed filter step |
| `query_returns` | per reading operation | what comes back, and grouping | select, group and projection steps |
| `nothing_found` | per reading operation | empty result or refusal | routing on no match |
| `trail` | always | what each operation records | append step, trail store |
| `announces` | per operation | event, and what it carries | EV, emit property |

Questions are asked in this order. A question that depends on an unanswered question is not asked.

## Doctrine, not questions

Some P7 content looks like a decision but follows from PGC doctrine. The front end applies it
without asking. Each rule is stated once and cited by every cell it produces.

- **Refusal precedence.** Authorization, then validation, then identity claim, then the write.
  Census finding 4 is settled here as doctrine, and the author can override it with an answer.
- **Storage mechanism.** A thing with identity gets a registry. A thing with a lifecycle gets a
  mutable store. A trail gets an append-only store.
- **Naming and versioning.** Codes come from the author's names. New artifacts start at `_V0`.
- **Trail on every operation.** This applies unless a `trail` answer says otherwise.

## What the census predicts

- All 34 decisions map onto a question in the catalog. Decision 19 (an additional edition needs an
  existing work) fit none of the nine groups. It needed the `precondition` question.
- Decision 31 (search excludes retired) maps onto `query_excludes`. The baseline never asked it.
  That is how the gap in the search rule arose.
- Census findings 2 and 3 (no event on reinstatement, inconsistent trail subject) become answers
  to `announces` and `trail`. They are no longer silent defaults.

## Open choices

- **Answer shapes are closed.** An answer that does not fit its shape is refused. It is not
  interpreted. This keeps derivation deterministic, at the cost of expressiveness. The prototype
  tests whether the shapes cover a second domain.
- **The catalog is PGC-owned and versioned.** Adding a question is a change to the front end,
  not to any domain.
