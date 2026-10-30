"""The four annotation constructs: `x-key`, `x-reference`, `x-carriage` and `x-grounding` (DESIGN_LANGUAGE §5)."""

from __future__ import annotations

import re
from typing import Any

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _cited,
    _content_rows,
    _items,
    _normalise,
    _rows,
    _value,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


def _present(row: dict, column: str) -> bool:
    """Whether a cell states a value: neither blank nor `null`."""
    return bool(_cell(row, column))


# Observation-aware checks ------------------------------------------------------------------
#
# These read `doc.observed` — facts gathered from the assembled composition through the governed
# inspection capability and handed to the evaluator as declared input. They are the only checks
# that can be wrong for a reason outside the document: a citation is a claim about the world, and
# checking it needs the world.


def _observed_identities(doc: ParsedDocument, operation: str) -> set[str]:
    """Artifact identities from an observation, however the inspection surface shaped them.

    `si.artifact.list` answers with rows, not bare identities; other operations may answer with
    plain strings. Normalising here keeps the shape of an inspection result out of the rule
    declaration, which should say *what* is checked rather than how the surface happens to reply.
    """
    out: set[str] = set()
    for entry in doc.observed.get(operation, []) or []:
        if isinstance(entry, str):
            out.add(entry)
        elif isinstance(entry, dict):
            value = entry.get("artifact") or entry.get("fqdn") or entry.get("fqdn_id")
            if value:
                out.add(str(value))
    return out


