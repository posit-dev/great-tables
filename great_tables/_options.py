from __future__ import annotations
from dataclasses import replace
from typing import TYPE_CHECKING, Optional, Union, List, cast
from great_tables import _utils


if TYPE_CHECKING:
    from ._types import GTSelf


def tab_options(
    self: GTSelf,
    container_width: Optional[str] = None,
    container_height: Optional[str] = None,
    container_overflow_x: Optional[str] = None,
    container_overflow_y: Optional[str] = None,
    table_width: Optional[str] = None,
    table_layout: Optional[str] = None,
    # table_align: Optional[str] = None,
    table_margin_left: Optional[str] = None,
    table_margin_right: Optional[str] = None,
    table_background_color: Optional[str] = None,
    # table_additional_css: Optional[str] = None,
    table_font_names: Optional[Union[str, List[str]]] = None,
    table_font_size: Optional[str] = None,
    table_font_weight: Optional[str] = None,
    table_font_style: Optional[str] = None,
    table_font_color: Optional[str] = None,
    table_font_color_light: Optional[str] = None,
    table_border_top_style: Optional[str] = None,
    table_border_top_width: Optional[str] = None,
    table_border_top_color: Optional[str] = None,
    table_border_bottom_style: Optional[str] = None,
    table_border_bottom_width: Optional[str] = None,
    table_border_bottom_color: Optional[str] = None,
    table_border_left_style: Optional[str] = None,
    table_border_left_width: Optional[str] = None,
    table_border_left_color: Optional[str] = None,
    table_border_right_style: Optional[str] = None,
    table_border_right_width: Optional[str] = None,
    table_border_right_color: Optional[str] = None,
    heading_background_color: Optional[str] = None,
    heading_align: Optional[str] = None,
    heading_title_font_size: Optional[str] = None,
    heading_title_font_weight: Optional[str] = None,
    heading_subtitle_font_size: Optional[str] = None,
    heading_subtitle_font_weight: Optional[str] = None,
    heading_padding: Optional[str] = None,
    heading_padding_horizontal: Optional[str] = None,
    heading_border_bottom_style: Optional[str] = None,
    heading_border_bottom_width: Optional[str] = None,
    heading_border_bottom_color: Optional[str] = None,
    heading_border_lr_style: Optional[str] = None,
    heading_border_lr_width: Optional[str] = None,
    heading_border_lr_color: Optional[str] = None,
    column_labels_background_color: Optional[str] = None,
    column_labels_font_size: Optional[str] = None,
    column_labels_font_weight: Optional[str] = None,
    column_labels_text_transform: Optional[str] = None,
    column_labels_padding: Optional[str] = None,
    column_labels_padding_horizontal: Optional[str] = None,
    column_labels_vlines_style: Optional[str] = None,
    column_labels_vlines_width: Optional[str] = None,
    column_labels_vlines_color: Optional[str] = None,
    column_labels_border_top_style: Optional[str] = None,
    column_labels_border_top_width: Optional[str] = None,
    column_labels_border_top_color: Optional[str] = None,
    column_labels_border_bottom_style: Optional[str] = None,
    column_labels_border_bottom_width: Optional[str] = None,
    column_labels_border_bottom_color: Optional[str] = None,
    column_labels_border_lr_style: Optional[str] = None,
    column_labels_border_lr_width: Optional[str] = None,
    column_labels_border_lr_color: Optional[str] = None,
    column_labels_hidden: Optional[bool] = None,
    row_group_background_color: Optional[str] = None,
    row_group_font_size: Optional[str] = None,
    row_group_font_weight: Optional[str] = None,
    row_group_text_transform: Optional[str] = None,
    row_group_padding: Optional[str] = None,
    row_group_padding_horizontal: Optional[str] = None,
    row_group_border_top_style: Optional[str] = None,
    row_group_border_top_width: Optional[str] = None,
    row_group_border_top_color: Optional[str] = None,
    row_group_border_bottom_style: Optional[str] = None,
    row_group_border_bottom_width: Optional[str] = None,
    row_group_border_bottom_color: Optional[str] = None,
    row_group_border_left_style: Optional[str] = None,
    row_group_border_left_width: Optional[str] = None,
    row_group_border_left_color: Optional[str] = None,
    row_group_border_right_style: Optional[str] = None,
    row_group_border_right_width: Optional[str] = None,
    row_group_border_right_color: Optional[str] = None,
    # row_group_default_label: Optional[str] = None,
    row_group_as_column: Optional[bool] = None,
    table_body_hlines_style: Optional[str] = None,
    table_body_hlines_width: Optional[str] = None,
    table_body_hlines_color: Optional[str] = None,
    table_body_vlines_style: Optional[str] = None,
    table_body_vlines_width: Optional[str] = None,
    table_body_vlines_color: Optional[str] = None,
    table_body_border_top_style: Optional[str] = None,
    table_body_border_top_width: Optional[str] = None,
    table_body_border_top_color: Optional[str] = None,
    table_body_border_bottom_style: Optional[str] = None,
    table_body_border_bottom_width: Optional[str] = None,
    table_body_border_bottom_color: Optional[str] = None,
    stub_background_color: Optional[str] = None,
    stub_font_size: Optional[str] = None,
    stub_font_weight: Optional[str] = None,
    stub_text_transform: Optional[str] = None,
    stub_border_style: Optional[str] = None,
    stub_border_width: Optional[str] = None,
    stub_border_color: Optional[str] = None,
    stub_row_group_font_size: Optional[str] = None,
    stub_row_group_font_weight: Optional[str] = None,
    stub_row_group_text_transform: Optional[str] = None,
    stub_row_group_border_style: Optional[str] = None,
    stub_row_group_border_width: Optional[str] = None,
    stub_row_group_border_color: Optional[str] = None,
    data_row_padding: Optional[str] = None,
    data_row_padding_horizontal: Optional[str] = None,
    # summary_row_background_color: Optional[str] = None,
    # summary_row_text_transform: Optional[str] = None,
    # summary_row_padding: Optional[str] = None,
    # summary_row_padding_horizontal: Optional[str] = None,
    # summary_row_border_style: Optional[str] = None,
    # summary_row_border_width: Optional[str] = None,
    # summary_row_border_color: Optional[str] = None,
    # grand_summary_row_background_color: Optional[str] = None,
    # grand_summary_row_text_transform: Optional[str] = None,
    # grand_summary_row_padding: Optional[str] = None,
    # grand_summary_row_padding_horizontal: Optional[str] = None,
    # grand_summary_row_border_style: Optional[str] = None,
    # grand_summary_row_border_width: Optional[str] = None,
    # grand_summary_row_border_color: Optional[str] = None,
    # footnotes_background_color: Optional[str] = None,
    # footnotes_font_size: Optional[str] = None,
    # footnotes_padding: Optional[str] = None,
    # footnotes_padding_horizontal: Optional[str] = None,
    # footnotes_border_bottom_style: Optional[str] = None,
    # footnotes_border_bottom_width: Optional[str] = None,
    # footnotes_border_bottom_color: Optional[str] = None,
    # footnotes_border_lr_style: Optional[str] = None,
    # footnotes_border_lr_width: Optional[str] = None,
    # footnotes_border_lr_color: Optional[str] = None,
    # footnotes_marks: Optional[Union[str, List[str]]] = None,
    # footnotes_multiline: Optional[bool] = None,
    # footnotes_sep: Optional[str] = None,
    source_notes_background_color: Optional[str] = None,
    source_notes_font_size: Optional[str] = None,
    source_notes_padding: Optional[str] = None,
    source_notes_padding_horizontal: Optional[str] = None,
    source_notes_border_bottom_style: Optional[str] = None,
    source_notes_border_bottom_width: Optional[str] = None,
    source_notes_border_bottom_color: Optional[str] = None,
    source_notes_border_lr_style: Optional[str] = None,
    source_notes_border_lr_width: Optional[str] = None,
    source_notes_border_lr_color: Optional[str] = None,
    source_notes_multiline: Optional[bool] = None,
    source_notes_sep: Optional[str] = None,
    # row_striping_background_color: Optional[str] = None,
    # row_striping_include_stub: Optional[bool] = None,
    # row_striping_include_table_body: Optional[bool] = None,
) -> GTSelf:
    """
    Modify the table output options.

    Modify the options available in a table. These options are named by the components, the
    subcomponents, and the element that can adjusted.

    Parameters
    ----------
    container_width : str
        The width of the table's container. Can be specified as a single-length
        character with units of pixels or as a percentage. If provided as a scalar numeric
        value, it is assumed that the value is given in units of pixels.
    container_height: str
        The height of the table's container.
    container_overflow_x : bool
        An option to enable scrolling in the horizontal direction when the table content overflows
        the container dimensions. Using `True` (the default) means that horizontal scrolling is
        enabled to view the entire table in those directions. With `False`, the table may be clipped
        if the table width or height exceeds the `container_width`.
    container_overflow_y : bool
        An option to enable scrolling in the vertical direction when the table content overflows.
        Same rules apply as for `container_overflow_x`; the dependency here is that of the table
        height (`container_height`).
    table_width : str
        The width of the table. Can be specified as a string with units of pixels or as a
        percentage. If provided as a numeric value, it is assumed that the value is given in
        units of pixels.
    table_layout : str
        The value for the `table-layout` CSS style in the HTML output context. By default, this
        is `"fixed"` but another valid option is `"auto"`.
    table_margin_left : str
        The size of the margins on the left of the table within the container. Can be
        specified as a single-length value with units of pixels or as a percentage. If
        provided as a numeric value, it is assumed that the value is given in units of pixels.
        Using `table_margin_left` will overwrite any values set by `table_align`.
    table_margin_right : str
        The size of the margins on the right of the table within the container. Same rules apply
        as for `table_margin_left`. Using `table_margin_right` will overwrite any values set by
        `table_align`.
    table_background_color : str
        The background color for the table. A color name or a hexadecimal color code should be
        provided.
    table_font_names : Union[str, List[str]]
        The names of the fonts used for the table. This should be provided as a list of font
        names. If the first font isn't available, then the next font is tried (and so on).
    table_font_size : str
        The font size for the table. Can be specified as a string with units of pixels or as a
        percentage. If provided as a numeric value, it is assumed that the value is given in
        units of pixels.
    table_font_weight : str
        The font weight of the table. Can be a text-based keyword such as `"normal"`, `"bold"`,
        `"lighter"`, `"bolder"`, or, a numeric value between `1` and `1000`, inclusive. Note that
        only variable fonts may support the numeric mapping of weight.
    table_font_style : str
        The font style for the table. Can be one of either `"normal"`, `"italic"`, or `"oblique"`.
    table_font_color : str
        The text color used throughout the table. A color name or a hexadecimal color code should be
        provided.
    table_font_color_light : str
        The text color used throughout the table when the background color is dark. A color name or
        a hexadecimal color code should be provided.
    table_border_top_style : str
        The style of the table's absolute top border. Can be one of either `"solid"`, `"dotted"`,
        `"dashed"`, `"double"`, `"groove"`, `"ridge"`, `"inset"`, or `"outset"`.
    table_border_top_width : str
        The width of the table's absolute top border. Can be specified as a string with units of
        pixels or as a percentage. If provided as a numeric value, it is assumed that the value is
        given in units of pixels.
    table_border_top_color : str
        The color of the table's absolute top border. A color name or a hexadecimal color code
        should be provided.
    table_border_bottom_style : str
        The style of the table's absolute bottom border.
    table_border_bottom_width : str
        The width of the table's absolute bottom border.
    table_border_bottom_color : str
        The color of the table's absolute bottom border.
    table_border_left_style : str
        The style of the table's absolute left border.
    table_border_left_width : str
        The width of the table's absolute left border.
    table_border_left_color : str
        The color of the table's absolute left border.
    table_border_right_style : str
        The style of the table's absolute right border.
    table_border_right_width : str
        The width of the table's absolute right border.
    table_border_right_color : str
        The color of the table's absolute right border.
    heading_background_color : str
        The background color for the heading. A color name or a hexadecimal color code should be
        provided.
    heading_align : str
        Controls the horizontal alignment of the heading title and subtitle. We can either use
        `"center"`, `"left"`, or `"right"`.
    heading_title_font_size : str
        The font size for the heading title element.
    heading_title_font_weight : str
        The font weight of the heading title.
    heading_subtitle_font_size : str
        The font size for the heading subtitle element.
    heading_subtitle_font_weight : str
        The font weight of the heading subtitle.
    heading_padding : str
        The amount of vertical padding to incorporate in the `heading` (title and subtitle). Can be
        specified as a string with units of pixels or as a percentage. If provided as a numeric
        value, it is assumed that the value is given in units of pixels.
    heading_padding_horizontal : str
        The amount of horizontal padding to incorporate in the `heading` (title and subtitle). Can
        be specified as a string with units of pixels or as a percentage. If provided as a numeric
        value, it is assumed that the value is given in units of pixels.
    heading_border_bottom_style : str
        The style of the header's bottom border.
    heading_border_bottom_width : str
        The width of the header's bottom border. If the `width` of this border is larger, then it
        will be the visible border.
    heading_border_bottom_color : str
        The color of the header's bottom border.
    heading_border_lr_style : str
        The style of the left and right borders of the `heading` location.
    heading_border_lr_width : str
        The width of the left and right borders of the `heading` location. If the `width` of this
        border is larger, then it will be the visible border.
    heading_border_lr_color : str
        The color of the left and right borders of the `heading` location.
    column_labels_background_color : str
        The background color for the column labels. A color name or a hexadecimal color code should
        be provided.
    column_labels_font_size : str
        The font size to use for all column labels.
    column_labels_font_weight : str
        The font weight of the table's column labels.
    column_labels_text_transform : str
        The text transformation for the column labels. Either of the `"uppercase"`, `"lowercase"`,
        or `"capitalize"` keywords can be used.
    column_labels_padding : str
        The amount of vertical padding to incorporate in the `column_labels` (this includes the
        column spanners).
    column_labels_padding_horizontal : str
        The amount of horizontal padding to incorporate in the `column_labels` (this includes the
        column spanners).
    column_labels_vlines_style : str
        The style of all vertical lines ('vlines') of the `column_labels`.
    column_labels_vlines_width : str
        The width of all vertical lines ('vlines') of the `column_labels`.
    column_labels_vlines_color : str
        The color of all vertical lines ('vlines') of the `column_labels`.
    column_labels_border_top_style : str
        The style of the top border of the `column_labels` location.
    column_labels_border_top_width : str
        The width of the top border of the `column_labels` location. If the `width` of this border
        is larger, then it will be the visible border.
    column_labels_border_top_color : str
        The color of the top border of the `column_labels` location.
    column_labels_border_bottom_style : str
        The style of the bottom border of the `column_labels` location.
    column_labels_border_bottom_width : str
        The width of the bottom border of the `column_labels` location. If the `width` of this
        border is larger, then it will be the visible border.
    column_labels_border_bottom_color : str
        The color of the bottom border of the `column_labels` location.
    column_labels_border_lr_style : str
        The style of the left and right borders of the `column_labels` location.
    column_labels_border_lr_width: str
        The width of the left and right borders of the `column_labels` location. If the `width` of
        this border is larger, then it will be the visible border.
    column_labels_border_lr_color : str
        The color of the left and right borders of the `column_labels` location.
    column_labels_hidden : bool
        An option to hide the column labels. If providing `True` then the entire `column_labels`
        location won't be seen and the table header (if present) will collapse downward.
    row_group_background_color : str
        The background color for the row group labels. A color name or a hexadecimal color code
        should be provided.
    row_group_font_weight : str
        The font weight for all row group labels present in the table.
    row_group_font_size : str
        The font size to use for all row group labels.
    row_group_padding : str
        The amount of vertical padding to incorporate in the row group labels.
    row_group_border_top_style : str
        The style of the top border of the `row_group` location.
    row_group_border_top_width : str
        The width of the top border of the `row_group` location. If the `width` of this border is
        larger, then it will be the visible border.
    row_group_border_top_color : str
        The color of the top border of the `row_group` location.
    row_group_border_bottom_style : str
        The style of the bottom border of the `row_group` location.
    row_group_border_bottom_width : str
        The width of the bottom border of the `row_group` location. If the `width` of this border
        is larger, then it will be the visible border.
    row_group_border_bottom_color : str
        The color of the bottom border of the `row_group` location.
    row_group_border_left_style : str
        The style of the left border of the `row_group` location.
    row_group_border_left_width : str
        The width of the left border of the `row_group` location. If the `width` of this border is
        larger, then it will be the visible border.
    row_group_border_left_color : str
        The color of the left border of the `row_group` location.
    row_group_border_right_style : str
        The style of the right border of the `row_group` location.
    row_group_border_right_width : str
        The width of the right border of the `row_group` location. If the `width` of this border is
    row_group_border_right_color : str
        The color of the right border of the `row_group` location.
    row_group_as_column : bool
        An option to render the row group labels as a column. If `True`, then the row group labels
        will be rendered as a column to the left of the table body. If `False`, then the row group
        labels will be rendered as a separate row above the grouping of rows.
    table_body_hlines_style : str
        The style of all horizontal lines ('hlines') in the `table_body`.
    table_body_hlines_width : str
        The width of all horizontal lines ('hlines') in the `table_body`.
    table_body_hlines_color : str
        The color of all horizontal lines ('hlines') in the `table_body`.
    table_body_vlines_style : str
        The style of all vertical lines ('vlines') in the `table_body`.
    table_body_vlines_width : str
        The width of all vertical lines ('vlines') in the `table_body`.
    table_body_vlines_color : str
        The color of all vertical lines ('vlines') in the `table_body`.
    table_body_border_top_style : str
        The style of the top border of the `table_body` location.
    table_body_border_top_width : str
        The width of the top border of the `table_body` location. If the `width` of this border is
        larger, then it will be the visible border.
    table_body_border_top_color : str
        The color of the top border of the `table_body` location.
    table_body_border_bottom_style : str
        The style of the bottom border of the `table_body` location.
    table_body_border_bottom_width : str
        The width of the bottom border of the `table_body` location. If the `width` of this border
    table_body_border_bottom_color : str
        The color of the bottom border of the `table_body` location.
    stub_background_color : str
        The background color for the stub. A color name or a hexadecimal color code should be
        provided.
    stub_font_size : str
        The font size to use for all row labels present in the table stub.
    stub_font_weight : str
        The font weight for all row labels present in the table stub.
    stub_text_transform : str
        The text transformation for the row labels present in the table stub.
    stub_border_style : str
        The style of the vertical border of the table stub.
    stub_border_width : str
        The width of the vertical border of the table stub.
    stub_border_color : str
        The color of the vertical border of the table stub.
    stub_row_group_font_size : str
        The font size for the row group column in the stub.
    stub_row_group_font_weight : str
        The font weight for the row group column in the stub.
    stub_row_group_text_transform : str
        The text transformation for the row group column in the stub.
    stub_row_group_border_style : str
        The style of the vertical border of the row group column in the stub.
    stub_row_group_border_width : str
        The width of the vertical border of the row group column in the stub.
    stub_row_group_border_color : str
        The color of the vertical border of the row group column in the stub.
    data_row_padding : str
        The amount of vertical padding to incorporate in the body/stub rows.
    data_row_padding_horizontal : str
        The amount of horizontal padding to incorporate in the body/stub rows.
    source_notes_background_color : str
        The background color for the source notes. A color name or a hexadecimal color code should
        be provided.
    source_notes_font_size : str
        The font size to use for all source note text.
    source_notes_padding : str
        The amount of vertical padding to incorporate in the source notes.
    source_notes_padding_horizontal : str
        The amount of horizontal padding to incorporate in the source notes.
    source_notes_multiline : bool
        An option to either put source notes in separate lines (the default, or `True`) or render
        them as a continuous line of text with `source_notes_sep` providing the separator (by
        default `" "`) between notes.
    source_notes_sep : str
        The separating characters between adjacent source notes when rendered as a continuous line
        of text (when `source_notes_multiline` is `False`). The default value is a single space
        character (`" "`).
    source_notes_border_bottom_style : str
        The style of the bottom border of the `source_notes` location.
    source_notes_border_bottom_width : str
        The width of the bottom border of the `source_notes` location. If the `width` of this border
        is larger, then it will be the visible border.
    source_notes_border_bottom_color : str
        The color of the bottom border of the `source_notes` location.
    source_notes_border_lr_style : str
        The style of the left and right borders of the `source_notes` location.
    source_notes_border_lr_width : str
        The width of the left and right borders of the `source_notes` location. If the `width` of
        this border is larger, then it will be the visible border.
    source_notes_border_lr_color : str
        The color of the left and right borders of the `source_notes` location.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using select columns from the `exibble` dataset, let's create a new table with a number of table
    components added. We can use this object going forward to demonstrate some of the features
    available in the `tab_options()` method.

    ```{python}
    from great_tables import GT, exibble, md

    gt_tbl = (
      GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
      )
      .tab_header(
        title=md("Data listing from **exibble**"),
        subtitle=md("`exibble` is a **Great Tables** dataset.")
      )
      .fmt_number(columns="num")
      .fmt_currency(columns="currency")
      .tab_source_note(source_note="This is only a subset of the dataset.")
    )

    gt_tbl
    ```

    We can modify the table width to be set as `"100%`". In effect, this spans the table to entirely
    fill the content width area. This is done with the `table_width` option.

    ```{python}
    gt_tbl.tab_options(table_width="100%")
    ```

    With the `table_background_color` option, we can modify the table's background color. Here, we
    want that to be `"lightcyan"`.

    ```{python}
    gt_tbl.tab_options(table_background_color="lightcyan")
    ```

    The data rows of a table typically take up the most physical space but we have some control over
    the extent of that. With the `data_row_padding` option, it's possible to modify the top and
    bottom padding of data rows. We'll do just that in the following example, reducing the padding
    to a value of `"3px"`.

    ```{python}
    gt_tbl.tab_options(data_row_padding="3px")
    ```

    The size of the title and the subtitle text in the header of the table can be altered with the
    `heading_title_font_size` and `heading_subtitle_font_size` options. Here, we'll use the
    `"small"` and `"x-small"` keyword values.

    ```{python}
    gt_tbl.tab_options(heading_title_font_size="small", heading_subtitle_font_size="x-small")
    ```
    """
    saved_args = locals()

    del saved_args["self"]

    modified_args = {k: v for k, v in saved_args.items() if v is not None}

    # Intercept modified args and modify before replacing options:
    # - `table_font_names` should be a list but if given as a string, ensure it is list
    if "table_font_names" in modified_args:
        if isinstance(modified_args["table_font_names"], str):
            modified_args["table_font_names"] = [modified_args["table_font_names"]]

    new_options_info = {
        k: replace(getattr(self._options, k), value=v) for k, v in modified_args.items()
    }
    new_options = replace(self._options, **new_options_info)

    return self._replace(_options=new_options)


