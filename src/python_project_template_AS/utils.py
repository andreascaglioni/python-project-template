"""Tiny helper utilities used by the examples and tests.

Only lightweight predicates live here to keep the package dependency-free and
easy to read.
"""

from typing import Any


def is_number(x: Any) -> bool:
    """Return True if x is int or float."""
    return isinstance(x, (int, float))
