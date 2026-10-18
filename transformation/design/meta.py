"""Meta-validation — governance validating governance, before it judges a document.

The design compiler's split is declaration in the register schemas, mechanism in `evaluate/`. That split is
only worth having if the two halves are held in correspondence, and nothing held them: a rule could
name a check kind that no longer exists, pass a parameter no check reads, or omit one every check
path requires, and none of it surfaces until a dossier happens to reach that rule. A mechanism could
lose its last caller and stay in the registry forever, read as governance that is no longer in
force.

This is the same property `INVARIANT_ASSERT_PARITY_V0` asserts for the platform surface — every
declaration enforceable, every enforcement declared — applied to the layer where design rules are
declared. It is meta-governance: it validates the rule sets, never a document, and it must pass
before a verdict over any document means anything. A rule that cannot run reports green over an
unevaluated subject, which is the vacuity failure this codebase exists to refuse.

**A check kind's parameter contract is read from its implementation, not restated.** Restating it
would produce a second declaration that can disagree with the tested one — the same reasoning that
put structural rules in `derive.py` rather than in nine phase modules. A parameter subscripted
unconditionally is required; one read through `.get`, or subscripted inside a branch or an
alternation, is optional. So the contract cannot drift from the code that implements it.
"""

from __future__ import annotations

import ast
import inspect
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from inspector import api

from transformation.design import catalog
from transformation.design.families import AUTHORABLE, BY_CODE
from transformation.design.evaluate import common, constructs, keywords, registry
from transformation.design.evaluate import procedures
from transformation.design.evaluate import kinds as declared_kinds
from transformation.design.rule_sets import PhaseRules
from transformation.design.rules import Rule

# A subscript under one of these is reached only on some paths, so the rule that omits it is not
# thereby broken. `BoolOp` covers the `params.get(a) or params[b]` alternation — b is required only
# when a is absent.
_CONDITIONAL = (ast.If, ast.IfExp, ast.BoolOp, ast.Try, ast.While)


@dataclass(frozen=True)
class MetaFinding:
    """One correspondence defect between what is declared and what is enforced."""

    code: str
    where: str
    detail: str

    def __str__(self) -> str:
        return f"[{self.code}] {self.where}: {self.detail}"


@dataclass(frozen=True)
class ParamContract:
    """What a check kind reads out of a rule's `params`."""

    required: frozenset[str]
    optional: frozenset[str]

    @property
    def known(self) -> frozenset[str]:
        return self.required | self.optional


def _params_read(node: ast.AST, functions: dict[str, ast.FunctionDef]) -> tuple[set[str], set[str], set[str]]:
    """Parameter names one function body reads directly, plus the module functions it calls.

    Returns (unconditionally required, optional, callees). A check kind's full contract is the
    union over its call graph — helpers in `evaluate/` read `params` on their caller's behalf,
    and a contract that stopped at the decorated function would miss them.
    """
    required: set[str] = set()
    optional: set[str] = set()
    callees: set[str] = set()

    def visit(parent: ast.AST, conditional: bool) -> None:
        for child in ast.iter_child_nodes(parent):
            reached_conditionally = conditional or isinstance(parent, _CONDITIONAL)
            name = _subscripted_param(child)
            if name is not None:
                (optional if reached_conditionally else required).add(name)
            if isinstance(child, ast.Call):
                got = _param_get(child)
                if got is not None:
                    optional.add(got)
                if isinstance(child.func, ast.Name) and child.func.id in functions:
                    callees.add(child.func.id)
            visit(child, reached_conditionally)

    visit(node, False)
    return required, optional, callees


def _is_params(node: ast.AST) -> bool:
    """Whether an expression is a rule's `params` mapping.

    Both idioms count: `rule.params` and the defensive `getattr(rule, "params", {})`. A contract
    blind to the second would call a parameter unknown that a check reads every run.
    """
    if isinstance(node, ast.Attribute) and node.attr == "params":
        return True
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "getattr"
        and len(node.args) >= 2
        and isinstance(node.args[1], ast.Constant)
        and node.args[1].value == "params"
    )


def _subscripted_param(node: ast.AST) -> str | None:
    """`params["name"]` — the name, or None."""
    if isinstance(node, ast.Subscript) and _is_params(node.value) and isinstance(node.slice, ast.Constant):
        return node.slice.value
    return None