def opt_footnote_marks(self: GTSelf, marks: Union[str, List[str]] = "numbers") -> GTSelf:
    """
    Option to modify the set of footnote marks
    Alter the footnote marks for any footnotes that may be present in the table. Either a list
    of marks can be provided (including Unicode characters), or, a specific keyword could be
    used to signify a preset sequence. This method serves as a shortcut for using
    `tab_options(footnotes_marks=<marks>)`

    We can supply a list of strings will represent the series of marks. The series of footnote
    marks is recycled when its usage goes beyond the length of the set. At each cycle, the marks
    are simply doubled, tripled, and so on (e.g., `*` -> `**` -> `***`). The option exists for
    providing keywords for certain types of footnote marks. The keywords are

    - `"numbers"`: numeric marks, they begin from 1 and these marks are not subject to recycling
    behavior
    - `"letters"`: lowercase alphabetic marks. Same as using the `gt.letters()` function which
    produces a list of 26 lowercase letters from the Roman alphabet
    - `"LETTERS"`: uppercase alphabetic marks. Same as using the `gt.LETTERS()` function which
    produces a list of 26 uppercase letters from the Roman alphabet
    - `"standard"`: symbolic marks, four symbols in total
    - `"extended"`: symbolic marks, extends the standard set by adding two more symbols, making
    six

    Parameters
    ----------
    marks : Union[str, List[str]]
        Either a list of strings that will represent the series of marks or a keyword string
        that represents a preset sequence of marks. The valid keywords are: `"numbers"` (for
        numeric marks), `"letters"` and `"LETTERS"` (for lowercase and uppercase alphabetic
        marks), `"standard"` (for a traditional set of four symbol marks), and `"extended"`
        (which adds two more symbols to the standard set).

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.
    """
    # Validate the marks keyword passed in as a string
    if marks is str:
        marks = _utils._match_arg(
            x=cast(str, marks),
            lst=["numbers", "letters", "LETTERS", "standard", "extended"],
        )

    return tab_options(self, footnotes_marks=marks)


