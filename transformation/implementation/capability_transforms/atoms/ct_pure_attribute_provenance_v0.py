"""CT_PURE_ATTRIBUTE_PROVENANCE_V0 — where each rendered value came from.

A value the renderer wrote from its own text is non-empty, exactly like one the design stated, so
presence alone cannot tell a design that determines its artifacts from a renderer that invented
them. Provenance can, and only the renderer knows it: it is the thing that put the value there.
This reports one origin per leaf from what the renderer recorded, and the completeness measure
reads it.

The attribution itself is `transformation.build.provenance.attribute`, the one place a leaf's
origin is derived; this transform is its governed step.

CONSTITUTIONAL: Pure — no I/O, no clock, no filesystem.
"""

from __future__ import annotations

from typing import Any

from transformation.build.provenance import attribute


def execute(inputs: dict, **_: Any) -> dict:
    return attribute(inputs["rendered"], inputs["sources"] or {})
