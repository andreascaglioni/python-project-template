import pytest

from python_project_template_AS.registry import OperationRegistry
from python_project_template_AS.operations import Operation
from python_project_template_AS.exceptions import RegistryError


def test_register_and_get():
    reg = OperationRegistry()

    op = Operation("double", lambda x: x * 2, arity=1)
    reg.register(op)
    assert reg.get("double") is op
    assert "double" in list(reg.list_ops())


def test_register_replace_and_duplicate():
    reg = OperationRegistry()
    op = Operation("inc", lambda x: x + 1, arity=1)
    reg.register(op)

    op2 = Operation("inc", lambda x: x + 2, arity=1)
    # can't register duplicate without replace
    with pytest.raises(RegistryError):
        reg.register(op2)

    # replace works
    reg.register(op2, replace=True)
    assert reg.get("inc")(1) == 3


def test_register_decorator():
    reg = OperationRegistry()

    # explicit registration (replace previous decorator-based test)
    def triple(x):
        return x * 3

    reg.register(Operation("triple", triple, arity=1))

    assert reg.get("triple")(3) == 9
