"""The generator behind every phase workflow — its sealed rule set, and the provenance saying so.

A phase declares its rules once, in `transformation/design/pN_*/rules.py`, over the registers its
template declares. The compiled workflow carries a *copy* of that declaration, because the rules
travel in the artifact where they can be sealed, versioned and inspected. Two copies of one truth
drift, and this one drifted silently: adding a rule after emitting a workflow left 52 rules sealed
against 55 declared, and every run reported confidently on the smaller set.

So the copy is generated, never typed, and this module is the generator. **A template and the
declaration read with it are one generator** — neither determines the artifact alone, and naming
either separately would permit regenerating from a stale pairing.

Two things are emitted into each workflow, and they answer different questions. The `rule_set:`
block is what the phase judges by. The `## Generated Artifact` section is what the artifact says
about itself: that it is generated, by what, and from which sources. Provenance belongs to the
artifact rather than to a list beside it, because a second statement of one truth can disagree with
the thing it describes.

**The generator is authoritative.** Where a workflow and this module disagree, the workflow is
stale — a disagreement is not a difference of opinion. Correcting the artifact would leave the
generator still producing the old value, so the fix would last until whoever next ran the emission.
`check()` is what makes that enforceable rather than merely stated.

This lives inside the package rather than under `scripts/` because construction must be able to
*invoke* it: a generated artifact is reached by invoking its generator, and a generator only a
person at a terminal can run is one nothing governs. `scripts/emit_rule_sets.py` remains as the
terminal's way in.
"""

from __future__ import annotations

from dataclasses import dataclass
import pathlib
from pathlib import Path

import yaml

from inspector import api as inspector_api

from transformation.design.catalog import PHASES
from transformation.machine_block import machine_yaml

REPO = Path(__file__).resolve().parents[2]
WORKFLOWS = REPO / "registry" / "design" / "workflows"

# The workflow each phase's rule set is sealed into, as the dispatch declares it.
SEALED_IN = {spec.id: f"{spec.workflow.split('::')[-1]}.md" for spec in PHASES}

# How a design names this generator, and how construction reaches it. One spelling, read by the
# provenance the artifacts carry and by the register a design states — the same string in both, or
# the agreement check compares a design against a generator it did not name.
GENERATOR = "transformation.design.emit:emit_rule_sets"

def workflow_fqdn(phase_id: str) -> str:
    """The identity of the artifact carrying a phase's sealed rule set.

    Derived from the one map above rather than restated, because a second spelling of which workflow
    belongs to which phase is a second thing to get wrong — and the thing it would get wrong is which
    rules a document is judged by.
    """
    return f"transformation::{SEALED_IN[phase_id][:-len('.md')]}"


RULE_SET_INDENT = 8

# The contract every phase workflow invokes, and the one place a phase's observations are handed to
# the evaluator. Its `observed` map was hand-authored while `OBSERVATIONS` declared the same thing in
# Python, and the two drifted exactly as two copies of one truth do: the map passed two keys where
# four were declared, so a rule reading the transform surface found nothing and returned nothing, and
# had been doing so through the compiled path since it was written.
JUDGE_CONTRACT = "registry/design/capability_contracts/CC_JUDGE_AGAINST_SNAPSHOT_V0.md"
CONTRACTS = REPO / "registry" / "design" / "capability_contracts"

OBSERVED_INDENT = 6

# The step that reads every observation, and therefore the one every observing step must precede.
# Named once: the emission places steps relative to it, and a second spelling would place them
# somewhere the runtime has already passed.
OBSERVATION_CONSUMER = "evaluate_rules"

# Every judging contract whose observing steps this generator owns. Only the first takes the
# generated `observed` map and its missing steps; both have their observing steps' outcomes brought
# into agreement, because an observing step written by hand is the copy that falls behind.
JUDGE_CONTRACTS = (
    JUDGE_CONTRACT,
    "registry/design/capability_contracts/CC_JUDGE_AGAINST_COMPOSITION_V0.md",
)

