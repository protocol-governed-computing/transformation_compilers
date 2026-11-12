"""The `GOVERNING_RULE_IN_SEALED_SET` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

import re

from transformation.design.evaluate.common import _at, _cell, _rows, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("GOVERNING_RULE_IN_SEALED_SET")
def _governing_rule_in_sealed_set(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A cited rule must really be in force, in the composition this design is pinned to.

    The register that names it exists so a refusal carried out by the governance surface can be
    stated. Stated and unchecked, it is the failure the refusal work was done to end: a citation
    nobody resolves documents intent and enforces nothing, and prose refuses nothing.

    So the rule is looked up in the **sealed** rule set — the one the composition carries, which is
    what a pin names and what actually judged a document — never in a working tree. Two consequences
    follow and both are stated in the template rather than left to be discovered. **A design cannot
    discharge a refusal by citing a rule its own change is adding**: the rule is not in the pinned
    composition, so the citation resolves to nothing and this rule says so. And a rule retired by a
    later change stops discharging anything, which is the point of asking every time rather than
    once.

    **Resolution is not coverage.** That the cited rule exists and is in force is checkable here;
    that it refuses the condition stated beside it is not, and no rule can check it. That judgment
    is Gate 1's, and this rule deliberately does not pretend to make it.

    The phase is read from its own column because rule identifiers are not unique across phases —
    every derived one is declared by all nine — so an identifier alone names nine rules and resolves
    against whichever happened to be looked at first.
    """
    observed = (doc.observed or {}).get(rule.params["observation"]) or []
    # Which workflow carries which phase is the design compiler's own naming, declared with the
    # rule rather than inferred here: the snapshot publishes identities and knows nothing of phases.
    # The rule names each workflow by its code without a version — a lineage, not an identity — and
    # the version in force is the latest the pinned composition carries: a successor sealed after
    # the pin is not there to be read.
    carried = {
        carrier.get("artifact"): set(carrier.get("rules") or ())
        for carrier in observed
        if isinstance(carrier, dict)
    }
    workflows: dict[str, str] = {}
    for phase, lineage in rule.params["phase_workflows"].items():
        versions = sorted((int(m.group(1)), fqdn) for fqdn in carried
                          if (m := re.fullmatch(rf"{re.escape(lineage)}_V(\d+)", str(fqdn).split("::")[-1])))
        workflows[phase] = versions[-1][1] if versions else lineage
    in_force = carried

    phase_column = rule.params.get("phase_column", "Phase")
    rule_column = rule.params.get("rule_column", "Governing Rule")

    out = []
    for i, row in _rows(doc, rule):
        phase = _cell(row, phase_column).strip()
        cited = _cell(row, rule_column).strip()
        if not phase or not cited or phase not in workflows:
            # A malformed phase and an empty citation are each another rule's finding. Reporting
            # them again here would make one wrong row look like two defects.
            continue
        wf = workflows[phase]
        declared = in_force.get(wf)
        if declared is None:
            out.append((
                _at(_where(rule), i),
                f"{wf.split('::')[-1]} carries no sealed rule set in the pinned composition — "
                f"nothing there can be discharging anything",
            ))
            continue
        if cited not in declared:
            out.append((
                _at(_where(rule), i),
                f"{cited!r} is not in force at {phase} — the composition this design is pinned to "
                f"declares no such rule, so the refusal is carried out by nothing. A design cannot "
                f"discharge a refusal by citing a rule its own change is adding",
            ))
    return out
