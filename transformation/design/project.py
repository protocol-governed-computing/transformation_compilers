"""Deterministic projections — a phase document that its prior uniquely determines.

Most phases decide something. P1 stopped deciding anything the moment blocking clarifications
became inadmissible at P0: with no open question left to interrogate, a change request is the seed's
registers plus, per row, the citation saying where it came from. Its inputs are the seed; its output
is determined; there is no design choice remaining. That is a compiler pass, not an authoring task,
and it is the same transition the Construction Compiler made when a design that uniquely determines
its artifacts stopped being rewritten by hand.

**The amendment ruling.** A question discovered while restating the seed amends P0 and is projected
again. It never enters at P1. Before the projection ran, P1 was where a second author could add a
row the business never said — the failure `ROW_NOT_IN_SEED` exists to catch — and P0's Clarification
Requests were one of two places a question could be asked. There is now one place, and human
semantic content enters the dossier exactly once.

**What P1's rule set governs afterwards.** A projected P1 cannot fail `SEED_ROW_NOT_CARRIED` or
`ROW_NOT_IN_SEED`: it was built from the rows those rules check. Reading its verdict as evidence
about the *change* would be vacuity of the kind this codebase keeps rediscovering. Those 169 rules
govern **amendment** — a P1 edited after projection, or authored by hand — and the derived fixtures
are what keeps them exercised. The check on a freshly projected P1 proves the projection, which is
worth running and is not the same claim.

A projection refuses to run against an inadmissible prior. Projecting a seed that still carries an
open blocking clarification would launder the question into a document that looks settled.
"""

from __future__ import annotations

from typing import Callable

import yaml

from transformation.design.evaluate import ParsedDocument
from transformation.design.schema import PhaseShape as PhaseTemplate, load

# The column a projected row's provenance goes in. P1 cites the seed's register and row ordinal; the
# ordinal is what makes a citation checkable, and hand-typing it is what makes it wrong — `#12`
# pointing at row 11 resolves to a claim the row does not make, and nothing downstream can tell.
PROVENANCE_KEY = "source_finding"


class _Dumper(yaml.SafeDumper):
    pass


_Dumper.add_representer(
    str, lambda d, v: d.represent_scalar("tag:yaml.org,2002:str", v, style="|" if "\n" in v else None))

# A citation is written on one line, `{phase: p2, register: gaps, row: 1}`, as an author writes it.
_CITATION_KEYS = {"phase", "register", "row", "key", "artifact", "source"}


def _mapping(dumper: yaml.SafeDumper, value: dict) -> yaml.Node:
    flow = bool(value) and set(value) <= _CITATION_KEYS and bool({"register", "artifact", "source"} & set(value))
    return dumper.represent_mapping("tag:yaml.org,2002:map", value, flow_style=flow or None)


_Dumper.add_representer(dict, _mapping)


def dump(block: dict) -> str:
    """A Machine block's YAML, as every writer of a phase document writes it."""
    return yaml.dump(block, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=100000)


def _template_layout(template: PhaseTemplate) -> list[tuple[str, str, str, tuple[str, ...]]]:
    """(number, title, register id, column keys) in the order the schema declares them.

    The schema is the single declaration of the document's shape, so the projection reads it rather
    than restating it. A register added to the schema appears in the projection with no code change.
    The section a register is cited by is the schema's, and every seed numbers its sections as the
    schema does, so the citation names a section the seed's reader finds.
    """
    return [(register.section_number or "", register.section_title, register.id, register.keys)
            for register in template.registers]


def project_p1(prior: ParsedDocument) -> str:
    """The change request the seed determines: its registers, each row cited to where it was said."""
    template = load("p1")
    by_id = {register["id"]: register for register in prior.registers}
    # The change request is the seed's change, in the same domain, judged by P1's rule set.
    document = {**{k: prior.header[k] for k in ("domain", "subdomain", "cr") if k in prior.header},
                "rule_set": template.schema_id}
    subject = (prior.raw.splitlines() or [""])[0].split("—")[-1].strip()

    registers: dict[str, list | None] = {}
    headings: list[str] = []
    for number, title, register_id, keys in _template_layout(template):
        source = by_id.get(register_id)
        content = source.get("value") if source else None
        if not isinstance(content, list):
            # A seed register that states nothing is projected as stating nothing; one the seed
            # declared empty is projected declared empty. Neither is cited: no row of the seed said it.
            registers[register_id] = content
        else:
            registers[register_id] = [
                {**{k: row.get(k) for k in keys if k != PROVENANCE_KEY},
                 PROVENANCE_KEY: {"phase": "p0", "register": register_id, "row": ordinal}}
                for ordinal, row in enumerate(content, start=1)
            ]
        headings += [f"## {number}. {title}", "", "---", ""]

    machine = dump(
        {"document": {"phase": "p1", **document}, "registers": registers})

    emits = " · ".join(register.id for register in template.registers)
    parts = [
        f"# Stage 1 — Change Request: Clarification & Fact Capture: {subject}",
        "",
        "## Machine",
        "",
        "```yaml",
        machine.rstrip("\n"),
        "```",
        "",
        "Projected from the change seed. Every row is the seed's own, cited to the section it was",
        "said in. S1 interrogates and does not author: a question raised by restating the seed",
        "amends the seed and is projected again, so no row here states business content the seed",
        "does not.",
        "",
        "---",
        "",
        *headings,
        "## gov_projection — Governed Handoff to Stage 2",
        "",
        "| Direction | Fields |",
        "|-----------|--------|",
        "| **Consumes** ← CR seed | human elicitation answers (the seed) |",
        f"| **Emits** → Stage 2 | {emits} |",
    ]
    return "\n".join(parts) + "\n"


# phase → (the prior it is projected from, the projection). A phase absent from this table is one a
# human still decides; adding an entry is a ruling that it no longer is.
PROJECTIONS: dict[str, tuple[str, Callable[[ParsedDocument], str]]] = {
    "p1": ("p0", project_p1),
}
