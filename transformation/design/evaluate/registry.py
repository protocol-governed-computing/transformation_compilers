"""The closed registry of check kinds. An unknown kind fails hard, never a skipped rule."""

from __future__ import annotations

from typing import Any, Callable

from transformation.design.evaluate.document import ParsedDocument


# Where a finding is: `{register, row, field}`, each `None` when the finding cannot place it.
Locator = dict[str, Any]


CheckFn = Callable[[ParsedDocument, "object"], list[tuple[Locator, str]]]


_REGISTRY: dict[str, CheckFn] = {}


def check(kind: str) -> Callable[[CheckFn], CheckFn]:
    def register(fn: CheckFn) -> CheckFn:
        if kind in _REGISTRY:
            raise KeyError(f"duplicate check kind: {kind}")
        _REGISTRY[kind] = fn
        return fn

    return register


def dispatch(kind: str) -> CheckFn:
    """Resolve a check kind, or fail hard."""
    if kind not in _REGISTRY:
        raise KeyError(
            f"unknown check kind {kind!r}; declared kinds are {sorted(_REGISTRY)}"
        )
    return _REGISTRY[kind]


def kinds() -> list[str]:
    return sorted(_REGISTRY)
