import re

import pandas as pd
import polars as pl
import pytest
from great_tables import GT, exibble, loc, md, google_font
from great_tables._scss import compile_scss
from great_tables._gt_data import default_fonts_list
from great_tables._helpers import _intify_scaled_px
from great_tables._utils_render_html import create_body_component_h


def test_options_overwrite():
    df = pd.DataFrame({"x": [1, 2, 3]})
    gt = GT(df)

    gt = gt.tab_options(container_width="50px")
    gt = gt.tab_options(container_width="100px")

    assert gt._options.container_width.value == "100px"


def test_options_no_mutate():
    df = pd.DataFrame({"x": [1, 2, 3]})
    gt = GT(df)

    gt2 = gt.tab_options(container_width="100px")
    gt3 = gt.tab_options(container_width="999px")

    assert gt2._options.container_width.value == "100px"
    assert gt3._options.container_width.value == "999px"


# Include shared variables for `tab_options()`
css_length_val_large = "100px"
css_length_val_margin = "10px"
css_length_val_small = "5px"
css_font_size_val = "12px"
css_font_color_val = "#000000"
css_font_color_val_light = "#FFFFFF"
css_color_val = "red"
css_style_val = "solid"
css_font_family_list = ["Arial", "Helvetica", "sans-serif"]
css_font_weight_val = "bold"
css_font_text_transform_val = "uppercase"


