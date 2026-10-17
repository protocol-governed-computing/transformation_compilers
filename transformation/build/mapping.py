"""The construction mapping as construction performs it: every artifact field, by kind, with its origin.

`doc/CONSTRUCTION_MAPPING.md` states, for each kind of artifact, every field construction writes,
where its value comes from, and under which provenance class. This module reads the same thing out
of the renderer, so the standard can be checked against the code that it specifies.

A field is addressed by its dotted path with two normalisations, because a path that spells data is
not a field:
- a key the design names, such as a node, an input or a store, reads as `<name>`;
- a value the design states whole, such as a literal binding or a test value, reads as `<value>`,
  and nothing beneath it is a field.
"""

from __future__ import annotations

import re
from typing import Any

from transformation.build.provenance import origin as _origin
from transformation.build.render import render_all

# Containers whose keys are names the design gives, by artifact kind. A path pattern, with `[]` for
# a list position and `<name>` for a key already normalised.
NAMED: dict[str, tuple[str, ...]] = {
    "ACTOR": ("core.attributes",),
    "CAPABILITY_CONTRACT": ("core.inputs", "core.outputs", "core.pipeline.[].inputs",
                            "core.pipeline.[].inputs.fields", "core.pipeline.[].inputs.parameters",
                            "core.pipeline.[].outputs", "core.pipeline.[].on_result"),
    "CAPABILITY_TRANSFORM": ("core.inputs", "core.outputs", "machine.atom_stream.[].inputs",
                             "machine.atom_stream.[].accumulator", "machine.atom_stream.[].with",
                             "machine.atom_stream.[].update_accumulator", "machine.emit"),
    "EVENT": ("core.schema",),
    "INTENT": ("core.inputs", "core.outcomes"),
    "RUNTIME_BINDING": ("core.bindings", "core.bindings.<name>.policy"),
    "STRUCTURE": ("core.entity_stores",),
    "TEST_DATA": ("cases.[].bindings", "cases.[].expected", "cases.[].assertions"),
    "TRANSPORT_INGRESS": ("handler.payload_template", "input_contract"),
    "TRANSPORT_EGRESS": ("core.response_template", "result_classification"),
    "WORKFLOW": ("core.nodes", "core.nodes.<name>.inputs", "core.nodes.<name>.next"),
}
BUILD_MANIFEST = re.compile(r"^[a-z_]+::STRUCTURE_BUILD_[A-Z_]+_CONFIG_V0$")
# Fields whose value the design states whole: nothing beneath them is a field of the artifact.
WHOLE = re.compile(r"(?:^|\.)(?:default|cases\.\[\]\.(?:bindings|expected|assertions)\.<name>|cases\.\[\]\.recorded|"
                   r"core\.nodes\.<name>\.inputs\.<name>|core\.pipeline\.\[\]\.inputs(?:\.fields|\.parameters)?\.<name>|"
                   r"handler\.payload_template\.<name>|core\.response_template\.<name>|"
                   r"machine\.atom_stream\.\[\]\.(?:inputs|accumulator|with|update_accumulator)\.<name>|machine\.emit\.<name>)$")


def _fields(kind: str, value: Any, path: tuple[str, str] = ()):
    """Every field of a rendered machine block, normalised, with the raw path it was read at."""
    named = NAMED.get(kind, ())
    if path and WHOLE.search(path[0]):
        yield path
        return
    if isinstance(value, dict) and value:
        for key, item in value.items():
            # A vocabulary's groups are named by the design, beside the header every artifact has.
            if not path and kind == "VOCABULARY" and isinstance(item, dict) and "entries" in item:
                norm = "<group>"
            elif path:
                norm = f"{path[0]}.{'<name>' if path[0] in named else key}"
            else:
                norm = key
            raw = f"{path[1]}.{key}" if path else key
            yield from _fields(kind, item, (norm.lstrip("."), raw))
    elif isinstance(value, list) and value:
        for i, item in enumerate(value):
            yield from _fields(kind, item, (f"{path[0]}.[]", f"{path[1]}.{i}"))
    elif path:
        yield path


def inventory(p7: dict, p8: dict) -> set[tuple[str, str, str, str]]:
    """`(kind, field, provenance class, what governs it)` for every field the design renders into."""
    out = set()
    for artifact in render_all(p7, p8):
        machine = artifact["machine"]
        kind = machine.get("artifact_kind", "")
        supplied = artifact.get("supplied") or {}
        for norm, raw in _fields(kind, machine):
            origin, governed = _origin(supplied, raw)
            # A domain's build manifest governs its own transforms: one rule, read as one.
            governed = BUILD_MANIFEST.sub("<domain>::STRUCTURE_BUILD_<DOMAIN>_CONFIG_V0", governed)
            out.add((kind, norm, origin, governed))
    return out
