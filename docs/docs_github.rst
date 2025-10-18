Documentation (GitHub Actions)
==============================

This page explains how the repository builds the Sphinx documentation and publishes
the generated HTML to GitHub Pages using GitHub Actions.

The workflow does the following:

- Whenever a commit is pushed to `main`, the workflow checks out the repository (manual dispatch is also supported).
- Sets up Python and installs the ``docs`` dependencies from :file:`pyproject.toml`.
- Builds HTML with ``sphinx-build`` into ``docs/_build/html``.
- Uploads the built HTML as a Pages artifact and deploys it to GitHub Pages.

Repository setup (one-time)
---------------------------
1. Ensure the repository has GitHub Pages enabled for the ``gh-pages`` site (no manual branch required when using the Pages actions). In repository Settings → Pages you should see the site status after the first successful run.
2. No secret is required. The workflow uses the repository's built-in ``GITHUB_TOKEN`` permissions to publish pages.

Local testing
-------------
See the previous page :doc:`Local documentation <docs_local>` for additional local setup and testing instructions.

Autosummary and generated files
-------------------------------
- ``autosummary_generate = True`` is enabled in ``docs/conf.py``, so Sphinx will generate the ``_autosummary`` pages during the build.
- Best practice: do NOT commit generated files (``docs/_build``, ``docs/_autosummary``) to the repository. Keep them in ``.gitignore`` and let CI produce the HTML. If you plan to serve source HTML directly from the ``docs/`` folder (without a build step), then you'd need to commit generated files — but the current workflow builds on CI and deploys the result, so committing generated files is unnecessary.

Troubleshooting
---------------
- If builds fail due to missing packages, ensure :file:`pyproject.toml` contains the correct ``docs`` extras and that ``pip install -e ".[docs]"`` succeeds.
- If the site does not appear after the workflow succeeds, check Settings → Pages to ensure the site is not blocked by organization policy.

The workflow will attempt to publish your Sphinx docs automatically when you push to ``main``.
