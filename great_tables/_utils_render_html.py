from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING, Any, cast

from htmltools import HTML, TagList, css, tags

from . import _locations as loc
from ._gt_data import (
    ColInfo,
    ColInfoTypeEnum,
    FootnoteInfo,
    FootnotePlacement,
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


def _get_locnum_for_footnote_location(locname: loc.Loc | None) -> int | float:
    """Get the visual hierarchy order for footnote location ordering."""
    if locname is None:
        return 999

    # Visual hierarchy mapping for footnote location ordering
    if isinstance(locname, loc.LocTitle):
        return 1
    elif isinstance(locname, loc.LocSubTitle):
        return 2
    elif isinstance(locname, loc.LocStubhead):
        return 3
    elif isinstance(locname, loc.LocSpannerLabels):
        return 4
    elif isinstance(locname, loc.LocColumnLabels):
        return 5
    elif isinstance(locname, (loc.LocBody, loc.LocStub)):
        return 6  # Same as data since stub and data cells are on the same row level
    elif isinstance(locname, loc.LocRowGroups):
        return 5
    elif isinstance(locname, loc.LocSummary):
        return 5.5
    else:
        return 999  # Default to 999 for unknown locations


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

    # Filter footnotes for title and subtitle - similar to styles filtering
    footnotes_title = [x for x in data._footnotes if isinstance(x.locname, loc.LocTitle)]
    footnotes_subtitle = [x for x in data._footnotes if isinstance(x.locname, loc.LocSubTitle)]

    # Add footnote marks to title and subtitle if applicable
    if has_title:
        title = _apply_footnotes_to_text(footnotes_title, data, title)
    if has_subtitle:
        subtitle = _apply_footnotes_to_text(footnotes_subtitle, data, subtitle)

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

    # Filter footnotes for stubhead - similar to styles filtering
    footnotes_stubhead = [x for x in data._footnotes if isinstance(x.locname, loc.LocStubhead)]

    # If there are no spanners, then we have to create the cells for the stubhead label
    # (if present) and for the column headings
    if spanner_row_count == 0:
        # Create the cell for the stubhead label
        if stub_layout:
            table_col_headings.append(
                tags.th(
                    HTML(
                        _apply_footnotes_to_text(
                            footnotes_stubhead, data, _process_text(stub_label)
                        )
                    ),
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

            # Filter footnotes for column label footnotes
            footnotes_i = [
                x
                for x in data._footnotes
                if isinstance(x.locname, loc.LocColumnLabels) and x.colname == info.var
            ]

            # Add footnote marks to column label if any
            column_label_with_footnotes = _apply_footnotes_to_text(
                footnotes=footnotes_i, data=data, text=_process_text(info.column_label)
            )

            table_col_headings.append(
                tags.th(
                    HTML(column_label_with_footnotes),
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
                    HTML(
                        _apply_footnotes_to_text(
                            footnotes_stubhead, data, _process_text(stub_label)
                        )
                    ),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{stubhead_label_alignment}",
                    rowspan=2,
                    colspan=len(stub_layout),
                    style=_flatten_styles(styles_stubhead),
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    id=_create_element_id(table_id, stub_label),
                )
            )  # NOTE: Run-length encoding treats missing values as distinct from each other; in other
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

                # Filter footnotes for this column label - similar to styles filtering
                footnotes_i = [
                    x
                    for x in data._footnotes
                    if isinstance(x.locname, loc.LocColumnLabels) and x.colname == h_info.var
                ]

                # Get the alignment values for the first set of column labels
                first_set_alignment = h_info.defaulted_align

                # Add footnote marks to column label if any
                column_label_with_footnotes = _apply_footnotes_to_text(
                    footnotes_i, data, _process_text(h_info.column_label)
                )

                # Creation of <th> tags for column labels with no spanners above them
                level_1_spanners.append(
                    tags.th(
                        HTML(column_label_with_footnotes),
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

                    # Filter footnotes for this spanner label - similar to styles filtering
                    footnotes_i = [
                        x
                        for x in data._footnotes
                        if isinstance(x.locname, loc.LocSpannerLabels)
                        and spanner_ids_level_1_index[ii]
                        and x.grpname == spanner_ids_level_1_index[ii]
                    ]

                    level_1_spanners.append(
                        tags.th(
                            tags.span(
                                HTML(
                                    _apply_footnotes_to_text(
                                        footnotes_i,
                                        data,
                                        _process_text(spanner_ids_level_1_index[ii]),
                                    )
                                ),
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

                # Filter footnotes for this column label - similar to styles filtering
                footnotes_i = [
                    x
                    for x in data._footnotes
                    if isinstance(x.locname, loc.LocColumnLabels) and x.colname == remaining_heading
                ]

                remaining_alignment = boxhead._get_boxhead_get_alignment_by_var(
                    var=remaining_heading
                )

                # Add footnote marks to column label if any
                remaining_headings_label_with_footnotes = _apply_footnotes_to_text(
                    footnotes_i,
                    data,
                    _process_text(remaining_headings_label),
                )

                spanned_column_labels.append(
                    tags.th(
                        HTML(remaining_headings_label_with_footnotes),
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

                    # Filter footnotes for this spanner label - similar to styles filtering
                    footnotes_i = [
                        x
                        for x in data._footnotes
                        if isinstance(x.locname, loc.LocSpannerLabels)
                        and span_label
                        and x.grpname == span_label
                    ]

                    if span_label:
                        span = tags.span(
                            HTML(
                                _apply_footnotes_to_text(
                                    footnotes_i,
                                    data,
                                    _process_text(span_label),
                                )
                            ),
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
            data=data,
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
    data: GTData | None = None,  # For footnote handling
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

        # Apply footnotes to cell content if data is provided
        if data is not None and not is_summary_row:
            if colinfo.is_stub:
                # For stub cells, footnotes are stored with colname=None
                footnotes_i = [
                    x
                    for x in data._footnotes
                    if isinstance(x.locname, loc.LocStub) and x.rownum == row_index
                ]
                cell_str = _apply_footnotes_to_text(footnotes_i, data, cell_str)
            else:
                footnotes_i = [
                    x
                    for x in data._footnotes
                    if isinstance(x.locname, loc.LocBody)
                    and x.colname == colinfo.var
                    and x.rownum == row_index
                ]
                cell_str = _apply_footnotes_to_text(footnotes_i, data, cell_str)

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


def create_footer_component_h(data: GTData) -> str:
    source_notes = data._source_notes
    footnotes = data._footnotes

    # Get the effective number of columns for colspan
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    n_cols_total = data._boxhead._get_effective_number_of_columns(
        stub=data._stub, has_summary_rows=has_summary_rows, options=data._options
    )

    footer_rows = []

    # Add source notes if they exist
    if source_notes:
        # Filter list of StyleInfo to only those that apply to the source notes
        styles_footer = [x for x in data._styles if _is_loc(x.locname, loc.LocFooter)]
        styles_source_notes = [x for x in data._styles if _is_loc(x.locname, loc.LocSourceNotes)]

        # Obtain the `multiline` and `separator` options from `_options`
        multiline = data._options.source_notes_multiline.value
        separator = cast(str, data._options.source_notes_sep.value)

        if multiline:
            # Each source note gets its own row with gt_sourcenotes class on the tr
            _styles = _flatten_styles(styles_footer + styles_source_notes, wrap=True)
            for note in source_notes:
                note_str = _process_text(note)
                footer_rows.append(
                    f'<tr class="gt_sourcenotes"><td class="gt_sourcenote" colspan="{n_cols_total}"{_styles}><span class="gt_from_md">{note_str}</span></td></tr>'
                )
        else:
            # All source notes in a single row with gt_sourcenotes class on the tr
            source_note_list = []
            for note in source_notes:
                note_str = _process_text(note)
                source_note_list.append(note_str)

            source_notes_str_joined = separator.join(source_note_list)
            footer_rows.append(
                f'<tr class="gt_sourcenotes"><td class="gt_sourcenote" colspan="{n_cols_total}"><span class="gt_from_md">{source_notes_str_joined}</span></td></tr>'
            )

    # Add footnotes if they exist
    if footnotes:
        # Process footnotes and assign marks
        footnotes_with_marks = _process_footnotes_for_display(data, footnotes)

        if footnotes_with_marks:
            # Each footnote gets its own row
            for footnote_data in footnotes_with_marks:
                mark = footnote_data.get("mark", "")
                text = footnote_data.get("text", "")

                footnote_mark_html = _create_footnote_mark_html(mark=mark)

                # Wrap footnote text in `gt_from_md` span if it contains HTML markup
                if "<" in text and ">" in text:
                    footnote_text = f'<span class="gt_from_md">{text}</span>'
                else:
                    footnote_text = text

                footnote_html = f"{footnote_mark_html} {footnote_text}"
                footer_rows.append(
                    f'<tr class="gt_footnotes"><td class="gt_footnote" colspan="{n_cols_total}">{footnote_html}</td></tr>'
                )

    # If no footer content, return empty string
    if not footer_rows:
        return ""

    return f'<tfoot>{"".join(footer_rows)}</tfoot>'


def _should_display_footnote(data: GTData, footnote: FootnoteInfo) -> bool:
    # If footnote targets a specific column, check if it's hidden
    if footnote.colname is not None:
        # Get column info from boxhead to check if it's hidden
        for col_info in data._boxhead._d:
            if col_info.var == footnote.colname:
                return col_info.visible
        # If column not found in boxhead, assume it should be displayed
        return True

    # For footnotes that don't target specific columns (e.g., title, subtitle), always display
    return True


def _process_footnotes_for_display(
    data: GTData, footnotes: list[FootnoteInfo]
) -> list[dict[str, str]]:
    if not footnotes:
        return []

    # Filter out footnotes for hidden columns
    visible_footnotes = [f for f in footnotes if _should_display_footnote(data, f)]

    # Sort footnotes by visual order (same logic as in _get_footnote_mark_string);
    # this ensures footnotes appear in the footnotes section in the same order as their
    # marks in the table
    footnote_positions: list[tuple[tuple[int | float, int, int], FootnoteInfo]] = []

    for fn_info in visible_footnotes:
        if fn_info.locname is None:
            continue

        # Assign locnum based on visual hierarchy
        locnum = _get_locnum_for_footnote_location(fn_info.locname)

        # Assign column number, with stub getting a lower value than data columns
        if isinstance(fn_info.locname, loc.LocStub):
            colnum = -1  # Stub appears before all data columns
        else:
            colnum = _get_column_index(data, fn_info.colname) if fn_info.colname else 0
        rownum = (
            0
            if isinstance(fn_info.locname, loc.LocColumnLabels)
            else (fn_info.rownum if fn_info.rownum is not None else 0)
        )

        sort_key = (locnum, rownum, colnum)
        footnote_positions.append((sort_key, fn_info))

    # Sort by visual order
    footnote_positions.sort(key=lambda x: x[0])
    sorted_footnotes = [fn_info for _, fn_info in footnote_positions]

    # Group footnotes by their text to avoid duplicates and get their marks
    footnote_data: dict[str, str] = {}  # text -> mark_string
    footnote_order: list[str] = []

    for footnote in sorted_footnotes:
        if footnote.footnotes:
            footnote_text = footnote.footnotes[0] if footnote.footnotes else ""
            if footnote_text not in footnote_data:
                mark_string = _get_footnote_mark_string(data, footnote)
                footnote_data[footnote_text] = mark_string
                footnote_order.append(footnote_text)

    # Add footnotes without marks at the beginning (also filter for visibility)
    markless_footnotes = [f for f in visible_footnotes if f.locname is None]  # type: ignore
    result: list[dict[str, str]] = []

    # Add markless footnotes first
    for footnote in markless_footnotes:
        if footnote.footnotes:
            footnote_text = footnote.footnotes[0]
            result.append({"mark": "", "text": footnote_text})

    # Add footnotes with marks and maintain visual order (order they appear in table);
    # the `footnote_order` list already contains footnotes in visual order based on how
    # `_get_footnote_mark_string()` assigns marks
    mark_type = _get_footnote_marks_option(data)
    if isinstance(mark_type, str) and mark_type == "numbers":
        # For numbers, sort by numeric mark value to handle any edge cases
        sorted_texts = sorted(
            footnote_order,
            key=lambda text: int(footnote_data[text])
            if footnote_data[text].isdigit()
            else float("inf"),
        )
    else:
        # For letters/symbols, maintain visual order (don't sort alphabetically)
        sorted_texts = footnote_order

    for text in sorted_texts:
        mark_string = footnote_data[text]
        result.append({"mark": mark_string, "text": text})

    return result


def _get_footnote_mark_symbols() -> dict[str, list[str]]:
    from ._helpers import LETTERS, letters

    return {
        "numbers": [],
        "letters": letters(),
        "LETTERS": LETTERS(),
        "standard": ["*", "†", "‡", "§"],
        "extended": ["*", "†", "‡", "§", "‖", "¶"],
    }


def _generate_footnote_mark(mark_index: int, mark_type: str | list[str] = "numbers") -> str:
    if isinstance(mark_type, str):
        if mark_type == "numbers":
            return str(mark_index)

        symbol_sets = _get_footnote_mark_symbols()
        if mark_type in symbol_sets:
            symbols = symbol_sets[mark_type]
        else:
            # Default to numbers if unknown type
            return str(mark_index)
    else:
        symbols = mark_type

    if not symbols:
        return str(mark_index)

    # Calculate symbol and repetition for cycling behavior;
    # e.g., for 4 symbols: index 1-4 -> symbol once, 5-8 -> symbol twice, etc.
    symbol_index = (mark_index - 1) % len(symbols)
    repetitions = (mark_index - 1) // len(symbols) + 1

    return symbols[symbol_index] * repetitions


def _get_footnote_marks_option(data: GTData) -> str | list[str]:
    # Read from the options system
    if hasattr(data, "_options") and hasattr(data._options, "footnotes_marks"):
        marks_value = data._options.footnotes_marks.value
        if marks_value is not None:
            return marks_value

    # Default to numbers
    return "numbers"


def _create_footnote_mark_html(mark: str) -> str:
    # Handle markless footnotes (footnotes added with `locations=None`)
    # These appear in the footer without marks in the table body
    if not mark:
        return ""

    # Use consistent span structure for both references and footer
    return f'<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">{mark}</span>'


def _get_footnote_mark_string(data: GTData, footnote_info: FootnoteInfo) -> str:
    if not data._footnotes or not footnote_info.footnotes:
        mark_type = _get_footnote_marks_option(data)
        return _generate_footnote_mark(1, mark_type)

    # Create a list of all footnote positions with their text, following R gt approach
    footnote_positions: list[tuple[tuple[int | float, int, int], str]] = []

    for fn_info in data._footnotes:
        if not fn_info.footnotes or fn_info.locname is None:
            continue

        # Skip footnotes for hidden columns
        if not _should_display_footnote(data, fn_info):
            continue

        footnote_text = _process_text(fn_info.footnotes[0])

        # Assign locnum (location number) based on the location hierarchy where
        # lower numbers appear first in reading order
        locnum = _get_locnum_for_footnote_location(fn_info.locname)

        # Get colnum (column number) and assign stub a lower value than data columns
        if isinstance(fn_info.locname, loc.LocStub):
            colnum = -1  # Stub appears before all data columns
        elif isinstance(fn_info.locname, loc.LocSpannerLabels):
            # For spanners, use the leftmost column index to ensure left-to-right ordering
            colnum = _get_spanner_leftmost_column_index(data, fn_info.grpname)
        else:
            colnum = _get_column_index(data, fn_info.colname) if fn_info.colname else 0

        # Get rownum; for headers use 0, for body use actual row number
        if isinstance(fn_info.locname, loc.LocColumnLabels):
            rownum = 0  # Headers are row 0
        else:
            rownum = fn_info.rownum if fn_info.rownum is not None else 0

        # Sort key: (locnum, rownum, colnum); this should match reading order
        # of top-to-bottom, left-to-right
        sort_key = (locnum, rownum, colnum)
        footnote_positions.append((sort_key, footnote_text))

    # Sort by (locnum, rownum, colnum): headers before body
    footnote_positions.sort(key=lambda x: x[0])

    # Get unique footnote texts in sorted order
    unique_footnotes: list[str] = []
    for _, text in footnote_positions:
        if text not in unique_footnotes:
            unique_footnotes.append(text)

    # Find the mark index for this footnote's text
    if footnote_info.footnotes:
        footnote_text = _process_text(footnote_info.footnotes[0])
        try:
            mark_index = unique_footnotes.index(footnote_text) + 1  # Use 1-based indexing
            mark_type = _get_footnote_marks_option(data)
            return _generate_footnote_mark(mark_index, mark_type)
        except ValueError:
            mark_type = _get_footnote_marks_option(data)
            return _generate_footnote_mark(1, mark_type)

    mark_type = _get_footnote_marks_option(data)
    return _generate_footnote_mark(1, mark_type)


def _get_column_index(data: GTData, colname: str | None) -> int:
    if not colname:
        return 0

    # Get the column order from boxhead
    columns = data._boxhead._get_default_columns()
    for i, col_info in enumerate(columns):
        if col_info.var == colname:
            return i

    return 0


def _get_spanner_leftmost_column_index(data: GTData, spanner_grpname: str | None) -> int:
    if not spanner_grpname:
        return 0

    # Find the spanner with this group name
    for spanner in data._spanners:
        if spanner.spanner_label == spanner_grpname:
            # Get the column indices for all columns in this spanner
            column_indices = []
            for col_var in spanner.vars:
                col_index = _get_column_index(data, col_var)
                column_indices.append(col_index)

            # Return the minimum (leftmost) column index
            return min(column_indices) if column_indices else 0

    return 0


def _apply_footnotes_to_text(footnotes: list[FootnoteInfo], data: GTData, text: str) -> str:
    if not footnotes:
        return text

    # Get mark strings for each footnote
    mark_strings: list[str] = []
    footnote_placements: list[FootnoteInfo] = []
    for footnote in footnotes:
        mark_string = _get_footnote_mark_string(data, footnote)
        if mark_string not in mark_strings:
            mark_strings.append(mark_string)
            footnote_placements.append(footnote)

    # Sort marks: for numbers, sort numerically; for symbols, sort by their order in symbol set
    mark_type = _get_footnote_marks_option(data)
    if isinstance(mark_type, str) and mark_type == "numbers":
        # Sort numerically for numbers
        mark_strings.sort(key=lambda x: int(x) if x.isdigit() else float("inf"))
    else:
        # For symbols, maintain the order they appear (which should already be correct)
        # since `_get_footnote_mark_string()` returns them in visual order
        pass

    # Create a single footnote mark span with comma-separated marks
    if mark_strings:
        # Join mark strings with commas (no spaces)
        marks_text = ",".join(mark_strings)
        marks_html = (
            '<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;'
            f'font-weight:normal;line-height:0;">{marks_text}</span>'
        )

        # Determine placement based on the first footnote's placement setting
        # (all footnotes for the same location should have the same placement)
        placement = footnote_placements[0].placement if footnote_placements else None

        # Apply placement logic
        return _apply_footnote_placement(text, marks_html, placement)

    return text


def _apply_footnote_placement(
    text: str, marks_html: str, placement: FootnotePlacement | None
) -> str:
    # Default to auto if no placement specified
    if placement is None:
        placement_setting = FootnotePlacement.auto
    else:
        placement_setting = placement

    if placement_setting == FootnotePlacement.left:
        # Left placement: footnote marks + space + text
        return f"{marks_html} {text}"
    elif placement_setting == FootnotePlacement.right:
        # Right placement: text + footnote marks
        return f"{text}{marks_html}"
    else:
        # Auto placement: left for numbers, right for everything else
        if _is_numeric_content(text):
            # For numbers, place marks on the left so alignment is preserved
            return f"{marks_html} {text}"
        else:
            # For text, place marks on the right
            return f"{text}{marks_html}"


def _is_numeric_content(text: str) -> bool:
    import re

    # Strip HTML tags for analysis
    clean_text = re.sub(r"<[^>]+>", "", text).strip()

    if not clean_text:
        return False

    # Remove common formatting characters to get to the core content
    # This handles formatted numbers with commas, currency symbols, percent signs, etc.
    # Include a wide range of currency symbols and formatting characters
    formatting_chars = r"[,\s$%€£¥₹₽₩₪₱₡₴₦₨₵₸₲₩\(\)−\-+]"
    number_core = re.sub(formatting_chars, "", clean_text)

    # Check if what remains is primarily numeric (including decimals)
    if not number_core:
        return False

    # Check if the core is a valid number: must have at least one digit,
    # and can have at most one decimal point
    numeric_pattern = r"^\d*\.?\d+$|^\d+\.?\d*$"
    return bool(re.match(numeric_pattern, number_core)) and number_core != "."


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