@check("CITED_ARTIFACTS_RESOLVE")
def _cited_artifacts_resolve(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Classify every cited artifact identity against the observed baseline, and report only defects.

    Field manual §4.7, Identity-Preserving Taxonomy — every reference resolves to one of:

        A  exact          the identity is in the baseline
        B  typo-alias     a near-match exists; the citation is misspelled
        C  wrong-domain   the code exists, under a different namespace
        D  proposed-new   well-formed, absent from the baseline — legitimate new design
        E  fabrication    no identity anywhere

    Only B, C and E are defects. **A count of not-found citations is inadmissible evidence**: it
    over-flags D, and D is what every CR that designs anything is full of. An earlier version of
    this check did exactly that — it would have rejected a correct dossier for proposing new work.

    D and E are not separable from the document alone; telling them apart needs the CR's declared
    new artifacts, which arrive at P7. Until then both are left unflagged rather than guessed,
    because guessing here reintroduces the over-flagging the taxonomy exists to prevent.
    """
    known = _observed_identities(doc, rule.params["observation"])
    if not known:
        return [(
            _at(_where(rule)),
            "no composition was observed — citations cannot be resolved, so this register's "
            "grounding is unchecked",
        )]

    # Index the baseline by bare code, so a right-code/wrong-namespace citation is recognisable.
    by_code: dict[str, list[str]] = {}
    for fqdn in known:
        by_code.setdefault(fqdn.split("::")[-1], []).append(fqdn)

    out = []
    column = rule.params["column"]
    gate_column = rule.params.get("only_when_column")
    gate_value = rule.params.get("only_when_value")
    pattern = re.compile(rule.params["pattern"])

    for i, row in _rows(doc, rule):
        if gate_column and _cell(row, gate_column).upper() != gate_value:
            continue
        cited = pattern.findall(_cell(row, column))
        if not cited and rule.params.get("detail_missing"):
            out.append((_at(_where(rule), i), rule.params["detail_missing"]))
            continue

        for fqdn in cited:
            if fqdn in known:
                continue                                        # A — exact
            code = fqdn.split("::")[-1]
            if code in by_code:                                 # C — wrong domain
                out.append((
                    _at(_where(rule), i),
                    f"{fqdn!r} names a code that exists elsewhere: {sorted(by_code[code])} — "
                    f"wrong namespace, not a new artifact",
                ))
                continue
            near = [k for k in by_code if _is_near(code, k)]
            if near:                                            # B — typo alias
                out.append((
                    _at(_where(rule), i),
                    f"{fqdn!r} closely resembles {sorted(near)[:3]} — likely a misspelled citation",
                ))
            # D / E — indistinguishable without the CR's proposed set; not flagged.
    return out


def _is_near(a: str, b: str) -> bool:
    """Cheap single-edit proximity — enough to catch a misspelling, not enough to over-match."""
    if a == b or abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    short, long = (a, b) if len(a) < len(b) else (b, a)
    for i in range(len(long)):
        if long[:i] + long[i + 1:] == short:
            return True
    return False


@check("REUSE_CANDIDATE_ELIGIBLE")
def _reuse_candidate_eligible(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Every artifact offered as a reuse candidate must come from a domain that permits it.

    A domain declares which plane it serves; the declaration bounds the *search space* and never
    makes the *decision*. So this check answers one question only — may this domain's artifacts be
    offered at all — and says nothing about whether reusing any particular one is wise. That call
    stays with the author, per artifact, against evidence.

    Two ways to fail, and the second matters more than it looks:

    - the cited domain declares a visibility this CR may not draw on
    - the cited domain declares **no** visibility at all

    The second is a hard failure rather than a permissive default. Nothing yet stops a domain from
    compiling without the declaration, so absence would otherwise mean "search everything" — the
    inference the declaration exists to prevent, arriving silently through the back door.

    One domain is always eligible when the rule declares `own_domain`: the domain the change is to.
    Its artifacts are its own to change, so reusing one couples the change to no other owner's
    surface. A change to a platform domain may then reuse that domain's own artifacts, whatever
    plane the domain serves.
    """
    observation = rule.params["observation"]
    eligible = set(rule.params["eligible"])
    own = doc.header.get("domain") if rule.params.get("own_domain") else None
    pattern = re.compile(rule.params["pattern"])

    # The observation is scope → visibility. Scope, not domain: substrate layers declare a
    # visibility but are not composed domains, so a domain-keyed answer would omit exactly the
    # artifacts a business change request most legitimately reuses.
    declared: dict[str, Any] = dict(doc.observed.get(observation, {}) or {})

    # A cited identity names a *namespace*; the domain that owns it is what declares visibility.
    # They coincide for a business domain and diverge for the platform, whose namespaces are
    # federation boundaries — so an unknown namespace is resolved through the observation, never
    # by splitting the string and hoping.
    out = []
    for i, row in _rows(doc, rule):
        value = _cell(row, rule.params["column"])
        for identity in pattern.findall(value):
            namespace = identity.split("::")[0]
            domain = namespace if namespace in declared else _owning_domain(doc, rule, identity)
            if domain is None:
                continue                          # not in the baseline: proposed-new, not a reuse
            if domain == own:
                continue                          # the change's own domain: its artifacts are its own
            visibility = declared.get(domain)
            if visibility is None:
                out.append((
                    _at(_where(rule), i),
                    f"{identity!r} belongs to domain {domain!r}, which declares no reuse "
                    f"visibility — eligibility would have to be inferred, and inferring "
                    f"relevance is reserved to the author",
                ))
            elif visibility not in eligible:
                out.append((
                    _at(_where(rule), i),
                    f"{identity!r} belongs to domain {domain!r}, declared {visibility!r} — "
                    f"not offerable to this change request "
                    f"(eligible: {', '.join(sorted(eligible))})",
                ))
    return out


def _owning_domain(doc: ParsedDocument, rule, identity: str) -> str | None:
    """The domain that owns a cited identity, from the artifact observation."""
    for entry in doc.observed.get(rule.params["artifact_observation"], []) or []:
        if isinstance(entry, dict) and entry.get("artifact") == identity:
            return entry.get("domain")
    return None


@check("CELL_RESOLVES_IN_REGISTER")
def _cell_resolves_in_register(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A value in one register must name a row that really exists in another.

    The first check that reads two registers at once. Earlier phases judge each register on its own
    terms, because discovery has nothing to be consistent *with* yet. A consolidation phase is
    different: its whole job is that the registers agree, so an entry pointing at a gap nobody
    declared is exactly the defect it exists to catch — and one no single-register rule can see.

    Absence of the cell is not this rule's business; a blank is `CELL_NOT_EMPTY`'s finding, and
    reporting it twice would make one defect look like two.

    `exempt_prefixes` names values that are terminals by construction rather than identities. A
    workflow's topology legitimately routes to `EXIT_REJECTED`, which is a graph terminal and never
    an artifact — the rule had simply never met one, because CR-1 declared no EXIT rows until its
    topology was completed.
    """
    # One target register, or several: a code may legitimately be declared new here OR carried over
    # from the existing inventory, and a rule naming only one of those would reject the other.
    targets = rule.params.get("target_registers") or [rule.params["target_register"]]
    target_column = rule.params["target_column"]
    target_columns = rule.params.get("target_columns") or [target_column] * len(targets)

    # A gate on the target rows, for a value that must name a row of one kind rather than any row:
    # a molecule's steps belong to a transform declared a molecule, and an atom of the same register
    # answering for it would let an atom own a stream it can never run.
    target_gate_column = rule.params.get("target_only_when_column")
    target_gate_value = rule.params.get("target_only_when_value")

    known: set[str] = set()
    for register, column in zip(targets, target_columns):
        block = doc.register(register)
        if block is None or block.table is None:
            continue
        for row in block.table.rows:
            if target_gate_column and _value(row, target_gate_column) != target_gate_value:
                continue
            known.update(_items(row, column))
    target = " or ".join(targets)
    exempt = tuple(rule.params.get("exempt_prefixes") or ())

    only_when_column = rule.params.get("only_when_column")
    only_when_value = rule.params.get("only_when_value")
    # A register may key its rows by a *family* of values rather than one. `artifact_properties`
    # holds every scalar an artifact declares and an emission is `emit.<ending>` — one property per
    # ending, so there is no single value to match on and an equality gate cannot select them. The
    # prefix is what they have in common, and it is what the register names them by.
    only_when_prefix = rule.params.get("only_when_prefix")
    out = []
    for i, row in _rows(doc, rule):
        if only_when_column:
            gate = _value(row, only_when_column)
            if only_when_prefix:
                if not isinstance(gate, str) or not gate.strip().startswith(only_when_prefix):
                    continue
            elif gate != only_when_value:
                continue
        # A row may name what it resolves to in a second column that overrides the first when
        # filled: a keyed topology node is a place, and the contract it runs is in `Runs`. A cell
        # stating nothing names nothing, and a list names each of its entries.
        prefer = rule.params.get("prefer_column")
        parts = (prefer and _items(row, prefer)) or _items(row, rule.params["column"])
        for part in parts:
            if exempt and part.startswith(exempt):
                continue
            if part not in known:
                detail = rule.params.get(
                    "detail", "a document may only point at what it declared"
                )
                out.append((
                    _at(_where(rule), i),
                    f"{part!r} names no row in {target}.{target_column} — {detail}",
                ))
    return out


@check("CITED_ARTIFACTS_ABSENT")
def _cited_artifacts_absent(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """An identity claimed as NEW must not already be in the composition.

    The inverse of `CITED_ARTIFACTS_RESOLVE`, and the only rule in the pipeline that reads a
    successful resolution as the defect. Every phase before this one cites what exists; the design
    phase assigns identities that will exist, and an assignment that collides with something
    already there is not a new artifact — it is a silent redefinition of an old one.

    Reported per identity, because a designer needs to know which name to change, not that one of
    them was taken.
    """
    observation = rule.params["observation"]
    pattern = re.compile(rule.params["pattern"])
    observed = _observed_identities(doc, observation)

    if not observed:
        return [(
            _at(_where(rule)),
            "no composition was observed — a collision check that cannot see the baseline would "
            "admit every colliding name",
        )]

    out = []
    for i, row in _rows(doc, rule):
        value = _cell(row, rule.params["column"])
        for identity in pattern.findall(value):
            if identity in observed:
                out.append((
                    _at(_where(rule), i),
                    f"{identity!r} already exists in the composition — assigning it here would "
                    f"redefine an artifact rather than create one",
                ))
    return out


@check("COLUMN_SEQUENCE_CONTIGUOUS")
def _column_sequence_contiguous(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """An integer column must run contiguously from a declared start.

    The first rule about a register's rows *as a sequence* rather than each row on its own. Every
    row can be individually perfect and the register still wrong: a gap in a build sequence means an
    artifact was dropped between two steps that both look fine, and nothing reading rows one at a
    time would notice the absence.
    """
    column = rule.params["column"]
    start = int(rule.params.get("start", 1))

    seen: list[tuple[int, int]] = []
    for i, row in _rows(doc, rule):
        value = _cell(row, column)
        if not value:
            continue
        try:
            seen.append((int(value), i))
        except ValueError:
            return [(_at(_where(rule), i), f"{value!r} is not a step number")]

    if not seen:
        return []

    out = []
    expected = start
    for number, i in sorted(seen):
        if number != expected:
            out.append((
                _at(_where(rule), i),
                f"step {number} follows {expected - 1} — the sequence skips {expected}, "
                f"and a gap is an artifact silently dropped",
            ))
            expected = number
        expected += 1
    duplicates = len(seen) - len({n for n, _ in seen})
    if duplicates:
        out.append((_at(_where(rule)), f"{duplicates} duplicate step number(s) — order must be total"))
    return out


# Cross-phase checks -------------------------------------------------------------------------
#
# These read `doc.priors` — the upstream phase documents this one was handed. Every check above
# judges one document, which is sufficient while a defect lives inside it. It stops being
# sufficient at a handoff: nine phases pass work forward through `gov_projection`, and a phase that
# quietly drops an upstream commitment is well formed in isolation and wrong as a pipeline.
#
# The defect is only visible with both documents open, which is what makes these a different rule
# form rather than another register rule. They carry no phase names — which phase reads which is
# declared in that phase's rule set, exactly as an observation is.


def _prior_rows(doc: ParsedDocument, rule):
    """Content rows of the upstream register a cross-phase rule reads.

    Returns `(rows, unavailable)`. `unavailable` distinguishes the two ways a prior register can be
    absent, because they blame different people: a prior nobody supplied is the driver's omission,
    a register missing from a supplied prior is the upstream author's. Collapsing them would report
    a document defect for a missing command-line argument.
    """
    phase = rule.params["prior_phase"]
    register = rule.params["prior_register"]

    if not doc.has_prior(phase):
        return [], (
            f"{phase} was not supplied — this handoff is unchecked, and an unchecked handoff "
            f"looks identical to a preserved one"
        )
    block = doc.prior_register(phase, register)
    if block is None or block.table is None:
        return [], f"{phase} carries no readable {register!r} register to preserve"
    return _content_rows(block), None


@check("PRIOR_PROSE_CARRIED")
def _prior_prose_carried(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A narrative register carried from an upstream phase, inherited or explicitly superseded.

    Preservation elsewhere is row-keyed, and a paragraph has no key. That is why the one register
    the pipeline could never derive — the subdomain purpose, human-authored once at P0 — was the
    one thing it dropped: P1 through P4 have nowhere to put it, and P5 wrote a fresh paragraph in
    its place. A second author's paragraph is not the business's statement, and nothing recorded
    that the substitution had happened.

    The register itself declares which it is. `INHERITED` means the prose is the prior's, and the
    two must match once whitespace is normalised. `REFINED` means this phase deliberately says more,
    and must state what it added — a disposition that permitted silence would be indistinguishable
    from the loss it exists to prevent.
    """
    phase = rule.params["prior_phase"]
    prior_register = rule.params["prior_register"]
    inherited = str(rule.params.get("inherited_value", "INHERITED")).upper()

    if not doc.has_prior(phase):
        return [(
            _at(_where(rule)),
            f"{phase} was not supplied — this handoff is unchecked, and an unchecked handoff "
            f"looks identical to a preserved one",
        )]
    prior = doc.prior_register(phase, prior_register)
    if prior is None:
        return [(_at(_where(rule)), f"{phase} carries no {prior_register!r} register to carry forward")]

    rows = _rows(doc, rule)
    if not rows:
        return [(_at(_where(rule)), "no disposition declared — say whether the prose is inherited or refined")]

    out = []
    column = rule.params["column"]
    carried = doc.register(rule.params["prose_register"])
    for i, row in rows:
        if _cell(row, column).strip().upper() != inherited:
            continue
        if carried is None:
            out.append((_at(_where(rule), i), "the register it declares a disposition for is absent"))
            continue
        if _normalise(carried.text()) != _normalise(prior.text()):
            out.append((_at(_where(rule), i), rule.params["detail"]))
    return out


def _cited_ordinals(row: dict, column: str, register: str) -> set[int]:
    """Every row of `register` a citation cell names by ordinal.

    A register id is unique across the pipeline, so the id alone identifies the upstream register
    and the phase a citation names beside it is redundant for matching.
    """
    return {c["row"] for c in _cited(row, column) if c.get("register") == register and "row" in c}


def _key_columns(declared: str | list[str]) -> list[str]:
    """A key column declaration, as a list.

    Some registers are keyed by one column and some by several: an acceptance criterion is unique on
    its own text, while a lifecycle state is unique only as `Object` + `State` — `Registered` appears
    once per object. Declaring a single column for those would compare a book's row against a copy's
    and call a dropped row present.
    """
    return [declared] if isinstance(declared, str) else list(declared)


def _claim(row: dict, columns: list[str]) -> str:
    """What a row asserts, as one comparable string across its key columns."""
    return " · ".join(_normalise(_cell(row, c)) for c in columns)


@check("PRIOR_ROWS_CITED")
def _prior_rows_cited(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Every row of an upstream register must be carried forward and cited here.

    Belief Preservation, stated as k of N: N rows were committed to upstream, k of them are cited
    downstream, and the rule is that k equals N. A belief nobody carried is not resolved — it is
    forgotten, and the dossier reports ADMISSIBLE over a question the change never answered.

    Reported per dropped row rather than as a count, because an author needs to know which
    commitment went missing, not how many did.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_at(_where(rule)), unavailable)]

    register = rule.params["prior_register"]
    phase = rule.params["prior_phase"]
    column = rule.params["citation_column"]
    key_column = rule.params.get("prior_key_column")

    cited: set[int] = set()
    for _, row in _rows(doc, rule):
        cited |= _cited_ordinals(row, column, register)

    out = []
    total = len(prior_rows)
    for ordinal, row in prior_rows:
        if ordinal in cited:
            continue
        subject = _normalise(_cell(row, key_column)) if key_column else ""
        out.append((
            _at(_where(rule)),
            f"{phase} {register} #{ordinal} of {total} is carried nowhere in this register"
            + (f": {subject!r}" if subject else ""),
        ))
    return out


@check("PRIOR_ROW_MATCHES_CITED")
def _prior_row_matches_cited(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A row that cites an upstream row must still say what that row said.

    Projection Fidelity. `PRIOR_ROWS_CITED` proves nothing was dropped; it does not prove anything
    was preserved — a row can carry the citation forward and restate the claim as something the
    upstream phase never committed to, which is worse than dropping it, because the citation now
    lends the substitution a provenance it does not have.

    An ordinal naming no upstream row is reported here too: it is a citation that resolves to
    nothing, and the coverage check cannot see it — a phantom `#7` leaves all of #1..#3 uncited
    just the same.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_at(_where(rule)), unavailable)]

    register = rule.params["prior_register"]
    phase = rule.params["prior_phase"]
    column = rule.params["citation_column"]
    key_column = rule.params["key_column"]
    prior_key_column = rule.params["prior_key_column"]

    upstream = {ordinal: row for ordinal, row in prior_rows}

    out = []
    for i, row in _rows(doc, rule):
        for ordinal in sorted(_cited_ordinals(row, column, register)):
            if ordinal not in upstream:
                out.append((
                    _at(_where(rule), i),
                    f"cites {register} #{ordinal}, and {phase} declares only "
                    f"{len(upstream)} row(s) there",
                ))
                continue
            here = _normalise(_cell(row, key_column))
            there = _normalise(_cell(upstream[ordinal], prior_key_column))
            if here != there:
                out.append((
                    _at(_where(rule), i),
                    f"restates {register} #{ordinal} as {here!r}, which {phase} declared as "
                    f"{there!r} — a citation is not a licence to change the claim",
                ))
    return out


