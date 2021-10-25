"Test for text_formatter.justify"

from text_formatter import justify


def test_string_justify():
    text = """
Lorem ipsum dolor sit amet,
consectetur adipisicing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
    expected = """
Lorem  ipsum  dolor  sit  amet,
consectetur  adipicising  elit,
sed do eiusmod tempor incidiunt
ut labore et dolore magna aliqua
"""
    result = justify.justify(text, 32)
    assert result == expected
