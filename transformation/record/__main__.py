"""Write a registry's baseline design. See `transformation.record`."""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from transformation.record import design, inventory, mandate


class Plain(yaml.SafeDumper):
    """Writes every row out in full: a reader of the design never resolves an anchor."""

    def ignore_aliases(self, data):
        return True


def _document(title: str, header: dict, registers: dict, prose: str) -> str:
    block = yaml.dump({"document": header, "registers": registers}, Dumper=Plain, sort_keys=False,
                      allow_unicode=True, width=100)
    return f"# {title}\n\n## Machine\n\n```yaml\n{block}```\n{prose}"


def main() -> None:
    parser = argparse.ArgumentParser(prog="python -m transformation.record")
    parser.add_argument("registry", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("--generated", nargs="+", default=[], metavar="ITEM",
                        help="a generator, then the codes it produces")
    args = parser.parse_args()

    held = inventory.artifacts(args.registry)
    domain = inventory.domain(held)
    subdomains = sorted({a["subdomain"] for a in held})
    generated = []
    if args.generated:
        generator, *codes = args.generated
        generated = [{"artifact": f"{domain}::{c}", "generator": generator,
                      "generator_sources": [str(args.registry.relative_to(args.registry.parent))]}
                     for c in codes]

    p7 = design.p7(held, inventory.vectors(args.registry), generated)
    p8 = mandate.p8(held, p7)
    header = {"domain": domain, "subdomain": subdomains, "cr": "baseline"}
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / f"p7_design_intent_{domain}_baseline.md").write_text(_document(
        f"Design Intent — {domain}, baseline",
        {"phase": "p7", **header, "rule_set": "transformation.schemas.REGISTER_SCHEMA_P7_V0"}, p7,
        PROSE_P7.format(domain=domain)), encoding="utf-8")
    (args.out / f"p8_authoring_mandate_{domain}_baseline.md").write_text(_document(
        f"Authoring Mandate — {domain}, baseline",
        {"phase": "p8", **header, "rule_set": "transformation.schemas.REGISTER_SCHEMA_P8_V0"}, p8,
        PROSE_P8.format(domain=domain, count=len(held))), encoding="utf-8")
    print(f"{domain}: {len(held)} artifacts → {args.out}")


PROSE_P7 = """
The design of record of `{domain}`: every artifact its registry holds, stated in the design language.
Written by `python -m transformation.record` from the registry. Construction of this design and its
mandate reproduces the registry, and `construction_acceptance` asks whether it does. A change to
`{domain}` is a dossier designed against the composition.
"""

PROSE_P8 = """
The {count} artifacts of `{domain}`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
"""

if __name__ == "__main__":
    main()
