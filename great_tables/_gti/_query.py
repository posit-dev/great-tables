"""Queries: the filters of an interactive table's view, in the data's terms.

A query is what `<gt-table>`'s `filter` property takes and gives, as JSON:

    {"and": [{"col": "status", "op": "in", "value": ["single-tier", None]},
             {"col": "population_2021", "op": "gte", "value": 10000}]}

Rows are kept when every clause keeps them. A clause's `op` is one of:

- `"contains"`, for a column with a text filter: keeps the rows whose cell shows `value` (a string,
  trimmed), ignoring case and accents, as the search does. Blank text keeps every row.
- `"matches"`, for a column with a text filter: keeps the rows whose cell's text (as "contains"
  matches it, but with its case and accents) has a match of `value` anywhere in it: a pattern,
  a regular expression in the part of their syntax that `_pattern.py` has (where `^` and `$`
  are the text's start and end), with case unless it starts with `(?i)`.
- `"in"`, for a facet: keeps the rows with one of `value`'s values (a non-empty list of them, as
  JSON holds them, like the spec's `values`; `None` is a missing value). For a bool filter: the
  rows with `value`'s one value (`[True]`, `[False]`, or `[None]`).
- `"gte"` and `"lte"`, for a range: keep the rows with a number that's at least (or at most)
  `value`, a finite number. Missing values, NaN and infinities are never kept. For a date filter:
  the rows with a date (or date and time) on or after (or on or before) `value`, ISO 8601 text: a
  date, `"2015-06-15"`, or for a column of dates and times, either that (its midnight) or a date
  and time, `"2015-06-15T09:30"` (with seconds, and up to six digits of their fraction, if
  wanted). Missing values are never kept.
- `"gt"` and `"lt"`, as `"gte"` and `"lte"`, but keeping the rows with a number more than (or less
  than) `value`, or a date (or date and time) after (or before) it: for a column of dates and
  times, a date is its midnight, so `"gt"` and `"2015-06-15"` keeps 09:30 that day.
- `"top_n"` and `"bottom_n"`, for a range or a date filter: keep the rows with the `value` largest
  (or smallest) numbers or dates among all the data's rows (not just those the rest of the query
  keeps), and those tied with the last of them, so maybe more than `value` rows; `value` is a
  whole number, at least 1. Missing values, NaN and infinities are never counted, nor kept.
- `"is_null"`, for a column with any filter, and without a `value`: keeps the rows whose value is
  missing (`None`, or NaN in a column of floats), as the spec's `missing` has them.

A part of the query can also be a group: `{"or": [parts]}` keeps the rows any of its parts keeps,
`{"and": [parts]}` the rows every one keeps, and `{"not": part}` the rows its part doesn't (so
the rows whose value is missing, which a clause leaves out, are kept), nested as wanted:

    {"and": [{"col": "status", "op": "in", "value": ["city"]},
             {"or": [{"col": "population_2021", "op": "gte", "value": 10000},
                     {"not": {"col": "name", "op": "contains", "value": "ville"}}]}]}

A column has at most one clause with each `op` (in the query, and in each `and` of a group), and a
"contains" clause in an "or" or a "not" needs text. Queries are checked as the runtime checks them
(`setFilterQuery()` in packages/gti/src/filter.ts), so that a view Python accepts is one
`<gt-table>` shows; and they're compiled, with a sort, to Narwhals expressions (`view_rows()`, the
rows a table's view shows) and to code for Polars, pandas, or Narwhals (`query_code()`).

Narwhals is needed only for compiling, and is imported by the functions that do it.
"""

from __future__ import annotations

import datetime as dt
import json
import math
import operator
import re
import unicodedata
from collections.abc import Callable, Iterator, Mapping, Sequence
from dataclasses import dataclass
from decimal import Decimal
from html.parser import HTMLParser
from typing import TYPE_CHECKING, Any, Literal

from ._pattern import (
    PatternError,
    check_pattern,
    format_pattern,
    pattern_code,
    pattern_search,
    read_pattern,
)
from ._spec import (
    CodeBackend,
    CodeColumnSpec,
    CodeSpec,
    FilterSpec,
    Spec,
    ViewSpec,
    _json_value,
)

if TYPE_CHECKING:
    import narwhals as nw

    from .._tbl_data import ColumnKind
    from ..gt import GT

Query = dict[str, list[dict[str, Any]]]

# A sort: column names, each with whether it's descending
SortKeys = tuple[tuple[str, bool], ...]

Backend = CodeBackend

# The filter types each op is for
OP_TYPES = {
    "contains": ("text",),
    "matches": ("text",),
    "in": ("facet", "bool"),
    "gte": ("range", "date"),
    "lte": ("range", "date"),
    "gt": ("range", "date"),
    "lt": ("range", "date"),
    "top_n": ("range", "date"),
    "bottom_n": ("range", "date"),
    "is_null": ("text", "facet", "bool", "range", "date"),
}

# The ops that compare to a bound, by their symbols in a query's text (and code's)
_SYMBOLS = {"gte": ">=", "lte": "<=", "gt": ">", "lt": "<"}
_COMPARISONS = {symbol: op for op, symbol in _SYMBOLS.items()}

# The ops no filter has, whose clauses the runtime keeps with the groups
_GROUPED = ("is_null", "matches", "gt", "lt", "top_n", "bottom_n")

# The ops that keep the rows with a column's largest (or smallest) values, by their words in a
# query's text
_EXTREMES = {"top_n": "top", "bottom_n": "bottom"}

# The largest count of rows they can have (as the runtime holds it, a double: an integer that's
# exact)
_MAX_COUNT = 2**53 - 1

# A date, or a date and time, as ISO 8601 text (as the runtime's `dateKey()` reads it)
_DATE_TEXT = re.compile(
    r"([0-9]{4})-([0-9]{2})-([0-9]{2})"
    r"(?:T([0-9]{2}):([0-9]{2})(?::([0-9]{2})(?:\.([0-9]{1,6}))?)?)?"
)

# What `String.prototype.trim()` removes (JavaScript's white space and line terminators), which
# isn't what `str.strip()` does
JS_WHITESPACE = (
    "\t\n\v\f\r \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a"
    "\u2028\u2029\u202f\u205f\u3000\ufeff"
)

_VALUE_TYPES = (bool, int, float, str, Decimal, dt.date, dt.time)


# Checking ----


def check_query(query: Any) -> Query | None:
    """Check a query's shape and values, and normalize them (as JSON values, in a new query).

    This is what can be checked without the table: that the columns have filters, and of the
    right types, is checked when the table is built (`check_view()`). A query can be given as
    text (`parse_query()`).

    Its groups are as the runtime writes them (`setFilterQuery()`): an `and` at the top, or in an
    `and` (or an `or` in an `or`), is spliced into it, and a group of one part is that part. (So
    the query's parts are clauses, `or` groups and `not` groups.)
    """
    if isinstance(query, str):
        try:
            query = parse_query(query)
        except ValueError as err:
            raise ValueError(f"`filter=` can't be read as a query: {err}.") from None
    if query is None:
        return None
    parts = query.get("and") if isinstance(query, Mapping) else None
    if (
        not isinstance(query, Mapping)
        or set(query) != {"and"}
        or not isinstance(parts, (list, tuple))
    ):
        raise ValueError(
            '`filter=` must be a query, `{"and": [parts]}`, or `None` (no filter), not '
            f"{query!r}."
        )

    checked: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()

    # (A clause not in a group, as one of a column's filter's)
    def add_clause(clause: dict[str, Any]) -> None:
        col, op = clause["col"], clause["op"]
        if (col, op) in seen:
            raise ValueError(f"The filter has more than one {op!r} clause on column {col!r}.")
        seen.add((col, op))
        checked.append(clause)

    def add(item: dict[str, Any]) -> None:
        if _is_clause(item):
            add_clause(item)
        elif "and" in item:
            for part in item["and"]:
                add(part)
        else:
            checked.append(item)

    def visit(item: Any, where: str) -> None:
        kind = _group_kind(item)
        if kind == "and":
            for i, part in enumerate(_group_parts(item, kind)):
                visit(part, f"part {i} of an 'and' group")
        elif kind is not None:
            add(_normal_item(item, where))
        else:
            add_clause(_check_clause(item, where))

    for i, part in enumerate(parts):
        visit(part, f"clause {i}")
    return {"and": checked}


def _is_clause(item: Mapping[str, Any]) -> bool:
    return "col" in item


def _group_kind(item: Any) -> Literal["or", "and", "not"] | None:
    """The kind of group a part of a query is, if it's one: a mapping with just an "or", "and" or
    "not"."""
    if isinstance(item, Mapping) and len(item) == 1:
        (key,) = item
        if key in ("or", "and", "not"):
            return key
    return None


