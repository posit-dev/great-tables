from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING, Any, cast

from htmltools import HTML, TagList, css, tags

from . import _locations as loc
from ._gt_data import (
    ColInfo,
    ColInfoTypeEnum,
    GroupRowInfo,
    GTData,
    StyleInfo,
    Styles,
    SummaryRowInfo,
)
from ._spanners import spanners_print_matrix
from ._tbl_data import _get_cell, cast_frame_to_string, replace_null_frame
from ._text import BaseText, _process_text, _process_text_id
from ._utils import heading_has_subtitle, heading_has_title, seq_groups

if TYPE_CHECKING:
    from ._tbl_data import TblData


def _is_loc(loc: str | loc.Loc, cls: type[loc.Loc]):
    if isinstance(loc, str):
        return loc == cls.groups

    return isinstance(loc, cls)


def _flatten_styles(styles: Styles, wrap: bool = False) -> str | None:
    # flatten all StyleInfo.styles lists
    style_entries = list(chain.from_iterable((x.styles for x in styles)))
    rendered_styles = [el._to_html_style() for el in style_entries]

    # TODO dedupe rendered styles in sequence

    if wrap:
        if rendered_styles:
            # return style html attribute
            return f' style="{" ".join(rendered_styles)}"'
        # if no rendered styles, just return a blank
        return ""
    if rendered_styles:
        # return space-separated list of rendered styles
        return " ".join(rendered_styles)
    # if not wrapping the styles for html element,
    # return None so htmltools omits a style attribute
    return None


def _create_element_id(table_id: str | None, element_id: str | BaseText | None) -> str:
    # Given a table ID, element IDs are prepended by it to ensure the resulting HTML
    # has unique IDs.
    new_table_id = table_id or ""
    processed_id = _process_text_id(element_id)
    return f"{new_table_id}-{processed_id}" if new_table_id and processed_id else processed_id


def create_heading_component_h(data: GTData) -> str:
    title = data._heading.title
    subtitle = data._heading.subtitle

    has_title = heading_has_title(title)
    has_subtitle = heading_has_subtitle(subtitle)

    # If there is no title or heading component, then return an empty string
    if not has_title and not has_subtitle:
        return ""

    # Raise an error if there is a subtitle but no title
    if not has_title and has_subtitle:
        raise ValueError("A subtitle was provided without a title.")

    title = _process_text(title)
    subtitle = _process_text(subtitle)

    # Filter list of StyleInfo for the various header components
    styles_header = [x for x in data._styles if _is_loc(x.locname, loc.LocHeader)]
    styles_title = [x for x in data._styles if _is_loc(x.locname, loc.LocTitle)]
    styles_subtitle = [x for x in data._styles if _is_loc(x.locname, loc.LocSubTitle)]
    title_style = _flatten_styles(styles_header + styles_title, wrap=True)
    subtitle_style = _flatten_styles(styles_header + styles_subtitle, wrap=True)

    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)

    # Get the effective number of columns, which is number of columns
    # that will finally be rendered accounting for the stub layout
    n_cols_total = data._boxhead._get_effective_number_of_columns(
        stub=data._stub,
        has_summary_rows=has_summary_rows,
        options=data._options,
    )

    if has_subtitle:
        heading = f"""
  <tr class="gt_heading">
    <td colspan="{n_cols_total}" class="gt_heading gt_title gt_font_normal"{title_style}>{title}</td>
  </tr>
  <tr class="gt_heading">
    <td colspan="{n_cols_total}" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"{subtitle_style}>{subtitle}</td>
  </tr>"""
    else:
        heading = f"""
  <tr class="gt_heading">
    <td colspan="{n_cols_total}" class="gt_heading gt_title gt_font_normal"{title_style}>{title}</td>
  </tr>"""

    return heading


