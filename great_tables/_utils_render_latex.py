from __future__ import annotations

import re
import warnings
from itertools import chain
from typing import TYPE_CHECKING

from ._spanners import spanners_print_matrix
from ._tbl_data import _get_cell, cast_frame_to_string, replace_null_frame
from ._text import _process_text
from ._utils import heading_has_subtitle, heading_has_title, seq_groups
from ._utils_render_html import _get_spanners_matrix_height
from .quarto import is_quarto_render

if TYPE_CHECKING:
    from ._gt_data import GroupRowInfo, GTData


LENGTH_TRANSLATIONS_TO_PX = {
    "px": 1.0,
    "pt": 4 / 3,
    "in": 96.0,
    "cm": 37.7952755906,
    "emu": 1 / 9525,
    "em": 16.0,
}


def _not_implemented(msg: str) -> None:
    warnings.warn(msg)


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

    return units in LENGTH_TRANSLATIONS_TO_PX


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


def latex_heading_row(content: list[str]) -> str:
    return "".join([" & ".join(content) + " \\\\ \n", "\\midrule\\addlinespace[2.5pt]"])


def create_table_start_l(data: GTData, use_longtable: bool) -> str:
    """
    Create the table start component for LaTeX output.

    This function generates the LaTeX code that signifies the start of the table. The output is
    different depending on whether the table uses the `longtable` environment or not.

    Parameters
    ----------
    data : GTData
        The GTData object that contains all the information about the table.

    Returns
    -------
    str
        The LaTeX code that signifies the start of the table.
    """

    # Determine if there are any source notes; if any, add a `\setlength` command that will pull up
    # the minipage environment for the footer block

    # Get all source notes as a list
    source_notes = data._source_notes

    if len(source_notes) > 0:
        longtable_post_length = "\\setlength{\\LTpost}{0mm}\n"

    else:
        longtable_post_length = ""

    # Get the column alignments for the visible columns as a list of `col_defs`
    col_defs = [align[0] for align in data._boxhead._get_default_alignments()]

    # Check if stub is present and determine layout
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    stub_layout = data._stub._get_stub_layout(
        has_summary_rows=has_summary_rows, options=data._options
    )

    # Determine if there's a stub column (rowname or group_label)
    has_stub = len(stub_layout) > 0

    # Build stub column definitions (left-aligned with separator)
    stub_col_defs = ""
    if has_stub:
        # Add 'l' for each stub column, with a '|' separator after the last one
        stub_col_defs = "l" * len(stub_layout) + "|"

    # If a table width is specified, add an extra column
    # space to fill in enough space to match the width
    extra_sep = ""

    # Obtain the table width value from the `table_width` options value
    table_width = data._options.table_width.value

    if table_width != "auto":
        extra_sep = "@{\\extracolsep{\\fill}}"

    # determine string for table width if using tabular* environment
    hdr_tabular = ""

    if not use_longtable:
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
            longtable_post_length if use_longtable else "",
            "\\begin{longtable}{" if use_longtable else hdr_tabular,
            extra_sep,
            stub_col_defs,
            "".join(col_defs),
            "}",
        ]
    )

    return table_start


def create_heading_component_l(data: GTData, use_longtable: bool) -> str:
    """
    Create the heading component for LaTeX output.

    This function generates the LaTeX code for the heading component of a table which involves the
    title and the optional subtitle. There is variation in the output based on whether the table
    uses the `longtable` environment or not.

    Parameters
    ----------
    data : GTData
        The GTData object that contains all the information about the table.

    Returns
    -------
    str
        The LaTeX code for the heading component of the table.
    """

    title = data._heading.title
    subtitle = data._heading.subtitle

    line_continuation = "\\\\"

    has_title = heading_has_title(title)

    # If there is no title, then return an empty string
    if not has_title:
        return ""

    title_str = _process_text(title, context="latex")

    title_row = f"{{\\large {title_str}}}"

    has_subtitle = heading_has_subtitle(subtitle)

    if has_subtitle:
        subtitle_str = _process_text(subtitle, context="latex")

        subtitle_row = f"{{\\small {subtitle_str}}}"

        header_component = f"""\\caption*{{
{title_row} \\\\
{subtitle_row}
}} {line_continuation if use_longtable else ""}"""

    else:
        header_component = f"""\\caption*{{
{title_row}
}} {line_continuation if use_longtable else ""}"""

    return header_component