# The capability every observing step asks, and every outcome its QUERY operation declares — the
# `result_status_values` of `CS_SNAPSHOT_QUERY_V0`. An observing step answers for each of them, and
# ends its contract on any but SUCCESS (Open PGC Standard `v1` CP-13). The steps were written with
# three and omitted NOT_FOUND, which the inspector reports for an operation that names nothing.
#
# Held here once rather than read from the declaration, because the platform's registry is not
# shipped with its package. The compiler's step-surface check compares every step against the
# capability it binds, so a disagreement between this tuple and the declaration fails the build.
QUERY_CAPABILITY = "capability_side_effects::CS_SNAPSHOT_QUERY_V0"
QUERY_OPERATION = "QUERY"
# Where the outcomes an observing step answers are read from. The capability declares them; the
# generator holding its own copy was a second statement of a platform fact, so it observes them.
QUERY_OUTCOMES_OBSERVATION = "si.capability.surface"


def query_outcomes(snapshot_root: str | Path) -> tuple[str, ...]:
    """The outcomes the observing capability's QUERY operation declares, as the snapshot states them.

    Observed through the inspector, the only way this package reads a composition. Fail-hard when
    the capability or the operation is absent: a generator that fell back to a remembered list would
    be the copy this replaces.
    """
    status, result = inspector_api.query(QUERY_OUTCOMES_OBSERVATION, {}, str(snapshot_root))
    if status != "SUCCESS":
        raise SystemExit(f"{QUERY_OUTCOMES_OBSERVATION} failed against {snapshot_root}: {status}")
    capability = next((c for c in result.get("capabilities", [])
                       if c.get("capability") == QUERY_CAPABILITY), None)
    operation = ((capability or {}).get("operations") or {}).get(QUERY_OPERATION)
    outcomes = (operation or {}).get("result_status_values")
    if not outcomes:
        raise SystemExit(f"{snapshot_root} declares no outcomes for {QUERY_CAPABILITY} "
                         f"{QUERY_OPERATION}; the observing steps have nothing to answer")
    return tuple(outcomes)

# Where a phase workflow sends every judging outcome but SUCCESS. A phase either judged the document
# or did not, and the workflow has one ending for each. Routing is generated from the contract's
# declared outcomes, so an outcome a contract gains is routed the moment it is declared, rather
# than left for someone to notice (Open PGC Standard `v1` GC-15).
REJECTED_ENDING = "EXIT_REJECTED"

PROVENANCE_HEADING = "## Generated Artifact"

# The section is placed where a reader meets the artifact, before its narrative begins. Every one of
# these workflows opens the same way, and an anchor that is not there is fail-hard rather than a
# section quietly appended somewhere nobody looks.
PROVENANCE_ANCHOR = "## 1. Intent"


def observations() -> dict[str, str]:
    """Every observation any phase declares, as `key -> the field its result carries`.

    The union across phases, because one contract judges all of them and its pipeline observes the
    same operations whatever phase invoked it. A phase that does not read a key is handed it and
    ignores it, which costs nothing; a phase that reads a key nobody passed is the defect this
    exists to prevent.
    """
    from transformation.design.rule_sets import RULE_SETS

    out: dict[str, str] = {}
    for phase in RULE_SETS.values():
        for key, field in phase.observations.items():
            out[key] = field
    return dict(sorted(out.items()))


def observing_steps(text: str) -> dict[str, str]:
    """`operation -> the step that performs it`, read out of the contract's own pipeline.

    Derived rather than declared here. Which step observes which operation is a fact the contract
    already states, and restating it would create the second copy this whole change is removing.
    """
    steps: dict[str, str] = {}
    current = ""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- step: "):
            current = stripped[len("- step: "):].strip()
        elif stripped.startswith("operation: ") and current:
            steps[stripped[len("operation: "):].strip()] = current
    return steps


