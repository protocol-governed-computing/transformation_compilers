"""Refuse a decision ledger whose answers fall outside their closed shapes.

Three checks, in order:
- the schema's own closure: every `x-question` in ledger_schema.yaml names a question in
  catalog.yaml, or a citation, and every catalog question the carried surface does not answer has
  a shape;
- shape: the ledger against ledger_schema.yaml (JSON Schema 2020-12);
- references: what one answer names that another must hold (a thing, a state, an operation, a
  check, a table, an event). A schema cannot state these.

Run as `tc phase derive check <ledger.yaml>...` and `tc phase derive selftest <book> <ai_governance>`.
"""
import copy

import jsonschema
import yaml

from transformation.design.derive import seal

SCHEMA = seal.load("ledger_schema")
CATALOG = seal.load("catalog")


def schema_questions(node, out=None):
    out = set() if out is None else out
    if isinstance(node, dict):
        q = node.get("x-question")
        out.update(q if isinstance(q, list) else [q] if q else [])
        for v in node.values():
            schema_questions(v, out)
    elif isinstance(node, list):
        for v in node:
            schema_questions(v, out)
    return out


def closure():
    """Every question the schema names is in the catalog."""
    known = set(CATALOG["questions"]) | {"citation", "entry"}
    named_ = schema_questions(SCHEMA)
    shaped = {q for q, d in CATALOG["questions"].items() if not d.get("carried")}
    return ([f"schema names question '{q}', which the catalog does not hold" for q in sorted(named_ - known)] +
            [f"catalog question '{q}' has no shape in the schema" for q in sorted(shaped - named_)])


def shape(ledger):
    v = jsonschema.Draft202012Validator(SCHEMA)
    return [f"{'/'.join(map(str, e.absolute_path)) or '(top)'}: {e.message}"
            for e in sorted(v.iter_errors(ledger), key=lambda e: list(map(str, e.absolute_path)))]


def parts_of(ledger):
    if "parts" in ledger:
        return ledger["parts"]
    return {ledger.get("subdomain", ledger["domain"]): {k: ledger[k] for k in
            ("things", "operations", "trail", "announces", "events", "tables") if k in ledger}}


def named(m):
    return {k: v for k, v in (m or {}).items() if k != "from"}


