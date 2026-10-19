"""Plain-data shapes shared by the genesis oracle and the compiled evaluator.

The compiled transform receives registers and rules as ordinary mappings — that is what crosses a
capability boundary. The genesis oracle works on the same shapes, so both apply identical logic to
identical inputs and a differential run compares like with like.

Nothing here judges anything. These are the structures a check kind is handed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass
class Table:
    """A register's rows. `rows` holds content only: an empty list is either a register declared
    empty (`declared_empty`) or one that states nothing at all (`stated` false)."""

    rows: list[dict[str, Any]] = field(default_factory=list)
    declared_empty: bool = False
    stated: bool = True

    @property
    def keys(self) -> list[str]:
        """Every column key a row carries, in first-seen order."""
        out: list[str] = []
        for row in self.rows:
            out += [k for k in row if k not in out]
        return out


@dataclass
class Block:
    """One `##` section of a phase document."""

    number: int | None
    title: str
    body: str = ""
    table: Table | None = None

    def text(self) -> str:
        return self.body.strip()

    @staticmethod
    def from_mapping(data: Mapping[str, Any]) -> "Block":
        return Block(number=data.get("number"), title=data.get("title", ""), body=data.get("text", ""))


def _register_block(registers: list, register_id: str) -> "Block | None":
    """Build a Block for one register out of parsed register data.

    Shared by a document's own registers and by an upstream phase's, so a prior register is read
    exactly the way the document's own is — two readers here would let a cross-phase rule disagree
    with a same-phase rule about what a register contains.
    """
    for entry in registers:
        if entry.get("id") != register_id:
            continue
        value = entry.get("value")
        if isinstance(value, list):
            table = Table(rows=[dict(r) for r in value if isinstance(r, Mapping)],
                          declared_empty=not value)
            return Block(number=None, title=register_id, table=table)
        if value is None:
            return Block(number=None, title=register_id, table=Table(stated=False))
        return Block(number=None, title=register_id, body=str(value))
    return None


@dataclass
class ParsedDocument:
    """A phase document as registers, plus whatever was observed about the composition.

    `observed` is empty for phases that judge a document alone. A phase that grounds claims against
    the assembled system fills it from a governed inspection capability, keyed by the operation that
    produced each fact — so a check can say which observation it relied on, and a missing
    observation is visible rather than silently absent.

    `priors` is the same shape for a different outside: the phase documents this one was handed.
    Nine phases hand off through `gov_projection` and every rule until now judged one document, so
    a phase could drop an upstream commitment and still report ADMISSIBLE. Keyed by phase id for
    the same reason `observed` is keyed by operation — a check names what it relied on, and an
    absent prior is visible rather than a silent pass.
    """

    header: dict[str, str]
    sections: list[Any]
    raw: str
    path: str = ""
    registers: list[Any] = field(default_factory=list)
    observed: dict[str, Any] = field(default_factory=dict)
    priors: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.blocks = [
            s if isinstance(s, Block) else Block.from_mapping(s) for s in self.sections
        ]

    def register(self, register_id: str) -> Block | None:
        """The register with this identity, or None if the document does not carry it.

        Registers are addressed by their key in the document's Machine block. Identity is stable
        across retitling and unambiguous when one section holds several registers.
        """
        return _register_block(self.registers, register_id)

    def prior_register(self, phase_id: str, register_id: str) -> Block | None:
        """A register of an upstream phase document, or None if it is not reachable.

        None means one of two different things — the prior was never supplied, or it was supplied
        and carries no such register — and a cross-phase check must distinguish them, so
        `has_prior` answers the first separately. Reporting "the register is missing" when the
        document was never handed over would blame the author for the driver's omission.
        """
        prior = self.priors.get(phase_id)
        if not prior:
            return None
        return _register_block(prior.get("registers") or [], register_id)

    def has_prior(self, phase_id: str) -> bool:
        """Whether the upstream phase document was supplied at all."""
        return bool(self.priors.get(phase_id))

    def find(self, title_prefix: str) -> Block | None:
        """First block whose title starts with `title_prefix`.

        Real titles carry trailing annotations ("Known Facts — Business Truths (…)"), so match on
        the prefix and keep the annotation as authored.
        """
        low = title_prefix.lower()
        for block in self.blocks:
            if block.title.lower().startswith(low):
                return block
        return None
