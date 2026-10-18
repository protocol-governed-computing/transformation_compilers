"""Regenerate the committed phase test payloads from their source documents.

A payload embeds a whole document as its text, so a hand-edited payload silently drifts from the
document it was copied from. Generating them keeps one source of truth: edit the corpus entry or the
fixture, run this, commit the result.

**One declaration, two derivations.** `PAYLOADS` maps a payload to the document it is cut from, and
that is the only thing stated here. Which key the text travels under follows from the phase; which
priors travel with it is read from `priors.py`, which derives them from the phase's declared `PRIORS`
and the document's own `cr` header field. A hand-kept table in their place would go stale the first
time a probe is added without it.

Run:   python scripts/testbed/build_payloads.py
       python scripts/testbed/build_payloads.py --check
Exit:  0 if every payload was written (or, under --check, already agreed); 1 under --check if any
       differed; 2 on an unrecognised argument, because the default action writes.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "testbed" / "phases" / "test_payloads"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from priors import declared_priors, prior_paths   # noqa: E402

AUTHOR = "bachipeachy"

# The phase a payload exercises, read from its own name. `NN_pX_...` is the form every payload uses.
PHASE_IN_NAME = re.compile(r"^\d+_(p\d)_")

# Payload → the document it is cut from. The fixture dossiers, not the approved ones: a closed change
# request is evidence and is never amended to satisfy a rule written after it was gated, while a
# fixture is maintained against the current rule set on purpose.
PAYLOADS = {
    "01_admissible_seed.json":
        "scripts/testbed/delivered_copies/transformation/dossiers/founding_design_bootstrap/p0_seed_transformation_phases_v0.md",
    "02_admissible_reference.json":
        "scripts/testbed/corpus/admissible_blockchain_reference.md",
    "03_inadmissible_seven_violations.json":
        "scripts/testbed/corpus/inadmissible_seven_violations.md",
    "04_inadmissible_structural.json":
        "scripts/testbed/corpus/inadmissible_structural.md",
    "05_inadmissible_truncated.json":
        "scripts/testbed/corpus/inadmissible_truncated.md",
    "06_p1_admissible_register.json":
        "scripts/testbed/delivered_copies/transformation/dossiers/founding_design_bootstrap/p1_change_request_transformation_phases_v0.md",
    "07_p1_inadmissible_register.json":
        "scripts/testbed/corpus_p1/inadmissible_p1_register.md",
    "08_p2_admissible_register.json":
        "scripts/testbed/delivered_copies/transformation/dossiers/founding_design_bootstrap/p2_domain_model_transformation_phases_v0.md",
    "09_p2_inadmissible_register.json":
        "scripts/testbed/corpus_p2/inadmissible_p2_register.md",
    "10_p0_admissible_catalog_seed.json":
        "scripts/testbed/fixture_dossiers/cr_01_catalog/p0_seed_book_library_mgmt_catalog_v0.md",
    "11_p1_admissible_catalog_register.json":
        "scripts/testbed/fixture_dossiers/cr_01_catalog/p1_change_request_book_library_mgmt_catalog_v0.md",
    "12_p2_admissible_catalog_register.json":
        "scripts/testbed/fixture_dossiers/cr_01_catalog/p2_domain_model_book_library_mgmt_catalog_v0.md",
    "13_p2_inadmissible_catalog_register.json":
        "scripts/testbed/corpus_p2/inadmissible_p2_catalog_register.md",
    "14_p3_admissible_catalog_register.json":
        "scripts/testbed/fixture_dossiers/cr_01_catalog/p3_analysis_loop_book_library_mgmt_catalog_v0.md",
    "15_p3_inadmissible_catalog_register.json":
        "scripts/testbed/corpus_p3/inadmissible_p3_ineligible_reuse.md",
    "16_p4_admissible_catalog_register.json":
        "scripts/testbed/fixture_dossiers/cr_01_catalog/p4_business_model_book_library_mgmt_catalog_v0.md",
    "17_p4_inadmissible_catalog_register.json":
        "scripts/testbed/corpus_p4/inadmissible_p4_broken_consolidation.md",
    "18_p5_admissible_catalog_register.json":
        "scripts/testbed/fixture_dossiers/cr_01_catalog/p5_business_intent_book_library_mgmt_catalog_v0.md",
    "19_p5_inadmissible_catalog_register.json":
        "scripts/testbed/corpus_p5/inadmissible_p5_binding_leak.md",
    "20_p6_admissible_catalog_register.json":
        "scripts/testbed/fixture_dossiers/cr_01_catalog/p6_governance_intent_book_library_mgmt_catalog_v0.md",
    "21_p6_inadmissible_catalog_register.json":
        "scripts/testbed/corpus_p6/inadmissible_p6_unplaced.md",
    "22_p7_admissible_catalog_register.json":
        "scripts/testbed/fixture_dossiers/cr_01_catalog/p7_design_intent_book_library_mgmt_catalog_v0.md",
    "23_p7_inadmissible_catalog_register.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_collision.md",
    "24_p8_admissible_catalog_mandate.json":
        "scripts/testbed/fixture_dossiers/cr_01_catalog/p8_authoring_mandate_book_library_mgmt_catalog_v0.md",
    "25_p8_inadmissible_catalog_mandate.json":
        "scripts/testbed/corpus_p8/inadmissible_p8_broken_order.md",
    "26_p2_inadmissible_dropped_belief.json":
        "scripts/testbed/corpus_p2/inadmissible_p2_dropped_belief.md",
    "27_p3_inadmissible_restated_result.json":
        "scripts/testbed/corpus_p3/inadmissible_p3_restated_result.md",
    "29_p8_inadmissible_undesigned_artifact.json":
        "scripts/testbed/corpus_p8/inadmissible_p8_undesigned_artifact.md",
    "30_p1_inadmissible_dropped_criterion.json":
        "scripts/testbed/corpus_p1/inadmissible_p1_dropped_criterion.md",
    "31_p7_inadmissible_unbound_code.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_unbound_code.md",
    "32_p4_inadmissible_dropped_decision.json":
        "scripts/testbed/corpus_p4/inadmissible_p4_dropped_decision.md",
    "33_p7_inadmissible_dropped_reuse.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_dropped_reuse.md",
    "34_p6_inadmissible_unplaced_scope.json":
        "scripts/testbed/corpus_p6/inadmissible_p6_unplaced_scope.md",
    "35_p8_inadmissible_dropped_artifact.json":
        "scripts/testbed/corpus_p8/inadmissible_p8_dropped_artifact.md",
    "36_p7_inadmissible_unrooted_source.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_unrooted_source.md",
    "37_p7_inadmissible_store_path.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_store_path.md",
    "38_p0_inadmissible_blocking_clarification.json":
        "scripts/testbed/corpus/inadmissible_p0_blocking_clarification.md",
    "39_p7_inadmissible_refusal_unaccounted.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_refusal_unaccounted.md",
    "40_p7_inadmissible_discharge_undeclared.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_discharge_undeclared.md",
    "41_p7_inadmissible_deferral_undeclared.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_deferral_undeclared.md",
    "42_p7_inadmissible_discharge_ungrounded.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_discharge_ungrounded.md",
    "43_p7_inadmissible_discharge_completes.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_discharge_completes.md",
    "44_p7_inadmissible_emission_unknown_ending.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_emission_unknown_ending.md",
    "45_p7_inadmissible_emission_from_refusal.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_emission_from_refusal.md",
    "46_p7_inadmissible_emission_undeclared_event.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_emission_undeclared_event.md",
    "47_p7_inadmissible_governance_undeclared_refusal.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_governance_undeclared_refusal.md",
    "48_p7_inadmissible_governing_rule_unnamed.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_governing_rule_unnamed.md",
    "49_p7_inadmissible_governing_rule_phase.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_governing_rule_phase.md",
    "50_p7_inadmissible_governing_rule_not_in_force.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_governing_rule_not_in_force.md",
    "51_p7_inadmissible_governing_rule_wrong_phase.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_governing_rule_wrong_phase.md",
    "52_p7_admissible_deferral_owned.json":
        "scripts/testbed/corpus_p7/admissible_p7_deferral_owned.md",
    "53_p7_inadmissible_deferral_unowned.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_deferral_unowned.md",
    "54_p5_inadmissible_uncited_rows.json":
        "scripts/testbed/corpus_p5/inadmissible_p5_uncited_rows.md",
    "55_p5_inadmissible_hollow_registers.json":
        "scripts/testbed/corpus_p5/inadmissible_p5_hollow_registers.md",
    "56_p5_inadmissible_malformed_document.json":
        "scripts/testbed/corpus_p5/inadmissible_p5_malformed_document.md",
    "57_p5_inadmissible_untouched_subdomain.json":
        "scripts/testbed/corpus_p5/inadmissible_p5_untouched_subdomain.md",
    "58_p6_inadmissible_uncited_rows.json":
        "scripts/testbed/corpus_p6/inadmissible_p6_uncited_rows.md",
    "59_p6_inadmissible_hollow_registers.json":
        "scripts/testbed/corpus_p6/inadmissible_p6_hollow_registers.md",
    "60_p6_inadmissible_malformed_document.json":
        "scripts/testbed/corpus_p6/inadmissible_p6_malformed_document.md",
    "61_p6_inadmissible_unowned_subdomain.json":
        "scripts/testbed/corpus_p6/inadmissible_p6_unowned_subdomain.md",
    "62_p3_inadmissible_uncited_rows.json":
        "scripts/testbed/corpus_p3/inadmissible_p3_uncited_rows.md",
    "63_p3_inadmissible_unreasoned_decisions.json":
        "scripts/testbed/corpus_p3/inadmissible_p3_unreasoned_decisions.md",
    "64_p3_inadmissible_malformed_document.json":
        "scripts/testbed/corpus_p3/inadmissible_p3_malformed_document.md",
    "65_p4_inadmissible_uncited_rows.json":
        "scripts/testbed/corpus_p4/inadmissible_p4_uncited_rows.md",
    "66_p4_inadmissible_untraced_consolidation.json":
        "scripts/testbed/corpus_p4/inadmissible_p4_untraced_consolidation.md",
    "67_p4_inadmissible_malformed_document.json":
        "scripts/testbed/corpus_p4/inadmissible_p4_malformed_document.md",
    "68_inadmissible_malformed_seed.json":
        "scripts/testbed/corpus/inadmissible_p0_malformed_seed.md",
    "69_p1_inadmissible_outstanding_clarifications.json":
        "scripts/testbed/corpus_p1/inadmissible_p1_outstanding_clarifications.md",
    "70_p1_inadmissible_malformed_document.json":
        "scripts/testbed/corpus_p1/inadmissible_p1_malformed_document.md",
    "71_p2_inadmissible_unverified_beliefs.json":
        "scripts/testbed/corpus_p2/inadmissible_p2_unverified_beliefs.md",
    "72_p2_inadmissible_malformed_document.json":
        "scripts/testbed/corpus_p2/inadmissible_p2_malformed_document.md",
    "73_p8_inadmissible_unbuildable_schedule.json":
        "scripts/testbed/corpus_p8/inadmissible_p8_unbuildable_schedule.md",
    "74_p8_inadmissible_hollow_mandate.json":
        "scripts/testbed/corpus_p8/inadmissible_p8_hollow_mandate.md",
    "75_p8_inadmissible_malformed_document.json":
        "scripts/testbed/corpus_p8/inadmissible_p8_malformed_document.md",
    "76_p8_inadmissible_unplaced_amendment.json":
        "scripts/testbed/corpus_p8/inadmissible_p8_unplaced_amendment.md",
    "77_p7_inadmissible_malformed_document.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_malformed_document.md",
    "78_p7_inadmissible_uncomposed_steps.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_uncomposed_steps.md",
    "79_p7_inadmissible_unbuildable_artifacts.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_unbuildable_artifacts.md",
    "80_p7_inadmissible_unbound_fields.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_unbound_fields.md",
    "81_p7_inadmissible_unbound_topology.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_unbound_topology.md",
    "82_p7_inadmissible_miscounted_inventory.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_miscounted_inventory.md",
    "83_p7_inadmissible_uncited_rows.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_uncited_rows.md",
    "84_p7_inadmissible_undeclared_reach.json":
        "scripts/testbed/corpus_p7/inadmissible_p7_undeclared_reach.md",
}


def phase_of(name: str) -> str:
    """The phase a payload exercises. P0's cases are the ones whose name does not carry a phase."""
    match = PHASE_IN_NAME.match(name)
    return match.group(1) if match else "p0"


