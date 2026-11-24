import re

import pandas as pd
import pytest

from great_tables import GT, Theme
from great_tables._gt_data import default_fonts_list
from great_tables._theme import foreground_option, pin_mode, render_mode, resolve_options


@pytest.fixture
def gt() -> GT:
    return GT(pd.DataFrame({"x": [1, 2]}), id="abc")


def test_theme_stores_tokens_and_options():
    theme = Theme(border="#cccccc", font="Inter", font_size=14, data_row_padding=2)
    assert theme.tokens == {"border": "#cccccc", "font": ["Inter"], "font_size": "14px"}
    assert theme.options == {"data_row_padding": "2px"}
    assert theme.dark is None


def test_theme_rejects_unknown_option():
    with pytest.raises(ValueError, match="no_such_option"):
        Theme(no_such_option=1)


def test_theme_validates_option_values():
    with pytest.raises(TypeError, match="row_striping_include_table_body"):
        Theme(row_striping_include_table_body="yes")


@pytest.mark.parametrize(
    "dark",
    [
        lambda: Theme(dark=Theme()),  # nested dark
        lambda: Theme(accent="#ff0000"),  # not a color-mode token
        lambda: Theme(font="Inter"),
        lambda: Theme(row_striping_include_table_body=True),  # not a stylesheet option
        lambda: Theme(data_row_padding="9px"),  # not a color
    ],
)
def test_theme_dark_rejects_what_cannot_vary_by_mode(dark):
    with pytest.raises(ValueError):
        Theme(dark=dark())


def test_theme_dark_accepts_color_tokens_and_stylesheet_color_options():
    theme = Theme(dark=Theme(background="#101418", table_body_hlines_color="#222222"))
    assert theme.dark.tokens == {"background": "#101418"}
    assert theme.dark.options == {"table_body_hlines_color": "#222222"}


@pytest.mark.parametrize(
    "tokens, message",
    [
        ({"stripe": "oklch(70% 0.1 200)"}, "stripe"),
        ({"background": "rgb(1, 2)"}, "rgb"),
        ({"background": 123}, "background"),
        ({"foreground": "currentcolor"}, "foreground"),
        ({"foreground": "not-a-color"}, "foreground"),
        ({"border": 5}, "border"),
        ({"border_strong": ["#000000"]}, "border_strong"),
        ({"accent": 5}, "accent"),
    ],
)
def test_theme_rejects_bad_colors(tokens: dict, message: str):
    with pytest.raises(ValueError, match=message):
        Theme(**tokens)


@pytest.mark.parametrize(
    "tokens",
    [
        {"background": "navy", "foreground": "#EEE", "stripe": "#FFFFFF0F"},
        {"background": "transparent", "stripe": "currentColor"},
        {"background": "rgb(253, 246, 227)", "foreground": "hsl(192 81% 14%)"},
        {"stripe": "rgba(0,0,0,.1)"},
        {"border": "rgb(0 0 0 / 20%)", "border_strong": "var(--x)", "accent": "oklch(70% 0.1 200)"},
    ],
)
def test_theme_accepts_colors(tokens: dict):
    assert Theme(**tokens).tokens == tokens


@pytest.mark.parametrize("font", [123, ["Inter", 1], {"Inter"}])
def test_theme_rejects_bad_font(font):
    with pytest.raises(TypeError, match="font"):
        Theme(font=font)


def test_theme_rejects_google_font():
    from great_tables import google_font

    with pytest.raises(TypeError, match="font"):
        Theme(font=google_font("Inter"))


def test_theme_accepts_font_tuple():
    assert Theme(font=("Inter", "Arial")).tokens["font"] == ["Inter", "Arial"]


@pytest.mark.parametrize(
    "tokens",
    [
        {"accent": "</style><script>alert(1)</script>"},
        {"accent": '#FF0000" onload="x'},
        {"accent": "red; color: blue"},
        {"border": "#000000}"},
        {"border_strong": "{"},
        {"font": "Inter;}"},
        {"font": ["Inter", "<b>"]},
        {"font_size": "14px; color: red"},
    ],
)
def test_theme_rejects_markup_in_tokens(tokens: dict):
    with pytest.raises(ValueError, match="can't contain"):
        Theme(**tokens)


