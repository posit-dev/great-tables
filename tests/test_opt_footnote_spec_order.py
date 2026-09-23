import re

import pandas as pd
import pytest
from great_tables import GT, loc
from great_tables._utils_render_html import (
    FootnoteMarkSpec,
    _apply_footnote_spec_to_mark,
    _build_footnote_mark_style,
    _create_footnote_mark_html,
    _parse_footnote_spec,
)


# ---------------------------------------------------------------------------
# _parse_footnote_spec
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "spec, expected",
    [
        ("^i", FootnoteMarkSpec(superscript=True, italic=True)),
        ("^b", FootnoteMarkSpec(superscript=True, bold=True)),
        ("bi", FootnoteMarkSpec(bold=True, italic=True)),
        ("(x)", FootnoteMarkSpec(enclosure="()")),
        ("[x]", FootnoteMarkSpec(enclosure="[]")),
        ("^i.", FootnoteMarkSpec(superscript=True, italic=True, period=True)),
        ("", FootnoteMarkSpec()),
        ("x", FootnoteMarkSpec()),
        (
            "^bi().",
            FootnoteMarkSpec(superscript=True, bold=True, italic=True, enclosure="()", period=True),
        ),
    ],
)
def test_parse_footnote_spec(spec: str, expected: FootnoteMarkSpec):
    assert _parse_footnote_spec(spec) == expected


# ---------------------------------------------------------------------------
# _apply_footnote_spec_to_mark
# ---------------------------------------------------------------------------


def test_apply_spec_parentheses():
    spec = FootnoteMarkSpec(enclosure="()")
    assert _apply_footnote_spec_to_mark("1", spec) == "(1)"


def test_apply_spec_brackets():
    spec = FootnoteMarkSpec(enclosure="[]")
    assert _apply_footnote_spec_to_mark("1", spec) == "[1]"


def test_apply_spec_period():
    spec = FootnoteMarkSpec(period=True)
    assert _apply_footnote_spec_to_mark("1", spec) == "1."


def test_apply_spec_brackets_and_period():
    spec = FootnoteMarkSpec(enclosure="[]", period=True)
    assert _apply_footnote_spec_to_mark("1", spec) == "[1]."


def test_apply_spec_no_decoration():
    spec = FootnoteMarkSpec()
    assert _apply_footnote_spec_to_mark("1", spec) == "1"


# ---------------------------------------------------------------------------
# _build_footnote_mark_style
# ---------------------------------------------------------------------------


def test_style_superscript_italic():
    spec = FootnoteMarkSpec(superscript=True, italic=True)
    style = _build_footnote_mark_style(spec)
    assert "font-style:italic" in style
    assert "font-weight:normal" in style
    assert "line-height:0" in style


def test_style_bold_no_superscript():
    spec = FootnoteMarkSpec(bold=True)
    style = _build_footnote_mark_style(spec)
    assert "font-weight:bold" in style
    assert "font-style:normal" in style
    assert "line-height:0" not in style


# ---------------------------------------------------------------------------
# _create_footnote_mark_html
# ---------------------------------------------------------------------------


def test_create_mark_html_empty():
    assert _create_footnote_mark_html("") == ""


def test_create_mark_html_default_spec():
    html = _create_footnote_mark_html("1")
    assert "font-style:italic" in html
    assert "line-height:0" in html
    assert ">1</span>" in html


def test_create_mark_html_custom_spec():
    spec = FootnoteMarkSpec(bold=True, enclosure="()")
    html = _create_footnote_mark_html("1", spec=spec)
    assert "font-weight:bold" in html
    assert ">(1)</span>" in html


# ---------------------------------------------------------------------------
# opt_footnote_spec validation
# ---------------------------------------------------------------------------


def test_opt_footnote_spec_invalid_ref():
    df = pd.DataFrame({"x": [1]})
    gt = GT(df)
    with pytest.raises(ValueError, match="Invalid characters in `spec_ref`"):
        gt.opt_footnote_spec(spec_ref="^z")


def test_opt_footnote_spec_invalid_ftr():
    df = pd.DataFrame({"x": [1]})
    gt = GT(df)
    with pytest.raises(ValueError, match="Invalid characters in `spec_ftr`"):
        gt.opt_footnote_spec(spec_ftr="!!")


# ---------------------------------------------------------------------------
# opt_footnote_spec sets options correctly
# ---------------------------------------------------------------------------


def test_opt_footnote_spec_sets_options():
    df = pd.DataFrame({"x": [1]})
    gt = GT(df).opt_footnote_spec(spec_ref="^b", spec_ftr="(x)")
    assert gt._options.footnotes_spec_ref.value == "^b"
    assert gt._options.footnotes_spec_ftr.value == "(x)"


def test_opt_footnote_spec_partial():
    df = pd.DataFrame({"x": [1]})
    gt = GT(df).opt_footnote_spec(spec_ftr="[x].")
    assert gt._options.footnotes_spec_ref.value == "^i"  # default unchanged
    assert gt._options.footnotes_spec_ftr.value == "[x]."


# ---------------------------------------------------------------------------
# opt_footnote_spec in rendered HTML — ref vs ftr independence
# ---------------------------------------------------------------------------


def _extract_footnote_mark_spans(html: str) -> list[str]:
    return re.findall(r'<span class="gt_footnote_marks"[^>]*>[^<]*</span>', html)