def _group_parts(item: Mapping[str, Any], kind: str) -> Sequence[Any]:
    parts = item[kind]
    if not isinstance(parts, (list, tuple)) or len(parts) == 0:
        raise ValueError(
            f"The filter's {kind!r} group needs a list of at least one part, not {parts!r}."
        )
    return parts


def _normal_item(item: Any, where: str) -> dict[str, Any]:
    """A part of a query in a group, checked, as the runtime writes it (`normalItem()`)."""
    kind = _group_kind(item)
    if kind == "not":
        return {"not": _normal_item(item["not"], "part of a 'not' group")}
    if kind is None:
        clause = _check_clause(item, where)
        if clause["op"] == "contains" and fold(js_trim(clause["value"])) == "":
            raise ValueError(
                f'The filter\'s "contains" clause on column {clause["col"]!r} needs text, in an '
                '"or" or a "not" (blank text keeps every row).'
            )
        return clause
    items: list[dict[str, Any]] = []
    for i, part in enumerate(_group_parts(item, kind)):
        normal = _normal_item(part, f"part {i} of an {kind!r} group")
        items.extend(normal[kind] if kind in normal else [normal])
    if kind == "and":
        seen: set[tuple[str, str]] = set()
        for part in items:
            if _is_clause(part):
                col, op = part["col"], part["op"]
                if (col, op) in seen:
                    raise ValueError(
                        f"The filter has more than one {op!r} clause on column {col!r}, in an "
                        "'and' group."
                    )
                seen.add((col, op))
    return items[0] if len(items) == 1 else {kind: items}


def _check_clause(clause: Any, where: str) -> dict[str, Any]:
    op = clause.get("op") if isinstance(clause, Mapping) else None
    if (
        not isinstance(clause, Mapping)
        or set(clause) != ({"col", "op"} if op == "is_null" else {"col", "op", "value"})
        or not isinstance(clause["col"], str)
        or op not in OP_TYPES
    ):
        raise ValueError(
            f'The filter\'s {where} must be `{{"col": ..., "op": ..., "value": ...}}`, with a '
            'column name and an op of "contains", "matches", "in", "gte", "lte", "gt", "lt", '
            '"top_n", or "bottom_n"; or '
            '`{"col": ..., "op": "is_null"}`; or a group, `{"or": [parts]}`, '
            f'`{{"and": [parts]}}`, or `{{"not": part}}`; not {clause!r}.'
        )
    col = clause["col"]
    if op == "is_null":
        return {"col": col, "op": op}
    value = clause["value"]
    if op in ("contains", "matches"):
        if not isinstance(value, str):
            raise ValueError(
                f'The filter\'s "{op}" clause on column {col!r} needs a string, not {value!r}.'
            )
        if op == "matches":
            try:
                value = check_pattern(value)
            except PatternError as err:
                place = "the end" if err.at >= len(value) else f"character {err.at + 1}"
                raise ValueError(
                    f"The pattern of the filter's \"matches\" clause on column {col!r} can't be "
                    f"read: {err}, at {place}."
                ) from None
    elif op == "in":
        if not isinstance(value, (list, tuple)) or len(value) == 0:
            raise ValueError(
                f'The filter\'s "in" clause on column {col!r} needs a list of at least one '
                f"value, not {value!r}."
            )
        value = [_facet_value(item, col) for item in value]
    elif op in _EXTREMES:
        value = _count(value, col, op)
    else:
        value = _bound(value, col, op)
    return {"col": col, "op": op, "value": value}


def _leaves(items: Sequence[Mapping[str, Any]]) -> Iterator[Mapping[str, Any]]:
    """A (checked) query's clauses, those in its groups too, in order."""
    for item in items:
        if _is_clause(item):
            yield item
        elif "not" in item:
            yield from _leaves([item["not"]])
        else:
            yield from _leaves(item["or"] if "or" in item else item["and"])


def _facet_value(item: Any, col: str) -> Any:
    """A value of an "in" clause, as JSON holds it (as the spec's `values` do)."""
    numpy_number = getattr(getattr(item, "dtype", None), "kind", None) in ("b", "i", "u", "f")
    if not (item is None or isinstance(item, _VALUE_TYPES) or numpy_number):
        raise ValueError(
            f"The filter's \"in\" clause on column {col!r} has {item!r}, which isn't a value a "
            "column can have (a number, string, boolean, date or time, or `None`)."
        )
    value = _json_value(item)
    if value is None and item is not None:
        raise ValueError(
            f"The filter's \"in\" clause on column {col!r} has {item!r}, which can't be chosen "
            "(use `None` for a missing value)."
        )
    return value


def _count(value: Any, col: str, op: str) -> int:
    # (A whole number, as JSON has it: so 10.0 is 10, as the runtime has it)
    numpy_number = getattr(getattr(value, "dtype", None), "kind", None) in ("i", "u", "f")
    if isinstance(value, (int, float, Decimal)) and not isinstance(value, bool) or numpy_number:
        number = _json_value(value)
        if number is not None and float(number).is_integer() and 1 <= number <= _MAX_COUNT:
            return int(number)
    raise ValueError(
        f"The filter's {op!r} clause on column {col!r} needs a whole number, at least 1, not "
        f"{value!r}."
    )


def _bound(value: Any, col: str, op: str) -> int | float | str:
    numpy_number = getattr(getattr(value, "dtype", None), "kind", None) in ("i", "u", "f")
    if isinstance(value, (int, float, Decimal)) and not isinstance(value, bool) or numpy_number:
        bound = _json_value(value)
        if bound is not None:
            return bound
    if isinstance(value, dt.datetime):
        if value.tzinfo is not None:
            raise ValueError(
                f"The filter's {op!r} clause on column {col!r} has {value!r}, which has a time "
                "zone: give a date and time without one."
            )
        # (As Python's datetime has it, to the microsecond: a pandas `Timestamp` too)
        return dt.datetime.isoformat(value)
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, str) and parse_date(value) is not None:
        return value
    raise ValueError(
        f"The filter's {op!r} clause on column {col!r} needs a finite number, or a date: as "
        'ISO 8601 text ("2015-06-15", or with a time, "2015-06-15T09:30"), or a '
        f"`datetime.date` or `datetime.datetime`; not {value!r}."
    )


def parse_date(text: str) -> dt.date | dt.datetime | None:
    """A date bound's ISO 8601 text (as `filter.ts` has it) as a date, or a date and time; or
    `None` if it isn't one."""
    found = _DATE_TEXT.fullmatch(text)
    if found is None:
        return None
    year, month, day, hour, minute, second, fraction = found.groups()
    try:
        date = dt.date(int(year), int(month), int(day))
        if hour is None:
            return date
        return dt.datetime(
            date.year,
            date.month,
            date.day,
            int(hour),
            int(minute),
            int(second or 0),
            int((fraction or "").ljust(6, "0")),
        )
    except ValueError:
        return None


# Queries as text, as the runtime reads and writes them (packages/gti/src/query.ts) ----
#
#     status in ("single-tier", null) and population >= 10000 and `Name of town` contains "ville"
#
# Clauses joined by `and` and `or`, each after `not` if wanted, and grouped in parentheses as
# wanted (`not` binding tighter than `and`, and `and` tighter than `or`); a clause is a column,
# then `contains` and a string, `matches` and a pattern (between slashes, with the flag `i` to
# ignore case, as in `/^st\./i`), `in` and values in parentheses, `>=`, `<=`, `>` or `<` and a
# number or a date (a string), `top` or `bottom` and a whole number (digits, at least 1), or
# `is null`; `x not in (...)`, `x not contains "..."`, `x not matches /.../` and
# `x is not null` are `not` and those. A column is a name of letters, digits and underscores (not
# starting with a digit), or any name in backticks (a backtick in it doubled); `not` before an op is
# a column's name. Strings and numbers are as in JSON; the other values are `true`, `false` and
# `null`. Keywords can be in any case. Empty text is no query. Errors are the runtime's, word for word.

_NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
_STRING = re.compile(r'"(?:[^"\\\x00-\x1f]|\\["\\/bfnrt]|\\u[0-9a-fA-F]{4})*"')
_NUMBER = re.compile(r"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?")
_SPACE = re.compile(r"[ \t\n\r]*")
# (A pattern, on one line: escapes, and classes, where a slash needn't be escaped; then its flags)
_PATTERN = re.compile(
    r"/(?:[^\\/\[\n\r]|\\[^\n\r]|\[(?:[^\\\]\n\r]|\\[^\n\r])*\]?)*(/?)([A-Za-z0-9_]*)"
)
_WORDS = {"true": True, "false": False, "null": None}
# (The ops that are words)
_OP_WORDS = ("in", "contains", "matches", "is", "top", "bottom")
# (The ops that can be after `not`, as in `x not in (...)`)
_NEGATED = ("contains", "matches", "in")
_VALUE_EXPECTED = "expected a value: a string in double quotes, a number, true, false or null"


