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
@click.option("--retired", type=click.Path(exists=True, dir_okay=False, path_type=Path), default=None,
              help="The retirement ledger: the replacements already made, which a spent `replaces` names.")
def derive_derive(ledger: Path, baseline: Path, out: Path, retired: Path | None) -> None:
    """Derive a domain's P7 rows from its ledger, against its design of record."""
    try:
        reg = derive_design(ledger, baseline, retired)
    except (Refused, seal.Unsealed, ValueError) as exc:  # Untraced is a ValueError
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
    # A successor names one predecessor: the version it supersedes now, not the one its predecessor did.
    successors = set(decided["superseded"].values())
    reg["artifact_properties"] = [r for r in reg.get("artifact_properties") or []
                                  if not (r.get("property") == "supersedes" and r["artifact"] in successors
                                          and r.get("_from") == "carried:surface")]
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
    problems += [why for why in [seal.route_unsealed()] if why] + seal.unsealed_dossiers()
    problems += seal.doctrine_closure(snapshot_root)
    rules = seal.load("doctrine")["rules"]
    unstated = sorted(n for n, r in rules.items() if r.get("realizes") == "none")
    for line in problems:
        click.echo(f"  FAIL  {line}")
    click.echo(f"  doctrine: {len(rules) - len(unstated)}/{len(rules)} rules cite an invariant"
               + (f"; realizing none: {', '.join(unstated)}" if unstated else ""))
    if problems:
        raise SystemExit(1)
    click.echo(f"  route: sealed by dossiers/{seal.route_in_force()['revision']} "
               f"({len(seal.seals())} seal(s))")
    click.echo("  DERIVE META PASSED")


@derive.command("seal")
@click.argument("dossier", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option("--snapshot", "snapshot_root", required=True,
              type=click.Path(exists=True, file_okay=False, path_type=Path),
              help="The composition each ledger is re-derived against.")
@click.option("--change", required=True, help="What the route change is, in one sentence.")
def derive_seal(dossier: Path, snapshot_root: Path, change: str) -> None:
    """Seal a route change: re-derive every ledger under the route as it stands, and record both."""
    dossier = dossier.resolve()
    if dossier.parent != seal.DOSSIERS.resolve():
        raise click.ClickException(f"a route change runs as its own dossier, under {seal.DOSSIERS}")
    if not (dossier / seal.CHANGE_FILE).is_file():
        raise click.ClickException(f"{dossier.name} has no {seal.CHANGE_FILE}: the dossier says what changed")
    for name in seal.SEALED:
        if why := seal.unrecorded(name):
            raise click.ClickException(why)
    seal.SEALING = True
    rederived = {}
    for ledger in sorted((seal.DOSSIERS.parent / "testbed" / "ledgers").glob("*/ledger.yaml")):
        name = ledger.parent.name
        summary = rederive(ledger, seal.DOSSIERS.parents[1] / "business_domains" / name, snapshot_root)
        rederived[name] = summary
        click.echo(f"  {name}: {summary['identities']}  — design of record {summary['design_of_record']}")
    entry = seal.record_seal(dossier.name, change, rederived)
    click.echo(f"  sealed by dossiers/{entry['dossier']}: {len(entry['route'])} file(s)")


def rederive(ledger: Path, domain_root: Path, snapshot_root: Path) -> dict:
    """What one ledger derives against its domain's design of record, by identity."""
    import tempfile
    workspace = seal.DOSSIERS.parents[1]
    retired = workspace / ".github" / "process" / "retired_identities.yaml"
    reg = derive_design(ledger, next((domain_root / "design").glob("p7_*.md")),
                        retired if retired.is_file() else None)
    with tempfile.TemporaryDirectory() as tmp:
        splice(domain_root / "design", reg, Path(tmp))
        d = identity.decide(Path(tmp), snapshot_root, domain_root, reg_codes(domain_root),
                            workspace / "pgc_release" / "snapshot",
                            retired, reg.get("_replaces"))
    moved = len(d["superseded"]) + len(d["new"]) + len(d["replaced"]) + len(d["retired"])
    return {"identities": f"kept {len(d['kept'])}, superseded {len(d['superseded'])}, new {len(d['new'])}, "
                          f"replaced {len(d['replaced'])}, retired {len(d['retired'])}",
            "design_of_record": "unchanged" if not moved else "changes: deliver it as a change request"}


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


@derive.command("project")
@click.argument("ledger", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument("baseline", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--out", "out_dir", type=click.Path(file_okay=False, path_type=Path), required=True,
              help="The directory the phase documents are written to.")
@click.option("--design", "design_path", type=click.Path(exists=True, dir_okay=False, path_type=Path),
              help="The derived design, with its identities decided (`tc phase derive identities`). "
                   "With --snapshot, P2 to P4 are projected from what it observed.")
@click.option("--snapshot", "snapshot_root", type=click.Path(exists=True, file_okay=False, path_type=Path),
              help="The composition the identities were decided against.")
@click.option("--cr", "cr_name", help="The change request the documents belong to, as `cr_NN_<subject>`. "
                                       "Without it, they are named for the ledger.")
def derive_project(ledger: Path, baseline: Path, out_dir: Path, design_path: Path | None,
                   snapshot_root: Path | None, cr_name: str | None) -> None:
    """Project the phase documents P0 to P6 from a ledger.

    P0 restates the ledger, P1 is P0's own projection, P5 cites P0 and P6 cites P5. Given the derived
    design and its snapshot, P2 to P4 restate what the derivation observed, each citing the phase
    before it. Judge each with `tc phase check`, by the rule set that governs an authored one.
    Exit 1 on a refused ledger.
    """
    from transformation.design.derive.project import project
    from transformation.design.project import project_p1
    from transformation.design.read import read_seed

    data = yaml.safe_load(ledger.read_text(encoding="utf-8"))
    errs = refusals(data)
    if errs:
        for e in errs:
            click.echo(f"  {e}")
        raise SystemExit(1)
    if (design_path is None) != (snapshot_root is None):
        raise click.ClickException("--design and --snapshot are given together")
    derived = json.loads(design_path.read_text(encoding="utf-8")) if design_path else None
    if derived is not None and "_identity" not in derived:
        raise click.ClickException(f"{design_path} has no identities decided — run `tc phase derive identities` first")
    docs = project(data, load_p7(baseline), derived, snapshot_root, cr_name)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{data['domain']}_{cr_name or 'ledger'}"
    names = {"p0": f"p0_seed_{stem}.md", "p1": f"p1_change_request_{stem}.md", "p2": f"p2_domain_model_{stem}.md",
             "p3": f"p3_analysis_loop_{stem}.md", "p4": f"p4_business_model_{stem}.md",
             "p5": f"p5_business_intent_{stem}.md", "p6": f"p6_governance_intent_{stem}.md"}
    (out_dir / names["p0"]).write_text(docs["p0"], encoding="utf-8")
    docs["p1"] = project_p1(read_seed(out_dir / names["p0"]))
    for phase in sorted(docs):
        (out_dir / names[phase]).write_text(docs[phase], encoding="utf-8")
    for phase in sorted(docs):
        click.echo(f"  projected {phase}  ->  {out_dir / names[phase]}")
