from __future__ import annotations

import re

from ._gt_data import GTData
from ._tbl_data import _get_cell, cast_frame_to_string, replace_null_frame
from .quarto import check_quarto
from great_tables._spanners import spanners_print_matrix
from great_tables._utils import heading_has_subtitle, heading_has_title
from great_tables._utils_render_html import _get_spanners_matrix_height

from typing import TypedDict, List


LENGTH_TRANSLATIONS_TO_PX = {
    "px": 1.0,
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


def is_css_length_string(x: str) -> bool:

    # This checks if there is a number followed by an optional string (only of letters)
    return re.match(r"^[0-9.]+[a-zA-Z]*$", x) is not None


def is_number_without_units(x: str) -> bool:

    # This check if the string is a number without any text
    return re.match(r"^[0-9.]+$", x) is not None


def css_length_has_supported_units(x: str, no_units_valid: bool = True) -> bool:

    # Check if the the string is a valid CSS length string with a text string

    if not is_css_length_string(x):
        return False

    # If the string is a number without units, we can return the value of `no_units_valid`
    if is_number_without_units(x):
        return no_units_valid

    units = get_units_from_length_string(x)

    return units in LENGTH_TRANSLATIONS_TO_PX.keys()


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


def escape_latex(text: str) -> str:

    # Replace characters in a string that's to be used in a LaTeX context

    latex_escape_regex = "[\\\\&%$#_{}~^]"
    text = re.sub(latex_escape_regex, lambda match: "\\" + match.group(), text)

    return text


# TODO: for now this is a fairly faithful translation of the R code, but a finalized
# implementation should not return a DataFrame but rather an Info object that holds the
# column widths and other information
def create_width_dict_l(data: GTData) -> WidthDict:

    boxhead = data._boxhead

    # Get the table width value
    tbl_width = data._options.table_width.value

    # Get list representation of stub layout
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

    return width_dict


def create_singlecolumn_width_text_l(pt: float, lw: float) -> str:

    if pt <= 0 and lw <= 0:
        out_txt = "0pt"
    elif pt <= 0:
        out_txt = "\\dimexpr {:.2f}\\linewidth -2\\tabcolsep-1.5\\arrayrulewidth".format(lw)
    elif lw <= 0:
        out_txt = "\\dimexpr {:.2f}pt -2\\tabcolsep-1.5\\arrayrulewidth".format(pt)
    else:
        out_txt = "\\dimexpr {:.2f}pt + {:.2f}\\linewidth -2\\tabcolsep-1.5\\arrayrulewidth".format(
            pt, lw
        )

    return out_txt


def calculate_multicolumn_width_text_l(
    begins: list[str], ends: list[str], width_dict: WidthDict
) -> str:

    out_text = [""] * len(begins)

    for i in range(len(begins)):

        ind = range(begins[i], ends[i])

        # If any of the combined columns has an unspecified width, it can't be determined
        # so it is left blank
        if any(width_dict["unspec"][i] > 0):

            continue

        pt_total = sum(width_dict["pt"][ind])
        lw_total = sum(width_dict["lw"][ind])

        if pt_total <= 0 & lw_total <= 0:

            continue

        else:

            out_text[i] = create_singlecolumn_width_text_l(pt=pt_total, lw=lw_total)

    return out_text


def latex_heading_row(content: list[str]) -> str:

    return "".join([" & ".join(content) + " \\\\ \n", "\\midrule\\addlinespace[2.5pt]"])


def consolidate_cell_styles_l(styles_df: Any):
    pass


def create_table_start_l(data: GTData, width_dict: WidthDict) -> str:

    # Get list representation of stub layout
    stub_layout = data._stub._get_stub_layout(options=data._options)

    # Is the longtable environment being used?
    latex_use_longtable = data._options.latex_use_longtable.value

    # Extract only visible columns of `colwidth_df` based on stub_layout
    types = ["default"]

    if "rowname" in stub_layout:
        types.append("stub")

    if "group_label" in stub_layout:
        types.append("row_group")

    # Get indices of the types in `types` that are in the `type` key of `width_dict`
    width_dict_visible_idx = [i for i, v in enumerate(width_dict["type"]) if v in types]

    # Filter the `width_dict` dict entries based on the indices in `width_dict_visible_idx`
    width_dict_visible = {k: [width_dict[k][i] for i in width_dict_visible_idx] for k in width_dict}

    # Ensure that the `width_dict_visible` entries are sorted such that the
    # `"row_group"` entry is first (only if it's located in the stub), then `"stub"`,
    # and then everything else
    if "stub" in width_dict_visible["type"]:
        stub_idx = width_dict_visible["type"].index("stub")
        othr_idx = [i for i in range(len(width_dict_visible["type"])) if i != stub_idx]
        width_dict_visible["type"] = ["row_group", "stub"] + width_dict_visible["type"][othr_idx]

    if "row_group" in width_dict_visible["type"]:
        row_group_idx = width_dict_visible["type"].index("row_group")
        othr_idx = [i for i in range(len(width_dict_visible["type"])) if i != row_group_idx]
        width_dict_visible["type"] = ["row_group"] + width_dict_visible["type"][othr_idx]

    # Determine if there are any footnotes or source notes; if any,
    # add a `\setlength` command that will pull up the minipage environment
    # for the footnotes block

    source_notes = data._source_notes

    if len(source_notes) > 0:

        longtable_post_length = "\\setlength{\\LTpost}{0mm}\n"

    else:

        longtable_post_length = ""

    # Generate the column definitions for visible columns
    # these can either be simple `l`, `c`, `r` directive if a width isn't set
    # for a column, or, use `p{<width>}` statements with leading `>{...}`
    # specifiers that should have one of the following:
    # - `>{\raggedright\arraybackslash}` <- left alignment
    # - `>{\raggedleft\arraybackslash}` <- right alignment
    # - `>{\centering\arraybackslash}` <- center alignment
    # the `\arraybackslash` command is used to restore the behavior of the
    # `\\` command in the table (all of this uses the CTAN `array` package)
    if any(width_dict_visible["unspec"]) < 1:

        col_defs = []

        for i in range(len(width_dict_visible["type"])):

            if width_dict_visible["unspec"][i] == 1:

                col_defs_i = width_dict_visible["column_align"][i][0]

            else:

                alignments = {
                    "left": ">{\\raggedright\\arraybackslash}",
                    "right": ">{\\raggedleft\\arraybackslash}",
                    "center": ">{\\centering\\arraybackslash}",
                }

                align = alignments.get(
                    width_dict_visible["column_align"][i], ">{\\raggedright\\arraybackslash}"
                )

                col_defs_i = (
                    align
                    + "p{"
                    + create_singlecolumn_width_text_l(
                        pt=width_dict_visible["pt"][i], lw=width_dict_visible["lw"][i]
                    )
                    + "}"
                )

            col_defs.append(col_defs_i)

    else:

        col_defs = [align[0] for align in width_dict_visible["column_align"]]

    # Add borders to the right of any columns in the stub
    if len(stub_layout) > 0:

        for i in range(len(stub_layout)):
            col_defs[i] = col_defs[i] + "|"

    # If a table width is specified, add an extra column
    # space to fill in enough space to match the width
    extra_sep = ""

    table_width = data._options.table_width.value

    if table_width != "auto":
        extra_sep = "@{\\extracolsep{\\fill}}"

    # determine string for table width if using tabular* environment
    hdr_tabular = ""

    if not latex_use_longtable:

        # we need to use the extracolsep here for tabular* regardless of width
        extra_sep = "@{\\extracolsep{\\fill}}"

        if table_width.endswith("%"):

            tw = float(table_width.replace("%", ""))

            tw_frac = tw / 100

            hdr_tabular = f"\\begin{{tabular*}}{{{tw_frac}\\linewidth}}{{"

        elif table_width.endswith("px"):

            width_in_pt = convert_to_pt(table_width)
            hdr_tabular = f"\\begin{{tabular*}}{{{width_in_pt}pt}}{{"

        else:

            hdr_tabular = "\\begin{tabular*}{\\linewidth}{"

    # Generate setup statements for table including default left
    # alignments and vertical lines for any stub columns
    table_start = "".join(
        [
            longtable_post_length if latex_use_longtable else "",
            "\\begin{longtable}{" if latex_use_longtable else hdr_tabular,
            extra_sep,
            "".join(col_defs),
            "}",
        ]
    )

    return table_start


def create_caption_component_l(data: GTData) -> str:

    # TODO: implement all logic
    pass


def create_heading_component_l(data: GTData) -> str:

    title = data._heading.title
    subtitle = data._heading.subtitle

    # Is the longtable environment being used?
    latex_use_longtable = data._options.latex_use_longtable.value

    line_continuation = "\\\\"

    has_title = heading_has_title(title)

    # If there is no title, then return an empty string
    if not has_title:
        return ""

    title_row = f"{{\\large {title}}}"

    has_subtitle = heading_has_subtitle(subtitle)

    if has_subtitle:

        subtitle_row = f"{{\\small {subtitle}}}"

        header_component = f"""\\caption*{{
{title_row} \\\\
{subtitle_row}
}} {line_continuation if latex_use_longtable else ""}"""

    else:

        header_component = f"""\\caption*{{
{title_row}
}} {line_continuation if latex_use_longtable else ""}"""

    return header_component


def create_columns_component_l(data: GTData, width_dict: WidthDict) -> str:

    # Get list representation of stub layout
    stub_layout = data._stub._get_stub_layout(options=data._options)

    # Get the style information
    styles_info = data._styles

    # Determine the finalized number of spanner rows
    spanner_row_count = _get_spanners_matrix_height(data=data, omit_columns_row=True)

    # Get the column headings
    headings_vars = data._boxhead._get_default_columns()
    headings_labels = data._boxhead._get_default_column_labels()

    # TODO: implement all logic for styling cells in the column headings

    # If there is a stub then modify the `headings_vars` and `headings_labels`
    if len(stub_layout) > 0:

        stubh = data._stubhead

        styles_stubhead = consolidate_cell_styles_l(...)

        headings_vars = ["::stub"] + headings_vars

        # TODO: implement logic for obtaining a styled `stub_label`

        if len(stub_layout) > 1:

            # If stub_layout == 1, multicolumn is not needed and `stub_label` is already defined
            stub_dict = {k: v for k, v in width_dict.items() if v["type"] in ["stub", "row_group"]}

            # If there are any unspecified column widths, we need to use width_txt = "c"
            if any(stub_dict["unspec"]):

                width_txt = "c"

            else:

                width_txt = ">{\\centering\\arraybackslash}m{{{}}}".format(
                    create_singlecolumn_width_text_l(
                        pt=sum(stub_dict["pt"]) if isinstance(stub_dict["pt"], list) else 0,
                        lw=sum(stub_dict["lw"]) if isinstance(stub_dict["lw"], list) else 0,
                    )
                    or ""
                )

            stub_label = "\\multicolumn{{{}}}{{{}}}{{{}}}".format(
                len(stub_layout), width_txt, stub_label
            )

        headings_labels = [stub_label] + headings_labels

    table_col_headings = "".join(latex_heading_row(content=headings_labels))

    if spanner_row_count > 0:

        boxhead = data._boxhead

        table_col_spanners = []

        spanners, _ = spanners_print_matrix(
            spanners=data._spanners,
            boxhead=boxhead,
            include_hidden=False,
            ids=False,
            omit_columns_row=True,
        )

        spanner_ids, _ = spanners_print_matrix(
            spanners=data._spanners,
            boxhead=boxhead,
            include_hidden=False,
            ids=True,
            omit_columns_row=True,
        )

        # Prepend the stub layout to the spanners matrix if it exists
        if len(stub_layout) > 0:

            # TODO: implement logic for this
            pass

        for i in range(len(spanners)):

            spanners_i = spanners[i]
            spanner_ids_i = spanner_ids[i,]

            # TODO: implement logic for calculating the `begins` and `ends` lists
            begins = [1]
            ends = [2]

            cmidrule = "\\cmidrule(lr){{{}}}-{{{}}}".format(begins, ends)

            # TODO: implement logic for determining whether a spanner is a single spanner
            is_spanner_na = False

            is_spanner_single = spanners_rle["lengths"] == 1

            # TODO: implement logic for calculating this
            # firsts = utils::head(cumsum(c(1L, spanners_rle$lengths)), -1L)
            # lasts = cumsum(spanners_rle$lengths)
            firsts = [1, 2, 3]
            firsts = [4, 5, 6]

            span_widths = calculate_multicolumn_width_text_l(
                begins=firsts, ends=lasts, width_dict=width_dict
            )

            tex_widths = (
                "c" if span_widths == "" else f">{{\\centering\\arraybackslash}}m{{{span_widths}}}"
            )

            multicol = (
                ""
                if is_spanner_na
                else (
                    spanners_rle["labels"]
                    if is_spanner_single
                    else "\\multicolumn{{{}}}{{{}}}{{{}}}".format(
                        spanners_rle["lengths"], tex_widths, spanners_rle["labels"]
                    )
                )
            )

            # If there is a stub we need to tweak the spanners row with a blank
            # multicolumn statement that's the same width as that in the columns
            # row; this is to prevent the automatic vertical line that would otherwise
            # appear here
            if len(stub_layout) > 1:

                tex_stub_width = calculate_multicolumn_width_text_l(
                    begins=1, ends=2, width_dict=width_dict
                )

                if tex_stub_width == "":

                    mc_stub = "l"

                else:
                    mc_stub = ">{\\raggedright\\arraybackslash}m{{{}}}".format(tex_stub_width)

                multicol = [
                    "\\multicolumn{{{}}}{{{}}}{{}}".format(len(stub_layout), mc_stub),
                    *multicol[len(stub_layout) :],
                ]

        multicol = " & ".join(multicol) + " \\\\ \n"
        cmidrule = " ".join(cmidrule) + "\n"

        col_spanners_i = multicol + cmidrule

        table_col_spanners += [col_spanners_i]

    else:

        table_col_spanners = ""

    columns_component = "\\toprule\n" + "".join(table_col_spanners) + table_col_headings

    return columns_component


def create_body_component_l(data: GTData, width_dict: WidthDict) -> str:

    _str_orig_data = cast_frame_to_string(data._tbl_data)
    tbl_data = replace_null_frame(data._body.body, _str_orig_data)

    #
    # TODO: summary information is not yet implemented
    # summaries_present = _summary_exists(data=data)
    # list_of_summaries = _summary_get(data=data)
    #

    # TODO: implement grouping and stub logic

    # Get list representation of stub layout
    stub_layout = data._stub._get_stub_layout(options=data._options)

    # Get the default column vars
    column_vars = data._boxhead._get_default_columns()

    # Determine if there is a stub column in `stub_layout` and whether we
    # have a two-column stub (with the group label on the left side)
    has_stub_column = "rowname" in stub_layout
    has_two_col_stub = "group_label" in stub_layout

    # Get the total number of columns in the table (this includes columns in the stub)
    n_cols = data._boxhead._get_effective_number_of_columns(stub=data._stub, options=data._options)

    # Get the styles for the body cells
    styles_cells = [x for x in data._styles if _is_loc(x.locname, loc.LocBody)]

    current_group_id = str(0)

    body_rows = []

    # iterate over rows (ordered by groupings)
    prev_group_info = None

    ordered_index: list[tuple[int, GroupRowInfo]] = data._stub.group_indices_map()

    for i, group_info in ordered_index:

        body_cells: list[str] = []

        # Create a body row
        for colinfo in column_vars:
            cell_content: Any = _get_cell(tbl_data, i, colinfo.var)
            cell_str: str = str(cell_content)

            body_cells.append(cell_str)

        prev_group_info = group_info

        # When joining the body cells together, we need to ensure that each item is separated by
        # an ampersand and that the row is terminated with a double backslash
        body_cells = " & ".join(body_cells) + " \\\\"

        body_rows.append("".join(body_cells))

    # When joining all the body rows together, we need to ensure that each row is separated by
    # newline except for the last

    all_body_rows = "\n".join(body_rows)

    return all_body_rows


def create_footer_component_l(data: GTData) -> str:

    # Get all source notes as a list
    source_notes_list = data._source_notes

    if len(source_notes_list) == 0:
        return ""

    # Create a formatted source notes string
    source_notes = "\\\\\n".join(source_notes_list) + "\\\\"

    # Create the footer block
    footer_block = f"""\\begin{{minipage}}{{\\linewidth}}
{source_notes}
\\end{{minipage}}"""

    return footer_block


def create_table_end_l(data: GTData) -> str:

    latex_use_longtable = data._options.latex_use_longtable.value

    table_end = "\\bottomrule\n" + (
        "\\end{longtable}" if latex_use_longtable else "\\end{tabular*}"
    )

    return table_end


def derive_table_width_statement_l(data: GTData) -> str:

    # Get the table width value
    tbl_width = data._options.table_width.value

    use_longtable = data._options.latex_use_longtable.value

    # Initialize the statement variables LTleft and LTright
    sides = ["LTleft", "LTright"]

    # Bookends are not required if a table width is not specified or if using floating table
    if tbl_width == "auto" or not use_longtable:

        statement = ""

    elif tbl_width.endswith("%"):

        tw = float(tbl_width.strip("%"))

        side_width = (100 - tw) / 200
        side_width = f"{side_width:.6f}".rstrip("0").rstrip(".")

        statement = "\n".join([f"\\setlength\\{side}{{{side_width}\\linewidth}}" for side in sides])

    else:

        width_in_pt = convert_to_pt(tbl_width)

        halfwidth_in_pt = f"{width_in_pt / 2:.6f}".rstrip("0").rstrip(".")

        statement = "\n".join(
            f"\\setlength\\{side}{{\\dimexpr(0.5\\linewidth - {halfwidth_in_pt}pt)}}"
            for side in sides
        )

    return statement


def create_fontsize_statement_l(data: GTData) -> str:

    table_font_size = data._options.table_font_size.value

    fs_fmt = "\\fontsize{%3.1fpt}{%3.1fpt}\\selectfont\n"

    if table_font_size.endswith("%"):

        multiple = float(table_font_size.strip("%")) / 100
        fs_statement = fs_fmt % (multiple * 12, multiple * 12 * 1.2)

    elif table_font_size.endswith("pt"):

        size_in_pt = float(table_font_size[:-2])
        fs_statement = fs_fmt % (size_in_pt, size_in_pt * 1.2)

    elif css_length_has_supported_units(table_font_size):

        size_in_pt = convert_to_px(table_font_size) * 0.75
        fs_statement = fs_fmt % (size_in_pt, size_in_pt * 1.2)

    else:
        fs_statement = ""

    return fs_statement


def create_wrap_start_l(data: GTData) -> str:

    if check_quarto():
        tbl_pos = ""

    else:
        latex_tbl_pos_val = data._options.latex_tbl_pos.value
        tbl_pos = f"[{latex_tbl_pos_val}]"

    latex_use_longtable = data._options.latex_use_longtable.value

    if latex_use_longtable:
        return "\\begingroup"
    else:
        return f"\\begin{{table}}{tbl_pos}"


def create_wrap_end_l(data: GTData) -> str:

    latex_use_longtable = data._options.latex_use_longtable.value

    wrap_end = "\\endgroup" if latex_use_longtable else "\\end{table}"

    return wrap_end