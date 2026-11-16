"""`GT.as_gridwell()`: the IR of gridwell (https://github.com/rich-iannone/gridwell) for a table.

These tests don't need gridwell: they check the IR against its JSON Schema (tier L0, with the
schema copied in `tests/gridwell_kit/`) and against what Great Tables draws (its HTML).
`tests/test_gridwell_conformance.py` checks it with gridwell itself.
"""

from __future__ import annotations

import datetime as dt
import importlib.util
import json
import re
import sys
from decimal import Decimal
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest
from syrupy.assertion import SnapshotAssertion

from great_tables import GT, exibble, html, loc, md, style
from great_tables._gridwell import (
    _SCRIPTS,
    _css_style,
    _infer_data_type,
    _lower_html,
    _typed_value,
    build_ir,
)
from tests.utils import INT_UPCAST, DataFrameConstructor, assert_parity

KIT = Path(__file__).parent / "gridwell_kit"

# The " × " of scientific notation, as Great Tables writes it
TIMES = "\xa0×\xa0"


def ir_of(gt: GT) -> dict[str, Any]:
    return json.loads(gt.as_gridwell())


def kit_cases() -> dict[str, Any]:
    """The conformance cases of gridwell's kit: name to {"description", "build"}."""
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("gridwell_kit_cases", KIT / "cases.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.cases


def text_of(cell: dict[str, Any]) -> str:
    return "".join(n.get("value", "") for n in cell["content"])


def nodes(ir: Any):
    """Every content node of the IR."""
    if isinstance(ir, dict):
        if "type" in ir and ("value" in ir or "mark_text" in ir):
            yield ir
        for v in ir.values():
            yield from nodes(v)
    elif isinstance(ir, list):
        for v in ir:
            yield from nodes(v)


def defs_of(ir: dict[str, Any], style_id: str | None) -> dict[str, Any]:
    return ir["styles"]["defs"].get(style_id, {}) if style_id else {}


def runs(ir: dict[str, Any], content: list[dict[str, Any]]) -> list[tuple[str, Any]]:
    """Content nodes as (text, style definition) pairs; a line break is ("\\n", None) and a
    footnote mark ("^" + its text, its footnote's id)."""
    defs = ir["styles"]["defs"]
    return [
        ("\n", None)
        if n["type"] == "line_break"
        else ("^" + n["mark_text"], n["ref"])
        if n["type"] == "footnote_mark"
        else (n["value"], defs[n["style_id"]] if n["type"] == "styled_text" else None)
        for n in content
    ]


def shape(row: dict[str, Any]) -> list[Any]:
    """A row's cells as (text, rowspan, colspan, scope, is_stub); a placeholder is "·"."""
    out: list[Any] = []
    for c in row["cells"]:
        if c["is_placeholder"]:
            assert c["content"] == [] and c["rowspan"] == c["colspan"] == 1
            out.append("·")
        else:
            out.append((text_of(c), c["rowspan"], c["colspan"], c.get("scope"), c["is_stub"]))
    return out


# Tables ----------------------------------------------------------------------------------------


def make_simple_gt():
    return GT(exibble.head(3))


def make_grouped_gt():
    return (
        GT(exibble, rowname_col="row", groupname_col="group")
        .tab_header(title="Example Table", subtitle="From exibble dataset")
        .tab_source_note(source_note="Source: great_tables package")
    )


def make_styled_gt():
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Carol"],
            "score": [95.5, 87.2, 91.8],
            "grade": ["A", "B+", "A-"],
        }
    )
    return (
        GT(df)
        .cols_label(name="Student Name", score="Test Score", grade="Letter Grade")
        .cols_align(align="center", columns="grade")
    )


def make_minimal_gt():
    return GT(pd.DataFrame({"x": [42]}))


def make_typed_gt():
    """A column of each typed kind, some formatted."""
    df = pd.DataFrame(
        {
            "b": [True, False],
            "i": [1, 2],
            "f": [0.5, 1234.5],
            "d": [dt.date(2024, 3, 15), dt.date(2024, 3, 16)],
            "ts": pd.to_datetime(["2024-03-15 14:30:00", "2024-03-15 09:05:30"]),
            "t": [dt.time(14, 30), dt.time(9, 5, 3)],
            "neg": [-1.5, -2.24],
            "cur": [49.95, 1.5],
            "s": ["x", "y"],
            # Booleans and datetimes in object columns, typed by their values
            "ob": pd.Series([True, False], dtype=object),
            "odt": pd.Series([dt.datetime(2024, 3, 15, 14, 30)] * 2, dtype=object),
        }
    )
    return (
        GT(df)
        .fmt_number(columns="f", decimals=1)
        .fmt_number(columns="neg", decimals=1)
        .fmt_date(columns="d", date_style="month_day_year")
        .fmt_currency(columns="cur")
    )


def make_shown_numbers_gt():
    """Numbers displayed in other locales' marks, as currencies, percentages, in scientific and
    compact notation, and with signs and units."""
    df = pd.DataFrame(
        {
            "de": [1234.5, -98765.4321],
            "fr": [1234.5, 0.25],
            "pct": [0.4512, -0.0123],
            "cur": [49.95, -5.0],
            "acc": [49.95, -5.0],
            "eur": [49.95, -5.0],
            "sci": [0.000123, 123456.0],
            "cmp": [1234567.0, 0.5],
            "sgn": [1234.5, -2.0],
            "kg": [1234.5, 2.0],
            "i": [1234, -5],
            "big": [1234.0, 1.234],
        }
    )
    return (
        GT(df)
        .fmt_number("de", decimals=2, locale="de")
        .fmt_number("fr", decimals=2, locale="fr")
        .fmt_percent("pct", decimals=1)
        .fmt_currency("cur")
        .fmt_currency("acc", accounting=True)
        .fmt_currency("eur", currency="EUR", locale="de")
        .fmt_scientific("sci")
        .fmt_number("cmp", compact=True)
        .fmt_number("sgn", decimals=2, force_sign=True)
        .fmt_number("kg", decimals=2, pattern="{x} kg")
        .fmt_integer("i")
        .fmt_number("big", decimals=3)
    )


def make_footnoted_gt():
    """Footnotes added out of reading order, one text on two cells, one without a mark."""
    return (
        GT(exibble[["char", "num"]].head(3))
        .tab_header(title="Title")
        .tab_footnote("Body note.", locations=loc.body(columns="char", rows=[1]))
        .tab_footnote("Label note.", locations=loc.column_labels(columns="num"))
        .tab_footnote("Title note.", locations=loc.title())
        .tab_footnote("Body note.", locations=loc.body(columns="num", rows=[2]))
        .tab_footnote("A general note.")
    )


def make_html_body_gt():
    """`fmt_*()` output that is HTML, and HTML of other kinds, in body cells."""
    df = pd.DataFrame(
        {
            "s": ["a < b & c", "<b>not bold</b>"],
            "m": ["**md** *it*\n\npara `two`", "x"],
            "sci": [0.000123, 12345.6],
            "u": ["{{m^2 s_1}}", "kg"],
            "img": ["a.png", "b.png"],
            "h": [
                # An SVG as written, the text around it kept; one never closed runs on
                "<svg width='8'><svg/><text>T</text></svg> &amp; <i>x</i><svg/>",
                "<sup>2q</sup> 10<sup>2<br>3</sup> <sub>a1</sub><svg><text>open",
            ],
            "i": [
                # Sizes: a number is pixels, `style` beats the attribute, ones the IR can't take
                # are dropped; `src` is only copied
                '<img src=" /no/such/file.png " alt="A" width="12" height="9" style="height: 2em !important">',
                '<img src="x.png" width="calc(1px)" style="width: -3px; height: auto">x',
            ],
        }
    )
    return (
        GT(df, rowname_col="s")
        .fmt_markdown("m")
        .fmt_scientific("sci")
        .fmt_units("u")
        # (A URL: Great Tables reads a local path itself to embed it)
        .fmt_image("img", path="https://example.invalid", height=20)
        .fmt(lambda x: x, columns=["h", "i"])
        .tab_footnote("Note.", locations=loc.body(columns="sci", rows=[0]))
    )


