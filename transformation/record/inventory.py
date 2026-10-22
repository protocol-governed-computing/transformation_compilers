"""The artifacts a registry holds, read for the baseline generators.

A baseline design is read from a registry and states it whole, so this reads every artifact under the
root except the two kinds no design states: a build manifest, which is compiler configuration, and a
test vector, which a design states as its transform's cases rather than as an artifact of its own.
Reads the registry; decides nothing.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import yaml

from transformation.design.families import FAMILIES
from transformation.machine_block import MACHINE_BLOCK

FAMILY = {f.artifact_kind: f.code for f in FAMILIES}
BUILD_MANIFEST = re.compile(r"^STRUCTURE_BUILD_[A-Z0-9_]+_CONFIG_V\d+$")


def _machine(path: Path) -> dict | None:
    found = MACHINE_BLOCK.search(path.read_text(encoding="utf-8"))
    if not found:
        return None
    machine = yaml.safe_load(found.group(1))
    return machine if isinstance(machine, dict) and "fqdn" in machine else None


def artifacts(registry: Path) -> list[dict]:
    """Every artifact a design states, each as `{path, machine, code, fqdn, family, subdomain}`.

    The subdomain is the artifact's declared `concern`, which construction writes from the design's
    subdomain field: a declared carrier, never the folder it sits in.
    """
    out = []
    for path in sorted(registry.rglob("*.md")):
        machine = _machine(path)
        if machine is None:
            continue
        code = machine["fqdn"].split("::")[1]
        kind = machine.get("artifact_kind")
        if kind == "TEST_DATA" or BUILD_MANIFEST.match(code) or kind not in FAMILY:
            continue
        out.append({"path": path, "machine": machine, "code": code, "fqdn": machine["fqdn"],
                    "family": FAMILY[kind], "subdomain": machine.get("concern") or ""})
    return out


def vectors(registry: Path) -> list[dict]:
    """Every test vector the registry holds, as its Machine block."""
    out = []
    for path in sorted(registry.rglob("TEST_DATA_*.md")):
        machine = _machine(path)
        if machine is not None:
            out.append(machine)
    return out


def domain(held: list[dict]) -> str:
    """The namespace the registry's artifacts are declared in."""
    counts = Counter(a["fqdn"].split("::")[0] for a in held)
    if len(counts) != 1:
        raise ValueError(f"a registry states one domain; this one declares {sorted(counts)}")
    return next(iter(counts))
