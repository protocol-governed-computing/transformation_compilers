"""A baseline P7: the design of record of a registry, read from the registry.

Every register is the inverse of construction. Each function here reads back from an artifact what
the matching builder in `transformation.build.render` reads to write it, so construction of the
design reproduces the registry. Where the design language cannot state a fact an artifact holds,
construction reproduces it wrongly or not at all, and `construction_acceptance` reports the
difference. The generator never states such a fact some other way.

A baseline design is a design of record, read by construction. It is not a phase document a rule
set judges: it has no P0 to P6 to cite, so its rows carry no `source_finding`. A change after the
baseline is a dossier, designed against the composition, whose P7 is judged in full.
"""
from __future__ import annotations

from typing import Any

# The roots a contract or workflow binding is rendered with `$.` restored (`render._binding`).
_PATH_ROOTS = ("payload.", "results.", "inputs.", "capability_result.", "result_status")
# The roots a molecule binding is rendered with `$.` restored (`render._molecule_source`).
_MOLECULE_ROOTS = ("inputs.", "results.", "accumulator.")
# Header keys every builder writes from the identity and the family. No register states them.
_HEADER = ("fqdn", "artifact_kind", "version", "governed_by", "authority", "concern", "supersedes")


def _bound(value: Any) -> Any:
    """A contract or workflow binding as the design states it: a path, or a literal."""
    if isinstance(value, str) and value.startswith("$.") and value[2:].startswith(_PATH_ROOTS):
        return value[2:]
    return {"literal": value}


def _molecule_bound(value: Any) -> Any:
    if value == "$.iterator":
        return "iterator"
    if isinstance(value, str) and value.startswith("$.") and value[2:].startswith(_MOLECULE_ROOTS):
        return value[2:]
    return {"literal": value}


def _text_bound(value: Any) -> Any:
    """A boundary binding: a text the boundary resolves passes as written; anything else is a literal."""
    if isinstance(value, str) and value == " ".join(value.split()) and value:
        return value
    return {"literal": value}


def _fields(a: dict, rows: list, side: str, direction: str, spec_of=None) -> None:
    held = spec_of if spec_of is not None else (a["machine"].get("core") or {}).get(side) or {}
    for name, spec in held.items():
        spec = spec or {}
        row = {"artifact": a["fqdn"], "direction": direction, "field": name,
               "type": spec.get("type"), "required": "YES" if spec.get("required") else "NO",
               "default": spec.get("default"),
               "meaning": " ".join(str(spec.get("description") or name.replace("_", " ")).split())}
        if spec.get("format"):
            row["format"] = spec["format"]
        if spec.get("structure"):
            row["structure"] = spec["structure"]
        rows.append(row)


def _prop(rows: list, a: dict, prop: str, value: Any) -> None:
    rows.append({"artifact": a["fqdn"], "property": prop, "value": value})


