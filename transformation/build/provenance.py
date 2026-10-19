"""Where each rendered value came from — addressed, looked up and attributed here, once.

Construction asks one question of every leaf it renders: did the design state it? The renderer is
the only thing that knows, because it is the thing that put the value there, so it records each
departure as it renders. This module turns those records into the provenance of every leaf, and it
is the only place that does. `CT_PURE_ATTRIBUTE_PROVENANCE_V0` attributes with it, and the
completeness measure reads the provenance it is handed rather than deriving its own.

  stated_by_design           a register of the design carries it
  governed_elsewhere         a constitution fixes it, and the artifact fixing it is named
  carried_from_predecessor   the artifact already carried it and no register can express it
  supplied_by_renderer       the renderer wrote it on its own authority, and nothing governs it

Only the last is unaccounted for. Silence means the design stated it: a builder reaches for a
register and writes what it finds, so the ordinary case needs no record and only a departure does.

A leaf is addressed by its dotted path in the artifact's Machine block, a list item by its index:
`core.pipeline[0].inputs`. An empty object or list is a leaf, because a design can leave one empty
and the measure must see it. Provenance is keyed `<artifact code>.<path>`.

CONSTITUTIONAL: Pure — no I/O, no clock, no filesystem.
"""
from __future__ import annotations

from typing import Any, Iterator

STATED_BY_DESIGN = "stated_by_design"
GOVERNED_ELSEWHERE = "governed_elsewhere"
SUPPLIED_BY_RENDERER = "supplied_by_renderer"
CARRIED_FROM_PREDECESSOR = "carried_from_predecessor"


def leaves(value: Any, path: str = "") -> Iterator[tuple[str, Any]]:
    """Every leaf of a rendered Machine block, as `(path, value)`."""
    if isinstance(value, dict) and value:
        for key, item in value.items():
            yield from leaves(item, f"{path}.{key}" if path else key)
    elif isinstance(value, list) and value:
        for index, item in enumerate(value):
            yield from leaves(item, f"{path}[{index}]")
    else:
        yield path, value


def origin(records: dict, path: str) -> tuple[str, str]:
    """The origin recorded for a leaf, and what governs it where anything does.

    A record on an ancestor covers what hangs beneath it: a builder supplying a whole field supplies
    every leaf of it, and making it enumerate them would be asking it to walk a shape it has not
    finished building.
    """
    def entry(record: Any) -> tuple[str, str]:
        return tuple(record) if isinstance(record, (list, tuple)) else (record, "")

    if path in records:
        return entry(records[path])
    for ancestor, record in records.items():
        if path.startswith(ancestor + "."):
            return entry(record)
    return (STATED_BY_DESIGN, "")


def code_of(machine: dict) -> str:
    return str(machine.get("fqdn", "")).split("::")[-1]


def attribute(rendered: list[dict], sources: dict) -> dict[str, dict[str, str]]:
    """The provenance of every leaf of every rendered artifact, and what governs those that are.

    `sources` is the renderer's record per artifact code: `{code: {path: (origin, governed_by)}}`.
    """
    provenance: dict[str, str] = {}
    governing: dict[str, str] = {}
    for artifact in rendered:
        machine = artifact.get("machine") or {}
        code = code_of(machine)
        records = (sources or {}).get(code) or {}
        for path, _ in leaves(machine):
            found, governed_by = origin(records, path)
            provenance[f"{code}.{path}"] = found
            if governed_by:
                governing[f"{code}.{path}"] = governed_by
    return {"provenance": provenance, "governing_artifacts": governing}


def of(rendered: list[dict]) -> dict[str, str]:
    """The provenance of a render, from the records it carries — what the governed contract's
    attribution step computes, for a caller holding the render itself."""
    sources = {code_of(a.get("machine") or {}): a.get("supplied") or {} for a in rendered}
    return attribute(rendered, sources)["provenance"]
