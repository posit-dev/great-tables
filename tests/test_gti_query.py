"""Queries: checking them, and compiling them, which must keep the rows `<gt-table>` shows.

The differential tests run tables through the built runtime, under Node (with happy-dom: see
packages/gti/scripts/engine.mjs), and check that the rows it shows for a view are the rows that
`view_rows()` gets with Narwhals, on pandas, Polars, and PyArrow data; and that Python reads and
writes queries as text as the runtime does, with the same errors. They're skipped without Node and
the package's dependencies (`npm ci` in packages/gti).
"""

from __future__ import annotations

import ast
import datetime as dt
import json
import math
import shutil
import subprocess
from collections.abc import Callable
from decimal import Decimal
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest

from great_tables import GT, GTI, loc, style
from great_tables._gti._pattern import PatternError, check_pattern
from great_tables._gti._query import (
    _Tree,
    cell_text,
    check_query,
    fold,
    format_query,
    js_trim,
    label_text,
    match_text,
    parse_query,
    parse_sort,
    query_code,
    view_rows,
)
from great_tables._gti._render import render_gti_html, render_parts
from great_tables._tbl_data import _get_column_kind

nw = pytest.importorskip("narwhals")
pl = pytest.importorskip("polars")
pa = pytest.importorskip("pyarrow")
hypothesis = pytest.importorskip("hypothesis")

PKG_DIR = Path(__file__).parent.parent / "packages" / "gti"

BACKENDS = ["pandas", "polars", "pyarrow"]


def query(*clauses: tuple[str, str, Any]) -> dict:
    return {"and": [{"col": col, "op": op, "value": value} for col, op, value in clauses]}


def clause(col: str, op: str, value: Any) -> dict:
    return {"col": col, "op": op, "value": value}


def or_(*parts: dict) -> dict:
    return {"or": list(parts)}


def and_(*parts: dict) -> dict:
    return {"and": list(parts)}


def is_null(col: str) -> dict:
    return {"col": col, "op": "is_null"}


def not_(part: dict) -> dict:
    return {"not": part}


A = clause("a", "gte", 1)
B = clause("b", "gte", 2)
C = clause("c", "contains", "x")


def view_of(gt: GT) -> dict:
    return render_parts(gt)[1]["view"]


# Frames of each backend, from columns of Python values: each is (kind, values), where the kind is
# "int", "float", "str", "bool", "cat" (a category, of the values' levels as given, or of the
# values in order of appearance), "date", or "datetime" (of dates and times, without a time zone)


def frame(backend: str, columns: dict[str, tuple[str, list[Any]]]) -> Any:
    if backend == "pandas":
        return pd.DataFrame({name: _pandas_column(*column) for name, column in columns.items()})
    if backend == "polars":
        return pl.DataFrame([_polars_column(name, *column) for name, column in columns.items()])
    return pa.table({name: _arrow_column(*column) for name, column in columns.items()})


def _levels(values: list[Any]) -> list[Any]:
    return list(dict.fromkeys(value for value in values if value is not None))


def _pandas_column(kind: str, values: list[Any]) -> Any:
    missing = None in values
    if kind == "int":
        return pd.array(values, dtype="Int64") if missing else np.array(values, dtype="int64")
    if kind == "float":
        return np.array([math.nan if v is None else v for v in values], dtype="float64")
    if kind == "bool":
        return pd.array(values, dtype="boolean") if missing else np.array(values, dtype=bool)
    if kind == "cat":
        return pd.Categorical(values, categories=_levels(values))
    if kind == "datetime":
        return pd.Series(pd.to_datetime(values))
    # (Dates as Python's: pandas has no dtype of its own for them)
    return pd.Series(values, dtype=object)


def _polars_column(name: str, kind: str, values: list[Any]) -> Any:
    dtypes = {
        "int": pl.Int64,
        "float": pl.Float64,
        "bool": pl.Boolean,
        "str": pl.String,
        "cat": pl.Categorical,
        "date": pl.Date,
        "datetime": pl.Datetime("us"),
    }
    return pl.Series(name, values, dtype=dtypes[kind])


def _arrow_column(kind: str, values: list[Any]) -> Any:
    types = {
        "int": pa.int64(),
        "float": pa.float64(),
        "bool": pa.bool_(),
        "str": pa.string(),
        "date": pa.date32(),
        "datetime": pa.timestamp("us"),
    }
    if kind == "cat":
        return pa.array(values, pa.string()).dictionary_encode()
    return pa.array(values, types[kind])


# checking queries ----


def test_check_query_normalizes_values():
    checked = check_query(
        {
            "and": (
                {"col": "x", "op": "in", "value": (np.int64(2), 1.5, Decimal("2.5"), None, True)},
                {"col": "y", "op": "gte", "value": np.float32(0.5)},
                {"col": "z", "op": "contains", "value": " ab "},
            )
        }
    )
    assert checked == query(
        ("x", "in", [2, 1.5, 2.5, None, True]), ("y", "gte", 0.5), ("z", "contains", " ab ")
    )
    assert type(checked["and"][0]["value"][0]) is int
    assert check_query(None) is None
    assert check_query({"and": []}) == {"and": []}


@pytest.mark.parametrize(
    "bad, message",
    [
        ([], "must be a query"),
        ({"or": []}, "must be a query"),
        ({"and": [], "or": []}, "must be a query"),
        ({"and": "x"}, "must be a query"),
        ({"and": [1]}, "clause 0 must be"),
        ({"and": [{"col": "x", "op": "ne", "value": 1}]}, "clause 0 must be"),
        ({"and": [{"col": 1, "op": "in", "value": [1]}]}, "clause 0 must be"),
        ({"and": [{"col": "x", "op": "in"}]}, "clause 0 must be"),
        ({"and": [{"col": "x", "op": "in", "value": [1], "not": True}]}, "clause 0 must be"),
        (query(("x", "contains", 1)), "needs a string"),
        (query(("x", "in", [])), "at least one value"),
        (query(("x", "in", "ab")), "at least one value"),
        (query(("x", "in", [[1]])), "isn't a value a column can have"),
        (query(("x", "in", [math.nan])), r"can't be chosen \(use `None`"),
        (query(("x", "in", [math.inf])), "can't be chosen"),
        (query(("x", "gte", "1")), "needs a finite number"),
        (query(("x", "gte", True)), "needs a finite number"),
        (query(("x", "lte", math.inf)), "needs a finite number"),
        (query(("x", "lte", None)), "needs a finite number"),
        (query(("x", "gt", math.nan)), "'gt' clause on column 'x' needs a finite number"),
        (query(("x", "lt", "2015-13-01")), "'lt' clause on column 'x' needs a finite number"),
        (query(("x", "gt", 1), ("x", "gt", 2)), "more than one 'gt' clause on column 'x'"),
        (query(("x", "gte", 1), ("x", "gte", 2)), "more than one 'gte' clause on column 'x'"),
        (query(("x", "in", [1]), ("x", "in", [2])), "more than one 'in' clause"),
    ],
)
def test_check_query_rejects(bad: Any, message: str):
    with pytest.raises(ValueError, match=message):
        check_query(bad)


def test_check_query_takes_top_and_bottom_clauses():
    checked = check_query(
        query(("x", "top_n", np.int64(3)), ("x", "bottom_n", 10.0), ("y", "top_n", Decimal(2)))
    )
    # (A whole number as an int, as JavaScript has it)
    assert checked == query(("x", "top_n", 3), ("x", "bottom_n", 10), ("y", "top_n", 2))
    assert [type(c["value"]) for c in checked["and"]] == [int, int, int]
    assert check_query("x top 1 and x bottom 1") == query(("x", "top_n", 1), ("x", "bottom_n", 1))


@pytest.mark.parametrize("value", [0, -1, 1.5, True, "3", 2**53, math.nan, math.inf, None, [1]])
def test_check_query_rejects_a_top_or_bottom_clause_without_a_whole_number(value: Any):
    with pytest.raises(ValueError, match="'top_n' clause on column 'x' needs a whole number"):
        check_query(query(("x", "top_n", value)))


def test_check_query_rejects_two_top_clauses_on_a_column():
    with pytest.raises(ValueError, match="more than one 'top_n' clause on column 'x'"):
        check_query("x top 1 and x top 2")
    with pytest.raises(ValueError, match="more than one 'bottom_n' clause on column 'x'"):
        check_query("(x bottom 1 and x bottom 2) or x top 1")


def test_check_query_takes_is_null_clauses():
    is_null = {"col": "x", "op": "is_null"}
    assert check_query({"and": [is_null, not_(is_null), or_(is_null, A)]}) == {
        "and": [is_null, not_(is_null), or_(is_null, A)]
    }
    assert check_query("x is null and y is not null") == {
        "and": [is_null, not_({"col": "y", "op": "is_null"})]
    }


@pytest.mark.parametrize(
    "bad, message",
    [
        ({"and": [{"col": "x", "op": "is_null", "value": None}]}, "clause 0 must be"),
        ({"and": [{"col": "x", "op": "is_null", "value": True}]}, "clause 0 must be"),
        ({"and": [not_({"op": "is_null"})]}, "part of a 'not' group must be"),
        (
            {"and": [{"col": "x", "op": "is_null"}, and_({"col": "x", "op": "is_null"})]},
            "more than one 'is_null' clause on column 'x'",
        ),
        (
            {"and": [or_(and_({"col": "x", "op": "is_null"}, {"col": "x", "op": "is_null"}), A)]},
            "more than one 'is_null' clause on column 'x', in an 'and' group",
        ),
    ],
)
def test_check_query_rejects_is_null_clauses(bad: Any, message: str):
    with pytest.raises(ValueError, match=message):
        check_query(bad)


def test_check_query_takes_matches_clauses_as_the_runtime_has_them():
    # (Without escapes before a slash)
    matches = clause("x", "matches", "(?i)^a\\/b[\\/]\\\\")
    checked = clause("x", "matches", "(?i)^a/b[/]\\\\")
    assert check_query({"and": [matches, not_(matches), or_(matches, A)]}) == {
        "and": [checked, not_(checked), or_(checked, A)]
    }
    assert check_query("x matches /^a\\/b[\\/]\\\\/i") == {"and": [checked]}


@pytest.mark.parametrize(
    "bad, message",
    [
        (query(("x", "matches", 1)), "\"matches\" clause on column 'x' needs a string"),
        (
            query(("x", "matches", "a(")),
            "The pattern of the filter's \"matches\" clause on column 'x' can't be read: "
            'expected "\\)", at the end',
        ),
        (query(("x", "matches", "")), "can't be read: expected a pattern, at the end"),
        (query(("x", "matches", "(?i)")), "expected a pattern, at the end"),
        (query(("x", "matches", "(?i)😀(?=a)")), 'must be "\\(\\?:".*, at character 6'),
        (query(("x", "matches", "[z-a]")), 'the range "z-a" is out of order, at character 2'),
        (
            query(("x", "matches", "a"), ("x", "matches", "b")),
            "more than one 'matches' clause on column 'x'",
        ),
        (
            {"and": [clause("x", "matches", "a"), or_(clause("x", "matches", "b"))]},
            "more than one 'matches' clause on column 'x'",
        ),
        (
            {"and": [or_(and_(clause("x", "matches", "a"), clause("x", "matches", "b")), A)]},
            "more than one 'matches' clause on column 'x', in an 'and' group",
        ),
    ],
)
def test_check_query_rejects_matches_clauses(bad: Any, message: str):
    with pytest.raises(ValueError, match=message):
        check_query(bad)


def test_check_query_takes_groups_as_the_runtime_has_them():
    # (Groups of one part as the part, and like groups spliced in; in the order given)
    checked = check_query(
        {
            "and": [
                and_(clause("x", "gte", 5)),
                or_(and_(clause("z", "contains", "fig"))),
                or_(clause("y", "in", ("a",)), or_(clause("x", "lte", 5), or_(B))),
                not_(and_(clause("x", "lte", 5), and_(clause("y", "in", ["a"])))),
            ]
        }
    )
    assert checked == {
        "and": [
            clause("x", "gte", 5),
            clause("z", "contains", "fig"),
            or_(clause("y", "in", ["a"]), clause("x", "lte", 5), B),
            not_(and_(clause("x", "lte", 5), clause("y", "in", ["a"]))),
        ]
    }
    # (Blank text keeps every row, but not in a group)
    assert check_query(query(("z", "contains", " "))) == query(("z", "contains", " "))
    # (The same clause in different parts)
    same = {
        "and": [clause("x", "gte", 5), or_(clause("x", "gte", 20), not_(clause("x", "gte", 5)))]
    }
    assert check_query(same) == same
    # (As text)
    assert check_query('x >= 5 and (y in ("a") or not z contains "q")') == {
        "and": [
            clause("x", "gte", 5),
            or_(clause("y", "in", ["a"]), not_(clause("z", "contains", "q"))),
        ]
    }


@pytest.mark.parametrize(
    "bad, message",
    [
        ({"and": [or_()]}, r"'or' group needs a list of at least one part, not \[\]"),
        ({"and": [{"and": {"col": "x"}}]}, "'and' group needs a list"),
        ({"and": [{"or": [], "and": []}]}, "clause 0 must be"),
        ({"and": [not_(1)]}, "part of a 'not' group must be"),
        ({"and": [and_(A, 1)]}, "part 1 of an 'and' group must be"),
        ({"and": [not_(clause("z", "contains", " "))]}, 'needs text, in an "or" or a "not"'),
        (
            {"and": [or_(and_(clause("x", "gte", 1), clause("x", "gte", 2)), A)]},
            "more than one 'gte' clause on column 'x', in an 'and' group",
        ),
        (
            {"and": [clause("x", "gte", 1), and_(clause("x", "gte", 2))]},
            "more than one 'gte' clause on column 'x'",
        ),
        ({"and": [not_(clause("x", "in", []))]}, "at least one value"),
    ],
)
def test_check_query_rejects_groups(bad: Any, message: str):
    with pytest.raises(ValueError, match=message):
        check_query(bad)


def test_check_query_takes_dates_as_iso_8601_text():
    checked = check_query(
        query(
            ("d", "gte", dt.date(2015, 6, 5)),
            ("d", "lte", "2015-06-15"),
            ("t", "gte", dt.datetime(2015, 6, 5, 9, 30)),
            ("t", "lte", pd.Timestamp("2015-06-05 09:30:00.000005")),
            ("u", "gte", "2015-06-05T09:30:59.5"),
            ("u", "lte", "2016-02-29T00:00"),
        )
    )
    assert [clause["value"] for clause in checked["and"]] == [
        "2015-06-05",
        "2015-06-15",
        "2015-06-05T09:30:00",
        "2015-06-05T09:30:00.000005",
        "2015-06-05T09:30:59.5",
        "2016-02-29T00:00",
    ]


@pytest.mark.parametrize(
    "bound",
    [
        "2015-6-5",
        "2015-02-29",
        "0000-01-01",
        "2015-06-05 09:30",
        "2015-06-05T24:00",
        "2015-06-05T09:30:60",
        "2015-06-05T09:30:00.0000001",
        "2015-06-05T09:30Z",
        "2015-06",
        "x",
    ],
)
def test_check_query_rejects_what_isnt_a_date(bound: str):
    with pytest.raises(ValueError, match="needs a finite number, or a date: as ISO 8601 text"):
        check_query(query(("d", "gte", bound)))