def render_observed(text: str) -> str:
    """The `observed` map as the contract carries it, one line per declared observation."""
    steps = observing_steps(text)
    pad = " " * OBSERVED_INDENT
    lines = [f"{pad}observed:\n"]
    for key, field in observations().items():
        operation = key.split("#", 1)[0]
        step = steps.get(operation)
        if step is None:
            raise SystemExit(
                f"{JUDGE_CONTRACT} observes no {operation!r}, which a phase declares it reads. "
                f"A key nobody produces is a rule that cannot see its subject"
            )
        lines.append(f"{pad}  {key}: $.results.{step}.capability_result.result.{field}\n")
    return "".join(lines)


def step_name(operation: str) -> str:
    """The step that performs an operation, named from the operation itself.

    Derived so that adding an observation is one line in a phase's rule module. Naming the step by
    hand would put the operation in the declaration and the step in the contract, which is the pair
    that has to be kept in step — the same pair the `observed` map was generated to stop copying.
    """
    return "observe_" + operation.split("#", 1)[0].replace("si.", "", 1).replace(".", "_")


def render_observing_step(operation: str, outcomes: tuple[str, ...]) -> str:
    """One pipeline step asking the bound snapshot capability one question.

    The step is the last hand-kept copy of a declaration that already lives in a phase's rule
    module. Generated, an observation a phase declares reaches the rules that read it; hand-written,
    the emission could only report that it was missing — which it did, correctly, and then left
    somebody to write the step themselves.
    """
    return (
        f"  - step: {step_name(operation)}\n"
        f"    side_effect: {QUERY_CAPABILITY}\n"
        f"    op: {QUERY_OPERATION}\n"
        f"    inputs:\n"
        f"      operation: {operation}\n"
        f"      params: {{}}\n"
        f"    outputs: {{}}\n"
        + render_query_answers(outcomes)
    )


def render_query_answers(outcomes: tuple[str, ...]) -> str:
    """An observing step's `result_surface` and `on_result`: every QUERY outcome, each answered.

    SUCCESS continues to the next step. Every other outcome ends the contract with it, so the
    workflow decides what follows rather than the step carrying on past an observation it never got.
    """
    surface = "".join(f"    - {o}\n" for o in outcomes)
    answers = "".join(f"      {o}: {'continue' if o == 'SUCCESS' else 'exit'}\n" for o in outcomes)
    return f"    result_surface:\n{surface}    on_result:\n{answers}"


def splice_query_answers(text: str, outcomes: tuple[str, ...]) -> str:
    """Bring every observing step's answers into agreement with what the capability declares.

    Only the two keys are rewritten. A step's comments, inputs and name are the contract's own, and
    regenerating the whole step would discard what a reviewer wrote above it.
    """
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i, observing = 0, False
    while i < len(lines):
        line = lines[i]
        bare = line.rstrip("\n")
        if bare.startswith("  - step: "):
            observing = False
        elif bare == f"    side_effect: {QUERY_CAPABILITY}":
            observing = True
        if observing and bare == "    result_surface:":
            j = i + 1
            while j < len(lines) and lines[j].startswith("    - "):
                j += 1
            if j >= len(lines) or lines[j].rstrip("\n") != "    on_result:":
                raise SystemExit(f"an observing step's result_surface is not followed by on_result "
                                 f"at line {j + 1}")
            j += 1
            while j < len(lines) and lines[j].startswith("      ") and lines[j].strip():
                j += 1
            out.append(render_query_answers(outcomes))
            i, observing = j, False
            continue
        out.append(line)
        i += 1
    return "".join(out)


def machine(text: str) -> dict:
    """The artifact's `Machine` block, parsed."""
    block = machine_yaml(text)
    if block is None:
        raise SystemExit("expected a ```yaml Machine block")
    return yaml.safe_load(block)


