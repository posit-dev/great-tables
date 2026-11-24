from __future__ import annotations

import copy
import re
from dataclasses import fields
from typing import TYPE_CHECKING, Any, Literal

from ._data_color.base import _ideal_fgnd_color
from ._data_color.utils import _html_color
from ._gt_data import Options, OptionsInfo, _ThemeOptionsInfo, default_fonts_list, is_user_set
from ._options import validate_option_values
from .quarto import is_quarto_render, quarto_format_is_html

if TYPE_CHECKING:
    from pathlib import Path

    from brand_yml import Brand

    from ._gt_data import GTData
    from ._types import GTSelf

ThemeMode = Literal["auto", "light", "dark"]

COLOR_TOKENS = ("background", "foreground", "border", "border_strong", "stripe")

# The CSS color keywords that have no brightness of their own
CSS_COLOR_KEYWORDS = ("transparent", "currentcolor", "inherit", "initial", "unset")

# Characters that could end the `<style>` block, rule or declaration a token is written into
UNSAFE = re.compile(r'[<>{};"]')

FONT_COLOR_VARS = (
    "table_background_color",
    "heading_background_color",
    "column_labels_background_color",
    "row_group_background_color",
    "stub_background_color",
    "stub_row_group_background_color",
    "summary_row_background_color",
    "grand_summary_row_background_color",
    "footnotes_background_color",
    "source_notes_background_color",
    "row_striping_background_color",
)

TOKEN_VARS = {
    "background": "--gt-color-background",
    "foreground": "--gt-color-foreground",
    "border": "--gt-color-border",
    "border_strong": "--gt-color-border-strong",
    "stripe": "--gt-color-stripe",
    "accent": "--gt-color-accent",
    "font": "--gt-font-family",
    "font_size": "--gt-font-size",
}

LIGHT = {
    "background": "#FFFFFF",
    "foreground": "#333333",
    "border": "#D3D3D3",
    "border_strong": "#A8A8A8",
    "stripe": "#F4F4F4",
}

DARK = {
    "background": "#1E1E1E",
    "foreground": "#E0E0E0",
    "border": "#4A4A4A",
    "border_strong": "#6E6E6E",
    "stripe": "#2A2A2A",
}

_DEFAULT_OPTIONS = Options()

TOKEN_OPTIONS = {
    "background": ("table_background_color",),
    "border": tuple(
        f.name
        for f in fields(Options)
        if getattr(_DEFAULT_OPTIONS, f.name).value == LIGHT["border"]
    ),
    "border_strong": ("table_border_top_color", "table_border_bottom_color"),
    "stripe": ("row_striping_background_color",),
    "font_size": ("table_font_size",),
}


