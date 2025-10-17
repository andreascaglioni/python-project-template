Project Structure
=================

The project has the following directory structure:
::

   src/python_project_template_AS/   # Core library package
     calculator.py                   # Calculator API
     operations.py                   # Built-in operations
     registry.py                     # Operation registry
     exceptions.py                   # Custom error types
     utils.py                        # Utility functions
   exampoles/                        # Example usage of API
   tests/                            # Test suite
   docs/                             # Documentation
   .github/workflows/
     tests.yml                     # GitHub Actions workflow for automated testing and coverage reporting
     docs.yml                      # GitHub Actions workflow for automated documentation and deployment
   pyproject.toml                    # Build/config file
   README.md                         # Project overview
   LICENSE                           # License info
   CITATION.cff                      # Citation metadata


.. note::

  Why is the module inside ``src/``? It prevents accidental imports from the working directory so your tests mirror real installs. This is a widely recommended pattern in the `Python Packaging User Guide <https://packaging.python.org/en/latest/tutorials/packaging-projects/#src-layout>`_.
