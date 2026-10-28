"""Derive a whole domain's P7 registers from a closed-shape decision ledger.

Patterns build components (CCs) and workflows (WFs) from ledger operations. A small renderer turns
them into P7 rows. Every row carries `_from`: the ledger entry, or the doctrine rule, it comes from.

Doctrine is engine/doctrine.yaml. A row that follows a rule cites it as `doctrine:<name>`, and a
citation of a rule the file does not state is refused.

Realization inventory: transforms whose implementation is code (key formation, select, group) are
carried from the baseline with their test cases. The ledger decides what they compute; it does not
author their implementation.

Usage: generate_domain.py <ledger.yaml> <baseline P7> > generated.json
"""
import json
import re
import sys
from pathlib import Path

import yaml

CS = "capability_side_effects::"
CT = "capability_transforms::"
MUTABLE, REGISTRY, APPENDONLY = (CS + "CS_MUTABLE_JSON_V0", CS + "CS_REGISTRY_V0",
                                 CS + "CS_APPENDONLY_JSONL_V0")
CLOCK = CS + "CS_CLOCK_V0"
STATUSES = {
    "READ": ["SUCCESS", "NOT_FOUND", "VIOLATION", "BACKEND_ERROR"],
    "RESOLVE": ["SUCCESS", "NOT_FOUND", "VIOLATION", "BACKEND_ERROR"],
    "REGISTER": ["SUCCESS", "ALREADY_EXISTS", "VIOLATION", "BACKEND_ERROR"],
    "WRITE": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    "UPDATE_WHERE": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    "UPDATE": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    "NOW": ["SUCCESS", "BACKEND_ERROR"],
    "APPEND": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    "SELECT": ["SUCCESS", "BACKEND_ERROR"],
    "DELETE": ["SUCCESS", "NOT_FOUND", "VIOLATION", "BACKEND_ERROR"],
    "DEREGISTER": ["SUCCESS", "NOT_FOUND", "VIOLATION", "BACKEND_ERROR"],
    None: ["SUCCESS", "VIOLATION"],
}
NATIVE_OUT = {"READ": "value", "RESOLVE": None, "REGISTER": None}
# Realization inventory carried from the baseline: the code-backed transforms.
CARRIED_REGISTERS = ("implementation_bindings", "test_cases", "test_case_values")
# Patterns for an actor who acts for themselves (`authorization: none`).
PARTICIPANT_KINDS = ("register", "decide", "list", "create_held")


def parts_of(ledger):
    """A ledger's parts. A ledger without `parts` is one part, named by its subdomain."""
    if "parts" in ledger:
        return ledger["parts"]
    return {ledger["subdomain"]: {k: ledger[k] for k in ("things", "operations", "trail", "announces", "events")
                                  if k in ledger}}


def tokens(name):
    """A name's words, singular, with `id` read as identity: how a carried store name is matched."""
    out = set()
    for w in re.split(r"[_\s]+", name.upper()):
        w = {"ID": "IDENTITY"}.get(w, w)
        w = w[:-3] + "Y" if w.endswith("IES") else (w[:-1] if w.endswith("S") else w)
        if w:
            out.add(w)
    return out


def up(name):
    return name.upper().replace(" ", "_")


def head(name):
    return name.split()[-1]


def noun(thing_name, key):
    """A key named after its thing drops the thing's name: a wallet's `wallet_id` is its `id`."""
    h = head(thing_name) + "_"
    return key[len(h):] if key.startswith(h) else key


def short(code):
    return str(code).split("::")[-1]


class Step:
    def __init__(self, name, capability, operation, store, ins, outs, src, routing=None):
        self.name, self.capability, self.operation, self.store = name, capability, operation, store
        self.ins, self.outs, self.src, self.routing = ins, outs, src, routing or {}


class Component:
    def __init__(self, code, summary, steps, inputs, outputs, src):
        self.code, self.summary, self.steps = code, summary, steps
        self.inputs, self.outputs, self.src = inputs, outputs, src

    def exits(self):
        """Statuses the component can end with: SUCCESS, plus any a step exits on."""
        out = ["SUCCESS"]
        for i, s in enumerate(self.steps):
            kind = "CS" if s.capability.startswith(CS) else "CT"
            for st in STATUSES[s.operation if kind == "CS" else None]:
                route = s.routing.get(st, "continue" if (st == "SUCCESS" and i < len(self.steps) - 1) else "exit")
                if st != "SUCCESS" and route == "exit" and st not in out:
                    out.append(st)
        return out