@pytest.fixture
def gt_tbl():
    gt_tbl = (
        GT(
            exibble[["num", "char", "currency", "row", "group"]],
            rowname_col="row",
            groupname_col="group",
        )
        .tab_header(
            title=md("Data listing from **exibble**"),
            subtitle=md("`exibble` is a **Great Tables** dataset."),
        )
        .fmt_number(columns="num")
        .fmt_currency(columns="currency")
        .tab_source_note(source_note="This is only a subset of the dataset.")
        .tab_options(
            container_width="1500px",
            container_height="500px",
            container_overflow_x="hidden",
            container_overflow_y="hidden",
            container_padding_x=css_length_val_small,
            container_padding_y=css_length_val_small,
            table_width=css_length_val_large,
            table_layout="auto",
            table_margin_left=css_length_val_margin,
            table_margin_right=css_length_val_margin,
            table_background_color="red",
            table_font_names=css_font_family_list,
            table_font_size=css_font_size_val,
            table_font_weight=css_font_weight_val,
            table_font_style=css_font_weight_val,
            table_font_color=css_font_color_val,
            table_font_color_light=css_font_color_val_light,
            table_border_top_style=css_style_val,
            table_border_top_width=css_length_val_small,
            table_border_top_color=css_color_val,
            table_border_bottom_style=css_style_val,
            table_border_bottom_width=css_length_val_small,
            table_border_bottom_color=css_color_val,
            table_border_left_style=css_style_val,
            table_border_left_width=css_length_val_small,
            table_border_left_color=css_color_val,
            table_border_right_style=css_style_val,
            table_border_right_width=css_length_val_small,
            table_border_right_color=css_color_val,
            heading_background_color=css_color_val,
            heading_align="right",
            heading_title_font_size=css_font_size_val,
            heading_title_font_weight=css_font_weight_val,
            heading_subtitle_font_size=css_font_size_val,
            heading_subtitle_font_weight=css_font_weight_val,
            heading_padding=css_length_val_small,
            heading_padding_horizontal=css_length_val_small,
            heading_border_bottom_style=css_style_val,
            heading_border_bottom_width=css_length_val_small,
            heading_border_bottom_color=css_color_val,
            heading_border_lr_style=css_style_val,
            heading_border_lr_width=css_length_val_small,
            heading_border_lr_color=css_color_val,
            column_labels_background_color=css_color_val,
            column_labels_font_size=css_font_size_val,
            column_labels_font_weight=css_font_weight_val,
            column_labels_text_transform=css_font_text_transform_val,
            column_labels_padding=css_length_val_small,
            column_labels_padding_horizontal=css_length_val_small,
            column_labels_vlines_style=css_style_val,
            column_labels_vlines_width=css_length_val_small,
            column_labels_vlines_color=css_color_val,
            column_labels_border_top_style=css_style_val,
            column_labels_border_top_width=css_length_val_small,
            column_labels_border_top_color=css_color_val,
            column_labels_border_bottom_style=css_style_val,
            column_labels_border_bottom_width=css_length_val_small,
            column_labels_border_bottom_color=css_color_val,
            column_labels_border_lr_style=css_style_val,
            column_labels_border_lr_width=css_length_val_small,
            column_labels_border_lr_color=css_color_val,
            row_group_background_color=css_color_val,
            row_group_font_size=css_font_size_val,
            row_group_font_weight=css_font_weight_val,
            row_group_text_transform=css_font_text_transform_val,
            row_group_padding=css_length_val_small,
            row_group_padding_horizontal=css_length_val_small,
            row_group_border_top_style=css_style_val,
            row_group_border_top_width=css_length_val_small,
            row_group_border_top_color=css_color_val,
            row_group_border_bottom_style=css_style_val,
            row_group_border_bottom_width=css_length_val_small,
            row_group_border_bottom_color=css_color_val,
            row_group_border_left_style=css_style_val,
            row_group_border_left_width=css_length_val_small,
            row_group_border_left_color=css_color_val,
            row_group_border_right_style=css_style_val,
            row_group_border_right_width=css_length_val_small,
            row_group_border_right_color=css_color_val,
            row_group_as_column=True,
            table_body_hlines_style=css_style_val,
            table_body_hlines_width=css_length_val_small,
            table_body_hlines_color=css_color_val,
            table_body_vlines_style=css_style_val,
            table_body_vlines_width=css_length_val_small,
            table_body_vlines_color=css_color_val,
            table_body_border_top_style=css_style_val,
            table_body_border_top_width=css_length_val_small,
            table_body_border_top_color=css_color_val,
            table_body_border_bottom_style=css_style_val,
            table_body_border_bottom_width=css_length_val_small,
            table_body_border_bottom_color=css_color_val,
            stub_background_color=css_color_val,
            stub_font_size=css_font_size_val,
            stub_font_weight=css_font_weight_val,
            stub_text_transform=css_font_text_transform_val,
            stub_border_style=css_style_val,
            stub_border_width=css_length_val_small,
            stub_border_color=css_color_val,
            stub_row_group_font_size=css_font_size_val,
            stub_row_group_font_weight=css_font_weight_val,
            stub_row_group_text_transform=css_font_text_transform_val,
            stub_row_group_border_style=css_style_val,
            stub_row_group_border_width=css_length_val_small,
            stub_row_group_border_color=css_color_val,
            data_row_padding=css_length_val_small,
            data_row_padding_horizontal=css_length_val_small,
            source_notes_background_color=css_color_val,
            source_notes_font_size=css_font_size_val,
            source_notes_padding=css_length_val_small,
            source_notes_padding_horizontal=css_length_val_small,
            source_notes_border_bottom_style=css_style_val,
            source_notes_border_bottom_width=css_length_val_small,
            source_notes_border_bottom_color=css_color_val,
            source_notes_border_lr_style=css_style_val,
            source_notes_border_lr_width=css_length_val_small,
            source_notes_border_lr_color=css_color_val,
            source_notes_multiline=False,
            source_notes_sep=" , ",
        )
    )

    return gt_tbl


