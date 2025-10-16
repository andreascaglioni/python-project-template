Documentation (local)
=====================

Good documentation is essential for code sustainability. It ensures that others can understand, use, and maintain the project, especially if the original developer leaves. Adopting a consistent style, such as Google (used here) or NumPy, helps keep docs clear and accessible.

To build the documentation for this project, follow these steps:

1. Ensure all dependencies for documentation generation are installed, for example with ``pip install -e ".[docs]"``.
2. Run the documentation build command (for example, ``make html``).
3. Review the generated HTML in ``docs/_build/html``.