def test_check_query_rejects_a_date_and_time_with_a_time_zone():
    aware = dt.datetime(2015, 6, 5, tzinfo=dt.timezone.utc)
    with pytest.raises(ValueError, match="which has a time zone"):
        check_query(query(("t", "gte", aware)))


def test_check_query_takes_a_range_with_both_bounds():
    both = query(("x", "gte", 1), ("x", "lte", 2))
    assert check_query(both) == both


# queries as text (as packages/gti/test/query.test.ts has them) ----


def test_parse_query_reads_every_kind_of_clause():
    text = (
        'population_2021 >= 10000 and status in ("single-tier", "city") and name contains "cote" '
        "and x <= -1.5e3"
    )
    assert parse_query(text) == query(
        ("population_2021", "gte", 10000),
        ("status", "in", ["single-tier", "city"]),
        ("name", "contains", "cote"),
        ("x", "lte", -1500),
    )
    # (An integer as an int, as JSON reads it, but any other number as a float)
    values = [c["value"] for c in parse_query("a >= 1 and a >= 1.0 and a >= 1e0")["and"]]
    assert [type(value) for value in values] == [int, float, float]


def test_parse_query_reads_strict_bounds():
    text = 'x > 1 and x < 1e1 and d > "2015-06-05" and t<"2015-06-05T09:30"'
    assert parse_query(text) == query(
        ("x", "gt", 1),
        ("x", "lt", 10.0),
        ("d", "gt", "2015-06-05"),
        ("t", "lt", "2015-06-05T09:30"),
    )
    # (`>=` is one symbol, and a column can have a bound and a strict bound)
    assert parse_query("x>=1 and x<2") == query(("x", "gte", 1), ("x", "lt", 2))
    assert check_query("x >= 1 and x > 1") == query(("x", "gte", 1), ("x", "gt", 1))
    # (Before `>` and `<`, `not` is a column's name)
    assert parse_query("not > 1 or not not < 2") == {
        "and": [or_(clause("not", "gt", 1), not_(clause("not", "lt", 2)))]
    }


def test_parse_query_reads_top_and_bottom():
    assert parse_query("x top 10 and d BOTTOM 3 and `a b` Top 1") == query(
        ("x", "top_n", 10), ("d", "bottom_n", 3), ("a b", "top_n", 1)
    )
    # (Before `top` and `bottom`, `not` is a column's name)
    assert parse_query("not top 1 or not not bottom 2") == {
        "and": [or_(clause("not", "top_n", 1), not_(clause("not", "bottom_n", 2)))]
    }
    assert parse_query("top top 2") == query(("top", "top_n", 2))
    assert type(parse_query("x top 10")["and"][0]["value"]) is int


def test_parse_query_reads_no_query_from_empty_text():
    assert parse_query("") is None
    assert parse_query(" \t\n ") is None


def test_parse_query_reads_keywords_in_any_case_and_any_spacing():
    assert parse_query('a IN(1,TRUE , False,NULL)AND b Contains"x"') == query(
        ("a", "in", [1, True, False, None]), ("b", "contains", "x")
    )


def test_parse_query_reads_any_column_name_in_backticks():
    text = '`Name of town` contains "x" and `a``b` >= 1 and `` <= 2 and `and` in (null)'
    assert parse_query(text) == query(
        ("Name of town", "contains", "x"), ("a`b", "gte", 1), ("", "lte", 2), ("and", "in", [None])
    )
    # (Keywords are column names where a column goes)
    assert parse_query("in in (1)") == query(("in", "in", [1]))


def test_parse_query_reads_is_null_and_is_not_null():
    is_null = {"col": "a", "op": "is_null"}
    assert parse_query("a is null") == {"and": [is_null]}
    # (`is not null` is `not` and `is null`)
    assert parse_query("a IS NOT NULL") == {"and": [not_(is_null)]}
    assert parse_query("not a is not null") == {"and": [not_(not_(is_null))]}
    assert parse_query("a is null or b >= 2 and a is not null") == {
        "and": [or_(is_null, and_(B, not_(is_null)))]
    }
    # (Before `is`, `not` is a column's name; and `is` and `null` are names where a column goes)
    assert parse_query("not is null") == {"and": [{"col": "not", "op": "is_null"}]}
    assert parse_query("is is not null and null is null") == {
        "and": [not_({"col": "is", "op": "is_null"}), {"col": "null", "op": "is_null"}]
    }


def test_parse_query_reads_dates_as_strings():
    assert parse_query('d >= "2015-06-05" and t <= "2015-06-05T09:30"') == query(
        ("d", "gte", "2015-06-05"), ("t", "lte", "2015-06-05T09:30")
    )
    # (Any string, which the view's checked for)
    assert parse_query('d >= "x"') == query(("d", "gte", "x"))
    with pytest.raises(ValueError, match="needs a finite number, or a date"):
        check_query('d >= "x"')


def test_parse_query_reads_strings_as_json_does():
    assert parse_query(r'a contains "q\"\\\/\b\f\n\r\té😀 Côté"') == query(
        ("a", "contains", 'q"\\/\b\f\n\r\té😀 Côté')
    )


VALUE_EXPECTED = "expected a value: a string in double quotes, a number, true, false or null"
UNENDED_STRING = "a string must end with a double quote (with escapes as in JSON)"
BOUND_EXPECTED = "expected a number, or a date in double quotes"
PATTERN_EXPECTED = "expected a pattern between slashes, as in /^st\\./"
REPEAT_TOO_LARGE = "a repeat can be at most 1000, and its first number no more than its second"
OP_EXPECTED = (
    'expected "contains", "matches", "in", "not", ">=", "<=", ">", "<", "top", "bottom" or "is"'
)
COUNT_EXPECTED = "expected a whole number (at least 1)"


@pytest.mark.parametrize(
    "text, message",
    [
        ("a", f"{OP_EXPECTED}, at the end"),
        ("a = 1", f"{OP_EXPECTED}, at character 3"),
        (">= 1", "expected a column name, at character 1"),
        ("a >= x", f"{BOUND_EXPECTED}, at character 6"),
        ("a >= (", f"{BOUND_EXPECTED}, at character 6"),
        ("a contains x", "expected a string in double quotes, at character 12"),
        ("a in 1", 'expected "(", at character 6'),
        ("a in ()", f"{VALUE_EXPECTED}, at character 7"),
        ("a in (1 2)", 'expected "," or ")", at character 9'),
        ("a in (1,", f"{VALUE_EXPECTED}, at the end"),
        ("a >= 1 b", 'expected "and", "or" or the end of the query, at character 8'),
        ("a >= 1 and", "expected a column name, at the end"),
        ("a >= 1e999", "the number 1e999 is too large, at character 6"),
        ('a contains "x', f"{UNENDED_STRING}, at character 12"),
        ('a contains "\\x"', f"{UNENDED_STRING}, at character 12"),
        ("`a", "a column name in backticks must end with a backtick, at the end"),
        ("a >= .5", f"{BOUND_EXPECTED}, at character 6"),
        # (Of strict bounds)
        ("a >", f"{BOUND_EXPECTED}, at the end"),
        ("a > x", f"{BOUND_EXPECTED}, at character 5"),
        ("a > = 1", f"{BOUND_EXPECTED}, at character 5"),
        ("a <> 1", f"{BOUND_EXPECTED}, at character 4"),
        ("a < 1 < 2", 'expected "and", "or" or the end of the query, at character 7'),
        ("> 1", "expected a column name, at character 1"),
        ("a >= 01", 'expected "and", "or" or the end of the query, at character 7'),
        # (Of `top` and `bottom`)
        ("x top", f"{COUNT_EXPECTED}, at the end"),
        ("x top 0", f"{COUNT_EXPECTED}, at character 7"),
        ("x top 1.5", f"{COUNT_EXPECTED}, at character 7"),
        ("x top -1", f"{COUNT_EXPECTED}, at character 7"),
        ("x top 1e3", f"{COUNT_EXPECTED}, at character 7"),
        ("x bottom x", f"{COUNT_EXPECTED}, at character 10"),
        ('x top "3"', f"{COUNT_EXPECTED}, at character 7"),
        ("x top 9007199254740992", "the number 9007199254740992 is too large, at character 7"),
        ("x top 3 4", 'expected "and", "or" or the end of the query, at character 9'),
        # (Characters, not UTF-16 code units)
        ('`😀` contains "😀" x', 'expected "and", "or" or the end of the query, at character 18'),
        # (Of groups)
        ("(a >= 1", 'expected "and", "or" or ")", at the end'),
        ("(a >= 1 b", 'expected "and", "or" or ")", at character 9'),
        ('(x >= 5 or y in ("a")', 'expected "and", "or" or ")", at the end'),
        ("a >= 1)", 'expected "and", "or" or the end of the query, at character 7'),
        ("()", "expected a column name, at character 2"),
        ("not", "expected a column name, at the end"),
        ("a >= 1 or", "expected a column name, at the end"),
        ("a >= 1 or not", "expected a column name, at the end"),
        ('not "x', f"{UNENDED_STRING}, at character 5"),
        # (Of `is null`)
        ("a is", 'expected "null" or "not null", at the end'),
        ("a is nul", 'expected "null" or "not null", at character 6'),
        ("a is not", 'expected "null", at the end'),
        ("a is not not null", 'expected "null", at character 10'),
        ("a is null null", 'expected "and", "or" or the end of the query, at character 11'),
        ("a is (null)", 'expected "null" or "not null", at character 6'),
        # (Of `matches`)
        ("a matches", f"{PATTERN_EXPECTED}, at the end"),
        ('a matches "x"', f"{PATTERN_EXPECTED}, at character 11"),
        ("a matches 1", f"{PATTERN_EXPECTED}, at character 11"),
        ("a matches /x", "a pattern must end with a slash, at character 11"),
        ("a matches /x\ny/", "a pattern must end with a slash, at character 11"),
        ("a matches /x/g", 'a pattern can have only the flag "i", at character 14'),
        ("a matches /x/ii", 'a pattern can have only the flag "i", at character 14'),
        ("a matches //", "expected a pattern, at character 12"),
        ("a matches /(/", 'expected ")", at character 13'),
        ("a matches /a{2,1}/", f"{REPEAT_TOO_LARGE}, at character 13"),
        ("`😀` matches /😀)/", '")" must close a "(" (or be escaped: "\\)"), at character 15'),
        (
            "a matches /(?i)x/",
            '"(?" must be "(?:" (a pattern can\'t have lookarounds, named groups or flags), '
            "at character 12",
        ),
        # (A pattern is read wherever it is)
        ("a >= 1/2", "a pattern must end with a slash, at character 7"),
        ("a contains /x/", "expected a string in double quotes, at character 12"),
    ],
)
def test_parse_query_says_whats_wrong_and_where(text: str, message: str):
    with pytest.raises(ValueError) as err:
        parse_query(text)
    assert str(err.value) == message


def test_parse_query_binds_not_tighter_than_and_and_and_tighter_than_or():
    assert parse_query('a >= 1 or b >= 2 and not c contains "x"') == {
        "and": [or_(A, and_(B, not_(C)))]
    }
    assert parse_query('not a >= 1 and b >= 2 OR c contains "x"') == {
        "and": [or_(and_(not_(A), B), C)]
    }


def test_parse_query_groups_in_parentheses_splicing_a_group_into_one_of_its_kind():
    assert parse_query('(a >= 1 or b >= 2) and c contains "x"') == {"and": [or_(A, B), C]}
    assert parse_query('a >= 1 or (b >= 2 or c contains "x")') == {"and": [or_(A, B, C)]}
    assert parse_query('(a >= 1 and b >= 2) and (c contains "x")') == {"and": [A, B, C]}
    assert parse_query("((a >= 1))") == {"and": [A]}
    assert parse_query("not (a >= 1 and b >= 2)") == {"and": [not_(and_(A, B))]}
    assert parse_query("not not a >= 1") == {"and": [not_(not_(A))]}


def test_parse_query_reads_not_before_an_op_as_a_columns_name():
    assert parse_query("not >= 1") == query(("not", "gte", 1))
    assert parse_query('NOT contains "x" or not in (1)') == {
        "and": [or_(clause("NOT", "contains", "x"), clause("not", "in", [1]))]
    }
    assert parse_query("not not <= 1") == {"and": [not_(clause("not", "lte", 1))]}
    assert parse_query("or >= 1 or and >= 2") == {
        "and": [or_(clause("or", "gte", 1), clause("and", "gte", 2))]
    }


def test_parse_query_reads_a_pattern_between_slashes_with_the_flag_i_as_its_prefix():
    assert parse_query("name matches /^st\\./ and `a b` MATCHES /x/i") == query(
        ("name", "matches", "^st\\."), ("a b", "matches", "(?i)x")
    )
    # (A slash in a class needn't be escaped, and an escaped one is the slash)
    assert parse_query("a matches /[/]\\/\\\\/") == query(("a", "matches", "[/]/\\\\"))
    assert parse_query("(a matches /\\)/ )") == query(("a", "matches", "\\)"))
    assert parse_query("not matches /x/") == query(("not", "matches", "x"))
    assert parse_query("not a matches /x/") == {"and": [not_(clause("a", "matches", "x"))]}


def test_parse_query_reads_not_in_not_contains_and_not_matches_as_not_and_the_clause():
    x, y = clause("x", "in", [1, None]), clause("y", "contains", "a")
    z = clause("z", "matches", "(?i)^b")
    assert parse_query('x not in (1, null) and y NOT contains "a" or z Not Matches /^b/i') == {
        "and": [or_(and_(not_(x), not_(y)), not_(z))]
    }
    assert parse_query("not x not in (1, null)") == {"and": [not_(not_(x))]}
    assert parse_query('`a b` not contains "a"') == {"and": [not_(clause("a b", "contains", "a"))]}
    # (`not` where a column goes, before an op, is still a column's name, and so are the ops)
    assert parse_query("not not in (1)") == {"and": [not_(clause("not", "in", [1]))]}
    assert parse_query("in not in (1)") == {"and": [not_(clause("in", "in", [1]))]}


@pytest.mark.parametrize(
    "text, message",
    [
        ("x not", 'expected "contains", "matches" or "in", at the end'),
        ("x not >= 1", 'expected "contains", "matches" or "in", at character 7'),
        ("x not > 1", 'expected "contains", "matches" or "in", at character 7'),
        ("x not is null", 'expected "contains", "matches" or "in", at character 7'),
        ("x not top 3", 'expected "contains", "matches" or "in", at character 7'),
        ("x not not in (1)", 'expected "contains", "matches" or "in", at character 7'),
        ("x not in 1", 'expected "(", at character 10'),
        ("x not contains /a/", "expected a string in double quotes, at character 16"),
    ],
)
def test_parse_query_says_whats_wrong_after_not(text: str, message: str):
    with pytest.raises(ValueError) as err:
        parse_query(text)
    assert str(err.value) == message


