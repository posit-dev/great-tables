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
def create_width_dict_l(data: GTData) -> WidthDict:

    boxhead = data._boxhead

    # Get the table width value
    tbl_width = data._options.table_width.value

    # Get vector representation of stub layout
    stub_layout = data._stub._get_stub_layout(options=data._options)

    n = len(boxhead)

    width_dict: WidthDict = {
        "type": [boxhead[i].type.name for i in range(n)],
        "unspec": [0] * n,  # Ensure this is initialized as a list of integers
        "lw": [0] * n,
        "pt": [0] * n,
        "column_align": [
            boxhead[i].column_align if boxhead[i].column_align else "" for i in range(n)
        ],
    }

    for i in range(n):

        raw_val = boxhead[i].column_width

        if raw_val is None or raw_val == "":

            width_dict["unspec"][i] = 1

            continue

        elif raw_val.endswith("%"):

            pct = float(raw_val.strip("%"))

            if tbl_width == "auto":
                width_dict["lw"][i] = pct / 100

            elif tbl_width.endswith("%"):
                width_dict["lw"][i] = (pct * float(tbl_width.strip("%"))) / 1e4

            else:
                width_dict["pt"][i] = (pct / 100) * convert_to_pt(tbl_width)

    # if (length(stub_layout) > sum(c('stub', 'row_group') %in% width_df$type)) {
    #     if ('stub' %in% width_df$type) {
    #       stub_row_group <- dplyr::filter(width_df, type == "stub")
    #
    #       stub_row_group$type <- "stub_row_group"
    #       stub_row_group$lw <- stub_row_group$lw / 2
    #       stub_row_group$pt <- stub_row_group$pt / 2
    #
    #       width_df$pt[width_df$type == 'stub'] <- width_df$pt[width_df$type == 'stub'] / 2
    #       width_df$lw[width_df$type == 'stub'] <- width_df$lw[width_df$type == 'stub'] / 2
    #     } else {
    #       stub_row_group <- data.frame(type = "stub_row_group", lw = 0, pt = 0)
    #     }
    #
    #     width_df <- vctrs::vec_rbind(stub_row_group, width_df)
    # }

    if tbl_width == "auto":

        if any(x > 0 for x in width_dict["unspec"]):

            # If any of the column widths are unspecified, a table width can't be inferred
            width_dict["tbl_width"] = None

        else:
            pt_total = sum(width_dict["pt"])
            lw_total = sum(width_dict["lw"])

            if pt_total <= 0:
                width_dict["tbl_width"] = f"{lw_total}\\linewidth"
            elif lw_total <= 0:
                width_dict["tbl_width"] = f"{pt_total}pt"
            else:
                width_dict["tbl_width"] = f"{pt_total}pt+{lw_total}\\linewidth"

    elif tbl_width.endswith("%"):

        lw_multiple = float(tbl_width.strip("%")) / 100
        width_dict["tbl_width"] = f"{lw_multiple}\\linewidth"

    else:

        tbl_width_pt = convert_to_pt(tbl_width)

        width_dict["tbl_width"] = f"{tbl_width_pt}pt"

    print(width_dict)

    return width_dict


def create_table_start_l(data: GTData, width_dict: WidthDict) -> str:

    # TODO: implement all logic
    return ""


def create_caption_component_l(data: GTData) -> str:

    # TODO: implement all logic
    return ""


def create_heading_component_l(data: GTData) -> str:

    # TODO: implement all logic
    return ""


def create_columns_component_l(data: GTData, width_dict: WidthDict) -> str:

    # TODO: implement all logic
    return ""


def create_body_component_l(data: GTData, width_dict: WidthDict) -> str:

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
