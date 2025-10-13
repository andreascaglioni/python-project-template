[![CI](https://github.com/andreascaglioni/python-project-template/actions/workflows/tests.yml/badge.svg)](https://github.com/andreascaglioni/python-project-template/actions/workflows/tests.yml)
[![PyPI Version](https://img.shields.io/pypi/v/python-project-template.svg)](https://pypi.org/project/python-project-template/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# python-project-template — showcasing good software practices
A minimal Python project demonstrating best practices for testing, documentation, CI/CD, packaging, examples.
The library provides a tiny Calculator API that can register and compose simple mathematical operations.

## Table of contents
- [Features](#features)
- [Installation](#installation)
- [Quick usage](#quick-usage)
- [Examples & experiments](#examples--experiments)
- [Running tests](#running-tests)
- [Project structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- Small, dependency-free core API: Operation, OperationRegistry, Calculator
- Example operations (add, sub, mul, div, neg, sqr)
- Utilities and clear error handling
- Tests (pytest) and CI workflow included

## Installation

Clone the repository and create a virtual environment (recommended):

```bash
git clone <repo-url>
cd python-project-template
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -e ".[dev]"
```

This installs the package in editable mode and the development extras (pytest,
pre-commit, formatting and linting tools) so you can run tests and linters.

## Quick usage

Interactive example using the package API:

```python
from python_project_template import default_calculator, Operation

# Create a default calculator (pre-populated with common ops)
calc = default_calculator()

# Apply an operation
print(calc.apply('add', 2, 3))  # -> 5

# Compose unary operations
f = calc.compose(['neg', 'sqr'])
print(f(3))  # -> 9

# Register a custom operation
def inc(x):
    return x + 1

calc.register(Operation('inc', inc, arity=1), replace=True)
print(calc.apply('inc', 4))  # -> 5
```

## Examples & experiments

- `experiments/` — short runnable demos. Each experiment should include a
  `README.md` explaining inputs and expected outputs.
- `notebooks/` — exploratory notebooks (keep final versions small).

## Running tests

Run the full test suite with coverage:

```bash
pytest -q --cov=python_project_template --cov-report=term --cov-report=html
```

Open `htmlcov/index.html` to view the coverage report.

## Project structure

```
src/python_project_template/        # library code
  - calculator.py                   # Calculator API
  - operations.py                   # Operation dataclass and example ops
  - registry.py                     # OperationRegistry
- exceptions.py                     # custom exceptions
  - utils.py            # small helpers
experiments/            # short runnable demos
notebooks/              # interactive exploration
tests/                  # pytest test suite
docs/                   # docs site (mkdocs)
pyproject.toml          # build & project config
.github/workflows/      # CI workflows
README.md
LICENSE
CITATION.cff
```

## Contributing

Contributions are welcome. A quick workflow:

```bash
git checkout -b feat/your-feature
# make changes
pytest  # run tests locally
git add -A && git commit -m "Add feature"
git push --set-upstream origin feat/your-feature
# open a PR
```

### Developer notes
- Use `pip install -e .[dev]` to get dev tools (pre-commit, black, ruff, mypy).
- Run `pre-commit run --all-files` before committing.
- CI runs tests on Ubuntu for Python 3.9–3.12 and uploads HTML coverage.

## License

This project is licensed under the MIT License — see the `LICENSE` file.

## Questions

If you have questions or want help extending the project (docs, CI, or
examples), open an issue or drop a message in the repo.
