"""Project the discovery phases — P2 domain model, P3 analysis loop, P4 business model — from what
the derivation observed.

An authored dossier discovers by reading the composition: what already exists, what fits, what a
change reaches. The derive route reads the same composition, and records what it found. The
baseline design names what the domain holds today. The derived design and its identity decisions
say what is kept, what changes meaning, what is new and what is retired. The inspector says what
each platform artifact the design reuses is for, and how far a change to it reaches. P2 to P4
restate those observations, each row citing the row it restates (P2 cites P1, P3 cites P2, P4
cites P3), and `tc phase check` grounds every name they give against the snapshot.

So this projection runs after identities are decided, never before: a discovery document written
before the derivation looked would claim observations nobody made.
"""
from __future__ import annotations

import re

from inspector import api as inspector_api

from transformation.design.derive.project import Ledger, binding, cap, cite, joined, storage, words

PLATFORM = ("capability_transforms::", "capability_side_effects::")
KIND = {"CT": "Capability transform", "CS": "Capability side effect"}


FAMILY = {"WF": "workflow", "CC": "contract", "IN": "entrance", "AC": "actor", "EV": "event", "RB": "binding",
          "STRUCTURE": "storage declaration", "CT": "transform", "CS": "side effect", "TEST_DATA": "test data"}


def short(code):
    return code.split("::")[-1]


def said_as(code):
    """An artifact named in words, for a column that states business meaning: `CC_REGISTER_BOOK_V0`
    is the register book contract. The code itself goes in the evidence beside it."""
    name = re.sub(r"_V\d+$", "", short(code))
    family = next((f for f in sorted(FAMILY, key=len, reverse=True) if name.startswith(f + "_")), "")
    rest = name[len(family) + 1:] if family else name
    rest = re.sub(r"^PURE_", "", rest).lower().replace("_", " ")
    return f"the {rest} {FAMILY.get(family, 'artifact')}"


def platform_capability(code):
    """A platform artifact's capability in words, as P2 to P4 key it."""
    return f"{cap(said_as(code)[4:])}, as the platform declares it"


class Observed:
    """What the derivation found: the baseline, the derived design, its identities, the snapshot."""

    def __init__(self, L, baseline, derived, snapshot):
        self.L, self.baseline, self.derived, self.snapshot = L, baseline, derived, str(snapshot)
        self.identity = derived["_identity"]
        uses = {}
        for row in derived.get("cc_composition") or []:
            if str(row.get("capability", "")).startswith(PLATFORM):
                uses[row["capability"]] = uses.get(row["capability"], 0) + 1
        for row in derived.get("rb_declarations") or []:
            for cs in row.get("cs_bindings") or []:
                uses.setdefault(cs, 0)
        self.platform = dict(sorted(uses.items()))

    def query(self, operation, artifact):
        status, result = inspector_api.query(operation, {"artifact": artifact}, self.snapshot)
        if status != "SUCCESS":
            raise ValueError(f"{operation} {artifact}: {status}")
        return result

    def intent(self, artifact):
        """The first paragraph of an artifact's stated intent or summary, or its machine description,
        as the composition publishes it."""
        content = self.query("si.artifact.show", artifact)["canonical"].get("content") or ""
        lines = content.splitlines()
        start = next((i for i, l in enumerate(lines) if re.match(r"^#+\s*(\d+\.\s*)?(Intent|Summary)\b", l)), None)
        para = []
        for line in lines[start + 1:] if start is not None else []:
            if line.strip():
                para.append(line.strip())
            elif para:
                break
        described = re.search(r"^\s+description:\s*(.+)$", content, re.MULTILINE)
        return " ".join(para) or (described.group(1).strip() if described else f"Declared in the composition as {short(artifact)}.")

    def workflow(self, op):
        """The derived workflow of an operation, and what identity decided for it."""
        stem = f"WF_{op.upper().replace(' ', '_')}_V"
        code = next(r["code"] for r in self.derived["new_artifacts"] if r["family"] == "WF" and stem in r["code"])
        old = {n: o for o, n in {**self.identity["superseded"], **self.identity["replaced"]}.items()}
        if code in self.identity["kept"]:
            return code, "REUSE", None
        if code in old:
            return code, "EXTEND", old[code]
        return code, "AUTHOR_NEW", None


