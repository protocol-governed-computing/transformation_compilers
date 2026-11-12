"""Read the rules a register schema declares beyond its shape, and write them.

A register schema states shape by its registers and columns, and `expand.py` derives the rules that
follow from it. Everything else a phase declares is an entry of an `allOf` list: on the register it
governs, or at the top of the schema for a rule about the whole document. One entry is one rule.

Every entry carries `x-finding`: the finding code an author reads, the rule's intent, and its detail
text when it has one. What the entry states is one of three things:

- **a constraint**, in JSON Schema keywords over the register (`minItems`, `maxItems`) or over each
  row (`items`): a column that must be present, say something, match a pattern, or not start with a
  prefix; a
  column or a value that must not appear. A rule that governs only some rows states its gate with
  `if` and `then`;
- **an annotation**, relating rows to other rows: `x-key`, `x-reference`, `x-carriage` or
  `x-grounding`, each with a `mode` and the parameters that mode reads;
- **a procedure**, `x-procedure`, a named check with its parameters, for a property no keyword or
  annotation states.

`decode` turns an entry into the rule the evaluator runs. `encode` is its inverse, used once to move
the rules out of code; every rule it writes is decoded again and must come back unchanged.
"""

from __future__ import annotations

import re
from typing import Any

from transformation.design.rules import Rule

ANNOTATIONS = {
    "x-key": {"unique": "COLUMN_VALUES_UNIQUE", "contiguous": "COLUMN_SEQUENCE_CONTIGUOUS"},
    "x-reference": {"resolves": "CELL_RESOLVES_IN_REGISTER", "covers": "REGISTER_COVERS_REGISTER"},
    "x-carriage": {
        "present_by_key": "PRIOR_ROWS_PRESENT_BY_KEY",
        "confined": "ROWS_CONFINED_TO_PRIOR",
        "cited": "PRIOR_ROWS_CITED",
        "matches_cited": "PRIOR_ROW_MATCHES_CITED",
        "identities_covered": "PRIOR_IDENTITIES_COVERED",
        "prose": "PRIOR_PROSE_CARRIED",
    },
    "x-grounding": {
        "exists": "CITED_ARTIFACTS_RESOLVE",
        "absent": "CITED_ARTIFACTS_ABSENT",
        "reuse_eligible": "REUSE_CANDIDATE_ELIGIBLE",
    },
}
_ANNOTATED = {kind: (construct, mode) for construct, modes in ANNOTATIONS.items()
              for mode, kind in modes.items()}

# Constraint kinds and the parameters each states as keywords. Anything else a rule of that kind
# carries is a reason it is not a constraint, and `encode` refuses it.
_GATE = {"only_when_column", "only_when_value", "only_when_values"}
CONSTRAINTS = {
    "CELL_NOT_EMPTY": {"column", "detail"} | _GATE,
    "CELL_PRESENT": {"column", "detail"},
    "CELL_MATCHES": {"column", "pattern", "detail"} | _GATE,
    "CELL_TOKEN_ABSENT": {"columns", "pattern", "detail"},
    "COLUMN_ABSENT": {"column", "detail"},
    "ROW_ABSENT_WHEN": {"column", "value", "detail"},
    "TABLE_ROW_COUNT": {"maximum", "detail"},
    "TABLE_HAS_ROWS": {"minimum"},
}


class Columns:
    """A register's columns, by the title a rule names and the key a row carries.

    A rule may name a column the register does not declare: one that must be absent. Its key is the
    title in `snake_case`, and the entry records the title under `x-columns` so it reads back.
    """

    def __init__(self, titles: dict[str, str], undeclared: dict[str, str] | None = None):
        self.by_title = dict(titles)
        self.by_key = {k: t for t, k in titles.items()}
        self.undeclared = dict(undeclared or {})
        self.by_key.update(self.undeclared)

    def key(self, title: str) -> str:
        if title in self.by_title:
            return self.by_title[title]
        key = re.sub(r"[^a-z0-9]+", "_", title.strip().lower()).strip("_")
        self.undeclared[key] = title
        self.by_key[key] = title
        return key

    def title(self, key: str) -> str:
        return self.by_key[key]

    def with_entry(self, entry: dict) -> "Columns":
        """These columns, plus the undeclared ones an entry names."""
        return Columns(self.by_title, {**self.undeclared, **entry.get("x-columns", {})})


def _finding(rule: Rule) -> dict[str, Any]:
    out: dict[str, Any] = {"code": rule.id, "intent": rule.intent}
    if "detail" in rule.params:
        out["detail"] = rule.params["detail"]
    return out


def _gate(params: dict, cols: Columns) -> dict | None:
    column = params.get("only_when_column")
    if not column:
        return None
    if "only_when_values" in params:
        test = {"enum": list(params["only_when_values"])}
    else:
        test = {"const": params["only_when_value"]}
    return {"properties": {cols.key(column): test}, "required": [cols.key(column)]}


def _row(rule: Rule, cols: Columns | None, body: dict) -> dict:
    gate = _gate(rule.params, cols) if cols else None
    return {"items": {"if": gate, "then": body}} if gate else {"items": body}


