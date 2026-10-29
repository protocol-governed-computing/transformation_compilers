"""The derive route is sealed whole, and a route no seal records derives nothing (readiness 3.6).

Each case alters what the seal reads, never the package: the digest of one building block, the set
of files, or the seal's dossier. The route as it stands must be the one a seal records.

Run:  python scripts/testbed/route_seal_test.py
Exit: 0 when every case passes, 1 otherwise.
"""
import sys
from pathlib import Path
from unittest import mock

from transformation.design.derive import seal
from transformation.design.derive.compose import derive

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
LEDGER = REPO / "testbed" / "ledgers" / "blockchain" / "ledger.yaml"
BASELINE = next((WORKSPACE / "business_domains" / "blockchain" / "design").glob("p7_*.md"))


def test_the_route_as_it_stands_is_sealed_by_a_dossier():
    assert seal.route_unsealed() is None, seal.route_unsealed()
    judged = seal.judged_by()["route"]
    assert judged["revision"] in {s["dossier"] for s in seal.seals()}, judged
    assert seal.unsealed_dossiers() == [], seal.unsealed_dossiers()


def test_a_changed_building_block_refuses_every_derivation():
    changed = {**seal.route_now(), "compose.py": "sha256:" + "0" * 64}
    with mock.patch.object(seal, "route_now", lambda: changed):
        why = seal.route_unsealed()
        assert why and "compose.py differs" in why and "outside a dossier" in why, why
        try:
            derive(LEDGER, BASELINE)
        except seal.Unsealed as exc:
            assert "outside a dossier" in str(exc), exc
        else:
            raise AssertionError("a derivation ran under a route no seal records")


def test_an_added_module_is_a_route_change():
    added = {**seal.route_now(), "new_block.py": "sha256:" + "1" * 64}
    with mock.patch.object(seal, "route_now", lambda: added):
        assert "new_block.py" in (seal.route_unsealed() or ""), seal.route_unsealed()


def test_a_seal_whose_dossier_says_nothing_is_refused():
    missing = [{**seal.seals()[-1], "dossier": "no_such_dossier"}]
    with mock.patch.object(seal, "seals", lambda: missing):
        assert seal.unsealed_dossiers() == ["seal of dossiers/no_such_dossier: the dossier has no change.md"], \
            seal.unsealed_dossiers()


def test_a_route_a_seal_already_records_is_not_sealed_again():
    try:
        seal.record_seal("derive_route_sealed", "again", {})
    except seal.Unsealed as exc:
        assert "already records" in str(exc), exc
    else:
        raise AssertionError("the same route was sealed twice")


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
