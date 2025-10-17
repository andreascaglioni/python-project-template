"""Custom exceptions used across the mini calculator package.

All exceptions inherit from :class:`CalculatorError` so callers may catch the
base class for broad error handling. Use the more specific subclasses for
programmatic checks in tests or higher-level code.
"""


class CalculatorError(Exception):
    """Base class for calculator-related errors.

    Use this as the top-level exception when handling errors coming from the
    package.
    """


class OperationError(CalculatorError):
    """Raised when an operation fails (wrong arity, invalid input, etc.)."""


class RegistryError(CalculatorError):
    """Raised for registry problems (duplicate name, not found)."""
