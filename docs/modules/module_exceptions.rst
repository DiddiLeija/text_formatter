.. _module-exceptions:

``text_formatter.exceptions`` - Customized exceptions collector for ``text_formatter``
======================================================================================

**Source code**: `text_formatter/exceptions.py <https://github.com/DiddiLeija/text_formatter/blob/main/text_formatter/exceptions.py>`_

Basically, this file was created to store some exceptions we have created,
to use them on many ``text_formatter`` features.

These exceptions are built as subclasses of the
standard Python exceptions, or subclasses of one of our exceptions.

.. py:exception:: text_formatter.exceptions.InvalidString

   Basic exception, raised when a string argument cannot be used by ``text_formatter``.