@dataclass
class _Token:
    kind: Literal["name", "quoted", "string", "regex", "number", "symbol", "end"]
    # The text of a name or symbol, or a string's, pattern's or number's value
    value: Any
    at: int


class _QueryParser:
    def __init__(self, text: str):
        self.text = text
        self.at = 0
        self.token = self._next()

    def fail(self, message: str, where: _Token | None = None) -> Any:
        where = where or self.token
        place = "the end" if where.kind == "end" else f"character {where.at + 1}"
        raise ValueError(f"{message}, at {place}")

    def _next(self) -> _Token:
        text = self.text
        self.at = _SPACE.match(text, self.at).end()  # type: ignore[union-attr]
        start = self.at
        if start >= len(text):
            return _Token("end", None, start)
        char = text[start]
        if name := _NAME.match(text, start):
            self.at = name.end()
            return _Token("name", name.group(), start)
        if char == "`":
            end = start + 1
            name_chars: list[str] = []
            while True:
                if end >= len(text):
                    self.fail(
                        "a column name in backticks must end with a backtick",
                        _Token("end", None, end),
                    )
                if text[end] == "`":
                    if text[end + 1 : end + 2] != "`":
                        break
                    end += 1
                name_chars.append(text[end])
                end += 1
            self.at = end + 1
            return _Token("quoted", "".join(name_chars), start)
        if char == '"':
            string = _STRING.match(text, start)
            if string is None:
                self.fail(
                    "a string must end with a double quote (with escapes as in JSON)",
                    _Token("symbol", char, start),
                )
            self.at = string.end()  # type: ignore[union-attr]
            return _Token("string", json.loads(string.group()), start)  # type: ignore[union-attr]
        if char == "/":
            pattern = _PATTERN.match(text, start)
            assert pattern is not None
            self.at = pattern.end()
            if pattern.group(1) == "":
                self.fail("a pattern must end with a slash", _Token("symbol", char, start))
            flags = pattern.group(2)
            # (Where its closing slash is)
            end = pattern.start(1)
            if flags not in ("", "i"):
                self.fail('a pattern can have only the flag "i"', _Token("symbol", flags, end + 1))
            try:
                return _Token("regex", read_pattern(text[start + 1 : end], flags == "i"), start)
            except PatternError as err:
                where = start + 1 + err.at
                self.fail(str(err), _Token("symbol", text[where], where))
        if number := _NUMBER.match(text, start):
            literal = number.group()
            # (As JavaScript reads it: a double, even for an integer)
            value = float(literal)
            if not math.isfinite(value):
                self.fail(f"the number {literal} is too large", _Token("symbol", literal, start))
            self.at = number.end()
            return _Token(
                "number", value if any(c in literal for c in ".eE") else int(value), start
            )
        symbol = text[start : start + 2] if text[start : start + 2] in (">=", "<=") else char
        self.at = start + len(symbol)
        return _Token("symbol", symbol, start)

    def advance(self) -> _Token:
        token = self.token
        self.token = self._next()
        return token

    def is_word(self, word: str) -> bool:
        return self.token.kind == "name" and self.token.value.lower() == word

    def is_symbol(self, symbol: str) -> bool:
        return self.token.kind == "symbol" and self.token.value == symbol

    def value(self) -> Any:
        if self.token.kind in ("string", "number"):
            return self.advance().value
        for word, value in _WORDS.items():
            if self.is_word(word):
                self.advance()
                return value
        return self.fail(_VALUE_EXPECTED)

    def clause(self) -> dict[str, Any]:
        if self.token.kind not in ("name", "quoted"):
            self.fail("expected a column name")
        col = self.advance().value
        if self.is_word("is"):
            self.advance()
            negated = self.is_word("not")
            if negated:
                self.advance()
            if not self.is_word("null"):
                self.fail('expected "null"' if negated else 'expected "null" or "not null"')
            self.advance()
            clause = {"col": col, "op": "is_null"}
            return {"not": clause} if negated else clause
        # (`not` before `contains`, `matches` or `in` is a `not` of the clause)
        if self.is_word("not"):
            self.advance()
            if not any(self.is_word(op) for op in _NEGATED):
                self.fail('expected "contains", "matches" or "in"')
            return {"not": self.op_clause(col)}
        return self.op_clause(col)

    def op_clause(self, col: str) -> dict[str, Any]:
        """A clause's op and what's after it."""
        if self.is_word("contains"):
            self.advance()
            if self.token.kind != "string":
                self.fail("expected a string in double quotes")
            return {"col": col, "op": "contains", "value": self.advance().value}
        if self.is_word("matches"):
            self.advance()
            if self.token.kind != "regex":
                self.fail("expected a pattern between slashes, as in /^st\\./")
            return {"col": col, "op": "matches", "value": self.advance().value}
        if self.is_word("in"):
            self.advance()
            if not self.is_symbol("("):
                self.fail('expected "("')
            self.advance()
            values = [self.value()]
            while not self.is_symbol(")"):
                if not self.is_symbol(","):
                    self.fail('expected "," or ")"')
                self.advance()
                values.append(self.value())
            self.advance()
            return {"col": col, "op": "in", "value": values}
        if self.token.kind == "symbol" and self.token.value in _COMPARISONS:
            op = _COMPARISONS[self.advance().value]
            if self.token.kind not in ("number", "string"):
                self.fail("expected a number, or a date in double quotes")
            return {"col": col, "op": op, "value": self.advance().value}
        if self.is_word("top") or self.is_word("bottom"):
            op = "top_n" if self.is_word("top") else "bottom_n"
            self.advance()
            # (Digits, as typed: not a fraction, an exponent or a sign)
            literal = self.text[self.token.at : self.at]
            whole = self.token.kind == "number" and literal.isascii() and literal.isdigit()
            if not whole or self.token.value < 1:
                self.fail("expected a whole number (at least 1)")
            if self.token.value > _MAX_COUNT:
                self.fail(f"the number {literal} is too large")
            return {"col": col, "op": op, "value": self.advance().value}
        return self.fail(
            'expected "contains", "matches", "in", "not", ">=", "<=", ">", "<", "top", "bottom" '
            'or "is"'
        )

    def is_not(self) -> bool:
        """Whether the token is the keyword `not` (rather than a column's name, before an op)."""
        if not self.is_word("not"):
            return False
        at = self.at
        after = self._next()
        self.at = at
        word = after.value.lower() if after.kind == "name" else None
        symbol = after.value if after.kind == "symbol" else None
        return word not in _OP_WORDS and symbol not in _COMPARISONS

    def unary(self) -> dict[str, Any]:
        if self.is_not():
            self.advance()
            return {"not": self.unary()}
        if self.is_symbol("("):
            self.advance()
            item = self.or_()
            if not self.is_symbol(")"):
                self.fail('expected "and", "or" or ")"')
            self.advance()
            return item
        return self.clause()

    def and_(self) -> dict[str, Any]:
        items = [self.unary()]
        while self.is_word("and"):
            self.advance()
            items.append(self.unary())
        return _joined("and", items)

    def or_(self) -> dict[str, Any]:
        items = [self.and_()]
        while self.is_word("or"):
            self.advance()
            items.append(self.and_())
        return _joined("or", items)

    def query(self) -> Query | None:
        if self.token.kind == "end":
            return None
        item = self.or_()
        if self.token.kind != "end":
            self.fail('expected "and", "or" or the end of the query')
        return {"and": item["and"] if "and" in item else [item]}


def _joined(kind: str, items: list[dict[str, Any]]) -> dict[str, Any]:
    # Parts joined by `or` or `and` (one part on its own; and the parts of a group of the same
    # kind spliced in)
    if len(items) == 1:
        return items[0]
    return {kind: [part for item in items for part in (item[kind] if kind in item else [item])]}


def parse_query(text: str) -> Query | None:
    """Read a query's text into a query (`None` for empty text), without checking its clauses.

    Raises `ValueError`, with the runtime's message, if the text isn't a query.
    """
    return _QueryParser(text).query()


def format_query(query: Query | None) -> str:
    """Write a (checked) query as text, as the runtime's `formatQuery()` does.

    `parse_query()` reads the text back as the same query (as `check_query()` writes it: with no
    `and` in an `and`, or `or` in an `or`, nor groups of one).
    """
    items = (query or {"and": []})["and"]
    if len(items) == 1:
        return _format_item(items[0], None)
    return " and ".join(_format_item(item, "and") for item in items)


