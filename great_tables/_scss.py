from __future__ import annotations

import re
from dataclasses import fields
from functools import cache, partial
from string import Template
from typing import TYPE_CHECKING, Any, Literal

from importlib_resources import files

from ._data_color.base import _html_color, _ideal_fgnd_color
from ._gt_data import Options, default_fonts_list, is_user_set
from ._helpers import pct, px
from ._theme import (
    COLOR_TOKENS,
    DARK,
    FONT_COLOR_VARS,
    LIGHT,
    TOKEN_OPTIONS,
    TOKEN_VARS,
    fills_foreground,
    follows_preference,
    foreground_option,
    mode_tokens,
    render_mode,
    resolve_options,
)
from ._utils import OrderedSet, _as_css_font_family_attr

if TYPE_CHECKING:
    from ._gt_data import GTData

DEFAULTS_TABLE_BACKGROUND = (
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

# A rule (at the start of a line or after another rule) whose selectors are all bare elements
ELEMENT = re.compile(r"\b(thead|tbody|tfoot|tr|td|th|p)\b")
ELEMENT_RULE = re.compile(
    r"(^|\}) *((?:thead|tbody|tfoot|tr|td|th|p)(?:\s*,\s*(?:thead|tbody|tfoot|tr|td|th|p))*\s*)\{",
    flags=re.MULTILINE,
)

DARK_HOSTS = (
    'body[data-jp-theme-light="false"]',
    "body.vscode-dark",
    "body.vscode-high-contrast:not(.vscode-high-contrast-light)",
    "body.quarto-dark",
    '[data-bs-theme="dark"]',
    'body.dark-theme[data-theme="dark"]',
)
LIGHT_HOSTS = (
    'body[data-jp-theme-light="true"]',
    "body.vscode-light",
    "body.vscode-high-contrast-light",
    "body.quarto-light",
    '[data-bs-theme="light"]',
    'body.light-theme[data-theme="light"]',
)


def font_color(color: str, dark_option: str, light_option: str) -> str:
    """Return either dark_option or light_option, whichever is higher contrast with color.

    Handles common html color kinds (like transparent), and always returns a hex color.
    """

    # Normalize return options to hex colors
    dark_normalized = _html_color(colors=[dark_option])[0]
    light_normalized = _html_color(colors=[light_option])[0]

    if color == "transparent":
        # With the `transparent` color, the font color should have the same value
        # as the `dark_option` option since the background will be transparent
        return dark_normalized
    if color in ("currentcolor", "currentColor"):
        # With two variations of `currentColor` value, normalize to `currentcolor`
        return "currentcolor"
    if color in ("inherit", "initial", "unset"):
        # For the other valid CSS color attribute values, we should pass them through
        return color

    # Normalize the color to a hexadecimal value
    color_normalized = _html_color(colors=[color])

    # Determine the ideal font color given the different background colors
    ideal_font_color = _ideal_fgnd_color(
        bgnd_color=color_normalized[0],
        light=light_normalized,
        dark=dark_normalized,
    )

    return ideal_font_color


def _clean_num(x: float) -> int | float:
    return int(x) if x == int(x) else x


def css_add(value: str | float, amount: float):
    if isinstance(value, (int, float)):
        return value + amount
    elif value.endswith("px"):
        return px(_clean_num(float(value[:-2]) + amount))
    elif value.endswith("%"):
        return pct(_clean_num(float(value[:-1]) + amount))
    else:
        raise NotImplementedError(f"Unable to add to CSS value: {value}")


def css_var(option: str) -> str:
    """The name of the custom property for an option, e.g. `data_row_padding` -> `--gt-data-row-padding`."""
    return "--gt-" + option.replace("_", "-")


def font_color_var(key: str) -> str:
    """The name of the private custom property for the text color on a `FONT_COLOR_VARS` background."""
    return "--_gt-font-color-" + key.removesuffix("_background_color").replace("_", "-")


def _scss_params(options: Options) -> tuple[dict[str, Any], dict[str, Any]]:
    """The values of the stylesheet options, and the same with default backgrounds filled in."""
    params = {
        f.name: getattr(options, f.name).value
        for f in fields(options)
        if getattr(options, f.name).scss and getattr(options, f.name).value is not None
    }
    scss_defaults = {k: params.get("table_background_color") for k in DEFAULTS_TABLE_BACKGROUND}
    return params, {**scss_defaults, **params}


@cache
def _var_params() -> dict[str, str]:
    """Template values that are the same for every table: `var()` references with defaults. (The
    dict is shared: don't change it.)"""
    default = Options()
    params: dict[str, str] = {}

    for f in fields(Options):
        info = getattr(default, f.name)
        if not info.scss:
            continue

        name = f.name
        ref = css_var(name)
        if name in TOKEN_OPTIONS["background"]:
            params[name] = "var(--_gt-background)"
        elif info.value is None:
            params[name] = f"var({ref}, var(--_gt-background))"
        elif name in TOKEN_OPTIONS["border"]:
            params[name] = f"var({ref}, var(--_gt-border))"
        elif name in TOKEN_OPTIONS["border_strong"]:
            params[name] = f"var({ref}, var(--_gt-border-strong))"
        elif name in TOKEN_OPTIONS["stripe"]:
            params[name] = f"var({ref}, var(--_gt-stripe))"
        elif name in TOKEN_OPTIONS["font_size"]:
            params[name] = f"var({ref}, var({TOKEN_VARS['font_size']}, {info.value}))"
        else:
            params[name] = f"var({ref}, {info.value})"

    params["footnotes_background_color"] = (
        f"var({css_var('footnotes_background_color')}, var(--_gt-background))"
    )

    for k in FONT_COLOR_VARS:
        params[f"font_color_{k}"] = f"var({font_color_var(k)})"

    heading_padding = f"var({css_var('heading_padding')}, {default.heading_padding.value})"
    column_labels_padding = (
        f"var({css_var('column_labels_padding')}, {default.column_labels_padding.value})"
    )
    params["heading_subtitle_padding_top"] = f"calc({heading_padding} - 1px)"
    params["heading_subtitle_padding_bottom"] = f"calc({heading_padding} + 1px)"
    params["column_labels_padding_bottom"] = f"calc({column_labels_padding} + 1px)"

    return params


@cache
def rule_params() -> dict[str, str]:
    """The template values of the options that the rules read directly, by custom property."""
    return {
        css_var(name): param
        for name, param in _var_params().items()
        if param.startswith(f"var({css_var(name)},")
    }


def _normalized(color: str) -> str:
    return _html_color(colors=[color])[0]


def private_declarations(
    data: GTData, mode: Literal["light", "dark"], options: Options
) -> dict[str, str]:
    """The private custom properties of a table for a mode (with its options resolved for the mode):
    what its rules read."""
    base = DARK if mode == "dark" else LIGHT
    tokens = mode_tokens(data, mode)
    fg = foreground_option(tokens["background"])

    default = Options()
    fills = fills_foreground(data, mode)

    def text_fallback(name: str) -> str:
        own = _normalized(getattr(default, name).value)
        if fg != name:
            return own
        return (
            f"var({TOKEN_VARS['foreground']}, {_normalized(base['foreground']) if fills else own})"
        )

    dark_color = _normalized(options.table_font_color.value)
    light_color = _normalized(options.table_font_color_light.value)

    declarations = {
        "--_gt-background": (
            f"var({css_var('table_background_color')}, "
            f"var({TOKEN_VARS['background']}, {base['background']}))"
        ),
        "--_gt-border": f"var({TOKEN_VARS['border']}, {base['border']})",
        "--_gt-border-strong": f"var({TOKEN_VARS['border_strong']}, {base['border_strong']})",
        "--_gt-stripe": f"var({TOKEN_VARS['stripe']}, {base['stripe']})",
        "--_gt-text-dark": f"var({css_var('table_font_color')}, {text_fallback('table_font_color')})",
        "--_gt-text-light": (
            f"var({css_var('table_font_color_light')}, {text_fallback('table_font_color_light')})"
        ),
    }

    _, scss_params = _scss_params(options)
    for k in FONT_COLOR_VARS:
        chosen = font_color(
            scss_params[k], options.table_font_color.value, options.table_font_color_light.value
        )
        if chosen == dark_color:
            chosen = "var(--_gt-text-dark)"
        elif chosen == light_color:
            chosen = "var(--_gt-text-light)"
        declarations[font_color_var(k)] = chosen

    return declarations


def _option_declaration(name: str, value: Any) -> tuple[str, str]:
    if name in ("table_font_color", "table_font_color_light"):
        value = _normalized(value)
    return css_var(name), str(value)


def light_public_declarations(data: GTData, options: Options) -> dict[str, str]:
    """The custom properties that Python set for a table (with its options resolved for light mode),
    as they apply in light mode."""
    theme = data._theme
    declarations: dict[str, str] = {}

    if theme is not None:
        for token, value in theme.tokens.items():
            if token in LIGHT:
                declarations[TOKEN_VARS[token]] = (
                    _normalized(value) if token == "foreground" else value
                )
        for token in ("accent", "font_size"):
            if token in theme.tokens:
                declarations[TOKEN_VARS[token]] = theme.tokens[token]

    names = options.table_font_names.value
    if names is not None and names != default_fonts_list:
        declarations[TOKEN_VARS["font"]] = _as_css_font_family_attr(
            OrderedSet(names).as_list(), value_only=True
        )

    from_theme = set(theme.options) if theme is not None else set()
    default = Options()

    for f in fields(Options):
        info = getattr(options, f.name)
        if not info.scss or info.value is None:
            continue
        if not (is_user_set(info, getattr(default, f.name)) or f.name in from_theme):
            continue

        name, value = _option_declaration(f.name, info.value)
        declarations[name] = value

    return declarations


def dark_public_declarations(data: GTData, options: Options) -> dict[str, str]:
    """The custom properties (of a table with its options resolved for dark mode) that differ in
    dark mode from those set for light mode."""
    theme = data._theme
    declarations: dict[str, str] = {}
    dark_tokens = theme.dark.tokens if theme is not None and theme.dark is not None else {}

    for token in COLOR_TOKENS:
        if token in dark_tokens:
            value = dark_tokens[token]
        elif theme is not None and token in theme.tokens:
            value = DARK[token]
        else:
            continue
        if token == "foreground" and not fills_foreground(data, "dark"):
            # (The light foreground mustn't reach the dark text, which keeps its defaults)
            declarations[TOKEN_VARS[token]] = "initial"
            continue
        declarations[TOKEN_VARS[token]] = _normalized(value) if token == "foreground" else value

    if theme is not None and theme.dark is not None:
        default = Options()
        for name in theme.dark.options:
            info = getattr(options, name)
            if is_user_set(getattr(data._options, name), getattr(default, name)):
                continue
            if info.value is None:
                continue
            key, value = _option_declaration(name, info.value)
            declarations[key] = value

    return declarations


def theme_declarations(
    data: GTData, light_options: Options | None = None
) -> tuple[dict[str, str], dict[str, str] | None]:
    """
    The custom properties for a table's light mode and, if it has one, its dark mode (then without
    a `color-scheme`, which the table takes from the page).

    `light_options` are the table's options resolved for light mode, if they are already at hand.
    """
    if light_options is None:
        light_options = resolve_options(data, "light")
    light_public = light_public_declarations(data, light_options)
    mode = render_mode(data)
    switches = follows_preference(data)

    if mode == "dark" or switches:
        dark_options = resolve_options(data, "dark")
        dark_private = private_declarations(data, "dark", dark_options)
        dark_public = dark_public_declarations(data, dark_options)

    if mode == "dark":
        return {"color-scheme": "dark", **dark_private, **light_public, **dark_public}, None

    light_private = private_declarations(data, "light", light_options)
    if not switches:
        return {"color-scheme": "light", **light_private, **light_public}, None

    # (A table with both modes takes its color scheme from the page)
    return {**light_private, **light_public}, {**dark_private, **dark_public}


VAR_START = re.compile(r"var\(\s*(--[\w-]+)\s*(,)?")


def substitute_vars(value: str, values: dict[str, str]) -> str:
    """`value` with each `var()` of a custom property in `values` replaced by its value there (by the
    `var()`'s fallback when that value is `initial`)."""
    out: list[str] = []
    start = 0

    while (m := VAR_START.search(value, start)) is not None:
        out.append(value[start : m.start()])
        depth, end = 1, m.end()
        while depth:
            depth += {"(": 1, ")": -1}.get(value[end], 0)
            end += 1
        name = m.group(1)
        fallback = substitute_vars(value[m.end() : end - 1].strip(), values) if m.group(2) else None

        if name in values and values[name] != "initial":
            out.append(values[name])
        elif name in values and fallback is not None:
            out.append(fallback)
        else:
            out.append(f"var({name}, {fallback})" if fallback is not None else f"var({name})")
        start = end

    out.append(value[start:])
    return "".join(out)


def var_blocks(scope: str, light: dict[str, str], dark: dict[str, str] | None) -> str:
    """
    The rules that declare a table's custom properties on its scope.

    A table with both modes follows the color scheme it inherits from the page (`light` unless the
    page declares one), through `light-dark()` values, and the nearest recognized host sets the
    scheme.
    """

    def block(selector: str, declarations: dict[str, str], indent: str = "") -> str:
        lines = "".join(f"{indent}  {name}: {value};\n" for name, value in declarations.items())
        return f"{indent}{selector} {{\n{lines}{indent}}}\n"

    if dark is None:
        return block(scope, light) + "\n"

    # (The dark values of the public properties are written into the private ones that read them,
    # which leaves the public ones as they are in light mode, for the page's CSS to set)
    dark_public = {name: value for name, value in dark.items() if name.startswith("--gt-")}
    switching = {}
    for name, value in dark.items():
        if name.startswith("--_gt-"):
            value = substitute_vars(value, dark_public)
            if value != light[name]:
                switching[name] = f"light-dark({light[name]}, {value})"

    # (Options that the rules read directly switch themselves, from what the rules would use in
    # light mode)
    for name, param in rule_params().items():
        if name in dark_public:
            light_value = light.get(name, substitute_vars(param, {name: "initial"}))
            switching[name] = f"light-dark({light_value}, {dark_public[name]})"

    blocks = [
        block(scope, light),
        f"@supports (color: light-dark(#000, #fff)) {{\n{block(scope, switching, '  ')}}}\n",
    ]

    # (A host's theme sets the scheme within it: in nested ones, the nearest wins. Browsers without
    # `@scope` use the rules in the layer, which lose to the `@scope` ones elsewhere)
    hosts = ((DARK_HOSTS, "dark"), (LIGHT_HOSTS, "light"))
    fallback = "".join(
        block(",\n  ".join(f"{host} {scope}" for host in names), {"color-scheme": scheme}, "  ")
        for names, scheme in hosts
    )
    blocks.append(f"@layer {{\n{fallback}}}\n")
    for names, scheme in hosts:
        rule = block(scope, {"color-scheme": scheme}, "  ")
        blocks.append(f"@scope ({', '.join(names)}) {{\n{rule}}}\n")

    return "\n".join(blocks) + "\n"


def compile_scss(
    data: GTData,
    id: str | None,
    compress: bool = True,
    all_important: bool = False,
    variables: bool = True,
) -> str:
    """Return CSS for styling a table, based on options set."""

    # Obtain the SCSS options, resolved against the table's theme and mode (as light with variables,
    # which declare both modes)
    resolved = resolve_options(data, "light" if variables else render_mode(data))

    if variables:
        final_params = _var_params()
    else:
        # Get collection of parameters that pertain to SCSS ----
        params, scss_params = _scss_params(resolved)

        # font color variables
        # TODO: at this stage, the params below (e.g. table_font_color) have to exist, right?
        p_font_color = partial(
            font_color,
            dark_option=params["table_font_color"],
            light_option=params["table_font_color_light"],
        )

        font_params = {f"font_color_{k}": p_font_color(scss_params[k]) for k in FONT_COLOR_VARS}

        final_params = {
            **scss_params,
            **font_params,
            "heading_subtitle_padding_top": css_add(scss_params["heading_padding"], -1),
            "heading_subtitle_padding_bottom": css_add(scss_params["heading_padding"], 1),
            "column_labels_padding_bottom": css_add(scss_params["column_labels_padding"], 1),
        }

    # Handle table id ----
    # Determine whether the table has an ID
    has_id = id is not None

    # Obtain the `table_id` value (might be set, might be None)
    # table_id = data._options._get_option_value(option="table_id")

    # TODO: need to implement a function to normalize color (`html_color()`)

    # Handle fonts ----
    # Get the unique list of fonts from `gt_options_dict`
    _font_names = default_fonts_list if variables else resolved.table_font_names.value
    font_list = OrderedSet(_font_names).as_list() if _font_names is not None else None

    # Generate a `font-family` string
    font_family_attr = _as_css_font_family_attr(fonts=font_list) if font_list is not None else ""
    if variables:
        font_family_attr = (
            f"font-family: var({TOKEN_VARS['font']}, "
            f"{_as_css_font_family_attr(fonts=font_list, value_only=True)});"
        )

    # Generate styles ----
    gt_table_open_str = f"#{id} table" if has_id else ".gt_table"

    # Get Google Font imports ----
    google_font_css = (
        data._google_font_imports.to_css() + "\n" if data._google_font_imports.to_css() else ""
    )

    # Process any additional CSS that will be appended at the end ----
    additional_css = resolved.table_additional_css.value

    # Determine if there are any additional CSS statements
    has_additional_css = (
        additional_css is not None and isinstance(additional_css, list) and len(additional_css) > 0
    )

    # Ensure that list items in `additional_css` are unique and then combine statements while
    # separating with `\n`; use an empty string if list is empty or value is None
    if has_additional_css:
        additional_css_unique = OrderedSet(additional_css).as_list()
        table_additional_css = "\n".join(additional_css_unique)
    else:
        table_additional_css = ""

    gt_table_class_str = f"""{gt_table_open_str} {{
          {font_family_attr}
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }}"""

    gt_styles_default = (files("great_tables") / "css/gt_styles_default.scss").read_text()

    if compress:
        gt_styles_default = re.sub(r"\s+", " ", gt_styles_default, count=0, flags=re.MULTILINE)
        gt_styles_default = re.sub(r"}", "}\n", gt_styles_default, count=0, flags=re.MULTILINE)

    compiled_css = Template(gt_styles_default).substitute(final_params)

    if has_id:
        compiled_css = re.sub(r"\.gt_", f"#{id} .gt_", compiled_css, count=0, flags=re.MULTILINE)

    # Scope each selector of the rules for bare elements (like `tr` or `td`) to the table, so that
    # they don't reach other tables on the page
    scope = f"#{id}" if has_id else ".gt_table"
    compiled_css = ELEMENT_RULE.sub(
        lambda m: m.group(1) + ELEMENT.sub(rf"{scope} \1", m.group(2)) + "{",
        compiled_css,
    )

    if all_important:
        compiled_css = re.sub(r";", " !important;", compiled_css, count=0, flags=re.MULTILINE)

    # Assemble blocks of CSS ----
    additional_css_block = f"\n{table_additional_css}\n" if has_additional_css else ""
    blocks = var_blocks(scope, *theme_declarations(data, resolved)) if variables else ""
    finalized_css = (
        f"{google_font_css}{gt_table_class_str}\n\n{blocks}{compiled_css}{additional_css_block}"
    )

    return finalized_css
