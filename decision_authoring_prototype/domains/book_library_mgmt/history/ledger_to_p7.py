"""Derive P7 register rows from a closed-shape decision ledger.

Every emitted row carries `_from`: the ledger entry it derives from, or the doctrine rule that
makes it mechanical. `compare.py` strips `_from` before diffing against the baseline.

Doctrine applied (each rule is cited by name in `_from`):
  order       authorize, then precondition, then identity claim, then write, then trail
  storage     a thing with identity gets a registry; a thing with states a mutable store;
              the trail an append-only store
  naming      codes from the author's names; records and registries by the thing's head noun
  interface   a request carries the actor's credentials and id, plus the operation's inputs;
              an event carries the operation's identifying inputs, the actor and the time
  binding     one resource binding per subdomain names every storage mechanism it uses
"""
import json
import sys

import yaml

CS = "capability_side_effects::"
CT = "capability_transforms::"
MUTABLE, REGISTRY, APPENDONLY = CS + "CS_MUTABLE_JSON_V0", CS + "CS_REGISTRY_V0", CS + "CS_APPENDONLY_JSONL_V0"

# What each step kind can return. A CC's routing in a workflow is the union over its steps.
STATUSES = {
    "READ": ["SUCCESS", "NOT_FOUND", "VIOLATION", "BACKEND_ERROR"],
    "REGISTER": ["SUCCESS", "ALREADY_EXISTS", "VIOLATION", "BACKEND_ERROR"],
    "WRITE": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    "UPDATE_WHERE": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    "APPEND": ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
    None: ["SUCCESS", "VIOLATION"],  # a pure transform
}


def up(name):
    return name.upper().replace(" ", "_")


def head(name):
    return name.split()[-1]


