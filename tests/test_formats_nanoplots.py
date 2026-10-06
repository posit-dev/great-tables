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
