"""Construction — render protocol artifacts from a design and a mandate.

The Construction lifecycle sits between Transformation and Compilation. P0–P8 judge documents and
emit verdicts; construction consumes `DesignIntent(P7) + AuthoringMandate(P8)` and emits artifacts.
It is the first governed step that *creates* rather than judges, which is why it is a lifecycle
stage and not a tenth phase — numbering it would blur a construction failure ("the mandate was valid
but did not uniquely determine an artifact") back into a P8 failure ("the mandate is incomplete").

**What is rendered is the Machine block.** An artifact's prose is human narrative — intent,
rationale, the reasoning a reviewer needs — and no register determines it or should. The Machine
block is what the compiler reads, what the snapshot seals and what the runtime executes, so it is
what a design has to determine. Acceptance is semantic equality of that block, never text equality
of the file.

Nothing here decides anything. Every value is read from a register or from a constitution-fixed
default, and a fact the design does not state is a fact this module must not invent — an inventing
generator is a second, ungoverned design authority. Where a value cannot be derived, the renderer
omits it and the acceptance harness reports it as undetermined.

**Some artifacts are not written here at all.** An artifact the design declares in
`generation_provenance` is reached by invoking its generator, and this module renders none of it:
rendering it would make construction a second producer of an artifact something else already
produces, and two producers of one truth drift silently until something reads the stale one. The
artifact is still scheduled and still measured — what the design owes for it is the generator.
"""

from __future__ import annotations

import re
from typing import Any

from transformation.build.provenance import (
    CARRIED_FROM_PREDECESSOR, GOVERNED_ELSEWHERE, STATED_BY_DESIGN, SUPPLIED_BY_RENDERER, leaves,
)
from transformation.design.families import BY_CODE, FAMILIES
from transformation.design.schema import column_key

# Where a `Machine` block begins and ends. One spelling, because there were three and two of them
# disagreed: a pattern missing the trailing newline captures a block ending one character later, and
# on a block whose last line is not newline-terminated the two read different content while both
# parsing as valid YAML. This module renders machine blocks, so it owns the definition of one.
MACHINE_BLOCK = re.compile(r"```yaml\n(.*?)\n```", re.S)


def machine_block(text: str) -> str | None:
    """The YAML source of a document's `Machine` block, or None where there is none."""
    found = MACHINE_BLOCK.search(text)
    return found.group(1) if found else None


# Constitution, compiled kind and registry directory per family — all three derived from the one
# declaration in `design.families`, because they were three hand-kept copies of it and the copies
# had already drifted. A design that restated them would be declaring something it does not own.
GOVERNED_BY = {f.code: f.constitution for f in FAMILIES}
KIND = {f.code: f.artifact_kind for f in FAMILIES}
DIRECTORY = {f.code: f.directory for f in FAMILIES}

# An intent's outcome surface is fixed by the intent constitution — every intent in the composition
# carries the same two. Requiring a design to restate them would be ceremony, not determinacy.
INTENT_OUTCOMES = {
    "ACK": {"description": "Request accepted for processing"},
    "NACK": {"description": "Request rejected"},
}

WORKFLOW_STRUCTURE = "execution::STRUCTURE_RUNTIME_EXECUTION_V0"

# The boundary's own substitution syntax, matched here so the renderer can tell a token it must
# preserve verbatim from a constant it should read as a value. Kept identical to the resolver's.


def norm(value: Any) -> str:
    return " ".join(str(value or "").split())


def value(row: dict, column: str) -> Any:
    """A cell as the row holds it, addressed by its column's title through the schema's key."""
    return row.get(column_key(column))


def cell(row: dict, column: str) -> str:
    """A text cell, whitespace-normalised. A cell stating nothing, or absent, reads as empty."""
    held = value(row, column)
    if isinstance(held, (list, dict)):
        raise TypeError(f"column {column!r} holds structure; read it with value() or items()")
    if isinstance(held, bool):
        return "true" if held else "false"
    return norm(held)


def items(row: dict, column: str) -> list[str]:
    """A cell as the names it states: a list's entries, a text's one value, or none."""
    held = value(row, column)
    if held is None or isinstance(held, dict):
        return []
    if isinstance(held, list):
        return [norm(v) for v in held if norm(v)]
    return [norm(held)] if norm(held) else []


def bare(value: str) -> str:
    return norm(value).split("::")[-1]


def rows(registers: dict, name: str) -> list[dict]:
    """A register's rows. One declared empty, or stating nothing, has none."""
    held = registers.get(name)
    return [r for r in held if isinstance(r, dict)] if isinstance(held, list) else []


def typed_fields(design: dict, code: str, direction: str) -> dict:
    """The typed fields an artifact declares in one direction, from `interface_fields`."""
    out: dict[str, Any] = {}
    for row in rows(design, "interface_fields"):
        if bare(cell(row, "Artifact")) != bare(code) or cell(row, "Direction") != direction:
            continue
        # A format is its own column. Without it an amended contract could not keep a format it
        # already had.
        spec: dict[str, Any] = {"type": cell(row, "Type") or "string"}
        if cell(row, "Format"):
            spec["format"] = cell(row, "Format")
        if cell(row, "Required") == "YES":
            spec["required"] = True
        # A default is the value the design states, of whatever type it is. One that states nothing,
        # or the empty text, declares no default.
        default = value(row, "Default")
        if default is not None and default != "":
            spec["default"] = default
        # `Meaning` is documentation. The built corpus carries a description on some fields and not
        # others, which is a sign it is prose rather than governed content — rendering it would make
        # the generator author documentation the design never committed to.
        out[cell(row, "Field")] = spec
    return out


# The origins a rendered fact may have, governed by `transformation::VOCAB_FACT_PROVENANCE_V0` and
# spelled once in `transformation.build.provenance`. The renderer records them as it renders.
#
# The measure admits the first two and refuses the third. That is the whole of the distinction: a
# fact the design stated and a fact something else governs are both accounted for, and a fact the
# renderer put there on its own authority is a second design nobody approved.
#
# A value the artifact already carried, which no register of the design can express. Prose
# descriptions are the case: `typed_fields` deliberately does not render a field's `Meaning`, because
# the built corpus carries a description on some fields and not others — a sign it is documentation
# rather than governed content, and rendering it would have the generator author documentation the
# design never committed to. That reasoning holds, and it left an amendment unable to state the
# artifact whole: re-rendering a contract dropped every description it had.
#
# Preserving is not inventing. The renderer authors nothing here; it declines to delete what the
# design has no way to speak about. The origin is recorded so the measure counts it as accounted for
# rather than as a fact somebody stated.


def _stated(design: dict, short: str, column: str) -> bool:
    """Whether the design carries a value in `column` for this vocabulary.

    Separate from reading the value because a fallback and a stated value that happens to equal the
    fallback are the same string and different facts, and the measure is asked about the second.
    """
    return any(cell(r, column) for r in rows(design, "vocabulary_extensions")
               if bare(cell(r, "Vocabulary Code")) == short)


def _carried(sink, path: str) -> None:
    """Record that a leaf was preserved from the artifact being amended, not authored here."""
    if sink is not None:
        sink[path] = (CARRIED_FROM_PREDECESSOR, "")


def _supplied(sink, path: str, governed_by: str = "") -> None:
    """Record that the renderer, not the design, put a value at `path`.

    `governed_by` names the artifact that fixes the value where one does — an event's moment field
    is supplied because the event constitution settles it, and a design restating what a
    constitution settles would state it twice. Where nothing governs it, the origin is the renderer
    itself and the measure refuses it.

    Silent when there is no sink: `_render` is called from places that want the machine block and
    not the accounting, and a builder should not have to know which caller it is serving.
    """
    if sink is None:
        return
    sink[path] = (GOVERNED_ELSEWHERE, governed_by) if governed_by else (SUPPLIED_BY_RENDERER, "")


