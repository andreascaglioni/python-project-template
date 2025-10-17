Installation
============

Clone the repository, create a virtual environment (recommended), and install dependencies and an editable installation of ``python-project-template``:

.. code-block:: bash

   git clone <https://github.com/andreascaglioni/python-project-template>
   cd python-project-template
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip setuptools wheel
   pip install -e ".[dev]"

The editable installation automatically updates with the source code. It is useful for development because it allows skipping additional installations after source edits.
