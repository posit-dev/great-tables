"""Patterns: the regular expressions of a query's "matches" clauses.

A pattern is in the part of regular expressions' syntax that JavaScript (the runtime), Python's
`re` (`view_rows()`, and pandas), Rust's `regex` (Polars) and RE2 (PyArrow) read alike, and is
translated for each of them so that it means the same:

- characters, with `\\` before punctuation for the character itself, and `\\n`, `\\t`, `\\r`, `\\f`
  and `\\v`; `.`, any character but a line break (`\\n`); `^` and `$`, the start and the end of
  the text;
- classes, as `[a-z_]` and `[^0-9]`; and `\\d`, `\\w` and `\\s` (or `\\D`, `\\W` and `\\S`, not in a
  class), ASCII's digits, word characters and white space, `[0-9]`, `[0-9A-Z_a-z]` and
  `[\\t\\n\\v\\f\\r ]`;
- groups, `(...)` or `(?:...)`, and `|`;
- repeats: `*`, `+`, `?`, `{n}`, `{n,}` and `{n,m}` (up to 1000), each lazy with a `?` after it.

A pattern that starts with `(?i)` ignores case (as each of them does, alike for ASCII's letters);
in a query's text, that's the flag `i`, as in `/^st\\./i`.

The runtime reads and translates patterns the same way (packages/gti/src/pattern.ts), with the
same errors (where they are counted in characters, here, rather than UTF-16 code units).
"""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Literal

_SYNTAX = "^$\\.*+?()[]{}|"
_CLASSES = {"d": "0-9", "w": "0-9A-Z_a-z", "s": "\\t\\n\\v\\f\\r "}
_PUNCT = re.compile(r"[!-/:-@\[-`{-~]")
_REPEAT = re.compile(r"\{([0-9]+)(,([0-9]*))?\}")
_CASE = "(?i)"
_ESCAPE = re.compile(r"\\.", re.S)
# (A query's text can't have a line break in a pattern, but the escape for it means the same)
_TO_ESCAPE = re.compile(r"\\.|[/\n\r]", re.S)
_ESCAPES = {"/": "\\/", "\n": "\\n", "\r": "\\r"}
# (Ignoring case, Python's `re` has i, I, İ and ı as one letter, which JavaScript, Rust's `regex`
# and RE2 don't: so `view_rows()` matches İ and ı as two noncharacters, which have no case)
_DOTTED = {0x130: 0xFDD0, 0x131: 0xFDD1}

# What a pattern is translated for: JavaScript's `RegExp` (with the `u` flag); Python's `re`, as
# `view_rows()` matches with it; or the code (Polars', pandas' and PyArrow's regexes)
_Target = Literal["js", "py", "code"]


class PatternError(ValueError):
    """A pattern that can't be read: what's wrong, and where (`at`, in characters)."""

    def __init__(self, message: str, at: int):
        super().__init__(message)
        self.at = at


