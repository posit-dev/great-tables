from __future__ import annotations

import re
from typing import Any, Union

# These helpers build the few HTML elements that the renderer composes as nested tags (the column
# labels, spanners and stubhead, and the `<colgroup>`). They serialize exactly as py-htmltools
# does (children on their own lines with two-space indentation, a lone text child kept inline),
# so the rendered HTML is unchanged from when that package was used.

__all__ = ("HTML", "Tag", "TagList", "css", "html_escape")


class HTML(str):
    """A string of markup that is inserted as is (i.e., without escaping)."""

    __slots__ = ()


TagChild = Union["Tag", "TagList", str, int, float, None, list[Any], tuple[Any, ...]]

# Elements written as `<name/>` when they have no children
_VOID_TAG_NAMES = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "command",
        "embed",
        "hr",
        "img",
        "input",
        "keygen",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }
)

_TEXT_ESCAPES = {"&": "&amp;", ">": "&gt;", "<": "&lt;"}
_ATTR_ESCAPES = {**_TEXT_ESCAPES, '"': "&quot;", "'": "&apos;", "\r": "&#13;", "\n": "&#10;"}


def html_escape(text: str, attr: bool = False) -> str:
    """Escape `text` for use as element content (or, with `attr=True`, as an attribute value)."""

    # (`&` comes first in both tables so that the entities added afterward aren't re-escaped)
    for char, entity in (_ATTR_ESCAPES if attr else _TEXT_ESCAPES).items():
        text = text.replace(char, entity)
    return text


def css(**kwargs: str | float | None) -> str | None:
    """Build a style declaration string, skipping `None` values (e.g., `width:10px;`).

    Underscores and camelCase in the property names become hyphens (`font_size` and `fontSize` both
    give `font-size`). Returns `None` (so that no style attribute is written) if every value is
    `None`.
    """

    declarations = ""
    for name, value in kwargs.items():
        if value is None:
            continue
        name = re.sub("([A-Z])", r"-\1", name).lower().replace("_", "-")
        declarations += f"{name}:{value};"
    return declarations or None


def _flatten_children(children: Any) -> list[Tag | str]:
    """Flatten nested lists/tuples/`TagList`s of children, dropping `None` and stringifying numbers."""

    flat: list[Tag | str] = []
    for child in children:
        if isinstance(child, (list, tuple, TagList)):
            flat.extend(_flatten_children(child))
        elif child is None:
            continue
        elif isinstance(child, (Tag, str)):
            flat.append(child)
        elif isinstance(child, (int, float)):
            flat.append(str(child))
        else:
            raise TypeError(f"Invalid HTML tag child of type {type(child).__name__}.")
    return flat


def _render_text(text: str) -> str:
    return text if isinstance(text, HTML) else html_escape(text)


def _render_children(children: list[Tag | str], indent: int) -> str:
    """Render children one per line; consecutive text children run together on a line."""

    out = ""
    prev_was_tag = True
    for i, child in enumerate(children):
        is_tag = isinstance(child, Tag)
        if i > 0 and (prev_was_tag or is_tag):
            out += "\n"
        if is_tag:
            out += child._render(indent)
        else:
            if prev_was_tag:
                out += "  " * indent
            out += _render_text(child)
        prev_was_tag = is_tag
    return out


class Tag:
    """An HTML element.

    Attribute names have a trailing underscore removed and other underscores turned into hyphens
    (so `class_=` gives `class` and `aria_label=` gives `aria-label`). An attribute with a value of
    `None` or `False` is omitted and one with `True` is written as empty.
    """

    def __init__(self, name: str, *children: TagChild, **attrs: str | float | bool | None):
        self.name = name
        self.children = _flatten_children(children)
        self.attrs: dict[str, str] = {}
        for key, value in attrs.items():
            if value is None or value is False:
                continue
            key = key.removesuffix("_").replace("_", "-")
            self.attrs[key] = "" if value is True else str(value)

    def _render(self, indent: int = 0) -> str:
        pad = "  " * indent
        open_tag = pad + "<" + self.name
        for key, value in self.attrs.items():
            open_tag += f' {key}="{html_escape(value, attr=True)}"'

        close_tag = f"</{self.name}>"

        if not self.children:
            return open_tag + ("/>" if self.name in _VOID_TAG_NAMES else ">" + close_tag)

        if len(self.children) == 1 and isinstance(self.children[0], str):
            return open_tag + ">" + _render_text(self.children[0]) + close_tag

        return f"{open_tag}>\n{_render_children(self.children, indent + 1)}\n{pad}{close_tag}"

    def __str__(self) -> str:
        return self._render()

    def __repr__(self) -> str:
        return str(self)


class TagList:
    """A sequence of HTML elements (and text) with no enclosing element."""

    def __init__(self, *children: TagChild):
        self.children = _flatten_children(children)

    def __iter__(self):
        return iter(self.children)

    def __str__(self) -> str:
        return _render_children(self.children, 0)

    def __repr__(self) -> str:
        return str(self)
