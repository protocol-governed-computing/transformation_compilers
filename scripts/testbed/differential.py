"""Differential conformance — the genesis oracle against each compiled phase.

The rehost claim is that authoring P0 as governed artifacts preserved its behaviour. That is only
evidence if both paths are actually exercised over the same seeds and compared:

    genesis oracle    rules expanded from the register schema   (working tree)
    compiled phase    rules from the sealed snapshot        (si.artifact.show)

The rule sets must be identical and the verdicts must agree, seed by seed and finding by finding.
Divergence is a defect in one of them, and this script says which seeds expose it.

Run:  python scripts/testbed/differential.py [snapshot_root]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from inspector import api

from transformation.implementation.capability_transforms.atoms import (
    ct_pure_evaluate_rules_v0,
    ct_pure_parse_prior_phases_v0,
    ct_pure_parse_registers_v0,
)
from transformation.design.oracle import evaluate
from transformation.design.read import read_seed
# One implementation, shared with `tc phase check`. Two readers of the sealed rule set
# would be two answers to "what judged this document".
from transformation.design.rule_sets import RULE_SETS
from transformation.design.sealed import sealed_rule_set
from transformation.design.emit import workflow_fqdn

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent

# Fixtures maintained against the current rule set. See `fixtures/README.md`.
CR_01 = REPO / "scripts/testbed/fixtures/catalog/cr_01_catalog"
# CR-3 is the only design in the corpus that announces anything, so it is the only one the
# emission guard and the governance-surface discharge can be probed against.
CR_03 = REPO / "scripts/testbed/fixtures/catalog/cr_03_catalog"

# A CR's dossier grounds against the composition it was designed against; judged against the live
# one, the P7/P8 documents report collisions with their own output — true, and uninformative about
# the two paths. Reproduced through `e2e_phases_test.design_baseline()` rather than checked for
# existence: a cached baseline whose sources have since been recompiled is stale, and a stale
# baseline seals a rule set the declaration has already moved past.
from e2e_phases_test import design_baseline
from meta_test import assert_consistent

# Each phase: its workflow, its declared rule set, and the corpus it judges. A phase added here
# without a corpus would report "identical rule sets" and prove nothing about behaviour, so the
# corpus is part of the declaration rather than discovered.
PHASES = {
    "P0": {
        "wf": workflow_fqdn("p0"),
        "rules": RULE_SETS["p0"].rule_set,
        "corpus": [
            REPO / "scripts/testbed/fixtures/transformation/founding_design_bootstrap/p0_seed_transformation_phases_v0.md",
            CR_01 / "p0_seed_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus").glob("*.md")),
        ],
    },
    "P1": {
        "wf": workflow_fqdn("p1"),
        "rules": RULE_SETS["p1"].rule_set,
        "corpus": [
            REPO / "scripts/testbed/fixtures/transformation/founding_design_bootstrap/p1_change_request_transformation_phases_v0.md",
            CR_01 / "p1_change_request_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p1").glob("*.md")),
        ],
    },
    "P2": {
        "wf": workflow_fqdn("p2"),
        "rules": RULE_SETS["p2"].rule_set,
        # P2 grounds claims against the composition, so the differential must supply the same
        # observation the compiled workflow gathers. Comparing two ungrounded runs would agree
        # perfectly while exercising none of the grounding.
        "observes": {"si.artifact.list": "artifacts"},
        # Cross-phase rules read an upstream document, and which one is a property of the
        "corpus": [
            REPO / "scripts/testbed/fixtures/transformation/founding_design_bootstrap/p2_domain_model_transformation_phases_v0.md",
            CR_01 / "p2_domain_model_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p2").glob("*.md")),
        ],
    },
    "P3": {
        "wf": workflow_fqdn("p3"),
        "rules": RULE_SETS["p3"].rule_set,
        # Two observations, answering different questions: does this identity exist, and may this
        # domain be drawn on at all. A differential that supplied only the first would agree with
        # itself perfectly while leaving the reuse ruling unexercised.
        "observes": {"si.artifact.list": "artifacts", "si.snapshot.summary": "reuse_visibility"},
        "corpus": [
            CR_01 / "p3_analysis_loop_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p3").glob("*.md")),
        ],
    },
    "P4": {
        "wf": workflow_fqdn("p4"),
        "rules": RULE_SETS["p4"].rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "corpus": [
            CR_01 / "p4_business_model_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p4").glob("*.md")),
        ],
    },
    "P5": {
        "wf": workflow_fqdn("p5"),
        "rules": RULE_SETS["p5"].rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "corpus": [
            CR_01 / "p5_business_intent_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p5").glob("*.md")),
        ],
    },
    "P6": {
        "wf": workflow_fqdn("p6"),
        "rules": RULE_SETS["p6"].rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "corpus": [
            CR_01 / "p6_governance_intent_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p6").glob("*.md")),
        ],
    },
    "P7": {
        "wf": workflow_fqdn("p7"),
        "rules": RULE_SETS["p7"].rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "corpus": [
            CR_01 / "p7_design_intent_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p7").glob("*.md")),
        ],
    },
    "P8": {
        "wf": workflow_fqdn("p8"),
        "rules": RULE_SETS["p8"].rule_set,
        "observes": {"si.artifact.list": "artifacts"},
        "corpus": [
            CR_01 / "p8_authoring_mandate_book_library_mgmt_catalog_v0.md",
            *sorted((REPO / "scripts/testbed/corpus_p8").glob("*.md")),
        ],
    },
}


def observation(operations: dict | None, snapshot_root: str) -> dict:
    """The facts a grounding phase's workflow gathers, keyed by the operation that produced them.

    `operations` maps operation → the key its result carries rows under, because a phase may ground
    against more than one surface and they do not answer in the same shape.
    """
    gathered = {}
    for operation, result_key in (operations or {}).items():
        status, result = api.query(operation, {}, snapshot_root)
        if status != "SUCCESS":
            raise RuntimeError(f"{operation} failed against {snapshot_root}: {status}")
        gathered[operation] = result.get(result_key, result)
    return gathered


# Which upstream document each judged document is handed — **derived, not restated**.
#
# This was a literal table: every corpus document, every prior it reads, by hand. It was wrong twice
# in one session. `scripts/testbed/priors.py` now derives it from the phase's declared `PRIORS` and
# the document's own `cr` header field, and both this harness and the payload builder read it from there
# rather than each keeping a copy.

sys.path.insert(0, str(Path(__file__).resolve().parent))
from priors import prior_paths   # noqa: E402


def prior_texts(doc_path: Path, declared_priors: tuple[str, ...]) -> dict:
    """The upstream documents this document is judged against, as text a workflow is handed."""
    return {
        phase_id: path.read_text(encoding="utf-8")
        for phase_id, path in prior_paths(doc_path, declared_priors).items()
    }


def compiled_verdict(
    seed_text: str,
    rules: list[dict],
    observed: dict | None = None,
    priors: dict | None = None,
) -> tuple[str, list[tuple[str, ...]]]:
    """Drive the compiled phase's atoms exactly as the workflow composes them."""
    parsed = ct_pure_parse_registers_v0.execute({"document_text": seed_text})
    parsed_priors = ct_pure_parse_prior_phases_v0.execute({"prior_texts": priors or {}})
    result = ct_pure_evaluate_rules_v0.execute(
        {
            "header": parsed["header"],
            "sections": parsed["sections"],
            "registers": parsed["registers"],
            "document_text": seed_text,
            "rule_set": rules,
            "observed": observed or {},
            "priors": parsed_priors["priors"],
        }
    )
    findings = [(f["code"], f["rule"], *map(str, f["locator"].values())) for f in result["findings"]]
    return result["verdict"], findings


