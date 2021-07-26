.. _module-check:

``text_formatter.check`` - Check the text types, to see if they can be used on other ``text_formatter`` functions
================================================================================================================

**Source code:** `text_formatter/check.py <https://github.com/DiddiLeija/text_formatter/blob/main/text_formatter/check.py>`_

This module has functions to test strings and other text types, to see if they can be easily used by
other ``text_formatter`` submodules.

.. py:function:: text_formatter.check.checkString(s, strict=False)

   :param s: String passed to be tested.
   :param strict: If `True`, use a stricter algorithm for checking.

   Checks if a string can be used by ``text_formatter``. In general, it checks if no region-specific characters are used. If ``strict`` is True, this function will only accept  
   letters and digits (not symbols!). If something fails, it raises an ``InvalidString`` exception from ``text_formatter.exceptions``.
   
   In most of the cases, this function is being used by internal ``text_formatter`` functions.
