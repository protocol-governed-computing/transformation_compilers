"""Compose a whole domain's P7 from a decision ledger, out of building blocks.

`doc/BUILDING_BLOCKS.md` is the design. A block is one step, realized by one platform capability.
A component is a sequence of blocks; a workflow is a sequence of components joined by three
operators: `then` (the next component on success), `branch` (a named status to another path) and
`end` (a named ending and what it announces).

The composer reads the questions each operation answers and selects blocks from them. No
operation names a pattern: an operation says what it does (`create`, `change`, `read`, `query`)
and to which things, and the rest of its answers decide the blocks. The doctrine
(`doctrine.yaml`) groups blocks into components and orders them.

Rendering, the carried surface and the realization inventory are `generate_domain.Domain`'s.

Run as `tc decision derive <ledger.yaml> <baseline P7>`.
"""
import json
import re

import yaml

from transformation.decision import seal
from transformation.decision.ledger import refuse
from transformation.decision.base import (APPENDONLY, CLOCK, CT, MUTABLE, REGISTRY, Component, Domain, Step,
                             check_doctrine, head, load_p7, noun, short, up)

RULES = CT + "CT_PURE_VALIDATE_PARAMETER_RULES_V0"
MEMBER = CT + "CT_PURE_VALIDATE_SET_MEMBERSHIP_V0"
SHAPE = CT + "CT_PURE_VALIDATE_RECORD_STRUCTURE_V0"
EQUAL = CT + "CT_PURE_COMPARE_EQUAL_V0"
ASSEMBLE = CT + "CT_PURE_ASSEMBLE_RECORD_V0"
FILTER = CT + "CT_PURE_FILTER_RECORDS_V0"
GENERATE = CT + "CT_PURE_GENERATE_ID_V0"
LOOKUP = CT + "CT_PURE_LOOKUP_V0"
# Conditions a ledger may name, and the carried transform that decides each.
CONDITIONS = {"unused_for_days": "CT_PURE_EVALUATE_INACTIVITY_V0"}


# -- the twelve blocks: each returns the steps that realize it -----------------------------------

def check_rules(name, params, rules, src):
    return [Step(name, RULES, None, None, {"parameters": {"literal": params}, "rules": {"literal": rules}},
                 {"valid": "capability_result.valid"}, src)]


def check_member(name, value, allowed, src):
    return [Step(name, MEMBER, None, None, {"value": value, "allowed_set": {"literal": allowed}},
                 {"is_member": "capability_result.is_member"}, src)]


def check_member_of(name, value, allowed, src):
    """check: a value is a member of a set an earlier step answered."""
    return [Step(name, MEMBER, None, None, {"value": value, "allowed_set": allowed},
                 {"is_member": "capability_result.is_member"}, src)]


def check_rules_of(name, params, rules, src):
    """check: parameters satisfy rules an earlier step answered."""
    return [Step(name, RULES, None, None, {"parameters": params, "rules": rules},
                 {"valid": "capability_result.valid"}, src)]


def look_up(name, table, key, out, src):
    return [Step(name, LOOKUP, None, None, {"map": {"literal": table}, "key": key},
                 {out: "capability_result.result"}, src)]


def now(src):
    return [Step("read_now", CLOCK, "NOW", None, {}, {"timestamp": "capability_result.timestamp"}, src)]


def check_shape(name, record, schema, src):
    return [Step(name, SHAPE, None, None, {"record": record, "schema": {"literal": schema}},
                 {"violations": "capability_result.violations"}, src)]


def check_equal(name, left, right, out, src):
    return [Step(name, EQUAL, None, None, {"left": left, "right": right}, {out: "capability_result.is_equal"},
                 src)]


def form(name, transform, ins, out, result, src):
    return [Step(name, transform, None, None, ins, {out: f"capability_result.{result}"}, src)]


def resolve(name, registry, key, src, routing=None):
    return [Step(name, REGISTRY, "RESOLVE", registry, {"key_or_address": key},
                 {"target_ref": "capability_result.target_ref", "result_status": "result_status"}, src, routing)]


def read(name, store, key, out, src, routing=None):
    return [Step(name, MUTABLE, "READ", store, {"key": key},
                 {out: "capability_result.value", "result_status": "result_status"}, src, routing)]


def query(name, store, src):
    return [Step(name, MUTABLE, "SELECT", store, {}, {"records": "capability_result.records",
                                                      "result_status": "result_status"}, src)]


def narrow(name, transform, source, criteria, out, src):
    return [Step(name, transform, None, None, {"source": source, "filter": criteria},
                 {out: "capability_result.extracted"}, src)]


def group(name, transform, source, attribute, out, src):
    return [Step(name, transform, None, None, {"source": source, "attribute": {"literal": attribute}},
                 {out: "capability_result.grouped"}, src)]


def claim(name, registry, key, target, src, routing=None):
    return [Step(name, REGISTRY, "REGISTER", registry,
                 {"key": key, "target_cs": {"literal": MUTABLE}, "target_ref": {"literal": target}},
                 {"address": "capability_result.address", "result_status": "result_status"}, src, routing)]


def release(name, registry, key, src):
    return [Step(name, REGISTRY, "DEREGISTER", registry, {"key_or_address": key},
                 {"result_status": "result_status"}, src)]


def write(rec, store, key, fields, src, fields_src=None):
    return [Step(f"assemble_{rec}", ASSEMBLE, None, None, {"fields": fields},
                 {rec: "capability_result.record"}, fields_src or src),
            Step(f"write_{rec}", MUTABLE, "WRITE", store, {"key": key, "value": f"results.assemble_{rec}.{rec}"},
                 {"result_status": "result_status"}, src)]


def change_where(name, store, criteria, updates, src, routing=None):
    return [Step(name, MUTABLE, "UPDATE_WHERE", store,
                 {"filter": {"literal": criteria}, "updates": {"literal": updates}},
                 {"matched_keys": "capability_result.matched_keys",
                  "updated_count": "capability_result.updated_count", "result_status": "result_status"},
                 src, routing)]


def remove(name, store, key, src):
    return [Step(name, MUTABLE, "DELETE", store, {"key": key}, {"result_status": "result_status"}, src)]


def record(store, fields, timed, stream, actor, src):
    steps = []
    if timed:
        fields = {**fields, timed: "$.results.read_now.timestamp"}
        steps.append(Step("read_now", CLOCK, "NOW", None, {}, {"timestamp": "capability_result.timestamp"},
                          "doctrine:own_values"))
    append = {"record": "results.assemble_occurrence.record", "stream_id": stream}
    if actor:
        append["actor_id"] = actor
    return steps + [Step("assemble_occurrence", ASSEMBLE, None, None, {"fields": {"literal": fields}},
                         {"record": "capability_result.record"}, src),
                    Step("append_occurrence", APPENDONLY, "APPEND", store, append,
                         {"sequence_number": "capability_result.sequence_number"}, src + " + doctrine:own_values")]


# -- the composer ---------------------------------------------------------------------------------

