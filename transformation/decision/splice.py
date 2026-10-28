"""Splice derived rows into a copy of a domain's P7 and P8, for the construction check.

P7: every baseline row owned by a derived artifact is replaced by the derived rows. A store keeps the
users outside the family. A binding elsewhere that names a field the derived design dropped is
removed, and reported.
P8: derived artifacts that are new join the build order, and each workflow's dependencies are
recomputed from its derived topology.

Run as part of `tc decision build`.
"""
from pathlib import Path

import yaml

from transformation.machine_block import MACHINE_BLOCK, machine_yaml

# The column that names a row's owning artifact, per register.
OWNER = {
    "new_artifacts": "code",
    "rb_declarations": "binds_wf",
    "execution_topology": "workflow",
    "cc_composition": "cc_code",
    "step_bindings": "owner",
    "interface_fields": "artifact",
    "implementation_bindings": "ct_code",
    "runtime_policies": "rb_code",
    "artifact_properties": "artifact",
    "structure_stores": "store_name",
    "test_cases": "ct_code",
    "test_case_values": "ct_code",
    "declared_reach": "act",
    "transport_bindings": "artifact",
    "vocabulary_extensions": "vocabulary_code",
}


def short(code):
    return str(code).split("::")[-1]



def read(path):
    text = path.read_text(encoding="utf-8")
    return text, yaml.safe_load(machine_yaml(text))


def write(path, text, doc):
    block = yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100).rstrip("\n")
    found = MACHINE_BLOCK.search(text)
    start, end = found.span("machine_yaml")
    path.write_text(text[:start] + block + text[end:], encoding="utf-8")


def clean(row):
    return {k: v for k, v in row.items() if not k.startswith("_")}


def splice_p7(reg, gen, whole=False):
    members = {short(r[OWNER[name]]) for name, rows in gen.items() for r in rows}
    report = []
    if whole:
        # The derived design is the whole domain: every register it covers is replaced.
        for name in OWNER:
            if name in gen or reg.get(name):
                reg[name] = [clean(r) for r in gen.get(name, [])]
        codes = [r["code"] for r in reg["new_artifacts"]]
        reg["artifact_summary"] = [{**reg["artifact_summary"][0], "count": str(len(codes)),
                                    "artifacts": ", ".join(sorted(codes))}]
        return report
    for name, rows in gen.items():
        col = OWNER[name]
        old = reg.get(name) or []
        if name == "structure_stores":
            derived = {r["store_name"]: r for r in rows}
            for r in old:
                if r["store_name"] in derived:
                    users = {u.strip() for u in r["used_by"].split(",")}
                    users = {u for u in users if short(u) not in members}
                    users |= {u.strip() for u in derived[r["store_name"]]["used_by"].split(",")}
                    r["used_by"] = ", ".join(sorted(users))
            continue
        reg[name] = [r for r in old if short(r[col]) not in members] + [clean(r) for r in rows]

    # Bindings outside the family into a family component's field that no longer exists.
    fields = {(r["artifact"], r["field"]) for r in reg["interface_fields"] if r["direction"] == "INPUT"}
    keep = []
    for r in reg["step_bindings"]:
        target = r["owner"].split("::")[0] + "::" + r["step"] if r["owner"].split("::")[-1].startswith("WF_") else None
        if (target and short(target) in members and r["direction"] == "INPUT"
                and (target, r["field"]) not in fields):
            report.append(f"dropped binding {short(r['owner'])} -> {r['step']}.{r['field']}")
            continue
        keep.append(r)
    reg["step_bindings"] = keep

    codes = [r["code"] for r in reg["new_artifacts"]]
    reg["artifact_summary"] = [{**reg["artifact_summary"][0], "count": str(len(codes)),
                                "artifacts": ", ".join(sorted(codes))}]
    return report


def identities(reg, identity):
    """The identity each artifact takes (`identity.py`), stated in the design's own registers.

    An artifact kept with its meaning is amended, not authored: it leaves `new_artifacts` and is
    named EXTEND. An artifact whose meaning changed is replaced, and its successor names it in
    `supersedes`. One the ledger no longer derives is retired (RETIRE), with no successor; the
    person delivering the change deletes it and records the deletion.
    """
    summary = {r["code"]: r["summary"] for r in reg["new_artifacts"]}
    kept = set(identity["kept"])
    reg["new_artifacts"] = [r for r in reg["new_artifacts"] if r["code"] not in kept]
    cite = lambda code: {"phase": "p7", "register": "existing_inventory", "key": short(code)}
    reg["existing_inventory"] = (
        [{"fqdn": c, "action": "EXTEND", "summary": summary.get(c, ""),
          "reason": "The ledger derives it with the meaning the composition holds.", "source_finding": cite(c)}
         for c in identity["kept"]] +
        [{"fqdn": old, "action": "REPLACE", "summary": "",
          "reason": f"The ledger derives it with a changed meaning at {identity['changed_at'][old]} place(s); "
                    f"{short(new)} succeeds it.", "source_finding": cite(old)}
         for old, new in identity["superseded"].items()] +
        [{"fqdn": old, "action": "REPLACE", "summary": "",
          "reason": f"The ledger says {short(new)} takes its place.", "source_finding": cite(old)}
         for old, new in identity.get("replaced", {}).items()] +
        [{"fqdn": old, "action": "RETIRE", "summary": "",
          "reason": "The ledger no longer derives it, and no operation takes its place.",
          "source_finding": cite(old)}
         for old in identity["retired"]])
    named = {}
    for old, new in list(identity["superseded"].items()) + list(identity.get("replaced", {}).items()):
        named.setdefault(new, []).append(old)
    reg["artifact_properties"] += [{"artifact": new, "property": "supersedes", "value": olds}
                                   for new, olds in named.items()]
    codes = [r["code"] for r in reg["new_artifacts"]]
    reg["artifact_summary"] = [{**reg["artifact_summary"][0], "count": str(len(codes)),
                                "artifacts": ", ".join(sorted(codes))}]


