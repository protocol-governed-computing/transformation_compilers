"""Load a phase's register schema: the declaration of what its document must carry.

Each phase's shape is a JSON Schema in `registry/schema/`, with an `$id`. It declares the registers,
their columns, which may be empty, which hold business prose, and which controlled vocabulary a
column draws on. Rules that follow from shape are expanded from it (`expand.py`), so it is the one
declaration of a document's shape. The phase templates are guides for an author, checked against it.

A column's vocabulary is a reference, `x-vocab: {artifact, group}`, to a group of a VOCABULARY
artifact. It is resolved from the artifact's declaration and never copied into the schema.

Every schema is validated against `SCHEMA_REGISTER_SCHEMA_V0` when it is loaded, so a schema using a
keyword the evaluator does not implement is refused rather than silently ignored.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import jsonschema
import yaml
from transformation.machine_block import MACHINE_BLOCK

REPO = Path(__file__).resolve().parents[2]
SCHEMAS = REPO / "registry" / "schema"
META = SCHEMAS / "SCHEMA_REGISTER_SCHEMA_V0.json"
REGISTRY = REPO / "registry"

# Columns that cite rather than state. A citation names its subject — including, in a grounding
# phase, a compiled artifact — so these are never business-language columns.
_PROVENANCE_COLUMNS = ("Source Finding", "Evidence")


def column_key(title: str) -> str:
    """The key a column's value is written under: its title in `snake_case`. `#`, an ordinal with no
    name, is keyed `number`. A rule names a column by title, and reads it through this."""
    return re.sub(r"[^a-z0-9]+", "_", title.strip().lower()).strip("_") or "number"


def _is_provenance_column(column: str) -> bool:
    return any(column.startswith(p) for p in _PROVENANCE_COLUMNS)


@dataclass(frozen=True)
class Register:
    """One declared register of a phase document."""

    id: str
    section_number: str | None
    section_title: str
    columns: tuple[str, ...]
    keys: tuple[str, ...] = ()
    vocabularies: dict[str, tuple[str, ...]] = field(default_factory=dict)
    required_columns: tuple[str, ...] = ()
    optional: bool = False
    business_language_scope: tuple[str, ...] | bool = ()
    # Column title → the type its value must take, for every column that carries structure.
    types: dict[str, dict] = field(default_factory=dict)

    @property
    def business_language(self) -> bool:
        """The register holds business prose throughout and must name no compiled artifact."""
        return self.business_language_scope is True

    @property
    def business_language_columns(self) -> tuple[str, ...]:
        """Columns that must hold business prose and name no compiled artifact.

        The register-wide flag exempts provenance columns: `Source Finding` and `Evidence` are
        citations by construction, and in a phase that grounds against the composition they must
        name artifacts. A scoped flag names exactly the columns it constrains.
        """
        if self.business_language_scope is True:
            return tuple(c for c in self.columns if not _is_provenance_column(c))
        by_key = dict(zip(self.keys, self.columns))
        return tuple(by_key[k] for k in self.business_language_scope or ())

    @property
    def optional_columns(self) -> tuple[str, ...]:
        required = set(self.required_columns)
        return tuple(c for c in self.columns if c not in required)

    @property
    def traceable(self) -> bool:
        """Rows cite where they came from."""
        return any(c.startswith("Source Finding") for c in self.columns)

    @property
    def headings(self) -> tuple[str, ...]:
        """Each column as a document heads it: its name, then any vocabulary it admits."""
        return tuple(
            f"{c} ({', '.join(self.vocabularies[c])})" if c in self.vocabularies else c
            for c in self.columns
        )


@dataclass(frozen=True)
class PhaseShape:
    """A phase's registers and its declared handoff, as its register schema states them."""

    phase: str
    schema_id: str
    path: Path
    registers: tuple[Register, ...]
    consumes: tuple[str, ...] = ()
    emits: tuple[str, ...] = ()
    # The upstream phases a document is judged against, and the rules the schema declares beyond
    # its shape, in declaration order (`declared.py`).
    priors: tuple[str, ...] = ()
    observations: dict[str, str] = field(default_factory=dict)
    entries: tuple[dict, ...] = ()
    # The header: the fields a document must state, and each field's declaration with `$ref` and
    # vocabularies resolved, so it can be sealed into the rule that checks it.
    document_required: tuple[str, ...] = ()
    document: dict[str, dict] = field(default_factory=dict)
    revisions: tuple[dict, ...] = ()

    def register(self, register_id: str) -> Register:
        for r in self.registers:
            if r.id == register_id:
                return r
        raise KeyError(f"{self.phase} declares no register {register_id!r}")


