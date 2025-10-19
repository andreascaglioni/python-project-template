Usage example
=============

The following is a quick example for the Calculator API. It shows how to:

* Use an operation already included in the library (addition)
* Compose operations (negation and squaring)
* Add a new operation (increase by 1 unit).

.. code-block:: python

    from python_project_template_AS import default_calculator, Operation  # import API

    calc = default_calculator()  # create a calculator instance

    print(calc.apply('add', 2, 3))  # use built-in addition -> 5

    f = calc.compose(['neg', 'sqr'])  # compose negation and squaring
    print(f(-3))  # composed function applied -> 9

    def inc(x):  # define increment operation
        return x + 1

    calc.register(Operation('inc', inc, arity=1), replace=True)  # register new operation
    print(calc.apply('inc', 4))  # apply new operation -> 5

Find additional examples in ``examples/``.
