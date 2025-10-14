python-project-template Documentation
=====================================

**python-project-template is a minimal Python project aimed at demonstrating good coding practices.**

The library provides a small dependence-free Calculator API (Operation, OperationRegistry, Calculator) that can register and compose simple mathematical operations.
This simple code is used to showcase some good coding practices:

- Argument validation with type annotation and checking with the ``typing`` module
- Consistent error messages for invalid operations and inputs through custom ``Exceptions``
- Unit tests unit with ``pytest``. Use of :file:`tests/convtest.py` to set global testing variables
- Example notebooks and scripts
- Google-style documentation with ``sphinx``
- Pre-commit routine set up in file :file:`.pre-commit-config.yaml`. It includes:

  - Formatting with ``black``
  - Linting with ``ruff-pre-commit``
  - Type checking with ``mypy``
  - Additional checks and fixes (remove trailing white spaces, ensure one empty line at end of the file, YAML files syntax check, prevent committing large files) with ``pre-commit-hooks``

- Modern packaging, easy installation, and project settings with ``pyproject.toml``
- Automated test suite and coverage reporting integrated with `GitHub Actions`; coverage reports can be published to `GitHub Pages`. Setup through file :file:`.github/workflows/tests.yml`
- Automatic compilation and deployment of the documentation to `GitHub Pages` with `Github-Actions`. Setup through file :file:`.github/workflows/docs.yml` [TODO]
- Easy contribution workflow.


Installation
------------

Clone the repository, create a virtual environment (recommended), and install dependencies and editable installation of ``python-project-template``:

.. code-block:: bash

   git clone <repo-url>
   cd python-project-template
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip setuptools wheel
   pip install -e ".[dev]"

Quick usage
-----------

The following is a quick example for the Calculator API.

.. code-block:: python

    from python_project_template import default_calculator, Operation

    calc = default_calculator()
    print(calc.apply('add', 2, 3))  # -> 5

    f = calc.compose(['neg', 'sqr'])
    print(f(3))  # -> 9

    def inc(x):
        return x + 1

    calc.register(Operation('inc', inc, arity=1), replace=True)
    print(calc.apply('inc', 4))


Find additional example in:

- ``experiments/`` — short runnable demos
- ``notebooks/`` — exploratory notebooks


API reference
-------------

See the full API reference for module and class details:
:doc:`API reference <api>`

Running tests
-------------

Run the full test suite with coverage:

.. code-block:: bash

   pytest -q --cov=python_project_template --cov-report=term --cov-report=html

Open ``htmlcov/index.html`` to view the coverage report.


Project structure
-----------------

The project presents the following directory structure:
::

   src/python_project_template/      # Core library package
     calculator.py                   # Calculator API
     operations.py                   # Built-in operations
     registry.py                     # Operation registry
     exceptions.py                   # Custom error types
     utils.py                        # Utility functions
   experiments/                      # Example scripts
   notebooks/                        # Jupyter notebooks
   tests/                            # Test suite
   docs/                             # Documentation
   .github/
     workflows/
       tests.yml                     # GitHub Actions workflow for automated testing and coverage reporting
       docs.yml                      # GitHub Actions workflow for automated documentation and deployment
   pyproject.toml                    # Build/config file
   README.md                         # Project overview
   LICENSE                           # License info
   CITATION.cff                      # Citation metadata


Contributing
------------

A quick workflow:

.. code-block:: bash

   git checkout -b feat/your-feature
   # make changes
   pytest
   git add -A && git commit -m "Add feature"
   git push --set-upstream origin feat/your-feature

Use ``pip install -e .[dev]`` to get dev tools (pre-commit, black, ruff, mypy)
and run ``pre-commit run --all-files`` before committing.


License
-------

This project is licensed under the MIT License — see the ``LICENSE`` file.


Questions
---------

If you have questions or want help extending the project (docs, CI, or examples),
open an issue or drop a message in the repository.


.. toctree::
..    :maxdepth: 2
..    :caption: Contents:

..    usage
..    api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
