"""
Justify the strings, according to a certain length.
"""

__all__ = ["justify", "justify_bytes"]

from typing import List

from text_formatter.check import checkBytes, checkString


def line_to string(l: List[str]):
    "Return a string from a list of strings."
    final_string = ""
    for char in l:
        final_string += char
    return final_string


def justify(s: str, length: int) -> str:
    """
    Justify a string (s) and make it
    fit to a specific length (length).
    """
    # check the string introduced
    checkString(s)
    
    for line in s.splitlines():
        if len(line.lstrip()) < 1:
            # there's nothing to do here
            continue

        while len(line) < length - 1:
            # extend the spaces until
            # they are enough...
            char_count = 0
            line_list = list(line)

            for char in line_list:
                if char == " ":
                    line_list.insert(char_count, " ")
                    char_count += 2
                    continue
                char_count += 1

            line = list_to_string(line_list)

            if len(line) > length - 1:
                line.replace("  ", " ")

    return s


def justify_bytes(b: bytes, length: int) -> bytes:
    """
    Same function than
    text_formatter.justify.justify(), but taking
    bytes instead of standard strings.
    """
    checkBytes(b)

    return justify(b.encode("utf-8"))
