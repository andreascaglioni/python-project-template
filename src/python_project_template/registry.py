"""Registry for operations: register, lookup, decorator support."""

from typing import Dict, Iterable

from .operations import Operation
from .exceptions import RegistryError


class OperationRegistry:
    """A simple name->Operation registry.

    Usage:
        reg = OperationRegistry()
        reg.register(Operation(...))
        op = reg.get('add')
    """

    def __init__(self):
        self._ops: Dict[str, Operation] = {}

    def register(self, op: Operation, *, replace: bool = False) -> None:
        if op.name in self._ops and not replace:
            raise RegistryError(f"Operation already registered: {op.name}")
        self._ops[op.name] = op

    def get(self, name: str) -> Operation:
        try:
            return self._ops[name]
        except KeyError:
            raise RegistryError(f"Unknown operation: {name}")

    def list_ops(self) -> Iterable[str]:
        return list(self._ops.keys())

    def update(self, other: "OperationRegistry") -> None:
        """Update the registry with operations from another registry."""
        for name in other.list_ops():
            self._ops[name] = other.get(name)