class Design:
    """The registers of one registry's baseline design, filled artifact by artifact."""

    def __init__(self, held: list[dict], vectors: list[dict]):
        self.held = held
        self.vectors = vectors
        self.by_fqdn = {a["fqdn"]: a for a in held}
        self.r: dict[str, list] = {name: [] for name in (
            "new_artifacts", "rb_declarations", "execution_topology", "cc_composition",
            "step_bindings", "interface_fields", "implementation_bindings", "vocabulary_extensions",
            "runtime_policies", "artifact_properties", "structure_stores", "transport_bindings",
            "declared_reach", "molecule_steps", "molecule_step_bindings", "test_cases",
            "test_case_values")}

    # The artifact as a whole ------------------------------------------------------------------

    def add(self, a: dict) -> None:
        core = a["machine"].get("core") or {}
        self.r["new_artifacts"].append({
            "family": a["family"], "code": a["fqdn"],
            "summary": " ".join(str(core.get("summary") or "").split()),
            "owner_subdomain": a["subdomain"], "status": "NEW"})
        supersedes = a["machine"].get("supersedes")
        if supersedes:
            _prop(self.r["artifact_properties"], a, "supersedes",
                  supersedes if isinstance(supersedes, list) else [supersedes])
        getattr(self, "_" + a["family"].lower())(a)

    # One per builder in `render._BUILDERS` -----------------------------------------------------

    def _in(self, a: dict) -> None:
        _fields(a, self.r["interface_fields"], "inputs", "INPUT")

    def _wf(self, a: dict) -> None:
        m, core = a["machine"], a["machine"]["core"]
        if core.get("actor_context"):
            _prop(self.r["artifact_properties"], a, "actor_context", core["actor_context"])
        if m.get("consults"):
            self.r["declared_reach"].append({"act": a["fqdn"], "consults": list(m["consults"])})
        start = core.get("start_node")
        nodes = list(core["nodes"].items())
        # The renderer takes the first IN node as the start, so the start is written first.
        nodes.sort(key=lambda kv: kv[0] != start)
        for key, node in nodes:
            if node["type"] == "EXIT":
                self.r["execution_topology"].append({
                    "workflow": a["fqdn"], "node": key, "node_type": "EXIT", "routing": None})
                emit = node.get("emit")
                if emit:
                    _prop(self.r["artifact_properties"], a, f"emit.{key}",
                          emit if isinstance(emit, list) else [emit])
                continue
            row = {"workflow": a["fqdn"], "node": key, "node_type": node["type"],
                   "routing": dict(node.get("next") or {})}
            if node.get("code") and node["code"] != key:
                row["runs"] = node["code"]
            self.r["execution_topology"].append(row)
            for field, value in (node.get("inputs") or {}).items():
                self.r["step_bindings"].append({"owner": a["fqdn"], "step": key, "direction": "INPUT",
                                                "field": field, "bound_to": _bound(value)})

    def _cc(self, a: dict) -> None:
        core = a["machine"]["core"]
        _fields(a, self.r["interface_fields"], "inputs", "INPUT")
        _fields(a, self.r["interface_fields"], "outputs", "OUTPUT")
        for index, step in enumerate(core.get("pipeline") or [], start=1):
            is_cs = "side_effect" in step
            consumes = list((step.get("inputs") or {}).keys())
            produces = list((step.get("outputs") or {}).keys())
            self.r["cc_composition"].append({
                "cc_code": a["fqdn"], "step": str(index), "step_name": step["step"],
                "capability": step.get("side_effect") or step.get("transform"),
                "kind": "CS" if is_cs else "CT", "operation": step.get("op") if is_cs else None,
                "store": step.get("store"), "consumes": consumes or None, "produces": produces,
                "routing": dict(step.get("on_result") or {}), "interpreted_by": None,
                "semantic_status": "SUCCESS",
                "interface": {"in": {f: f for f in consumes}, "out": {f: f for f in produces}}})
            for direction, side in (("INPUT", "inputs"), ("OUTPUT", "outputs")):
                for field, value in (step.get(side) or {}).items():
                    self.r["step_bindings"].append({
                        "owner": a["fqdn"], "step": step["step"], "direction": direction,
                        "field": field, "bound_to": _bound(value)})

    def _ct(self, a: dict) -> None:
        m, core = a["machine"], a["machine"].get("core") or {}
        machine = m.get("machine") or {}
        _fields(a, self.r["interface_fields"], "inputs", "INPUT")
        _fields(a, self.r["interface_fields"], "outputs", "OUTPUT")
        self.r["implementation_bindings"].append({
            "ct_code": a["fqdn"],
            "callable": (machine.get("implementation") or {}).get("callable"),
            "operation": machine.get("operation"), "kind": machine.get("ct_kind"),
            "purity": machine.get("ct_purity"), "refusal": core.get("refusal")})
        if machine.get("ct_kind") == "molecule":
            emitted = {step: name for name, step in (machine.get("emit") or {}).items()}
            for entry in machine.get("atom_stream") or []:
                kind = entry["kind"]
                step = entry["as"]
                self.r["molecule_steps"].append({
                    "ct_code": a["fqdn"], "step": step, "kind": kind,
                    "target": entry.get("atom") if kind == "atom" else entry.get("molecule"),
                    "over": entry["over"][2:] if kind == "loop" else None,
                    "iterator": entry.get("iterator"), "emits": emitted.get(step)})
                roles = (("accumulator", "CARRY"), ("inputs", "INPUT"), ("update_accumulator", "UPDATE")) \
                    if kind == "loop" else (("with", "INPUT"),)
                for key, role in roles:
                    for field, value in (entry.get(key) or {}).items():
                        self.r["molecule_step_bindings"].append({
                            "ct_code": a["fqdn"], "step": step, "role": role, "field": field,
                            "bound_to": _molecule_bound(value)})
        for vector in self.vectors:
            if vector.get("target") != a["fqdn"]:
                continue
            for case in vector.get("cases") or []:
                self.r["test_cases"].append({"ct_code": a["fqdn"], "case": case["case_id"],
                                             "expected_outcome": case["expected_outcome"]})
                for role, side in (("INPUT", "bindings"), ("EXPECTED", "expected"),
                                   ("ASSERT", "assertions"), ("RECORDED", "recorded")):
                    for field, value in (case.get(side) or {}).items():
                        self.r["test_case_values"].append({
                            "ct_code": a["fqdn"], "case": case["case_id"], "role": role,
                            "field": field, "value": value})

    def _ac(self, a: dict) -> None:
        core = a["machine"].get("core") or {}
        for key, value in core.items():
            if key not in ("summary", "attributes"):
                _prop(self.r["artifact_properties"], a, key, value)
        _fields(a, self.r["interface_fields"], "attributes", "ATTRIBUTE")

    def _vocab(self, a: dict) -> None:
        m = a["machine"]
        extends = m.get("extends") or None
        for group, spec in m.items():
            if group in _HEADER or not isinstance(spec, dict) or "entries" not in spec:
                continue
            meanings = spec.get("meanings") or {}
            for value in spec["entries"]:
                self.r["vocabulary_extensions"].append({
                    "vocabulary_code": a["fqdn"], "extends": extends, "group": group,
                    "casing": spec.get("casing"), "names_kind": spec.get("names_kind"),
                    "value": value,
                    "meaning": " ".join(str(meanings.get(value) or value).split())})

    def _structure(self, a: dict) -> None:
        core = a["machine"].get("core") or {}
        for name, store in (core.get("entity_stores") or {}).items():
            steps = [(c["fqdn"], step) for c in self.held if c["family"] == "CC"
                     for step in (c["machine"].get("core") or {}).get("pipeline") or []
                     if step.get("store") == name]
            users = sorted({fqdn for fqdn, _ in steps})
            kinds = sorted({step["side_effect"].split("::")[-1] for _, step in steps
                            if step.get("side_effect")})
            self.r["structure_stores"].append({
                "store_name": name, "storage_type": ", ".join(kinds) or None,
                "proposed_path": (store or {}).get("path"), "used_by": ", ".join(users) or None,
                "structure": a["fqdn"]})
        for key, value in core.items():
            if key not in ("summary", "domain", "subdomain", "entity_stores"):
                _prop(self.r["artifact_properties"], a, key, value)

    def _rb(self, a: dict) -> None:
        m, core = a["machine"], a["machine"].get("core") or {}
        bindings = core.get("bindings") or {}
        bound_wfs = [w["fqdn"] for w in self.held if w["family"] == "WF"
                     and w["machine"].get("runtime_binding") in (a["fqdn"], a["code"])]
        for wf in bound_wfs or [None]:
            self.r["rb_declarations"].append({
                "rb_code": a["fqdn"], "binds_wf": wf, "cs_bindings": list(bindings),
                "storage_structure": core.get("storage_structure")})
        for capability, spec in bindings.items():
            policy = (spec or {}).get("policy") or {}
            if not policy:
                self.r["runtime_policies"].append({"rb_code": a["fqdn"], "capability": capability,
                                                   "key": None, "value": None})
            for key, value in policy.items():
                self.r["runtime_policies"].append({"rb_code": a["fqdn"], "capability": capability,
                                                   "key": key, "value": value})
        if m.get("parameters"):
            _prop(self.r["artifact_properties"], a, "parameters", list(m["parameters"]))

    def _ev(self, a: dict) -> None:
        core = a["machine"].get("core") or {}
        _fields(a, self.r["interface_fields"], "", "OUTPUT", spec_of=core.get("schema") or {})
        if core.get("moment"):
            _prop(self.r["artifact_properties"], a, "moment", core["moment"])

    def _ti(self, a: dict) -> None:
        m = a["machine"]
        _fields(a, self.r["interface_fields"], "", "INPUT", spec_of=m.get("input_contract") or {})
        handler = m.get("handler") or {}
        base = {"artifact": a["fqdn"], "direction": "INGRESS", "operation": m.get("operation"),
                "handler_kind": handler.get("kind"), "handler_target": handler.get("workflow")}
        leaves = list(_leaves(handler.get("payload_template") or {}, ""))
        for path, value in leaves or [(None, None)]:
            self.r["transport_bindings"].append({**base, "field": path,
                                                 "bound_to": _text_bound(value) if path else None})

    def _te(self, a: dict) -> None:
        m = a["machine"]
        for i, row in enumerate(m.get("output_contract") or [{}]):
            out = {"artifact": a["fqdn"], "direction": "EGRESS",
                   "operation": m.get("operation") if i == 0 else None,
                   "handler_kind": None, "handler_target": None,
                   "field": row.get("field"), "bound_to": row.get("from")}
            if row.get("required") is False:
                out["required"] = False
            self.r["transport_bindings"].append(out)
        for result, cls in (m.get("result_classification") or {}).items():
            _prop(self.r["artifact_properties"], a, f"result_class.{result}", cls)
        for key in ("default_result_class", "evidence_policy"):
            if m.get(key):
                _prop(self.r["artifact_properties"], a, key, m[key])

    # The registers as a design states them -----------------------------------------------------

    def registers(self, generated: list[dict]) -> dict[str, Any]:
        out = {"design_resolution": [], "existing_inventory": []}
        out.update(self.r)
        out["generation_provenance"] = generated
        out["artifact_summary"] = [
            {"action": "NEW", "subdomain": sub, "count": str(len(codes)), "artifacts": ", ".join(codes)}
            for sub in sorted({a["subdomain"] for a in self.held})
            for codes in [[a["fqdn"] for a in self.held if a["subdomain"] == sub]]]
        for empty in ("refusal_discharge", "refusal_deferrals", "refusal_governance_discharge"):
            out[empty] = []
        out["withdrawn_facts"] = None
        return out


def _leaves(value: Any, path: str):
    """Every leaf of a payload template, addressed by its dotted path, in declared order."""
    if isinstance(value, dict) and value:
        for key, item in value.items():
            yield from _leaves(item, f"{path}.{key}" if path else key)
    else:
        yield path, value


def p7(held: list[dict], vectors: list[dict], generated: list[dict]) -> dict[str, Any]:
    """The registers of the baseline P7 for `held`, in the order the template lists them."""
    design = Design(held, vectors)
    for a in held:
        design.add(a)
    return design.registers(generated)