def test_options_all_available(gt_tbl: GT):
    assert gt_tbl._options.container_width.value == "1500px"
    assert gt_tbl._options.container_height.value == "500px"
    assert gt_tbl._options.container_overflow_x.value == "hidden"
    assert gt_tbl._options.container_overflow_y.value == "hidden"
    assert gt_tbl._options.container_padding_x.value == css_length_val_small
    assert gt_tbl._options.container_padding_y.value == css_length_val_small
    assert gt_tbl._options.table_width.value == css_length_val_large
    assert gt_tbl._options.table_layout.value == "auto"
    assert gt_tbl._options.table_margin_left.value == css_length_val_margin
    assert gt_tbl._options.table_margin_right.value == css_length_val_margin
    assert gt_tbl._options.table_background_color.value == css_color_val
    assert gt_tbl._options.table_font_names.value == css_font_family_list
    assert gt_tbl._options.table_font_size.value == css_font_size_val
    assert gt_tbl._options.table_font_weight.value == css_font_weight_val
    assert gt_tbl._options.table_font_style.value == css_font_weight_val
    assert gt_tbl._options.table_font_color.value == css_font_color_val
    assert gt_tbl._options.table_font_color_light.value == css_font_color_val_light
    assert gt_tbl._options.table_border_top_style.value == css_style_val
    assert gt_tbl._options.table_border_top_width.value == css_length_val_small
    assert gt_tbl._options.table_border_top_color.value == css_color_val
    assert gt_tbl._options.table_border_bottom_style.value == css_style_val
    assert gt_tbl._options.table_border_bottom_width.value == css_length_val_small
    assert gt_tbl._options.table_border_bottom_color.value == css_color_val
    assert gt_tbl._options.table_border_left_style.value == css_style_val
    assert gt_tbl._options.table_border_left_width.value == css_length_val_small
    assert gt_tbl._options.table_border_left_color.value == css_color_val
    assert gt_tbl._options.table_border_right_style.value == css_style_val
    assert gt_tbl._options.table_border_right_width.value == css_length_val_small
    assert gt_tbl._options.table_border_right_color.value == css_color_val
    assert gt_tbl._options.heading_background_color.value == css_color_val
    assert gt_tbl._options.heading_align.value == "right"
    assert gt_tbl._options.heading_title_font_size.value == css_font_size_val
    assert gt_tbl._options.heading_title_font_weight.value == css_font_weight_val
    assert gt_tbl._options.heading_subtitle_font_size.value == css_font_size_val
    assert gt_tbl._options.heading_subtitle_font_weight.value == css_font_weight_val
    assert gt_tbl._options.heading_padding.value == css_length_val_small
    assert gt_tbl._options.heading_padding_horizontal.value == css_length_val_small
    assert gt_tbl._options.heading_border_bottom_style.value == css_style_val
    assert gt_tbl._options.heading_border_bottom_width.value == css_length_val_small
    assert gt_tbl._options.heading_border_bottom_color.value == css_color_val
    assert gt_tbl._options.heading_border_lr_style.value == css_style_val
    assert gt_tbl._options.heading_border_lr_width.value == css_length_val_small
    assert gt_tbl._options.heading_border_lr_color.value == css_color_val
    assert gt_tbl._options.column_labels_background_color.value == css_color_val
    assert gt_tbl._options.column_labels_font_size.value == css_font_size_val
    assert gt_tbl._options.column_labels_font_weight.value == css_font_weight_val
    assert gt_tbl._options.column_labels_text_transform.value == css_font_text_transform_val
    assert gt_tbl._options.column_labels_padding.value == css_length_val_small
    assert gt_tbl._options.column_labels_padding_horizontal.value == css_length_val_small
    assert gt_tbl._options.column_labels_vlines_style.value == css_style_val
    assert gt_tbl._options.column_labels_vlines_width.value == css_length_val_small
    assert gt_tbl._options.column_labels_vlines_color.value == css_color_val
    assert gt_tbl._options.column_labels_border_top_style.value == css_style_val
    assert gt_tbl._options.column_labels_border_top_width.value == css_length_val_small
    assert gt_tbl._options.column_labels_border_top_color.value == css_color_val
    assert gt_tbl._options.column_labels_border_bottom_style.value == css_style_val
    assert gt_tbl._options.column_labels_border_bottom_width.value == css_length_val_small
    assert gt_tbl._options.column_labels_border_bottom_color.value == css_color_val
    assert gt_tbl._options.column_labels_border_lr_style.value == css_style_val
    assert gt_tbl._options.column_labels_border_lr_width.value == css_length_val_small
    assert gt_tbl._options.column_labels_border_lr_color.value == css_color_val
    assert gt_tbl._options.row_group_background_color.value == css_color_val
    assert gt_tbl._options.row_group_font_size.value == css_font_size_val
    assert gt_tbl._options.row_group_font_weight.value == css_font_weight_val
    assert gt_tbl._options.row_group_text_transform.value == css_font_text_transform_val
    assert gt_tbl._options.row_group_padding.value == css_length_val_small
    assert gt_tbl._options.row_group_padding_horizontal.value == css_length_val_small
    assert gt_tbl._options.row_group_border_top_style.value == css_style_val
    assert gt_tbl._options.row_group_border_top_width.value == css_length_val_small
    assert gt_tbl._options.row_group_border_top_color.value == css_color_val
    assert gt_tbl._options.row_group_border_bottom_style.value == css_style_val
    assert gt_tbl._options.row_group_border_bottom_width.value == css_length_val_small
    assert gt_tbl._options.row_group_border_bottom_color.value == css_color_val
    assert gt_tbl._options.row_group_border_left_style.value == css_style_val
    assert gt_tbl._options.row_group_border_left_width.value == css_length_val_small
    assert gt_tbl._options.row_group_border_left_color.value == css_color_val
    assert gt_tbl._options.row_group_border_right_style.value == css_style_val
    assert gt_tbl._options.row_group_border_right_width.value == css_length_val_small
    assert gt_tbl._options.row_group_border_right_color.value == css_color_val
    assert gt_tbl._options.row_group_as_column.value == True
    assert gt_tbl._options.table_body_hlines_style.value == css_style_val
    assert gt_tbl._options.table_body_hlines_width.value == css_length_val_small
    assert gt_tbl._options.table_body_hlines_color.value == css_color_val
    assert gt_tbl._options.table_body_vlines_style.value == css_style_val
    assert gt_tbl._options.table_body_vlines_width.value == css_length_val_small
    assert gt_tbl._options.table_body_vlines_color.value == css_color_val
    assert gt_tbl._options.table_body_border_top_style.value == css_style_val
    assert gt_tbl._options.table_body_border_top_width.value == css_length_val_small
    assert gt_tbl._options.table_body_border_top_color.value == css_color_val
    assert gt_tbl._options.table_body_border_bottom_style.value == css_style_val
    assert gt_tbl._options.table_body_border_bottom_width.value == css_length_val_small
    assert gt_tbl._options.table_body_border_bottom_color.value == css_color_val
    assert gt_tbl._options.stub_background_color.value == css_color_val
    assert gt_tbl._options.stub_font_size.value == css_font_size_val
    assert gt_tbl._options.stub_font_weight.value == css_font_weight_val
    assert gt_tbl._options.stub_text_transform.value == css_font_text_transform_val
    assert gt_tbl._options.stub_border_style.value == css_style_val
    assert gt_tbl._options.stub_border_width.value == css_length_val_small
    assert gt_tbl._options.stub_border_color.value == css_color_val
    assert gt_tbl._options.stub_row_group_font_size.value == css_font_size_val
    assert gt_tbl._options.stub_row_group_font_weight.value == css_font_weight_val
    assert gt_tbl._options.stub_row_group_text_transform.value == css_font_text_transform_val
    assert gt_tbl._options.stub_row_group_border_style.value == css_style_val
    assert gt_tbl._options.stub_row_group_border_width.value == css_length_val_small
    assert gt_tbl._options.stub_row_group_border_color.value == css_color_val
    assert gt_tbl._options.data_row_padding.value == css_length_val_small
    assert gt_tbl._options.data_row_padding_horizontal.value == css_length_val_small
    assert gt_tbl._options.source_notes_background_color.value == css_color_val
    assert gt_tbl._options.source_notes_font_size.value == css_font_size_val
    assert gt_tbl._options.source_notes_padding.value == css_length_val_small
    assert gt_tbl._options.source_notes_padding_horizontal.value == css_length_val_small
    assert gt_tbl._options.source_notes_border_bottom_style.value == css_style_val
    assert gt_tbl._options.source_notes_border_bottom_width.value == css_length_val_small
    assert gt_tbl._options.source_notes_border_bottom_color.value == css_color_val
    assert gt_tbl._options.source_notes_border_lr_style.value == css_style_val
    assert gt_tbl._options.source_notes_border_lr_width.value == css_length_val_small
    assert gt_tbl._options.source_notes_border_lr_color.value == css_color_val
    assert gt_tbl._options.source_notes_multiline.value == False
    assert gt_tbl._options.source_notes_sep.value == " , "