def create_columns_component_h(data: GTData) -> str:
    """
    Returns the HTML text fragment for the column/spanner labels.
    """

    # Should the column labels be hidden?
    column_labels_hidden: bool = data._options.column_labels_hidden.value

    if column_labels_hidden:
        return ""

    # Get necessary data objects for composing the column labels and spanners
    stubh = data._stubhead
    boxhead = data._boxhead

    # TODO: The body component of the table is only needed for determining RTL alignment
    # is needed in the corresponding column labels
    # body = data._body

    # Get vector representation of stub layout
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    stub_layout = data._stub._get_stub_layout(
        has_summary_rows=has_summary_rows, options=data._options
    )

    # Determine the finalized number of spanner rows
    spanner_row_count = _get_spanners_matrix_height(data=data, omit_columns_row=True)

    # TODO: Modify alignments for RTL support, skip this for now
    # Detect any RTL script characters within the visible columns;
    # this creates a vector the same length as `col_alignment`
    # rtl_detect = [
    #     any(char in rtl_modern_unicode_charset() for char in str(body[x])) for x in range(len(body))
    # ]
    #
    # For any columns containing characters from RTL scripts; we
    # will transform a 'left' alignment to a 'right' alignment
    # for i in range(len(rtl_detect)):
    #     if rtl_detect[i] and col_alignment[i] != "center":
    #         col_alignment[i] = "right"

    # Get the column headings
    headings_info = boxhead._get_default_columns()

    # Filter list of StyleInfo for the various stubhead and column labels components
    styles_stubhead = [x for x in data._styles if _is_loc(x.locname, loc.LocStubhead)]
    styles_column_labels = [x for x in data._styles if _is_loc(x.locname, loc.LocColumnHeader)]
    styles_spanner_label = [x for x in data._styles if _is_loc(x.locname, loc.LocSpannerLabels)]
    styles_column_label = [x for x in data._styles if _is_loc(x.locname, loc.LocColumnLabels)]

    # If columns are present in the stub, then replace with a set stubhead label or nothing
    if stub_layout and stubh is not None:
        stub_label = stubh
        stub_var = "::stub"
    else:
        stub_label = ""
        stub_var = None

    # Set a default alignment for the stubhead label
    stubhead_label_alignment = "left"

    # Initialize the column headings list
    table_col_headings = []

    # Extract the table ID to ensure subsequent IDs are unique
    table_id = data._options.table_id.value

    # If there are no spanners, then we have to create the cells for the stubhead label
    # (if present) and for the column headings
    if spanner_row_count == 0:
        # Create the cell for the stubhead label
        if stub_layout:
            table_col_headings.append(
                tags.th(
                    HTML(_process_text(stub_label)),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{stubhead_label_alignment}",
                    rowspan="1",
                    colspan=len(stub_layout),
                    style=_flatten_styles(styles_stubhead),
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    id=_create_element_id(table_id, stub_label),
                )
            )

        # Create the headings in the case where there are no spanners at all -------------------------
        for info in headings_info:
            # Filter by column label / id, join with overall column labels style
            styles_i = [x for x in styles_column_label if x.colname == info.var]

            table_col_headings.append(
                tags.th(
                    HTML(_process_text(info.column_label)),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{info.defaulted_align}",
                    rowspan=1,
                    colspan=1,
                    style=_flatten_styles(styles_column_labels + styles_i),
                    scope="col",
                    id=_create_element_id(table_id, info.var),
                )
            )

        # Join the <th> cells into a string and begin each with a newline
        # th_cells = "\n" + "\n".join(["  " + str(tag) for tag in table_col_headings]) + "\n"

        table_col_headings = tags.tr(*table_col_headings, class_="gt_col_headings")

    #
    # Create the spanners and column labels in the case where there *are* spanners -------------
    #

    if spanner_row_count >= 1:
        spanner_ids, spanner_col_names = spanners_print_matrix(
            spanners=data._spanners, boxhead=boxhead, include_hidden=False, ids=False
        )

        # Last is column labels
        # So take second to last
        level_1_index = -2

        # A list of <th> elements that will go in the first level; this
        # includes spanner labels and column labels for solo columns (don't
        # have spanner labels above them)
        level_1_spanners = []

        # A list of <th> elements that will go in the second row. This is
        # all column labels that DO have spanners above them.
        spanned_column_labels = []

        # Create the cell for the stubhead label
        if stub_layout:
            level_1_spanners.append(
                tags.th(
                    HTML(_process_text(stub_label)),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{stubhead_label_alignment}",
                    rowspan=2,
                    colspan=len(stub_layout),
                    style=_flatten_styles(styles_stubhead),
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    id=_create_element_id(table_id, stub_label),
                )
            )

        # NOTE: Run-length encoding treats missing values as distinct from each other; in other
        # words, each missing value starts a new run of length 1

        spanner_ids_level_1 = spanner_ids[level_1_index]
        spanner_ids_level_1_index = list(spanner_ids_level_1.values())
        spanners_rle = seq_groups(seq=spanner_ids_level_1_index)

        # `colspans` matches `spanners` in length; each element is the number of columns that the
        # <th> at that position should span; if 0, then skip the <th> at that position
        group_spans = ([x[1]] + [0] * (x[1] - 1) for x in spanners_rle)

        colspans = list(chain.from_iterable(group_spans))

        for ii, (span_key, h_info) in enumerate(zip(spanner_col_names, headings_info)):
            if spanner_ids_level_1[span_key] is None:
                # Filter by column label / id, join with overall column labels style
                styles_i = [x for x in styles_column_label if x.colname == h_info.var]

                # Get the alignment values for the first set of column labels
                first_set_alignment = h_info.defaulted_align

                # Creation of <th> tags for column labels with no spanners above them
                level_1_spanners.append(
                    tags.th(
                        HTML(_process_text(h_info.column_label)),
                        class_=f"gt_col_heading gt_columns_bottom_border gt_{first_set_alignment}",
                        rowspan=2,
                        colspan=1,
                        style=_flatten_styles(styles_column_labels + styles_i),
                        scope="col",
                        id=_create_element_id(table_id, h_info.var),
                    )
                )

            elif spanner_ids_level_1[span_key] is not None:
                # If colspans[i] == 0, it means that a previous cell's
                # `colspan` will cover us
                if colspans[ii] > 0:
                    # Filter by spanner label / id, join with overall column labels style
                    styles_i = [
                        x
                        for x in styles_spanner_label
                        if spanner_ids_level_1_index[ii]
                        and spanner_ids_level_1_index[ii] in x.grpname
                    ]

                    level_1_spanners.append(
                        tags.th(
                            tags.span(
                                HTML(_process_text(spanner_ids_level_1_index[ii])),
                                class_="gt_column_spanner",
                            ),
                            class_="gt_center gt_columns_top_border gt_column_spanner_outer",
                            rowspan=1,
                            colspan=colspans[ii],
                            style=_flatten_styles(styles_column_labels + styles_i),
                            scope="colgroup" if colspans[ii] > 1 else "col",
                            id=_create_element_id(table_id, spanner_ids_level_1_index[ii]),
                        )
                    )

        remaining_headings = [k for k, v in spanner_ids[level_1_index].items() if v is not None]
        remaining_headings_labels = (
            entry.column_label for entry in boxhead if entry.var in remaining_headings
        )
        # col_alignment = [
        #     entry.defaulted_align for entry in boxhead if entry.var in remaining_headings
        # ]

        if remaining_headings:
            spanned_column_labels = []

            remaining_heading_ids = (
                entry.var for entry in boxhead if entry.var in remaining_headings
            )

            for remaining_heading, remaining_headings_label, element_id in zip(
                remaining_headings, remaining_headings_labels, remaining_heading_ids
            ):
                # Filter by column label / id, join with overall column labels style
                # TODO check this filter logic
                styles_i = [x for x in styles_column_label if x.colname == remaining_heading]

                remaining_alignment = boxhead._get_boxhead_get_alignment_by_var(
                    var=remaining_heading
                )

                spanned_column_labels.append(
                    tags.th(
                        HTML(_process_text(remaining_headings_label)),
                        class_=f"gt_col_heading gt_columns_bottom_border gt_{remaining_alignment}",
                        rowspan=1,
                        colspan=1,
                        style=_flatten_styles(styles_column_labels + styles_i),
                        scope="col",
                        id=_create_element_id(table_id, element_id),
                    )
                )

            table_col_headings = TagList(
                tags.tr(level_1_spanners, class_="gt_col_headings gt_spanner_row"),
                tags.tr(spanned_column_labels, class_="gt_col_headings"),
            )

        else:
            # Create the `table_col_headings` HTML component
            table_col_headings = tags.tr(level_1_spanners, class_="gt_col_headings gt_spanner_row")

    if _get_spanners_matrix_height(data=data) > 2:
        # Spanners are listed top to bottom, so we need to work bottom to top
        # We can skip the last (column labels) and second to last (first spanner)
        higher_spanner_rows = TagList()

        for spanners_row in spanner_ids[:-2]:
            spanners_row = {k: "" if v is None else v for k, v in spanners_row.items()}

            spanner_ids_index = spanners_row.values()
            spanners_rle = seq_groups(seq=spanner_ids_index)
            group_spans = ([x[1]] + [0] * (x[1] - 1) for x in spanners_rle)
            colspans = list(chain.from_iterable(group_spans))
            level_i_spanners = []

            for colspan, span_label in zip(colspans, spanners_row.values()):
                if colspan > 0:
                    # Filter by spanner label / id, join with overall column labels style
                    styles_i = [
                        x for x in styles_spanner_label if span_label and span_label in x.grpname
                    ]

                    if span_label:
                        span = tags.span(
                            HTML(_process_text(span_label)),
                            class_="gt_column_spanner",
                        )
                    else:
                        span = tags.span(HTML("&nbsp;"))

                    level_i_spanners.append(
                        tags.th(
                            span,
                            class_="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer",
                            rowspan=1,
                            colspan=colspan,
                            style=_flatten_styles(styles_column_labels + styles_i),
                            scope="colgroup" if colspan > 1 else "col",
                        )
                    )

            if stub_layout:
                level_i_spanners.insert(
                    0,
                    tags.th(
                        tags.span(HTML("&nbsp")),
                        class_=f"gt_col_heading gt_columns_bottom_border gt_{stubhead_label_alignment}",
                        rowspan=1,
                        colspan=len(stub_layout),
                        scope="colgroup" if len(stub_layout) > 1 else "col",
                        # TODO check if ok to just use base styling?
                        style=_flatten_styles(styles_column_labels),
                    ),
                )

            higher_spanner_rows = TagList(
                higher_spanner_rows,
                TagList(
                    tags.tr(
                        level_i_spanners,
                        class_="gt_col_headings gt_spanner_row",
                        # TODO check if ok to just use base styling?
                        style=_flatten_styles(styles_column_labels),
                    )
                ),
            )

        table_col_headings = TagList(
            higher_spanner_rows,
            table_col_headings,
        )
    return table_col_headings


