"""Execution validation — the three requirements the owner's answers added to blockchain.

Written from LEDGER_BRIEF_BLOCKCHAIN.md
(git history at 3859bec, decision_authoring_prototype/domains/blockchain/) before any design realizes them, so the design is held to
the brief and not the other way round. Today's design fails them; that is the expected baseline.

  1. The business can list the actors in a given state.
  2. A repeated registration records the details it submitted, and the actor is unchanged by them.
  3. A repeated registration is announced as a registration again, distinct from a first one.
  4. Listing a state no actor is in answers with an empty list.
  5. Two wallets never share an address.

The criteria read behaviour, not structure. They name no store, step or event. Where an act must be
named to be dispatched, `ACTS` names it, and it is the only part fitted to a design after the ledger
exists. A refit is recorded in the findings, never made silently.

Run:  python .../checks/execution_validation_owner_answers.py [snapshot] [--act name=WF_CODE ...]
Exit: 0 if every criterion holds, 1 otherwise.
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve()
WORKSPACE = HERE.parents[5]

for root in (WORKSPACE / "software_governance", WORKSPACE / "business_domains",
             WORKSPACE / "conformance_workloads", WORKSPACE / "transformation_compilers",
             WORKSPACE / "protocol_transport"):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402

NS = "blockchain::"
DOMAIN_DATA = "blockchain"

# Each business act and the request field that names a state when listing.
ACTS = {"register": "WF_REGISTER_ACTOR_V0", "accept": "WF_ACCEPT_ACTOR_V0",
        "reject": "WF_REJECT_ACTOR_V0", "list": "WF_LIST_ACTORS_V0", "list_field": "state",
        "create_wallet": "WF_CREATE_WALLET_V0"}

ADA, BOB, CAROL, DAN = "ada@example.test", "bob@example.test", "carol@example.test", "dan@example.test"
AUTHORITY = "authority-01"
FIRST, SECOND = "Ada Lovelace", "Ada King"
# Two public keys: the secp256k1 generator, and twice the generator.
KEY_ONE = ("79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
           "483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8")
KEY_TWO = ("c6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee5"
           "1ae168fea63dc339a3c58419466ceaeef7f632653266d0e1236431a950cfe52a")


def registration(name: str, address: str) -> dict:
    return {"actor_record": {"name": name, "contact_address": address,
                             "currency_preference": "BACHI", "language": "en"}}


def decision(address: str, grounds: str = "") -> dict:
    return {"contact_address": address, "verifying_authority": AUTHORITY, "grounds": grounds}


def announced(result) -> set[str]:
    """Every event a run announced."""
    names = set()
    for f in sorted(Path(result.trace_dir).glob("*.jsonl")):
        for line in f.read_text().splitlines():
            e = json.loads(line) if line.strip() else {}
            if e.get("event_type") == "EVENT":
                names.add(e.get("detail", {}).get("ev_fqdn"))
    return names


def lists_of_actors(surface) -> list[set[str]]:
    """Every list of actor records the answer holds, as the set of addresses each names.

    An answer may carry what its act read on the way to it, so the criterion asks that one list in
    it names exactly the expected actors, not that nothing else appears anywhere in it.
    """
    found = []
    for value in (surface or {}).values():
        if isinstance(value, list) and all(isinstance(v, dict) and "contact_address" in v for v in value):
            found.append({v["contact_address"] for v in value})
    return found


def records(data_root: Path, suffix: str) -> str:
    """Everything the domain holds in files of one kind, as text."""
    base = data_root / DOMAIN_DATA
    return "\n".join(p.read_text() for p in sorted(base.rglob(f"*{suffix}")) if p.is_file())


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

    data_root = Path(tempfile.mkdtemp(prefix="pgc_blockchain_owner_answers_"))
    results: list[tuple[str, bool, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    def run(act: str, payload: dict):
        return api.run_workflow(wf_fqdn=NS + ACTS[act], payload=payload,
                                snapshot_root=str(snapshot), data_root=str(data_root))

    def listing(state: str):
        try:
            r = run("list", {ACTS["list_field"]: state})
        except Exception as exc:  # an act the snapshot does not hold is a failed criterion
            return None, f"{type(exc).__name__}: {exc}", []
        return r, json.dumps(r.surface), lists_of_actors(r.surface)

    try:
        first = run("register", registration(FIRST, ADA))

        # 4 — a state no actor is in lists as empty
        r, text, lists = listing("ACCEPTED")
        check("listing a state no actor is in answers with an empty list",
              r is not None and r.status == "SUCCESS" and set() in lists,
              f"status {r.status if r else 'absent'}; surface {text[:160]}")

        run("register", registration("Bob Stone", BOB))
        run("reject", decision(BOB, grounds="address unreachable"))
        run("register", registration("Carol Ng", CAROL))
        run("accept", decision(CAROL))
        again = run("register", registration(SECOND, ADA))

        # 1 — listing by state
        shown = {}
        for state in ("UNVERIFIED", "ACCEPTED", "REJECTED"):
            r, text, lists = listing(state)
            shown[state] = (r.status if r else "absent", text, lists)
        expected = {"UNVERIFIED": ADA, "ACCEPTED": CAROL, "REJECTED": BOB}
        for state, who in expected.items():
            status, text, lists = shown[state]
            check(f"listing the {state.lower()} actors shows exactly them",
                  status == "SUCCESS" and {who} in lists,
                  f"status {status}; lists answered: {lists}; surface {text[:160]}")

        # 2 — a repeated registration records what it submitted, and the actor keeps the first
        trail, held = records(data_root, ".jsonl"), records(data_root, ".json")
        _, unverified, _ = shown["UNVERIFIED"]
        check("a repeated registration does not fail", again.status == "SUCCESS",
              f"status {again.status}")
        check("a repeated registration records the details it submitted",
              SECOND in trail, f"'{SECOND}' on no trail")
        check("the actor keeps the details it was first admitted with",
              FIRST in held and SECOND not in held and SECOND not in unverified,
              f"first in record: {FIRST in held}; second in record: {SECOND in held}; "
              f"second listed: {SECOND in unverified}")

        # 3 — a registration again is announced, and not as a first registration
        once, twice = announced(first), announced(again)
        check("a repeated registration is announced, distinct from a first registration",
              bool(twice) and not (twice & once), f"first: {once}; again: {twice}")

        # 5 — two wallets never share an address
        run("register", registration("Dan Ito", DAN))
        run("accept", decision(DAN))
        mine = run("create_wallet", {"contact_address": CAROL, "key_material": KEY_ONE})
        shared = run("create_wallet", {"contact_address": DAN, "key_material": KEY_ONE})
        own = run("create_wallet", {"contact_address": DAN, "key_material": KEY_TWO})
        check("a wallet whose key another wallet's address already uses is refused",
              mine.status == "SUCCESS" and shared.status != "SUCCESS" and own.status == "SUCCESS",
              f"first {mine.status}; same key {shared.status}; own key {own.status}")
    finally:
        shutil.rmtree(data_root, ignore_errors=True)

    failed = [c for c, held, _ in results if not held]
    for criterion, held, detail in results:
        print(f"  {'OK  ' if held else 'FAIL'}  {criterion}" + ("" if held else f"\n          {detail}"))
    print(f"\n  {len(results) - len(failed)}/{len(results)} criteria hold  (0 not exercised)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