def _format_item(item: Mapping[str, Any], inside: str | None) -> str:
    # A part of a query as text, in what it's a part of (`None` for the whole query): in
    # parentheses only where it needs them (`not` binding tighter than `and`, and `and` tighter
    # than `or`)
    if _is_clause(item):
        return f"{_format_column(item['col'])} {_format_op(item)}"
    if "not" in item:
        part = item["not"]
        if _is_clause(part) and part["op"] == "is_null":
            return f"{_format_column(part['col'])} is not null"
        if _is_clause(part) and part["op"] in _NEGATED:
            return f"{_format_column(part['col'])} not {_format_op(part)}"
        return f"not {_format_item(part, 'not')}"
    kind = "or" if "or" in item else "and"
    text = f" {kind} ".join(_format_item(part, kind) for part in item[kind])
    return text if inside is None or (kind == "and" and inside == "or") else f"({text})"


def _format_column(col: str) -> str:
    # (In backticks, unless it's letters, digits and underscores, and not an op after `not`)
    plain = _NAME.fullmatch(col) and col.lower() not in _OP_WORDS
    return col if plain else "`" + col.replace("`", "``") + "`"


def _format_op(clause: Mapping[str, Any]) -> str:
    # A clause's op and what's after it, as text
    op, value = clause["op"], clause.get("value")
    if op == "is_null":
        return "is null"
    if op == "contains":
        return f"contains {_format_value(value)}"
    if op == "matches":
        return f"matches {format_pattern(value)}"
    if op == "in":
        return f"in ({', '.join(_format_value(item) for item in value)})"
    if op in _EXTREMES:
        return f"{_EXTREMES[op]} {_format_value(value)}"
    return f"{_SYMBOLS[op]} {_format_value(value)}"


def _format_value(value: Any) -> str:
    # (As the runtime writes it: a number as `String()` does, a string as `JSON.stringify()`)
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            return _js_number(float(value))
        except OverflowError:
            return str(value)
    text = json.dumps(value, ensure_ascii=False)
    return _SURROGATE.sub(lambda m: f"\\u{ord(m.group()):04x}", text)


_SURROGATE = re.compile("[\ud800-\udfff]")


def _js_number(value: float) -> str:
    """A finite number as JavaScript's `String()` writes it: its shortest digits, laid out."""
    if value == 0:
        return "0"
    sign, digit_tuple, exponent = Decimal(repr(value)).normalize().as_tuple()
    digits = "".join(map(str, digit_tuple))
    k, n = len(digits), int(exponent) + len(digits)
    if k <= n <= 21:
        text = digits + "0" * (n - k)
    elif 0 < n <= 21:
        text = f"{digits[:n]}.{digits[n:]}"
    elif -6 < n <= 0:
        text = f"0.{'0' * -n}{digits}"
    else:
        rest = f".{digits[1:]}" if k > 1 else ""
        text = f"{digits[0]}{rest}e{'+' if n >= 1 else '-'}{abs(n - 1)}"
    return ("-" if sign else "") + text


def parse_sort(sort: Any) -> SortKeys:
    """Sort keys from a column name or a list of them (with `-` before a name for descending)."""
    if sort is None:
        return ()
    names = [sort] if isinstance(sort, str) else sort
    if not isinstance(names, (list, tuple)) or not all(isinstance(name, str) for name in names):
        raise ValueError(
            '`sort=` must be a column name (e.g., "population" or "-population", for descending '
            f"order), a list of them, or `None`, not {sort!r}."
        )
    keys: list[tuple[str, bool]] = []
    for name in names:
        descending = name.startswith("-")
        column = name[1:] if descending else name
        if column == "":
            raise ValueError(f"`sort=` has {name!r}, which isn't a column name.")
        if any(column == seen for seen, _ in keys):
            raise ValueError(f"`sort=` has column {column!r} more than once.")
        keys.append((column, descending))
    return tuple(keys)


def check_view(
    query: Query | None,
    sort: SortKeys,
    filters: list[FilterSpec],
    ranks: Mapping[str, Any],
    hidden: Sequence[str] = (),
    hideable: Sequence[str] = (),
    kinds: Mapping[str | None, ColumnKind] | None = None,
    group_by: str | None = None,
    groupable: Sequence[str] = (),
) -> ViewSpec:
    """
    Check a view against a table's filters, sortable columns, the columns readers can hide (in
    column order), and those they can group the rows by, as the runtime does. (A date filter's bounds go by its column's kind: a
    column of dates takes dates, without times.)
    """
    by_column = {f["column"]: f for f in filters}
    for clause in _leaves(query["and"] if query is not None else []):
        col, op, value = clause["col"], clause["op"], clause.get("value")
        found = by_column.get(col)
        if found is None:
            raise ValueError(
                f"The view's filter has a clause on column {col!r}, which has no filter. Give it "
                "one with `i_cols_filter()`."
            )
        if found["type"] not in OP_TYPES[op]:
            names = [
                repr(name)
                for name, types in OP_TYPES.items()
                if found["type"] in types and name != "is_null"
            ]
            ops = " or ".join([", ".join(names[:-1]), names[-1]] if len(names) > 1 else names)
            raise ValueError(
                f"The view's filter has a {op!r} clause on column {col!r}, which has a "
                f"{found['type']} filter (for {ops} clauses)."
            )
        if op in ("is_null", "matches", *_EXTREMES):
            continue
        if found["type"] == "range" and isinstance(value, str):
            raise ValueError(
                f"The view's filter has {value!r} for its {op!r} clause on column {col!r}, which "
                "has a range filter (for numbers)."
            )
        if found["type"] == "date":
            if not isinstance(value, str):
                raise ValueError(
                    f"The view's filter has {value!r} for its {op!r} clause on column {col!r}, "
                    'which has a date filter (for dates, as "2015-06-15").'
                )
            if "T" in value and (kinds or {}).get(col) != "datetime":
                raise ValueError(
                    f"The view's filter has {value!r} for its {op!r} clause on column {col!r}, "
                    "whose values are dates, without times (give a date, as "
                    f"{value.split('T')[0]!r})."
                )
        if op == "in":
            if found["type"] == "bool" and len(value) > 1:
                raise ValueError(
                    f"The view's filter has {value!r} for its 'in' clause on column {col!r}, "
                    "which has a bool filter (for one value: `[True]`, `[False]`, or `[None]`)."
                )
            keys = {_value_key(item) for item in found["values"] or [] if item is not None}
            for item in value:
                if item is not None and _value_key(item) not in keys:
                    raise ValueError(
                        f"The view's filter has {item!r}, which isn't a value of column {col!r}."
                    )
    for column, _ in sort:
        if column not in ranks:
            raise ValueError(
                f"The view can't be sorted by column {column!r}: it isn't one the table can be "
                "sorted by."
            )
    for column in hidden:
        if column not in hideable:
            raise ValueError(
                f"The view can't hide column {column!r}: it isn't one readers can hide. Make it "
                "one with `i_cols_controls(hideable=True)` (the stub and the row group column "
                "can't be)."
            )
    if group_by is not None and group_by not in groupable:
        raise ValueError(
            f"The view can't group the rows by column {group_by!r}: it isn't one readers can "
            "group them by. Make it one with `i_cols_controls(groupable=True)` (the stub can't be, "
            "and neither can a column the table can't be sorted by, or any column of a table with "
            "row groups or summary rows)."
        )
    return ViewSpec(
        filter=query,
        sort=[{"column": column, "descending": desc} for column, desc in sort],
        hidden=[column for column in hideable if column in hidden],
        group_by=group_by,
    )


def _value_key(value: Any) -> tuple[str, Any]:
    # As JavaScript tells values apart: 1 is 1.0, but not `true` or "1"
    if isinstance(value, bool):
        return ("b", value)
    if isinstance(value, (int, float)):
        return ("n", float(value))
    return ("s", value)


# Folding text, as the runtime does (`fold()` in packages/gti/src/search.ts) ----


def fold(text: str) -> str:
    """Text folded for matching: each character decomposed, without combining marks, lowercased."""
    if text.isascii():
        return text.lower()
    # (A character at a time, as the runtime does: so a final sigma is a sigma)
    return "".join(
        "".join(
            c for c in unicodedata.normalize("NFD", char) if unicodedata.category(c)[0] != "M"
        ).lower()
        for char in text
    )


def js_trim(text: str) -> str:
    return text.strip(JS_WHITESPACE)


# Reading the table body, as the runtime does ----


