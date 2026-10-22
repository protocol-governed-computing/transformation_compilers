"""Construction acceptance — render each root's design of record and compare it with its registry.

Every designed root carries one P7 and one P8 of record in `<root>/design/`, written from its
registry by `python -m transformation.record`. Construction of that pair is compared with the
registry, artifact by artifact, and the question is whether **the design states every fact of the
registry**. A design generated from a registry and rendered back is a round trip: it proves that the
design language can state the registry whole, not how the registry came to be.

Every difference is one of exactly two things, and the difference itself says which:

    a generator bug          the design states the fact and the renderer got it wrong
    a design insufficiency   the design does not state the fact at all

Comparison is semantic and scoped to the Machine block. An artifact's prose is human narrative that
no register determines, and comparing text would report differences about paragraphs nobody claims
are generated.

Two kinds of root carry no design of record, and neither is compared. The platform's governance
surface is constitutions, invariants and surface contracts, kinds the design language cannot state.
The inspection surface's transport contracts are generated from their declaration by
`author_transport_contracts.py`, whose `--check` compares them.

Run:  python scripts/testbed/construction_acceptance.py
Exit: 0 when every artifact matches, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from transformation.machine_block import MACHINE_BLOCK as MACHINE
from transformation.build.render import bare, generated, implementation_namespace, render_all
from transformation.design.read import read_seed

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent

# Every root with a design of record, as (root, registry). The design is `<root>/design/`.
DOMAINS = tuple((root, root / "registry") for root in (
    WORKSPACE / "business_domains/ai_governance",
    WORKSPACE / "business_domains/blockchain",
    WORKSPACE / "business_domains/book_library_mgmt",
    WORKSPACE / "business_domains/causal_language_model",
    WORKSPACE / "conformance_workloads/workloads/collatz",
    REPO,
))

# A build manifest is determined by no design. Every field of it is configuration the compiler
# discovers a domain by, and no register of any phase states one.
BUILD_MANIFEST = re.compile(r"^STRUCTURE_BUILD_[A-Z0-9_]+_CONFIG_V\d+$")


def registers(path: Path) -> dict[str, list[dict]]:
    doc = read_seed(path)
    out: dict[str, list[dict]] = {}
    for entry in doc.registers:
        block = doc.register(entry["id"])
        if block and block.table:
            out[entry["id"]] = block.table.rows
    return out


def built(registry: Path) -> dict[str, dict]:
    out = {}
    for path in sorted(registry.rglob("*.md")):
        found = MACHINE.search(path.read_text(encoding="utf-8"))
        if not found:
            continue
        machine = yaml.safe_load(found.group(1))
        if isinstance(machine, dict) and "fqdn" in machine:
            out[bare(machine["fqdn"])] = machine
    return out


# Keys that are documentation even inside the Machine block. Two tests decide membership, and both
# are empirical rather than aesthetic:
#
#   nothing consumes it   `isolation`, `resolution`, `storage_roots` and `extensions` appear in no
#                         compiler, assembler or runtime read path. `isolation.rules` restates in
#                         prose what `entity_stores` already says structurally.
#   it varies by author   a field `description` is present on some fields and not others; a
#                         governed fact is present or absent by rule.
#
# A key that something reads is governed however prose-like it looks — `parameters` on a runtime
# binding is a list of names an assertion checks, so it stays in.
DOCUMENTATION = {"description", "isolation", "resolution", "storage_roots", "extensions"}


def diff(expected, actual, path: str = "") -> list[str]:
    """Every leaf where two Machine blocks disagree, addressed by dotted path."""
    if isinstance(expected, dict) and isinstance(actual, dict):
        out = []
        for key in sorted(set(expected) | set(actual)):
            if key in DOCUMENTATION:
                continue
            here = f"{path}.{key}" if path else key
            if key not in actual:
                out.append(f"{here}: not rendered")
            elif key not in expected:
                out.append(f"{here}: rendered but not built")
            else:
                out += diff(expected[key], actual[key], here)
        return out
    if isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            return [f"{path}: {len(actual)} rendered, {len(expected)} built"]
        out = []
        for i, (e, a) in enumerate(zip(expected, actual)):
            out += diff(e, a, f"{path}[{i}]")
        return out
    if expected != actual:
        return [f"{path}: rendered {actual!r}, built {expected!r}"]
    return []


def namespace(reference: dict[str, dict]) -> str | None:
    """The implementation namespace the root's build manifest declares."""
    for code, machine in reference.items():
        if BUILD_MANIFEST.match(code):
            return implementation_namespace(machine)
    return None


def acceptance(root: Path, registry: Path) -> tuple[int, int, int]:
    """Render one root's design of record and compare it with its registry.

    Returns (compared, failures, field differences).
    """
    design = root / "design"
    p7_path, p8_path = next(design.glob("p7_*.md"), None), next(design.glob("p8_*.md"), None)
    print(f"construction acceptance — {root.relative_to(WORKSPACE)}")
    if p7_path is None or p8_path is None:
        print(f"  MISS  {design.relative_to(WORKSPACE)} holds no design of record\n")
        return 0, 1, 0
    p7, p8 = registers(p7_path), registers(p8_path)
    reference = built(registry)
    rendered = {bare(a["machine"]["fqdn"]): a for a in render_all(p7, p8, namespace(reference))}
    # An artifact the design says its generator produces is not construction's to write, and the
    # generator's own check compares it.
    reached = set(generated(p7))
    print(f"{len(rendered)} rendered, {len(reached)} reached by a generator, against "
          f"{len(reference)} built\n")

    failures = total_diffs = undetermined = 0
    for code in sorted(reference):
        if BUILD_MANIFEST.match(code):
            undetermined += 1
            continue
        if code in reached:
            print(f"  GEN   {code}")
            continue
        if code not in rendered:
            print(f"  MISS  {code:<44} rendered nothing")
            failures += 1
            continue
        differences = diff(reference[code], rendered[code]["machine"])
        total_diffs += len(differences)
        if not differences:
            print(f"  OK    {code}")
            continue
        failures += 1
        print(f"  DIFF  {code:<44} {len(differences)} field(s)")
        for line in differences[:6]:
            print(f"          {line}")
        if len(differences) > 6:
            print(f"          … {len(differences) - 6} more")

    for code in sorted(set(rendered) - set(reference)):
        print(f"  EXTRA {code:<44} rendered, never built")
        failures += 1

    compared = len(reference) - undetermined
    print(f"\n  {compared - failures}/{compared} artifacts reproduced"
          f"   ({total_diffs} field difference(s))\n")
    return compared, failures, total_diffs


def uncovered() -> list[Path]:
    """Designs of record that `DOMAINS` does not read."""
    covered = {(root / "design").resolve() for root, _ in DOMAINS}
    return [p.parent for p in sorted(WORKSPACE.glob("**/design/p7_*_baseline.md"))
            if p.parent.resolve() not in covered and ".venv" not in p.parts]


def main() -> int:
    compared = failures = diffs = 0
    for root, registry in DOMAINS:
        c, f, d = acceptance(root, registry)
        compared += c; failures += f; diffs += d

    print(f"  {compared - failures}/{compared} artifacts reproduced across {len(DOMAINS)} domain(s)"
          f"   ({diffs} field difference(s))")

    missing = uncovered()
    for root in missing:
        print(f"  UNCOVERED  {root.relative_to(WORKSPACE)} is a design of record compared against "
              f"nothing")
    return 1 if failures or missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
