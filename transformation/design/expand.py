"""Expand a phase's register schema into its rule set.

Most of what governs a phase document is already declared in the template: which registers exist,
what columns they carry, which columns hold a controlled vocabulary, which hold business prose, and
which may legitimately be empty. Restating that in Python produces a second declaration that can
disagree with the tested one — and did, in this repo's first cut.

So the rules that follow mechanically from a template are generated here, and a phase's own
`rules.py` declares only what the template cannot express: belief resolution, citation grounding,
and anything else that is a judgement about meaning rather than shape.

Adding a register to a template therefore adds its rules. Forgetting to add them is not possible,
which is the failure mode that leaves one register quietly ungoverned.
"""

from __future__ import annotations

import re
from dataclasses import replace

from transformation.design.schema import PhaseShape as PhaseTemplate, Register
from transformation.design.rules import Rule

# A compiled artifact identity. Business-language columns must not contain one — a business
# register that names artifacts has had design smuggled into it.
ARTIFACT_TOKEN_PATTERN = r"\b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b"



def _register_rules(register: Register, citable: list[str]) -> list[Rule]:
    """Every rule that follows mechanically from one register's declaration.

    `citable` is what this phase may cite — its own registers plus those its handoff contract
    declares it consumes.
    """
    # A register declared without a table is narrative — the Subdomain Purpose is the only one,
    # and it is narrative by definition: the business context no compiled artifact can derive.
    # It is still governed; it just cannot be governed as rows.
    if not register.columns:
        return [
            Rule(
                id="REGISTER_EMPTY",
                check="SECTION_HAS_TEXT",
                register=register.id,
                params={"detail": "narrative register is empty — it states nothing"},
                intent="a narrative register carries the context nothing downstream can rederive",
            )
        ]

    out: list[Rule] = [
        Rule(
            id="REGISTER_MISSING",
            check="TABLE_PRESENT",
            register=register.id,
            intent="a declared register must be present and readable as rows",
        ),
    ]

    if register.columns:
        out.append(
            Rule(
                id="REGISTER_COLUMN_MISSING",
                check="TABLE_HAS_COLUMNS",
                register=register.id,
                params={"columns": list(register.required_columns)},
                intent="downstream phases read these columns by name",
            )
        )

    if not register.optional:
        out.append(
            Rule(
                id="REGISTER_EMPTY",
                check="TABLE_HAS_ROWS",
                register=register.id,
                intent="an empty required register asserts nothing",
            )
        )

    # Vocabularies declared inline in the column header, e.g. `Certainty (HIGH, MEDIUM, LOW)`.
    for column, values in register.vocabularies.items():
        out.append(
            Rule(
                id="CELL_NOT_IN_VOCABULARY",
                check="CELL_IN_VOCABULARY",
                register=register.id,
                params={"column": column, "vocabulary": list(values)},
                intent=f"{column} is a controlled vocabulary declared by the template",
            )
        )

    # A column that carries structure — a list, a routing, an interface, a binding — holds a value
    # of its declared type. A cell that did not structure is refused here, once, rather than read
    # wrongly by every rule downstream. A column whose value may be anything declares no type.
    for column, declared in register.types.items():
        if not declared:
            continue
        out.append(
            Rule(
                id="CELL_NOT_OF_TYPE",
                check="CELL_OF_TYPE",
                register=register.id,
                params={"column": column, "type": declared},
                intent=f"{column} carries structure, and its value must take the declared form",
            )
        )

    # Business-language columns hold prose about the business, never compiled identities. The flag
    # may scope to specific columns, which is why this is not a whole-document rule.
    business_columns = [c for c in register.business_language_columns if c]
    if business_columns:
        out.append(
            Rule(
                id="DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
                check="CELL_TOKEN_ABSENT",
                register=register.id,
                params={
                    "columns": business_columns,
                    "pattern": ARTIFACT_TOKEN_PATTERN,
                    "detail": (
                        "{token!r} appears in business-language column {column!r} — "
                        "this register states business meaning, not design"
                    ),
                },
                intent="business registers name no compiled artifact",
            )
        )

    if register.traceable:
        out.append(
            Rule(
                id="ROW_WITHOUT_SOURCE_FINDING",
                check="CITATION_PRESENT",
                register=register.id,
                params={
                    "column": "Source Finding",
                    "detail": "row cites no earlier finding — a phase restates its input, it does not add to it",
                },
                intent="an uncited row has no provenance in the dossier",
            )
        )
        out.append(
            Rule(
                id="SOURCE_FINDING_UNRESOLVED",
                check="SOURCE_FINDING_RESOLVES",
                register=register.id,
                params={
                    "column": "Source Finding",
                    "known_registers": citable,
                },
                intent="a citation must name something this phase can actually cite",
            )
        )
        out.append(
            Rule(
                id="CITATION_ORDINAL_UNRESOLVED",
                check="CITED_ORDINAL_RESOLVES",
                register=register.id,
                params={"column": "Source Finding"},
                intent="an ordinal past the end of a register cites a finding that is not there",
            )
        )

    return out


