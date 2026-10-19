"""The pinned baseline.

Validation runs against a named, frozen snapshot — never "the current snapshot". Every register a
snapshot-reading phase emits encodes facts about one specific composition: which artifacts exist,
what the normative closure contains, what a REUSE decision found. Against a moving snapshot those
fixtures fail for reasons that have nothing to do with the transformation compiler, and a
regression becomes indistinguishable from a rebuild.

So: a run that observes a different snapshot_id fails before any phase executes. Rebaselining is a
deliberate, reviewed act — re-pin the id, re-approve the affected registers.

**Re-approval is the other half of the pin.** Verifying the id proves the composition is the one
named; it proves nothing about whether anyone re-read the registers that encode facts about it. A
register asserting `impacted_count 58` goes false without anyone editing it, and an id alone cannot
tell "re-grounded against this snapshot" from "never re-checked since the id changed". `approved_registers` records the second half, and because it
lives in the file the id lives in, re-pinning drops it: an approval is against one composition and
survives no other.

**Which registers need approving is derived, not declared.** A register rests on a snapshot fact
exactly when a rule governing it consults an observation, which the rule set already says. A
hand-kept list would be a second declaration that drifts from the rules the moment either changes.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Iterable

from inspector import api


class BaselineMismatch(RuntimeError):
    """The snapshot on disk is not the one this CR was validated against."""


@dataclass(frozen=True)
class Baseline:
    snapshot_id: str
    artifact_count: int
    domains: tuple[str, ...]
    # phase -> register -> who re-grounded it against this snapshot_id. Absent on a freshly
    # observed pin, because observing a composition approves nothing about it.
    approved_registers: dict[str, dict[str, str]] = field(default_factory=dict)

    @staticmethod
    def load(path: Path) -> "Baseline":
        if not path.is_file():
            raise FileNotFoundError(f"baseline pin not found: {path}")
        data = json.loads(path.read_text(encoding="utf-8"))
        for key in ("snapshot_id", "artifact_count", "domains"):
            if key not in data:
                raise KeyError(f"baseline pin {path} is missing {key!r}")
        return Baseline(
            snapshot_id=data["snapshot_id"],
            artifact_count=int(data["artifact_count"]),
            domains=tuple(data["domains"]),
            approved_registers={
                phase: dict(registers)
                for phase, registers in (data.get("approved_registers") or {}).items()
            },
        )

    def as_dict(self) -> dict:
        """The pin as it is written. `approved_registers` is omitted when nothing is approved, so
        a freshly observed pin is byte-identical to what `tc baseline show` has always emitted."""
        out: dict = {
            "snapshot_id": self.snapshot_id,
            "artifact_count": self.artifact_count,
            "domains": list(self.domains),
        }
        if self.approved_registers:
            out["approved_registers"] = {
                phase: dict(sorted(registers.items()))
                for phase, registers in sorted(self.approved_registers.items())
            }
        return out

    def approve(self, phase: str, registers: Iterable[str], by: str) -> "Baseline":
        """Record that someone re-grounded these registers against this composition."""
        merged = {p: dict(r) for p, r in self.approved_registers.items()}
        merged.setdefault(phase, {}).update({register: by for register in registers})
        return replace(self, approved_registers=merged)


def grounded_registers(phase: str) -> tuple[str, ...]:
    """The registers of a phase that rest on a snapshot fact, read from its own rule set.

    A rule consulting an observation is the definition: it is the only way a register comes to
    assert something the composition could later contradict. Registers governed only by structural
    or cross-phase rules say nothing about the snapshot and need no re-approval.
    """
    from transformation.design.rule_sets import RULE_SETS

    module = RULE_SETS.get(phase)
    if module is None:
        return ()
    return tuple(sorted({
        rule.register for rule in module.rule_set()
        if rule.register and any(key.endswith("observation") for key in rule.params)
    }))


def pending(pin: Baseline, phase: str) -> tuple[str, ...]:
    """Grounded registers of a phase that nobody has approved against this pin."""
    approved = pin.approved_registers.get(phase, {})
    return tuple(r for r in grounded_registers(phase) if r not in approved)


def observe(snapshot_root: Path) -> Baseline:
    """Read the composition actually present at `snapshot_root`."""
    status, summary = api.query("si.snapshot.summary", {}, str(snapshot_root))
    if status != "SUCCESS":
        raise RuntimeError(f"si.snapshot.summary failed on {snapshot_root}: {status}")
    return Baseline(
        snapshot_id=summary["snapshot_id"],
        artifact_count=int(summary["artifact_count"]),
        domains=tuple(d["domain"] for d in summary.get("domains", [])),
    )


def verify(pin: Baseline, snapshot_root: Path) -> Baseline:
    """Assert the snapshot on disk is the pinned one. Fail hard on any drift."""
    actual = observe(snapshot_root)
    if actual.snapshot_id != pin.snapshot_id:
        raise BaselineMismatch(
            "snapshot does not match the pinned baseline — no phase may run.\n"
            f"  pinned:   {pin.snapshot_id}\n"
            f"  observed: {actual.snapshot_id}\n"
            "Rebaselining is deliberate: re-pin the id and re-approve the affected registers."
        )
    return actual
