"""
CT_PURE_MEASURE_COMPLETENESS_V0

Pure Capability Transform (Atom)

Purpose:
    Measure whether a design uniquely determines the artifacts it specifies, and refuse when it
    does not.

Implementation:
    - Derives the requirement list from what the renderer emits, so it cannot drift from
      construction
    - Reads where each value came from in the provenance it is handed, the attribution step's
      output, rather than deriving origins a second time
    - Raises when completeness is below the declared threshold: UNIQUELY_DETERMINED_OR_STOP is a
      refusal, not a report, and the runtime maps a raise to VIOLATION
    - No side effects, no external state

Purity Class: ct_pure
"""

from typing import Any, Dict

from runtime.ct_executor import CTExecutionError

from transformation.build.completeness import measure


def _registers(parsed: list) -> Dict[str, list]:
    """Parsed register entries as the id → rows mapping construction reads."""
    return {entry["id"]: entry["value"] if isinstance(entry.get("value"), list) else []
            for entry in parsed or []}


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Execute CT_PURE_MEASURE_COMPLETENESS_V0.

    Inputs:
        design_registers (list): parsed P7 registers
        mandate_registers (list): parsed P8 registers
        threshold (number): minimum Construction Completeness, 0-100
        provenance (dict): where each rendered value came from, keyed `<code>.<path>`, as
            CT_PURE_ATTRIBUTE_PROVENANCE_V0 reports it. A leaf it does not name was stated by the
            design. The measure reads it and derives no origin of its own.

    Outputs:
        completeness (float): percentage of required facts the design determines
        determined (int): facts the design states
        required (int): facts construction needs
        undetermined (list): the facts it does not state, by field
    """
    for required in ("design_registers", "mandate_registers", "threshold", "provenance"):
        if required not in inputs:
            raise CTExecutionError(
                f"CT_PURE_MEASURE_COMPLETENESS_V0: missing required input {required!r}"
            )

    result = measure(_registers(inputs["design_registers"]),
                     _registers(inputs["mandate_registers"]),
                     inputs["provenance"] or {})
    threshold = float(inputs["threshold"])

    if not result.meets(threshold):
        # A design that does not determine its artifacts is one construction would have to invent
        # design for, and a generator that invents design is a second, ungoverned design authority.
        raise CTExecutionError(
            f"CT_PURE_MEASURE_COMPLETENESS_V0: Construction Completeness "
            f"{result.percentage:.1f}% is below the required {threshold:.1f}% — "
            f"{result.total - result.determined} fact(s) undetermined: "
            f"{', '.join(sorted(result.undetermined))}"
        )

    return {
        "completeness": round(result.percentage, 2),
        "determined": result.determined,
        "required": result.total,
        "undetermined": sorted(result.undetermined),
    }
