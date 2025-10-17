Tests
=====

It is a good idea to run the tests after installation to make sure the library works.

Testing during development is essential for identifying issues early and ensuring that new features do not break existing functionality.

Automated tests provide confidence in code changes and help maintain a stable and reliable code base as the project evolves. In the next section we'll see how to automatically run tests whenever the repository is pushed to the remote using GitHub-Actions.

Test-driven development is a software development approach where tests are written before the actual code. This process helps clarify requirements, ensures code correctness, and encourages modular design. By writing tests first, developers can catch bugs early and maintain a high level of code quality.


Running the tests manually
--------------------------

Run the full PyTest test suite with coverage:

.. code-block:: bash

   pytest -q --cov=python_project_template_AS --cov-report=term --cov-report=html

Open ``htmlcov/index.html`` to view the coverage report.
