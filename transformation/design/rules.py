"""The rule declaration shared by every phase.

A rule is data: what it is called, which register it governs, which check kind evaluates it, and
with what parameters. No rule logic lives here and no governance intent lives in `evaluate/`.

Every rule is declared in a phase's register schema. Those that follow from shape are derived by
`expand.py`; the rest are the schema's `allOf` entries, decoded by `declared.py`. A sealed rule
arrives as a mapping, from a workflow, and is read back with `Rule.from_mapping`. This module
publishes only the `Rule` type all of them become.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class Rule:
    """One declared admissibility rule.

    `id` is the finding code the oracle emits, shared by every rule finding the same kind of defect.
    `identity` is the rule's own: its schema's `$id` and a JSON Pointer to where it is declared.
    `register` names the register identity the rule
    governs — stable across retitling — with `section_title` as the fallback for a document that
    carries no register markers. Either may be None for a whole-document rule. `check` names a
    kind in `evaluate/`, and `params` must satisfy that kind's contract; `tc phase meta` asserts
    both.
    """

    id: str
    check: str
    identity: str = ""
    section_title: str | None = None
    register: str | None = None
    params: dict[str, Any] = field(default_factory=dict)
    intent: str = ""

    @staticmethod
    def from_mapping(data: Mapping[str, Any]) -> "Rule":
        """A rule as a workflow seals it. A rule that names a register is located by it; the section
        title falls back to the register, so a rule arriving without its title still finds its
        place rather than passing over the whole register."""
        for required in ("id", "check"):
            if required not in data:
                raise KeyError(f"declared rule is missing {required!r}: {dict(data)}")
        register = data.get("register")
        return Rule(
            id=data["id"],
            check=data["check"],
            identity=data.get("identity", ""),
            section_title=data.get("section_title") or register,
            register=register,
            params=dict(data.get("params") or {}),
            intent=data.get("intent", ""),
        )
