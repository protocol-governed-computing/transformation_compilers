"""The seed declares where a change ends: an authored change is complete at P6 (P0 revision 2).

A change whose deliverable no construction renders — a constitution, an invariant, the derive
route's code — has no design intent. Its seed says so in the `delivery` register, the verdict at P6
reads it, and P7 refuses a design intent for it. A seed that declares nothing is judged as before.

Each case judges a copy of a dossier with the seed's `delivery` register set, against the working
snapshot, by the rule set sealed there:

- an authored seed makes an admissible P6 complete, with no next phase;
- a constructed seed, or one that declares nothing, sends an admissible P6 on to P7;
- a seed declaring delivery twice is refused;
- P7 refuses a design intent whose seed declares the change authored, and only then.

Run:  python scripts/testbed/delivery_declared_test.py
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
AUTHORED = REPO.parent / "software_governance" / "dossiers" / "complete_at_governance_intent"
CATALOG = REPO / "scripts" / "testbed" / "fixtures" / "catalog" / "cr_01_catalog"


def _doc(dossier: Path, phase: str) -> Path:
    return next(p for p in dossier.glob(f"{phase}_*.md") if "business_problem" not in p.name)


def _seed(dossier: Path, tmp: Path, rows: list[str] | None) -> Path:
    """A copy of the dossier's seed, its `delivery` register holding `rows`, or absent for None."""
    text = _doc(dossier, "p0").read_text(encoding="utf-8")
    if rows is not None:
        close = text.index("\n```\n", text.index("registers:"))
        block = "\n  delivery:" + "".join(f"\n  - mode: {mode}\n    rationale: Stated for the test." for mode in rows)
        text = text[:close] + block + text[close:]
    out = tmp / "p0_seed.md"
    out.write_text(text, encoding="utf-8")
    return out


def judged(dossier: Path, phase: str, delivery: list[str] | None, priors: tuple[str, ...]) -> dict:
    """The JSON verdict on the dossier's `phase` document, its seed declaring `delivery`."""
    tmp = Path(tempfile.mkdtemp(prefix="pgc_delivery_declared_"))
    try:
        seed = _seed(dossier, tmp, delivery)
        args = ["tc", "phase", "check", str(seed if phase == "p0" else _doc(dossier, phase)), "--phase", phase,
                "--snapshot", str(SNAPSHOT), "--json"]
        for prior in priors:
            args += ["--prior", f"{prior}={seed if prior == 'p0' else _doc(dossier, prior)}"]
        run = subprocess.run(args, capture_output=True, text=True)
        return json.loads(run.stdout)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _codes(verdict: dict) -> list[str]:
    return [f["code"] for f in verdict["findings"]]


def test_an_authored_seed_makes_governance_intent_complete():
    verdict = judged(AUTHORED, "p6", ["AUTHORED"], ("p5", "p0"))
    assert verdict["verdict"] == "ADMISSIBLE", _codes(verdict)
    assert (verdict["delivery"], verdict["next_phase"]) == ("AUTHORED", None), verdict


def test_a_constructed_seed_goes_on_to_design_intent():
    verdict = judged(AUTHORED, "p6", ["CONSTRUCTED"], ("p5", "p0"))
    assert (verdict["delivery"], verdict["next_phase"]) == ("CONSTRUCTED", "p7"), verdict


def test_a_seed_that_declares_nothing_is_judged_as_before():
    seed = judged(AUTHORED, "p0", None, ())
    assert seed["verdict"] == "ADMISSIBLE", _codes(seed)
    verdict = judged(AUTHORED, "p6", None, ("p5", "p0"))
    assert (verdict["delivery"], verdict["next_phase"]) == (None, "p7"), verdict


def test_a_seed_declaring_delivery_twice_is_refused():
    codes = _codes(judged(AUTHORED, "p0", ["AUTHORED", "CONSTRUCTED"], ()))
    assert codes == ["DELIVERY_NOT_SINGULAR"], codes


def test_design_intent_refuses_an_authored_change_and_only_it():
    priors = ("p5", "p6", "p0")
    authored = _codes(judged(CATALOG, "p7", ["AUTHORED"], priors))
    constructed = _codes(judged(CATALOG, "p7", ["CONSTRUCTED"], priors))
    assert "AUTHORED_CHANGE_HAS_DESIGN" not in constructed, constructed
    assert sorted(authored) == sorted(constructed + ["AUTHORED_CHANGE_HAS_DESIGN"]), (authored, constructed)


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