def _all_declared_registers() -> set[str]:
    """Every register id declared by any phase template.

    Cached on first use — the templates are vendored and do not change during a run.
    """
    global _DECLARED
    if _DECLARED is None:
        from transformation.design.catalog import PHASES
        from transformation.design.schema import load

        ids: set[str] = set()
        for spec in PHASES:
            ids |= {r.id for r in load(spec.id).registers}
        _DECLARED = ids
    return _DECLARED


_DECLARED: set[str] | None = None


def derived_rules(template: PhaseTemplate) -> list[Rule]:
    """The rule set that follows from a template, before any phase-specific declaration.

    What a phase may cite is **every register the dossier declares**, not only what its
    `gov_projection` Consumes list forwards. Consumes is the lossless handoff — the working input a
    phase receives — while provenance may reach further back: the tested P7 register cites S1, S3,
    S5 and S6 alike, and none of those are in its Consumes.

    Restricting citation to Consumes rejected six of eight tested dossier documents. The rule that
    holds is that a citation must name a register some phase actually declares, so a typo or a
    fabricated register id is still caught.
    """
    citable = sorted(_all_declared_registers() | {r.id for r in template.registers})
    out: list[Rule] = _document_rules(template)
    for register in template.registers:
        out.extend(replace(rule, identity=f"{template.schema_id}#{_pointer(register, rule)}")
                   for rule in _register_rules(register, citable))
    return out


def _document_rules(shape: PhaseTemplate) -> list[Rule]:
    """The header rules: one for the fields a document must state, and one per declared field."""
    base = f"{shape.schema_id}#/properties/document"
    out = [Rule(
        id="HEADER_FIELD_MISSING", check="HEADER_FIELD_PRESENT", identity=f"{base}/required",
        params={"fields": list(shape.document_required)},
        intent="a phase document states its phase, its domain and subdomain, its change, and the "
               "rule set it was authored under",
    )]
    for name, declared in shape.document.items():
        at = f"{base}/properties/{name}"
        if "const" in declared:
            out.append(Rule(id="HEADER_FIELD_MISMATCH", check="HEADER_FIELD_MATCHES", identity=f"{at}/const",
                            params={"fields": [name], "pattern": f"^{re.escape(declared['const'])}$"},
                            intent=f"a document's {name} is the phase whose rules judge it"))
        elif "pattern" in declared:
            out.append(Rule(id="HEADER_FIELD_MISMATCH", check="HEADER_FIELD_MATCHES", identity=f"{at}/pattern",
                            params={"fields": [name], "pattern": declared["pattern"]},
                            intent=f"a document's {name} names a rule set of its own phase"))
        else:
            out.append(Rule(id="HEADER_FIELD_NOT_OF_TYPE", check="HEADER_FIELD_OF_TYPE", identity=at,
                            params={"field": name, "type": declared},
                            intent=f"a document's {name} takes its declared form"))
    return out


