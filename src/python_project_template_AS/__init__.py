"""Top-level package for python_project_template_AS.

This package exposes the core types and a small set of convenience symbols
for the mini calculator demo project.

Module layout (concise):
- exceptions: error classes
- operations: Operation class and example operations
- registry: OperationRegistry for registering operations
- calculator: Calculator class to apply/compose operations
- utils: tiny helper functions

The exported symbols are intentionally small and stable for tests and
examples. Use :func:`default_calculator` to quickly get a Calculator pre-
populated with common operations.
"""

from .exceptions import CalculatorError, OperationError, RegistryError
from .operations import Operation, ADD, SUB, MUL, DIV, NEG, SQR
from .registry import OperationRegistry
from .calculator import Calculator
from .utils import is_number
from importlib.metadata import version

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

__version__ = version("python-project-template-AS")

# Default registry pre-populated with a few convenience operations.
_default_registry = OperationRegistry()
for op in (ADD, SUB, MUL, DIV, NEG, SQR):
    _default_registry.register(op)


def default_calculator() -> Calculator:
    """Create a Calculator using the package default registry.

    Returns:
        Calculator: a calculator with common operations already registered.
    """

    return Calculator(registry=_default_registry)
