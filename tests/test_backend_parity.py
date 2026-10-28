"""Every scenario renders the same output from every frame constructor."""

from __future__ import annotations

import re
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal
from typing import Any, Callable, TypeVar, cast
from unittest.mock import ANY

import polars as pl
import pyarrow as pa
import pyarrow.compute as pc
import pytest
from syrupy.assertion import SnapshotAssertion

from great_tables import GT, col_bin, loc, style
from great_tables._tbl_data import DataFrameLike
from great_tables._utils_render_html import create_body_component_h
from tests.utils import (
    DataFrameConstructor,
    DataLike,
    Divergent,
    Render,
    assert_parity,
    cast_to_categorical,
    native_backend,
)

T = TypeVar("T")

ISSUES = "https://github.com/posit-dev/great-tables/issues"
NUMBER_LIKE_TEXT = f"{ISSUES}/1023"
OBJECT_ALIGNED_RIGHT = f"{ISSUES}/1024"
NULL_IN_ROW_MASK = f"{ISSUES}/1047"
DURATION_SPELLING = f"inherited from native data (pd.Timedelta spelling), {ISSUES}/1048"
INT_UPCAST = "inherited from native data (pandas stores ints with a missing value as float64)"

# every pandas constructor keeps times, decimals and lists in object columns
PANDAS_OBJECT_ALIGNED_RIGHT = Divergent(
    pandas_constructor=OBJECT_ALIGNED_RIGHT,
    pandas_nullable_constructor=OBJECT_ALIGNED_RIGHT,
    pandas_pyarrow_constructor=OBJECT_ALIGNED_RIGHT,
)

# every column has a missing value, and floats are non-integral because the pandas nullable and
# pyarrow-backed constructors turn whole floats into ints
FLOATS = [1234.5678, None, -0.25]
TEXT = ["apple", None, "cherry"]


def _native(df: DataFrameLike, *, pandas: T, polars: T, pyarrow: T) -> T:
    return {"pandas": pandas, "polars": polars, "pyarrow": pyarrow}[native_backend(df)]


def _body_html(gt: GT) -> str:
    return create_body_component_h(gt._build_data("html"))


def _body_renderer(
    data: DataLike, build: Callable[[GT], GT] = lambda gt: gt, **gt_kwargs: Any
) -> Render:
    return lambda constructor: _body_html(build(GT(constructor(data), id="parity", **gt_kwargs)))


# Formatting ------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "values, fmt, divergent",
    [
        pytest.param(FLOATS, GT.fmt_number, {}, id="fmt_number"),
        pytest.param(FLOATS, GT.fmt_integer, {}, id="fmt_integer"),
        pytest.param(FLOATS, GT.fmt_percent, {}, id="fmt_percent"),
        pytest.param(FLOATS, GT.fmt_currency, {}, id="fmt_currency"),
        pytest.param(FLOATS, GT.fmt_scientific, {}, id="fmt_scientific"),
        pytest.param([date(2024, 1, 1), None, date(2024, 2, 29)], GT.fmt_date, {}, id="fmt_date"),
        pytest.param(
            [time(12, 30), None, time(8, 5, 30)],
            GT.fmt_time,
            PANDAS_OBJECT_ALIGNED_RIGHT,
            id="fmt_time",
        ),
        pytest.param(
            [datetime(2024, 1, 1, 12, 30), None, datetime(2024, 2, 29)],
            GT.fmt_datetime,
            {},
            id="fmt_datetime",
        ),
        pytest.param(
            [timedelta(hours=1), None, timedelta(days=2, minutes=5)],
            GT.fmt_duration,
            {},
            id="fmt_duration",
        ),
        pytest.param(
            [True, None, False],
            GT.fmt_tf,
            Divergent(pandas_constructor=OBJECT_ALIGNED_RIGHT),
            id="fmt_tf",
        ),
        pytest.param(["**bold**", None, "*italic*"], GT.fmt_markdown, {}, id="fmt_markdown"),
        pytest.param(FLOATS, GT.fmt_nanoplot, {}, id="fmt_nanoplot-float"),
        pytest.param(
            [[1.5, None, -0.25], None, [3.75]],
            GT.fmt_nanoplot,
            PANDAS_OBJECT_ALIGNED_RIGHT,
            id="fmt_nanoplot-list",
        ),
    ],
)
def test_fmt(
    snapshot: SnapshotAssertion,
    all_frame_constructors: list[DataFrameConstructor],
    values: list[Any],
    fmt: Callable[..., GT],
    divergent: Divergent,
):
    render = _body_renderer({"x": values}, lambda gt: fmt(gt, columns="x"))
    assert_parity(snapshot, all_frame_constructors, render, divergent)


