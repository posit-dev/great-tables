from __future__ import annotations

import re

from ._gt_data import GTData
from .quarto import check_quarto

from typing import TypedDict, List


LENGTH_TRANSLATIONS_TO_PX = {
    "pt": 4 / 3,
    "in": 96.0,
    "cm": 37.7952755906,
    "emu": 1 / 9525,
    "em": 16.0,
}


class WidthDict(TypedDict):
    type: List[str]
    unspec: List[int]
    lw: List[float]
    pt: List[float]
    column_align: List[str]
    tbl_width: str | None


def get_units_from_length_string(length: str) -> str:

    # Extract the units from a string that is likely in the form of '123px' or '3.23in' in
    # order to return 'px' or 'in' respectively; we'll also need to trim any whitespace and
    # convert the string to lowercase
    units_str = re.sub(r"[0-9.]+", "", length).strip().lower()

    if units_str == "":
        return "px"

    return units_str


def get_px_conversion(length: str) -> float:

    input_units = get_units_from_length_string(length)

    if input_units == "px":
        return 1.0

    valid_units = list(LENGTH_TRANSLATIONS_TO_PX.keys())

    if input_units not in valid_units:
        raise ValueError(f"Invalid units: {input_units}")

    return LENGTH_TRANSLATIONS_TO_PX.get(input_units, 0.0)


def convert_to_px(length: str) -> float:

    # Extract the units from a string that is likely in the form of '123px' or '3.23in'
    units = get_units_from_length_string(length=length)

    # Extract the numeric value from the string and convert to a float
    value = float(re.sub(r"[a-zA-Z\s]", "", length))

    # If the units are already in pixels, we can return the value as-is (w/o rounding)
    if units == "px":
        return value

    # Get the conversion factor for the units
    # - this defaults to 1.0 if the units are 'px'
    # - otherwise, it will be a value that converts the units `value` to pixels
    px_conversion = get_px_conversion(length=units)

    return round(value * px_conversion)


def convert_to_pt(x: str) -> float:

    px_value = convert_to_px(x)

    return px_value * 3 / 4


# TODO: for now this is a fairly faithful translation of the R code, but a finalized
# implementation should not return a DataFrame but rather an Info object that holds the
# column widths and other information
def create_colwidth_df_l(data: GTData) -> str:

    boxhead = data._boxhead

    # Get the table width value
    tbl_width = data._options.table_width.value

    # Get vector representation of stub layout
    stub_layout = data._stub._get_stub_layout(options=data._options)

    n = len(boxhead)

    import pandas as pd

    width_df = pd.DataFrame(
        {
            "type": [boxhead[i].type.name for i in range(n)],
            "unspec": [0] * n,
            "lw": [0] * n,
            "pt": [0] * n,
        }
    )

    for i in range(n):

        raw_val = boxhead[i].column_width

        print(raw_val)

        if raw_val is None or raw_val == "":

            width_df.loc[i, "unspec"] = 1
            print(width_df)

            continue

        elif raw_val.endswith("%"):

            pct = float(raw_val.strip("%"))

            if tbl_width == "auto":
                width_df.loc[i, "lw"] = pct / 100

            elif tbl_width.endswith("%"):
                width_df.loc[i, "lw"] = (pct * float(tbl_width.strip("%"))) / 1e4

            else:
                width_df.loc[i, "pt"] = (pct / 100) * convert_to_pt(tbl_width)

    # TODO: implement rest of the logic
    return ""


def create_table_start_l(data: GTData, colwidth_df: str) -> str:

    # TODO: implement all logic
    return ""


def create_caption_component_l(data: GTData) -> str:

    # TODO: implement all logic
    return ""


def create_heading_component_l(data: GTData) -> str:

    # TODO: implement all logic
    return ""


def create_columns_component_l(data: GTData, colwidth_df: str) -> str:

    # TODO: implement all logic
    return ""


def create_body_component_l(data: GTData, colwidth_df: str) -> str:

    # TODO: implement all logic
    return ""


def create_footer_component_l(data: GTData) -> str:

    # TODO: implement all logic
    return ""


def create_table_end_l(data: GTData) -> str:

    # TODO: implement all logic
    return ""


def derive_table_width_statement_l(data: GTData) -> str:

    # TODO: implement all logic
    return ""


def create_fontsize_statement_l(data: GTData) -> str:

    # TODO: implement all logic
    return ""


def create_wrap_start_l(data: GTData) -> str:

    if check_quarto():
        tbl_pos = ""

    else:
        latex_tbl_pos_val = data._options.latex_tbl_pos.value
        tbl_pos = f"[{latex_tbl_pos_val}]"

    latex_use_longtable = data._options.latex_use_longtable.value

    if latex_use_longtable:
        return "\\begingroup\n"
    else:
        return f"\\begin{{table}}{tbl_pos}\n"


def create_wrap_end_l(data: GTData) -> str:

    # TODO: implement all logic
    return ""
