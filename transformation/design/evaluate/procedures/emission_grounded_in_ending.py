"""The `EMISSION_GROUNDED_IN_ENDING` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _items,
    _rows,
    _topology,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("EMISSION_GROUNDED_IN_ENDING")
def _emission_grounded_in_ending(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """An announcement must be attached to an ending the act has, and one that completes it.

    A moment names something that happened. Announcing one from an ending that refuses the act
    states something untrue — the business declared exactly that refusal, and nothing read it: no
    rule in the pipeline read an `emit.` property at all, so a design could announce a completion
    from a rejection and be admissible for it.

    Both facts were already declared and neither was joined to the other. `artifact_properties`
    states the site as `emit.<ending>`, and `execution_topology` types every node. **No register is
    added for this** — a second place to state the emission site would be a second producer of one
    truth, and the drift between them would be silent until something read the stale one.

    Site and type are one traversal of one row and are reported once. A property naming an ending
    the act does not have has no type to check, so splitting them would report one wrong row twice.
    That is the same reasoning that keeps act, step and outcome together in
    `DISCHARGE_GROUNDED_IN_TOPOLOGY`, and the reason the discharge's *destination* check is separate
    there is that it reads a different row. This one does not.

    The completing type is read from the topology, never from the ending's name: a name is a
    convention anybody can break by calling an exit something reassuring.
    """
    prefix = rule.params.get("property_prefix", "emit.")
    artifact_column = rule.params.get("artifact_column", "Artifact")
    property_column = rule.params.get("property_column", "Property")
    type_column = rule.params.get("type_column", "Node Type")
    completing = rule.params.get("completing_type", "EXIT_SUCCESS")
    refusing = rule.params.get("refusing_type", "EXIT")
    refusal_property = rule.params.get("refusal_property", "moment")
    refusal_value = rule.params.get("refusal_value", "refusal")

    topology = _topology(doc, rule)
    refusals = {
        _bare_identity(_cell(row, artifact_column)): True
        for _, row in _rows(doc, rule)
        if _cell(row, property_column).strip() == refusal_property
        and _cell(row, "Value").strip() == refusal_value
    }

    out = []
    for i, row in _rows(doc, rule):
        prop = _cell(row, property_column).strip()
        if not prop.startswith(prefix):
            continue
        act = _cell(row, artifact_column)
        ending = prop[len(prefix):].strip()
        if not ending:
            out.append((
                _at(_where(rule), i),
                f"{prop!r} names no ending — an announcement with no site is emitted from nowhere",
            ))
            continue
        node = topology.get((act, ending))
        if node is None:
            declared = sorted(n for a, n in topology if a == act)
            out.append((
                _at(_where(rule), i),
                f"{ending!r} is no node of {act.split('::')[-1]} — it declares "
                f"{', '.join(declared) or 'no nodes'}, and a moment cannot be announced from a "
                f"place the act does not have",
            ))
            continue
        node_type = _cell(node, type_column).strip().upper()
        if node_type == completing:
            continue
        # A refusal is itself something that happened. An act that refuses may announce the
        # refusal, and only that: every moment it announces must be one the design declares a
        # refusal, by property on the moment — never read from the moment's name.
        announced = _items(row, "Value")
        if node_type == refusing and announced and all(
                refusals.get(_bare_identity(m)) for m in announced):
            continue
        out.append((
            _at(_where(rule), i),
            f"{ending!r} is typed {node_type or 'nothing'} — a moment names something that "
            f"happened, so it is announced only from an ending typed {completing}, or from one "
            f"typed {refusing} when every moment announced is declared "
            f"`{refusal_property}: {refusal_value}`",
        ))
    return out
