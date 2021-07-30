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
   :raises text_formatter.exceptions.InvalidString: if the applied ``text_formatter.check.checkString()`` test fails [#f1]_.

   A simple function to justify strings. It uses ``text_formatter.check.checkString()`` [#f1]_ for testing ``s``.
   
   .. warning::
      
      Even when this documentation is telling that ``justify()`` returns the adjusted string, at this moment it only returns an unmodified
      ``s``. This function needs a larger development, so the actual documentation is not stable at all. See http://github.com/DiddiLeija/text_formatter/issues/1
      for more information.

.. rubric:: Footnotes

.. [#f1] See the reference for ``text_formatter.check`` `here <https://text-formatter.readthedocs.io/en/latest/modules/module_check.html>`_.
