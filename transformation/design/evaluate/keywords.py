"""The keyword subset: the checks a schema's shape and its constraints expand into (DESIGN_LANGUAGE §3, §4.1)."""

from __future__ import annotations

import re

import jsonschema

from transformation.design.evaluate.common import (
    _at,
    _block,
    _cell,
    _cited,
    _content_rows,
    _rows,
    _value,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check
from transformation.design.schema import column_key


def _stated(row: dict, column: str) -> bool:
    """Whether a cell answers its column. `null` is an answer: the row says there is nothing to
    state. A blank text, an empty list and an absent column are not."""
    key = column_key(column)
    if key not in row:
        return False
    value = row[key]
    if value is None:
        return True
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def _gated_out(row: dict[str, str], rule) -> bool:
    """Whether a row falls outside the rows a rule is about.

    `only_when_column` with `only_when_value` selects the rows in one state; with `only_when_values`
    it selects the rows in any of several, which a register whose column names three kinds of row
    needs for a fact two of them share.
    """
    column = rule.params.get("only_when_column")
    if not column:
        return False
    gate = _value(row, column)
    values = rule.params.get("only_when_values")
    if values is not None:
        return gate not in list(values)
    return gate != rule.params.get("only_when_value")


# Check kinds ------------------------------------------------------------------------------


@check("HEADER_FIELD_PRESENT")
def _header_field_present(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    out = []
    for name in rule.params["fields"]:
        value = doc.header.get(name)
        if value is None or value == [] or (isinstance(value, str) and not value.strip()):
            out.append((_at("document", None, name), f"required field {name!r} absent"))
    return out


@check("HEADER_FIELD_MATCHES")
def _header_field_matches(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    out = []
    pattern = re.compile(rule.params["pattern"])
    for name in rule.params["fields"]:
        value = doc.header.get(name)
        if value is None or (isinstance(value, str) and not value.strip()):
            continue
        if not isinstance(value, str) or not pattern.match(value.strip()):
            out.append((_at("document", None, name), f"{name} {value!r} does not match {rule.params['pattern']}"))
    return out


@check("HEADER_FIELD_OF_TYPE")
def _header_field_of_type(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A stated header field takes its declared form. An absent one is `HEADER_FIELD_PRESENT`'s."""
    name = rule.params["field"]
    value = doc.header.get(name)
    if value is None or jsonschema.Draft202012Validator(rule.params["type"]).is_valid(value):
        return []
    return [(_at("document", None, name), f"{name} does not take its declared form: {value!r}")]


@check("SECTION_HAS_TEXT")
def _section_has_text(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    block = _block(doc, rule)
    if block is None:
        # Same reasoning as TABLE_PRESENT: an absent narrative register is a finding, not a skip.
        if getattr(rule, "register", None):
            return [(_at(_where(rule)), "declared register is absent from the document")]
        return []
    if not block.text():
        return [(_at(_where(rule)), rule.params["detail"])]
    return []


@check("TABLE_PRESENT")
def _table_present(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """The register must be there, and must be readable as rows.

    Absence is the finding this check exists for. Returning nothing when the register is missing —
    which is what an earlier version did — meant a document could drop a register entirely and be
    judged admissible: every cell-level rule skips a register it cannot find, so nothing else would
    have spoken up either.
    """
    block = _block(doc, rule)
    if block is None:
        return [(_at(_where(rule)), "declared register is absent from the document")]
    if block.table is None:
        return [(_at(_where(rule)), "register is present but carries no table, so it cannot be read as rows")]
    return []


@check("TABLE_HAS_COLUMNS")
def _table_has_columns(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Every row carries every column the register requires. A column with nothing to state carries
    `null`; a row that leaves the column out has not answered it."""
    out = []
    for i, row in _rows(doc, rule):
        for expected in rule.params["columns"]:
            if column_key(expected) not in row:
                out.append((_at(_where(rule), i), f"required column {expected!r} absent"))
    return out


@check("TABLE_HAS_ROWS")
def _table_has_rows(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    # `minimum` defaults to 1 — "declared but empty asserts nothing". A register whose rows are a
    # fixed checklist rather than free content declares the count it owes, so a claim resting on
    # fewer rows than the criteria it cites is reported rather than read as complete.
    minimum = int(rule.params.get("minimum", 1))
    # A register declared empty has answered: it counts as one considered row. One that states
    # nothing has not, and counts as none.
    rows = len(block.table.rows) or (1 if block.table.declared_empty else 0)
    if rows < minimum:
        detail = (
            "section requires at least one row"
            if minimum == 1
            else f"section declares {rows} row(s); {minimum} are required"
        )
        return [(_at(_where(rule)), detail)]
    return []


@check("TABLE_ROW_COUNT")
def _table_row_count(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """How many rows a register may carry.

    `TABLE_HAS_ROWS` already asserts a floor — a declared register that is empty asserts nothing.
    Nothing asserted a ceiling, so a register meant to carry one answer could carry three
    contradictory ones and no rule anyone could write would notice. That is not a rule nobody
    wrote; it is a rule nobody *could* write, which is why this is a way of judging rather than a
    rule.

    `maximum` is the half that was missing; `minimum` is accepted too so a register owing an exact
    count can declare one thing rather than two rules that could disagree.

    Adding this changes no verdict. A ceiling is a judgement about what a particular register
    means, made per register, and this kind ships applied to none.
    """
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    rows = len(block.table.rows)
    minimum = rule.params.get("minimum")
    maximum = rule.params.get("maximum")
    out = []
    if minimum is not None and rows < int(minimum):
        out.append((_at(_where(rule)), f"register carries {rows} row(s); at least {minimum} required"))
    if maximum is not None and rows > int(maximum):
        # A rule may say what its own ceiling means; a generic message cannot know why one row.
        detail = rule.params.get("detail")
        out.append((
            _at(_where(rule)),
            f"register carries {rows} row(s); at most {maximum} permitted"
            + (f" — {detail}" if detail else ""),
        ))
    return out


@check("COLUMN_ABSENT")
def _column_absent(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    forbidden = column_key(rule.params["column"])
    if forbidden in block.table.keys:
        return [(_at(_where(rule)), rule.params["detail"])]
    return []


@check("CELL_OF_TYPE")
def _cell_of_type(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A column that carries structure holds a value of its declared type.

    A routing is a mapping from outcome to target, an interface a mapping per side, a list a list,
    a binding a path, a literal or the generated marker. A cell that is still the text it was
    written as did not structure, and every rule reading the column would read it wrongly; so it is
    refused here, once, with the value shown.
    """
    validator = jsonschema.Draft202012Validator(rule.params["type"])
    out = []
    key = column_key(rule.params["column"])
    for i, row in _rows(doc, rule):
        if key in row and not validator.is_valid(row[key]):
            out.append((_at(_where(rule), i),
                        f"{rule.params['column']!r} does not take its declared form: {row[key]!r}"))
    return out


@check("CELL_IN_VOCABULARY")
def _cell_in_vocabulary(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    out = []
    column = rule.params["column"]
    vocabulary = rule.params["vocabulary"]
    for i, row in _rows(doc, rule):
        value = _cell(row, column)
        if value not in vocabulary:
            out.append(
                (
                    _at(_where(rule), i),
                    f"{value!r} is not one of {list(vocabulary)}",
                )
            )
    return out


@check("CELL_NOT_EMPTY")
def _cell_not_empty(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A column that must carry a value — optionally only for rows in a given state.

    `only_when_column` / `only_when_value` narrow the rule to the rows it is really about, the same
    gating `CITED_ARTIFACTS_RESOLVE` uses. Without it a requirement that applies to one status
    would report against every row, and a register would have to be split to say something true
    about part of itself.
    """
    out = []
    column = rule.params["column"]
    for i, row in _rows(doc, rule):
        if _gated_out(row, rule):
            continue
        if not _stated(row, column):
            out.append((_at(_where(rule), i), rule.params["detail"]))
    return out


@check("CELL_PRESENT")
def _cell_present(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A column every row must carry. For a column whose value may be anything, an empty string and
    `null` are values, so the only way a row leaves it unstated is to leave it out."""
    key = column_key(rule.params["column"])
    return [(_at(_where(rule), i), rule.params["detail"])
            for i, row in _rows(doc, rule) if key not in row]


@check("CITATION_PRESENT")
def _citation_present(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A row must cite where it came from. A citation column that says nothing, `null`, cites
    nothing; a citation is never an answer of "none"."""
    column = rule.params["column"]
    return [(_at(_where(rule), i), rule.params["detail"])
            for i, row in _rows(doc, rule) if _value(row, column) in (None, "", [])]


@check("ROW_ABSENT_WHEN")
def _row_absent_when(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A register may not carry a row in a given state.

    `CELL_IN_VOCABULARY` says which values a column may hold; this says which of them the document
    may still be carrying when it is judged. The difference matters for a register whose whole
    purpose is to hold rows that must eventually be gone — an open question is well-formed and
    still not something a downstream phase may consume.
    """
    out = []
    column = rule.params["column"]
    value = rule.params["value"]
    for i, row in _rows(doc, rule):
        if _value(row, column) == value:
            out.append((_at(_where(rule), i), rule.params["detail"]))
    return out


@check("CELL_MATCHES")
def _cell_matches(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """Every non-empty cell in a column must match a declared pattern.

    Emptiness is CELL_NOT_EMPTY's concern — a rule that checked both would report two findings for
    one defect and make the cause ambiguous.
    """
    out = []
    column = rule.params["column"]
    pattern = re.compile(rule.params["pattern"])
    # A pattern that applies to only some rows says so, the way every other gated check does. A
    # naming rule for one artifact family would otherwise have to be a check kind of its own.
    for i, row in _rows(doc, rule):
        if _gated_out(row, rule):
            continue
        value = _value(row, column)
        # A pattern constrains text. A typed value (a literal binding, a list) is not text, and a
        # cell stating nothing has nothing to match.
        if isinstance(value, str) and value.strip() and not pattern.match(value.strip()):
            value = value.strip()
            out.append((_at(_where(rule), i), rule.params["detail"].format(value=value)))
    return out


@check("CELL_TOKEN_ABSENT")
def _cell_token_absent(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A pattern must not appear in specific columns.

    Scoped to columns rather than the whole document, because a register can legitimately hold both
    business prose and the identity it was grounded against. Applying the rule document-wide would
    forbid the citation that makes the grounding checkable.
    """
    out = []
    pattern = re.compile(rule.params["pattern"])
    for column in rule.params["columns"]:
        for i, row in _rows(doc, rule):
            for token in sorted(set(pattern.findall(_cell(row, column)))):
                out.append((
                    _at(_where(rule), i),
                    rule.params["detail"].format(token=token, column=column),
                ))
    return out


@check("SOURCE_FINDING_RESOLVES")
def _source_finding_resolves(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A citation must name something this phase can legitimately cite.

    The valid set is declared, not guessed at:

    - a register this phase **consumes**, from its `gov_projection` handoff contract
    - a register this phase **owns** — a later register citing an earlier one of the same phase is
      ordinary intra-phase provenance
    - the **seed**, which every phase may cite, and a **human ruling**
    - an artifact already in the baseline, by exact identity (field manual §4.2): citing the
      baseline is observation, not design

    One resolvable citation makes the row traceable; requiring all of them would reject a row whose
    second reference is an aside rather than a register.
    """
    known = set(rule.params["known_registers"])

    def resolves(citation: dict) -> bool:
        return ("source" in citation or "artifact" in citation or citation.get("phase") == "p0"
                or citation.get("register") in known)

    out = []
    for i, row in _rows(doc, rule):
        cited = _cited(row, rule.params["column"])
        if not cited or any(resolves(c) for c in cited):
            continue                             # nothing cited is ROW_WITHOUT_SOURCE_FINDING's job
        out.append((
            _at(_where(rule), i),
            f"{_value(row, rule.params['column'])!r} names no register this phase may cite. "
            f"A citation names a register this phase may cite — {_examples(known)} — the seed "
            f"(`phase: p0`), a human ruling (`source: human`), or an artifact already in the "
            f"baseline (`artifact: <identity>`)",
        ))
    return out


def _examples(known: set[str] | list[str], count: int = 3) -> str:
    """A few register ids the author may actually cite, so a diagnostic teaches the grammar.

    A rule that says only what is wrong makes an author read the checker to learn what is right.
    """
    shown = sorted(known)[:count]
    return ", ".join(f"'{{register: {r}, row: 1}}'" for r in shown) + (", …" if len(known) > count else "")


@check("CITED_ORDINAL_RESOLVES")
def _cited_ordinal_resolves(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A citation naming a row by ordinal must name a row that is there.

    `SOURCE_FINDING_RESOLVES` asks whether a citation names a register this phase may cite. It never
    asks whether the register has the row. So `S1 known_facts #18` against a register holding
    seventeen rows passes, and the finding it claims to rest on does not exist — the failure
    `project.py` names exactly: an ordinal pointing past the end resolves to a claim the row does
    not make, and nothing downstream can tell.

    A projected document cannot have this defect: its ordinals are generated from the rows they
    count. Every hand-authored phase from P2 on can, and P2 did — four citations off by one and one
    past the end of the register, all admitted.

    Resolved against whichever document the citation names: a stage-qualified register is looked up
    in that prior, an unqualified one in this document, which is ordinary intra-phase provenance.

    **Silent when the register cannot be reached.** A prior nobody supplied is the driver's
    omission, and reporting a document defect for a missing command-line argument is the confusion
    `_prior_rows` exists to avoid. This rule reports one thing only: the register was read, and the
    row it was asked for is not in it.
    """
    column = rule.params["column"]

    out: list[tuple[Locator, str]] = []
    for index, row in _rows(doc, rule):
        for citation in _cited(row, column):
            if "register" not in citation or "row" not in citation:
                continue
            phase, register, ordinal = citation.get("phase"), citation["register"], citation["row"]
            block = doc.prior_register(phase, register) if phase else doc.register(register)
            if block is None or block.table is None:
                continue
            held = len(_content_rows(block))
            if ordinal < 1 or ordinal > held:
                where = _at(_where(rule), index)
                out.append((
                    where,
                    f"cites {register} #{ordinal}, which holds {held} row(s) — the citation "
                    f"resolves to a finding that is not there",
                ))
    return out
