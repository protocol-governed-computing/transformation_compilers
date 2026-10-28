"""Execution validation — ai_governance as the owner decided it, in LEDGER_BRIEF_AI_GOVERNANCE.md
(git history at 3859bec, decision_authoring_prototype/domains/ai_governance/).

Written from the brief before any design realizes it. The domain had no acceptance suite and no
business statement, so these criteria are the domain's first. Today's design fails most of them:
it takes every licensing fact from the request, and agent governance reads a store no act writes.

The criteria read behaviour: answers, announcements and what the audit trails hold. They name no
store and no step. Where an act must be named to be dispatched, `ACTS` names it; it is the only
part fitted to a design after the ledger exists, and a refit is recorded in the findings.

Two criteria need time or a refusal the run cannot produce, and stand them in, as the domain's
routing-closure suite does:
- 30 days without use: every time the business recorded is moved 40 days back;
- a removal the license registry refuses: the registry answers VIOLATION for that run only.

Run:  python .../checks/execution_validation_owner_answers.py [snapshot] [--act name=WF_CODE ...]
Exit: 0 if every criterion holds, 1 otherwise.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve()
WORKSPACE = HERE.parents[5]

for root in (WORKSPACE / "software_governance", WORKSPACE / "business_domains",
             WORKSPACE / "conformance_workloads", WORKSPACE / "transformation_compilers"):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402
from capability_side_effects.implementation.CS_REGISTRY_V0.impl.executor import (  # noqa: E402
    RegistryExecutor)

NS = "ai_governance::"
DOMAIN_DATA = "ai_governance"

ACTS = {"register": "WF_REGISTER_EMPLOYEE_V0", "train": "WF_RECORD_TRAINING_COMPLETED_V0",
        "cap": "WF_SET_LICENSE_CAP_V0", "provision": "WF_PROVISION_LICENSE_V0",
        "use": "WF_RECORD_LICENSE_USAGE_V0", "reclaim": "WF_RECLAIM_LICENSE_V0",
        "govern": "WF_GOVERN_AGENT_ACTION_V0"}

STAMP = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?")


class Outcome:
    """What a dispatched act answered, and the moments it announced."""

    def __init__(self, status: str, surface: dict, announced: set[str]):
        self.status, self.surface, self.announced = status, surface, announced


class Run:
    def __init__(self, snapshot: Path):
        self.snapshot = snapshot
        self.root = Path(tempfile.mkdtemp(prefix="pgc_ai_governance_owner_answers_"))

    def __call__(self, act: str, payload: dict):
        r = api.run_workflow(wf_fqdn=NS + ACTS[act], payload=payload,
                             snapshot_root=str(self.snapshot), data_root=str(self.root))
        announced = set()
        for f in sorted(Path(r.trace_dir).glob("*.jsonl")):
            for line in f.read_text().splitlines():
                e = json.loads(line) if line.strip() else {}
                if e.get("event_type") == "EVENT":
                    announced.add(str(e.get("detail", {}).get("ev_fqdn")))
        return Outcome(r.status, r.surface, announced)

    def held(self) -> str:
        """Everything the domain holds, as text."""
        base = self.root / DOMAIN_DATA
        return "\n".join(p.read_text() for p in sorted(base.rglob("*")) if p.is_file()) if base.is_dir() else ""

    def age(self, days: int) -> None:
        """Stand in records made `days` earlier: move every time the business recorded back."""
        def back(m):
            text = m.group(0)
            t = datetime.fromisoformat(text.replace("Z", "+00:00"))
            moved = (t - timedelta(days=days)).isoformat()
            return moved.replace("+00:00", "Z") if text.endswith("Z") else moved
        for p in (self.root / DOMAIN_DATA).rglob("*"):
            if p.is_file() and p.suffix in (".json", ".jsonl"):
                p.write_text(STAMP.sub(back, p.read_text()))

    def close(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)


def ran(r) -> bool:
    """Whether the act exists to answer: an absent act refuses nothing."""
    return not r.status.startswith("absent")


def says(r, word: str) -> bool:
    return any(word in name for name in r.announced)


def action(user: str, tool: str, parameters: dict, request: str) -> dict:
    return {"tool_name": tool, "parameters": parameters, "requesting_user_id": user,
            "domain_context": "ai_licensing", "request_id": request}


def main() -> int:
    args = sys.argv[1:]
    while "--act" in args:
        i = args.index("--act")
        name, code = args[i + 1].split("=", 1)
        ACTS[name] = code
        del args[i:i + 2]
    snapshot = Path(args[0]) if args else WORKSPACE / "snapshot"
    if not (snapshot / "manifest.json").is_file():
        print(f"no assembled snapshot at {snapshot}")
        return 1

    results: list[tuple[str, bool, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    # A request may state facts and rules of its own; the business reads none of them.
    claims = {"training_completed": True, "assigned_count": 0, "cap": 1000, "threshold_days": 0,
              "context": {"training_completed": True, "assigned_count": 0, "cap": 1000}}
    run = Run(snapshot)
    try:
        def acts(act, payload):
            try:
                return run(act, payload)
            except Exception as exc:  # an act the snapshot does not hold fails its criterion
                return Outcome(f"absent ({type(exc).__name__})", {}, set())

        # Employees
        r = acts("register", {"employee_id": "e-1"})
        check("an employee is registered", r.status == "SUCCESS" and says(r, "EMPLOYEE_REGISTERED"),
              f"status {r.status}, announced {r.announced}")
        r = acts("register", {"employee_id": "e-1"})
        check("a second registration of the same employee is refused", ran(r) and r.status != "SUCCESS",
              f"status {r.status}")
        r = acts("train", {"employee_id": "ghost"})
        check("training is refused for an employee nobody registered", ran(r) and r.status != "SUCCESS",
              f"status {r.status}")

        # The cap, before it is set
        acts("register", {"employee_id": "e-2"})
        acts("train", {"employee_id": "e-1"})
        r = acts("provision", {"employee_id": "e-1", "tier": "standard", **claims})
        check("no license is provisioned before a cap is set, whatever the request says",
              ran(r) and not says(r, "PROVISIONED"), f"status {r.status}, announced {r.announced}")

        r = acts("cap", {"cap": 1})
        check("the system sets the cap", r.status == "SUCCESS" and says(r, "CAP_SET"),
              f"status {r.status}, announced {r.announced}")

        # Training, from the business's record
        r = acts("provision", {"employee_id": "e-2", "tier": "standard", **claims})
        check("a license is refused without recorded training, whatever the request says",
              not says(r, "PROVISIONED") and says(r, "DENIED"),
              f"status {r.status}, announced {r.announced}")

        # Licenses
        r = acts("provision", {"employee_id": "e-1", "tier": "gold"})
        check("a tier other than standard or enterprise is refused", ran(r) and not says(r, "PROVISIONED"),
              f"status {r.status}, announced {r.announced}")
        r = acts("provision", {"employee_id": "e-1", "tier": "standard",
                               "license_id": "mine", "generated": {"license_id": "mine"}})
        held = run.held()
        check("a trained employee under the cap is provisioned a license the business identifies",
              r.status == "SUCCESS" and says(r, "PROVISIONED") and "lic" in held and '"mine"' not in held,
              f"status {r.status}, announced {r.announced}")
        first = r
        r = acts("provision", {"employee_id": "e-1", "tier": "enterprise"})
        check("an employee holding an active license is refused a second",
              says(first, "PROVISIONED") and ran(r) and not says(r, "PROVISIONED"),
              f"status {r.status}, announced {r.announced}")
        acts("train", {"employee_id": "e-2"})
        r = acts("provision", {"employee_id": "e-2", "tier": "standard", **claims})
        check("a license is refused at the cap, whatever the request says about the cap or the count",
              not says(r, "PROVISIONED") and says(r, "DENIED"),
              f"status {r.status}, announced {r.announced}")

        # Agent actions, judged on the license AI licensing granted
        r = acts("govern", action("e-1", "READ_RECORD", {"record_type": "user_profile", "id": "x"}, "R1"))
        check("a standard user's valid read is authorized", says(r, "AUTHORIZED"),
              f"status {r.status}, announced {r.announced}")
        r = acts("govern", action("e-2", "READ_RECORD", {"record_type": "user_profile", "id": "x"}, "R2"))
        check("a user without a license is denied", says(r, "DENIED") and not says(r, "AUTHORIZED"),
              f"status {r.status}, announced {r.announced}")
        r = acts("govern", action("e-1", "PROVISION_PREMIUM_LICENSE", {"tier": "premium", "quantity": 10}, "R3"))
        check("a standard user is denied a premium tool", says(r, "DENIED") and not says(r, "AUTHORIZED"),
              f"status {r.status}, announced {r.announced}")
        r = acts("govern", action("e-1", "DELETE_DATABASE", {}, "R4"))
        check("an undeclared tool is denied", says(r, "DENIED") and not says(r, "AUTHORIZED"),
              f"status {r.status}, announced {r.announced}")
        r = acts("govern", action("e-1", "PROVISION_STANDARD_LICENSE", {"tier": "standard", "quantity": 200}, "R5"))
        check("parameters breaking a rule are denied", says(r, "DENIED") and not says(r, "AUTHORIZED"),
              f"status {r.status}, announced {r.announced}")

        # Usage and reclaim
        r = acts("use", {"employee_id": "e-1"})
        check("a use of a license is recorded", r.status == "SUCCESS" and says(r, "USAGE_RECORDED"),
              f"status {r.status}, announced {r.announced}")
        r = acts("reclaim", {"employee_id": "e-1", "threshold_days": 0,
                             "context": {"last_active_date": "2000-01-01T00:00:00Z"}})
        g = acts("govern", action("e-1", "READ_RECORD", {"record_type": "user_profile", "id": "x"}, "R6"))
        check("a license used recently is not reclaimed, whatever the request says",
              not says(r, "REVOKED") and says(g, "AUTHORIZED"),
              f"reclaim {r.status} {r.announced}; then govern {g.announced}")

        run.age(40)
        real = RegistryExecutor.deregister
        RegistryExecutor.deregister = lambda self, payload: {"result_status": "VIOLATION"}
        try:
            r = acts("reclaim", {"employee_id": "e-1"})
        finally:
            RegistryExecutor.deregister = real
        g = acts("govern", action("e-1", "READ_RECORD", {"record_type": "user_profile", "id": "x"}, "R7"))
        check("a reclaim the registry refuses leaves the license assigned, and announces no revocation",
              not says(r, "REVOKED") and says(g, "AUTHORIZED"),
              f"reclaim {r.status} {r.announced}; then govern {g.announced}")

        r = acts("reclaim", {"employee_id": "e-1"})
        g = acts("govern", action("e-1", "READ_RECORD", {"record_type": "user_profile", "id": "x"}, "R8"))
        check("a license unused for 30 days or more is reclaimed, and no longer authorizes anything",
              says(r, "REVOKED") and says(g, "DENIED") and not says(g, "AUTHORIZED"),
              f"reclaim {r.status} {r.announced}; then govern {g.announced}")
        r = acts("provision", {"employee_id": "e-2", "tier": "enterprise"})
        check("a reclaimed license no longer counts against the cap",
              r.status == "SUCCESS" and says(r, "PROVISIONED"), f"status {r.status}, announced {r.announced}")
        g = acts("govern", action("e-2", "PROVISION_PREMIUM_LICENSE", {"tier": "premium", "quantity": 10}, "R9"))
        check("an enterprise user may use a premium tool", says(g, "AUTHORIZED"),
              f"status {g.status}, announced {g.announced}")
    finally:
        run.close()

    failed = [c for c, held, _ in results if not held]
    for criterion, held, detail in results:
        print(f"  {'OK  ' if held else 'FAIL'}  {criterion}" + ("" if held else f"\n          {detail}"))
    print(f"\n  {len(results) - len(failed)}/{len(results)} criteria hold  (0 not exercised)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
