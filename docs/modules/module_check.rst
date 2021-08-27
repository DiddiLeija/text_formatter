.. _module-check:

``text_formatter.check`` - Check the text types, to see if they can be used on other ``text_formatter`` functions
================================================================================================================

**Source code:** `text_formatter/check.py <https://github.com/DiddiLeija/text_formatter/blob/main/text_formatter/check.py>`_

This module has functions to test strings and other text types, to see if they can be easily used by
other ``text_formatter`` submodules.

Stuff to test strings
---------------------

.. py:function:: text_formatter.check.checkString(s, strict=False)

   :param s: String passed to be tested.
   :param strict: If `True`, use a stricter algorithm for checking.
   :return: Nothing.
   :rtype: None
   :raises text_formatter.exceptions.InvalidString: if the string does not satisfies the expected.

   Checks if a string can be used by ``text_formatter``. In general, it checks if no region-specific characters are used. If ``strict`` is True, this function will only accept  
   letters and digits (not symbols!).
   
   In most of the cases, this function is being used by internal ``text_formatter`` functions.

.. py:data:: text_formatter.check.strict_allowed_chars

   :type: str
   :value: ``"ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 "``
   
   The string used by ``checkString()`` when the arg ``strict`` is True. Basically, it is the result of ``string.ascii_letters + string.string_digits + " "``.

.. py:data:: text_formatter.check.allowed_string_chars

   :type: str
   :value: ``"ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-$#%/()=!'<>.:,;[]{}*+?¿¡\" "``
   
   A more-inclusive string, the default for ``checkString``. It includes all around ``strict_allowed_chars``, and also includes symbols, quotes, etc.

Stuff to test bytes
-------------------

.. py:function:: text_formatter.check.checkBytes(b)

   :param b: Bytestring to be tested.
   :return: Nothing
   :rtype: None
   :raises text_formatter.exceptions.InvalidString: if the bytes are not what we expected.
   
   This function is similar to ``checkString``, with the following differences:
   
   * The parameter ``strict`` does not exist here, we are using only one ruler to test.
   * The parameter names, the exception raised and the ruler are different.
   
   .. note::
      
      The ruler used on this function is limited. Many errors could result, even on
      a normal text. We'll try to enable more characters in the future.
   
.. py:data:: text_formatter.check.strict_bytes
   
   :type: bytes
   :value: ``b"ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 "``
   
   This bytestring is the ruler used by ``checkBytes()``. As you can see,
   it is a bytes version of ``text_formatter.check.strict_allowed_chars``.
   
   .. note::
   
      This ruler is really limited, see the note for ``checkBytes``.
