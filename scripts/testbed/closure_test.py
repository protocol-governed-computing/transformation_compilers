"""Closure — the rule sets against the governance they realise.

`meta_test` asserts that every rule can run. This asserts what the rules are for: every rule names
an invariant in force or a statement of DESIGN_LANGUAGE, every design invariant is realised by some
rule, and every template names exactly its schema's registers and columns.

Run:  python scripts/testbed/closure_test.py [snapshot_root]
Exit: 0 when the rule sets close, 1 otherwise.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

from transformation.design.meta import DESIGN_CONSTITUTION, closure
from transformation.design.rule_sets import RULE_SETS


def main(argv: list[str]) -> int:
    snapshot = argv[1] if len(argv) > 1 else str(REPO.parent / "snapshot")
    findings = closure(RULE_SETS, snapshot)
    if not findings:
        print(f"CLOSURE PASSED — {len(RULE_SETS)} phase(s) close over {DESIGN_CONSTITUTION} "
              f"and DESIGN_LANGUAGE, and every template agrees with its schema")
        return 0
    for finding in findings:
        print(f"  {finding.code}  {finding.where}")
        print(f"      {finding.detail}")
    print(f"\nCLOSURE FAILED — {len(findings)} finding(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
