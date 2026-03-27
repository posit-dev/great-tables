import pytest
import pandas as pd

from great_tables import GT, exibble, loc, style
from great_tables.data import gtcars
from great_tables._text import (
    _typst_escape,
    _md_typst,
    _process_text,
    escape_pattern_str_typst,
    Md,
    Html,
    Text,
)
from great_tables._utils_render_typst import (
    create_table_start_typst,
    create_heading_component_typst,
    create_columns_component_typst,
    create_body_component_typst,
    create_footer_component_typst,
    _render_as_typst,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Text escaping tests
# ---------------------------------------------------------------------------


class TestTypstEscape:
    def test_escape_hash(self):
        assert _typst_escape("use #func") == "use \\#func"

    def test_escape_dollar(self):
        assert _typst_escape("$100") == "\\$100"

    def test_escape_at(self):
        assert _typst_escape("@ref") == "\\@ref"

    def test_escape_angle_brackets(self):
        assert _typst_escape("<label>") == "\\<label\\>"

    def test_escape_asterisk(self):
        assert _typst_escape("*bold*") == "\\*bold\\*"

    def test_escape_underscore(self):
        assert _typst_escape("_italic_") == "\\_italic\\_"

    def test_escape_backtick(self):
        assert _typst_escape("`code`") == "\\`code\\`"

    def test_escape_tilde(self):
        assert _typst_escape("a~b") == "a\\~b"

    def test_escape_brackets(self):
        assert _typst_escape("[content]") == "\\[content\\]"

    def test_escape_backslash(self):
        assert _typst_escape("a\\b") == "a\\\\b"

    def test_no_escape_plain(self):
        assert _typst_escape("hello world 123") == "hello world 123"

    def test_escape_multiple_specials(self):
        assert _typst_escape("$100 @ref #fn") == "\\$100 \\@ref \\#fn"


class TestMdTypst:
    def test_bold(self):
        assert _md_typst("**bold**") == "*bold*"

    def test_italic_underscore(self):
        assert _md_typst("_italic_") == "_italic_"

    def test_italic_asterisk(self):
        assert _md_typst("*italic*") == "_italic_"

    def test_bold_italic(self):
        assert _md_typst("***bold italic***") == "*_bold italic_*"

    def test_bold_with_nested_italic(self):
        assert _md_typst("**_bold italic_**") == "*_bold italic_*"

    def test_plain(self):
        assert _md_typst("plain text") == "plain text"

    def test_link(self):
        assert (
            _md_typst("[click here](https://example.com)")
            == '#link("https://example.com")[click here]'
        )

    def test_link_with_bold(self):
        assert (
            _md_typst("[**bold link**](https://example.com)")
            == '#link("https://example.com")[*bold link*]'
        )

    def test_inline_code(self):
        assert _md_typst("`code`") == "`code`"

    def test_inline_code_preserves_special_chars(self):
        assert _md_typst("`$100 + #tag`") == "`$100 + #tag`"

    def test_strikethrough(self):
        assert _md_typst("~~deleted~~") == "#strike[deleted]"

    def test_escape_dollar(self):
        assert _md_typst("price is $100") == "price is \\$100"

    def test_escape_hash(self):
        assert _md_typst("item #1") == "item \\#1"

    def test_escape_at(self):
        assert _md_typst("email@test") == "email\\@test"

    def test_escape_angle_brackets(self):
        assert _md_typst("a < b > c") == "a \\< b \\> c"

    def test_backslash_escape(self):
        assert _md_typst("\\*not bold\\*") == "\\*not bold\\*"

    def test_mixed_formatting(self):
        result = _md_typst("**bold** and _italic_ and `code`")
        assert result == "*bold* and _italic_ and `code`"

    def test_multiple_bold_segments(self):
        assert _md_typst("**a** and **b**") == "*a* and *b*"


class TestProcessTextTypst:
    def test_plain_string_escapes(self):
        assert _process_text("$100", context="typst") == "\\$100"

    def test_none_returns_empty(self):
        assert _process_text(None, context="typst") == ""

    def test_text_object_passthrough(self):
        assert _process_text(Text("hello"), context="typst") == "hello"

    def test_md_object(self):
        result = _process_text(Md("**bold**"), context="typst")
        assert result == "*bold*"

    def test_html_object_warns_and_escapes(self):
        with pytest.warns(match="won't convert HTML to Typst"):
            result = _process_text(Html("<b>bold</b>"), context="typst")
        assert "\\<" in result


class TestEscapePatternStrTypst:
    def test_preserves_placeholder(self):
        assert escape_pattern_str_typst("{x} $") == "{x} \\$"

    def test_preserves_numbered_placeholder(self):
        assert escape_pattern_str_typst("{x} #tag") == "{x} \\#tag"

    def test_no_escape_needed(self):
        assert escape_pattern_str_typst("{x} units") == "{x} units"


# ---------------------------------------------------------------------------
# Renderer component tests
# ---------------------------------------------------------------------------


class TestCreateTableStartTypst:
    def test_basic_table(self, gt_tbl: GT):
        result = create_table_start_typst(gt_tbl)
        assert "#table(" in result
        assert "columns: 2" in result

    def test_alignment(self):
        gt = GT(pd.DataFrame({"a": ["x"], "b": [1]})).cols_align(align="right", columns="b")
        result = create_table_start_typst(gt)
        assert "right" in result


class TestCreateHeadingComponentTypst:
    def test_no_heading(self, gt_tbl: GT):
        assert create_heading_component_typst(gt_tbl, n_cols=2) == ""

    def test_title_only(self):
        gt = GT(exibble).tab_header(title="Title")
        result = create_heading_component_typst(gt, n_cols=9)
        assert "Title" in result
        assert "bold" in result
        assert "colspan: 9" in result

    def test_title_and_subtitle(self):
        gt = GT(exibble).tab_header(title="Title", subtitle="Subtitle")
        result = create_heading_component_typst(gt, n_cols=9)
        assert "Title" in result
        assert "Subtitle" in result


class TestCreateColumnsComponentTypst:
    def test_simple_columns(self):
        gt = GT(exibble)
        result = create_columns_component_typst(gt)
        assert "table.header(" in result
        # Default column_labels_font_weight is "normal" (not bold)
        assert "[num]" in result
        assert "[char]" in result

    def test_bold_columns(self):
        gt = GT(exibble).tab_options(column_labels_font_weight="bold")
        result = create_columns_component_typst(gt)
        assert "[*num*]" in result
        assert "[*char*]" in result

    def test_one_spanner(self):
        gt = GT(exibble).tab_spanner(label="Spanner", columns=["num", "char"])
        result = create_columns_component_typst(gt)
        assert "table.cell(colspan: 2" in result
        assert "Spanner" in result

    def test_hidden_cols(self):
        gt = GT(exibble).cols_hide(columns=["char", "date"])
        result = create_columns_component_typst(gt)
        assert "[char]" not in result
        assert "[date]" not in result
        assert "[num]" in result


class TestCreateBodyComponentTypst:
    def test_simple_body(self, gt_tbl: GT):
        built = gt_tbl._build_data(context="typst")
        result = create_body_component_typst(built)
        assert "[1]" in result
        assert "[4]" in result
        assert "[2]" in result
        assert "[5]" in result

    def test_body_row_count(self, gt_tbl: GT):
        built = gt_tbl._build_data(context="typst")
        result = create_body_component_typst(built)
        # Two data rows (plus any body border hlines from options)
        data_lines = [
            line
            for line in result.strip().split("\n")
            if line.strip() and "table.hline" not in line
        ]
        assert len(data_lines) == 2


class TestCreateFooterComponentTypst:
    def test_no_notes(self, gt_tbl: GT):
        assert create_footer_component_typst(gt_tbl, n_cols=2) == ""

    def test_one_note(self, gt_tbl: GT):
        gt = gt_tbl.tab_source_note(source_note="Source Note.")
        result = create_footer_component_typst(gt, n_cols=2)
        assert "Source Note." in result
        assert "text(size:" in result
        assert "table.cell(" in result
        assert "colspan: 2" in result

    def test_two_notes(self, gt_tbl: GT):
        gt = gt_tbl.tab_source_note(source_note="Note 1.").tab_source_note(source_note="Note 2.")
        result = create_footer_component_typst(gt, n_cols=2)
        assert "Note 1." in result
        assert "Note 2." in result

    def test_footer_has_fill(self, gt_tbl: GT):
        """Footer should always have fill to prevent striping bleed."""
        gt = gt_tbl.tab_source_note(source_note="Note.")
        result = create_footer_component_typst(gt, n_cols=2)
        assert "fill:" in result


class TestRenderAsTypst:
    def test_basic_render(self, gt_tbl: GT):
        built = gt_tbl._build_data(context="typst")
        result = _render_as_typst(built)
        assert "#table(" in result
        assert "table.header(" in result
        assert ")" in result

    def test_render_with_heading(self):
        gt = GT(pd.DataFrame({"x": [1]})).tab_header(title="My Title")
        built = gt._build_data(context="typst")
        result = _render_as_typst(built)
        assert "My Title" in result
        assert "#table(" in result

    def test_render_with_source_note(self, gt_tbl: GT):
        gt = gt_tbl.tab_source_note(source_note="A note.")
        built = gt._build_data(context="typst")
        result = _render_as_typst(built)
        assert "A note." in result


# ---------------------------------------------------------------------------
# Format context tests (fmt_* with context="typst")
# ---------------------------------------------------------------------------


class TestFmtNumberTypst:
    def test_basic(self, gt_tbl_dec: GT):
        built = gt_tbl_dec.fmt_number(columns="x", decimals=3)._build_data(context="typst")
        result = create_body_component_typst(built)
        assert "[1.520]" in result

    def test_pattern_escapes_typst_chars(self, gt_tbl_dec: GT):
        built = gt_tbl_dec.fmt_number(columns="x", rows=0, decimals=2, pattern="{x} $")._build_data(
            context="typst"
        )
        result = create_body_component_typst(built)
        # Dollar sign should be escaped in Typst
        assert "\\$" in result


class TestFmtIntegerTypst:
    def test_basic(self, gt_tbl_dec: GT):
        built = gt_tbl_dec.fmt_integer(columns="x")._build_data(context="typst")
        result = create_body_component_typst(built)
        assert "[2]" in result


class TestFmtPercentTypst:
    def test_basic(self, gt_tbl_pct: GT):
        built = gt_tbl_pct.fmt_percent(columns="x")._build_data(context="typst")
        result = create_body_component_typst(built)
        # Percent should NOT be escaped in Typst (unlike LaTeX's \%)
        assert "53.00%" in result


class TestFmtCurrencyTypst:
    def test_basic(self, gt_tbl_dec: GT):
        built = gt_tbl_dec.fmt_currency(columns="x")._build_data(context="typst")
        result = create_body_component_typst(built)
        # Dollar sign should be escaped in Typst
        assert "\\$" in result


class TestFmtScientificTypst:
    def test_basic(self, gt_tbl_sci: GT):
        built = gt_tbl_sci.fmt_scientific(columns="x")._build_data(context="typst")
        result = create_body_component_typst(built)
        # Should have Typst math mode for exponent
        assert "×" in result or "times" in result


class TestFmtDateTypst:
    def test_basic(self, gt_tbl_dttm: GT):
        built = gt_tbl_dttm.fmt_date(columns="date", date_style="wday_month_day_year")._build_data(
            context="typst"
        )
        result = create_body_component_typst(built)
        assert "Saturday" in result or "August" in result


class TestFmtTimeTypst:
    def test_basic(self, gt_tbl_dttm: GT):
        built = gt_tbl_dttm.fmt_time(columns="time", time_style="h_m_s_p")._build_data(
            context="typst"
        )
        result = create_body_component_typst(built)
        assert "AM" in result or "PM" in result


class TestTableOptionsTypst:
    def test_font_size(self, gt_tbl: GT):
        gt = gt_tbl.tab_options(table_font_size="18px")
        result = gt.as_typst()
        assert "size: 13.5pt" in result

    def test_column_widths(self):
        gt = GT(pd.DataFrame({"a": [1], "b": [2]})).cols_width({"a": "100px", "b": "200px"})
        result = create_table_start_typst(gt)
        assert "75pt" in result
        assert "150pt" in result

    def test_row_striping(self, gt_tbl: GT):
        gt = gt_tbl.opt_row_striping()
        result = create_table_start_typst(gt)
        assert "fill:" in result
        assert "calc.odd" in result


class TestSubMissingZeroTypst:
    def test_sub_missing(self):
        gt = GT(pd.DataFrame({"x": [1.0, None, 3.0]})).sub_missing(columns="x")
        result = gt.as_typst()
        # Default missing text is em dash (—)
        assert "—" in result

    def test_sub_missing_custom_text(self):
        gt = GT(pd.DataFrame({"x": [1.0, None, 3.0]})).sub_missing(columns="x", missing_text="N/A")
        result = gt.as_typst()
        assert "N/A" in result

    def test_sub_zero(self):
        gt = GT(pd.DataFrame({"x": [1, 0, 3]})).sub_zero(columns="x")
        result = gt.as_typst()
        assert "nil" in result

    def test_sub_zero_custom_text(self):
        gt = GT(pd.DataFrame({"x": [1, 0, 3]})).sub_zero(columns="x", zero_text="--")
        result = gt.as_typst()
        assert "--" in result


class TestFmtMarkdownTypst:
    def test_basic(self):
        gt = GT(pd.DataFrame({"x": ["**bold**", "_italic_"]})).fmt_markdown(columns="x")
        result = gt.as_typst()
        # Typst bold is *...*, italic is _..._
        assert "*bold*" in result


class TestRowGroupsAndStub:
    def test_row_groups(self):
        gt = GT(exibble, groupname_col="group")
        result = gt.as_typst()
        # Should have group label rows spanning all columns
        assert "table.cell(colspan:" in result
        # Underscores get escaped in Typst
        assert "grp\\_a" in result or "grp_a" in result

    def test_stub_column(self):
        gt = GT(exibble, rowname_col="row")
        result = gt.as_typst()
        # Stub adds an extra column and bold row labels (underscores escaped in Typst)
        assert "row\\_1" in result or "row\\_2" in result

    def test_groups_and_stub(self):
        gt = GT(exibble, rowname_col="row", groupname_col="group")
        result = gt.as_typst()
        assert "table.cell(colspan:" in result
        assert "#table(" in result


class TestDataColorTypst:
    def test_data_color_basic(self):
        gt = GT(pd.DataFrame({"x": [1, 5, 10]})).data_color(columns="x", palette=["red", "green"])
        result = gt.as_typst()
        # data_color applies fill styles — should see table.cell with fill
        assert "table.cell(" in result
        assert "fill:" in result

    def test_data_color_autocolor_text(self):
        gt = GT(pd.DataFrame({"x": [1, 5, 10]})).data_color(
            columns="x", palette=["#000000", "#FFFFFF"], autocolor_text=True
        )
        result = gt.as_typst()
        # Should have both fill and text styling
        assert "fill:" in result
        assert "text(" in result


class TestCellStylingTypst:
    def test_fill_style(self):
        gt = GT(pd.DataFrame({"x": [1, 2]})).tab_style(
            style=style.fill(color="#FF0000"),
            locations=loc.body(columns="x", rows=[0]),
        )
        built = gt._build_data(context="typst")
        result = create_body_component_typst(built)
        assert "table.cell(" in result
        assert 'fill: rgb("#FF0000")' in result

    def test_text_color_style(self):
        gt = GT(pd.DataFrame({"x": [1, 2]})).tab_style(
            style=style.text(color="blue"),
            locations=loc.body(columns="x", rows=[0]),
        )
        built = gt._build_data(context="typst")
        result = create_body_component_typst(built)
        assert "text(" in result
        assert "fill: blue" in result

    def test_border_style(self):
        gt = GT(pd.DataFrame({"x": [1, 2]})).tab_style(
            style=style.borders(sides="bottom", color="#000000", weight="2px"),
            locations=loc.body(columns="x", rows=[0]),
        )
        built = gt._build_data(context="typst")
        result = create_body_component_typst(built)
        assert "table.cell(" in result
        assert "stroke:" in result


class TestPolarsBackend:
    def test_basic_polars_table(self):
        import polars as pl

        gt = GT(pl.DataFrame({"x": [1, 2], "y": [4, 5]}))
        result = gt.as_typst()
        assert "#table(" in result
        assert "[1]" in result

    def test_polars_with_formatting(self):
        import polars as pl

        gt = GT(pl.DataFrame({"x": [1.52, 2.23]})).fmt_number(columns="x", decimals=1)
        result = gt.as_typst()
        assert "[1.5]" in result

    def test_polars_with_grouping(self):
        import polars as pl

        df = pl.DataFrame({"val": [1, 2, 3], "grp": ["a", "a", "b"]})
        gt = GT(df, groupname_col="grp")
        result = gt.as_typst()
        assert "table.cell(colspan:" in result


# ---------------------------------------------------------------------------
# typst() helper, Typst text class, and fmt_typst() tests
# ---------------------------------------------------------------------------


class TestTypstTextClass:
    def test_to_typst_passes_through(self):
        """Typst content should pass through as-is in typst context."""
        from great_tables._text import Typst

        t = Typst("#text(fill: red)[Warning]")
        assert t.to_typst() == "#text(fill: red)[Warning]"

    def test_to_typst_no_escaping(self):
        """Special chars in Typst content should NOT be escaped."""
        from great_tables._text import Typst

        t = Typst("$ x^2 + y^2 $")
        assert t.to_typst() == "$ x^2 + y^2 $"

    def test_to_html_warns(self):
        """Typst content in HTML context should warn."""
        from great_tables._text import Typst

        t = Typst("#text(fill: red)[Warning]")
        with pytest.warns(match="won't convert Typst to HTML"):
            result = t.to_html()
        # Should escape HTML-special chars
        assert isinstance(result, str)

    def test_to_latex_warns(self):
        """Typst content in LaTeX context should warn."""
        from great_tables._text import Typst

        t = Typst("#text(fill: red)[Warning]")
        with pytest.warns(match="won't convert Typst to LaTeX"):
            result = t.to_latex()
        assert isinstance(result, str)

    def test_process_text_typst_context(self):
        """_process_text with Typst object in typst context passes through."""
        from great_tables._text import Typst

        result = _process_text(Typst("$ alpha $"), context="typst")
        assert result == "$ alpha $"

    def test_process_text_html_context_warns(self):
        """_process_text with Typst object in html context warns."""
        from great_tables._text import Typst

        with pytest.warns(match="won't convert Typst to HTML"):
            _process_text(Typst("#strong[x]"), context="html")


class TestTypstHelper:
    def test_returns_typst_instance(self):
        """typst() helper should return a Typst instance."""
        from great_tables import typst
        from great_tables._text import Typst

        result = typst("#text(fill: blue)[Hello]")
        assert isinstance(result, Typst)
        assert result.text == "#text(fill: blue)[Hello]"

    def test_in_tab_header(self):
        """typst() should work in tab_header for Typst output."""
        from great_tables import typst

        gt = GT(pd.DataFrame({"x": [1]})).tab_header(title=typst("#text(fill: red)[Red Title]"))
        result = gt.as_typst()
        # Should contain the raw Typst, not escaped
        assert "#text(fill: red)[Red Title]" in result


class TestFmtTypst:
    def test_typst_context_passes_through(self):
        """fmt_typst should pass raw Typst through in typst context."""
        gt = GT(pd.DataFrame({"x": ["#strong[bold]", "$ x^2 $"]})).fmt_typst(columns="x")
        result = gt.as_typst()
        assert "#strong[bold]" in result
        assert "$ x^2 $" in result

    def test_html_context_raises(self):
        """fmt_typst should raise NotImplementedError in HTML context."""
        gt = GT(pd.DataFrame({"x": ["#strong[bold]"]})).fmt_typst(columns="x")
        with pytest.raises(NotImplementedError):
            gt.as_raw_html()


class TestAsTypstMethod:
    def test_as_typst_returns_string(self, gt_tbl: GT):
        result = gt_tbl.as_typst()
        assert isinstance(result, str)
        assert "#table(" in result

    def test_as_typst_via_render(self, gt_tbl: GT):
        result = gt_tbl.render(context="typst")
        assert isinstance(result, str)
        assert "#table(" in result

    def test_save_typst(self, gt_tbl: GT, tmp_path):
        f = tmp_path / "table.typ"
        gt_tbl.save(str(f))
        assert f.exists()
        content = f.read_text()
        assert "#table(" in content

    def test_snap_as_typst(self, snapshot):
        gt = (
            GT(
                gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
            )
            .tab_header(title="The _title_", subtitle="The subtitle")
            .tab_spanner(label="Make and Model", columns=["mfr", "model"])
            .tab_spanner(label="Performance", columns=["hp", "trq"])
            .fmt_currency(columns="msrp")
            .tab_source_note("Note 1")
            .tab_source_note("Note 2")
        )

        typst_str = gt.as_typst()
        assert snapshot == typst_str


# ---------------------------------------------------------------------------
# Grand summary rows tests
# ---------------------------------------------------------------------------


def _mean_expr(df):
    return df.mean(numeric_only=True)


def _max_expr(df):
    return df.max(numeric_only=True)


def _min_expr(df):
    return df.min(numeric_only=True)


class TestGrandSummaryTypst:
    def test_basic_grand_summary_bottom(self):
        df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        gt = GT(df).grand_summary_rows(fns={"Average": _mean_expr})
        result = gt.as_typst()
        # Summary row label should appear
        assert "Average" in result
        # Summary values should appear (mean of a=2, b=5 — integer-valued floats strip .0)
        assert "[2]" in result or "2," in result
        assert "[5]" in result or "5," in result

    def test_grand_summary_top(self):
        df = pd.DataFrame({"a": [1, 2, 3]})
        gt = GT(df).grand_summary_rows(fns={"Min": _min_expr}, side="top")
        result = gt.as_typst()
        assert "Min" in result
        assert "1" in result

    def test_grand_summary_top_and_bottom(self):
        df = pd.DataFrame({"a": [1, 2, 3]})
        gt = (
            GT(df)
            .grand_summary_rows(fns={"Top": _min_expr}, side="top")
            .grand_summary_rows(fns={"Bottom": _max_expr}, side="bottom")
        )
        result = gt.as_typst()
        assert "Top" in result
        assert "Bottom" in result

    def test_grand_summary_with_stub(self):
        df = pd.DataFrame({"a": [1, 2], "b": [4, 5], "row": ["x", "y"]})
        gt = GT(df, rowname_col="row").grand_summary_rows(fns={"Average": _mean_expr})
        result = gt.as_typst()
        assert "Average" in result
        # Row labels should also appear
        assert "x" in result
        assert "y" in result

    def test_grand_summary_missing_values(self):
        df = pd.DataFrame({"a": [1, 2], "non_numeric": ["x", "y"]})
        gt = GT(df).grand_summary_rows(fns={"Average": _mean_expr}, missing_text="N/A")
        result = gt.as_typst()
        assert "Average" in result
        assert "N/A" in result

    def test_grand_summary_without_stub_adds_stub_column(self):
        """When there's no explicit rowname_col, summary rows still need a label column."""
        df = pd.DataFrame({"a": [1, 2]})
        gt = GT(df).grand_summary_rows(fns={"Sum": _max_expr})
        result = gt.as_typst()
        # The summary label "Sum" should appear
        assert "Sum" in result

    def test_grand_summary_with_hline_separator(self):
        """Summary rows should have visual separation from data rows."""
        df = pd.DataFrame({"a": [1, 2]})
        gt = GT(df).grand_summary_rows(fns={"Total": _max_expr})
        result = gt.as_typst()
        assert "table.hline(" in result
