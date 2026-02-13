import pytest
from unittest import mock
import pandas as pd
import os

from great_tables import GT, exibble
from great_tables.data import gtcars

from great_tables._utils_render_latex import (
    is_css_length_string,
    is_number_without_units,
    css_length_has_supported_units,
    get_px_conversion,
    get_units_from_length_string,
    convert_to_px,
    convert_to_pt,
    create_wrap_start_l,
    create_fontsize_statement_l,
    create_heading_component_l,
    create_body_component_l,
    create_columns_component_l,
    create_footer_component_l,
    create_wrap_end_l,
    create_table_end_l,
    create_table_start_l,
    derive_table_width_statement_l,
    _render_as_latex,
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
    assert is_css_length_string("12.5units")


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
    assert not css_length_has_supported_units("12.8units")
    assert not css_length_has_supported_units("units12.8")


def test_get_units_from_length_string():
    assert get_units_from_length_string("12.5pt") == "pt"
    assert get_units_from_length_string("") == "px"


def test_get_px_conversion_val():
    assert get_px_conversion(length="2343.23pt") == 4 / 3
    assert get_px_conversion(length="43.2px") == 1.0


def test_get_px_conversion_val_raises():
    with pytest.raises(ValueError) as exc_info:
        get_px_conversion(length="12.8bolts")

    assert "Invalid units: bolts" in exc_info.value.args[0]


def test_convert_to_px():
    assert convert_to_px("12.5pt") == 17.0
    assert convert_to_px("12.5px") == 12.5


def test_convert_to_pt():
    assert convert_to_pt("16px") == 12.0


def test_create_fontsize_statement_l(gt_tbl: GT):
    assert create_fontsize_statement_l(gt_tbl) == "\\fontsize{12.0pt}{14.4pt}\\selectfont\n"


def test_create_fontsize_statement_l_pt(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_font_size="18.2pt")

    assert create_fontsize_statement_l(gt_tbl_new) == "\\fontsize{18.2pt}{21.8pt}\\selectfont\n"


def test_create_fontsize_statement_l_px(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_font_size="11px")

    assert create_fontsize_statement_l(gt_tbl_new) == "\\fontsize{8.2pt}{9.9pt}\\selectfont\n"


def test_create_fontsize_statement_l_pct(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_font_size="50%")

    assert create_fontsize_statement_l(gt_tbl_new) == "\\fontsize{6.0pt}{7.2pt}\\selectfont\n"


def test_create_fontsize_statement_l_cm(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_font_size="0.6cm")

    assert create_fontsize_statement_l(gt_tbl_new) == "\\fontsize{17.2pt}{20.7pt}\\selectfont\n"


def test_create_fontsize_statement_l_unknown_unit(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_font_size="1span")

    assert create_fontsize_statement_l(gt_tbl_new) == ""


def test_derive_table_width_statement_l_px_lt(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_width="500px")

    assert (
        derive_table_width_statement_l(gt_tbl_new, use_longtable=True)
        == "\\setlength\\LTleft{\\dimexpr(0.5\\linewidth - 187.5pt)}\n\\setlength\\LTright{\\dimexpr(0.5\\linewidth - 187.5pt)}"
    )


def test_derive_table_width_statement_l_pct_lt(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_width="45%")

    assert (
        derive_table_width_statement_l(gt_tbl_new, use_longtable=True)
        == "\\setlength\\LTleft{0.275\\linewidth}\n\\setlength\\LTright{0.275\\linewidth}"
    )


def test_derive_table_width_statement_l_px_no_lt(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_width="500px")

    assert derive_table_width_statement_l(gt_tbl_new, use_longtable=False) == ""


def test_create_fontsize_statement_l_settings():
    gt_tbl = GT(exibble).tab_options(table_font_size="18.5px")

    assert create_fontsize_statement_l(gt_tbl) == "\\fontsize{13.9pt}{16.6pt}\\selectfont\n"


def test_create_heading_component_l():
    gt_tbl_no_heading = GT(exibble)
    gt_tbl_title = GT(exibble).tab_header(title="Title")
    gt_tbl_title_subtitle = GT(exibble).tab_header(title="Title", subtitle="Subtitle")

    assert create_heading_component_l(gt_tbl_no_heading, use_longtable=False) == ""
    assert (
        create_heading_component_l(gt_tbl_title, use_longtable=False)
        == "\\caption*{\n{\\large Title}\n} "
    )
    assert (
        create_heading_component_l(gt_tbl_title_subtitle, use_longtable=False)
        == "\\caption*{\n{\\large Title} \\\\\n{\\small Subtitle}\n} "
    )


def test_create_columns_component_l_simple():
    gt_tbl = GT(exibble)

    assert (
        create_columns_component_l(data=gt_tbl)
        == "\\toprule\nnum & char & fctr & date & time & datetime & currency & row & group \\\\ \n\\midrule\\addlinespace[2.5pt]"
    )


def test_create_columns_component_l_simple_hidden_cols():
    gt_tbl = GT(exibble).cols_hide(columns=["char", "date"])

    assert (
        create_columns_component_l(data=gt_tbl)
        == "\\toprule\nnum & fctr & time & datetime & currency & row & group \\\\ \n\\midrule\\addlinespace[2.5pt]"
    )


def test_create_columns_component_l_one_spanner():
    gt_tbl = GT(exibble).tab_spanner(label="Spanner", columns=["num", "char"])

    assert (
        create_columns_component_l(data=gt_tbl)
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

    assert (
        create_columns_component_l(data=gt_tbl)
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

    assert (
        create_columns_component_l(data=gt_tbl)
        == "\\toprule\n & \\multicolumn{2}{c}{Spanner Above 1} &  & \\multicolumn{2}{c}{Spanner Above 2} &  \\\\ \n\\cmidrule(lr){2-3} \\cmidrule(lr){5-6}\n\\multicolumn{2}{c}{Spanner 1} &  & \\multicolumn{2}{c}{Spanner 2} &  & \\multicolumn{2}{c}{Spanner 3} &  \\\\ \n\\cmidrule(lr){1-2} \\cmidrule(lr){4-5} \\cmidrule(lr){7-8}\nnum & char & fctr & date & time & datetime & currency & row & group \\\\ \n\\midrule\\addlinespace[2.5pt]"
    )


def test_create_body_component_l_simple(gt_tbl: GT):
    assert create_body_component_l(data=gt_tbl) == "1 & 4 \\\\\n2 & 5 \\\\"


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


def test_create_body_component_l_fmt_number(gt_tbl_dec: GT):
    gt_tbl_built = gt_tbl_dec.fmt_number(
        columns="x", rows=0, scale_by=-1, decimals=3, pattern="{x} _"
    )._build_data(context="latex")

    assert create_body_component_l(data=gt_tbl_built) == "-1.520 \\_ & 4.75 \\\\\n2.23 & 5.23 \\\\"


def test_create_body_component_l_fmt_integer(gt_tbl_dec: GT):
    gt_tbl_built = gt_tbl_dec.fmt_integer(
        columns="x", rows=0, scale_by=-1, pattern="{x} _"
    )._build_data(context="latex")

    assert create_body_component_l(data=gt_tbl_built) == "-2 \\_ & 4.75 \\\\\n2.23 & 5.23 \\\\"


def test_create_body_component_l_fmt_scientific(gt_tbl_sci: GT):
    gt_tbl_built = gt_tbl_sci.fmt_scientific(columns="x", pattern="{x} _")._build_data(
        context="latex"
    )

    assert (
        create_body_component_l(data=gt_tbl_built)
        == "4.66 $\\times$ 10\\textsuperscript{5} \\_ & 4.509 \\\\\n-3.45 $\\times$ 10\\textsuperscript{-9} \\_ & 176.23 \\\\"
    )


def test_create_body_component_l_fmt_percent(gt_tbl_pct: GT):
    gt_tbl_built = gt_tbl_pct.fmt_percent(columns="x", pattern="{x} _")._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built)
        == "53.00\\% \\_ & 0.17 \\\\\n6.74\\% \\_ & 0.32 \\\\"
    )


def test_create_body_component_l_fmt_currency(gt_tbl_dec: GT):
    gt_tbl_built = gt_tbl_dec.fmt_currency(columns="x", pattern="{x} _")._build_data(
        context="latex"
    )

    assert (
        create_body_component_l(data=gt_tbl_built)
        == "\\$1.52 \\_ & 4.75 \\\\\n\\$2.23 \\_ & 5.23 \\\\"
    )


def test_create_body_component_l_fmt_bytes(gt_tbl_sci: GT):
    gt_tbl_built = gt_tbl_sci.fmt_bytes(columns="x", pattern="{x} _")._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built)
        == "465.6 kB \\_ & 4.509 \\\\\n0 B \\_ & 176.23 \\\\"
    )


