"""Operation container and a few example math operations.

The :class:`Operation` is a tiny callable wrapper that validates arity and
delegates to the underlying function. A small set of convenience
instances (ADD, SUB, MUL, DIV, NEG, SQR) are provided for tests/examples.
"""

from dataclasses import dataclass
from typing import Callable, Any

from .exceptions import OperationError


@dataclass
class Operation:
    """Container for a named callable with an expected arity.

    Attributes:
        name: operation name used for registry lookups.
        func: callable implementing the operation.
        arity: number of positional arguments expected by the operation.
    """

    name: str
    func: Callable[..., Any]
    arity: int = 1

    def __call__(self, *args):
        if len(args) != self.arity:
            raise OperationError(
                f"Operation '{self.name}' expects {self.arity} arguments, got {len(args)}"
            )
        return self.func(*args)


# --- Example operations -------------------------------------------------


def add(a, b):
    """Return the sum of two numbers."""

    return a + b


def sub(a, b):
    """Return the difference of two numbers."""

    return a - b


def mul(a, b):
    """Return the product of two numbers."""

    return a * b


def safe_div(a, b):
    """Divide a by b, raising :class:`OperationError` on zero division."""

    try:
        return a / b
    except ZeroDivisionError as e:
        raise OperationError("Division by zero") from e


def neg(a):
    """Return the numeric negation of a value."""

    return -a


def square(a):
    """Return the square of a value."""

    return a * a


# Convenience instances
ADD = Operation("add", add, arity=2)
SUB = Operation("sub", sub, arity=2)
MUL = Operation("mul", mul, arity=2)
DIV = Operation("div", safe_div, arity=2)
NEG = Operation("neg", neg, arity=1)
SQR = Operation("sqr", square, arity=1)
