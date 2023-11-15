from great_tables._spanners import spanners_print_matrix, seq_groups
from ._gt_data import GTData
from typing import List, Dict, Any
from htmltools import tags, HTML, css, TagList
from itertools import groupby, accumulate, chain
from functools import reduce
import pandas as pd


def create_columns_component_h(data: GTData) -> str:
    """
    Returns the HTML text fragment for the column/spanner labels.
    """

    # Should the column labels be hidden?
    column_labels_hidden: bool = data._options._get_option_value(option="column_labels_hidden")

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
    stub_layout = _get_stub_layout(data=data)

    # Determine the finalized number of spanner rows
    spanner_row_count = _get_spanners_matrix_height(data=data, omit_columns_row=True)

    # Get the column alignments and also the alignment class names
    col_alignment = data._boxhead._get_visible_alignments()

    # Replace None values in `col_alignment` with "left"
    col_alignment = ["left" if x == "None" else x for x in col_alignment]

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
    headings_vars = boxhead._get_visible_columns()
    headings_labels = boxhead._get_visible_column_labels()

    # TODO: Skipping styles for now
    # Get the style attrs for the stubhead label
    # stubhead_style_attrs = subset(styles_tbl, locname == "stubhead")
    # Get the style attrs for the spanner column headings
    # spanner_style_attrs = subset(styles_tbl, locname == "columns_groups")
    # Get the style attrs for the spanner column headings
    # column_style_attrs = subset(styles_tbl, locname == "columns_columns")

    # If columns are present in the stub, then replace with a set stubhead label or nothing
    if len(stub_layout) > 0 and len(stubh.stubhead) > 0:
        stub_label = stubh.stubhead
        stub_var = "::stub"
    else:
        stub_label = ""
        stub_var = "::stub"

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
                    HTML(stub_label),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{stubhead_label_alignment}",
                    rowspan="1",
                    colspan=len(stub_layout),
                    style=stubhead_style,
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    id=stub_label,
                )
            )

        #
        # Create the headings in the case where there are no spanners at all -------------------------
        col_entries = [
            (stub_var, stub_label, stubhead_label_alignment),
            *zip(headings_vars, headings_labels, col_alignment),
        ]
        for var_, label, alignment in col_entries:
            # NOTE: Ignore styles for now
            # styles_column = subset(column_style_attrs, colnum == i)
            #
            # Convert the code above this comment from R to valid python
            # if len(styles_column) > 0:
            #    column_style = styles_column[0].html_style
            column_style = None

            table_col_headings.append(
                tags.th(
                    HTML(label),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{str(alignment)}",
                    rowspan=1,
                    colspan=1,
                    style=column_style,
                    scope="col",
                    id=str(label),
                )
            )

        # Join the <th> cells into a string and separate each with a newline
        th_cells = "\n".join([str(tag) for tag in table_col_headings])

        table_col_headings = tags.tr(HTML(th_cells), class_="gt_col_headings")

    #
    # Create the spanners and column labels in the case where there *are* spanners -------------
    #

    if spanner_row_count >= 1:
        spanners, _ = spanners_print_matrix(
            spanners=data._spanners, boxhead=boxhead, include_hidden=False
        )

        spanner_ids, spanner_col_names = spanners_print_matrix(
            spanners=data._spanners, boxhead=boxhead, include_hidden=False, ids=True
        )

        level_1_index = 0

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
                    HTML(stub_label),
                    class_=f"gt_col_heading gt_columns_bottom_border gt_{str(stubhead_label_alignment)}",
                    rowspan=2,
                    colspan=len(stub_layout),
                    style=stubhead_style,
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    id=stub_label,
                )
            )

        # NOTE: Run-length encoding treats missing values as distinct from each other; in other
        # words, each missing value starts a new run of length 1

        spanner_ids_level_1_index = list(spanner_ids[level_1_index].values())
        spanners_rle = list(seq_groups(seq=list(spanner_ids_level_1_index)))

        # `colspans` matches `spanners` in length; each element is the number of columns that the
        # <th> at that position should span; if 0, then skip the <th> at that position
        group_spans = [[x[1]] + [0] * (x[1] - 1) for x in spanners_rle]

        colspans = list(chain(*group_spans))

        for ii, (span_key, h_var) in enumerate(zip(spanner_col_names, headings_vars)):
            if spanner_ids[level_1_index][span_key] is None:
                # NOTE: Ignore styles for now
                # styles_heading = filter(
                #     lambda x: x.get('locname') == "columns_columns" and x.get('colname') == headings_vars[i],
                #     styles_tbl if 'styles_tbl' in locals() else []
                # )
                #
                # heading_style = next(styles_heading, {}).get('html_style', None)
                heading_style = None

                # Get the alignment for the current column
                first_set_alignment = boxhead._get_boxhead_get_alignment_by_var(var=h_var)

                level_1_spanners.append(
                    tags.th(
                        class_=" ".join(
                            [
                                "gt_col_heading",
                                "gt_columns_bottom_border",
                                f"gt_{first_set_alignment}",
                            ]
                        ),
                        rowspan=2,
                        colspan=1,
                        style=heading_style,
                        scope="col",
                        id=headings_labels[i],
                        contents=HTML(headings_labels[i]),
                    )
                )

            elif spanner_ids[level_1_index][i] is not None:
                # If colspans[i] == 0, it means that a previous cell's
                # `colspan` will cover us
                if colspans[i] > 0:
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
                            class_=" ".join(
                                ["gt_center", "gt_columns_top_border", "gt_column_spanner_outer"]
                            ),
                            rowspan=1,
                            colspan=colspans[i],
                            style=spanner_style,
                            scope="colgroup" if colspans[i] > 1 else "col",
                            id=str(spanners[level_1_index][i]),
                            contents=str(
                                tags.span(
                                    class_="gt_column_spanner",
                                    contents=HTML(spanners[level_1_index][i]),
                                )
                            ),
                        )
                    )

        solo_headings = headings_vars[pd.isna(spanner_ids[level_1_index])]
        remaining_headings = headings_vars[~(headings_vars.isin(solo_headings))]

        remaining_headings_labels = boxhead
        remaining_headings_labels = remaining_headings_labels[
            remaining_headings_labels["var"].isin(remaining_headings)
        ]
        remaining_headings_labels = remaining_headings_labels["column_label"].tolist()

        col_alignment = col_alignment[1:][~(headings_vars.isin(solo_headings))]

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
                        class_=" ".join(
                            [
                                "gt_col_heading",
                                "gt_columns_bottom_border",
                                f"gt_{remaining_alignment}",
                            ]
                        ),
                        rowspan=1,
                        colspan=1,
                        style=remaining_style,
                        scope="col",
                        id=remaining_headings_labels[j],
                        contents=HTML(remaining_headings_labels[j]),
                    )
                )

            table_col_headings = tags.tagList(
                tags.tr(level_1_spanners, class_="gt_col_headings gt_spanner_row"),
                tags.tr(spanned_column_labels, class_="gt_col_headings"),
            )

        else:
            # Create the `table_col_headings` HTML component
            table_col_headings = tags.tr(
                class_="gt_col_headings gt_spanner_row", contents=level_1_spanners
            )

    if _get_spanners_matrix_height(data=data) > 2:
        higher_spanner_rows_idx = seq_len(nrow(spanner_ids) - 2)

        higher_spanner_rows = tags.tagList()

        for i in higher_spanner_rows_idx:
            spanner_ids_row = spanner_ids[i]
            spanners_row = spanners[i]
            spanners_vars = list(set(spanner_ids_row[~np.isnan(spanner_ids_row)].tolist()))

            # Replace NA values in spanner_ids_row with an empty string
            spanner_ids_row[np.isnan(spanner_ids_row)] = ""

            spanners_rle = [(k, len(list(g))) for k, g in groupby(list(spanner_ids_row))]

            sig_cells = [1] + [
                i + 1
                for i, (k, _) in enumerate(spanners_rle[:-1])
                if k is None or k != spanners_rle[i - 1][0]
            ]

            colspans = [
                spanners_rle[j][1] if (j + 1) in sig_cells else 0
                for j in range(len(spanner_ids_row))
            ]

            level_i_spanners = []

            for j in range(len(colspans)):
                if colspans[j] > 0:
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

                    level_i_spanners.append(
                        tags.th(
                            class_=" ".join(
                                ["gt_center", "gt_columns_top_border", "gt_column_spanner_outer"]
                            ),
                            rowspan=1,
                            colspan=colspans[j],
                            style=spanner_style,
                            scope="colgroup" if colspans[j] > 1 else "col",
                            contents=tags.tagList(
                                tags.span(contents=HTML(spanners_row[j])),
                                tags.span(
                                    class_="gt_column_spanner_inner", contents=HTML("&nbsp;")
                                ),
                            ),
                        )
                    )

            if len(stub_layout) > 0 and i == 1:
                level_i_spanners = tags.th(
                    rowspan=max(list(higher_spanner_rows_idx)),
                    colspan=len(stub_layout),
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    contents=tags.tagList(level_i_spanners),
                )

            higher_spanner_rows = tags.tagList(
                higher_spanner_rows,
                tags.tagList(tags.tr(level_i_spanners, class_="gt_col_headings gt_spanner_row")),
            )

        table_col_headings = tags.tagList(
            higher_spanner_rows,
            table_col_headings,
        )

    return str(table_col_headings)


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