def references(ledger):
    errs = []
    parts = parts_of(ledger)
    things = {n: t for p in parts.values() for n, t in named(p.get("things")).items()}
    ops = {n: o for p in parts.values() for n, o in named(p.get("operations")).items()}
    actors = named(ledger.get("actors")) or {ledger["actor"]["name"]: ledger["actor"]}

    def thing(where, name):
        if name not in things:
            errs.append(f"{where}: names thing '{name}', which no part holds")
            return None
        return things[name]

    for name, t in things.items():
        for key in ("belongs_to",):
            if key in t:
                thing(f"things/{name}/{key}", t[key])
        held = t.get("held_by")
        if held and thing(f"things/{name}/held_by", held["thing"]) and held.get("requires_state"):
            if held["requires_state"] not in things[held["thing"]].get("states", []):
                errs.append(f"things/{name}/held_by: state '{held['requires_state']}' is not a state of "
                            f"{held['thing']}")
    for name, a in actors.items():
        if a.get("part") and a["part"] not in parts:
            errs.append(f"actors/{name}: names part '{a['part']}', which the ledger does not hold")

    for pname, p in parts.items():
        tables = named(p.get("tables"))
        p_ops = named(p.get("operations"))
        announced = set()
        for op_name, events in named(p.get("announces")).items():
            if op_name not in p_ops:
                errs.append(f"parts/{pname}/announces: names operation '{op_name}', which the part does not hold")
            announced.update(events)
        for op_name, o in p_ops.items():
            where = f"operations/{op_name}"
            for n in o.get("creates", []) + o.get("with", []) + [o[k] for k in ("thing", "group_by") if k in o]:
                thing(where, n)
            if o.get("actor") and o["actor"] not in actors:
                errs.append(f"{where}: names actor '{o['actor']}', which the ledger does not hold")
            t = things.get(o.get("thing"))
            for k in ("from_state", "to_state"):
                if t is not None and k in o and o[k] not in t.get("states", []):
                    errs.append(f"{where}/{k}: '{o[k]}' is not a state of {o['thing']}")
            if t is not None and "when" in o:
                fields = set(t.get("clock", [])) | set(t.get("required", {}))
                if o["when"]["since"] not in fields:
                    errs.append(f"{where}/when: since '{o['when']['since']}', which the {o['thing']} does not hold")
            if t is not None and "clock" in o.get("sets", {}).values():
                for f, v in o["sets"].items():
                    if v == "clock" and f not in t.get("clock", []):
                        errs.append(f"{where}/sets: '{f}' is set to the time, but is not a clock value of {o['thing']}")
            checked, resolved = set(), set()
            for c in o.get("checks", []):
                checked.add(c["name"])
                kind, q = next((k, v) for k, v in c.items() if k != "name")
                for k in ("thing",):
                    if k in q:
                        thing(f"{where}/checks/{c['name']}", q[k])
                if kind == "requires":
                    resolved.add(q["thing"])
                if kind == "count":
                    thing(f"{where}/checks/{c['name']}/below", q["below"]["thing"])
                if kind == "exists" and q["thing"] in things and "fixed" not in things[q["thing"]]["identity"]:
                    errs.append(f"{where}/checks/{c['name']}: exists needs a thing with a fixed identity")
                if kind == "look_up":
                    if q["table"] not in tables:
                        errs.append(f"{where}/checks/{c['name']}: names table '{q['table']}', which the part does not hold")
                    owner = q["key"].rpartition(".")[0]
                    if owner and owner not in resolved:
                        errs.append(f"{where}/checks/{c['name']}: keys on '{owner}', which no earlier check requires")
            for reason in (o.get("on_refusal", {}).get("reasons") or {}):
                if reason not in checked:
                    errs.append(f"{where}/on_refusal: gives a reason for '{reason}', which is not a check")
            for k in ("on_refusal", "on_repeat"):
                if o.get(k, {}).get("announces"):
                    announced.add(o[k]["announces"])
        for event in named(p.get("events")):
            if event not in announced:
                errs.append(f"parts/{pname}/events: '{event}' is announced by no operation")

    for op_name, r in named(ledger.get("reads_other_part")).items():
        if op_name not in ops:
            errs.append(f"reads_other_part: names operation '{op_name}', which no part holds")
        if r["part"] not in parts:
            errs.append(f"reads_other_part/{op_name}: names part '{r['part']}', which the ledger does not hold")
        for n in r["reads"]:
            thing(f"reads_other_part/{op_name}", n)
    for i, entry in enumerate(ledger.get("open") or []):
        if entry["ask"] not in CATALOG["questions"]:
            errs.append(f"open/{i}: asks '{entry['ask']}', which is not a catalog question")
        if entry["about"] not in ops:
            errs.append(f"open/{i}: is about '{entry['about']}', which no part holds as an operation")
    for i, case in enumerate(ledger.get("cases") or []):
        if case["when"] not in ops:
            errs.append(f"cases/{i}: is about '{case['when']}', which no part holds as an operation")
    for op_name in named(ledger.get("public_acts")):
        if op_name not in ops:
            errs.append(f"public_acts: names operation '{op_name}', which no part holds")
    return errs


def answered(ledger, node=SCHEMA, value=None, out=None):
    """The catalog questions a ledger's answers fall under."""
    out = set() if out is None else out
    value = ledger if value is None else value
    if not isinstance(node, dict):
        return out
    if "$ref" in node:
        node = {**SCHEMA["$defs"][node["$ref"].split("/")[-1]], **{k: v for k, v in node.items() if k != "$ref"}}
    q = node.get("x-question")
    if q and value is not None:
        out.update(q if isinstance(q, list) else [q])
    if isinstance(value, dict):
        for k, v in value.items():
            sub = (node.get("properties") or {}).get(k, node.get("additionalProperties"))
            answered(ledger, sub, v, out)
    elif isinstance(value, list) and isinstance(node.get("items"), dict):
        for v in value:
            answered(ledger, node["items"], v, out)
    return out - {"citation", "entry"}