def _translate(source: str, target: _Target) -> str:
    """A pattern (without its `(?i)`) translated for a target. Raises `PatternError`."""
    i = 0
    depth = 0
    out: list[str] = []
    # What's before: something to repeat, a repeat (which only `?` can follow), or neither
    last: Literal["atom", "repeat"] | None = None

    def fail(message: str, at: int | None = None) -> PatternError:
        return PatternError(message, i if at is None else at)

    def peek() -> str:
        return source[i] if i < len(source) else ""

    # A character (after a `\`, it's escaped), or a class's escape, as `\d`
    def atom(in_class: bool) -> str:
        nonlocal i
        at = i
        c = peek()
        i += len(c)
        if c != "\\":
            return c
        e = peek()
        if e == "":
            raise fail('expected a character after "\\"', at)
        i += 1
        if e in "dDwWsS":
            if in_class and e.isupper():
                raise fail(f'"\\{e}" can\'t be in a class', at)
            return f"\\{e}"
        k = "nrtfv".find(e)
        if k < 0 and not _PUNCT.fullmatch(e):
            raise fail(
                f'"\\{e}" isn\'t an escape a pattern can have (\\d, \\w, \\s, \\D, \\W, \\S, \\n, '
                "\\t, \\r, \\f, \\v, or \\ before punctuation)",
                at,
            )
        return e if k < 0 else "\n\r\t\f\v"[k]

    def is_set(a: str) -> bool:
        return len(a) == 2 and a[0] == "\\"

    # A character or a class's escape, in a class or not
    def item(a: str, in_class: bool) -> str:
        if is_set(a):
            letter = a[1]
            body = _CLASSES[letter.lower()]
            return body if in_class else f"[{'^' if letter.isupper() else ''}{body}]"
        escaped = ("\\]^-[" if target == "js" else "\\]^-[&~|") if in_class else _SYNTAX
        return f"\\{a}" if a in escaped else a.translate(_DOTTED) if target == "py" else a

    def span(a: str, b: str) -> str:
        lo, hi = ord(a), ord(b)
        if target != "py" or lo > 0x131 or hi < 0x130:
            return f"{item(a, True)}-{item(b, True)}"
        # (Without İ and ı, but with what they're matched as)
        parts = [(lo, 0x12F), (0x132, hi)]
        return "".join(
            f"{item(chr(start), True)}-{item(chr(end), True)}"
            for start, end in parts
            if start <= end
        ) + "".join(chr(_DOTTED[c]) for c in _DOTTED if lo <= c <= hi)

    def klass() -> str:
        nonlocal i
        body = "^" if peek() == "^" else ""
        i += len(body)
        if peek() == "]":
            raise fail('a class can\'t be empty (a "]" in it must be escaped: "\\]")')
        while True:
            c = peek()
            if c == "":
                raise fail('expected "]"')
            if c == "]":
                i += 1
                return f"[{body}]"
            if c == "[":
                raise fail('"[" in a class must be escaped: "\\["')
            at = i
            a = atom(True)
            if peek() != "-" or i + 1 >= len(source) or source[i + 1] == "]":
                body += item(a, True)
                continue
            i += 1
            if peek() == "[":
                raise fail('"[" in a class must be escaped: "\\["')
            to = i
            b = atom(True)
            if is_set(a) or is_set(b):
                raise fail(
                    f'"{a if is_set(a) else b}" can\'t be in a range', at if is_set(a) else to
                )
            if ord(a) > ord(b):
                raise fail(f'the range "{source[at:i]}" is out of order', at)
            body += span(a, b)

    if source == "":
        raise fail("expected a pattern")
    while i < len(source):
        at = i
        c = peek()
        if c in "*+?{":
            repeat = c
            if c == "{":
                found = _REPEAT.match(source, i)
                if found is None:
                    raise fail(
                        '"{" must start a repeat, as in {2}, {2,} or {2,5} (or be escaped: "\\{")'
                    )
                low, high = found.group(1), found.group(3) or ""
                if int(low) > 1000 or (high != "" and (int(high) > 1000 or int(high) < int(low))):
                    raise fail(
                        "a repeat can be at most 1000, and its first number no more than its second"
                    )
                repeat = found.group()
            if last != "atom":
                raise fail(f'"{c}" must follow something to repeat')
            i += len(repeat)
            if peek() == "?":
                repeat += "?"
                i += 1
            out.append(repeat)
            last = "repeat"
            continue
        i += 1
        last = "atom"
        if c == "(":
            if peek() == "?":
                if source[i + 1 : i + 2] != ":":
                    raise fail(
                        '"(?" must be "(?:" (a pattern can\'t have lookarounds, named groups or '
                        "flags)",
                        at,
                    )
                i += 2
            depth += 1
            out.append("(?:")
            last = None
        elif c == ")":
            if depth == 0:
                raise fail('")" must close a "(" (or be escaped: "\\)")', at)
            depth -= 1
            out.append(")")
        elif c in "|^$":
            # (Python's `$` is before a line break at the end, too)
            out.append("\\Z" if c == "$" and target == "py" else c)
            last = None
        elif c in "]}":
            raise fail(f'"{c}" must be escaped: "\\{c}"', at)
        elif c == ".":
            out.append("[^\\n]" if target == "js" else ".")
        elif c == "[":
            out.append(klass())
        else:
            i = at
            out.append(item(atom(False), False))
    if depth > 0:
        raise fail('expected ")"')
    return "".join(out)


def _split(value: str) -> tuple[str, bool]:
    # A pattern's source, and whether it ignores case
    return (value[len(_CASE) :], True) if value.startswith(_CASE) else (value, False)


def read_pattern(source: str, ignore_case: bool) -> str:
    """A pattern from a query's text (between its slashes), with whether it ignores case (its
    flag `i`), as a query has it: without escapes before a slash (which only the text needs).

    Raises `PatternError` for a pattern that isn't one.
    """
    _translate(source, "js")
    unescaped = _ESCAPE.sub(lambda m: "/" if m.group() == "\\/" else m.group(), source)
    return (_CASE if ignore_case else "") + unescaped


def check_pattern(value: str) -> str:
    """A query's pattern, checked, as `read_pattern()` writes it.

    Raises `PatternError` (where in `value`) for a pattern that isn't one.
    """
    source, ignore_case = _split(value)
    try:
        return read_pattern(source, ignore_case)
    except PatternError as err:
        err.at += len(value) - len(source)
        raise


def pattern_search(value: str) -> Callable[[str], bool]:
    """A (checked) pattern as a test of text: whether it has a match, as the runtime has it (with
    Python's `re`)."""
    source, ignore_case = _split(value)
    regex = re.compile(_translate(source, "py"), re.IGNORECASE if ignore_case else 0)
    return lambda text: regex.search(text.translate(_DOTTED)) is not None


def pattern_code(value: str) -> str:
    """A (checked) pattern for the code: a regex as Polars, pandas and PyArrow read it.

    (Python's `re`, which pandas uses for a column that isn't of PyArrow's strings, has `$` match
    before a line break at the end of the text, too; and ignoring case, has i, I, İ and ı as one
    letter.)
    """
    source, ignore_case = _split(value)
    return (_CASE if ignore_case else "") + _translate(source, "code")


def format_pattern(value: str) -> str:
    """A (checked) pattern as a query's text has it: between slashes, with the flag `i` to ignore
    case."""
    source, ignore_case = _split(value)
    escaped = _TO_ESCAPE.sub(lambda m: _ESCAPES.get(m.group(), m.group()), source)
    return f"/{escaped}/{'i' if ignore_case else ''}"