@dataclass
class _Element:
    tag: str
    attrs: dict[str, str | None]
    children: list[_Element | str]

    @property
    def classes(self) -> list[str]:
        return (self.attrs.get("class") or "").split()

    def text(self) -> str:
        return "".join(child if isinstance(child, str) else child.text() for child in self.children)


_VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track",
    "wbr",
}  # fmt: skip


class _Tree(HTMLParser):
    """A table's HTML, as elements (enough of a DOM for reading its cells)."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = _Element("#root", {}, [])
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        element = _Element(tag, dict(attrs), [])
        self.stack[-1].children.append(element)
        if tag not in _VOID:
            self.stack.append(element)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack[-1].children.append(_Element(tag, dict(attrs), []))

    def handle_endtag(self, tag: str) -> None:
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data: str) -> None:
        self.stack[-1].children.append(data)


def _find(element: _Element, tag: str) -> _Element | None:
    for child in element.children:
        if isinstance(child, _Element):
            if child.tag == tag:
                return child
            found = _find(child, tag)
            if found is not None:
                return found
    return None


def _body_trs(table_html: str) -> list[_Element]:
    """The `<tr>`s of a table's body (`tbody.gt_table_body`)."""
    table = _find(_parsed(table_html), "table")
    tbody = None
    if table is not None:
        tbody = next(
            (
                child
                for child in table.children
                if isinstance(child, _Element)
                and child.tag == "tbody"
                and "gt_table_body" in child.classes
            ),
            None,
        )
    if tbody is None:
        return []
    return [child for child in tbody.children if isinstance(child, _Element) and child.tag == "tr"]


def _data_cells(tr: _Element) -> list[_Element]:
    # (Not a group's label cell, as with the runtime's `dataCells()`)
    return [
        child
        for child in tr.children
        if isinstance(child, _Element)
        and child.tag in ("td", "th")
        and "gt_stub_row_group" not in child.classes
    ]


def _is_merged(tr: _Element) -> bool:
    for cell in tr.children:
        if isinstance(cell, _Element) and "gt_stub_row_group" not in cell.classes:
            try:
                if float(cell.attrs.get("rowspan") or 1) > 1:
                    return True
            except ValueError:
                pass
    return False


def cell_text(cell: _Element) -> str:
    """A cell's text, folded, as the runtime matches it (`CellText.folded`).

    The text it shows, then (after a newline) what isn't shown: an image's `alt` text, and an
    SVG's `<title>`.
    """
    return fold(_text_of(cell)[0])


def _text_of(element: _Element) -> tuple[str, str]:
    # (The text matched, as `cell_text()` has it, unfolded; and the text shown)
    shown: list[str] = []
    extra: list[str] = []
    _collect(element, shown, extra)
    text = "".join(shown)
    return (text + "\n" + "\n".join(extra) if extra else text), text


def _parsed(html: str) -> _Element:
    tree = _Tree()
    # (As an HTML parser does, line breaks are `\n`)
    tree.feed(html.replace("\r\n", "\n").replace("\r", "\n"))
    tree.close()
    return tree.root


def match_text(html: str) -> str:
    """The text a cell's HTML would be matched by, as `cell_text()` has it, but not folded."""
    if not any(c in html for c in "<&\r"):
        return html
    return _text_of(_parsed(html))[0]


def label_text(html: str) -> str:
    """The text of a label's (or a cell's) HTML, as the runtime shows it (`labelText()`): without
    footnote marks, its whitespace collapsed."""
    text = html if not any(c in html for c in "<&") else _text_of(_parsed(html))[1]
    return " ".join(text.split())


def _collect(element: _Element, shown: list[str], extra: list[str]) -> None:
    for child in element.children:
        if isinstance(child, str):
            shown.append(child)
        elif child.tag == "svg":
            title = next(
                (c for c in child.children if isinstance(c, _Element) and c.tag == "title"), None
            )
            text = js_trim(title.text()) if title is not None else ""
            if text:
                extra.append(text)
        elif child.tag == "img":
            alt = js_trim(child.attrs.get("alt") or "")
            if alt:
                extra.append(alt)
        elif child.tag not in ("script", "style", "template") and (
            "gt_footnote_marks" not in child.classes
        ):
            _collect(child, shown, extra)


# Compiling ----


@dataclass(frozen=True)
class _In:
    col: str
    values: tuple[Any, ...]  # (as the column holds them; without a missing value)
    missing: bool
    as_text: bool  # (a categorical column, matched as its text)
    signed_zero: bool = False  # (a zero, in a column of floats, which has both zeros)

    def keys(self) -> list[Any]:
        """The values, as Narwhals matches them (with PyArrow, -0.0 isn't 0.0)."""
        zeros = [-0.0, 0.0] if self.signed_zero else []
        return [*(value for value in self.values if value != 0 or not zeros), *zeros]


@dataclass(frozen=True)
class _Compare:
    col: str
    op: Literal["gte", "lte", "gt", "lt"]
    value: int | float | dt.date  # (a date filter's as a date, or a datetime for one with times)
    finite: bool  # (a column of floats, whose NaN and infinities aren't kept)


_COMPARE_EXPRS = {"gte": operator.ge, "lte": operator.le, "gt": operator.gt, "lt": operator.lt}


@dataclass(frozen=True)
class _Extreme:
    col: str
    op: Literal["top_n", "bottom_n"]
    n: int
    finite: bool  # (a column of floats, whose NaN and infinities aren't ranked)


@dataclass(frozen=True)
class _Contains:
    col: str
    needle: str  # (trimmed and folded)


@dataclass(frozen=True)
class _Matches:
    col: str
    pattern: str  # (checked, as the query has it)


@dataclass(frozen=True)
class _IsNull:
    col: str
    nan: bool  # (a column of floats, whose NaN is missing too)


_Clause = _In | _Compare | _Extreme | _Contains | _Matches | _IsNull


@dataclass(frozen=True)
class _Group:
    kind: Literal["or", "and"]
    parts: tuple[_Predicate, ...]


@dataclass(frozen=True)
class _Not:
    part: _Predicate


_Predicate = _In | _Compare | _Extreme | _Contains | _Matches | _IsNull | _Group | _Not


def _plan(query: Query | None, spec: Spec, schema: Mapping[str, Any]) -> list[_Predicate]:
    """A query's parts as predicates on a frame with the table's data (of `schema`)."""
    import narwhals as nw

    kinds = {c["id"]: c["kind"] for c in [*spec["columns"], *spec.get("query_columns", [])]}

    def clause_predicate(clause: Mapping[str, Any]) -> _Clause:
        col, op, value = clause["col"], clause["op"], clause.get("value")
        dtype = schema[col]
        if op == "is_null":
            return _IsNull(col, dtype.is_float())
        if op == "contains":
            return _Contains(col, fold(js_trim(value)))
        if op == "matches":
            return _Matches(col, value)
        if op == "in":
            present = [item for item in value if item is not None]
            categorical = isinstance(dtype, (nw.Categorical, nw.Enum))
            as_text = categorical and all(isinstance(item, str) for item in present)
            values = tuple(_from_json(item, kinds.get(col), dtype, col) for item in present)
            # (The runtime has -0 as 0, as JavaScript's `Map` does)
            signed_zero = dtype.is_float() and 0 in values
            return _In(col, values, None in value, as_text, signed_zero)
        finite = isinstance(dtype, (nw.Float32, nw.Float64))
        if op in _EXTREMES:
            return _Extreme(col, op, value, finite)
        if isinstance(value, str):
            return _Compare(col, op, _date_bound(value, kinds.get(col)), False)
        return _Compare(col, op, value, finite)

    def predicate(item: Mapping[str, Any]) -> _Predicate:
        if _is_clause(item):
            return clause_predicate(item)
        if "not" in item:
            return _Not(predicate(item["not"]))
        kind = "or" if "or" in item else "and"
        return _Group(kind, tuple(predicate(part) for part in item[kind]))

    predicates = [predicate(item) for item in (query["and"] if query is not None else [])]
    # (Blank text, not in a group, keeps every row)
    return [p for p in predicates if not (isinstance(p, _Contains) and p.needle == "")]


def _clauses(predicates: Sequence[_Predicate]) -> Iterator[_Clause]:
    """The clauses of predicates, those in groups too."""
    for p in predicates:
        if isinstance(p, _Not):
            yield from _clauses([p.part])
        elif isinstance(p, _Group):
            yield from _clauses(p.parts)
        else:
            yield p


def _date_bound(text: str, kind: str | None) -> dt.date:
    """A date filter's bound as the column compares to it: a date, or for a column of dates and
    times, a datetime (a date as its midnight)."""
    value = parse_date(text)
    if value is None:
        raise ValueError(f"{text!r} isn't a date.")
    if kind == "datetime" and not isinstance(value, dt.datetime):
        return dt.datetime(value.year, value.month, value.day)
    return value


