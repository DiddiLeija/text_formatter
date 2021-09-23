.. _ci-description:

Continous Integrations (CI) used on ``text_formatter``
=====================================================

We have set up a Continous Integration (commonly named *CI*) to test pull requests before merging
them, and analyzing the head branch (``main``) commits.

Tests and linters using ``nox``
-------------------------------

**Nox setup file:** `noxfile.py <https://github.com/DiddiLeija/text_formatter/blob/main/noxfile.py>`_

We use `Nox <https://nox.thea.codes>`_ to run tests and linters.

Basically, ``nox`` will run the following commands:

``flake8 . --exclude=.nox/test/lib --count --max-complexity=10 --max-line-length=127 --show-source --statistic``
  Find undefined names and other common mistakes. Ignore the Python library at ``.nox/test/lib``.

``isort . --check-only -v``
  Run ``isort`` to check the sorting of imports.

Running ``nox`` at GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^

**Source code:** `.github/workflows/python-app.yml <https://github.com/DiddiLeija/text_formatter/blob/main/.github/workflows/python-app.yml>`_

The YAML setup file (``python-app.yml``) defines a list of steps to test the Python code used by ``text_formatter`` at
`GitHub <https://github.com/DiddiLeija/text_formatter>`_. It automatically calls ``nox``.

Run ``nox`` locally
^^^^^^^^^^^^^^^^^^^

To test your code locally, you only have to run

::

    nox --non-interactive --sessions test