def requirements(p7: dict, p8: dict, provenance: dict) -> list[tuple[str, str, bool]]:
    """Every fact construction needs, and whether the design supplies it.

    Derived rather than declared: the requirement list *is* the shape the renderer emits, walked
    leaf by leaf. A hand-maintained list drifts from the renderer the moment either changes, and it
    did — it read 100% while the generator could reproduce one artifact in twenty-five, because it
    asked whether a contract declared a pipeline and never whether each step declared its store.

    A leaf that comes out empty is a leaf the design did not determine — unless the design said so.
    An empty policy and an undeclared one look identical in the output, so the difference has to be
    a declaration: a capability with an explicit "no configuration" row is determined, one that is
    simply absent from `runtime_policies` is not.

    Where each leaf came from is read from `provenance`, keyed `<code>.<path>`: the attribution of
    this render, which `transformation.build.provenance` derives and nothing here derives again. A
    leaf it does not name was stated by the design, as the renderer's own records read.
    """
    out: list[tuple[str, str, bool]] = []
    for artifact in render_all(p7, p8):
        code = bare(artifact["machine"]["fqdn"])
        declared_empty = set(artifact.get("declared_empty") or ())
        for path, value in leaves(artifact["machine"]):
            # Presence, then origin. Presence alone cannot tell a value the design stated from one
            # the renderer wrote on its own authority — both are non-empty, and for as long as that
            # was the whole test a renderer that never asked could invent freely and still measure
            # complete. A leaf is determined when the design stated it, or when something else
            # governs it and the renderer said which.
            present = not _empty(value) or path in declared_empty
            origin = provenance.get(f"{code}.{path}", STATED_BY_DESIGN)
            out.append((code, path, present and origin != SUPPLIED_BY_RENDERER))

    # An artifact construction has no builder for determines nothing, and must be counted as
    # determining nothing. Leaving it out of the measurement entirely — which is what skipping it
    # silently amounted to — let a design score 100% while naming an artifact that cannot be built.
    for code, fam in unrenderable(p7, p8):
        out.append((bare(code), f"<no builder for family {fam}>", False))

    # A generated artifact is determined by its generator, not by this design, and construction
    # renders none of its fields. It still has to appear in the measurement: an artifact that
    # vanished from it would let a design schedule something and be graded on everything else, which
    # is the same silence that let an unbuildable family read as no failure. What the design owes is
    # the generator, so that is the one fact measured.
    for code, (generator, srcs) in generated(p7).items():
        out.append((code, "<reached by generator>", bool(generator and srcs)))

    # A replaced artifact is not rendered — there is nothing left to render it from — and so none of
    # its facts were required and it vanished from the measurement entirely. A design could retire a
    # workflow and be graded on everything except the retirement. What it owes is the successor, so
    # that is the one fact measured, exactly as a generated artifact owes its generator.
    for code, successors in retirements(p7).items():
        out.append((code, "<superseded by>", bool(successors)))
    return out


def _empty(value: Any) -> bool:
    return value is None or value == "" or value == {} or value == []


def generated(p7: dict) -> dict[str, tuple[str, list[str]]]:
    """`bare code → (generator, sources)` for every artifact the design says is reached, not written.

    An artifact is generated or it is authored, and the difference is the whole of what construction
    may do with it. Construction never writes a generated artifact: two producers of one truth drift,
    and the drift is silent until something reads the stale one. So this is consulted before anything
    is rendered rather than after — a renderer that produced the file and then discarded it would
    still have decided what the file says.
    """
    out: dict[str, tuple[str, list[str]]] = {}
    for row in rows(p7, "generation_provenance"):
        code = bare(cell(row, "Artifact"))
        if not code:
            continue
        srcs = items(row, "Generator Sources")
        out[code] = (cell(row, "Generator"), srcs)
    return out


def supersessions(p7: dict) -> dict[str, tuple[str, list[str]]]:
    """`retired bare code -> (its identity as authored, the identities superseding it)`.

    Addressed by bare code because that is how the topology and the inventory name an artifact, and
    carrying the authored identity alongside because closure is asserted over exact FQDNs.

    Stated on the *successor*, because that is the artifact being authored and the one whose header
    carries `Supersedes`. Read the other way — a column on the inventory row of the artifact going
    away — the fact would live on a document construction never renders, which is how it came to
    live only in prose.

    Several successors for one predecessor is the ordinary case rather than an edge: a workflow split
    into an accept and a reject path retires one artifact and authors two.
    """
    out: dict[str, tuple[str, list[str]]] = {}
    for row in rows(p7, "artifact_properties"):
        if cell(row, "Property") != "supersedes":
            continue
        # Keyed by the bare code, because that is how the topology and the inventory address an
        # artifact. The *value* stays the identity as authored: closure is asserted over an exact
        # FQDN, and baring it here would emit a short name into the one place short names are refused.
        successor = norm(cell(row, "Artifact"))
        for retired in items(row, "Value"):
            out.setdefault(bare(retired), (retired, []))
            if successor not in out[bare(retired)][1]:
                out[bare(retired)][1].append(successor)
    return out


def retirements(p7: dict) -> dict[str, list[str]]:
    """Every artifact this design replaces, and what stands in its place.

    A REPLACE is not rendered. The design says the artifact is superseded, not that it is rewritten,
    and construction has nothing to write it from — the inventory row carries no summary because
    there is no artifact left to summarise. What construction does instead is mark it, so a reader
    of the composition can see that it has been stood down and by what.
    """
    superseded = supersessions(p7)
    return {bare(cell(r, "FQDN")): superseded.get(bare(cell(r, "FQDN")), ("", []))[1]
            for r in rows(p7, "existing_inventory") if cell(r, "Action") == "REPLACE"}


def _scheduled(p7: dict, p8: dict) -> list[tuple[str, str, str]]:
    """Every `(code, short, family)` the mandate schedules or the design amends.

    Shared by `render_all` and `unrenderable` so the two cannot disagree about what construction
    was asked for — the whole point of separating them is that one answers and the other reports
    the remainder, and a second reading of the mandate would let a family fall through both.
    """
    family = {bare(cell(r, "Code")): cell(r, "Family") for r in rows(p7, "new_artifacts")}
    # What the mandate schedules, then what the design amends. An extended artifact is never a build
    # step — `BUILD_CODE_ALREADY_EXISTS` refuses to mandate authoring an identity the composition
    # already holds — so nothing rendered it, and the first change request to extend anything
    # produced a workflow naming a runtime binding that did not bind it and contracts writing to
    # stores that did not exist. Scheduling and amendment are different acts; both are realized.
    amended = [cell(r, "FQDN") for r in rows(p7, "existing_inventory")
               if cell(r, "Action") == "EXTEND"]
    scheduled = [cell(r, "Code") for r in rows(p8, "build_order")]

    # A generated artifact is scheduled like any other — the artifact is what enters the composition
    # and what conformance judges, and a mandate scheduling a generator would schedule something that
    # never appears in a snapshot. It is simply not construction's to write. Dropping it here rather
    # than at the point of writing is what keeps `ONE_ARTIFACT_ONE_PRODUCER` true of the renderer and
    # not only of the caller: nothing downstream is ever handed a rendering of it to be tempted by.
    reached = generated(p7)

    out = []
    for code in scheduled + amended:
        short = bare(code)
        if short in reached:
            continue
        # A scheduled artifact declares its family; an amended one carries it in its own identity,
        # which is the only place it can, because the design assigns no new code for it.
        out.append((code, short, family.get(short) or short.split("_")[0]))
    return out


def unrenderable(p7: dict, p8: dict) -> list[tuple[str, str]]:
    """`(code, family)` the mandate schedules that construction has no builder for.

    A family with no builder was previously skipped in silence. Nothing was emitted, so nothing was
    measured, and completeness reported a fully determined design over an artifact construction
    cannot produce at all — the design was graded only on the artifacts it happened to be able to
    build. An unbuildable artifact is the strongest possible construction failure and it read as no
    failure at all.

    Reported here rather than raised: the whole point of Construction Completeness is that a design
    is told everything it fails to determine in one pass, and a family gap is one more such fact.
    """
    return [(code, fam) for code, _, fam in _scheduled(p7, p8) if fam not in _BUILDERS]


