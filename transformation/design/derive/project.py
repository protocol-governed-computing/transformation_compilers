"""Project a ledger's phase documents: the seed (P0), business intent (P5) and governance intent (P6).

The derive route goes from a closed decision ledger to P7 without the phases between. Projecting
them gives the intermediate dossier a reader expects, and puts each one in front of the rule set
that already governs it: `tc phase check` judges a projected document exactly as it judges an
authored one. Nothing here relaxes a rule. A projection that fails on form is a fault in the
projection.

Each document is projected from the one before it, and every row cites the row it restates: P0
restates the ledger, P5 cites P0, P6 cites P5. P1 is not projected here — it is P0's projection
(`transformation.design.project.project_p1`), and it stays one.

What a ledger states in business words — its purpose, why it keeps each thing, what it does not do —
is carried word for word. What it states as structure (identity, states, refusals, events) is said
in sentences built from that structure, and those sentences claim nothing the structure does not.
"""
from __future__ import annotations

import re

from transformation.design.derive.base import parts_of
from transformation.design.project import dump
from transformation.design.schema import load

CLASSIFICATION = "MODIFY"  # a ledger redesigns a domain the composition already holds


def named(m):
    return {k: v for k, v in (m or {}).items() if k != "from"}


def cap(text):
    return text[:1].upper() + text[1:]


def joined(words):
    words = list(words)
    return words[0] if len(words) == 1 else ", ".join(words[:-1]) + " and " + words[-1]


def article(text):
    """`a` or `an`, as the next word sounds."""
    return re.sub(r"\b([Aa]) (?=[aeiouAEIOU])", lambda m: m.group(1) + "n ", text)


def words(field):
    return field.replace("_", " ")


