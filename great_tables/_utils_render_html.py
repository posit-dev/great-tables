from __future__ import annotations

from itertools import chain
from typing import Any, cast

from great_tables._spanners import spanners_print_matrix
from htmltools import HTML, TagList, css, tags

from ._gt_data import GTData
from ._tbl_data import _get_cell, cast_frame_to_string, n_rows, replace_null_frame
from ._text import _process_text, _process_text_id
from ._utils import heading_has_subtitle, heading_has_title, seq_groups


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

    # Get the effective number of columns, which is number of columns
    # that will finally be rendered accounting for the stub layout
    n_cols_total = data._boxhead._get_effective_number_of_columns(
        stub=data._stub, options=data._options
    )

    if has_subtitle:
        heading = f"""
  <tr class="gt_heading">
    <td colspan="{n_cols_total}" class="gt_heading gt_title gt_font_normal">{title}</td>
  </tr>
  <tr class="gt_heading">
    <td colspan="{n_cols_total}" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">{subtitle}</td>
  </tr>"""
    else:
        heading = f"""
  <tr class="gt_heading">
    <td colspan="{n_cols_total}" class="gt_heading gt_title gt_font_normal">{title}</td>
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
    # TODO: skipping styles for now
    # styles_tbl = dt_styles_get(data = data)
    boxhead = data._boxhead

    # TODO: The body component of the table is only needed for determining RTL alignment
    # is needed in the corresponding column labels
    # body = data._body

    # Get vector representation of stub layout
    stub_layout = data._stub._get_stub_layout(options=data._options)

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

    # TODO: Skipping styles for now
    # Get the style attrs for the stubhead label
    # stubhead_style_attrs = subset(styles_tbl, locname == "stubhead")
    # Get the style attrs for the spanner column headings
    # spanner_style_attrs = subset(styles_tbl, locname == "columns_groups")
    # Get the style attrs for the spanner column headings
    # column_style_attrs = subset(styles_tbl, locname == "columns_columns")

    # If columns are present in the stub, then replace with a set stubhead label or nothing
    if len(stub_layout) > 0 and stubh is not None:
        stub_label = stubh
        stub_var = "::stub"
    else:
        stub_label = ""
        stub_var = None

    # Set a default alignment for the stubhead label
    stubhead_label_alignment = "left"

    # Initialize the column headings list
    table_col_headings = []

    # If there are no spanners, then we have to create the cells for the stubhead label
    # (if present) and for the column headings
    if spanner_row_count == 0:
        # Create the cell for the stubhead label
        if len(stub_layout) > 0:
            stubhead_style = None
            # FIXME: Ignore styles for now
            # if stubhead_style_attrs is not None and len(stubhead_style_attrs) > 0:
            #    stubhead_style = stubhead_style_attrs[0].html_style

            table_col_headings.append(
                tags.th(
                    HTML(_process_text(stub_label)),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{stubhead_label_alignment}",
                    rowspan="1",
                    colspan=len(stub_layout),
                    style=stubhead_style,
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    id=_process_text_id(stub_label),
                )
            )

        # Create the headings in the case where there are no spanners at all -------------------------
        for info in headings_info:
            # NOTE: Ignore styles for now
            # styles_column = subset(column_style_attrs, colnum == i)
            #
            # Convert the code above this comment from R to valid python
            # if len(styles_column) > 0:
            #    column_style = styles_column[0].html_style
            column_style = None

            table_col_headings.append(
                tags.th(
                    HTML(_process_text(info.column_label)),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{info.defaulted_align}",
                    rowspan=1,
                    colspan=1,
                    style=column_style,
                    scope="col",
                    id=_process_text_id(info.column_label),
                )
            )

        # Join the <th> cells into a string and begin each with a newline
        th_cells = "\n" + "\n".join(["  " + str(tag) for tag in table_col_headings]) + "\n"

        table_col_headings = tags.tr(HTML(th_cells), class_="gt_col_headings")

    #
    # Create the spanners and column labels in the case where there *are* spanners -------------
    #

    if spanner_row_count >= 1:
        spanners, _ = spanners_print_matrix(
            spanners=data._spanners, boxhead=boxhead, include_hidden=False
        )

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
        if len(stub_layout) > 0:
            # NOTE: Ignore styles for now
            # if len(stubhead_style_attrs) > 0:
            #     stubhead_style = stubhead_style_attrs.html_style
            # else:
            #     stubhead_style = None
            stubhead_style = None

            level_1_spanners.append(
                tags.th(
                    HTML(_process_text(stub_label)),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{str(stubhead_label_alignment)}",
                    rowspan=2,
                    colspan=len(stub_layout),
                    style=stubhead_style,
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    id=_process_text_id(stub_label),
                )
            )

        # NOTE: Run-length encoding treats missing values as distinct from each other; in other
        # words, each missing value starts a new run of length 1

        spanner_ids_level_1_index = list(spanner_ids[level_1_index].values())
        spanners_rle = seq_groups(seq=spanner_ids_level_1_index)

        # `colspans` matches `spanners` in length; each element is the number of columns that the
        # <th> at that position should span; if 0, then skip the <th> at that position
        group_spans = [[x[1]] + [0] * (x[1] - 1) for x in spanners_rle]

        colspans = list(chain(*group_spans))

        for ii, (span_key, h_info) in enumerate(zip(spanner_col_names, headings_info)):
            if spanner_ids[level_1_index][span_key] is None:
                # NOTE: Ignore styles for now
                # styles_heading = filter(
                #     lambda x: x.get('locname') == "columns_columns" and x.get('colname') == headings_vars[i],
                #     styles_tbl if 'styles_tbl' in locals() else []
                # )
                #
                # heading_style = next(styles_heading, {}).get('html_style', None)
                heading_style = None

                # Get the alignment values for the first set of column labels
                first_set_alignment = h_info.defaulted_align

                # Creation of <th> tags for column labels with no spanners above them
                level_1_spanners.append(
                    tags.th(
                        HTML(_process_text(h_info.column_label)),
                        class_=f"gt_col_heading gt_columns_bottom_border gt_{str(first_set_alignment)}",
                        rowspan=2,
                        colspan=1,
                        style=heading_style,
                        scope="col",
                        id=_process_text_id(h_info.column_label),
                    )
                )

            elif spanner_ids[level_1_index][span_key] is not None:
                # If colspans[i] == 0, it means that a previous cell's
                # `colspan` will cover us
                if colspans[ii] > 0:
                    # NOTE: Ignore styles for now
                    # FIXME: this needs to be rewritten
                    # styles_spanners = filter(
                    #    spanner_style_attrs,
                    #    locname == "columns_groups",
                    #    grpname == spanner_ids[level_1_index, ][i]
                    #  )
                    #
                    # spanner_style =
                    #   if (nrow(styles_spanners) > 0) {
                    #     styles_spanners$html_style
                    #   } else {
                    #     NULL
                    #   }
                    spanner_style = None

                    level_1_spanners.append(
                        tags.th(
                            tags.span(
                                HTML(_process_text(spanner_ids_level_1_index[ii])),
                                class_="gt_column_spanner",
                            ),
                            class_="gt_center gt_columns_top_border gt_column_spanner_outer",
                            rowspan=1,
                            colspan=colspans[ii],
                            style=spanner_style,
                            scope="colgroup" if colspans[ii] > 1 else "col",
                            id=_process_text_id(spanner_ids_level_1_index[ii]),
                        )
                    )

        remaining_headings = [k for k, v in spanner_ids[level_1_index].items() if v is not None]
        remaining_headings_labels = [
            entry.column_label for entry in boxhead if entry.var in remaining_headings
        ]
        col_alignment = [
            entry.defaulted_align for entry in boxhead if entry.var in remaining_headings
        ]

        if len(remaining_headings) > 0:
            spanned_column_labels = []

            for j in range(len(remaining_headings)):
                # Skip styles for now
                # styles_remaining = styles_tbl[
                #     (styles_tbl["locname"] == "columns_columns") &
                #     (styles_tbl["colname"] == remaining_headings[j])
                # ]
                #
                # remaining_style = (
                #     styles_remaining["html_style"].values[0]
                #     if len(styles_remaining) > 0
                #     else None
                # )
                remaining_style = None

                remaining_alignment = boxhead._get_boxhead_get_alignment_by_var(
                    var=remaining_headings[j]
                )

                spanned_column_labels.append(
                    tags.th(
                        HTML(_process_text(remaining_headings_labels[j])),
                        class_=f"gt_col_heading gt_columns_bottom_border gt_{remaining_alignment}",
                        rowspan=1,
                        colspan=1,
                        style=remaining_style,
                        scope="col",
                        id=_process_text_id(remaining_headings_labels[j]),
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
        higher_spanner_rows_idx = range(0, len(spanner_ids) - 2)
        higher_spanner_rows = TagList()

        for i in higher_spanner_rows_idx:
            spanners_row = spanners[i]
            for k, v in spanners_row.items():
                if v is None:
                    spanners_row[k] = ""

            spanner_ids_index = spanners_row.values()
            spanners_rle = seq_groups(seq=spanner_ids_index)
            group_spans = [[x[1]] + [0] * (x[1] - 1) for x in spanners_rle]
            colspans = list(chain(*group_spans))
            level_i_spanners = []

            for colspan, span_label in zip(colspans, spanners_row.values()):
                if colspan > 0:
                    # Skip styles for now
                    # styles_spanners = styles_tbl[
                    #     (styles_tbl["locname"] == "columns_groups") &
                    #     (styles_tbl["grpname"] in spanners_vars)
                    # ]
                    #
                    # spanner_style = (
                    #     styles_spanners["html_style"].values[0]
                    #     if len(styles_spanners) > 0
                    #     else None
                    # )
                    spanner_style = None

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
                            style=spanner_style,
                            scope="colgroup" if colspan > 1 else "col",
                        )
                    )

            if len(stub_layout) > 0:
                level_i_spanners.insert(
                    0,
                    tags.th(
                        tags.span(HTML("&nbsp")),
                        class_=f"gt_col_heading gt_columns_bottom_border gt_{str(stubhead_label_alignment)}",
                        rowspan=1,
                        colspan=len(stub_layout),
                        scope="colgroup" if len(stub_layout) > 1 else "col",
                    ),
                )

            higher_spanner_rows = TagList(
                higher_spanner_rows,
                TagList(
                    tags.tr(
                        level_i_spanners,
                        class_="gt_col_headings gt_spanner_row",
                    )
                ),
            )

        table_col_headings = TagList(
            higher_spanner_rows,
            table_col_headings,
        )
    return str(table_col_headings)


def create_body_component_h(data: GTData) -> str:
    # for now, just coerce everything in the original data to a string
    # so we can fill in the body data with it
    _str_orig_data = cast_frame_to_string(data._tbl_data)
    tbl_data = replace_null_frame(data._body.body, _str_orig_data)

    # Filter list of StyleInfo to only those that apply to the body (where locname="data")
    styles_body = [x for x in data._styles if x.locname == "data"]

    # Get the default column vars
    column_vars = data._boxhead._get_default_columns()

    stub_var = data._boxhead._get_stub_column()

    stub_layout = data._stub._get_stub_layout(options=data._options)

    has_stub_column = "rowname" in stub_layout
    has_two_col_stub = "group_label" in stub_layout
    has_groups = data._stub.group_ids is not None and len(data._stub.group_ids) > 0

    # If there is a stub, then prepend that to the `column_vars` list
    if stub_var is not None:
        column_vars = [stub_var] + column_vars

    # Is the stub to be striped?
    table_stub_striped = data._options.row_striping_include_stub.value

    # Are the rows in the table body to be striped?
    table_body_striped = data._options.row_striping_include_table_body.value

    body_rows: list[str] = []

    # iterate over rows (ordered by groupings)
    prev_group_label = None

    ordered_index = data._stub.group_indices_map()

    for i, group_label in ordered_index:

        # For table striping we want to add a striping CSS class to the even-numbered
        # rows in the rendered table; to target these rows, determine if `i` in the current
        # row render is an odd number
        odd_i_row = i % 2 == 1

        body_cells: list[str] = []

        if has_stub_column and has_groups and not has_two_col_stub:
            colspan_value = data._boxhead._get_effective_number_of_columns(
                stub=data._stub, options=data._options
            )

            # Generate a row that contains the row group label (this spans the entire row) but
            # only if `i` indicates there should be a row group label
            if group_label != prev_group_label:
                group_class = (
                    "gt_empty_group_heading" if group_label == "" else "gt_group_heading_row"
                )

                group_row = f"""  <tr class="{group_class}">
    <th class="gt_group_heading" colspan="{colspan_value}">{group_label}</th>
  </tr>"""

                prev_group_label = group_label

                body_rows.append(group_row)

        # Create a single cell and append result to `body_cells`
        for colinfo in column_vars:
            cell_content: Any = _get_cell(tbl_data, i, colinfo.var)
            cell_str: str = str(cell_content)

            # Determine whether the current cell is the stub cell
            if has_stub_column:
                is_stub_cell = colinfo.var == stub_var.var
            else:
                is_stub_cell = False

            # Get alignment for the current column from the `col_alignment` list
            # by using the `name` value to obtain the index of the alignment value
            cell_alignment = colinfo.defaulted_align

            # Get the style attributes for the current cell by filtering the
            # `styles_body` list for the current row and column
            styles_i = [x for x in styles_body if x.rownum == i and x.colname == colinfo.var]

            # Develop the `style` attribute for the current cell
            if len(styles_i) > 0:
                # flatten all StyleInfo.styles lists
                style_entries = list(chain(*[x.styles for x in styles_i]))
                rendered_styles = [el._to_html_style() for el in style_entries]
                cell_styles = f'style="{" ".join(rendered_styles)}"' + " "
            else:
                cell_styles = ""

            if is_stub_cell:

                el_name = "th"

                classes = ["gt_row", "gt_left", "gt_stub"]

                if table_stub_striped and odd_i_row:
                    classes.append("gt_striped")

            else:

                el_name = "td"

                classes = ["gt_row", f"gt_{cell_alignment}"]

                if table_body_striped and odd_i_row:
                    classes.append("gt_striped")

            # Ensure that `classes` becomes a space-separated string
            classes = " ".join(classes)

            body_cells.append(
                f"""    <{el_name} {cell_styles}class="{classes}">{cell_str}</{el_name}>"""
            )

        prev_group_label = group_label
        body_rows.append("  <tr>\n" + "\n".join(body_cells) + "\n  </tr>")

    all_body_rows = "\n".join(body_rows)

    return f"""<tbody class="gt_table_body">
{all_body_rows}
</tbody>"""


def create_source_notes_component_h(data: GTData) -> str:
    source_notes = data._source_notes

    # If there are no source notes, then return an empty string
    if source_notes == []:
        return ""

    # Obtain the `multiline` and `separator` options from `_options`
    multiline = data._options.source_notes_multiline.value
    separator = cast(str, data._options.source_notes_sep.value)

    # Get the effective number of columns, which is number of columns
    # that will finally be rendered accounting for the stub layout
    n_cols_total = data._boxhead._get_effective_number_of_columns(
        stub=data._stub, options=data._options
    )

    # Handle the multiline source notes case (each note takes up one line)
    if multiline:
        # Create the source notes component as a series of `<tr><td>` (one per
        # source note) inside of a `<tfoot>`

        source_notes_tr: list[str] = []

        for note in source_notes:
            note_str = _process_text(note)

            source_notes_tr.append(
                f"""
  <tr>
    <td class="gt_sourcenote" colspan="{n_cols_total}">{note_str}</td>
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

    # Get all the widths for the columns as a list where None values mean that the width is
    # not set for that column
    # TODO: ensure that the stub column is set first in the list
    widths = data._boxhead._get_column_widths()

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
