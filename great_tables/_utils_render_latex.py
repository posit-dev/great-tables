from __future__ import annotations

from ._gt_data import GTData


def create_colwidth_df_l(data: GTData) -> str:
    return ""


def create_table_start_l(data: GTData, colwidth_df: str) -> str:
    return ""


def create_caption_component_l(data: GTData) -> str:
    return ""


def create_heading_component_l(data: GTData) -> str:
    return ""


def create_columns_component_l(data: GTData, colwidth_df: str) -> str:
    return ""


def create_body_component_l(data: GTData, colwidth_df: str) -> str:
    return ""


def create_footer_component_l(data: GTData) -> str:
    return ""


def create_table_end_l(data: GTData) -> str:
    return ""


def derive_table_width_statement_l(data: GTData) -> str:
    return ""


def create_fontsize_statement_l(data: GTData) -> str:
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
    return ""
