from __future__ import annotations

import pkg_resources
import re
import webcolors as wc

from dataclasses import fields
from functools import partial
from typing import Optional
from string import Template

from ._gt_data import GTData
from ._utils import _as_css_font_family_attr, _unique_set

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
)

FONT_COLOR_VARS = (
    "table_background_color",
    "heading_background_color",
    "column_labels_background_color",
    "column_labels_background_color",
    "row_group_background_color",
    "stub_background_color",
    "stub_row_group_background_color",
    "summary_row_background_color",
    "grand_summary_row_background_color",
    "footnotes_background_color",
    "source_notes_background_color",
)


def font_color(color: str, table_font_color: str, table_font_color_light: str):
    if color.startswith("#"):
        rgb = wc.hex_to_rgb(color)
    elif color.startswith("rgb") and "%" in color:
        # TODO: rgb_percent_to_rgb() expects a tuple
        raise NotImplementedError()
        rgb = wc.rgb_percent_to_rgb(color)
    else:
        rgb = wc.name_to_rgb(color)

    if (rgb.red * 0.299 + rgb.green * 0.587 + rgb.blue * 0.114) > 186:
        return table_font_color

    return table_font_color_light


def css_add(value: str | int, amount: int):
    if isinstance(value, int):
        return value + amount
    elif value.endswith("px"):
        return f"{int(value[:-2]) + amount}px"
    elif value.endswith("%"):
        return f"{int(value[:-1]) + amount}%"
    else:
        raise NotImplementedError(f"Unable to add to CSS value: {value}")


def compile_scss(data: GTData, id: Optional[str], compress: bool = True) -> str:
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
        table_font_color=params["table_font_color"],
        table_font_color_light=params["table_font_color_light"],
    )

    font_params = {f"font_color_{k}": p_font_color(scss_params[k]) for k in FONT_COLOR_VARS}

    final_params = {
        **scss_params,
        **font_params,
        "heading_subtitle_padding_top": css_add(scss_params["heading_padding"], -1),
        "heading_subtitle_padding_bottom": css_add(scss_params["heading_padding"], 1),
        "heading_padding_bottom": css_add(scss_params["heading_padding"], 1),
    }

    # Handle table id ----
    # Determine whether the table has an ID
    has_id = id is not None

    # Obtain the `table_id` value (might be set, might be None)
    # table_id = data._options._get_option_value(option="table_id")

    # TODO: need to implement a function to normalize color (`html_color()`)

    # Handle fonts ----
    # Get the unique list of fonts from `gt_options_dict`
    font_list = _unique_set(data._options.table_font_names.value)

    # Generate a `font-family` string
    if font_list is not None:
        font_family_attr = _as_css_font_family_attr(fonts=font_list)
    else:
        font_family_attr = ""

    # Generate styles ----
    gt_table_open_str = f"#{id} table" if has_id else ".gt_table"

    gt_table_class_str = f"""{gt_table_open_str} {{
          {font_family_attr}
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }}"""

    gt_styles_default_file = open(
        pkg_resources.resource_filename("great_tables", "css/gt_styles_default.scss")
    )

    gt_styles_default = gt_styles_default_file.read()

    if compress:
        gt_styles_default = re.sub(r"\s+", " ", gt_styles_default, 0, re.MULTILINE)
        gt_styles_default = re.sub(r"}", "}\n", gt_styles_default, 0, re.MULTILINE)

    compiled_css = Template(gt_styles_default).substitute(final_params)

    if has_id:
        compiled_css = re.sub(r"\.gt_", f"#{id} .gt_", compiled_css, 0, re.MULTILINE)
        compiled_css = re.sub(r"thead", f"#{id} thead", compiled_css, 0, re.MULTILINE)
        compiled_css = re.sub(r"^( p|p) \{", f"#{id} p {{", compiled_css, 0, re.MULTILINE)

    finalized_css = f"{gt_table_class_str}\n\n{compiled_css}"

    return finalized_css