def everywhere(id: str | None = None):
    """A style and a footnote at every kind of location Great Tables has."""
    df = pd.DataFrame(
        {
            "r": ["r1", "r2", "r3"],
            "g": ["G1", "G1", "G2"],
            "a": [1, 2, 3],
            "b": [4.5, 5.5, 6.5],
            "c": ["x", "y", "z"],
            "d": [7, 8, 9],
        }
    )
    text_color = lambda c: style.text(color=c)  # noqa: E731
    return (
        GT(df, rowname_col="r", groupname_col="g", id=id)
        .tab_header(title="Title", subtitle="Sub")
        .tab_stubhead("Stubhead")
        .tab_spanner("Low", ["a", "b"])
        .tab_spanner("High", ["a", "b", "c"])
        .summary_rows(fns={"Max": lambda x: x[["a", "b", "d"]].max()})
        .grand_summary_rows(fns={"Sum": lambda x: x[["a", "b", "d"]].sum()})
        .tab_source_note("Source.")
        .tab_style(text_color("#000001"), loc.header())
        .tab_style([style.fill("#EEEEE1"), style.text(weight="bold")], loc.title())
        .tab_style(style.text(style="italic", size="12px"), loc.subtitle())
        .tab_style(style.fill("#EEEEE2"), loc.stubhead())
        .tab_style(style.borders(sides="bottom", color="#123456", weight=3), loc.column_header())
        .tab_style(text_color("#000002"), loc.column_labels(columns=["a", "d"]))
        .tab_style(text_color("#000003"), loc.spanner_labels(ids=["Low"]))
        .tab_style(style.fill("#EEEEE3"), loc.row_groups(rows=["G2"]))
        .tab_style(text_color("#000004"), loc.stub(rows=[1]))
        .tab_style(
            [style.fill("#EEEEE4"), style.text(font="Courier New, monospace", align="right")],
            loc.body(columns="c", rows=[0, 2]),
        )
        # Later declarations win: the fill of row 2's c cell is #EEEEE5
        .tab_style(style.fill("#EEEEE5"), loc.body(columns="c", rows=[2]))
        .tab_style(text_color("#000005"), loc.body(columns="a"))
        .tab_style(text_color("#000006"), loc.summary(columns="b"))
        .tab_style(text_color("#000007"), loc.grand_summary(columns="d"))
        .tab_style(text_color("#000008"), loc.summary_stub())
        .tab_style(text_color("#000009"), loc.grand_summary_stub())
        .tab_style(style.text(transform="uppercase"), loc.footer())
        .tab_style(style.css("letter-spacing: 1px; padding: 1px 2px"), loc.source_notes())
        .tab_style(text_color("#00000A"), loc.footnotes())
        .tab_footnote("On title.", loc.title())
        .tab_footnote("On sub.", loc.subtitle(), placement="left")
        .tab_footnote("On stubhead.", loc.stubhead())
        .tab_footnote("On d.", loc.column_labels(columns="d"))
        .tab_footnote("On Low.", loc.spanner_labels(ids=["Low"]))
        .tab_footnote("On G1.", loc.row_groups(rows=["G1"]))
        .tab_footnote("On stub r3.", loc.stub(rows=[2]))
        .tab_footnote("On a, auto.", loc.body(columns="a", rows=[0]))
        .tab_footnote("On a, right.", loc.body(columns="a", rows=[1]), placement="right")
        .tab_footnote("On c, left.", loc.body(columns="c", rows=[1]), placement="left")
        .tab_footnote("On d.", loc.body(columns="d", rows=[2]))
        .tab_footnote("On d twice.", loc.body(columns="d", rows=[0]))
        .tab_footnote("On d twice, again.", loc.body(columns="d", rows=[0]))
        .tab_footnote("On summary.", loc.summary(columns="a"))
        .tab_footnote("On grand stub.", loc.grand_summary_stub())
    )


def stub_data():
    return pd.DataFrame(
        {
            "g": ["G1", "G1", "G1", "G2", "G2"],
            "o": ["x", "x", "y", "x", "x"],
            "i": ["p", "q", "r", "s", "t"],
            "v": [1, 2, 3, 4, 5],
            "w": [6, 7, 8, 9, 10],
        }
    )


def stub_tables():
    return GT(stub_data(), rowname_col=["o", "i"], groupname_col="g")


def make_themed_gt():
    return (
        GT(
            exibble[["num", "char", "row", "group"]].head(4),
            rowname_col="row",
            groupname_col="group",
        )
        .opt_stylize(style=6, color="blue")
        .opt_row_striping()
        .summary_rows(fns={"Max": lambda x: x[["num"]].max()})
        .grand_summary_rows(fns={"Sum": lambda x: x[["num"]].sum()})
        .tab_style(style.text(weight="bold"), loc.stub(rows=[1]))
        .tab_style(style.fill("#FF0000"), loc.summary_stub())
    )


def make_indented_gt():
    df = pd.DataFrame({"r": ["a", "b", "c", "d"], "g": ["x", "x", "y", "y"], "v": [1, 2, 3, 4]})
    return (
        GT(df, rowname_col="r", groupname_col="g")
        .tab_stub_indent(rows=[1], indent=3)
        .tab_stub_indent(rows=[3], indent=5)
        .summary_rows(fns={"Sum": lambda x: x[["v"]].sum()})
    )


def tables() -> dict[str, GT]:
    """Tables of every kind the emitter handles."""
    st = stub_data()
    built: dict[str, GT] = {
        "simple": make_simple_gt(),
        "grouped": make_grouped_gt(),
        "styled": make_styled_gt(),
        "minimal": make_minimal_gt(),
        "typed": make_typed_gt(),
        "shown numbers": make_shown_numbers_gt(),
        "footnoted": make_footnoted_gt(),
        "html body": make_html_body_gt(),
        "everywhere": everywhere(),
        "themed": make_themed_gt(),
        "indented": make_indented_gt(),
        "stub of two columns": stub_tables().tab_stubhead("Rows"),
        "row group column": stub_tables()
        .tab_options(row_group_as_column=True)
        .summary_rows(fns={"Sum": lambda d: d[["v", "w"]].sum()})
        .grand_summary_rows(fns={"Tot": lambda d: d[["v", "w"]].sum()}),
        "row group column, no stub": GT(st[["g", "i", "v"]], groupname_col="g").tab_options(
            row_group_as_column=True
        ),
        "summaries on top": GT(
            exibble[["num", "row", "group"]].head(4), rowname_col="row", groupname_col="group"
        )
        .summary_rows(fns={"Top": lambda x: x[["num"]].sum()}, side="top")
        .grand_summary_rows(fns={"First": lambda x: x[["num"]].sum()}, side="top"),
        "locale": GT(pd.DataFrame({"x": [1.5]}), locale="ar_EG"),
        "widths": GT(exibble[["num", "char"]].head(2))
        .tab_options(table_width="80%")
        .cols_width(num="100px"),
        "exibble, all": GT(exibble, rowname_col="row", groupname_col="group")
        .fmt_number("num", decimals=2)
        .fmt_date("date")
        .fmt_time("time")
        .fmt_datetime("datetime")
        .fmt_currency("currency")
        .sub_missing(),
    }
    for name, case in kit_cases().items():
        built[f"kit: {name}"] = case["build"]()
    return built


TABLES = tables()


# The IR as a whole -----------------------------------------------------------------------------


@pytest.fixture(scope="module")
def schema_validator():
    jsonschema = pytest.importorskip("jsonschema")
    schema = json.loads((KIT / "ir-1.0.schema.json").read_text(encoding="utf-8"))
    validator_cls = jsonschema.validators.validator_for(schema)
    validator_cls.check_schema(schema)
    return validator_cls(schema)


@pytest.mark.parametrize("name", TABLES)
def test_the_ir_is_valid_against_its_json_schema(name: str, schema_validator: Any):
    ir = ir_of(TABLES[name])
    errors = [
        f"{'/'.join(map(str, e.absolute_path))}: {e.message}"
        for e in schema_validator.iter_errors(ir)
    ]
    assert errors == []


def test_the_schema_check_finds_an_ir_that_isnt_valid(schema_validator: Any):
    # Not vacuous: the schema rejects IR without its table, with a cell spanning no columns, or
    # with a style that isn't one
    ir = ir_of(make_simple_gt())
    assert schema_validator.is_valid(ir)
    assert not schema_validator.is_valid({k: v for k, v in ir.items() if k != "table"})
    ir["table"]["tbody"][0]["rows"][0]["cells"][0]["colspan"] = 0
    assert not schema_validator.is_valid(ir)
    ir = ir_of(everywhere())
    some_def = next(iter(ir["styles"]["defs"].values()))
    some_def["font_weight"] = {"not": "a weight"}
    assert not schema_validator.is_valid(ir)


@pytest.mark.parametrize("name", TABLES)
def test_the_ir_is_the_same_json_each_time(name: str):
    gt = TABLES[name]
    first = gt.as_gridwell()
    assert gt.as_gridwell() == first
    assert first == json.dumps(build_ir(gt), indent=2)
    ir = json.loads(first)
    assert ir["ir_version"] == "1.0"
    assert ir["config"]["table_cols"] > 0


def test_as_gridwell_leaves_the_table_as_it_was():
    gt = everywhere(id="t")
    html_before = gt.as_raw_html()
    gt.as_gridwell()
    assert gt.as_raw_html() == html_before


@pytest.mark.parametrize(
    "name", [n for n in TABLES if n not in ("html body", "stub of two columns")]
)
def test_text_nodes_are_text_not_markup(name: str):
    # Markup is lowered to styled runs, and entities to their characters; only `raw` nodes have
    # markup, and only from body cells that are HTML.
    for node in nodes(ir_of(TABLES[name])):
        if node["type"] in ("text", "styled_text"):
            assert not re.search(r"</?[a-zA-Z][^>]*>|&[a-zA-Z]+;|&#", node["value"]), node


# Structure -------------------------------------------------------------------------------------


def test_groups_header_and_source_note():
    ir = ir_of(make_grouped_gt())
    tbody = ir["table"]["tbody"]
    assert [g["group_id"] for g in tbody] == ["grp_a", "grp_b"]
    assert ir["header"]["title"]["content"][0]["value"] == "Example Table"
    assert ir["header"]["subtitle"]["content"][0]["value"] == "From exibble dataset"
    (note,) = ir["footer"]["source_notes"]
    assert note["content"][0]["value"] == "Source: great_tables package"


def test_the_stub_is_a_row_header():
    ir = ir_of(make_grouped_gt())
    assert ir["config"]["stub_cols"] == 1
    for row in ir["table"]["tbody"][0]["rows"]:
        assert row["cells"][0]["is_stub"] is True
        # As Great Tables writes it (`<th scope="row">`); other cells have no scope
        assert row["cells"][0]["scope"] == "row"
        assert all("scope" not in c for c in row["cells"][1:])


def test_column_labels_are_the_labels_set():
    ir = ir_of(make_styled_gt())
    labels = [text_of(c) for c in ir["table"]["thead"]["rows"][0]["cells"]]
    assert labels == ["Student Name", "Test Score", "Letter Grade"]
    assert [c["align"] for c in ir["column_spec"]] == ["left", "right", "center"]


def test_missing_values_show_what_great_tables_shows():
    gt = GT(exibble.head(6)[["char", "num"]])
    shown = re.findall(r"<td[^>]*>([^<]*)</td>", gt.as_raw_html())
    ir = ir_of(gt)
    cells = [c for r in ir["table"]["tbody"][0]["rows"] for c in r["cells"]]
    assert [text_of(c) for c in cells] == shown
    # The missing ones (char row 5, num row 6) have no typed value; the others do
    assert all(("typed_value" in c) == (i not in (8, 11)) for i, c in enumerate(cells))
    # Cells have no sort key or data type (IR 1.0 has neither)
    assert not any("sort_key" in c or "data_type" in c for c in cells)


