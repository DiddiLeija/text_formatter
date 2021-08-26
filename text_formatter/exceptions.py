# exceptions.py - Python exceptions for everything at "text_formatter"
#
# This file contains many, many exceptions (subclasses of the
# standard "Exception") and related functions.

class InvalidString(Exception):
    """
    This exception must be raised when a string
    argument is not what we expected.
    """
    pass


class InvalidBytes(Exception):
    """
    The same function than InvalidString,
    but applied to bytestrings.
    """
    pass