def render_all(p7: dict, p8: dict) -> list[dict]:
    """Every artifact the mandate schedules *and construction can build*, as `{path, machine}`.

    One call over the whole mandate rather than one call per artifact: a capability contract is a
    fixed pipeline with no iteration, so a construction step that rendered one artifact could never
    render twenty-five. The iteration lives inside a pure transform, where it observes nothing.

    A family with no builder is absent from this list and reported by `unrenderable` instead, so a
    caller that writes files never has to reason about an artifact that has no path.
    """
    summary = {bare(cell(r, "Code")): cell(r, "Summary") for r in rows(p7, "new_artifacts")}
    # An amended artifact states what it is in the inventory, because the design assigns it no new
    # identity row to state it in. Rendering it without its summary would empty a field the
    # composition already carries — an amendment that quietly deletes is worse than none.
    summary.update({bare(cell(r, "FQDN")): cell(r, "Summary")
                    for r in rows(p7, "existing_inventory") if cell(r, "Action") == "EXTEND"})
    subdomain = {bare(cell(r, "Code")): cell(r, "Subdomain Field")
                 for r in rows(p8, "field_declarations")}

    # Read once, inverted: the design states supersession on the successor, and the successor is
    # what is being rendered here.
    supersedes: dict[str, list[str]] = {}
    for retired_fqdn, successors in supersessions(p7).values():
        for successor in successors:
            supersedes.setdefault(bare(successor), []).append(retired_fqdn)

    out = []
    for code, short, fam in _scheduled(p7, p8):
        if fam not in _BUILDERS:
            continue
        declared_empty: list[str] = []
        supplied: dict[str, tuple[str, str]] = {}
        machine = _render(fam, code, short, summary.get(short, ""), subdomain.get(short, ""),
                          p7, p8, declared_empty, sorted(supersedes.get(short, ())), supplied)
        domain = norm(code).split("::")[0]
        out.append({
            "path": f"registry/{subdomain.get(short, '')}/{DIRECTORY[fam]}/{short}.md",
            "domain": domain,
            "machine": machine,
            # Header, not Machine: what an artifact stands in for is a fact about the composition's
            # history, and the compiler models none of it.
            "supersedes": sorted(supersedes.get(short, ())),
            # Leaves the design deliberately left empty, so a measurement can tell a declared
            # "nothing here" from an omission.
            "declared_empty": declared_empty,
            # Where each value the renderer did not read from a register came from. Absent means the
            # design stated it: a builder reaches for a register and writes what it finds, so the
            # ordinary case needs no record and only a departure does.
            "supplied": supplied,
        })
        if fam == "CT":
            vector = _vector(code, short, subdomain.get(short, ""), p7)
            if vector is not None:
                out.append(vector)
    return out


def _vector(code: str, short: str, sub: str, p7: dict) -> dict | None:
    """A transform's test vector, rendered beside it from the design's cases.

    A companion, not a scheduled artifact: its identity follows from its transform's, so the design
    assigns it no code and the mandate orders no step for it (`design.families`, `companion`). Governed
    by `conformance::CONSTITUTION_TEST_DATA_V1`; its shape is `SCHEMA_TEST_DATA_V0`.
    """
    cases = [r for r in rows(p7, "test_cases") if bare(cell(r, "CT Code")) == short]
    if not cases:
        return None
    values = [r for r in rows(p7, "test_case_values") if bare(cell(r, "CT Code")) == short]
    declared_empty: list[str] = []
    rendered_cases = []
    for i, row in enumerate(cases):
        case_id = cell(row, "Case")
        by_role: dict[str, dict] = {"INPUT": {}, "EXPECTED": {}, "ASSERT": {}, "RECORDED": {}}
        for v in values:
            if cell(v, "Case") == case_id and cell(v, "Role") in by_role:
                by_role[cell(v, "Role")][cell(v, "Field")] = value(v, "Value")
        case: dict[str, Any] = {"case_id": case_id, "expected_outcome": cell(row, "Expected Outcome"),
                                "bindings": by_role["INPUT"]}
        for key, role in (("expected", "EXPECTED"), ("assertions", "ASSERT"), ("recorded", "RECORDED")):
            if by_role[role]:
                case[key] = by_role[role]
        # A case handed nothing, or expecting a value that is empty, says so — both are stated.
        declared_empty.extend(_declared_empty_leaves(case, f"cases[{i}]"))
        rendered_cases.append(case)
    domain = norm(code).split("::")[0]
    fqdn = f"{domain}::TEST_DATA_{short}"
    machine = {
        "fqdn": fqdn,
        "artifact_kind": KIND["TEST_DATA"],
        "version": "V0",
        "governed_by": GOVERNED_BY["TEST_DATA"],
        "authority": "pgc.platform",
        "concern": sub,
        "target": norm(code),
        "cases": rendered_cases,
    }
    return {
        "path": f"registry/{sub}/{DIRECTORY['TEST_DATA']}/TEST_DATA_{short}.md",
        "domain": domain,
        "machine": machine,
        "supersedes": [],
        "declared_empty": declared_empty,
        "supplied": {},
    }


def _declared_version(code: str) -> str:
    """The version an identity declares, as its `_V<n>` suffix states it."""
    match = re.search(r"_V(\d+)$", bare(code))
    if not match:
        raise ValueError(f"{code} declares no version: an identity ends in _V<n>")
    return f"v{match.group(1)}"


def _render(fam, code, short, summary, sub, p7, p8, declared_empty=None,
            supersedes: list[str] | None = None, supplied: dict | None = None) -> dict:
    machine: dict[str, Any] = {
        "fqdn": code,
        "artifact_kind": KIND[fam],
        # The version the design declared, which is the suffix of the identity it assigned. A literal
        # here sealed every successor as `v0`: a `_V1` replacing its predecessor read as the same
        # version as what it replaced.
        "version": _declared_version(code),
        "governed_by": GOVERNED_BY[fam],
        # Authority and concern are declared carriers, never derived from the identifier or the
        # source directory (GO-11, MB-7, ID-12, `2e` CA-1). `concern` is the design's own subdomain
        # field, so the renderer states what the design already decided rather than inferring it.
        "authority": "pgc.platform",
        "concern": sub,
    }
    # In the Machine block, not the header. It was a header fact for as long as nothing read it; the
    # compiler now asserts referential closure over it, so it is governed content and belongs where
    # governed content lives. The header line is rendered from here, so there is still one copy.
    if supersedes:
        machine["supersedes"] = supersedes[0] if len(supersedes) == 1 else list(supersedes)
    builder = _BUILDERS[fam]
    # The two extra channels are threaded the same way and for the same reason: a builder knows
    # things about what it wrote that the shape it returns cannot express. `declared_empty` carries
    # an emptiness the design chose; `supplied` carries a value the design never stated.
    if fam in ("RB", "CC", "TI", "WF"):
        builder(machine, code, short, summary, sub, p7, p8, declared_empty)
    elif fam == "VOCAB":
        builder(machine, code, short, summary, sub, p7, p8, declared_empty, supplied)
    elif fam == "CT":
        builder(machine, code, short, summary, sub, p7, p8, supplied, declared_empty)
    elif fam in ("STRUCTURE", "EV"):
        builder(machine, code, short, summary, sub, p7, p8, supplied)
    else:
        builder(machine, code, short, summary, sub, p7, p8)
    return machine


def _intent(m, code, short, summary, sub, p7, p8):
    row = next((r for r in rows(p8, "new_intents") if bare(cell(r, "Code")) == short), {})
    m["core"] = {
        "summary": summary or cell(row, "Purpose"),
        "workflow": bare(cell(row, "Workflow")),
        "inputs": typed_fields(p7, code, "INPUT"),
        "outcomes": INTENT_OUTCOMES,
    }