def test_merged_and_transformed_columns_are_what_great_tables_shows():
    # The text is the HTML's, after `cols_merge()` and `text_transform()`: the table is built
    # once, as Great Tables builds it for its HTML.
    gt = (
        GT(exibble[["num", "char", "currency"]].head(2))
        .fmt_currency("currency")
        .cols_merge(["num", "char"], pattern="{0} / {1}")
        .text_transform(loc.body(columns="currency"), lambda x: "X" + x)
    )
    ir = ir_of(gt)
    rows = [[text_of(c) for c in r["cells"]] for r in ir["table"]["tbody"][0]["rows"]]
    assert rows == [["0.1111 / apricot", "X$49.95"], ["2.222 / banana", "X$17.95"]]
    assert re.findall(r"<td[^>]*>([^<]*)</td>", gt.as_raw_html()) == [c for r in rows for c in r]


def test_summary_rows_get_a_stub_when_the_table_has_none():
    gt = GT(exibble[["num", "currency"]].head(3)).grand_summary_rows(
        fns={"Sum": lambda x: x.sum(numeric_only=True)}
    )
    ir = ir_of(gt)
    assert ir["config"]["stub_cols"] == 1
    assert [c["label"] for c in ir["column_spec"]] == ["", "num", "currency"]
    groups = ir["table"]["tbody"]
    data = groups[0]["rows"][0]["cells"]
    assert (data[0]["content"], data[0]["is_stub"], data[0]["scope"]) == ([], True, "row")
    assert groups[-1]["group_id"] is None and groups[-1]["rows"] == []
    (grand,) = groups[-1]["summary_rows"]
    assert grand["role"] == "grand_summary_row"
    stub, *values = grand["cells"]
    assert runs(ir, stub["content"]) == [("Sum", None)]
    assert (stub["is_stub"], stub["scope"]) == (True, "row")
    assert [c["is_stub"] for c in values] == [False, False]
    assert all(c["content"] for c in values)


def test_summary_rows_at_the_top_are_where_great_tables_draws_them():
    total = lambda x: x[["num"]].sum()  # noqa: E731
    gt = (
        GT(exibble[["num", "row", "group"]].head(4), rowname_col="row", groupname_col="group")
        .summary_rows(fns={"Top": total}, side="top")
        .grand_summary_rows(fns={"First": total}, side="top")
        .grand_summary_rows(fns={"Last": total})
    )
    groups = ir_of(gt)["table"]["tbody"]
    assert [(g["group_id"], g.get("summary_placement"), len(g["rows"])) for g in groups] == [
        (None, "top", 0),
        ("grp_a", "top", 4),
        (None, None, 0),
    ]
    assert [r["role"] for r in groups[0]["summary_rows"]] == ["grand_summary_row"]
    assert [r["role"] for r in groups[2]["summary_rows"]] == ["grand_summary_row"]


def test_a_group_with_summary_rows_on_both_sides_has_them_below():
    total = lambda x: x[["num"]].sum()  # noqa: E731
    gt = (
        GT(exibble[["num", "row", "group"]].head(4), rowname_col="row", groupname_col="group")
        .summary_rows(fns={"Top": total}, side="top")
        .summary_rows(fns={"Bottom": total})
    )
    (group,) = ir_of(gt)["table"]["tbody"]
    assert "summary_placement" not in group
    assert len(group["summary_rows"]) == 2


def test_a_stub_of_several_columns_merges_its_outer_cells():
    ir = ir_of(stub_tables().tab_stubhead("Rows"))
    assert ir["config"]["stub_cols"] == 2
    assert [c["align"] for c in ir["column_spec"]] == ["left", "left", "right", "right"]
    (head,) = ir["table"]["thead"]["rows"]
    assert shape(head) == [
        ("Rows", 1, 2, "colgroup", False),
        "·",
        ("v", 1, 1, "col", False),
        ("w", 1, 1, "col", False),
    ]
    # A label over several stub columns is at their left, as Great Tables draws it
    assert ir["styles"]["defs"][head["cells"][0]["style_id"]] == {"text_align": "left"}
    g1, g2 = ir["table"]["tbody"]
    assert [shape(r) for r in g1["rows"]] == [
        [
            ("x", 2, 1, "rowgroup", True),
            ("p", 1, 1, "row", True),
            ("1", 1, 1, None, False),
            ("6", 1, 1, None, False),
        ],
        ["·", ("q", 1, 1, "row", True), ("2", 1, 1, None, False), ("7", 1, 1, None, False)],
        [
            ("y", 1, 1, "row", True),
            ("r", 1, 1, "row", True),
            ("3", 1, 1, None, False),
            ("8", 1, 1, None, False),
        ],
    ]
    # A cell isn't merged across groups
    assert [shape(r)[:2] for r in g2["rows"]] == [
        [("x", 2, 1, "rowgroup", True), ("s", 1, 1, "row", True)],
        ["·", ("t", 1, 1, "row", True)],
    ]


def test_stub_cells_are_merged_in_the_order_shown():
    # Grouping moves row 2 up beside row 0: the two are merged, row 1 isn't
    df = pd.DataFrame(
        {"g": ["G1", "G2", "G1"], "o": ["x", "x", "x"], "i": ["p", "q", "r"], "v": [1, 2, 3]}
    )
    g1, g2 = ir_of(GT(df, rowname_col=["o", "i"], groupname_col="g"))["table"]["tbody"]
    assert [shape(r)[:2] for r in g1["rows"]] == [
        [("x", 2, 1, "rowgroup", True), ("p", 1, 1, "row", True)],
        ["·", ("r", 1, 1, "row", True)],
    ]
    assert [shape(r)[:2] for r in g2["rows"]] == [
        [("x", 1, 1, "row", True), ("q", 1, 1, "row", True)]
    ]


def test_a_row_group_column_is_the_first_stub_column():
    ir = ir_of(
        stub_tables()
        .tab_options(row_group_as_column=True)
        .tab_stubhead("Rows")
        .tab_spanner("S1", ["v", "w"])
        .tab_spanner("S2", ["v", "w"], level=2)
        .summary_rows(fns={"Sum": lambda d: d[["v", "w"]].sum()})
        .grand_summary_rows(fns={"Tot": lambda d: d[["v", "w"]].sum()})
    )
    assert ir["config"]["stub_cols"] == 3
    assert [c["align"] for c in ir["column_spec"]] == ["left"] * 3 + ["right"] * 2
    top, low, labels = ir["table"]["thead"]["rows"]
    # The top spanner row has one blank over the stub; the lowest one per column
    assert shape(top) == [
        ("", 1, 3, "colgroup", False),
        "·",
        "·",
        ("S2", 1, 2, "colgroup", False),
        "·",
    ]
    assert shape(low)[:3] == [("", 1, 1, "col", False)] * 3
    assert shape(labels)[:3] == [("Rows", 1, 3, "colgroup", False), "·", "·"]
    g1, g2, grand = ir["table"]["tbody"]
    # The group's label is its first stub cell, spanning its rows; it has no label row
    assert (g1["label"], g2["label"]) == (None, None)
    assert [shape(r)[:3] for r in g1["rows"]] == [
        [("G1", 3, 1, "rowgroup", True), ("x", 2, 1, "rowgroup", True), ("p", 1, 1, "row", True)],
        ["·", "·", ("q", 1, 1, "row", True)],
        ["·", ("y", 1, 1, "row", True), ("r", 1, 1, "row", True)],
    ]
    assert shape(g2["rows"][0])[0] == ("G2", 2, 1, "rowgroup", True)
    # A group's summary: an empty cell under the group's, the label over the row stub (the IR
    # has no span from a group's rows into its summary rows)
    assert [shape(r) for r in g1["summary_rows"]] == [
        [
            ("", 1, 1, None, True),
            ("Sum", 1, 2, "row", True),
            "·",
            ("6", 1, 1, None, False),
            ("21", 1, 1, None, False),
        ]
    ]
    # The grand summary's label spans the whole stub
    assert shape(grand["summary_rows"][0])[:3] == [("Tot", 1, 3, "row", True), "·", "·"]


def test_a_row_group_column_without_a_stub():
    ir = ir_of(
        GT(stub_data()[["g", "i", "v"]], groupname_col="g")
        .tab_options(row_group_as_column=True)
        .grand_summary_rows(fns={"Tot": lambda d: d[["v"]].sum()})
    )
    assert ir["config"]["stub_cols"] == 1
    g1, _, grand = ir["table"]["tbody"]
    assert [shape(r)[0] for r in g1["rows"]] == [("G1", 3, 1, "rowgroup", True), "·", "·"]
    assert shape(grand["summary_rows"][0])[0] == ("Tot", 1, 1, "row", True)


@pytest.mark.parametrize("as_column", [False, True])
def test_a_stubhead_label_for_each_stub_column(as_column: bool):
    ir = ir_of(stub_tables().tab_options(row_group_as_column=as_column).tab_stubhead(["A", "B"]))
    blank = [("", 1, 1, "col", False)] if as_column else []
    (head,) = ir["table"]["thead"]["rows"]
    assert shape(head) == blank + [
        ("A", 1, 1, "col", False),
        ("B", 1, 1, "col", False),
        ("v", 1, 1, "col", False),
        ("w", 1, 1, "col", False),
    ]


def test_a_single_stub_column_is_at_the_left():
    ir = ir_of(GT(pd.DataFrame({"r": [1, 2], "v": [3, 4]}), rowname_col="r"))
    assert [c["align"] for c in ir["column_spec"]] == ["left", "right"]