def _from_json(value: Any, kind: str | None, dtype: Any, col: str) -> Any:
    """A value of a facet, as JSON holds it, as the column holds it."""
    import narwhals as nw

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if dtype.is_integer() and float(value).is_integer():
            return int(value)
        if dtype.is_float():
            return float(value)
        return value
    if isinstance(value, str):
        if kind == "date" or isinstance(dtype, nw.Date):
            return dt.date.fromisoformat(value)
        if kind == "datetime" or isinstance(dtype, nw.Datetime):
            return dt.datetime.fromisoformat(value)
        if kind == "time" or isinstance(dtype, nw.Time):
            return dt.time.fromisoformat(value)
        if kind == "duration" or isinstance(dtype, nw.Duration):
            raise ValueError(
                f"A filter on column {col!r}, of durations, can't be compiled to a query yet."
            )
    return value


def _expr(
    predicate: _Predicate, texts: Mapping[str, str], matched: Mapping[tuple[str, str], str]
) -> nw.Expr:
    import narwhals as nw

    if isinstance(predicate, _Not):
        # (A clause leaves out a row with a missing value, which its expression is missing for)
        return ~_expr(predicate.part, texts, matched).fill_null(False)
    if isinstance(predicate, _Group):
        exprs = [_expr(part, texts, matched) for part in predicate.parts]
        joined = exprs[0]
        for expr in exprs[1:]:
            joined = joined | expr if predicate.kind == "or" else joined & expr
        return joined
    if isinstance(predicate, _Contains):
        return nw.col(texts[predicate.col]).str.contains(predicate.needle, literal=True)
    if isinstance(predicate, _Matches):
        return nw.col(matched[predicate.col, predicate.pattern])
    col = nw.col(predicate.col)
    if isinstance(predicate, _IsNull):
        return col.is_null() | col.is_nan() if predicate.nan else col.is_null()
    if isinstance(predicate, _Compare):
        expr = _COMPARE_EXPRS[predicate.op](col, predicate.value)
        return expr & col.is_finite() if predicate.finite else expr
    if isinstance(predicate, _Extreme):
        # (Ranked among all the frame's rows, as `filter()` has them: ties with the n-th have its
        # rank, so are kept)
        ranked = nw.when(col.is_finite()).then(col) if predicate.finite else col
        return ranked.rank("min", descending=predicate.op == "top_n") <= predicate.n
    keys = col.cast(nw.String) if predicate.as_text else col
    if not predicate.values:
        return col.is_null()
    expr = keys.is_in(predicate.keys())
    return expr | col.is_null() if predicate.missing else expr


def filter_exprs(
    query: Query | None,
    spec: Spec,
    schema: Mapping[str, Any],
    texts: Mapping[str, str] | None = None,
    matched: Mapping[tuple[str, str], str] | None = None,
) -> list[nw.Expr]:
    """A query as Narwhals expressions, on a frame with the table's data (of `schema`).

    A "contains" clause matches the folded text of a column's cells, which the frame needs as a
    column of its own: `texts` names them (by the data column). Blank text keeps every row, so has
    no expression. A "matches" clause's matches are a column of bools: `matched` names them (by
    the data column and the pattern, as the query has it).
    """
    predicates = _plan(query, spec, schema)
    clauses = list(_clauses(predicates))
    needed = {p.col for p in clauses if isinstance(p, _Contains)} - set(texts or {})
    if needed:
        raise ValueError(f'A "contains" clause needs a column of cell text, for {sorted(needed)}.')
    unmatched = {(p.col, p.pattern) for p in clauses if isinstance(p, _Matches)} - set(
        matched or {}
    )
    if unmatched:
        raise ValueError(
            f'A "matches" clause needs a column of its matches, for {sorted(unmatched)}.'
        )
    return [_expr(predicate, texts or {}, matched or {}) for predicate in predicates]


def _free_name(base: str, taken: Any) -> str:
    name = base
    while name in taken:
        name = f"_{name}"
    return name


def view_rows(gt: GT) -> list[int]:
    """The data rows a table's view shows (on every page), in order, as `<gt-table>` shows them.

    The view's filter and sort, compiled to Narwhals and applied to the table's data: rows are
    kept within their blocks (the runs of rows between group headings and summary rows), and
    sorted within them, ties keeping their order. A table whose stub has cells merged across
    rows keeps its rows as they are, as the runtime does. (A PyArrow dictionary column is sorted
    as its text; an ordered one, by its levels.)
    """
    import narwhals as nw

    from .._tbl_data import _get_column_levels
    from ._render import render_parts

    table_html, spec = render_parts(gt)
    trs = _body_trs(table_html)
    body = spec["body"]
    shown = [entry for entry in body if isinstance(entry, int)]
    if len(trs) != len(body):
        raise ValueError(f"The table body has {len(trs)} rows but the spec has {len(body)}.")
    data_trs = {entry: tr for entry, tr in zip(body, trs) if isinstance(entry, int)}
    if any(_is_merged(tr) for tr in data_trs.values()):
        return shown

    view = spec["view"]
    query = view["filter"]
    native = gt._tbl_data
    frame = nw.maybe_reset_index(nw.from_native(native, eager_only=True))
    namespace = nw.get_native_namespace(frame)
    taken = set(frame.columns)

    def add(base: str, values: list[Any], dtype: Any) -> str:
        name = _free_name(base, taken)
        taken.add(name)
        nonlocal frame
        frame = frame.with_columns(nw.new_series(name, values, dtype, backend=namespace))
        return name

    # Each data row's block and place in the body
    blocks = [0] * spec["nrows"]
    places = [0] * spec["nrows"]
    group_of = {row: group["id"] for group in spec["groups"] for row in group["rows"]}
    block, previous = -1, None
    for place, entry in enumerate(body):
        if not isinstance(entry, int):
            previous = None
            continue
        group = group_of.get(entry)
        if previous is None or previous[0] != group:
            block += 1
        previous = (group,)
        blocks[entry], places[entry] = block, place
    row_col = add("__gti_row", list(range(spec["nrows"])), nw.Int64)
    block_col = add("__gti_block", blocks, nw.Int64)
    place_col = add("__gti_place", places, nw.Int64)

    # The text of the cells of each column a "contains" or "matches" clause is on (unfolded)
    indices = {column["id"]: i for i, column in enumerate(spec["columns"])}
    # (A column only for querying has its texts in the spec)
    query_texts = {c["id"]: c["texts"] for c in spec["query_columns"]}
    unfolded: dict[str, list[str | None]] = {}

    def text_of(col: str) -> list[str | None]:
        if col not in unfolded:
            values: list[str | None] = []
            if col in query_texts:
                values = list(query_texts[col] or [])
            else:
                index = indices[col]
                for row in range(spec["nrows"]):
                    cells = _data_cells(data_trs[row]) if row in data_trs else []
                    values.append(_text_of(cells[index])[0] if index < len(cells) else None)
            unfolded[col] = values
        return unfolded[col]

    # The folded text of a "contains" clause's column, and a "matches" clause's matches (with
    # Python's `re`, as the runtime matches them, rather than the data's library)
    texts: dict[str, str] = {}
    matched: dict[tuple[str, str], str] = {}
    for clause in _leaves(query["and"] if query is not None else []):
        col, op = clause["col"], clause["op"]
        if op == "contains" and col not in texts:
            folded = [None if text is None else fold(text) for text in text_of(col)]
            texts[col] = add(f"__gti_text_{col}", folded, nw.String)
        elif op == "matches" and (col, clause["value"]) not in matched:
            search = pattern_search(clause["value"])
            found = [text is not None and search(text) for text in text_of(col)]
            matched[col, clause["value"]] = add(f"__gti_matches_{col}", found, nw.Boolean)

    predicates = filter_exprs(query, spec, frame.schema, texts, matched)
    if len(shown) < spec["nrows"]:
        # (Only the rows in the table's body are shown)
        predicates.append(nw.col(row_col).is_in(shown))
    if predicates:
        frame = frame.filter(*predicates)

    by, descending = [block_col], [False]
    schema = frame.schema
    for key in view["sort"]:
        column, desc = key["column"], key["descending"]
        dtype = schema[column]
        sort_col = column
        if desc and dtype.is_float():
            # (NaN is first in descending order, as it's after every number in ascending order,
            # as Polars has it: but not with pandas, whose NaN is missing)
            nan_col = _free_name(f"__gti_nan_{column}", taken)
            taken.add(nan_col)
            frame = frame.with_columns(
                (nw.col(column).is_nan() & ~nw.col(column).is_null())
                .fill_null(False)
                .alias(nan_col)
            )
            by.append(nan_col)
            descending.append(True)
        if isinstance(dtype, (nw.Categorical, nw.Enum)) and namespace.__name__ == "pyarrow":
            # (PyArrow can't sort dictionaries: as `_get_column_ranks()` ranks them)
            sort_col = _free_name(f"__gti_sort_{column}", taken)
            taken.add(sort_col)
            levels = _get_column_levels(native, column)
            text = nw.col(column).cast(nw.String)
            key_expr = (
                text
                if levels is None
                else text.replace_strict(levels, list(range(len(levels))), return_dtype=nw.Int64)
            )
            frame = frame.with_columns(key_expr.alias(sort_col))
        by.append(sort_col)
        descending.append(desc)
    by.append(place_col)
    descending.append(False)
    frame = frame.sort(by, descending=descending, nulls_last=True)
    return [int(row) for row in frame[row_col].to_list()]