def _workflow(m, code, short, summary, sub, p7, p8, declared_empty=None):
    binding = next((cell(r, "RB Code") for r in rows(p7, "rb_declarations")
                    if bare(cell(r, "Binds WF")) == short), "")
    topo = [r for r in rows(p7, "execution_topology") if bare(cell(r, "Workflow")) == short]
    # The actor a workflow runs as is the one the change authored — or, when the change extends a
    # subdomain that already has one, the one it carries over. Reading `new_artifacts` alone was
    # correct for exactly as long as every change request authored its own actor: the first
    # extension change reused the actor its predecessor built, and its workflows resolved to no
    # actor context at all while every design rule passed.
    actor = next((cell(r, "Code") for r in rows(p7, "new_artifacts")
                  if cell(r, "Family") == "AC"), "")
    if not actor:
        actor = next((cell(r, "FQDN") for r in rows(p7, "existing_inventory")
                      if bare(cell(r, "FQDN")).startswith("AC_")), "")

    nodes: dict[str, Any] = {}
    start = ""
    for r in topo:
        node = bare(cell(r, "Node"))
        node_type = cell(r, "Node Type")
        if node_type == "IN" and not start:
            start = node
        if node_type in ("EXIT", "EXIT_SUCCESS"):
            # An exit announces or it does not. `emit` is the only key the platform reads on an
            # EXIT node — the compiler projects it into the dispatch table and the scheduler fires
            # the event when the node is reached. What stood here before was `outcome`, which no
            # constitution declares, no compiler assertion checks and no runtime reads, carrying a
            # value derived from whether the node's name ended in COMPLETED. Every domain this
            # renderer produced therefore declared events it could never fire, while every
            # hand-authored domain fired them: the field that worked was the one nothing wrote.
            spec_exit: dict[str, Any] = {"type": "EXIT"}
            # An act may complete several moments at one ending and announces each of them, in the
            # order the design states. A design says so by writing them comma-separated in one
            # property, or by declaring `emit.<node>` more than once — rows are read in document
            # order, so the order a reader sees is the order the act announces.
            #
            # One moment is rendered as one name rather than a list of one, because that is what
            # every act announcing today carries and rewriting them would be a change to artifacts
            # this design does not touch. The platform reads either.
            announced = [m for r in rows(p7, "artifact_properties")
                         if bare(cell(r, "Artifact")) == short
                         and cell(r, "Property") == f"emit.{node}"
                         for m in items(r, "Value")]
            if len(announced) == 1:
                spec_exit["emit"] = announced[0]
            elif announced:
                spec_exit["emit"] = announced
            elif declared_empty is not None:
                # An exit that announces nothing is a design decision, not an omission — most
                # refusal exits announce nothing — so it is declared rather than left to measure
                # as an undetermined leaf.
                declared_empty.append(f"core.nodes.{node}.emit")
            nodes[node] = spec_exit
            continue
        # A node is its contract unless the design keys it: a workflow running one contract at
        # several places names each place and states the contract in `Runs`.
        spec: dict[str, Any] = {"type": node_type, "code": bare(cell(r, "Runs")) or node}
        bindings = _bindings(p7, short, node, "INPUT")
        if bindings:
            spec["inputs"] = bindings
        spec["next"] = _edges(value(r, "Routing"))
        nodes[node] = spec

    m["runtime_binding"] = binding
    # The reach the design declared, emitted onto the act that declared it. Omitted where none is
    # declared, which is most acts — the schema admits its absence and reads a present-but-empty
    # list as a claim that the act consults nothing, which is a different statement.
    #
    # This is the half without which the register is decoration: a reach a reviewer approved and
    # construction dropped would leave the act to be finished by hand, and a reach added by hand
    # works, passes every check, and is one no reviewer saw.
    named = sorted({n for r in rows(p7, "declared_reach") if bare(cell(r, "Act")) == short
                    for n in items(r, "Consults")})
    if named:
        m["consults"] = named
    m["subdomain"] = sub
    m["structure"] = WORKFLOW_STRUCTURE
    m["core"] = {"summary": summary, "actor_context": actor, "start_node": start, "nodes": nodes}


def _bindings(p7: dict, owner: str, step: str, direction: str) -> dict:
    """What one node or step is handed, or where its results go."""
    return {cell(b, "Field"): _binding(value(b, "Bound To"))
            for b in rows(p7, "step_bindings")
            if bare(cell(b, "Owner")) == owner and bare(cell(b, "Step")) == step
            and cell(b, "Direction") == direction}


def _literal_or(bound: Any) -> tuple[bool, Any]:
    """Whether a binding states its value outright, and the value: a literal is the value it states,
    and the generated marker reads as the word that declared it."""
    if isinstance(bound, dict) and "literal" in bound:
        return True, bound["literal"]
    if isinstance(bound, dict) and bound.get("generated") is True:
        return True, "generated"
    return False, bound


def _binding(bound: Any) -> Any:
    """A declared source rendered as the runtime's binding expression.

    The design states where a value comes from; the `$.`-prefixed form is a rendering convention of
    the execution surface, which is construction's business and not the designer's. A literal is
    the value it states. Any other text is a source the design rules refuse, and is handed on as
    written.
    """
    stated, bound_to = _literal_or(bound)
    if stated:
        return bound_to
    bound_to = norm(bound_to)
    if bound_to.startswith(("payload.", "results.", "inputs.", "capability_result.", "result_status")):
        return f"$.{bound_to}"
    return bound_to


def _edges(routing: Any) -> dict:
    """A routing, outcome → target, with each target bare. One that states nothing routes nowhere."""
    if not isinstance(routing, dict):
        return {}
    return {norm(outcome): bare(target) for outcome, target in routing.items()}


def _declared_empty_leaves(value, path: str) -> list[str]:
    """Every leaf inside a step that the design stated as empty.

    An empty value a design *wrote* is determined; the completeness measure cannot tell it from a
    value nobody supplied, because both are falsy. The distinction is the same one `declared_empty`
    already draws for a step handed nothing — a rule comparing a barcode against `''` or a subject
    list against `[]` says exactly what it means, and refusing the design for saying it would make
    "must not be empty" inexpressible.
    """
    out = []
    # An empty container is the leaf, not a thing to descend into: recursing first would iterate
    # nothing and record nothing, which is how `value: []` stayed undetermined.
    if _empty(value):
        out.append(path)
    elif isinstance(value, dict):
        for key, item in value.items():
            out.extend(_declared_empty_leaves(item, f"{path}.{key}"))
    elif isinstance(value, (list, tuple)):
        for i, item in enumerate(value):
            out.extend(_declared_empty_leaves(item, f"{path}[{i}]"))
    return out


def _contract(m, code, short, summary, sub, p7, p8, declared_empty=None):
    steps = [r for r in rows(p7, "cc_composition") if bare(cell(r, "CC Code")) == short]
    pipeline = []
    for r in steps:
        # A step handed nothing is determined, not undetermined — the design said so by writing the
        # none marker in `Consumes`. `SELECT` reads a whole store and declares no parameters, so the
        # empty `inputs` the schema requires has to be a declaration rather than a silence, or the
        # completeness measure counts a stated fact as a gap and the build gate refuses its own design.
        if not items(r, "Consumes") and declared_empty is not None:
            declared_empty.append(f"core.pipeline[{len(pipeline)}].inputs")
        index = len(pipeline)
        pipeline.append(_step(p7, short, r))
        if declared_empty is not None:
            declared_empty.extend(_declared_empty_leaves(pipeline[index], f"core.pipeline[{index}]"))
        interpreter = cell(r, "Interpreted By")
        if interpreter:
            # The interpretation is a step of its own; the register folds it into the row it
            # interprets because it is always positionally bound to that observation.
            name = _interpret_step(p7, short, r)
            pipeline.append(_step(p7, short, r, interpreter=interpreter, name=name,
                                  last=r is steps[-1]))
    statuses = _exit_statuses(pipeline)
    m["core"] = {
        "summary": summary,
        "inputs": typed_fields(p7, code, "INPUT"),
        "outputs": typed_fields(p7, code, "OUTPUT"),
        "result_status_contract": {"allowed": statuses, "on_input_failure": "VIOLATION"},
        "pipeline": pipeline,
    }


