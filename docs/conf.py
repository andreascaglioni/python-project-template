import os
import sys

# -- Path setup --------------------------------------------------------------
# Ensure the project package is importable for autodoc (assumes src layout)
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------
project = "python-project-template-AS"
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
    "sphinxcontrib.spelling",
]

autosummary_generate = True
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

# Use the docs static logo now stored in docs/_static
html_logo = "_static/logo.svg"

# Set a concise HTML title (avoid theme/appending 'Documentation')
html_title = "python-project-template"
# Optional short title used in smaller viewports or sidebars
html_short_title = "py-project-template"

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

# Spelling check options
spelling_lang = "en_US"
spelling_word_list_filename = "spelling_wordlist.txt"
spelling_show_suggestions = True