def create_body_component_h(data: GTData) -> str:
    # for now, just coerce everything in the original data to a string
    # so we can fill in the body data with it
    _str_orig_data = cast_frame_to_string(data._tbl_data)
    tbl_data = replace_null_frame(data._body.body, _str_orig_data)

    # Filter list of StyleInfo to only those that apply to the stub
    styles_row_group_label = [x for x in data._styles if _is_loc(x.locname, loc.LocRowGroups)]
    styles_row_label = [x for x in data._styles if _is_loc(x.locname, loc.LocStub)]
    # styles_summary_label = [x for x in data._styles if _is_loc(x.locname, loc.LocSummaryStub)]
    styles_grand_summary_label = [
        x for x in data._styles if _is_loc(x.locname, loc.LocGrandSummaryStub)
    ]

    # Filter list of StyleInfo to only those that apply to the body
    styles_cells = [x for x in data._styles if _is_loc(x.locname, loc.LocBody)]
    # styles_body = [x for x in data._styles if _is_loc(x.locname, loc.LocBody2)]
    # styles_summary = [x for x in data._styles if _is_loc(x.locname, loc.LocSummary)]
    styles_grand_summary = [x for x in data._styles if _is_loc(x.locname, loc.LocGrandSummary)]

    # Get the default column vars
    column_vars = data._boxhead._get_default_columns()

    row_stub_var = data._boxhead._get_stub_column()

    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    stub_layout = data._stub._get_stub_layout(
        has_summary_rows=has_summary_rows, options=data._options
    )

    has_row_stub_column = "rowname" in stub_layout
    has_group_stub_column = "group_label" in stub_layout
    has_groups = data._stub.group_ids is not None and len(data._stub.group_ids) > 0

    # If there is a stub, then prepend that to the `column_vars` list
    if has_row_stub_column:
        # There is already a column assigned to the rownames
        if row_stub_var:
            column_vars = [row_stub_var] + column_vars
        # Else we have summary rows but no stub yet
        else:
            # TODO: this naming is not ideal
            summary_row_stub_var = ColInfo(
                "__do_not_use__", ColInfoTypeEnum.summary_placeholder, column_align="left"
            )
            column_vars = [summary_row_stub_var] + column_vars

    # Is the stub to be striped?
    table_stub_striped = data._options.row_striping_include_stub.value

    # Are the rows in the table body to be striped?
    table_body_striped = data._options.row_striping_include_table_body.value

    body_rows: list[str] = []

    # Add grand summary rows at top
    top_g_summary_rows = data._summary_rows_grand.get_summary_rows(side="top")
    for i, summary_row in enumerate(top_g_summary_rows):
        row_html = _create_row_component_h(
            column_vars=column_vars,
            row_stub_var=row_stub_var,  # Should probably include group stub?
            has_row_stub_column=has_row_stub_column,  # Should probably include group stub?
            has_group_stub_column=has_group_stub_column,  # Add this parameter
            apply_stub_striping=False,  # No striping for summary rows
            apply_body_striping=False,  # No striping for summary rows
            styles_cells=styles_grand_summary,
            styles_labels=styles_grand_summary_label,
            row_index=i,
            summary_row=summary_row,
            css_class="gt_last_grand_summary_row_top" if i == len(top_g_summary_rows) - 1 else None,
        )
        body_rows.append(row_html)

    # iterate over rows (ordered by groupings)
    prev_group_info = None

    ordered_index: list[tuple[int, GroupRowInfo]] = data._stub.group_indices_map()

    for j, (i, group_info) in enumerate(ordered_index):
        # For table striping we want to add a striping CSS class to the even-numbered
        # rows in the rendered table; to target these rows, determine if `i` in the current
        # row render is an odd number

        odd_j_row = j % 2 == 1

        leading_cell = None

        # Create table row or label in the stub specifically for group (if applicable)
        if has_groups:
            # Only create if this is the first row of data within the group
            if group_info is not prev_group_info:
                group_label = group_info.defaulted_label()

                _styles = [
                    style
                    for style in styles_row_group_label
                    if group_info.group_id in style.grpname
                ]
                group_styles = _flatten_styles(_styles, wrap=True)

                # Add group label that spans multiple columns when row_group_as_column is true
                if has_group_stub_column:
                    rowspan_value = len(group_info.indices)

                    leading_cell = f"""  <th{group_styles} class="gt_row gt_left gt_stub_row_group"
    rowspan="{rowspan_value}">{group_label}</th>"""

                # Append a table row for the group heading
                else:
                    colspan_value = data._boxhead._get_effective_number_of_columns(
                        stub=data._stub, has_summary_rows=has_summary_rows, options=data._options
                    )

                    group_class = (
                        "gt_empty_group_heading" if group_label == "" else "gt_group_heading_row"
                    )

                    group_row = f"""  <tr class="{group_class}">
    <th class="gt_group_heading" colspan="{colspan_value}"{group_styles}>{group_label}</th>
  </tr>"""

                    body_rows.append(group_row)

        # Create data row
        row_html = _create_row_component_h(
            column_vars=column_vars,
            row_stub_var=row_stub_var,
            has_row_stub_column=has_row_stub_column,
            has_group_stub_column=has_group_stub_column,
            leading_cell=leading_cell,
            apply_stub_striping=table_stub_striped and odd_j_row,
            apply_body_striping=table_body_striped and odd_j_row,
            styles_cells=styles_cells,
            styles_labels=styles_row_label,
            row_index=i,
            tbl_data=tbl_data,
        )
        body_rows.append(row_html)

        prev_group_info = group_info

        ## after the last row in the group, we need to append the summary rows for the group
        ## if this table has summary rows

    # Add grand summary rows at bottom
    bottom_g_summary_rows = data._summary_rows_grand.get_summary_rows(side="bottom")
    for i, summary_row in enumerate(bottom_g_summary_rows):
        row_html = _create_row_component_h(
            column_vars=column_vars,
            row_stub_var=row_stub_var,
            has_row_stub_column=has_row_stub_column,
            has_group_stub_column=has_group_stub_column,  # Add this parameter
            apply_stub_striping=False,
            apply_body_striping=False,
            styles_cells=styles_grand_summary,
            styles_labels=styles_grand_summary_label,
            row_index=i + len(top_g_summary_rows),
            summary_row=summary_row,
            css_class="gt_first_grand_summary_row_bottom" if i == 0 else None,
        )
        body_rows.append(row_html)

    all_body_rows = "\n".join(body_rows)

    return f"""<tbody class="gt_table_body">
{all_body_rows}
</tbody>"""


