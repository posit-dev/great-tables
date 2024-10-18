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
    escape_latex,
    create_heading_component_l,
    create_body_component_l,
    create_columns_component_l,
    create_footer_component_l,
    create_wrap_end_l,
    escape_pattern_str_latex,
)


@pytest.fixture
def gt_tbl():
    return GT(pd.DataFrame({"x": [1, 2], "y": [4, 5]}))


@pytest.fixture
def gt_tbl_dec():
    return GT(pd.DataFrame({"x": [1.52, 2.23], "y": [4.75, 5.23]}))


@pytest.fixture
def gt_tbl_sci():
    return GT(pd.DataFrame({"x": [465633.46, -0.00000000345], "y": [4.509, 176.23]}))


@pytest.fixture
def gt_tbl_pct():
    return GT(pd.DataFrame({"x": [0.53, 0.0674], "y": [0.17, 0.32]}))


@pytest.fixture
def gt_tbl_dttm():
    return GT(
        pd.DataFrame(
            {
                "date": ["2023-08-12", "2020-11-17"],
                "time": ["09:21:23", "22:45:02"],
                "dttm": ["2023-08-12 09:21:23", "2020-11-17 22:45:02"],
            }
        )
    )


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


def test_escape_latex():

    assert escape_latex("a & b") == "a \\& b"
    assert escape_latex("a & b & c") == "a \\& b \\& c"
    assert escape_latex("\\a_\\d") == "\\\\a\\_\\\\d"


def test_escape_pattern_str_latex():

    assert escape_pattern_str_latex("{x}") == "{x}"
    assert escape_pattern_str_latex("a $_{1} %ab {2}") == "a \\$\\_{1} \\%ab {2}"
    assert escape_pattern_str_latex("a{b}c") == "a\\{b\\}c"


def test_create_fontsize_statement_l():

    gt_tbl = GT(exibble)

    assert create_fontsize_statement_l(gt_tbl) == "\\fontsize{12.0pt}{14.4pt}\\selectfont\n"


def test_create_fontsize_statement_l_settings():

    gt_tbl = GT(exibble).tab_options(table_font_size="18.5px")

    assert create_fontsize_statement_l(gt_tbl) == "\\fontsize{13.9pt}{16.6pt}\\selectfont\n"


def test_create_heading_component_l():

    gt_tbl_no_heading = GT(exibble)
    gt_tbl_title = GT(exibble).tab_header(title="Title")
    gt_tbl_title_subtitle = GT(exibble).tab_header(title="Title", subtitle="Subtitle")

    assert create_heading_component_l(gt_tbl_no_heading) == ""
    assert create_heading_component_l(gt_tbl_title) == "\\caption*{\n{\\large Title}\n} "
    assert (
        create_heading_component_l(gt_tbl_title_subtitle)
        == "\\caption*{\n{\\large Title} \\\\\n{\\small Subtitle}\n} "
    )


def test_create_columns_component_l_simple():

    gt_tbl = GT(exibble)

    width_dict = create_width_dict_l(gt_tbl)

    assert (
        create_columns_component_l(data=gt_tbl, width_dict=width_dict)
        == "\\toprule\nnum & char & fctr & date & time & datetime & currency & row & group \\\\ \n\\midrule\\addlinespace[2.5pt]"
    )


def test_create_columns_component_l_simple_hidden_cols():

    gt_tbl = GT(exibble).cols_hide(columns=["char", "date"])

    width_dict = create_width_dict_l(gt_tbl)

    assert (
        create_columns_component_l(data=gt_tbl, width_dict=width_dict)
        == "\\toprule\nnum & fctr & time & datetime & currency & row & group \\\\ \n\\midrule\\addlinespace[2.5pt]"
    )


def test_create_columns_component_l_one_spanner():

    gt_tbl = GT(exibble).tab_spanner(label="Spanner", columns=["num", "char"])

    width_dict = create_width_dict_l(gt_tbl)

    assert (
        create_columns_component_l(data=gt_tbl, width_dict=width_dict)
        == "\\toprule\n\\multicolumn{2}{c}{Spanner} &  \\\\ \n\\cmidrule(lr){1-2}\nnum & char & fctr & date & time & datetime & currency & row & group \\\\ \n\\midrule\\addlinespace[2.5pt]"
    )