@lru_cache(maxsize=None)
def vocabulary_group(artifact: str, group: str) -> tuple[str, ...]:
    """The entries of one group of a VOCABULARY artifact, read from its declaration."""
    code = artifact.split("::")[-1]
    found = sorted(REGISTRY.rglob(f"{code}.md"))
    if not found:
        raise KeyError(f"vocabulary {artifact} is declared nowhere in {REGISTRY}")
    machine = yaml.safe_load(MACHINE_BLOCK.search(found[0].read_text(encoding="utf-8")).group(1))
    if machine.get("fqdn") != artifact:
        raise KeyError(f"{found[0]} declares {machine.get('fqdn')}, not {artifact}")
    if group not in machine:
        raise KeyError(f"vocabulary {artifact} has no group {group!r}")
    return tuple(machine[group]["entries"])


@lru_cache(maxsize=None)
def _meta() -> dict:
    return json.loads(META.read_text(encoding="utf-8"))


def _resolved(declared_type: dict, schema: dict) -> dict:
    """A column's type, with a `$ref` to the schema's `$defs` replaced by what it names."""
    if "$ref" not in declared_type:
        return declared_type
    name = declared_type["$ref"].removeprefix("#/$defs/")
    return {**{k: v for k, v in declared_type.items() if k != "$ref"}, **schema["$defs"][name]}


def _sealable(declared_type: dict, schema: dict) -> dict:
    """A header field's type as a rule can carry it: `$ref` resolved, a vocabulary as its entries."""
    resolved = _resolved(declared_type, schema)
    if "x-vocab" in resolved:
        rest = {k: v for k, v in resolved.items() if k != "x-vocab"}
        return {**rest, "enum": list(vocabulary_group(**resolved["x-vocab"]))}
    if "properties" in resolved:
        return {**resolved, "properties": {k: _sealable(v, schema) for k, v in resolved["properties"].items()}}
    return resolved


def read_schema(path: Path, phase: str) -> PhaseShape:
    """Parse a register schema. One that the meta-schema refuses is fail-hard."""
    declared = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.validate(declared, _meta())
    registers: list[Register] = []
    for register_id, body in declared["properties"]["registers"]["properties"].items():
        section = body.get("x-section") or {}
        if body["type"] == "string":
            registers.append(Register(id=register_id, section_number=section.get("number"),
                                      section_title=section.get("title", ""), columns=(),
                                      optional=False))
            continue
        items = body["items"]
        keys = tuple(items["properties"])
        columns = tuple(items["properties"][k]["title"] for k in keys)
        vocabularies = {
            items["properties"][k]["title"]: vocabulary_group(**items["properties"][k]["x-vocab"])
            for k in keys if "x-vocab" in items["properties"][k]
        }
        required = set(items.get("required") or ())
        text = {"type": ["string", "null"]}
        types = {}
        for k in keys:
            declared_type = _resolved({t: v for t, v in items["properties"][k].items()
                                       if t not in ("title", "x-vocab")}, declared)
            if declared_type != text:
                types[items["properties"][k]["title"]] = declared_type
        scope = body.get("x-business-language", ())
        registers.append(Register(
            id=register_id,
            section_number=section.get("number"),
            section_title=section.get("title", ""),
            columns=columns,
            keys=keys,
            vocabularies=vocabularies,
            required_columns=tuple(c for k, c in zip(keys, columns) if k in required),
            optional=body.get("minItems", 0) == 0,
            business_language_scope=scope if scope is True else tuple(scope),
            types=types,
        ))
    return PhaseShape(
        phase=phase,
        schema_id=declared["$id"],
        path=path,
        registers=tuple(registers),
        consumes=tuple(declared.get("x-consumes") or ()),
        emits=tuple(declared.get("x-emits") or ()),
        priors=tuple(declared.get("x-priors") or ()),
        observations=dict(declared.get("x-observations") or {}),
        entries=tuple(declared.get("allOf") or ()),
        document_required=tuple(declared["properties"]["document"]["required"]),
        document={name: _sealable(body, declared)
                  for name, body in declared["properties"]["document"]["properties"].items()},
        revisions=tuple(declared.get("x-revisions") or ()),
    )


@lru_cache(maxsize=None)
def load(phase: str) -> PhaseShape:
    """Load a phase's register schema, named by the phase catalogue."""
    from transformation.design.catalog import phase as phase_spec

    return read_schema(SCHEMAS / phase_spec(phase).schema, phase)
