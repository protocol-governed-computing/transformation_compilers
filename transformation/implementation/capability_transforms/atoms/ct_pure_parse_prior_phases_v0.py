"""
CT_PURE_PARSE_PRIOR_PHASES_V0

Pure Capability Transform (Atom)

Purpose:
    Parse the upstream phase documents a phase is judged against, keyed by phase id.

Implementation:
    - Reads supplied text only; never touches the filesystem
    - Parses every prior in one call: a capability contract is a fixed pipeline with no
      iteration, so a step that parsed one prior could never parse two
    - Reports what each document contains and judges nothing; whether a handoff was preserved
      is the rule set's business
    - No side effects, no external state

Purity Class: ct_pure
"""

from typing import Any, Dict

from runtime.ct_executor import CTExecutionError

from transformation.design.read import parse_text


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Execute CT_PURE_PARSE_PRIOR_PHASES_V0.

    Inputs:
        prior_texts (dict): phase id → full text of that phase's document

    Outputs:
        priors (dict): phase id → {header, sections, registers}
    """
    if "prior_texts" not in inputs:
        raise CTExecutionError(
            "CT_PURE_PARSE_PRIOR_PHASES_V0: missing required input 'prior_texts'"
        )

    prior_texts = inputs["prior_texts"]

    if not isinstance(prior_texts, dict):
        raise CTExecutionError(
            "CT_PURE_PARSE_PRIOR_PHASES_V0: 'prior_texts' must be an object keyed by phase id, "
            f"got {type(prior_texts).__name__}"
        )

    priors: Dict[str, Any] = {}
    for phase_id, text in prior_texts.items():
        if not isinstance(text, str):
            raise CTExecutionError(
                f"CT_PURE_PARSE_PRIOR_PHASES_V0: prior {phase_id!r} must be document text, "
                f"got {type(text).__name__}"
            )
        header, sections, registers = parse_text(text)
        priors[phase_id] = {
            "header": header,
            "sections": sections,
            "registers": registers,
        }

    return {"priors": priors}