def _collapse_list_elements(lst, separator=""):
    """
    Concatenates all elements of a list into a single string, separated by a given separator.

    Args:
        lst (list): The list to be collapsed.
        separator (str, optional): The separator to be used. Defaults to "".

    Returns:
        str: The collapsed string.
    """
    return separator.join(lst)


def _insert_into_list(lst: List[Any], el: Any) -> List[Any]:
    """
    Inserts an element into the beginning of a list and returns the updated list.

    Args:
        lst (List[Any]): The list to insert the element into.
        el (Any): The element to insert.

    Returns:
        List[Any]: The updated list with the element inserted at the beginning.
    """
    lst.insert(0, el)
    return lst


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


# Determine whether the table has any row labels or row groups defined and provide
# a simple list that contains at a maximum two components
def _get_stub_components(data: GTData):
    # TODO: we should be using `row_id` instead of `rowname`
    # Obtain the object that describes the table stub
    tbl_stub = data._stub

    # Get separate lists of `group_id` and `row_id` values from the `_stub` object
    group_id_vals = [tbl_stub[i].group_id for i in range(len(tbl_stub))]
    rowname_vals = [tbl_stub[i].rowname for i in range(len(tbl_stub))]

    stub_components: list[str] = []

    if any(x is not None for x in group_id_vals):
        stub_components.append("group_id")

    if any(x is not None for x in rowname_vals):
        stub_components.append("row_id")

    return stub_components