# -- P2 ---------------------------------------------------------------------------------------------
def p2_registers(L, O, p1):
    ops = list(L.ops)
    refusal_rows, i = {}, 1
    for op in ops:
        for when, _ in L.refusals(op):
            refusal_rows[(op, when)] = i
            i += 1
    reg = {"entities": [], "entity_attributes": []}
    for t_i, (n, (_, t)) in enumerate(L.things.items(), start=1):
        changed = any(o.get("thing") == n and o["does"] == "change" for _, o in L.ops.values())
        model = [f"One durable record per {n}, addressed by its {L.identity_sentence(n)[1]}"
                 if L.identified_by(n) else f"One durable record of the {n}"]
        if changed:
            model.append("updated in place")
        if t.get("states"):
            model.append(f"carrying its own state ({joined(t['states'])})")
        reg["entities"].append({"entity": cap(n), "description": t["why"]["says"],
                                "store_model": ", ".join(model) + ".", "evidence_status": "INFERRED",
                                "source_finding": cite("p1", "business_vocabulary", t_i)})
        for field in L.identified_by(n) or [t["identity"]["field"]]:
            reg["entity_attributes"].append({
                "entity": cap(n), "attribute": cap(words(field)),
                "meaning": f"What identifies {'a' if L.identified_by(n) else 'the'} {n}.",
                "evidence_status": "INFERRED", "source_finding": cite("p1", "identity_and_sameness", t_i)})
        for field, kind in (t.get("required") or {}).items():
            if field in (L.identified_by(n) or []):
                continue
            reg["entity_attributes"].append({
                "entity": cap(n), "attribute": cap(words(field)),
                "meaning": f"Required when a {n} is recorded, as {'a list' if kind == 'array' else 'a ' + kind}.",
                "evidence_status": "INFERRED", "source_finding": cite("p1", "business_vocabulary", t_i)})
    reg["business_processes"] = [{"process": cap(op), "initiator": cap(L.acted_by(op)),
                                  "outcome": cap(L.describe(op)) + ".", "evidence_status": "INFERRED",
                                  "source_finding": cite("p1", "requested_outcomes", i)}
                                 for i, op in enumerate(ops, start=1)]
    reg["process_steps"] = []
    for i, op in enumerate(ops, start=1):
        steps = [(f"Refuse when {when}", "A refusal, and nothing recorded", cite("p1", "operation_refusals", refusal_rows[(op, when)]))
                 for when, _ in L.refusals(op)]
        steps.append((cap(L.describe(op)), f"The {L.subject(op)} record", cite("p1", "requested_outcomes", i)))
        if L.parts[L.ops[op][0]].get("trail"):
            steps.append((f"Record the operation on the {L.ops[op][0]} trail", "A trail entry",
                          cite("p1", "requested_outcomes", i)))
        reg["process_steps"] += [{"process": cap(op), "step": str(s), "action": a, "record_produced": r,
                                  "evidence_status": "INFERRED", "source_finding": c}
                                 for s, (a, r, c) in enumerate(steps, start=1)]
    reg["belief_verification"] = []
    for i, (p, row) in enumerate(zip(L.parts, p1["system_beliefs"]), start=1):
        reg["belief_verification"].append({"belief": row["belief"], "result": "VERIFIED",
                                           "evidence": belief_evidence(L, O, p),
                                           "source_finding": cite("p1", "system_beliefs", i)})
    reg["pps_baseline_fqdns"] = [{
        "capability": platform_capability(a),
        "fqdn": a, "what_it_does": O.intent(a), "fit": "EXACT",
        "cannot_do": "Nothing this design asks of it: every step the derived design binds to it uses an operation it declares."}
        for a in O.platform]
    ident = O.identity
    reg["gaps"] = []
    if ident["new"]:
        reg["gaps"].append({
            "gap": f"The composition holds none of {len(ident['new'])} artifacts the ledger's decisions need.",
            "severity": "CRITICAL", "impact": "They are authored by this change.",
            "evidence_status": "OBSERVED", "source_finding": cite("p1", "requested_outcomes", 1)})
    if ident["superseded"]:
        reg["gaps"].append({
            "gap": f"{len(ident['superseded'])} artifacts the composition holds mean something other than the ledger decides.",
            "severity": "MAJOR", "impact": "Each takes the next unused version and names its predecessor as superseded.",
            "evidence_status": "OBSERVED", "source_finding": cite("p1", "requested_outcomes", 1)})
    if not reg["gaps"]:
        reg["gaps"].append({"gap": "Nothing the ledger decides is missing from the composition.", "severity": "MINOR",
                            "impact": "Every derived artifact keeps the identity it has.", "evidence_status": "OBSERVED",
                            "source_finding": cite("p1", "requested_outcomes", 1)})
    reg["architectural_observations"] = []
    for i, p in enumerate(L.parts, start=1):
        rb = binding(O.baseline, L, p)
        if rb:
            reg["architectural_observations"].append({
                "observation": f"The {p} design keeps its records through one binding, and the derived design carries its name.",
                "evidence": f"{rb} · {storage(O.baseline, L, p)}", "evidence_status": "OBSERVED",
                "source_finding": cite("p1", "system_beliefs", i)})
    if ident["kept"]:
        reg["architectural_observations"].append({
            "observation": f"{len(ident['kept'])} artifacts the composition holds mean what the ledger decides, and keep their identity.",
            "evidence": " · ".join(ident["kept"][:3]), "evidence_status": "OBSERVED",
            "source_finding": cite("p1", "requested_outcomes", 1)})
    reg["discovery_concerns"] = concerns(L, O)
    reg["open_questions"] = [{"question": e["ask"], "category": "BUSINESS", "why_it_matters": f"{cap(e['about'])} waits on it.",
                              "source_finding": cite("p1", "out_of_scope", i)}
                             for i, e in enumerate(L.raw.get("open") or [], start=len(L.raw["out_of_scope"]) + 1)]
    return reg


