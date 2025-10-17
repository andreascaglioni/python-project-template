"""
example_1_calculator.py

Basic example usage for the Calculator and Operation classes. This script demonstrates:

- Initializing a Calculator instance.
- Registering and applying a custom unary operation (square).
- Registering and applying a binary operation (addition) from the API.
- Chaining multiple operations together.
- Composing unary operations to create a new callable.

Each operation is tested and the results are printed to verify correct behavior.
"""

from python_project_template_AS import Calculator, Operation, ADD, NEG


# Initialize new calculator
calc = Calculator()


# Adding and using a unary opeartion
def square(x):
    return x * x


sqr_op = Operation(name="sqr", func=square)
calc.register(sqr_op)
sq_n = calc.apply("sqr", 4)
sq_str = 'calc.apply("sqr", 4)'
print(f"{sq_str} = {sq_n}")

# Adding an opeartion from the API to current calculator
add_op = Operation(name="add", func=ADD, arity=2)
calc.register(add_op)
add_result = calc.apply("add", 2, 3)
add_str = 'calc.apply("add", 2, 3)'
print(f"{add_str} = {add_result}")

# Chaining opeartions
chain_res = calc.chain(["add", 5, "sqr"], initial=2)
chain_str = "calc.chain(['add', 5, 'sqr'], initial=2)"
print(f"{chain_str} = {chain_res}")

# Generate a Callable from composing unary operations (computed right-to-left)
neg_op = Operation(name="neg", func=NEG, arity=1)
calc.register(neg_op)
sqr_neg = calc.compose(["neg", "sqr"], left_to_right=False)
comp_test = sqr_neg(16)
comp_str = "sqr_neg(16)"
print(f"{comp_str} = {comp_test}")