def test_create_body_component_l_fmt_date(gt_tbl_dttm: GT):
    gt_tbl_built = gt_tbl_dttm.fmt_date(
        columns="date", date_style="wday_month_day_year", pattern="{x} _"
    )._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built)
        == "Saturday, August 12, 2023 \\_ & 09:21:23 & 2023-08-12 09:21:23 \\\\\nTuesday, November 17, 2020 \\_ & 22:45:02 & 2020-11-17 22:45:02 \\\\"
    )


def test_create_body_component_l_fmt_time(gt_tbl_dttm: GT):
    gt_tbl_built = gt_tbl_dttm.fmt_time(
        columns="time", time_style="h_m_s_p", pattern="{x} _"
    )._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built)
        == "2023-08-12 & 9:21:23 AM \\_ & 2023-08-12 09:21:23 \\\\\n2020-11-17 & 10:45:02 PM \\_ & 2020-11-17 22:45:02 \\\\"
    )


def test_create_body_component_l_fmt_datetime(gt_tbl_dttm: GT):
    gt_tbl_built = gt_tbl_dttm.fmt_datetime(
        columns="dttm", date_style="wday_month_day_year", time_style="h_m_s_p", pattern="{x} _"
    )._build_data(context="latex")

    assert (
        create_body_component_l(data=gt_tbl_built)
        == "2023-08-12 & 09:21:23 & Saturday, August 12, 2023 9:21:23 AM \\_ \\\\\n2020-11-17 & 22:45:02 & Tuesday, November 17, 2020 10:45:02 PM \\_ \\\\"
    )