# Config ----------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "locale, lang, direction",
    [
        ("ar_EG", "ar-EG", "rtl"),
        ("he", "he", "rtl"),
        ("fa", "fa", "rtl"),
        ("pa_Arab", "pa-Arab", "rtl"),
        ("fr_CA", "fr-CA", None),
        ("zh_Hant_TW", "zh-Hant-TW", None),
        ("uz_Latn", "uz-Latn", None),
    ],
)
def test_a_locale_is_the_tables_language_and_direction(
    locale: str, lang: str, direction: str | None
):
    config = ir_of(GT(pd.DataFrame({"x": [1.5]}), locale=locale))["config"]
    assert config["locale"] == lang
    assert config["lang"] == lang
    assert config.get("dir") == direction


def test_without_a_locale_the_language_is_unset():
    config = ir_of(make_simple_gt())["config"]
    assert config["locale"] == "en-US"
    assert "lang" not in config and "dir" not in config


@pytest.mark.parametrize("table_id, expected", [("sales", "sales"), ("a b", None), ("", None)])
def test_the_tables_id_is_config_id(table_id: str, expected: str | None):
    config = ir_of(GT(exibble[["num"]].head(2), id=table_id))["config"]
    assert config.get("id") == expected


@pytest.mark.parametrize(
    "width, expected",
    [
        ("500px", "500px"),
        (500, "500px"),
        (12.5, "12.5px"),
        ("50%", "50%"),
        ("30em", "30em"),
        # Left to gridwell: the default, and widths the IR doesn't take
        ("auto", None),
        ("AUTO", None),
        ("calc(100% - 2em)", None),
        ("-5px", None),
    ],
)
def test_a_table_width_set_is_the_tables_width(width: Any, expected: str | None):
    config = ir_of(GT(exibble[["num", "char"]].head(2)).tab_options(table_width=width))["config"]
    assert config.get("table_width") == expected


def test_column_widths_are_the_columns_not_the_tables():
    # Great Tables gives a table whose columns all have a width in pixels their sum as its width;
    # the IR has the columns' widths only, and gridwell sizes the table.
    gt = GT(exibble[["num", "char"]].head(2)).cols_width(num="100px", char="200px")
    ir = ir_of(gt)
    assert ir["config"]["table_width"] is None
    assert [c["width"] for c in ir["column_spec"]] == ["100px", "200px"]


# Stub indents ----------------------------------------------------------------------------------


def stub_indents(ir: dict[str, Any]) -> list[tuple[str, str | None]]:
    """Each data row's primary stub cell as (text, its indent)."""
    out = []
    for group in ir["table"]["tbody"]:
        for row in group["rows"]:
            cell = [c for c in row["cells"] if c["is_stub"] and not c["is_placeholder"]][-1]
            out.append((text_of(cell), defs_of(ir, cell["style_id"]).get("indent")))
    return out


def html_indents(gt: GT) -> list[tuple[str, int]]:
    """Each stub cell in Great Tables' HTML as (text, its `gt_indent_*` level)."""
    found = re.findall(
        r'<th [^>]*class="([^"]*\bgt_stub\b[^"]*)"[^>]*>([^<]*)</th>', gt.as_raw_html()
    )
    return [
        (text, int(m.group(1)) if (m := re.search(r"\bgt_indent_(\d)\b", cls)) else 0)
        for cls, text in found
    ]


def test_a_stub_indent_is_the_level_times_the_indent_length():
    gt = make_indented_gt()
    ir = ir_of(gt)
    assert stub_indents(ir) == [("a", None), ("b", "15px"), ("c", None), ("d", "25px")]
    # As Great Tables indents them (its classes, `calc(5px * 3)` in its CSS); not summary rows
    assert html_indents(gt) == [("a", 0), ("b", 3), ("Sum", 0), ("c", 0), ("d", 5), ("Sum", 0)]
    assert "gt_indent_3 { text-indent: calc(5px * 3); }" in gt.as_raw_html()
    summaries = [c for g in ir["table"]["tbody"] for r in g["summary_rows"] for c in r["cells"]]
    assert not any("indent" in defs_of(ir, c["style_id"]) for c in summaries)
    # Body cells aren't indented
    body = [c for g in ir["table"]["tbody"] for r in g["rows"] for c in r["cells"][1:]]
    assert not any("indent" in defs_of(ir, c["style_id"]) for c in body)


@pytest.mark.parametrize(
    "length, expected",
    [
        ("10px", ["20px", "50px"]),
        (8, ["16px", "40px"]),
        ("1.5em", ["3em", "7.5em"]),
        ("0.3rem", ["0.6rem", "1.5rem"]),
        ("2%", ["4%", "10%"]),
        # A length the IR can't take: no indent
        ("calc(1em + 2px)", [None, None]),
        ("-3px", [None, None]),
    ],
)
def test_a_stub_indent_takes_the_indent_length_option(length: Any, expected: list[str | None]):
    df = pd.DataFrame({"r": ["a", "b"], "v": [1, 2]})
    gt = (
        GT(df, rowname_col="r")
        .tab_stub_indent(rows=[0], indent=2)
        .tab_stub_indent(rows=[1], indent=5)
        .tab_options(stub_indent_length=length)
    )
    assert [indent for _, indent in stub_indents(ir_of(gt))] == expected


def test_a_stub_indent_is_under_tab_style():
    df = pd.DataFrame({"r": ["a", "b"], "v": [1, 2]})
    gt = (
        GT(df, rowname_col="r")
        .tab_stub_indent(rows=[0, 1], indent=2)
        .tab_style(style.text(weight="bold"), loc.stub(rows=[0]))
        .tab_style(style.css("text-indent: 3em"), loc.stub(rows=[1]))
    )
    ir = ir_of(gt)
    first, second = (
        defs_of(ir, r["cells"][0]["style_id"]) for r in ir["table"]["tbody"][0]["rows"]
    )
    assert first == {"font_weight": "bold", "indent": "10px"}
    # The cell's own style wins, as its `style` attribute does over the class in the HTML
    assert second == {"indent": "3em"}


def test_only_the_primary_stub_column_is_indented():
    gt = stub_tables().tab_stub_indent(rows=[0, 2], indent=1)
    ir = ir_of(gt)
    assert stub_indents(ir) == [("p", "5px"), ("q", None), ("r", "5px"), ("s", None), ("t", None)]
    outer = [
        defs_of(ir, r["cells"][0]["style_id"])
        for g in ir["table"]["tbody"]
        for r in g["rows"]
        if not r["cells"][0]["is_placeholder"]
    ]
    assert not any("indent" in d for d in outer)


# Typed values ----------------------------------------------------------------------------------


def test_typed_values_are_json_values_as_displayed():
    rows = ir_of(make_typed_gt())["table"]["tbody"][0]["rows"]
    typed = [[c.get("typed_value") for c in r["cells"]] for r in rows]
    assert typed[0] == [
        {"type": "boolean", "value": True},
        {"type": "integer", "value": 1},
        {"type": "number", "value": 0.5},
        {"type": "date", "value": "2024-03-15"},
        {"type": "datetime", "value": "2024-03-15T14:30:00"},
        {"type": "time", "value": "14:30:00"},
        # The number shown (U+2212 MINUS SIGN read as a minus), not the data's
        {"type": "number", "value": -1.5},
        # A currency is the number it shows
        {"type": "number", "value": 49.95},
        {"type": "string", "value": "x"},
        {"type": "boolean", "value": True},
        {"type": "datetime", "value": "2024-03-15T14:30:00"},
    ]
    assert typed[1][:7] == [
        {"type": "boolean", "value": False},
        {"type": "integer", "value": 2},
        # Thousands separators dropped
        {"type": "number", "value": 1234.5},
        {"type": "date", "value": "2024-03-16"},
        {"type": "datetime", "value": "2024-03-15T09:05:30"},
        {"type": "time", "value": "09:05:03"},
        {"type": "number", "value": -2.2},
    ]


def test_typed_values_are_the_numbers_any_display_shows():
    rows = ir_of(make_shown_numbers_gt())["table"]["tbody"][0]["rows"]
    shown = [[text_of(c) for c in r["cells"]] for r in rows]
    typed = [[c.get("typed_value") for c in r["cells"]] for r in rows]
    # fmt: off
    assert shown == [
        ["1.234,50", "1 234,50", "45.1%", "$49.95", "$49.95", "€49,95", f"1.23{TIMES}10⁻⁴",
         "1.23M", "+1,234.50", "1,234.50 kg", "1,234", "1,234.000"],
        ["−98.765,43", "0,25", "−1.2%", "−$5.00", "($5.00)", "−€5,00", f"1.23{TIMES}10⁵",
         "0.50", "−2.00", "2.00 kg", "−5", "1.234"],
    ]
    # fmt: on
    number = lambda v: {"type": "number", "value": v}  # noqa: E731
    assert typed[0] == [
        # In the locale's marks (once read as 1.2345: the `,` dropped as a separator)
        number(1234.5),
        number(1234.5),
        number(0.451),
        number(49.95),
        number(49.95),
        number(49.95),
        number(0.000123),
        number(1230000.0),
        number(1234.5),
        number(1234.5),
        {"type": "integer", "value": 1234},
        number(1234.0),
    ]
    assert typed[1] == [
        number(-98765.43),
        number(0.25),
        number(-0.012),
        number(-5.0),
        number(-5.0),
        number(-5.0),
        number(123000.0),
        number(0.5),
        number(-2.0),
        number(2.0),
        {"type": "integer", "value": -5},
        # `1.234` is a little more than one here, a thousand and more above
        number(1.234),
    ]