class Ledger:
    """A ledger read as its parts, with each thing and operation knowing its part."""

    def __init__(self, ledger):
        self.raw = ledger
        self.domain = ledger["domain"]
        self.parts = parts_of(ledger)
        self.purpose = ledger["purpose"]["says"]
        self.part_purpose = {p: (v.get("purpose") or ledger["purpose"])["says"] for p, v in self.parts.items()}
        self.things = {n: (p, t) for p, v in self.parts.items() for n, t in named(v.get("things")).items()}
        held = {e["about"] for e in ledger.get("open") or []}
        self.ops = {n: (p, o) for p, v in self.parts.items() for n, o in named(v.get("operations")).items()
                    if n not in held}
        self.actor = ledger["actor"]["name"]
        self.actors = named(ledger.get("actors"))

    def carried(self):
        """The ledger's own words, which a projection carries as they are."""
        out = {self.purpose, *self.part_purpose.values(), *(t["why"]["says"] for _, t in self.things.values())}
        return out | {e[k] for e in self.raw["out_of_scope"] for k in ("item", "reason")}

    def subdomain(self):
        names = list(self.parts)
        return names[0] if len(names) == 1 else names

    def plural(self, thing):
        return self.things[thing][1]["plural"]

    def subject(self, op):
        o = self.ops[op][1]
        return o.get("thing") or joined(o.get("creates") or [])

    def describe(self, op):
        """What an operation does, said from its shape."""
        o = self.ops[op][1]
        does = o["does"]
        if does == "create":
            return f"records a new {joined(o['creates'])}"
        if does == "change" and "to_state" in o:
            return f"moves a {o['thing']} from {o['from_state']} to {o['to_state']}"
        if does == "change":
            changed = o.get("may_change") or list((o.get("sets") or {}))
            return f"changes a {o['thing']}'s {joined(words(f) for f in changed)}" if changed else f"changes a {o['thing']}"
        if does == "read":
            extra = f", with its {joined(self.plural(t) for t in o['with'])}" if o.get("with") else ""
            return f"returns one {o['thing']}{extra}"
        return f"returns the {self.plural(o['thing'])} that match"

    def acted_by(self, op):
        return self.ops[op][1].get("actor") or self.actor

    def identified_by(self, thing):
        ident = self.things[thing][1]["identity"]
        if "fixed" in ident:
            return None
        source = ident.get("from") or ident["field"]
        return [source] if isinstance(source, str) else source

    def freed(self, thing):
        """`, until <op> frees it`, when an operation releases the thing's identity for reuse."""
        ops = [op for op, (_, o) in self.ops.items() if o.get("thing") == thing and o.get("releases") == "identity"]
        return f", until {joined(ops)} frees it" if ops else ""

    def identity_sentence(self, thing):
        ident = self.things[thing][1]["identity"]
        fields = self.identified_by(thing)
        if fields is None:
            return f"There is one {thing}", "one"
        norm = ", without regard to letter case or repeated spacing" if ident.get("normalized") else ""
        return f"they carry the same {joined(words(f) for f in fields)}{norm}", joined(words(f) for f in fields)

    # -- what each operation refuses, said from its shape ---------------------------------------
    def refusals(self, op):
        p, o = self.ops[op]
        out = []
        thing = o.get("thing")
        if o.get("precondition") == "exists":
            out.append((f"the {thing} is not recorded", f"There is no {thing} to act on."))
        if "from_state" in o:
            out.append((f"the {thing} is not {o['from_state']}",
                        f"Only a {o['from_state']} {thing} becomes {o['to_state']}."))
        if o.get("refuse_if") == "duplicate":
            out.append((f"the change would make the {thing} the same as another",
                        f"Two {self.plural(thing)} that are the same would describe one {thing} twice."))
        for created in o.get("creates") or []:
            if self.things[created][1]["identity"].get("on_duplicate") == "refuse":
                out.append((f"a {created} that is the same is already recorded",
                            f"Two {self.plural(created)} that are the same would describe one {created} twice."))
        for created in o.get("creates") or []:
            h = self.things[created][1].get("held_by")
            if h:
                out.append((f"the {h['thing']} who would hold it is not recorded",
                            f"A {created} no {h['thing']} holds belongs to nobody the business knows."))
                if h.get("requires_state"):
                    out.append((f"the {h['thing']} who would hold it is not {h['requires_state']}",
                                f"Only {h['requires_state']} {self.plural(h['thing'])} hold {self.plural(created)}."))
        if o.get("parent") == "existing":
            parent = self.things[o["creates"][0]][1].get("belongs_to")
            out.append((f"the {parent} it belongs to is not recorded", f"A {o['creates'][0]} belongs to a recorded {parent}."))
        for check in o.get("checks") or []:
            out.append((f"{check['name']} does not hold", f"The business requires {check['name']} before it acts."))
        return out


# -- P0 ---------------------------------------------------------------------------------------------
def p0_registers(L):
    reg = {"subdomain_purpose": L.purpose}
    reg["cr_type"] = [{"subdomain": p, "classification": CLASSIFICATION, "rationale": L.part_purpose[p]}
                      for p in L.parts]
    reg["business_vocabulary"] = [{"term": cap(n), "definition": t["why"]["says"]} for n, (_, t) in L.things.items()]
    reg["requested_outcomes"] = [{"outcome": f"{cap(op)}: {L.describe(op)}."} for op in L.ops]
    reg["known_facts"] = []
    for n, (_, t) in L.things.items():
        same, by = L.identity_sentence(n)
        reg["known_facts"].append({"fact": f"A {n} is identified by its {by}." if by != "one" else f"{same}.",
                                   "certainty": "HIGH"})
    reg["system_beliefs"] = [{
        "belief": f"The current {p} design names the records, entrances and requests its callers use today.",
        "why_it_matters": "The derived design keeps those names, so a caller meets no change the ledger did not decide.",
        "verification_goal": f"Read the {p} baseline design and find there each name the derived design carries.",
    } for p in L.parts]
    reg["assumptions"] = []
    reg["constraints"] = []
    reg["business_invariants"] = [{"invariant": inv} for inv, _ in invariants(L)]
    reg["lifecycle_states"] = [{"object": n, "state": s, "meaning": state_meaning(L, n, s)}
                               for n, (_, t) in L.things.items() for s in t.get("states") or []]
    reg["business_events"] = [{"event": cap(e), "when_it_occurs": f"When {op} completes",
                               "significance": f"Others learn that {op} completed without reading the {L.ops[op][0]} records."}
                              for op, e in events(L)]
    reg["authority_boundaries"] = [{"business_object": n, "authoritative_owner": p} for n, (p, _) in L.things.items()]
    reg["out_of_scope"] = ([{"item": e["item"], "reason": e["reason"]} for e in L.raw["out_of_scope"]] +
                           [{"item": cap(e["about"]), "reason": f"Held until {e['waits_on']} answers: {e['ask']}"}
                            for e in L.raw.get("open") or []])
    reg["governance_scope"] = [{"scope_item": p, "relationship": "MODIFIED"} for p in L.parts]
    reg["clarification_requests"] = []
    reg["acceptance_criteria"] = ([{"criterion": f"{cap(op)} is refused when {when}."}
                                   for op in L.ops for when, _ in L.refusals(op)] +
                                  [{"criterion": f"When {c['when']}, {c['then']}, because {c['because']}."}
                                   for c in L.raw.get("cases") or []])
    reg["identity_and_sameness"] = [{"business_object": n, "identified_by": L.identity_sentence(n)[1],
                                     "two_are_the_same_when": L.identity_sentence(n)[0]} for n in L.things]
    reg["lifecycle_transitions"] = [{"object": o["thing"], "from_state": o["from_state"], "to_state": o["to_state"],
                                     "triggered_by": op, "cascade": "None"}
                                    for op, (_, o) in L.ops.items() if "to_state" in o]
    reg["operation_refusals"] = [{"operation": op, "refused_when": when, "business_reason": why}
                                 for op in L.ops for when, why in L.refusals(op)]
    reg["authority_deferrals"] = []
    return reg


