"""Keyed nodes — one contract run at several places in one workflow.

A workflow that refuses for several reasons and records each refusal runs one recording contract at
several places, each handed its own reason. A node named by its contract's code can be only one of
those places, so the topology names each place with a key and states the contract it runs in `Runs`.
Shown here: construction renders each key as a node running the contract, with its own inputs; a
design that keys its nodes passes every rule that reads the topology, including a discharge that
names a keyed step; and each rule that governs keys fires on a design built to trip it and stays
silent on the one that keeps it. A design with no `Runs` column is the design language as it was.

Run:  python scripts/testbed/keyed_node_design_test.py
"""

from __future__ import annotations

import sys

import machine
from transformation.build.render import render_all
from transformation.design.evaluate import ParsedDocument
from transformation.design.oracle import evaluate
from transformation.design.rule_sets import RULE_SETS

rule_set = RULE_SETS["p7"].rule_set
from transformation.design.read import parse_text

# The observation the rule under test reads, as its schema entry names it.
CONTRACT_OBSERVATION = "si.capability.surface#contracts"
D = "probe"
WF, CHECK, RECORD = f"{D}::WF_SUBMIT_V0", f"{D}::CC_CHECK_V0", f"{D}::CC_RECORD_V0"
NEW = [("Submit", "WF", WF), ("Asked to submit", "IN", f"{D}::IN_SUBMIT_V0"), ("Check", "CC", CHECK),
       ("Record", "CC", RECORD)]
TOPOLOGY = [  # node, runs, type, routing
    (f"{D}::IN_SUBMIT_V0", "", "IN", {"ACK": CHECK}),
    (CHECK, "", "CC", {"SUCCESS": "RECORD_ACCEPTED", "NOT_FOUND": "RECORD_UNKNOWN", "DENIED": "RECORD_DENIED"}),
    ("RECORD_ACCEPTED", RECORD, "CC", {"SUCCESS": "EXIT_SUCCESS"}),
    ("RECORD_UNKNOWN", RECORD, "CC", {"SUCCESS": "EXIT_REFUSED"}),
    ("RECORD_DENIED", RECORD, "CC", {"SUCCESS": "EXIT_REFUSED"}),
    ("EXIT_SUCCESS", "", "EXIT_SUCCESS", None),
    ("EXIT_REFUSED", "", "EXIT", None),
]
INTERFACE = [(RECORD, "INPUT", "reason"), (RECORD, "INPUT", "entry"), (CHECK, "INPUT", "entry")]
BINDINGS = [  # step, field, source
    (CHECK, "entry", "input.entry"),
    ("RECORD_ACCEPTED", "entry", "input.entry"),
    ("RECORD_ACCEPTED", "reason", {"literal": "accepted"}),
    ("RECORD_UNKNOWN", "entry", "input.entry"),
    ("RECORD_UNKNOWN", "reason", {"literal": "unknown"}),
    ("RECORD_DENIED", "entry", f"results.{CHECK}.entry"),
    ("RECORD_DENIED", "reason", {"literal": "denied"}),
]
DISCHARGES = [("Submit an entry", "The entry is unknown", "RECORD_UNKNOWN", "SUCCESS")]
HELD = {"TOPOLOGY_NODE_UNDECLARED", "TOPOLOGY_NODE_REPEATED", "TOPOLOGY_ROUTE_UNRESOLVED",
        "NODE_INPUT_UNBOUND", "BINDING_SOURCE_UNREACHABLE", "DISCHARGE_NOT_IN_TOPOLOGY",
        "DISCHARGE_DOES_NOT_REFUSE"}
RULES = [r for r in rule_set() if r.id in HELD]


def _table(register: str, header: list[str], rows: list[tuple]) -> tuple[str, dict]:
    return machine.register(register, header, rows)


