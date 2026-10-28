"""Derive a whole domain's P7 registers from a closed-shape decision ledger.

Patterns build components (CCs) and workflows (WFs) from ledger operations. A small renderer turns
them into P7 rows. Every row carries `_from`: the ledger entry, or the doctrine rule, it comes from.

Doctrine (cited by name in `_from`):
  order       authorize; validate; preconditions and pre-checks; claims; writes; trail last.
              A read is trailed before it reads: a workflow answers with its last component.
              After the first claim that can refuse, nothing else may refuse: every later claim
              is pre-checked by resolving it first.
  storage     a thing with identity gets a registry; a thing with states or records a mutable
              store; the trail an append-only store
  naming      codes from the author's names; records and registries by the thing's head noun
  interface   a request carries the actor's credentials and id plus the operation's inputs; an
              event carries the operation's identifying inputs, the actor and the time, unless the
              ledger lists what it carries
  binding     one resource binding per subdomain names every storage mechanism it uses
              (interface, continued) every component declares an output; a write-only one
              outputs what its write reports
  reuse       one component per (thing, purpose); workflows share them

Realization inventory: transforms whose implementation is code (key formation, select, group) are
carried from the baseline with their test cases. The ledger decides what they compute; it does not
author their implementation.

Usage: generate_domain.py <ledger.yaml> <baseline P7> > generated.json
"""
import json
import re
import sys

import yaml

CS = "capability_side_effects::"
CT = "capability_transforms::"
MUTABLE, REGISTRY, APPENDONLY = (CS + "CS_MUTABLE_JSON_V0", CS + "CS_REGISTRY_V0",
                                 CS + "CS_APPENDONLY_JSONL_V0")
STATUSES = {
    "READ": ["SUCCESS", "NOT_FOUND", "VIOLATION", "BACKEND_ERROR"],
    "RESOLVE": ["SUCCESS", "NOT_FOUND", "VIOLATION", "BACKEND_ERROR"],
    "REGISTER": ["SUCCESS", "ALREADY_EXISTS", "VIOLATION", "BACKEND_ERROR"],
    "WRITE": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    "UPDATE_WHERE": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    "APPEND": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    "SELECT": ["SUCCESS", "BACKEND_ERROR"],
    "DELETE": ["SUCCESS", "NOT_FOUND", "VIOLATION", "BACKEND_ERROR"],
    "DEREGISTER": ["SUCCESS", "NOT_FOUND", "VIOLATION", "BACKEND_ERROR"],
    None: ["SUCCESS", "VIOLATION"],
}
NATIVE_OUT = {"READ": "value", "RESOLVE": None, "REGISTER": None}
# Realization inventory carried from the baseline: the code-backed transforms.
CARRIED_REGISTERS = ("implementation_bindings", "test_cases", "test_case_values")


def up(name):
    return name.upper().replace(" ", "_")