def create_columns_component_l(data: GTData) -> str:
    """
    Create the columns component for LaTeX output.

    This function generates the LaTeX code for the columns component of a table which involves the
    column headings and the spanners.

    Parameters
    ----------
    data : GTData
        The GTData object that contains all the information about the table.

    Returns
    -------
    str
        The LaTeX code for the columns component of the table.
    """

    # Determine the finalized number of spanner rows
    spanner_row_count = _get_spanners_matrix_height(data=data, omit_columns_row=True)

    # Check if stub is present and determine layout
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    stub_layout = data._stub._get_stub_layout(
        has_summary_rows=has_summary_rows, options=data._options
    )

    # Determine if there's a stub column (rowname or group_label)
    has_stub = len(stub_layout) > 0

    # Create stub header cells (empty space for each stub column)
    stub_headers = []
    if has_stub:
        stub_headers = [" "] * len(stub_layout)

    # Get the column headings
    headings_labels = data._boxhead._get_default_column_labels()

    # Ensure that the heading labels are processed for LaTeX
    headings_labels = [_process_text(x, context="latex") for x in headings_labels]

    # Prepend stub headers to column headings
    all_headings = stub_headers + headings_labels

    table_col_headings = "".join(latex_heading_row(content=all_headings))

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

        # TODO: ensure that spanner IDs are not included in the output (spanner
        # labels should be used instead)

        # spanner_ids, spanner_col_names = spanners_print_matrix(
        #     spanners=data._spanners,
        #     boxhead=boxhead,
        #     include_hidden=False,
        #     ids=True,
        #     omit_columns_row=True,
        # )
        for spanners_row in spanners:
            spanners_row = {k: "" if v is None else v for k, v in spanners_row.items()}

            spanner_ids_index = spanners_row.values()
            spanners_rle = seq_groups(seq=spanner_ids_index)

            group_spans = [[x[1]] + [0] * (x[1] - 1) for x in spanners_rle]
            colspans = chain.from_iterable(group_spans)
            level_i_spanners = (
                _process_text(span_label, context="latex") if span_label else None
                for colspan, span_label in zip(colspans, spanners_row.values())
                if colspan > 0
            )

            spanner_labs = []
            spanner_lines = []
            span_accumulator = 0

            # Add empty cells for stub columns in spanner row
            if has_stub:
                spanner_labs.extend([" "] * len(stub_layout))
                span_accumulator = len(stub_layout)

            for j, level_i_spanner_j in enumerate(level_i_spanners):
                if level_i_spanner_j is None:
                    # Get the number of columns to span nothing
                    span = group_spans[j][0]
                    spanner_labs.append("" * span)

                elif level_i_spanner_j is not None:
                    # Get the number of columns to span the spanner
                    span = group_spans[j][0]

                    # TODO: Get alignment for spanner, for now it's center (`c`)

                    # Get multicolumn statement for spanner
                    multicolumn_stmt = f"\\multicolumn{{{span}}}{{c}}{{{level_i_spanner_j}}}"

                    spanner_labs.append(multicolumn_stmt)

                    # Get cmidrule statement for spanner, it uses 1-based indexing
                    # and the span is the number of columns to span; we use the `span_accumulator`
                    # across iterations to adjust the starting index (j) to adjust for previous
                    # multicolumn spanning values

                    begin = j + span_accumulator + 1
                    end = j + span_accumulator + span

                    cmidrule = f"\\cmidrule(lr){{{begin}-{end}}}"

                    span_accumulator += span - 1

                    spanner_lines.append(cmidrule)

            spanner_labs_row = " & ".join(spanner_labs) + " \\\\ \n"
            spanner_lines_row = " ".join(spanner_lines) + "\n"

            col_spanners_i = spanner_labs_row + spanner_lines_row

            table_col_spanners.append(col_spanners_i)

        table_col_spanners = "".join(table_col_spanners)

    else:
        table_col_spanners = ""

    columns_component = "\\toprule\n" + table_col_spanners + table_col_headings

    return columns_component