def splice_allowed(text: str) -> str:
    """Declare every outcome the contract's steps can end it with, appending only what is missing.

    A contract states how it can end. A step that exits with an outcome the contract does not
    declare is a way to end that nobody routes, so the declaration follows the steps.
    """
    core = machine(text)["core"]
    allowed = list(core["result_status_contract"]["allowed"])
    exits = [code for step in core["pipeline"]
             for code, act in (step.get("on_result") or {}).items() if act == "exit"]
    missing = [code for code in dict.fromkeys(exits) if code not in allowed]
    if not missing:
        return text
    lines = text.splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if line.rstrip("\n") == "    allowed:"]
    if len(starts) != 1:
        raise SystemExit(f"expected exactly one '    allowed:' line, found {len(starts)}")
    end = starts[0] + 1
    while end < len(lines) and lines[end].startswith("    - "):
        end += 1
    return "".join(lines[:end]) + "".join(f"    - {code}\n" for code in missing) + "".join(lines[end:])


def judge_node(text: str) -> str:
    """The workflow's judging node: the one CC node every phase workflow has."""
    nodes = machine(text)["core"]["nodes"]
    judges = [key for key, node in nodes.items() if node.get("type") == "CC"]
    if len(judges) != 1:
        raise SystemExit(f"expected exactly one judging node, found {judges}")
    return judges[0]


def judge_contract(text: str) -> str:
    """The contract the judging node runs: its `code`, which a re-point moves while the place keeps
    its label. Read by label, a workflow re-pointed to a successor would be routed by the contract it
    no longer runs."""
    node = judge_node(text)
    return machine(text)["core"]["nodes"][node].get("code") or node


def splice_routing(text: str, allowed: list[str]) -> str:
    """Route every outcome the judging contract declares, appending only what is missing.

    SUCCESS keeps the ending the workflow already names; every other outcome is routed to
    `REJECTED_ENDING`. A route for an outcome the contract does not declare is refused, because it
    names a way to end that cannot happen and hides which ones can.
    """
    node = judge_node(text)
    lines = text.splitlines(keepends=True)
    heads = [i for i, line in enumerate(lines) if line.rstrip("\n") == f"    {node}:"]
    if len(heads) != 1:
        raise SystemExit(f"expected exactly one '    {node}:' line, found {len(heads)}")
    nxt = next((i for i in range(heads[0] + 1, len(lines))
                if lines[i].rstrip("\n") == "      next:"), None)
    if nxt is None:
        raise SystemExit(f"{node} declares no next:")
    end = nxt + 1
    while end < len(lines) and lines[end].startswith("        ") and lines[end].strip():
        end += 1
    routed = [line.strip().split(":", 1)[0] for line in lines[nxt + 1:end]]
    stray = [code for code in routed if code not in allowed]
    if stray or "SUCCESS" not in routed:
        raise SystemExit(f"{node} routes {stray or 'no SUCCESS'}; the contract declares {allowed}")
    missing = [code for code in allowed if code not in routed]
    return "".join(lines[:end]) + "".join(f"        {code}: {REJECTED_ENDING}\n" for code in missing) \
        + "".join(lines[end:])


def splice_observing_steps(text: str, outcomes: tuple[str, ...]) -> str:
    """Place a step for every declared observation the contract does not already perform.

    Inserted before the step that reads them, because the runtime chains by result and a step
    consuming an observation produced after it reads nothing. Only the missing ones are written: a
    step already there is the contract's own, and regenerating it would discard whatever a reviewer
    put in its comments.
    """
    have = observing_steps(text)
    missing = [op for op in sorted({k.split("#", 1)[0] for k in observations()})
               if op not in have]
    if not missing:
        return text
    lines = text.splitlines(keepends=True)
    anchor = [i for i, line in enumerate(lines)
              if line.rstrip("\n") == f"  - step: {OBSERVATION_CONSUMER}"]
    if len(anchor) != 1:
        raise SystemExit(
            f"expected exactly one {OBSERVATION_CONSUMER!r} step in {JUDGE_CONTRACT} to place an "
            f"observing step before, found {len(anchor)}"
        )
    at = anchor[0]
    return "".join(lines[:at]) + "".join(render_observing_step(op, outcomes) for op in missing) \
        + "".join(lines[at:])


