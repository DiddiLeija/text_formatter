.. _github-issues:

How do we handle issues on our GitHub repository
================================================

We use `GitHub issues <https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues#quickly-create-issues>`_ to
track bugs, requests and other important jobs. This document talks about our issues, labels, and templates.

Labels
------

We have labels to identify what does the issue tries to do.

Our labels
^^^^^^^^^^

They specify what is the issue proposal.

* ``Addition proposal``
* ``Announcement``
* ``answered``
* ``bug``
* ``bugfix``
* ``Deletion proposal``
* ``documentation - ReadTheDocs``
* ``documentation``
* ``duplicate``
* ``enhancement``
* ``good first issue``
* ``help wanted``
* ``invalid``
* ``Migration proposal``
* ``Modification proposal``
* ``Must be discussed``
* ``Please triage this``
* ``question``
* ``Related to automation``
* ``Related to bots/apps``
* ``Related to GitHub``
* ``Related to manifest files``
* ``Related to text_formatter.check``
* ``Related to text_formatter.exceptions``
* ``Related to text_formatter.justify``
* ``Release tracker``
* ``Security issue``
* ``Trivial proposal``
* ``Undefined proposal``
* ``wontifx``
* ``Wrong project``

Dependabot labels
^^^^^^^^^^^^^^^^^

The Dependabot PRs have a ``dependencies`` label, and most of the times, one of these labels:

* ``python``
* ``github_actions``

Labels used by ``lock-threads``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This action ignores issues with a ``Do not lock this`` label. When it locks
something, it applies the label ``Outdated and locked``.

Markdown templates
------------------

We have created issue templates to ease the issue creation. The templates made for any users are:

* **Bug report**: Create a report to help us improve
* **Feature request**: Suggest an idea for this project
* **Security vulnerability issue**: An issue about a security vulnerability

.. note::

   In most of the cases, you don't have to open issues with the ``Security vulnerability issue`` template.

.. warning::

   We created the issue templates to make an easier diagnose of bug reports and feature requests. Please provide *all the information requested*
   that applies on your case.
   
   If we see invalid issues, we'll request for more information by using a ``no-response`` bot [#f1]_, but if you don't give us
   complete information, the bot will close the issue.

.. warning::

   We have more issue templates, but they were made for the project maintainers (like release trackers and other things). If you are
   not a maintainer of ``text_formatter``, *please don't open that kind of issues*. We'll ignore those special issues if they were created
   without permission.