def create_body_component_l(data: GTData) -> str:
    """
    Create the body component for LaTeX output.

    This function generates the LaTeX code for the body component of a table which involves the
    data cells, the row groups, and the stub.

    Parameters
    ----------
    data : GTData
        The GTData object that contains all the information about the table.

    Returns
    -------
    str
        The LaTeX code for the body component of the table.
    """

    _str_orig_data = cast_frame_to_string(data._tbl_data)
    tbl_data = replace_null_frame(data._body.body, _str_orig_data)

    # Get the default column vars
    column_vars = data._boxhead._get_default_columns()

    # Check if stub is present and determine layout
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    stub_layout = data._stub._get_stub_layout(
        has_summary_rows=has_summary_rows, options=data._options
    )

    # Determine what stub components are present
    has_row_stub_column = "rowname" in stub_layout
    has_group_stub_column = "group_label" in stub_layout
    has_groups = len(data._stub.group_ids) > 0

    # Get the stub column info if it exists
    row_stub_var = data._boxhead._get_stub_column()

    body_rows = []

    ordered_index: list[tuple[int, GroupRowInfo | None]] = data._stub.group_indices_map()

    prev_group_info = None
    first_group_added = False

    # Calculate total number of columns for multicolumn spanning in group headers
    n_cols = len(column_vars) + len(stub_layout)

    for i, group_info in ordered_index:
        # Handle row group labels
        if has_groups and group_info is not None:
            # Only create group row if this is first row of the group
            if group_info is not prev_group_info:
                group_label = group_info.defaulted_label()

                # Process the group label for LaTeX
                group_label = _process_text(group_label, context="latex")

                # When group is shown as a column, we don't add a separate row
                # Instead, it will be added as a cell in each data row
                if not has_group_stub_column:
                    # Add midrule before group heading (except for first group, which already has
                    # one from column headers) then the group heading, then midrule after
                    if first_group_added:
                        group_row = f"\\midrule\\addlinespace[2.5pt]\n\\multicolumn{{{n_cols}}}{{l}}{{{group_label}}} \\\\[2.5pt] \n\\midrule\\addlinespace[2.5pt]"
                    else:
                        group_row = f"\\multicolumn{{{n_cols}}}{{l}}{{{group_label}}} \\\\[2.5pt] \n\\midrule\\addlinespace[2.5pt]"
                        first_group_added = True
                    body_rows.append(group_row)

        # Create data row cells
        body_cells: list[str] = []

        # Add stub cells first (group_label column, then rowname column)
        if has_group_stub_column and group_info is not None:
            # Only show group label in first row of group
            if group_info is prev_group_info:
                # Use an empty cell for continuation rows in same group
                body_cells.append("")
            else:
                # Get the group label from the group info
                group_label = group_info.defaulted_label()
                group_label = _process_text(group_label, context="latex")

                body_cells.append(group_label)

        if has_row_stub_column:
            # Get the row name from the stub
            rowname = _get_cell(tbl_data, i, row_stub_var.var)
            rowname_str = str(rowname)

            body_cells.append(rowname_str)

        # Add data cells
        for colinfo in column_vars:
            cell_content = _get_cell(tbl_data, i, colinfo.var)
            cell_str: str = str(cell_content)

            body_cells.append(cell_str)

        # Join cells with ampersand and terminate with a double backslash
        body_row_str = " & ".join(body_cells) + " \\\\"

        body_rows.append(body_row_str)

        prev_group_info = group_info

    # Join all body rows with newlines
    all_body_rows = "\n".join(body_rows)

    return all_body_rows