def genesis_verdict(
    doc_path: Path,
    rules,
    observed: dict | None = None,
    priors: dict | None = None,
) -> tuple[str, list[tuple[str, ...]]]:
    doc = read_seed(doc_path)
    doc.observed = observed or {}
    # The genesis path parses its priors with the same reader the transform uses, so a divergence
    # is a difference in rule evaluation rather than in how the two paths read a document.
    doc.priors = ct_pure_parse_prior_phases_v0.execute({"prior_texts": priors or {}})["priors"]
    verdict = evaluate(doc, rules)
    return verdict.verdict, [(f.code, f.rule, *map(str, f.locator.values())) for f in verdict.findings]


def main() -> int:
    # The rule sets must hold together before either path's verdict is evidence — two paths can
    # agree perfectly on a rule that never ran.
    assert_consistent()
    # The reproduced baseline rather than the workspace snapshot, for the reason this script exists
    # to test: the sealed rule set is read from the composition, and the assembled snapshot at the
    # workspace root is reassembled by hand. It had fallen one rule behind, so P5 reported the
    # sealed set diverging from the declared one — a true statement about a stale snapshot and a
    # false one about the rule set. `design_baseline()` rebuilds when a source domain recompiles.
    snapshot_root = sys.argv[1] if len(sys.argv) > 1 else design_baseline()
    failures = 0
    total = 0

    for phase, spec in PHASES.items():
        # P7 and P8 judge assigned identities against a baseline; the rest are baseline-agnostic.
        root = design_baseline() if phase in ("P7", "P8") else snapshot_root
        sealed = sealed_rule_set(spec["wf"], root)
        declared = spec["rules"]()

        print(f"{phase}  rule sets   sealed={len(sealed)}  declared={len(declared)}")
        if [r["id"] for r in sealed] != [r.id for r in declared]:
            print("  DIVERGENT: the sealed rule set is not the declared one")
            failures += 1
            continue
        print("  identical")

        observed = observation(spec.get("observes"), root)
        # Which phases this one is judged against, read from the schema that declares them rather
        # than from a flag beside the corpus. A phase reads priors exactly when it declares some.
        declared_priors = RULE_SETS[phase.lower()].priors
        corpus = [p for p in spec["corpus"] if p.is_file()]
        if not corpus:
            print(f"  NO DOCUMENTS — a differential over an empty corpus is not evidence")
            failures += 1
            continue

        for doc_path in corpus:
            total += 1
            text = doc_path.read_text(encoding="utf-8")
            priors = prior_texts(doc_path, declared_priors)
            g_verdict, g_findings = genesis_verdict(doc_path, declared, observed, priors)
            c_verdict, c_findings = compiled_verdict(text, sealed, observed, priors)
            agree = g_verdict == c_verdict and sorted(g_findings) == sorted(c_findings)
            print(f"  {'AGREE ' if agree else 'DIVERGE'}  {g_verdict:<12} {len(g_findings):>2} finding(s)  {doc_path.name}")
            if not agree:
                failures += 1
                print(f"           genesis : {g_verdict} {sorted(g_findings)}")
                print(f"           compiled: {c_verdict} {sorted(c_findings)}")
        print()

    if failures:
        print(f"DIFFERENTIAL FAILED — {failures} divergence(s) over {total} document(s)")
        return 1
    print(f"DIFFERENTIAL PASSED — {total} document(s) across {len(PHASES)} phase(s), both paths agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