def _get_stub_layout(data: GTData) -> List[str]:
    # Determine which stub components are potentially present as columns
    stub_rownames_is_column = _stub_rownames_has_column(data=data)
    stub_groupnames_is_column = _stub_group_names_has_column(data=data)

    # Get the potential total number of columns in the table stub
    n_stub_cols = stub_rownames_is_column + stub_groupnames_is_column

    # Resolve the layout of the stub (i.e., the roles of columns if present)
    if n_stub_cols == 0:
        # If summary rows are present, we will use the `rowname` column
        # for the summary row labels
        if _summary_exists(data=data):
            stub_layout = ["rowname"]
        else:
            stub_layout = []

    else:
        stub_layout = [
            label
            for label, condition in [
                ("group_label", stub_groupnames_is_column),
                ("rowname", stub_rownames_is_column),
            ]
            if condition
        ]

    return stub_layout


# Determine whether the table should have row labels set within a column in the stub
def _stub_rownames_has_column(data: GTData) -> bool:
    return "row_id" in _get_stub_components(data=data)


# Determine whether the table should have row group labels set within a column in the stub
def _stub_group_names_has_column(data: GTData) -> bool:
    # If there aren't any row groups then the result is always False
    if len(_row_groups_get(data=data)) < 1:
        return False

    # Given that there are row groups, we need to look at the option `row_group_as_column` to
    # determine whether they populate a column located in the stub; if set as True then that's
    # the return value
    row_group_as_column = data._options._get_option_value(option="row_group_as_column")

    row_group_as_column: Any
    if not isinstance(row_group_as_column, bool):
        raise TypeError("Variable type mismatch. Expected bool, got something entirely different.")

    return row_group_as_column


def _row_groups_get(data: GTData) -> List[str]:
    return data._row_groups._d


def _summary_exists(data: GTData):
    return False


# Get the attributes needed for the <table> tag
def _get_table_defs(data: GTData):
    # Get the `table-layout` value, which is set in `_options`
    table_layout = data._options._get_option_value(option="table_layout")
    table_style = f"table-layout: {table_layout};"

    # Get the number of columns that have a width set
    n_column_width = len(data._boxhead._get_column_widths())

    # In the case that column widths are not set for any columns,
    # there should not be a `<colgroup>` tag requirement
    if n_column_width < 1:
        return dict(table_style=None, table_colgroups=None)

    # Get the table's width (which or may not have been set)
    table_width = data._options._get_option_value(option="table_width")

    # Get all the widths for the columns as a list where None values mean
    # that the width is not set for that column
    # TODO: ensure that the stub column is set first in the list
    widths = data._boxhead._get_column_widths()

    # If all of the widths are defined as px values for all columns,
    # then ensure that the width values are strictly respected as
    # absolute width values (even if a table width has already been set)
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

    return dict(table_style=table_style, table_colgroups=table_colgroups)