def opt_row_striping(self: GTSelf, row_striping: bool = True) -> GTSelf:
    """
    Option to add or remove row striping.

    By default, a gt*table does not have row striping enabled. However, this method allows us to
    easily enable or disable striped rows in the table body. It's a convenient shortcut for
    `gt.tab_options(row_striping_include_table_body=<True|False>)`.

    Parameters
    ----------
    row_striping : bool
        A boolean that indicates whether row striping should be added or removed. Defaults to
        `True`.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.
    """
    return tab_options(self, row_striping_include_table_body=row_striping)


def opt_align_table_header(self: GTSelf, align: str = "center") -> GTSelf:
    """
    Option to align the table header.

    By default, an added table header will have center alignment for both the title and the subtitle
    elements. This method allows us to easily set the horizontal alignment of the title and subtitle
    to the left, right, or center by using the `"align"` argument. This method serves as a
    convenient shortcut for `gt.tab_options(heading_align=<align>)`.

    Parameters
    ----------
    align : str
        The alignment of the title and subtitle elements in the table header. Options are `"center"`
        (the default), `"left"`, or `"right"`.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using select columns from the `exibble` dataset, let's create a table with a number of
    components added. Following that, we'll align the header contents (consisting of the title and
    the subtitle) to the left with the `opt_align_table_header()` method.

    ```{python}
    from great_tables import GT, exibble, md

    (
      GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
      )
      .tab_header(
        title=md("Data listing from **exibble**"),
        subtitle=md("`exibble` is a **Great Tables** dataset.")
      )
      .fmt_number(columns="num")
      .fmt_currency(columns="currency")
      .tab_source_note(source_note="This is only a subset of the dataset.")
      .opt_align_table_header(align="left")
    )
    ```
    """

    align = _utils._match_arg(x=align, lst=["left", "center", "right"])

    return tab_options(self, heading_align=align)


