import os
import sys

# -- Path setup --------------------------------------------------------------
# Ensure the project package is importable for autodoc (assumes src layout)
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------
project = "python-project-template"
author = "Andrea Scaglioni"
# Keep in sync with pyproject.toml
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    "sphinx_mdinclude",
    "sphinx_copybutton",
]

autosummary_generate = True
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}

autodoc_typehints = "description"

# Optional: link to other projects
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
