"""Which upstream documents a phase document is judged against — derived, never restated.

Two harnesses need this answer and neither should hold its own copy of it. The differential judges
corpus documents against their priors; the payload builder embeds those priors into the runtime
payloads. A hand-kept table in either one is a table that goes stale the first time a probe is added.

Two facts already exist and this reads them rather than duplicating them:

  **which phases** a document is judged against — `x-priors` in that phase's register schema, which is also
  what the compiled workflow declares;

  **which dossier** supplies them — the document's own `cr` header field, which every dossier document
  carries because P1 is the Change Request phase whatever domain it runs against.

So a new probe needs no wiring at all: cut it from a fixture, and it is judged against that fixture's
priors because it says so in its own header.
"""
from __future__ import annotations

import re
from pathlib import Path

from transformation.design.read import parse_text

REPO = Path(__file__).resolve().parents[2]

# Where a dossier that can supply priors may live. A directory is one if it carries a seed — the
# document P0 produces — rather than because it was listed here. Delivered dossiers stay in the form
# they were approved in, so a prior from one is read from its test copy, converted once by the
# oracle's reader.
DOSSIER_ROOTS = (
    REPO / "scripts/testbed/fixture_dossiers",
    REPO / "scripts/testbed/delivered_copies/transformation/dossiers",
)


def cr_of(path: Path) -> str | None:
    """The change request a document declares itself part of, read from its Machine block."""
    return parse_text(path.read_text(encoding="utf-8"))[0].get("cr") or None


def dossiers_by_cr() -> dict[str, Path]:
    """`cr` value → the dossier that declares it, read from each dossier's own seed.

    The seed is the authority for what a dossier is called, and it is not always the directory name:
    `dossiers/founding_design_bootstrap` declares `new_subdomain`. Reading the header rather than
    mapping the two keeps the one place a rename has to happen inside the dossier.
    """
    out: dict[str, Path] = {}
    for root in DOSSIER_ROOTS:
        for seed in sorted(root.glob("*/p0_seed_*.md")):
            cr = cr_of(seed)
            if cr and cr not in out:
                out[cr] = seed.parent
    return out


DOSSIERS_BY_CR = dossiers_by_cr()


def prior_path(dossier: Path, phase_id: str) -> Path:
    """The document a dossier offers for one phase.

    P0's prior is the **seed**, never `p0_business_problem_statement.md` — the seed is what P1
    consumes, and handing the problem statement instead would judge a handoff that never happened.
    """
    pattern = "p0_seed_*.md" if phase_id == "p0" else f"{phase_id}_*.md"
    found = sorted(dossier.glob(pattern))
    if not found:
        raise SystemExit(f"{dossier.name} offers no {phase_id} document, and one is declared a prior")
    return found[0]


def prior_paths(doc_path: Path, declared: tuple[str, ...]) -> dict[str, Path]:
    """`phase id → prior document`, for one judged document.

    A document that cannot say which dossier it belongs to is a hard failure rather than an unchecked
    handoff: a corpus is discovered by glob, and a document judged against no prior at all would
    quietly stop exercising every cross-phase rule while still producing a verdict.
    """
    if not declared:
        return {}
    cr = cr_of(doc_path)
    if cr is None:
        raise SystemExit(
            f"{doc_path.name} is judged by a phase with cross-phase rules and carries no cr "
            f"header, so nothing says which dossier supplies its priors"
        )
    dossier = DOSSIERS_BY_CR.get(cr)
    if dossier is None:
        raise SystemExit(
            f"{doc_path.name} declares CR {cr!r} and no dossier under "
            f"{', '.join(r.name for r in DOSSIER_ROOTS)} carries a seed declaring it"
        )
    return {phase_id: prior_path(dossier, phase_id) for phase_id in declared}


def declared_priors(phase_id: str) -> tuple[str, ...]:
    """The phases a phase declares as priors, read from the module that declares them."""
    from transformation.design.rule_sets import RULE_SETS

    return RULE_SETS[phase_id].priors