def splice_observed(text: str, rendered: str) -> str:
    """Replace the `observed:` block, leaving the rest of the contract untouched."""
    lines = text.splitlines(keepends=True)
    key = " " * OBSERVED_INDENT + "observed:"
    starts = [i for i, line in enumerate(lines) if line.rstrip("\n") == key]
    if len(starts) != 1:
        raise SystemExit(f"expected exactly one {key!r} line, found {len(starts)}")
    start = starts[0]

    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].lstrip()
        if not stripped:
            continue
        if len(lines[i]) - len(stripped) <= OBSERVED_INDENT:
            end = i
            break
    return "".join(lines[:start]) + rendered + "".join(lines[end:])


@dataclass(frozen=True)
class Emission:
    """What one workflow's generation produced, and whether it had drifted."""

    phase: str
    filename: str
    rules: int
    drifted: bool
    # Why the phase's rules may not be sealed: they changed without a recorded revision.
    unrecorded: str | None = None


def sources(phase_id: str) -> list[str]:
    """Everything the emission reads for one phase, as repo-relative paths.

    The register schema declares the registers and their columns, the vocabulary declaration the
    values its columns admit. Together they are the generator, so
    all are named, and a change to any is a change to it.
    """
    from transformation.design.catalog import phase as phase_spec
    from transformation.design.schema import SCHEMAS, load

    out = [str((SCHEMAS / phase_spec(phase_id).schema).relative_to(REPO))]
    vocabularies = sorted({v["artifact"] for r in load(phase_id).registers for v in _vocab_refs(phase_id, r.id)})
    for artifact in vocabularies:
        out.append(str(_declaration_path(artifact).relative_to(REPO)))
    # The judging contract's declared outcomes are what the workflow's routing is generated from.
    contract = judge_contract((WORKFLOWS / SEALED_IN[phase_id]).read_text(encoding="utf-8"))
    out.append(str((CONTRACTS / f"{contract}.md").relative_to(REPO)))
    return out


def _vocab_refs(phase_id: str, register_id: str) -> list[dict]:
    """The vocabulary references one register's columns make, as its schema writes them."""
    import json

    from transformation.design.catalog import phase as phase_spec
    from transformation.design.schema import SCHEMAS

    declared = json.loads((SCHEMAS / phase_spec(phase_id).schema).read_text(encoding="utf-8"))
    body = declared["properties"]["registers"]["properties"][register_id]
    columns = (body.get("items") or {}).get("properties") or {}
    return [c["x-vocab"] for c in columns.values() if "x-vocab" in c]


def _declaration_path(artifact: str) -> Path:
    from transformation.design.schema import REGISTRY

    return sorted(REGISTRY.rglob(f"{artifact.split('::')[-1]}.md"))[0]


def declared(phase_id: str) -> list[dict]:
    """A phase's rule set as the plain data a workflow seals.

    Both locators are emitted when a rule declares a register. `section_title` alone unbinds a
    derived rule from the register it was derived for, and `register` alone loses the fallback P0
    depends on — the failure mode is a rule that resolves to nothing and passes silently.
    """
    from transformation.design.rule_sets import RULE_SETS

    out = []
    for rule in RULE_SETS[phase_id].rule_set():
        entry: dict = {"id": rule.id, "identity": rule.identity, "check": rule.check}
        if rule.register:
            entry["register"] = rule.register
        if rule.section_title and rule.section_title != rule.register:
            entry["section_title"] = rule.section_title
        if rule.params:
            entry["params"] = rule.params
        if rule.intent:
            entry["intent"] = rule.intent
        out.append(entry)
    return out