def refusals(ledger):
    return closure() + shape(ledger) or references(ledger)


class Refused(ValueError):
    """A ledger holds an answer outside its shape."""


def refuse(ledger):
    """Raise with the refusals, when the ledger has any. The composer calls this before it derives."""
    errs = refusals(ledger)
    if errs:
        raise Refused("ledger refused:\n  " + "\n  ".join(errs))


def selftest(book_path, ai_path):
    """Answers outside their shapes, each of which must be refused."""
    book = yaml.safe_load(open(book_path))
    ai = yaml.safe_load(open(ai_path))

    def bad(base, edit):
        x = copy.deepcopy(base)
        edit(x)
        return x

    cases = {
        "an operation that names a pattern": bad(book, lambda x: x["operations"]["register book"].update(pattern="register_with_parent")),
        "an unknown kind of operation": bad(book, lambda x: x["operations"]["retire book record"].update(does="archive")),
        "a duplicate answer outside its set": bad(book, lambda x: x["things"]["book"]["identity"].update(on_duplicate="merge")),
        "a field type outside the types": bad(book, lambda x: x["things"]["book"]["required"].update(title="text")),
        "a create that also moves a state": bad(book, lambda x: x["operations"]["register book"].update(from_state="registered", to_state="retired")),
        "a query without criteria": bad(book, lambda x: x["operations"]["search catalog"].pop("criteria")),
        "a state the thing does not have": bad(book, lambda x: x["operations"]["retire book record"].update(to_state="lost")),
        "a change of a thing nobody declared": bad(book, lambda x: x["operations"]["retire book record"].update(thing="magazine")),
        "an announcement for an operation nobody declared": bad(book, lambda x: x["announces"].update({"burn book": ["book burned"]})),
        "a trail moment outside its set": bad(book, lambda x: x["trail"].update(moment="nightly")),
        "a check of two kinds at once": bad(ai, lambda x: x["parts"]["ai_licensing"]["operations"]["provision license"]["checks"][1]
                                           .update(exists={"thing": "license cap"})),
        "a refusal reason for no check": bad(ai, lambda x: x["parts"]["agent_governance"]["operations"]["govern agent action"]
                                            ["on_refusal"]["reasons"].update({"moon phase": "BAD_MOON"})),
        "a look-up in a table nobody declared": bad(ai, lambda x: x["parts"]["agent_governance"]["operations"]["govern agent action"]
                                                   ["checks"][2]["look_up"].update(table="tier budgets")),
        "a condition without its other ending": bad(ai, lambda x: x["parts"]["ai_licensing"]["operations"]["reclaim license"].pop("otherwise")),
        "a fact set to the time that is not a clock value": bad(ai, lambda x: x["parts"]["ai_licensing"]["operations"]
                                                               ["record training completed"]["sets"].update(training_completed="clock")),
        "an operation by an actor nobody declared": bad(ai, lambda x: x["parts"]["ai_licensing"]["operations"]["set license cap"]
                                                       .update(actor="auditor")),
        "an open question that names no catalog question": bad(book, lambda x: x.update(
            open=[{"ask": "favourite_colour", "about": "search catalog", "waits_on": "catalog owner"}])),
        "an open question about an operation nobody declared": bad(book, lambda x: x.update(
            open=[{"ask": "nothing_found", "about": "lend book", "waits_on": "catalog owner"}])),
        "a case about an operation nobody declared": bad(book, lambda x: x.update(
            cases=[{"when": "lend book", "then": "refused", "because": "not offered"}])),
        "a case that gives no reason": bad(book, lambda x: x.update(
            cases=[{"when": "search catalog", "then": "returns nothing"}])),
        "an answer that cites no authority": bad(book, lambda x: x["operations"]["register book"].pop("from")),
        "a ledger that does not say what it is for": bad(book, lambda x: x.pop("purpose")),
        "a thing kept for no stated reason": bad(book, lambda x: x["things"]["book"].pop("why")),
    }
    return [(name, refusals(ledger)) for name, ledger in cases.items()]
