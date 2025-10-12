"""Small utilities for the mini calculator library."""

from typing import Any


def is_number(x: Any) -> bool:
    return isinstance(x, (int, float))