def test_create_body_component_l_fmt_roman(gt_tbl_dec: GT):
    gt_tbl_built = gt_tbl_dec.fmt_roman(columns="x", rows=0, pattern="{x} _")._build_data(
        context="latex"
    )

    assert create_body_component_l(data=gt_tbl_built) == "II \\_ & 4.75 \\\\\n2.23 & 5.23 \\\\"


def test_create_wrap_start():
    assert create_wrap_start_l(use_longtable=False, tbl_pos=None) == "\\begin{table}[!t]"
    assert create_wrap_start_l(use_longtable=False, tbl_pos="!b") == "\\begin{table}[!b]"
    assert create_wrap_start_l(use_longtable=True, tbl_pos=None) == "\\begingroup"


@mock.patch.dict(os.environ, {"QUARTO_BIN_PATH": "1"}, clear=True)
def test_create_wrap_start_quarto():
    assert create_wrap_start_l(use_longtable=False, tbl_pos="!t") == "\\begin{table}"
    assert create_wrap_start_l(use_longtable=True, tbl_pos="!t") == "\\begingroup"


def test_create_wrap_end_l():
    assert create_wrap_end_l(use_longtable=False) == "\\end{table}"
    assert create_wrap_end_l(use_longtable=True) == "\\endgroup"


def test_create_table_end_l_longtable():
    assert create_table_end_l(use_longtable=False) == "\\bottomrule\n\\end{tabular*}"
    assert create_table_end_l(use_longtable=True) == "\\bottomrule\n\\end{longtable}"