def head(name):
    return name.split()[-1]


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
        self.l, self.base = ledger, baseline
        self.ns = ledger["domain"] + "::"
        self.sub = ledger["subdomain"]
        self.components = {}
        self.workflows = []
        self.stores = {}
        self.events = {}
        self.unrealized = []
        self.conflicts = []
        a = ledger["actor"]
        self.ac = self.code("AC", a["name"])
        self.rb = f"{self.ns}RB_{up(self.sub)}_BINDINGS_V0"
        self.structure = f"{self.ns}STRUCTURE_{up(self.sub)}_STORAGE_V0"
        self.trail_store = f"{up(self.sub)}_OPERATIONS"

    def code(self, family, name):
        return f"{self.ns}{family}_{up(name)}_V0"

    def thing(self, name):
        return self.l["things"][name]

    def add(self, comp):
        self.components.setdefault(comp.code, comp)
        return comp.code

    def store(self, name, cs, src):
        self.stores.setdefault(name, (cs, src))
        return name

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

    def registry(self, thing_name):
        t = self.thing(thing_name)
        key = t["identity"]["field"]
        name = (f"{up(thing_name)}_IDENTITY_REGISTRY" if "from" in t["identity"]
                else f"{up(head(thing_name))}_{up(key)}_REGISTRY")
        return self.store(name, REGISTRY, f"ledger:things/{thing_name}/identity + doctrine:storage")

    def records(self, thing_name):
        t = self.thing(thing_name)
        return self.store(up(t["plural"]), MUTABLE, f"ledger:things/{thing_name} + doctrine:storage")

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

    def claim_plain(self, thing_name):
        t = self.thing(thing_name)
        key, src = t["identity"]["field"], f"ledger:things/{thing_name}/identity"
        reg = self.registry(thing_name)
        return self.add(Component(
            f"{self.ns}CC_CLAIM_{up(head(thing_name))}_{up(key)}_V0",
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

    def require_free(self, thing_name):
        """Pre-check that an identity is unclaimed. Refuses with VIOLATION when it is held, so the
        workflow's status names the refusal (a workflow reports its last component's status)."""
        t = self.thing(thing_name)
        key, src = t["identity"]["field"], "doctrine:order"
        h = head(thing_name)
        return self.add(Component(
            f"{self.ns}CC_REQUIRE_{up(h)}_{up(key)}_FREE_V0",
            f"Refuse when a {h}'s {key} is already held, before any identity is claimed",
            [Step("resolve_identity", REGISTRY, "RESOLVE", self.registry(thing_name),
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

    # -- workflows -----------------------------------------------------------------------------

    def workflow(self, op_name, op):
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
        self.workflows.append((op_name, op, chain, request))
        for event in self.l["announces"].get(op_name, []):
            owner = event.rsplit(" ", 1)[0] == op.get("thing")
            if owner or event not in self.events:
                if owner or not self.events.get(event, (None, None, False))[2]:
                    self.events[event] = (op_name, request, owner)

    def run(self):
        for op_name, op in self.l["operations"].items():
            self.workflow(op_name, op)
        return self.render()

    # -- rendering -----------------------------------------------------------------------------

    def render(self):
        reg = {k: [] for k in ("new_artifacts", "rb_declarations", "execution_topology", "cc_composition",
                               "step_bindings", "interface_fields", "implementation_bindings",
                               "runtime_policies", "artifact_properties", "structure_stores",
                               "test_cases", "test_case_values")}
        row = lambda r, src, **c: reg[r].append({**c, "_from": src})

        def artifact(family, code, summary, src):
            row("new_artifacts", src, family=family, code=code, summary=summary,
                owner_subdomain=self.sub, status="NEW")

        def field(art, direction, name, typ, src, meaning=None, fmt=None, required="YES", default=None):
            extra = {"format": fmt} if fmt else {}
            row("interface_fields", src, artifact=art, direction=direction, field=name, type=typ,
                required=required, default=default, meaning=meaning or name.replace("_", " "), **extra)

        store_users = {}
        a = self.l["actor"]
        artifact("AC", self.ac, f"The actor whose authorization every {self.sub} operation binds", "ledger:actor")
        row("artifact_properties", "ledger:actor", artifact=self.ac, property="type", value=a["kind"])
        field(self.ac, "ATTRIBUTE", "staff_id", "string", "ledger:actor")
        field(self.ac, "ATTRIBUTE", "authorized", "boolean", "ledger:actor", required="NO", default=False)
        artifact("STRUCTURE", self.structure, f"Declares the stores the {self.sub} owns and the paths they occupy",
                 "doctrine:storage")
        row("artifact_properties", "doctrine:storage", artifact=self.structure, property="layer", value="DOMAINS")
        artifact("RB", self.rb, f"Binds the {self.sub}'s workflows to the stores and mechanisms they use",
                 "doctrine:binding")
        for cs in (MUTABLE, REGISTRY, APPENDONLY):
            row("runtime_policies", "doctrine:binding", rb_code=self.rb, capability=cs, key="structure",
                value=self.structure)

        for comp in self.components.values():
            artifact("CC", comp.code, comp.summary, comp.src)
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

        for op_name, op, chain, request in self.workflows:
            wf, inn, src = self.code("WF", op_name), self.code("IN", op_name), f"ledger:operations/{op_name}"
            artifact("WF", wf, f"The governed sequence that performs: {op_name}", src)
            artifact("IN", inn, f"A request to {op_name}", src)
            field(inn, "INPUT", "staff_credentials", "object", "ledger:actor")
            for f, t in request.items():
                field(inn, "INPUT", f, t, src)
            field(inn, "INPUT", "staff_id", "string", "ledger:actor")
            row("rb_declarations", "doctrine:binding", rb_code=self.rb, binds_wf=wf,
                cs_bindings=[MUTABLE, REGISTRY, APPENDONLY], storage_structure=self.structure)
            row("artifact_properties", "ledger:actor", artifact=wf, property="actor_context", value=self.ac)
            events = [self.code("EV", e) for e in self.l["announces"].get(op_name, [])]
            if events:
                row("artifact_properties", "ledger:announces", artifact=wf, property="emit.EXIT_COMPLETED",
                    value=events)
            row("execution_topology", "doctrine:order", workflow=wf, node=short(inn), node_type="IN",
                routing={"ACK": short(chain[0][0]), "NACK": "EXIT_REJECTED"})
            for i, (comp_code, binds, overrides, bsrc) in enumerate(chain):
                comp = self.components[comp_code]
                nxt = short(chain[i + 1][0]) if i + 1 < len(chain) else "EXIT_COMPLETED"
                routing = {}
                for st in comp.exits():
                    target = overrides.get(st, nxt if st == "SUCCESS" else "EXIT_REJECTED")
                    routing[st] = nxt if target == "next" else target
                row("execution_topology", bsrc if overrides else "doctrine:order", workflow=wf,
                    node=short(comp_code), node_type="CC", routing=routing)
                for f, b in binds.items():
                    row("step_bindings", bsrc, owner=wf, step=short(comp_code), direction="INPUT", field=f,
                        bound_to=b)
            for x in ("EXIT_COMPLETED", "EXIT_REJECTED"):
                row("execution_topology", "doctrine:order", workflow=wf, node=x, node_type="EXIT", routing=None)

        explicit = self.l.get("events", {})
        for event, (op_name, request, _) in self.events.items():
            ev = self.code("EV", event)
            artifact("EV", ev, f"A {event}", "ledger:announces")
            carries = explicit.get(event, {}).get("carries")
            if carries is None:
                ident = [f for f in request if f in {t["identity"]["field"] for t in self.l["things"].values()}]
                carries = ident + ["staff_id"]
            types = {**{f: ty for t in self.l["things"].values() for f, ty in t.get("required", {}).items()}}
            for f in carries:
                field(ev, "OUTPUT", f, types.get(f, "string"), "ledger:announces" if event in explicit
                      else "doctrine:interface")
            field(ev, "OUTPUT", "timestamp", "string", "doctrine:interface", "When the moment occurred",
                  fmt="date-time")

        for name, (cs, src) in self.stores.items():
            row("structure_stores", src, store_name=name, storage_type=short(cs),
                proposed_path=f"{self.l['domain']}/{self.sub}/{name.lower()}"
                              f"{'.jsonl' if cs in (REGISTRY, APPENDONLY) else '.json'}",
                used_by=", ".join(sorted(store_users.get(name, ()))), structure=self.structure)

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


def load_p7(path):
    text = open(path).read()
    return yaml.safe_load(re.findall(r"```yaml\n(.*?)```", text, re.S)[0])["registers"]


if __name__ == "__main__":
    ledger = yaml.safe_load(open(sys.argv[1]))
    json.dump(Domain(ledger, load_p7(sys.argv[2])).run(), sys.stdout, indent=1)
