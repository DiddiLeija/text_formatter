.. _module-justify:

``text_formatter.justify`` - Justify the strings, according to a certain length
================================================================================

**Source code**: `text_formatter/justify.py <https://github.com/DiddiLeija/text_formatter/blob/main/text_formatter/justify.py>`_

This module provides functions to modify the length of some text Python types, like ``str`` or ``bytes``.

.. py:function:: text_formatter.justify.justify(s, length)
   
   :param str s: The string to be justified.
   :param int length: The expected length *per line*.
   :return: The string adjusted to the given length *per line*.
   :rtype: str
   :raises text_formatter.exceptions.InvalidString: if text_formatter.check.checkString failed.

   A simple function to justify strings.
   
   .. warning::
      
      Even when this documentation is telling that ``justify()`` returns the adjusted string, at this moment it only returns an unmodified
      ``s``. This function needs a larger development, so the actual documentation is not stable at all.
      
      Actually the whole project needs a more-stable development [#f1]_.

.. py:function:: text_formatter.justify.justify_bytes(b, length)

   :param bytes b: The bytestring to be justified.
   :param length: The expected length *per line*.
   :return: The bytestring adjusted to length ``length``.
   :rtype: bytes
   :raises text_formatter.exceptions.InvalidBytes: if text_formatter.check.checkBytes fails.
   
   Probably the same than ``justify()``, but converting byte-like strings instead
   of Python strings.
   
   .. warning::
   
      Just like ``justify()``, this function hasn't been completed (yet), like most of the
      ``text_formatter`` features [#f1]_.

.. rubric:: Footnotes

.. [#f1] See http://github.com/DiddiLeija/text_formatter/issues/7 for more information.
