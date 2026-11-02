"""Queries: checking them, and compiling them, which must keep the rows `<gt-table>` shows.

The differential tests run tables through the built runtime, under Node (with happy-dom: see
packages/gti/scripts/engine.mjs), and check that the rows it shows for a view are the rows that
`view_rows()` gets with Narwhals, on pandas, Polars, and PyArrow data. They're skipped without
Node and the package's dependencies (`npm ci` in packages/gti).
"""

from __future__ import annotations

import ast
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
from great_tables._gti._query import (
    _Tree,
    cell_text,
    check_query,
    fold,
    js_trim,
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


def view_of(gt: GT) -> dict:
    return render_parts(gt)[1]["view"]


# Frames of each backend, from columns of Python values: each is (kind, values), where the kind is
# "int", "float", "str", "bool", or "cat" (a category, of the values' levels as given, or of the
# values in order of appearance)


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
    return pd.Series(values, dtype=object)


def _polars_column(name: str, kind: str, values: list[Any]) -> Any:
    dtypes = {
        "int": pl.Int64,
        "float": pl.Float64,
        "bool": pl.Boolean,
        "str": pl.String,
        "cat": pl.Categorical,
    }
    return pl.Series(name, values, dtype=dtypes[kind])


def _arrow_column(kind: str, values: list[Any]) -> Any:
    types = {"int": pa.int64(), "float": pa.float64(), "bool": pa.bool_(), "str": pa.string()}
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
        ({"and": [{"col": "x", "op": "gt", "value": 1}]}, "clause 0 must be"),
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
        (query(("x", "gte", 1), ("x", "gte", 2)), "more than one 'gte' clause on column 'x'"),
        (query(("x", "in", [1]), ("x", "in", [2])), "more than one 'in' clause"),
    ],
)
def test_check_query_rejects(bad: Any, message: str):
    with pytest.raises(ValueError, match=message):
        check_query(bad)


def test_check_query_takes_a_range_with_both_bounds():
    both = query(("x", "gte", 1), ("x", "lte", 2))
    assert check_query(both) == both


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
    }


def test_the_default_view_is_the_table_as_it_is():
    assert view_of(GTI(DF)) == {"filter": None, "sort": []}
    assert view_of(filtered().i_view(sort="num").i_view()) == {"filter": None, "sort": []}
    # (A `GT` table's too)
    assert view_of(GT(DF).opt_interactive()) == {"filter": None, "sort": []}


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
        ({"filter": query(("name", "in", ["a"]))}, "which has a text filter"),
        ({"filter": query(("few", "contains", "x"))}, "which has a facet filter"),
        ({"filter": query(("flag", "in", ["True"]))}, "'True', which isn't a value of column"),
        ({"filter": query(("few", "in", ["z"]))}, "isn't a value of column 'few'"),
        ({"filter": query(("nope", "in", ["z"]))}, r"which has no filter.*`i_cols_filter\(\)`"),
        ({"sort": "nope"}, "can't be sorted by column 'nope'"),
    ],
)
def test_views_are_checked_against_the_table(view: dict, message: str):
    with pytest.raises(ValueError, match=message):
        view_of(filtered().i_view(**view))


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


# view_rows() ----


def test_view_rows_filters_and_sorts():
    gti = filtered().i_view(filter=query(("flag", "in", [True])), sort="-name")
    assert view_rows(gti) == [2, 0]
    assert view_rows(filtered()) == [0, 1, 2, 3]
    assert view_rows(filtered().i_view(sort="-num")) == [3, 1, 0, 2]


def test_view_rows_keeps_rows_in_their_groups():
    gti = GTI(DF, groupname_col="flag").i_cols_filter(columns="num").i_view(sort="-num")
    # (The groups, in the order they're first seen: True, then False)
    assert view_rows(gti) == [0, 2, 3, 1]
    gti = gti.i_view(filter=query(("num", "lte", 2)), sort="-num")
    assert view_rows(gti) == [0, 1]


def test_view_rows_of_a_table_with_merged_stub_cells():
    df = pd.DataFrame({"a": ["x", "x", "y"], "b": ["1", "2", "3"], "n": [3, 1, 2]})
    gti = GTI(df, rowname_col=["a", "b"]).i_view(sort="n")
    assert 'rowspan="2"' in render_parts(gti)[0]
    assert view_rows(gti) == [0, 1, 2]


# query_code() ----