def test_from_brand_rejects_markup():
    brand_yml = pytest.importorskip("brand_yml")
    brand = brand_yml.Brand.from_yaml_str(
        'color:\n  primary: "</style><script>alert(1)</script>"\n'
    )
    with pytest.raises(ValueError, match="accent"):
        Theme.from_brand(brand)


def test_from_brand_accepts_color_functions():
    brand_yml = pytest.importorskip("brand_yml")
    brand = brand_yml.Brand.from_yaml_str(
        'color:\n  background: "rgb(253, 246, 227)"\n  foreground: "hsl(192 81% 14%)"\n'
    )
    theme = Theme.from_brand(brand)
    assert theme.tokens == {"background": "rgb(253, 246, 227)", "foreground": "hsl(192 81% 14%)"}


@pytest.mark.parametrize(
    "dark, field",
    [
        (False, "The brand's field `color.background`"),
        (True, "The dark brand's field `color.background`"),
    ],
)
def test_from_brand_names_the_field_it_cannot_use(dark: bool, field: str):
    brand_yml = pytest.importorskip("brand_yml")
    bad = brand_yml.Brand.from_yaml_str('color:\n  background: "oklch(70% 0.1 200)"\n')
    good = brand_yml.Brand.from_yaml_str('color:\n  background: "#FFFFFF"\n')
    with pytest.raises(ValueError, match=re.escape(field)):
        Theme.from_brand(good, dark=bad) if dark else Theme.from_brand(bad)


def test_theme_rejects_interactive_options():
    with pytest.raises(ValueError, match="opt_interactive"):
        Theme(ihtml_use_search=True)


def test_accent_is_written_escaped(gt: GT):
    html = gt.opt_interactive().opt_theme(Theme(accent="a&b")).as_raw_html()
    assert "--gt-i-accent: a&amp;b" in html


def test_opt_theme_stores_theme_and_mode(gt: GT):
    theme = Theme(border="#cccccc")
    assert gt._theme is None and gt._theme_mode == "auto"

    out = gt.opt_theme(theme, mode="dark")
    assert out._theme is theme and out._theme_mode == "dark"
    assert gt._theme is None  # original untouched

    assert out.opt_theme(mode="light")._theme is theme  # None leaves theme alone
    assert out.opt_theme(Theme())._theme_mode == "dark"  # None leaves mode alone

    removed = out.opt_theme(False)
    assert removed._theme is None and removed._theme_mode == "dark"  # False removes the theme
    assert removed.as_raw_html() == gt.opt_theme(mode="dark").as_raw_html()


def test_opt_theme_rejects_bad_arguments(gt: GT):
    with pytest.raises(ValueError, match="mode"):
        gt.opt_theme(mode="night")
    with pytest.raises(TypeError, match="Theme"):
        gt.opt_theme("dark")


def test_theme_repr_and_eq():
    theme = Theme(border="#cccccc", font="Inter", data_row_padding=2, dark=Theme(stripe="#222222"))
    assert repr(theme) == (
        "Theme(border='#cccccc', font=['Inter'], data_row_padding='2px', "
        "dark=Theme(stripe='#222222'))"
    )
    assert repr(Theme()) == "Theme()"
    assert eval(repr(theme)) == theme

    assert Theme(border="#cccccc") == Theme(border="#cccccc")
    assert Theme(border="#cccccc") != Theme(border="#dddddd")
    assert Theme(border="#cccccc") != Theme(border="#cccccc", dark=Theme(border="#000000"))
    assert Theme(data_row_padding="2px") != Theme(heading_padding="2px")
    assert Theme() != "Theme()"


def test_theme_ignores_none_options():
    theme = Theme(data_row_padding=None, heading_padding="3px")
    assert theme.options == {"heading_padding": "3px"}


def values(gt: GT, mode: str, *names: str) -> tuple:
    options = resolve_options(gt, mode)
    return tuple(getattr(options, name).value for name in names)


def test_resolve_unthemed_light_is_todays_defaults(gt: GT):
    assert resolve_options(gt, "light") == gt._options


def test_resolve_builtin_dark(gt: GT):
    assert values(
        gt,
        "dark",
        "table_background_color",
        "table_font_color",
        "table_font_color_light",
        "table_body_hlines_color",
        "table_border_top_color",
        "row_striping_background_color",
        "data_row_padding",
    ) == ("#1E1E1E", "#333333", "#E0E0E0", "#4A4A4A", "#6E6E6E", "#2A2A2A", "8px")


