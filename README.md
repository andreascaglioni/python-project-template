[![CI](https://github.com/andreascaglioni/python-project-template/actions/workflows/tests.yml/badge.svg)](https://github.com/andreascaglioni/python-project-template/actions/workflows/tests.yml)
[![Docs](https://github.com/andreascaglioni/python-project-template/actions/workflows/docs.yml/badge.svg)](https://github.com/andreascaglioni/python-project-template/actions/workflows/docs.yml)
[![PyPI Version](https://img.shields.io/pypi/v/python-project-template.svg)](https://pypi.org/project/python-project-template-AS/)
[![TestPyPI Version](https://img.shields.io/badge/TestPyPI-latest-informational.svg)](https://test.pypi.org/project/python-project-template-AS/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)



# python-project-template — showcasing good software practices

`python-project-template` is a small python project to showcase good programming and software practices such as testing, documentation, CI/CD.

This project implements a small dependence-free Calculator API (Operation, OperationRegistry, Calculator) that can register and compose simple mathematical operations.

## Table of contents
- [Features](#features)
- [Installation](#installation)
- [Usage and Testing](#Usage-and-Testing)
- [Examples & experiments](#examples--experiments)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Features Highlights

- **Type-annotated API** with runtime argument validation.
- **Custom exceptions** for clear error reporting.
- **Comprehensive unit tests** using `pytest`.
- **Google-style documentation** auto-generated with Sphinx.
- **Pre-commit checks** and code formatting tools.
- **CI/CD pipelines** for testing and docs via GitHub Actions.


See the [Documentation](#documentation) for a detailed list of features.

## Installation

To install the latest release from TestPyPI, use:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple python-project-template-AS
```

Alternatively, you can clone the repository and install dependencies and an editable installation of `python-project-template-AS` with:

```bash
git clone <https://github.com/andreascaglioni/python-project-template-AS>
cd python-project-template
pip install -e ".[dev]"
```

## Usage and Testing

The following is a quick example for the Calculator API.

```python
from python_project_template_AS import default_calculator, Operation

# Create a default calculator (pre-populated with common operations)
calc = default_calculator()

# Apply an addition operation
print(calc.apply('add', 2, 3))  # -> 5

# Compose unary operations into a Callable
f = calc.compose(['neg', 'sqr'])
print(f(-3))  # -> 9

# Register a custom operation
def inc(x):
    return x + 1

calc.register(Operation('inc', inc, arity=1), replace=True)
print(calc.apply('inc', 4))  # -> 5
```

Find more examples in `examples/`.

To run the tests:

```bash
pytest tests/
pytest -v tests/  # verbose output
pytest --cov=python_project_template_AS tests/  # show test coverage
```

## Documentation

For detailed documentation, please visit our [GitHub Pages](https://andreascaglioni.github.io/your-repo-name/).


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
Run the pre-commit routine with `pre-commit run --all-files` before committing.

## License

This project is licensed under the MIT License — see the `LICENSE` file.

## Questions

If you have questions or want help extending the project (docs, CI, or examples), open an issue or drop a message in the repository.