def test_scss_default_generated(gt_tbl: GT, snapshot):
    assert snapshot == compile_scss(gt_tbl, id="abc", compress=False)


def test_scss_from_opt_table_outline(gt_tbl: GT, snapshot):
    gt_tbl_outline = (
        GT(
            exibble[["num", "char", "currency", "row", "group"]],
            rowname_col="row",
            groupname_col="group",
        )
        .tab_header(
            title=md("Data listing from **exibble**"),
            subtitle=md("`exibble` is a **Great Tables** dataset."),
        )
        .opt_table_outline(width="10px", style="dotted", color="blue")
    )

    assert gt_tbl._options.source_notes_border_bottom_color.value == css_color_val

    for part in ["top", "right", "bottom", "left"]:
        assert getattr(gt_tbl_outline._options, f"table_border_{part}_style").value == "dotted"
        assert getattr(gt_tbl_outline._options, f"table_border_{part}_width").value == "10px"
        assert getattr(gt_tbl_outline._options, f"table_border_{part}_color").value == "blue"

    assert snapshot == compile_scss(gt_tbl_outline, id="abc", compress=False)


def test_opt_table_font_add_font():
    gt_tbl = GT(exibble).opt_table_font(font="Arial", weight="bold", style="italic")

    assert gt_tbl._options.table_font_names.value == ["Arial"] + default_fonts_list
    assert gt_tbl._options.table_font_weight.value == "bold"
    assert gt_tbl._options.table_font_style.value == "italic"


