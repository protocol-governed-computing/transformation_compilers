"""The `AUTHORED_CHANGE_HAS_NO_DESIGN` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _cell, _content_rows, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("AUTHORED_CHANGE_HAS_NO_DESIGN")
def _authored_change_has_no_design(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A change its seed declares authored has no design intent.

    Construction renders nothing an authored change delivers, so its dossier is complete at
    governance intent. A design intent for it would schedule a constitution or the derive route's
    code to be rendered from registers that never held their content.

    The seed declares delivery once, at the start, because it is known there. A seed that declares
    none is judged as before: the declaration is new, and a seed written before it is not refused
    for its absence.
    """
    phase = rule.params["prior_phase"]
    register = rule.params["prior_register"]
    if not doc.has_prior(phase):
        return [(_at(_where(rule)), f"{phase} was not supplied — whether this change may have a design "
                                     f"intent at all is unchecked")]
    return [
        (_at(_where(rule)), f"{phase} declares this change {mode} in its {register!r} register, so it is "
                             f"complete at governance intent and has no design intent")
        for _, row in _content_rows(doc.prior_register(phase, register))
        if (mode := _cell(row, "Mode").upper()) == rule.params["authored"]
    ]
