"""python-project-template: mini math utility library

Exports:
- Operation, Operation registry, Calculator, convenience operations
"""

from .exceptions import CalculatorError, OperationError, RegistryError
from .operations import Operation, ADD, SUB, MUL, DIV, NEG, SQR
from .registry import OperationRegistry
from .calculator import Calculator
from .utils import is_number

__all__ = [
    "CalculatorError",
    "OperationError",
    "RegistryError",
    "Operation",
    "OperationRegistry",
    "Calculator",
    "ADD",
    "SUB",
    "MUL",
    "DIV",
    "NEG",
    "SQR",
    "is_number",
]

# Provide a default registry populated with common ops
_default_registry = OperationRegistry()
for op in (ADD, SUB, MUL, DIV, NEG, SQR):
    _default_registry.register(op)


# Convenience constructor using default registry
def default_calculator() -> Calculator:
    return Calculator(registry=_default_registry)