def splice_p8(reg8, reg7, gen):
    order = reg8["build_order"]
    live = {r["code"] for r in reg7["new_artifacts"]}
    extended = {r["fqdn"] for r in reg7.get("existing_inventory") or [] if r["action"] == "EXTEND"}
    order[:] = [r for r in order if r["code"] in live]
    for name in ("field_declarations", "critical_path", "new_capabilities", "new_intents"):
        reg8[name] = [r for r in reg8.get(name) or [] if r["code"] in live | extended]
    known = {r["code"] for r in order}
    families = {}
    for r in reg7["new_artifacts"]:
        families.setdefault(r["code"].split("::")[-1].split("_")[0], []).append(r["code"])
    for r in gen.get("new_artifacts", []):
        if r["code"] not in known and r["code"] not in extended:
            order.insert(0, {"wave": "1", "step": "0", "code": r["code"], "action": "NEW",
                             "subdomain": r["owner_subdomain"], "depends_on": None})
            reg8["field_declarations"].append({"code": r["code"], "subdomain_field": r["owner_subdomain"]})
    for i, r in enumerate(order, 1):
        r["step"] = str(i)
    # A workflow depends on its nodes, its binding, its actor and the moments it announces.
    ns = gen["new_artifacts"][0]["code"].split("::")[0] + "::"
    for wf in {r["workflow"] for r in gen.get("execution_topology", [])}:
        nodes = list(dict.fromkeys(ns + r.get("runs", r["node"]) for r in reg7["execution_topology"]
                                   if r["workflow"] == wf and r["node_type"] in ("IN", "CC")))
        emits = [v for r in reg7["artifact_properties"] if r["artifact"] == wf
                 and r["property"].startswith("emit.") for v in r["value"]]
        rb = next(r["rb_code"] for r in reg7["rb_declarations"] if r["binds_wf"] == wf)
        actor = next(r["value"] for r in reg7["artifact_properties"]
                     if r["artifact"] == wf and r["property"] == "actor_context")
        for r in order:
            if r["code"] == wf:
                r["depends_on"] = [rb, actor] + emits + nodes
    counts = {f: len(c) for f, c in families.items()}
    total = sum(counts.values())
    reg8["mandate_artifact_summary"] = [{**reg8["mandate_artifact_summary"][0], "count": str(total),
                                         "description": ", ".join(f"{n} {f}" for f, n in counts.items())}]
    # A request the derived design names that the mandate does not yet hold.
    entrance = {t["node"]: short(t["workflow"]) for t in gen.get("execution_topology", []) if t["node_type"] == "IN"}
    if gen.get("execution_topology"):
        reg8["new_intents"] = [{**r, "workflow": entrance[short(r["code"])]}
                               for r in reg8.get("new_intents") or [] if short(r["code"]) in entrance]
    held = {r["code"] for r in reg8.get("new_intents") or []}
    for r in gen.get("new_artifacts", []):
        if r["family"] == "IN" and r["code"] not in held:
            wf = next(t["workflow"] for t in gen["execution_topology"]
                      if t["node_type"] == "IN" and t["node"] == short(r["code"]))
            reg8.setdefault("new_intents", []).append({"code": r["code"], "purpose": r["summary"],
                                                       "workflow": short(wf), "inputs": ""})
    for r in reg8.get("new_intents", []):
        fields = [f"{x['field']}:{x['type']}" for x in reg7["interface_fields"]
                  if x["artifact"] == r["code"] and x["direction"] == "INPUT"]
        if any(x["artifact"] == r["code"] for x in gen.get("interface_fields", [])):
            r["inputs"] = ", ".join(fields)
    for i, r in enumerate(reg8.get("critical_path") or [], 1):
        r["position"] = str(i)


def splice(design, generated, out, mode="whole"):
    """Write the design's P7 and P8 into `out`, with the derived rows spliced in. Returns the report."""
    design, out = Path(design), Path(out)
    out.mkdir(parents=True, exist_ok=True)
    gen = {k: v for k, v in generated.items() if not k.startswith("_")}
    p7_path = next(design.glob("p7_*.md"))
    p8_path = next(design.glob("p8_*.md"))
    t7, d7 = read(p7_path)
    t8, d8 = read(p8_path)
    report = splice_p7(d7["registers"], gen, whole=(mode == "whole"))
    if generated.get("_identity"):
        identities(d7["registers"], generated["_identity"])
    splice_p8(d8["registers"], d7["registers"], gen)
    write(out / p7_path.name, t7, d7)
    write(out / p8_path.name, t8, d8)
    return report