def test_opt_table_font_replace_font():
    gt_tbl = GT(exibble).opt_table_font(font="Arial", weight="bold", style="bold", add=False)

    assert gt_tbl._options.table_font_names.value == ["Arial"]
    assert gt_tbl._options.table_font_weight.value == "bold"
    assert gt_tbl._options.table_font_style.value == "bold"


def test_opt_table_font_use_stack():
    gt_tbl = GT(exibble).opt_table_font(stack="humanist")

    assert gt_tbl._options.table_font_names.value[0] == "Seravek"
    assert gt_tbl._options.table_font_names.value[-1] == "Noto Color Emoji"


def test_opt_table_font_use_stack_and_system_font():
    gt_tbl = GT(exibble).opt_table_font(font="Comic Sans MS", stack="humanist")

    assert gt_tbl._options.table_font_names.value[0] == "Comic Sans MS"
    assert gt_tbl._options.table_font_names.value[1] == "Seravek"
    assert gt_tbl._options.table_font_names.value[-1] == "Noto Color Emoji"


def test_opt_table_font_google_font():
    gt_tbl = GT(exibble).opt_table_font(font=google_font(name="IBM Plex Mono"))

    rendered_html = gt_tbl.as_raw_html()

    assert rendered_html.find(
        "@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');"
    )

    assert rendered_html.find(
        "font-family: 'IBM Plex Mono', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;"
    )


def test_opt_table_font_raises():
    # Both `font` and `stack` cannot be `None`
    with pytest.raises(ValueError) as exc_info:
        GT(exibble).opt_table_font(font=None, stack=None)

    assert "Either `font=` or `stack=` must be provided." in exc_info.value.args[0]


@pytest.mark.parametrize("font", [1, [1]])
def test_opt_table_font_raises_font(font):
    with pytest.raises(TypeError) as exc_info:
        GT(exibble).opt_table_font(font=font)

    assert (
        "`font=` must be a string/GoogleFont object or a list of strings/GoogleFont objects."
        in exc_info.value.args[0]
    )


def test_opt_table_font_raises_weight():
    with pytest.raises(TypeError) as exc_info:
        GT(exibble).opt_table_font(stack="humanist", weight=(1, 2))

    assert (
        "`weight=` must be a numeric value between 1 and 1000 or a text-based keyword."
        in exc_info.value.args[0]
    )


def test_opt_row_striping():
    gt_tbl_0 = GT(exibble)
    gt_tbl_1 = GT(exibble).opt_row_striping()
    gt_tbl_2 = GT(exibble).opt_row_striping().opt_row_striping(row_striping=False)

    assert gt_tbl_0._options.row_striping_include_table_body.value == False
    assert gt_tbl_1._options.row_striping_include_table_body.value == True
    assert gt_tbl_2._options.row_striping_include_table_body.value == False


def test_tab_options_striping():
    gt_tbl_tab_opts = GT(exibble).tab_options(row_striping_include_table_body=True)
    gt_tbl_opt_stri = GT(exibble).opt_row_striping()

    assert gt_tbl_tab_opts._options.row_striping_include_table_body.value == True
    assert gt_tbl_tab_opts._options.row_striping_include_stub.value == False

    assert gt_tbl_opt_stri._options.row_striping_include_table_body.value == True
    assert gt_tbl_opt_stri._options.row_striping_include_stub.value == False


