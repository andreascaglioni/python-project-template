"""Tiny helper utilities used by the examples and tests.

Only lightweight predicates live here to keep the package dependency-free and
easy to read.
"""

from typing import Any


def is_number(x: Any) -> bool:
    """Return True if ``x`` is an int or float.

    Useful in examples and tests to guard numeric operations.
    """

    return isinstance(x, (int, float))