def _step(p7: dict, owner: str, r: dict, interpreter: str = "", name: str = "",
          last: bool = False) -> dict:
    """One pipeline step: what it binds, what it addresses, and how it routes on its own result."""
    step_name = name or cell(r, "Step Name")
    out: dict[str, Any] = {"step": step_name}
    if interpreter:
        out["transform"] = interpreter
    else:
        kind = cell(r, "Kind")
        out["side_effect" if kind == "CS" else "transform"] = cell(r, "Capability")
        if kind == "CS":
            out["op"] = cell(r, "Operation")
        store = cell(r, "Store")
        if store:
            out["store"] = store
    inputs = _bindings(p7, owner, step_name, "INPUT")
    outputs = _bindings(p7, owner, step_name, "OUTPUT")
    # `inputs` is emitted even when empty. The capability-contract schema requires the key on every
    # step, and a step legitimately takes none: `SELECT` reads a whole store and declares no
    # parameters. Omitting it made the compiler refuse two contracts for a schema violation the
    # design had not committed — an absent binding is a declaration that there is none, and it has to
    # be written down to say so.
    out["inputs"] = inputs
    if outputs:
        out["outputs"] = outputs
    if interpreter:
        semantic = cell(r, "Semantic Status")
        routing = {"SUCCESS": "exit" if last else "continue"}
        if semantic and semantic != "SUCCESS":
            routing[semantic] = "exit"
        routing["VIOLATION"] = "exit"
    else:
        routing = _edges(value(r, "Routing"))
    if routing:
        out["result_surface"] = list(routing)
        out["on_result"] = routing
    return out


def _exit_statuses(pipeline: list[dict]) -> list[str]:
    """Every status that can exit the contract, which is what its surface must contract for.

    Derived from the routing rather than from `Semantic Status`. The two are not the same set — a
    step's own operation can exit on a status the design never named semantically, and
    `ASSERT_TOPOLOGY_CONTRACT_CLOSED_V1` requires the contract to be closed over *exits*: an
    uncontracted exit and an unreachable contracted code are both violations. Deriving from the
    semantic column produced exactly the first when a READ began exiting on NOT_FOUND.

    A last step routing `continue` exits the contract too — there is nothing left to continue to.
    """
    out: list[str] = []
    for i, step in enumerate(pipeline):
        last = i == len(pipeline) - 1
        for outcome, target in (step.get("on_result") or {}).items():
            if target == "exit" or (last and target == "continue"):
                if outcome not in out:
                    out.append(outcome)
    return out


def _interpret_step(p7: dict, owner: str, r: dict) -> str:
    """The interpreting step's declared name — the one step_bindings addresses it by."""
    observed = cell(r, "Step Name")
    for b in rows(p7, "step_bindings"):
        if bare(cell(b, "Owner")) != owner:
            continue
        if cell(b, "Bound To").startswith(f"results.{observed}."):
            return cell(b, "Step")
    return f"interpret_{observed}"


TRANSFORM_CONSTITUTIONS = {
    "molecule": "capability_transforms::CONSTITUTION_MOLECULES_V0",
    "ct_impure": "capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0",
}


def _transform_constitution(kind: str, purity: str) -> str:
    """The constitution that governs a transform, placed by kind and then by purity."""
    if kind == "molecule":
        return TRANSFORM_CONSTITUTIONS["molecule"]
    return TRANSFORM_CONSTITUTIONS.get(purity, GOVERNED_BY["CT"])


def _transform(m, code, short, summary, sub, p7, p8, supplied=None, declared_empty=None):
    row = next((r for r in rows(p7, "implementation_bindings") if bare(cell(r, "CT Code")) == short), {})
    m["core"] = {
        "summary": summary,
        # How the transform expresses a judgement, which the schema requires and no other register
        # carries. Rendered from the design rather than inferred from the implementation: the
        # implementation is what the module path points at, and reading behaviour out of it here
        # would make construction a second authority on what the transform does.
        "refusal": cell(row, "Refusal"),
        "inputs": typed_fields(p7, code, "INPUT"),
        "outputs": typed_fields(p7, code, "OUTPUT"),
    }
    if not cell(row, "Kind"):
        _supplied(supplied, "machine.ct_kind")
    if not cell(row, "Purity"):
        _supplied(supplied, "machine.ct_purity")
    m["machine"] = {
        "ct_kind": cell(row, "Kind") or "atom",
        "ct_purity": cell(row, "Purity") or "ct_pure",
        "operation": cell(row, "Operation"),
    }
    # Which constitution governs a transform is decided by what it declares, never by its family: a
    # molecule by the molecules constitution, a non-deterministic atom by its own, every other atom by
    # the transforms constitution. The family's single constitution was right for as long as every
    # transform rendered was a deterministic atom, and the compiler refused the first design that
    # rendered anything else.
    m["governed_by"] = _transform_constitution(m["machine"]["ct_kind"], m["machine"]["ct_purity"])
    if cell(row, "Kind") == "molecule":
        # A molecule is run as its declared steps and names no implementation: a module beside the
        # steps would be a second account of what it does, and the runtime would follow one of them.
        stream, emit = _molecule(p7, short, declared_empty)
        m["machine"]["atom_stream"] = stream
        m["machine"]["emit"] = emit
    else:
        # Where the implementation lives is not the design's to state: the domain's build manifest
        # resolves transforms under `<domain>.implementation.capability_transforms.atoms`, and the
        # module is named for the artifact it implements (CONSTRUCTION_MAPPING.md).
        domain = norm(code).split("::")[0]
        m["machine"]["implementation"] = {
            "module": f"{domain}.implementation.capability_transforms.atoms.{short.lower()}",
            "callable": cell(row, "Callable"),
        }
        _supplied(supplied, "machine.implementation.module",
                  governed_by=f"{domain}::STRUCTURE_BUILD_{domain.upper()}_CONFIG_V0")


def _molecule_source(bound: Any) -> Any:
    """A molecule binding's declared source as the executor's binding expression.

    Separate from `_binding` because a molecule has two roots a contract step does not — the member a
    loop pass is on, and the values the loop carries — and `iterator` read as a contract binding is a
    literal word. A constant is stated as `{literal: v}` and is that value; any other text passes
    through as written.
    """
    stated, bound_to = _literal_or(bound)
    if stated:
        return bound_to
    bound_to = norm(bound_to)
    if bound_to == "iterator":
        return "$.iterator"
    if bound_to.startswith(("inputs.", "results.", "accumulator.")):
        return f"$.{bound_to}"
    return _bound_value(bound_to)


def _molecule(p7: dict, owner: str, declared_empty=None) -> tuple[list[dict], dict]:
    """A molecule's atom stream and its emission, as the compiler reads them.

    One entry per `molecule_steps` row, in the order the design states — the order the steps run in
    and in no other. An atom or a molecule run once is handed its `INPUT` rows as `with`; a loop is
    handed them on every pass as `inputs`, starts its carried values from `CARRY` and takes them
    forward from `UPDATE`. Each map is omitted where the design binds nothing into it, because the
    compiler reads an absent map as an empty one and an empty map is a leaf nothing determined.
    """
    steps = [r for r in rows(p7, "molecule_steps") if bare(cell(r, "CT Code")) == owner]
    bindings = [r for r in rows(p7, "molecule_step_bindings") if bare(cell(r, "CT Code")) == owner]

    def bound(step: str, role: str) -> dict:
        return {cell(b, "Field"): _molecule_source(value(b, "Bound To"))
                for b in bindings if cell(b, "Step") == step and cell(b, "Role") == role}

    stream: list[dict] = []
    emit: dict[str, str] = {}
    for r in steps:
        step, kind, target = cell(r, "Step"), cell(r, "Kind"), cell(r, "Target")
        entry: dict[str, Any] = {"kind": kind, "atom" if kind == "atom" else "molecule": target, "as": step}
        if kind == "loop":
            entry["over"] = f"$.{cell(r, 'Over')}"
            entry["iterator"] = cell(r, "Iterator")
            for key, role in (("accumulator", "CARRY"), ("inputs", "INPUT"),
                              ("update_accumulator", "UPDATE")):
                values = bound(step, role)
                if values:
                    entry[key] = values
        else:
            values = bound(step, "INPUT")
            if values:
                entry["with"] = values
        if declared_empty is not None:
            # A carried value that starts empty is stated, not missing — a response that begins as
            # no words is exactly what the design says it is.
            declared_empty.extend(_declared_empty_leaves(entry, f"machine.atom_stream[{len(stream)}]"))
        stream.append(entry)
        emits = cell(r, "Emits")
        if emits:
            emit[emits] = step
    return stream, emit