def _param_get(node: ast.Call) -> str | None:
    """`params.get("name", ...)` — the name, or None."""
    func = node.func
    if isinstance(func, ast.Attribute) and func.attr == "get" and _is_params(func.value):
        if node.args and isinstance(node.args[0], ast.Constant):
            return node.args[0].value
    return None


def _check_kind(node: ast.FunctionDef) -> str | None:
    """The kind a `@check("...")`-decorated function implements."""
    for decorator in node.decorator_list:
        if (
            isinstance(decorator, ast.Call)
            and isinstance(decorator.func, ast.Name)
            and decorator.func.id == "check"
            and decorator.args
            and isinstance(decorator.args[0], ast.Constant)
        ):
            return decorator.args[0].value
    return None


def param_contracts() -> dict[str, ParamContract]:
    """Read every check kind's parameter contract out of the evaluator's own source."""
    sources = [registry, common, keywords, constructs] + [
        getattr(procedures, name) for name in sorted(vars(procedures))
        if inspect.ismodule(getattr(procedures, name)) and getattr(procedures, name).__name__.startswith(procedures.__name__ + ".")]
    functions = {n.name: n for module in sources
                 for n in ast.parse(inspect.getsource(module)).body if isinstance(n, ast.FunctionDef)}

    def contract(name: str, seen: tuple[str, ...] = ()) -> tuple[set[str], set[str]]:
        if name in seen:  # a cycle contributes nothing it has not already contributed
            return set(), set()
        required, optional, callees = _params_read(functions[name], functions)
        for callee in callees:
            inherited_required, inherited_optional = contract(callee, seen + (name,))
            required |= inherited_required
            optional |= inherited_optional
        return required, optional

    contracts: dict[str, ParamContract] = {}
    for name, node in functions.items():
        kind = _check_kind(node)
        if kind is None:
            continue
        required, optional = contract(name)
        # A name read both ways is optional: the subscript is the guarded arm of its own `.get`.
        contracts[kind] = ParamContract(frozenset(required - optional), frozenset(optional))
    return contracts


def verify(rule_sets: dict[str, PhaseRules]) -> list[MetaFinding]:
    """Assert the declaration/enforcement correspondence across every phase's rule set.

    `rule_sets` is always supplied — for the same reason `oracle.evaluate` takes its rules. A
    default here would silently verify eight phases and report a confident verdict over nine.
    """
    contracts = param_contracts()
    findings: list[MetaFinding] = []
    referenced_kinds: set[str] = set()

    # A phase the catalogue declares but nothing judges is the vacuity failure one level up: the
    # pipeline reports a phase exists and no rule ever runs against its document.
    for spec in catalog.PHASES:
        if spec.id not in rule_sets:
            findings.append(
                MetaFinding(
                    "PHASE_RULE_SET_MISSING",
                    f"catalog/{spec.id}",
                    f"is declared in the phase catalogue ({spec.purpose}) but no rule set is "
                    f"composed for it — its document would be admitted unjudged",
                )
            )
    # A template's Family vocabulary is a copy of the family declaration, and the copies had already
    # drifted — P5 admitted no VOCAB where P7 did, so a design could name a family its own intent
    # phase had refused. The vocabulary is authored in the template and cannot be generated from
    # here, so it is asserted instead.
    for phase_id, phase in sorted(rule_sets.items()):
        for register in phase.shape.registers:
            declared = register.vocabularies.get("Family")
            if not declared:
                continue
            unknown = sorted(set(declared) - set(BY_CODE))
            missing = sorted(set(AUTHORABLE) - set(declared))
            for code in unknown:
                findings.append(MetaFinding(
                    "TEMPLATE_FAMILY_UNDECLARED",
                    f"{phase_id}/{register.id}",
                    f"admits family {code!r}, which design.families does not declare",
                ))
            for code in missing:
                findings.append(MetaFinding(
                    "TEMPLATE_FAMILY_MISSING",
                    f"{phase_id}/{register.id}",
                    f"does not admit family {code!r}, which is declared authorable — a design "
                    f"could not name it even though construction can build one",
                ))

    for phase_id in sorted(set(rule_sets) - {spec.id for spec in catalog.PHASES}):
        findings.append(
            MetaFinding(
                "PHASE_UNDECLARED",
                f"rules/{phase_id}",
                "composes a rule set for a phase the catalogue does not declare",
            )
        )

    for phase_id, phase in sorted(rule_sets.items()):
        rules: list[Rule] = phase.rule_set()
        for rule in rules:
            where = f"{phase_id}/{rule.id}"
            referenced_kinds.add(rule.check)

            if rule.check not in contracts:
                findings.append(
                    MetaFinding(
                        "CHECK_KIND_UNDECLARED",
                        where,
                        f"names check kind {rule.check!r}, which no mechanism in the evaluator "
                        f"implements — the rule cannot run",
                    )
                )
                continue

            contract = contracts[rule.check]
            for name in sorted(set(rule.params) - contract.known):
                findings.append(
                    MetaFinding(
                        "RULE_PARAM_UNREAD",
                        where,
                        f"passes {name!r} to {rule.check}, which never reads it — the parameter "
                        f"is inert and the rule does not govern what its author declared",
                    )
                )
            for name in sorted(contract.required - set(rule.params)):
                findings.append(
                    MetaFinding(
                        "RULE_PARAM_MISSING",
                        where,
                        f"omits {name!r}, which {rule.check} requires on every path — the rule "
                        f"raises rather than judges as soon as a document reaches it",
                    )
                )

            if not rule.intent:
                findings.append(
                    MetaFinding(
                        "RULE_INTENT_MISSING",
                        where,
                        "declares no intent — a finding nobody can read the reason for is a "
                        "rule nobody can review",
                    )
                )

            if rule.register and rule.section_title:
                findings.append(
                    MetaFinding(
                        "RULE_TARGET_AMBIGUOUS",
                        where,
                        "declares both a register identity and a section title; the register "
                        "wins and the title is never consulted",
                    )
                )

    for kind in sorted(set(declared_kinds()) - referenced_kinds):
        findings.append(
            MetaFinding(
                "CHECK_KIND_ORPHANED",
                f"evaluate/{kind}",
                "is implemented but no declared rule invokes it — enforcement without a "
                "declaration reads as governance that is not in force",
            )
        )

    return findings


