"""The generators construction may invoke, and how it asks whether one already agrees.

A design names the generator an artifact is reached by. Construction reaches it by *invoking* that
generator and never by writing the artifact itself — refusing outright would leave the delivery of
every generated artifact ungoverned, and rendering it directly would make construction a second
producer of the same truth. Two producers drift, and the drift is silent until something reads the
stale one.

**The registry is closed**, exactly as the check-kind registry is. A design naming a generator
nothing here declares is fail-hard, never a silently skipped artifact: resolving an arbitrary dotted
path at runtime would let a design point construction at any callable in the interpreter, and an
artifact reached by something nobody admitted is an artifact nobody governs. Adding a generator is a
change to this file, which is where it can be reviewed.

Each entry answers two questions, and they are different questions. `invoke` reaches the artifact.
`stale` reports whether the artifact already agrees with what produces it — asked without changing
the answer, which is what makes it usable as a build gate rather than as a habit.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import yaml

from transformation.build.render import (
    MACHINE_BLOCK,
    build_manifest,
    manifest_path,
    render_document,
)
from transformation.design import emit as phase_emit

# How a design names the manifest generator, and how construction reaches it. One spelling,
# read by the provenance a design states and by the founding emission below.
MANIFEST_GENERATOR = "transformation.build.render:build_manifest"



@dataclass(frozen=True)
class Context:
    """What a generator is handed.

    A generator reads either its own sources or the design that named it, and the two need different
    things. The phase workflows are determined by a template and a rule module and know nothing about
    any dossier; a domain's build manifest is determined by the mandate in front of it. One context
    carrying both keeps the registry uniform rather than making the caller know which kind it holds.
    """

    p7: dict
    p8: dict
    # Absent when the caller is only measuring a design. A generator that writes into a domain says
    # so with `needs_root`, and is asked nothing it cannot answer.
    domain_root: Path | None = None
    # The composition a generator observes. The phase workflows' observing steps answer what the
    # snapshot capability declares, which only a composition can say.
    snapshot_root: Path | None = None


@dataclass(frozen=True)
class Generator:
    """One admitted generator: what it produces its artifacts with, and how it is questioned."""

    name: str
    invoke: Callable[[Context], list[Path]]
    stale: Callable[[Context], list[str]]
    summary: str
    # Each artifact as the generator would write it, by code, without writing. Construction compares
    # a generated amendment with the composition before anything is written, as it does a rendered
    # one: an amendment that changes meaning is refused whoever produces it.
    preview: Callable[[Context], dict[str, dict]] = lambda ctx: {}
    # Whether the generator can answer at all without a domain to write into. Declared rather than
    # discovered, so a caller that cannot supply one reports that the question went unasked instead
    # of reading an empty answer as agreement.
    needs_root: bool = False
    # Whether it observes a composition, and so cannot answer without `snapshot_root`. Declared for
    # the same reason as `needs_root`.
    needs_snapshot: bool = False
    # Whether the generator reads the design in front of it, or its own sources.
    #
    # The distinction decides what a disagreement *means*, and getting it wrong makes the agreement
    # gate refuse the very changes it exists to permit. The phase workflows are derived from a
    # template and a rule module: a disagreement is a stale copy, now, and the build must refuse it.
    # A domain's build manifest is derived from the mandate: before that mandate is built, the
    # artifact necessarily differs from what the design determines, and that difference *is* the
    # change. Refusing it would refuse every design that touches a generated artifact.
    #
    # So a design-derived generator is reported as pending here and enforced at emission, where
    # `construction emit` refuses anything still disagreeing after the generator has run.
    derived_from_design: bool = False


# The phase workflows -----------------------------------------------------------------------------


def _phase_workflows_invoke(ctx: Context) -> list[Path]:
    return [phase_emit.WORKFLOWS / e.filename for e in phase_emit.emit_rule_sets(ctx.snapshot_root)]


def _phase_workflows_stale(ctx: Context) -> list[str]:
    return [e.filename for e in phase_emit.check(ctx.snapshot_root)]


def _phase_workflows_preview(ctx: Context) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for code, text in phase_emit.preview(ctx.snapshot_root).items():
        found = MACHINE_BLOCK.search(text)
        out[code] = (yaml.safe_load(found.group(1)) or {}) if found else {}
    return out


# The domain build manifest -----------------------------------------------------------------------
#
# Every field of it is compiler configuration — which layers to search, how a namespace is matched,
# where projections are written — and `render.build_manifest` already derives the whole thing from
# three facts the mandate declares. It was nonetheless inventoried as an artifact a design amends,
# which obliged a change adding a subdomain to restate fifty-one derived facts it does not decide,
# and produced one it could not: a `core.subdomain` the artifact does not carry.
#
# So it is generated, and the design says so. What actually varies with a subdomain is one prose
# sentence in the summary; nothing in the compiler's read path varies at all.


def _manifest(ctx: Context) -> tuple[dict | None, Path | None]:
    if ctx.domain_root is None:
        return build_manifest(ctx.p7, ctx.p8), None
    # The subdomains the domain already holds are its registry's folders beside `structures`, where
    # the manifest itself lives.
    registry = ctx.domain_root / "registry"
    held = tuple(d.name for d in registry.iterdir()
                 if d.is_dir() and d.name != "structures") if registry.is_dir() else ()
    manifest = build_manifest(ctx.p7, ctx.p8, held)
    if manifest is None:
        return manifest, None
    return manifest, ctx.domain_root / manifest_path(manifest)


def _build_manifest_invoke(ctx: Context) -> list[Path]:
    manifest, path = _manifest(ctx)
    if manifest is None or path is None:
        return []
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_document({"machine": manifest}), encoding="utf-8")
    return [path]


def _build_manifest_preview(ctx: Context) -> dict[str, dict]:
    manifest, _ = _manifest(ctx)
    return {} if manifest is None else {manifest["fqdn"].split("::")[-1]: manifest}


def _build_manifest_stale(ctx: Context) -> list[str]:
    """Whether the manifest on disk is what the mandate determines.

    Compared as the Machine block rather than as text: the document carries a header and an intent
    line a human reads, and acceptance for a rendered artifact has always been semantic equality of
    the block the compiler reads. A file that differs only in its prose is not stale.
    """
    manifest, path = _manifest(ctx)
    if manifest is None or path is None:
        return []
    if not path.is_file():
        return [path.name]
    found = MACHINE_BLOCK.search(path.read_text(encoding="utf-8"))
    built = yaml.safe_load(found.group(1)) if found else None
    return [] if built == manifest else [path.name]


GENERATORS: dict[str, Generator] = {
    phase_emit.GENERATOR: Generator(
        name=phase_emit.GENERATOR,
        invoke=_phase_workflows_invoke,
        stale=_phase_workflows_stale,
        preview=_phase_workflows_preview,
        summary="the phase workflows and the rule set each of them seals",
        needs_snapshot=True,
    ),
    MANIFEST_GENERATOR: Generator(
        name=MANIFEST_GENERATOR,
        invoke=_build_manifest_invoke,
        stale=_build_manifest_stale,
        preview=_build_manifest_preview,
        summary="the domain build manifest, derived from the domain, its subdomains and its families",
        needs_root=True,
        derived_from_design=True,
    ),
}


class UnknownGenerator(KeyError):
    """A design named a generator construction is not permitted to invoke."""


def resolve(name: str) -> Generator:
    """The admitted generator by the name a design gave it, or fail hard."""
    if name not in GENERATORS:
        raise UnknownGenerator(
            f"unknown generator {name!r}; construction may invoke {sorted(GENERATORS)}"
        )
    return GENERATORS[name]