def encode(rule: Rule, cols: Columns | None) -> dict:
    """The schema entry stating one rule."""
    p, kind = rule.params, rule.check
    entry: dict[str, Any] = {"x-finding": _finding(rule)}
    if kind in CONSTRAINTS and set(p) <= CONSTRAINTS[kind]:
        if kind == "CELL_NOT_EMPTY":
            k = cols.key(p["column"])
            entry.update(_row(rule, cols, {"properties": {k: {"minLength": 1}}}))
        elif kind == "CELL_PRESENT":
            entry["items"] = {"required": [cols.key(p["column"])]}
        elif kind == "CELL_MATCHES":
            k = cols.key(p["column"])
            entry.update(_row(rule, cols, {"properties": {k: {"pattern": p["pattern"]}}}))
        elif kind == "CELL_TOKEN_ABSENT":
            entry["items"] = {"properties": {cols.key(c): {"not": {"pattern": p["pattern"]}}
                                             for c in p["columns"]}}
        elif kind == "COLUMN_ABSENT":
            entry["items"] = {"not": {"required": [cols.key(p["column"])]}}
        elif kind == "ROW_ABSENT_WHEN":
            k = cols.key(p["column"])
            entry["items"] = {"not": {"properties": {k: {"const": p["value"]}}, "required": [k]}}
        elif kind == "TABLE_ROW_COUNT":
            entry["maxItems"] = p["maximum"]
        elif kind == "TABLE_HAS_ROWS":
            entry["minItems"] = p["minimum"]
    elif kind in _ANNOTATED:
        construct, mode = _ANNOTATED[kind]
        entry[construct] = {"mode": mode, "params": dict(p)}
    else:
        entry["x-procedure"] = {"name": kind, "params": dict(p)}
    if cols and cols.undeclared:
        entry["x-columns"] = dict(cols.undeclared)
    decoded = decode(entry, rule.register, Columns(cols.by_title) if cols else None)
    if decoded != rule:
        raise ValueError(f"{rule.id} on {rule.register} does not round-trip:\n  {rule}\n  {decoded}")
    return entry


def _ungate(items: dict, cols: Columns) -> tuple[dict, dict]:
    """A row constraint's body, and the gate params it was stated under."""
    if "if" not in items:
        return items, {}
    gate = items["if"]
    (key, test), = gate["properties"].items()
    params: dict[str, Any] = {"only_when_column": cols.title(key)}
    if "enum" in test:
        params["only_when_values"] = list(test["enum"])
    else:
        params["only_when_value"] = test["const"]
    return items["then"], params


def decode(entry: dict, register: str | None, cols: Columns | None) -> Rule:
    """The rule one schema entry states."""
    finding = entry["x-finding"]
    cols = cols.with_entry(entry) if cols else None
    detail = {"detail": finding["detail"]} if "detail" in finding else {}

    def rule(check: str, params: dict) -> Rule:
        return Rule(id=finding["code"], check=check, register=register, params=params,
                    intent=finding["intent"])

    for construct in ANNOTATIONS:
        if construct in entry:
            body = entry[construct]
            return rule(ANNOTATIONS[construct][body["mode"]], dict(body["params"]))
    if "x-procedure" in entry:
        return rule(entry["x-procedure"]["name"],
                    {k: _parameter(v) for k, v in entry["x-procedure"]["params"].items()})
    if "maxItems" in entry:
        return rule("TABLE_ROW_COUNT", {"maximum": entry["maxItems"], **detail})
    if "minItems" in entry:
        return rule("TABLE_HAS_ROWS", {"minimum": entry["minItems"]})
    items = entry["items"]
    if "not" in items:
        negated = items["not"]
        if "properties" in negated:
            (k, test), = negated["properties"].items()
            return rule("ROW_ABSENT_WHEN", {"column": cols.title(k), "value": test["const"], **detail})
        return rule("COLUMN_ABSENT", {"column": cols.title(negated["required"][0]), **detail})
    if set(items) == {"required"}:
        return rule("CELL_PRESENT", {"column": cols.title(items["required"][0]), **detail})
    body, gate = _ungate(items, cols)
    properties = body["properties"]
    if all("not" in v for v in properties.values()):
        pattern = next(iter(properties.values()))["not"]["pattern"]
        return rule("CELL_TOKEN_ABSENT", {"columns": [cols.title(k) for k in properties],
                                          "pattern": pattern, **detail})
    (k, test), = properties.items()
    if "minLength" in test:
        return rule("CELL_NOT_EMPTY", {"column": cols.title(k), **gate, **detail})
    return rule("CELL_MATCHES", {"column": cols.title(k), "pattern": test["pattern"], **gate, **detail})


def entries(declared: Any) -> list[dict]:
    """The `allOf` entries of a schema node, in order."""
    return list((declared or {}).get("allOf") or [])


__all__ = ["ANNOTATIONS", "CONSTRAINTS", "Columns", "decode", "encode", "entries"]


def _parameter(value: Any) -> Any:
    """A procedure parameter, with what it references read in so the sealed rule is complete.

    - `{"x-dispatch": <field>}` reads as that field of every phase in
      `transformation::STRUCTURE_REGISTER_SCHEMA_DISPATCH_V0`, keyed by phase.
    - `{"x-vocab": {"artifact": …, "group": …}}` reads as that vocabulary group's entries.

    Either way the schema does not hold a second copy of what it names."""
    if isinstance(value, dict) and set(value) == {"x-dispatch"}:
        from transformation.design.catalog import PHASES

        return {spec.id: getattr(spec, value["x-dispatch"]) for spec in PHASES}
    if isinstance(value, dict) and set(value) == {"x-vocab"}:
        from transformation.design.schema import vocabulary_group

        return list(vocabulary_group(**value["x-vocab"]))
    return value
