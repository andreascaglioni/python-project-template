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

    calc.register(Operation(name="add", func=add_v1))
    assert calc.apply("add", 1, 2) == 3

    # replace existing operation
    calc.register(Operation(name="add", func=add_v2), replace=True)
    assert calc.apply("add", 1, 2) == 30
