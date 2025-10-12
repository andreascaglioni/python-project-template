"""Definition of Operation and a handful of example math operations."""

from dataclasses import dataclass
from typing import Callable, Any

from .exceptions import OperationError


@dataclass
class Operation:
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
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise OperationError("Division by zero") from e


def neg(a):
    return -a


def square(a):
    return a * a


# Convenience instances
ADD = Operation("add", add, arity=2)
SUB = Operation("sub", sub, arity=2)
MUL = Operation("mul", mul, arity=2)
DIV = Operation("div", safe_div, arity=2)
NEG = Operation("neg", neg, arity=1)
SQR = Operation("sqr", square, arity=1)