# Properties that describe the *document* rather than the artifact the compiler reads. Supersession
# is a fact about which artifact stands in the composition, and the compiler models no such thing —
# putting it in the Machine block would declare a key nothing reads, which is the shape of defect
# this codebase keeps finding rather than one to add.
HEADER_ONLY_PROPERTIES = {"supersedes"}


def _property_value(r: dict) -> Any:
    """A property's value as the design states it: the names it lists, a text, or a typed value."""
    held = value(r, "Value")
    if isinstance(held, list):
        return list(items(r, "Value"))
    return norm(held) if isinstance(held, str) else held


def _properties(p7: dict, code: str) -> dict:
    return {cell(r, "Property"): _property_value(r)
            for r in rows(p7, "artifact_properties")
            if bare(cell(r, "Artifact")) == bare(code)
            and cell(r, "Property") not in HEADER_ONLY_PROPERTIES}


def _actor(m, code, short, summary, sub, p7, p8):
    m["core"] = {"summary": summary, **_properties(p7, code),
                 "attributes": typed_fields(p7, code, "ATTRIBUTE")}


def _vocabulary(m, code, short, summary, sub, p7, p8, declared_empty=None, supplied=None):
    """A controlled vocabulary: what it admits, and what it builds on.

    A base vocabulary extends nothing, and that is a decision rather than an omission. The design
    says so with the none marker; rendered, the field is empty either way, so the measurement is told
    which emptiness this is. Without that a vocabulary nobody finished and one deliberately rooted
    look identical, and only one of them is designed.
    """
    own = [r for r in rows(p7, "vocabulary_extensions") if bare(cell(r, "Vocabulary Code")) == short]
    stated = next((value(r, "Extends") for r in rows(p7, "vocabulary_extensions")
                   if bare(cell(r, "Vocabulary Code")) == short), "")
    extends = norm(stated)
    if stated is None:
        if declared_empty is not None:
            declared_empty.append("extends")
    m.pop("core", None)
    m["extends"] = extends
    # The group each value belongs to and the spelling it must take. Both were literals for as long
    # as every vocabulary rendered was a result status, and the first one that was not carried a
    # group it does not belong to and a spelling its values do not have — the platform refused it.
    #
    # Each row states its own group, and a vocabulary may declare several. Reading the group from the
    # first row put every entry under it: a vocabulary of two groups was sealed as one, every value
    # still present, and the measure counted it determined because it reads values, not where they
    # sit. So the groups are rendered as the rows state them, in the order they first appear.
    #
    # The group name is a key rather than a value, so no leaf *is* it — recording it as supplied
    # would mark the whole subtree beneath it, which would slander every entry the design stated.
    for r in own:
        group = cell(r, "Group") or "result_status"
        if group not in m:
            if not cell(r, "Casing"):
                _supplied(supplied, f"{group}.casing")
            m[group] = {"casing": cell(r, "Casing") or "UPPER_SNAKE", "entries": []}
        m[group]["entries"].append(cell(r, "Value"))


def _structure(m, code, short, summary, sub, p7, p8, supplied=None):
    stores = {cell(r, "Store Name"): {"path": cell(r, "Proposed Path")}
              for r in rows(p7, "structure_stores")}
    props = _properties(p7, code)
    if "layer" not in props:
        _supplied(supplied, "core.layer")
    m["core"] = {"summary": summary, "layer": props.pop("layer", "DOMAINS"),
                 "domain": norm(code).split("::")[0], "subdomain": sub,
                 "entity_stores": stores, **props}


def _binding_artifact(m, code, short, summary, sub, p7, p8, declared_empty=None):
    """A runtime binding as the runtime reads it.

    `dispatcher.py` resolves `rb_policy[rb][cs]["policy"]` at execution, so the bindings map is
    keyed by capability side effect, not by workflow. Which workflow binds which RB is a different
    fact and lives on the workflow, where `rb_declarations.Binds WF` puts it.
    """
    decls = [r for r in rows(p7, "rb_declarations") if bare(cell(r, "RB Code")) == short]
    structure = next((cell(r, "Storage Structure") for r in decls), "")

    policies: dict[str, dict] = {}
    for r in rows(p7, "runtime_policies"):
        if bare(cell(r, "RB Code")) != short:
            continue
        capability = cell(r, "Capability")
        key = cell(r, "Key")
        # A row whose key is the none-marker declares that this capability needs no configuration,
        # which is a different statement from having no row at all.
        policies.setdefault(capability, {})
        if key:
            policies[capability][key] = cell(r, "Value")
        elif declared_empty is not None:
            declared_empty.append(f"core.bindings.{capability}.policy")

    bindings = {}
    for r in decls:
        for capability in items(r, "CS Bindings"):
            if capability:
                bindings[capability] = {"policy": policies.get(capability, {})}

    props = _properties(p7, code)
    parameters = props.pop("parameters", "")
    if parameters:
        m["parameters"] = list(parameters) if isinstance(parameters, list) else [str(parameters)]
    m["core"] = {"summary": summary, "storage_structure": structure, "bindings": bindings}


def _event(m, code, short, summary, sub, p7, p8, supplied=None):
    """A business moment the domain recognises: what it records, and the shape of the record.

    An event states a fact and triggers nothing — the workflow that raises it has already decided
    what happened. So the only thing to render beyond identity is the schema of the fact, which the
    design declares as the event's typed fields, plus the moment when it occurs.

    `timestamp` is added because every event in the composition carries one and no design should have
    to restate a fact the event constitution fixes — the same reason an intent's ACK/NACK surface is
    not restated either. A design that declares its own `timestamp` keeps it.
    """
    # An event's fields are what it records, whichever direction the design wrote them in. ATTRIBUTE
    # was dropped here without a word: blockchain's wallet and identity events were designed with
    # their fields as ATTRIBUTE and sealed carrying none of them.
    schema: dict[str, Any] = {}
    for direction in ("OUTPUT", "INPUT", "ATTRIBUTE"):
        for field, spec in typed_fields(p7, code, direction).items():
            schema.setdefault(field, spec)
    if "timestamp" not in schema:
        # Supplied, and accounted for: the event constitution fixes that a moment carries when it
        # occurred, so a design restating it would state it twice. Naming what governs it is what
        # separates this from the vocabulary's two literals, which nothing governs at all.
        for leaf in ("type", "format", "required", "description"):
            _supplied(supplied, f"core.schema.timestamp.{leaf}",
                      governed_by="event::CONSTITUTION_EVENT_V0")
    schema.setdefault("timestamp", {
        "type": "string",
        "format": "date-time",
        "required": True,
        "description": "When the moment occurred",
    })
    m["core"] = {
        "summary": summary or short,
        "description": summary or short,
        "subdomain": sub,
        "schema": schema,
    }
    # A refusal is a moment too: the design declares it, and an ending that refuses may announce only
    # a moment declared a refusal. Rendered so the sealed event says what it is, rather than the
    # declaration living in a design document the composition never reads.
    moment = next((cell(r, "Value") for r in rows(p7, "artifact_properties")
                   if bare(cell(r, "Artifact")) == bare(code) and cell(r, "Property") == "moment"), "")
    if moment:
        m["core"]["moment"] = moment