def invariants(L):
    """(invariant, business reason), from identity, belonging, holding, keeping and the trail."""
    out = []
    for n, (_, t) in L.things.items():
        ident = t["identity"]
        if ident.get("on_duplicate") in ("refuse", "reuse") and L.identified_by(n):
            out.append((f"No two {L.plural(n)} share their {L.identity_sentence(n)[1]}{L.freed(n)}.",
                        f"Two {L.plural(n)} that are the same would describe one {n} twice."))
        if ident.get("on_duplicate") == "repeat" and L.identified_by(n):
            out.append((f"Recording a {n} again with the same {L.identity_sentence(n)[1]} records the repeat, "
                        f"and the {n} already recorded is unchanged by it.",
                        f"The business keeps one record of each {n}, and a repeat does not undo what was decided."))
        if t.get("belongs_to"):
            out.append((f"Each {n} belongs to exactly one {t['belongs_to']}.",
                        f"A {n} recorded against two {L.plural(t['belongs_to'])} would make the record untrue."))
        if t.get("held_by"):
            h = t["held_by"]
            state = f" who is {h['requires_state']}" if h.get("requires_state") else ""
            out.append((f"Each {n} is held by one {h['thing']}{state}.",
                        f"A {n} no {h['thing']} holds belongs to nobody the business knows."))
    for op, (_, o) in L.ops.items():
        if o.get("keeps"):
            out.append((f"{cap(op)} never changes a {o['thing']}'s {joined(words(k) for k in o['keeps'])}.",
                        f"{cap(op)} changes only what it is for."))
    for p, v in L.parts.items():
        trail = v.get("trail") or {}
        if trail:
            out.append((f"Every {p} operation records {joined(words(r) for r in trail['records'])} on the {p} trail, "
                        "and no entry is changed or removed.",
                        "Every operation must be traceable afterwards, and a trail that could be amended would not be evidence."))
    return out


def state_meaning(L, thing, state):
    into = [op for op, (_, o) in L.ops.items()
            if o.get("to_state") == state and o.get("thing") == thing]
    if L.things[thing][1]["states"][0] == state:
        into = [op for op, (_, o) in L.ops.items() if thing in (o.get("creates") or [])] + into
    return f"A {thing} is {state} after {joined(into)}." if into else f"A {thing} that is {state}."


def events(L):
    return [(op, e) for p, v in L.parts.items() for op, es in named(v.get("announces")).items()
            if op in L.ops for e in es]


