import re
import math
from typing import Any

import polars as pl
import pytest
from great_tables import GT
from great_tables._formats import _generate_data_vals, _process_number_stream


@pytest.mark.parametrize(
    "src",
    [
        "1 2 3",
        "1  2, 3",
        "a1 b2 c3",
        [1, 2, 3],
        {"x": [1, 2, 3]},
        {"any_name": [1, 2, 3]},
        pl.Series([1, 2, 3]),
    ],
)
def test_generate_data_vals(src: Any):
    assert _generate_data_vals(src) == [1, 2, 3]


@pytest.mark.xfail
def test_generate_data_vals_fails_ambig():
    with pytest.raises(ValueError):
        _generate_data_vals("a1b2c3")


def test_generate_data_vals_fails_novals():
    with pytest.raises(ValueError):
        _generate_data_vals("abc")


def test_fmt_nanoplot_pandas_nullable_float_with_missing_value():
    np = pytest.importorskip("numpy")
    pd = pytest.importorskip("pandas")

    values = [1.5, None, 3.0]
    gt_nullable = GT(pd.DataFrame({"x": pd.array(values, dtype="Float64")}), id="t")
    gt_numpy = GT(pd.DataFrame({"x": [1.5, np.nan, 3.0]}), id="t")

    html_nullable = gt_nullable.fmt_nanoplot("x").as_raw_html()

    # The missing value gets no plot, and the others share the scale as with a NumPy column
    assert html_nullable.count("<svg") == 2
    assert html_nullable == gt_numpy.fmt_nanoplot("x").as_raw_html()


def test_generate_data_vals_fails_date_strings():
    with pytest.raises(ValueError) as exc_info:
        _generate_data_vals(["2022-01-01"])

    assert "Only the x-axis of a nanoplot allows strings." in exc_info.value.args[0]


def test_generate_data_vals_fails_scalar_date_string():
    with pytest.raises(ValueError) as exc_info:
        _generate_data_vals("2022-01-01")

    assert exc_info.value.args[0] == "could not convert string to float: '2022-01-01'"


@pytest.mark.parametrize("nested_el", [[2, 3], (2, 3), "2 3", "abc"])
def test_generate_data_vals_fails_nested_list(nested_el):
    with pytest.raises(ValueError) as exc_info:
        _generate_data_vals([1, nested_el])

    assert f"Value received: {nested_el}" in exc_info.value.args[0]


@pytest.mark.xfail
def test_nanoplot_ref_line_area():
    # TODO: add this test
    assert False


@pytest.mark.parametrize(
    "src,dst",
    [
        ("1 2 3", [1, 2, 3]),
        ("1,   2,3, 4.5", [1, 2, 3, 4.5]),
        ("1.1; 2;3;   4.5", [1.1, 2, 3, 4.5]),
        (" 1.1, 2 3;   4.5 5 ", [1.1, 2, 3, 4.5, 5]),
        (" 1.342e12, 2.e-2 3,  4.55634 -5.23 ", [1.342e12, 2.0e-2, 3, 4.55634, -5.23]),
        (" +1.342e12, +2.E-2 +3,  4.55634 -5.23 ", [1.342e12, 2.0e-2, 3, 4.55634, -5.23]),
        ("1 2 3 nan 5", [1, 2, 3, float("nan"), 5]),
        (
            "1 2 3 NaN NaN NaN 7 8 9 10 11 12",
            [1, 2, 3, float("nan"), float("nan"), float("nan"), 7, 8, 9, 10, 11, 12],
        ),
        ("1 NA 3", [1, float("nan"), 3]),
        ("[1, 2, 3]", [1, 2, 3]),
        ("[1,2.5;-3]", [1, 2.5, -3]),
        (" [ 1 NA 3 ] ", [1, float("nan"), 3]),
        ("na, 2; NA", [float("nan"), 2, float("nan")]),
    ],
)
def test_process_number_stream(src: str, dst: list[float]):
    res = _process_number_stream(data_vals=src)
    assert len(res) == len(dst)
    for r, d in zip(res, dst):
        if math.isnan(d):
            assert math.isnan(r)
        else:
            assert r == d


