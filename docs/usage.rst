Usage example
=============

The following is a quick example for the Calculator API. It shows how to:

* Use an operation already included in the library (addition)
* Compose operations (negation and squaring)
* Add a new operation (increase by 1 unit).

.. code-block:: python

    from python_project_template_AS import default_calculator, Operation

    calc = default_calculator()

    print(calc.apply('add', 2, 3))  # -> 5

    f = calc.compose(['neg', 'sqr'])
    print(f(-3))  # -> 9

    def inc(x):
        return x + 1

    calc.register(Operation('inc', inc, arity=1), replace=True)
    print(calc.apply('inc', 4))

Find additional examples in ``examples/``.