@check("PRIOR_IDENTITIES_COVERED")
def _prior_identities_covered(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Two registers naming artifact identities must name the same ones.

    The handoffs above are checked row by row, because a belief is a claim and claims are matched by
    what they say. From P4 on, a dossier stops citing upstream rows ordinally and starts naming
    artifacts, so there is nothing to match a row against — but there is something better. An
    identity is exact. Two registers that both name identities are reconciled as sets, and the
    citation idiom stops mattering entirely.

    `require` says which way the containment runs, and the two directions are different defects:

        prior_in_here   something the upstream phase committed to went unscheduled
        here_in_prior   something is scheduled that no upstream phase ever designed

    Both are silent in either document alone. A build order made entirely of well-formed rows can
    omit an artifact the design declared, and a design listing every artifact can be missing one the
    mandate invented — and each document is internally consistent throughout.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_at(_where(rule)), unavailable)]

    phase = rule.params["prior_phase"]
    register = rule.params["prior_register"]
    require = rule.params["require"]
    if require not in ("prior_in_here", "here_in_prior"):
        raise KeyError(f"{rule.id}: 'require' must be prior_in_here or here_in_prior, not {require!r}")

    # A provisional code and the FQDN it is later bound to are the same identity stated at two rungs
    # of the purity ladder — P5 must not namespace one, P7 must. Comparing the raw cells would
    # report every code unbound, so the rule declares which representation it is matching on.
    match_on = rule.params.get("match_on", "exact")
    if match_on not in ("exact", "bare_code"):
        raise KeyError(f"{rule.id}: 'match_on' must be exact or bare_code, not {match_on!r}")
    normalise = (lambda v: v.split("::")[-1]) if match_on == "bare_code" else (lambda v: v)

    # A prior row may not oblige anything. A subdomain a change merely reads is named upstream and
    # authors nothing, so the obligation is gated on what the upstream row says about itself rather
    # than on its presence. Absent the gate every prior row obliges, which is the prior behaviour.
    gate_column = rule.params.get("prior_only_when_column")
    gate_values = rule.params.get("prior_only_when_values")
    # A family gate, where the obligation is about what kind of artifact a row names rather than
    # what the row says about it. `existing_inventory` carries no Family column — an artifact
    # carried over from the composition states its family in its own identity, which is the only
    # place it can, because the design assigns it no new code. So the prefix is the family.
    gate_prefixes = rule.params.get("prior_only_when_prefixes")

    def obliges(row) -> bool:
        if gate_prefixes:
            code = _cell(row, rule.params["prior_column"]).split("::")[-1]
            if not any(code.startswith(prefix) for prefix in gate_prefixes):
                return False
        if not gate_column:
            return True
        return _cell(row, gate_column) in gate_values

    there = {
        normalise(identity): ordinal
        for ordinal, row in prior_rows
        if obliges(row) and (identity := _cell(row, rule.params["prior_column"]))
    }
    here = {
        normalise(identity): i
        for i, row in _rows(doc, rule)
        if (identity := _cell(row, rule.params["column"]))
    }

    # `union` widens the local side across more than one register, because a commitment can be
    # honoured in more than one place. A change request that *extends* an existing artifact honours
    # its provisional code in the existing inventory, not by authoring a new identity — and the
    # first CR to extend anything found that no P7 could satisfy both directions of the closure at
    # once. Declared per rule and gated per register, so a widening states which rows count.
    #
    # Only ever declared on `prior_in_here`. The reverse direction asks a different question — was
    # this authored without intent — and an extended artifact may legitimately be substrate the
    # business never named, which is why a union there would refuse correct dossiers.
    for spec in rule.params.get("union", ()):
        block = doc.register(spec["register"])
        gate_column = spec.get("only_when_column")
        gate_value = str(spec.get("only_when_value", "")).strip().upper()
        for i, row in _content_rows(block):
            if gate_column and _cell(row, gate_column).strip().upper() != gate_value:
                continue
            identity = _cell(row, spec["column"])
            if identity:
                here.setdefault(normalise(identity), i)

    if require == "prior_in_here":
        return [
            (_at(_where(rule)),
             f"{identity} is declared at {phase} {register} #{ordinal} and appears nowhere here")
            for identity, ordinal in sorted(there.items(), key=lambda kv: kv[1])
            if identity not in here
        ]
    return [
        (_at(_where(rule), i),
         f"{identity} appears in no {phase} {register} row — it was never designed")
        for identity, i in sorted(here.items(), key=lambda kv: kv[1])
        if identity not in there
    ]