def test_generate_data_vals_date_list_is_x_axis():
    # List of date strings with is_x_axis=True triggers ISO date parsing
    result = _generate_data_vals(["2022-01-01", "2022-01-02", "2022-01-03"], is_x_axis=True)
    assert isinstance(result, list)
    assert len(result) == 3
    # Should be ordinal integers
    assert all(isinstance(v, int) for v in result)


def test_generate_data_vals_dict_xy_mismatched_lengths():
    # Dict with 'x' and 'y' of different lengths raises ValueError
    with pytest.raises(ValueError, match="lengths"):
        _generate_data_vals({"x": [1, 2], "y": [1, 2, 3]})


def test_generate_data_vals_dict_wrong_keys():
    # Dict without 'x' and 'y' keys raises ValueError
    with pytest.raises(ValueError, match="'x' and 'y' keys"):
        _generate_data_vals({"a": [1, 2], "b": [3, 4]})


def test_generate_data_vals_unsupported_type():
    # Unsupported type raises NotImplementedError
    with pytest.raises(NotImplementedError):
        _generate_data_vals(object())


def _y_axis_bounds(html: str) -> list[tuple[float, float]]:
    """The (max, min) values labeled on the y-axis guide of each nanoplot."""

    import re

    labels = re.findall(
        r'class="y-axis-line">.*?<text[^>]*>([^<]*)</text><text[^>]*>([^<]*)</text>', html
    )

    return [(float(max_label), float(min_label)) for max_label, min_label in labels]


def test_fmt_nanoplot_na_in_number_stream():
    gt = GT(pl.DataFrame({"v": ["1 NA 3", "NA 5 NA"]})).fmt_nanoplot(columns="v")

    # The second plot has a single value, so its scale is centered on it
    assert _y_axis_bounds(gt.as_raw_html()) == [(3, 1), (6, 4)]


@pytest.mark.parametrize(
    "vals",
    [
        pytest.param(["NA 5 1", "2 3 40"], id="na_in_stream"),
        pytest.param(["nan 5 1", "2 3 40"], id="nan_in_stream"),
        pytest.param([[None, 5, 1], [2, 3, 40]], id="none_in_list"),
        pytest.param(["5 1", "2 3 40", None], id="missing_cell"),
    ],
)
def test_fmt_nanoplot_autoscale_ignores_missing_values(vals: list[Any]):
    gt = GT(pl.DataFrame({"v": vals})).fmt_nanoplot(columns="v", autoscale=True)

    # Every nanoplot shares the scale of all of the values, from 1 to 40
    assert set(_y_axis_bounds(gt.as_raw_html())) == {(40, 1)}


def test_fmt_nanoplot_autoscale_all_missing():
    gt = GT(pl.DataFrame({"v": [[None, None], None]})).fmt_nanoplot(columns="v", autoscale=True)

    assert "<svg" not in gt.as_raw_html()


@pytest.mark.parametrize("plot_type", ["line", "bar"])
def test_fmt_nanoplot_na_in_number_stream_with_ref_keywords(plot_type: str):
    gt = GT(pl.DataFrame({"v": ["1 NA 2 6", "NA 4 8"]})).fmt_nanoplot(
        columns="v", plot_type=plot_type, reference_line="mean", reference_area=["min", "max"]
    )

    import re

    ref_line_labels = re.findall(r'<g class="ref-line">.*?>([^<>]*)</text></g>', gt.as_raw_html())

    # The means of the non-missing values in each row are 3 and 6
    assert [float(label) for label in ref_line_labels] == [3, 6]