def payload_key(phase_id: str) -> str:
    """P0 offers a seed, every later phase offers a register. The intent field differs, so the key does."""
    return "seed_text" if phase_id == "p0" else "register_text"


def rendered() -> dict[Path, str]:
    """Every payload this declaration produces, as path → text."""
    out: dict[Path, str] = {}
    for name, source in sorted(PAYLOADS.items()):
        src = REPO / source
        if not src.is_file():
            raise FileNotFoundError(f"payload source missing: {src}")
        phase_id = phase_of(name)
        payload = {
            payload_key(phase_id): src.read_text(encoding="utf-8"),
            "author_of_record": AUTHOR,
        }
        # A phase that reads no upstream document still declares that it read none. Omitting the
        # field would make "this handoff is ungoverned" indistinguishable from "the driver forgot".
        payload["prior_texts"] = {
            prior_id: path.read_text(encoding="utf-8")
            for prior_id, path in prior_paths(src, declared_priors(phase_id)).items()
        }
        out[OUT / name] = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    return out


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    check_only = "--check" in argv
    unknown = [a for a in argv if a != "--check"]
    if unknown:
        print(__doc__.strip())
        print(f"\nunrecognised argument(s): {' '.join(unknown)}", file=sys.stderr)
        return 2

    payloads = rendered()

    if check_only:
        on_disk = set(OUT.glob("*.json"))
        drifted = sorted(p.name for p, text in payloads.items()
                         if not p.is_file() or p.read_text(encoding="utf-8") != text)
        orphaned = sorted(p.name for p in on_disk - set(payloads))
        for name in drifted:
            print(f"  DRIFTED  {name}")
        for name in orphaned:
            print(f"  ORPHANED {name}  — cut from no declared source")
        if drifted or orphaned:
            print(f"\n{len(drifted) + len(orphaned)} payload(s) do not agree with the "
                  f"declaration that produces them.")
            return 1
        print(f"  OK       {len(payloads)} payload(s) agree with their source documents")
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    for path, text in payloads.items():
        path.write_text(text, encoding="utf-8")
    print(f"{len(payloads)} payload(s) written to {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