@pytest.mark.parametrize(
    "shown, raw, value",
    [
        # Rounded displays: the number shown, not the data's
        ("1,230", 1234.5678, 1230.0),
        ("0", 0.4, 0.0),
        ("-0", -0.2, 0.0),
        # A display only one reading fits is read as shown (`scale_by=`), even when the value
        # doesn't round to it
        ("1.2", 1234.5678, 1.2),
        ("1.2 MB", 1234567, 1.2),
        ("45.1%", 45.1, 0.451),
        ("1.000", 1, 1.0),
        ("1.000", 1000, 1000.0),
        ("12,34,567", 1234567, 1234567.0),
        ("1.5K", 1.5, 1.5),
        ("1.5K", 1500, 1500.0),
        ("451.20‰", 0.4512, 0.4512),
        ("1.23 × 10^-4", 0.000123, 0.000123),
        ("1.23\xa0×\xa010⁻⁴", 0.000123, 0.000123),
        ("1.23e-04", 0.000123, 0.000123),
        ("(10%)", -0.1, -0.1),
        ("CA$1,250", 1250, 1250.0),
        ("5,00 kr.", 5, 5.0),
        # Not one number: no typed value
        ("1,234", 5, None),
        ("<0.001", 0.0001, None),
        ("46 (37, 60)", 46, None),
        ("~5", 5, None),
        ("±5", 5, None),
        ("5/8", 0.625, None),
        ("1.2 m2", 1.2, None),
        ("[5]", 5, None),
        ("(-5)", -5, None),
        ("--5", -5, None),
        ("5-", 5, None),
        ("5%%", 0.05, None),
        ("%5", 0.05, None),
        ("007", 7, None),
        ("1.234.5", 1234.5, None),
        ("1;234", 1234, None),
        ("-(10)", -10, None),
        ("1,234,.5", 1234.5, None),
        (". 5", 5, None),
        ("5 .", 5, None),
        ("1.23M", 1.24, None),
    ],
)
def test_typed_numbers_are_read_off_their_display(shown: str, raw: Any, value: float | None):
    typed = _typed_value(raw, shown, "number")
    if value is None:
        assert typed is None
    else:
        assert typed == {"type": "number", "value": value}
        # (`-0` is 0.0, not -0.0)
        assert str(typed["value"]) == str(value)


def test_typed_integers_are_plain_integers_shown():
    assert _typed_value(1234, "1,234", "integer") == {"type": "integer", "value": 1234}
    assert _typed_value(1234, "1.234", "integer") == {"type": "integer", "value": 1234}
    assert _typed_value(-5, "−5", "integer") == {"type": "integer", "value": -5}
    # Shown scaled or with decimals, an integer is a number
    assert _typed_value(1234567, "1.23M", "integer") == {"type": "number", "value": 1230000.0}
    assert _typed_value(5, "5.00", "integer") == {"type": "number", "value": 5.0}
    assert _typed_value(1, "100%", "integer") == {"type": "number", "value": 1.0}


@pytest.mark.parametrize(
    "value, kind, expected",
    [
        # A column's kind first
        (1, "number", "integer"),
        (np.int64(1), "number", "integer"),
        (1.5, "number", "number"),
        (Decimal("1.5"), "number", "number"),
        (True, "boolean", "boolean"),
        (dt.date(2024, 1, 1), "date", "date"),
        (dt.datetime(2024, 1, 1), "datetime", "datetime"),
        (dt.time(1, 2), "time", "time"),
        # Durations are strings (IR 1.0 has no duration type)
        (dt.timedelta(hours=1), "duration", "string"),
        ("x", "string", "string"),
        ("x", "category", "string"),
        # Else the value's own type: a bool (numpy's too) before an integer, a datetime before
        # a date
        (True, "other", "boolean"),
        (np.bool_(False), "other", "boolean"),
        (7, "other", "integer"),
        (np.int32(7), "other", "integer"),
        (2.5, "other", "number"),
        (np.float32(2.5), "other", "number"),
        (dt.datetime(2024, 1, 1, 12), "other", "datetime"),
        (pd.Timestamp("2024-01-01 12:00"), "other", "datetime"),
        (dt.date(2024, 1, 1), "other", "date"),
        (dt.time(12), "other", "time"),
        (Decimal("2.5"), "other", "string"),
        (None, "other", "string"),
        ([1], "other", "string"),
    ],
)
def test_a_cells_data_type_is_its_columns_kind_or_its_values(value: Any, kind: str, expected: str):
    assert _infer_data_type(value, kind) == expected


def test_a_datetime_is_its_wall_clock_time():
    # An aware datetime is the time shown (its offset dropped); a pandas one to its precision
    aware = dt.datetime(2024, 3, 15, 14, 30, tzinfo=dt.timezone(dt.timedelta(hours=-5)))
    assert _typed_value(aware, "x", "datetime") == {
        "type": "datetime",
        "value": "2024-03-15T14:30:00",
    }
    stamp = pd.Timestamp("2024-03-15 14:30:00.123456")
    assert _typed_value(stamp, "x", "datetime") == {
        "type": "datetime",
        "value": "2024-03-15T14:30:00.123456",
    }
    # A value in a datetime column that isn't a datetime is its text
    assert _typed_value("2024", "2024", "datetime") == {"type": "string", "value": "2024"}


def test_tz_aware_datetimes_are_typed_as_shown():
    df = pd.DataFrame({"ts": pd.to_datetime(["2024-03-15 14:30:00"]).tz_localize("US/Eastern")})
    (cell,) = ir_of(GT(df))["table"]["tbody"][0]["rows"][0]["cells"]
    assert cell["typed_value"] == {"type": "datetime", "value": "2024-03-15T14:30:00"}


PARITY = {
    "i": [1, 2, 3],
    "f": [1234.5678, None, -0.25],
    "s": ["apple", None, "cherry"],
    "b": [True, False, True],
    "d": [dt.date(2024, 1, 1), None, dt.date(2024, 2, 29)],
    "ts": [dt.datetime(2024, 1, 1, 12, 30), None, dt.datetime(2024, 2, 29, 8, 5, 30)],
    "t": [dt.time(12, 30), None, dt.time(8, 5, 30)],
    "n": [1, None, 3],
}


def _typed_cells(build: Any = lambda gt: gt) -> Any:
    def render(constructor: DataFrameConstructor) -> str:
        ir = build_ir(build(GT(constructor(PARITY), id="parity")))
        rows = [r for g in ir["table"]["tbody"] for r in g["rows"]]
        return "\n".join(
            " | ".join(f"{text_of(c)!r} {json.dumps(c.get('typed_value'))}" for c in r["cells"])
            for r in rows
        )

    return render


@pytest.mark.parametrize(
    "build",
    [
        pytest.param(lambda gt: gt, id="unformatted"),
        pytest.param(
            lambda gt: (
                gt.fmt_number("f", decimals=1)
                .fmt_integer(["i", "n"])
                .fmt_tf("b")
                .fmt_date("d", date_style="iso")
                .fmt_datetime("ts", date_style="iso", time_style="iso")
                .fmt_time("t", time_style="h_m_p")
                .sub_missing()
            ),
            id="formatted",
        ),
    ],
)
def test_typed_values_are_the_same_from_every_backend(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor], build: Any
):
    # (Column `n`: pandas makes integers with a missing value floats, so they're numbers)
    divergent = {"pandas_constructor": INT_UPCAST}
    assert_parity(snapshot, all_frame_constructors, _typed_cells(build), divergent)


# Footnotes, notes and labels -------------------------------------------------------------------


def _footnotes_shown(html: str) -> list[tuple[str, str]]:
    """(mark, text) of each footnote Great Tables lists under the table."""
    out = []
    for item in re.findall(r'<td class="gt_footnote"[^>]*>(.*?)</td>', html, re.S):
        mark = re.search(r'<span class="gt_footnote_marks"[^>]*>([^<]*)</span>', item)
        text = re.sub(
            r"<[^>]+>", "", re.sub(r'<span class="gt_footnote_marks".*?</span>', "", item)
        )
        out.append((mark.group(1) if mark else "", text.strip()))
    return out


def test_footnotes_are_the_ones_great_tables_shows_with_its_marks():
    gt = make_footnoted_gt()
    shown = _footnotes_shown(gt.as_raw_html())
    # Reading order, one per text
    assert shown == [
        ("", "A general note."),
        ("1", "Title note."),
        ("2", "Label note."),
        ("3", "Body note."),
    ]
    footnotes = ir_of(gt)["footer"]["footnotes"]
    assert [(f["mark"], f["content"][0]["value"]) for f in footnotes] == shown
    assert len({f["id"] for f in footnotes}) == len(footnotes)


def test_md_notes_are_their_text_not_the_objects_repr():
    gt = GT(exibble[["num"]].head(1)).tab_source_note(md("Source *two*."))
    note = "".join(n["value"] for n in ir_of(gt)["footer"]["source_notes"][0]["content"])
    assert note == "Source two." and "Md(" not in note and "Text(" not in note


