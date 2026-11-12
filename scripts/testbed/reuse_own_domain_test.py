"""A change may reuse its own domain's artifacts, whatever plane the domain serves (P3 revision 2).

P3 offers a change reuse candidates only from a domain that permits reuse: `business` or
`substrate`. A change to a platform domain could not record reusing that domain's own artifacts,
which are its own to change. The rule now declares `own_domain`, and the change's own domain is
eligible.

Each case judges the analysis of `dossiers/route_change_judged_by_phases` with one authoring
decision added, against the working snapshot, by the rule set sealed there:

- the transformation domain reusing its own seed-judging workflow is admitted;
- the same decision in a business domain's change is refused, as before;
- the transformation domain reusing another platform domain's artifact is refused, as before.

Run:  python scripts/testbed/reuse_own_domain_test.py
Exit: 0 when every case passes, 1 otherwise.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SNAPSHOT = REPO.parent / "snapshot"
DOSSIER = REPO / "dossiers" / "route_change_judged_by_phases"
P2 = DOSSIER / "p2_domain_model_transformation_design_v0.md"
P3 = DOSSIER / "p3_analysis_loop_transformation_design_v0.md"
REUSE = '''  - capability: Judging a seed, as the seal calls it
    decision: REUSE
    rationale: The seal judges a route change's seed as any seed is judged.
    alternatives_checked: {candidate} satisfies it as-is.
    source_finding: {{phase: p2, register: pps_baseline_fqdns, row: 1}}
'''


def judged(candidate: str, domain: str = "transformation") -> list[str]:
    """The finding codes P3 reports with one REUSE decision citing `candidate`."""
    text = P3.read_text(encoding="utf-8")
    text = text.replace("  placement_decision:\n", REUSE.format(candidate=candidate) + "  placement_decision:\n", 1)
    text = text.replace("  domain: transformation\n", f"  domain: {domain}\n", 1)
    prior = P2.read_text(encoding="utf-8").replace("  domain: transformation\n", f"  domain: {domain}\n", 1)
    tmp = Path(tempfile.mkdtemp(prefix="pgc_reuse_own_domain_"))
    try:
        (tmp / P3.name).write_text(text, encoding="utf-8")
        (tmp / P2.name).write_text(prior, encoding="utf-8")
        run = subprocess.run(["tc", "phase", "check", str(tmp / P3.name), "--phase", "p3", "--snapshot",
                              str(SNAPSHOT), "--prior", f"p2={tmp / P2.name}", "--json"],
                             capture_output=True, text=True)
        return [f["code"] for f in json.loads(run.stdout)["findings"]]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_a_platform_change_may_reuse_its_own_domains_artifact():
    codes = judged("transformation::WF_P0_SEED_ADMISSIBILITY_V0")
    assert codes == [], codes


def test_a_business_change_may_not_reuse_a_platform_service():
    codes = judged("transformation::WF_P0_SEED_ADMISSIBILITY_V0", domain="book_library_mgmt")
    assert "REUSE_CANDIDATE_NOT_ELIGIBLE" in codes, codes


def test_a_platform_change_may_not_reuse_another_platform_domain():
    codes = judged("inspection::TE_SI_ARTIFACT_LIST_V0")
    assert codes == ["REUSE_CANDIDATE_NOT_ELIGIBLE"], codes


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except Exception as exc:  # report every test, then fail the run
            failed += 1
            print(f"  FAIL  {name}: {exc!r}"[:600])
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