def opt_vertical_padding(self: GTSelf, scale: float = 1.0) -> GTSelf:
    """
    Option to scale the vertical padding of the table.

    This method allows us to scale the vertical padding of the table by a factor of `scale`. The
    default value is `1.0` and this method serves as a convenient shortcut for
    `gt.tab_options(heading_padding=<new_val>, column_labels_padding=<new_val>,
    data_row_padding=<new_val>, row_group_padding=<new_val>, source_notes_padding=<new_val>)`.

    Parameters
    ----------
    scale : float
        The factor by which to scale the vertical padding. The default value is `1.0`. A value
        less than `1.0` will reduce the padding, and a value greater than `1.0` will increase the
        padding. The value must be between `0` and `3`.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using select columns from the `exibble` dataset, let's create a table with a number of
    components added. Following that, we'll scale the vertical padding of the table by a factor of
    `3` using the `opt_vertical_padding()` method.

    ```{python}
    from great_tables import GT, exibble, md

    gt_tbl = (
        GT(
            exibble[["num", "char", "currency", "row", "group"]],
            rowname_col="row",
            groupname_col="group"
        )
        .tab_header(
            title=md("Data listing from **exibble**"),
            subtitle=md("`exibble` is a **Great Tables** dataset.")
        )
        .fmt_number(columns="num")
        .fmt_currency(columns="currency")
        .tab_source_note(source_note="This is only a subset of the dataset.")
    )

    gt_tbl.opt_vertical_padding(scale=3)
    ```

    Now that's a tall table! The overall effect of scaling the vertical padding is that the table
    will appear taller and there will be more buffer space between the table elements. A value of
    `3` is pretty extreme and is likely to be too much in most cases, so, feel free to experiment
    with different values when looking to increase the vertical padding.

    Let's go the other way (using a value less than `1`) and try to condense the content vertically
    with a `scale` factor of `0.5`. This will reduce the top and bottom padding globally and make
    the table appear more compact.

    ```{python}
    gt_tbl.opt_vertical_padding(scale=0.5)
    ```

    A value of `0.5` provides a reasonable amount of vertical padding and the table will appear more
    compact. This is useful when space is limited and, in such a situation, this is a practical
    solution to that problem.
    """

    # Stop if `scale` is beyond an acceptable range
    if scale < 0 or scale > 3:
        raise ValueError("`scale` must be a value between `0` and `3`.")

    # Get the parameters from the options that relate to vertical padding
    vertical_padding_params = [
        "heading_padding",
        "column_labels_padding",
        "data_row_padding",
        "row_group_padding",
        "source_notes_padding",
    ]

    # Get the current values for the vertical padding parameters
    vertical_padding_vals = [
        self._options.heading_padding.value,
        self._options.column_labels_padding.value,
        self._options.data_row_padding.value,
        self._options.row_group_padding.value,
        self._options.source_notes_padding.value,
    ]

    # Multiply each of the padding values by the `scale` factor but strip off the units first
    # then reattach the units after the multiplication
    # TODO: a current limitation is that the padding values must be in pixels and not percentages
    # TODO: another limitation is that the returned values must be in integer pixel values
    new_vertical_padding_vals = [
        str(int(float(v.split("px")[0]) * scale)) + "px" for v in vertical_padding_vals
    ]

    return tab_options(self, **dict(zip(vertical_padding_params, new_vertical_padding_vals)))