def test_create_columns_component_l_adjacent_spanners_hiding():

    gt_tbl = (
        GT(exibble)
        .tab_spanner(label="Spanner 1", columns=["num", "char"])
        .tab_spanner(label="Spanner 2", columns=["date", "time"])
        .tab_spanner(label="Spanner 3", columns=["currency", "row"])
        .cols_hide(columns="row")
    )

    width_dict = create_width_dict_l(gt_tbl)

    assert (
        create_columns_component_l(data=gt_tbl, width_dict=width_dict)
        == "\\toprule\n\\multicolumn{2}{c}{Spanner 1} &  & \\multicolumn{2}{c}{Spanner 2} &  & \\multicolumn{1}{c}{Spanner 3} &  \\\\ \n\\cmidrule(lr){1-2} \\cmidrule(lr){4-5} \\cmidrule(lr){7-7}\nnum & char & fctr & date & time & datetime & currency & group \\\\ \n\\midrule\\addlinespace[2.5pt]"
    )


def test_create_columns_component_l_many_spanners():

    gt_tbl = (
        GT(exibble)
        .tab_spanner(label="Spanner 1", columns=["num", "char"])
        .tab_spanner(label="Spanner 2", columns=["date", "time"])
        .tab_spanner(label="Spanner 3", columns=["currency", "row"])
        .tab_spanner(label="Spanner Above 1", columns=["char", "fctr"])
        .tab_spanner(label="Spanner Above 2", columns=["time", "datetime"])
    )

    width_dict = create_width_dict_l(gt_tbl)

    assert (
        create_columns_component_l(data=gt_tbl, width_dict=width_dict)
        == "\\toprule\n & \\multicolumn{2}{c}{Spanner Above 1} &  & \\multicolumn{2}{c}{Spanner Above 2} &  \\\\ \n\\cmidrule(lr){2-3} \\cmidrule(lr){5-6}\n\\multicolumn{2}{c}{Spanner 1} &  & \\multicolumn{2}{c}{Spanner 2} &  & \\multicolumn{2}{c}{Spanner 3} &  \\\\ \n\\cmidrule(lr){1-2} \\cmidrule(lr){4-5} \\cmidrule(lr){7-8}\nnum & char & fctr & date & time & datetime & currency & row & group \\\\ \n\\midrule\\addlinespace[2.5pt]"
    )


def test_create_body_component_l_simple(gt_tbl: GT):

    width_dict = create_width_dict_l(gt_tbl)

    assert create_body_component_l(data=gt_tbl, width_dict=width_dict) == "1 & 4 \\\\\n2 & 5 \\\\"


def test_create_body_component_l_fmt_number(gt_tbl: GT):

    gt_tbl_built = gt_tbl.fmt_number(columns="x", rows=0, decimals=3, scale_by=-1)._build_data(
        context="latex"
    )

    assert (
        create_body_component_l(data=gt_tbl_built, width_dict=create_width_dict_l(gt_tbl_built))
        == "-1.000 & 4 \\\\\n2 & 5 \\\\"
    )


def test_create_footer_component_one_note(gt_tbl: GT):

    gt_tbl_new = gt_tbl.tab_source_note(source_note="Source Note.")

    assert (
        create_footer_component_l(gt_tbl_new)
        == "\\begin{minipage}{\\linewidth}\nSource Note.\\\\\n\\end{minipage}"
    )


def test_create_footer_component_two_notes(gt_tbl: GT):

    gt_tbl_new = gt_tbl.tab_source_note(source_note="Source Note 1.").tab_source_note(
        source_note="Source Note 2."
    )

    assert (
        create_footer_component_l(gt_tbl_new)
        == "\\begin{minipage}{\\linewidth}\nSource Note 1.\\\\\nSource Note 2.\\\\\n\\end{minipage}"
    )


def test_create_footer_component_no_notes(gt_tbl: GT):

    assert create_footer_component_l(gt_tbl) == ""