def test_format_query_writes_not_and_one_of_those_clauses_with_not_after_the_column():
    x, y = clause("x", "in", [1, None]), clause("y", "contains", "a")
    z = clause("z", "matches", "(?i)^b")
    assert format_query({"and": [not_(x), not_(y)]}) == 'x not in (1, null) and y not contains "a"'
    assert format_query({"and": [or_(not_(z), not_(not_(x)))]}) == (
        "z not matches /^b/i or not x not in (1, null)"
    )
    assert format_query({"and": [not_(clause("in", "in", [1]))]}) == "`in` not in (1)"
    # (Not the others, or a group)
    assert format_query({"and": [not_(clause("x", "gte", 1)), not_(and_(x, y))]}) == (
        'not x >= 1 and not (x in (1, null) and y contains "a")'
    )
    queries = [
        {"and": [not_(x), not_(not_(y)), or_(not_(z), not_(clause("not", "in", [True])))]},
        {"and": [not_(clause("not", "contains", "x")), not_(clause("is", "matches", "a"))]},
    ]
    for q in queries:
        assert parse_query(format_query(q)) == q


def test_format_query_writes_a_query_as_text():
    assert format_query(
        query(
            ("population_2021", "gte", 10000),
            ("status", "in", ["single-tier", None, True, 1.5]),
            ("Name of town", "contains", 'a "b"'),
            ("a`b", "lte", -0.25),
        )
    ) == (
        'population_2021 >= 10000 and status in ("single-tier", null, true, 1.5) and '
        '`Name of town` contains "a \\"b\\"" and `a``b` <= -0.25'
    )
    assert format_query(None) == ""


def test_format_query_writes_strict_bounds():
    q = {
        "and": [
            clause("x", "gt", 1.5),
            not_(clause("d", "lt", "2015-06-05")),
            or_(clause("x", "lt", -0.25), clause("not", "gt", 2)),
        ]
    }
    assert format_query(q) == 'x > 1.5 and not d < "2015-06-05" and (x < -0.25 or not > 2)'
    assert parse_query(format_query(q)) == q


def test_format_query_writes_top_and_bottom():
    q = {
        "and": [
            clause("x", "top_n", 10),
            not_(clause("d", "bottom_n", 1)),
            or_(clause("top", "top_n", 2), clause("Bottom", "bottom_n", 3)),
        ]
    }
    # (A column named `top` or `bottom` in backticks, as they're ops after `not`)
    assert format_query(q) == "x top 10 and not d bottom 1 and (`top` top 2 or `Bottom` bottom 3)"
    assert parse_query(format_query(q)) == q
    assert format_query({"and": [not_(clause("not", "top_n", 1))]}) == "not not top 1"


def test_format_query_writes_groups_with_the_parentheses_they_need():
    b = clause("b", "in", [2])
    assert format_query({"and": [or_(A, and_(b, C))]}) == 'a >= 1 or b in (2) and c contains "x"'
    assert format_query({"and": [A, or_(b, C)]}) == 'a >= 1 and (b in (2) or c contains "x")'
    assert format_query({"and": [not_(or_(A, b))]}) == "not (a >= 1 or b in (2))"
    assert format_query({"and": [not_(and_(A, b)), C]}) == (
        'not (a >= 1 and b in (2)) and c contains "x"'
    )
    assert format_query({"and": [not_(not_(A))]}) == "not not a >= 1"
    # (A column named as a keyword that goes after a column, in backticks)
    assert format_query(query(("in", "in", [1]), ("Contains", "gte", 1))) == (
        "`in` in (1) and `Contains` >= 1"
    )
    assert format_query({"and": [{"col": "Is", "op": "is_null"}]}) == "`Is` is null"


def test_format_query_writes_is_null_and_is_not_null():
    is_null = {"col": "a b", "op": "is_null"}
    assert format_query({"and": [is_null]}) == "`a b` is null"
    assert format_query({"and": [not_(is_null), A]}) == "`a b` is not null and a >= 1"
    assert format_query({"and": [not_(not_(is_null))]}) == "not `a b` is not null"
    assert format_query({"and": [or_(is_null, not_(and_(is_null, A)))]}) == (
        "`a b` is null or not (`a b` is null and a >= 1)"
    )


@pytest.mark.parametrize(
    "value, text",
    [
        (1.0, "1"),
        (-0.0, "0"),
        (2**60, "1152921504606847000"),
        (1e21, "1e+21"),
        (1.5e21, "1.5e+21"),
        (123456.789, "123456.789"),
        (1e-6, "0.000001"),
        (1.25e-7, "1.25e-7"),
        (5e-324, "5e-324"),
        (-1.7976931348623157e308, "-1.7976931348623157e+308"),
    ],
)
def test_format_query_writes_numbers_as_javascript_does(value: float, text: str):
    assert format_query(query(("x", "gte", value))) == f"x >= {text}"


def test_format_query_writes_strings_as_javascript_does():
    # (With a lone surrogate escaped, as `JSON.stringify()` has it)
    text = format_query(query(("x", "contains", "\x00\x1f\x7f é\ud800")))
    assert text == 'x contains "\\u0000\\u001f\x7f é\\ud800"'


def test_format_query_writes_dates_as_strings():
    q = query(("d", "gte", "2015-06-05"), ("t", "lte", "2015-06-05T09:30:00.5"))
    assert format_query(q) == 'd >= "2015-06-05" and t <= "2015-06-05T09:30:00.5"'
    assert parse_query(format_query(q)) == q


def test_format_query_writes_what_parse_query_reads_back():
    queries = [
        query(("", "contains", "")),
        query(("``", "in", ["\n", " ", "é", 1e21, 5e-7])),
        query(("1a", "gte", -1), ("_", "lte", 0)),
        query(("and", "in", [False])),
        {"and": [clause("in", "in", [1]), not_(clause("contains", "contains", "x"))]},
        {
            "and": [
                not_(clause("not", "gte", 1)),
                or_(clause("or", "lte", 1), clause("and", "in", [None])),
            ]
        },
        {
            "and": [
                A,
                or_(and_(clause("b", "in", [1]), not_(or_(B, not_(C)))), clause("e", "gte", 3)),
                not_(and_(clause("f", "gte", 0), clause("g", "lte", 0))),
            ]
        },
        {"and": [or_(A, B)]},
        {"and": [{"col": "not", "op": "is_null"}, not_({"col": "is", "op": "is_null"})]},
        {"and": [not_(not_({"col": "null", "op": "is_null"}))]},
        query(("a", "matches", "^st\\.")),
        {"and": [or_(clause("a", "matches", "x"), clause("a", "contains", "/"))]},
    ]
    for q in queries:
        assert parse_query(format_query(q)) == q


def test_format_query_writes_a_pattern_between_slashes():
    q = {
        "and": [
            clause("matches", "matches", "(?i)a/b[/]\\\\"),
            not_(clause("b", "matches", "/")),
        ]
    }
    assert format_query(q) == "`matches` matches /a\\/b[\\/]\\\\/i and b not matches /\\//"
    assert parse_query(format_query(q)) == q
    # (A line break, which the text can't have in a pattern, as its escape)
    assert format_query(query(("a", "matches", "a\n[\r]"))) == "a matches /a\\n[\\r]/"
    assert parse_query("a matches /a\\n[\\r]/") == query(("a", "matches", "a\\n[\\r]"))


def test_check_query_reads_text():
    assert check_query('x in (1, null) and y >= 2 and z contains " ab "') == query(
        ("x", "in", [1, None]), ("y", "gte", 2), ("z", "contains", " ab ")
    )
    assert check_query("  ") is None
    with pytest.raises(ValueError) as err:
        check_query("y >= x")
    assert (
        str(err.value)
        == "`filter=` can't be read as a query: expected a number, or a date in double quotes, "
        "at character 6."
    )
    # (And checks the query it reads)
    with pytest.raises(ValueError, match="more than one 'gte' clause on column 'y'"):
        check_query("y >= 1 and y >= 2")


@pytest.mark.parametrize(
    "sort, expected",
    [
        (None, ()),
        ("x", (("x", False),)),
        ("-x", (("x", True),)),
        (["-x", "y"], (("x", True), ("y", False))),
        (("--x",), (("-x", True),)),
        ([], ()),
    ],
)
def test_parse_sort(sort: Any, expected: tuple):
    assert parse_sort(sort) == expected


@pytest.mark.parametrize(
    "sort, message",
    [
        (1, "must be a column name"),
        (["x", 1], "must be a column name"),
        ("-", "isn't a column name"),
        ("", "isn't a column name"),
        (["x", "-x"], "column 'x' more than once"),
    ],
)
def test_parse_sort_rejects(sort: Any, message: str):
    with pytest.raises(ValueError, match=message):
        parse_sort(sort)


# checking views, against the table ----

DF = pd.DataFrame(
    {
        "name": ["a", "b", "c", "d"],
        "num": [1.5, 2.0, None, 3.0],
        "few": ["x", "y", "x", None],
        "flag": [True, False, True, False],
    }
)


def filtered() -> GTI:
    return (
        GTI(DF)
        .i_cols_filter(columns="name", type="text")
        .i_cols_filter(columns="num", type="range")
        .i_cols_filter(columns=["few", "flag"], type="facet")
    )


def test_i_view_goes_in_the_spec():
    gti = filtered().i_view(
        filter=query(("few", "in", ["x", None]), ("num", "gte", 1), ("name", "contains", "A")),
        sort=["-num", "name"],
    )
    assert view_of(gti) == {
        "filter": query(("few", "in", ["x", None]), ("num", "gte", 1), ("name", "contains", "A")),
        "sort": [{"column": "num", "descending": True}, {"column": "name", "descending": False}],
        "hidden": [],
    }


def test_the_default_view_is_the_table_as_it_is():
    assert view_of(GTI(DF)) == {"filter": None, "sort": [], "hidden": []}
    assert view_of(filtered().i_view(sort="num").i_view()) == {
        "filter": None,
        "sort": [],
        "hidden": [],
    }
    # (A `GT` table's too)
    assert view_of(GT(DF).opt_interactive()) == {"filter": None, "sort": [], "hidden": []}


def test_i_view_checks_the_query_when_called():
    with pytest.raises(ValueError, match="needs a finite number"):
        GTI(DF).i_view(filter=query(("num", "gte", math.nan)))
    with pytest.raises(ValueError, match="isn't a column name"):
        GTI(DF).i_view(sort="-")


def test_a_facet_value_matches_as_javascript_matches_it():
    # (An integer matches a float that's equal to it, but not a boolean or a string)
    df = pd.DataFrame({"x": [1.0, 2.5]})
    gti = GTI(df).i_cols_filter(type="facet")
    assert view_of(gti.i_view(filter=query(("x", "in", [1]))))["filter"] is not None
    for value in [True, "1"]:
        with pytest.raises(ValueError, match="isn't a value of column 'x'"):
            view_of(gti.i_view(filter=query(("x", "in", [value]))))


@pytest.mark.parametrize(
    "view, message",
    [
        ({"filter": query(("num", "in", [1.5]))}, "'in' clause on column 'num', which has a range"),
        ({"filter": query(("few", "gte", 1))}, r"which has a facet filter \(for 'in' clauses\)"),
        ({"filter": "name > 1"}, r"'gt' clause on column 'name', which has a text filter"),
        (
            {"filter": query(("name", "in", ["a"]))},
            r"which has a text filter \(for 'contains' or 'matches' clauses\)",
        ),
        ({"filter": query(("few", "contains", "x"))}, "which has a facet filter"),
        ({"filter": query(("num", "matches", "x"))}, "'matches' clause on column 'num', which has"),
        ({"filter": "few matches /x/"}, "'matches' clause on column 'few', which has a facet"),
        ({"filter": "name top 1"}, "'top_n' clause on column 'name', which has a text filter"),
        ({"filter": "few bottom 2"}, "'bottom_n' clause on column 'few', which has a facet"),
        ({"filter": "nope top 2"}, "column 'nope', which has no filter"),
        ({"filter": query(("flag", "in", ["True"]))}, "'True', which isn't a value of column"),
        ({"filter": query(("few", "in", ["z"]))}, "isn't a value of column 'few'"),
        ({"filter": query(("nope", "in", ["z"]))}, r"which has no filter.*`i_cols_filter\(\)`"),
        ({"filter": "nope is not null"}, r"column 'nope', which has no filter"),
        ({"sort": "nope"}, "can't be sorted by column 'nope'"),
    ],
)
def test_views_are_checked_against_the_table(view: dict, message: str):
    with pytest.raises(ValueError, match=message):
        view_of(filtered().i_view(**view))


DATES = pd.DataFrame(
    {
        "d": pd.Series([dt.date(2015, 6, 5), None, dt.date(2015, 6, 15), dt.date(1999, 12, 31)]),
        "t": pd.to_datetime(
            ["2015-06-05 09:30", "2015-06-05", None, "2015-06-04 23:59:59"], format="ISO8601"
        ),
        "num": [1.0, 2.0, 3.0, 4.0],
    }
)


def dated() -> GTI:
    return GTI(DATES).i_cols_filter(columns=["d", "t"], type="date").i_cols_filter(columns="num")


@pytest.mark.parametrize(
    "filter, message",
    [
        (
            query(("num", "gte", "2015-06-05")),
            "'2015-06-05' for its 'gte' clause on column 'num', ",
        ),
        (query(("d", "gte", 1)), r'which has a date filter \(for dates, as "2015-06-15"\)'),
        (
            query(("d", "in", ["2015-06-05"])),
            r"which has a date filter \(for 'gte', 'lte', 'gt', 'lt', 'top_n' or 'bottom_n'",
        ),
        (query(("d", "lte", "2015-06-05T09:30")), r"without times \(give a date, as '2015-06-05'"),
        ('d > "2015-06-05T09:30"', r"'gt' clause on column 'd', whose values are dates, without"),
        ('num < "2015-06-05"', "'2015-06-05' for its 'lt' clause on column 'num', "),
    ],
)
def test_date_views_are_checked_against_the_table(filter: dict, message: str):
    with pytest.raises(ValueError, match=message):
        view_of(dated().i_view(filter=filter))


@pytest.mark.parametrize(
    "filter, message",
    [
        ({"and": [not_(clause("few", "in", ["z"]))]}, "isn't a value of column 'few'"),
        (
            {"and": [or_(clause("num", "gte", 1), clause("num", "in", [1.5]))]},
            "'in' clause on column 'num'",
        ),
        ({"and": [or_(clause("num", "gte", 2), not_(clause("nope", "gte", 1)))]}, "no filter"),
    ],
)
def test_groups_are_checked_against_the_table(filter: dict, message: str):
    with pytest.raises(ValueError, match=message):
        view_of(filtered().i_view(filter=filter))


def test_a_view_can_sort_without_sorting():
    gti = filtered().i_sorting(False).i_view(sort="-num")
    assert view_of(gti)["sort"] == [{"column": "num", "descending": True}]


# folding and cell text, as the runtime has them ----


@pytest.mark.parametrize(
    "text, expected",
    [
        ("ABC", "abc"),
        ("École", "ecole"),
        ("ÅNGSTRÖM", "angstrom"),
        ("Straße", "straße"),
        # (A character at a time: so a capital sigma is a sigma, even at the end of a word)
        ("ΣΊΣΥΦΟΣ", "σισυφοσ"),
        # (A dotted capital I is an i, with its dot, a combining mark, gone)
        ("İ", "i"),
        ("ﬁ", "ﬁ"),
        ("á", "a"),
    ],
)
def test_fold(text: str, expected: str):
    assert fold(text) == expected


