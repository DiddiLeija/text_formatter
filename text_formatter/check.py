"""
Check the text types, to see if they can be used on other
``text_formatter`` functions.
"""

# import the required std libraries
import string

# get a custom exception from ``text_formatter.exceptions``
from text_formatter.exceptions import InvalidBytes, InvalidString

# generate an "allowed characters list" for strings
strict_allowed_chars = string.ascii_letters + string.digits + " "  # allow a space
allowed_string_chars = strict_allowed_chars + "_-$#%/()=!'<>.:,;[]{}*+?¿¡" + '"'  # include double quotes ("")

# The same for the bytes. But we only have
# a strict ruler on this case.
strict_bytes = bytes(strict_allowed_chars+".-_,;:$%/#\"'*+", "utf-8")


def checkString(s: str, strict: bool = False) -> None:
    """
    Check a Python string (str), to see if it can be used by text_formatter.
    """
    # check the string
    if not isinstance(s, str):
        raise TypeError(f"Expected strings, but got {type(s).__name__}")
    # check if the user wants a "strict" mode: If he wants to,
    # we are using a stricter ruler for checking the string.
    if strict is True:
        ruler = strict_allowed_chars
    else:
        ruler = allowed_string_chars
    # now, check the string
    for char in s:
        if s not in ruler:
            raise InvalidString(f"String didn't satisfied what we expected: char '{char}' is not on the allowed chars")
    # everything passed? Just return None
    return None


def checkBytes(b: bytes) -> None:
    "The same than text_formatter.check.checkString(), but testing bytes."
    # check the type
    if not isinstance(b, bytes):
        raise TypeError(f"Expected bytestrings, but got {type(b).__name__}")
    ruler = strict_bytes
    # now, check the bytestring
    for char in b:
        if b not in ruler:
            raise InvalidBytes(f"String didn't satisfied what we expected: char '{char}' is not on the allowed chars")
    # everything passed? Just return None
    return None
