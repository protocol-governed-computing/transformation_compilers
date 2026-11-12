"""The P0 structural oracle — a generic evaluator over the declared rule set.

This module contains **no rules**. It walks a phase's rule set, dispatches each declared rule to
its check kind, and collects findings. What makes a seed admissible is declared in `rules.py`; how
a check is performed is implemented in `evaluate/`; this file only composes them.

The oracle is deterministic and reads no snapshot. It judges shape and discipline, never business
correctness: it cannot know whether a Business Truth is true, only whether the seed keeps truths,
beliefs and questions in their proper registers and invents no design.

The verdict is ADMISSIBLE or INADMISSIBLE. There is no warning tier — a seed a human must think
about before P1 consumes it is not admissible.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from transformation.design.evaluate import dispatch, place
from transformation.design.evaluate import ParsedDocument
from transformation.design.read import read_seed
from transformation.design.rules import Rule

ADMISSIBLE = "ADMISSIBLE"
INADMISSIBLE = "INADMISSIBLE"


@dataclass(frozen=True)
class Finding:
    """One defect. `code` names its kind, `rule` the declaration that found it, and `locator` the
    register, row and field it is in."""

    code: str
    rule: str
    locator: dict
    detail: str
    intent: str = ""

    def __str__(self) -> str:
        at = " ".join(str(v) for v in self.locator.values() if v is not None)
        return f"[{self.code}] {at}: {self.detail}"


@dataclass
class Verdict:
    verdict: str
    seed: str
    rules_evaluated: int
    findings: list[Finding] = field(default_factory=list)

    @property
    def admissible(self) -> bool:
        return self.verdict == ADMISSIBLE

    def as_dict(self) -> dict:
        return {
            "verdict": self.verdict,
            "seed": self.seed,
            "rules_evaluated": self.rules_evaluated,
            "findings": [
                {
                    "code": f.code,
                    "rule": f.rule,
                    "locator": f.locator,
                    "detail": f.detail,
                    "intent": f.intent,
                }
                for f in self.findings
            ],
        }


def evaluate(doc: ParsedDocument, rules: list[Rule]) -> Verdict:
    """Apply a phase's declared rule set to an already-read document.

    The rule set is always supplied — the oracle is generic across phases and has no default. A
    default would silently judge a P1 register against P0's rules and report a confident verdict
    about the wrong thing.

    Every rule is evaluated; there is no short-circuit on first failure. An author needs the whole
    finding set, and a rule that never runs is a rule that cannot be trusted.
    """
    declared = rules
    findings: list[Finding] = []

    for rule in declared:
        # dispatch() fails hard on an unknown kind: a skipped rule reports green over an
        # unevaluated subject, which is exactly the vacuity failure the oracle exists to catch.
        for at, detail in dispatch(rule.check)(doc, rule):
            findings.append(Finding(code=rule.id, rule=rule.identity, locator=place(rule, at),
                                    detail=detail, intent=rule.intent))

    return Verdict(
        verdict=INADMISSIBLE if findings else ADMISSIBLE,
        seed=str(doc.path),
        rules_evaluated=len(declared),
        findings=findings,
    )


