"""Each phase's rule set, expanded from the register schema the dispatch names for it.

A phase has no module of its own. Its shape, its priors, its observations and its rules are all
declared in its schema, and `transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0` says which schema
that is. Adding a phase to the dispatch is the whole of adding its rule set.
"""

from __future__ import annotations

from dataclasses import dataclass

from transformation.design.catalog import PHASES
from transformation.design.expand import expanded_rules
from transformation.design.rules import Rule
from transformation.design.schema import PhaseShape, load


@dataclass(frozen=True)
class PhaseRules:
    """One phase's declaration, read from its schema."""

    id: str

    @property
    def shape(self) -> PhaseShape:
        return load(self.id)

    @property
    def priors(self) -> tuple[str, ...]:
        """The earlier phases a document of this phase is judged against."""
        return self.shape.priors

    @property
    def observations(self) -> dict[str, str]:
        """The composition facts this phase grounds against: inspection operation → result key."""
        return self.shape.observations

    def rule_set(self) -> list[Rule]:
        """The complete rule set: what the shape implies, then what the schema declares."""
        return expanded_rules(self.shape)


RULE_SETS: dict[str, PhaseRules] = {spec.id: PhaseRules(spec.id) for spec in PHASES}
