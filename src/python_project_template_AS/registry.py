"""Operation registry used to register and lookup operations by name.

The :class:`OperationRegistry` is intentionally minimal: register operations,
retrieve them by name, list registered names, and update from another
registry. It raises :class:`RegistryError` for lookup/registration problems.
"""

from typing import Dict, Iterable

from .operations import Operation
from .exceptions import RegistryError


class OperationRegistry:
    """A simple name->Operation registry.

    Example:
        reg = OperationRegistry()
        reg.register(Operation('add', func, arity=2))
        op = reg.get('add')
    """

    def __init__(self):
        self._ops: Dict[str, Operation] = {}

    def register(self, op: Operation, *, replace: bool = False) -> None:
        """Register an :class:`Operation`.

        Args:
            op: operation instance to register.
            replace: if False (default) raise on duplicate names.
        """

        if op.name in self._ops and not replace:
            raise RegistryError(f"Operation already registered: {op.name}")
        self._ops[op.name] = op

    def get(self, name: str) -> Operation:
        """Return a registered Operation by name.

        Raises:
            RegistryError: if the name is unknown.
        """

        try:
            return self._ops[name]
        except KeyError:
            raise RegistryError(f"Unknown operation: {name}")

    def list_ops(self) -> Iterable[str]:
        """Return a list of registered operation names."""

        return list(self._ops.keys())

    def update(self, other: "OperationRegistry") -> None:
        """Update the registry with operations from another registry."""

        for name in other.list_ops():
            self._ops[name] = other.get(name)
