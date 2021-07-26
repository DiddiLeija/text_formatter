.. _module-justify:

``text_formatter.justify`` - Justify the strings, according to a certain length
================================================================================

**Source code**: `text_formatter/justify.py <https://github.com/DiddiLeija/text_formatter/blob/main/text_formatter/justify.py>`_

This module provides functions to modify the length of some text Python types, like ``str`` or ``bytes``.

.. py:function:: text_formatter.justify.justify(s, l)
   
   :param s: The string to be justified.
   :param l: The expected length *per line*.

   A simple function to justify strings. It uses ``text_formatter.check.checkString()`` for testing ``s``.