# Code ----


def query_code(gt: GT, backend: Backend = "polars") -> str:
    """Code that filters and sorts a table's data (`df`) as its view does, with its imports.

    The code keeps and orders the data's rows, not the table's, so doesn't keep rows within their
    row groups; and drops the columns the view hides. A "contains" clause is a match, ignoring
    case, of the column's values as text (not of the text the table shows, nor ignoring accents);
    and a "matches" clause, a search of them with its pattern, translated for the library's
    regexes. (With pandas, a column that isn't of PyArrow's strings is searched with Python's
    `re`, whose `$` also matches before a line break at the end of the text.)
    """
    from ._render import render_parts

    if backend not in ("polars", "pandas", "narwhals"):
        raise ValueError(f'`backend=` must be "polars", "pandas", or "narwhals", not {backend!r}.')
    import narwhals as nw

    _, spec = render_parts(gt)
    frame = nw.from_native(gt._tbl_data, eager_only=True)
    schema = frame.schema
    # (As the runtime has the query, so that its code is the runtime's, character for character)
    predicates = _plan(_canonical(spec["view"]["filter"], spec["filters"]), spec, schema)
    sort = [(key["column"], key["descending"]) for key in spec["view"]["sort"]]
    hidden = spec["view"]["hidden"]
    imports: set[str] = set()
    if backend == "polars":
        code = _polars_code(predicates, sort, hidden, schema, imports)
    elif backend == "pandas":
        code = _pandas_code(predicates, sort, hidden, schema, gt._tbl_data, imports)
    else:
        code = _narwhals_code(predicates, sort, hidden, schema, imports)
    for predicate in _clauses(predicates):
        values = predicate.values if isinstance(predicate, _In) else ()
        if isinstance(predicate, _Compare):
            values = (predicate.value,)
        if any(isinstance(value, (dt.date, dt.time)) for value in values):
            imports.add("import datetime")
    header = "\n".join(sorted(imports))
    return f"{header}\n\n{code}\n" if header else f"{code}\n"


def _canonical(query: Query | None, filters: list[FilterSpec]) -> Query | None:
    """A (checked) query as the runtime has it (`filterQuery()` in packages/gti/src/filter.ts).

    Its clauses are in the order of the filters, a range's lower bound first, then its groups and
    its "is_null", "matches", "gt", "lt", "top_n" and "bottom_n" clauses (which no filter has), in
    their order. An "in" clause's values are the facet's, in their order (a missing value last),
    and a bound that's a number is as JavaScript holds it.
    """
    if query is None:
        return None
    order = {f["column"]: i for i, f in enumerate(filters)}

    def clause_of(clause: Mapping[str, Any]) -> dict[str, Any]:
        if clause["op"] in ("is_null", "matches"):
            return dict(clause)
        value = clause["value"]
        if clause["op"] == "in":
            values = filters[order[clause["col"]]]["values"] or []
            ranks: dict[tuple[str, Any], int] = {}
            for rank, item in enumerate(values):
                if item is not None:
                    ranks.setdefault(_value_key(item), rank)
            chosen = sorted({ranks[_value_key(item)] for item in value if item is not None})
            value = [values[rank] for rank in chosen] + ([None] if None in value else [])
        elif clause["op"] != "contains" and not isinstance(value, str):
            value = _whole(value)
        return {**clause, "value": value}

    def item_of(item: Mapping[str, Any]) -> dict[str, Any]:
        if _is_clause(item):
            return clause_of(item)
        if "not" in item:
            return {"not": item_of(item["not"])}
        kind = "or" if "or" in item else "and"
        return {kind: [item_of(part) for part in item[kind]]}

    def kept(item: Mapping[str, Any]) -> bool:
        # (As a filter keeps it)
        return _is_clause(item) and item["op"] not in _GROUPED

    clauses = sorted(
        (item for item in query["and"] if kept(item)),
        key=lambda c: (order[c["col"]], c["op"] == "lte"),
    )
    groups = [item for item in query["and"] if not kept(item)]
    return {"and": [*map(clause_of, clauses), *map(item_of, groups)]}


def _whole(value: float) -> int | float:
    # (A bound as JavaScript holds it, a double: an integer if it's whole)
    number = float(value)
    return int(number) if number.is_integer() else number


def _nullable(data: Any, name: str) -> bool:
    """Whether a column of pandas data has a nullable dtype (which compares to `pd.NA`)."""
    try:
        dtype = data.dtypes[name]
    except (AttributeError, KeyError, TypeError):
        return False
    return type(dtype).__module__.startswith("pandas") and not hasattr(dtype, "categories")


def code_spec(
    data: Any,
    kinds: Mapping[str | None, ColumnKind],
    filters: list[FilterSpec],
    ranks: Mapping[str, Any],
) -> CodeSpec:
    """What the runtime needs to write a view's code as `query_code()` does.

    That's the library of the data, and for each column the view can filter or sort by, the
    type that the code goes by (a date filter's bounds are dates, or datetimes for a column of
    dates and times) and (for a facet or a bool filter) its values as Python, as the code writes
    them.
    """
    import narwhals as nw

    frame = nw.from_native(data, eager_only=True)
    schema = frame.schema
    facets = {f["column"]: f["values"] or [] for f in filters if f["type"] in ("facet", "bool")}
    spec: dict[str, CodeColumnSpec] = {}
    for name in [*(f["column"] for f in filters), *ranks]:
        if name in spec:
            continue
        dtype = schema[name]
        literals = None
        if name in facets:
            literals = []
            for value in facets[name]:
                try:
                    literal = _literal(_from_json(value, kinds.get(name), dtype, name))
                except ValueError:
                    literal = None
                literals.append(None if value is None else literal)
        kind = kinds.get(name)
        spec[name] = CodeColumnSpec(
            dtype=(
                "string"
                if dtype == nw.String
                else "float"
                if dtype.is_float()
                else "categorical"
                if isinstance(dtype, (nw.Categorical, nw.Enum))
                else "date"
                if kind == "date"
                else "datetime"
                if kind == "datetime"
                else "other"
            ),
            nullable=_nullable(data, name),
            literals=literals,
        )
    implementation = frame.implementation
    backend: Backend = (
        "polars"
        if implementation is nw.Implementation.POLARS
        else "pandas"
        if implementation is nw.Implementation.PANDAS
        else "narwhals"
    )
    return CodeSpec(backend=backend, columns=spec)


def _literal(value: Any) -> str:
    if isinstance(value, str):
        # (Python's and JSON's escapes, but for non-ASCII text, which is kept)
        return json.dumps(value, ensure_ascii=False)
    return repr(value)


def _list(values: tuple[Any, ...]) -> str:
    return "[" + ", ".join(_literal(value) for value in values) + "]"


def _col(name: str, prefix: str) -> str:
    return f"{prefix}({_literal(name)})"


def _rank_args(p: _Extreme, pandas: bool) -> str:
    # (Ranked among all the rows, ties with the n-th kept)
    if pandas:
        return 'method="min", ascending=False' if p.op == "top_n" else 'method="min"'
    return '"min", descending=True' if p.op == "top_n" else '"min"'


# A term of the code's filter, and how tightly it binds, as Python's operators do: a comparison, an
# `|`, an `&`, a `~`, or an atom (a call, or in parentheses), as `Term` in packages/gti/src/code.ts
_COMPARE, _OR, _AND, _NOT, _ATOM = range(5)
_Term = tuple[str, int]