# Unformatted -----------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "values, divergent",
    [
        pytest.param([1, 2, None], Divergent(pandas_constructor=INT_UPCAST), id="int"),
        pytest.param([1.5, -0.25, None], {}, id="float"),
        pytest.param(["a", "b", None], {}, id="str"),
        pytest.param(
            [True, False, None], Divergent(pandas_constructor=OBJECT_ALIGNED_RIGHT), id="bool"
        ),
        pytest.param([date(2024, 1, 1), date(2024, 2, 29), None], {}, id="date"),
        pytest.param(
            [datetime(2024, 1, 1, 12, 30), datetime(2024, 2, 29), None], {}, id="datetime"
        ),
        pytest.param(
            [
                datetime(2024, 1, 1, 12, 30, tzinfo=timezone.utc),
                datetime(2024, 2, 29, tzinfo=timezone.utc),
                None,
            ],
            {},
            id="datetime_tz",
        ),
        pytest.param(
            [timedelta(hours=1), timedelta(days=2, minutes=5), None],
            Divergent(
                pandas_constructor=DURATION_SPELLING,
                pandas_nullable_constructor=DURATION_SPELLING,
                pandas_pyarrow_constructor=DURATION_SPELLING,
            ),
            id="duration",
        ),
        pytest.param(
            [Decimal("1.50"), Decimal("-2.25"), None], PANDAS_OBJECT_ALIGNED_RIGHT, id="decimal"
        ),
        pytest.param([[1, 2], [3], None], PANDAS_OBJECT_ALIGNED_RIGHT, id="list"),
    ],
)
def test_unformatted(
    snapshot: SnapshotAssertion,
    all_frame_constructors: list[DataFrameConstructor],
    values: list[Any],
    divergent: Divergent,
):
    # the body also pins automatic alignment, so these double as the `cols_align` auto scenarios
    assert_parity(snapshot, all_frame_constructors, _body_renderer({"x": values}), divergent)


# Substitution and text -------------------------------------------------------------------------


def test_sub_missing(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"x": FLOATS, "s": TEXT}, lambda gt: gt.sub_missing(missing_text="--"))
    assert_parity(snapshot, all_frame_constructors, render)


def test_sub_zero(snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]):
    render = _body_renderer({"x": [0.0, None, 1.5]}, lambda gt: gt.sub_zero())
    assert_parity(snapshot, all_frame_constructors, render)


def test_sub_values(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer(
        {"x": FLOATS, "s": TEXT},
        lambda gt: gt.sub_values(values=[-0.25], replacement="quarter").sub_values(
            columns="s", pattern="^ch", replacement="replaced"
        ),
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_text_transform(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"s": TEXT}, lambda gt: gt.text_transform(loc.body(), fn=str.upper))
    assert_parity(snapshot, all_frame_constructors, render)


def test_text_replace(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"s": TEXT}, lambda gt: gt.text_replace("e", "E", locations=loc.body()))
    assert_parity(snapshot, all_frame_constructors, render)


def test_text_case_when(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer(
        {"s": TEXT},
        lambda gt: gt.text_case_when(
            (lambda text: text.startswith("a"), "starts with a"),
            default="other",
            locations=loc.body(),
        ),
    )
    assert_parity(snapshot, all_frame_constructors, render)


# Color -----------------------------------------------------------------------------------------


def test_data_color_numeric(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"x": FLOATS}, lambda gt: gt.data_color(palette=["white", "red"]))
    assert_parity(snapshot, all_frame_constructors, render)


def test_data_color_bin(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    fn = col_bin(palette=["white", "red"], bins=[-1, 0, 2000])
    render = _body_renderer({"x": FLOATS}, lambda gt: gt.data_color(fn=fn))
    assert_parity(snapshot, all_frame_constructors, render)


def test_data_color_factor(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"s": TEXT}, lambda gt: gt.data_color(palette=["white", "red"]))
    assert_parity(snapshot, all_frame_constructors, render)


def test_data_color_ordered_levels(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    # first-appearance levels aren't alphabetical, so the colors show which order was used
    data = {"s": ["low", None, "high", "mid"]}

    def render(constructor: DataFrameConstructor) -> str:
        df = cast_to_categorical(constructor(data), "s", ordered=True)
        return _body_html(GT(df, id="parity").data_color(palette=["white", "orange", "red"]))

    assert_parity(snapshot, all_frame_constructors, render)


# Stub and groups -------------------------------------------------------------------------------


def test_rowname_col(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"row": TEXT, "x": FLOATS}, rowname_col="row")
    assert_parity(snapshot, all_frame_constructors, render)


