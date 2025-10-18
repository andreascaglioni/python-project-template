Documentation (local)
=====================

Good documentation is essential for code sustainability. It ensures that others can understand, use, and maintain the project, especially if the original developer leaves. Adopting a consistent style, such as Google (used here) or NumPy, helps keep docs clear and accessible.

To build the documentation for this project, follow these steps:

1. Install documentation dependencies with ``pip install -e ".[docs]"``.
2. Move to ``docs/`` (``cd docs``) and build the documentation ``make html``.

The generated HTML is in ``docs/_build/html``.