def test_tab_options_striping_body_snap(snapshot):
    gt_tbl = GT(
        exibble[["row", "group", "char"]].head(4), rowname_col="row", groupname_col="group"
    ).tab_options(
        row_striping_include_table_body=True,
        row_striping_background_color="lightblue",
    )

    built = gt_tbl._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def test_tab_options_striping_stub_snap(snapshot):
    gt_tbl = GT(
        exibble[["row", "group", "char"]].head(4), rowname_col="row", groupname_col="group"
    ).tab_options(
        row_striping_include_stub=True,
        row_striping_background_color="lightblue",
    )

    built = gt_tbl._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def test_opt_stylize_default(snapshot):
    gt_tbl = GT(exibble, rowname_col="row", groupname_col="group").opt_stylize()

    assert snapshot == compile_scss(gt_tbl, id="abc", compress=False)


def test_opt_stylize_no_striping(snapshot):
    gt_tbl = GT(exibble, rowname_col="row", groupname_col="group").opt_stylize(
        add_row_striping=False
    )

    assert snapshot == compile_scss(gt_tbl, id="abc", compress=False)


def test_opt_striping_with_group_snap(snapshot):
    pl_df = pl.DataFrame(
        {"a": [1, 2, 3, 4, 5, 6], "b": ["a", "b", "a", "b", "a", "b"], "c": ["val"] * 6}
    )

    gt = GT(pl_df, groupname_col="b", rowname_col="a").opt_row_striping()

    built = gt._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


@pytest.mark.parametrize("style", [1, 2, 3, 4, 5, 6])
def test_opt_stylize_outline_present(style, snapshot):
    gt_tbl = GT(exibble, rowname_col="row", groupname_col="group").opt_stylize(style=style)

    css = compile_scss(gt_tbl, id="abc", compress=False)

    css_gt_table_cls = re.sub(r"^.*?#abc \.gt_table \{\n(.*?)\}.*$", r"\1", css, flags=re.DOTALL)

    css_gt_table_border = re.sub(r".*?width: auto;(.*)", r"\1", css_gt_table_cls, flags=re.DOTALL)

    assert snapshot == css_gt_table_border


@pytest.mark.parametrize("align", ["left", "center", "right"])
def test_opt_align_table_header(gt_tbl: GT, align: list[str]):
    tbl = gt_tbl.opt_align_table_header(align=align)

    assert tbl._options.heading_align.value == align


@pytest.mark.parametrize("scale, expected", [(0.7, "3px"), (1.0, "5px"), (2.1, "10px")])
def test_opt_vertical_padding(gt_tbl: GT, scale: float, expected: int):
    """
    css_length_val_small = "5px"
    => int(0.7 * 5) = 3
    => int(1.0 * 5) = 5
    => int(2.1 * 5) = 10
    """
    tbl = gt_tbl.opt_vertical_padding(scale=scale)

    assert tbl._options.heading_padding.value == expected
    assert tbl._options.column_labels_padding.value == expected
    assert tbl._options.data_row_padding.value == expected
    assert tbl._options.row_group_padding.value == expected
    assert tbl._options.source_notes_padding.value == expected


@pytest.mark.parametrize("scale", [-0.2, 3.2])
def test_opt_vertical_padding_raises(gt_tbl: GT, scale: float):
    with pytest.raises(ValueError) as exc_info:
        gt_tbl.opt_vertical_padding(scale=scale)

    assert "`scale` must be a value between `0` and `3`." in exc_info.value.args[0]


@pytest.mark.parametrize("scale, expected", [(0.1, "0px"), (1.0, "5px"), (2.2, "11px")])
def test_opt_horizontal_padding(gt_tbl: GT, scale: float, expected: int):
    """
    css_length_val_small = "5px"
    => int(0.1 * 5) = 0
    => int(1.0 * 5) = 5
    => int(2.2 * 5) = 11
    """
    tbl = gt_tbl.opt_horizontal_padding(scale=scale)

    assert tbl._options.heading_padding_horizontal.value == expected
    assert tbl._options.column_labels_padding_horizontal.value == expected
    assert tbl._options.data_row_padding_horizontal.value == expected
    assert tbl._options.row_group_padding_horizontal.value == expected
    assert tbl._options.source_notes_padding_horizontal.value == expected