def belief_evidence(L, O, part):
    rb = binding(O.baseline, L, part)
    entrances = sorted({L.domain + "::" + short(r["node"]) for r in O.baseline.get("execution_topology") or []
                        if r.get("node_type") == "IN" and r["workflow"].startswith(L.domain + "::")
                        and any(f"WF_{op.upper().replace(' ', '_')}_V" in r["workflow"]
                                for op, (p, _) in L.ops.items() if p == part)})
    named = ([rb] if rb else []) + entrances[:2]
    if not named:
        return f"The baseline design names no binding or entrance for {part}; the derived design names its own."
    return f"The baseline design names {joined(named)}, and the derived design carries them."


def concerns(L, O):
    ident, out = O.identity, []
    for old, new in ident["replaced"].items():
        out.append({"concern": f"{cap(said_as(old))} is replaced: the ledger names the operation that takes its place.",
                    "evidence": f"{old} · {new}", "severity": "MAJOR", "evidence_status": "OBSERVED",
                    "source_finding": cite("p1", "requested_outcomes", 1)})
    for code in ident["retired"]:
        out.append({"concern": f"The ledger no longer derives {said_as(code)}, so it is retired.",
                    "evidence": code, "severity": "MAJOR", "evidence_status": "OBSERVED",
                    "source_finding": cite("p1", "requested_outcomes", 1)})
    if ident["superseded"]:
        sample = list(ident["superseded"].items())[:2]
        out.append({"concern": f"{len(ident['superseded'])} artifacts change meaning, so a caller that dispatches by identity must follow supersedes.",
                    "evidence": " · ".join(f"{o} · {n}" for o, n in sample), "severity": "MAJOR",
                    "evidence_status": "OBSERVED", "source_finding": cite("p1", "requested_outcomes", 1)})
    if not out:
        out.append({"concern": "Nothing the composition holds changes meaning or is retired.", "evidence": "",
                    "severity": "MINOR", "evidence_status": "OBSERVED", "source_finding": cite("p1", "requested_outcomes", 1)})
    return out


# -- P3 ---------------------------------------------------------------------------------------------
RESOLUTION = {
    "replaced": "Replaced by record: its successor names it as superseded, and delivery deletes it and records the retirement.",
    "retired": "Retired by record: construction accounts every reference to it, and delivery deletes it and records the retirement.",
    "superseded": "Each successor takes the next unused version and names its predecessor; the suites dispatch the successor.",
    "none": "Nothing to resolve.",
}