def _terms(
    predicates: list[_Predicate], leaf: Callable[[_Clause], _Term], pandas: bool
) -> list[str]:
    """The terms of predicates' code, a group's parts joined by `|` or `&` (each in parentheses
    unless it's an atom, a `~`, or of the same kind); and a `not`'s part after `~`, a clause that
    leaves out a row with a missing value keeping it (as pandas' terms do already, filling them).
    """

    def term(p: _Predicate) -> _Term:
        if isinstance(p, _Not):
            code, rank = term(p.part)
            if pandas:
                return f"~{code if rank >= _NOT else f'({code})'}", _NOT
            return f"~{code if rank == _ATOM else f'({code})'}.fill_null(False)", _NOT
        if isinstance(p, _Group):
            rank, joint = (_OR, " | ") if p.kind == "or" else (_AND, " & ")
            codes = [
                code if r >= _NOT or r == rank else f"({code})" for code, r in map(term, p.parts)
            ]
            return joint.join(codes), rank
        return leaf(p)

    return [term(p)[0] for p in predicates]


def _polars_code(
    predicates: list[_Predicate],
    sort: list[tuple[str, bool]],
    hidden: list[str],
    schema: Any,
    imports: set[str],
) -> str:
    import narwhals as nw

    imports.add("import polars as pl")

    def leaf(p: _Clause) -> _Term:
        col = _col(p.col, "pl.col")
        if isinstance(p, _IsNull):
            return (
                (f"{col}.is_null() | {col}.is_nan()", _OR) if p.nan else (f"{col}.is_null()", _ATOM)
            )
        if isinstance(p, _Matches):
            text = col if schema[p.col] == nw.String else f"{col}.cast(pl.String)"
            return f"{text}.str.contains({_literal(pattern_code(p.pattern))})", _ATOM
        if isinstance(p, _Contains):
            text = col if schema[p.col] == nw.String else f"{col}.cast(pl.String)"
            return (
                f"{text}.str.to_lowercase().str.contains({_literal(p.needle)}, literal=True)",
                _ATOM,
            )
        if isinstance(p, _Compare):
            op = _SYMBOLS[p.op]
            term = f"{col} {op} {_literal(p.value)}"
            return (f"({term}) & {col}.is_finite()", _AND) if p.finite else (term, _COMPARE)
        if isinstance(p, _Extreme):
            ranked = f"pl.when({col}.is_finite()).then({col})" if p.finite else col
            return f"{ranked}.rank({_rank_args(p, pandas=False)}) <= {p.n}", _COMPARE
        keys = f"{col}.cast(pl.String)" if p.as_text else col
        if not p.values:
            return f"{col}.is_null()", _ATOM
        term = f"{keys}.is_in({_list(p.values)})"
        return (f"{term} | {col}.is_null()", _OR) if p.missing else (term, _ATOM)

    terms = _terms(predicates, leaf, pandas=False)
    code = "df"
    if terms:
        code += ".filter(\n" + "".join(f"    {term},\n" for term in terms) + ")"
    if sort:
        names = _list(tuple(column for column, _ in sort))
        flags = "[" + ", ".join(str(desc) for _, desc in sort) + "]"
        code += f".sort({names}, descending={flags}, nulls_last=True, maintain_order=True)"
    if hidden:
        code += f".drop({_list(tuple(hidden))})"
    return code


def _pandas_code(
    predicates: list[_Predicate],
    sort: list[tuple[str, bool]],
    hidden: list[str],
    schema: Any,
    data: Any,
    imports: set[str],
) -> str:
    import narwhals as nw

    def leaf(p: _Clause) -> _Term:
        col = f"df[{_literal(p.col)}]"
        if isinstance(p, _IsNull):
            # (A float's NaN is missing too, as pandas has it already)
            return f"{col}.isna()", _ATOM
        if isinstance(p, _Matches):
            text = col if schema[p.col] == nw.String else f"{col}.astype(str)"
            pattern = _literal(pattern_code(p.pattern))
            return f"{text}.str.contains({pattern}, regex=True, na=False)", _ATOM
        if isinstance(p, _Contains):
            text = col if schema[p.col] == nw.String else f"{col}.astype(str)"
            return (
                f"{text}.str.contains({_literal(p.needle)}, case=False, regex=False, na=False)",
                _ATOM,
            )
        if isinstance(p, _Compare):
            op = _SYMBOLS[p.op]
            term: _Term = (f"{col} {op} {_literal(p.value)}", _COMPARE)
            if p.finite:
                imports.add("import numpy as np")
                term = (f"({term[0]}) & np.isfinite({col})", _AND)
            # (pandas' nullable dtypes compare to `pd.NA`, which a mask can't have)
            return (f"({term[0]}).fillna(False)", _ATOM) if _nullable(data, p.col) else term
        if isinstance(p, _Extreme):
            ranked = col
            if p.finite:
                imports.add("import numpy as np")
                ranked = f"{col}.where(np.isfinite({col}))"
            return f"{ranked}.rank({_rank_args(p, pandas=True)}) <= {p.n}", _COMPARE
        if not p.values:
            return f"{col}.isna()", _ATOM
        term_ = f"{col}.isin({_list(p.values)})"
        return (f"{term_} | {col}.isna()", _OR) if p.missing else (term_, _ATOM)

    terms = _terms(predicates, leaf, pandas=True)
    code = "df"
    if terms:
        mask = "\n    & ".join(f"({term})" if len(terms) > 1 else term for term in terms)
        code = f"df[\n    {mask}\n]"
    if sort:
        names = _list(tuple(column for column, _ in sort))
        ascending = "[" + ", ".join(str(not desc) for _, desc in sort) + "]"
        code += f'.sort_values({names}, ascending={ascending}, na_position="last", kind="stable")'
    if hidden:
        code += f".drop(columns={_list(tuple(hidden))})"
    return code


def _narwhals_code(
    predicates: list[_Predicate],
    sort: list[tuple[str, bool]],
    hidden: list[str],
    schema: Any,
    imports: set[str],
) -> str:
    import narwhals as nw

    imports.add("import narwhals as nw")

    def leaf(p: _Clause) -> _Term:
        col = _col(p.col, "nw.col")
        if isinstance(p, _IsNull):
            return (
                (f"{col}.is_null() | {col}.is_nan()", _OR) if p.nan else (f"{col}.is_null()", _ATOM)
            )
        if isinstance(p, _Matches):
            text = col if schema[p.col] == nw.String else f"{col}.cast(nw.String)"
            return f"{text}.str.contains({_literal(pattern_code(p.pattern))})", _ATOM
        if isinstance(p, _Contains):
            text = col if schema[p.col] == nw.String else f"{col}.cast(nw.String)"
            return (
                f"{text}.str.to_lowercase().str.contains({_literal(p.needle)}, literal=True)",
                _ATOM,
            )
        if isinstance(p, _Compare):
            op = _SYMBOLS[p.op]
            term = f"{col} {op} {_literal(p.value)}"
            return (f"({term}) & {col}.is_finite()", _AND) if p.finite else (term, _COMPARE)
        if isinstance(p, _Extreme):
            ranked = f"nw.when({col}.is_finite()).then({col})" if p.finite else col
            return f"{ranked}.rank({_rank_args(p, pandas=False)}) <= {p.n}", _COMPARE
        keys = f"{col}.cast(nw.String)" if p.as_text else col
        if not p.values:
            return f"{col}.is_null()", _ATOM
        term = f"{keys}.is_in({_list(tuple(p.keys()))})"
        return (f"{term} | {col}.is_null()", _OR) if p.missing else (term, _ATOM)

    terms = _terms(predicates, leaf, pandas=False)

    lines = ["nw.from_native(df)"]
    if terms:
        lines.append(".filter(\n" + "".join(f"        {term},\n" for term in terms) + "    )")
    if sort:
        # (Narwhals' sort mightn't keep ties in order, so the rows' order is the last key; and
        # NaN is first in descending order, as with Polars)
        lines.append('.with_row_index("_row")')
        by: list[str] = []
        flags: list[bool] = []
        extra: list[str] = ["_row"]
        for column, desc in sort:
            if desc and schema[column].is_float():
                name = f"_nan_{column}"
                col = _col(column, "nw.col")
                lines.append(
                    f".with_columns(({col}.is_nan() & ~{col}.is_null()).fill_null(False)"
                    f".alias({_literal(name)}))"
                )
                by.append(name)
                flags.append(True)
                extra.append(name)
            by.append(column)
            flags.append(desc)
        by.append("_row")
        flags.append(False)
        lines.append(
            f".sort({_list(tuple(by))}, descending=[{', '.join(str(f) for f in flags)}], "
            "nulls_last=True)"
        )
        lines.append(f".drop({_list(tuple(extra))})")
    if hidden:
        lines.append(f".drop({_list(tuple(hidden))})")
    lines.append(".to_native()")
    return "(\n    " + "\n    ".join(lines) + "\n)"
