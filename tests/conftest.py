import pytest

from python_project_template_AS import default_calculator


@pytest.fixture(scope="session")
def calc():
    """Session-scoped default Calculator (requires editable install)."""
    return default_calculator()
