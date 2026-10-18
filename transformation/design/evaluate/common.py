"""What every check kind reads with: locating a register, reading a cell, placing a finding."""

from __future__ import annotations

from typing import Any

from transformation.design.evaluate.document import Block, ParsedDocument
from transformation.design.evaluate.registry import Locator
from transformation.design.schema import column_key


# Helpers ----------------------------------------------------------------------------------


def _block(doc: ParsedDocument, rule) -> Block | None:
    """Locate what a rule governs.

    A register identity wins when the rule declares one — it is stable across retitling and
    unambiguous when a section holds several registers. Section-title matching remains for P0,
    whose template carries no register markers.
    """
    register = getattr(rule, "register", None)
    if register:
        found = doc.register(register)
        if found is not None:
            return found
        # Fall through: a document with no register markers (P0, and any hand-authored register
        # predating the template salvage) is still addressable by section title. Returning None
        # here would report every register missing rather than checking it.
    return doc.find(rule.section_title) if rule.section_title else None


def _where(rule) -> str:
    return getattr(rule, "register", None) or rule.section_title or "document"


def _at(register: str, row: int | str | None = None, field: str | None = None) -> dict:
    """Where a finding is: the register, the row by ordinal or by the key it is named by, and the
    field. What the finding cannot place stays `None`."""
    return {"register": register, "row": row, "field": field}


def place(rule, locator: Locator) -> Locator:
    """A check's locator, with the field filled from the rule when the rule is about one column."""
    column = rule.params.get("column") if isinstance(rule.params, dict) else None
    if locator["field"] is None and locator["row"] is not None and isinstance(column, str):
        return {**locator, "field": column_key(column)}
    return locator


def _value(row: dict, column: str) -> Any:
    """A cell as the row holds it, addressed by its column's title through the schema's key."""
    return row.get(column_key(column))


def _cell(row: dict, column: str) -> str:
    """A text cell, stripped. A cell that says nothing (`null`) or is absent reads as empty."""
    value = _value(row, column)
    if value is None:
        return ""
    if isinstance(value, (list, dict)):
        raise TypeError(f"column {column!r} holds structure; read it with _value")
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value).strip()


def _items(row: dict, column: str) -> list[str]:
    """A cell as the names it states: a list's entries, a text's one value, or none."""
    value = _value(row, column)
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, dict):
        return []
    return [str(value).strip()] if str(value).strip() else []


def _runs(row: dict[str, str]) -> str:
    """The contract a topology node runs: its `Runs`, or the node itself when that is blank.

    A node is named by its contract's code unless the workflow runs that contract at more than one
    place. Then each place is a key, and `Runs` names the contract. Anything read from a contract —
    its interface, its reach, its writes — is read through this; anything that names a place in the
    graph — routing, bindings, discharges — names the key.
    """
    return _bare_identity(_cell(row, "Runs") or _cell(row, "Node"))


def _source(row: dict) -> str:
    """A binding's source when it names a place: the path it reads. A literal, the generated marker
    and a binding that states nothing name no place, and read as empty."""
    value = _value(row, "Bound To")
    return value.strip() if isinstance(value, str) else ""


def _cited(row: dict, column: str) -> list[dict]:
    """The citations a cell states, each a mapping. A cell that says nothing cites nothing, and one
    that is not a citation is the type rule's to refuse, so neither is read here."""
    value = _value(row, column)
    if isinstance(value, dict):
        return [value]
    if isinstance(value, list):
        return [c for c in value if isinstance(c, dict)]
    return []


def _content_rows(block: Block | None):
    """The numbered rows of a register block."""
    if block is None or block.table is None:
        return []
    return list(enumerate(block.table.rows, start=1))


def _rows(doc: ParsedDocument, rule):
    """Content rows of the register a rule governs."""
    return _content_rows(_block(doc, rule))


def _normalise(text: str) -> str:
    return " ".join(text.split())


def _bare_identity(value: str) -> str:
    """An identity without its namespace.

    One register writes `book_library_mgmt::WF_SEARCH_CATALOG_V0` and another writes the same
    workflow as a bare code; both name one artifact, and a coverage check that distinguished them
    would report every row uncovered.
    """
    return _normalise(value).split("::")[-1]


def _routing(value: Any) -> dict[str, str]:
    """A node's routing, outcome → destination. A terminal node routes nowhere and states nothing.
    A routing that did not structure is `CELL_NOT_OF_TYPE`'s finding, and reads here as no routes."""
    if not isinstance(value, dict):
        return {}
    return {str(k).strip(): str(v).strip() for k, v in value.items()}


