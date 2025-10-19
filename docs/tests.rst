Tests
=====

It is a good idea to run the tests right after installation to make sure the library works (see “Running the tests manually” below).

Running tests frequently during development catches issues early, provide fast feedback during development, and make refactoring safer. They also serve as executable documentation of expected behavior, reducing the risk of shipping bugs.

Test-driven development (TDD) means writing a failing test before implementing functionality. This practice clarifies requirements, encourages small, focused changes and modular design, and helps prevent regressions as the codebase evolves.

For information on running tests automatically in CI, see the “GitHub Actions workflow for testing” section below for details on the included workflow that runs on pushes and pull requests.

Running the tests manually
--------------------------

Run the full PyTest test suite with coverage:

.. code-block:: bash

   pytest -q --cov=python_project_template_AS --cov-report=term --cov-report=html

Open ``htmlcov/index.html`` to view the coverage report.


GitHub Actions workflow for testing
-----------------------------------

This project includes a CI workflow at ``.github/workflows/tests.yml`` that runs on pushes and pull requests. The workflow sets up one or more Python versions, installs the package and test dependencies, runs exact configuration used in this project.
