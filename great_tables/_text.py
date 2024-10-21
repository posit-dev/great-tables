from __future__ import annotations

import html
import re
from dataclasses import dataclass
from typing import Callable

import commonmark


@dataclass
class Text:
    text: str

    def to_html(self) -> str:
        return self.text

    def to_latex(self) -> str:
        return self.text


@dataclass
class Md(Text):
    """Markdown text"""

    def to_html(self) -> str:
        return _md_html(self.text)

    def to_latex(self) -> str:
        return _md_latex(self.text)


@dataclass
class Html(Text):
    """HTML text"""

    def to_html(self) -> str:
        return self.text

    def to_latex(self) -> str:
        return self.text


def _md_html(x: str) -> str:
    str = commonmark.commonmark(x)
    return re.sub(r"^<p>|</p>\n$", "", str)


def _md_latex(x: str) -> str:

    # TODO: Implement commonmark to LaTeX conversion (through a different library as
    # commonmark-py does not support it)
    raise NotImplementedError("Markdown to LaTeX conversion is not supported yet")


def _process_text(x: str | Text | None, context: str = "html") -> str:

    from great_tables._helpers import UnitStr

    if x is None:
        return ""

    escape_fn = _html_escape if context == "html" else _latex_escape

    if isinstance(x, str):

        return escape_fn(x)

    elif isinstance(x, (Md, Text, Html, UnitStr)):

        return x.to_html() if context == "html" else x.to_latex()

    raise TypeError(f"Invalid type: {type(x)}")


def _process_text_id(x: str | Text | None) -> str:
    return _process_text(x)


def _html_escape(x: str) -> str:
    return html.escape(x)


def _latex_escape(text: str) -> str:

    latex_escape_regex = "[\\\\&%$#_{}~^]"
    text = re.sub(latex_escape_regex, lambda match: "\\" + match.group(), text)

    return text


def escape_pattern_str_latex(pattern_str: str) -> str:

    pattern = r"(\{[x0-9]+\})"

    return process_string(pattern_str, pattern, _latex_escape)


def process_string(string: str, pattern: str, func: Callable[[str], str]) -> str:
    """
    Process a string selectively based on a pattern.

    This function splits a string based on a pattern and applies a function to elements that do not
    match the pattern. The processed elements are then recombined to obtain a selectively processed
    string.

    Args:
        string (str): The string to process.
        pattern (str): The pattern to split the string by.
        func (Callable[[str], str]): The function applied to elements that do not match the pattern.

    Returns:
        str: The selectively processed string.
    """

    # Split the string by the pattern
    split_result = re.split(pattern, string)

    # Apply the function to elements that do not match the pattern
    processed_list = [func(part) if not re.match(pattern, part) else part for part in split_result]

    # Recombine the list elements to obtain a selectively processed string
    combined_str = "".join(processed_list)

    return combined_str
