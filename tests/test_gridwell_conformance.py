"""`GT.as_gridwell()` checked with gridwell itself (https://github.com/rich-iannone/gridwell).

gridwell reads the IR, validates it and draws it in each of its formats. Its conformance kit (copied
in `tests/gridwell_kit/`) checks each case's IR against the case's expected grid (tiers L1 to L3),
and other tables against the grid of Great Tables' own HTML. Skipped when gridwell isn't
installed.
"""

from __future__ import annotations

import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import pandas as pd
import pytest

from great_tables import GT, exibble, html, loc, md, style
from tests.test_gridwell import (
    KIT,
    TABLES,
    TIMES,
    kit_cases,
    make_html_body_gt,
    make_shown_numbers_gt,
    make_typed_gt,
    stub_data,
)

gridwell = pytest.importorskip("gridwell")
conformance = pytest.importorskip("gridwell.conformance")

TEXT_FORMATS = ["html", "latex", "typst", "rtf", "svg", "ansi", "pandoc", "quarto"]
BINARY_FORMATS = ["docx", "xlsx", "pptx"]


def table_of(gt: GT) -> Any:
    return gridwell.Table.from_json(gt.as_gridwell())


def html_grid() -> Any:
    """The kit's reader of the grid of Great Tables' HTML."""
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("gridwell_kit_html_grid", KIT / "html_grid.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# The kit's cases -------------------------------------------------------------------------------


@pytest.mark.parametrize("name", sorted(kit_cases()))
def test_each_kit_case_conforms_to_its_expected_grid(name: str):
    gt = kit_cases()[name]["build"]()
    report = conformance.assert_conforms(gt.as_gridwell(), KIT / "expected" / f"{name}.json")
    assert report.tier == "L3"


def test_the_expected_grids_catch_a_wrong_table():
    # Not vacuous: one case's table doesn't conform to another case's grid, nor a cell changed
    cases = kit_cases()
    first, second = sorted(cases)[:2]
    assert not conformance.check(
        cases[first]["build"]().as_gridwell(), KIT / "expected" / f"{second}.json"
    ).passed
    ir = json.loads(cases[first]["build"]().as_gridwell())
    cell = next(
        c for g in ir["table"]["tbody"] for r in g["rows"] for c in r["cells"] if c["content"]
    )
    cell["content"] = [{"type": "text", "value": "not what it was"}]
    report = conformance.check(json.dumps(ir), KIT / "expected" / f"{first}.json")
    assert not report.passed
    assert any("not what it was" in str(d.actual) for d in report.differences)


def edge_tables() -> dict[str, GT]:
    """Tables beyond the kit's cases, for what the IR has of labels, spanners and summary rows."""
    df = pd.DataFrame(
        {
            "a": [1, 2, 3],
            "b": [4.5, 5.5, 6.5],
            "c": ["x", "y", "z"],
            "d": [7, 8, 9],
            "g": ["G1", "G1", "G2"],
            "r": ["r1", "r2", "r3"],
        }
    )
    return {
        "grand summary, no stub": GT(df[["a", "b", "d"]]).grand_summary_rows(
            fns={
                "Sum": lambda x: x[["a", "d"]].sum(),
                "**Mean**": lambda x: x.mean(numeric_only=True),
            }
        ),
        # Summary values are put in Great Tables' HTML as they are
        "summary values as HTML": GT(df[["a", "b"]]).grand_summary_rows(
            fns={"Sum": lambda x: x.sum()},
            fmt=lambda x: [f"<b>{v:.1f}</b>&nbsp;&amp;" for v in x],
        ),
        "summaries on top": GT(df[["a", "b", "g", "r"]], rowname_col="r", groupname_col="g")
        .summary_rows(fns={"Max": lambda x: x[["a", "b"]].max()}, side="top")
        .grand_summary_rows(fns={"Min": lambda x: x[["a"]].min()}, side="top"),
        "group summaries, no stub": GT(df[["a", "b", "g"]], groupname_col="g").summary_rows(
            fns={"Max <1>": lambda x: x[["a", "b"]].max()}
        ),
        "unspanned columns under a higher level": GT(df[["a", "b", "c", "d"]])
        .tab_spanner("Low", ["c", "d"])
        .tab_spanner("High", spanners=["Low"]),
        "spanner levels apart": GT(df[["a", "b", "c", "d"]])
        .tab_spanner("Low", ["a", "b"])
        .tab_spanner("High", ["a", "b", "d"]),
        "hidden column under a spanner": GT(df[["a", "b", "c", "d"]])
        .tab_spanner("S", ["b", "c", "d"])
        .cols_hide("c"),
        "stub under spanners": GT(df[["r", "a", "b", "d"]], rowname_col="r")
        .tab_spanner("S", ["a", "b"])
        .tab_spanner("T", ["a", "b", "d"])
        .tab_stubhead("Rows"),
        "markup in labels": GT(df, rowname_col="r", groupname_col="g")
        .tab_header(title=md("A *b* **c**"), subtitle=html("x<br>y <code>z</code>"))
        .cols_label(a=md("**A**"), b=html("B<sub>2</sub>"), c="c < d & e")
        .tab_spanner(md("*Span*"), ["c", "d"])
        .tab_stubhead(md("**Stub**"))
        .tab_footnote(md("Note *one*"), locations=loc.column_labels(columns="a"))
        .tab_footnote("Plain <two> & more", locations=loc.title())
        .tab_source_note(html("<p>Para one</p><p>Para <b>two</b></p>"))
        .tab_source_note("a < b"),
        "plain strings stay text": GT(df[["a", "b"]])
        .cols_label(a="*not md* <b>", b="x\ny")
        .tab_header(title="Tom & Jerry's <script>")
        .tab_source_note("  spaced   out  "),
        # Body cells are the HTML Great Tables puts in them: `fmt_*()` output, or the data
        # escaped
        "HTML in body cells": GT(
            pd.DataFrame(
                {
                    "r": ["a < b & c", "<b>not bold</b>"],
                    "m": ["**md** *it*\n\npara `two`", "- x\n- y"],
                    "sci": [0.000123, 12345.6],
                    "u": ["{{m^2 s_1}}", "{{kg m^-1}}"],
                    "h": [
                        "<svg><text>T</text></svg> &amp; <i>x</i>",
                        "<sup>2q</sup> 10<sup>2<br>3</sup>",
                    ],
                }
            ),
            rowname_col="r",
        )
        .fmt_markdown("m")
        .fmt_scientific("sci")
        .fmt_units("u")
        .fmt(lambda x: x, columns="h"),
        "entities and paragraphs": GT(df[["a"]])
        .tab_header(title=html("A&nbsp;B &amp; C&#x2014;D"))
        .tab_source_note(md("line one\n\nline two"))
        .tab_source_note(html("<p>x</p><br>y<br><br><div>z</div><p></p>")),
        "merged and transformed columns": GT(exibble[["num", "char", "currency"]].head(3))
        .fmt_currency("currency")
        .cols_merge(["num", "char"], pattern="{0} / {1}")
        .text_transform(loc.body(columns="currency"), lambda x: "X" + x),
        "indented stub": GT(exibble[["num", "row"]].head(3), rowname_col="row").tab_stub_indent(
            rows=[1], indent=2
        ),
        **stub_cases(),
    }


def stub_cases() -> dict[str, GT]:
    """Tables with a stub of several columns or a row group column."""
    st = stub_data()
    total = {"Total": lambda x: x[["v", "w"]].sum()}

    def multi(**kw: Any) -> GT:
        return GT(st, rowname_col=["o", "i"], groupname_col="g", **kw)

    def as_column(gt: GT) -> GT:
        return gt.tab_options(row_group_as_column=True)

    return {
        "stub of two columns, in groups": multi().tab_spanner("S", ["v", "w"]).tab_stubhead("Rows"),
        "stub of two columns, no groups": GT(st.iloc[[0, 1, 3, 4]], rowname_col=["o", "i"]),
        # (Row 3's "x" is beside row 4's, under another "g": not merged)
        "stub of three columns": GT(st.iloc[[2, 0, 1, 3, 4]], rowname_col=["g", "o", "i"]),
        "spanner levels over a stub of two columns": GT(st, rowname_col=["o", "i"])
        .tab_spanner("S1", ["v", "w"])
        .tab_spanner("S0", ["w"])
        .tab_spanner("Top", ["v", "w"], level=2),
        "a stubhead label for each stub column": multi().tab_stubhead(["A", "B"]),
        "notes on merged stub cells": multi()
        .tab_footnote("outer", locations=loc.stub(rows=[1], columns="o"))
        .tab_footnote("plain", locations=loc.stub(rows=[0])),
        "row group column": as_column(GT(st[["g", "i", "v"]], rowname_col="i", groupname_col="g")),
        "row group column, no stub": as_column(GT(st[["g", "i", "v"]], groupname_col="g")),
        "row group column and a stub of two columns": as_column(multi())
        .tab_spanner("S1", ["v", "w"])
        .tab_spanner("S2", ["v"], level=0),
        "row group column, a stubhead label for each stub column": as_column(
            multi().tab_stubhead(["A", "B"])
        ),
        "row group column, striped": as_column(multi().opt_row_striping()).tab_options(
            row_striping_include_stub=True
        ),
        "row group column, styled": as_column(multi()).tab_style(
            style.text(weight="bold"), loc.row_groups()
        ),
        "row group column, grand summary": as_column(multi()).grand_summary_rows(fns=total),
    }


EDGE_TABLES = edge_tables()


@pytest.mark.parametrize("name", EDGE_TABLES)
def test_the_ir_has_what_great_tables_html_shows(name: str):
    gt = EDGE_TABLES[name]
    seen = html_grid().grid(gt.as_raw_html())
    report = conformance.check(gt.as_gridwell(), seen)
    assert report.passed, str(report)


@pytest.mark.parametrize("stub", [["i"], ["o", "i"]])
def test_a_row_group_columns_summaries_differ_from_great_tables_html_as_known(stub: list[str]):
    # Great Tables' group cell spans the group's summary rows too; the IR's can't (a rowspan
    # stays in its group's rows), so its summary rows start with an empty stub cell under it
    gt = (
        GT(stub_data()[["g", *stub, "v", "w"]], rowname_col=stub, groupname_col="g")
        .tab_options(row_group_as_column=True)
        .summary_rows(fns={"Sum": lambda x: x[["v", "w"]].sum()})
    )
    ir = gt.as_gridwell()
    seen = html_grid().grid(gt.as_raw_html())
    assert not conformance.check(ir, seen, tier="L1").passed
    for group in seen["grid"]["groups"]:
        assert group["rows"][0]["cells"][0]["rowspan"] == len(group["rows"]) + 1
        group["rows"][0]["cells"][0]["rowspan"] = len(group["rows"])
        for row in group["summary_rows"]:
            row["cells"].insert(0, {"col": 0, "stub": True, "text": ""})
    report = conformance.check(ir, seen, tier="L1")
    assert report.passed, str(report)


def test_a_gt_is_checked_as_its_ir():
    gt = GT(exibble.head(2))
    grid = conformance.normalize(gt.as_gridwell())
    assert conformance.normalize(gt) == grid
    assert conformance.check(gt, grid).passed
    assert not conformance.check(GT(exibble.head(3)), grid).passed


# Validating and drawing ------------------------------------------------------------------------

ALL = {**TABLES, **{f"edge: {k}": v for k, v in EDGE_TABLES.items()}}


@pytest.mark.parametrize("name", ALL)
def test_gridwell_validates_the_ir(name: str):
    assert table_of(ALL[name]).validate() == []


@pytest.mark.parametrize("name", TABLES)
@pytest.mark.parametrize("fmt", TEXT_FORMATS)
def test_gridwell_draws_the_ir_in_each_text_format(name: str, fmt: str):
    assert table_of(TABLES[name]).render(fmt)


@pytest.mark.parametrize("name", TABLES)
@pytest.mark.parametrize("fmt", BINARY_FORMATS)
def test_gridwell_draws_the_ir_in_each_binary_format(name: str, fmt: str):
    assert table_of(TABLES[name]).render_binary(fmt)[:4] == b"PK\x03\x04"


def test_gridwell_takes_a_gt_directly():
    gt = TABLES["grouped"]
    expected = json.loads(gridwell.parse_ir(gt.as_gridwell()).to_json())
    assert json.loads(gridwell.Table(gt).to_json()) == expected
    assert 'titled "Example Table"' in repr(gridwell.Table(gt))


def test_labels_and_body_html_are_drawn_in_every_format():
    table = table_of(make_html_body_gt())
    out = table.render("html")
    assert "<svg width='8'><svg/><text>T</text></svg>" in out
    assert f"1.23{TIMES}10⁻⁴" in out and "&lt;b&gt;not bold&lt;/b&gt;" in out
    ansi = table.render("ansi")
    assert "m² s₁" in ansi and "a < b & c" in ansi
    labeled = table_of(
        GT(exibble[["num"]].head(1))
        .tab_header(title=md("A *b* **c**"))
        .cols_label(num=html("N<sub>2</sub>"))
    )
    # Labels are drawn as styled text, not as their markup
    for fmt in TEXT_FORMATS:
        drawn = labeled.render(fmt)
        assert "*b*" not in drawn and "**c**" not in drawn and "<sub>" not in drawn, fmt
    assert "N₂" in labeled.render("ansi") and "N₂" in labeled.render("html")


def test_superscripts_are_the_characters_gridwell_draws():
    # gridwell lowers raw HTML itself for formats other than HTML; the IR's superscripts and
    # subscripts are the same characters
    from great_tables._gridwell import _SCRIPTS

    for tag, chars in _SCRIPTS.items():
        ir = json.loads(GT(pd.DataFrame({"x": [1]})).as_gridwell())
        ir["table"]["tbody"][0]["rows"][0]["cells"][0]["content"] = [
            {"type": "raw", "format": "html", "value": f"<{tag}>{''.join(chars)}</{tag}>"}
        ]
        assert "".join(chars.values()) in gridwell.Table(json.dumps(ir)).render("ansi"), tag


@pytest.mark.parametrize(
    "locale, lang, direction", [("ar_EG", "ar-EG", "rtl"), ("fr_CA", "fr-CA", None)]
)
def test_a_locale_is_drawn_as_the_tables_language(locale: str, lang: str, direction: str | None):
    out = table_of(GT(pd.DataFrame({"x": [1.5]}), locale=locale)).render_html()
    assert f'lang="{lang}"' in out
    assert ('dir="rtl"' in out) == (direction == "rtl")
    plain = table_of(GT(pd.DataFrame({"x": [1.5]}))).render_html()
    assert "lang=" not in plain and "dir=" not in plain


def _header_ids(markup: str) -> dict[str, list[Any]]:
    """The ids of the `<th>` cells, the `headers` of the `<td>` cells, and the table's aria
    attributes, in document order."""
    found: dict[str, list[Any]] = {"th": [], "td": [], "table": []}

    class Parser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            a = dict(attrs)
            if tag == "th":
                found["th"].append(a.get("id"))
            elif tag == "td" and "headers" in a:
                found["td"].append(a["headers"])
            elif tag == "table":
                found["table"].append((a.get("aria-labelledby"), a.get("aria-describedby")))

    Parser().feed(markup)
    return found


@pytest.mark.parametrize("table_id", [None, "sales"])
def test_header_ids_are_great_tables_ids(table_id: str | None):
    df = pd.DataFrame(
        {
            "name": ["Oslo", "Bergen", "Rome"],
            "grp": ["North East", "North East", "South"],
            "x (km)": [1, 2, 3],
            "y": [4, 5, 6],
        }
    )
    gt = GT(df, rowname_col="name", groupname_col="grp", id=table_id).tab_header(
        title="Sales", subtitle="By region"
    )
    ours = table_of(gt).render_html()
    theirs = _header_ids(gt.as_raw_html())
    assert _header_ids(ours) == theirs
    # Not vacuous: every kind of header is there
    p = "" if table_id is None else "sales-"
    assert theirs["th"] == [
        None,  # the blank stubhead
        f"{p}x-km",
        f"{p}y",
        f"{p}North-East",
        f"{p}stub-1",
        f"{p}stub-2",
        f"{p}South",
        f"{p}stub-3",
    ]
    assert theirs["td"][0] == f"{p}North-East {p}stub-1 {p}x-km"
    assert theirs["table"] == [(f"{p}title", f"{p}subtitle")]
    if table_id is not None:
        assert ours.startswith('<div id="sales"')


class _BodyRows(HTMLParser):
    """The first cell's text of each row in a table body."""

    def __init__(self):
        super().__init__()
        self.rows: list[str | None] = []
        self._in_body = False
        self._cell: str | None = None

    def handle_starttag(self, tag, attrs):
        if tag == "tbody":
            self._in_body = True
        elif tag == "tr" and self._in_body:
            self.rows.append(None)
        elif tag in ("th", "td") and self._in_body and self.rows and self.rows[-1] is None:
            self._cell = ""

    def handle_endtag(self, tag):
        if tag == "tbody":
            self._in_body = False
        elif tag in ("th", "td") and self._cell is not None:
            self.rows[-1], self._cell = self._cell.strip(), None

    def handle_data(self, data):
        if self._cell is not None:
            self._cell += data


def body_rows(markup: str) -> list[str | None]:
    parser = _BodyRows()
    parser.feed(markup)
    return parser.rows


def test_summary_rows_are_drawn_where_great_tables_draws_them():
    total = lambda x: x[["num"]].sum()  # noqa: E731
    gt = (
        GT(exibble[["num", "row", "group"]].head(4), rowname_col="row", groupname_col="group")
        .summary_rows(fns={"Top": total}, side="top")
        .grand_summary_rows(fns={"First": total}, side="top")
        .grand_summary_rows(fns={"Last": total})
    )
    ours = body_rows(table_of(gt).render_html())
    assert ours == body_rows(gt.as_raw_html())
    assert ours[:3] == ["First", "grp_a", "Top"] and ours[-1] == "Last"


# XLSX: typed cells -----------------------------------------------------------------------------


def _xlsx_cells(data: bytes, row: int) -> dict[str, Any]:
    """Each cell in sheet row `row`: a number's or boolean's (type, value), else "text"."""
    sheet = zipfile.ZipFile(io.BytesIO(data)).read("xl/worksheets/sheet1.xml").decode()
    found = re.search(rf'<row r="{row}".*?</row>', sheet)
    assert found is not None
    got: dict[str, Any] = {}
    for col, attrs, body in re.findall(rf'<c r="([A-Z]+){row}"([^>]*)>(.*?)</c>', found.group(0)):
        t = re.search(r' t="(\w+)"', attrs)
        kind = t.group(1) if t else "n"
        value = re.search(r"<v>(.*?)</v>", body)
        got[col] = (kind, value.group(1) if value else None) if kind in ("n", "b") else "text"
    return got


def _xlsx_number_formats(data: bytes, row: int) -> dict[str, Any]:
    """Each typed number cell's value and format code in sheet row `row`."""
    z = zipfile.ZipFile(io.BytesIO(data))
    styles = z.read("xl/styles.xml").decode()
    codes = {
        int(i): c.replace("&quot;", '"')
        for i, c in re.findall(r'<numFmt numFmtId="(\d+)" formatCode="([^"]*)"', styles)
    }
    codes.update({0: "General", 1: "0", 2: "0.00", 3: "#,##0", 4: "#,##0.00", 9: "0%", 10: "0.00%"})
    xfs = re.search(r"<cellXfs[^>]*>(.*?)</cellXfs>", styles, re.S)
    assert xfs is not None
    fmt_ids = [
        int(m.group(1))
        for x in re.findall(r"<xf [^>]*>", xfs.group(1))
        if (m := re.search(r'numFmtId="(\d+)"', x))
    ]
    sheet = z.read("xl/worksheets/sheet1.xml").decode()
    out: dict[str, Any] = {}
    for col, attrs, body in re.findall(rf'<c r="([A-Z]+){row}"([^>]*)>(.*?)</c>', sheet):
        if " t=" in attrs:
            out[col] = "text"
            continue
        s = re.search(r' s="(\d+)"', attrs)
        value = re.search(r"<v>(.*?)</v>", body)
        out[col] = (
            value.group(1) if value else None,
            codes[fmt_ids[int(s.group(1))]] if s else "General",
        )
    return out


def test_typed_values_are_typed_xlsx_cells():
    data = table_of(make_typed_gt()).render_binary("xlsx")
    assert _xlsx_cells(data, 2) == {
        "A": ("b", "1"),  # TRUE
        "B": ("n", "1"),
        "C": ("n", "0.5"),
        "D": ("n", "45366"),  # 2024-03-15
        "E": ("n", "45366.604166666664"),  # 14:30
        "F": ("n", "0.6041666666666666"),
        "G": ("n", "-1.5"),
        "H": ("n", "49.95"),  # $49.95
        "I": "text",  # "x"
        "J": ("b", "1"),
        "K": ("n", "45366.604166666664"),
    }


def test_shown_numbers_are_xlsx_numbers_formatted_as_shown():
    data = table_of(make_shown_numbers_gt()).render_binary("xlsx")
    # Other marks are the reader's (Excel shows a number in its own locale's)
    assert _xlsx_number_formats(data, 2) == {
        "A": ("1234.5", "#,##0.00"),
        "B": ("1234.5", "#,##0.00"),
        "C": ("0.451", "0.0%"),
        "D": ("49.95", '"$"0.00'),
        "E": ("49.95", '"$"0.00'),
        "F": ("49.95", '"€"0.00'),
        # Scientific notation stays as shown
        "G": "text",
        "H": ("1230000", '0.00,,"M"'),
        "I": ("1234.5", '"+"#,##0.00'),
        "J": ("1234.5", '#,##0.00" kg"'),
        "K": ("1234", "#,##0"),
        "L": ("1234", "#,##0.000"),
    }
    assert _xlsx_number_formats(data, 3) == {
        "A": ("-98765.43", '#,##0.00;"−"#,##0.00'),
        "B": ("0.25", "0.00"),
        "C": ("-0.012", '0.0%;"−"0.0%'),
        "D": ("-5", '"$"0.00;"−$"0.00'),
        "E": ("-5", '"$"0.00;"($"0.00")"'),
        "F": ("-5", '"€"0.00;"−€"0.00'),
        "G": "text",
        "H": ("0.5", "0.00"),
        "I": ("-2", '0.00;"−"0.00'),
        "J": ("2", '0.00" kg"'),
        "K": ("-5", '0;"−"0'),
        "L": ("1.234", "0.000"),
    }


# The kit's copy --------------------------------------------------------------------------------


@pytest.mark.skipif(
    not os.environ.get("GRIDWELL_DIR"), reason="set GRIDWELL_DIR to a gridwell checkout"
)
def test_the_kit_is_the_one_in_gridwell():
    script = Path(__file__).parent.parent / "scripts" / "sync_gridwell_kit.py"
    result = subprocess.run(
        [sys.executable, str(script), "--check"], capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, result.stdout + result.stderr
