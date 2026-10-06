from typing import Any

import polars as pl
import pytest

from great_tables import GT, nanoplot_options
from great_tables._utils_nanoplots import _generate_nanoplot

from tests.utils import assert_rendered_body


# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------

# Simple gap in the middle
Y_MIDDLE_GAP = [
    1.0,
    2.0,
    3.0,
    4.0,
    float("nan"),
    float("nan"),
    float("nan"),
    8.0,
    9.0,
    10.0,
    11.0,
    12.0,
]

# Gap at the start
Y_START_GAP = [float("nan"), float("nan"), 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

# Gap at the end
Y_END_GAP = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, float("nan"), float("nan")]

# Multiple gaps
Y_MULTI_GAP = [
    1.0,
    2.0,
    float("nan"),
    4.0,
    5.0,
    float("nan"),
    float("nan"),
    8.0,
    9.0,
    float("nan"),
    11.0,
    12.0,
]

# Alternating values and gaps
Y_ALTERNATING = [
    1.0,
    float("nan"),
    3.0,
    float("nan"),
    5.0,
    float("nan"),
    7.0,
    float("nan"),
    9.0,
    float("nan"),
    11.0,
    float("nan"),
]

# Negative values with gaps
Y_NEGATIVE_GAP = [-3.0, -1.0, float("nan"), 2.0, 4.0, float("nan"), -2.0, 1.0, 3.0, 5.0]


# ---------------------------------------------------------------------------
# Line plot snapshots — curved
# ---------------------------------------------------------------------------


def test_snap_line_gap_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_start(snapshot):
    result = _generate_nanoplot(y_vals=Y_START_GAP, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_end(snapshot):
    result = _generate_nanoplot(y_vals=Y_END_GAP, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_multiple(snapshot):
    result = _generate_nanoplot(y_vals=Y_MULTI_GAP, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_alternating(snapshot):
    result = _generate_nanoplot(y_vals=Y_ALTERNATING, missing_vals="gap")
    assert snapshot == result


def test_snap_line_gap_negative(snapshot):
    result = _generate_nanoplot(y_vals=Y_NEGATIVE_GAP, missing_vals="gap")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Line plot snapshots — straight
# ---------------------------------------------------------------------------


def test_snap_line_straight_gap_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="gap", data_line_type="straight")
    assert snapshot == result


def test_snap_line_straight_gap_multiple(snapshot):
    result = _generate_nanoplot(y_vals=Y_MULTI_GAP, missing_vals="gap", data_line_type="straight")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Line plot snapshots — marker
# ---------------------------------------------------------------------------


def test_snap_line_marker_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="marker")
    assert snapshot == result


def test_snap_line_marker_alternating(snapshot):
    result = _generate_nanoplot(y_vals=Y_ALTERNATING, missing_vals="marker")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Line plot snapshots — zero
# ---------------------------------------------------------------------------


def test_snap_line_zero_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="zero")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Line plot snapshots — remove
# ---------------------------------------------------------------------------


def test_snap_line_remove_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, missing_vals="remove")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Bar plot snapshots
# ---------------------------------------------------------------------------


def test_snap_bar_gap_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, plot_type="bar", missing_vals="gap")
    assert snapshot == result


def test_snap_bar_gap_multiple(snapshot):
    result = _generate_nanoplot(y_vals=Y_MULTI_GAP, plot_type="bar", missing_vals="gap")
    assert snapshot == result


def test_snap_bar_gap_alternating(snapshot):
    result = _generate_nanoplot(y_vals=Y_ALTERNATING, plot_type="bar", missing_vals="gap")
    assert snapshot == result


def test_snap_bar_gap_negative(snapshot):
    result = _generate_nanoplot(y_vals=Y_NEGATIVE_GAP, plot_type="bar", missing_vals="gap")
    assert snapshot == result


def test_snap_bar_marker_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, plot_type="bar", missing_vals="marker")
    assert snapshot == result


