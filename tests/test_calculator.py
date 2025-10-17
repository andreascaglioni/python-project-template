import pytest

from python_project_template_AS import default_calculator, Operation
from python_project_template_AS.exceptions import OperationError


def test_default_calculator_apply_compose_chain():
    c = default_calculator()
    assert c.apply("add", 2, 3) == 5

    comp = c.compose(["neg", "sqr"])  # neg then sqr: ( -x )^2 == x^2
    assert comp(3) == 9

    res = c.chain(["add", 5, "sqr"], initial=2)
    assert res == 49


def test_register_and_apply_custom_op():
    c = default_calculator()

    # define and register a new unary op
    op = Operation("inc", lambda x: x + 1, arity=1)
    c.register(op, replace=True)
    assert c.apply("inc", 4) == 5

    # wrong arity on apply
    with pytest.raises(OperationError):
        c.apply("inc", 1, 2)


def test_chain_errors():
    c = default_calculator()
    # missing argument for binary op in chain
    with pytest.raises(OperationError):
        c.chain(["add"], initial=1)
