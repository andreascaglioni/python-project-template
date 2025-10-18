"""
example_2_replace_operation.py

Example on registering and replacing an operation with a new one (by the same name) in the Calculator class.
"""

from python_project_template_AS.calculator import Calculator, Operation


if __name__ == "__main__":
    calc = Calculator()

    def add_v1(a, b):
        return a + b

    def add_v2(a, b):
        return (a + b) * 10

    op_v1 = Operation(name="add", func=add_v1, arity=2)
    calc.register(op_v1)
    sum_1 = calc.apply("add", 1, 2)
    print("calc.apply('add', 1, 2) =", sum_1)

    # Replace existing operation adn recompute the sum
    op_v2 = Operation(name="add", func=add_v2, arity=2)
    calc.register(op_v2, replace=True)
    sum_2 = calc.apply("add", 1, 2)
    print("calc.apply('add', 1, 2) = ", sum_2)