class Theme:
    """
    A set of design tokens and table options that style a table.

    A `Theme` collects values for a small set of semantic tokens, plus any option accepted by
    `GT.tab_options()`, so that they can be applied to a table together with `GT.opt_theme()`. Only
    the tokens and options that are given are stored. Each token is exposed in the table's CSS as a
    custom property:

    | Token           | CSS variable               |
    |-----------------|----------------------------|
    | `background`    | `--gt-color-background`    |
    | `foreground`    | `--gt-color-foreground`    |
    | `border`        | `--gt-color-border`        |
    | `border_strong` | `--gt-color-border-strong` |
    | `stripe`        | `--gt-color-stripe`        |
    | `accent`        | `--gt-color-accent`        |
    | `font`          | `--gt-font-family`         |
    | `font_size`     | `--gt-font-size`           |

    Parameters
    ----------
    background
        The background color of the table.
    foreground
        The color of text in the table.
    border
        The color of the table's regular lines.
    border_strong
        The color of the table's emphasized lines, such as the one under the column labels.
    stripe
        The background color of striped rows.
    accent
        The accent color, used for interactive elements.
    font
        The font or fonts of the table, as a single name or a list of names in order of preference.
    font_size
        The base font size of the table, as a CSS length or a number of pixels.
    dark
        A `Theme` with the values to use instead when the table is shown in dark mode. It can hold
        only the color tokens `background`, `foreground`, `border`, `border_strong` and `stripe`,
        and color options that are written to the table's stylesheet (such as
        `table_body_hlines_color`). A background option of the theme with no value here keeps an
        `"auto"` table light, and a border color option with no value here is blended toward the
        text color in dark mode.
    **options
        Any option accepted by `GT.tab_options()`, for example `data_row_padding`.

    Examples
    --------
    A theme that sets a border color and font, with its own colors for dark mode.

    ```{python}
    from great_tables import GT, Theme, exibble

    theme = Theme(
        border="#CCCCCC",
        font="Inter",
        dark=Theme(background="#101418", border="#2A3038"),
    )

    GT(exibble[["num", "char", "currency"]]).opt_theme(theme)
    ```
    """

    tokens: dict[str, Any]
    options: dict[str, Any]
    dark: Theme | None

    def __init__(
        self,
        *,
        background: str | None = None,
        foreground: str | None = None,
        border: str | None = None,
        border_strong: str | None = None,
        stripe: str | None = None,
        accent: str | None = None,
        font: str | list[str] | None = None,
        font_size: str | int | None = None,
        dark: Theme | None = None,
        **options: Any,
    ) -> None:
        given = {
            "background": background,
            "foreground": foreground,
            "border": border,
            "border_strong": border_strong,
            "stripe": stripe,
            "accent": accent,
            "font": font,
            "font_size": font_size,
        }
        self.tokens = {k: v for k, v in given.items() if v is not None}

        if isinstance(font, str):
            self.tokens["font"] = [font]
        elif isinstance(font, (list, tuple)) and all(isinstance(name, str) for name in font):
            self.tokens["font"] = list(font)
        elif font is not None:
            raise TypeError(
                "`font` must be a font name or a list or tuple of font names, "
                f"but received type `{type(font).__name__}`."
            )

        if font_size is not None:
            self.tokens["font_size"] = Options().table_font_size._validate_value(
                font_size, option_name="font_size"
            )

        _check_tokens(self.tokens)

        interactive = [k for k in options if k.startswith("ihtml_")]
        if interactive:
            raise ValueError(
                f"A `Theme` can't set the options of interactive tables ({', '.join(interactive)}): "
                "set them with `GT.opt_interactive()`."
            )

        self.options = validate_option_values(Options(), options)

        if dark is not None:
            _check_dark(dark)
        self.dark = dark

    @classmethod
    def from_brand(
        cls,
        brand: str | Path | Brand | None = None,
        dark: str | Path | Brand | None = None,
    ) -> Theme:
        """
        Build a `Theme` from a brand.yml file.

        A [brand.yml](https://posit-dev.github.io/brand-yml/) file describes the colors and fonts of
        a brand. `Theme.from_brand()` reads one and maps these fields to the tokens of a `Theme`:

        | brand.yml field          | `Theme` token |
        |--------------------------|---------------|
        | `color.background`       | `background`  |
        | `color.foreground`       | `foreground`  |
        | `color.primary`          | `accent`      |
        | `typography.base.family` | `font`        |
        | `typography.base.size`   | `font_size`   |

        Colors that name an entry of `color.palette` are used as the color of that entry. Fields
        that the brand does not have are left out of the theme. This method requires the
        [brand_yml](https://pypi.org/project/brand-yml/) package, which is installed with
        `pip install great_tables[brand]`.

        Parameters
        ----------
        brand
            The brand to use: the path to a brand.yml file, a `brand_yml.Brand` object, or `None` to
            have `brand_yml` find a brand file itself (see `brand_yml.Brand.from_yaml()`).
        dark
            A brand to use in dark mode, given in the same ways as `brand`. Only its `background`
            and `foreground` colors are used, as the colors of the theme's `dark=` theme.

        Returns
        -------
        Theme
            A `Theme` that can be applied to a table with `GT.opt_theme()`.

        Examples
        --------
        Take a brand file `_brand.yml` with these contents.

        ```yaml
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
        ```

        Building a theme from it and applying the theme to a table looks like this.

        ```python
        from great_tables import GT, Theme, exibble

        theme = Theme.from_brand("_brand.yml")

        GT(exibble).opt_theme(theme)
        ```

        The result is the same as the theme made directly with
        `Theme(background="#FDF6E3", foreground="#073642", accent="#001F3F", font="Inter",
        font_size="14px")`. A second brand file can supply colors for dark mode with
        `Theme.from_brand("_brand.yml", dark="_brand-dark.yml")`.
        """
        try:
            from brand_yml import Brand as BrandCls
        except ImportError as e:
            raise ImportError(
                "`Theme.from_brand()` requires the `brand_yml` package. "
                "Install it with `pip install great_tables[brand]`."
            ) from e

        def load(source: str | Path | Brand | None) -> Brand:
            if isinstance(source, BrandCls):
                return source
            return BrandCls.from_yaml(source)

        brand_obj = load(brand)
        color = brand_obj.color
        base = brand_obj.typography.base if brand_obj.typography is not None else None

        tokens: dict[str, Any] = {}
        if color is not None:
            tokens.update(
                background=color.background, foreground=color.foreground, accent=color.primary
            )
        if base is not None:
            tokens.update(font=base.family, font_size=base.size)

        dark_theme = None
        if dark is not None:
            dark_color = load(dark).color
            if dark_color is not None:
                dark_theme = cls(background=dark_color.background, foreground=dark_color.foreground)

        return cls(**tokens, dark=dark_theme)


