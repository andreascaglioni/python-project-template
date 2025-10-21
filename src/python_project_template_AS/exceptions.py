"""Custom exceptions used across the mini calculator package.

All exceptions inherit from :class:`CalculatorError` so callers may catch the
base class for broad error handling. Use the more specific subclasses for
programmatic checks in tests or higher-level code.
"""


class CalculatorError(Exception):
    """Base exception for calculator errors."""


class OperationError(CalculatorError):
    """Raised for operation failures (e.g., wrong arity, invalid input)."""


class RegistryError(CalculatorError):
    """Raised for registry errors (duplicate or missing name)."""
