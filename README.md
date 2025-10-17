[![CI](https://github.com/andreascaglioni/python-project-template/actions/workflows/tests.yml/badge.svg)](https://github.com/andreascaglioni/python-project-template/actions/workflows/tests.yml)
[![PyPI Version](https://img.shields.io/pypi/v/python-project-template.svg)](https://pypi.org/project/python-project-template/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)



# python-project-template — showcasing good software practices
The library provides a small dependence-free Calculator API (Operation, OperationRegistry, Calculator) that can register and compose simple mathematical operations.
This simple code is used to showcase some good coding practices.

## Table of contents
- [Features](#features)
- [Installation](#installation)
- [Quick usage](#quick-usage)
- [Examples & experiments](#examples--experiments)
- [Documentation](#documentation)
- [Running tests](#running-tests)
- [Project structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Argument validation** with type annotations and runtime checking using the ``typing`` module.
- **Consistent error messages** for invalid operations and inputs via custom ``Exceptions``.
- **Unit tests** with ``pytest``. Global testing variables set in `tests/convtest.py`.
- **Example notebooks and scripts** for demonstration and exploration.
- **Google-style documentation** generated with ``sphinx``.
- **Pre-commit routine** configured in `.pre-commit-config.yaml`:

  - Code formatting with ``black``
  - Linting with ``ruff-pre-commit``
  - Type checking with ``mypy``
  - Additional checks and fixes (trailing whitespace removal, enforcing empty line at EOF, YAML syntax checks, blocking large files) via ``pre-commit-hooks``

- **Modern packaging** and easy installation using `pyproject.toml`.
- **Automated test suite and coverage reporting** integrated with GitHub Actions; coverage reports can be published to GitHub Pages. Setup in `.github/workflows/tests.yml`.
- **Automatic documentation build and deployment** to GitHub Pages with GitHub Actions. Setup in `.github/workflows/docs.yml`.
- **Easy contribution workflow** for new features and improvements.

## Installation

Clone the repository, create a virtual environment (recommended), and install dependencies and an editable installation of `python-project-template`:

```bash
git clone <https://github.com/andreascaglioni/python-project-template>
cd python-project-template
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -e ".[dev]"
```

## Quick usage

The following is a quick example for the Calculator API.

```python
from python_project_template import default_calculator, Operation

# Create a default calculator (pre-populated with common operations)
calc = default_calculator()

# Apply an addition operation
print(calc.apply('add', 2, 3))  # -> 5

# Compose unary operations into a Callable
f = calc.compose(['neg', 'sqr'])
print(f(3))  # -> 9

# Register a custom operation
def inc(x):
    return x + 1

calc.register(Operation('inc', inc, arity=1), replace=True)
print(calc.apply('inc', 4))  # -> 5
```

## Examples & experiments

- `experiments/` — short runnable demos.
- `notebooks/` — exploratory notebooks.

## Documentation

For detailed documentation, please visit our [GitHub Pages](https://andreascaglioni.github.io/your-repo-name/).

## Running tests

Run the full PyTest test suite with coverage:

```bash
pytest -q --cov=python_project_template --cov-report=term --cov-report=html
```

Open `htmlcov/index.html` to view the coverage report.

## Project structure

```
src/python_project_template/      # Core library package
  calculator.py                   # Calculator API
  operations.py                   # Built-in operations
  registry.py                     # Operation registry
  exceptions.py                   # Custom error types
  utils.py                        # Utility functions
examples/                         # Example usage of API
tests/                            # Test suite
docs/                             # Documentation (Sphinx source)
.github/workflows/                # CI workflows (tests, docs)
pyproject.toml                    # Project configuration and packaging
README.md                         # This file
LICENSE                           # License text
CITATION.cff                      # Citation metadata
```

## Contributing

Contributions are welcome. Typical workflow:

```bash
git checkout -b feat/your-feature
# make changes
pytest  # run tests locally
git add -A && git commit -m "Add feature"
git push --set-upstream origin feat/your-feature
# open a PR
```

Run `pip install -e .[dev]` to get development tools (pre-commit, black, ruff, mypy, pytest, ...).
The pre-commit routine is called with `pre-commit run --all-files` before committing.

## License

This project is licensed under the MIT License — see the `LICENSE` file.

## Questions

If you have questions or want help extending the project (docs, CI, or examples), open an issue or drop a message in the repository.
