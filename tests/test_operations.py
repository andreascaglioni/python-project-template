import pytest

from python_project_template_AS.operations import ADD, SUB, MUL, DIV, NEG, SQR
from python_project_template_AS.exceptions import OperationError


def test_basic_binary_ops():
    assert ADD(2, 3) == 5
    assert SUB(10, 4) == 6
    assert MUL(3, 5) == 15


def test_division_and_zero():
    assert DIV(10, 2) == 5
    with pytest.raises(OperationError):
        DIV(1, 0)


def test_unary_ops_and_arity_check():
    assert NEG(5) == -5
    assert SQR(4) == 16
    # wrong arity
    with pytest.raises(OperationError):
        NEG(1, 2)
    with pytest.raises(OperationError):
        ADD(1)