class Domain:
    def __init__(self, ledger, baseline):
        self.top, self.base = ledger, baseline
        self.ns = ledger["domain"] + "::"
        self.parts = parts_of(ledger)
        self.things = {n: t for p in self.parts.values() for n, t in p.get("things", {}).items()}
        self.thing_part = {n: name for name, p in self.parts.items() for n in p.get("things", {})}
        self.carried_stores = {}
        self.event_part = {}
        self.components = {}
        self.workflows = []
        self.stores = {}
        self.events = {}
        self.unrealized = []
        self.conflicts = []
        a = ledger["actor"]
        self.ac = self.code("AC", a["name"])
        self.enter(next(iter(self.parts)))

    def enter(self, part):
        """Generate within one part: its own stores, trail and bindings (doctrine binding)."""
        self.sub = part
        self.l = {**self.top, **self.parts[part], "subdomain": part, "things": self.things}
        self.rb, self.structure = self.rb_of(part), self.structure_of(part)
        self.trail_store = f"{up(part)}_OPERATIONS"

    def rb_of(self, part):
        return f"{self.ns}RB_{up(part)}_BINDINGS_V0"

    def structure_of(self, part):
        return f"{self.ns}STRUCTURE_{up(part)}_STORAGE_V0"

    def code(self, family, name):
        return f"{self.ns}{family}_{up(name)}_V0"

    def thing(self, name):
        return self.things[name]

    def add(self, comp, part=None):
        if comp.code not in self.components:
            comp.part = part or self.sub
            self.components[comp.code] = comp
        return comp.code

    def store(self, name, cs, src, part=None, match=None):
        """A store, under the name the existing composition already gives it (carried:surface).

        A record store is carried only under its own name. A registry is carried from the part's
        registry whose name holds every word of `match`. A trail is the part's one append-only store.
        """
        part = part or self.sub
        key = (part, name)
        if key not in self.carried_stores:
            base = [r for r in self.base.get("structure_stores") or []
                    if r["storage_type"] == short(cs) and r["structure"] == self.structure_of(part)]
            taken = {n for (_, n, _) in self.carried_stores.values()}
            hit = next((r for r in base if r["store_name"] == name), None)
            if hit is None and cs == REGISTRY and match:
                hit = next((r for r in base if r["store_name"] not in taken
                            and tokens(match) <= tokens(r["store_name"])), None)
            if hit is None and cs == APPENDONLY and len(base) == 1 and base[0]["store_name"] not in taken:
                hit = base[0]
            carried = hit["store_name"] if hit else name
            path = hit["proposed_path"] if hit else None
            src = src + " + carried:surface" if hit and carried != name else src
            self.carried_stores[key] = (part, carried, path)
        _, carried, path = self.carried_stores[key]
        self.stores.setdefault(carried, (cs, src, part, path))
        return carried

    # -- shared components ---------------------------------------------------------------------

    def authorize(self):
        a, src = self.l["actor"], "ledger:actor"
        return self.add(Component(
            f"{self.ns}CC_CONFIRM_{up(a['role'])}_AUTHORIZED_V0",
            f"Confirm the {a['role']} member may perform {self.sub} operations",
            [Step("confirm_authorization", CT + "CT_PURE_VALIDATE_PARAMETER_RULES_V0", None, None,
                  {"parameters": "inputs.staff_credentials", "rules": {"literal": a["authorized_when"]}},
                  {"is_authorized": "capability_result.valid"}, src)],
            {"staff_credentials": "object"}, {"is_authorized": "boolean"}, src))

    def trail(self):
        src = "ledger:trail"
        store = self.store(self.trail_store, APPENDONLY, src + " + doctrine:storage")
        return self.add(Component(
            f"{self.ns}CC_APPEND_{up(self.sub)}_OPERATION_V0",
            f"Append a durable account of a performed operation to the {self.sub}'s own trail",
            [Step("append_operation", APPENDONLY, "APPEND", store,
                  {"record": "inputs.record", "stream_id": {"literal": store}, "actor_id": "inputs.staff_id"},
                  {"record_id": "capability_result.record_id",
                   "sequence_number": "capability_result.sequence_number"}, src)],
            {"record": "object", "staff_id": "string", "operation": "string"},
            {"record_id": "string", "sequence_number": "integer"}, src))

    def registry(self, thing_name, key=None):
        """The registry of a thing's identity, or of another value the thing holds uniquely."""
        t = self.thing(thing_name)
        unique = key is not None
        key = key or t["identity"]["field"]
        name = (f"{up(thing_name)}_IDENTITY_REGISTRY" if "from" in t["identity"] and not unique
                else f"{up(head(thing_name))}_{up(key)}_REGISTRY")
        return self.store(name, REGISTRY, f"ledger:things/{thing_name}/identity + doctrine:storage",
                          part=self.thing_part[thing_name], match=key.replace("_", " "))

    def records(self, thing_name):
        t = self.thing(thing_name)
        return self.store(up(t["plural"]), MUTABLE, f"ledger:things/{thing_name} + doctrine:storage",
                          part=self.thing_part[thing_name])

    def key_ct(self, thing_name):
        return f"{self.ns}CT_PURE_FORM_{up(thing_name)}_IDENTITY_KEY_V0"

    def validate(self, src):
        """Required fields of the book and its work, and what a registration must carry."""
        book, work = self.thing("book"), self.thing("work")
        schema = lambda t: {f: {"required": True, "type": "string" if ty == "string" else ty}
                            for f, ty in t["required"].items()}
        vsrc = "ledger:things/book/required"
        return self.add(Component(
            f"{self.ns}CC_VALIDATE_BOOK_SUBMISSION_V0",
            "Confirms a registration carries what a work and an edition require, before any identity is claimed",
            [Step("validate_book_fields", CT + "CT_PURE_VALIDATE_RECORD_STRUCTURE_V0", None, None,
                  {"record": "inputs.book_fields", "schema": {"literal": schema(book)}},
                  {"violations": "capability_result.violations"}, vsrc),
             Step("validate_work_fields", CT + "CT_PURE_VALIDATE_RECORD_STRUCTURE_V0", None, None,
                  {"record": "inputs.work_fields", "schema": {"literal": schema(work)}},
                  {"violations": "capability_result.violations"}, "ledger:things/work/required"),
             Step("require_submission_complete", CT + "CT_PURE_VALIDATE_PARAMETER_RULES_V0", None, None,
                  {"parameters": {"literal": {"barcode": "$.inputs.barcode", "subject": "$.inputs.book_fields.subject",
                                              "book_violations": "$.results.validate_book_fields.violations",
                                              "work_violations": "$.results.validate_work_fields.violations"}},
                   "rules": {"literal": [{"field": "barcode", "op": "neq", "value": ""},
                                         {"field": "subject", "op": "neq", "value": []},
                                         {"field": "book_violations", "op": "eq", "value": []},
                                         {"field": "work_violations", "op": "eq", "value": []}]}},
                  {"valid": "capability_result.valid"}, src)],
            {"work_fields": "object", "book_fields": "object", "barcode": ("string", "NO")}, {"valid": "boolean"},
            src))

    def claim_keyed(self, thing_name):
        """Form a thing's identity key and claim it. A reused identity also writes the record when new."""
        t = self.thing(thing_name)
        idt, key = t["identity"], t["identity"]["field"]
        src = f"ledger:things/{thing_name}/identity"
        reg, rec_store = self.registry(thing_name), self.records(thing_name)
        form = Step(f"form_{'identity_key' if key == 'identity_key' else key}", self.key_ct(thing_name), None, None,
                    {f: f"inputs.{f}" for f in idt["from"]}, {key: f"capability_result.{key}"}, src)
        claim_name = "claim_identity" if idt["on_duplicate"] == "refuse" else f"claim_{thing_name}"
        claim = Step(claim_name, REGISTRY, "REGISTER", reg,
                     {"key": f"results.{form.name}.{key}", "target_cs": {"literal": MUTABLE},
                      "target_ref": {"literal": rec_store}},
                     {"address": "capability_result.address", "result_status": "result_status"}, src)
        steps, inputs = [form, claim], {f: self.thing("book")["required"].get(f, "string") for f in idt["from"]}
        outputs = {key: "string"}
        if idt["on_duplicate"] == "reuse":
            # A new work's record is written by the claim that creates it; a held one is reused.
            claim.routing = {"SUCCESS": "continue"}
            rec = f"{thing_name}_record"
            steps += [Step(f"assemble_{rec}", CT + "CT_PURE_ASSEMBLE_RECORD_V0", None, None,
                           {"fields": "inputs.work_fields"}, {rec: "capability_result.record"}, src),
                      Step(f"write_{rec}", MUTABLE, "WRITE", rec_store,
                           {"key": f"results.{form.name}.{key}", "value": f"results.assemble_{rec}.{rec}"},
                           {"result_status": "result_status"}, src)]
            inputs["work_fields"] = "object"
        else:
            outputs["address"] = "string"
        verb = "Claim" if idt["on_duplicate"] == "refuse" else "Forms the key for, and claims,"
        return self.add(Component(f"{self.ns}CC_CLAIM_{up(thing_name)}_IDENTITY_V0",
                                  f"{verb} a {thing_name}'s identity", steps, inputs, outputs, src))

    def claim_plain(self, thing_name, unique=None):
        """Claim a thing's identity, or another value it holds uniquely, in its registry."""
        t = self.thing(thing_name)
        key, src = unique or t["identity"]["field"], f"ledger:things/{thing_name}/identity"
        reg = self.registry(thing_name, unique)
        return self.add(Component(
            f"{self.ns}CC_CLAIM_{up(head(thing_name))}_{up(noun(thing_name, key))}_V0",
            f"Claim a {head(thing_name)}'s {key} so a second {head(thing_name)} carrying it is refused",
            [Step(f"claim_{key}", REGISTRY, "REGISTER", reg,
                  {"key": f"inputs.{key}", "target_cs": {"literal": MUTABLE},
                   "target_ref": {"literal": self.records(thing_name)}},
                  {"address": "capability_result.address", "result_status": "result_status"}, src)],
            {key: "string"}, {"address": "string"}, src))

    def resolve_plain(self, thing_name):
        """Resolve an identity in its registry: the precondition `exists`, or the pre-check `free`."""
        t = self.thing(thing_name)
        key, src = t["identity"]["field"], f"ledger:things/{thing_name}/identity"
        name = (f"CC_RESOLVE_{up(thing_name)}_IDENTITY_V0" if "from" in t["identity"]
                else f"CC_RESOLVE_{up(head(thing_name))}_{up(key)}_V0")
        return self.add(Component(
            self.ns + name, f"Resolve a {thing_name}'s {key.replace('_', ' ')}",
            [Step("resolve_identity", REGISTRY, "RESOLVE", self.registry(thing_name),
                  {"key_or_address": f"inputs.{key}"},
                  {"target_ref": "capability_result.target_ref", "result_status": "result_status"}, src)],
            {key: "string"}, {"target_ref": "string"}, src))

    def require_free(self, thing_name, unique=None):
        """Pre-check that an identity is unclaimed. Refuses with VIOLATION when it is held, so the
        workflow's status names the refusal (a workflow reports its last component's status)."""
        t = self.thing(thing_name)
        key, src = unique or t["identity"]["field"], "doctrine:order"
        h = head(thing_name)
        return self.add(Component(
            f"{self.ns}CC_REQUIRE_{up(h)}_{up(key)}_FREE_V0",
            f"Refuse when a {h}'s {key} is already held, before any identity is claimed",
            [Step("resolve_identity", REGISTRY, "RESOLVE", self.registry(thing_name, unique),
                  {"key_or_address": f"inputs.{key}"},
                  {"target_ref": "capability_result.target_ref", "result_status": "result_status"}, src,
                  routing={"SUCCESS": "continue", "NOT_FOUND": "continue"}),
             Step("require_unheld", CT + "CT_PURE_VALIDATE_PARAMETER_RULES_V0", None, None,
                  {"parameters": {"literal": {"held": "$.results.resolve_identity.result_status"}},
                   "rules": {"literal": [{"field": "held", "op": "eq", "value": "NOT_FOUND"}]}},
                  {"valid": "capability_result.valid"}, src)],
            {key: "string"}, {"valid": "boolean"}, src))

    def resolve_keyed(self, thing_name):
        """Form the key from attributes, resolve it, and read the record it names."""
        t = self.thing(thing_name)
        idt, key, src = t["identity"], t["identity"]["field"], f"ledger:things/{thing_name}/identity"
        rec = f"{thing_name}_record"
        return self.add(Component(
            f"{self.ns}CC_RESOLVE_{up(thing_name)}_V0",
            f"Forms the {thing_name} key, resolves it against the registry, and reads the record it names",
            [Step(f"form_{key}", self.key_ct(thing_name), None, None,
                  {f: f"inputs.{f}" for f in idt["from"]}, {key: f"capability_result.{key}"}, src),
             Step(f"resolve_{thing_name}_claim", REGISTRY, "RESOLVE", self.registry(thing_name),
                  {"key_or_address": f"results.form_{key}.{key}"},
                  {"target_ref": "capability_result.target_ref", "result_status": "result_status"}, src),
             Step(f"read_{rec}", MUTABLE, "READ", self.records(thing_name),
                  {"key": f"results.form_{key}.{key}"},
                  {rec: "capability_result.value", "result_status": "result_status"}, src)],
            {f: "string" for f in idt["from"]}, {key: "string", rec: "object"}, src))

    def write_record(self, thing_name, op_name):
        """Assemble a new record in the thing's first state, and write it: one per thing (doctrine reuse)."""
        t = self.thing(thing_name)
        key, src = t["identity"]["field"], f"ledger:operations/{op_name}"
        h = head(thing_name)
        rec = f"{h}_record"
        if thing_name == "book":
            # The work key is formed from the edition's own title and author, so the record never
            # depends on an earlier component's output having been carried forward.
            work = t["belongs_to"]
            wfrom = self.thing(work)["identity"]["from"]
            fields = {key: f"$.inputs.{key}", **{f: f"$.inputs.{h}_fields.{f}" for f in t["required"]},
                      "state": up(t["states"][0]), "work_key": "$.results.form_work_key.work_key"}
            return self.add(Component(
                f"{self.ns}CC_REGISTER_BOOK_V0",
                "Assembles an edition record against the work it belongs to, and writes it",
                [Step("form_work_key", self.key_ct(work), None, None,
                      {f: f"inputs.{h}_fields.{f}" for f in wfrom}, {"work_key": "capability_result.work_key"},
                      f"ledger:things/{work}/identity"),
                 Step(f"assemble_{rec}", CT + "CT_PURE_ASSEMBLE_RECORD_V0", None, None,
                      {"fields": {"literal": fields}}, {rec: "capability_result.record"},
                      "ledger:things/book/states"),
                 Step(f"write_{rec}", MUTABLE, "WRITE", self.records(thing_name),
                      {"key": f"inputs.{key}", "value": f"results.assemble_{rec}.{rec}"},
                      {"result_status": "result_status"}, src)],
                {key: "string", "book_fields": "object"}, {rec: "object"}, src))
        parent = t["belongs_to"]
        pkey = self.thing(parent)["identity"]["field"]
        prec = f"{parent}_record"
        return self.add(Component(
            f"{self.ns}CC_REGISTER_{up(thing_name)}_V0", f"Record a {h} against exactly one {parent}",
            [Step(f"read_{prec}", MUTABLE, "READ", self.records(parent), {"key": f"inputs.{pkey}"},
                  {prec: "capability_result.value", "result_status": "result_status"}, src),
             Step(f"assemble_{rec}", CT + "CT_PURE_ASSEMBLE_RECORD_V0", None, None,
                  {"fields": {"literal": {pkey: f"$.inputs.{pkey}", key: f"$.inputs.{key}",
                                          "state": up(t["states"][0])}}},
                  {rec: "capability_result.record"}, f"ledger:things/{thing_name}/states"),
             Step(f"write_{rec}", MUTABLE, "WRITE", self.records(thing_name),
                  {"key": f"inputs.{key}", "value": f"results.assemble_{rec}.{rec}"},
                  {"result_status": "result_status"}, src)],
            {pkey: "string", key: "string"}, {prec: "object"}, src))

    # -- operation patterns: each returns (component chain, request fields, trail subject) -------
    # A chain entry is (component, bindings, routing overrides, source).

    def register_with_first_child(self, op_name, op):
        src = f"ledger:operations/{op_name}"
        book, work, child = op["thing"], self.thing(op["thing"])["belongs_to"], op["child"]
        bkey = self.thing(book)["identity"]["field"]
        ckey = self.thing(child)["identity"]["field"]
        bfields = {f: f"$.payload.{f}" if f != "subject" else "$.payload.book_fields.subject"
                   for f in self.thing(book)["required"]}
        wfields = {f: f"$.payload.{f}" for f in self.thing(work)["required"]}
        claimed = f"results.CC_CLAIM_{up(book)}_IDENTITY_V0.{bkey}"
        chain = [
            (self.validate(src), {"work_fields": {"literal": wfields}, "book_fields": {"literal": bfields},
                                  "barcode": f"payload.{ckey}"}, {}, "ledger:things/book/required"),
            # Pre-check: the copy's barcode is free before the first refusable claim (doctrine order).
            (self.require_free(child), {ckey: f"payload.{ckey}"}, {}, "doctrine:order"),
            (self.claim_keyed(book), {f: f"payload.{f}" for f in self.thing(book)["identity"]["from"]}, {},
             f"ledger:things/{book}/identity"),
            (self.claim_plain(child), {ckey: f"payload.{ckey}"}, {}, f"ledger:things/{child}/identity"),
            (self.claim_keyed(work), {**{f: f"payload.{f}" for f in self.thing(work)["identity"]["from"]},
                                      "work_fields": {"literal": wfields}},
             {"ALREADY_EXISTS": "next"}, f"ledger:things/{work}/identity"),
            (self.write_record(book, op_name), {bkey: claimed, "book_fields": {"literal": bfields}}, {}, src),
            (self.write_record(child, op_name), {bkey: claimed, ckey: f"payload.{ckey}"}, {}, src),
        ]
        request = {"title": "string", "author": "string", "publication_year": "integer",
                   "book_fields": "object", ckey: "string"}
        return chain, request, f"$.{claimed}"

    def register_into_existing_parent(self, op_name, op):
        src = f"ledger:operations/{op_name}"
        book = op["thing"]
        work = self.thing(book)["belongs_to"]
        bkey = self.thing(book)["identity"]["field"]
        bfields = {f: f"$.payload.{f}" for f in self.thing(book)["required"]}
        wfields = {f: f"$.payload.{f}" for f in self.thing(work)["required"]}
        claimed = f"results.CC_CLAIM_{up(book)}_IDENTITY_V0.{bkey}"
        chain = [
            (self.validate(src), {"book_fields": {"literal": bfields}, "work_fields": {"literal": wfields}},
             {}, "ledger:things/book/required"),
            (self.resolve_keyed(work), {f: f"payload.{f}" for f in self.thing(work)["identity"]["from"]}, {},
             src + "/precondition"),
            (self.claim_keyed(book), {f: f"payload.{f}" for f in self.thing(book)["identity"]["from"]}, {},
             f"ledger:things/{book}/identity"),
            (self.write_record(book, op_name), {bkey: claimed, "book_fields": {"literal": bfields}}, {}, src),
        ]
        request = {f: ty for f, ty in self.thing(book)["required"].items()}
        return chain, request, f"$.{claimed}"

    def create(self, op_name, op):
        src = f"ledger:operations/{op_name}"
        t = self.thing(op["thing"])
        parent = t["belongs_to"]
        pkey, key = self.thing(parent)["identity"]["field"], t["identity"]["field"]
        chain = [
            (self.resolve_plain(parent), {pkey: f"payload.{pkey}"}, {}, src + "/precondition"),
            (self.claim_plain(op["thing"]), {key: f"payload.{key}"}, {}, f"ledger:things/{op['thing']}/identity"),
            (self.write_record(op["thing"], op_name), {pkey: f"payload.{pkey}", key: f"payload.{key}"}, {}, src),
        ]
        return chain, {pkey: "string", key: "string"}, f"$.payload.{key}"

    def transition(self, op_name, op):
        src = f"ledger:operations/{op_name}"
        t = self.thing(op["thing"])
        key, store = t["identity"]["field"], self.records(op["thing"])
        cc = self.add(Component(
            self.code("CC", op_name), f"Mark a {head(op['thing'])} {op['to_state']}",
            [Step("set_record_state", MUTABLE, "UPDATE_WHERE", store,
                  {"filter": {"literal": {key: f"$.inputs.{key}", "state": up(op["from_state"])}},
                   "updates": {"literal": {"state": up(op["to_state"])}}},
                  {"matched_keys": "capability_result.matched_keys",
                   "updated_count": "capability_result.updated_count", "result_status": "result_status"}, src)],
            {key: "string"}, {"updated_count": "integer"}, src))
        return [(cc, {key: f"payload.{key}"}, {}, src)], {key: "string"}, f"$.payload.{key}"

    def update(self, op_name, op):
        """Correct a record. Same identity: write in place. Changed identity: claim the new one
        (a duplicate refuses), then re-key (doctrine order: every refusal before the first write)."""
        src = f"ledger:operations/{op_name}"
        name = op["thing"]
        book = self.thing(name)
        key, ident = book["identity"]["field"], book["identity"]["from"]
        work = book["belongs_to"]
        wkey, wfrom = self.thing(work)["identity"]["field"], self.thing(work)["identity"]["from"]
        changing = [f for f in op.get("may_change", []) if f in ident]
        moves_work = [f for f in changing if f in wfrom]
        on_change = op.get("on_identity_change", {})
        if moves_work and on_change.get("work") != "follows":
            self.conflicts.append(f"{op_name}: may change {', '.join(moves_work)}, which form the {work} key; "
                                  f"on_identity_change.work is not decided.")
        schema = {f: {"required": True, "type": ty} for f, ty in book["required"].items()}
        fields = {key: "$.results.form_updated_identity_key.updated_identity_key",
                  **{f: f"$.inputs.updated_fields.{f}" for f in book["required"]},
                  **{k: f"$.results.read_book_record.book_record.{k}" for k in op["keeps"]},
                  wkey: f"$.results.form_{wkey}.{wkey}"}
        rules = [{"field": "violations", "op": "eq", "value": []}] + \
                [{"field": f, "op": "neq", "value": []} for f in book.get("non_empty", [])]
        params = {"violations": "$.results.check_corrected_record.violations",
                  **{f: f"$.results.assemble_updated_record.updated_record.{f}" for f in book.get("non_empty", [])}}
        store, registry = self.records(name), self.registry(name)
        prepare = self.add(Component(
            self.code("CC", op_name),
            "Assembles a corrected edition record, under the identity and work its corrected description names",
            [Step("read_book_record", MUTABLE, "READ", store, {"key": f"inputs.{key}"},
                  {"book_record": "capability_result.value", "result_status": "result_status"}, src),
             Step("form_updated_identity_key", self.key_ct(name), None, None,
                  {f: f"inputs.updated_fields.{f}" for f in ident},
                  {"updated_identity_key": f"capability_result.{key}"}, f"ledger:things/{name}/identity"),
             Step(f"form_{wkey}", self.key_ct(work), None, None,
                  {f: f"inputs.updated_fields.{f}" for f in wfrom},
                  {wkey: f"capability_result.{wkey}"}, src + "/on_identity_change/work"),
             Step("assemble_updated_record", CT + "CT_PURE_ASSEMBLE_RECORD_V0", None, None,
                  {"fields": {"literal": fields}}, {"updated_record": "capability_result.record"}, src + "/keeps"),
             Step("check_corrected_record", CT + "CT_PURE_VALIDATE_RECORD_STRUCTURE_V0", None, None,
                  {"record": "results.assemble_updated_record.updated_record", "schema": {"literal": schema}},
                  {"violations": "capability_result.violations"}, f"ledger:things/{name}/required"),
             Step("refuse_incomplete_correction", CT + "CT_PURE_VALIDATE_PARAMETER_RULES_V0", None, None,
                  {"parameters": {"literal": params}, "rules": {"literal": rules}},
                  {"valid": "capability_result.valid"}, f"ledger:things/{name}/required")],
            {key: "string", "updated_fields": "object"},
            {"updated_record": "object", "updated_identity_key": "string"}, src))
        same = self.add(Component(
            f"{self.ns}CC_CONFIRM_{up(name)}_IDENTITY_UNCHANGED_V0",
            f"Confirm a corrected {name} keeps its identity",
            [Step("compare_identity", CT + "CT_PURE_COMPARE_EQUAL_V0", None, None,
                  {"left": f"inputs.{key}", "right": "inputs.updated_identity_key"},
                  {"identity_unchanged": "capability_result.is_equal"}, src),
             Step("require_identity_unchanged", CT + "CT_PURE_VALIDATE_PARAMETER_RULES_V0", None, None,
                  {"parameters": {"literal": {"identity_unchanged": "$.results.compare_identity.identity_unchanged"}},
                   "rules": {"literal": [{"field": "identity_unchanged", "op": "eq", "value": True}]}},
                  {"valid": "capability_result.valid"}, src)],
            {key: "string", "updated_identity_key": "string"}, {"valid": "boolean"}, src))
        in_place = self.add(Component(
            f"{self.ns}CC_WRITE_CORRECTED_{up(name)}_RECORD_V0",
            f"Write a corrected {name} record under its unchanged identity",
            [Step("write_updated_record", MUTABLE, "WRITE", store,
                  {"key": f"inputs.{key}", "value": "inputs.updated_record"},
                  {"result_status": "result_status"}, src)],
            {key: "string", "updated_record": "object"}, {"result_status": "string"}, src))
        child = next(n for n, t in self.l["things"].items() if t.get("belongs_to") == name)
        rekey = self.add(Component(
            f"{self.ns}CC_REKEY_{up(name)}_V0",
            f"Move a {name} to its new identity: its record, its {self.thing(child)['plural']}, and its claim",
            [Step(f"write_{name}_record", MUTABLE, "WRITE", store,
                  {"key": "inputs.updated_identity_key", "value": "inputs.updated_record"},
                  {"result_status": "result_status"}, src + "/on_identity_change"),
             # An edition may hold no copies: matching none is not a failure here.
             Step(f"move_{head(child)}_records", MUTABLE, "UPDATE_WHERE", self.records(child),
                  {"filter": {"literal": {key: f"$.inputs.{key}"}},
                   "updates": {"literal": {key: "$.inputs.updated_identity_key"}}},
                  {"updated_count": "capability_result.updated_count", "result_status": "result_status"},
                  src + "/on_identity_change/children", routing={"VIOLATION": "continue"}),
             Step(f"remove_old_{name}_record", MUTABLE, "DELETE", store, {"key": f"inputs.{key}"},
                  {"result_status": "result_status"}, src + "/on_identity_change"),
             Step("release_old_identity", REGISTRY, "DEREGISTER", registry, {"key_or_address": f"inputs.{key}"},
                  {"result_status": "result_status"}, src + "/on_identity_change/old_identity")],
            {key: "string", "updated_identity_key": "string", "updated_record": "object"},
            {"updated_count": "integer"}, src))
        trail_code = short(self.trail())
        prep = f"results.{short(prepare)}"
        chain = [
            (self.resolve_plain(name), {key: f"payload.{key}"}, {}, src + "/precondition"),
            (prepare, {key: f"payload.{key}", "updated_fields": "payload.updated_fields"}, {}, src),
            (same, {key: f"payload.{key}", "updated_identity_key": f"{prep}.updated_identity_key"},
             {"VIOLATION": f"CC_CLAIM_{up(name)}_IDENTITY_V0"},
             src),
            (in_place, {key: f"payload.{key}", "updated_record": f"{prep}.updated_record"},
             {"SUCCESS": trail_code}, src),
            (self.claim_keyed(name), {f: f"payload.updated_fields.{f}" for f in ident}, {},
             f"ledger:operations/{op_name}/refuse_if"),
            (self.claim_keyed(work), {**{f: f"payload.updated_fields.{f}" for f in wfrom},
                                      "work_fields": {"literal": {f: f"$.payload.updated_fields.{f}" for f in wfrom}}},
             {"ALREADY_EXISTS": "next"}, src + "/on_identity_change/work"),
            (rekey, {key: f"payload.{key}", "updated_identity_key": f"{prep}.updated_identity_key",
                     "updated_record": f"{prep}.updated_record"}, {}, src + "/on_identity_change"),
        ]
        return chain, {key: "string", "updated_fields": "object"}, f"$.payload.{key}"

    def details(self, op_name, op):
        src = f"ledger:operations/{op_name}"
        book = self.thing(op["thing"])
        key = book["identity"]["field"]
        work, child = op["with"]
        ckey_parent = key
        cc = self.add(Component(
            f"{self.ns}CC_ASSEMBLE_BOOK_DETAILS_V0",
            "Assembles an edition, the physical copies of it, and the record of the work it belongs to",
            [Step("read_book_record", MUTABLE, "READ", self.records(op["thing"]), {"key": f"inputs.{key}"},
                  {"book_record": "capability_result.value", "result_status": "result_status"}, src),
             Step("form_work_key", self.key_ct(work), None, None,
                  {f: f"results.read_book_record.book_record.{f}" for f in self.thing(work)["identity"]["from"]},
                  {"work_key": "capability_result.work_key"}, f"ledger:things/{work}/identity"),
             Step("read_work_record", MUTABLE, "READ", self.records(work),
                  {"key": "results.form_work_key.work_key"},
                  {"work_record": "capability_result.value"}, src, routing={"NOT_FOUND": "continue"}),
             Step("select_copy_records", MUTABLE, "SELECT", self.records(child), {},
                  {"records": "capability_result.records", "result_status": "result_status"}, src),
             Step("select_copies_of_book", f"{self.ns}CT_PURE_SELECT_RECORDS_V0", None, None,
                  {"source": "results.select_copy_records.records",
                   "filter": {"literal": {ckey_parent: f"$.inputs.{key}"}}},
                  {"copies_held": "capability_result.extracted"}, src)],
            {key: "string"}, {"work_record": "object", "book_record": "object", "copies_held": "array"}, src))
        return [(cc, {key: f"payload.{key}"}, {}, src)], {key: "string"}, f"$.payload.{key}"

    def search(self, op_name, op):
        src = f"ledger:operations/{op_name}"
        group_key = self.thing(op["group_by"])["identity"]["field"]
        exclude = {k: up(self.thing(op["thing"])["states"][0]) for k in op["always_exclude"]}
        if op.get("nothing_found") == "empty":
            self.unrealized.append(
                f"{op_name}: nothing_found=empty needs a filter that answers empty and supports "
                "presence criteria; the available filter (CT_PURE_FILTER_RECORDS_V0) refuses an empty "
                "result. Realized with that filter; an empty search is still refused.")
        cc = self.add(Component(
            self.code("CC", op_name),
            "Selects the registered editions matching a subject or title and groups them under their work",
            [Step("select_book_records", MUTABLE, "SELECT", self.records(op["thing"]), {},
                  {"records": "capability_result.records", "result_status": "result_status"}, src),
             Step("select_registered_books", f"{self.ns}CT_PURE_SELECT_RECORDS_V0", None, None,
                  {"source": "results.select_book_records.records", "filter": {"literal": exclude}},
                  {"registered_books": "capability_result.extracted"}, src + "/always_exclude"),
             Step("select_matching_books", CT + "CT_PURE_FILTER_RECORDS_V0", None, None,
                  {"source": "results.select_registered_books.registered_books", "filter": "inputs.search_criteria"},
                  {"matching_books": "capability_result.extracted"}, src),
             Step("group_editions_by_work", f"{self.ns}CT_PURE_GROUP_RECORDS_V0", None, None,
                  {"source": "results.select_matching_books.matching_books", "attribute": {"literal": group_key}},
                  {"matching_works": "capability_result.grouped"}, src + "/group_by")],
            {"search_criteria": "object"}, {"matching_works": "array", "matching_books": "array"}, src))
        return ([(cc, {"search_criteria": "payload.search_criteria"}, {}, src)],
                {"search_criteria": "object"}, "$.payload.search_criteria")

    # -- the published surface, carried --------------------------------------------------------

    def path(self, op_name, f):
        """Where a request carries a field: where the existing act's callers already put it."""
        wf = self.code("WF", op_name)
        for r in self.base.get("step_bindings") or []:
            if r["owner"] == wf:
                for p in re.findall(r"payload\.([\w.]+)", json.dumps(r["bound_to"])):
                    if p.split(".")[-1] == f:
                        return "payload." + p
        return "payload." + f

    def request_shape(self, op_name, generated):
        """An existing act's request fields, as its callers send them; a new act's, as generated."""
        wf = self.code("WF", op_name)
        inn = next((r["node"] for r in self.base.get("execution_topology") or []
                    if r["workflow"] == wf and r["node_type"] == "IN"), None)
        if inn is None:
            return generated
        return {f["field"]: (f["type"], f["required"]) for f in self.base["interface_fields"]
                if short(f["artifact"]) == short(inn)}

    def carried_trail(self, part):
        """The keys of the part's trail records, and whether its trail is one stream or one per subject."""
        store = self.store(f"{up(part)}_OPERATIONS", APPENDONLY, "ledger:trail + doctrine:storage", part=part)
        spec = {"occurrence": "occurrence", "time": None, "stream": "store", "store": store}
        cc = next((r["cc_code"] for r in self.base.get("cc_composition") or []
                   if r.get("operation") == "APPEND" and r.get("store") == store), None)
        if cc is None:
            return spec
        rows = [r for r in self.base["cc_composition"] if r["cc_code"] == cc]
        clock = next((r["step_name"] for r in rows if r["capability"] == CLOCK), None)
        binds = self.base["step_bindings"]
        literals = [r["bound_to"]["literal"] for r in binds
                    if (r["owner"] == cc and r["field"] == "fields") or r["field"] == "occurrence_fields"
                    if isinstance(r["bound_to"], dict) and isinstance(r["bound_to"].get("literal"), dict)]
        for lit in literals:
            for k, v in lit.items():
                if clock and isinstance(v, str) and f"results.{clock}.timestamp" in v:
                    spec["time"] = k
                if isinstance(v, str) and (v.isupper() or v.endswith(".occurrence")):
                    spec["occurrence"] = k
        streams = [r["bound_to"] for r in binds if r["field"] == "stream_id" and r["owner"].split("::")[-1].startswith("WF_")
                   and any(c["node"] == short(cc) for c in self.base["execution_topology"]
                           if c["workflow"] == r["owner"])]
        if streams and not any(isinstance(b, dict) for b in streams):
            spec["stream"] = "subject"
        return spec

    # -- components of a participant domain -----------------------------------------------------

    def moment(self, op_name=None, extra=()):
        """Record a moment on the part's trail, in the record shape the trail already holds.

        `extra` names further fields a moment records; such a moment is its own component, so the
        workflow can end it at its own exit and announce its own event.
        """
        part, src = self.sub, "ledger:trail"
        spec = self.carried_trail(part)
        trail = self.l["trail"]
        subject = trail.get("subject")
        fields = list(trail["records"]) + list(extra)
        record = {spec["occurrence"]: "$.inputs.occurrence", **{f: f"$.inputs.{f}" for f in fields}}
        steps = []
        if spec["time"]:
            steps.append(Step("read_now", CLOCK, "NOW", None, {}, {"timestamp": "capability_result.timestamp"},
                              "doctrine:own_values"))
            record[spec["time"]] = "$.results.read_now.timestamp"
        stream = f"inputs.{subject}" if spec["stream"] == "subject" else {"literal": spec["store"]}
        steps += [Step("assemble_occurrence", CT + "CT_PURE_ASSEMBLE_RECORD_V0", None, None,
                       {"fields": {"literal": record}}, {"record": "capability_result.record"}, src),
                  Step("append_occurrence", APPENDONLY, "APPEND", spec["store"],
                       {"record": "results.assemble_occurrence.record", "stream_id": stream},
                       {"sequence_number": "capability_result.sequence_number"}, src + " + doctrine:own_values")]
        inputs = {"occurrence": "string", **{f: ("string", "NO") for f in fields}}
        if spec["stream"] == "subject":
            inputs[subject] = "string"
        if extra:
            return self.add(Component(
                f"{self.ns}CC_RECORD_REPEATED_{up(op_name)}_V0",
                f"Record a repeated {op_name} on the {part}'s trail, with the details it submitted",
                steps, inputs, {"sequence_number": "integer"}, f"ledger:operations/{op_name}/on_repeat"))
        return self.add(Component(
            f"{self.ns}CC_RECORD_{up(part)}_MOMENT_V0", f"Record a moment on the {part}'s own trail",
            steps, inputs, {"sequence_number": "integer"}, src))

    def moment_binds(self, op_name, occurrence, values):
        return {"occurrence": {"literal": occurrence}, **values}

    def submission(self, op_name, fields):
        """Bind a submission: the object the callers already send, or one assembled from the request."""
        paths = {f: self.path(op_name, f) for f in fields}
        parents = {p.rsplit(".", 1)[0] for p in paths.values()}
        if len(parents) == 1 and parents != {"payload"}:
            return parents.pop()
        return {"literal": {f: "$." + p for f, p in paths.items()}}

    def resolve_record(self, thing_name):
        """Resolve an identity and read the record it names; refuses when no record is held."""
        t = self.thing(thing_name)
        key, src = t["identity"]["field"], f"ledger:things/{thing_name}/identity"
        return self.add(Component(
            f"{self.ns}CC_RESOLVE_{up(thing_name)}_V0",
            f"Answer which {thing_name} a {key.replace('_', ' ')} names, and refuse when none does",
            [Step("resolve_identity", REGISTRY, "RESOLVE", self.registry(thing_name), {"key_or_address": f"inputs.{key}"},
                  {"target_ref": "capability_result.target_ref"}, src),
             Step(f"read_{thing_name}", MUTABLE, "READ", self.records(thing_name), {"key": f"inputs.{key}"},
                  {"value": "capability_result.value"}, src)],
            {key: "string"}, {"value": "object"}, src), part=self.thing_part[thing_name])

    def require_stated(self, op_name, f):
        src = f"ledger:operations/{op_name}/required"
        return self.add(Component(
            f"{self.ns}CC_REQUIRE_{up(f)}_TO_{up(op_name)}_V0",
            f"Refuse to {op_name} without {f.replace('_', ' ')}, before anything is read or recorded",
            [Step(f"require_{f}_stated", CT + "CT_PURE_VALIDATE_PARAMETER_RULES_V0", None, None,
                  {"parameters": {"literal": {f: f"$.inputs.{f}"}},
                   "rules": {"literal": [{"field": f, "op": "not_null"}, {"field": f, "op": "neq", "value": ""}]}},
                  {"valid": "capability_result.valid"}, src)],
            {f: ("string", "NO")}, {"valid": "boolean"}, src))

    # -- operation patterns of a participant domain: each returns (chain, request) ---------------

    def register(self, op_name, op):
        """Admit a thing in its first state. A repeat of its identity records the repeat and changes nothing."""
        src = f"ledger:operations/{op_name}"
        name = op["thing"]
        t = self.thing(name)
        key = t["identity"]["field"]
        fields = list(t["required"]) + list(t.get("defaults", {}))
        schema = {f: {"type": ty, "required": True} for f, ty in t["required"].items()}
        validate = self.add(Component(
            f"{self.ns}CC_VALIDATE_{up(op_name)}_V0",
            f"Refuse a {op_name.split()[0]} lacking what a {name} requires",
            [Step("read_submission", CT + "CT_PURE_VALIDATE_RECORD_STRUCTURE_V0", None, None,
                  {"record": "inputs.submission", "schema": {"literal": schema}},
                  {"violations": "capability_result.violations"}, f"ledger:things/{name}/required"),
             Step("refuse_incomplete_submission", CT + "CT_PURE_VALIDATE_PARAMETER_RULES_V0", None, None,
                  {"parameters": {"literal": {"violations": "$.results.read_submission.violations"}},
                   "rules": {"literal": [{"field": "violations", "op": "eq", "value": []}]}},
                  {"valid": "capability_result.valid"}, f"ledger:things/{name}/required")],
            {"submission": "object"}, {"valid": "boolean"}, f"ledger:things/{name}/required"))
        if t.get("defaults"):
            self.unrealized.append(
                f"{op_name}: defaults {t['defaults']} apply when a request leaves a field out. No platform "
                "transform supplies a default; the entrance supplies them for callers outside, and a direct "
                "request that leaves one out records none.")
        write = self.add(Component(
            self.code("CC", op_name), f"Write a new {name} in its first state",
            [Step(f"assemble_{name}", CT + "CT_PURE_ASSEMBLE_RECORD_V0", None, None,
                  {"fields": {"literal": {**{f: f"$.inputs.submission.{f}" for f in fields},
                                          "state": up(t["states"][0])}}},
                  {"record": "capability_result.record"}, f"ledger:things/{name}/states + doctrine:own_values"),
             Step(f"write_{name}", MUTABLE, "WRITE", self.records(name),
                  {"key": f"inputs.{key}", "value": f"results.assemble_{name}.record"},
                  {"result_status": "result_status"}, src)],
            {key: "string", "submission": "object"}, {"result_status": "string"}, src))
        repeat = op["on_repeat"]
        moment, again = self.moment(), self.moment(op_name, extra=repeat["records"])
        occurrence = up(self.l["announces"][op_name][0])
        sub = self.submission(op_name, fields)
        subject = {key: self.path(op_name, key)}
        chain = [
            (validate, {"submission": sub}, {}, f"ledger:things/{name}/required"),
            (self.claim_plain(name), subject, {"ALREADY_EXISTS": short(again)}, f"{src}/on_repeat"),
            (write, {**subject, "submission": sub}, {}, src),
            (moment, self.moment_binds(op_name, occurrence, subject), {"SUCCESS": "EXIT_COMPLETED"}, "ledger:trail"),
            (again, self.moment_binds(op_name, occurrence, {**subject, **{f: self.path(op_name, f) for f in repeat["records"]}}),
             {"SUCCESS": "EXIT_REPEATED"}, f"{src}/on_repeat"),
        ]
        return chain, self.request_shape(op_name, {f: "string" for f in fields})

    def decide(self, op_name, op):
        """Move a thing from one state to a decided one, under the rules the business holds."""
        src = f"ledger:operations/{op_name}"
        name = op["thing"]
        t = self.thing(name)
        key, by = t["identity"]["field"], op["decided_by"]
        decides = [o for o in self.l["operations"].values() if o.get("kind") == "decide" and o["thing"] == name]
        outcomes = [up(o["to_state"]) for o in decides]
        changes = [f for f in op["may_change"] if f != "state"]
        steps = [Step("read_state_admits_decision", CT + "CT_PURE_VALIDATE_SET_MEMBERSHIP_V0", None, None,
                      {"value": "inputs.current_state", "allowed_set": {"literal": [up(op["from_state"])]}},
                      {"is_member": "capability_result.is_member"}, src + "/from_state + doctrine:rules_held"),
                 Step("read_outcome_admitted", CT + "CT_PURE_VALIDATE_SET_MEMBERSHIP_V0", None, None,
                      {"value": "inputs.decision", "allowed_set": {"literal": outcomes}},
                      {"is_member": "capability_result.is_member"}, f"ledger:things/{name}/states + doctrine:rules_held")]
        if op.get("not_self"):
            steps += [Step(f"compare_{by}_to_{name}", CT + "CT_PURE_COMPARE_EQUAL_V0", None, None,
                           {"left": f"inputs.{by}", "right": f"inputs.{key}"},
                           {"is_self": "capability_result.is_equal"}, src + "/not_self"),
                      Step("refuse_self_decision", CT + "CT_PURE_VALIDATE_PARAMETER_RULES_V0", None, None,
                           {"parameters": {"literal": {"is_self": f"$.results.compare_{by}_to_{name}.is_self"}},
                            "rules": {"literal": [{"field": "is_self", "op": "eq", "value": False}]}},
                           {"valid": "capability_result.valid"}, src + "/not_self + doctrine:rules_held")]
        steps += [Step(f"assemble_decided_{name}", CT + "CT_PURE_ASSEMBLE_RECORD_V0", None, None,
                       {"fields": {"literal": {key: f"$.inputs.{key}", "state": "$.inputs.decision",
                                               **{f: f"$.inputs.{f}" for f in changes}}}},
                       {"record": "capability_result.record"}, src + "/may_change"),
                  Step(f"write_decided_{name}", MUTABLE, "UPDATE", self.records(name),
                       {"key": f"inputs.{key}", "updates": f"results.assemble_decided_{name}.record"},
                       {"result_status": "result_status"}, src + "/may_change")]
        decide = self.add(Component(
            f"{self.ns}CC_RECORD_{up(name)}_DECISION_V0",
            f"Refuse a decision the business does not admit, and record the one it does, changing only "
            f"{', '.join(['state'] + changes)}",
            steps, {"current_state": "string", "decision": "string", key: "string",
                    **{f: (f"string", "YES" if f == by else "NO") for f in changes}},
            {"result_status": "string"}, src))
        resolve = self.resolve_record(name)
        chain = [(self.require_stated(op_name, f), {f: self.path(op_name, f)}, {}, src + "/required")
                 for f in op.get("required", [])]
        values = {f: self.path(op_name, f) for f in [key] + changes}
        chain += [
            (resolve, {key: self.path(op_name, key)}, {}, src + "/precondition"),
            (decide, {"current_state": f"results.{short(resolve)}.value.state",
                      "decision": {"literal": up(op["to_state"])}, **values}, {}, src),
            (self.moment(), self.moment_binds(op_name, up(self.l["announces"][op_name][0]), values), {}, "ledger:trail"),
        ]
        return chain, self.request_shape(op_name, {f: "string" for f in values})

    def list(self, op_name, op):
        """Answer the things matching the criteria the caller names. A read is trailed before it reads."""
        src = f"ledger:operations/{op_name}"
        name = op["thing"]
        t = self.thing(name)
        crit = op["criteria"]
        if op.get("nothing_found") == "empty":
            self.unrealized.append(
                f"{op_name}: nothing_found=empty needs a filter that answers empty; the platform's "
                "(CT_PURE_FILTER_RECORDS_V0) refuses an empty result. Realized with it; listing a state no "
                f"{name} is in is still refused.")
        listing = self.add(Component(
            self.code("CC", op_name), f"Answer every {name} matching the named {', '.join(crit)}",
            [Step(f"select_{name}_records", MUTABLE, "SELECT", self.records(name), {},
                  {"records": "capability_result.records"}, src),
             Step(f"select_matching_{t['plural'].replace(' ', '_')}", CT + "CT_PURE_FILTER_RECORDS_V0", None, None,
                  {"source": f"results.select_{name}_records.records",
                   "filter": {"literal": {c: f"$.inputs.{c}" for c in crit}}},
                  {t["plural"].replace(" ", "_"): "capability_result.extracted"}, src + "/criteria")],
            {c: "string" for c in crit}, {t["plural"].replace(" ", "_"): "array"}, src))
        chain = [(self.moment(), self.moment_binds(op_name, up(op_name), {}), {}, "ledger:trail + doctrine:order"),
                 (listing, {c: self.path(op_name, c) for c in crit}, {}, src)]
        return chain, self.request_shape(op_name, {c: "string" for c in crit})

    def create_held(self, op_name, op):
        """Create a thing for a holder another part keeps, with the values the business fixes."""
        src = f"ledger:operations/{op_name}"
        name = op["thing"]
        t = self.thing(name)
        held = t["held_by"]
        holder = held["thing"]
        hkey = self.thing(holder)["identity"]["field"]
        idt, key = t["identity"], t["identity"]["field"]
        resolve = self.resolve_record(holder)
        rv = f"results.{short(resolve)}.value"
        require = self.add(Component(
            f"{self.ns}CC_REQUIRE_{up(held['requires_state'])}_{up(holder)}_V0",
            f"Refuse a {name} for a {holder} who is not {held['requires_state']}, before anything is claimed",
            [Step(f"require_{holder}_{held['requires_state']}", CT + "CT_PURE_VALIDATE_SET_MEMBERSHIP_V0", None, None,
                  {"value": "inputs.state", "allowed_set": {"literal": [up(held["requires_state"])]}},
                  {"is_member": "capability_result.is_member"}, f"ledger:things/{name}/held_by + doctrine:own_values")],
            {"state": "string"}, {"is_member": "boolean"}, f"ledger:things/{name}/held_by"))
        form = self.add(Component(
            f"{self.ns}CC_FORM_{up(name)}_IDENTITY_V0", f"Form a {name}'s identity from its {held['field']}",
            [Step(f"form_{key}", CT + "CT_PURE_GENERATE_ID_V0", None, None,
                  {"data": f"inputs.{held['field']}", "prefix": {"literal": idt["prefix"]}},
                  {"id": "capability_result.id"}, f"ledger:things/{name}/identity + doctrine:own_values")],
            {held["field"]: "string"}, {"id": "string"}, f"ledger:things/{name}/identity"))
        chain = [
            (resolve, {hkey: self.path(op_name, hkey)}, {}, f"ledger:reads_other_part + {src}/precondition"),
            (require, {"state": f"{rv}.state"}, {}, f"ledger:things/{name}/held_by"),
            (form, {held["field"]: f"{rv}.{hkey}"}, {}, f"ledger:things/{name}/identity"),
        ]
        derived_binds, claims = {}, []
        for value, d in t.get("derived", {}).items():
            dsrc = f"ledger:things/{name}/derived/{value}"
            ct = f"{self.ns}CT_PURE_DERIVE_{up(name)}_{up(value)}_V0"
            if not any(r["code"] == ct for r in self.base["new_artifacts"]):
                self.unrealized.append(f"{op_name}: {value} is derived by a rule no carried transform realizes.")
                continue
            derive = self.add(Component(
                f"{self.ns}CC_DERIVE_{up(name)}_{up(value)}_V0",
                f"Derive the {name}'s {value} from the {d['from'].replace('_', ' ')} supplied with the request",
                [Step(f"derive_{value}", ct, None, None, {d["from"]: f"inputs.{d['from']}"},
                      {value: f"capability_result.{value}"}, dsrc + " + carried:realization")],
                {d["from"]: "string"}, {value: "string"}, dsrc))
            chain.append((derive, {d["from"]: self.path(op_name, d["from"])}, {}, dsrc))
            derived_binds[value] = f"results.{short(derive)}.{value}"
            if d.get("unique"):
                chain.append((self.require_free(name, value), {value: derived_binds[value]}, {}, "doctrine:order"))
                claims.append((self.claim_plain(name, value), {value: derived_binds[value]}, {}, dsrc + "/unique"))
        wid = f"results.{short(form)}.id"
        write = self.add(Component(
            self.code("CC", op_name), f"Record a new {name} with the values the business fixes",
            [Step(f"assemble_{name}", CT + "CT_PURE_ASSEMBLE_RECORD_V0", None, None,
                  {"fields": {"literal": {held["field"]: f"$.inputs.{held['field']}", **t["fixed"]}}},
                  {"record": "capability_result.record"}, f"ledger:things/{name}/fixed + doctrine:own_values"),
             Step(f"write_{name}", MUTABLE, "WRITE", self.records(name),
                  {"key": f"inputs.{key}", "value": f"results.assemble_{name}.record"},
                  {"result_status": "result_status"}, src)],
            {key: "string", held["field"]: "string"}, {"result_status": "string"}, src))
        chain += [(self.claim_plain(name), {key: wid}, {}, f"ledger:things/{name}/identity")] + claims
        chain += [
            (write, {key: wid, held["field"]: f"{rv}.{hkey}"}, {}, src),
            (self.moment(), self.moment_binds(op_name, up(self.l["announces"][op_name][0]),
                                              {key: wid, held["field"]: f"{rv}.{hkey}"}), {}, "ledger:trail"),
        ]
        return chain, self.request_shape(op_name, {hkey: "string", **{d["from"]: "string" for d in t.get("derived", {}).values()}})

    # -- workflows -----------------------------------------------------------------------------

    def workflow(self, op_name, op):
        if op["kind"] in PARTICIPANT_KINDS:
            # A participant acts for themselves: no authorization step, and each pattern records its
            # own moments, because what a moment holds differs by operation.
            chain, request = getattr(self, op["kind"])(op_name, op)
            self.workflows.append((op_name, op, chain, request, self.sub))
            announced = list(self.l.get("announces", {}).get(op_name, []))
            if op.get("on_repeat", {}).get("announces"):
                announced.append(op["on_repeat"]["announces"])
            for event in announced:
                self.events[event] = (op_name, request, True)
                self.event_part[event] = self.sub
            return
        chain, request, subject = getattr(self, op["kind"])(op_name, op)
        auth, trail = self.authorize(), self.trail()
        entry = (trail, {"staff_id": "payload.staff_id", "operation": {"literal": up(op_name)},
                         "record": {"literal": {"operation": up(op_name), "staff_id": "$.payload.staff_id",
                                                "subject": subject}}}, {}, "ledger:trail")
        head_ = [(auth, {"staff_credentials": "payload.staff_credentials"}, {}, "ledger:actor")]
        # A workflow answers with its last component's output, so a read is trailed before it reads
        # (doctrine order, realization constraint). A change is trailed after it succeeds.
        reads = op["kind"] in ("details", "search")
        chain = head_ + ([entry] + chain if reads else chain + [entry])
        self.workflows.append((op_name, op, chain, request, self.sub))
        for event in self.l["announces"].get(op_name, []):
            owner = event.rsplit(" ", 1)[0] == op.get("thing")
            if owner or event not in self.events:
                if owner or not self.events.get(event, (None, None, False))[2]:
                    self.events[event] = (op_name, request, owner)
                    self.event_part[event] = self.sub

    def run(self):
        for part in self.parts:
            self.enter(part)
            for op_name, op in self.l["operations"].items():
                self.workflow(op_name, op)
        return self.render()

    # -- rendering -----------------------------------------------------------------------------

    def render_reach(self, reg, row, reach):
        """An act that runs another part's component consults that part's bindings, and only reads."""
        if not reach:
            return
        reg.setdefault("declared_reach", [])
        writes = {"WRITE", "UPDATE", "UPDATE_WHERE", "REGISTER", "DEREGISTER", "DELETE", "APPEND"}
        for wf, parts in reach.items():
            for op_name, _, chain, _, part in self.workflows:
                if self.code("WF", op_name) != wf:
                    continue
                for comp_code, *_ in chain:
                    comp = self.components[comp_code]
                    if comp.part != part and any(s.operation in writes for s in comp.steps):
                        self.conflicts.append(f"{op_name}: writes {comp.part}'s records through {short(comp_code)}; "
                                              f"reads_other_part says it never writes them.")
            row("declared_reach", "ledger:reads_other_part + doctrine:binding", act=wf,
                consults=sorted(self.rb_of(p) for p in parts))

    def render_offering(self, reg, row, artifact, field):
        """Each public act's entrance and answer, carried from the composition callers already use."""
        acts = self.top.get("public_acts")
        if not acts:
            return
        reg.setdefault("transport_bindings", [])
        tb = self.base.get("transport_bindings") or []
        src = "ledger:public_acts + carried:surface"
        for op_name, public in acts.items():
            if op_name == "from":
                continue
            wf = self.code("WF", op_name)
            ti = sorted({r["artifact"] for r in tb if r["direction"] == "INGRESS" and r["handler_target"] == wf})
            te = sorted({r["artifact"] for r in tb if r["direction"] == "EGRESS" and r.get("operation") == public})
            if not ti or not te:
                self.unrealized.append(f"{op_name}: offered as {public}; the composition has no entrance for it, "
                                       "and a new entrance is not generated yet.")
                continue
            for code in ti + te:
                art = next(r for r in self.base["new_artifacts"] if r["code"] == code)
                reg["new_artifacts"].append({**art, "_from": src})
                reg["interface_fields"] += [{**f, "_from": src} for f in self.base["interface_fields"]
                                            if f["artifact"] == code]
                reg["artifact_properties"] += [{**r, "_from": src} for r in self.base["artifact_properties"]
                                               if r["artifact"] == code]
                reg["transport_bindings"] += [{**r, "_from": src} for r in tb if r["artifact"] == code]

    def render_vocabulary(self, reg, row, artifact):
        """A named set of values the business fixes, in the shape the composition already declares."""
        for name, t in self.things.items():
            for f, allowed in t.get("allowed_values", {}).items():
                code = f"{self.ns}VOCAB_{up(head(name))}_{up(f)}_V0"
                src = f"ledger:things/{name}/allowed_values"
                shape = next((r for r in self.base.get("vocabulary_extensions") or []
                              if r["vocabulary_code"] == code), {})
                artifact("VOCAB", code, f"The {f} values the business names for a {name}", src,
                         self.thing_part[name])
                reg.setdefault("vocabulary_extensions", [])
                for v in allowed["named"]:
                    row("vocabulary_extensions", src + (" + carried:surface" if shape else ""),
                        vocabulary_code=code, extends=shape.get("extends"), group=shape.get("group", f),
                        casing=shape.get("casing", "UPPER_SNAKE"), names_kind=shape.get("names_kind"),
                        value=up(v), meaning=up(v))

    def render(self):
        reg = {k: [] for k in ("new_artifacts", "rb_declarations", "execution_topology", "cc_composition",
                               "step_bindings", "interface_fields", "implementation_bindings",
                               "runtime_policies", "artifact_properties", "structure_stores",
                               "test_cases", "test_case_values")}
        row = lambda r, src, **c: reg[r].append({**c, "_from": src})

        def artifact(family, code, summary, src, part):
            row("new_artifacts", src, family=family, code=code, summary=summary,
                owner_subdomain=part, status="NEW")

        def field(art, direction, name, typ, src, meaning=None, fmt=None, required="YES", default=None):
            extra = {"format": fmt} if fmt else {}
            row("interface_fields", src, artifact=art, direction=direction, field=name, type=typ,
                required=required, default=default, meaning=meaning or name.replace("_", " "), **extra)

        store_users = {}
        a = self.top["actor"]
        first = next(iter(self.parts))
        if a.get("authorization") == "none":
            artifact("AC", self.ac, f"The {a['name']} who acts for themselves", "ledger:actor", first)
            row("artifact_properties", "ledger:actor", artifact=self.ac, property="type", value=a["kind"])
            for f, spec in a["attributes"].items():
                typ, dflt = (spec, None) if isinstance(spec, str) else (spec["type"], spec.get("default"))
                field(self.ac, "ATTRIBUTE", f, typ, "ledger:actor", required="YES" if dflt is None else "NO",
                      default=dflt)
        else:
            artifact("AC", self.ac, f"The actor whose authorization every {first} operation binds",
                     "ledger:actor", first)
            row("artifact_properties", "ledger:actor", artifact=self.ac, property="type", value=a["kind"])
            field(self.ac, "ATTRIBUTE", "staff_id", "string", "ledger:actor")
            field(self.ac, "ATTRIBUTE", "authorized", "boolean", "ledger:actor", required="NO", default=False)
        clocked = {c.part for c in self.components.values() for s in c.steps if s.capability == CLOCK}
        mechanisms = {p: [MUTABLE, REGISTRY, APPENDONLY] + ([CLOCK] if p in clocked else []) for p in self.parts}
        for part in self.parts:
            structure, rb = self.structure_of(part), self.rb_of(part)
            artifact("STRUCTURE", structure, f"Declares the stores the {part} owns and the paths they occupy",
                     "doctrine:storage", part)
            row("artifact_properties", "doctrine:storage", artifact=structure, property="layer", value="DOMAINS")
            artifact("RB", rb, f"Binds the {part}'s workflows to the stores and mechanisms they use",
                     "doctrine:binding", part)
            for cs in mechanisms[part]:
                if cs == CLOCK:
                    row("runtime_policies", "doctrine:binding", rb_code=rb, capability=cs, key="precision",
                        value="seconds")
                else:
                    row("runtime_policies", "doctrine:binding", rb_code=rb, capability=cs, key="structure",
                        value=structure)

        for comp in self.components.values():
            artifact("CC", comp.code, comp.summary, comp.src, comp.part)
            for f, t in comp.inputs.items():
                t, req = (t, "YES") if isinstance(t, str) else t
                field(comp.code, "INPUT", f, t, comp.src, required=req)
            for f, t in comp.outputs.items():
                field(comp.code, "OUTPUT", f, t, "doctrine:interface")
            for i, s in enumerate(comp.steps, 1):
                kind = "CS" if s.capability.startswith(CS) else "CT"
                last = i == len(comp.steps)
                routing = {st: s.routing.get(st, "continue" if (st == "SUCCESS" and not last) else "exit")
                           for st in STATUSES[s.operation if kind == "CS" else None]}
                produces = list(s.outs)
                row("cc_composition", s.src, cc_code=comp.code, step=str(i), step_name=s.name,
                    capability=s.capability, kind=kind, operation=s.operation, store=s.store,
                    consumes=list(s.ins) or None, produces=produces, routing=routing, interpreted_by=None,
                    semantic_status="SUCCESS",
                    interface={"in": {f: f for f in s.ins}, "out": {f: f for f in produces}})
                for f, b in s.ins.items():
                    row("step_bindings", s.src, owner=comp.code, step=s.name, direction="INPUT", field=f, bound_to=b)
                for f, b in s.outs.items():
                    row("step_bindings", s.src, owner=comp.code, step=s.name, direction="OUTPUT", field=f,
                        bound_to=b)
                if s.store:
                    store_users.setdefault(s.store, set()).add(comp.code)

        authorized = a.get("authorization") != "none"
        reach = {}
        for op_name, op, chain, request, part in self.workflows:
            wf, inn, src = self.code("WF", op_name), self.code("IN", op_name), f"ledger:operations/{op_name}"
            artifact("WF", wf, f"The governed sequence that performs: {op_name}", src, part)
            artifact("IN", inn, f"A request to {op_name}", src, part)
            if authorized:
                field(inn, "INPUT", "staff_credentials", "object", "ledger:actor")
            for f, t in request.items():
                t, req = (t, "YES") if isinstance(t, str) else t
                field(inn, "INPUT", f, t, src if req == "YES" or authorized else src + " + carried:surface",
                      required=req)
            if authorized:
                field(inn, "INPUT", "staff_id", "string", "ledger:actor")
            row("rb_declarations", "doctrine:binding", rb_code=self.rb_of(part), binds_wf=wf,
                cs_bindings=mechanisms[part], storage_structure=self.structure_of(part))
            row("artifact_properties", "ledger:actor", artifact=wf, property="actor_context", value=self.ac)
            announces = self.parts[part].get("announces", {})
            events = [self.code("EV", e) for e in announces.get(op_name, [])]
            if events:
                row("artifact_properties", "ledger:announces", artifact=wf, property="emit.EXIT_COMPLETED",
                    value=events)
            repeat = op.get("on_repeat", {}).get("announces")
            if repeat:
                row("artifact_properties", f"{src}/on_repeat", artifact=wf, property="emit.EXIT_REPEATED",
                    value=[self.code("EV", repeat)])
            row("execution_topology", "doctrine:order", workflow=wf, node=short(inn), node_type="IN",
                routing={"ACK": short(chain[0][0]), "NACK": "EXIT_REJECTED"})
            exits = ["EXIT_COMPLETED", "EXIT_REJECTED"]
            for i, (comp_code, binds, overrides, bsrc) in enumerate(chain):
                comp = self.components[comp_code]
                if comp.part != part:
                    reach.setdefault(wf, set()).add(comp.part)
                nxt = short(chain[i + 1][0]) if i + 1 < len(chain) else "EXIT_COMPLETED"
                routing = {}
                for st in comp.exits():
                    target = overrides.get(st, nxt if st == "SUCCESS" else "EXIT_REJECTED")
                    routing[st] = nxt if target == "next" else target
                    if routing[st].startswith("EXIT_") and routing[st] not in exits:
                        exits.append(routing[st])
                row("execution_topology", bsrc if overrides else "doctrine:order", workflow=wf,
                    node=short(comp_code), node_type="CC", routing=routing)
                for f, b in binds.items():
                    row("step_bindings", bsrc, owner=wf, step=short(comp_code), direction="INPUT", field=f,
                        bound_to=b)
            for x in exits:
                row("execution_topology", "doctrine:order", workflow=wf, node=x, node_type="EXIT", routing=None)

        for event, (op_name, request, _) in self.events.items():
            part = self.event_part[event]
            explicit = self.parts[part].get("events", {})
            ev = self.code("EV", event)
            artifact("EV", ev, f"A {event}", "ledger:announces", part)
            carries = explicit.get(event, {}).get("carries")
            if carries is None:
                ident = [f for f in request if f in {t["identity"]["field"] for t in self.things.values()}]
                carries = ident + ["staff_id"]
            types = {**{f: ty for t in self.things.values() for f, ty in t.get("required", {}).items()}}
            for f in carries:
                field(ev, "OUTPUT", f, types.get(f, "string"), "ledger:announces" if event in explicit
                      else "doctrine:interface")
            field(ev, "OUTPUT", "timestamp", "string", "doctrine:interface", "When the moment occurred",
                  fmt="date-time")

        for name, (cs, src, part, path) in self.stores.items():
            row("structure_stores", src, store_name=name, storage_type=short(cs),
                proposed_path=path or f"{self.top['domain']}/{part}/{name.lower()}"
                                      f"{'.jsonl' if cs in (REGISTRY, APPENDONLY) else '.json'}",
                used_by=", ".join(sorted(store_users.get(name, ()))), structure=self.structure_of(part))

        self.render_reach(reg, row, reach)
        self.render_offering(reg, row, artifact, field)
        self.render_vocabulary(reg, row, artifact)

        # Realization inventory: code-backed transforms, carried with their cases.
        for r in self.base["new_artifacts"]:
            if r["family"] == "CT":
                reg["new_artifacts"].append({**r, "_from": "carried:realization"})
                reg["interface_fields"] += [{**f, "_from": "carried:realization"}
                                            for f in self.base["interface_fields"] if f["artifact"] == r["code"]]
        for name in CARRIED_REGISTERS:
            reg[name] += [{**r, "_from": "carried:realization"} for r in self.base.get(name) or []]
        reg["_unrealized"] = self.unrealized
        reg["_conflicts"] = self.conflicts
        return reg


DOCTRINE = yaml.safe_load(open(Path(__file__).with_name("doctrine.yaml")))["rules"]


def check_doctrine(reg):
    """Refuse a row citing a doctrine rule doctrine.yaml does not state."""
    cited = {m for rows in reg.values() if isinstance(rows, list) for r in rows if isinstance(r, dict)
             for m in re.findall(r"doctrine:(\w+)", str(r.get("_from", "")))}
    unknown = sorted(cited - set(DOCTRINE))
    if unknown:
        sys.exit(f"cited doctrine not stated in doctrine.yaml: {unknown}")
    return reg


def load_p7(path):
    text = open(path).read()
    return yaml.safe_load(re.findall(r"```yaml\n(.*?)```", text, re.S)[0])["registers"]


if __name__ == "__main__":
    ledger = yaml.safe_load(open(sys.argv[1]))
    json.dump(check_doctrine(Domain(ledger, load_p7(sys.argv[2])).run()), sys.stdout, indent=1)