def test_create_table_start_l_longtable(gt_tbl: GT):
    gt_tbl_no_source_notes = gt_tbl._build_data(context="latex")
    gt_tbl_source_notes = gt_tbl.tab_source_note(source_note="Note")._build_data(context="latex")

    assert (
        create_table_start_l(
            data=gt_tbl_no_source_notes,
            use_longtable=True,
        )
        == "\\begin{longtable}{rr}"
    )

    assert (
        create_table_start_l(
            data=gt_tbl_source_notes,
            use_longtable=True,
        )
        == "\\setlength{\\LTpost}{0mm}\n\\begin{longtable}{rr}"
    )


def test_create_table_start_l_float_tbl_pct(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_width="50%")

    assert (
        create_table_start_l(
            data=gt_tbl_new,
            use_longtable=False,
        )
        == "\\begin{tabular*}{0.5\\linewidth}{@{\\extracolsep{\\fill}}rr}"
    )


def test_create_table_start_l_float_tbl_px(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_width="500px")

    assert (
        create_table_start_l(
            data=gt_tbl_new,
            use_longtable=False,
        )
        == "\\begin{tabular*}{375.0pt}{@{\\extracolsep{\\fill}}rr}"
    )


def test_create_table_start_l_float_tbl_auto(gt_tbl: GT):
    gt_tbl_new = gt_tbl.tab_options(table_width="auto")

    assert (
        create_table_start_l(
            data=gt_tbl_new,
            use_longtable=False,
        )
        == "\\begin{tabular*}{\\linewidth}{@{\\extracolsep{\\fill}}rr}"
    )


def test_snap_render_as_latex_longtable(snapshot):
    gt_tbl = (
        GT(
            gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
        )
        .tab_header(title="The _title_", subtitle="The subtitle")
        .tab_spanner(label="Make _and_ Model", columns=["mfr", "model"])
        .tab_spanner(label="Performance", columns=["hp", "trq"])
        .fmt_currency(columns="msrp")
        .tab_source_note("Note 1")
        .tab_source_note("Note 2")
        .tab_options(table_width="600px", table_font_size="12px")
    )

    latex_str = _render_as_latex(
        data=gt_tbl._build_data(context="latex"), use_longtable=True, tbl_pos=None
    )

    assert snapshot == latex_str


def test_snap_render_as_latex_floating_table(snapshot):
    gt_tbl = (
        GT(
            gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
        )
        .tab_header(title="The _title_", subtitle="The subtitle")
        .tab_spanner(label="Make _and_ Model", columns=["mfr", "model"])
        .tab_spanner(label="Performance", columns=["hp", "trq"])
        .fmt_currency(columns="msrp")
        .tab_source_note("Note 1")
        .tab_source_note("Note 2")
        .tab_options(table_width="600px", table_font_size="12px")
    )

    latex_str = _render_as_latex(
        data=gt_tbl._build_data(context="latex"), use_longtable=False, tbl_pos=None
    )

    assert snapshot == latex_str


def test_render_as_latex_stub_raises():
    gt_tbl = GT(exibble, rowname_col="row")
    with pytest.raises(NotImplementedError) as exc_info:
        _render_as_latex(data=gt_tbl._build_data(context="latex"))

    assert (
        "The table stub (row names and/or row groups) are not yet supported in LaTeX output."
        in exc_info.value.args[0]
    )


def test_render_as_latex_rowgroup_raises():
    gt_tbl = GT(exibble, groupname_col="group")
    with pytest.raises(NotImplementedError) as exc_info:
        _render_as_latex(data=gt_tbl._build_data(context="latex"))

    assert "Row groups are not yet supported in LaTeX output." in exc_info.value.args[0]
