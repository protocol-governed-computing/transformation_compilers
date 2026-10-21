"""Write every designed root's design of record, or check that each is current.

    python scripts/write_baseline_designs.py           write <root>/design/ for every root
    python scripts/write_baseline_designs.py --check   exit 1 if any design differs or is incomplete

A design of record is generated from its registry, so a registry changed without its design is
stale. `--check` regenerates each design aside and compares it with the one on disk.

It also measures each design as construction does. A design of record must determine its whole
registry: below 100%, construction could not rebuild the registry from it, and a change designed
against that baseline would start from a design that is not the system. This held as a condition of
the v6 baseline and nothing measured it, so two designs sat below 100% unnoticed.
"""
from __future__ import annotations

import json
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

    incomplete = 0
    for root in ROOTS:
        measured = subprocess.run(
            [sys.executable, "-m", "transformation", "construction", "check", str(root / "design"),
             "--root", str(root), "--json"],
            capture_output=True, text=True)
        result = json.loads(measured.stdout)
        whole = (result["completeness"] == 100.0 and not result["disagreeing"]
                 and not result["pending"])
        print(f"  {'OK     ' if whole else 'GAP    '}{(root / 'design').relative_to(WORKSPACE)}  "
              f"{result['determined']}/{result['required']}"
              + ("" if whole else f"  {dict(result['undetermined'])}"))
        incomplete += not whole
    print(f"\n  BASELINE DESIGNS {'COMPLETE' if not incomplete else 'INCOMPLETE'} — "
          f"{len(ROOTS) - incomplete}/{len(ROOTS)} determine their registry")
    return 1 if stale or incomplete else 0


if __name__ == "__main__":
    raise SystemExit(main())
