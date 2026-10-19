"""Execution validation — run the design phases against the criteria `routing_closure` declared.

The change answers one question for every phase that observes the composition: what happens when an
observation reports that nothing was found. The business answered it: the phase rejects, and judges
nothing. And every way the observing capability can answer is answered, now and when it gains one.

Criteria 1 and 2 dispatch a real phase workflow through `protocol_runtime`. Each makes one
observation answer NOT_FOUND at the capability boundary, by standing in for `inspector.api.query`
for that operation only, then reads the trace: the phase must end at EXIT_REJECTED, and the step
that judges must never run. A control run of the same document, with nothing replaced, must reach
the judging step.

Criterion 3 reads the assembled snapshot. Criterion 4 runs the generator over the artifacts as
text, with one invented outcome added to what the capability declares, and writes nothing.

Run:  python testbed/routing_closure/execution_validation.py [snapshot]
Exit: 0 if every exercised criterion holds, 1 otherwise.
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

from inspector import api as inspector_api
from runtime import api

from transformation.design import emit

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
PAYLOADS = REPO / "testbed" / "phases" / "test_payloads"
# The capability the judging step runs. A step record names the capability it ran, not the step, so
# this is how a trace shows that a phase judged.
JUDGING_CAPABILITY = "transformation::CT_PURE_EVALUATE_RULES_V0"


def trace(result) -> list[dict]:
    lines: list[dict] = []
    for f in sorted(Path(result.trace_dir).glob("*.jsonl")):
        lines += [json.loads(line) for line in f.read_text().splitlines() if line.strip()]
    return lines


def ending(events: list[dict]) -> str | None:
    routes = [e for e in events if e.get("event_type") == "WF_ROUTE"]
    return routes[-1].get("detail", {}).get("to_node") if routes else None


def judged(events: list[dict]) -> bool:
    """Whether the judging step ran: a step record names the capability it runs."""
    return any(e.get("event_type") == "CC_STEP"
               and e.get("detail", {}).get("step_fqdn") == JUDGING_CAPABILITY
               for e in events)


def dispatch(wf: str, payload_file: str, snapshot: Path, nothing_found: str | None):
    """Run one phase, with one observation answering NOT_FOUND when `nothing_found` names it."""
    real = inspector_api.query

    def query(operation, params, snapshot_root, trace_root=None):
        if operation == nothing_found:
            return "NOT_FOUND", {}
        return real(operation, params, snapshot_root, trace_root)

    data_root = Path(tempfile.mkdtemp(prefix="pgc_routing_closure_"))
    inspector_api.query = query
    try:
        payload = json.loads((PAYLOADS / payload_file).read_text(encoding="utf-8"))
        result = api.run_workflow(wf_fqdn=wf, payload=payload,
                                  snapshot_root=str(snapshot), data_root=str(data_root))
        return trace(result)
    finally:
        inspector_api.query = real
        shutil.rmtree(data_root, ignore_errors=True)


def canonical(snapshot: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in (snapshot / "canonical").rglob("*.json"):
        if p.name == "metadata.json":
            continue
        d = json.loads(p.read_text())
        if "fqdn_id" in d:
            out[d["fqdn_id"]] = d["frontmatter"]
    return out


def main() -> int:
    snapshot = Path(sys.argv[1]) if len(sys.argv) > 1 else WORKSPACE / "snapshot"
    if not (snapshot / "manifest.json").is_file():
        print(f"no assembled snapshot at {snapshot}")
        return 1
    results: list[tuple[str, bool | None, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    # 1 and 2 — a phase whose observation finds nothing rejects, and judges nothing
    for phase, wf, payload, op in (
        ("P2", "transformation::WF_P2_DOMAIN_MODEL_ADMISSIBILITY_V0",
         "08_p2_admissible_register.json", "si.store.list"),
        ("P3", "transformation::WF_P3_ANALYSIS_LOOP_ADMISSIBILITY_V0",
         "14_p3_admissible_catalog_register.json", "si.artifact.list"),
    ):
        control = dispatch(wf, payload, snapshot, None)
        found_nothing = dispatch(wf, payload, snapshot, op)
        check(f"a {phase} judgement whose observation reports that nothing was found ends as "
              f"rejected, and judges nothing",
              judged(control) and ending(found_nothing) == "EXIT_REJECTED"
              and not judged(found_nothing),
              f"control judged={judged(control)}; with {op} NOT_FOUND: ending "
              f"{ending(found_nothing)}, judged={judged(found_nothing)}")

    # 3 — every way the observing capability answers is answered and routed
    arts = canonical(snapshot)
    outcomes = set(emit.query_outcomes(snapshot))
    unanswered = []
    for relative in emit.JUDGE_CONTRACTS:
        fqdn = f"transformation::{Path(relative).stem}"
        core = arts[fqdn]["core"]
        for step in core["pipeline"]:
            if step.get("side_effect") == emit.QUERY_CAPABILITY and step.get("op") == "QUERY":
                if set(step.get("on_result", {})) != outcomes:
                    unanswered.append(f"{fqdn} {step['step']}")
    unrouted = []
    for phase_id in emit.SEALED_IN:
        wf = arts[emit.workflow_fqdn(phase_id)]["core"]
        node = next(k for k, n in wf["nodes"].items() if n.get("type") == "CC")
        contract = wf["nodes"][node].get("code") or node
        allowed = set(arts[f"transformation::{contract}"]["core"]["result_status_contract"]["allowed"])
        if set(wf["nodes"][node].get("next", {})) != allowed:
            unrouted.append(emit.workflow_fqdn(phase_id))
    check("every way the observing capability can answer is answered by every observing step and "
          "routed by every phase",
          not unanswered and not unrouted,
          f"{len(unanswered)} step(s) unanswered, {len(unrouted)} phase(s) unrouted")

    # 4 — an outcome the capability gains is answered and routed by the next emission
    # The generator is handed the outcomes it observed, plus one invented; nothing is replaced.
    gained = "GAINED_OUTCOME"
    gaining = (*emit.query_outcomes(snapshot), gained)
    allowed_by: dict[str, list[str]] = {}
    for relative in emit.JUDGE_CONTRACTS:
        text = emit.splice_allowed(emit.splice_query_answers(
            (REPO / relative).read_text(encoding="utf-8"), gaining))
        allowed_by[Path(relative).stem] = emit.machine(text)["core"]["result_status_contract"]["allowed"]
    missed = []
    for phase_id, filename in emit.SEALED_IN.items():
        text = (emit.WORKFLOWS / filename).read_text(encoding="utf-8")
        node, contract = emit.judge_node(text), emit.judge_contract(text)
        if contract not in allowed_by:
            continue
        routed = emit.machine(emit.splice_routing(text, allowed_by[contract]))["core"]["nodes"][node]["next"]
        if routed.get(gained) != emit.REJECTED_ENDING:
            missed.append(filename)
    observing = sum(1 for p in emit.SEALED_IN
                    if emit.judge_contract((emit.WORKFLOWS / emit.SEALED_IN[p]).read_text()) in allowed_by)
    check("an outcome the observing capability gains leaves no phase that does not answer it",
          all(gained in a for a in allowed_by.values()) and not missed,
          f"{observing - len(missed)}/{observing} observing phase(s) route it to "
          f"{emit.REJECTED_ENDING}")

    results.append(("every phase judges every document it judged before this change exactly as it did",
                    None, "exercised by e2e_phases_test.py (83 cases) and differential.py"))

    held = 0
    for criterion, ok, detail in results:
        tag = "SKIP" if ok is None else ("OK  " if ok else "FAIL")
        print(f"  {tag}  {criterion}")
        if detail:
            print(f"          {detail}")
        held += ok is True
    exercised = sum(ok is not None for _, ok, _ in results)
    print(f"\n  {held}/{exercised} criteria hold  ({len(results) - exercised} not exercised)")
    return 0 if held == exercised else 1


if __name__ == "__main__":
    sys.exit(main())
