"""Queries: the filters of an interactive table's view, in the data's terms.

A query is what `<gt-table>`'s `filter` property takes and gives, as JSON:

    {"and": [{"col": "status", "op": "in", "value": ["single-tier", None]},
             {"col": "population_2021", "op": "gte", "value": 10000}]}

Rows are kept when every clause keeps them. A clause's `op` is one of:

- `"contains"`, for a column with a text filter: keeps the rows whose cell shows `value` (a string,
  trimmed), ignoring case and accents, as the search does. Blank text keeps every row.
- `"in"`, for a facet: keeps the rows with one of `value`'s values (a non-empty list of them, as
  JSON holds them, like the spec's `values`; `None` is a missing value).
- `"gte"` and `"lte"`, for a range: keep the rows with a number that's at least (or at most)
  `value`, a finite number. Missing values, NaN and infinities are never kept.

A column has at most one clause with each `op`. Queries are checked as the runtime checks them
(`setFilterQuery()` in packages/gti/src/filter.ts), so that a view Python accepts is one
`<gt-table>` shows; and they're compiled, with a sort, to Narwhals expressions (`view_rows()`, the
rows a table's view shows) and to code for Polars, pandas, or Narwhals (`query_code()`).

Narwhals is needed only for compiling, and is imported by the functions that do it.
"""

from __future__ import annotations

import datetime as dt
import json
import math
import re
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from decimal import Decimal
from html.parser import HTMLParser
from typing import TYPE_CHECKING, Any, Literal, Union

from ._spec import (
    CodeBackend,
    CodeColumnSpec,
    CodeSpec,
    ColumnSpec,
    FilterSpec,
    Spec,
    ViewSpec,
    _json_value,
)

if TYPE_CHECKING:
    import narwhals as nw

    from ..gt import GT

Query = dict[str, list[dict[str, Any]]]

# A sort: column names, each with whether it's descending
SortKeys = tuple[tuple[str, bool], ...]

Backend = CodeBackend

