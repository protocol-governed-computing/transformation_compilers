"""Meta-validation suite — the rule sets themselves, before any suite judges a document.

Every other suite in this directory asserts a verdict over a document. A verdict is only evidence
if the rules that produced it could all run: a rule naming a check kind that no longer exists, or
omitting a parameter that check requires on every path, does not fail loudly at the top of a run —
it fails, or silently contributes nothing, at whatever moment a document happens to reach it. A
suite that never authored such a document passes while proving less than it reports.

So this runs first and it is a gate, not a report. `assert_consistent()` is called at the head of
each suite that evaluates rule sets, which is why this file is importable as well as runnable.

Run:  python scripts/testbed/meta_test.py
Exit: 0 if the declaration/enforcement correspondence holds, 1 otherwise.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from transformation.design.evaluate import kinds as check_kinds
from transformation.design.meta import verify
from transformation.design.rule_sets import RULE_SETS


def report() -> int:
    """Print the meta verdict. Returns the process exit code."""
    findings = verify(RULE_SETS)
    examined = sum(len(module.rule_set()) for module in RULE_SETS.values())

    print(
        f"meta — {examined} rule(s) across {len(RULE_SETS)} phase(s) "
        f"against {len(check_kinds())} check kind(s)\n"
    )

    if not findings:
        print("META PASSED — every declared rule resolves, every mechanism is declared")
        return 0

    for finding in findings:
        print(f"  {finding.code}  {finding.where}")
        print(f"      {finding.detail}")
    print(f"\nMETA FAILED — {len(findings)} correspondence defect(s)")
    return 1


def assert_consistent() -> None:
    """Refuse to run a document suite over rule sets that do not hold together.

    Fail-hard rather than a warning: a suite that proceeds past this reports verdicts it cannot
    stand behind, and a green run is then indistinguishable from an unevaluated one.
    """
    findings = verify(RULE_SETS)
    if findings:
        print("META FAILED — rule sets are inconsistent; no verdict over a document is evidence\n")
        for finding in findings:
            print(f"  {finding.code}  {finding.where}")
            print(f"      {finding.detail}")
        print("\n  run: tc phase meta")
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(report())