def render(rules: list[dict]) -> str:
    """The rule set as it appears inside the workflow's `Machine` block.

    Dumped with aliases left on: several phases repeat one large `known_registers` list across
    dozens of rules, and expanding it every time would bury the declaration in its own boilerplate.
    """
    body = yaml.dump(rules, sort_keys=False, width=100, allow_unicode=True, default_flow_style=False)
    pad = " " * RULE_SET_INDENT
    return "".join(f"{pad}{line}\n" if line.strip() else "\n" for line in body.splitlines())


def splice(text: str, rendered: str) -> str:
    """Replace the `rule_set:` block in a workflow artifact, leaving everything else untouched.

    The block runs from its key to the next line indented shallower than the key — the node's
    `next:` routing. Rewriting the whole YAML document instead would reformat hand-written
    structure and strip the comments that explain it.
    """
    lines = text.splitlines(keepends=True)
    key = " " * RULE_SET_INDENT + "rule_set:"
    starts = [i for i, line in enumerate(lines) if line.rstrip("\n") == key]
    if len(starts) != 1:
        raise SystemExit(f"expected exactly one {key!r} line, found {len(starts)}")
    start = starts[0]

    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].lstrip()
        if not stripped:
            continue
        if len(lines[i]) - len(stripped) < RULE_SET_INDENT:
            end = i
            break

    return "".join(lines[:start + 1]) + rendered + "".join(lines[end:])


def provenance(phase_id: str) -> str:
    """What the artifact says about how it was reached.

    Prose, deliberately: the compiler reads the `## Machine` block and nothing else, so this states
    the fact to the person who opens the file and to the review that would otherwise have to take
    the generator's word for it. It is emitted rather than typed for the same reason the rule set
    is — a hand-written provenance is a third copy, and the one nobody regenerates.
    """
    listed = "\n".join(f"  - `{path}`" for path in sources(phase_id))
    return (
        f"{PROVENANCE_HEADING}\n"
        "\n"
        "This artifact is generated. The rule set in its `Machine` block is a **sealed copy**, and\n"
        "the copy is never corrected directly: where this artifact and its generator disagree, this\n"
        "artifact is stale, and an edit here lasts until whoever next runs the emission.\n"
        "\n"
        f"- **Generator:** `{GENERATOR}`\n"
        "- **Generator sources** — one generator together, never separately:\n"
        f"{listed}\n"
        "\n"
        "To change what this phase judges, amend a source and invoke the generator.\n"
        "`tc phase emit --check` refuses a build in which the two disagree.\n"
        "\n"
        "---\n"
        "\n"
    )


def splice_provenance(text: str, block: str) -> str:
    """Place the provenance section, replacing any the artifact already carries.

    Replacing rather than appending is what keeps this idempotent — an emission that added a second
    section every run would produce exactly the two-statements-of-one-truth this section exists to
    refuse.
    """
    lines = text.splitlines(keepends=True)
    heads = [i for i, line in enumerate(lines) if line.rstrip("\n") == PROVENANCE_HEADING]

    if heads:
        start = heads[0]
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        return "".join(lines[:start]) + block + "".join(lines[end:])

    anchors = [i for i, line in enumerate(lines) if line.rstrip("\n") == PROVENANCE_ANCHOR]
    if not anchors:
        raise SystemExit(f"expected {PROVENANCE_ANCHOR!r} to place the provenance section before")
    at = anchors[0]
    return "".join(lines[:at]) + block + "".join(lines[at:])


