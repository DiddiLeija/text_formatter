.. _contributions-page:

Contributing on ``text_formatter``
==================================

This is an open-source project, so we accept
contributions, and we appreciate it a lot.

Collaborate on the code
-----------------------

We are hosting the ``text_formatter`` code on `GitHub <https://github.com/DiddiLeija/text_formatter/>`_. That supports
many ways for contributing.

Fork the repository and contribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To propose changes to the code, you can `fork the GitHub repository <https://docs.github.com/en/get-started/quickstart/fork-a-repo#about-forks>`_, and
then push commits to a branch. After that, you can open a `pull request <https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#about-pull-requests>`_
on the original repository. That pull request could close an open issue, or add a new feature.

After you submit a pull request, the project maintainers will review the code to decide if your suggestion will
be applied.

Code style
^^^^^^^^^^

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

We have adopted the ``black`` code style to format our code. When you contribute with Python code, you should
respect that style. To avoid a CI failure, you can run ``nox -s format`` to format the code according to ``black``.

Participate on issues
^^^^^^^^^^^^^^^^^^^^^

Like most of the projects, we have enabled the `GitHub issues <https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues#quickly-create-issues>`_. Use
them to report an unexpected behaviour or a feature request.

.. seealso::
   
   :ref:`github-issues`
      Read about our GitHub issues, labels, and templates.

Contributions to documentation
------------------------------

.. image:: https://readthedocs.org/projects/text-formatter/badge/?version=latest
     :target: https://text-formatter.readthedocs.io/en/latest/?badge=latest
     :alt: Documentation Status

We are hosting our documentation at `ReadTheDocs <https://readthedocs.org>`_. The documentation is built using `Sphinx <https://github.com/sphinx-doc/sphinx>`_
(version 4.0 or greater) and uses some other dependencies [#f1]_.

Since we are saving the documentation files on the same repository than the code (on a ``docs`` folder), the same recomendations
(mentioned before) apply for contributing to the documentation.

Maintainers of the code
-----------------------

At this moment, ``text_formatter`` is maintained and owned by `Diego Ramirez <http://github.com/DiddiLeija>`_.

Contributing guidelines
-----------------------

Read the contributing guidelines `here <https://github.com/DiddiLeija/text_formatter/blob/main/CONTRIBUTING.md>`_.

.. rubric:: Footnotes

.. [#f1] See the full list of the docs dependencies `on GitHub <https://github.com/DiddiLeija/text_formatter/blob/main/docs/requirements.txt>`_.
