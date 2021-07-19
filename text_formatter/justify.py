"""
Justify the strings, according to a certain length.
"""

__all__ = ["justify"]

from text_formatter.check import checkString

def justify(s: str, l: int) -> str:
    """
    Justify a string (s) and make it
    fit to a specific length (l).
    """
    # check the string introduced
    checkString(s)

    return s # This func needs larger development!!! (DiddiLeija/text_formatter#1)