def test_snap_bar_zero_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, plot_type="bar", missing_vals="zero")
    assert snapshot == result


def test_snap_bar_remove_middle(snapshot):
    result = _generate_nanoplot(y_vals=Y_MIDDLE_GAP, plot_type="bar", missing_vals="remove")
    assert snapshot == result


# ---------------------------------------------------------------------------
# Snapshots covering each layer and option of multi-value plots
# ---------------------------------------------------------------------------

Y_MIXED = [-5.3, 6.3, -2.3, 0, 2.3, 6.7, 14.2, 0, 2.3, 13.3]
Y_INT = [1, 5, 3, 8, 2, 9, 4]


@pytest.mark.parametrize(
    "kwargs",
    [
        pytest.param(dict(y_vals=Y_MIXED, y_ref_line=0), id="line_ref_line_num"),
        pytest.param(dict(y_vals=Y_INT, y_ref_line="mean"), id="line_ref_line_keyword"),
        pytest.param(dict(y_vals=Y_MIXED, y_ref_area=["min", "median"]), id="line_ref_area"),
        pytest.param(
            dict(y_vals=Y_MIXED, y_ref_line="q1", y_ref_area=[2.3, "max"]),
            id="line_ref_line_and_area",
        ),
        pytest.param(dict(y_vals=Y_MIXED, plot_type="bar", y_ref_line=0), id="bar_ref_line"),
        pytest.param(
            dict(y_vals=Y_INT, plot_type="bar", y_ref_line=4, y_ref_area=[3, 5]),
            id="bar_ref_line_and_area",
        ),
        pytest.param(
            dict(y_vals=Y_MIXED, plot_type="bar", y_ref_area=["q1", "q3"]), id="bar_ref_area"
        ),
        pytest.param(
            dict(y_vals=[-5.3, 6.3, -2.3, 0, 2.3], x_vals=[1.2, 3.4, 4.2, 5.0, 5.8]),
            id="line_x_vals",
        ),
        pytest.param(
            dict(y_vals=[1, 4, 2, 8], x_vals=[10, 2, 7, 4], expand_x=[0, 20], expand_y=[-10, 30]),
            id="line_x_vals_expand",
        ),
        pytest.param(dict(y_vals=Y_INT, expand_y=[-20, 30]), id="line_expand_y"),
        pytest.param(dict(y_vals=[3, 3, 3, 3]), id="line_invariant"),
        pytest.param(dict(y_vals=[5]), id="line_one_point"),
        pytest.param(dict(y_vals=[(i * 37) % 23 - 8 for i in range(25)]), id="line_25_points"),
        pytest.param(
            dict(y_vals=[(i * 7) % 11 for i in range(45)], plot_type="bar"), id="bar_45_points"
        ),
        pytest.param(dict(y_vals=[12000, 450000, 3_200_000, 87_654]), id="line_large_values"),
        pytest.param(dict(y_vals=[0.001, 0.005, 0.0002, 0.03]), id="line_small_values"),
        pytest.param(dict(y_vals=Y_MIXED, interactive_data_values=False), id="line_static_values"),
        pytest.param(
            dict(
                y_vals=Y_MIXED,
                show_data_area=False,
                show_vertical_guides=False,
                show_y_axis_guide=False,
            ),
            id="line_layers_hidden",
        ),
        pytest.param(
            dict(
                y_vals=[-2, 5, 0, 3.5, 7],
                data_point_radius=[2, 4, 6, 8, 10],
                data_point_fill_color=["#F00", "#0F0", "#00F", "#FF0", "#0FF"],
                data_line_stroke_color="#ABCDEF",
                data_area_fill_color="#00FF00",
            ),
            id="line_styled",
        ),
        pytest.param(
            dict(
                y_vals=[-2, 5, 0, 3.5, 7],
                plot_type="bar",
                data_bar_fill_color=["#a", "#b", "#c", "#d", "#e"],
                data_bar_negative_fill_color="#FFF",
            ),
            id="bar_styled",
        ),
        pytest.param(dict(y_vals=Y_MIXED, plot_type="bar", currency="USD"), id="bar_currency"),
        pytest.param(
            dict(
                y_vals=Y_INT,
                y_ref_line="median",
                y_val_fmt_fn=lambda v: f"v{v}",
                y_axis_fmt_fn=lambda v: f"a{v}",
                y_ref_line_fmt_fn=lambda v: f"r{v}",
            ),
            id="line_fmt_fns",
        ),
    ],
)
def test_snap_multi_value(snapshot, kwargs: dict[str, Any]):
    assert snapshot == _generate_nanoplot(**kwargs)