# The filter type each op is for
OP_TYPES = {"contains": "text", "in": "facet", "gte": "range", "lte": "range"}

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
    """
    if isinstance(query, str):
        try:
            query = parse_query(query)
        except ValueError as err:
            raise ValueError(f"`filter=` can't be read as a query: {err}.") from None
    if query is None:
        return None
    clauses = query.get("and") if isinstance(query, Mapping) else None
    if (
        not isinstance(query, Mapping)
        or set(query) != {"and"}
        or not isinstance(clauses, (list, tuple))
    ):
        raise ValueError(
            '`filter=` must be a query, `{"and": [clauses]}`, or `None` (no filter), not '
            f"{query!r}."
        )

    checked: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for i, clause in enumerate(clauses):
        if (
            not isinstance(clause, Mapping)
            or set(clause) != {"col", "op", "value"}
            or not isinstance(clause["col"], str)
            or clause["op"] not in OP_TYPES
        ):
            raise ValueError(
                f'The filter\'s clause {i} must be `{{"col": ..., "op": ..., "value": ...}}`, with a '
                'column name and an op of "contains", "in", "gte", or "lte", not '
                f"{clause!r}."
            )
        col, op, value = clause["col"], clause["op"], clause["value"]
        if (col, op) in seen:
            raise ValueError(f"The filter has more than one {op!r} clause on column {col!r}.")
        seen.add((col, op))

        if op == "contains":
            if not isinstance(value, str):
                raise ValueError(
                    f'The filter\'s "contains" clause on column {col!r} needs a string, not '
                    f"{value!r}."
                )
        elif op == "in":
            if not isinstance(value, (list, tuple)) or len(value) == 0:
                raise ValueError(
                    f'The filter\'s "in" clause on column {col!r} needs a list of at least one '
                    f"value, not {value!r}."
                )
            value = [_facet_value(item, col) for item in value]
        else:
            value = _bound(value, col, op)
        checked.append({"col": col, "op": op, "value": value})
    return {"and": checked}


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


def _bound(value: Any, col: str, op: str) -> int | float:
    numpy_number = getattr(getattr(value, "dtype", None), "kind", None) in ("i", "u", "f")
    if isinstance(value, (int, float, Decimal)) and not isinstance(value, bool) or numpy_number:
        bound = _json_value(value)
        if bound is not None:
            return bound
    raise ValueError(
        f"The filter's {op!r} clause on column {col!r} needs a finite number, not {value!r}."
    )


# Queries as text, as the runtime reads and writes them (packages/gti/src/query.ts) ----
#
#     status in ("single-tier", null) and population >= 10000 and `Name of town` contains "ville"
#
# Clauses joined by `and`; a clause is a column, then `contains` and a string, `in` and values in
# parentheses, or `>=` or `<=` and a number. A column is a name of letters, digits and underscores
# (not starting with a digit), or any name in backticks (a backtick in it doubled). Strings and
# numbers are as in JSON; the other values are `true`, `false` and `null`. Keywords can be in any
# case. Empty text is no query. Errors are the runtime's, word for word.

_NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
_STRING = re.compile(r'"(?:[^"\\\x00-\x1f]|\\["\\/bfnrt]|\\u[0-9a-fA-F]{4})*"')
_NUMBER = re.compile(r"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?")
_SPACE = re.compile(r"[ \t\n\r]*")
_WORDS = {"true": True, "false": False, "null": None}
_VALUE_EXPECTED = "expected a value: a string in double quotes, a number, true, false or null"


@dataclass
class _Token:
    kind: Literal["name", "quoted", "string", "number", "symbol", "end"]
    # The text of a name or symbol, or a string's or number's value
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
        if self.is_word("contains"):
            self.advance()
            if self.token.kind != "string":
                self.fail("expected a string in double quotes")
            return {"col": col, "op": "contains", "value": self.advance().value}
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
        if self.is_symbol(">=") or self.is_symbol("<="):
            op = "gte" if self.advance().value == ">=" else "lte"
            if self.token.kind != "number":
                self.fail("expected a number")
            return {"col": col, "op": op, "value": self.advance().value}
        return self.fail('expected "contains", "in", ">=" or "<="')

    def query(self) -> Query | None:
        if self.token.kind == "end":
            return None
        clauses = [self.clause()]
        while self.token.kind != "end":
            if not self.is_word("and"):
                self.fail('expected "and" or the end of the query')
            self.advance()
            clauses.append(self.clause())
        return {"and": clauses}


def parse_query(text: str) -> Query | None:
    """Read a query's text into a query (`None` for empty text), without checking its clauses.

    Raises `ValueError`, with the runtime's message, if the text isn't a query.
    """
    return _QueryParser(text).query()


def format_query(query: Query | None) -> str:
    """Write a (checked) query as text, as the runtime's `formatQuery()` does.

    `parse_query()` reads the text back as the same query.
    """
    return " and ".join(_format_clause(clause) for clause in (query or {"and": []})["and"])


def _format_clause(clause: Mapping[str, Any]) -> str:
    col, op, value = clause["col"], clause["op"], clause["value"]
    name = col if _NAME.fullmatch(col) else "`" + col.replace("`", "``") + "`"
    if op == "contains":
        return f"{name} contains {_format_value(value)}"
    if op == "in":
        return f"{name} in ({', '.join(_format_value(item) for item in value)})"
    return f"{name} {'>=' if op == 'gte' else '<='} {_format_value(value)}"


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
) -> ViewSpec:
    """
    Check a view against a table's filters, sortable columns, and the columns readers can hide
    (in column order), as the runtime does.
    """
    by_column = {f["column"]: f for f in filters}
    for clause in query["and"] if query is not None else []:
        col, op, value = clause["col"], clause["op"], clause["value"]
        found = by_column.get(col)
        if found is None:
            raise ValueError(
                f"The view's filter has a clause on column {col!r}, which has no filter. Give it "
                "one with `i_cols_filter()`."
            )
        if OP_TYPES[op] != found["type"]:
            ops = " or ".join(
                repr(name) for name, type in OP_TYPES.items() if type == found["type"]
            )
            raise ValueError(
                f"The view's filter has a {op!r} clause on column {col!r}, which has a "
                f"{found['type']} filter (for {ops} clauses)."
            )
        if op == "in":
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
    return ViewSpec(
        filter=query,
        sort=[{"column": column, "descending": desc} for column, desc in sort],
        hidden=[column for column in hideable if column in hidden],
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
    tree = _Tree()
    # (As an HTML parser does, line breaks are `\n`)
    tree.feed(table_html.replace("\r\n", "\n").replace("\r", "\n"))
    tree.close()
    table = _find(tree.root, "table")
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
    shown: list[str] = []
    extra: list[str] = []
    _collect(cell, shown, extra)
    folded = fold("".join(shown))
    if extra:
        folded += "\n" + fold("\n".join(extra))
    return folded


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
    op: Literal["gte", "lte"]
    value: int | float
    finite: bool  # (a column of floats, whose NaN and infinities aren't kept)


@dataclass(frozen=True)
class _Contains:
    col: str
    needle: str  # (trimmed and folded)


_Predicate = Union[_In, _Compare, _Contains]


def _plan(query: Query | None, spec: Spec, schema: Mapping[str, Any]) -> list[_Predicate]:
    """A query's clauses as predicates on a frame with the table's data (of `schema`)."""
    import narwhals as nw

    kinds = {column["id"]: column["kind"] for column in spec["columns"]}
    predicates: list[_Predicate] = []
    for clause in query["and"] if query is not None else []:
        col, op, value = clause["col"], clause["op"], clause["value"]
        dtype = schema[col]
        if op == "contains":
            needle = fold(js_trim(value))
            if needle != "":
                predicates.append(_Contains(col, needle))
        elif op == "in":
            present = [item for item in value if item is not None]
            categorical = isinstance(dtype, (nw.Categorical, nw.Enum))
            as_text = categorical and all(isinstance(item, str) for item in present)
            values = tuple(_from_json(item, kinds.get(col), dtype, col) for item in present)
            # (The runtime has -0 as 0, as JavaScript's `Map` does)
            signed_zero = dtype.is_float() and 0 in values
            predicates.append(_In(col, values, None in value, as_text, signed_zero))
        else:
            finite = isinstance(dtype, (nw.Float32, nw.Float64))
            predicates.append(_Compare(col, op, value, finite))
    return predicates


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


def _expr(predicate: _Predicate, texts: Mapping[str, str]) -> nw.Expr:
    import narwhals as nw

    if isinstance(predicate, _Contains):
        return nw.col(texts[predicate.col]).str.contains(predicate.needle, literal=True)
    col = nw.col(predicate.col)
    if isinstance(predicate, _Compare):
        expr = col >= predicate.value if predicate.op == "gte" else col <= predicate.value
        return expr & col.is_finite() if predicate.finite else expr
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
) -> list[nw.Expr]:
    """A query as Narwhals expressions, on a frame with the table's data (of `schema`).

    A "contains" clause matches the folded text of a column's cells, which the frame needs as a
    column of its own: `texts` names them (by the data column). Blank text keeps every row, so has
    no expression.
    """
    predicates = _plan(query, spec, schema)
    needed = {p.col for p in predicates if isinstance(p, _Contains)} - set(texts or {})
    if needed:
        raise ValueError(f'A "contains" clause needs a column of cell text, for {sorted(needed)}.')
    return [_expr(predicate, texts or {}) for predicate in predicates]


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

    # The folded text of the cells of each column a "contains" clause is on
    texts: dict[str, str] = {}
    indices = {column["id"]: i for i, column in enumerate(spec["columns"])}
    for clause in query["and"] if query is not None else []:
        col = clause["col"]
        if clause["op"] == "contains" and col not in texts:
            index = indices[col]
            values: list[str | None] = []
            for row in range(spec["nrows"]):
                cells = _data_cells(data_trs[row]) if row in data_trs else []
                values.append(cell_text(cells[index]) if index < len(cells) else None)
            texts[col] = add(f"__gti_text_{col}", values, nw.String)

    predicates = filter_exprs(query, spec, frame.schema, texts)
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
    case, of the column's values as text (not of the text the table shows, nor ignoring accents).
    """
    from ._render import render_parts

    if backend not in ("polars", "pandas", "narwhals"):
        raise ValueError(f'`backend=` must be "polars", "pandas", or "narwhals", not {backend!r}.')
    import narwhals as nw

    _, spec = render_parts(gt)
    frame = nw.from_native(gt._tbl_data, eager_only=True)
    schema = frame.schema
    # (As the runtime has the query, so that its code is the runtime's, character for character)
    predicates = [
        replace(p, value=_whole(p.value)) if isinstance(p, _Compare) else p
        for p in _plan(_canonical(spec["view"]["filter"], spec["filters"]), spec, schema)
    ]
    sort = [(key["column"], key["descending"]) for key in spec["view"]["sort"]]
    hidden = spec["view"]["hidden"]
    imports: set[str] = set()
    if backend == "polars":
        code = _polars_code(predicates, sort, hidden, schema, imports)
    elif backend == "pandas":
        code = _pandas_code(predicates, sort, hidden, schema, gt._tbl_data, imports)
    else:
        code = _narwhals_code(predicates, sort, hidden, schema, imports)
    for predicate in predicates:
        if isinstance(predicate, _In) and any(
            isinstance(value, (dt.date, dt.time)) for value in predicate.values
        ):
            imports.add("import datetime")
    header = "\n".join(sorted(imports))
    return f"{header}\n\n{code}\n" if header else f"{code}\n"


