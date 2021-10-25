"Test for text_formatter.justify"

from text_formatter import justify
from text_formatter.exceptions import InvalidString

import pytest


def test_string_justify():
    text = """Lorem ipsum dolor sit amet,
consectetur adipisicing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
    expected = """Lorem   ipsum  dolor  sit  amet,
consectetur   adipicising  elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
    result = justify.justify(text, 32)
    assert result == expected


def test_justify_error():
    text = "aa á aa"  # this will certainly fail
    with pytest.raises(
        InvalidString,
        match="String didn't satisfied what we expected: char 'á' is not on the allowed chars",
    ):
        justify.justify(text)