def test_explicit_option_beats_theme_in_both_modes(gt: GT):
    theme = Theme(background="#FF0000", dark=Theme(background="#0000FF"))
    for themed in (
        gt.tab_options(table_background_color="#FFFFFF").opt_theme(theme),
        gt.opt_theme(theme).tab_options(table_background_color="#FFFFFF"),
    ):
        assert values(themed, "light", "table_background_color") == ("#FFFFFF",)
        assert values(themed, "dark", "table_background_color") == ("#FFFFFF",)
        assert resolve_options(themed, "dark").table_background_color.is_set is True


def test_theme_tokens_and_options(gt: GT):
    themed = gt.opt_theme(Theme(border="#cccccc", data_row_padding="2px"))
    assert values(themed, "light", "table_body_hlines_color", "data_row_padding") == (
        "#cccccc",
        "2px",
    )
    # a light token is never used in dark mode; spacing carries over
    assert values(themed, "dark", "table_body_hlines_color", "data_row_padding") == (
        "#4A4A4A",
        "2px",
    )
    assert resolve_options(themed, "light").data_row_padding.is_set is False


def test_theme_option_beats_tokens_and_carries_to_dark(gt: GT):
    themed = gt.opt_theme(Theme(border="#cccccc", table_body_hlines_color="#abcdef"))
    assert values(themed, "light", "table_body_hlines_color") == ("#abcdef",)
    assert values(themed, "dark", "table_body_hlines_color") == ("#abcdef",)


def test_theme_dark_overrides(gt: GT):
    themed = gt.opt_theme(
        Theme(
            table_body_hlines_color="#abcdef",
            dark=Theme(background="#101418", table_body_hlines_color="#222222"),
        )
    )
    assert values(
        themed,
        "dark",
        "table_background_color",
        "table_body_hlines_color",
        "table_border_right_color",
    ) == ("#101418", "#222222", "#4A4A4A")


@pytest.mark.parametrize(
    "background, option",
    [
        ("#FFFFFF", "table_font_color"),
        ("#1E1E1E", "table_font_color_light"),
        ("black", "table_font_color_light"),
        ("transparent", "table_font_color"),
        ("currentcolor", "table_font_color"),
    ],
)
def test_foreground_option(background: str, option: str):
    assert foreground_option(background) == option


def test_foreground_follows_token_background(gt: GT):
    themed = gt.opt_theme(Theme(background="#000000", foreground="#EEEEEE"))
    assert values(themed, "light", "table_font_color", "table_font_color_light") == (
        "#333333",
        "#EEEEEE",
    )
    # an explicit background does not move the foreground token
    explicit = gt.tab_options(table_background_color="black")
    assert values(explicit, "light", "table_font_color", "table_font_color_light") == (
        "#333333",
        "#FFFFFF",
    )


def test_dark_token_background_without_foreground_keeps_contrast_text(gt: GT):
    navy = gt.opt_theme(Theme(background="#0B1E33"))
    assert values(navy, "light", "table_font_color", "table_font_color_light") == (
        "#333333",
        "#FFFFFF",
    )
    pale = gt.opt_theme(Theme(dark=Theme(background="#FAFAFA")))
    assert values(pale, "dark", "table_font_color") == ("#333333",)
    with_foreground = gt.opt_theme(Theme(background="#0B1E33", foreground="#DDEEFF"))
    assert values(with_foreground, "light", "table_font_color_light") == ("#DDEEFF",)


def test_theme_font_and_non_stylesheet_options(gt: GT):
    themed = gt.opt_theme(Theme(font="Inter", font_size=14, row_striping_include_table_body=True))
    assert values(
        themed, "light", "table_font_names", "table_font_size", "row_striping_include_table_body"
    ) == (["Inter", *default_fonts_list], "14px", True)
    # an explicit font list replaces the theme's font entirely
    explicit = themed.tab_options(table_font_names=["Courier"])
    assert values(explicit, "light", "table_font_names") == (["Courier"],)


def test_resolve_is_idempotent_and_theme_is_reusable(gt: GT):
    theme = Theme(border="#cccccc")
    themed = gt.opt_theme(theme)
    once = themed._replace(_options=resolve_options(themed, "light"))
    assert resolve_options(once, "dark") == resolve_options(themed, "dark")

    other = (
        GT(pd.DataFrame({"y": [1]})).tab_options(table_body_hlines_color="#000000").opt_theme(theme)
    )
    assert values(other, "light", "table_body_hlines_color") == ("#000000",)
    assert values(themed, "light", "table_body_hlines_color") == ("#cccccc",)


