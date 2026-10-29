"""Delivery repoints callers outside the domain, and refuses the ones it cannot.

Each case builds a small workspace in a temporary directory: two repositories, a delivered domain and
the files that name it. Nothing in the real workspace is read or written.

Run:  python scripts/testbed/repoint_callers_test.py
Exit: 0 when every case passes, 1 otherwise.
"""
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import repoint_callers as rc  # noqa: E402

DOMAIN = "shop"
GENERATED = {"_identity": {"superseded": {"shop::WF_PAY_V0": "shop::WF_PAY_V1"},
                           "replaced": {"shop::WF_OLD_CHECKOUT_V0": "shop::WF_CHECKOUT_V0"},
                           "retired": ["shop::CC_LEGACY_TAX_V0"]}}


MADE: list[Path] = []


def workspace(files: dict[str, str]) -> Path:
    root = Path(tempfile.mkdtemp(prefix="pgc_repoint_"))
    MADE.append(root)
    for repo in ("platform", "business_domains"):
        (root / repo / ".git").mkdir(parents=True)
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text)
    return root


def test_a_caller_outside_the_domain_follows_each_successor():
    w = workspace({
        "platform/testbed/test_pay.py": 'WF = "WF_PAY_V0"  # shop\nrun("shop::WF_OLD_CHECKOUT_V0")\n',
        "platform/scripts/testbed/corpus/fixture.md": "node: shop::WF_PAY_V0\n",
    })
    assert rc.check(w, DOMAIN, GENERATED) == []
    touched = rc.apply(w, DOMAIN, GENERATED)
    assert sorted(touched) == ["platform/scripts/testbed/corpus/fixture.md", "platform/testbed/test_pay.py"], touched
    assert (w / "platform/testbed/test_pay.py").read_text() == 'WF = "WF_PAY_V1"  # shop\nrun("shop::WF_CHECKOUT_V0")\n'
    assert (w / "platform/scripts/testbed/corpus/fixture.md").read_text() == "node: shop::WF_PAY_V1\n"


def test_a_short_name_is_followed_only_where_the_file_names_the_domain():
    w = workspace({"platform/testbed/other.py": 'WF = "WF_PAY_V0"  # another domain\'s act of that name\n'})
    assert rc.apply(w, DOMAIN, GENERATED) == []


def test_history_is_never_rewritten():
    files = {"platform/doc/FINDINGS.md": "shop::WF_PAY_V0 was slow\n",
             "platform/dossiers/change/p7_design_intent_x.md": "shop::WF_PAY_V0\n",
             "business_domains/other/cr_dossiers/cr_01_x/ledger.yaml": "uses: shop::WF_PAY_V0\n",
             "platform/design/p7_design_intent_platform_baseline.md": "shop::WF_PAY_V0\n",
             "platform/process/retired_identities.yaml": "identity: shop::WF_PAY_V0\n"}
    w = workspace(files)
    assert rc.apply(w, DOMAIN, GENERATED) == []
    assert all((w / rel).read_text() == text for rel, text in files.items())


def test_the_domain_itself_is_left_to_delivery():
    w = workspace({"business_domains/shop/testbed/t.py": "shop::WF_PAY_V0\n"})
    assert rc.apply(w, DOMAIN, GENERATED) == []


def test_a_caller_of_a_retired_artifact_refuses_the_delivery():
    w = workspace({"platform/testbed/test_tax.py": 'run("shop::CC_LEGACY_TAX_V0")\n'})
    assert rc.check(w, DOMAIN, GENERATED) == [
        "platform/testbed/test_tax.py names shop::CC_LEGACY_TAX_V0, which this change retires with no successor"]


def test_another_domains_declaration_refuses_the_delivery():
    w = workspace({"business_domains/other/registry/part/workflows/WF_X_V0.md": "next: shop::WF_PAY_V0\n"})
    problems = rc.check(w, DOMAIN, GENERATED)
    assert len(problems) == 1 and "another domain's declaration" in problems[0], problems
    assert rc.apply(w, DOMAIN, GENERATED) == []


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
        finally:
            while MADE:
                shutil.rmtree(MADE.pop(), ignore_errors=True)
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
