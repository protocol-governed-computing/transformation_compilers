"""
CT_PURE_EVALUATE_RULES_V0

Pure Capability Transform (Atom)

Purpose:
    Apply a declared rule set to parsed registers and report every rule that failed.

Implementation:
    - Iterates the supplied rule set, dispatching each rule to its check kind
    - Every rule is applied to every document; no short-circuit on first failure, because a
      rule that stops running is a rule that cannot be trusted
    - An unknown check kind raises: a silently skipped rule reports green over an unevaluated
      subject, which is the failure this transform exists to prevent
    - Carries no policy: what is checked and why is declared in the rule set, not here
    - No side effects, no external state

Purity Class: ct_pure
"""

from typing import Any, Dict, List

from runtime.ct_executor import CTExecutionError

from transformation.design.evaluate import dispatch, kinds, place
from transformation.design.evaluate import ParsedDocument
from transformation.design.rules import Rule

ADMISSIBLE = "ADMISSIBLE"
INADMISSIBLE = "INADMISSIBLE"


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Execute CT_PURE_EVALUATE_RULES_V0.

    Inputs:
        header (dict): parsed header fields
        sections (list): parsed document sections
        document_text (str): original document text, for whole-document rules
        rule_set (list): declared rules deciding admissibility
        observed (dict): facts about the composition, keyed by inspection operation
        priors (dict): upstream phase documents, parsed, keyed by phase id

    Outputs:
        verdict (str): ADMISSIBLE or INADMISSIBLE
        findings (list): one entry per failed rule
        rules_evaluated (int): how many rules were applied
    """
    for required in ("header", "sections", "registers", "document_text", "rule_set", "observed",
                     "priors"):
        if required not in inputs:
            raise CTExecutionError(
                f"CT_PURE_EVALUATE_RULES_V0: missing required input {required!r}"
            )

    rule_set = inputs["rule_set"]
    if not isinstance(rule_set, list):
        raise CTExecutionError(
            "CT_PURE_EVALUATE_RULES_V0: 'rule_set' must be a list, "
            f"got {type(rule_set).__name__}"
        )

    doc = ParsedDocument(
        header=inputs["header"],
        sections=inputs["sections"],
        registers=inputs["registers"],
        raw=inputs["document_text"],
        observed=inputs["observed"] or {},
        priors=inputs["priors"] or {},
    )

    findings: List[Dict[str, Any]] = []

    for entry in rule_set:
        rule = Rule.from_mapping(entry)
        try:
            check = dispatch(rule.check)
        except KeyError:
            raise CTExecutionError(
                f"CT_PURE_EVALUATE_RULES_V0: rule {rule.id!r} names unknown check kind "
                f"{rule.check!r}; declared kinds are {kinds()}"
            )
        for at, detail in check(doc, rule):
            findings.append(
                {
                    "code": rule.id,
                    "rule": rule.identity,
                    "locator": place(rule, at),
                    "detail": detail,
                    "intent": rule.intent,
                }
            )

    return {
        "verdict": INADMISSIBLE if findings else ADMISSIBLE,
        "findings": findings,
        "rules_evaluated": len(rule_set),
    }