# -- P5 ---------------------------------------------------------------------------------------------
def cite(phase, register, row):
    return {"phase": phase, "register": register, "row": row}


def p5_registers(L, p0):
    def row(register, match):
        return next(i for i, r in enumerate(p0[register], start=1) if match(r))

    reg = {"subdomain_purpose": L.purpose,
           "purpose_provenance": [{"source": "Change seed §0 Subdomain Purpose", "disposition": "INHERITED",
                                   "refinement": None}]}
    reg["subdomain_purposes"] = [{"subdomain": p, "purpose": L.part_purpose[p],
                                  "source_finding": cite("p0", "cr_type", i)}
                                 for i, p in enumerate(L.parts, start=1)]
    outcomes = {op: i for i, op in enumerate(L.ops, start=1)}
    reg["scope_boundary"] = (
        [{"capability": cap(op), "status": "IN_SCOPE", "notes": cap(L.describe(op)),
          "source_finding": cite("p0", "requested_outcomes", i)} for op, i in outcomes.items()] +
        [{"capability": r["item"], "status": "DEFERRED", "notes": r["reason"],
          "source_finding": cite("p0", "out_of_scope", i)} for i, r in enumerate(p0["out_of_scope"], start=1)])
    reg["business_objects"] = []
    for n, (p, t) in L.things.items():
        vocab = row("business_vocabulary", lambda r: r["term"] == cap(n))
        reg["business_objects"].append({"store_name": f"{cap(n)} record", "record_model": "MUTABLE_STATE",
                                        "business_rationale": t["why"]["says"],
                                        "source_finding": cite("p0", "business_vocabulary", vocab)})
        if t["identity"].get("on_duplicate") in ("refuse", "reuse") and L.identified_by(n):
            same = row("identity_and_sameness", lambda r: r["business_object"] == n)
            reg["business_objects"].append({
                "store_name": f"{cap(n)} identity registry", "record_model": "IDENTITY_REGISTRY",
                "business_rationale": f"Telling one {n} from another needs a claim on its identity at the moment it is recorded.",
                "source_finding": cite("p0", "identity_and_sameness", same)})
    invs = invariants(L)
    for p, v in L.parts.items():
        if v.get("trail"):
            i = next(i for i, (inv, _) in enumerate(invs, start=1) if inv.startswith(f"Every {p} operation records"))
            reg["business_objects"].append({"store_name": f"Audit trail of {p}",
                                            "record_model": "APPEND_ONLY_JOURNAL",
                                            "business_rationale": invs[i - 1][1],
                                            "source_finding": cite("p0", "business_invariants", i)})
    reg["identity_semantics"] = []
    for i, n in enumerate(L.things, start=1):
        p, t = L.things[n]
        same, by = L.identity_sentence(n)
        parent = t.get("belongs_to") or (t.get("held_by") or {}).get("thing")
        reg["identity_semantics"].append({
            "store_name": f"{cap(n)} record", "identity_field": cap(by),
            "source": "Formed by the business" if "prefix" in t["identity"] or "fixed" in t["identity"] else "Supplied with the request",
            "uniqueness_rule": f"Two {L.plural(n)} are the same when {same}{L.freed(n)}." if by != "one" else f"{same}.",
            "cross_subdomain_relationship": f"Names exactly one {parent}" if parent else "None",
            "source_finding": cite("p0", "identity_and_sameness", i)})
    reg["invariants"] = [{"invariant": inv, "business_reason": why, "source_finding": cite("p0", "business_invariants", i)}
                         for i, (inv, why) in enumerate(invs, start=1)]
    reg["actions"] = [{"action": cap(op), "object": L.subject(op), "trigger": f"Requested by the {L.acted_by(op)}",
                       "status": "IN_SCOPE", "source_finding": cite("p0", "requested_outcomes", i)}
                      for op, i in outcomes.items()]
    reg["provisional_codes"] = [{"subdomain": L.ops[op][0], "provisional_code": f"WF_{op.upper().replace(' ', '_')}_V0",
                                 "family": "WF", "summary": cap(L.describe(op)),
                                 "source_finding": cite("p0", "requested_outcomes", i)}
                                for op, i in outcomes.items()]
    reg["cross_subdomain_refs"] = []
    return reg