# Closure ----------------------------------------------------------------------------------------

DESIGN_LANGUAGE = Path(__file__).resolve().parents[2] / "doc" / "DESIGN_LANGUAGE.md"
# The constitution naming the invariants a phase's rules must realise. The construction invariants
# are realised by construction, not by a register schema, and are not asked of it.
DESIGN_CONSTITUTION = "lifecycle::CONSTITUTION_CHANGE_MGMT_V0"
# The constitution naming the invariants construction realises, each specified by a section of the
# construction mapping standard.
CONSTRUCTION_CONSTITUTION = "lifecycle::CONSTITUTION_CONSTRUCTION_V0"
CONSTRUCTION_MAPPING = DESIGN_LANGUAGE.parent / "CONSTRUCTION_MAPPING.md"
TEMPLATES = Path(__file__).resolve().parents[1] / "templates"
STATEMENT = "DESIGN_LANGUAGE.md#"


def _machine(content: str) -> dict:
    found = re.search(r"^```yaml\n(.*?)^```", content, re.M | re.S)
    return yaml.safe_load(found.group(1)) if found else {}


def _artifact(fqdn: str, snapshot_root: str) -> dict | None:
    status, artifact = api.query("si.artifact.show", {"artifact": fqdn}, snapshot_root)
    return artifact if status == "SUCCESS" else None


def _statements() -> set[str]:
    """The procedures DESIGN_LANGUAGE states, by the anchor of their heading."""
    text = DESIGN_LANGUAGE.read_text(encoding="utf-8")
    return {m.lower() for m in re.findall(r"^#### ([A-Z0-9_]+)$", text, re.M)}


def _template(phase_id: str) -> str:
    """A phase's template, as the dispatch names it."""
    from transformation.design.catalog import phase

    return (TEMPLATES / phase(phase_id).template).read_text(encoding="utf-8")