# ---------------------------------------------------------------------------
# Snapshots of single-value plots
# ---------------------------------------------------------------------------

ALL_SINGLE = [-5.3, 6.3, -2.3, 0, 2.3, 6.7, 14.2]


@pytest.mark.parametrize("plot_type", ["line", "bar"])
@pytest.mark.parametrize(
    "kwargs",
    [
        pytest.param(dict(y_vals=6.3), id="positive"),
        pytest.param(dict(y_vals=-5.3), id="negative"),
        pytest.param(dict(y_vals=0), id="zero"),
        pytest.param(dict(y_vals=0, all_single_y_vals=[-1, -5, -3]), id="zero_all_negative"),
        pytest.param(dict(y_vals=0, all_single_y_vals=[0, 0, 0]), id="zero_all_zero"),
        pytest.param(dict(y_vals=2.3, y_ref_line="mean"), id="ref_line_keyword"),
        pytest.param(dict(y_vals=2.3, y_ref_line=14), id="ref_line_label_on_left"),
        pytest.param(dict(y_vals=3, all_single_y_vals=[1, 3, 8], currency="EUR"), id="currency"),
    ],
)
def test_snap_single_value(snapshot, plot_type: str, kwargs: dict[str, Any]):
    kwargs = {"all_single_y_vals": ALL_SINGLE, **kwargs}

    assert snapshot == _generate_nanoplot(plot_type=plot_type, **kwargs)


# ---------------------------------------------------------------------------
# Snapshots of tables made with `fmt_nanoplot()`
# ---------------------------------------------------------------------------

STREAMS = ["20 23 6 7 37 23 21 4 7 16", "2.3 6.8 9.2 2.42 3.5 12.1", "-12 -5 6 3.7 0 8 -7.4"]


def test_snap_fmt_nanoplot_autoscale(snapshot):
    gt = GT(pl.DataFrame({"v": STREAMS})).fmt_nanoplot(
        columns="v", autoscale=True, reference_line="mean", reference_area=["q1", "q3"]
    )

    assert_rendered_body(snapshot, gt)


def test_snap_fmt_nanoplot_x_y_dates(snapshot):
    df = pl.DataFrame(
        {
            "v": [
                {"x": ["2020-01-01", "2020-02-15", "2020-06-30"], "y": [5, 3, 6]},
                {"x": ["2021-03-01", "2021-03-05", "2021-03-09"], "y": [1, 2, 3]},
            ]
        }
    )

    with pytest.warns(UserWarning, match="curved data line is not supported"):
        assert_rendered_body(snapshot, GT(df).fmt_nanoplot(columns="v"))


def test_snap_fmt_nanoplot_single_values_bar(snapshot):
    gt = GT(pl.DataFrame({"v": [1, None, -3, 4]})).fmt_nanoplot(
        columns="v", plot_type="bar", reference_line="max"
    )

    assert_rendered_body(snapshot, gt)


def test_snap_fmt_nanoplot_options(snapshot):
    gt = GT(pl.DataFrame({"v": STREAMS})).fmt_nanoplot(
        columns="v",
        plot_type="bar",
        options=nanoplot_options(
            data_bar_fill_color="orange",
            data_bar_negative_fill_color="lightblue",
            interactive_data_values=False,
            show_y_axis_guide=False,
        ),
    )

    assert_rendered_body(snapshot, gt)
