Appendix
========

Contributing
------------

A quick workflow:

.. code-block:: bash

   git checkout -b feat/your-feature
   # make changes
   pytest
   git add -A && git commit -m "Add feature"
   git push --set-upstream origin feat/your-feature

Use ``pip install -e .[dev]`` to get development tools (pre-commit, black, ruff, mypy)
and run ``pre-commit run --all-files`` before committing.


License
-------

This project is licensed under the MIT License — see the ``LICENSE`` file.


Questions
---------

If you have questions or want help extending the project (docs, CI, or examples), open an issue or drop a message in the repository.
