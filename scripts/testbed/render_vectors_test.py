"""Render vectors — how construction renders each form of value the design language admits.

DESIGN_LANGUAGE §1.2 specifies the forms once; these vectors pin what construction makes of each. A
change to how a value renders changes a vector here, never silently an artifact.

Run:  python scripts/testbed/render_vectors_test.py
Exit: 0 when every vector holds, 1 otherwise.
"""

from __future__ import annotations

import sys

from transformation.build.render import (
    _binding, _bound_value, _molecule_source, _property_value, typed_fields,
)

# (what is rendered, the value the design states, what construction renders)
VECTORS = [
    # A contract step's binding: a path gains the runtime's root, a literal is its value.
    ("step", "payload.title", "$.payload.title"),
    ("step", "results.lookup.record", "$.results.lookup.record"),
    ("step", "capability_result.value", "$.capability_result.value"),
    ("step", "result_status", "$.result_status"),
    ("step", {"literal": 30}, 30),
    ("step", {"literal": False}, False),
    ("step", {"literal": ["a", "b"]}, ["a", "b"]),
    ("step", {"literal": ""}, ""),
    ("step", {"literal": "en"}, "en"),
    ("step", {"generated": True}, "generated"),
    # A molecule step's binding: two roots a contract step does not have.
    ("molecule", "iterator", "$.iterator"),
    ("molecule", "accumulator.total", "$.accumulator.total"),
    ("molecule", "inputs.words", "$.inputs.words"),
    ("molecule", {"literal": 0}, 0),
    # A boundary binding: a token or a surface path passes through, a constant is its value.
    ("boundary", "${input.title}", "${input.title}"),
    ("boundary", "surface.record.grounds", "surface.record.grounds"),
    ("boundary", {"literal": ["ACCEPT", "REJECT"]}, ["ACCEPT", "REJECT"]),
    ("boundary", {"literal": True}, True),
    # A property's value: text, a list of names, or a typed value.
    ("property", "append_only", "append_only"),
    ("property", ["a", "b"], ["a", "b"]),
    ("property", 3, 3),
    ("property", False, False),
]

RENDER = {
    "step": _binding,
    "molecule": _molecule_source,
    "boundary": _bound_value,
    "property": lambda v: _property_value({"value": v}),
}

# An interface field: type, format, required and default, each as the design states it.
FIELD_ROWS = [
    ({"type": "integer", "required": "NO", "default": 30}, {"type": "integer", "default": 30}),
    ({"type": "boolean", "required": "YES", "default": False}, {"type": "boolean", "required": True, "default": False}),
    ({"type": "string", "format": "date-time", "required": "YES", "default": ""},
     {"type": "string", "format": "date-time", "required": True}),
    ({"type": "array", "required": "NO", "default": "[]"}, {"type": "array", "default": "[]"}),
    ({"type": "string", "required": "NO", "default": None}, {"type": "string"}),
]


def main() -> int:
    failures = 0
    for form, stated, expected in VECTORS:
        actual = RENDER[form](stated)
        ok = actual == expected and type(actual) is type(expected)
        failures += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {form:<9} {stated!r:<40} -> {actual!r}"
              + ("" if ok else f"   expected {expected!r}"))
    for stated, expected in FIELD_ROWS:
        row = {"artifact": "d::IN_X_V0", "direction": "INPUT", "field": "f", "meaning": None, **stated}
        actual = typed_fields({"interface_fields": [row]}, "d::IN_X_V0", "INPUT")["f"]
        ok = actual == expected
        failures += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  field     {stated!r} -> {actual!r}"
              + ("" if ok else f"   expected {expected!r}"))
    total = len(VECTORS) + len(FIELD_ROWS)
    if failures:
        print(f"\nRENDER VECTORS FAILED — {failures} of {total}")
        return 1
    print(f"\nRENDER VECTORS PASSED — {total} vectors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
