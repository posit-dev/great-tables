import re
import subprocess
import sys

import pytest

from great_tables._fontawesome import _get_icon_data, fa_svg, get_icon


def _style(svg: str) -> str:
    return re.search(r'style="([^"]*)"', svg).group(1)


# Getting icons by name ----------------------------------------------------------------------


def test_icon_data_loaded():
    data = _get_icon_data()

    assert len(data.by_full_name) > 2000
    assert {icon.style for icon in data.by_full_name.values()} == {"regular", "solid", "brands"}
    assert all(name in data.by_name for name in data.aliases.values())


def test_get_icon_prefers_regular_style():
    assert get_icon("star").full_name == "far fa-star"
    assert get_icon("star", prefer_type="solid").full_name == "fas fa-star"


def test_get_icon_single_style_used_regardless_of_preference():
    # (the hippo icon is only available in the solid style; the github icon is a brand icon)
    assert get_icon("hippo").full_name == "fas fa-hippo"
    assert get_icon("github", prefer_type="solid").full_name == "fab fa-github"


def test_get_icon_three_styles():
    assert get_icon("font-awesome").full_name == "far fa-font-awesome"
    assert get_icon("font-awesome", prefer_type="solid").full_name == "fas fa-font-awesome"


@pytest.mark.parametrize("full_name", ["fas fa-star", "far fa-star", "fab fa-github"])
def test_get_icon_full_name(full_name: str):
    assert get_icon(full_name).full_name == full_name


@pytest.mark.parametrize(
    "alias, name",
    [
        ("user-large", "user"),
        ("user-large-slash", "user-slash"),
        ("handshake-simple", "handshake"),
        ("handshake-simple-slash", "handshake-slash"),
        ("headphones-simple", "headphones"),
        ("child-rifle", "child-combatant"),
        ("vcard", "address-card"),
    ],
)
def test_get_icon_alias(alias: str, name: str):
    assert get_icon(alias).name == name


def test_get_icon_alias_prefers_regular_style():
    assert get_icon("vcard").full_name == "far fa-address-card"


@pytest.mark.parametrize("name", ["not-an-icon", "vector-square", "Star", "fas fa-github", ""])
def test_get_icon_unknown_name_raises(name: str):
    with pytest.raises(ValueError, match="does not correspond to a known icon"):
        get_icon(name)


# Sizing -------------------------------------------------------------------------------------


def test_fa_svg_default_size():
    # (the hippo icon has a viewBox of 640 x 512)
    svg = fa_svg("hippo")

    assert 'viewBox="0 0 640 512"' in svg
    assert "height:1em;width:1.25em;" in _style(svg)
    assert "preserveAspectRatio" not in svg


def test_fa_svg_height_sets_width():
    assert "height:20px;width:25px;" in _style(fa_svg("hippo", height="20px"))
    assert "height:1.5em;width:1.88em;" in _style(fa_svg("hippo", height="1.5em"))


def test_fa_svg_width_sets_height():
    assert "height:1.6em;width:2em;" in _style(fa_svg("hippo", width="2em"))


def test_fa_svg_percent_length_used_for_both():
    assert "height:50%;width:50%;" in _style(fa_svg("hippo", height="50%"))
    assert "height:50%;width:50%;" in _style(fa_svg("hippo", width="50%"))


def test_fa_svg_height_and_width_stretch_icon():
    svg = fa_svg("hippo", height="1em", width="3em")

    assert 'preserveAspectRatio="none"' in svg
    assert "height:1em;width:3em;" in _style(svg)


@pytest.mark.parametrize("length", ["20", "px", "1.5 em", "-1em", "1EM", "2parsecs"])
def test_fa_svg_invalid_length_raises(length: str):
    with pytest.raises(ValueError):
        fa_svg("star", height=length)

    with pytest.raises(ValueError):
        fa_svg("star", height="1em", width=length)


# Styles and accessibility -------------------------------------------------------------------


def test_fa_svg_default_style():
    assert _style(fa_svg("star")) == (
        "fill:currentColor;height:1em;width:1.12em;margin-left:auto;margin-right:auto;"
        "position:relative;vertical-align:-0.125em;overflow:visible;"
    )


def test_fa_svg_style_options():
    svg = fa_svg(
        "star",
        fill="red",
        fill_opacity=0.5,
        stroke="blue",
        stroke_width="2px",
        stroke_opacity=0.25,
        margin_left="1px",
        margin_right="2px",
        vertical_align="middle",
        position="absolute",
    )

    assert _style(svg) == (
        "fill:red;fill-opacity:0.5;stroke:blue;stroke-width:2px;stroke-opacity:0.25;height:1em;"
        "width:1.12em;margin-left:1px;margin-right:2px;position:absolute;vertical-align:middle;"
        "overflow:visible;"
    )


def test_fa_svg_style_escaped():
    assert 'style="fill:url(&quot;#g&quot;);' in fa_svg("star", fill='url("#g")')


def test_fa_svg_markup():
    icon = get_icon("star")

    assert fa_svg("star") == (
        '<svg viewBox="0 0 576 512" aria-hidden="true" role="img" class="fa" '
        f'style="{_style(fa_svg("star"))}"><path d="{icon.path}"/></svg>'
    )


def test_fa_svg_decorative_icon_hidden():
    svg = fa_svg("star")

    assert 'aria-hidden="true" role="img"' in svg
    assert "aria-label" not in svg and "<title>" not in svg


def test_fa_svg_semantic_icon_labelled():
    assert 'aria-label="Star" role="img"' in fa_svg("star", a11y="sem")
    assert "<title>Star</title>" in fa_svg("star", a11y="sem")


def test_fa_svg_semantic_icon_title_escaped():
    svg = fa_svg("star", a11y="sem", title='5 "stars" & <up>')

    assert 'aria-label="5 &quot;stars&quot; &amp; &lt;up&gt;"' in svg
    assert '<title>5 "stars" &amp; &lt;up&gt;</title>' in svg
    assert "aria-hidden" not in svg


def test_fa_svg_no_a11y_attrs():
    svg = fa_svg("star", a11y="none")

    assert "aria-" not in svg and "role=" not in svg


def test_fa_svg_title_on_decorative_icon():
    svg = fa_svg("star", title="Rating")

    assert "<title>Rating</title>" in svg
    assert 'aria-hidden="true"' in svg


# Loading ------------------------------------------------------------------------------------


def test_importing_great_tables_needs_neither_faicons_nor_htmltools():
    # The icon data is only read when an icon is first generated
    code = (
        "import sys\n"
        "sys.modules['faicons'] = None\n"
        "sys.modules['htmltools'] = None\n"
        "import great_tables\n"
        "from great_tables._fontawesome import _get_icon_data\n"
        "assert _get_icon_data.cache_info().currsize == 0\n"
        "import polars as pl\n"
        "gt = great_tables.GT(pl.DataFrame({'icon': ['star', 'hippo']})).fmt_icon('icon')\n"
        "assert gt.as_raw_html().count('<svg') == 2\n"
    )
    subprocess.run([sys.executable, "-c", code], check=True)