def test_create_body_component_l_fmt_integer(gt_tbl_dec: GT):

    gt_tbl_built = gt_tbl_dec.fmt_integer(columns="x", rows=0, scale_by=-1)._build_data(
        context="latex"
    )

    assert (
        create_body_component_l(data=gt_tbl_built, width_dict=create_width_dict_l(gt_tbl_built))
        == "-2 & 4.75 \\\\\n2.23 & 5.23 \\\\"
    )


def test_create_body_component_l_fmt_scientific(gt_tbl_sci: GT):

    gt_tbl_built = gt_tbl_sci.fmt_scientific(columns="x")._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built, width_dict=create_width_dict_l(gt_tbl_built))
        == "4.66 $\\times$ 10\\textsuperscript{5} & 4.509 \\\\\n-3.45 $\\times$ 10\\textsuperscript{-9} & 176.23 \\\\"
    )


def test_create_body_component_l_fmt_percent(gt_tbl_pct: GT):

    gt_tbl_built = gt_tbl_pct.fmt_percent(columns="x")._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built, width_dict=create_width_dict_l(gt_tbl_built))
        == "53.00\\% & 0.17 \\\\\n6.74\\% & 0.32 \\\\"
    )


def test_create_body_component_l_fmt_currency(gt_tbl_dec: GT):

    gt_tbl_built = gt_tbl_dec.fmt_currency(columns="x")._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built, width_dict=create_width_dict_l(gt_tbl_built))
        == "\\$1.52 & 4.75 \\\\\n\\$2.23 & 5.23 \\\\"
    )


def test_create_body_component_l_fmt_date(gt_tbl_dttm: GT):

    gt_tbl_built = gt_tbl_dttm.fmt_date(
        columns="date", date_style="wday_month_day_year"
    )._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built, width_dict=create_width_dict_l(gt_tbl_built))
        == "Saturday, August 12, 2023 & 09:21:23 & 2023-08-12 09:21:23 \\\\\nTuesday, November 17, 2020 & 22:45:02 & 2020-11-17 22:45:02 \\\\"
    )


def test_create_body_component_l_fmt_time(gt_tbl_dttm: GT):

    gt_tbl_built = gt_tbl_dttm.fmt_time(columns="time", time_style="h_m_s_p")._build_data(
        context="latex"
    )

    assert (
        create_body_component_l(data=gt_tbl_built, width_dict=create_width_dict_l(gt_tbl_built))
        == "2023-08-12 & 9:21:23 AM & 2023-08-12 09:21:23 \\\\\n2020-11-17 & 10:45:02 PM & 2020-11-17 22:45:02 \\\\"
    )


def test_create_body_component_l_fmt_datetime(gt_tbl_dttm: GT):

    gt_tbl_built = gt_tbl_dttm.fmt_datetime(
        columns="dttm", date_style="wday_month_day_year", time_style="h_m_s_p"
    )._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built, width_dict=create_width_dict_l(gt_tbl_built))
        == "2023-08-12 & 09:21:23 & Saturday, August 12, 2023 9:21:23 AM \\\\\n2020-11-17 & 22:45:02 & Tuesday, November 17, 2020 10:45:02 PM \\\\"
    )


def test_create_wrap_start(gt_tbl: GT):

    assert create_wrap_start_l(gt_tbl) == "\\begin{table}[!t]"
    assert create_wrap_start_l(gt_tbl.tab_options(latex_tbl_pos="!b")) == "\\begin{table}[!b]"
    assert create_wrap_start_l(gt_tbl.tab_options(latex_use_longtable=True)) == "\\begingroup"


@mock.patch.dict(os.environ, {"QUARTO_BIN_PATH": "1"}, clear=True)
def test_create_wrap_start_quarto(gt_tbl: GT):

    assert create_wrap_start_l(gt_tbl) == "\\begin{table}"
    assert create_wrap_start_l(gt_tbl.tab_options(latex_use_longtable=True)) == "\\begingroup"


def test_create_wrap_end_l(gt_tbl: GT):

    assert create_wrap_end_l(gt_tbl) == "\\end{table}"
    assert create_wrap_end_l(gt_tbl.tab_options(latex_use_longtable=True)) == "\\endgroup"