@pytest.mark.parametrize("plot_type", ["line", "bar", "boxplot"])
@pytest.mark.parametrize("keyword,dst", [("first", [2, 7]), ("last", [4, 6])])
def test_fmt_nanoplot_ref_keywords_first_last(plot_type: str, keyword: str, dst: list[float]):
    gt = GT(pl.DataFrame({"v": ["2 5 3 9 4", "7 1 6"]})).fmt_nanoplot(
        columns="v", plot_type=plot_type, reference_line=keyword, reference_area=["first", "last"]
    )

    import re

    ref_line_labels = re.findall(r'<g class="ref-line">.*?>([^<>]*)</text></g>', gt.as_raw_html())

    assert [float(label) for label in ref_line_labels] == dst


@pytest.mark.parametrize("plot_type", ["line", "bar"])
def test_fmt_nanoplot_bracketed_number_stream(plot_type: str):
    def render(vals: list[str]) -> str:
        gt = GT(pl.DataFrame({"v": vals}), id="t").fmt_nanoplot(columns="v", plot_type=plot_type)
        return gt.as_raw_html()

    assert render(["[1, 5, 3]", "[2; 4]"]) == render(["1 5 3", "2 4"])


@pytest.mark.parametrize("dtype", ["int64", "int32", "float32"])
def test_generate_data_vals_numpy_scalars(dtype: str):
    np = pytest.importorskip("numpy")

    scalar = _generate_data_vals(np.dtype(dtype).type(3))
    values = _generate_data_vals([np.dtype(dtype).type(1), None, np.dtype(dtype).type(3)])

    assert scalar == 3 and type(scalar) in (int, float)
    assert values == [1, None, 3] and all(type(v) in (int, float) for v in values if v is not None)


@pytest.mark.parametrize("dtype", ["int64", "int32", "float32"])
def test_fmt_nanoplot_pandas_numpy_columns(dtype: str):
    pd = pytest.importorskip("pandas")

    pl_dtypes = {"int64": pl.Int64, "int32": pl.Int32, "float32": pl.Float32}
    values = [1, 2, 3]
    gt_pandas = GT(pd.DataFrame({"x": pd.Series(values, dtype=dtype)}), id="t").fmt_nanoplot("x")
    gt_polars = GT(
        pl.DataFrame({"x": pl.Series(values, dtype=pl_dtypes[dtype])}), id="t"
    ).fmt_nanoplot("x")

    # The nanoplots of a pandas column match those of a Polars column of the same dtype
    assert gt_pandas.as_raw_html().count("<svg") == 3
    assert gt_pandas.as_raw_html() == gt_polars.as_raw_html()

    
def _numeric_column(kind: str):
    import pyarrow as pa
    from decimal import Decimal

    vals = ["1.5", "2.5", "4.0"]
    if kind == "polars_float":
        return pl.DataFrame({"x": [float(v) for v in vals]})
    if kind == "pyarrow_float64":
        return pa.table({"x": pa.array([float(v) for v in vals])})
    if kind == "polars_decimal":
        return pl.DataFrame({"x": [Decimal(v) for v in vals]}, schema={"x": pl.Decimal(10, 2)})
    if kind == "pyarrow_decimal":
        return pa.table({"x": pa.array([Decimal(v) for v in vals], type=pa.decimal128(10, 2))})
    raise ValueError(kind)


@pytest.mark.parametrize("plot_type", ["line", "bar"])
@pytest.mark.parametrize("kind", ["pyarrow_float64", "polars_decimal", "pyarrow_decimal"])
def test_fmt_nanoplot_numeric_column_dtypes_match_polars_float(kind: str, plot_type: str):
    pytest.importorskip("pyarrow")

    def draw(tbl):
        # the alignment is fixed: it is inferred from the dtype, which is not under test here
        gt = GT(tbl).fmt_nanoplot("x", plot_type=plot_type).cols_align("right", columns="x")
        html = gt.as_raw_html()
        # the table id and the ids of the SVG elements differ between tables
        return re.sub(r'id="[^"]*"|#[a-z]+\w*', "", html)

    assert draw(_numeric_column(kind)) == draw(_numeric_column("polars_float"))