def _create_row_component_h(
    column_vars: list[ColInfo],
    row_stub_var: ColInfo | None,
    has_row_stub_column: bool,
    has_group_stub_column: bool,
    apply_stub_striping: bool,
    apply_body_striping: bool,
    styles_cells: list[StyleInfo],  # Either styles_cells OR styles_grand_summary
    styles_labels: list[StyleInfo],  # Either styles_row_label OR styles_grand_summary_label
    leading_cell: str | None = None,  # For group label when row_group_as_column = True
    row_index: int | None = None,
    summary_row: SummaryRowInfo | None = None,  # For summary rows
    tbl_data: TblData | None = None,
    css_class: str | None = None,
) -> str:
    """Create a single table row (either data row or summary row)"""

    is_summary_row = summary_row is not None
    body_cells: list[str] = []

    if leading_cell:
        body_cells.append(leading_cell)

    # Handle special cases for summary rows with group stub columns
    if is_summary_row and has_group_stub_column:
        if has_row_stub_column:
            # Case 1: Both row_stub_column and group_stub_column
            # Create a single cell that spans both columns for summary row label (id)
            colspan = 2
        else:
            # Case 2: Only group_stub_column, no row_stub_column
            colspan = 1

        cell_styles = _flatten_styles(
            [x for x in styles_labels if x.rownum == row_index], wrap=True
        )

        classes = ["gt_row", "gt_left", "gt_stub", "gt_grand_summary_row"]
        if css_class:
            classes.append(css_class)
        classes_str = " ".join(classes)

        body_cells.append(
            f"""    <th{cell_styles} class="{classes_str}" colspan="{colspan}">{summary_row.id}</th>"""
        )

        # Skip the first column in column_vars since we've already handled the stub
        column_vars_to_process = [column for column in column_vars if not column.is_stub]

    else:
        # Normal case: process all column_vars
        column_vars_to_process = column_vars

    for colinfo in column_vars_to_process:
        # Get cell content
        if is_summary_row:
            if colinfo == row_stub_var or colinfo.is_stub:
                cell_content = summary_row.id
            else:
                cell_content = summary_row.values.get(colinfo.var)
        elif colinfo.type == ColInfoTypeEnum.summary_placeholder:
            # TODO: this row is technically a summary row, but is_summary_row is False here
            cell_content = "&nbsp;"
        else:
            cell_content = _get_cell(tbl_data, row_index, colinfo.var)

        if css_class:
            classes = [css_class]
        else:
            classes = []

        cell_str = str(cell_content)
        cell_alignment = colinfo.defaulted_align

        # Get styles
        _body_styles = [
            x for x in styles_cells if x.rownum == row_index and x.colname == colinfo.var
        ]
        _rowname_styles = (
            [x for x in styles_labels if x.rownum == row_index] if colinfo.is_stub else []
        )

        # Build classes and element
        if colinfo.is_stub:
            el_name = "th"
            classes += ["gt_row", "gt_left", "gt_stub"]
            if is_summary_row:
                classes.append("gt_grand_summary_row")
            if apply_stub_striping:
                classes.append("gt_striped")
        else:
            el_name = "td"
            classes += ["gt_row", f"gt_{cell_alignment}"]
            if is_summary_row:
                classes.append("gt_grand_summary_row")
            if apply_body_striping:
                classes.append("gt_striped")

        classes_str = " ".join(classes)
        cell_styles = _flatten_styles(_body_styles + _rowname_styles, wrap=True)

        body_cells.append(
            f"""    <{el_name}{cell_styles} class="{classes_str}">{cell_str}</{el_name}>"""
        )

    return "  <tr>\n" + "\n".join(body_cells) + "\n  </tr>"


