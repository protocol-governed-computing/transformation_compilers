"""The shared base of the composer: steps, components, stores, the carried surface, and rendering.

`compose.py` selects building blocks from a ledger and groups them into components. This module
holds what it builds on:
- `Step` and `Component`, and the statuses each capability answers;
- `Domain`: the ledger's parts, stores named under the carried surface, request shapes and trail
  record keys carried from the baseline, and the renderer that turns components and workflows into
  P7 rows. Every row carries `_from`: the ledger entry, the doctrine rule or the carried fact it
  comes from;
- the doctrine check. Doctrine is `doctrine.yaml`, sealed (`seal.py`). A row that follows a rule
  cites it as `doctrine:<name>`, and a citation of a rule the doctrine does not state is refused.

Realization inventory: transforms whose implementation is code (key formation, select, group) are
carried from the baseline with their test cases. The ledger decides what they compute; it does not
author their implementation.
"""
import json
import re
from pathlib import Path

import yaml

from transformation.design.derive import seal
from transformation.machine_block import machine_yaml

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
    "COUNT": ["SUCCESS", "BACKEND_ERROR"],
    None: ["SUCCESS", "VIOLATION"],
}
# Realization inventory carried from the baseline: the code-backed transforms.
CARRIED_REGISTERS = ("implementation_bindings", "test_cases", "test_case_values")


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
        self.actors = {n: x for n, x in ledger.get("actors", {a["name"]: a}).items() if n != "from"}
        self.enter(next(iter(self.parts)))

    def enter(self, part):
        """Generate within one part: its own stores, trail and bindings (doctrine binding)."""
        self.sub = part
        self.l = {**self.top, **self.parts[part], "subdomain": part, "things": self.things}
        self.rb, self.structure = self.rb_of(part), self.structure_of(part)
        self.trail_store = f"{up(part)}_OPERATIONS"

    def rb_of(self, part):
        """A part's binding, under the name the composition already gives the binding of the part's
        storage (carried:surface)."""
        carried = next((r["rb_code"] for r in self.base.get("rb_declarations") or []
                        if r.get("storage_structure") == self.structure_of(part)), None)
        return carried or f"{self.ns}RB_{up(part)}_BINDINGS_V0"

    def entrance(self, op_name):
        """An operation's request, under the name its callers already meet it by (carried:surface)."""
        wf = self.code("WF", op_name)
        inn = next((r["node"] for r in self.base.get("execution_topology") or []
                    if r["workflow"] == wf and r["node_type"] == "IN"), None)
        return self.ns + short(inn) if inn else self.code("IN", op_name)

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

    # -- stores ---------------------------------------------------------------------

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

    # A chain entry is (component, bindings, routing overrides, source).

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
            for name, act in self.actors.items():
                ac = self.code("AC", name)
                part = act.get("part", first)
                artifact("AC", ac, act.get("summary", f"The {name} who acts for themselves"), "ledger:actor", part)
                row("artifact_properties", "ledger:actor", artifact=ac, property="type", value=act["kind"])
                for f, spec in act["attributes"].items():
                    typ, dflt = (spec, None) if isinstance(spec, str) else (spec["type"], spec.get("default"))
                    field(ac, "ATTRIBUTE", f, typ, "ledger:actor", required="YES" if dflt is None else "NO",
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
            wf, inn, src = self.code("WF", op_name), self.entrance(op_name), f"ledger:operations/{op_name}"
            artifact("WF", wf, f"The governed sequence that performs: {op_name}", src, part)
            artifact("IN", inn, f"A request to {op_name}", src, part)
            if authorized and "staff_credentials" not in request:
                field(inn, "INPUT", "staff_credentials", "object", "ledger:actor")
            for f, t in request.items():
                t, req = (t, "YES") if isinstance(t, str) else t
                field(inn, "INPUT", f, t, src if req == "YES" or authorized else src + " + carried:surface",
                      required=req)
            if authorized and "staff_id" not in request:
                field(inn, "INPUT", "staff_id", "string", "ledger:actor")
            row("rb_declarations", "doctrine:binding", rb_code=self.rb_of(part), binds_wf=wf,
                cs_bindings=mechanisms[part], storage_structure=self.structure_of(part))
            row("artifact_properties", "ledger:actor", artifact=wf, property="actor_context",
                value=self.code("AC", op["actor"]) if op.get("actor") else self.ac)
            announces = self.parts[part].get("announces", {})
            events = [self.code("EV", e) for e in announces.get(op_name, [])]
            if events:
                row("artifact_properties", "ledger:announces", artifact=wf, property="emit.EXIT_COMPLETED",
                    value=events)
            repeat = op.get("on_repeat", {}).get("announces")
            if repeat:
                row("artifact_properties", f"{src}/on_repeat", artifact=wf, property="emit.EXIT_REPEATED",
                    value=[self.code("EV", repeat)])
            for exit_, (events_, esrc) in op.get("_ends", {}).items():
                row("artifact_properties", esrc, artifact=wf, property=f"emit.{exit_}",
                    value=[self.code("EV", e) for e in events_])
            node_of = lambda entry: entry[4] if len(entry) > 4 else short(entry[0])
            row("execution_topology", "doctrine:order", workflow=wf, node=short(inn), node_type="IN",
                routing={"ACK": node_of(chain[0]), "NACK": "EXIT_REJECTED"})
            exits = ["EXIT_COMPLETED", "EXIT_REJECTED"]
            for i, entry in enumerate(chain):
                comp_code, binds, overrides, bsrc = entry[:4]
                node = node_of(entry)
                comp = self.components[comp_code]
                if comp.part != part:
                    reach.setdefault(wf, set()).add(comp.part)
                nxt = node_of(chain[i + 1]) if i + 1 < len(chain) else "EXIT_COMPLETED"
                routing = {}
                for st in comp.exits():
                    target = overrides.get(st, nxt if st == "SUCCESS" else "EXIT_REJECTED")
                    routing[st] = nxt if target == "next" else target
                    if routing[st].startswith("EXIT_") and routing[st] not in exits:
                        exits.append(routing[st])
                runs = {"runs": short(comp_code)} if node != short(comp_code) else {}
                row("execution_topology", bsrc if overrides else "doctrine:order", workflow=wf,
                    node=node, node_type="CC", routing=routing, **runs)
                for f, b in binds.items():
                    row("step_bindings", bsrc, owner=wf, step=node, direction="INPUT", field=f,
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
        invoked = {s.capability for c in self.components.values() for s in c.steps}
        for r in self.base["new_artifacts"]:
            if r["family"] == "CT" and r["code"] in invoked:
                reg["new_artifacts"].append({**r, "_from": "carried:realization"})
                reg["interface_fields"] += [{**f, "_from": "carried:realization"}
                                            for f in self.base["interface_fields"] if f["artifact"] == r["code"]]
        dropped = {r["code"] for r in self.base["new_artifacts"] if r["family"] == "CT"} - invoked
        names = lambda r: set(re.findall(r"[\w]+::CT_\w+", json.dumps(r)))
        for name in CARRIED_REGISTERS:
            reg[name] += [{**r, "_from": "carried:realization"} for r in self.base.get(name) or []
                          if not names(r) & dropped]
        reg["_unrealized"] = self.unrealized
        reg["_conflicts"] = self.conflicts
        return reg


DOCTRINE = seal.load("doctrine")["rules"]


def check_doctrine(reg):
    """Refuse a row citing a doctrine rule doctrine.yaml does not state."""
    cited = {m for rows in reg.values() if isinstance(rows, list) for r in rows if isinstance(r, dict)
             for m in re.findall(r"doctrine:(\w+)", str(r.get("_from", "")))}
    unknown = sorted(cited - set(DOCTRINE))
    if unknown:
        raise ValueError(f"cited doctrine not stated in the doctrine: {unknown}")
    return reg


def load_p7(path):
    """A design's registers, from its machine block, as every reader in this package finds it."""
    return yaml.safe_load(machine_yaml(Path(path).read_text(encoding="utf-8")))["registers"]

