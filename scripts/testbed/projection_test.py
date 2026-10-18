"""The P1 projection — reproducible, general, and refusing an inadmissible prior.

A projection is only worth trusting if it is the same document every time it runs. The dossier on
disk is therefore an assertion: re-project the seed, and what comes out must be byte-identical to
what is committed. A projection nobody re-runs drifts from its input exactly the way a hand-authored
fixture drifts from its dossier.

Generality comes from CR-1, a different CR of a different type with registers of different sizes.
Its P1 was authored by hand before the projection existed: every register row already matched what
the compiler derives, and only the preamble and a widened vocabulary heading differed. That is the
strongest evidence the projection is right, and asserting it byte for byte is what stops the
authored and derived forms diverging again.

Run:  python scripts/testbed/projection_test.py
Exit: 0 if every case matched, 1 otherwise.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
sys.path.insert(0, str(REPO))

from meta_test import assert_consistent  # noqa: E402
from transformation.design.oracle import evaluate  # noqa: E402
from transformation.design.rule_sets import RULE_SETS  # noqa: E402
from transformation.design.project import PROJECTIONS  # noqa: E402
from transformation.design.read import parse_text, read_seed  # noqa: E402

# Fixtures maintained against the current rule set. See `fixtures/README.md`.
DOSSIERS = REPO / "scripts/testbed/fixtures/catalog"
CR_01 = DOSSIERS / "cr_01_catalog"
CR_02 = DOSSIERS / "cr_02_catalog"
CORPUS = REPO / "scripts/testbed/corpus"


def _priors(seed_path: Path) -> dict:
    prior = read_seed(seed_path)
    return {"p0": {"header": prior.header, "sections": prior.sections,
                   "registers": prior.registers}}


def _projected(seed_path: Path):
    """The projected document, read back as the oracle reads one."""
    _, projection = PROJECTIONS["p1"]
    text = projection(read_seed(seed_path))
    header, sections, registers = parse_text(text)
    doc = read_seed(seed_path)
    doc.header, doc.sections, doc.registers, doc.raw = header, sections, registers, text
    doc.__post_init__()
    doc.priors = _priors(seed_path)
    return text, doc


def main() -> int:
    # The projected P1 is judged against P1's rule set; that judgement is the whole assertion here.
    assert_consistent()
    problems: list[str] = []

    # Reproducible: every committed P1 is what the projection emits, byte for byte. Both dossiers,
    # because CR-1's P1 was authored by hand before the projection existed and re-projected
    # afterwards — every register row was already identical, and only its preamble and a widened
    # vocabulary heading changed. A committed document the compiler would not reproduce is the drift
    # the projection exists to remove, and it can only return here.
    for name, dossier in (("cr_01", CR_01), ("cr_02", CR_02)):
        text, doc = _projected(dossier / "p0_seed_book_library_mgmt_catalog_v0.md")
        committed = (dossier / "p1_change_request_book_library_mgmt_catalog_v0.md").read_text(
            encoding="utf-8"
        )
        if text == committed:
            print(f"  PASS  {name}  projection reproduces the committed P1")
        else:
            problems.append(f"{name} projection differs from the committed P1")
            print(f"  FAIL  {name}  projection differs from the committed P1")

        verdict = evaluate(doc, RULE_SETS["p1"].rule_set())
        status = "PASS" if verdict.admissible else "FAIL"
        print(f"  {status}  {name}  projected P1 {verdict.verdict} "
              f"over {verdict.rules_evaluated} rules")
        if not verdict.admissible:
            problems.append(f"{name} projected P1 {verdict.verdict}")
            for finding in verdict.findings:
                print(f"          {finding}")

    # Refused: a prior that still carries an open blocking clarification is not projectable, and the
    # CLI is what enforces it — this asserts the verdict the CLI acts on.
    blocked = read_seed(CORPUS / "inadmissible_p0_blocking_clarification.md")
    verdict = evaluate(blocked, RULE_SETS["p0"].rule_set())
    fired = {f.code for f in verdict.findings}
    if not verdict.admissible and "BLOCKING_CLARIFICATION_OUTSTANDING" in fired:
        print("  PASS  corpus blocking-clarification seed refused before projection")
    else:
        problems.append("a seed with an open blocking clarification was not refused")
        print("  FAIL  corpus blocking-clarification seed was not refused")

    if problems:
        print(f"\nPROJECTION FAILED — {len(problems)} problem(s)")
        return 1
    print("\nPROJECTION PASSED — reproducible, general, and refusing an inadmissible prior")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