class Emitter:
    def __init__(self, ledger):
        self.l = ledger
        self.ns = ledger["domain"] + "::"
        self.sub = ledger["subdomain"]
        self.reg = {k: [] for k in (
            "new_artifacts", "rb_declarations", "execution_topology", "cc_composition",
            "step_bindings", "interface_fields", "artifact_properties", "structure_stores")}
        self.store_users = {}

    def code(self, family, name):
        return f"{self.ns}{family}_{up(name)}_V0"

    def row(self, register, src, **cols):
        self.reg[register].append({**cols, "_from": src})

    def artifact(self, family, name, summary, src):
        self.row("new_artifacts", src, family=family, code=self.code(family, name), summary=summary,
                 owner_subdomain=self.sub, status="NEW")

    def field(self, artifact, direction, name, typ, src, meaning=None, fmt=None):
        extra = {"format": fmt} if fmt else {}
        self.row("interface_fields", src, artifact=artifact, direction=direction, field=name, type=typ,
                 required="YES", default=None, meaning=meaning or name.replace("_", " "), **extra)

    # -- steps ---------------------------------------------------------------------------------

    def step(self, cc, n, name, capability, operation, store, ins, outs, last, src):
        """One CC step. `ins` maps field -> binding; `outs` maps field -> capability result."""
        kind = "CS" if capability.startswith(CS) else "CT"
        statuses = STATUSES[operation if kind == "CS" else None]
        routing = {s: ("continue" if (s == "SUCCESS" and not last) else "exit") for s in statuses}
        produces = list(outs)
        self.row("cc_composition", src, cc_code=cc, step=str(n), step_name=name, capability=capability,
                 kind=kind, operation=operation, store=store, consumes=list(ins), produces=produces,
                 routing=routing, interpreted_by=None, semantic_status="SUCCESS",
                 interface={"in": {f: f for f in ins}, "out": {f: f for f in produces}})
        for f, b in ins.items():
            self.row("step_bindings", src, owner=cc, step=name, direction="INPUT", field=f, bound_to=b)
        for f, b in outs.items():
            self.row("step_bindings", src, owner=cc, step=name, direction="OUTPUT", field=f, bound_to=b)
        if store:
            self.store_users.setdefault(store, set()).add(cc)
        return statuses

    # -- operation patterns --------------------------------------------------------------------

    def create(self, op_name, op):
        """Resolve the parent, claim the identity, then assemble and write: doctrine `order`.

        The parent check and the claim are separate components, so a workflow that creates the
        parent itself can claim without resolving. Resolving reuses the parent's own component.
        """
        thing = self.l["things"][op["thing"]]
        parent_name = thing["belongs_to"]
        parent = self.l["things"][parent_name]
        pkey, key = parent["identity"]["field"], thing["identity"]["field"]
        store, pstore = up(thing["plural"]), up(parent["plural"])
        h = head(op["thing"])
        registry = f"{up(h)}_{up(key)}_REGISTRY"
        resolve = f"{self.ns}CC_RESOLVE_{up(parent_name)}_IDENTITY_V0"
        claim = f"{self.ns}CC_CLAIM_{up(h)}_{up(key)}_V0"
        cc, src = self.code("CC", op_name), f"ledger:operations/{op_name}"
        isrc = f"ledger:things/{op['thing']}/identity"
        rec = f"{h}_record"

        claim_st = self.step(claim, 1, f"claim_{key}", REGISTRY, "REGISTER", registry,
                             {"key": f"inputs.{key}", "target_cs": {"literal": MUTABLE},
                              "target_ref": {"literal": store}},
                             {"address": "capability_result.address", "result_status": "result_status"},
                             True, isrc)
        self.row("new_artifacts", isrc, family="CC", code=claim,
                 summary=f"Claim a {h}'s {key} so a second {h} carrying it is refused",
                 owner_subdomain=self.sub, status="NEW")
        self.field(claim, "INPUT", key, "string", isrc)
        self.field(claim, "OUTPUT", "address", "string", "doctrine:interface")

        st = set()
        st |= set(self.step(cc, 1, f"read_{head(parent_name)}_record", MUTABLE, "READ", pstore,
                            {"key": f"inputs.{pkey}"},
                            {f"{head(parent_name)}_record": "capability_result.value",
                             "result_status": "result_status"}, False, src))
        st |= set(self.step(cc, 2, f"assemble_{rec}", CT + "CT_PURE_ASSEMBLE_RECORD_V0", None, None,
                            {"fields": {"literal": {pkey: f"$.inputs.{pkey}", key: f"$.inputs.{key}",
                                                    "state": up(thing["states"][0])}}},
                            {rec: "capability_result.record"}, False, f"ledger:things/{op['thing']}/states"))
        st |= set(self.step(cc, 3, f"write_{rec}", MUTABLE, "WRITE", store,
                            {"key": f"inputs.{key}", "value": f"results.assemble_{rec}.{rec}"},
                            {"result_status": "result_status"}, True, src))
        self.stores[store] = (MUTABLE, f"ledger:things/{op['thing']}/states")
        self.stores[registry] = (REGISTRY, isrc)
        self.field(cc, "INPUT", pkey, "string", src)
        self.field(cc, "INPUT", key, "string", src)
        self.field(cc, "OUTPUT", f"{head(parent_name)}_record", "object", "doctrine:interface")
        nodes = [
            (resolve, STATUSES["READ"], {pkey: f"payload.{pkey}"}, src + "/precondition"),
            (claim, claim_st, {key: f"payload.{key}"}, isrc),
            (cc, sorted(st, key=lambda s: s != "SUCCESS"), {pkey: f"payload.{pkey}", key: f"payload.{key}"}, src),
        ]
        return cc, {pkey: "string", key: "string"}, [pkey, key], nodes

    def transition(self, op_name, op):
        thing = self.l["things"][op["thing"]]
        key, store = thing["identity"]["field"], up(thing["plural"])
        cc, src = self.code("CC", op_name), f"ledger:operations/{op_name}"
        st = set(self.step(cc, 1, "set_record_state", MUTABLE, "UPDATE_WHERE", store,
                           {"filter": {"literal": {key: f"$.inputs.{key}", "state": up(op["from_state"])}},
                            "updates": {"literal": {"state": up(op["to_state"])}}},
                           {"matched_keys": "capability_result.matched_keys",
                            "updated_count": "capability_result.updated_count",
                            "result_status": "result_status"}, True, src))
        self.field(cc, "INPUT", key, "string", src)
        self.field(cc, "OUTPUT", "updated_count", "integer", "doctrine:interface")
        return cc, {key: "string"}, [key], [(cc, sorted(st, key=lambda s: s != "SUCCESS"),
                                             {key: f"payload.{key}"}, src)]

    # -- shared components ---------------------------------------------------------------------

    def shared(self):
        a = self.l["actor"]
        self.auth = f"{self.ns}CC_CONFIRM_{up(a['role'])}_AUTHORIZED_V0"
        self.ac = self.code("AC", a["name"])
        self.trail_cc = f"{self.ns}CC_APPEND_{up(self.sub)}_OPERATION_V0"
        self.trail_store = f"{up(self.sub)}_OPERATIONS"

    # -- workflows -----------------------------------------------------------------------------

    def workflow(self, op_name, op):
        cc, ins, ident, nodes = getattr(self, op["kind"])(op_name, op)
        wf, inn, src = self.code("WF", op_name), self.code("IN", op_name), f"ledger:operations/{op_name}"
        verb, thing = op_name.split()[0], op["thing"]
        self.artifact("WF", op_name, f"{verb.capitalize()} a {thing}", src)
        self.artifact("IN", op_name, f"A request to {op_name}", src)
        self.artifact("CC", op_name, f"{verb.capitalize()} a {thing}", src)

        # The request: doctrine `interface`.
        self.field(inn, "INPUT", "staff_credentials", "object", "ledger:actor")
        for f, t in ins.items():
            self.field(inn, "INPUT", f, t, src)
        self.field(inn, "INPUT", "staff_id", "string", "ledger:actor")

        # Topology: doctrine `order`.
        chain = [(self.auth, STATUSES[None])] + [(n, st) for n, st, _, _ in nodes] + \
                [(self.trail_cc, STATUSES["APPEND"])]
        short = lambda c: c.split("::")[-1]
        self.row("execution_topology", "doctrine:order", workflow=wf, node=short(inn), node_type="IN",
                 routing={"ACK": short(chain[0][0]), "NACK": "EXIT_REJECTED"})
        for i, (node, statuses) in enumerate(chain):
            nxt = short(chain[i + 1][0]) if i + 1 < len(chain) else "EXIT_COMPLETED"
            self.row("execution_topology", "doctrine:order", workflow=wf, node=short(node), node_type="CC",
                     routing={s: (nxt if s == "SUCCESS" else "EXIT_REJECTED") for s in statuses})
        for x in ("EXIT_COMPLETED", "EXIT_REJECTED"):
            self.row("execution_topology", "doctrine:order", workflow=wf, node=x, node_type="EXIT", routing=None)

        # Workflow bindings into each CC.
        sb = lambda node, f, b, s: self.row("step_bindings", s, owner=wf, step=short(node),
                                            direction="INPUT", field=f, bound_to=b)
        sb(self.auth, "staff_credentials", "payload.staff_credentials", "ledger:actor")
        for node, _, binds, nsrc in nodes:
            for f, b in binds.items():
                sb(node, f, b, nsrc)
        subject = ident[-1]
        sb(self.trail_cc, "staff_id", "payload.staff_id", "ledger:trail")
        sb(self.trail_cc, "operation", {"literal": up(op_name)}, "ledger:trail")
        sb(self.trail_cc, "record", {"literal": {"operation": up(op_name), "staff_id": "$.payload.staff_id",
                                                 "subject": f"$.payload.{subject}"}}, "ledger:trail")

        # Binding, actor, event.
        self.row("rb_declarations", "doctrine:binding", rb_code=f"{self.ns}RB_{up(self.sub)}_BINDINGS_V0",
                 binds_wf=wf, cs_bindings=[MUTABLE, REGISTRY, APPENDONLY],
                 storage_structure=f"{self.ns}STRUCTURE_{up(self.sub)}_STORAGE_V0")
        self.row("artifact_properties", "ledger:actor", artifact=wf, property="actor_context", value=self.ac)
        event = self.l["announces"].get(op_name)
        if event:
            ev, esrc = self.code("EV", event), "ledger:announces"
            self.artifact("EV", event, f"A {event}", esrc)
            self.row("artifact_properties", esrc, artifact=wf, property="emit.EXIT_COMPLETED", value=[ev])
            for f in ident:
                self.field(ev, "OUTPUT", f, "string", "doctrine:interface")
            self.field(ev, "OUTPUT", "staff_id", "string", "doctrine:interface")
            self.field(ev, "OUTPUT", "timestamp", "string", "doctrine:interface", "When the moment occurred",
                       fmt="date-time")

    def run(self):
        self.stores = {}
        self.shared()
        for op_name, op in self.l["operations"].items():
            self.workflow(op_name, op)
        for name, (cs, src) in self.stores.items():
            self.row("structure_stores", f"{src} + doctrine:storage", store_name=name,
                     storage_type=cs.split("::")[-1],
                     proposed_path=f"{self.l['domain']}/{self.sub}/{name.lower()}"
                                   f"{'.jsonl' if cs == REGISTRY else '.json'}",
                     used_by=", ".join(sorted(self.store_users.get(name, ()))),
                     structure=f"{self.ns}STRUCTURE_{up(self.sub)}_STORAGE_V0")
        return self.reg


if __name__ == "__main__":
    ledger = yaml.safe_load(open(sys.argv[1]))
    json.dump(Emitter(ledger).run(), sys.stdout, indent=1)