@check("PRIOR_ROWS_PRESENT_BY_KEY")
def _prior_rows_present_by_key(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Every row of an upstream register must reappear here, matched on what it says.

    The third way two documents are compared, and the one that needs no idiom at all.

    `PRIOR_ROWS_CITED` matches on an ordinal citation, which works from P1 to P3 because those
    dossiers cite `S1 system_beliefs #2`. It cannot work against the seed: the seed is cited by
    section title, and the title is free-form — CR-0 writes `CR seed §5 Beliefs #1` where CR-1
    writes `System Beliefs #1`, both abbreviating "Existing-System Beliefs — Requiring
    Verification". A label that has already drifted between two change requests is not something to
    match on, and blessing both spellings would only invite a third.

    `PRIOR_IDENTITIES_COVERED` matches on an identity, which is exact but only exists once a phase
    is naming artifacts.

    Between them sits a register that is restated in business language: the row is the same claim,
    written the same way, in a register of the same name. So match on the claim.

    Coverage only, deliberately. A row here that is in no upstream register is an *addition*, and
    the phases that restate legitimately elaborate — splitting one outcome into two is not a defect.
    Loss is the silent half: a change request missing an acceptance criterion is a perfectly
    well-formed change request, and that criterion is what the finished composition is later
    validated against.

    Coverage may be owed to several registers at once rather than one. A declared refusal is
    accounted for by being discharged *or* by being deferred, and the two are separate registers
    because a discharge names a place in the topology and a deferral names a person — so a rule
    reading either alone would report every deferred refusal as uncovered. `registers` is that list
    and defaults to the single register the rule governs, exactly as `CELL_RESOLVES_IN_REGISTER`
    already accepts `target_registers`: every rule that does not pass it is judged as it was before.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_at(_where(rule)), unavailable)]

    phase = rule.params["prior_phase"]
    register = rule.params["prior_register"]
    prior_key = _key_columns(rule.params["prior_key_column"])
    key = _key_columns(rule.params["key_column"])

    # A phase may owe a carry for only some upstream rows: every capability P5 declares IN_SCOPE
    # must be placed at P6, while a DEFERRED one is under no such obligation. The filter reads the
    # upstream row, because that is where the obligation is declared.
    gate_column = rule.params.get("prior_only_when_column")
    gate_value = rule.params.get("prior_only_when_value")

    # The register this rule governs, unless it declares the several a row may be covered by. A
    # second register is read with the same key columns: it answers the same question about the same
    # upstream row, which is what makes it an alternative rather than a different check.
    covering = rule.params.get("registers")
    if covering:
        here = {
            _claim(row, key)
            for name in covering
            for _, row in _content_rows(doc.register(name))
        }
        where = "in " + " or ".join(covering)
    else:
        here = {_claim(row, key) for _, row in _rows(doc, rule)}
        # "here" and not the register's name, because that is what every rule using this kind
        # already reports and a widened kind must not reword a finding it did not change.
        where = "here"

    out = []
    total = len(prior_rows)
    for ordinal, row in prior_rows:
        if gate_column and _cell(row, gate_column) != gate_value:
            continue
        claim = _claim(row, prior_key)
        if not claim or claim in here:
            continue
        out.append((
            _at(_where(rule)),
            f"{phase} {register} #{ordinal} of {total} is restated nowhere {where}: {claim!r}",
        ))
    return out


