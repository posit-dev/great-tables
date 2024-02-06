import pandas as pd
import pytest
from great_tables import GT, md, exibble
from great_tables._scss import compile_scss


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
css_color_val = "red"
css_color_val_light = "lightred"
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
            table_width=css_length_val_large,
            table_layout="auto",
            table_margin_left=css_length_val_margin,
            table_margin_right=css_length_val_margin,
            table_background_color=css_color_val,
            table_font_names=css_font_family_list,
            table_font_size=css_font_size_val,
            table_font_weight=css_font_weight_val,
            table_font_style=css_font_weight_val,
            table_font_color=css_color_val,
            table_font_color_light=css_color_val_light,
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
    assert gt_tbl._options.table_width.value == css_length_val_large
    assert gt_tbl._options.table_layout.value == "auto"
    assert gt_tbl._options.table_margin_left.value == css_length_val_margin
    assert gt_tbl._options.table_margin_right.value == css_length_val_margin
    assert gt_tbl._options.table_background_color.value == css_color_val
    assert gt_tbl._options.table_font_names.value == css_font_family_list
    assert gt_tbl._options.table_font_size.value == css_font_size_val
    assert gt_tbl._options.table_font_weight.value == css_font_weight_val
    assert gt_tbl._options.table_font_style.value == css_font_weight_val
    assert gt_tbl._options.table_font_color.value == css_color_val
    assert gt_tbl._options.table_font_color_light.value == css_color_val_light
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