def opt_horizontal_padding(self: GTSelf, scale: float = 1.0) -> GTSelf:
    """
    Option to scale the horizontal padding of the table.

    This method allows us to scale the horizontal padding of the table by a factor of `scale`. The
    default value is `1.0` and this method serves as a convenient shortcut for `gt.tab_options(
    heading_padding_horizontal=<new_val>, column_labels_padding_horizontal=<new_val>,
    data_row_padding_horizontal=<new_val>, row_group_padding_horizontal=<new_val>,
    source_notes_padding_horizontal=<new_val>)`.

    Parameters
    ----------
    scale : float
        The factor by which to scale the horizontal padding. The default value is `1.0`. A value
        less than `1.0` will reduce the padding, and a value greater than `1.0` will increase the
        padding. The value must be between `0` and `3`.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using select columns from the `exibble` dataset, let's create a table with a number of
    components added. Following that, we'll scale the horizontal padding of the table by a factor of
    `3` using the `opt_horizontal_padding()` method.

    ```{python}
    from great_tables import GT, exibble, md

    gt_tbl = (
        GT(
            exibble[["num", "char", "currency", "row", "group"]],
            rowname_col="row",
            groupname_col="group"
        )
        .tab_header(
            title=md("Data listing from **exibble**"),
            subtitle=md("`exibble` is a **Great Tables** dataset.")
        )
        .fmt_number(columns="num")
        .fmt_currency(columns="currency")
        .tab_source_note(source_note="This is only a subset of the dataset.")
    )

    gt_tbl.opt_horizontal_padding(scale=3)
    ```

    The overall effect of scaling the horizontal padding is that the table will appear wider or
    and there will added buffer space between the table elements. The overall look of the table will
    be more spacious and neigboring pieces of text will be less cramped.

    Let's go the other way and scale the horizontal padding of the table by a factor of `0.5` using
    the `opt_horizontal_padding()` method.

    ```{python}
    gt_tbl.opt_horizontal_padding(scale=0.5)
    ```

    What you get in this case is more condensed text across the horizontal axis. This may not always
    be desired when cells consist mainly of text, but it could be useful when the table is more
    visual and the cells are filled with graphics or other non-textual elements.
    """

    # Stop if `scale` is beyond an acceptable range
    if scale < 0 or scale > 3:
        raise ValueError("`scale` must be a value between `0` and `3`.")

    # Get the parameters from the options that relate to horizontal padding
    horizontal_padding_params = [
        "heading_padding_horizontal",
        "column_labels_padding_horizontal",
        "data_row_padding_horizontal",
        "row_group_padding_horizontal",
        "source_notes_padding_horizontal",
    ]

    # Get the current values for the horizontal padding parameters
    horizontal_padding_vals = [
        self._options.heading_padding_horizontal.value,
        self._options.column_labels_padding_horizontal.value,
        self._options.data_row_padding_horizontal.value,
        self._options.row_group_padding_horizontal.value,
        self._options.source_notes_padding_horizontal.value,
    ]

    # Multiply each of the padding values by the `scale` factor but strip off the units first
    # then reattach the units after the multiplication
    # TODO: a current limitation is that the padding values must be in pixels and not percentages
    # TODO: another limitation is that the returned values must be in integer pixel values
    new_horizontal_padding_vals = [
        str(int(float(v.split("px")[0]) * scale)) + "px" for v in horizontal_padding_vals
    ]

    return tab_options(self, **dict(zip(horizontal_padding_params, new_horizontal_padding_vals)))


