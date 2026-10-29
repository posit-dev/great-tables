import re
from pathlib import Path

import pytest

import great_tables
from great_tables._html import HTML, Tag, TagList, css, html_escape


def test_html_escape_text():
    assert html_escape("a & b < c > d \"e\" 'f'") == "a &amp; b &lt; c &gt; d \"e\" 'f'"


def test_html_escape_attr():
    assert html_escape("a&b\"c'd<e\nf", attr=True) == "a&amp;b&quot;c&apos;d&lt;e&#10;f"


def test_html_escape_entities_not_double_escaped():
    assert html_escape("&lt;") == "&amp;lt;"


def test_css():
    assert css(width="10px", font_size=12, backgroundColor="red") == (
        "width:10px;font-size:12;background-color:red;"
    )


def test_css_skips_none():
    assert css(width="10px", color=None) == "width:10px;"
    assert css(width=None) is None


def test_tag_attrs():
    tag = Tag("th", class_="x", aria_label="lbl", rowspan=2, hidden=True, id=None, open=False)

    assert tag.attrs == {"class": "x", "aria-label": "lbl", "rowspan": "2", "hidden": ""}
    assert str(tag) == '<th class="x" aria-label="lbl" rowspan="2" hidden=""></th>'


def test_tag_attr_values_escaped():
    assert str(Tag("th", style='font-family:"A&B";')) == (
        '<th style="font-family:&quot;A&amp;B&quot;;"></th>'
    )


def test_tag_text_child_escaped_but_html_child_not():
    assert str(Tag("span", "<b>")) == "<span>&lt;b&gt;</span>"
    assert str(Tag("span", HTML("<b>x</b>"))) == "<span><b>x</b></span>"


def test_tag_void_element():
    assert str(Tag("col", style="width:10px;")) == '<col style="width:10px;"/>'
    assert str(Tag("th")) == "<th></th>"


def test_tag_nested_children_indented():
    tag = Tag("tr", Tag("th", "a"), Tag("th", Tag("span", HTML("&nbsp;"))))

    assert str(tag) == "\n".join(
        [
            "<tr>",
            "  <th>a</th>",
            "  <th>",
            "    <span>&nbsp;</span>",
            "  </th>",
            "</tr>",
        ]
    )


def test_tag_children_flattened():
    tag = Tag("tr", [Tag("th"), None, (Tag("td"), [1])], TagList(Tag("th", 2.5)))

    assert [str(x) for x in tag.children] == ["<th></th>", "<td></td>", "1", "<th>2.5</th>"]


def test_tag_invalid_child_raises():
    with pytest.raises(TypeError, match="Invalid HTML tag child of type dict"):
        Tag("th", {"a": 1})


def test_taglist():
    tags = TagList(TagList(Tag("tr", Tag("th", "a"))), Tag("tr"))

    assert str(tags) == "<tr>\n  <th>a</th>\n</tr>\n<tr></tr>"
    assert str(TagList()) == ""


def test_text_children_run_together():
    tag = Tag("div", "a", "b", Tag("span"), "c")

    assert str(tag) == "<div>\n  ab\n  <span></span>\n  c\n</div>"


# Parity with py-htmltools ---------------------------------------------------------------------
# (The renderer used htmltools for these elements before; matching its output exactly means that
# the rendered HTML of existing tables is unchanged.)


def _to_htmltools(x):
    htmltools = pytest.importorskip("htmltools")

    if isinstance(x, Tag):
        return htmltools.Tag(x.name, *[_to_htmltools(child) for child in x.children], **x.attrs)
    if isinstance(x, TagList):
        return htmltools.TagList(*[_to_htmltools(child) for child in x.children])
    if isinstance(x, HTML):
        return htmltools.HTML(x)
    return x


@pytest.mark.parametrize(
    "x",
    [
        Tag("th"),
        Tag("col"),
        Tag("col", style=css(width="25%")),
        Tag("th", "a & b", title='say "hi"\n'),
        Tag("th", HTML("<b>bold</b>"), class_="gt_col_heading", rowspan=2, colspan=1),
        Tag("tr", Tag("th", HTML("a")), Tag("th", Tag("span", HTML("&nbsp;")))),
        Tag("tr", Tag("th", Tag("span", Tag("span", "deep")))),
        Tag("div", "a", "b", Tag("span"), "c", HTML("<i>d</i>")),
        Tag("div", Tag("span"), "a", Tag("span")),
        Tag("colgroup", [Tag("col", style=css(width=w)) for w in ["10px", None, "20px"]]),
        TagList(TagList(Tag("tr", Tag("th", "x")), TagList(Tag("tr"))), Tag("tr", Tag("th"))),
        TagList(),
    ],
)
def test_matches_htmltools(x):
    assert str(x) == str(_to_htmltools(x))


def test_htmltools_only_imported_by_shiny_module():
    # htmltools isn't a dependency of great_tables (only of shiny, which `great_tables.shiny`
    # requires), so no other module may import it
    package_dir = Path(great_tables.__file__).parent
    importers = {
        path.relative_to(package_dir).as_posix()
        for path in package_dir.rglob("*.py")
        if re.search(r"^\s*(from|import)\s+htmltools\b", path.read_text(), re.MULTILINE)
    }

    assert importers == {"shiny.py"}
