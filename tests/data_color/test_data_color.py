from great_tables import GT
from great_tables.data import exibble
from great_tables._utils_render_html import create_body_component_h
import pandas as pd


def assert_rendered_body(snapshot, gt):
    built = gt._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def test_data_color_simple_df_snap(snapshot):
    df = pd.DataFrame(
        {
            "A": [1, 2, 3],
            "B": [10, 9, 8],
            "C": ["one", "two", "three"],
        }
    )

    new_gt = GT(df).data_color()

    assert_rendered_body(snapshot, new_gt)


def test_data_color_simple_exibble_snap(snapshot):
    gt = GT(exibble).data_color()

    assert_rendered_body(snapshot, gt)


def test_data_color_palette_snap(snapshot):
    gt = GT(exibble).data_color(columns=["num", "currency"], palette=["red", "green"])

    assert_rendered_body(snapshot, gt)


def test_data_color_domain_na_color_snap(snapshot):
    """`data_color` works with `domain` and `na_color`."""
    gt = GT(exibble).data_color(
        columns="currency", palette=["red", "green"], domain=[0, 50], na_color="blue"
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_domain_na_color_reverse_snap(snapshot):
    """`data_color` works with `domain`, `na_color`, and `reverse`."""
    gt = GT(exibble).data_color(
        columns="currency", palette=["red", "green"], domain=[0, 50], na_color="blue", reverse=True
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_overlapping_domain(snapshot):
    """`data_color` works with overlapping `domain` (RHS domain extends outside the data range)."""
    gt = GT(exibble).data_color(
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 65555],
        na_color="red",
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_subset_domain(snapshot):
    """`data_color` works with subset `domain`."""
    gt = GT(exibble).data_color(
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 60000],
        na_color="red",
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_autocolor_text_false(snapshot):
    """`data_color` works with `autocolor_text=False`."""
    gt = GT(exibble).data_color(
        columns="currency",
        palette=["red", "green"],
        domain=[0, 50],
        na_color="blue",
        reverse=True,
        autocolor_text=False,
    )

    assert_rendered_body(snapshot, gt)