# -- P6 ---------------------------------------------------------------------------------------------
def storage(baseline, L, part):
    """The part's storage structure, at the version the baseline design holds it, or None."""
    stem = re.compile(rf"{re.escape(L.domain)}::STRUCTURE_{part.upper()}_STORAGE_V\d+$")
    return next((r["storage_structure"] for r in baseline.get("rb_declarations") or []
                 if stem.match(r.get("storage_structure") or "")), None)


def binding(baseline, L, part):
    """The binding the baseline design already gives a part's storage (carried:surface), or None."""
    structure = storage(baseline, L, part)
    return next((r["rb_code"] for r in baseline.get("rb_declarations") or []
                 if structure and r.get("storage_structure") == structure), None)


def p6_registers(L, p5, baseline):
    owner_of_op = {cap(op): p for op, (p, _) in L.ops.items()}
    first = next(iter(L.parts))
    reg = {"ownership": [{
        "capability": r["capability"], "owner_subdomain": owner_of_op.get(r["capability"], first),
        "disposition": "OWNED" if r["status"] == "IN_SCOPE" else "DEFERRED", "existing_artifact": "",
        "source_finding": cite("p5", "scope_boundary", i)} for i, r in enumerate(p5["scope_boundary"], start=1)]}
    part_of_store = {f"{cap(n)} record": p for n, (p, _) in L.things.items()}
    part_of_store |= {f"{cap(n)} identity registry": p for n, (p, _) in L.things.items()}
    part_of_store |= {f"Audit trail of {p}": p for p in L.parts}
    reg["storage_governance"] = [{"storage_need": f"A durable {r['store_name'][:1].lower()}{r['store_name'][1:]}",
                                  "purpose": r["business_rationale"], "subdomain": part_of_store[r["store_name"]],
                                  "source_finding": cite("p5", "business_objects", i)}
                                 for i, r in enumerate(p5["business_objects"], start=1)]
    actions = {r["action"]: i for i, r in enumerate(p5["actions"], start=1)}
    reg["cross_subdomain_deps"] = []
    for op, r in named(L.raw.get("reads_other_part")).items():
        if op not in L.ops:
            continue
        bound = binding(baseline, L, r["part"])
        reg["cross_subdomain_deps"].append({
            "dependency": f"{cap(op)} reads the {joined(L.plural(t) for t in r['reads'])} {r['part']} keeps, and never writes them",
            "direction": f"{L.ops[op][0]} -> {r['part']}", "existing_artifact": bound or "",
            "status": "SATISFIED" if bound else "GAP", "source_finding": cite("p5", "actions", actions[cap(op)])})
    reg["pps_artifacts_requiring_action"] = []
    purposes = {r["subdomain"]: i for i, r in enumerate(p5["subdomain_purposes"], start=1)}
    reg["boundary_rules"] = [{
        "rule_name": f"{p.upper()}_OWNS_ITS_RECORDS",
        "statement": f"Every record {p} keeps is written only by {p}'s own operations.",
        "source_finding": cite("p5", "subdomain_purposes", purposes[p])} for p in L.parts]
    reg["boundary_rules"] += [{
        "rule_name": f"{L.ops[op][0].upper()}_READS_{r['part'].upper()}_NEVER_WRITES",
        "statement": f"{cap(op)} reads what {r['part']} keeps and leaves it exactly as it was, including when it is refused.",
        "source_finding": cite("p5", "actions", actions[cap(op)])}
        for op, r in named(L.raw.get("reads_other_part")).items() if op in L.ops]
    reg["governance_outcome"] = [{"capability": r["capability"], "owner_subdomain": r["owner_subdomain"],
                                  "source_finding": {"phase": "p6", "register": "ownership", "key": r["capability"]}}
                                 for r in reg["ownership"] if r["disposition"] == "OWNED"]
    return reg


# -- documents -------------------------------------------------------------------------------------
TITLES = {"p0": "Change Seed", "p2": "Stage 2 — Domain Model", "p3": "Stage 3 — Analysis Loop",
          "p4": "Stage 4 — Business Model", "p5": "Stage 5 — Business Intent", "p6": "Stage 6 — Governance Intent"}