def test_query_code():
    gti = filtered().i_view(
        filter=query(("few", "in", ["x", None]), ("num", "gte", 1.5)), sort=["-num", "name"]
    )
    assert query_code(gti, "polars") == (
        "import polars as pl\n\n"
        "df.filter(\n"
        '    pl.col("few").is_in(["x"]) | pl.col("few").is_null(),\n'
        '    (pl.col("num") >= 1.5) & pl.col("num").is_finite(),\n'
        ').sort(["num", "name"], descending=[True, False], nulls_last=True, maintain_order=True)\n'
    )
    assert query_code(gti, "pandas") == (
        "import numpy as np\n\n"
        "df[\n"
        '    (df["few"].isin(["x"]) | df["few"].isna())\n'
        '    & ((df["num"] >= 1.5) & np.isfinite(df["num"]))\n'
        '].sort_values(["num", "name"], ascending=[False, True], na_position="last", '
        'kind="stable")\n'
    )
    assert query_code(gti, "narwhals") == (
        "import narwhals as nw\n\n"
        "(\n"
        "    nw.from_native(df)\n"
        "    .filter(\n"
        '        nw.col("few").is_in(["x"]) | nw.col("few").is_null(),\n'
        '        (nw.col("num") >= 1.5) & nw.col("num").is_finite(),\n'
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


def test_query_code_needs_a_backend():
    with pytest.raises(ValueError, match='`backend=` must be "polars", "pandas", or "narwhals"'):
        query_code(GTI(DF), "duckdb")  # type: ignore[arg-type]


# the runtime ----


@pytest.fixture(scope="module")
def engine() -> Any:
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

    def run(gt: GT) -> dict:
        html = render_gti_html(gt, runtime="none")
        proc.stdin.write(json.dumps({"html": html}) + "\n")
        proc.stdin.flush()
        result = json.loads(proc.stdout.readline())
        assert "error" not in result, result.get("error")
        return result

    yield run
    proc.stdin.close()
    proc.wait(timeout=10)


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


# Tables of each backend whose views are compared: missing values, NaN, text, and range edges

EDGE_COLUMNS: dict[str, tuple[str, list[Any]]] = {
    "f": ("float", [1.5, None, math.nan, -math.inf, 2.0, math.inf, 1.5, 0.0]),
    "i": ("int", [3, 1, None, 2, 2, None, 1, 3]),
    "s": ("str", ["École", "ecole", "ÉCOLES", None, "Straße", "SS", "σίσυφος", "a\xa0b"]),
    "b": ("bool", [True, False, None, True, None, False, True, False]),
    "c": ("cat", ["lo", "hi", None, "lo", "mid", "hi", None, "lo"]),
}

EDGE_VIEWS: list[tuple[str, dict, Any]] = [
    ("missing facet", query(("i", "in", [None])), None),
    ("missing and a value", query(("i", "in", [2, None])), "i"),
    ("float facet", query(("f", "in", [1.5, 0])), None),
    ("float missing (not NaN)", query(("f", "in", [None])), None),
    ("bool facet", query(("b", "in", [False, None])), "-i"),
    ("category facet", query(("c", "in", ["mid", "lo"])), "-c"),
    ("category missing", query(("c", "in", [None])), None),
    ("range edges", query(("f", "gte", 1.5), ("f", "lte", 2)), None),
    ("range of ints", query(("i", "gte", 1.5)), "-i"),
    ("range without NaN or infinities", query(("f", "gte", -1e308)), None),
    ("upper bound", query(("f", "lte", 0)), None),
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
]


def edge_table(backend: str) -> GTI:
    return (
        GTI(frame(backend, EDGE_COLUMNS))
        .i_pagination(False)
        .i_cols_filter(columns=["f", "i"], type="range")
        .i_cols_filter(columns="s", type="text")
        .i_cols_filter(columns=["b", "c"], type="facet")
    )


def edge_table_for(backend: str, filter: dict | None) -> GTI:
    gti = edge_table(backend)
    # (A clause's column gets the filter that has its op)
    for clause in filter["and"] if filter is not None else []:
        col, op = clause["col"], clause["op"]
        if op == "in":
            gti = gti.i_cols_filter(columns=col, type="facet")
        elif op == "contains":
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
    assert rows(query(("i", "in", [2, None])), "i") == [3, 4, 2, 5]
    # (Descending, NaN is first, as it's after every number, ascending; but not if it's missing)
    descending = rows(None, "-f")
    assert descending == ([5, 4, 0, 6, 7, 3, 1, 2] if nan_missing else [2, 5, 4, 0, 6, 7, 3, 1])
    assert rows(None, "f") == [3, 7, 0, 6, 4, 5] + ([1, 2] if nan_missing else [2, 1])


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
VALUES: dict[str, list[Any]] = {
    "int": [-2, 0, 1, 3, None],
    "float": [-1.5, -0.0, 0.0, 1.0, 2.5, math.nan, math.inf, -math.inf, None],
    "str": [*TEXTS, None],
    "bool": [True, False, None],
    "cat": ["lo", "hi", "mid", None],
}


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
                "other": ["text"],
            }.get(_get_column_kind(data, name), ["facet", "text"])
            gti = gti.i_cols_filter(columns=name, type=draw(st.sampled_from(types)))
    return gti, columns


@st.composite
def views(draw: Any, spec: dict) -> tuple[dict | None, list[str]]:
    """A view of a table, of its spec's filters and sortable columns."""
    clauses = []
    for f in some(draw, spec["filters"], 3):
        col = f["column"]
        if f["type"] == "text":
            clauses.append({"col": col, "op": "contains", "value": draw(st.sampled_from(NEEDLES))})
        elif f["type"] == "facet":
            choices = [value for value in f["values"] if value is not None] + [None]
            value = draw(st.lists(st.sampled_from(choices), min_size=1, max_size=3, unique=True))
            clauses.append({"col": col, "op": "in", "value": value})
        else:
            numbers = [value for value in f["values"] if value is not None]
            bound = st.sampled_from(numbers) | st.floats(-3, 4) if numbers else st.floats(-3, 4)
            for op in draw(st.lists(st.sampled_from(["gte", "lte"]), min_size=1, unique=True)):
                clauses.append({"col": col, "op": op, "value": draw(bound)})
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
        filter = {"and": [c for c in filter["and"] if c["op"] != "contains"]}
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