def create_footer_component_l(data: GTData) -> str:
    """
    Create the footer component for LaTeX output.

    This function generates the LaTeX code for the footer component of a table which involves the
    source notes.

    Parameters
    ----------
    data : GTData
        The GTData object that contains all the information about the table.

    Returns
    -------
    str
        The LaTeX code for the footer component of the table.
    """

    # Get all source notes as a list
    source_notes = data._source_notes

    if len(source_notes) == 0:
        return ""

    # Ensure that the source notes are processed for LaTeX
    source_notes = [_process_text(x, context="latex") for x in source_notes]

    # Create a formatted source notes string
    source_notes = "\\\\\n".join(source_notes) + "\\\\"

    # Create the footer block
    footer_block = f"""\\begin{{minipage}}{{\\linewidth}}
{source_notes}
\\end{{minipage}}"""

    return footer_block


def create_table_end_l(use_longtable: bool) -> str:
    """
    Create the table end component for LaTeX output.

    This function generates the LaTeX code that signifies the end of the table. The output is
    different depending on whether the table uses the `longtable` environment or not.

    Parameters
    ----------
    data : GTData
        The GTData object that contains all the information about the table.

    Returns
    -------
    str
        The LaTeX code that signifies the end of the table.
    """

    table_end = "\\bottomrule\n" + ("\\end{longtable}" if use_longtable else "\\end{tabular*}")

    return table_end


def derive_table_width_statement_l(data: GTData, use_longtable: bool) -> str:
    # Get the table width value
    tbl_width = data._options.table_width.value

    # Initialize the statement variables LTleft and LTright
    sides = ("LTleft", "LTright")

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


def create_wrap_start_l(use_longtable: bool, tbl_pos: str | None) -> str:
    if is_quarto_render():
        tbl_pos = ""

    else:
        if tbl_pos is None:
            tbl_pos = "!t"

        tbl_pos = f"[{tbl_pos}]"

    return "\\begingroup" if use_longtable else f"\\begin{{table}}{tbl_pos}"


def create_wrap_end_l(use_longtable: bool) -> str:
    wrap_end = "\\endgroup" if use_longtable else "\\end{table}"

    return wrap_end


def _render_as_latex(data: GTData, use_longtable: bool = False, tbl_pos: str | None = None) -> str:
    # Check for styles (not yet supported so warn user)
    if data._styles:
        _not_implemented("Styles are not yet supported in LaTeX output.")

    # Create a LaTeX fragment for the start of the table
    table_start = create_table_start_l(data=data, use_longtable=use_longtable)

    # Create the heading component
    heading_component = create_heading_component_l(data=data, use_longtable=use_longtable)

    # Create the columns component
    columns_component = create_columns_component_l(data=data)

    # Create the body component
    body_component = create_body_component_l(data=data)

    # Create the footnotes component
    footer_component = create_footer_component_l(data=data)

    # Create a LaTeX fragment for the ending tabular statement
    table_end = create_table_end_l(use_longtable=use_longtable)

    # Create a LaTeX fragment for the table width statement
    table_width_statement = derive_table_width_statement_l(data=data, use_longtable=use_longtable)

    # Allow user to set a font-size
    fontsize_statement = create_fontsize_statement_l(data=data)

    # Create wrapping environment
    wrap_start_statement = create_wrap_start_l(use_longtable=use_longtable, tbl_pos=tbl_pos)
    wrap_end_statement = create_wrap_end_l(use_longtable=use_longtable)

    # Compose the LaTeX table
    if use_longtable:
        finalized_table = f"""{wrap_start_statement}
{table_width_statement}
{fontsize_statement}
{table_start}
{heading_component}
{columns_component}
{body_component}
{table_end}
{footer_component}
{wrap_end_statement}
"""

    else:
        finalized_table = f"""{wrap_start_statement}
{heading_component}
{table_width_statement}
{fontsize_statement}
{table_start}
{columns_component}
{body_component}
{table_end}
{footer_component}
{wrap_end_statement}
"""

    return finalized_table