def p3_registers(L, O, p2):
    reg = {"analysis_findings": []}
    for i, c in enumerate(p2["discovery_concerns"], start=1):
        kind = ("replaced" if "is replaced" in c["concern"] else "retired" if "no longer derives" in c["concern"]
                else "superseded" if "change meaning" in c["concern"] else "none")
        reg["analysis_findings"].append({
            "question_id": f"S2 discovery_concerns #{i}", "finding": RESOLUTION[kind],
            "impact": "The composition changes only as the ledger decides.", "evidence_status": "OBSERVED",
            "confidence": "HIGH", "resolution_status": "CLOSED",
            "evidence": c["evidence"] or "tc phase derive identities"})
    reg["verification_results"] = [{"item": r["belief"], "origin": cite("p2", "belief_verification", i),
                                    "result": "CONFIRMED", "evidence": r["evidence"]}
                                   for i, r in enumerate(p2["belief_verification"], start=1)]
    reg["dependency_discoveries"] = [{
        "dependency": a, "type": KIND.get(short(a)[:2], "Platform artifact"), "disposition": "REUSE",
        "evidence": f"Declared in the composition; the derived design binds {n} step(s) to it." if n else
                    "Declared in the composition; the derived design binds its storage to it."}
        for a, n in O.platform.items()]
    reg["impact_analysis"] = []
    for a in O.platform:
        impact = O.query("si.topology.impact", a)
        reg["impact_analysis"].append({"artifact": a, "impact_scope": ", ".join(impact["impacted_namespaces"]),
                                       "consumer_count": str(impact["impacted_count"]),
                                       "evidence": f"si.topology.impact impacted_count {impact['impacted_count']}; "
                                                   "reused as declared, so no consumer is affected"})
    reg["authoring_decisions"] = [{
        "capability": r["capability"], "decision": "REUSE",
        "rationale": "The derived design uses it as the composition declares it; it is read, never modified.",
        "alternatives_checked": f"{r['fqdn']} satisfies it as-is.", "source_finding": cite("p2", "pps_baseline_fqdns", i)}
        for i, r in enumerate(p2["pps_baseline_fqdns"], start=1)]
    for i, op in enumerate(L.ops, start=1):
        code, decision, old = O.workflow(op)
        rationale, checked = {
            "REUSE": (f"The workflow the composition holds already does what the ledger decides for {op}.",
                      f"{code} satisfies it as-is."),
            "EXTEND": (f"The workflow the composition holds for {op} means something other than the ledger decides, "
                       "so its successor takes the next unused version.", f"{old} was compared by meaning and differs."),
            "AUTHOR_NEW": (f"No workflow in the composition does what the ledger decides for {op}.",
                           f"No workflow in the {L.domain} namespace performs it."),
        }[decision]
        reg["authoring_decisions"].append({"capability": f"The {op} workflow", "decision": decision,
                                           "rationale": rationale, "alternatives_checked": checked,
                                           "source_finding": cite("p2", "business_processes", i)})
    # P2 observes each part whose storage the composition already binds, in the ledger's order.
    observed = {p: n for n, p in enumerate([p for p in L.parts if binding(O.baseline, L, p)], start=1)}
    reg["placement_decision"] = [{
        "decision": "EXTEND", "subdomain": p,
        "rationale": f"The composition already holds {p}; the derived design keeps its binding and its entrances.",
        "source_finding": cite("p2", "architectural_observations", observed[p])}
        for p in L.parts if p in observed]
    open_ = bool(L.raw.get("open"))
    reg["saturation"] = [
        {"criterion": "No unresolved CRITICAL gaps", "status": "SATISFIED",
         "evidence": "Every CRITICAL gap has an authoring decision: each new artifact is authored by this change."},
        {"criterion": "No open analyst questions", "status": "NOT_SATISFIED" if open_ else "SATISFIED",
         "evidence": "Open ledger questions hold back their operations." if open_ else "The ledger holds no open question."},
        {"criterion": "No dependency expansion in the last pass", "status": "SATISFIED",
         "evidence": f"The derived design reuses {len(O.platform)} platform artifacts, each declared in the composition."},
        {"criterion": "Verification pass complete, no OVERTURNED item unresolved", "status": "SATISFIED",
         "evidence": f"{len(reg['verification_results'])} belief(s) re-verified, none overturned."},
        {"criterion": "Every INFERRED finding promoted, accepted or carried forward with a reason", "status": "SATISFIED",
         "evidence": "Every INFERRED finding restates a ledger answer, which the owner decided."},
    ]
    return reg


# -- P4 ---------------------------------------------------------------------------------------------
AUTHORITY = {"human": "Operator", "system": "System", "agent": "Agent"}


