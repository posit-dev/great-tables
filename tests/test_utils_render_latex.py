import pytest
from unittest import mock
import pandas as pd
import os

from great_tables import GT, exibble

from great_tables._utils_render_latex import (
    is_css_length_string,
    is_number_without_units,
    css_length_has_supported_units,
    get_px_conversion,
    get_units_from_length_string,
    convert_to_px,
    convert_to_pt,
    create_width_dict_l,
    create_wrap_start_l,
    create_fontsize_statement_l,
)


@pytest.fixture
def gt_tbl():
    return GT(pd.DataFrame({"x": [1, 2], "y": [4, 5]}))


def test_is_css_length_string():

    assert is_css_length_string("12.5pt")
    assert is_css_length_string("12.5px")
    assert is_css_length_string("12.5")


def test_is_number_without_units():

    assert is_number_without_units("12.5")
    assert not is_number_without_units("12.5pt")


def test_css_length_has_supported_units():

    assert css_length_has_supported_units("12.5pt")
    assert css_length_has_supported_units("12.5px")
    assert css_length_has_supported_units("12.5")
    assert css_length_has_supported_units("12.5pt", no_units_valid=False)
    assert css_length_has_supported_units("12.5px", no_units_valid=False)
    assert not css_length_has_supported_units("12.5", no_units_valid=False)


def test_get_units_from_length_string():

    assert get_units_from_length_string("12.5pt") == "pt"
    assert get_units_from_length_string("") == "px"


def test_get_px_conversion_val():

    assert get_px_conversion(length="2343.23pt") == 4 / 3
    assert get_px_conversion(length="43.2px") == 1.0


def test_convert_to_px():

    assert convert_to_px("12.5pt") == 17.0
    assert convert_to_px("12.5px") == 12.5


def test_convert_to_pt():

    assert convert_to_pt("16px") == 12.0


def test_create_width_dict_l_simple():

    gt_tbl = GT(exibble)

    width_dict = create_width_dict_l(gt_tbl)

    assert width_dict["type"] == ["default"] * 9
    assert width_dict["unspec"] == [1] * 9
    assert width_dict["lw"] == [0] * 9
    assert width_dict["pt"] == [0] * 9
    assert width_dict["column_align"] == [
        "right",
        "left",
        "left",
        "right",
        "right",
        "right",
        "right",
        "left",
        "left",
    ]
    assert width_dict["tbl_width"] is None


def test_create_width_dict_l_settings():

    gt_tbl = (
        GT(exibble)
        .cols_align(align="left", columns="num")
        .cols_hide(columns="char")
        .cols_width(cases={"fctr": "150px", "time": "200px"})
    )

    width_dict = create_width_dict_l(gt_tbl)

    assert width_dict["type"] == ["default"] + ["hidden"] + ["default"] * 7
    assert width_dict["unspec"] == [1, 1, 0, 1, 0, 1, 1, 1, 1]
    assert width_dict["lw"] == [0] * 9
    assert width_dict["pt"] == [0] * 9
    assert width_dict["column_align"] == [
        "left",
        "left",
        "left",
        "right",
        "right",
        "right",
        "right",
        "left",
        "left",
    ]
    assert width_dict["tbl_width"] is None


def test_create_fontsize_statement_l():

    gt_tbl = GT(exibble)

    assert create_fontsize_statement_l(gt_tbl) == "\\fontsize{12.0pt}{14.4pt}\\selectfont\n"


def test_create_fontsize_statement_l_settings():

    gt_tbl = GT(exibble).tab_options(table_font_size="18.5px")

    assert create_fontsize_statement_l(gt_tbl) == "\\fontsize{13.9pt}{16.6pt}\\selectfont\n"


@mock.patch.dict(os.environ, {"QUARTO_BIN_PATH": "1"}, clear=True)
def test_create_wrap_start_quarto(gt_tbl: GT):

    assert create_wrap_start_l(gt_tbl) == "\\begin{table}\n"


def test_create_wrap_start_simple_tbl(gt_tbl: GT):

    assert create_wrap_start_l(gt_tbl) == "\\begin{table}[!t]\n"