def _transport_rows(p7, code, direction):
    """The `transport_bindings` rows for one boundary contract, in declared order."""
    return [r for r in rows(p7, "transport_bindings")
            if bare(cell(r, "Artifact")) == bare(code)
            and cell(r, "Direction").upper() == direction]


def _nest(target: dict, path: str, value: Any) -> None:
    """Place `value` at a dotted `path`, creating the objects along the way.

    A payload template mirrors the shape the workflow reads, and a workflow reads structure —
    `$.payload.decided_actor_fields.state` is a value inside an object, not a key with a dot in its
    name. One row per leaf keeps the mapping checkable; nesting is what makes it the payload.
    """
    *parents, leaf = path.split(".")
    for key in parents:
        node = target.get(key)
        if not isinstance(node, dict):
            node = {}
            target[key] = node
        target = node
    target[leaf] = value


def _bound_value(bound: Any) -> Any:
    """What a `Bound To` cell means: a constant, or a text the boundary resolves.

    A constant is stated as `{literal: v}` and is that value, typed — the rules an act requires and a
    caller must not send. A text is a `${input.KEY}` substitution token or a path into the surface,
    and passes through as written. Nothing is read out of a text: a constant written as text would
    reach the act as text, which is how a template once silently sent the word "constant".
    """
    stated, bound = _literal_or(bound)
    return bound if stated else norm(bound)


def _transport_ingress(m, code, short, summary, sub, p7, p8, declared_empty=None):
    """A boundary contract admitting a caller the composition does not control.

    Its input contract is the artifact's own declared INPUT fields, exactly as an intent's is — the
    boundary and the intent behind it state their surface the same way, and a second spelling would
    let the two disagree about what a caller may send.
    """
    first = next(iter(_transport_rows(p7, code, "INGRESS")), {})
    m["operation"] = cell(first, "Operation")
    m["core"] = {"summary": summary}
    m["input_contract"] = typed_fields(p7, code, "INPUT")
    # Reserved in V0 and declared empty rather than omitted, so a measurement can tell a stated
    # "nothing required" from a fact the design forgot. The emptiness is the contract's own — the
    # version reserves it — so the builder declares it here rather than asking a design to state a
    # fact no design owns.
    m["context_requirements"] = []
    if declared_empty is not None:
        declared_empty.append("context_requirements")
    handler: dict[str, Any] = {
        "kind": cell(first, "Handler Kind"),
        "workflow": cell(first, "Handler Target"),
    }
    template: dict[str, Any] = {}
    for row in _transport_rows(p7, code, "INGRESS"):
        field = cell(row, "Field")
        if field:
            _nest(template, field, _bound_value(value(row, "Bound To")))
    if template:
        handler["payload_template"] = template
        if declared_empty is not None:
            # A payload leaf the design wrote as empty is determined, not missing. A rule refusing a
            # value equal to the empty string states that emptiness as its subject — measured as an
            # omission, the design would be told to supply the very thing it is forbidding.
            declared_empty.extend(_declared_empty_leaves(template, "handler.payload_template"))
    m["handler"] = handler


def _transport_egress(m, code, short, summary, sub, p7, p8):
    """A boundary contract shaping what a caller is told, and how a result status is classified.

    The output contract is a list rather than a mapping because order is part of it: a client reads
    the fields in the order the contract declares them.
    """
    first = next(iter(_transport_rows(p7, code, "EGRESS")), {})
    m["operation"] = cell(first, "Operation")
    m["core"] = {"summary": summary}
    m["output_contract"] = [
        {"field": cell(r, "Field"), "from": cell(r, "Bound To")}
        for r in _transport_rows(p7, code, "EGRESS") if cell(r, "Field")
    ]
    classification = {cell(r, "Property").removeprefix("result_class."): cell(r, "Value")
                      for r in rows(p7, "artifact_properties")
                      if bare(cell(r, "Artifact")) == bare(code)
                      and cell(r, "Property").startswith("result_class.")}
    if classification:
        m["result_classification"] = classification
    for key in ("default_result_class", "evidence_policy"):
        value = next((cell(r, "Value") for r in rows(p7, "artifact_properties")
                      if bare(cell(r, "Artifact")) == bare(code) and cell(r, "Property") == key), "")
        m[key] = value


_BUILDERS = {
    "IN": _intent, "WF": _workflow, "CC": _contract, "CT": _transform,
    "AC": _actor, "VOCAB": _vocabulary, "STRUCTURE": _structure, "RB": _binding_artifact,
    "EV": _event, "TI": _transport_ingress, "TE": _transport_egress,
}



# The domain build manifest ---------------------------------------------------------------------
#
# Not an artifact any change request designs. Every field of it is compiler configuration — which
# layers to search, how a namespace is matched, where projections are written — and a design that
# restated them would be declaring something it does not own, exactly as it would by restating a
# constitution.
#
# Hand-copying it per domain had failed visibly: the book library's manifest described itself as the
# AI governance domain and listed that domain's subdomains, because it was copied and never
# corrected, and nothing governed it. So it is derived from the three facts that actually vary — the
# domain, its subdomains, and the families it uses — all of which the mandate already declares.
#
# **It is a generated artifact, and a design that touches it says so** rather than restating it. The
# cost of the other reading was measured: a change adding a subdomain inventoried this as an EXTEND,
# and because an amendment must state the artifact whole it was obliged to restate fifty-one derived
# facts and invented a fifty-second — a `core.subdomain` the artifact does not carry — while the
# only thing that actually varies with a subdomain is one sentence of the summary. Reached now by
# invoking `build_manifest` through `build.generators`, which is also what the acceptance harness
# compares, so the claim that this derives what the composition holds is checked rather than
# asserted.

BUILD_PHASES = [
    ("discover", "Discover {domain} artifacts via STRUCTURE"),
    ("parse", "Parse artifacts into canonical machine form"),
    ("normalize", "Resolve references ({domain} + imported governance surface)"),
    ("validate", "Validate artifacts using compiler schema rules"),
    ("assert", "Evaluate cross-artifact invariants"),
    ("materialize", "Emit deterministic compiled artifacts ({domain} scope only)"),
]


def manifest_path(manifest: dict) -> str:
    """Where a domain's build manifest lives, relative to the domain root.

    One spelling, because two callers need it — the generator that writes the file and the check
    that asks whether the file agrees — and a second spelling is how they would come to disagree
    about which file they were talking about.
    """
    return f"registry/structures/{bare(manifest['fqdn'])}.md"


