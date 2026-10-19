"""The `CROSS_SUBDOMAIN_REACH_READ_ONLY` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _at,
    _bare_identity,
    _cell,
    _content_rows,
    _runs,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("CROSS_SUBDOMAIN_REACH_READ_ONLY")
def _cross_subdomain_reach_read_only(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """An act reaching into another subdomain may read what it holds and never change it.

    A subdomain owns what it holds, and ownership that does not include being the only writer is not
    ownership. An act may consult another subdomain's records because a second copy of one truth can
    disagree with the thing it describes; it may not change them, because then two subdomains decide
    what is true and neither is answerable for the result.

    Three published facts and no inference: which subdomain owns a contract, which operations that
    contract's steps perform, and whether each of those operations writes. The last of those did not
    exist until it was declared — the operation *names* read as reads and writes, and a rule resting
    on a name is a convention anybody can break by naming an operation well. `idempotent` does not
    answer it either: a last-write-wins write is idempotent.
    """
    artifacts = doc.observed.get(rule.params["artifact_observation"]) or []
    contracts = doc.observed.get(rule.params["contract_observation"]) or []
    capabilities = doc.observed.get(rule.params["capability_observation"]) or []
    if not artifacts or not contracts or not capabilities:
        return [(
            _at(_where(rule)),
            "the composition was not observed — a reach across a subdomain boundary cannot be "
            "checked against subdomains nobody published",
        )]

    # Where each artifact lives. The composition answers for what it already holds; the design
    # answers for what it is authoring, which the composition has never seen.
    subdomain = {_bare_identity(str(a.get("artifact"))): a.get("owner_subdomain")
                 for a in artifacts if isinstance(a, dict)}
    for _, row in _content_rows(doc.register(rule.params["new_register"])):
        code, owner = _bare_identity(_cell(row, "Code")), _cell(row, "Owner Subdomain")
        if code and owner:
            subdomain[code] = owner

    effect = {(str(c.get("capability")), op): spec.get("effect")
              for c in capabilities if isinstance(c, dict)
              for op, spec in (c.get("operations") or {}).items()}

    writes: dict[str, list[tuple[Locator, str]]] = {}
    for contract in contracts:
        if not isinstance(contract, dict):
            continue
        performed = [
            (str(step.get("op")), str(step.get("store")))
            for step in (contract.get("steps") or [])
            if isinstance(step, dict) and step.get("side_effect")
            and effect.get((str(step.get("side_effect")), str(step.get("op")))) == "write"
        ]
        if performed:
            writes[_bare_identity(str(contract.get("contract")))] = performed

    out = []
    for i, row in _content_rows(doc.register(rule.params["topology_register"])):
        if _cell(row, "Node Type").upper() != "CC":
            continue
        workflow, node = _bare_identity(_cell(row, "Workflow")), _runs(row)
        here, there = subdomain.get(workflow), subdomain.get(node)
        # An unplaced artifact is another rule's finding. Reporting it here too would say the same
        # thing twice and say it less clearly.
        if not here or not there or here == there:
            continue
        for op, store in writes.get(node, []):
            out.append((
                _at(rule.params['topology_register'], i),
                f"{workflow} is in {here} and reaches {node} in {there}, which performs {op} on "
                f"{store}. A subdomain may read what another holds and never change it — the owner "
                f"of a record is the only writer of it",
            ))
    return out