def create_source_notes_component_h(data: GTData) -> str:
    source_notes = data._source_notes

    # Filter list of StyleInfo to only those that apply to the source notes
    styles_footer = [x for x in data._styles if _is_loc(x.locname, loc.LocFooter)]
    styles_source_notes = [x for x in data._styles if _is_loc(x.locname, loc.LocSourceNotes)]

    # If there are no source notes, then return an empty string
    if not source_notes:
        return ""

    # Obtain the `multiline` and `separator` options from `_options`
    multiline = data._options.source_notes_multiline.value
    separator = cast(str, data._options.source_notes_sep.value)

    # Get the effective number of columns, which is number of columns
    # that will finally be rendered accounting for the stub layout
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    n_cols_total = data._boxhead._get_effective_number_of_columns(
        stub=data._stub, has_summary_rows=has_summary_rows, options=data._options
    )

    # Handle the multiline source notes case (each note takes up one line)
    if multiline:
        # Create the source notes component as a series of `<tr><td>` (one per
        # source note) inside of a `<tfoot>`

        source_notes_tr: list[str] = []

        _styles = _flatten_styles(styles_footer + styles_source_notes, wrap=True)
        for note in source_notes:
            note_str = _process_text(note)

            source_notes_tr.append(
                f"""
  <tr>
    <td class="gt_sourcenote" colspan="{n_cols_total}"{_styles}>{note_str}</td>
  </tr>
"""
            )

        source_notes_joined = "\n".join(source_notes_tr)

        source_notes_component = f"""  <tfoot class="gt_sourcenotes">
  {source_notes_joined}
</tfoot>"""

        return source_notes_component

    # TODO: Perform HTML escaping on the separator text and
    # transform space characters to non-breaking spaces

    # Create the source notes component as a single `<tr><td>` inside
    # of a `<tfoot>`

    source_note_list: list[str] = []
    for note in source_notes:
        note_str = _process_text(note)
        source_note_list.append(note_str)

    source_notes_str_joined = separator.join(source_note_list)

    source_notes_component = f"""<tfoot>
  <tr class="gt_sourcenotes">
    <td class="gt_sourcenote" colspan="{n_cols_total}">
      <div style="padding-bottom:2px;">{source_notes_str_joined}</div>
    </td>
  </tr>
</tfoot>
    """

    return source_notes_component


