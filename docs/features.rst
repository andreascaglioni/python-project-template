Features
========

This code is used to showcase a number of good software practices:

- Argument validation with type annotations and runtime checking using the ``typing`` module
- Consistent error messages for invalid operations and inputs via custom ``Exceptions``
- Unit tests with ``pytest``. Use :file:`tests/convtest.py` to set global testing variables
- Example notebooks and scripts
- Google-style documentation generated with ``sphinx``
- Pre-commit routine set up in file :file:`.pre-commit-config.yaml`. It includes:

  - Formatting with ``black``
  - Linting with ``ruff`` via pre-commit
  - Type checking with ``mypy``
  - Additional checks and fixes (trailing whitespace removal, enforcing empty line at EOF, YAML syntax checks, blocking large files) via ``pre-commit-hooks``

- Modern packaging, easy installation, and project settings with :file:`pyproject.toml`
- Automated test suite and coverage reporting integrated with `GitHub Actions`; coverage reports can be published to `GitHub Pages`. See :file:`.github/workflows/tests.yml`
- Automatic documentation build and deployment to `GitHub Pages` with GitHub Actions. Setup in :file:`.github/workflows/docs.yml`
- Easy contribution workflow for new features and improvements.
