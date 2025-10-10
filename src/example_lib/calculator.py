"""Calculator that can register and compose operations."""

from typing import Callable, Iterable, List, Any, Optional

from .registry import OperationRegistry
from .operations import Operation
from .exceptions import OperationError


class Calculator:
    """A tiny calculator that uses an OperationRegistry.

    Features:
    - register operations (via registry or helper)
    - apply a named operation to arguments
    - compose a sequence of operations into a single callable
    """

    def __init__(self, registry: Optional[OperationRegistry] = None):
        self.registry = registry or OperationRegistry()

    def register(self, op: Operation, *, replace: bool = False) -> None:
        self.registry.register(op, replace=replace)

    def apply(self, op_name: str, *args) -> Any:
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
        """Compose a sequence of unary operations into a single callable.

        The composed function takes one argument and applies the operations in order.
        Only unary operations (arity == 1) are supported for composition.

        Args:
            ops: iterable of operation names
            left_to_right: if True, apply first op then next (f2(f1(x))).

        Returns:
            callable f(x)
        """

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

    def chain(self, sequence: Iterable[str], initial: Any) -> Any:
        """Apply a mixed sequence of operations to an initial value.

        For binary operations, the operation consumes (current_value, next_input)
        and returns a new current_value. To support binary ops in a chain, the
        sequence should alternate between operation names and provided literals
        (which are interpreted as inputs). Example:

            sequence = ['add', 5, 'sqr']
            chain(sequence, initial=2) -> sqr(add(2,5)) = (2+5)^2

        This is a very small DSL useful for demos.
        """
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