def test_labels_are_styled_runs_as_great_tables_draws_them():
    gt = (
        GT(exibble[["num", "char", "group"]].head(2), groupname_col="group")
        .tab_header(title=md("A *b* **c** ***d***"), subtitle=html("x<br>y <code>z</code>"))
        .cols_label(num=md("**Num**"), char="<b>not bold</b> & *not md*")
        .tab_spanner(html("<i>Span</i>"), ["num", "char"])
        .tab_footnote(md("Note *one*"), locations=loc.title())
        .tab_source_note(html("<p>Para one</p>\n<p>Para <b><i>two</i></b></p><script>x()</script>"))
        .tab_source_note(html("A&nbsp;B &amp; C&#x2014;D <u>u</u> <del>d</del>"))
        # A stray end tag closes nothing; runs of one style are one run
        .tab_source_note(html("<br> <b>a</i>b</b>c<span>d</span> <br>"))
    )
    ir = ir_of(gt)
    bold, italic = {"font_weight": "bold"}, {"font_style": "italic"}
    both = {"font_style": "italic", "font_weight": "bold"}
    assert runs(ir, ir["header"]["title"]["content"]) == [
        ("A ", None),
        ("b", italic),
        (" ", None),
        ("c", bold),
        (" ", None),
        ("d", both),
        ("^1", "fn1"),
    ]
    assert runs(ir, ir["header"]["subtitle"]["content"]) == [
        ("x", None),
        ("\n", None),
        ("y ", None),
        ("z", {"font_family": "monospace"}),
    ]
    head = ir["table"]["thead"]["rows"]
    assert runs(ir, head[0]["cells"][0]["content"]) == [("Span", italic)]
    assert (head[0]["cells"][0]["colspan"], head[0]["cells"][0]["scope"]) == (2, "colgroup")
    labels = [runs(ir, c["content"]) for c in head[1]["cells"]]
    # A plain string is text as it is, not markup
    assert labels == [[("Num", bold)], [("<b>not bold</b> & *not md*", None)]]
    assert ir["column_spec"][0]["label"] == "Num"
    footer = ir["footer"]
    assert runs(ir, footer["footnotes"][0]["content"]) == [("Note ", None), ("one", italic)]
    notes = [runs(ir, n["content"]) for n in footer["source_notes"]]
    assert notes == [
        [("Para one", None), ("\n", None), ("Para ", None), ("two", both)],
        [
            ("A\xa0B & C—D ", None),
            ("u", {"text_decoration": "underline"}),
            (" ", None),
            ("d", {"text_decoration": "line-through"}),
        ],
        [("ab", bold), ("cd", None)],
    ]
    # One definition per distinct style, numbered as gt's (R) emitter numbers them
    ids = [
        n["style_id"]
        for part in (ir["header"]["title"], *footer["source_notes"])
        for n in part["content"]
        if n["type"] == "styled_text"
    ]
    assert ids[:3] == ["gw_1", "gw_2", "gw_3"] and ids[3] == "gw_3"
    gw = {k: v for k, v in ir["styles"]["defs"].items() if k.startswith("gw_")}
    assert len(gw) == len({json.dumps(v, sort_keys=True) for v in gw.values()}) == 6


# Body cells ------------------------------------------------------------------------------------


def test_body_cells_are_the_html_great_tables_draws():
    ir = ir_of(make_html_body_gt())
    rows = [r["cells"] for r in ir["table"]["tbody"][0]["rows"]]
    bold, italic = {"font_weight": "bold"}, {"font_style": "italic"}
    mono = {"font_family": "monospace"}
    # A string is escaped: its text as it is
    assert [runs(ir, r[0]["content"]) for r in rows] == [
        [("a < b & c", None)],
        [("<b>not bold</b>", None)],
    ]
    assert runs(ir, rows[0][1]["content"]) == [
        ("md", bold),
        (" ", None),
        ("it", italic),
        ("\n", None),
        ("para ", None),
        ("two", mono),
    ]
    # Superscripts in Unicode characters; the mark after the text, as Great Tables places it
    # (the HTML isn't a number)
    assert runs(ir, rows[0][2]["content"]) == [(f"1.23{TIMES}10⁻⁴", None), ("^1", "fn1")]
    assert runs(ir, rows[1][2]["content"]) == [(f"1.23{TIMES}10⁴", None)]
    assert runs(ir, rows[0][3]["content"]) == [("m² s₁", None)]
    assert [r[4]["content"] for r in rows] == [
        [{"type": "image", "src": f"https://example.invalid/{f}.png", "alt": "", "height": "20px"}]
        for f in "ab"
    ]
    assert rows[0][5]["content"] == [
        {"type": "raw", "format": "html", "value": "<svg width='8'><svg/><text>T</text></svg>"},
        {"type": "text", "value": " & "},
        {"type": "styled_text", "value": "x", "style_id": rows[0][5]["content"][2]["style_id"]},
        {"type": "raw", "format": "html", "value": "<svg/>"},
    ]
    assert runs(ir, rows[0][5]["content"][1:3]) == [(" & ", None), ("x", italic)]
    # A character without a superscript form, or a line break: as written
    assert rows[1][5]["content"] == [
        {"type": "text", "value": "2q 102"},
        {"type": "line_break"},
        {"type": "text", "value": "3 ₐ₁"},
        {"type": "raw", "format": "html", "value": "<svg><text>open"},
    ]
    assert [r[6]["content"] for r in rows] == [
        [
            {
                "type": "image",
                "src": "/no/such/file.png",
                "alt": "A",
                "width": "12px",
                "height": "2em",
            }
        ],
        [{"type": "image", "src": "x.png", "height": "auto"}, {"type": "text", "value": "x"}],
    ]
    # The stub is a row header; nothing else has a scope
    assert [r[0]["scope"] for r in rows] == ["row", "row"]
    assert not any("scope" in c for r in rows for c in r[1:])
    # The text shown is the typed value, not the markup
    assert rows[0][1]["typed_value"] == {"type": "string", "value": "md it para two"}
    assert rows[0][3]["typed_value"] == {"type": "string", "value": "m² s₁"}
    # A number in scientific notation is the number (its superscripts read)
    assert rows[0][2]["typed_value"] == {"type": "number", "value": 0.000123}
    assert rows[1][2]["typed_value"] == {"type": "number", "value": 12300.0}
    assert "typed_value" not in rows[0][4]


@pytest.mark.parametrize("tag", sorted(_SCRIPTS))
def test_superscripts_and_subscripts_are_their_characters(tag: str):
    chars = _SCRIPTS[tag]
    source = "".join(chars)
    assert _lower_html(f"<{tag}>{source}</{tag}>") == [[("".join(chars.values()), {})]]


def test_the_ir_never_reads_an_images_file():
    # `src` is copied as it is, never read (gridwell draws only `data:` URIs)
    gt = GT(pd.DataFrame({"i": ['<img src="file:///etc/passwd">', '<img src="../x.png">']})).fmt(
        lambda x: x, columns="i"
    )
    rows = ir_of(gt)["table"]["tbody"][0]["rows"]
    assert [r["cells"][0]["content"] for r in rows] == [
        [{"type": "image", "src": "file:///etc/passwd"}],
        [{"type": "image", "src": "../x.png"}],
    ]


# Styles ----------------------------------------------------------------------------------------


def mark_tokens(content: list[dict[str, Any]]) -> list[str]:
    """Content as its text pieces and marks ("^" + the marks, those next to each other together,
    as Great Tables draws them), white space between them dropped."""
    out: list[str] = []
    for n in content:
        if n["type"] == "footnote_mark":
            if out and out[-1].startswith("^") and out[-1].endswith(","):
                out[-1] += n["mark_text"]
            else:
                out.append("^" + n["mark_text"])
        elif n.get("value", "").strip():
            out.append(n["value"].strip())
    return out


class _Cells(HTMLParser):
    """Great Tables' HTML as its cells, in document order: (section, classes, style attribute,
    text pieces and marks)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.cells: list[tuple[str | None, set[str], str, list[str]]] = []
        self.section: str | None = None
        self.cell: tuple[str | None, set[str], str, list[str]] | None = None
        self.in_mark = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("thead", "tbody", "tfoot"):
            self.section = tag
        elif tag in ("th", "td"):
            classes = set((a.get("class") or "").split())
            self.cell = (self.section, classes, a.get("style") or "", [])
            self.cells.append(self.cell)
        elif tag == "span" and "gt_footnote_marks" in (a.get("class") or ""):
            self.in_mark = True

    def handle_endtag(self, tag):
        if tag == "span":
            self.in_mark = False

    def handle_data(self, data):
        if self.cell is not None and data.strip():
            self.cell[3].append(("^" + data.strip()) if self.in_mark else data.strip())


def drawn(gt: GT) -> dict[str, Any]:
    """What Great Tables draws, by part: each cell's text and marks, with its style attribute
    read as the IR's style definitions."""
    parser = _Cells()
    parser.feed(gt.as_raw_html())
    parts: dict[str, Any] = {"head": {}, "body": [], "footnotes": [], "source_notes": []}
    for section, classes, css, tokens in parser.cells:
        entry = (tokens, _css_style(css))
        if "gt_title" in classes:
            parts["title"] = entry
        elif "gt_subtitle" in classes:
            parts["subtitle"] = entry
        elif section == "thead":
            if tokens:
                parts["head"][tokens[0]] = entry
        elif "gt_footnote" in classes:
            # The footnote's own mark comes first; the IR has it as `mark`
            parts["footnotes"].append((tokens[1:], entry[1]))
        elif "gt_sourcenote" in classes:
            parts["source_notes"].append(entry)
        elif section == "tbody":
            parts["body"].append(entry)
    return parts


def emitted(gt: GT) -> tuple[dict[str, Any], dict[str, Any]]:
    """The same parts of the IR (only the cells' own styles)."""
    ir = ir_of(gt)
    defs = ir["styles"]["defs"]

    def entry(part):
        return (mark_tokens(part["content"]), defs.get(part.get("style_id"), {}))

    parts: dict[str, Any] = {
        **{k: entry(ir["header"][k]) for k in ("title", "subtitle") if ir["header"][k]},
        "head": {},
        "body": [],
        "footnotes": [entry(f) for f in ir["footer"]["footnotes"]],
        "source_notes": [entry(n) for n in ir["footer"]["source_notes"]],
    }
    for row in ir["table"]["thead"]["rows"]:
        for c in row["cells"]:
            if c["content"]:
                parts["head"][mark_tokens(c["content"])[0]] = entry(c)
    for group in ir["table"]["tbody"]:
        if group.get("label"):
            parts["body"].append(entry(group["label"]))
        for row in group["rows"] + group["summary_rows"]:
            parts["body"].extend(entry(c) for c in row["cells"] if not c["is_placeholder"])
    return ir, parts


