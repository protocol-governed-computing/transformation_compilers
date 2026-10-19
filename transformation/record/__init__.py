"""Baseline designs: each registry's P7 and P8 of record, generated from the registry.

    python -m transformation.record <registry> <design dir> [--generated GENERATOR CODE...]

writes `p7_design_intent_<domain>_baseline.md` and `p8_authoring_mandate_<domain>_baseline.md` into
the design directory. Construction of the pair reproduces the registry; `construction_acceptance`
asks whether it does.
"""
