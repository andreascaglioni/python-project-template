"""Calculator utilities for applying and composing operations.

The :class:`Calculator` provides a thin layer over :class:`OperationRegistry`.
It supports applying named operations, composing unary operations into a
callable, and a small 'chain' helper for mixed sequences of unary/binary
operations used by the examples and tests.

Keep the behaviour minimal: methods raise :class:`OperationError` for
operation-related failures.
"""

from typing import Callable, Iterable, List, Any, Optional, Union

from .registry import OperationRegistry
from .operations import Operation
from .exceptions import OperationError


class Calculator:
    """Thin calculator wrapper around an OperationRegistry.

    Methods:
        register(op, replace=False): Register an Operation.
        apply(op_name, *args): Apply a registered operation.
        compose(ops, left_to_right=True): Compose unary operations.
        chain(sequence, initial): Apply a mixed sequence DSL-style.
    """

    def __init__(self, registry: Optional[OperationRegistry] = None):
        if registry is None:
            self.registry = OperationRegistry()
        else:
            self.registry = registry

    def register(self, op: Operation, *, replace: bool = False) -> None:

        self.registry.register(op, replace=replace)

    def apply(self, op_name: str, *args: Any) -> Any:

        op = self.registry.get(op_name)
        try:
            return op(*args)
        except Exception as exc:
            raise OperationError(
                f"Error applying operation '{op_name}': {exc}"
            ) from exc

    def compose(
        self, ops: Iterable[str], *, left_to_right: bool = True
    ) -> Callable[[Any], Any]:

        op_list: List[Operation] = [self.registry.get(name) for name in ops]
        for op in op_list:
            if op.arity != 1:
                raise OperationError(f"Cannot compose non-unary operation: {op.name}")

        if left_to_right:

            def composed(x):
                val = x
                for op in op_list:
                    val = op(val)
                return val

        else:

            def composed(x):
                val = x
                for op in reversed(op_list):
                    val = op(val)
                return val

        return composed

    def chain(self, sequence: Iterable[Union[str, int]], initial: Any) -> Any:

        seq = list(sequence)
        cur = initial
        i = 0
        while i < len(seq):
            item = seq[i]
            if isinstance(item, str):
                op = self.registry.get(item)
                if op.arity == 1:
                    cur = op(cur)
                    i += 1
                elif op.arity == 2:
                    # expect next item as argument
                    if i + 1 >= len(seq):
                        raise OperationError(
                            f"Operation '{op.name}' expects an additional argument in the sequence"
                        )
                    arg = seq[i + 1]
                    cur = op(cur, arg)
                    i += 2
                else:
                    raise OperationError("Only arity 1 or 2 supported in chain")
            else:
                # literal encountered: treat as updating current value
                cur = item
                i += 1
        return cur
