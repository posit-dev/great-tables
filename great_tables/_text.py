from __future__ import annotations

import html
import re
from dataclasses import dataclass
from typing import Callable

import commonmark


class BaseText:
    """Abstract base class for text elements"""

    def to_html(self) -> str:
        raise NotImplementedError("Method not implemented")

    def to_latex(self) -> str:
        raise NotImplementedError("Method not implemented")

    def to_typst(self) -> str:
        raise NotImplementedError("Method not implemented")


@dataclass
class Text(BaseText):
    """As-is text"""

    text: str

    def to_html(self) -> str:
        return self.text

    def to_latex(self) -> str:
        return self.text

    def to_typst(self) -> str:
        return self.text


class Md(Text):
    """Markdown text"""

    def to_html(self) -> str:
        return _md_html(self.text)

    def to_latex(self) -> str:
        return _md_latex(self.text)

    def to_typst(self) -> str:
        return _md_typst(self.text)


class Typst(Text):
    """Typst-formatted text. Content passes through as-is in Typst context."""

    def to_html(self) -> str:
        import warnings

        warnings.warn(
            "Using the `typst()` helper function won't convert Typst to HTML. "
            "Escaping Typst string instead.",
            stacklevel=2,
        )

        return _html_escape(self.text)

    def to_latex(self) -> str:
        import warnings

        warnings.warn(
            "Using the `typst()` helper function won't convert Typst to LaTeX. "
            "Escaping Typst string instead.",
            stacklevel=2,
        )

        return _latex_escape(self.text)

    def to_typst(self) -> str:
        # Pass through as-is — content is already valid Typst
        return self.text


class Html(Text):
    """HTML text"""

    def to_html(self) -> str:
        return self.text

    def to_latex(self) -> str:
        from ._utils_render_latex import _not_implemented

        _not_implemented(
            "Using the `html()` helper function won't convert HTML to LaTeX. Escaping HTML string instead."
        )

        return _latex_escape(self.text)

    def to_typst(self) -> str:
        import warnings

        warnings.warn(
            "Using the `html()` helper function won't convert HTML to Typst. "
            "Escaping HTML string instead.",
            stacklevel=2,
        )

        return _typst_escape(self.text)


def _md_html(x: str) -> str:
    str = commonmark.commonmark(x)
    return re.sub(r"^<p>|</p>\n$", "", str)


def _md_latex(x: str) -> str:
    # TODO: Implement commonmark to LaTeX conversion (through a different library as
    # commonmark-py does not support it)
    raise NotImplementedError("Markdown to LaTeX conversion is not supported yet")


def _md_typst(x: str) -> str:
    # Direct Markdown -> Typst conversion for inline formatting in table cells.
    # Markdown and Typst share similar syntax, so we convert directly rather than
    # going through HTML. Processing order matters to avoid conflicts between
    # Markdown and Typst marker characters.
    result = x

    # 1. Extract code spans into placeholders (identical syntax in both)
    code_spans: list[str] = []

    def _save_code(m: re.Match[str]) -> str:
        code_spans.append(m.group(0))
        return f"\x00C{len(code_spans) - 1}\x00"

    result = re.sub(r"`[^`]+`", _save_code, result)

    # 2. Handle Markdown backslash escapes -> placeholders (restore as Typst escapes)
    escapes: list[str] = []

    def _save_escape(m: re.Match[str]) -> str:
        escapes.append(m.group(1))
        return f"\x00E{len(escapes) - 1}\x00"

    result = re.sub(r"\\([\\*_`~\[\]()#$@<>])", _save_escape, result)

    # 3. Escape Typst-special chars that are not Markdown syntax
    for ch in ["\\", "#", "$", "@", "<", ">"]:
        result = result.replace(ch, "\\" + ch)

    # 4. Convert links: [text](url) -> #link("url")[text]
    result = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'#link("\2")[\1]', result)

    # 5. Convert bold-italic: ***text*** -> placeholder for *_text_*
    result = re.sub(r"\*{3}(.+?)\*{3}", lambda m: f"\x00BS\x00_{m.group(1)}_\x00BE\x00", result)

    # 6. Convert bold: **text** -> placeholder for *text*
    result = re.sub(r"\*{2}(.+?)\*{2}", lambda m: f"\x00BS\x00{m.group(1)}\x00BE\x00", result)

    # 7. Convert remaining italic asterisks: *text* -> _text_
    result = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"_\1_", result)

    # 8. Convert strikethrough: ~~text~~ -> #strike[text]
    result = re.sub(r"~~(.+?)~~", r"#strike[\1]", result)

    # 9. Restore bold marker placeholders
    result = result.replace("\x00BS\x00", "*").replace("\x00BE\x00", "*")

    # 10. Restore backslash-escape placeholders as Typst escapes
    for i, ch in enumerate(escapes):
        typst_escaped = "\\" + ch if ch in r"\#$@<>*_`~[]" else ch
        result = result.replace(f"\x00E{i}\x00", typst_escaped)

    # 11. Restore code spans
    for i, code in enumerate(code_spans):
        result = result.replace(f"\x00C{i}\x00", code)

    return result


def _process_text(x: str | BaseText | None, context: str = "html") -> str:
    if x is None:
        return ""

    if context == "html":
        escape_fn = _html_escape
    elif context == "typst":
        escape_fn = _typst_escape
    else:
        escape_fn = _latex_escape

    if isinstance(x, str):
        return escape_fn(x)

    elif isinstance(x, BaseText):
        if context == "html":
            return x.to_html()
        elif context == "typst":
            return x.to_typst()
        else:
            return x.to_latex()

    raise TypeError(f"Invalid type: {type(x)}")


def _process_text_id(x: str | BaseText | None) -> str:
    return _process_text(x).replace(" ", "-")


def _html_escape(x: str) -> str:
    return html.escape(x)


def _latex_escape(text: str) -> str:
    latex_escape_regex = "[\\\\&%$#_{}~^]"
    text = re.sub(latex_escape_regex, lambda match: "\\" + match.group(), text)

    return text


def _typst_escape(text: str) -> str:
    # Typst special characters: \ # $ @ < > * _ ` ~ [ ]
    typst_escape_regex = r"[\\#$@<>*_`~\[\]]"
    text = re.sub(typst_escape_regex, lambda match: "\\" + match.group(), text)

    return text


def escape_pattern_str_latex(pattern_str: str) -> str:
    pattern = r"(\{[x0-9]+\})"

    return process_string(pattern_str, pattern, _latex_escape)


def escape_pattern_str_typst(pattern_str: str) -> str:
    pattern = r"(\{[x0-9]+\})"

    return process_string(pattern_str, pattern, _typst_escape)


def process_string(string: str, pattern: str, func: Callable[[str], str]) -> str:
    """
    Apply a function to segments of a string that are unmatched by a regex pattern.

    This function splits a string based on a regex pattern to a list of strings, and invokes the
    supplied function (in `func=`) to those list elements that *do not* match the pattern (i.e.,
    the matched components are untouched). Finally, the processed list of text fragments is then
    joined back into a single .

    Parameters
    ----------
    string
        The string to process.
    pattern
        The regex pattern used for splitting the input string.
    func
        The function applied to elements that do not match the pattern.

    Returns
    -------
    str
        A processed string.
    """

    # Split the string by the pattern
    split_result = re.split(pattern, string)

    # Apply the function to elements that do not match the pattern
    processed_list = (func(part) if not re.match(pattern, part) else part for part in split_result)

    # Recombine the list elements to obtain a selectively processed string
    combined_str = "".join(processed_list)

    return combined_str