def emit_contract(relative: str, outcomes: tuple[str, ...],
                  check_only: bool = False) -> tuple[Emission, str]:
    """Bring one judging contract into agreement with what the phases and the capability declare.

    The `observed` map is generated for the same reason the rule sets are: it is a copy of a
    declaration that lives elsewhere, and the two drifted the moment anyone added an observation.
    Generated, adding one to a phase is enough — and an observation no step produces is a build
    failure rather than a rule that silently sees nothing. Only the snapshot judge takes the map.

    Every judge has its observing steps' answers brought into agreement with `outcomes`, and
    its declared outcomes with what those steps can end it with. Returns the contract as emitted, so
    the workflows' routing is generated from what the contract now declares, written or not.
    """
    path = REPO / relative
    current = path.read_text(encoding="utf-8")
    updated = current
    if relative == JUDGE_CONTRACT:
        stepped = splice_observing_steps(updated, outcomes)
        updated = splice_observed(stepped, render_observed(stepped))
    updated = splice_allowed(splice_query_answers(updated, outcomes))
    drifted = updated != current
    if drifted and not check_only:
        path.write_text(updated, encoding="utf-8")
    rules = len(observations()) if relative == JUDGE_CONTRACT else 0
    return Emission(phase="cc", filename=pathlib.Path(relative).name,
                    rules=rules, drifted=drifted), updated


def emit(snapshot_root: str | Path, check_only: bool = False,
         texts: dict[str, str] | None = None) -> list[Emission]:
    """Bring every judging contract, then every phase workflow, into agreement with its sources.

    Contracts first: a workflow's routing is generated from its judging contract's declared outcomes,
    so the contract must already say what it can end with. Under `check_only` nothing is written and
    the drift is reported instead, which is what a build gate needs: the question "does the
    composition already agree with its generator" has to be answerable without changing the answer.

    `texts`, when given, receives each artifact as the generator determines it, by code, so a
    caller can compare it with the composition before anything is written.
    """
    out: list[Emission] = []
    contracts: dict[str, str] = {}
    outcomes = query_outcomes(snapshot_root)
    for relative in JUDGE_CONTRACTS:
        emission, text = emit_contract(relative, outcomes, check_only)
        contracts[pathlib.Path(relative).stem] = text
        if texts is not None:
            texts[pathlib.Path(relative).stem] = text
        out.append(emission)
    from transformation.design.effectivity import unrecorded
    from transformation.design.rule_sets import RULE_SETS

    for phase_id, filename in SEALED_IN.items():
        path = WORKFLOWS / filename
        phase = RULE_SETS[phase_id]
        # A rule set changed without declaring its effectivity is not sealed: the workflow would
        # carry rules no revision accounts for, and a verdict could not say what judged it.
        refused = unrecorded(phase.shape, phase.rule_set())
        rules = declared(phase_id)
        current = path.read_text(encoding="utf-8")
        code = judge_contract(current)
        contract = contracts.get(code) or (CONTRACTS / f"{code}.md").read_text(encoding="utf-8")
        allowed = list(machine(contract)["core"]["result_status_contract"]["allowed"])
        updated = splice_provenance(splice_routing(splice(current, render(rules)), allowed),
                                    provenance(phase_id))
        drifted = updated != current
        if drifted and not check_only and refused is None:
            path.write_text(updated, encoding="utf-8")
        if texts is not None:
            texts[filename[:-len(".md")]] = updated
        out.append(Emission(phase=phase_id, filename=filename, rules=len(rules), drifted=drifted,
                            unrecorded=refused))
    return out


def preview(snapshot_root: str | Path) -> dict[str, str]:
    """Every artifact this generator produces, as it would write it, by code. Writes nothing."""
    texts: dict[str, str] = {}
    emit(snapshot_root, check_only=True, texts=texts)
    return texts


def emit_rule_sets(snapshot_root: str | Path) -> list[Emission]:
    """The generator, as a design names it and as construction invokes it."""
    return emit(snapshot_root, check_only=False)


def check(snapshot_root: str | Path) -> list[Emission]:
    """Every workflow that does not agree with its generator. Empty is the only passing answer."""
    return [e for e in emit(snapshot_root, check_only=True) if e.drifted]