def _is_color(value: Any, keywords: bool) -> bool:
    """Whether a value is a color the table can find the brightness of (or, with `keywords`, one of
    `CSS_COLOR_KEYWORDS`)."""
    if not isinstance(value, str):
        return False
    if keywords and value.strip().lower() in CSS_COLOR_KEYWORDS:
        return True
    try:
        _html_color([value])
    except ValueError:
        return False
    return True


def _check_tokens(tokens: dict[str, Any]) -> None:
    """Raise if a token's value can't be used, or could break out of the CSS it is written into."""
    for token, value in tokens.items():
        for item in value if isinstance(value, list) else [value]:
            if isinstance(item, str) and UNSAFE.search(item):
                raise ValueError(
                    f"`{token}` can't contain any of the characters < > {{ }} ; \", "
                    f"but received {item!r}."
                )

    for token in ("background", "foreground", "stripe"):
        keywords = token != "foreground"
        if token in tokens and not _is_color(tokens[token], keywords):
            accepted = "a color name or a hexadecimal color"
            if keywords:
                accepted += f", or one of {', '.join(CSS_COLOR_KEYWORDS)}"
            raise ValueError(f"`{token}` must be {accepted}, but received {tokens[token]!r}.")

    for token in ("border", "border_strong", "accent"):
        if token in tokens and not isinstance(tokens[token], str):
            raise ValueError(
                f"`{token}` must be a CSS color, as a string, "
                f"but received type `{type(tokens[token]).__name__}`."
            )


def _check_dark(dark: Theme) -> None:
    if not isinstance(dark, Theme):
        raise TypeError(f"`dark` must be a `Theme`, but received type `{type(dark).__name__}`.")

    if dark.dark is not None:
        raise ValueError("`dark` cannot itself have a `dark` theme.")

    not_colors = [k for k in dark.tokens if k not in COLOR_TOKENS]
    if not_colors:
        raise ValueError(
            f"A `dark` theme can only set the color tokens {', '.join(COLOR_TOKENS)}, "
            f"but received: {', '.join(not_colors)}."
        )

    default_options = Options()
    not_colors = [k for k in dark.options if not is_color_option(k, default_options)]
    if not_colors:
        raise ValueError(
            "A `dark` theme can only set color options that are written to the table's "
            f"stylesheet (such as `table_body_hlines_color`), but received: "
            f"{', '.join(not_colors)}."
        )


def is_color_option(name: str, default_options: Options) -> bool:
    """Whether an option is a color written to the table's stylesheet (which can vary by mode, as
    `light-dark()` takes colors only)."""
    return getattr(default_options, name).scss and name.endswith(("_color", "_color_light"))