def create_footnotes_component_h(data: GTData):
    # Filter list of StyleInfo to only those that apply to the footnotes
    styles_footnotes = [x for x in data._styles if _is_loc(x.locname, loc.LocFootnotes)]

    return ""


def rtl_modern_unicode_charset() -> str:
    """
    Returns a string containing a regular expression that matches all characters
    from RTL scripts that are supported by modern web browsers.
    """
    # The Hebrew Unicode character set (112 code points)
    hebrew_unicode_charset = r"[\u0590-\u05FF]"

    # The Arabic Unicode character set (256 code points)
    arabic_unicode_charset = r"[\u0600-\u06FF]"

    # The Syriac Unicode character set (80 code points)
    syriac_unicode_charset = r"[\u0700-\u074F]"

    # The Thaana Unicode character set (64 code points)
    thaana_unicode_charset = r"[\u0780-\u07BF]"

    # The Samaritan Unicode character set (61 code points)
    samaritan_unicode_charset = r"[\u0800-\u083F]"

    # The Mandaic Unicode character set (32 code points)
    mandaic_unicode_charset = r"[\u0840-\u085F]"

    # The combination of these RTL character sets
    rtl_modern_unicode_charset = (
        hebrew_unicode_charset
        + "|"
        + arabic_unicode_charset
        + "|"
        + syriac_unicode_charset
        + "|"
        + thaana_unicode_charset
        + "|"
        + samaritan_unicode_charset
        + "|"
        + mandaic_unicode_charset
    )

    return rtl_modern_unicode_charset