def _canonical(query: Query | None, filters: list[FilterSpec]) -> Query | None:
    """A query as the runtime has it (`filterQuery()` in packages/gti/src/filter.ts).

    Its clauses are in the order of the filters, a range's lower bound first, and an "in"
    clause's values are the facet's, in their order (a missing value last).
    """
    if query is None:
        return None
    order = {f["column"]: i for i, f in enumerate(filters)}
    clauses = sorted(query["and"], key=lambda c: (order[c["col"]], c["op"] == "lte"))
    canonical: list[dict[str, Any]] = []
    for clause in clauses:
        value = clause["value"]
        if clause["op"] == "in":
            values = filters[order[clause["col"]]]["values"] or []
            ranks: dict[tuple[str, Any], int] = {}
            for rank, item in enumerate(values):
                if item is not None:
                    ranks.setdefault(_value_key(item), rank)
            chosen = sorted({ranks[_value_key(item)] for item in value if item is not None})
            value = [values[rank] for rank in chosen] + ([None] if None in value else [])
        canonical.append({**clause, "value": value})
    return {"and": canonical}


def _whole(value: int | float) -> int | float:
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
    columns: list[ColumnSpec],
    filters: list[FilterSpec],
    ranks: Mapping[str, Any],
) -> CodeSpec:
    """What the runtime needs to write a view's code as `query_code()` does.

    That's the library of the data, and for each column the view can filter or sort by, the
    type that the code goes by and (for a facet) its values as Python, as the code writes them.
    """
    import narwhals as nw

    frame = nw.from_native(data, eager_only=True)
    schema = frame.schema
    kinds = {column["id"]: column["kind"] for column in columns}
    facets = {f["column"]: f["values"] or [] for f in filters if f["type"] == "facet"}
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
        spec[name] = CodeColumnSpec(
            dtype=(
                "string"
                if dtype == nw.String
                else "float"
                if dtype.is_float()
                else "categorical"
                if isinstance(dtype, (nw.Categorical, nw.Enum))
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


def _polars_code(
    predicates: list[_Predicate],
    sort: list[tuple[str, bool]],
    hidden: list[str],
    schema: Any,
    imports: set[str],
) -> str:
    import narwhals as nw

    imports.add("import polars as pl")
    terms = []
    for p in predicates:
        col = _col(p.col, "pl.col")
        if isinstance(p, _Contains):
            text = col if schema[p.col] == nw.String else f"{col}.cast(pl.String)"
            terms.append(
                f"{text}.str.to_lowercase().str.contains({_literal(p.needle)}, literal=True)"
            )
        elif isinstance(p, _Compare):
            op = ">=" if p.op == "gte" else "<="
            term = f"{col} {op} {_literal(p.value)}"
            terms.append(f"({term}) & {col}.is_finite()" if p.finite else term)
        else:
            keys = f"{col}.cast(pl.String)" if p.as_text else col
            term = f"{keys}.is_in({_list(p.values)})" if p.values else f"{col}.is_null()"
            terms.append(f"{term} | {col}.is_null()" if p.missing and p.values else term)
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

    terms = []
    for p in predicates:
        col = f"df[{_literal(p.col)}]"
        if isinstance(p, _Contains):
            text = col if schema[p.col] == nw.String else f"{col}.astype(str)"
            terms.append(
                f"{text}.str.contains({_literal(p.needle)}, case=False, regex=False, na=False)"
            )
        elif isinstance(p, _Compare):
            op = ">=" if p.op == "gte" else "<="
            term = f"{col} {op} {_literal(p.value)}"
            if p.finite:
                imports.add("import numpy as np")
                term = f"({term}) & np.isfinite({col})"
            # (pandas' nullable dtypes compare to `pd.NA`, which a mask can't have)
            terms.append(f"({term}).fillna(False)" if _nullable(data, p.col) else term)
        else:
            term = f"{col}.isin({_list(p.values)})" if p.values else f"{col}.isna()"
            terms.append(f"{term} | {col}.isna()" if p.missing and p.values else term)
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
    terms = []
    for p in predicates:
        col = _col(p.col, "nw.col")
        if isinstance(p, _Contains):
            text = col if schema[p.col] == nw.String else f"{col}.cast(nw.String)"
            terms.append(
                f"{text}.str.to_lowercase().str.contains({_literal(p.needle)}, literal=True)"
            )
        elif isinstance(p, _Compare):
            op = ">=" if p.op == "gte" else "<="
            term = f"{col} {op} {_literal(p.value)}"
            terms.append(f"({term}) & {col}.is_finite()" if p.finite else term)
        else:
            keys = f"{col}.cast(nw.String)" if p.as_text else col
            term = f"{keys}.is_in({_list(tuple(p.keys()))})" if p.values else f"{col}.is_null()"
            terms.append(f"{term} | {col}.is_null()" if p.missing and p.values else term)

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
