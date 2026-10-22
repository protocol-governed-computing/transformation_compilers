"""The phase catalogue — what each phase is for, and what it may say.

A filename says which phase; it does not say what the phase is *for*. Authoring a dossier means
holding in mind, per phase, the question being answered and the vocabulary admitted — and the
commonest authoring failure is answering the next phase's question early, which the purity ladder
exists to prevent.

Purpose, question and key rule are taken from field manual §4.1; the purity rung from §4.2. They
are declared in `transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0`, with each phase's schema,
workflow and template, so that `tc phase list` can state them at the moment of authoring, and so a
rule set can key on the rung rather than restating it.

**The purity ladder** (§4.2) — each phase admits exactly one more vocabulary class:

    p1–p4    business language only — nothing new gets a code
    p5       + provisional capability names (IN/WF/CC vocabulary, unbound)
    p6       + placement (WHERE) — still no new codes
    p7      + binding FQDNs, topology, schemas, stores
    p7       + build order

With one exception at every rung: **an artifact already in the baseline may be cited by exact FQDN
as evidence — citing the baseline is observation, not design.** That exception is why a grounding
register legitimately names artifacts a business register may not, and it is checked by resolving
the identity against the baseline rather than by which column it sits in.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml
from transformation.machine_block import machine_yaml

# Vocabulary classes a phase may introduce, in ladder order. A phase admits its own rung and every
# rung below it.
RUNGS = ("business_language", "provisional_codes", "placement", "binding_fqdns", "build_order")


@dataclass(frozen=True)
class Phase:
    """One phase of the dossier pipeline."""

    id: str
    schema_id: str
    workflow: str
    template: str
    rung: str
    purpose: str
    question: str
    key_rule: str
    gate: str | None = None

    @property
    def schema(self) -> str:
        """The file of the register schema declaring this phase's document shape."""
        return f"{self.schema_id.rsplit('.', 1)[-1]}.json"

    @property
    def lineage(self) -> str:
        """The workflow's code without its version: what a design cites to mean its latest."""
        return re.sub(r"_V\d+$", "", self.workflow.split("::")[-1])

    @property
    def admits(self) -> tuple[str, ...]:
        """Every vocabulary class this phase may use — its rung and all below it."""
        return RUNGS[: RUNGS.index(self.rung) + 1]

    @property
    def may_declare_new_codes(self) -> bool:
        """Whether this phase may introduce an artifact identity that does not yet exist."""
        return self.rung in ("binding_fqdns", "build_order")


# The dispatch is declared in the registry, once. Read at import, because every phase lookup needs it
# and the registry does not change during a run.
DISPATCH = Path(__file__).resolve().parents[2] / "registry" / "structures" / "STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0.md"


def _declared() -> tuple[Phase, ...]:
    text = DISPATCH.read_text(encoding="utf-8")
    machine = machine_yaml(text)
    if machine is None:
        raise ValueError(f"{DISPATCH.name} carries no Machine block")
    rows = yaml.safe_load(machine)["core"]["phases"]
    return tuple(Phase(id=row["phase"], schema_id=row["schema"], workflow=row["workflow"],
                       template=row["template"], rung=row["rung"], purpose=row["purpose"],
                       question=row["question"], key_rule=row["key_rule"], gate=row.get("gate"))
                 for row in rows)


PHASES: tuple[Phase, ...] = _declared()

PHASES_BY_ID: dict[str, Phase] = {p.id: p for p in PHASES}


def phase(phase_id: str) -> Phase:
    """Look up a declared phase, or fail hard. There is no default."""
    if phase_id not in PHASES_BY_ID:
        raise KeyError(f"no such phase: {phase_id!r}; declared phases are {sorted(PHASES_BY_ID)}")
    return PHASES_BY_ID[phase_id]


def next_phase(phase_id: str) -> str | None:
    """The phase this one feeds, or None at the end of the pipeline.

    Read from the declared order rather than a lookup table, so adding a phase to the dispatch is the
    whole of adding it to the pipeline.
    """
    ids = [p.id for p in PHASES]
    if phase_id not in ids:
        return None
    position = ids.index(phase_id) + 1
    return ids[position] if position < len(ids) else None
