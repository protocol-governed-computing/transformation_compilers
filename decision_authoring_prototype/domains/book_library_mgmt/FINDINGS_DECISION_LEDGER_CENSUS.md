# Findings — Decision Ledger Census of `book_library_mgmt`

Step 1 of `PLAN_DECISION_LEDGER_AUTHORING.md`. The census classifies every leaf value in the
baseline P7 registers and lists the distinct human decisions they encode.

## Result

The gate passes. The domain rests on 34 decisions. Its P7 holds 4,033 leaf values.

| Class | Leaves | Share |
|---|---:|---:|
| Decision | 415 | 10.3% |
| Case | 111 | 2.8% |
| Mechanical | 3,507 | 87.0% |
| Unaccounted | 0 | — |

The 415 decision leaves repeat 34 decisions. For example, "an edition requires title, author,
year and subject" appears in four schema literals, and staff authorization appears on all ten
boundaries. One decision costs about 12 leaves on average. One decision costs about 119 leaves of
P7 overall.

| Register | Decision | Case | Mechanical |
|---|---:|---:|---:|
| `step_bindings` | 152 | | 1,120 |
| `interface_fields` | 217 | | 748 |
| `cc_composition` | 6 | | 864 |
| `execution_topology` | | | 369 |
| `new_artifacts` | 34 | | 221 |
| `test_cases`, `test_case_values` | | 111 | |
| other registers | 6 | | 185 |

Most of the bulk is wiring: step bindings, interface fields, composition and topology.

## The 34 decisions

**Authority (2)**
1. Only identified, authorized library staff perform catalog operations.
2. Authorization is denied unless it is stated.

**Operations (10)**
3–12. Register a book with its first copy, register an additional edition, register a copy,
update bibliographic information, retire a book, retire a copy, reinstate a book, reinstate a
copy, retrieve book details, search the catalog.

**Concepts (3)**
13. The catalog holds works, editions and physical copies.
14. A copy belongs to exactly one edition.
15. An edition belongs to exactly one work.

**Required content (4)**
16. An edition requires title, author, publication year and at least one subject.
17. A work requires title and author.
18. Registering a book requires a barcode and records its first copy.
19. An additional edition requires that its work already exists.

**Identity (4)**
20. A work is identified by its normalized title and author.
21. An edition is identified by its normalized title, author and year.
22. A copy is identified by its barcode.
23. A duplicate edition or copy is refused. A known work is reused.

**Lifecycle (3)**
24. Books and copies are either registered or retired.
25. A retired book or copy can be reinstated.
26. A retired book stays retrievable.

**Change (2)**
27. An update cannot change an edition's identity.
28. An update must leave at least one subject.

**Query (3)**
29. Search is by subject or by title.
30. Results are grouped by work and carry no copy information.
31. Search excludes retired books.

**Evidence (3)**
32. Every operation is appended to a trail with its actor and subject.
33. Six operations publish an event when they complete.
34. Each event carries the identity, the actor and the time.

The cases are the 5 P7 unit cases and the 50 checks in `testbed/catalog/`.

## Hidden and unaccounted content

The classifier labels every leaf it does not match as mechanical, so "unaccounted: 0" holds by
construction. A manual read found five places where content is not traceable to a decision.

1. **Decision 31 is not held by the snapshot.** The search workflow's summary says it excludes
   retired books. The registers pass `inputs.search_criteria` straight to the filter. The caller
   supplies `state: REGISTERED` (`testbed/catalog/test_payloads/04_search_catalog.json`). A caller
   who omits it sees retired books. This is a governance gap, not only an authoring finding.
2. **Reinstatement publishes no event.** Retirement does. No decision says whether this is
   intended.
3. **The trail subject is inconsistent.** `REGISTER_BOOK` records the title. Every other
   operation records the identity key or barcode.
4. **Check order is a hidden decision.** Topology fixes authorization, then validation, then
   identity claim. The order decides which refusal a caller sees.
5. **The storage mechanism is a realization choice.** It is not a decision (mutable JSON,
   registry, append-only trail). The front end needs a rule for it, so it is not free.

Findings 1–3 are what a ledger would expose: each is a question nobody answered on the record.

## Limits

- "Mechanical" is asserted, not shown. Steps 4 and 5 test it by generating P7 from the ledger.
- The decision list is one reader's extraction. Step 3 checks it with an author who has not
  seen P7.
- The mechanical bulk repeats a few composition patterns: authorize, validate, claim identity,
  assemble, write, append to the trail, emit. A front end needs those patterns as doctrine.
  That library is the real cost of the prototype.

## Reproduce

`python transformation_compilers/decision_authoring_prototype/engine/census.py business_domains/book_library_mgmt/design/p7_design_intent_book_library_mgmt_baseline.md transformation_compilers/decision_authoring_prototype/domains/book_library_mgmt/census_profile.yaml`

The classifier rules are in the script: workflow, actor and event names; request, actor and event
fields; rule, schema and state literals; identity-forming attributes; and emitted events count as
decisions. Test cases count as cases. Everything else counts as mechanical.