def build_manifest(p7: dict, p8: dict, held: tuple[str, ...] = ()) -> dict | None:
    """The compiler's discovery manifest for the domain this mandate builds.

    Returns None when the design neither schedules nor amends anything, because a manifest for no
    artifacts would declare a domain the composition has no reason to compile. An amendment is a
    reason: a change that states cases for transforms it only redeclares schedules nothing, and its
    domain must still compile the cases.

    `held` names the subdomains the domain already holds. A change to one subdomain declares only
    that one, and the manifest describes the domain, not the change: without them, amending one
    subdomain would describe a domain that had lost the others.
    """
    scheduled = [cell(r, "Code") for r in rows(p8, "build_order")]
    scheduled += [cell(r, "FQDN") for r in rows(p7, "existing_inventory") if cell(r, "Action") == "EXTEND"]
    if not scheduled:
        return None
    domain = norm(scheduled[0]).split("::")[0]
    subdomains = sorted({cell(r, "Subdomain Field") for r in rows(p8, "field_declarations")
                         if cell(r, "Subdomain Field")} | set(held))
    families = [f.code for f in FAMILIES if f.authorable]
    # A domain whose design states cases compiles vectors, and declares where their runnable cases are
    # written — beside its projections, where the runtime's conformance reads them and the assembler
    # carries them, apart from composition evidence. A domain with none declares neither, and its
    # manifest is exactly what it was.
    vectors = bool(rows(p7, "test_cases"))
    if vectors:
        families.append("TEST_DATA")
    layer = domain.upper()
    return {
        "fqdn": f"{domain}::STRUCTURE_BUILD_{layer}_CONFIG_V0",
        "artifact_kind": "STRUCTURE",
        "version": "V0",
        "governed_by": BY_CODE["STRUCTURE"].constitution,
        # Declared carriers, as for every rendered artifact. A build manifest sits at the domain
        # root rather than in a subdomain, so its concern is the domain itself.
        "authority": "pgc.platform",
        "concern": domain,
        "structure_scope": domain,
        "reuse_visibility": "business",
        "core": {
            "summary": f"Build-time STRUCTURE manifest ({domain} business-domain scope)",
            "description": (
                f"Compiles the {domain} domain's own artifacts, resolving governance and platform "
                f"capability references against the imported compiled governance surface. Emits "
                f"only {domain} artifacts. Self-describing: declares its own source layer and "
                f"namespace rule additively. Subdomains: {', '.join(subdomains) or 'none declared'}."
            ),
        },
        "layer_definitions": {
            layer: {
                "domain_subpath": "registry",
                "registry_module": f"{domain}.registry",
                "implementation_namespace":
                    f"{domain}.implementation.capability_transforms.atoms",
                "layer_category": "domain",
            }
        },
        "identity_rules": [{"match": f"{domain}.registry", "namespace": domain}],
        "artifact_discovery": {
            "search_layers": [layer],
            "import_surface": {"domain": "platform"},
            "artifact_types": families,
        },
        "output_configuration": {
            # Where this build writes, declared rather than taken from the environment (A10): two
            # compositions naming one root are refused, and a manifest without one does not build.
            "root": "snapshot",
            "artifacts": {"layer": "PROTOCOL_BUILD_ROOT", "subpath": "compiled/canonical"},
            "vocabulary_projection_path": {"layer": "GOVERNANCE", "subpath": "compiled/vocabulary"},
            "tokenized_projection_path": {"layer": "GOVERNANCE", "subpath": "compiled/tokenized"},
            "evidence_projection_path": {"layer": "GOVERNANCE", "subpath": "compiled/evidence"},
            "trust_attestation_path": {"layer": "GOVERNANCE", "subpath": "compiled/trust"},
            "visualization_projection_path":
                {"layer": "GOVERNANCE", "subpath": "compiled/visualization"},
            "layer_outputs": {layer: {"layer": layer, "subpath": "compiled/canonical"}},
            "bootstrap_search_roots": [{"layer": "GOVERNANCE", "subpath": "structure/structures"}],
        } | ({"conformance": {"layer": "GOVERNANCE", "subpath": "compiled/transform_conformance"}}
             if vectors else {}),
        "build_phases": [
            {"phase": name, "description": text.format(domain=domain)}
            | ({"target": "compiled/artifacts/"} if name == "materialize" else {})
            for name, text in BUILD_PHASES
        ],
    }


# Document rendering ---------------------------------------------------------------------------
#
# The Machine block is what the compiler reads, but an artifact is a *document*, and a document a
# human opens needs a header stating what it is. Every header field is determined — the code, the
# family, the constitution that governs it, the version — so rendering it invents nothing.
#
# What construction does **not** write is narrative. An artifact's rationale is human reasoning no
# register determines, and a generator that produced it would be authoring documentation nobody
# committed to and overwriting it on every rebuild. The document carries its declared summary and
# stops there; a reader who wants the reasoning reads the dossier that produced it.

HEADER_KIND = {
    "ACTOR": "actor", "INTENT": "intent", "WORKFLOW": "workflow",
    "CAPABILITY_CONTRACT": "capability_contract", "CAPABILITY_TRANSFORM": "capability_transform",
    "RUNTIME_BINDING": "runtime_binding", "VOCABULARY": "vocabulary", "STRUCTURE": "structure",
}


def render_document(artifact: dict) -> str:
    """One artifact as the Markdown document the compiler ingests."""
    import yaml

    machine = artifact["machine"]
    code = bare(machine["fqdn"])
    kind = machine["artifact_kind"]
    constitution = bare(machine["governed_by"])
    summary = (machine.get("core") or {}).get("summary", "")

    body = yaml.dump(machine, sort_keys=False, width=100, allow_unicode=True,
                     default_flow_style=False)
    # No header block. Artifact code, kind, governing constitution, version and supersession are
    # all declared in the Machine block below; restating them in prose is a second surface that can
    # disagree with the first, and the prose copy is always the weaker one (a short name where the
    # declaration carries an identity). The policy is vocabulary::VOCAB_HUMAN_BLOCK_CONSTRAINTS_V0;
    # the reasoning is in the Field Manual, `The human block`.
    #
    # The Machine block leads and the prose follows it as commentary, which is the actual
    # relationship between them.
    return (
        f"# {code}\n\n"
        "## Machine\n\n"
        "```yaml\n"
        f"{body}```\n\n"
        "---\n\n"
        "## Intent\n\n"
        f"{summary}\n"
    )


def render_documents(p7: dict, p8: dict) -> list[dict]:
    """Every scheduled artifact as `{path, text}` — what persistence is handed."""
    return [{"path": a["path"], "text": render_document(a)} for a in render_all(p7, p8)]


# Retirement ------------------------------------------------------------------------------------
#
# The one act construction performs on an artifact it did not write. A replaced artifact is marked
# rather than deleted: deleting is not construction's decision to make, and a composition that
# silently loses a file tells a later reader nothing about why. Marked, the artifact says what stood
# it down and a reader can follow the successor.
#
# Only the header is touched. The Machine block is what the compiler reads and it is not
# construction's to rewrite here; the prose is human narrative no register determines. So this is a
# header amendment and nothing else, and it is idempotent — running it twice leaves one marking.
#
# **What this does not do.** The compiler still discovers and compiles a marked artifact, because
# nothing in the governance surface models supersession. The marking is the record, and excluding a
# superseded artifact from a composition is a platform question that belongs with the platform.



def mark_superseded(text: str, successors: list[str]) -> str:
    """An existing artifact's Machine block, marked as stood down by its successors.

    The block rather than the header, because `INVARIANT_SUPERSEDED_NOT_REFERENCED_V0` reads it. The
    compiler sees the Machine block and nothing else, so a marking in the header was a marking
    nothing could enforce — true of this act from the day it was written until the invariant existed.
    The header line is rewritten to match, derived from the block rather than stated beside it.

    Fail-hard on a document with no block to mark, and on a marking with no successor. A marking that
    silently did nothing would leave the composition holding a live artifact the design believes is
    retired, which is the failure this act exists to close; and "superseded" by nothing is a deletion,
    which is a human act and not one a design declares.
    """
    if not successors:
        raise ValueError("refusing to mark an artifact superseded by nothing — that is a deletion")

    lines = text.splitlines(keepends=True)
    anchors = [i for i, line in enumerate(lines) if line.startswith("fqdn:")]
    if not anchors:
        raise ValueError("artifact carries no Machine block; refusing to mark it superseded")

    block = ["superseded_by:\n"] + [f"- {s}\n" for s in successors]
    existing = [i for i, line in enumerate(lines) if line.startswith("superseded_by:")]
    if existing:
        start = existing[0]
        end = next((i for i in range(start + 1, len(lines))
                    if not lines[i].startswith("- ")), len(lines))
        lines[start:end] = block
    else:
        lines[anchors[0] + 1:anchors[0] + 1] = block

    # Standing an artifact down writes `superseded_by` into the Machine block above and nothing
    # else. There was a prose `- **Status:**` line kept in step with it; it is gone, because two
    # records of one governed fact can disagree and supersession is a declared relation (`4e` SU-1,
    # SU-3). A reader asking whether an artifact is superseded reads the declaration.
    return "".join(lines)
