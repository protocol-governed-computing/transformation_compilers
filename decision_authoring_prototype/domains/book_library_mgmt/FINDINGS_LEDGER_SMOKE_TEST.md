# Findings — Blind Ledger Smoke Test

Step 3 of `PLAN_DECISION_LEDGER_AUTHORING.md`, run with an LLM author as a smoke test.

## Setup

- **Author.** A fresh agent with no tool access. It was told to act as a library's catalog owner.
- **Brief.** One sentence: "Library staff keep the catalog of the books the library holds and the
  copies it owns."
- **Format.** `LEDGER_FORMAT_V0.md` with the derivation column removed. Its example came from
  another domain (a tool shed), so no library decision leaked.
- **Answer key.** The 34 decisions in `FINDINGS_DECISION_LEDGER_CENSUS.md`.

## Format result: it works

- The author produced 34 answers, 4 open questions and 15 cases in about 230 lines.
- It used no PGC vocabulary.
- It used every question in the catalog. It split `actor` by operation group, as the format
  allows.
- It placed open questions where a real owner would defer: the public-catalog access rule, the
  identity of a title with no ISBN, withdrawing a copy that is out on loan, and record retention.
  Each open question names the authority it waits on.
- It answered both questions the baseline never asked:
  - `query_excludes`: retired titles are excluded. A cataloger may override the exclusion.
  - `nothing_found`: search returns an empty list. Viewing an unknown title is refused.

  The baseline refuses an empty search (VIOLATION). The ledger forced the question, and the
  author's answer differs from the baseline.

## Score against the 34 decisions

| Outcome | Count | Decisions |
|---|---:|---|
| Matched | 17 | 1, 5–8, 11, 12, 14, 19, 22–24, 27, 31–34 |
| Different but defensible | 11 | 3, 9, 10, 13, 16, 18, 21, 25, 28–30 |
| Absent (no "work" concept) | 4 | 4, 15, 17, 20 |
| Missed | 2 | 2 (deny by default), 26 (retired stays retrievable) |

The author also made about 13 decisions that the baseline does not hold. Examples:

- Copy states for processing, missing and found.
- A required reason for each withdrawal.
- A title cannot be retired while it still has copies.
- Barcodes are never reused.
- Branch and shelf location.
- The trail records values before and after each change.
- Reads are not trailed. The baseline trails search and retrieval.

The main divergences:

- **Edition identity.** The author identifies an edition by ISBN. The baseline uses normalized
  title, author and year. The author left the title-without-ISBN case open, which is close to the
  baseline's whole identity rule.
- **No work concept.** The author has titles and copies only. The baseline's work/edition split,
  and its additional-edition operation, never appear.
- **Reinstatement.** The author's retirement is terminal. The baseline allows reinstatement.

## What this shows

1. **The format is usable without PGC knowledge.** This is evidence only from an LLM author.
2. **The 34 are real decisions.** Half of them were made differently by another competent owner
   working from the same purpose. A one-sentence purpose does not determine them, so they cannot
   be mechanical. This supports the census classification.
3. **The comparison in step 5 needs the real requirements.** Snapshot equivalence can hold only
   when the author starts from the same business requirements as the baseline. The purpose
   sentence is not enough. The repository keeps no P0 seed for this domain. The closest source is
   the criteria stated in `testbed/catalog/execution_validation*.py`.
4. **The ledger exposes silent defaults.** `nothing_found` and trailed reads are behavior the
   baseline holds that nobody decided on the record.

## Limits

- The author is an LLM. It knows libraries in general, and it knows nothing of this library.
- The scoring is one reader's judgment. "Different but defensible" is a judgment call for each
  decision.
- The test does not exercise derivation. No P7 was generated.

The authored ledger is `LEDGER_SMOKE_TEST_LIBRARY_CATALOG.yaml`.

## Run 2 — brief from the testbed criteria

- **Brief.** `LEDGER_BRIEF_LIBRARY_CATALOG.md`. It restates the criteria from
  `testbed/catalog/execution_validation*.py` in plain business language. It leaves out the
  migration criteria ("a record written before this change…").
- **Author.** A fresh agent with no tool access. It was told to follow the brief, to leave open
  whatever the brief does not settle, and to flag every inference with `why_inferred`.
- **Ledger.** `LEDGER_BRIEF_RUN_LIBRARY_CATALOG.yaml`: 24 answers, 9 open questions and 17 cases.
  It uses no PGC vocabulary.

### Score against the 34 decisions

| Outcome | Count | Decisions |
|---|---:|---|
| Matched | 27 | 1–15, 18, 19, 21–26, 29–32 |
| Misread wording in the brief | 2 | 16, 28 |
| Follows the brief; the baseline encodes more | 1 | 27 |
| Open, because the brief is silent | 4 | 17 (work fields), 20 (work identity), 33–34 (events) |

The author made no decision without either a basis in the brief or a disclosed inference. That
meets the plan's target of zero unauthorized rules.

### The divergences

- **16 and 28: "description".** The brief says a correction may not leave a book "without its
  description". The author read "description" as a separate required field. In the baseline it
  means the subject list. The wording of the brief caused this, and the author disclosed the
  inference.
- **27: the update rule is stronger than its criterion.** The criterion says an update that
  "would duplicate another registered book is refused." The baseline compares the updated
  identity key with the current one and refuses any change of title, author or year
  (`compare_identity`, `require_identity_unchanged`). Check 17 changes the Iliad into the Odyssey,
  which is both a duplicate and an identity change, so it cannot tell the two rules apart. This is
  a second place where the stated behavior and the encoded behavior differ. The first is the
  search gap.

### What the open questions show

The 9 open questions are decisions the baseline holds that its own criteria never state:

| Open question | What the baseline does |
|---|---|
| Required fields of a work | title and author |
| Identity of a work | normalized title and author |
| Identity of an edition beyond the book key | the same key as the book |
| Can a correction move an edition to another work? | No: the work key is copied from the record |
| Can a search include retired books? | Yes, if the caller says so (the search gap) |
| Empty search | refused (VIOLATION) |
| Retrieving an unknown book | refused |
| What the trail holds | operation, staff, subject (inconsistent, census finding 3) |
| Events | six, on completion |

None of the 9 are stated in the criteria. For three of them, the baseline's answer is a defect or
an unexamined default: the search override, the empty-search refusal and the inconsistent trail
subject.

### Conclusion

- From the real requirements, the ledger reproduces 27 of 34 decisions. It leaves the rest
  visibly open or flagged.
- The ledger is a stricter account of the domain than its own acceptance criteria. Every
  divergence it found is a place where the baseline holds behavior nobody stated.
- Step 4 is next. The owner answers the 9 open questions and fixes "description" to mean subject.
  Then a front end derives P7 from the completed ledger. The expected difference from the baseline
  is decision 27 and the three defects. Nothing else should differ.