def opt_all_caps(
    self: GTSelf,
    all_caps: bool = True,
    locations: Union[str, List[str]] = ["column_labels", "stub", "row_group"],
) -> GTSelf:
    """
    Option to use all caps in select table locations.

    Sometimes an all-capitalized look is suitable for a table. By using `opt_all_caps()`, we can
    transform characters in the column labels, the stub, and in all row groups in this way (and
    there's control over which of these locations are transformed). This method serves as a
    convenient shortcut for `tab_options(<location>_text_transform="uppercase",
    <location>_font_size="80%", <location>_font_weight="bolder")` (for all `locations` selected).

    Parameters
    ----------
    all_caps : bool
        Indicates whether the text transformation to all caps should be performed (`True`, the
        default) or reset to default values (`False`) for the `locations` targeted.

    locations : Union[str, List[str]]
        Which locations should undergo this text transformation? By default it includes all of
        the `"column_labels"`, the `"stub"`, and the `"row_group"` locations. However, we could
        just choose one or two of those.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using select columns from the `exibble` dataset, let's create a table with a number of
    components added. Following that, we'll ensure that all text in the column labels, the stub, and
    in all row groups is transformed to all caps using the `opt_all_caps()` method.

    ```{python}
    from great_tables import GT, exibble, md

    (
      GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
      )
      .tab_header(
        title=md("Data listing from **exibble**"),
        subtitle=md("`exibble` is a **Great Tables** dataset.")
      )
      .fmt_number(columns="num")
      .fmt_currency(columns="currency")
      .tab_source_note(source_note="This is only a subset of the dataset.")
      .opt_all_caps()
    )
    ```
    """

    # If providing a scalar string value, normalize it to be in a list
    if type(locations).__name__ != "list":
        locations = _utils._str_scalar_to_list(cast(str, locations))

    # Ensure that the `locations` value is a list of strings
    _utils._assert_str_list(locations)

    # TODO: Ensure that all values within `locations` are valid

    # Set new options for `locations` selected, or, reset to default options
    # if `all_caps` is False
    # TODO: the code constantly reassigns res, in order to prepare for a
    # world where options are not mutating the GT options object.
    # TODO: is there a way to set multiple options at once?
    res = self
    if all_caps is True:
        if "column_labels" in locations:
            res = tab_options(res, column_labels_font_size="80%")
            res = tab_options(res, column_labels_font_weight="bolder")
            res = tab_options(res, column_labels_text_transform="uppercase")

        if "stub" in locations:
            res = tab_options(res, stub_font_size="80%")
            res = tab_options(res, stub_font_weight="bolder")
            res = tab_options(res, stub_text_transform="uppercase")

        if "row_group" in locations:
            res = tab_options(res, row_group_font_size="80%")
            res = tab_options(res, row_group_font_weight="bolder")
            res = tab_options(res, row_group_text_transform="uppercase")

    else:
        res = tab_options(res, column_labels_font_size="100%")
        res = tab_options(res, column_labels_font_weight="normal")
        res = tab_options(res, column_labels_text_transform="inherit")
        res = tab_options(res, stub_font_size="100%")
        res = tab_options(res, stub_font_weight="initial")
        res = tab_options(res, stub_text_transform="inherit")
        res = tab_options(res, row_group_font_size="100%")
        res = tab_options(res, row_group_font_weight="initial")
        res = tab_options(res, row_group_text_transform="inherit")

    return res
