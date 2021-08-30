.. _github-features:

GitHub features used on ``text_formatter``
==========================================

We hosted ``text_formatter`` on `GitHub <http://github.com/DiddiLeija/text_formatter>`_ since we started
to develop the code. As the project were growing, we decided to implement some GitHub special features.

GitHub actions
--------------

We are using GitHub actions to automate tests and processes. Those workflows are
stored `right here <https://github.com/DiddiLeija/text_formatter/tree/main/.github/workflows>`_. They are used
to make tests on the code before/after merging commits to the ``main`` branch.

The ``greetings`` workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^

When you fill an issue/pull request for the first time, a special workflow
named ``greetings`` will send you a message.

On issues, it says:

    Thanks for your first issue! The ``text_formatter`` maintainers will try to help or support you, as soon as possible. We really appreciate your recent contribution.

On pull requests, it says:

    Thanks for your first pull request! We really appreciate your contribution. Now, you may need a maintainer to review the code and give you some style suggestions.

GitHub bots
-----------

These bots are used on the GitHub interface for issues and pull requests.

Dependabot [#f1]_
   This bot is only used to keep some GitHub actions fresh.

Lock [#f2]_
   This bot locks outdated conversation and applies a related label.

No-response [#f3]_
   This bot has a more-complex function. When we want more information/response from the author of a pull request/issue,
   we apply an ``Awaiting response`` label. After 15 days, if the author hasn't answered, this bot will close it.

GitHub projects
---------------

Diego Ramirez has a personal project board for ``text_formatter`` (see it `here <https://github.com/users/DiddiLeija/projects/4>`_). But the
repository has more boards, related to some specific topics. See them `here <https://github.com/DiddiLeija/text_formatter/projects>`_.

GitHub issue templates
----------------------

Read about how to use those templates on ":ref:`contributions-page`".

.. rubric:: Footnotes

.. [#f1] See the reference for ``dependabot`` `here <https://github.com/apps/dependabot>`_.
.. [#f2] See the reference for ``lock`` `here <https://github.com/apps/lock>`_.
.. [#f3] See the reference for ``no-response`` `here <https://github.com/apps/no-response>`_.
