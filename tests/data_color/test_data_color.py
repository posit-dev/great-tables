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
            "A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "B": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            "C": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"],
        }
    )

    new_gt = GT(df).data_color()

    assert_rendered_body(snapshot, new_gt)


def test_data_color_exibble_snap_1(snapshot):
    gt = GT(exibble).data_color()

    assert_rendered_body(snapshot, gt)


def test_data_color_exibble_snap_2(snapshot):
    gt = GT(exibble).data_color(columns=["num", "currency"], palette=["red", "green"])

    assert_rendered_body(snapshot, gt)


def test_data_color_exibble_snap_3(snapshot):
    gt = GT(exibble).data_color(
        columns="currency", palette=["red", "green"], domain=[0, 50], na_color="blue"
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_exibble_snap_4(snapshot):
    gt = GT(exibble).data_color(
        columns="currency", palette=["red", "green"], domain=[0, 50], na_color="blue", reverse=True
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_exibble_snap_5(snapshot):
    gt = GT(exibble).data_color(
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 65555],
        na_color="red",
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_exibble_snap_6(snapshot):
    gt = GT(exibble).data_color(
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 60000],
        na_color="red",
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_exibble_snap_7(snapshot):
    gt = GT(exibble).data_color(
        columns="currency",
        palette=["red", "green"],
        domain=[0, 50],
        na_color="blue",
        reverse=True,
        autocolor_text=False,
    )

    assert_rendered_body(snapshot, gt)