def is_border_color_option(name: str, default_options: Options) -> bool:
    """Whether an option is the color of a border or of lines between cells (written to the table's
    stylesheet)."""
    return is_color_option(name, default_options) and ("_border_" in name or "lines_" in name)


def dark_blend(color: str) -> str:
    """A color blended toward the text color, for use in dark mode: a color chosen for a light table
    (black lines, dark text) would vanish on a dark one."""
    return f"color-mix(in srgb, {color} 35%, currentcolor)"


def opt_theme(self: GTSelf, theme: Theme | None = None, mode: ThemeMode | None = None) -> GTSelf:
    """
    Apply a theme to the table and choose its color mode.

    The `opt_theme()` method stores a `Theme` and a color mode on the table. The theme gives the
    table its colors, fonts and other options, and can hold a separate set of colors for dark mode
    through its `dark=` argument. The mode picks which colors are used: `"light"` always uses the
    light colors, `"dark"` always uses the dark colors, and `"auto"` (the default) follows the
    color scheme of the page the table is shown in.

    Parameters
    ----------
    theme
        The `Theme` to apply. If `None`, the theme already on the table is left as it is.
    mode
        The color mode, one of `"auto"`, `"light"` or `"dark"`. If `None`, the mode already on the
        table is left as it is. An `"auto"` table stays light when a background color is set for
        light mode only (with `tab_options()`, `opt_stylize()`, or a theme option with no value in
        the theme's `dark=`).

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using select columns from the `exibble` dataset, let's create a table and choose its color
    mode with `opt_theme()`.

    ```{python}
    from great_tables import GT, Theme, exibble

    gt_tbl = GT(exibble[["num", "char", "currency", "row"]], rowname_col="row")

    gt_tbl.opt_theme(mode="dark")
    ```

    A custom `Theme` sets the tokens and options that should differ from the defaults.

    ```{python}
    gt_tbl.opt_theme(Theme(border="#9AA5B1", font="Georgia", data_row_padding=4))
    ```

    Use the `dark=` argument of `Theme` to give the table its own colors in dark mode.

    ```{python}
    gt_tbl.opt_theme(
        Theme(border="#9AA5B1", dark=Theme(background="#101418", border="#2A3038")),
        mode="dark",
    )
    ```
    """
    if theme is not None and not isinstance(theme, Theme):
        raise TypeError(f"`theme` must be a `Theme`, but received type `{type(theme).__name__}`.")

    if mode is not None and mode not in ("auto", "light", "dark"):
        raise ValueError(f'`mode` must be one of "auto", "light" or "dark", but received {mode!r}.')

    return self._replace(
        _theme=self._theme if theme is None else theme,
        _theme_mode=self._theme_mode if mode is None else mode,
    )


def mode_tokens(data: GTData, mode: Literal["light", "dark"]) -> dict[str, str]:
    """The color tokens in effect for a mode, as a new dict."""
    theme = data._theme

    if mode == "dark":
        tokens = dict(DARK)
        if theme is not None and theme.dark is not None:
            tokens.update(theme.dark.tokens)
    else:
        tokens = dict(LIGHT)
        if theme is not None:
            tokens.update({k: v for k, v in theme.tokens.items() if k in COLOR_TOKENS})

    return tokens


def fills_foreground(data: GTData, mode: Literal["light", "dark"]) -> bool:
    """
    Whether the `foreground` token is the text color on the token background in a mode.

    It is when the theme gives a foreground for the mode (in dark mode, in its `dark=` theme), or
    when the mode's background is the built-in one. Otherwise the text options keep their defaults,
    so the text color is chosen for contrast with the background.
    """
    theme = data._theme
    base = DARK if mode == "dark" else LIGHT
    if mode == "dark":
        given = theme.dark.tokens if theme is not None and theme.dark is not None else {}
    else:
        given = theme.tokens if theme is not None else {}

    background = given.get("background", base["background"])
    return "foreground" in given or background.upper() == base["background"]