@pytest.mark.parametrize("scale", [-0.2, 3.2])
def test_opt_horizontal_padding_raises(gt_tbl: GT, scale: float):
    with pytest.raises(ValueError) as exc_info:
        gt_tbl.opt_horizontal_padding(scale=scale)

    assert "`scale` must be a value between `0` and `3`." in exc_info.value.args[0]


def test_opt_css_add_single_rule():
    # Test adding a single CSS rule
    res = GT(exibble).opt_css(css=".gt_table { background-color: red; }")
    assert res._options.table_additional_css.value == [".gt_table { background-color: red; }"]


def test_opt_css_chaining():
    # Test chaining multiple CSS additions
    res = (
        GT(exibble)
        .opt_css(css=".gt_table { background-color: red; }")
        .opt_css(css=".gt_row { color: blue; }")
    )
    assert len(res._options.table_additional_css.value) == 2
    assert ".gt_table { background-color: red; }" in res._options.table_additional_css.value
    assert ".gt_row { color: blue; }" in res._options.table_additional_css.value


def test_opt_css_duplicate_prevented():
    # Test that duplicate CSS is prevented by default
    gt_tbl = GT(exibble)
    css_rule = ".gt_table { color: green; }"

    res = gt_tbl.opt_css(css=css_rule).opt_css(css=css_rule)

    assert res._options.table_additional_css.value == [css_rule]


def test_opt_css_allow_duplicates():
    # Test that duplicates are allowed when allow_duplicates=True
    gt_tbl = GT(exibble)
    css_rule = ".gt_table { color: green; }"

    res = gt_tbl.opt_css(css=css_rule).opt_css(css=css_rule, allow_duplicates=True)

    assert res._options.table_additional_css.value == [css_rule, css_rule]


def test_opt_css_replace_mode():
    # Add initial CSS
    res = (
        GT(exibble).opt_css(css=".gt_table { color: red; }").opt_css(css=".gt_row { color: blue; }")
    )

    assert len(res._options.table_additional_css.value) == 2

    # Replace all CSS with `add=False`
    res_2 = res.opt_css(css=".gt_table { color: green; }", add=False)
    assert res_2._options.table_additional_css.value == [".gt_table { color: green; }"]


def test_opt_css_whitespace_handling():
    gt_tbl = GT(exibble)

    # Test using empty-string CSS
    res = gt_tbl.opt_css(css="")
    assert res._options.table_additional_css.value == []

    # Test whitespace-only CSS
    res_2 = gt_tbl.opt_css(css="   \n  \t  ")
    assert res_2._options.table_additional_css.value == []

    # Test CSS with leading and trailing whitespace (it should get stripped)
    res_3 = gt_tbl.opt_css(css="  .gt_table { color: red; }  ")
    assert res_3._options.table_additional_css.value == [".gt_table { color: red; }"]


def test_opt_css_empty_string_preserves_existing():
    # Test that opt_css(css="") preserves existing CSS when add=True (default)
    gt_tbl = GT(exibble).opt_css(css=".gt_table { color: red; }")

    res = gt_tbl.opt_css(css="")

    assert res._options.table_additional_css.value == [".gt_table { color: red; }"]


def test_opt_css_empty_string_clears_with_add_false():
    # Test that opt_css(css="", add=False) clears existing CSS
    gt_tbl = GT(exibble).opt_css(css=".gt_table { color: red; }")

    res = gt_tbl.opt_css(css="", add=False)

    assert res._options.table_additional_css.value == []


def test_opt_css_multiline():
    multiline_css = """
#test_table .gt_table {
  background-color: skyblue;
}
#test_table .gt_row {
  padding: 20px;
}"""

    result = GT(exibble, id="test_table").opt_css(css=multiline_css)

    expected_css = multiline_css.strip()

    assert result._options.table_additional_css.value == [expected_css]


def test_opt_css_html_output():
    css_rule = "#test_table .gt_table { background-color: lightblue; }"
    res = GT(exibble, id="test_table").opt_css(css=css_rule)

    html = res.as_raw_html()

    # Check that the CSS appears in the HTML string
    assert css_rule in html

    # For the CSS ordering, the added CSS should come after the default CSS
    default_css_pos = html.find("#test_table .gt_table { display: table;")
    custom_css_pos = html.find(css_rule)

    assert default_css_pos > 0
    assert custom_css_pos > 0
    assert custom_css_pos > default_css_pos