def test_every_location_is_styled_and_marked_as_great_tables_draws_it():
    gt = everywhere()
    ir, ours = emitted(gt)
    theirs = drawn(gt)
    assert ours == theirs
    # Not vacuous: every kind of location has its style and mark
    assert theirs["title"] == (
        ["Title", "^1"],
        {"background_color": "#EEEEE1", "color": "#000001", "font_weight": "bold"},
    )
    assert theirs["subtitle"] == (
        ["^2", "Sub"],
        {"color": "#000001", "font_size": "12px", "font_style": "italic"},
    )
    border = {"border": {"bottom": {"color": "#123456", "style": "solid", "width": "3px"}}}
    assert theirs["head"] == {
        "High": (["High"], border),
        "Stubhead": (["Stubhead", "^3"], {"background_color": "#EEEEE2"}),
        "Low": (["Low", "^4"], {**border, "color": "#000003"}),
        "a": (["a"], {**border, "color": "#000002"}),
        "b": (["b"], border),
        "c": (["c"], border),
        "d": (["d", "^5"], {**border, "color": "#000002"}),
    }
    body = theirs["body"]
    assert body[0] == (["G1", "^6"], {})
    # A number's mark goes before it, anything else's after; two marks are one list
    assert body[1:6] == [
        (["r1"], {}),
        (["^7", "1"], {"color": "#000005"}),
        (["4.5"], {}),
        (
            ["x"],
            {
                "background_color": "#EEEEE4",
                "font_family": "Courier New, monospace",
                "text_align": "right",
            },
        ),
        (["^8,9", "7"], {}),
    ]
    assert body[6:9] == [
        (["r2"], {"color": "#000004"}),
        (["2", "^10"], {"color": "#000005"}),
        (["5.5"], {}),
    ]
    assert body[9] == (["^11", "y"], {})
    assert body[11:14] == [
        (["Max"], {"color": "#000008"}),
        (["^13", "2.0"], {}),
        (["5.5"], {"color": "#000006"}),
    ]
    assert body[16] == (["G2"], {"background_color": "#EEEEE3"})
    assert body[17] == (["r3", "^12"], {})
    assert body[20][1]["background_color"] == "#EEEEE5"
    assert body[-5:] == [
        (["Sum", "^14"], {"color": "#000009"}),
        (["6.0"], {}),
        (["16.5"], {}),
        (["---"], {}),
        (["24.0"], {"color": "#000007"}),
    ]
    note = {"color": "#00000A", "text_transform": "uppercase"}
    assert theirs["footnotes"][:2] == [(["On title."], note), (["On sub."], note)]
    assert theirs["source_notes"] == [
        (
            ["Source."],
            {
                "padding": {"top": "1px", "right": "2px", "bottom": "1px", "left": "2px"},
                "text_transform": "uppercase",
            },
        )
    ]
    # Every mark is its footnote's
    marks = {f["id"]: f["mark"] for f in ir["footer"]["footnotes"]}
    refs = [n for n in nodes(ir) if n["type"] == "footnote_mark"]
    assert len(refs) == 16
    assert all(marks[n["ref"]] == n["mark_text"].rstrip(",") for n in refs)


def test_source_notes_on_one_line_are_styled_too():
    gt = (
        GT(exibble[["num"]].head(1))
        .tab_source_note("One.")
        .tab_source_note("Two.")
        .tab_options(source_notes_multiline=False)
        .tab_style(style.text(color="#00000B"), loc.source_notes())
        .tab_style(style.text(transform="uppercase"), loc.footer())
    )
    styled = {"color": "#00000B", "text_transform": "uppercase"}
    # Two notes in the IR, each styled, as gt styles them
    assert emitted(gt)[1]["source_notes"] == [(["One."], styled), (["Two."], styled)]
    ((tokens, theirs),) = drawn(gt)["source_notes"]
    assert tokens == ["One. Two."]
    assert theirs == styled


def test_the_blank_head_cells_have_great_tables_look():
    # Blank cells in the spanner rows have the column header's style, and the one just above a
    # label spanning rows in Great Tables' HTML has the label's fill
    gt = (
        GT(pd.DataFrame({"r": ["x"], "a": [1], "b": [2], "c": [3]}), rowname_col="r")
        .tab_stubhead("S")
        .tab_spanner("Low", ["a"])
        .tab_spanner("High", ["a", "b"])
        .tab_style(style.fill("#AAAAAA"), loc.stubhead())
        .tab_style(style.fill("#BBBBBB"), loc.column_labels(columns="c"))
        .tab_style(style.text(color="#CCCCCC"), loc.column_header())
    )
    ir = ir_of(gt)
    rows = [
        [
            defs_of(ir, c["style_id"])
            for c in r["cells"]
            if not c["content"] and not c["is_placeholder"]
        ]
        for r in ir["table"]["thead"]["rows"]
    ]
    header = {"color": "#CCCCCC"}
    assert rows == [
        [header, header],  # above the stub, and above c
        [{"background_color": "#AAAAAA"}, {}, {"background_color": "#BBBBBB"}],  # b, then c
        [],
    ]


def test_a_mark_goes_where_the_first_footnote_says():
    df = pd.DataFrame({"n": [1.5], "s": ["x"]})
    for placement, expected in [
        ("left", ["^1", "x"]),
        ("right", ["x", "^1"]),
        ("auto", ["x", "^1"]),
    ]:
        gt = GT(df).tab_footnote("A.", loc.body(columns="s"), placement=placement)
        assert emitted(gt)[1]["body"][1][0] == expected == drawn(gt)["body"][1][0]
    gt = (
        GT(df)
        .tab_footnote("B.", loc.body(columns="n"), placement="right")
        .tab_footnote("A.", loc.body(columns="n"), placement="left")
    )
    assert emitted(gt)[1]["body"][0][0] == ["1.5", "^1,2"] == drawn(gt)["body"][0][0]


def test_symbol_marks_are_in_the_order_great_tables_gives():
    gt = (
        GT(exibble[["num", "char"]].head(2))
        .opt_footnote_marks("standard")
        .tab_footnote("Two.", loc.body(columns="char", rows=[1]))
        .tab_footnote("One.", loc.column_labels(columns="char"))
        .tab_footnote("Three.", loc.body(columns="char", rows=[1]))
    )
    _, ours = emitted(gt)
    theirs = drawn(gt)
    assert ours["head"] == theirs["head"]
    assert ours["body"] == theirs["body"]
    assert [t for t, _ in ours["body"]] == [["0.1111"], ["apricot"], ["2.222"], ["banana", "^†,‡"]]


@pytest.mark.parametrize("as_column", [False, True])
def test_merged_stub_cells_are_styled_and_marked_as_great_tables_draws_them(as_column: bool):
    gt = (
        stub_tables()
        .tab_options(row_group_as_column=as_column)
        .tab_stubhead(["A", "B"])
        .tab_style(style.fill("#FF0000"), loc.stub(rows=[1], columns="o"))
        .tab_style(style.text(color="#000001"), loc.stub(rows=[2]))
        .tab_style(style.text(color="#000002"), loc.row_groups(rows=[1]))
        .tab_footnote("Outer.", loc.stub(rows=[1], columns="o"))
        .tab_footnote("Inner.", loc.stub(rows=[0]))
        .tab_footnote("Group.", loc.row_groups(rows=[0]))
        .tab_footnote("Stubhead.", loc.stubhead())
    )
    _, ours = emitted(gt)
    theirs = drawn(gt)
    assert ours == theirs
    # Not vacuous: a style and a mark on a merged cell, as given for a row it covers
    body = [b for b in theirs["body"] if b[0][0] in ("x", "y")]
    assert body[0] == (["x", "^4"], {"background_color": "#FF0000"})
    assert body[1:] == [(["y"], {"color": "#000001"}), (["x"], {})]


# fmt: off
@pytest.mark.parametrize(
    "css, expected",
    [
        ("color: red; color: #00F;", {"color": "#00F"}),
        ("font-size: 12;", {"font_size": "12px"}),
        ("font-size: 1.5em; font-weight: 700 !important;", {"font_size": "1.5em", "font_weight": "700"}),
        ("font-family: 'IBM Plex Sans', \"Helvetica Neue\", sans-serif;",
         {"font_family": "IBM Plex Sans, Helvetica Neue, sans-serif"}),
        ("font-stretch: condensed; letter-spacing: 1px;", {}),
        ("text-indent: 2em; white-space: nowrap", {"indent": "2em", "white_space": "nowrap"}),
        ("padding: 1px 2px 3px", {"padding": {"top": "1px", "right": "2px", "bottom": "3px", "left": "2px"}}),
        ("padding: 4px; padding-left: 0", {"padding": {"top": "4px", "right": "4px", "bottom": "4px", "left": "0"}}),
        ("border-left: 2px dashed rgb(1, 2, 3);",
         {"border": {"left": {"width": "2px", "style": "dashed", "color": "rgb(1, 2, 3)"}}}),
        ("border: thin solid black; border-top: none;",
         {"border": {"top": {"style": "none"},
                     **{s: {"width": "thin", "style": "solid", "color": "black"}
                        for s in ("right", "bottom", "left")}}}),
        ("border-bottom-color: red; border-style: SOLID none",
         {"border": {"bottom": {"color": "red", "style": "solid"}, "top": {"style": "solid"},
                     "right": {"style": "none"}, "left": {"style": "none"}}}),
        ("background-color: url('a;b'); color", {"background_color": "url('a;b')"}),
        ("", {}),
        ("not css at all", {}),
    ],
)
# fmt: on
def test_css_is_read_as_style_definitions(css: str, expected: dict[str, Any]):
    assert _css_style(css) == expected