def foreground_option(background: str) -> Literal["table_font_color", "table_font_color_light"]:
    """The option that holds the text color to use on a background."""
    if background.strip().lower() in CSS_COLOR_KEYWORDS:
        return "table_font_color"

    light = "#FFFFFF"
    dark = "#000000"
    ideal = _ideal_fgnd_color(_html_color([background])[0], light=light, dark=dark)

    return "table_font_color_light" if ideal == light else "table_font_color"


def resolve_options(data: GTData, mode: Literal["light", "dark"]) -> Options:
    """
    The options of a table for a mode, from its explicit options, theme and the built-in tokens.

    An option set explicitly always wins. Otherwise a value given for the option by the theme (by
    its `dark=` theme first, in dark mode) wins over a value derived from a token.
    """
    theme = data._theme
    tokens = mode_tokens(data, mode)

    derived: dict[str, Any] = {}
    for token, names in TOKEN_OPTIONS.items():
        if token == "font_size":
            continue
        for name in names:
            derived[name] = tokens[token]

    if fills_foreground(data, mode):
        derived[foreground_option(tokens["background"])] = tokens["foreground"]

    if theme is not None:
        if "font_size" in theme.tokens:
            derived["table_font_size"] = theme.tokens["font_size"]
        if "font" in theme.tokens:
            derived["table_font_names"] = [*theme.tokens["font"], *default_fonts_list]

    sources = []
    if mode == "dark" and theme is not None and theme.dark is not None:
        sources.append(theme.dark.options)
    if theme is not None:
        sources.append(theme.options)
    sources.append(derived)

    default = Options()
    resolved = {}
    for f in fields(Options):
        current = getattr(data._options, f.name)
        base = getattr(default, f.name)
        if is_user_set(current, base):
            resolved[f.name] = current
            continue

        for source in sources:
            if f.name in source:
                value = copy.deepcopy(source[f.name])
                # (A value the theme changed is marked as derived, so that it isn't taken as set)
                info_cls = OptionsInfo if value == base.value else _ThemeOptionsInfo
                resolved[f.name] = info_cls(base.scss, base.category, base.type, value)
                break
        else:
            resolved[f.name] = base

    return Options(**resolved)


def render_mode(data: GTData) -> Literal["light", "dark"]:
    """The mode a table is rendered in: dark only when the theme mode is `"dark"`."""
    return "dark" if data._theme_mode == "dark" else "light"


def uses_variables(variables: bool = True) -> bool:
    """
    Whether a table's CSS uses variables: in a Quarto render, only when its format is known to be
    HTML.
    """
    return variables and not (is_quarto_render() and not quarto_format_is_html())


def follows_preference(data: GTData) -> bool:
    """
    Whether a table follows the color scheme of the page it is shown in (on a page that the table
    makes, the viewer's preference).

    Only a table in `"auto"` mode does, and not one with a background color set explicitly (with
    `tab_options()` or `opt_stylize()`, or as a theme's option with no value in its `dark=` theme),
    as those colors were chosen for a light table.
    """
    if data._theme_mode != "auto":
        return False

    theme = data._theme
    light = theme.options if theme is not None else {}
    dark = theme.dark.options if theme is not None and theme.dark is not None else {}

    default = Options()
    return not any(
        is_user_set(getattr(data._options, name), getattr(default, name))
        or (name in light and name not in dark)
        for name in FONT_COLOR_VARS
        if hasattr(default, name)
    )


def color_scheme_style_attr(data: GTData, variables: bool = True) -> str:
    """
    The `style` attribute (with a leading space) that declares the color scheme on the root element
    of a table's page, or `""`. (Unlike a `<meta>`, it doesn't change the scheme of a page that the
    HTML is inserted into.)
    """
    if data._theme_mode == "dark":
        scheme = "dark"
    elif follows_preference(data) and uses_variables(variables):
        scheme = "light dark"
    else:
        return ""

    return f' style="color-scheme: {scheme}"'


def pin_mode(data: GTSelf) -> GTSelf:
    """Turn the `"auto"` theme mode into `"light"`, and leave other modes unchanged."""
    if data._theme_mode == "auto":
        return data._replace(_theme_mode="light")

    return data