def test_js_trim():
    assert js_trim("\xa0　 a b﻿\n") == "a b"
    # (Not what `str.strip()` takes away)
    assert js_trim("\x1c a \x85") == "\x1c a \x85"


def parsed_cell(html: str) -> Any:
    tree = _Tree()
    tree.feed(f"<table><tbody><tr><td>{html}</td></tr></tbody></table>")
    return tree.root.children[0].children[0].children[0].children[0]


@pytest.mark.parametrize(
    "html, expected",
    [
        ("Caf&eacute; <b>Noir</b>", "cafe noir"),
        ('x<span class="gt_footnote_marks">1</span>', "x"),
        ("x<script>y</script><style>z</style><template>w</template>", "x"),
        ('<img src="a.png" alt=" Árbol "> tree<img alt="">', " tree\narbol"),
        ("<svg><title> Up </title><g><title>no</title></g></svg>!", "!\nup"),
        ('<img alt="a"><svg><title>B</title></svg>', "\na\nb"),
        ("a<br>b", "ab"),
    ],
)
def test_cell_text(html: str, expected: str):
    assert cell_text(parsed_cell(html)) == expected


@pytest.mark.parametrize(
    "html, expected",
    [
        ("Plain  text", "Plain  text"),
        ("a &amp;\nb", "a &\nb"),
        ('<b>Ä</b><span class="gt_footnote_marks">1</span> <img alt=" Tree ">', "Ä \nTree"),
    ],
)
def test_match_text(html: str, expected: str):
    # (As `cell_text()` has it, but not folded)
    assert match_text(html) == expected
    assert fold(expected) == cell_text(parsed_cell(html))
    # (Line breaks as an HTML parser has them)
    assert match_text("a\r\nb\rc") == "a\nb\nc"


def test_label_text():
    assert label_text("  The\n kind ") == "The kind"
    assert (
        label_text('<b>A</b>&nbsp;b<span class="gt_footnote_marks">1</span><img alt="x">') == "A b"
    )


# view_rows() ----


def test_view_rows_filters_and_sorts():
    gti = filtered().i_view(filter=query(("flag", "in", [True])), sort="-name")
    assert view_rows(gti) == [2, 0]
    assert view_rows(filtered()) == [0, 1, 2, 3]
    assert view_rows(filtered().i_view(sort="-num")) == [3, 1, 0, 2]


def test_view_rows_by_a_querys_groups():
    # (`num` is 1.5, 2.0, missing, 3.0; `few` is "x", "y", "x", missing)
    def rows(filter: str) -> list[int]:
        return view_rows(filtered().i_view(filter=filter))

    assert rows('num >= 3 or few in ("y")') == [1, 3]
    assert rows('flag in (true) and (num <= 1.5 or name contains "C")') == [0, 2]
    # (A row whose value is missing, which a clause leaves out, is kept by `not`)
    assert rows("not num >= 2") == [0, 2]
    assert rows('not few in ("x")') == [1, 3]
    assert rows("not not num >= 2") == [1, 3]
    assert rows('not (num >= 2 or name contains "a")') == [2]
    # (`few not in (...)` is `not few in (...)`, and so are `not contains` and `not matches`)
    assert rows('few not in ("x")') == [1, 3]
    assert rows('name not contains "a"') == rows('not name contains "a"')
    assert rows("name not matches /^[AB]/") == rows("not name matches /^[AB]/")
    assert view_of(filtered().i_view(filter='few not in ("x")'))["filter"] == {
        "and": [not_(clause("few", "in", ["x"]))]
    }


def test_view_rows_by_is_null_clauses():
    # (`num` is 1.5, 2.0, missing, 3.0; `few` is "x", "y", "x", missing)
    def rows(filter: str, gti: GTI | None = None) -> list[int]:
        return view_rows((gti or filtered()).i_view(filter=filter))

    assert rows("num is null") == [2]
    assert rows("num is not null") == [0, 1, 3]
    assert rows("few is null or num is null") == [2, 3]
    assert rows('few is not null and few in ("x")') == [0, 2]
    assert rows("name is null") == []
    # (A float's NaN is missing too, with every backend)
    nan = {"n": ("float", [1.0, math.nan, None, 0.0])}
    for backend in BACKENDS:
        gti = GTI(frame(backend, nan)).i_cols_filter(type="range")
        assert rows("n is null", gti) == [1, 2]
        assert rows("not n is null", gti) == [0, 3]
    # (And of a column only for querying)
    hidden = filtered().i_cols_controls("few", display=False)
    assert rows("few is null", hidden) == [3]


def test_view_rows_by_matches_clauses():
    df = pd.DataFrame({"s": ["Straße", "st. Ives", None, "ÉCOLE", "x\n", "Iİı"]})
    gti = GTI(df).i_cols_filter(type="text")

    def rows(filter: str) -> list[int]:
        return view_rows(gti.i_view(filter=filter))

    # (Of the text unfolded: case-sensitive, and with its accents, unless the flag i ignores case)
    assert rows("s matches /^St/") == [0]
    assert rows("s matches /^st/i") == [0, 1]
    assert rows("s matches /^st\\./") == [1]
    assert rows("s matches /É/") == [3]
    # (A missing value's cell shows "None", which is text like any other)
    assert rows("s matches /e/i") == [0, 1, 2, 3]
    assert rows("s matches /ß$/") == []
    assert rows("s matches /e$/") == [0, 2]
    # (`$` is the end of the text, not before a line break at its end, and `.` isn't a line break)
    assert rows("s matches /x$/") == []
    assert rows("s matches /x./") == []
    assert rows("s matches /x\\n$/") == [4]
    # (Ignoring case, İ and ı are only themselves, as the runtime has them)
    assert rows("s matches /^ii/i") == []
    assert rows("s matches /İ/i") == [5]
    assert rows("s matches /[h-j]{3}/i") == []
    assert rows("s matches /I[^a-z]ı/i") == [5]
    assert rows("not s matches /e/i") == [4, 5]
    assert rows("s matches /\\S/ or s is null") == [0, 1, 2, 3, 4, 5]
    assert rows('s matches /^s/i and s contains "ives"') == [1]


def test_view_rows_keeps_rows_in_their_groups():
    gti = GTI(DF, groupname_col="flag").i_cols_filter(columns="num").i_view(sort="-num")
    # (The groups, in the order they're first seen: True, then False)
    assert view_rows(gti) == [0, 2, 3, 1]
    gti = gti.i_view(filter=query(("num", "lte", 2)), sort="-num")
    assert view_rows(gti) == [0, 1]


def test_view_rows_by_columns_only_for_querying():
    gti = (
        filtered()
        .fmt(columns="name", fns=lambda x: f"<b>{x.upper()}</b> item")
        .i_cols_controls(["name", "few", "num"], display=False)
    )
    assert "few" not in [column["id"] for column in render_parts(gti)[1]["columns"]]
    # (By the text its cells would show)
    assert view_rows(gti.i_view(filter=query(("name", "contains", "B ITEM")))) == [1]
    assert view_rows(gti.i_view(filter=query(("name", "contains", "a")))) == [0]
    assert view_rows(gti.i_view(filter=query(("name", "matches", "^[A-C] item$")))) == [0, 1, 2]
    assert view_rows(gti.i_view(filter=query(("few", "in", ["x"])), sort="-num")) == [0, 2]
    assert view_rows(gti.i_view(filter=query(("num", "gte", 2)), sort="-name")) == [3, 1]


def test_view_rows_of_a_table_with_merged_stub_cells():
    df = pd.DataFrame({"a": ["x", "x", "y"], "b": ["1", "2", "3"], "n": [3, 1, 2]})
    gti = GTI(df, rowname_col=["a", "b"]).i_view(sort="n")
    assert 'rowspan="2"' in render_parts(gti)[0]
    assert view_rows(gti) == [0, 1, 2]


def test_view_rows_by_dates():
    assert view_rows(dated().i_view(filter=query(("d", "gte", "2015-06-05")))) == [0, 2]
    assert view_rows(dated().i_view(filter=query(("d", "lte", "2015-06-05")), sort="d")) == [3, 0]
    # (A date as its midnight, in a column of dates and times)
    assert view_rows(dated().i_view(filter=query(("t", "lte", "2015-06-05")))) == [1, 3]
    assert view_rows(dated().i_view(filter=query(("t", "gte", "2015-06-05T09:30")))) == [0]
    # (A strict bound leaves out the bound: a date's midnight, for dates and times)
    assert view_rows(dated().i_view(filter=query(("d", "gt", "2015-06-05")))) == [2]
    assert view_rows(dated().i_view(filter=query(("d", "lt", "2015-06-05")))) == [3]
    assert view_rows(dated().i_view(filter=query(("t", "gt", "2015-06-05")))) == [0]
    assert view_rows(dated().i_view(filter=query(("t", "lt", "2015-06-05")))) == [3]


def test_view_rows_by_top_and_bottom():
    # (`num` is 1.5, 2.0, missing, 3.0; `d` is 2015-06-05, missing, 2015-06-15, 1999-12-31; `t`
    # is 2015-06-05 09:30, 2015-06-05, missing, 2015-06-04 23:59:59)
    def rows(filter: str, gti: GTI | None = None) -> list[int]:
        return view_rows((gti or filtered()).i_view(filter=filter))

    assert rows("num top 1") == [3]
    assert rows("num top 2") == [1, 3]
    assert rows("num bottom 1") == [0]
    # (Not a missing value, however many are asked for)
    assert rows("num top 100") == [0, 1, 3]
    assert rows("not num top 1") == [0, 1, 2]
    assert rows("num top 2 and num bottom 2") == [1]
    assert rows("num top 1 or num bottom 1") == [0, 3]
    assert rows("d top 1", dated()) == [2]
    assert rows("d bottom 2", dated()) == [0, 3]
    assert rows("t top 1", dated()) == [0]
    assert rows("t bottom 2", dated()) == [1, 3]
    # (Ranked among all the table's rows, not those the rest of the query keeps)
    assert rows('num top 1 and few in ("x")') == []
    assert rows('few in ("x") and num top 2') == []
    assert rows("num bottom 2 and flag in (true)") == [0]
    # (Ties with the n-th value are all kept)
    ties = pd.DataFrame({"n": [2, 3, 3, 1, 2, None]})
    tied = GTI(ties).i_cols_filter(type="range")
    assert rows("n top 1", tied) == [1, 2]
    assert rows("n top 2", tied) == [1, 2]
    assert rows("n top 3", tied) == [0, 1, 2, 4]
    assert rows("n bottom 2", tied) == [0, 3, 4]
    # (A float's NaN and infinities aren't ranked, with every backend; and the two zeros tie)
    floats = {"f": ("float", [1.0, math.nan, math.inf, -0.0, -math.inf, 0.0, None])}
    for backend in BACKENDS:
        gti = GTI(frame(backend, floats)).i_cols_filter(type="range")
        assert rows("f top 1", gti) == [0]
        assert rows("f bottom 1", gti) == [3, 5]
        assert rows("f top 9", gti) == [0, 3, 5]


# query_code() ----


def test_query_code():
    gti = filtered().i_view(
        filter=query(("few", "in", ["x", None]), ("num", "gte", 1.5)), sort=["-num", "name"]
    )
    assert query_code(gti, "polars") == (
        "import polars as pl\n\n"
        "df.filter(\n"
        '    (pl.col("num") >= 1.5) & pl.col("num").is_finite(),\n'
        '    pl.col("few").is_in(["x"]) | pl.col("few").is_null(),\n'
        ').sort(["num", "name"], descending=[True, False], nulls_last=True, maintain_order=True)\n'
    )
    assert query_code(gti, "pandas") == (
        "import numpy as np\n\n"
        "df[\n"
        '    ((df["num"] >= 1.5) & np.isfinite(df["num"]))\n'
        '    & (df["few"].isin(["x"]) | df["few"].isna())\n'
        '].sort_values(["num", "name"], ascending=[False, True], na_position="last", '
        'kind="stable")\n'
    )
    assert query_code(gti, "narwhals") == (
        "import narwhals as nw\n\n"
        "(\n"
        "    nw.from_native(df)\n"
        "    .filter(\n"
        '        (nw.col("num") >= 1.5) & nw.col("num").is_finite(),\n'
        '        nw.col("few").is_in(["x"]) | nw.col("few").is_null(),\n'
        "    )\n"
        '    .with_row_index("_row")\n'
        '    .with_columns((nw.col("num").is_nan() & ~nw.col("num").is_null()).fill_null(False)'
        '.alias("_nan_num"))\n'
        '    .sort(["_nan_num", "num", "name", "_row"], descending=[True, True, False, False], '
        "nulls_last=True)\n"
        '    .drop(["_row", "_nan_num"])\n'
        "    .to_native()\n"
        ")\n"
    )


def test_query_code_of_dates():
    gti = dated().i_view(
        filter=query(
            ("t", "lte", "2015-06-05T09:30:00.000005"),
            ("d", "gte", "2015-06-05"),
            ("t", "gte", "2015-06-05"),
        )
    )
    # (A date as its midnight, in a column of dates and times)
    assert query_code(gti, "polars") == (
        "import datetime\nimport polars as pl\n\n"
        "df.filter(\n"
        '    pl.col("d") >= datetime.date(2015, 6, 5),\n'
        '    pl.col("t") >= datetime.datetime(2015, 6, 5, 0, 0),\n'
        '    pl.col("t") <= datetime.datetime(2015, 6, 5, 9, 30, 0, 5),\n'
        ")\n"
    )
    assert query_code(gti, "pandas") == (
        "import datetime\n\n"
        "df[\n"
        '    (df["d"] >= datetime.date(2015, 6, 5))\n'
        '    & (df["t"] >= datetime.datetime(2015, 6, 5, 0, 0))\n'
        '    & (df["t"] <= datetime.datetime(2015, 6, 5, 9, 30, 0, 5))\n'
        "]\n"
    )
    for backend, data in [
        ("polars", pl.from_pandas(DATES)),
        ("pandas", DATES),
        ("narwhals", DATES),
    ]:
        assert run_code(query_code(gti, backend), data) == [0]


def test_query_code_of_strict_bounds():
    # (A bound first, as the filter has it, then the strict bounds, which no filter has)
    gti = dated().i_view(filter='num < 4 and num >= 2 and t < "2015-06-05T09:30"')
    assert query_code(gti, "polars") == (
        "import datetime\nimport polars as pl\n\n"
        "df.filter(\n"
        '    (pl.col("num") >= 2) & pl.col("num").is_finite(),\n'
        '    (pl.col("num") < 4) & pl.col("num").is_finite(),\n'
        '    pl.col("t") < datetime.datetime(2015, 6, 5, 9, 30),\n'
        ")\n"
    )
    assert query_code(gti, "pandas") == (
        "import datetime\nimport numpy as np\n\n"
        "df[\n"
        '    ((df["num"] >= 2) & np.isfinite(df["num"]))\n'
        '    & ((df["num"] < 4) & np.isfinite(df["num"]))\n'
        '    & (df["t"] < datetime.datetime(2015, 6, 5, 9, 30))\n'
        "]\n"
    )
    assert view_rows(gti) == [1]
    for backend, data in [
        ("polars", pl.from_pandas(DATES)),
        ("pandas", DATES),
        ("narwhals", DATES),
    ]:
        assert run_code(query_code(gti, backend), data) == [1]


