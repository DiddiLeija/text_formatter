.. _module-check:

``text_formatter.check`` - Check the text types, to see if they can be used on other ``text_formatter`` functions
================================================================================================================

**Source code:** `text_formatter/check.py <https://github.com/DiddiLeija/text_formatter/blob/main/text_formatter/check.py>`_

This module has functions to test strings and other text types, to see if they can be easily used by
other ``text_formatter`` submodules.

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