def test_option_changed_without_is_set_counts_as_set(gt: GT):
    from dataclasses import replace

    from great_tables._scss import compile_scss

    changed = gt._replace(
        _options=replace(
            gt._options,
            table_background_color=replace(gt._options.table_background_color, value="#FF0000"),
        )
    )
    assert values(changed, "light", "table_background_color") == ("#FF0000",)
    assert values(changed, "dark", "table_background_color") == ("#FF0000",)
    assert "light-dark(" not in compile_scss(changed, id="abc", variables=True)


def test_built_table_resolves_from_its_theme(gt: GT):
    themed = gt.opt_theme(Theme(border="#CCCCCC"))
    built = themed._build_data("html")
    assert resolve_options(built, "dark").table_body_hlines_color.value == "#4A4A4A"
    assert resolve_options(built, "dark") == resolve_options(themed, "dark")
    assert resolve_options(gt, "light") == gt._options


def test_pickled_built_table_resolves_the_same(gt: GT):
    import pickle

    built = gt.opt_theme(Theme(border="#CCCCCC", dark=Theme(background="#101418")))._build_data(
        "html"
    )
    unpickled = pickle.loads(pickle.dumps(built))
    for mode in ("light", "dark"):
        assert resolve_options(unpickled, mode) == resolve_options(built, mode)


def test_modes(gt: GT):
    assert render_mode(gt) == "light"
    assert render_mode(gt.opt_theme(mode="dark")) == "dark"
    assert pin_mode(gt)._theme_mode == "light"
    assert pin_mode(gt.opt_theme(mode="dark"))._theme_mode == "dark"


def test_build_applies_theme_as_light(gt: GT):
    themed = gt.opt_theme(Theme(table_font_size="20px"), mode="dark")
    built = themed._build_data(context="latex")
    assert built._options.table_font_size.value == "20px"
    assert built._options.table_background_color.value == "#FFFFFF"
    assert "#112233" in str(
        gt.opt_theme(Theme(column_labels_background_color="#112233")).as_gridwell()
    )


BRAND = """
color:
  palette:
    navy: "#001F3F"
  background: "#FDF6E3"
  foreground: "#073642"
  primary: navy
typography:
  fonts:
    - family: Inter
      source: system
  base:
    family: Inter
    size: 14px
"""

DARK_BRAND = """
color:
  background: "#101418"
  foreground: "#E6E6E6"
  primary: "#FF0000"
"""


def test_from_brand_maps_colors_and_typography():
    brand_yml = pytest.importorskip("brand_yml")
    theme = Theme.from_brand(brand_yml.Brand.from_yaml_str(BRAND))
    assert theme.tokens == {
        "background": "#FDF6E3",
        "foreground": "#073642",
        "accent": "#001F3F",
        "font": ["Inter"],
        "font_size": "14px",
    }
    assert theme.dark is None


def test_from_brand_reads_a_path_and_a_dark_brand(tmp_path):
    pytest.importorskip("brand_yml")
    light, dark = tmp_path / "_brand.yml", tmp_path / "_brand-dark.yml"
    light.write_text(BRAND)
    dark.write_text(DARK_BRAND)
    theme = Theme.from_brand(light, dark=str(dark))
    assert theme.tokens["background"] == "#FDF6E3"
    assert theme.dark.tokens == {"background": "#101418", "foreground": "#E6E6E6"}


def test_from_brand_skips_missing_fields():
    brand_yml = pytest.importorskip("brand_yml")
    theme = Theme.from_brand(brand_yml.Brand.from_yaml_str('color:\n  primary: "#FF0000"\n'))
    assert theme.tokens == {"accent": "#FF0000"}


def test_from_brand_without_brand_yml(monkeypatch):
    import sys

    monkeypatch.setitem(sys.modules, "brand_yml", None)
    with pytest.raises(ImportError, match=r"great_tables\[brand\]"):
        Theme.from_brand("_brand.yml")


def test_theme_font_with_a_quote_is_escaped(gt: GT):
    html = gt.opt_theme(Theme(font="O'Reilly Sans")).as_raw_html()
    assert "--gt-font-family: 'O\\'Reilly Sans', -apple-system," in html