class Composer(Domain):
    """Selects blocks from each operation's answers and groups them into components."""

    def __init__(self, ledger, baseline):
        super().__init__(ledger, baseline)
        self.authorized = ledger["actor"].get("authorization") != "none"

    # -- small helpers ---------------------------------------------------------------------------

    def key_of(self, name):
        return self.thing(name)["identity"]["field"]

    def formed(self, name):
        """How a thing's identity is formed: `key` (a key transform over attributes), `id` (generated
        from a holder), or None (supplied by the request)."""
        idt = self.thing(name)["identity"]
        if "fixed" in idt:
            return "fixed"
        if "from" not in idt:
            return None
        return "id" if "prefix" in idt else "key"

    def parent_of(self, name):
        return self.thing(name).get("belongs_to")

    def at(self, op_name, f):
        """A request field, as a workflow binds it, where the callers already send it."""
        p = self.path(op_name, f)
        if p == "payload." + f:
            p = self.nested(op_name, f) or p
        return p

    def nested(self, op_name, f):
        """A field the request carries inside its one object, when it carries no field of that name."""
        shape = self.request_shape(op_name, {})
        actor = {"staff_credentials"}
        objects = [k for k, (t, _) in ((k, v if isinstance(v, tuple) else (v, "YES")) for k, v in shape.items())
                   if t == "object" and k not in actor]
        if shape and f not in shape and len(objects) == 1:
            return f"payload.{objects[0]}.{f}"
        return None

    def submission(self, op_name, fields):
        paths = {f: self.at(op_name, f) for f in fields}
        parents = {p.rsplit(".", 1)[0] for p in paths.values()}
        if len(parents) == 1 and parents != {"payload"}:
            return parents.pop()
        return {"literal": {f: "$." + p for f, p in paths.items()}}

    def type_of(self, f):
        """A field's type, as the things that require it declare it."""
        return next((t["required"][f] for t in self.things.values() if f in t.get("required", {})), "string")

    def fields_of(self, name):
        t = self.thing(name)
        return list(t.get("required", {})) + list(t.get("defaults", {}))

    # -- components ------------------------------------------------------------------------------

    def authorize(self):
        a, src = self.top["actor"], "ledger:actor"
        return self.add(Component(
            f"{self.ns}CC_CONFIRM_{up(a['role'])}_AUTHORIZED_V0",
            f"Confirm the {a['role']} member may perform the operation",
            [Step("confirm_authorization", RULES, None, None,
                  {"parameters": "inputs.staff_credentials", "rules": {"literal": a["authorized_when"]}},
                  {"is_authorized": "capability_result.valid"}, src)],
            {"staff_credentials": "object"}, {"is_authorized": "boolean"}, src))

    def check_submission(self, op_name, names):
        """check: what each created thing requires, before any identity is claimed."""
        src = f"ledger:operations/{op_name}/required"
        steps, inputs, params, rules = [], {}, {}, []
        for name in names:
            t = self.thing(name)
            if t.get("required"):
                inp = f"{head(name)}_fields" if len(names) > 1 else "submission"
                schema = {f: {"type": ty, "required": True} for f, ty in t["required"].items()}
                steps += check_shape(f"check_{head(name)}_fields", f"inputs.{inp}", schema,
                                     f"ledger:things/{name}/required")
                inputs[inp] = "object"
                params[f"{head(name)}_violations"] = f"$.results.check_{head(name)}_fields.violations"
                rules.append({"field": f"{head(name)}_violations", "op": "eq", "value": []})
                for f in t.get("non_empty", []):
                    params[f] = f"$.inputs.{inp}.{f}"
                    rules.append({"field": f, "op": "neq", "value": []})
            elif not self.formed(name):
                key = self.key_of(name)
                inputs[key] = ("string", "NO")
                params[key] = f"$.inputs.{key}"
                rules.insert(0, {"field": key, "op": "neq", "value": ""})
        if not steps:
            return None
        steps += check_rules("refuse_incomplete_submission", params, rules, src)
        return self.add(Component(f"{self.ns}CC_CHECK_{up(op_name)}_SUBMISSION_V0",
                                  f"Refuse a request to {op_name} that lacks what it requires",
                                  steps, inputs, {"valid": "boolean"}, src))

    def check_stated(self, op_name, f):
        src = f"ledger:operations/{op_name}/required"
        return self.add(Component(
            f"{self.ns}CC_REQUIRE_{up(f)}_TO_{up(op_name)}_V0",
            f"Refuse to {op_name} without {f.replace('_', ' ')}",
            check_rules(f"require_{f}_stated", {f: f"$.inputs.{f}"},
                        [{"field": f, "op": "not_null"}, {"field": f, "op": "neq", "value": ""}], src),
            {f: ("string", "NO")}, {"valid": "boolean"}, src))

    def by_attributes(self, op_name, name):
        """Whether a request names a thing by the attributes its key is formed from, not by the key."""
        return self.formed(name) in ("key", "id") and not self.carries(op_name, self.key_of(name))

    def carries(self, op_name, f):
        """Whether the request carries a field, where its callers already send it."""
        shape = self.request_shape(op_name, {})
        return f in shape or self.path(op_name, f) != "payload." + f or bool(self.nested(op_name, f))

    def resolver(self, name, by_attributes=False):
        """resolve, and read the record: the precondition that a thing exists."""
        key, src = self.key_of(name), f"ledger:things/{name}/identity"
        steps, inputs = [], {}
        if by_attributes and self.formed(name) == "id":
            steps += self.form_id(name, src)
            inputs, ref = {f: self.type_of(f) for f in self.id_from(name)}, f"results.form_{key}.{key}"
        elif by_attributes:
            attrs = self.thing(name)["identity"]["from"]
            steps += form(f"form_{key}", self.key_ct(name), {f: f"inputs.{f}" for f in attrs}, key, key, src)
            inputs, ref = {f: self.type_of(f) for f in attrs}, f"results.form_{key}.{key}"
        else:
            inputs, ref = {key: "string"}, f"inputs.{key}"
        steps += resolve("resolve_identity", self.registry(name), ref, src)
        steps += read(f"read_{head(name)}_record", self.records(name), ref, f"{head(name)}_record", src)
        code = f"CC_RESOLVE_{up(name)}_V0" if by_attributes else f"CC_RESOLVE_{up(name)}_IDENTITY_V0"
        return self.add(Component(self.ns + code,
                                  f"Answer which {name} its identity names, and refuse when none does",
                                  steps, inputs, {f"{head(name)}_record": "object"}, src),
                        part=self.thing_part[name])

    def free(self, name, value=None):
        """resolve, check: a later claim is pre-checked before the first claim that can refuse."""
        key = value or self.key_of(name)
        return self.add(Component(
            f"{self.ns}CC_REQUIRE_{up(head(name))}_{up(noun(name, key))}_FREE_V0",
            f"Refuse when a {head(name)}'s {key.replace('_', ' ')} is already held, before any is claimed",
            resolve("resolve_identity", self.registry(name, value), f"inputs.{key}", "doctrine:order",
                    {"SUCCESS": "continue", "NOT_FOUND": "continue"}) +
            check_rules("require_unheld", {"held": "$.results.resolve_identity.result_status"},
                        [{"field": "held", "op": "eq", "value": "NOT_FOUND"}], "doctrine:order"),
            {key: "string"}, {"valid": "boolean"}, "doctrine:order"))

    def claimer(self, name, value=None):
        """form, claim: take a thing's identity, or a value it holds uniquely. A reused identity
        also writes the record when it is new."""
        t = self.thing(name)
        idt = t["identity"]
        key = value or idt["field"]
        src = f"ledger:things/{name}/" + (f"derived/{value}" if value else "identity")
        how = None if value else self.formed(name)
        steps, inputs, outputs = [], {}, {}
        if how == "key":
            steps += form(f"form_{key}", self.key_ct(name), {f: f"inputs.{f}" for f in idt["from"]}, key, key, src)
            inputs, ref = {f: self.type_of(f) for f in idt["from"]}, f"results.form_{key}.{key}"
        elif how == "id":
            steps += self.form_id(name, src)
            inputs, ref = {f: self.type_of(f) for f in self.id_from(name)}, f"results.form_{key}.{key}"
        else:
            inputs, ref = {key: "string"}, f"inputs.{key}"
        reuse = not value and idt.get("on_duplicate") == "reuse"
        steps += claim(f"claim_{noun(name, key)}", self.registry(name, value), ref, self.records(name), src,
                       {"SUCCESS": "continue"} if reuse else None)
        if reuse:
            rec = f"{head(name)}_record"
            inputs[f"{head(name)}_fields"] = "object"
            steps += write(rec, self.records(name), ref, f"inputs.{head(name)}_fields", src)
        outputs[key] = "string"
        if how:
            outputs[key] = "string"
        else:
            outputs["address"] = "string"
        code = (f"CC_CLAIM_{up(name)}_IDENTITY_V0" if how else
                f"CC_CLAIM_{up(head(name))}_{up(noun(name, key))}_V0")
        return self.add(Component(self.ns + code, f"Claim a {name}'s {key.replace('_', ' ')}",
                                  steps, inputs, outputs, src))

    def deriver(self, name, value):
        d = self.thing(name)["derived"][value]
        src = f"ledger:things/{name}/derived/{value}"
        if d.get("rule") == "generated id":
            fields = d["from"]
            return self.add(Component(
                f"{self.ns}CC_FORM_{up(name)}_{up(value)}_V0", f"Form a {name}'s {value.replace('_', ' ')}",
                form(f"form_{value}", GENERATE, {"data": {"literal": {f: f"$.inputs.{f}" for f in fields}},
                                                 "prefix": {"literal": d["prefix"]}}, value, "id",
                     src + " + doctrine:own_values"),
                {f: self.type_of(f) for f in fields}, {value: "string"}, src))
        ct = f"{self.ns}CT_PURE_DERIVE_{up(name)}_{up(value)}_V0"
        if not any(r["code"] == ct for r in self.base["new_artifacts"]):
            self.unrealized.append(f"{name}: {value} is derived by a rule no carried transform realizes.")
        return self.add(Component(
            f"{self.ns}CC_DERIVE_{up(name)}_{up(value)}_V0",
            f"Derive a {name}'s {value} from the {d['from'].replace('_', ' ')} supplied",
            form(f"derive_{value}", ct, {d["from"]: f"inputs.{d['from']}"}, value, value,
                 src + " + carried:realization"),
            {d["from"]: "string"}, {value: "string"}, src))

    def writer(self, op_name, name):
        """write: a new record in the thing's first state, naming its parent or holder."""
        t = self.thing(name)
        key, src = self.key_of(name), f"ledger:operations/{op_name}"
        rec = f"{head(name)}_record"
        fixed_key = t["identity"].get("fixed")
        steps, inputs = ([], {}) if fixed_key else ([], {key: "string"})
        fields = {} if fixed_key else {key: f"$.inputs.{key}"}
        if t.get("clock"):
            steps += now("doctrine:own_values")
            fields.update({f: "$.results.read_now.timestamp" for f in t["clock"]})
        given = self.fields_of(name)
        if given:
            inputs["submission"] = "object"
            fields.update({f: f"$.inputs.submission.{f}" for f in given})
        parent = self.parent_of(name)
        if parent:
            pkey = self.key_of(parent)
            if self.formed(parent) == "key" and set(self.thing(parent)["identity"]["from"]) <= set(given):
                # The parent's key is formed here, from the record's own attributes, so the record
                # never depends on an earlier component's output having been carried forward.
                attrs = self.thing(parent)["identity"]["from"]
                steps += form(f"form_{pkey}", self.key_ct(parent),
                              {f: f"inputs.submission.{f}" for f in attrs}, pkey, pkey,
                              f"ledger:things/{parent}/identity")
                fields[pkey] = f"$.results.form_{pkey}.{pkey}"
            else:
                inputs[pkey] = "string"
                fields[pkey] = f"$.inputs.{pkey}"
        holder = t.get("held_by")
        if holder:
            inputs[holder["field"]] = "string"
            fields[holder["field"]] = f"$.inputs.{holder['field']}"
            fields.pop(key, None)
        fields.update(t.get("fixed", {}))
        if "state" in t.get("fixed", {}):
            fields["state"] = up(t["fixed"]["state"])
        if t.get("states") and "state" not in t.get("fixed", {}):
            fields["state"] = up(t["states"][0])
        if t.get("defaults"):
            note = (f"{op_name}: defaults {t['defaults']} apply when a request leaves a field out. No platform "
                    "transform supplies a default; the entrance supplies them for callers outside, and a direct "
                    "request that leaves one out records none.")
            if note not in self.unrealized:
                self.unrealized.append(note)
        steps += write(rec, self.records(name), {"literal": fixed_key} if fixed_key else f"inputs.{key}",
                       {"literal": fields}, src,
                       f"ledger:things/{name} + doctrine:own_values")
        return self.add(Component(f"{self.ns}CC_WRITE_{up(name)}_V0", f"Write a new {name} in its first state",
                                  steps, inputs, {"result_status": "string"}, src))

    def mover(self, op_name, name, frm, to_states, decided, not_self, by):
        """check, change: move a thing from one state to a decided one, changing only what it names."""
        key, src = self.key_of(name), f"ledger:operations/{op_name}"
        steps = []
        inputs = {key: "string", "to_state": "string"}
        if not_self:
            steps += check_equal(f"compare_{by}_to_{name}", f"inputs.{by}", f"inputs.{key}", "is_self",
                                 src + "/not_self")
            steps += check_rules("refuse_self_decision", {"is_self": f"$.results.compare_{by}_to_{name}.is_self"},
                                 [{"field": "is_self", "op": "eq", "value": False}],
                                 src + "/not_self + doctrine:rules_held")
        steps += check_member("read_outcome_admitted", "inputs.to_state", to_states,
                              f"ledger:things/{name}/states + doctrine:rules_held")
        steps += change_where("set_record_state", self.records(name), {key: f"$.inputs.{key}", "state": up(frm)},
                              {"state": "$.inputs.to_state", **{f: f"$.inputs.{f}" for f in decided}},
                              src + "/from_state + doctrine:rules_held")
        for f in decided:
            inputs[f] = ("string", "YES" if f == by else "NO")
        return self.add(Component(f"{self.ns}CC_MOVE_{up(name)}_FROM_{up(frm)}_V0",
                                  f"Move a {name} from {frm} to a state the business admits",
                                  steps, inputs, {"updated_count": "integer"}, src))

    def recorder(self, extra=()):
        """record: a moment on the part's trail, in the record shape the trail already holds."""
        part, trail = self.sub, self.l["trail"]
        spec = self.trail_spec(part)
        fields = list(trail["records"]) + list(extra)
        values = {f: f"$.inputs.{f}" for f in fields if f != spec["occurrence"]}
        record_fields = {spec["occurrence"]: "$.inputs.occurrence", **values}
        stream = f"inputs.{trail['subject']}" if spec["stream"] == "subject" else {"literal": spec["store"]}
        actor = "inputs.staff_id" if self.authorized else None
        inputs = {"occurrence": "string", **{f: ("string", "NO") for f in values}}
        if spec["stream"] == "subject":
            inputs[trail["subject"]] = "string"
        steps = record(spec["store"], record_fields, spec["time"], stream, actor, "ledger:trail")
        suffix = "REPEATED_MOMENT" if extra else "MOMENT"
        return self.add(Component(f"{self.ns}CC_RECORD_{up(part)}_{suffix}_V0",
                                  f"Record a moment on the {part}'s own trail", steps, inputs,
                                  {"sequence_number": "integer"}, "ledger:trail"))

    def trail_spec(self, part):
        spec = self.carried_trail(part)
        own = {r["code"] for r in self.base["new_artifacts"] if r.get("owner_subdomain") == part}
        base = [r for r in self.base.get("step_bindings") or [] if r["owner"] in own]
        for r in base:
            lit = r["bound_to"].get("literal") if isinstance(r["bound_to"], dict) else None
            if r["field"] == "record" and isinstance(lit, dict):
                for k, v in lit.items():
                    if isinstance(v, str) and v.isupper():
                        spec["occurrence"] = k
        return spec

    # -- composing an operation ------------------------------------------------------------------

    def moment_of(self, op_name):
        trail = self.l["trail"]
        if trail.get("moment") == "operation":
            return up(op_name)
        announced = self.l.get("announces", {}).get(op_name)
        return up(announced[0]) if announced else up(op_name)

    def moment_binds(self, op_name, subject, values):
        trail = self.l["trail"]
        binds = {"occurrence": {"literal": self.moment_of(op_name)}}
        for f in trail["records"]:
            if f == self.trail_spec(self.sub)["occurrence"]:
                continue
            if f == "staff_id":
                binds[f] = "payload.staff_id"
            elif f == "subject":
                binds[f] = subject
            elif f in values:
                binds[f] = values[f]
        if trail.get("subject") and trail["subject"] in values and self.trail_spec(self.sub)["stream"] == "subject":
            binds[trail["subject"]] = values[trail["subject"]]
        return binds

    def create(self, op_name, op):
        src = f"ledger:operations/{op_name}"
        names = op["creates"]
        first = names[0]
        chain, values = [], {}
        parent = self.parent_of(first)
        reuse_parent = parent and op.get("parent") == "create_or_reuse"
        checked = names + ([parent] if reuse_parent else [])
        sub = self.check_submission(op_name, checked)
        if sub:
            binds = {}
            for name in checked:
                t = self.thing(name)
                if t.get("required"):
                    inp = f"{head(name)}_fields" if len(checked) > 1 else "submission"
                    binds[inp] = self.submission(op_name, self.fields_of(name))
                elif not self.formed(name):
                    binds[self.key_of(name)] = self.at(op_name, self.key_of(name))
            chain.append((sub, binds, {}, f"{src}/required"))
        # Preconditions: a parent that must exist, and a holder that must be in a state.
        if parent and not reuse_parent and parent not in names:
            r = self.resolve_of(op_name, parent)
            chain.append((r, self.resolve_binds(op_name, parent), {}, f"{src}/precondition"))
            values[self.key_of(parent)] = f"results.{short(r)}.{head(parent)}_record.{self.key_of(parent)}" \
                if self.by_attributes(op_name, parent) else self.at(op_name, self.key_of(parent))
        holder = self.thing(first).get("held_by")
        if holder:
            r = self.resolver(holder["thing"])
            hkey = self.key_of(holder["thing"])
            chain.append((r, {hkey: self.at(op_name, hkey)}, {}, f"ledger:reads_other_part + {src}/precondition"))
            rec = f"results.{short(r)}.{head(holder['thing'])}_record"
            req = self.add(Component(
                f"{self.ns}CC_REQUIRE_{up(holder['requires_state'])}_{up(holder['thing'])}_V0",
                f"Refuse a {first} for a {holder['thing']} who is not {holder['requires_state']}",
                check_member(f"require_{holder['thing']}_{holder['requires_state']}", "inputs.state",
                             [up(holder["requires_state"])], f"ledger:things/{first}/held_by + doctrine:own_values"),
                {"state": "string"}, {"is_member": "boolean"}, f"ledger:things/{first}/held_by"))
            chain.append((req, {"state": f"{rec}.state"}, {}, f"ledger:things/{first}/held_by"))
            values[holder["field"]] = f"{rec}.{hkey}"
        denials = {}
        for check in op.get("checks", []):
            chain += self.checked(op_name, op, check, values, denials)
        # Derived values, then the claims: every claim after the first that can refuse is
        # pre-checked before it (doctrine order).
        claims = []
        for name in names:
            if self.formed(name) != "fixed":
                claims.append((name, None))
            for value, d in self.thing(name).get("derived", {}).items():
                dv = self.deriver(name, value)
                froms = d["from"] if isinstance(d["from"], list) else [d["from"]]
                chain.append((dv, {f: self.at(op_name, f) for f in froms}, {}, f"ledger:things/{name}/derived/{value}"))
                values[value] = f"results.{short(dv)}.{value}"
                if d.get("unique"):
                    claims.append((name, value))
        if reuse_parent:
            claims.append((parent, None))
        refusable = [c for c in claims if not (c[1] is None and self.thing(c[0])["identity"].get("on_duplicate")
                                               in ("reuse", "repeat"))]
        for name, value in refusable[1:]:
            key = value or self.key_of(name)
            chain.append((self.free(name, value), {key: values.get(key) or self.at(op_name, key)}, {},
                          "doctrine:order"))
        repeat = None
        for name, value in claims:
            c = self.claimer(name, value)
            key = value or self.key_of(name)
            idt = self.thing(name)["identity"]
            how = None if value else self.formed(name)
            if how == "key":
                binds = {f: self.at(op_name, f) for f in idt["from"]}
            elif how == "id":
                binds = {f: values.get(f) or self.at(op_name, f) for f in self.id_from(name)}
            else:
                binds = {key: values.get(key) or self.at(op_name, key)}
            overrides = {}
            if not value and idt.get("on_duplicate") == "reuse":
                binds[f"{head(name)}_fields"] = {"literal": {f: "$." + self.at(op_name, f)
                                                             for f in self.thing(name)["required"]}}
                overrides = {"ALREADY_EXISTS": "next"}
            if not value and idt.get("on_duplicate") == "repeat":
                repeat = name
            chain.append((c, binds, overrides, f"ledger:things/{name}/identity"))
            if how:
                values.setdefault(key, f"results.{short(c)}.{key}")
            if repeat == name:
                chain[-1] = (c, binds, {"ALREADY_EXISTS": "REPEAT"}, f"{src}/on_repeat")
            elif op.get("on_refusal") and not overrides:
                deny = self.denial(op_name, op, f"{name} already held", denials)
                chain[-1] = (c, binds, {"ALREADY_EXISTS": deny}, f"{src}/on_refusal")
        for name in names:
            w = self.writer(op_name, name)
            binds = {}
            for f in self.components[w].inputs:
                binds[f] = (self.submission(op_name, self.fields_of(name)) if f == "submission"
                            else values.get(f) or self.at(op_name, f))
            chain.append((w, binds, {}, src))
        subject = values.get(self.key_of(first)) or self.at(op_name, self.key_of(first))
        trail_values = {**{f: self.at(op_name, f) for f in self.l["trail"]["records"]
                           if self.carries(op_name, f) or f in self.fields_of(first)},
                        **values}
        chain.append((self.recorder(), self.moment_binds(op_name, subject, trail_values),
                      {"SUCCESS": "EXIT_COMPLETED"} if repeat or denials else {}, "ledger:trail"))
        chain += self.denied(op_name, op, denials, trail_values)
        if repeat:
            rp = op["on_repeat"]
            again = self.recorder(extra=rp["records"])
            binds = self.moment_binds(op_name, subject, trail_values)
            binds.update({f: self.at(op_name, f) for f in rp["records"]})
            chain.append((again, binds, {"SUCCESS": "EXIT_REPEATED"}, f"{src}/on_repeat"))
            chain = [(c, b, {k: (short(again) if v == "REPEAT" else v) for k, v in o.items()}, s)
                     for c, b, o, s in chain]
        return chain

    # -- checks an operation names, and where a refused one ends ---------------------------------

    def checked(self, op_name, op, check, values, denials):
        """The components that realize one named check. A refusal ends at the operation's denial."""
        src = f"ledger:operations/{op_name}/checks/{check['name']}"
        if "count" in check:
            self.unrealized.append(
                f"{op_name}: '{check['name']}' counts {self.thing(check['count']['thing'])['plural']}; the "
                "registry declares no COUNT operation and no carried transform counts records. Not realized.")
            return []
        deny = self.denial(op_name, op, check["name"], denials) if op.get("on_refusal") else "EXIT_REJECTED"
        refused = {"VIOLATION": deny, "NOT_FOUND": deny}
        code = f"{self.ns}CC_REQUIRE_{up(check['name'])}_V0"
        chain = []
        if "requires" in check:
            q = check["requires"]
            name = q["thing"]
            key = self.key_of(name)
            by = q.get("by", key)
            if by != key and self.formed(name) == "id":
                # Named by the field its identity is generated from, under the request's own name.
                r = self.resolver(name, by_attributes=True)
                binds = {f: self.at(op_name, by) for f in self.id_from(name)}
            else:
                r, binds = self.resolver(name), {key: self.at(op_name, by)}
            chain.append((r, binds, refused, src))
            rec = f"results.{short(r)}.{head(name)}_record"
            values[name] = rec
            holds = self.held(q.get("holds", {}))
            c = self.add(Component(code, f"Refuse to {op_name} unless the {name} holds what the business requires",
                                   check_rules(f"require_{up(check['name']).lower()}",
                                               {f: f"$.inputs.{f}" for f in holds},
                                               [{"field": f, "op": "eq", "value": v} for f, v in holds.items()],
                                               src + " + doctrine:rules_held"),
                                   {f: self.type_of(f) if f in holds else "string" for f in holds},
                                   {"valid": "boolean"}, src))
            chain.append((c, {f: f"{rec}.{f}" for f in holds}, refused, src))
        elif "allowed" in check:
            a = check["allowed"]
            c = self.add(Component(code, f"Refuse a {a['field'].replace('_', ' ')} the business does not admit",
                                   check_member(f"require_{a['field']}_admitted", f"inputs.{a['field']}", a["values"],
                                                src + " + doctrine:rules_held"),
                                   {a["field"]: "string"}, {"is_member": "boolean"}, src))
            chain.append((c, {a["field"]: self.at(op_name, a["field"])}, refused, src))
        elif "exists" in check:
            name = check["exists"]["thing"]
            rec, key = f"{head(name)}_record", self.key_of(name)
            c = self.add(Component(code, f"Refuse to {op_name} before the {name} is set",
                                   read(f"read_{rec}", self.records(name), f"inputs.{key}", rec, src),
                                   {key: "string"}, {rec: "object"}, src))
            chain.append((c, {key: {"literal": self.thing(name)["identity"]["fixed"]}}, refused, src))
            values[name] = f"results.{short(c)}.{rec}"
        elif "look_up" in check:
            q = check["look_up"]
            table = {k: v for k, v in self.l["tables"][q["table"]].items()}
            thing, _, f = q["key"].rpartition(".")
            key = f"{values[thing]}.{f}" if thing else self.at(op_name, f)
            found = up(q["table"]).lower()
            steps = look_up(f"look_up_{found}", table, "inputs.key", found, src + " + ledger:tables")
            if "contains" in q:
                steps += check_member_of(f"require_{q['contains']}_in_{found}", f"inputs.{q['contains']}",
                                         f"results.look_up_{found}.{found}", src + " + doctrine:rules_held")
                given = q["contains"]
            else:
                steps += check_rules_of(f"require_{q['rules_on']}_hold", f"inputs.{q['rules_on']}",
                                        f"results.look_up_{found}.{found}", src + " + doctrine:rules_held")
                given = q["rules_on"]
            typ = "object" if "rules_on" in q else "string"
            c = self.add(Component(code, f"Refuse to {op_name} unless {check['name']}", steps,
                                   {"key": "string", given: typ}, {"valid": "boolean"}, src))
            chain.append((c, {"key": key, given: self.at(op_name, given)}, refused, src))
        return chain

    def held(self, holds):
        return {f: up(v) if f == "state" else v for f, v in holds.items()}

    def denial(self, op_name, op, reason_of, denials):
        """The node a refused check ends at: it records the refusal, with its reason, and announces it."""
        reason = op["on_refusal"].get("reasons", {}).get(reason_of, up(reason_of))
        denials.setdefault(reason, f"CC_DENY_{reason}")
        event = op["on_refusal"]["announces"]
        op["_ends"] = {"EXIT_DENIED": ([event], f"ledger:operations/{op_name}/on_refusal")}
        if event not in self.events:
            self.events[event] = (op_name, {}, True)
            self.event_part[event] = self.sub
        return denials[reason]

    def denied(self, op_name, op, denials, values):
        if not denials:
            return []
        rec, event = self.recorder(), op["on_refusal"]["announces"]
        subject = values.get(self.l["trail"]["subject"]) or self.at(op_name, self.l["trail"]["subject"])
        chain = []
        for reason, node in denials.items():
            binds = self.moment_binds(op_name, subject, values)
            binds["occurrence"] = {"literal": up(event)}
            binds["reason"] = {"literal": reason}
            chain.append((rec, binds, {"SUCCESS": "EXIT_DENIED"}, f"ledger:operations/{op_name}/on_refusal", node))
        return chain

    def resolve_of(self, op_name, name):
        return self.resolver(name, self.by_attributes(op_name, name))

    def id_from(self, name):
        f = self.thing(name)["identity"]["from"]
        return f if isinstance(f, list) else [f]

    def form_id(self, name, src):
        """form: a generated identity, from one field or several, with the business's prefix."""
        idt, key = self.thing(name)["identity"], self.key_of(name)
        fields = self.id_from(name)
        data = f"inputs.{fields[0]}" if len(fields) == 1 else {"literal": {f: f"$.inputs.{f}" for f in fields}}
        return form(f"form_{key}", GENERATE, {"data": data, "prefix": {"literal": idt["prefix"]}}, key, "id",
                    src + " + doctrine:own_values")

    def resolve_binds(self, op_name, name, by=None):
        if self.by_attributes(op_name, name) and self.formed(name) == "id":
            return {f: self.at(op_name, by or f) for f in self.id_from(name)}
        if self.by_attributes(op_name, name):
            return {f: self.at(op_name, f) for f in self.thing(name)["identity"]["from"]}
        return {self.key_of(name): self.at(op_name, self.key_of(name))}

    def change(self, op_name, op):
        name = op["thing"]
        if set(op.get("may_change", [])) & set(self.thing(name)["identity"].get("from", [])):
            return self.change_identity(op_name, op)
        src = f"ledger:operations/{op_name}"
        key = self.key_of(name)
        chain = [(self.check_stated(op_name, f), {f: self.at(op_name, f)}, {}, src + "/required")
                 for f in op.get("required", [])]
        keyref = self.at(op_name, key)
        if op.get("precondition") == "exists":
            r = self.resolve_of(op_name, name)
            chain.append((r, self.resolve_binds(op_name, name), {}, src + "/precondition"))
            if self.by_attributes(op_name, name):
                keyref = f"results.{short(r)}.{head(name)}_record.{key}"
        if "from_state" not in op:
            return chain + self.setter(op_name, op, name, keyref)
        if op.get("when"):
            chain.append(self.condition(op_name, op, name, f"results.{short(r)}.{head(name)}_record"))
        if op.get("releases") == "identity":
            rel = self.add(Component(
                f"{self.ns}CC_RELEASE_{up(name)}_IDENTITY_V0", f"Release a {name}'s identity",
                release("release_identity", self.registry(name), f"inputs.{key}", src + "/releases"),
                {key: "string"}, {"result_status": "string"}, src + "/releases"))
            chain.append((rel, {key: keyref}, {}, src + "/releases + doctrine:failed_record_ends"))
        siblings = [o for o in self.l["operations"].values() if isinstance(o, dict) and o.get("does") == "change"
                    and o.get("thing") == name and o.get("from_state") == op["from_state"]]
        decided = [f for f in op.get("may_change", []) if f != "state"]
        mover = self.mover(op_name, name, op["from_state"], [up(o["to_state"]) for o in siblings], decided,
                           op.get("not_self"), op.get("decided_by"))
        values = {f: self.at(op_name, f) for f in [key] + decided}
        values[key] = keyref
        chain.append((mover, {"to_state": {"literal": up(op["to_state"])}, **values}, {}, src))
        trail = {**{f: self.at(op_name, f) for f in self.l["trail"]["records"] if self.carries(op_name, f)}, **values}
        chain.append((self.recorder(), self.moment_binds(op_name, keyref, trail), {}, "ledger:trail"))
        return chain

    def setter(self, op_name, op, name, keyref):
        """change: set what the operation names on the one record, while it holds what it must."""
        src, key = f"ledger:operations/{op_name}", self.key_of(name)
        steps = now("doctrine:own_values") if "clock" in op["sets"].values() else []
        updates = {f: "$.results.read_now.timestamp" if v == "clock" else v for f, v in op["sets"].items()}
        steps += change_where("set_record", self.records(name),
                              {key: f"$.inputs.{key}", **self.held(op.get("holds", {}))}, updates,
                              src + "/sets + doctrine:rules_held")
        c = self.add(Component(self.code("CC", op_name), f"Set what {op_name} records on the {name}",
                               steps, {key: "string"}, {"updated_count": "integer"}, src))
        values = {key: keyref}
        trail = {**{f: self.at(op_name, f) for f in self.l["trail"]["records"] if self.carries(op_name, f)}, **values}
        return [(c, values, {}, src),
                (self.recorder(), self.moment_binds(op_name, keyref, trail), {}, "ledger:trail")]

    def condition(self, op_name, op, name, rec):
        """check: the condition a change waits for; otherwise the operation ends where it says."""
        src = f"ledger:operations/{op_name}/when"
        (cond, n), = [(k, v) for k, v in op["when"].items() if k in CONDITIONS]
        since = op["when"]["since"]
        ct = self.ns + CONDITIONS[cond]
        if not any(r["code"] == ct for r in self.base["new_artifacts"]):
            self.unrealized.append(f"{op_name}: {cond} needs {ct}, which the composition does not carry.")
        c = self.add(Component(
            f"{self.ns}CC_REQUIRE_{up(name)}_{up(cond)}_V0", f"Refuse to {op_name} until the condition holds",
            now("doctrine:own_values") +
            form(f"evaluate_{cond}", ct, {"last_active_date": f"inputs.{since}",
                                          "evaluation_date": "results.read_now.timestamp",
                                          "threshold_days": {"literal": n}}, "is_inactive", "is_inactive",
                 src + " + carried:realization"),
            {since: "string"}, {"is_inactive": "boolean"}, src))
        end = "EXIT_" + up(op["otherwise"])
        return (c, {since: f"{rec}.{since}"}, {"VIOLATION": end}, src + "/otherwise")

    def change_identity(self, op_name, op):
        """A change that may change identity: resolve; prepare the corrected record; check identity
        unchanged (refused: branch to the new identity); write in place, or claim and re-key."""
        src = f"ledger:operations/{op_name}"
        name = op["thing"]
        t = self.thing(name)
        key, ident = t["identity"]["field"], t["identity"]["from"]
        parent = t["belongs_to"]
        pkey, pfrom = self.key_of(parent), self.thing(parent)["identity"]["from"]
        moves_parent = [f for f in op["may_change"] if f in pfrom]
        if moves_parent and op.get("on_identity_change", {}).get(parent) != "follows":
            self.conflicts.append(f"{op_name}: may change {', '.join(moves_parent)}, which form the {parent} key; "
                                  f"on_identity_change.{parent} is not decided.")
        store, registry = self.records(name), self.registry(name)
        rec = f"{head(name)}_record"
        schema = {f: {"required": True, "type": ty} for f, ty in t["required"].items()}
        fields = {key: "$.results.form_updated_identity_key.updated_identity_key",
                  **{f: f"$.inputs.updated_fields.{f}" for f in t["required"]},
                  **{k: f"$.results.read_{rec}.{rec}.{k}" for k in op["keeps"]},
                  pkey: f"$.results.form_{pkey}.{pkey}"}
        rules = [{"field": "violations", "op": "eq", "value": []}] + \
                [{"field": f, "op": "neq", "value": []} for f in t.get("non_empty", [])]
        params = {"violations": "$.results.check_corrected_record.violations",
                  **{f: f"$.results.assemble_updated_record.updated_record.{f}" for f in t.get("non_empty", [])}}
        prepare = self.add(Component(
            self.code("CC", op_name), f"Prepare a corrected {name} under the identity its correction names",
            read(f"read_{rec}", store, f"inputs.{key}", rec, src) +
            form("form_updated_identity_key", self.key_ct(name), {f: f"inputs.updated_fields.{f}" for f in ident},
                 "updated_identity_key", key, f"ledger:things/{name}/identity") +
            form(f"form_{pkey}", self.key_ct(parent), {f: f"inputs.updated_fields.{f}" for f in pfrom},
                 pkey, pkey, src + f"/on_identity_change/{parent}") +
            [Step("assemble_updated_record", ASSEMBLE, None, None, {"fields": {"literal": fields}},
                  {"updated_record": "capability_result.record"}, src + "/keeps")] +
            check_shape("check_corrected_record", "results.assemble_updated_record.updated_record", schema,
                        f"ledger:things/{name}/required") +
            check_rules("refuse_incomplete_correction", params, rules, f"ledger:things/{name}/required"),
            {key: "string", "updated_fields": "object"}, {"updated_record": "object", "updated_identity_key": "string"},
            src))
        same = self.add(Component(
            f"{self.ns}CC_CONFIRM_{up(name)}_IDENTITY_UNCHANGED_V0", f"Confirm a corrected {name} keeps its identity",
            check_equal("compare_identity", f"inputs.{key}", "inputs.updated_identity_key", "identity_unchanged", src) +
            check_rules("require_identity_unchanged", {"identity_unchanged": "$.results.compare_identity.identity_unchanged"},
                        [{"field": "identity_unchanged", "op": "eq", "value": True}], src),
            {key: "string", "updated_identity_key": "string"}, {"valid": "boolean"}, src))
        in_place = self.add(Component(
            f"{self.ns}CC_WRITE_CORRECTED_{up(name)}_RECORD_V0", f"Write a corrected {name} under its unchanged identity",
            [Step("write_updated_record", MUTABLE, "WRITE", store, {"key": f"inputs.{key}", "value": "inputs.updated_record"},
                  {"result_status": "result_status"}, src)],
            {key: "string", "updated_record": "object"}, {"result_status": "string"}, src))
        child = next(n for n, x in self.things.items() if x.get("belongs_to") == name)
        rekey = self.add(Component(
            f"{self.ns}CC_REKEY_{up(name)}_V0", f"Move a {name} to its new identity, with its {self.thing(child)['plural']}",
            [Step(f"write_{name}_record", MUTABLE, "WRITE", store,
                  {"key": "inputs.updated_identity_key", "value": "inputs.updated_record"},
                  {"result_status": "result_status"}, src + "/on_identity_change")] +
            change_where(f"move_{head(child)}_records", self.records(child), {key: f"$.inputs.{key}"},
                         {key: "$.inputs.updated_identity_key"}, src + "/on_identity_change/children",
                         {"VIOLATION": "continue"}) +
            remove(f"remove_old_{name}_record", store, f"inputs.{key}", src + "/on_identity_change") +
            release("release_old_identity", registry, f"inputs.{key}", src + "/on_identity_change/old_identity"),
            {key: "string", "updated_identity_key": "string", "updated_record": "object"}, {"updated_count": "integer"}, src))
        recorder = self.recorder()
        prep = f"results.{short(prepare)}"
        claim_book = self.claimer(name)
        chain = [
            (self.resolve_of(op_name, name), self.resolve_binds(op_name, name), {}, src + "/precondition"),
            (prepare, {key: self.at(op_name, key), "updated_fields": self.at(op_name, "updated_fields")}, {}, src),
            (same, {key: self.at(op_name, key), "updated_identity_key": f"{prep}.updated_identity_key"},
             {"VIOLATION": short(claim_book)}, src),
            (in_place, {key: self.at(op_name, key), "updated_record": f"{prep}.updated_record"},
             {"SUCCESS": short(recorder)}, src),
            (claim_book, {f: f"payload.updated_fields.{f}" for f in ident}, {}, f"{src}/refuse_if"),
            (self.claimer(parent), {**{f: f"payload.updated_fields.{f}" for f in pfrom},
                                    f"{head(parent)}_fields": {"literal": {f: f"$.payload.updated_fields.{f}" for f in pfrom}}},
             {"ALREADY_EXISTS": "next"}, src + f"/on_identity_change/{parent}"),
            (rekey, {key: self.at(op_name, key), "updated_identity_key": f"{prep}.updated_identity_key",
                     "updated_record": f"{prep}.updated_record"}, {}, src + "/on_identity_change"),
            (recorder, self.moment_binds(op_name, self.at(op_name, key), {}), {}, "ledger:trail"),
        ]
        return chain

    def read(self, op_name, op):
        """read the thing, its parent and its children. A read is trailed before it reads."""
        src = f"ledger:operations/{op_name}"
        name = op["thing"]
        key = self.key_of(name)
        rec = f"{head(name)}_record"
        steps = read(f"read_{rec}", self.records(name), f"inputs.{key}", rec, src)
        outputs = {rec: "object"}
        for w in op.get("with", []):
            if self.parent_of(name) == w:
                wkey, wrec = self.key_of(w), f"{head(w)}_record"
                if self.formed(w) == "key":
                    steps += form(f"form_{wkey}", self.key_ct(w),
                                  {f: f"results.read_{rec}.{rec}.{f}" for f in self.thing(w)["identity"]["from"]},
                                  wkey, wkey, f"ledger:things/{w}/identity")
                    ref = f"results.form_{wkey}.{wkey}"
                else:
                    ref = f"results.read_{rec}.{rec}.{wkey}"
                steps += read(f"read_{wrec}", self.records(w), ref, wrec, src, {"NOT_FOUND": "continue"})
                outputs[wrec] = "object"
            elif self.parent_of(w) == name:
                plural = self.thing(w)["plural"].replace(" ", "_")
                steps += query(f"select_{head(w)}_records", self.records(w), src)
                steps += narrow(f"select_{plural}_of_{name}", self.select_ct(), f"results.select_{head(w)}_records.records",
                                {"literal": {key: f"$.inputs.{key}"}}, plural, src)
                outputs[plural] = "array"
        outputs, steps = self.carried_outputs(op_name, outputs, steps)
        reader = self.add(Component(self.code("CC", op_name), f"Answer a {name} with {', '.join(op.get('with', []))}",
                                    steps, {key: "string"}, outputs, src))
        values = {key: self.at(op_name, key)}
        return [(self.recorder(), self.moment_binds(op_name, values[key], values), {}, "ledger:trail + doctrine:order"),
                (reader, values, {}, src)]

    def query(self, op_name, op):
        """query: the records matching fixed exclusions and the caller's criteria, grouped."""
        src = f"ledger:operations/{op_name}"
        name = op["thing"]
        t = self.thing(name)
        plural = t["plural"].replace(" ", "_")
        steps = query(f"select_{head(name)}_records", self.records(name), src)
        source = f"results.select_{head(name)}_records.records"
        if op.get("always_exclude"):
            kept = {k: up(t["states"][0]) for k in op["always_exclude"]}
            steps += narrow(f"select_{t['states'][0]}_{plural}", self.select_ct(), source, {"literal": kept},
                            f"{t['states'][0]}_{plural}", src + "/always_exclude")
            source = f"results.select_{t['states'][0]}_{plural}.{t['states'][0]}_{plural}"
        criteria = op["criteria"]
        if criteria == "caller":
            crit, inputs = "inputs.search_criteria", {"search_criteria": "object"}
        else:
            crit, inputs = {"literal": {c: f"$.inputs.{c}" for c in criteria}}, {c: "string" for c in criteria}
        steps += narrow(f"select_matching_{plural}", FILTER, source, crit, f"matching_{plural}", src + "/criteria")
        outputs = {f"matching_{plural}": "array"}
        if op.get("group_by"):
            g = op["group_by"]
            steps += group(f"group_{plural}_by_{g}", f"{self.ns}CT_PURE_GROUP_RECORDS_V0",
                           f"results.select_matching_{plural}.matching_{plural}", self.key_of(g),
                           f"matching_{self.thing(g)['plural'].replace(' ', '_')}", src + "/group_by")
            outputs = {f"matching_{self.thing(g)['plural'].replace(' ', '_')}": "array", **outputs}
        if op.get("nothing_found") == "empty":
            self.unrealized.append(
                f"{op_name}: nothing_found=empty needs a filter that answers empty; the platform's "
                "(CT_PURE_FILTER_RECORDS_V0) refuses an empty result. Realized with it; an empty answer is "
                "still refused.")
        q = self.add(Component(self.code("CC", op_name), f"Answer the {t['plural']} matching the criteria named",
                               steps, inputs, outputs, src))
        binds = {k: self.at(op_name, k) for k in inputs}
        return [(self.recorder(), self.moment_binds(op_name, next(iter(binds.values())), binds), {},
                 "ledger:trail + doctrine:order"),
                (q, binds, {}, src)]

    def select_ct(self):
        """The transform that selects records and answers empty: the domain's, when it carries one."""
        own = f"{self.ns}CT_PURE_SELECT_RECORDS_V0"
        return own if any(r["code"] == own for r in self.base["new_artifacts"]) else FILTER

    def carried_outputs(self, op_name, outputs, steps):
        """A read's answer keeps the names callers already read (carried:surface)."""
        wf = self.code("WF", op_name)
        nodes = [r["node"] for r in self.base.get("execution_topology") or []
                 if r["workflow"] == wf and r["node_type"] == "CC"]
        known = {}
        for node in nodes:
            out = {f["field"]: f["type"] for f in self.base["interface_fields"]
                   if short(f["artifact"]) == node and f["direction"] == "OUTPUT"}
            if set(out) & set(outputs):
                known.update(out)
        if not known:
            return outputs, steps
        rename = {}
        for name, typ in outputs.items():
            if name not in known:
                spare = [k for k, t in known.items() if t == typ and k not in outputs and k not in rename.values()]
                if spare:
                    rename[name] = spare[0]
        for s in steps:
            s.outs = {rename.get(k, k): v for k, v in s.outs.items()}
        return {rename.get(k, k): t for k, t in outputs.items()}, steps

    # -- workflows -------------------------------------------------------------------------------

    def workflow(self, op_name, op):
        chain = getattr(self, op["does"])(op_name, op)
        if self.authorized:
            chain = [(self.authorize(), {"staff_credentials": "payload.staff_credentials"}, {}, "ledger:actor")] + chain
        request = self.request_shape(op_name, {})
        if not request:
            request = {}
            for entry in chain:
                for b in entry[1].values():
                    found = [b] if isinstance(b, str) else re.findall(r"\$\.(payload\.\w+)", json.dumps(b))
                    for p in found:
                        if p.startswith("payload."):
                            request.setdefault(p.split(".")[1], self.type_of(p.split(".")[1]))
        self.workflows.append((op_name, op, chain, request, self.sub))
        announced = [e for e in self.l.get("announces", {}).get(op_name, [])]
        if op.get("on_repeat", {}).get("announces"):
            announced.append(op["on_repeat"]["announces"])
        for event in announced:
            if event not in self.events:
                self.events[event] = (op_name, request, True)
                self.event_part[event] = self.sub

    def predecessors(self, op_name, op):
        """The workflows and entrances an operation takes the place of, as the composition names them."""
        held = {r["code"] for r in self.base["new_artifacts"]}
        out = {}
        for old in op.get("replaces", []):
            wf = self.code("WF", old)
            if wf not in held:
                raise ValueError(f"{op_name} replaces '{old}', which the composition does not hold as {wf}")
            out[wf] = self.code("WF", op_name)
            inn = next((r["node"] for r in self.base.get("execution_topology") or []
                        if r["workflow"] == wf and r["node_type"] == "IN"), None)
            if inn:
                out[self.ns + short(inn)] = self.code("IN", op_name)
        return out

    def run(self):
        replaces = {}
        for part in self.parts:
            self.enter(part)
            for op_name, op in self.l["operations"].items():
                if op_name != "from":
                    self.workflow(op_name, op)
                    replaces.update(self.predecessors(op_name, op))
        reg = self.render()
        reg["_replaces"] = replaces
        return reg


def derive(ledger_path, baseline_path):
    """The P7 rows a ledger derives, judged by the sealed doctrine, schema and catalog."""
    judged = seal.judged_by()
    ledger = yaml.safe_load(open(ledger_path))
    refuse(ledger)
    reg = check_doctrine(Composer(ledger, load_p7(baseline_path)).run())
    return {"_judged_by": judged, **reg}
