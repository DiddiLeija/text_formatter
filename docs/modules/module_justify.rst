.. _module-justify:

``text_formatter.justify`` - Justify the strings, according to a certain length
================================================================================

**Source code**: `text_formatter/justify.py <https://github.com/DiddiLeija/text_formatter/blob/main/text_formatter/justify.py>`_

This module provides functions to modify the length of some text Python types, like ``str`` or ``bytes``.

.. py:function:: text_formatter.justify.justify(s, l)
   
   :param str s: The string to be justified.
   :param int l: The expected length *per line*.
   :return: The string adjusted to the given length *per line*.
   :rtype: str
   :raises text_formatter.exceptions.InvalidString: if the applied ``text_formatter.check.checkString()`` test fails [#f1]_ [#f2]_.

   A simple function to justify strings. It uses ``text_formatter.check.checkString()`` [#f2]_ for testing ``s``.

.. rubric:: Footnotes

.. [#f1] See the reference for ``text_formatter.exceptions`` `here <https://text-formatter.readthedocs.io/en/latest/modules/module_exception.html>`_.

.. [#f2] See the reference for ``text_formatter.check`` `here <https://text-formatter.readthedocs.io/en/latest/modules/module_check.html>`_