def _get_spanners_matrix_height(
    data: GTData, include_hidden: bool = False, omit_columns_row: bool = False
) -> int:
    """
    Returns the height of the spanners matrix.

    Args:
        data (GTData): The data to be used for rendering the table.
        include_hidden (bool, optional): Whether to include hidden columns in the table. Defaults to False.
        omit_columns_row (bool, optional): Whether to omit the columns row in the table. Defaults to False.

    Returns:
        int: The height of the spanners matrix.
    """
    spanners_matrix, _ = spanners_print_matrix(
        spanners=data._spanners,
        boxhead=data._boxhead,
        include_hidden=include_hidden,
        omit_columns_row=omit_columns_row,
    )

    return len(spanners_matrix)


# Get the attributes needed for the <table> tag
def _get_table_defs(data: GTData) -> dict[str, Any]:
    # Get the `table-layout` value, which is set in `_options`
    table_layout = data._options.table_layout.value
    table_style = f"table-layout: {table_layout};"

    # Get the number of columns that have a width set
    column_widths = data._boxhead._get_column_widths()

    # If all values in the `column_widths` lists are None, then return a dictionary with
    # `table_style` and `table_colgroups` set to None; this is the case where column widths are
    # not set for any columns and, as a result, there should not be a `<colgroup>` tag requirement
    if all(width is None for width in column_widths):
        return dict(table_style=None, table_colgroups=None)

    # Get the table's width (which or may not have been set)
    table_width = data._options.table_width.value

    # Get finalized names of the columns (this includes the stub column)
    final_columns = data._boxhead.final_columns(options=data._options)

    # Get the widths of the columns
    widths = [col.column_width for col in final_columns]

    # If all of the widths are defined as px values for all columns, then ensure that the width
    # values are strictly respected as absolute width values (even if table width already set)
    if (
        all(isinstance(width, str) and width is not None and "px" in width for width in widths)
        and table_width == "auto"
    ):
        table_width = "0px"

    if (
        all(isinstance(width, str) and width is not None and "%" in width for width in widths)
        and table_width == "auto"
    ):
        table_width = "100%"

    if table_width != "auto":
        table_style = f"{table_style}; width: {table_width}"

    # Stop function if all length dimensions (where provided)
    # don't conform to accepted CSS length definitions
    # TODO: skipping this for now as the method/function doesn't exist
    # validate_css_lengths(widths)
    # Create the `<colgroup>` tag
    table_colgroups = tags.colgroup([tags.col(style=css(width=width)) for width in widths])

    table_defs_dict = dict(table_style=table_style, table_colgroups=table_colgroups)

    return table_defs_dict