def test_query_code_of_top_and_bottom():
    # (Ranked among all the rows, as the filter's terms are of the data's rows; a float's NaN and
    # infinities not ranked)
    gti = dated().i_view(filter="num bottom 2 and not d bottom 1 and t top 1")
    assert query_code(gti, "polars") == (
        "import polars as pl\n\n"
        "df.filter(\n"
        '    pl.when(pl.col("num").is_finite()).then(pl.col("num")).rank("min") <= 2,\n'
        '    ~(pl.col("d").rank("min") <= 1).fill_null(False),\n'
        '    pl.col("t").rank("min", descending=True) <= 1,\n'
        ")\n"
    )
    assert query_code(gti, "pandas") == (
        "import numpy as np\n\n"
        "df[\n"
        '    (df["num"].where(np.isfinite(df["num"])).rank(method="min") <= 2)\n'
        '    & (~(df["d"].rank(method="min") <= 1))\n'
        '    & (df["t"].rank(method="min", ascending=False) <= 1)\n'
        "]\n"
    )
    assert view_rows(gti) == [0]
    for backend, data in [
        ("polars", pl.from_pandas(DATES)),
        ("pandas", DATES),
        ("narwhals", DATES),
    ]:
        assert run_code(query_code(gti, backend), data) == [0]


# (Booleans, one of them missing: pandas' nullable ones)
FLAGS = pd.DataFrame({"on": pd.array([True, None, False, True], dtype="boolean")})


def flagged() -> GTI:
    return GTI(FLAGS).i_cols_filter(columns="on")


def test_bool_views_are_checked_against_the_table():
    assert render_parts(flagged())[1]["filters"] == [
        {"column": "on", "type": "bool", "values": [False, True], "missing": [1]}
    ]
    with pytest.raises(ValueError, match=r"which has a bool filter \(for one value: `\[True\]`"):
        render_parts(flagged().i_view(filter=query(("on", "in", [True, None]))))
    with pytest.raises(ValueError, match=r"which has a bool filter \(for one value"):
        render_parts(flagged().i_view(filter="on in (false, true)"))
    # (A value the column hasn't, as for a facet)
    all_on = GTI(pd.DataFrame({"on": [True, True]})).i_cols_filter()
    with pytest.raises(ValueError, match="False, which isn't a value of column 'on'"):
        render_parts(all_on.i_view(filter=query(("on", "in", [False]))))
    with pytest.raises(ValueError, match="'gte' clause on column 'on', which has a bool filter"):
        render_parts(flagged().i_view(filter=query(("on", "gte", 1))))


def test_view_rows_by_a_bool_filter():
    assert view_rows(flagged().i_view(filter=query(("on", "in", [True])))) == [0, 3]
    assert view_rows(flagged().i_view(filter=query(("on", "in", [False])))) == [2]
    assert view_rows(flagged().i_view(filter="on in (null)")) == [1]


def test_query_code_of_a_bool_filter():
    gti = flagged().i_view(filter=query(("on", "in", [True])))
    assert query_code(gti, "polars") == (
        'import polars as pl\n\ndf.filter(\n    pl.col("on").is_in([True]),\n)\n'
    )
    assert query_code(gti, "pandas") == 'df[\n    df["on"].isin([True])\n]\n'
    for value, expected in [(True, [0, 3]), (False, [2]), (None, [1])]:
        gti = flagged().i_view(filter=query(("on", "in", [value])))
        for backend, data in [
            ("polars", pl.from_pandas(FLAGS)),
            ("pandas", FLAGS),
            ("narwhals", FLAGS),
        ]:
            assert run_code(query_code(gti, backend), data) == expected


def test_query_code_by_columns_only_for_querying():
    gti = filtered().i_cols_controls(["few", "num"], display=False)
    gti = gti.i_view(filter=query(("few", "in", ["y"])), sort="-num")
    assert query_code(gti, "polars") == (
        "import polars as pl\n\n"
        "df.filter(\n"
        '    pl.col("few").is_in(["y"]),\n'
        ').sort(["num"], descending=[True], nulls_last=True, maintain_order=True)\n'
    )


def test_query_code_of_the_whole_table():
    assert query_code(GTI(DF), "polars") == "import polars as pl\n\ndf\n"
    assert query_code(GTI(DF), "pandas") == "df\n"


def test_query_code_of_text_and_missing_values():
    gti = filtered().i_view(filter=query(("name", "contains", " É "), ("few", "in", [None])))
    assert query_code(gti, "polars") == (
        "import polars as pl\n\n"
        "df.filter(\n"
        '    pl.col("name").str.to_lowercase().str.contains("e", literal=True),\n'
        '    pl.col("few").is_null(),\n'
        ")\n"
    )


def test_query_code_of_is_null_clauses():
    gti = filtered().i_view(
        filter="num is null and not few is null and (name is null or flag in (true))"
    )
    assert query_code(gti, "polars") == (
        "import polars as pl\n\n"
        "df.filter(\n"
        '    pl.col("num").is_null() | pl.col("num").is_nan(),\n'
        '    ~pl.col("few").is_null().fill_null(False),\n'
        '    pl.col("name").is_null() | pl.col("flag").is_in([True]),\n'
        ")\n"
    )
    assert query_code(gti, "pandas") == (
        "df[\n"
        '    (df["num"].isna())\n'
        '    & (~df["few"].isna())\n'
        '    & (df["name"].isna() | df["flag"].isin([True]))\n'
        "]\n"
    )
    assert query_code(gti, "narwhals").splitlines()[5:8] == [
        '        nw.col("num").is_null() | nw.col("num").is_nan(),',
        '        ~nw.col("few").is_null().fill_null(False),',
        '        nw.col("name").is_null() | nw.col("flag").is_in([True]),',
    ]
    # (After the filters' clauses, as the runtime has it, in their order)
    gti = filtered().i_view(filter="few is null and num >= 2 and name is null")
    assert query_code(gti, "pandas") == (
        "import numpy as np\n\n"
        "df[\n"
        '    ((df["num"] >= 2) & np.isfinite(df["num"]))\n'
        '    & (df["few"].isna())\n'
        '    & (df["name"].isna())\n'
        "]\n"
    )


def test_query_code_of_matches_clauses():
    gti = (
        GTI(DF)
        .i_cols_filter(columns=["name", "few", "flag"], type="text")
        .i_cols_filter(columns="num", type="range")
        .i_view(
            filter='name matches /^a.\\d\\/"/i and not few matches /[x&]/ and '
            "(flag matches /^T/ or num is null)"
        )
    )

    # (As packages/gti/test/code.test.ts has them: the pattern as the code reads it)
    def terms(ns: str) -> list[str]:
        return [
            f'{ns}.col("name").str.contains("(?i)^a.[0-9]/\\"")',
            f'~{ns}.col("few").str.contains("[x\\\\&]").fill_null(False)',
            f'{ns}.col("flag").cast({ns}.String).str.contains("^T") | {ns}.col("num").is_null() | '
            f'{ns}.col("num").is_nan()',
        ]

    polars = "".join(f"    {term},\n" for term in terms("pl"))
    assert query_code(gti, "polars") == f"import polars as pl\n\ndf.filter(\n{polars})\n"
    narwhals = "".join(f"        {term},\n" for term in terms("nw"))
    assert query_code(gti, "narwhals") == (
        "import narwhals as nw\n\n(\n    nw.from_native(df)\n    .filter(\n"
        f"{narwhals}    )\n    .to_native()\n)\n"
    )
    assert query_code(gti, "pandas") == (
        "df[\n"
        '    (df["name"].str.contains("(?i)^a.[0-9]/\\"", regex=True, na=False))\n'
        '    & (~df["few"].str.contains("[x\\\\&]", regex=True, na=False))\n'
        '    & (df["flag"].astype(str).str.contains("^T", regex=True, na=False) | df["num"].isna())\n'
        "]\n"
    )


@pytest.mark.parametrize("pattern", ["^[a-c]$", "(?i)^[B-D]", "x|y$", "(?i)^X$", "[^x]"])
def test_query_code_of_matches_clauses_keeps_the_rows_of_the_view(pattern: str):
    # (Of columns of strings, whose values are the text the table shows, a missing value none)
    gti = GTI(DF).sub_missing(missing_text="").i_cols_filter(columns=["name", "few"], type="text")
    for filter in [
        query(("name", "matches", pattern)),
        {"and": [not_(clause("few", "matches", pattern))]},
        {"and": [or_(clause("name", "matches", pattern), clause("few", "matches", pattern))]},
    ]:
        for backend, data in [
            ("polars", pl.from_pandas(DF)),
            ("pandas", DF),
            ("narwhals", DF),
            ("narwhals", pl.from_pandas(DF)),
            ("narwhals", pa.Table.from_pandas(DF)),
        ]:
            view = gti.i_view(filter=filter)
            assert run_code(query_code(view, backend), data) == view_rows(view), (filter, backend)


def test_query_code_has_the_query_as_the_runtime_does():
    # (Its clauses in the order of the filters, a range's lower bound first, and a facet's values
    # in their order, a missing value last; and whole bounds as integers)
    gti = filtered().i_view(
        filter=query(("few", "in", [None, "y", "x"]), ("num", "lte", 3.0), ("num", "gte", 1))
    )
    assert query_code(gti, "polars") == (
        "import polars as pl\n\n"
        "df.filter(\n"
        '    (pl.col("num") >= 1) & pl.col("num").is_finite(),\n'
        '    (pl.col("num") <= 3) & pl.col("num").is_finite(),\n'
        '    pl.col("few").is_in(["x", "y"]) | pl.col("few").is_null(),\n'
        ")\n"
    )


GROUPS = {
    "and": [
        clause("few", "in", ["x"]),
        or_(clause("num", "gte", 2), clause("name", "contains", "Ab")),
        not_(clause("flag", "in", [True, None])),
        not_(not_(clause("num", "lte", 3))),
        or_(
            and_(clause("few", "in", ["y"]), clause("num", "lte", 1.5)),
            not_(or_(clause("name", "contains", "q"), clause("flag", "in", [None]))),
        ),
    ]
}


def group_terms(ns: str) -> list[str]:
    # (As packages/gti/test/code.test.ts has them)
    return [
        f'{ns}.col("few").is_in(["x"])',
        f'(({ns}.col("num") >= 2) & {ns}.col("num").is_finite()) | '
        f'{ns}.col("name").str.to_lowercase().str.contains("ab", literal=True)',
        f'~({ns}.col("flag").is_in([True]) | {ns}.col("flag").is_null()).fill_null(False)',
        f'~(~(({ns}.col("num") <= 3) & {ns}.col("num").is_finite()).fill_null(False))'
        ".fill_null(False)",
        f'({ns}.col("few").is_in(["y"]) & ({ns}.col("num") <= 1.5) & {ns}.col("num").is_finite())'
        f' | ~({ns}.col("name").str.to_lowercase().str.contains("q", literal=True) | '
        f'{ns}.col("flag").is_null()).fill_null(False)',
    ]


def test_query_code_of_groups():
    gti = filtered().i_view(filter=GROUPS)
    terms = "".join(f"    {term},\n" for term in group_terms("pl"))
    assert query_code(gti, "polars") == f"import polars as pl\n\ndf.filter(\n{terms})\n"
    terms = "".join(f"        {term},\n" for term in group_terms("nw"))
    assert query_code(gti, "narwhals") == (
        "import narwhals as nw\n\n(\n    nw.from_native(df)\n    .filter(\n"
        f"{terms}    )\n    .to_native()\n)\n"
    )
    # (pandas' terms are never missing)
    assert query_code(gti, "pandas") == (
        "import numpy as np\n\ndf[\n"
        '    (df["few"].isin(["x"]))\n'
        '    & (((df["num"] >= 2) & np.isfinite(df["num"])) | '
        'df["name"].str.contains("ab", case=False, regex=False, na=False))\n'
        '    & (~(df["flag"].isin([True]) | df["flag"].isna()))\n'
        '    & (~~((df["num"] <= 3) & np.isfinite(df["num"])))\n'
        '    & ((df["few"].isin(["y"]) & (df["num"] <= 1.5) & np.isfinite(df["num"])) | '
        '~(df["name"].str.contains("q", case=False, regex=False, na=False) | df["flag"].isna()))\n'
        "]\n"
    )
    # (A nullable comparison, filled, is an atom)
    nullable = DF.assign(num=pd.array([1, 2, None, 3], dtype="Int64"))
    gti = GTI(nullable).i_cols_filter(columns="num").i_view(filter="not num >= 2")
    assert query_code(gti, "pandas") == 'df[\n    ~(df["num"] >= 2).fillna(False)\n]\n'


def test_query_code_of_groups_keeps_the_rows_of_the_view():
    for filter in [
        "not num >= 2",
        'not few in ("x") or num <= 1.5',
        'not (num >= 2 or few in ("y", null)) and flag in (true)',
        "not not num >= 2",
    ]:
        for backend, data in [
            ("polars", pl.from_pandas(DF)),
            ("pandas", DF),
            ("narwhals", DF),
            ("narwhals", pa.Table.from_pandas(DF)),
        ]:
            gti = filtered().i_view(filter=filter)
            assert run_code(query_code(gti, backend), data) == view_rows(gti), (filter, backend)


def test_query_code_for_pandas_of_other_data():
    gti = (
        GTI(pl.from_pandas(DF))
        .i_cols_filter(columns="num", type="range")
        .i_view(filter=query(("num", "gte", 2.5)))
    )
    assert query_code(gti, "pandas") == (
        'import numpy as np\n\ndf[\n    (df["num"] >= 2.5) & np.isfinite(df["num"])\n]\n'
    )


@pytest.mark.parametrize("backend", ["polars", "pandas", "pyarrow"])
@pytest.mark.parametrize("code_backend", ["polars", "pandas", "narwhals"])
def test_query_code_drops_the_hidden_columns(backend: str, code_backend: str):
    if code_backend != "narwhals" and backend != code_backend:
        pytest.skip("The code is for the data's own library")
    data = {"pandas": DF, "polars": pl.from_pandas(DF), "pyarrow": pa.Table.from_pandas(DF)}
    gti = (
        GTI(data[backend])
        .i_cols_filter(columns="few", type="facet")
        .i_cols_controls(columns=["few", "flag"], hideable=True)
        .i_view(filter=query(("few", "in", ["x"])), sort="-name", hidden=["flag", "few"])
    )
    code = query_code(gti, code_backend)
    # (After the filter and sort, which can use them)
    assert code.rstrip().endswith(
        ('.drop(columns=["few", "flag"])', '.drop(["few", "flag"])', ".to_native()\n)")
    )
    *statements, last = ast.parse(code).body
    scope: dict[str, Any] = {"df": data[backend]}
    exec(compile(ast.Module(statements, type_ignores=[]), "<code>", "exec"), scope)
    result = eval(compile(ast.Expression(last.value), "<code>", "eval"), scope)  # type: ignore[attr-defined]
    assert list(result.columns if not isinstance(result, pa.Table) else result.column_names) == [
        "name",
        "num",
    ]
    assert len(result) == 2


