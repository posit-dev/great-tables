from __future__ import annotations

import re
from dataclasses import fields
from functools import partial
from string import Template
from typing import TYPE_CHECKING

from importlib_resources import files

from ._data_color.base import _html_color, _ideal_fgnd_color
from ._helpers import pct, px
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


def compile_scss(
    data: GTData, id: str | None, compress: bool = True, all_important: bool = False
) -> str:
    """Return CSS for styling a table, based on options set."""

    # Obtain the SCSS options dictionary
    options = {field.name: getattr(data._options, field.name) for field in fields(data._options)}

    # Get collection of parameters that pertain to SCSS ----
    params = {k: opt.value for k, opt in options.items() if opt.scss and opt.value is not None}
    scss_defaults = {k: params.get("table_background_color") for k in DEFAULTS_TABLE_BACKGROUND}
    scss_params = {**scss_defaults, **params}

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
    _font_names = data._options.table_font_names.value
    font_list = OrderedSet(_font_names).as_list() if _font_names is not None else None

    # Generate a `font-family` string
    font_family_attr = _as_css_font_family_attr(fonts=font_list) if font_list is not None else ""

    # Generate styles ----
    gt_table_open_str = f"#{id} table" if has_id else ".gt_table"

    # Get Google Font imports ----
    google_font_css = (
        data._google_font_imports.to_css() + "\n" if data._google_font_imports.to_css() else ""
    )

    # Process any additional CSS that will be appended at the end ----
    additional_css = data._options.table_additional_css.value

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
    finalized_css = f"{google_font_css}{gt_table_class_str}\n\n{compiled_css}{additional_css_block}"

    return finalized_css
