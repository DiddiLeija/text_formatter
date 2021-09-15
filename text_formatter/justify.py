"""
Justify the strings, according to a certain length.
"""

__all__ = ["justify", "justify_bytes"]

from text_formatter.check import checkBytes, checkString


def justify(s: str, length: int) -> str:
    """
    Justify a string (s) and make it
    fit to a specific length (length).
    """
    # check the string introduced
    checkString(s)#blablabla

    return s  # This func needs larger development!!! (DiddiLeija/text_formatter#1)


def justify_bytes(b: bytes, length: int) -> bytes:
    """
    Same function than
    text_formatter.justify.justify(), but taking
    bytes instead of standard strings.
    """
    checkBytes(b)

    # Just like justify(), this
    # function is not completed yet.
    return b