HANDOFF = {"p0": ("the decision ledger", "Stage 1"), "p2": ("Stage 1", "Stage 3"), "p3": ("Stage 2", "Stage 4"),
           "p4": ("Stage 3", "Stage 5"), "p5": ("Change seed", "Stage 6"), "p6": ("Stage 5", "Stage 7")}
NOTE = {
    "p0": "Projected from the decision ledger. Business prose (the purpose, each vocabulary definition, "
          "what is out of scope) is the ledger's own, word for word; every other row is said from the "
          "ledger's structure and claims nothing it does not state.",
    "p2": "Projected from what the derivation observed: the baseline design, the derived design and the "
          "composition the inspector reads. Every row cites the change-request row it models.",
    "p3": "Projected from the domain model and the identity decisions the derivation made. Every row cites "
          "what it resolves.",
    "p4": "Projected from the analysis loop. Every row cites what it consolidates.",
    "p5": "Projected from the change seed, which is projected from the decision ledger. Every row cites the "
          "seed row it restates.",
    "p6": "Projected from the business intent. Every row cites the business-intent row it places.",
}


def said(node, carried):
    """Every generated sentence with its articles right; the ledger's own words untouched."""
    if isinstance(node, dict):
        return {k: said(v, carried) for k, v in node.items()}
    if isinstance(node, list):
        return [said(v, carried) for v in node]
    return article(node) if isinstance(node, str) and node not in carried else node


def document(phase, L, registers, cr=None):
    template = load(phase)
    header = {"phase": phase, "domain": L.domain, "subdomain": L.subdomain(), "cr": cr or f"{L.domain}_ledger",
              "rule_set": template.schema_id}
    headings, seen = [], set()
    for register in template.registers:
        heading = f"## {register.section_number or ''}. {register.section_title}"
        if heading not in seen:
            seen.add(heading)
            headings += [heading, "", "---", ""]
    consumes, emits = HANDOFF[phase]
    machine = dump({"document": header, "registers": said(registers, L.carried())}).rstrip("\n")
    parts = [f"# {TITLES[phase]} — {L.domain} / {', '.join(L.parts)}", "", "## Machine", "", "```yaml", machine,
             "```", "", NOTE[phase], "", "---", "", *headings,
             f"## gov_projection — Governed Handoff to {emits}", "", "| Direction | Fields |", "|-----------|--------|",
             f"| **Consumes** ← {consumes} | {' · '.join(sorted(registers))} |" if phase != "p0" else
             f"| **Consumes** ← {consumes} | the owner's answers |",
             f"| **Emits** → {emits} | {' · '.join(r.id for r in template.registers)} |"]
    return "\n".join(parts) + "\n"


def project(ledger, baseline, derived=None, snapshot=None, cr=None):
    """{phase: document text} for P0, P5 and P6, each projected from the one before it, and P2 to P4
    when the derivation's observations are given.

    `baseline` is the domain's current design (P7 registers): what a read of another part already
    reads through is named there, as the derived design carries it. `derived` is the derived design
    with its identity decisions (`_identity`), and `snapshot` the composition they were decided
    against; P2 to P4 restate what those show (`discover.py`)."""
    L = Ledger(ledger)
    p0 = p0_registers(L)
    p5 = p5_registers(L, p0)
    p6 = p6_registers(L, p5, baseline)
    docs = {"p0": document("p0", L, p0, cr), "p5": document("p5", L, p5, cr), "p6": document("p6", L, p6, cr)}
    if derived is not None:
        from transformation.design.derive import discover
        O = discover.Observed(L, baseline, derived, snapshot)
        p1 = said(p0, L.carried())  # P1 restates P0 row for row, as P0's document says it
        p2 = discover.p2_registers(L, O, p1)
        p3 = discover.p3_registers(L, O, said(p2, L.carried()))
        p4 = discover.p4_registers(L, O, p1, p2, p3)
        docs |= {"p2": document("p2", L, p2, cr), "p3": document("p3", L, p3, cr), "p4": document("p4", L, p4, cr)}
    return docs
