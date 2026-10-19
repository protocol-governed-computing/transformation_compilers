"""The `INTERPRETATION_TRANSFORM_REFUSES` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _content_rows,
    _rows,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("INTERPRETATION_TRANSFORM_REFUSES")
def _interpretation_transform_refuses(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A transform that interprets an observation must be able to refuse it.

    A read reports that the store answered, never what it found, so a step reading state names the
    transform that turns the observation into a decision and the status that decision yields. Both
    have been required since CR-1. Neither asks the one question that decides whether the
    interpretation happens: a `CT` step yields SUCCESS when its transform returns and VIOLATION when
    it raises, so a transform that returns its judgement as a value leaves the step SUCCEEDing
    whatever it found, and the semantic status the row promises is never reached.

    `refuse_self_verification` was exactly this. It named `CT_PURE_COMPARE_EQUAL_V0`, which returns
    `is_equal` and raises only on missing inputs, and routed on whether the transform *ran* rather
    than on what it found — so a person could accept themselves, through a step named for refusing
    it. It passed every rule here, at full Construction Completeness, and the criterion covering it
    passed too because a prior defect had left the subject already decided.

    The fact this rests on could not be inferred: both transforms raise, and only a declaration
    distinguishes the one that raises on its judgement from the one that raises on a missing input.
    Read from the composition for a transform that already exists, and from this design's own
    implementation bindings for one it is authoring — the composition has never seen that one, and a
    rule that skipped it would be silent on exactly the transforms a change introduces.
    """
    column = rule.params["column"]
    observed = doc.observed.get(rule.params["observation"])
    if not observed:
        return [(
            _at(_where(rule)),
            "no transform surface was observed — whether an interpreting transform can refuse "
            "cannot be checked against transforms nobody published",
        )]

    refusal = {_bare_identity(str(t.get("transform"))): t.get("refusal")
               for t in observed if isinstance(t, dict) and t.get("transform")}
    for _, row in _content_rows(doc.register(rule.params["design_register"])):
        code = _bare_identity(_cell(row, rule.params["design_code_column"]))
        if code:
            refusal[code] = _cell(row, rule.params["design_refusal_column"]).lower()

    out = []
    for i, row in _rows(doc, rule):
        named = _cell(row, column)
        if not named or named in ("—", "-"):
            continue
        declared = refusal.get(_bare_identity(named))
        where = _at(_where(rule), i)
        if declared is None:
            out.append((
                where,
                f"interprets with {_bare_identity(named)}, which neither the composition nor this "
                f"design declares a refusal for — an interpretation that cannot be shown to refuse "
                f"has not been checked",
            ))
        elif declared != "raises":
            answers = ("yields its judgement as a value" if declared == "returns"
                       else "makes no judgement at all")
            status = _cell(row, rule.params["status_column"]) or "semantic status"
            out.append((
                where,
                f"interprets with {_bare_identity(named)}, which {answers} — the step succeeds "
                f"whatever it found, so the {status} this row declares is a branch nothing can "
                f"reach",
            ))
    return out