def design(topology=TOPOLOGY, bindings=BINDINGS, discharges=DISCHARGES, keyed=True, extra=()) -> str:
    header = ["Workflow", "Node", "Runs", "Node Type", "Routing", "Source Finding"]
    rows = [(WF, n, r, t, route, "human decision") for n, r, t, route in topology]
    if not keyed:
        header.remove("Runs")
        rows = [(WF, n, t, route, "human decision") for n, _, t, route in topology]
    return machine.document(
        "Design Intent: probe / keyed",
        _table("new_artifacts", ["Capability", "Family", "Code", "Summary", "Owner Subdomain", "Status",
                                   "Source Finding"],
                 [(c, f, code, c, "keyed", "NEW", "human decision") for c, f, code in NEW]),
        _table("execution_topology", header, rows),
        _table("interface_fields", ["Artifact", "Direction", "Field", "Type", "Required", "Default", "Meaning"],
                 [(a, d, f, "string", "YES", None, f) for a, d, f in INTERFACE]),
        _table("step_bindings", ["Owner", "Step", "Direction", "Field", "Bound To", "Source Finding"],
                 [(WF, s, "INPUT", f, b, "human decision") for s, f, b in bindings]),
        _table("refusal_discharge", ["Operation", "Refused When", "Act", "Step", "Outcome", "Source Finding"],
                 [(o, w, WF, s, out, "human decision") for o, w, s, out in discharges]),
        *extra,
    )


def parsed(text: str, observed: dict | None = None) -> ParsedDocument:
    header, sections, registers = parse_text(text)
    return ParsedDocument(header=header, sections=sections, registers=registers, raw=text, path="probe",
                          observed=observed or {})


def registers(text: str) -> dict[str, list[dict]]:
    doc = parsed(text)
    return {e["id"]: doc.register(e["id"]).table.rows for e in doc.registers
            if doc.register(e["id"]) and doc.register(e["id"]).table}


def fired(text: str) -> list[str]:
    return sorted(f.code for f in evaluate(parsed(text), RULES).findings)


def nodes(text: str) -> dict:
    mandate = {"build_order": [{"code": code} for _, _, code in NEW],
               "field_declarations": [{"code": code, "subdomain_field": "keyed"} for _, _, code in NEW]}
    workflow = next(a for a in render_all(registers(text), mandate) if a["machine"]["fqdn"] == WF)
    return workflow["machine"]["core"]["nodes"]


def test_each_key_renders_as_a_node_running_its_contract_with_its_own_inputs():
    rendered = nodes(design())
    for key, reason in (("RECORD_ACCEPTED", "accepted"), ("RECORD_UNKNOWN", "unknown"),
                        ("RECORD_DENIED", "denied")):
        assert rendered[key]["code"] == "CC_RECORD_V0", rendered[key]
        assert rendered[key]["inputs"]["reason"] == reason, rendered[key]
    assert rendered["CC_CHECK_V0"]["code"] == "CC_CHECK_V0"
    assert rendered["CC_CHECK_V0"]["next"]["NOT_FOUND"] == "RECORD_UNKNOWN", rendered["CC_CHECK_V0"]


def test_a_design_without_the_column_renders_as_it_always_did():
    plain = [row for row in TOPOLOGY if not row[1]]
    plain[1] = (CHECK, "", "CC", {"SUCCESS": "EXIT_SUCCESS", "NOT_FOUND": "EXIT_REFUSED"})
    rendered = nodes(design(topology=plain, bindings=BINDINGS[:1], discharges=[], keyed=False))
    assert rendered["CC_CHECK_V0"]["code"] == "CC_CHECK_V0", rendered
    assert fired(design(topology=plain, bindings=BINDINGS[:1], discharges=[], keyed=False)) == []


def test_a_keyed_design_passes_every_rule_that_reads_the_topology():
    assert fired(design()) == []