@check("REGISTER_COVERS_REGISTER")
def _register_covers_register(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Every row of one register must be accounted for in another register of the same document.

    The cross-phase kinds above check that a handoff between two documents preserved something. This
    is the same question asked *inside* one document, and it is the one the pipeline never asked: P7
    declared six workflows and gave three of them a topology, declared eight capability contracts and
    composed five, and was ADMISSIBLE at fifty-seven rules — because every rule judged the rows that
    were present and nothing required the rows that were not.

    The information already had somewhere to live. What was missing was any obligation that it
    exist, which is a deficiency in the language's **constraints** rather than in its expressiveness.

    Filtered on the source row, because the obligation usually applies to one artifact family: a
    workflow needs a topology, a capability contract needs a composition, and neither needs the
    other's.
    """
    source = rule.params["source_register"]
    block = doc.register(source)
    if block is None or block.table is None:
        return [(
            _at(_where(rule)),
            f"{source!r} is absent, so nothing establishes what this register must cover",
        )]

    gate_column = rule.params.get("only_when_column")
    gate_value = rule.params.get("only_when_value")
    source_column = rule.params["source_column"]

    # A gate on the covering side too, because a register may account for several kinds of fact in
    # one table. `artifact_properties` carries every scalar an artifact declares, so a rule asking
    # "is this artifact named as superseded" must read only the rows that say so — otherwise any
    # cell whose value happened to match would answer for it, and the rule would pass on a
    # coincidence.
    covered_gate_column = rule.params.get("covered_only_when_column")
    covered_gate_value = rule.params.get("covered_only_when_value")

    # Or a gate on whether the covering row states anything at all in a column, for a fact whose
    # value varies row to row — a molecule's emission is named, not flagged, so no one value selects
    # the row that carries it.
    covered_present_column = rule.params.get("covered_present_column")

    covered = {
        _bare_identity(item)
        for _, row in _rows(doc, rule)
        if (not covered_gate_column or _cell(row, covered_gate_column) == covered_gate_value)
        and (not covered_present_column or _present(row, covered_present_column))
        for item in _items(row, rule.params["column"])
    }

    # A gate on the source key's form, for a register holding several families in one column: the
    # inventory carries every amended artifact, and an obligation owed by transforms alone must read
    # only the rows naming a transform.
    source_pattern = rule.params.get("only_when_source_pattern")
    source_re = re.compile(source_pattern) if source_pattern else None

    out = []
    for ordinal, row in _content_rows(block):
        if gate_column and _cell(row, gate_column) != gate_value:
            continue
        key = _cell(row, source_column)
        if source_re and not source_re.match(_bare_identity(key)):
            continue
        if not key or _bare_identity(key) in covered:
            continue
        out.append((
            _at(_where(rule)),
            f"{key} is declared at {source} #{ordinal} and this register says nothing about it"
            + (f" ({gate_column} {gate_value})" if gate_column else ""),
        ))
    return out


@check("ROWS_CONFINED_TO_PRIOR")
def _rows_confined_to_prior(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """No row here may assert something the upstream register does not.

    `PRIOR_ROWS_PRESENT_BY_KEY` is coverage — it catches the row that went missing. This is the
    other direction, and the hole it closes was demonstrable: a change request carrying
    "books must be shelved by Dewey Decimal number", a business fact no seed states, cited to a
    seed row that does not exist, was ADMISSIBLE over 131 rules. Loss was governed; invention was
    not.

    Only a phase whose contract is *restatement* may carry this rule. P1 interrogates and does not
    author, so its business registers are confined to the seed's; a phase that legitimately adds
    (P2 projects, P3 decides) must not be judged this way.

    It also narrows something the coverage rule deliberately permitted — elaborating one upstream
    row into two. That freedom is what let a business fact enter at P1 wearing the clothes of an
    elaboration. Elaboration now belongs at P0, in the seed, where a person owns the wording.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_at(_where(rule)), unavailable)]

    phase = rule.params["prior_phase"]
    register = rule.params["prior_register"]
    prior_key = _key_columns(rule.params["prior_key_column"])
    key = _key_columns(rule.params["key_column"])

    upstream = {_claim(row, prior_key) for _, row in prior_rows}

    out = []
    for i, (_, row) in enumerate(_rows(doc, rule), start=1):
        claim = _claim(row, key)
        if not claim or claim in upstream:
            continue
        out.append((
            _at(_where(rule), i),
            f"states what {phase} {register} does not: {claim!r} — this phase restates business "
            f"content, so a new claim belongs upstream where a person owns it",
        ))
    return out


