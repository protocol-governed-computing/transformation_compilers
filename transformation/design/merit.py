"""Figure of merit — a deterministic rating of a phase document.

Begin at the maximum, subtract for named defects, clamp, and report the reasons alongside the
number.

**This module holds no policy.** What is deducted and by how much is declared in
`transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1` and read from the composition. That split is
the same one the phases themselves obey — a rule set is governance and lives in the snapshot, a
check kind is a mechanism and may live in code. Weights in Python would make the quality bar a
property of a build tool: unversioned, unreadable from the composition, changeable without a
governed act.

**The rating is not the verdict.** Admissibility is decided by the rule set alone. The two axes are
independent in both directions: an admissible document can rate poorly for carrying declared open
questions, and an inadmissible one can rate well when a single misspelled citation is fatal to
admissibility but cheap in quality.

Without a composition there is no policy, and therefore no rating — reported as *not computed*,
never as a default. A figure of merit invented from a built-in fallback would look exactly like one
read from governance, which is the failure the phases' own grounding rules avoid by refusing to
pass quietly when they could not check.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from transformation.design.schema import column_key
from transformation.design.evaluate import ParsedDocument
from transformation.design.oracle import Verdict

POLICY_ARTIFACT = "transformation::STRUCTURE_FIGURE_OF_MERIT_POLICY_V1"


class PolicyUnavailable(RuntimeError):
    """The composition does not publish a figure-of-merit policy."""


class PolicyAbsent(PolicyUnavailable):
    """The composition holds no policy. Transformation's own founding change is grounded against a
    composition without transformation, and so without the policy: the rating is not computed."""


@dataclass(frozen=True)
class Deduction:
    """One declared deduction that actually fired, and what tripped it."""

    id: str
    label: str
    weight: int
    count: int

    def __str__(self) -> str:
        return f"-{self.weight} {self.label} ({self.count})"


@dataclass(frozen=True)
class Merit:
    """A rating and the reasons for it — never a bare number.

    The breakdown is the useful half: a star count says an artifact could be better, and the
    deductions say exactly how.
    """

    rating: int
    maximum: int
    deductions: list[Deduction]

    @property
    def stars(self) -> str:
        return "★" * self.rating + "☆" * (self.maximum - self.rating)


def load_policy(snapshot_root: str) -> dict[str, Any]:
    """Read the declared policy from the composition. Absence is fail-hard, never a default."""
    from inspector import api

    status, artifact = api.query("si.artifact.show", {"artifact": POLICY_ARTIFACT}, snapshot_root)
    if status == "NOT_FOUND":
        raise PolicyAbsent(f"{POLICY_ARTIFACT} is not in {snapshot_root}")
    if status != "SUCCESS":
        raise PolicyUnavailable(f"{POLICY_ARTIFACT} not readable from {snapshot_root}: {status}")
    core = ((artifact.get("canonical") or {}).get("frontmatter") or {}).get("core") or {}
    if not core.get("deductions"):
        raise PolicyUnavailable(f"{POLICY_ARTIFACT} declares no deductions")
    return core


def _row_hits(doc: ParsedDocument, spec: dict[str, Any]) -> int:
    """Rows the document itself declares as unresolved, per the policy's row selector."""
    hits = 0
    hole_registers = tuple(spec.get("registers") or ())
    columns = {column_key(k): {str(v).strip() for v in vals}
               for k, vals in (spec.get("columns") or {}).items()}

    for register in hole_registers:
        block = doc.register(register)
        if block is None or block.table is None:
            continue
        # A register declared empty is a considered answer, not an open question, and holds no rows.
        hits += sum(1 for row in block.table.rows
                    if any(str(v).strip() for v in row.values() if v is not None))

    for entry in doc.registers:
        block = doc.register(entry["id"] if isinstance(entry, dict) else entry.id)
        if block is None or block.table is None:
            continue
        for row in block.table.rows:
            for key, value in row.items():
                if key in columns and isinstance(value, str) and value.strip() in columns[key]:
                    hits += 1
    return hits


def rate(verdict: Verdict, doc: ParsedDocument | None, policy: dict[str, Any]) -> Merit:
    """Apply a declared policy to a judged document. Pure arithmetic — no policy of its own."""
    maximum = int(policy.get("maximum", 5))
    minimum = int(policy.get("minimum", 0))

    if doc is None:
        return Merit(rating=minimum, maximum=maximum, deductions=[])

    fired = [f.code for f in verdict.findings]
    claimed: set[int] = set()
    deductions: list[Deduction] = []
    remaining_spec = None

    for spec in policy["deductions"]:
        if spec.get("remaining_findings"):
            remaining_spec = spec           # evaluated last, over whatever no rule claimed
            continue
        count = 0
        if spec.get("findings"):
            named = set(spec["findings"])
            for i, rule in enumerate(fired):
                if rule in named:
                    claimed.add(i)
                    count += 1
        if spec.get("rows"):
            count += _row_hits(doc, spec["rows"])
        if count:
            deductions.append(
                Deduction(spec["id"], spec.get("label", spec["id"]), int(spec["weight"]), count)
            )

    if remaining_spec is not None:
        count = len(fired) - len(claimed)
        if count:
            deductions.append(Deduction(
                remaining_spec["id"],
                remaining_spec.get("label", remaining_spec["id"]),
                int(remaining_spec["weight"]),
                count,
            ))

    score = maximum - sum(d.weight for d in deductions)
    return Merit(rating=max(minimum, min(maximum, score)), maximum=maximum, deductions=deductions)
