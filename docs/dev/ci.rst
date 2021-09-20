Continous Integrations (CI) used on ``text_formatter``
=====================================================

We have set up a Continous Integration (commonly named *CI*) to test pull requests before merging
them, and analyzing the head branch (``main``) commits.

Workflow setup file
-------------------

**Source code:** `.github/workflows/python-app.yml <https://github.com/DiddiLeija/text_formatter/blob/main/.github/workflows/python-app.yml>`_

**Nox setup file:** `noxfile.py <https://github.com/DiddiLeija/text_formatter/blob/main/noxfile.py>`_

The YAML setup file (``python-app.yml``) defines a list of steps to test the Python code used by ``text_formatter``. It uses `Nox <https://nox.thea.codes>`_
to run tests and linters.
