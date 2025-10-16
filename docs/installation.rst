Installation
============

Clone the repository, create a virtual environment (recommended), and install dependencies and an editable installation of ``python-project-template``:

.. code-block:: bash

   git clone <repo-url>
   cd python-project-template
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip setuptools wheel
   pip install -e ".[dev]"
