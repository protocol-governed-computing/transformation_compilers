"""Write every designed root's design of record, or check that each is current.

    python scripts/write_baseline_designs.py           write <root>/design/ for every root
    python scripts/write_baseline_designs.py --check   exit 1 if any written design differs

A design of record is generated from its registry, so a registry changed without its design is
stale. `--check` regenerates each design aside and compares it with the one on disk.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

from transformation.record import inventory

REPO = Path(__file__).resolve().parents[1]
WORKSPACE = REPO.parent
ROOTS = (
    WORKSPACE / "business_domains/ai_governance",
    WORKSPACE / "business_domains/blockchain",
    WORKSPACE / "business_domains/book_library_mgmt",
    WORKSPACE / "business_domains/causal_language_model",
    WORKSPACE / "conformance_workloads/workloads/collatz",
    REPO,
)
# Artifacts a generator produces, per root: the phase workflows and the judging contracts carry the
# rule sets `emit_rule_sets` seals into them.
GENERATED = {REPO: ("transformation.design.emit:emit_rule_sets",
                    re.compile(r"^(WF_P\d_[A-Z_]+|CC_JUDGE_AGAINST_[A-Z_]+)_V\d+$"))}


def write(root: Path, out: Path) -> None:
    args = [sys.executable, "-m", "transformation.record", str(root / "registry"), str(out)]
    if root in GENERATED:
        generator, pattern = GENERATED[root]
        codes = [a["code"] for a in inventory.artifacts(root / "registry") if pattern.match(a["code"])]
        args += ["--generated", generator, *codes]
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL)


def main() -> int:
    if "--check" not in sys.argv[1:]:
        for root in ROOTS:
            write(root, root / "design")
            print(f"  wrote  {(root / 'design').relative_to(WORKSPACE)}")
        return 0
    stale = 0
    for root in ROOTS:
        with tempfile.TemporaryDirectory() as tmp:
            write(root, Path(tmp))
            for fresh in sorted(Path(tmp).glob("*.md")):
                held = root / "design" / fresh.name
                same = held.is_file() and held.read_text(encoding="utf-8") == fresh.read_text(encoding="utf-8")
                print(f"  {'OK     ' if same else 'STALE  '}{held.relative_to(WORKSPACE)}")
                stale += not same
    print(f"\n  BASELINE DESIGNS {'CURRENT' if not stale else 'STALE'} — {stale} stale")
    return 1 if stale else 0


if __name__ == "__main__":
    raise SystemExit(main())
