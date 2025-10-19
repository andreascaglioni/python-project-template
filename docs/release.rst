Release procedure
=================

This page describes the recommended steps to create, test, and publish a release
for this project. Follow the "prerelease first, stable later" flow to avoid
accidental uploads to PyPI.

Prerequisites
-------------

- Add repository secrets in GitHub (Settings → Secrets and variables → Actions):
  - `TEST_PYPI_API_TOKEN` — API token created on TestPyPI (value begins with
    ``pypi-``).
  - `PYPI_API_TOKEN` — API token created on PyPI (value begins with
    ``pypi-``).
- Verify `pyproject.toml` metadata (`project.name` and `version`).
- Confirm build tooling is available locally when needed:
  ``python -m pip install --upgrade build twine``

Release checklist
-----------------

1. Bump the version in `pyproject.toml`.

   - For a prerelease/test run use a prerelease version (example: ``0.2.0-rc1``).
   - For a stable release use a normal version (example: ``0.2.0``).

2. Commit the version change and create a tag.

   Annotated prerelease (publishes to TestPyPI):

   .. code-block:: bash

      git add pyproject.toml
      git commit -m "Bump version to 0.2.0-rc1"
      git tag -a v0.2.0-rc1 -m "v0.2.0-rc1 - prerelease"
      git push origin v0.2.0-rc1

   Annotated stable release (publishes to PyPI):

   .. code-block:: bash

      git add pyproject.toml
      git commit -m "Bump version to 0.2.0"
      git tag -a v0.2.0 -m "v0.2.0 - release"
      git push origin v0.2.0

3. Verify the CI run

   - The release workflow builds the sdist and wheel and uploads them as an
     artifact, then publishes to TestPyPI or PyPI depending on the tag name.
   - Tags containing a dash (``-``) publish to TestPyPI. Tags without a dash
     publish to PyPI. This repository uses that convention intentionally so you
     can test on TestPyPI first.

4. Smoke-test the published package (for prerelease)

   Install from TestPyPI and run quick checks:

   .. code-block:: bash

      python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple python-project-template-AS==0.2.0rc1

   - Verify that imports and basic functionality work as expected.

5. Promote to stable (after verification)

   - Update `pyproject.toml` version to the stable version (e.g. ``0.2.0``),
     commit, tag, and push the stable tag. The workflow will publish to PyPI.

Deleting tags
-------------

If you accidentally pushed a tag and want to remove it from the remote:

.. code-block:: bash

   # delete remote tag
   git push origin --delete refs/tags/v0.2.0

   # delete local tag
   git tag -d v0.2.0

Removing GitHub Releases
------------------------

- To remove a GitHub Release created by CI, use the Releases page in the
  repository or the GitHub CLI:

.. code-block:: bash

   gh release delete v0.2.0 --repo andreascaglioni/python-project-template -y

Notes and tips
--------------

- The release workflow in `.github/workflows/release.yml` has two publish jobs:
  - `publish-testpypi` runs for prerelease tags (contains ``-``) and uses
    `TEST_PYPI_API_TOKEN`.
  - `publish-pypi` runs for stable tags (no ``-``) and uses `PYPI_API_TOKEN`.
- The workflow intentionally disables OIDC for publishing and uses repository
  secrets. Keep your secrets rotated and never commit them.
- Consider protecting the PyPI publish step with a GitHub environment that
  requires manual approval for extra safety.

Changelog and release notes
---------------------------

- Prepare changelog entries in `CHANGELOG.md` under an "Unreleased" section
  and move them into a versioned section when releasing.

Acknowledgments
---------------

Automated by repository release workflow. If you find a problem, open an issue
or submit a PR.