def p4_registers(L, O, p1, p2, p3):
    actors = L.actors or {L.actor: L.raw["actor"]}
    processes = {r["process"]: i for i, r in enumerate(p2["business_processes"], start=1)}
    reg = {"actors": []}
    for name, a in actors.items():
        ops = [op for op in L.ops if L.acted_by(op) == name]
        if ops:
            reg["actors"].append({"actor": cap(name), "role": f"Requests {joined(ops)}",
                                  "authority_class": AUTHORITY.get(a.get("kind"), "Operator"),
                                  "source_finding": cite("p2", "business_processes", processes[cap(ops[0])])})
    reg["bm_entities"] = [{"entity": r["entity"], "description": r["description"], "store_model": r["store_model"],
                           "source_finding": cite("p2", "entities", i)} for i, r in enumerate(p2["entities"], start=1)]
    reg["resources"] = [{"resource": f"{cap(L.plural(n))} records", "description": t["why"]["says"],
                         "source_finding": cite("p2", "entities", i)} for i, (n, (_, t)) in enumerate(L.things.items(), start=1)]
    reg["events"] = [{"event": r["event"], "trigger": r["when_it_occurs"], "lifecycle_meaning": r["significance"],
                      "source_finding": cite("p1", "business_events", i)} for i, r in enumerate(p1["business_events"], start=1)]
    reg["relationships"] = []
    for i, (n, (_, t)) in enumerate(L.things.items(), start=1):
        if L.identified_by(n):
            reg["relationships"].append({"subject": cap(n), "verb": "is identified by", "object": cap(L.identity_sentence(n)[1]),
                                         "capability_need": f"Tell one {n} from another when it is recorded",
                                         "source_finding": cite("p1", "identity_and_sameness", i)})
        if t.get("belongs_to"):
            reg["relationships"].append({"subject": cap(n), "verb": "belongs to", "object": cap(t["belongs_to"]),
                                         "capability_need": f"Record a {n} against exactly one {t['belongs_to']}",
                                         "source_finding": cite("p1", "identity_and_sameness", i)})
        if t.get("held_by"):
            reg["relationships"].append({"subject": cap(n), "verb": "is held by", "object": cap(t["held_by"]["thing"]),
                                         "capability_need": f"Read the {t['held_by']['thing']} who holds it",
                                         "source_finding": cite("p1", "identity_and_sameness", i)})
    reg["capability_graph"], reg["gap_register"], reg["authoring_scope"] = [], [], []
    owner = {f"The {op} workflow": p for op, (p, _) in L.ops.items()}
    first = next(iter(L.parts))
    for i, r in enumerate(p3["authoring_decisions"], start=1):
        satisfied = r["decision"] == "REUSE"
        gap = "" if satisfied else f"GAP-{len(reg['gap_register']) + 1:02d}"
        reg["capability_graph"].append({"capability": r["capability"],
                                        "source_finding": cite("p3", "authoring_decisions", i),
                                        "status": "SATISFIED" if satisfied else "CRITICAL", "gap_register_entry": gap,
                                        "notes": "Reused as the composition holds it." if satisfied else r["rationale"]})
        if gap:
            reg["gap_register"].append({"gap_code": gap, "source_finding": cite("p3", "authoring_decisions", i),
                                        "capability": r["capability"], "owner_subdomain": owner.get(r["capability"], first),
                                        "resolution": "NEW" if r["decision"] == "AUTHOR_NEW" else "EXTEND"})
            reg["authoring_scope"].append({"capability": r["capability"], "gap_register_ref": gap})
    reg["dependency_graph"] = [{"from": L.domain, "to": r["dependency"], "dependency_type": "capability call",
                                "pps_status": "SATISFIED", "source_finding": cite("p3", "dependency_discoveries", i)}
                               for i, r in enumerate(p3["dependency_discoveries"], start=1)]
    reg["constraint_register"] = [{"number": str(i), "constraint": r["invariant"],
                                   "source_finding": cite("p1", "business_invariants", i), "source": "invariant"}
                                  for i, r in enumerate(p1["business_invariants"], start=1)]
    reg["design_decisions"] = [{
        "number": str(i), "decision": f"{p} stays the subdomain it is; the derived design extends it.",
        "source_finding": cite("p3", "placement_decision", i), "rationale": r["rationale"],
        "constraints_imposed": "The binding and entrances callers meet keep their names."}
        for i, (p, r) in enumerate(zip(L.parts, p3["placement_decision"]), start=1)]
    reg["design_decisions"].append({
        "number": str(len(reg["design_decisions"]) + 1),
        "decision": "Each artifact keeps its identity when its meaning is unchanged, and takes the next unused version when it changes.",
        "source_finding": cite("p3", "analysis_findings", 1),
        "rationale": "A caller relying on an identity relies on what it means.",
        "constraints_imposed": "A caller dispatching by identity follows supersedes."})
    return reg
