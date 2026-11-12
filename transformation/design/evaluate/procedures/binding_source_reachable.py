"""The `BINDING_SOURCE_REACHABLE` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

import re

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _content_rows,
    _rows,
    _source,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("BINDING_SOURCE_REACHABLE")
def _binding_source_reachable(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A source rooted at another node must name a node the workflow actually runs.

    `BINDING_SOURCE_UNROOTED` proves a source is a reference rather than a literal. It cannot prove
    the reference resolves: a source naming a contract this workflow never reaches is well-rooted,
    well-formed, and null at execution. One such binding existed in a design that passed every rule.
    """
    topology = rule.params["topology_register"]
    pattern = re.compile(rule.params["pattern"])

    nodes: dict[str, set[str]] = {}
    for _, row in _content_rows(doc.register(topology)):
        nodes.setdefault(_bare_identity(_cell(row, "Workflow")), set()).add(
            _bare_identity(_cell(row, "Node")))

    out = []
    for i, row in _rows(doc, rule):
        owner = _bare_identity(_cell(row, "Owner"))
        if owner not in nodes:
            continue
        for named in sorted(set(pattern.findall(_source(row)))):
            if _bare_identity(named) not in nodes[owner]:
                out.append((
                    _at(_where(rule), i),
                    f"source names {named!r}, which {owner} never runs — well-rooted and unreachable",
                ))
    return out