def test_query_code_needs_a_backend():
    with pytest.raises(ValueError, match='`backend=` must be "polars", "pandas", or "narwhals"'):
        query_code(GTI(DF), "duckdb")  # type: ignore[arg-type]


# the runtime ----


@pytest.fixture(scope="module")
def node_engine() -> Any:
    """Send a line to the engine, and get its answer."""
    node = shutil.which("node")
    if node is None or not (PKG_DIR / "node_modules" / "happy-dom").exists():
        pytest.skip("needs Node and packages/gti's dependencies (`npm ci`)")
    proc = subprocess.Popen(
        [node, str(PKG_DIR / "scripts" / "engine.mjs")],
        cwd=PKG_DIR,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    assert proc.stdin is not None and proc.stdout is not None

    def send(line: dict) -> dict:
        proc.stdin.write(json.dumps(line) + "\n")
        proc.stdin.flush()
        result = json.loads(proc.stdout.readline())
        assert "error" not in result, result.get("error")
        return result

    yield send
    proc.stdin.close()
    proc.wait(timeout=10)


@pytest.fixture(scope="module")
def engine(node_engine: Callable[[dict], dict]) -> Callable[[GT], dict]:
    """The rows the runtime shows for a table, its state, and its warnings."""
    return lambda gt: node_engine({"html": render_gti_html(gt, runtime="none")})


def assert_same_rows(engine: Callable[[GT], dict], gt: GT) -> list[int]:
    shown = engine(gt)
    assert shown["state"] == "ready"
    assert shown["warnings"] == []
    rows = view_rows(gt)
    assert rows == shown["rows"]
    return rows


def test_engine_shows_the_view(engine: Callable[[GT], dict]):
    gti = filtered().i_view(filter=query(("flag", "in", [True])), sort="-name")
    assert assert_same_rows(engine, gti) == [2, 0]
    # (Of a query as text, too)
    text = filtered().i_view(filter='flag in (true) and name contains "C"', sort="-name")
    assert assert_same_rows(engine, text) == [2]


# Tables of each backend whose views are compared: missing values, NaN, text, and range edges

EDGE_COLUMNS: dict[str, tuple[str, list[Any]]] = {
    "f": ("float", [1.5, None, math.nan, -math.inf, 2.0, math.inf, 1.5, 0.0]),
    "i": ("int", [3, 1, None, 2, 2, None, 1, 3]),
    "s": ("str", ["École", "ecole", "ÉCOLES", None, "Straße", "SS", "σίσυφος", "a\xa0b"]),
    "b": ("bool", [True, False, None, True, None, False, True, False]),
    "c": ("cat", ["lo", "hi", None, "lo", "mid", "hi", None, "lo"]),
    "d": (
        "date",
        [
            *[dt.date(2015, 6, 5), None, dt.date(2015, 6, 15), dt.date(1999, 12, 31)],
            *[dt.date(2015, 6, 5), dt.date(2015, 6, 4), None, dt.date(2016, 2, 29)],
        ],
    ),
    "t": (
        "datetime",
        [
            *[dt.datetime(2015, 6, 5), dt.datetime(2015, 6, 5, 9, 30), None],
            *[dt.datetime(2015, 6, 4, 23, 59, 59, 999999), dt.datetime(2015, 6, 6)],
            *[dt.datetime(2015, 6, 5, 9, 30, 0, 1), dt.datetime(2015, 6, 5, 9, 29, 59), None],
        ],
    ),
}

EDGE_VIEWS: list[tuple[str, dict, Any]] = [
    ("missing facet", query(("i", "in", [None])), None),
    ("missing and a value", query(("i", "in", [2, None])), "i"),
    ("float facet", query(("f", "in", [1.5, 0])), None),
    ("float missing (not NaN)", query(("f", "in", [None])), None),
    ("bool facet", query(("b", "in", [False, None])), "-i"),
    ("bool filter, true", query(("b", "in", [True])), None),
    ("bool filter, false", query(("b", "in", [False])), "-i"),
    ("bool filter, missing", query(("b", "in", [None])), None),
    ("category facet", query(("c", "in", ["mid", "lo"])), "-c"),
    ("category missing", query(("c", "in", [None])), None),
    ("range edges", query(("f", "gte", 1.5), ("f", "lte", 2)), None),
    ("range of ints", query(("i", "gte", 1.5)), "-i"),
    ("range without NaN or infinities", query(("f", "gte", -1e308)), None),
    ("upper bound", query(("f", "lte", 0)), None),
    ("strict range", query(("f", "gt", 0), ("f", "lt", 2)), None),
    ("strict range of ints", query(("i", "gt", 1.5)), "-i"),
    ("strict range without NaN or infinities", query(("f", "gt", -1e308)), None),
    ("strict upper bound", query(("f", "lt", 1.5)), "f"),
    ("a bound and a strict bound", query(("f", "gte", 1.5), ("f", "lt", 2)), None),
    ("text ignoring case and accents", query(("s", "contains", "ECOLE")), None),
    ("text, trimmed", query(("s", "contains", "\xa0 ÉCOLES　")), None),
    ("text with a no-break space", query(("s", "contains", "a\xa0b")), None),
    ("text, a sigma", query(("s", "contains", "ΣΊΣ")), None),
    ("text, a sharp s", query(("s", "contains", "ß")), None),
    ("blank text", query(("s", "contains", "  ")), "s"),
    ("text of numbers", query(("f", "contains", "1.5")), None),
    ("text of booleans", query(("b", "contains", "TRUE")), None),
    ("a missing value's text", query(("i", "contains", "NA")), None),
    ("several clauses", query(("i", "in", [1, 3]), ("c", "in", ["lo"])), ["-f", "s"]),
    ("sort floats descending", None, "-f"),
    ("sort floats", None, ["f", "-i"]),
    ("sort text", None, ["-s"]),
    ("sort booleans", None, ["b", "-c"]),
    ("date range", query(("d", "gte", "2015-06-05"), ("d", "lte", "2015-06-15")), None),
    ("date lower bound", query(("d", "gte", "2015-06-05")), "-d"),
    ("date upper bound, a leap day", query(("d", "lte", "2016-02-29")), "d"),
    ("dates and times from a date (its midnight)", query(("t", "gte", "2015-06-05")), None),
    ("dates and times to a date (its midnight)", query(("t", "lte", "2015-06-05")), "t"),
    ("dates and times to a time", query(("t", "lte", "2015-06-05T09:30")), None),
    ("to a time, with seconds", query(("t", "lte", "2015-06-05T09:29:59")), "-t"),
    ("from a time, to the microsecond", query(("t", "gte", "2015-06-05T09:30:00.000001")), None),
    ("after a date", query(("d", "gt", "2015-06-05")), "-d"),
    ("before a date", query(("d", "lt", "2015-06-05")), None),
    ("dates and times after a date (its midnight)", query(("t", "gt", "2015-06-05")), None),
    ("dates and times before a time", query(("t", "lt", "2015-06-05T09:30")), "t"),
    ("after a time, to the microsecond", query(("t", "gt", "2015-06-05T09:30")), None),
    ("text of dates", query(("d", "contains", "2015-06")), None),
    ("sort dates", None, ["d", "-t"]),
    ("not a range, keeping missing values and NaN", {"and": [not_(clause("f", "gte", 1.5))]}, None),
    ("not a facet with a missing value", {"and": [not_(clause("i", "in", [2, None]))]}, "-i"),
    ("not a bool filter", {"and": [not_(clause("b", "in", [True]))]}, None),
    ("not a category", {"and": [not_(clause("c", "in", ["lo"]))]}, None),
    ("not text, keeping missing values", {"and": [not_(clause("s", "contains", "ecole"))]}, None),
    ("not a date", {"and": [not_(clause("d", "lte", "2015-06-05"))]}, "d"),
    ("not dates and times", {"and": [not_(clause("t", "gte", "2015-06-05T09:30"))]}, None),
    ("or of ranges", {"and": [or_(clause("f", "lte", 0), clause("i", "gte", 3))]}, None),
    ("not a strict range, keeping missing values", {"and": [not_(clause("f", "gt", 1.5))]}, None),
    (
        "strict bounds in an or",
        {"and": [or_(clause("i", "lt", 2), clause("d", "gt", "2015-06-05"))]},
        "-i",
    ),
    (
        "not an or",
        {
            "and": [
                clause("i", "gte", 1),
                not_(or_(clause("b", "in", [True]), clause("c", "in", ["lo"]))),
            ]
        },
        "-f",
    ),
    ("not not", {"and": [not_(not_(clause("f", "gte", 1.5)))]}, None),
    (
        "and in an or",
        {
            "and": [
                or_(
                    and_(clause("i", "gte", 2), clause("c", "in", ["lo", None])),
                    clause("d", "gte", "2015-06-15"),
                    not_(clause("s", "contains", "s")),
                )
            ]
        },
        "s",
    ),
    ("float is null, NaN too", {"and": [is_null("f")]}, None),
    ("float is not null", {"and": [not_(is_null("f"))]}, "-f"),
    ("is null of every kind", {"and": [or_(*map(is_null, "isbcdt"))]}, ["c", "-t"]),
    ("is null and a facet", {"and": [clause("c", "in", ["lo", None]), not_(is_null("c"))]}, None),
    ("is null in an and", {"and": [or_(and_(is_null("i"), is_null("d")), is_null("b"))]}, None),
    ("pattern with accents", query(("s", "matches", "^É")), None),
    ("pattern ignoring case", query(("s", "matches", "(?i)école")), "s"),
    ("pattern at the end", query(("s", "matches", "S$")), None),
    ("pattern, a sharp s", query(("s", "matches", "(?i)ss|ß")), None),
    ("pattern, a sigma", query(("s", "matches", "(?i)^Σ.Σ")), None),
    ("pattern, a no-break space", query(("s", "matches", "a\\sb|a\\Wb")), None),
    ("pattern of a word", query(("s", "matches", "^\\w+$")), None),
    ("pattern of numbers", query(("f", "matches", "^-?\\d\\.\\d$")), "-f"),
    ("pattern of a missing value's text", query(("i", "matches", "(?i)^<?na")), None),
    ("pattern of dates", query(("d", "matches", "-0?6-(?:05|15)$")), None),
    ("not a pattern, keeping missing values", {"and": [not_(clause("s", "matches", "e"))]}, None),
    (
        "a pattern in an or",
        {"and": [or_(clause("s", "matches", "(?i)^s"), clause("s", "contains", "ecole"))]},
        "s",
    ),
    ("top floats, without NaN or infinities", query(("f", "top_n", 2)), None),
    ("bottom floats, ties kept", query(("f", "bottom_n", 2)), "-f"),
    ("top ints, ties kept", query(("i", "top_n", 3)), "i"),
    ("bottom ints", query(("i", "bottom_n", 1)), None),
    ("more than there are", query(("i", "top_n", 100)), None),
    ("top dates", query(("d", "top_n", 3)), "-d"),
    ("bottom dates", query(("d", "bottom_n", 2)), None),
    ("top dates and times", query(("t", "top_n", 2)), "t"),
    ("bottom dates and times", query(("t", "bottom_n", 1)), None),
    ("not top", {"and": [not_(clause("f", "top_n", 1))]}, None),
    ("top of the whole table", query(("f", "gte", 1.5), ("d", "top_n", 1)), None),
    ("top and bottom", query(("i", "top_n", 3), ("i", "bottom_n", 3)), None),
    (
        "top or bottom in groups",
        {"and": [or_(clause("f", "top_n", 1), and_(clause("t", "bottom_n", 3), is_null("i")))]},
        "-t",
    ),
]


def edge_table(backend: str) -> GTI:
    return (
        GTI(frame(backend, EDGE_COLUMNS))
        .i_pagination(False)
        .i_cols_filter(columns=["f", "i"], type="range")
        .i_cols_filter(columns="s", type="text")
        .i_cols_filter(columns="b", type="bool")
        .i_cols_filter(columns="c", type="facet")
        .i_cols_filter(columns=["d", "t"], type="date")
    )


def leaves(items: list[dict]) -> list[dict]:
    """The clauses of a query's parts, those in groups too."""
    found = []
    for item in items:
        if "col" in item:
            found.append(item)
        elif "not" in item:
            found.extend(leaves([item["not"]]))
        else:
            found.extend(leaves(next(iter(item.values()))))
    return found


def edge_table_for(backend: str, filter: dict | None) -> GTI:
    gti = edge_table(backend)
    # (A clause's column gets the filter that has its op: for "in", a facet, but for one value of
    # the booleans, their bool filter)
    for leaf in leaves(filter["and"] if filter is not None else []):
        col, op = leaf["col"], leaf["op"]
        if op == "in" and (col != "b" or len(leaf["value"]) > 1):
            gti = gti.i_cols_filter(columns=col, type="facet")
        elif op in ("contains", "matches"):
            gti = gti.i_cols_filter(columns=col, type="text")
    return gti


@pytest.mark.parametrize("backend", BACKENDS)
@pytest.mark.parametrize("name, filter, sort", EDGE_VIEWS, ids=[view[0] for view in EDGE_VIEWS])
def test_views_of_edge_cases(
    engine: Callable[[GT], dict], backend: str, name: str, filter: dict | None, sort: Any
):
    gti = edge_table_for(backend, filter).i_view(filter=filter, sort=sort)
    assert_same_rows(engine, gti)


@pytest.mark.parametrize("backend", BACKENDS)
def test_edge_cases_keep_the_rows_expected(engine: Callable[[GT], dict], backend: str):
    def rows(filter: dict | None, sort: Any = None) -> list[int]:
        return assert_same_rows(engine, edge_table_for(backend, filter).i_view(filter, sort))

    # (pandas' NaN is missing)
    nan_missing = backend == "pandas"
    assert rows(query(("f", "in", [None]))) == ([1, 2] if nan_missing else [1])
    assert rows(query(("f", "gte", 1.5), ("f", "lte", 2))) == [0, 4, 6]
    assert rows(query(("f", "gte", -1e308))) == [0, 4, 6, 7]
    assert rows(query(("s", "contains", "ECOLE"))) == [0, 1, 2]
    assert rows(query(("s", "contains", "ss"))) == [5]
    assert rows(query(("s", "contains", "ß"))) == [4]
    # (A pattern doesn't fold accents, and ignores only case; its \s and \W are ASCII's)
    assert rows(query(("s", "matches", "(?i)école"))) == [0, 2]
    assert rows(query(("s", "matches", "S$"))) == [2, 5]
    assert rows(query(("s", "matches", "a\\sb"))) == []
    assert rows(query(("s", "matches", "a\\Wb"))) == [7]
    assert rows(query(("i", "in", [2, None])), "i") == [3, 4, 2, 5]
    assert rows(query(("b", "in", [True]))) == [0, 3, 6]
    assert rows(query(("b", "in", [False])), "-i") == [7, 1, 5]
    assert rows(query(("b", "in", [None]))) == [2, 4]
    assert rows(query(("d", "gte", "2015-06-05"), ("d", "lte", "2015-06-15"))) == [0, 2, 4]
    assert rows(query(("t", "lte", "2015-06-05"))) == [0, 3]
    assert rows(query(("t", "gte", "2015-06-05"), ("t", "lte", "2015-06-05T09:30"))) == [0, 1, 6]
    # (A strict bound leaves out the bound itself, and NaN and infinities, as a bound does)
    assert rows(query(("f", "gt", 1.5))) == [4]
    assert rows(query(("f", "lt", 1.5))) == [7]
    assert rows(query(("f", "gt", 0), ("f", "lt", 2))) == [0, 6]
    assert rows(query(("i", "lt", 2))) == [1, 6]
    assert rows(query(("d", "gt", "2015-06-05"))) == [2, 7]
    assert rows(query(("d", "lt", "2015-06-05"))) == [3, 5]
    # (A date is its midnight, so after it is that day's times but midnight)
    assert rows(query(("t", "gt", "2015-06-05"))) == [1, 4, 5, 6]
    assert rows(query(("t", "lt", "2015-06-05T09:30"))) == [0, 3, 6]
    assert rows({"and": [not_(clause("f", "gt", 1.5))]}) == [0, 1, 2, 3, 5, 6, 7]
    # (Descending, NaN is first, as it's after every number, ascending; but not if it's missing)
    descending = rows(None, "-f")
    assert descending == ([5, 4, 0, 6, 7, 3, 1, 2] if nan_missing else [2, 5, 4, 0, 6, 7, 3, 1])
    assert rows(None, "f") == [3, 7, 0, 6, 4, 5] + ([1, 2] if nan_missing else [2, 1])
    # (A row whose value is missing, or NaN or infinite, which a clause leaves out, is kept by `not`)
    assert rows({"and": [not_(clause("f", "gte", 1.5))]}) == [1, 2, 3, 5, 7]
    assert rows({"and": [not_(clause("i", "in", [2, None]))]}) == [0, 1, 6, 7]
    assert rows({"and": [not_(clause("b", "in", [None]))]}) == [0, 1, 3, 5, 6, 7]
    assert rows({"and": [not_(clause("s", "contains", "ecole"))]}) == [3, 4, 5, 6, 7]
    assert rows({"and": [not_(clause("d", "lte", "2015-06-05"))]}) == [1, 2, 6, 7]
    assert rows({"and": [or_(clause("f", "lte", 0), clause("i", "gte", 3))]}) == [0, 7]
    assert rows({"and": [not_(not_(clause("f", "gte", 1.5)))]}) == [0, 4, 6]
    # (A float's NaN is missing, as pandas has it, with every backend)
    assert rows({"and": [is_null("f")]}) == [1, 2]
    assert rows({"and": [not_(is_null("f"))]}, "-f") == [5, 4, 0, 6, 7, 3]
    assert rows({"and": [is_null("i")]}) == [2, 5]
    assert rows({"and": [is_null("s"), not_(is_null("b"))]}) == [3]
    assert rows({"and": [or_(is_null("d"), is_null("t"))]}) == [1, 2, 6, 7]
    # (Top and bottom: the rows tied with the n-th kept, but not missing values, NaN or
    # infinities, and ranked among all the table's rows)
    assert rows(query(("f", "top_n", 1))) == [4]
    assert rows(query(("f", "top_n", 2))) == [0, 4, 6]
    assert rows(query(("f", "top_n", 3))) == [0, 4, 6]
    assert rows(query(("f", "top_n", 4))) == [0, 4, 6, 7]
    assert rows(query(("f", "top_n", 100))) == [0, 4, 6, 7]
    assert rows(query(("f", "bottom_n", 1))) == [7]
    assert rows(query(("f", "bottom_n", 2))) == [0, 6, 7]
    assert rows(query(("i", "top_n", 1))) == [0, 7]
    assert rows(query(("i", "top_n", 2))) == [0, 7]
    assert rows(query(("i", "top_n", 3))) == [0, 3, 4, 7]
    assert rows(query(("i", "bottom_n", 1))) == [1, 6]
    assert rows(query(("d", "top_n", 1))) == [7]
    assert rows(query(("d", "top_n", 2))) == [2, 7]
    assert rows(query(("d", "top_n", 3))) == [0, 2, 4, 7]
    assert rows(query(("d", "bottom_n", 1))) == [3]
    assert rows(query(("d", "bottom_n", 2))) == [3, 5]
    assert rows(query(("t", "top_n", 2))) == [4, 5]
    assert rows(query(("t", "bottom_n", 1))) == [3]
    assert rows({"and": [not_(clause("f", "top_n", 1))]}) == [0, 1, 2, 3, 5, 6, 7]
    assert rows(query(("f", "gte", 1.5), ("d", "top_n", 1))) == []


@pytest.mark.parametrize("backend", BACKENDS)
def test_views_of_formatted_text(engine: Callable[[GT], dict], backend: str):
    columns = {
        "n": ("float", [1234.5, 0.5, None, 1e6]),
        "m": ("str", ["![Árbol](a.png) tree", "*bold*", "plain", None]),
    }
    gti = (
        GTI(frame(backend, columns))
        .fmt_number(columns="n", decimals=1)
        .fmt_markdown(columns="m")
        .tab_footnote("A note", locations=loc.body(columns="m", rows=[2]))
        .tab_style(style.text(weight="bold"), locations=loc.body(columns="n"))
        .i_cols_filter(type="text")
    )
    for filter, expected in [
        (query(("n", "contains", "1,234.5")), [0]),
        (query(("n", "contains", "0.5")), [1]),
        (query(("m", "contains", "arbol")), [0]),
        (query(("m", "contains", "tree\narbol")), [0]),
        (query(("m", "contains", "bold")), [1]),
        # (Not the footnote's mark)
        (query(("m", "contains", "plain1")), []),
        (query(("m", "contains", "plain")), [2]),
        (query(("n", "matches", "^1,2")), [0]),
        (query(("m", "matches", "^ tree\nÁrbol$")), [0]),
        (query(("m", "matches", "(?i)árbol$")), [0]),
        (query(("m", "matches", "plain$")), [2]),
        (query(("m", "matches", "\\*")), []),
    ]:
        assert assert_same_rows(engine, gti.i_view(filter=filter)) == expected


@pytest.mark.parametrize("backend", BACKENDS)
def test_views_of_groups(engine: Callable[[GT], dict], backend: str):
    columns = {
        "g": ("str", ["A", "B", "A", "B", "A", "C"]),
        "s": ("str", ["r0", "r1", "r2", "r3", "r4", "r5"]),
        "n": ("int", [5, 3, 1, 4, 2, 6]),
    }
    for as_column in [False, True]:
        gti = (
            GTI(frame(backend, columns), rowname_col="s", groupname_col="g")
            .tab_options(row_group_as_column=as_column)
            .i_pagination(False)
            .i_cols_filter(columns="n", type="range")
        )
        assert assert_same_rows(engine, gti.i_view(sort="-n")) == [0, 4, 2, 3, 1, 5]
        filtered = gti.i_view(filter=query(("n", "gte", 3)), sort="n")
        assert assert_same_rows(engine, filtered) == [0, 1, 3, 5]


def test_views_of_merged_stub_cells(engine: Callable[[GT], dict]):
    df = pd.DataFrame({"a": ["x", "x", "y"], "b": ["1", "2", "3"], "n": [3, 1, 2]})
    gti = GTI(df, rowname_col=["a", "b"]).i_cols_filter(columns="n").i_view(sort="n")
    assert assert_same_rows(engine, gti) == [0, 1, 2]


def test_views_of_an_ordered_arrow_dictionary(engine: Callable[[GT], dict]):
    levels = pa.array(["lo", "mid", "hi"])
    column = pa.DictionaryArray.from_arrays(pa.array([2, 0, None, 1, 0]), levels, ordered=True)
    gti = GTI(pa.table({"c": column})).i_cols_filter(type="facet")
    assert assert_same_rows(engine, gti.i_view(sort="-c")) == [0, 3, 1, 4, 2]
    filtered = gti.i_view(filter=query(("c", "in", ["hi", None])), sort="c")
    assert assert_same_rows(engine, filtered) == [0, 2]


# the runtime, with random tables and views ----

st = hypothesis.strategies

TEXTS = [
    "Ábc", "abc", "ÉCOLE", "école", "Straße", "SS", "İx", "ix", "ΣΊΣΥΦΟΣ", "σίσυφος", "a\xa0b",
    "x y", "", "1.5", "lo",
]  # fmt: skip
NEEDLES = [
    "a", "É", "e", "ss", "ß", "İ", "i̇", "σ", "Σ", "ς", " a ", "\xa0b", "1", ".", "true", "NA",
    "lo", "ab", "x y", "zzz", " ",
]  # fmt: skip
PATTERNS = [
    "^a", "(?i)^a", "É", "(?i)école", "[a-z]+$", "\\d", "s{2}", "(?i)ss", "^.{3}$", "x y|lo", "\\.",
    "\\W", "(?i)σ", "(?i)i", "(?i)İ", "^\\S+$", "ß", "(?i)[^a-z]", "^$", "(?i)^(?:true|na)",
]  # fmt: skip
VALUES: dict[str, list[Any]] = {
    "int": [-2, 0, 1, 3, None],
    "float": [-1.5, -0.0, 0.0, 1.0, 2.5, math.nan, math.inf, -math.inf, None],
    "str": [*TEXTS, None],
    "bool": [True, False, None],
    "cat": ["lo", "hi", "mid", None],
    "date": [dt.date(2015, 6, 5), dt.date(2015, 6, 15), dt.date(1999, 12, 31), None],
    "datetime": [
        *[dt.datetime(2015, 6, 5), dt.datetime(2015, 6, 5, 9, 30), None],
        *[dt.datetime(2015, 6, 5, 23, 59, 59, 999999), dt.datetime(1999, 12, 31, 12)],
    ],
}
# (A date filter's bounds, besides its values: dates, and dates and times, around the values')
DATE_BOUNDS = [
    *["2015-06-05", "2015-06-06", "2015-06-04", "1999-12-31", "2016-01-01", "0001-01-01"],
    *["2015-06-05T09:30", "2015-06-05T09:29:59.999999", "2015-06-05T00:00:00.000001"],
    *["1999-12-31T12:00:00", "2015-06-05T23:59:59.999999"],
]


# (Hypothesis draws what's first of a sample, and small numbers, more often than others: so these
# start with what's typical)


def some(draw: Any, items: list[Any], most: int) -> list[Any]:
    """Some of `items` (up to `most` of them, or none), in any order."""
    count = draw(st.sampled_from([1, 2, 0, 3]))
    return draw(st.permutations(items))[: min(count, most)]


@st.composite
def tables(
    draw: Any, backend: str, groups: bool = True
) -> tuple[GTI, dict[str, tuple[str, list[Any]]]]:
    """A table, filterable by its columns (but without a view), and its columns."""
    nrows = draw(st.sampled_from([6, 9, 3, 1, 2, 4, 5, 7, 8]))
    kinds = draw(st.lists(st.sampled_from(list(VALUES)), min_size=1, max_size=4))
    columns = {}
    for i, kind in enumerate(kinds):
        # (A column's values are a few of its kind's, so that rows tie, and have NaN, and so on)
        pool = draw(st.permutations(VALUES[kind]))[: draw(st.sampled_from([3, 2, 4, 1]))]
        values = draw(st.lists(st.sampled_from(pool), min_size=nrows, max_size=nrows))
        columns[f"c{i}"] = (kind, values)
    groups = groups and draw(st.booleans())
    if groups:
        columns["g"] = (
            "str",
            draw(st.lists(st.sampled_from("ABC"), min_size=nrows, max_size=nrows)),
        )
    stub = draw(
        st.sampled_from(
            [None, *[name for name, (kind, _) in columns.items() if kind == "str" and name != "g"]]
        )
    )

    data = frame(backend, columns)
    gti = GTI(data, rowname_col=stub, groupname_col="g" if groups else None).i_pagination(False)
    if groups and draw(st.booleans()):
        gti = gti.tab_options(row_group_as_column=True)
    for name, (kind, _) in columns.items():
        if kind in ("int", "float") and draw(st.booleans()):
            gti = gti.fmt_number(columns=name, decimals=draw(st.integers(0, 2)))
        if name != "g" and draw(st.sampled_from([True, False, True])):
            # (The filters the column's values can have: e.g., not a range of missing values)
            types = {
                "number": ["range", "facet", "text"],
                "date": ["date", "facet", "text"],
                "datetime": ["date", "facet", "text"],
                "boolean": ["bool", "facet", "text"],
                "other": ["text"],
            }.get(_get_column_kind(data, name), ["facet", "text"])
            gti = gti.i_cols_filter(columns=name, type=draw(st.sampled_from(types)))
    return gti, columns


def filter_clauses(draw: Any, f: dict, kinds: dict, blank: bool = True) -> list[dict]:
    """Clauses of a filter: its text (or blank text, which isn't in a group) or a pattern, a facet's
    values, a range's bounds (one or both), or that it's missing."""
    col = f["column"]
    if draw(st.sampled_from([False, False, False, True])):
        # (A column with any filter can be missing)
        return [is_null(col)]
    if f["type"] == "text":
        if draw(st.sampled_from([False, True, False])):
            return [{"col": col, "op": "matches", "value": draw(st.sampled_from(PATTERNS))}]
        needles = [needle for needle in NEEDLES if blank or js_trim(needle) != ""]
        return [{"col": col, "op": "contains", "value": draw(st.sampled_from(needles))}]
    if f["type"] in ("facet", "bool"):
        # (A bool filter's one value)
        choices = [value for value in f["values"] if value is not None] + [None]
        most = 1 if f["type"] == "bool" else 3
        value = draw(st.lists(st.sampled_from(choices), min_size=1, max_size=most, unique=True))
        return [{"col": col, "op": "in", "value": value}]
    if f["type"] == "date":
        # (A column of dates takes dates, without times)
        times = kinds[col] == "datetime"
        bounds = [b for b in DATE_BOUNDS if times or "T" not in b]
        values = [value for value in f["values"] if value is not None]
        bound = (
            st.sampled_from(values) | st.sampled_from(bounds) if values else st.sampled_from(bounds)
        )
    else:
        numbers = [value for value in f["values"] if value is not None]
        bound = st.sampled_from(numbers) | st.floats(-3, 4) if numbers else st.floats(-3, 4)
    ops = ["gte", "lte", "gt", "lt", "top_n", "bottom_n"]
    ops = draw(st.lists(st.sampled_from(ops), min_size=1, unique=True))
    # (A top or bottom's count: often fewer than the rows, but sometimes more)
    count = st.sampled_from([1, 2, 3, 4, 9])
    return [
        {"col": col, "op": op, "value": draw(count if op.endswith("_n") else bound)} for op in ops
    ]


def group_part(
    draw: Any, spec: dict, kinds: dict, depth: int, outer: str | None, kind: str | None = None
) -> dict:
    """A part of a query's group: a clause, or a group (not of the kind it's in)."""
    if kind is None:
        options = ["clause", "not", "or", "and"] if depth < 3 else ["clause"]
        kind = draw(st.sampled_from([option for option in options if option != outer]))
    if kind == "clause":
        f = draw(st.sampled_from(spec["filters"]))
        return draw(st.sampled_from(filter_clauses(draw, f, kinds, blank=False)))
    if kind == "not":
        return {"not": group_part(draw, spec, kinds, depth + 1, None)}
    parts = [
        group_part(draw, spec, kinds, depth + 1, kind) for _ in range(draw(st.sampled_from([2, 3])))
    ]
    if kind == "and":
        # (A column has one clause with each op in an `and`: which, of one part, is that part)
        ops = [(part["col"], part["op"]) if "col" in part else i for i, part in enumerate(parts)]
        parts = [part for i, part in enumerate(parts) if ops[i] not in ops[:i]]
    return {kind: parts} if len(parts) > 1 else parts[0]


@st.composite
def views(draw: Any, spec: dict) -> tuple[dict | None, list[str]]:
    """A view of a table, of its spec's filters and sortable columns: its query's clauses, with
    a group or two (of `or`, `and`, and `not`) at times."""
    kinds = {c["id"]: c["kind"] for c in spec["columns"]}
    clauses = [
        clause for f in some(draw, spec["filters"], 3) for clause in filter_clauses(draw, f, kinds)
    ]
    if spec["filters"]:
        for _ in range(draw(st.sampled_from([0, 1, 0, 2]))):
            # (Not an `and`, whose clauses would be the query's)
            kind = draw(st.sampled_from(["or", "not"]))
            clauses.append(group_part(draw, spec, kinds, 0, None, kind))
    sort = [
        ("-" if draw(st.booleans()) else "") + column
        for column in some(draw, sorted(spec["ranks"]), 3)
    ]
    return ({"and": clauses} if clauses or draw(st.booleans()) else None), sort


@pytest.mark.parametrize("backend", BACKENDS)
@hypothesis.settings(max_examples=200, deadline=None)
@hypothesis.given(data=st.data())
def test_random_views(engine: Callable[[GT], dict], backend: str, data: Any):
    gti, _ = data.draw(tables(backend))
    filter, sort = data.draw(views(render_parts(gti)[1]))
    assert_same_rows(engine, gti.i_view(filter=filter, sort=sort))


# The code a view's query compiles to, run on the data, keeps the rows of the view (of a table
# without row groups, which the code doesn't keep rows within)

CODE_BACKENDS = [
    ("polars", "polars"),
    ("pandas", "pandas"),
    ("narwhals", "pandas"),
    ("narwhals", "polars"),
    ("narwhals", "pyarrow"),
]


def run_code(code: str, data: Any) -> list[int]:
    """The rows (by their index in `data`) that code leaves of `data` (as `df`)."""
    if isinstance(data, pd.DataFrame):
        df = data
    elif isinstance(data, pl.DataFrame):
        df = data.with_row_index("__index")
    else:
        df = data.append_column("__index", pa.array(range(data.num_rows), pa.int64()))
    # (The code's last statement is the expression for the rows)
    module = ast.parse(code)
    *statements, last = module.body
    assert isinstance(last, ast.Expr)
    scope: dict[str, Any] = {"df": df}
    exec(compile(ast.Module(statements, type_ignores=[]), "<code>", "exec"), scope)
    result = eval(compile(ast.Expression(last.value), "<code>", "eval"), scope)
    if isinstance(result, pd.DataFrame):
        return result.index.tolist()
    return (
        [int(i) for i in result["__index"].to_pylist()]
        if isinstance(result, pa.Table)
        else (result["__index"].to_list())
    )


@pytest.mark.parametrize("code_backend, backend", CODE_BACKENDS)
@hypothesis.settings(max_examples=100, deadline=None)
@hypothesis.given(data=st.data())
def test_random_query_code(code_backend: str, backend: str, data: Any):
    gti, _ = data.draw(tables(backend, groups=False))
    filter, sort = data.draw(views(render_parts(gti)[1]))
    # (Text is matched as the column's values, not as the table shows them)
    if filter is not None:
        filter = {
            "and": [
                item
                for item in filter["and"]
                if all(leaf["op"] not in ("contains", "matches") for leaf in leaves([item]))
            ]
        }
    gti = gti.i_view(filter=filter, sort=sort)
    if backend == "pyarrow":
        # (Narwhals can't sort PyArrow's dictionaries)
        kinds = render_parts(gti)[1]["columns"]
        categories = {c["id"] for c in kinds if c["kind"] == "category"}
        hypothesis.assume(not any(key.lstrip("-") in categories for key in sort))
    code = query_code(gti, code_backend)
    assert run_code(code, gti._tbl_data) == view_rows(gti)


@pytest.mark.parametrize("backend", BACKENDS)
def test_a_facet_has_one_zero(engine: Callable[[GT], dict], backend: str):
    # (As JavaScript's `Map` has it, and the ranks: -0.0 is 0.0)
    gti = GTI(frame(backend, {"x": ("float", [0.0, -0.0, 1.0, -0.0])})).i_cols_filter(type="facet")
    for zero in [0.0, -0.0, 0]:
        filtered = gti.i_view(filter=query(("x", "in", [zero])))
        assert assert_same_rows(engine, filtered) == [0, 1, 3]
        assert run_code(query_code(filtered, "narwhals"), filtered._tbl_data) == [0, 1, 3]


# The code the runtime writes for a view (`toCode()`) is the code `query_code()` writes

LIBRARIES = ["polars", "pandas", "narwhals"]


def runtime_code(node_engine: Callable[[dict], dict], gt: GTI) -> dict:
    shown = node_engine(
        {"html": render_gti_html(gt.i_export("code"), runtime="none"), "code": True}
    )
    assert shown["state"] == "ready"
    assert shown["warnings"] == []
    return shown["code"]


@pytest.mark.parametrize("backend", BACKENDS)
@hypothesis.settings(max_examples=200, deadline=None)
@hypothesis.given(data=st.data())
def test_random_runtime_code(node_engine: Callable[[dict], dict], backend: str, data: Any):
    gti, _ = data.draw(tables(backend))
    filter, sort = data.draw(views(render_parts(gti)[1]))
    gti = gti.i_view(filter=filter, sort=sort)
    assert runtime_code(node_engine, gti) == {lib: query_code(gti, lib) for lib in LIBRARIES}


def test_runtime_code_drops_the_hidden_columns(node_engine: Callable[[dict], dict]):
    gti = (
        filtered()
        .i_cols_controls(columns=["few", "flag", "name"], hideable=True)
        .i_view(filter=query(("num", "gte", 2)), sort="name", hidden=["flag", "name"])
    )
    code = runtime_code(node_engine, gti)
    assert code == {lib: query_code(gti, lib) for lib in LIBRARIES}
    assert code["pandas"].endswith('.drop(columns=["name", "flag"])\n')


def test_runtime_code_of_other_values(node_engine: Callable[[dict], dict]):
    import datetime as dt

    data = pd.DataFrame(
        {
            "n": pd.array([1, None, 3], dtype="Int64"),
            "d": [dt.date(2020, 1, 2), None, dt.date(2021, 3, 4)],
            "t": [dt.datetime(2020, 1, 2, 3, 4, 5, 6), dt.datetime(2021, 1, 1), None],
            "s": ['say "hi"', "é\n", "x"],
            "x": [1e-5, 0.1, 1e16],
        }
    )
    gti = (
        GTI(data)
        .i_cols_filter(columns=["n", "x"], type="range")
        .i_cols_filter(columns=["d", "t", "s"], type="facet")
        .i_view(
            filter=query(
                ("x", "lte", 2.0**60),
                ("x", "gte", 1.5e-7),
                ("n", "gte", -0.0),
                ("t", "in", ["2021-01-01T00:00:00", "2020-01-02T03:04:05.000006"]),
                ("d", "in", ["2021-03-04", None]),
                ("s", "in", ["é\n", 'say "hi"']),
            ),
            sort=["-x", "s"],
        )
    )
    code = runtime_code(node_engine, gti)
    assert code == {lib: query_code(gti, lib) for lib in LIBRARIES}
    assert 'pl.col("x") >= 1.5e-07' in code["polars"]
    assert 'pl.col("x") <= 1152921504606846976' in code["polars"]
    assert "datetime.datetime(2020, 1, 2, 3, 4, 5, 6)" in code["polars"]
    assert '(df["n"] >= 0).fillna(False)' in code["pandas"]


def test_runtime_code_of_durations(node_engine: Callable[[dict], dict]):
    data = pd.DataFrame({"td": pd.to_timedelta([1, 2], unit="D")})
    gti = GTI(data).i_cols_filter(type="facet")
    values = render_parts(gti)[1]["filters"][0]["values"]
    code = runtime_code(node_engine, gti.i_view(filter=query(("td", "in", values[:1]))))
    assert code["polars"] == {"error": 'the filter on "td" can\'t be written as code'}
    # (Without a filter on them, the code is written)
    assert runtime_code(node_engine, gti)["polars"] == "import polars as pl\n\ndf\n"


# queries as text, in Python and in the runtime ----

# (Numbers as JavaScript holds them: doubles, and the integers it holds exactly)
NUMBERS = st.floats(allow_nan=False, allow_infinity=False) | st.integers(-(2**53), 2**53)
NAMES = (
    st.sampled_from(
        [
            *["a", "x_1", "and", "IN", "Name of town", "a`b", "", "1a", "é", "not", "Or", "is"],
            *["null", "top", "Bottom"],
        ]
    )
    | st.text()
)


def is_pattern(value: str) -> bool:
    """Whether a value is a pattern, as a query has it."""
    try:
        return check_pattern(value) == value
    except PatternError:
        return False


# (Without line breaks, which the text has as their escapes)
PATTERN_VALUES = st.sampled_from(PATTERNS) | st.builds(
    str.__add__,
    st.sampled_from(["", "(?i)"]),
    st.text("abcxy/\\.^$*+?()[]{}|-:,1dsW é😀", min_size=1, max_size=8),
).filter(is_pattern)


@st.composite
def clauses(draw: Any) -> dict:
    ops = ["contains", "in", "gte", "lte", "is_null", "matches", "gt", "lt", "top_n", "bottom_n"]
    op = draw(st.sampled_from(ops))
    if op == "is_null":
        return {"col": draw(NAMES), "op": op}
    if op in ("top_n", "bottom_n"):
        value = draw(st.integers(1, 2**53 - 1))
    elif op == "matches":
        value = draw(PATTERN_VALUES)
    elif op == "contains":
        value = draw(st.text())
    elif op == "in":
        values = st.text() | NUMBERS | st.booleans() | st.none()
        value = draw(st.lists(values, min_size=1, max_size=4))
    else:
        # (A date's a string: any string, as the text has it)
        dates = st.dates().map(dt.date.isoformat) | st.datetimes().map(dt.datetime.isoformat)
        value = draw(NUMBERS | dates | st.text())
    return {"col": draw(NAMES), "op": op, "value": value}


@st.composite
def parts(draw: Any, depth: int = 0, outer: str | None = None) -> dict:
    """A part of a query, as `parse_query()` makes it: a clause, or a group of a kind that's not
    the one it's in, of more than one part (or of one, a `not`)."""
    options = ["clause", "not", "or", "and"] if depth < 3 else ["clause"]
    kind = draw(st.sampled_from([option for option in options if option != outer]))
    if kind == "clause":
        return draw(clauses())
    if kind == "not":
        return {"not": draw(parts(depth + 1))}
    return {kind: draw(st.lists(parts(depth + 1, kind), min_size=2, max_size=3))}


QUERIES = st.lists(parts(outer="and"), min_size=1, max_size=4).map(lambda items: {"and": items})

# Pieces of queries, right and wrong, for texts that are nearly queries
PIECES = [
    *["a", "B_2", "`x y`", "`a``b`", "``", "`", "😀", "and", "AND", "contains", "in", "IN"],
    *["true", "False", "null", "(", ")", ",", ">=", "<=", ">", "=", "-", " ", "\t", "\n", "\xa0"],
    *['"x"', '"é\\n"', '"\\u00e9"', '"\\x"', '"', "1", "-0", "1.5e3", "01", ".5", "1e999"],
    *['"2015-06-05"', '"2015-06-05T09:30"', "2015-06-05"],
    *["or", "OR", "not", "Not", "not ", " or ", "(a >= 1 or b in (2))", "not a >= 1"],
    *["is", "IS", " is ", "is null", "is not null", "Is Not", "not is null", "`is`"],
    *[" not ", "not in", " NOT IN ", "not contains", "Not Matches", "x not", "not not"],
    *["matches", "MATCHES", " matches ", "/a/", "/[a-z]+/i", "/", "/(/", "/a\\/b/", "/x/g", "[/]"],
    *["/i", "\\", "(?i)", "{2}", "/^st\\./"],
    *["<", " > ", "> =", "a > 1", 'd < "2015-06-05"', "not > 1", "x not >", ">>", "<>"],
    *["top", "TOP", " bottom ", "top 3", "bottom 1", "x top 0", "top -1", "top 1.5"],
    *["9007199254740993", "not top 1", "x not top"],
]


@st.composite
def texts(draw: Any) -> str:
    """Text that's mostly a query, or nearly one."""
    kind = draw(st.sampled_from(["pieces", "query", "mutated", "any"]))
    if kind == "pieces":
        return "".join(draw(st.lists(st.sampled_from(PIECES), max_size=12)))
    if kind == "any":
        return draw(st.text(max_size=20))
    text = format_query(draw(QUERIES))
    if kind == "query":
        return text
    start = draw(st.integers(0, len(text)))
    end = draw(st.integers(start, min(len(text), start + 3)))
    return text[:start] + draw(st.sampled_from(["", *PIECES])) + text[end:]


def tagged(value: Any) -> Any:
    """A query's values, with booleans and numbers told apart (as `==` doesn't)."""
    if isinstance(value, bool):
        return ("bool", value)
    if isinstance(value, (int, float)):
        return ("number", float(value))
    if isinstance(value, list):
        return [tagged(item) for item in value]
    if isinstance(value, dict):
        return {key: tagged(item) for key, item in value.items()}
    return value


def python_parse(text: str) -> dict:
    """What `parse_query()` makes of text, as the engine has it."""
    try:
        return {"query": tagged(parse_query(text))}
    except ValueError as err:
        return {"syntaxError": str(err)}


@hypothesis.settings(max_examples=300)
@hypothesis.given(q=QUERIES)
def test_parse_query_reads_back_what_format_query_writes(q: dict):
    assert tagged(parse_query(format_query(q))) == tagged(q)


@hypothesis.settings(max_examples=500, deadline=None)
@hypothesis.given(text=texts())
def test_python_reads_queries_as_the_runtime_does(node_engine: Callable[[dict], dict], text: str):
    assert python_parse(text) == tagged(node_engine({"parse": text}))


@hypothesis.settings(max_examples=300, deadline=None)
@hypothesis.given(q=QUERIES)
def test_python_writes_queries_as_the_runtime_does(node_engine: Callable[[dict], dict], q: dict):
    assert format_query(q) == node_engine({"format": q})["text"]


def test_python_writes_lone_surrogates_as_the_runtime_does(node_engine: Callable[[dict], dict]):
    q = query(("\udc00", "contains", "a\ud800"))
    assert format_query(q) == node_engine({"format": q})["text"]
