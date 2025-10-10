import pytest

from example_lib import default_calculator


@pytest.fixture(scope="session")
def calc():
    """Session-scoped default Calculator (requires editable install)."""
    return default_calculator()