def test_groupname_col(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"g": ["b", "a", "b"], "x": FLOATS}, groupname_col="g")
    assert_parity(snapshot, all_frame_constructors, render)


def test_groupname_col_with_null_key(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"g": ["b", None, "b"], "x": FLOATS}, groupname_col="g")
    assert_parity(snapshot, all_frame_constructors, render)


def test_row_group_order(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer(
        {"g": ["b", "a", "b"], "x": FLOATS},
        lambda gt: gt.row_group_order(["a", "b"]),
        groupname_col="g",
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_tab_stub_indent(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer(
        {"row": TEXT, "x": FLOATS},
        lambda gt: gt.tab_stub_indent(rows=[1, 2], indent=2),
        rowname_col="row",
    )
    assert_parity(snapshot, all_frame_constructors, render)


# Columns ---------------------------------------------------------------------------------------


def test_cols_merge(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer(
        {"a": TEXT, "b": ["x", "y", None]},
        lambda gt: gt.cols_merge(columns=["a", "b"], pattern="{0}<< ({1})>>"),
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_cols_merge_range(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer(
        {"lo": [1.5, None, -0.25, 2.5], "hi": [2.5, 3.5, None, 2.5]},
        lambda gt: gt.cols_merge_range(col_begin="lo", col_end="hi"),
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_cols_merge_uncert(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer(
        {"v": [1.5, None, -0.25], "u": [0.25, 0.5, None]},
        lambda gt: gt.cols_merge_uncert(col_val="v", col_uncert="u"),
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_cols_merge_n_pct(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    # the formatters keep pandas' float64 upcast of the int column out of the merged text
    render = _body_renderer(
        {"n": [10, None, 0, 5], "pct": [0.255, 0.5, None, 0.0]},
        lambda gt: (
            gt.fmt_integer(columns="n")
            .fmt_percent(columns="pct")
            .cols_merge_n_pct(col_n="n", col_pct="pct")
        ),
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_cols_align_number_like_text(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"s": ["1.5", None, "2024-01-01"]})
    divergent = Divergent(
        pandas_constructor=NUMBER_LIKE_TEXT, pandas_pyarrow_constructor=NUMBER_LIKE_TEXT
    )
    assert_parity(snapshot, all_frame_constructors, render, divergent)


# Selection -------------------------------------------------------------------------------------


def _highlight_rows(rows: Any) -> Callable[[GT], GT]:
    return lambda gt: gt.tab_style(style.fill("red"), loc.body(columns="x", rows=rows))


def test_rows_by_index(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _body_renderer({"x": FLOATS}, _highlight_rows([0, 2]))
    assert_parity(snapshot, all_frame_constructors, render)


@pytest.mark.parametrize(
    "values, polars_rows, divergent",
    [
        pytest.param([1.5, 0.5, 3.5], pl.col("x") > 2, {}, id="no-nulls"),
        pytest.param(
            [1.5, None, 3.5],
            pl.col("x") > 2,
            Divergent(
                pandas_nullable_constructor=NULL_IN_ROW_MASK,
                pandas_pyarrow_constructor=NULL_IN_ROW_MASK,
                pyarrow_table_constructor=NULL_IN_ROW_MASK,
            ),
            id="nulls-polars-expr",
        ),
        pytest.param(
            [1.5, None, 3.5],
            lambda df: df["x"] > 2,
            Divergent(
                pandas_nullable_constructor=NULL_IN_ROW_MASK,
                pandas_pyarrow_constructor=NULL_IN_ROW_MASK,
                polars_constructor=NULL_IN_ROW_MASK,
                pyarrow_table_constructor=NULL_IN_ROW_MASK,
            ),
            id="nulls-polars-callable",
        ),
    ],
)
def test_rows_by_mask(
    snapshot: SnapshotAssertion,
    all_frame_constructors: list[DataFrameConstructor],
    values: list[Any],
    polars_rows: Any,
    divergent: Divergent,
):
    def render(constructor: DataFrameConstructor) -> str:
        df = constructor({"x": values})
        rows = _native(
            df,
            pandas=lambda df: df["x"] > 2,
            polars=polars_rows,
            pyarrow=lambda tbl: pc.greater(tbl["x"], 2),
        )
        return _body_html(GT(df, id="parity").pipe(_highlight_rows(rows)))

    assert_parity(snapshot, all_frame_constructors, render, divergent)


# Summary rows ----------------------------------------------------------------------------------


def _sum_and_max_fns(df: DataFrameLike) -> dict[str, Any]:
    return _native(
        df,
        pandas={"Sum": lambda df: df[["x"]].sum(), "Max": lambda df: df[["x"]].max()},
        polars={"Sum": pl.col("x").sum(), "Max": pl.col("x").max()},
        pyarrow={
            "Sum": lambda tbl: pa.table({"x": [pc.sum(tbl["x"]).as_py()]}),
            "Max": lambda tbl: pa.table({"x": [pc.max(tbl["x"]).as_py()]}),
        },
    )


def test_grand_summary_rows(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    def render(constructor: DataFrameConstructor) -> str:
        df = constructor({"x": FLOATS})
        return _body_html(GT(df, id="parity").grand_summary_rows(fns=_sum_and_max_fns(df)))

    assert_parity(snapshot, all_frame_constructors, render)


def test_summary_rows(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    # no missing group key: summary_rows() raises on it on every backend (#1049)
    data = {"g": ["b", "a", "b", "a"], "x": [*FLOATS, 2.5]}

    def render(constructor: DataFrameConstructor) -> str:
        df = constructor(data)
        gt = GT(df, groupname_col="g", id="parity")
        return _body_html(gt.summary_rows(fns=_sum_and_max_fns(df)))

    assert_parity(snapshot, all_frame_constructors, render)


# Outputs ---------------------------------------------------------------------------------------


def test_as_latex(snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]):
    data = {"g": ["b", "a", "b"], "row": TEXT, "x": FLOATS, "s": TEXT}

    def render(constructor: DataFrameConstructor) -> str:
        gt = (
            GT(constructor(data), rowname_col="row", groupname_col="g", id="parity")
            .tab_header(title="Parity", subtitle="as_latex()")
            .tab_spanner(label="values", columns=["x", "s"])
            .fmt_number(columns="x")
            .sub_missing()
        )
        return gt.as_latex()

    assert_parity(snapshot, all_frame_constructors, render)


def test_opt_interactive(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    data = {"x": FLOATS, "s": TEXT}

    def render(constructor: DataFrameConstructor) -> str:
        html = GT(constructor(data), id="parity").opt_interactive().as_raw_html()
        # the rest of the page is the bundled reactable JavaScript (about 400 kB)
        props = re.search(r"const _props = (\{.*?\});\n", html, re.DOTALL)
        assert props, "no props JSON in the interactive HTML"
        return props.group(1)

    assert_parity(snapshot, all_frame_constructors, render)


# assert_parity ---------------------------------------------------------------------------------


def _constructor_named(name: str) -> DataFrameConstructor:
    def constructor(data: DataLike) -> DataFrameLike:
        raise NotImplementedError

    constructor.__name__ = name
    return constructor


@pytest.mark.parametrize(
    "pandas_output, polars_output, divergent, error",
    [
        pytest.param("a", "b", {}, "differ from pandas_constructor", id="mismatch"),
        pytest.param(KeyError("x"), KeyError("x"), {}, "<raised KeyError", id="shared-crash"),
        pytest.param(
            "a",
            "a",
            Divergent(polars_constructor="polars renders b instead of a"),
            "now matches",
            id="stale-divergent",
        ),
        pytest.param(
            "a",
            "b",
            Divergent(
                pandas_constructor="pandas renders a instead of b",
                polars_constructor="polars renders b instead of a",
            ),
            "every constructor",
            id="all-divergent",
        ),
        pytest.param(
            "a",
            "a",
            {"polars_constuctor": "polars renders b instead of a"},
            "unknown constructors",
            id="misspelled-divergent",
        ),
    ],
)
def test_assert_parity_rejects(
    pandas_output: str | Exception,
    polars_output: str | Exception,
    divergent: Divergent,
    error: str,
):
    outputs = {"pandas_constructor": pandas_output, "polars_constructor": polars_output}

    def render(constructor: DataFrameConstructor) -> str:
        output = outputs[constructor.__name__]
        if isinstance(output, Exception):
            raise output
        return output

    constructors = [_constructor_named(name) for name in outputs]
    any_snapshot = cast(SnapshotAssertion, lambda name: ANY)
    with pytest.raises(AssertionError, match=error):
        assert_parity(any_snapshot, constructors, render, divergent)
