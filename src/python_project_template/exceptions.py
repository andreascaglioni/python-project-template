"""Custom exceptions for the mini calculator library."""


class CalculatorError(Exception):
    """Base class for calculator-related errors."""


class OperationError(CalculatorError):
    """Raised when an operation fails (e.g. wrong arity or invalid input)."""


class RegistryError(CalculatorError):
    """Raised for registry problems (duplicate name, not found)."""