def test_opt_css_with_tab_options():
    res = (
        GT(exibble)
        .tab_options(table_additional_css=".initial { color: red; }")
        .opt_css(css=".added { color: blue; }")
    )

    css_list = res._options.table_additional_css.value

    assert len(css_list) == 2
    assert ".initial { color: red; }" in css_list
    assert ".added { color: blue; }" in css_list

    # Test that `opt_css()` rule comes after the `tab_options()` rule in the rendered HTML
    html = res.as_raw_html()

    assert html.index(".added { color: blue; }") > html.index(".initial { color: red; }")


def test_tab_options_empty_string_css():
    # Test that tab_options(table_additional_css="") results in empty list, not [""]
    res = GT(exibble).tab_options(table_additional_css="")

    assert res._options.table_additional_css.value == []


def test_opt_all_caps(gt_tbl: GT):
    tbl = gt_tbl.opt_all_caps(locations=loc.column_labels)

    assert tbl._options.column_labels_font_size.value == "80%"
    assert tbl._options.column_labels_font_weight.value == "bolder"
    assert tbl._options.column_labels_text_transform.value == "uppercase"

    tbl = gt_tbl.opt_all_caps(locations=[loc.column_labels, loc.stub])

    assert tbl._options.column_labels_font_size.value == "80%"
    assert tbl._options.column_labels_font_weight.value == "bolder"
    assert tbl._options.column_labels_text_transform.value == "uppercase"

    assert tbl._options.stub_font_size.value == "80%"
    assert tbl._options.stub_font_weight.value == "bolder"
    assert tbl._options.stub_text_transform.value == "uppercase"

    tbl = gt_tbl.opt_all_caps(locations=[loc.column_labels, loc.stub, loc.row_groups])

    assert tbl._options.column_labels_font_size.value == "80%"
    assert tbl._options.column_labels_font_weight.value == "bolder"
    assert tbl._options.column_labels_text_transform.value == "uppercase"

    assert tbl._options.stub_font_size.value == "80%"
    assert tbl._options.stub_font_weight.value == "bolder"
    assert tbl._options.stub_text_transform.value == "uppercase"

    assert tbl._options.row_group_font_size.value == "80%"
    assert tbl._options.row_group_font_weight.value == "bolder"
    assert tbl._options.row_group_text_transform.value == "uppercase"

    # Activate the following tests once the circular import issue is resolved.
    # tbl = gt_tbl.opt_all_caps()

    # assert tbl._options.column_labels_font_size.value == "80%"
    # assert tbl._options.column_labels_font_weight.value == "bolder"
    # assert tbl._options.column_labels_text_transform.value == "uppercase"

    # assert tbl._options.stub_font_size.value == "80%"
    # assert tbl._options.stub_font_weight.value == "bolder"
    # assert tbl._options.stub_text_transform.value == "uppercase"

    # assert tbl._options.row_group_font_size.value == "80%"
    # assert tbl._options.row_group_font_weight.value == "bolder"
    # assert tbl._options.row_group_text_transform.value == "uppercase"

    # tbl = gt_tbl.opt_all_caps(all_caps=False)

    # assert tbl._options.column_labels_font_size.value == "100%"
    # assert tbl._options.column_labels_font_weight.value == "normal"
    # assert tbl._options.column_labels_text_transform.value == "inherit"

    # assert tbl._options.stub_font_size.value == "100%"
    # assert tbl._options.stub_font_weight.value == "initial"
    # assert tbl._options.stub_text_transform.value == "inherit"

    # assert tbl._options.row_group_font_size.value == "100%"
    # assert tbl._options.row_group_font_weight.value == "initial"
    # assert tbl._options.row_group_text_transform.value == "inherit"


def test_opt_all_caps_raises(gt_tbl: GT):
    with pytest.raises(AssertionError) as exc_info:
        gt_tbl.opt_all_caps(locations="column_labels")

    assert (
        "Only `loc.column_labels`, `loc.stub` and `loc.row_groups` are allowed in the locations."
        in exc_info.value.args[0]
    )