def _topology(doc: ParsedDocument, rule):
    """The design's own topology, indexed by (workflow, node).

    Both discharge kinds read it, and both read it the same way: a discharge is grounded in the
    design that states it, never in the composition. Nothing here observes a snapshot.
    """
    register = rule.params.get("topology_register", "execution_topology")
    workflow_column = rule.params.get("workflow_column", "Workflow")
    node_column = rule.params.get("node_column", "Node")
    return {
        (_cell(row, workflow_column), _cell(row, node_column)): row
        for _, row in _content_rows(doc.register(register))
    }


def _composition_steps(doc: ParsedDocument, register: str):
    """(owner, step) -> the step's declared row, from a phase's capability composition."""
    block = doc.register(register)
    if block is None or block.table is None:
        return {}
    return {(_bare_identity(_cell(r, "CC Code")), _cell(r, "Step Name")): r
            for _, r in _content_rows(block)}


def _interface_map(value: Any, side: str) -> dict[str, str]:
    """One side of a step's Interface, `in` or `out`, as capability name → design name.

    The left of each pair is the capability's own name for the value, which is the only half a
    contract can be held to; the right is what the design calls it, which is the design's business.
    """
    if not isinstance(value, dict) or not isinstance(value.get(side), dict):
        return {}
    return {str(k).strip(): str(v or "").strip() for k, v in value[side].items()}


def _binding_stores(observed: list) -> dict[str, set[str]]:
    """`binding -> the store keys it covers`, inverted from the surface that answers every store.

    The surface is keyed by store because that is what it lists; the question a reach asks is keyed
    by binding. Inverting here rather than publishing it inverted keeps the projection a projection.
    """
    out: dict[str, set[str]] = {}
    for entry in observed:
        if not isinstance(entry, dict):
            continue
        key = str(entry.get("key") or "")
        for binding in entry.get("bindings") or []:
            out.setdefault(_bare_identity(str(binding)), set()).add(key)
    return out


def _store_keys(observed: list) -> dict[str, str]:
    """`bare store name -> its one key`, and nothing for a name two domains both declare.

    A design names a store by its bare name. Where that name is ambiguous the design has not said
    which store it means, and guessing would attribute a read to the wrong domain — so the name
    resolves to nothing and the rules that need it stay silent about it.
    """
    seen: dict[str, list[str]] = {}
    for entry in observed:
        if isinstance(entry, dict) and entry.get("store"):
            seen.setdefault(str(entry["store"]), []).append(str(entry.get("key") or ""))
    return {name: keys[0] for name, keys in seen.items() if len(keys) == 1}


def _act_stores(doc: ParsedDocument, rule, keys: dict[str, str]) -> dict[str, set[str]]:
    """`act -> the store keys the steps it runs address`.

    Read from the composition for a contract that already exists and from the design's own
    composition for one it authors, because an act's reads are what the change is judged on and half
    of them may not be built yet.
    """
    contracts: dict[str, set[str]] = {}
    for entry in doc.observed.get(rule.params["contract_observation"]) or []:
        if not isinstance(entry, dict):
            continue
        stores = {keys[s] for step in entry.get("steps") or []
                  if (s := str(step.get("store") or "")) in keys}
        contracts[_bare_identity(str(entry.get("contract")))] = stores

    for (owner, _), row in _composition_steps(doc, rule.params["composition_register"]).items():
        store = _cell(row, "Store")
        if store in keys:
            contracts.setdefault(owner, set()).add(keys[store])

    out: dict[str, set[str]] = {}
    block = doc.register(rule.params["topology_register"])
    for _, row in _content_rows(block) if block is not None else []:
        act = _bare_identity(_cell(row, "Workflow"))
        node = _runs(row)
        if node in contracts:
            out.setdefault(act, set()).update(contracts[node])
    return out


def _declared_reach(doc: ParsedDocument, rule) -> dict[str, set[str]]:
    """`act -> the bindings its design says it consults`."""
    out: dict[str, set[str]] = {}
    block = doc.register(rule.params["register"])
    for _, row in _content_rows(block) if block is not None else []:
        act = _bare_identity(_cell(row, "Act"))
        for binding in _items(row, "Consults"):
            out.setdefault(act, set()).add(_bare_identity(binding))
    return out
