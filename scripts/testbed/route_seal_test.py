"""The derive route is sealed whole, and a route no seal records derives nothing (readiness 3.6).

Each case alters what the seal reads, never the package: the digest of one building block, the set
of files, or the seals. The route as it stands must be the one a seal records, and once a seal is
judged by the phases, every later one must be, with every phase document in its dossier.

Run:  python scripts/testbed/route_seal_test.py
Exit: 0 when every case passes, 1 otherwise.
"""
import json
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
    unjudged = {k: v for k, v in seal.seals()[-1].items() if k not in ("phases", "pinned")}
    missing = [{**unjudged, "dossier": "no_such_dossier"}]
    with mock.patch.object(seal, "seals", lambda: missing):
        assert seal.unsealed_dossiers() == ["seal of dossiers/no_such_dossier: the dossier has no change.md"], \
            seal.unsealed_dossiers()


def test_a_seal_without_verdicts_after_one_with_them_is_refused():
    judged = next(s for s in seal.seals() if s.get("phases"))
    unjudged = {k: v for k, v in judged.items() if k not in ("phases", "pinned")}
    with mock.patch.object(seal, "seals", lambda: [judged, {**unjudged, "dossier": "derive_route_sealed"}]):
        assert any("no phase verdicts, after a seal judged by the phases" in p for p in seal.unsealed_dossiers()), \
            seal.unsealed_dossiers()


def test_a_judged_seal_whose_dossier_lacks_a_phase_document_is_refused():
    judged = next(s for s in seal.seals() if s.get("phases"))
    with mock.patch.object(seal, "seals", lambda: [{**judged, "dossier": "derive_route_sealed"}]):
        assert seal.unsealed_dossiers() == [
            "seal of dossiers/derive_route_sealed: the dossier has no p0, p1, p2, p3, p4, p5, p6 document"], \
            seal.unsealed_dossiers()


def test_each_phase_is_judged_against_the_priors_its_schema_declares():
    for phase, priors in seal.PRIORS.items():
        schema = json.loads((REPO / "registry" / "schema" / f"REGISTER_SCHEMA_{phase.upper()}_V0.json").read_text())
        assert priors == (schema.get("x-priors") or []), (phase, priors, schema.get("x-priors"))


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
