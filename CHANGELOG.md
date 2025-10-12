# Changelog
All notable changes to this project are recorded here.

## [Unreleased]

### Added
- python project template (`python-project-template`) with:
	- `Operation`, `OperationRegistry`, and `Calculator` classes
	- example operations: `add`, `sub`, `mul`, `div`, `neg`, `sqr`
- Minimal test suite (pytest) with unit and edge tests
- `pyproject.toml` for editable installs and packaging
- `.gitignore` and basic repo scaffolding (`src/`, `tests/`, `experiments/`, `notebooks/`, `docs/`, `scripts/`)

### Changed
- Replaced decorator-based registration with explicit `Operation` registration API

### Fixed
- Import path handling in tests: tests now assume editable install; `conftest.py` removed sys.path hacks

---

## [0.1.0] - 2025-10-10

Initial public release

### Added
- Project scaffold and minimal working library to demonstrate portfolio-ready features
