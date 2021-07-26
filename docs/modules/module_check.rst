.. _module-check:

``text_formatter.check`` - Check the text types, to see if they can be used on other ``text_formatter`` functions
================================================================================================================

**Source code:** `text_formatter/check.py <https://github.com/DiddiLeija/text_formatter/blob/main/text_formatter/check.py>`_

This module has functions to test strings and other text types, to see if they can be safely used by
other ``text_formatter`` submodules.

.. py:function:: text_formatter.check.checkString(s, strict=False)

   :param s: String passed to be converted.
   :param l: Integer/Float for the length per line.

   Checks if a string can be used by ``text_formatter``. In general, it checks if no special characters are used. ``s`` is
   the string to be tested. If ``strict`` is True, this function will only accept letters and digits (not symbols).