def test_each_rule_fires_on_the_defect_it_names():
    unkeyed = [(n, "" if n == "RECORD_DENIED" else r, t, route) for n, r, t, route in TOPOLOGY]
    undeclared = [(n, f"{D}::CC_RECORDS_V0" if n == "RECORD_DENIED" else r, t, route)
                  for n, r, t, route in TOPOLOGY]
    repeated = TOPOLOGY + [("RECORD_DENIED", RECORD, "CC", {"SUCCESS": "EXIT_REFUSED"})]
    by_contract = [(n, r, t, {o: RECORD if to == "RECORD_UNKNOWN" else to for o, to in route.items()}
                    if route else route) for n, r, t, route in TOPOLOGY]
    unbound = [b for b in BINDINGS if b[:2] != ("RECORD_UNKNOWN", "reason")]
    unreachable = [b if b[0] != "RECORD_DENIED" or b[1] != "entry"
                   else (b[0], b[1], "results.RECORD_ELSEWHERE.entry") for b in BINDINGS]
    completes = [("Submit an entry", "The entry was accepted", "RECORD_ACCEPTED", "SUCCESS")]
    nowhere = [("Submit an entry", "The entry is unknown", "RECORD_ELSEWHERE", "SUCCESS")]
    cases = {
        "a key with no contract": (design(topology=unkeyed), "TOPOLOGY_NODE_UNDECLARED"),
        "a key running a contract nobody declared": (design(topology=undeclared), "TOPOLOGY_NODE_UNDECLARED"),
        "one key at two places": (design(topology=repeated), "TOPOLOGY_NODE_REPEATED"),
        "a route naming the contract, not the key": (design(topology=by_contract), "TOPOLOGY_ROUTE_UNRESOLVED"),
        "a key handed less than its contract requires": (design(bindings=unbound), "NODE_INPUT_UNBOUND"),
        "a source naming a key the workflow never runs": (design(bindings=unreachable),
                                                          "BINDING_SOURCE_UNREACHABLE"),
        "a discharge at a key that completes": (design(discharges=completes), "DISCHARGE_DOES_NOT_REFUSE"),
        "a discharge at a key the act lacks": (design(discharges=nowhere), "DISCHARGE_NOT_IN_TOPOLOGY"),
    }
    for name, (text, rule) in cases.items():
        assert rule in fired(text), (name, rule, fired(text))


def test_a_route_to_a_place_the_composition_already_has_resolves():
    # An amendment declares the places it changes. It routes on to a place the workflow already has
    # and does not redeclare, which resolves against the composition and nowhere else.
    amendment = [(f"{D}::IN_SUBMIT_V0", "", "IN", {"ACK": CHECK}),
                 (CHECK, "", "CC", {"SUCCESS": "RECORD_ACCEPTED", "NOT_FOUND": "EXIT_REFUSED"})]
    route = [r for r in rule_set() if r.id == "TOPOLOGY_ROUTE_UNRESOLVED"]

    def fired_against(workflows):
        doc = parsed(design(topology=amendment), {"si.behavior_logic.list": workflows})
        return [f.code for f in evaluate(doc, route).findings]

    composed = {"domain": D, "wf_code": "WF_SUBMIT_V0", "nodes": ["CC_CHECK_V0", "RECORD_ACCEPTED"]}
    assert fired_against([composed]) == [], fired_against([composed])
    assert fired_against([]) == ["TOPOLOGY_ROUTE_UNRESOLVED"], "unobserved, the route is reported"
    elsewhere = dict(composed, domain="other")
    assert fired_against([elsewhere]) == ["TOPOLOGY_ROUTE_UNRESOLVED"], "another domain's workflow"
    lacking = dict(composed, nodes=["CC_CHECK_V0"])
    assert fired_against([lacking]) == ["TOPOLOGY_ROUTE_UNRESOLVED"], "a place the workflow lacks"


def test_a_contract_redeclared_whole_requires_only_what_it_now_declares():
    # The composition still has the contract taking a rule from its caller. A design that composes
    # the contract's steps authors it again and withdraws that input; one that only calls it does not.
    unbound = [r for r in rule_set() if r.id == "NODE_INPUT_UNBOUND"]
    pinned = {CONTRACT_OBSERVATION: [{"contract": CHECK, "inputs": {"entry": {"required": True},
                                                                   "rule": {"required": True}}}]}
    composition = _table("cc_composition", ["CC Code", "Step", "Step Name", "Capability", "Kind", "Source Finding"],
                         [(CHECK, 1, "check_entry", "capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0",
                           "CT", "human decision")])

    def fired_with(text):
        return [f.code for f in evaluate(parsed(text, pinned), unbound).findings]

    assert fired_with(design(extra=(composition,))) == [], fired_with(design(extra=(composition,)))
    assert fired_with(design()) == ["NODE_INPUT_UNBOUND"], "a contract only called keeps what it had"


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except Exception as exc:  # report every test, then fail the run
            failed += 1
            print(f"  FAIL  {name}: {exc!r}"[:1500])
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