def test_every_style_great_tables_has_is_a_style_definition():
    gt = GT(exibble[["num", "char"]].head(2)).tab_style(
        [
            style.text(
                color="red",
                font="Arial",
                size=12,
                align="center",
                v_align="middle",
                style="italic",
                weight=300,
                stretch="condensed",
                decorate="underline",
                transform="lowercase",
                whitespace="pre-wrap",
            ),
            style.fill("#ABCDEF"),
            style.borders(sides="all", color="blue", style="dotted", weight="2px"),
            style.css("max-width: 10px; overflow: hidden; text-overflow: ellipsis"),
        ],
        loc.body(columns="num", rows=[0]),
    )
    ir = ir_of(gt)
    cell = ir["table"]["tbody"][0]["rows"][0]["cells"][0]
    edge = {"width": "2px", "style": "dotted", "color": "blue"}
    assert ir["styles"]["defs"][cell["style_id"]] == {
        "color": "red",
        "font_family": "Arial",
        "font_size": "12px",
        "text_align": "center",
        "vertical_align": "middle",
        "font_style": "italic",
        "font_weight": "300",
        "text_decoration": "underline",
        "text_transform": "lowercase",
        "white_space": "pre-wrap",
        "background_color": "#ABCDEF",
        "border": {s: edge for s in ("top", "right", "bottom", "left")},
        "max_width": "10px",
        "overflow": "hidden",
        "text_overflow": "ellipsis",
    }


# Table options ---------------------------------------------------------------------------------


def test_default_options_add_no_styles():
    ir = ir_of(
        GT(exibble, rowname_col="row", groupname_col="group").grand_summary_rows(
            fns={"Sum": lambda x: x.sum(numeric_only=True)}
        )
    )
    assert ir["styles"] == {"defs": {}, "compositions": {}, "conditionals": []}
    assert "rules" not in ir["config"]


def test_a_theme_is_the_options_styles():
    ir = ir_of(make_themed_gt())
    head = ir["table"]["thead"]["rows"][0]
    assert defs_of(ir, head["style_id"]) == {"background_color": "#0076BA", "color": "#FFFFFF"}
    groups = ir["table"]["tbody"]
    assert defs_of(ir, groups[0]["rows"][0]["style_id"]) == {"border": {"top": {"style": "none"}}}
    assert ir["styles"]["conditionals"] == [
        {
            "id": "row_striping",
            "selector": {"row_parity": "even", "scope": "tbody"},
            "style": {"background_color": "#EDF7FC", "color": "#333333"},
        }
    ]
    stub = {"background_color": "#89D3FE", "color": "#333333"}
    # The stub isn't striped: its own fill on every row (with tab_style() over it)
    stubs = [defs_of(ir, r["cells"][0]["style_id"]) for g in groups for r in g["rows"]]
    assert stubs == [stub, {**stub, "font_weight": "bold"}, stub, stub]
    # Summary rows: the row's fill; the stub's, the row's, then tab_style()'s in a stub cell
    summary = groups[0]["summary_rows"][0]
    assert defs_of(ir, summary["style_id"]) == {}
    assert defs_of(ir, summary["cells"][0]["style_id"]) == {
        "background_color": "#FF0000",
        "color": "#333333",
    }
    grand = groups[-1]["summary_rows"][0]
    assert defs_of(ir, grand["style_id"]) == {"background_color": "#D5D5D5", "color": "#333333"}


def test_a_fill_without_a_readable_color_has_no_text_color():
    gt = GT(exibble[["num"]].head(1)).tab_options(
        column_labels_background_color="rgb(1, 2, 3)", table_font_color=123
    )
    ir = ir_of(gt)
    head = ir["table"]["thead"]["rows"][0]
    assert defs_of(ir, head["style_id"]) == {"background_color": "rgb(1, 2, 3)"}


@pytest.mark.parametrize("heading, footer", [(False, False), (True, True)])
def test_border_options_are_the_tables_rules(heading: bool, footer: bool):
    from great_tables import px

    gt = GT(exibble[["num", "row", "group"]].head(4), rowname_col="row", groupname_col="group")
    if heading:
        gt = gt.tab_header(title="T")
    if footer:
        gt = gt.tab_source_note("Note")
    gt = gt.tab_options(
        table_border_top_color="#FF0000",
        heading_border_bottom_style="dashed",
        column_labels_border_top_width=px(5),
        column_labels_border_bottom_color="#00FF00",
        row_group_border_top_style="dotted",
        row_group_border_bottom_style="double",
        table_body_hlines_style="groove",
        table_body_hlines_width=px(3),
        stub_border_color="#0000FF",
        summary_row_border_width=px(4),
        grand_summary_row_border_style="solid",
        table_body_border_bottom_color="#111111",
        table_border_bottom_width=px(6),
    )
    expected: dict[str, Any] = {
        # Labels and spanners share Great Tables' column label bottom border
        "column_labels": {"color": "#00FF00"},
        "spanners": {"color": "#00FF00"},
        # The group's top border wins over its bottom one; groove isn't a rule
        "group": {"style": "dotted"},
        "rows": {"width": "3px"},
        "stub": {"color": "#0000FF"},
        "summary": {"width": "4px"},
        "grand_summary": {"style": "solid"},
    }
    if heading:
        expected["title"] = {"color": "#FF0000"}
        expected["top"] = {"width": "5px", "style": "dashed"}
    else:
        # Without a heading, the table's top border is the table's top
        expected["top"] = {"width": "5px", "color": "#FF0000"}
    if footer:
        expected["bottom"] = {"color": "#111111"}
        expected["notes"] = {"width": "6px"}
    else:
        expected["bottom"] = {"color": "#111111", "width": "6px"}
    assert ir_of(gt)["config"]["rules"] == expected


def test_striping_covers_the_parts_great_tables_stripes():
    # (Groups of odd sizes: the stripes follow the rows shown, not each group's)
    df = pd.DataFrame({"r": list("abcd"), "g": ["G", "H", "H", "H"], "x": [1, 2, 3, 4]})

    def cells(gt):
        ir = ir_of(gt)
        rows = [r for g in ir["table"]["tbody"] for r in g["rows"]]
        return ir, [[defs_of(ir, c["style_id"]) for c in r["cells"]] for r in rows]

    table = {"background_color": "#FFFFFF", "color": "#333333"}
    stripe = {"background_color": "#F4F4F4", "color": "#333333"}
    base = GT(df, rowname_col="r", groupname_col="g")
    # The body only (opt_row_striping()'s): the stub's cells on the stripe rows keep the table's
    # background. Rows are counted across groups.
    ir, got = cells(base.opt_row_striping())
    assert ir["styles"]["conditionals"][0]["style"] == stripe
    assert got == [[{}, {}], [table, {}], [{}, {}], [table, {}]]
    # The stub only
    _, got = cells(base.tab_options(row_striping_include_stub=True))
    assert got == [[{}, {}], [{}, table], [{}, {}], [{}, table]]
    # The stub with a fill of its own: the stripe over it
    _, got = cells(
        base.tab_options(
            row_striping_include_stub=True,
            row_striping_include_table_body=True,
            stub_background_color="#123456",
            row_striping_background_color="#EEEEEE",
        )
    )
    own = {"background_color": "#123456", "color": "#FFFFFF"}
    assert got == [[own, {}], [{"background_color": "#EEEEEE", "color": "#333333"}, {}]] * 2
    # No striping without either part
    no_stripes = ir_of(base.tab_options(row_striping_include_table_body=False))
    assert no_stripes["styles"]["conditionals"] == []


def test_options_style_fonts_and_group_labels():
    gt = (
        GT(pd.DataFrame({"g": ["A"], "x": [1]}), groupname_col="g")
        .tab_options(
            column_labels_font_weight="bold",
            row_group_background_color="#000000",
            row_group_font_weight="bold",
            table_font_color="#111111",
            table_font_color_light="#EEEEEE",
        )
        .tab_style(style.text(color="red"), loc.row_groups())
    )
    ir = ir_of(gt)
    assert defs_of(ir, ir["table"]["thead"]["rows"][0]["style_id"]) == {"font_weight": "bold"}
    label = ir["table"]["tbody"][0]["label"]
    # The light text color on a dark fill; tab_style() over the options
    assert defs_of(ir, label["style_id"]) == {
        "background_color": "#000000",
        "color": "red",
        "font_weight": "bold",
    }


def test_a_row_group_columns_cells_take_the_options():
    gt = (
        stub_tables()
        .tab_options(
            row_group_as_column=True,
            stub_row_group_font_weight="bold",
            row_striping_include_stub=True,
        )
        .opt_row_striping()
        .tab_style(style.text(color="blue"), loc.row_groups(rows=[1]))
        .summary_rows(fns={"Sum": lambda x: x[["v"]].sum()})
    )
    ir = ir_of(gt)
    g1, g2 = ir["table"]["tbody"]
    # The empty cell under a group's cell in its summary rows is styled as it
    for g in (g1, g2):
        under = g["summary_rows"][0]["cells"][0]
        assert under["content"] == []
        assert under["style_id"] == g["rows"][0]["cells"][0]["style_id"]
    first = [defs_of(ir, g["rows"][0]["cells"][0]["style_id"]) for g in (g1, g2)]
    # Great Tables doesn't stripe the group's cell: on a striped row (G2 starts on the fourth)
    # it keeps the table's background over the stripe
    assert first == [
        {"color": "blue", "font_weight": "bold"},
        {"background_color": "#FFFFFF", "color": "#333333", "font_weight": "bold"},
    ]
    assert ir["styles"]["conditionals"][0]["id"] == "row_striping"
    # Without striping, no background of its own
    ir = ir_of(stub_tables().tab_options(row_group_as_column=True))
    assert [r["cells"][0]["style_id"] for g in ir["table"]["tbody"] for r in g["rows"][:1]] == [
        None,
        None,
    ]


# The kit ---------------------------------------------------------------------------------------


def test_the_kit_has_every_case_and_its_expected_grid():
    cases = kit_cases()
    expected = sorted(p.stem for p in (KIT / "expected").glob("*.json"))
    assert sorted(cases) == expected
    for name in expected:
        grid = json.loads((KIT / "expected" / f"{name}.json").read_text(encoding="utf-8"))
        assert (grid["case"], grid["tier"]) == (name, "L3")
        assert grid["producer"]["package"] == "great_tables"
    assert (KIT / "SYNCED_FROM").read_text().startswith("gridwell ")