@check("COLUMN_VALUES_UNIQUE")
def _column_values_unique(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A column whose value identifies the row, so two rows may not carry the same one.

    Every other register check asks whether a row says the right thing. This asks whether the
    register says one thing about a subject at all: where a second row restates a subject the first
    already settled, the two may disagree, and nothing downstream can tell which was meant. Reading
    the first, the last, or refusing are three different behaviours and none of them is declared.

    Compared on the bare identity, because a subject written once as `domain::CODE_V0` and once as
    `CODE_V0` is one subject stated twice, and a comparison on the full string would call it two.
    """
    seen: dict[tuple[str, ...], int] = {}
    out: list[tuple[Locator, str]] = []
    # A key is one column, or several that identify a row only together: a topology node is a
    # place within its workflow, and the same key names another place in another workflow.
    columns = rule.params.get("columns") or [rule.params["column"]]
    # Uniqueness over the rows that state something in another column, where a register holds many
    # rows per subject and only one of them may carry a given fact: a molecule has many steps and
    # exactly one emission.
    present_column = rule.params.get("only_when_present_column")
    for index, row in _rows(doc, rule):
        if present_column and not _present(row, present_column):
            continue
        key = tuple(_bare_identity(_cell(row, c)) for c in columns)
        if not all(key):
            continue
        first = seen.setdefault(key, index)
        if first != index:
            out.append((_at(_where(rule), index),
                        rule.params["detail"].format(*key, value=" · ".join(key), first=first)))
    return out