# The invariant a derived rule realises, where it realises one. A declared rule states its own in
# `x-realises`; a derived rule has no entry to state it in, so its check kind states it here. The rest
# of the derived rules realise the register schema itself (DESIGN_LANGUAGE §3).
DERIVED_REALISES = {
    "CITATION_PRESENT": "lifecycle::INVARIANT_ROW_PROVENANCE_CITED_V0",
    "SOURCE_FINDING_RESOLVES": "lifecycle::INVARIANT_ROW_PROVENANCE_CITED_V0",
    "CITED_ORDINAL_RESOLVES": "lifecycle::INVARIANT_ROW_PROVENANCE_CITED_V0",
    "CELL_TOKEN_ABSENT": "lifecycle::INVARIANT_PHASE_SPEAKS_ITS_RUNG_V0",
}


# Where a derived rule is declared: the keyword it expands, where the schema has one, and otherwise
# the declaration it derives from, followed by `x-derived/<check>`.
_AT_REGISTER = {"SECTION_HAS_TEXT": "minLength", "TABLE_HAS_ROWS": "minItems",
                "TABLE_HAS_COLUMNS": "items/required", "CELL_TOKEN_ABSENT": "x-business-language"}


def _pointer(register: Register, rule: Rule) -> str:
    """The JSON Pointer to the declaration a derived rule expands, unique within its schema."""
    base = f"/properties/registers/properties/{register.id}"
    if rule.check in _AT_REGISTER:
        return f"{base}/{_AT_REGISTER[rule.check]}"
    column = rule.params.get("column")
    if column is None:
        return f"{base}/x-derived/{rule.check}"
    key = dict(zip(register.columns, register.keys))[column]
    if rule.check == "CELL_IN_VOCABULARY":
        return f"{base}/items/properties/{key}/x-vocab"
    return f"{base}/items/properties/{key}/x-derived/{rule.check}"


def coverage(template: PhaseTemplate) -> dict[str, int]:
    """How much of a phase its template governs — reported so it cannot be assumed.

    A phase whose rules are wholly derived is fully covered by the tested template. One with many
    hand-declared rules is carrying judgement the template does not express, which is legitimate but
    worth seeing.
    """
    return {
        "registers": len(template.registers),
        "derived_rules": len(derived_rules(template)),
        "vocabulary_columns": sum(len(r.vocabularies) for r in template.registers),
        "business_language_registers": sum(1 for r in template.registers if r.business_language_columns),
        "traceable_registers": sum(1 for r in template.registers if r.traceable),
        "optional_registers": sum(1 for r in template.registers if r.optional),
    }


def declared_rules(shape: PhaseTemplate) -> list[Rule]:
    """The rules a schema declares beyond its shape: each `allOf` entry, decoded, in order.

    An entry about one register names it with `x-register`; one without is about the whole document.
    """
    from transformation.design.declared import Columns, decode

    out = []
    for index, entry in enumerate(shape.entries):
        register_id = entry.get("x-register")
        if register_id is None:
            rule = decode(entry, None, None)
        else:
            register = shape.register(register_id)
            rule = decode(entry, register_id, Columns(dict(zip(register.columns, register.keys))))
        out.append(replace(rule, identity=f"{shape.schema_id}#/allOf/{index}"))
    return out


def expanded_rules(shape: PhaseTemplate) -> list[Rule]:
    """A phase's whole rule set: what its shape implies, then what it declares beyond that. Every
    rule carries an identity no other rule of the set shares."""
    rules = derived_rules(shape) + declared_rules(shape)
    seen = [r.identity for r in rules]
    if len(set(seen)) != len(seen):
        raise ValueError(f"{shape.schema_id}: two rules share an identity")
    return rules