def test_spec_ref_and_ftr_independent():
    df = pd.DataFrame({"x": [1, 2]})
    gt = (
        GT(df)
        .tab_footnote("A note", locations=loc.body(columns="x", rows=[0]))
        .opt_footnote_spec(spec_ref="(x)", spec_ftr="[x].")
    )
    html = gt.as_raw_html()
    spans = _extract_footnote_mark_spans(html)

    # Should have at least 2 spans: one ref, one ftr
    assert len(spans) >= 2

    # Ref mark should have parentheses, no brackets
    ref_span = spans[0]
    assert "(1)" in ref_span
    assert "[" not in ref_span

    # Footer mark should have brackets and period
    ftr_span = spans[1]
    assert "[1]." in ftr_span
    assert "(" not in ftr_span


# ---------------------------------------------------------------------------
# opt_footnote_order validation
# ---------------------------------------------------------------------------


def test_opt_footnote_order_invalid():
    df = pd.DataFrame({"x": [1]})
    gt = GT(df)
    with pytest.raises(ValueError):
        gt.opt_footnote_order(order="invalid")


def test_opt_footnote_order_sets_option():
    df = pd.DataFrame({"x": [1]})
    gt = GT(df).opt_footnote_order(order="marks_first")
    assert gt._options.footnotes_order.value == "marks_first"


# ---------------------------------------------------------------------------
# opt_footnote_order — marks_last (default behavior)
# ---------------------------------------------------------------------------


def _extract_footer_texts(html: str) -> list[str]:
    tfoot = re.search(r"<tfoot>(.*)</tfoot>", html, re.DOTALL)
    if not tfoot:
        return []
    cells = re.findall(r'<td class="gt_footnote"[^>]*>(.*?)</td>', tfoot.group(1))
    return [re.sub(r"<[^>]+>", "", c).strip() for c in cells]


def test_order_marks_last():
    df = pd.DataFrame({"x": [1, 2]})
    gt = (
        GT(df)
        .tab_footnote("Marked", locations=loc.body(columns="x", rows=[0]))
        .tab_footnote("Unmarked", locations=None)
        .opt_footnote_order(order="marks_last")
    )
    texts = _extract_footer_texts(gt.as_raw_html())
    assert texts[0] == "Unmarked"
    assert "Marked" in texts[1]


# ---------------------------------------------------------------------------
# opt_footnote_order — marks_first
# ---------------------------------------------------------------------------


def test_order_marks_first():
    df = pd.DataFrame({"x": [1, 2]})
    gt = (
        GT(df)
        .tab_footnote("Marked", locations=loc.body(columns="x", rows=[0]))
        .tab_footnote("Unmarked", locations=None)
        .opt_footnote_order(order="marks_first")
    )
    texts = _extract_footer_texts(gt.as_raw_html())
    assert "Marked" in texts[0]
    assert texts[1] == "Unmarked"


# ---------------------------------------------------------------------------
# opt_footnote_order — preserve_order
# ---------------------------------------------------------------------------


def test_order_preserve_order():
    df = pd.DataFrame({"x": [1, 2]})
    gt = (
        GT(df)
        .tab_footnote("First (marked)", locations=loc.body(columns="x", rows=[0]))
        .tab_footnote("Second (unmarked)", locations=None)
        .tab_footnote("Third (marked)", locations=loc.body(columns="x", rows=[1]))
        .opt_footnote_order(order="preserve_order")
    )
    texts = _extract_footer_texts(gt.as_raw_html())
    assert len(texts) == 3
    assert "First (marked)" in texts[0]
    assert texts[1] == "Second (unmarked)"
    assert "Third (marked)" in texts[2]


def test_order_preserve_order_marks_follow_insertion():
    """Marks are assigned by insertion order, not visual reading order."""
    df = pd.DataFrame({"a": [1], "b": [2]})
    gt = (
        GT(df)
        # "b" is visually to the right of "a", but inserted first → gets mark 1
        .tab_footnote("Note on b", locations=loc.body(columns="b", rows=[0]))
        .tab_footnote("Note on a", locations=loc.body(columns="a", rows=[0]))
        .opt_footnote_order(order="preserve_order")
    )
    texts = _extract_footer_texts(gt.as_raw_html())
    # Mark 1 should be "Note on b" (inserted first), mark 2 should be "Note on a"
    assert texts[0].startswith("1")
    assert "Note on b" in texts[0]
    assert texts[1].startswith("2")
    assert "Note on a" in texts[1]


# ---------------------------------------------------------------------------
# Integration: spec + order together
# ---------------------------------------------------------------------------


def test_spec_and_order_combined():
    df = pd.DataFrame({"x": [1, 2]})
    gt = (
        GT(df)
        .tab_footnote("Note A", locations=loc.body(columns="x", rows=[0]))
        .tab_footnote("General note", locations=None)
        .opt_footnote_spec(spec_ref="^b", spec_ftr="(x)")
        .opt_footnote_order(order="marks_first")
    )
    html = gt.as_raw_html()
    texts = _extract_footer_texts(html)

    # marks_first: marked note should come first
    assert "Note A" in texts[0]
    assert texts[1] == "General note"

    # Footer mark should be parenthesized
    spans = _extract_footnote_mark_spans(html)
    ftr_spans = [s for s in spans if "(1)" in s]
    assert len(ftr_spans) >= 1

    # Ref mark should be bold superscript (no parens since ref spec is "^b")
    ref_spans = [s for s in spans if "font-weight:bold" in s and "line-height:0" in s]
    assert len(ref_spans) >= 1