def closure(rule_sets: dict[str, PhaseRules], snapshot_root: str) -> list[MetaFinding]:
    """Assert that the rule sets close over the governance they realise.

    - every `x-realises` resolves: to an invariant the composition carries and the design
      constitution names, or to a statement in DESIGN_LANGUAGE;
    - every invariant the design constitution names is realised by some rule;
    - every template's Machine skeleton names exactly its schema's registers, with the same keys,
      and a header the schema declares;
    - every rule set is the last revision its schema records;
    - every construction invariant has its section in the construction mapping standard.

    That every check kind is used, and every rule's kind exists, `verify` asserts.
    """
    from transformation.design.expand import DERIVED_REALISES, derived_rules

    findings: list[MetaFinding] = []
    constitution = _artifact(DESIGN_CONSTITUTION, snapshot_root)
    if constitution is None:
        return [MetaFinding("CONSTITUTION_UNREADABLE", DESIGN_CONSTITUTION,
                            f"is not in the composition at {snapshot_root}, so nothing can be closed over it")]
    # The constitution's rules name its invariants and its gates; a gate is enforced by process.
    in_force = {r["enforced_by"] for r in _machine(constitution["canonical"]["content"]).get("rules", [])
                if str(r.get("enforced_by", "")).startswith("lifecycle::INVARIANT_")}
    statements = _statements()
    realised: set[str] = set()

    for phase_id, phase in sorted(rule_sets.items()):
        realised |= {DERIVED_REALISES[r.check] for r in derived_rules(phase.shape) if r.check in DERIVED_REALISES}
        for index, entry in enumerate(phase.shape.entries):
            target = entry.get("x-realises")
            if target is None:
                continue
            where = f"{phase_id}/allOf/{index}"
            if target.startswith(STATEMENT):
                if target[len(STATEMENT):] not in statements:
                    findings.append(MetaFinding("STATEMENT_UNRESOLVED", where,
                                                f"realises {target}, which DESIGN_LANGUAGE does not state"))
            elif target not in in_force:
                findings.append(MetaFinding("INVARIANT_NOT_IN_FORCE", where,
                                            f"realises {target}, which {DESIGN_CONSTITUTION} does not name"))
            else:
                realised.add(target)

    for fqdn in sorted(in_force):
        if _artifact(fqdn, snapshot_root) is None:
            findings.append(MetaFinding("INVARIANT_UNRESOLVED", fqdn,
                                        f"is named by {DESIGN_CONSTITUTION} but is not in the composition"))
        elif fqdn not in realised:
            findings.append(MetaFinding("INVARIANT_UNREALISED", fqdn,
                                        "is in force, and no rule of any phase realises it"))

    construction = _artifact(CONSTRUCTION_CONSTITUTION, snapshot_root)
    if construction is None:
        findings.append(MetaFinding("CONSTITUTION_UNREADABLE", CONSTRUCTION_CONSTITUTION,
                                    f"is not in the composition at {snapshot_root}"))
    else:
        sections = set(re.findall(r"^#### ([A-Z0-9_]+)$", CONSTRUCTION_MAPPING.read_text(encoding="utf-8"), re.M))
        for rule in _machine(construction["canonical"]["content"]).get("rules", []):
            fqdn = str(rule.get("enforced_by", ""))
            name = re.sub(r"^lifecycle::INVARIANT_|_V\d+$", "", fqdn)
            if fqdn.startswith("lifecycle::INVARIANT_") and name not in sections:
                findings.append(MetaFinding("CONSTRUCTION_INVARIANT_UNSPECIFIED", fqdn,
                                            "is in force, and CONSTRUCTION_MAPPING.md specifies nothing that realises it"))

    from transformation.design.effectivity import unrecorded

    for phase_id, phase in sorted(rule_sets.items()):
        reason = unrecorded(phase.shape, phase.rule_set())
        if reason:
            findings.append(MetaFinding("REVISION_UNRECORDED", phase_id, reason))

    for phase_id, phase in sorted(rule_sets.items()):
        skeleton = _machine(_template(phase_id))
        template = {rid: tuple(value[0]) if isinstance(value, list) and value else ()
                    for rid, value in (skeleton.get("registers") or {}).items()}
        schema = {r.id: tuple(r.keys) for r in phase.shape.registers}
        header = set(skeleton.get("document") or {})
        if not set(phase.shape.document_required) <= header <= set(phase.shape.document):
            findings.append(MetaFinding("TEMPLATE_SCHEMA_DISAGREE", f"{phase_id}/document",
                                        f"the template's header {sorted(header)} is not the schema's "
                                        f"{sorted(phase.shape.document)}"))
        for register in sorted(set(template) ^ set(schema)):
            side = "template" if register in template else "schema"
            findings.append(MetaFinding("TEMPLATE_SCHEMA_DISAGREE", f"{phase_id}/{register}",
                                        f"is declared only by the {side}"))
        for register in sorted(set(template) & set(schema)):
            if template[register] != schema[register]:
                findings.append(MetaFinding("TEMPLATE_SCHEMA_DISAGREE", f"{phase_id}/{register}",
                                            f"the template's columns {list(template[register])} are not the "
                                            f"schema's {list(schema[register])}"))
    return findings
