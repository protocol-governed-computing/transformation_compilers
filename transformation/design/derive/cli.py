"""`tc phase derive`: check a ledger, derive a design from it, splice the design into a dossier."""
from __future__ import annotations

import json
from pathlib import Path

import click
import yaml

from transformation.design.derive import seal
from transformation.design.derive.compose import derive as derive_design
from transformation.design.derive.ledger import CATALOG, Refused, answered, refusals, selftest
from transformation.design.derive import identity
from transformation.design.derive.base import load_p7
from transformation.design.derive.splice import short, splice


@click.group()
def derive() -> None:
    """Derive a design from a decision ledger — the Design Compiler's route for answered decisions."""


@derive.command("check")
@click.argument("ledgers", nargs=-1, required=True, type=click.Path(exists=True, dir_okay=False, path_type=Path))
def derive_check(ledgers: tuple[Path, ...]) -> None:
    """Admit or refuse each ledger, and name the catalog questions it answers. Exit 1 on a refusal."""
    refused = False
    for path in ledgers:
        ledger = yaml.safe_load(path.read_text(encoding="utf-8"))
        errs = refusals(ledger)
        click.echo(f"== {ledger.get('domain', path)}: {'refused' if errs else 'admitted'}")
        for e in errs:
            click.echo(f"  {e}")
        if not errs:
            qs = answered(ledger)
            click.echo(f"  answers {len(qs)} of {len(CATALOG['questions'])} catalog questions: "
                       f"{', '.join(sorted(qs))}")
        refused |= bool(errs)
    raise SystemExit(1 if refused else 0)


@derive.command("selftest")
@click.argument("book", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument("ai_governance", type=click.Path(exists=True, dir_okay=False, path_type=Path))
def derive_selftest(book: Path, ai_governance: Path) -> None:
    """Show that answers outside their shapes are refused, by editing two admitted ledgers."""
    results = selftest(book, ai_governance)
    for name, errs in results:
        click.echo(f"  {'OK  ' if errs else 'FAIL'}  refused: {name}" + (f"  ({errs[0][:90]})" if errs else ""))
    held = sum(1 for _, errs in results if errs)
    click.echo(f"\n  {held}/{len(results)} answers outside their shapes refused")
    raise SystemExit(0 if held == len(results) else 1)


@derive.command("design")
@click.argument("ledger", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument("baseline", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--out", type=click.Path(dir_okay=False, path_type=Path), required=True,
              help="Where the derived rows are written, as JSON.")
def derive_derive(ledger: Path, baseline: Path, out: Path) -> None:
    """Derive a domain's P7 rows from its ledger, against its design of record."""
    try:
        reg = derive_design(ledger, baseline)
    except (Refused, seal.Unsealed, ValueError) as exc:
        raise click.ClickException(str(exc))
    out.write_text(json.dumps(reg, indent=1) + "\n", encoding="utf-8")
    judged = reg["_judged_by"]
    click.echo(f"  derived {len(reg['new_artifacts'])} artifact(s); judged by "
               + ", ".join(f"{j['id']} revision {j['revision']}" for j in judged.values()))
    for line in reg["_unrealized"]:
        click.echo(f"  unrealized: {line}")


@derive.command("splice")
@click.argument("design", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.argument("generated", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument("out", type=click.Path(file_okay=False, path_type=Path))
def derive_splice(design: Path, generated: Path, out: Path) -> None:
    """Write a design's P7 and P8 into a dossier, with the derived rows in place of the domain's."""
    for line in splice(design, json.loads(generated.read_text(encoding="utf-8")), out):
        click.echo(f"  {line}")


@derive.command("identities")
@click.argument("dossier", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.argument("generated", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--snapshot", "snapshot_root", required=True,
              type=click.Path(exists=True, file_okay=False, path_type=Path),
              help="The composition the design is pinned to; what it holds is what is compared.")
@click.option("--root", "domain_root", required=True,
              type=click.Path(exists=True, file_okay=False, path_type=Path), help="The domain.")
@click.option("--release", type=click.Path(file_okay=False, path_type=Path), default=None,
              help="The published composition, whose identities are never used again.")
@click.option("--retired", type=click.Path(dir_okay=False, path_type=Path), default=None,
              help="The retirement ledger, whose identities are never used again.")
def derive_identities(dossier: Path, generated: Path, snapshot_root: Path, domain_root: Path,
                        release: Path | None, retired: Path | None) -> None:
    """Decide each derived artifact's identity by meaning, and name successors in the derived rows."""
    reg = json.loads(generated.read_text(encoding="utf-8"))
    design = reg_codes(domain_root)
    decided = identity.decide(dossier, snapshot_root, domain_root, design, release, retired,
                              reg.get("_replaces"))
    reg = identity.renumber(reg, decided["superseded"])
    reg["_identity"] = decided
    generated.write_text(json.dumps(reg, indent=1) + "\n", encoding="utf-8")
    click.echo(f"  kept {len(decided['kept'])}, superseded {len(decided['superseded'])}, "
               f"new {len(decided['new'])}, replaced {len(decided['replaced'])}, "
               f"retired {len(decided['retired'])}")
    for old, new in decided["replaced"].items():
        click.echo(f"    {short(old)} replaced by {short(new)}")
    for old, new in decided["superseded"].items():
        click.echo(f"    {short(old)} -> {short(new)}  ({decided['changed_at'][old]} place(s))")
    for code in decided["retired"]:
        click.echo(f"    retired {short(code)}")


def reg_codes(domain_root: Path) -> list[str]:
    """The artifacts the domain's design of record names."""
    p7 = next((domain_root / "design").glob("p7_*.md"))
    return [r["code"] for r in load_p7(p7)["new_artifacts"]]


@derive.command("meta")
@click.option("--snapshot", "snapshot_root", required=True,
              type=click.Path(exists=True, file_okay=False, path_type=Path),
              help="The composition whose invariants the doctrine cites.")
def derive_meta(snapshot_root: Path) -> None:
    """Check the sealed documents: each is its last revision, and every doctrine citation resolves."""
    problems = [why for name in seal.SEALED if (why := seal.unrecorded(name))]
    problems += seal.doctrine_closure(snapshot_root)
    rules = seal.load("doctrine")["rules"]
    unstated = sorted(n for n, r in rules.items() if r.get("realizes") == "none")
    for line in problems:
        click.echo(f"  FAIL  {line}")
    click.echo(f"  doctrine: {len(rules) - len(unstated)}/{len(rules)} rules cite an invariant"
               + (f"; realizing none: {', '.join(unstated)}" if unstated else ""))
    if problems:
        raise SystemExit(1)
    click.echo("  DERIVE META PASSED")


@derive.command("revise")
@click.argument("document", type=click.Choice(sorted(seal.SEALED)))
@click.option("--change", required=True, help="What the change is, in one sentence.")
def derive_revise(document: str, change: str) -> None:
    """Record a revision of the doctrine, the ledger schema or the catalog."""
    try:
        r = seal.revise(document, change)
    except seal.Unsealed as exc:
        raise click.ClickException(str(exc))
    click.echo(f"  {seal.load(document)['$id']} revision {r['revision']}  {r['digest']}")
