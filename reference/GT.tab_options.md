# GT.tab_options()


Modify the table output options.


Usage

``` python
GT.tab_options(
    container_width=None,
    container_height=None,
    container_padding_x=None,
    container_padding_y=None,
    container_overflow_x=None,
    container_overflow_y=None,
    table_width=None,
    table_layout=None,
    table_margin_left=None,
    table_margin_right=None,
    table_background_color=None,
    table_additional_css=None,
    table_font_names=None,
    table_font_size=None,
    table_font_weight=None,
    table_font_style=None,
    table_font_color=None,
    table_font_color_light=None,
    table_border_top_style=None,
    table_border_top_width=None,
    table_border_top_color=None,
    table_border_bottom_style=None,
    table_border_bottom_width=None,
    table_border_bottom_color=None,
    table_border_left_style=None,
    table_border_left_width=None,
    table_border_left_color=None,
    table_border_right_style=None,
    table_border_right_width=None,
    table_border_right_color=None,
    heading_background_color=None,
    heading_align=None,
    heading_title_font_size=None,
    heading_title_font_weight=None,
    heading_subtitle_font_size=None,
    heading_subtitle_font_weight=None,
    heading_padding=None,
    heading_padding_horizontal=None,
    heading_border_bottom_style=None,
    heading_border_bottom_width=None,
    heading_border_bottom_color=None,
    heading_border_lr_style=None,
    heading_border_lr_width=None,
    heading_border_lr_color=None,
    column_labels_background_color=None,
    column_labels_font_size=None,
    column_labels_font_weight=None,
    column_labels_text_transform=None,
    column_labels_padding=None,
    column_labels_padding_horizontal=None,
    column_labels_vlines_style=None,
    column_labels_vlines_width=None,
    column_labels_vlines_color=None,
    column_labels_border_top_style=None,
    column_labels_border_top_width=None,
    column_labels_border_top_color=None,
    column_labels_border_bottom_style=None,
    column_labels_border_bottom_width=None,
    column_labels_border_bottom_color=None,
    column_labels_border_lr_style=None,
    column_labels_border_lr_width=None,
    column_labels_border_lr_color=None,
    column_labels_hidden=None,
    row_group_background_color=None,
    row_group_font_size=None,
    row_group_font_weight=None,
    row_group_text_transform=None,
    row_group_padding=None,
    row_group_padding_horizontal=None,
    row_group_border_top_style=None,
    row_group_border_top_width=None,
    row_group_border_top_color=None,
    row_group_border_bottom_style=None,
    row_group_border_bottom_width=None,
    row_group_border_bottom_color=None,
    row_group_border_left_style=None,
    row_group_border_left_width=None,
    row_group_border_left_color=None,
    row_group_border_right_style=None,
    row_group_border_right_width=None,
    row_group_border_right_color=None,
    row_group_as_column=None,
    table_body_hlines_style=None,
    table_body_hlines_width=None,
    table_body_hlines_color=None,
    table_body_vlines_style=None,
    table_body_vlines_width=None,
    table_body_vlines_color=None,
    table_body_border_top_style=None,
    table_body_border_top_width=None,
    table_body_border_top_color=None,
    table_body_border_bottom_style=None,
    table_body_border_bottom_width=None,
    table_body_border_bottom_color=None,
    stub_background_color=None,
    stub_font_size=None,
    stub_font_weight=None,
    stub_text_transform=None,
    stub_border_style=None,
    stub_border_width=None,
    stub_border_color=None,
    stub_indent_length=None,
    stub_row_group_font_size=None,
    stub_row_group_font_weight=None,
    stub_row_group_text_transform=None,
    stub_row_group_border_style=None,
    stub_row_group_border_width=None,
    stub_row_group_border_color=None,
    data_row_padding=None,
    data_row_padding_horizontal=None,
    summary_row_background_color=None,
    summary_row_text_transform=None,
    summary_row_padding=None,
    summary_row_padding_horizontal=None,
    summary_row_border_style=None,
    summary_row_border_width=None,
    summary_row_border_color=None,
    grand_summary_row_background_color=None,
    grand_summary_row_text_transform=None,
    grand_summary_row_padding=None,
    grand_summary_row_padding_horizontal=None,
    grand_summary_row_border_style=None,
    grand_summary_row_border_width=None,
    grand_summary_row_border_color=None,
    footnotes_marks=None,
    footnotes_spec_ref=None,
    footnotes_spec_ftr=None,
    footnotes_order=None,
    source_notes_background_color=None,
    source_notes_font_size=None,
    source_notes_padding=None,
    source_notes_padding_horizontal=None,
    source_notes_border_bottom_style=None,
    source_notes_border_bottom_width=None,
    source_notes_border_bottom_color=None,
    source_notes_border_lr_style=None,
    source_notes_border_lr_width=None,
    source_notes_border_lr_color=None,
    source_notes_multiline=None,
    source_notes_sep=None,
    row_striping_background_color=None,
    row_striping_include_stub=None,
    row_striping_include_table_body=None,
    quarto_disable_processing=None,
    ihtml_active=None,
    ihtml_use_pagination=None,
    ihtml_use_pagination_info=None,
    ihtml_use_sorting=None,
    ihtml_use_search=None,
    ihtml_use_filters=None,
    ihtml_use_resizers=None,
    ihtml_use_highlight=None,
    ihtml_use_compact_mode=None,
    ihtml_use_text_wrapping=None,
    ihtml_use_page_size_select=None,
    ihtml_page_size_default=None,
    ihtml_page_size_values=None,
    ihtml_pagination_type=None,
    ihtml_height=None,
    ihtml_selection_mode=None,
)
```


Modify the options available in a table. These options are named by the components, the subcomponents, and the element that can adjusted.


## Parameters


`container_width: str | None = None`  
The width of the table's container. Can be specified as a single-length character with units of pixels or as a percentage. If provided as a scalar numeric value, it is assumed that the value is given in units of pixels.

`container_height: str | None = None`  
The height of the table's container.

`container_padding_x: str | None = None`  
The horizontal padding of the table's container. Can be specified as a single-length character with units of pixels or as a percentage. If provided as a scalar numeric value, it is assumed that the value is given in units of pixels.

`container_padding_y: str | None = None`  
The vertical padding of the table's container. Same rules apply as for `container_padding_x`.

`container_overflow_x: str | None = None`  
An option to enable scrolling in the horizontal direction when the table content overflows the container dimensions. Using `True` (the default) means that horizontal scrolling is enabled to view the entire table in those directions. With `False`, the table may be clipped if the table width or height exceeds the `container_width`.

`container_overflow_y: str | None = None`  
An option to enable scrolling in the vertical direction when the table content overflows. Same rules apply as for `container_overflow_x`; the dependency here is that of the table height (`container_height`).

`table_width: str | None = None`  
The width of the table. Can be specified as a string with units of pixels or as a percentage. If provided as a numeric value, it is assumed that the value is given in units of pixels.

`table_layout: str | None = None`  
The value for the `table-layout` CSS style in the HTML output context. By default, this is `"fixed"` but another valid option is `"auto"`.

`table_margin_left: str | None = None`  
The size of the margins on the left of the table within the container. Can be specified as a single-length value with units of pixels or as a percentage. If provided as a numeric value, it is assumed that the value is given in units of pixels. Using `table_margin_left` will overwrite any values set by `table_align`.

`table_margin_right: str | None = None`  
The size of the margins on the right of the table within the container. Same rules apply as for `table_margin_left`. Using `table_margin_right` will overwrite any values set by `table_align`.

`table_background_color: str | None = None`  
The background color for the table. A color name or a hexadecimal color code should be provided.

`table_additional_css: str | list[str] | None = None`  
Additional CSS that can be added to the table. This can be used to add any custom CSS that is not covered by the other options.

`table_font_names: str | list[str] | None = None`  
The names of the fonts used for the table. This should be provided as a list of font names. If the first font isn't available, then the next font is tried (and so on).

`table_font_size: str | None = None`  
The font size for the table. Can be specified as a string with units of pixels or as a percentage. If provided as a numeric value, it is assumed that the value is given in units of pixels.

`table_font_weight: str | float | None = None`  
The font weight of the table. Can be a text-based keyword such as `"normal"`, `"bold"`, `"lighter"`, `"bolder"`, or, a numeric value between `1` and `1000`, inclusive. Note that only variable fonts may support the numeric mapping of weight.

`table_font_style: str | None = None`  
The font style for the table. Can be one of either `"normal"`, `"italic"`, or `"oblique"`.

`table_font_color: str | None = None`  
The text color used throughout the table. A color name or a hexadecimal color code should be provided.

`table_font_color_light: str | None = None`  
The text color used throughout the table when the background color is dark. A color name or a hexadecimal color code should be provided.

`table_border_top_style: str | None = None`  
The style of the table's absolute top border. Can be one of either `"solid"`, `"dotted"`, `"dashed"`, `"double"`, `"groove"`, `"ridge"`, `"inset"`, or `"outset"`.

`table_border_top_width: str | None = None`  
The width of the table's absolute top border. Can be specified as a string with units of pixels or as a percentage. If provided as a numeric value, it is assumed that the value is given in units of pixels.

`table_border_top_color: str | None = None`  
The color of the table's absolute top border. A color name or a hexadecimal color code should be provided.

`table_border_bottom_style: str | None = None`  
The style of the table's absolute bottom border.

`table_border_bottom_width: str | None = None`  
The width of the table's absolute bottom border.

`table_border_bottom_color: str | None = None`  
The color of the table's absolute bottom border.

`table_border_left_style: str | None = None`  
The style of the table's absolute left border.

`table_border_left_width: str | None = None`  
The width of the table's absolute left border.

`table_border_left_color: str | None = None`  
The color of the table's absolute left border.

`table_border_right_style: str | None = None`  
The style of the table's absolute right border.

`table_border_right_width: str | None = None`  
The width of the table's absolute right border.

`table_border_right_color: str | None = None`  
The color of the table's absolute right border.

`heading_background_color: str | None = None`  
The background color for the heading. A color name or a hexadecimal color code should be provided.

`heading_align: str | None = None`  
Controls the horizontal alignment of the heading title and subtitle. We can either use `"center"`, `"left"`, or `"right"`.

`heading_title_font_size: str | None = None`  
The font size for the heading title element.

`heading_title_font_weight: str | float | None = None`  
The font weight of the heading title.

`heading_subtitle_font_size: str | None = None`  
The font size for the heading subtitle element.

`heading_subtitle_font_weight: str | float | None = None`  
The font weight of the heading subtitle.

`heading_padding: str | None = None`  
The amount of vertical padding to incorporate in the `heading` (title and subtitle). Can be specified as a string with units of pixels or as a percentage. If provided as a numeric value, it is assumed that the value is given in units of pixels.

`heading_padding_horizontal: str | None = None`  
The amount of horizontal padding to incorporate in the `heading` (title and subtitle). Can be specified as a string with units of pixels or as a percentage. If provided as a numeric value, it is assumed that the value is given in units of pixels.

`heading_border_bottom_style: str | None = None`  
The style of the header's bottom border.

`heading_border_bottom_width: str | None = None`  
The width of the header's bottom border. If the `width` of this border is larger, then it will be the visible border.

`heading_border_bottom_color: str | None = None`  
The color of the header's bottom border.

`heading_border_lr_style: str | None = None`  
The style of the left and right borders of the `heading` location.

`heading_border_lr_width: str | None = None`  
The width of the left and right borders of the `heading` location. If the `width` of this border is larger, then it will be the visible border.

`heading_border_lr_color: str | None = None`  
The color of the left and right borders of the `heading` location.

`column_labels_background_color: str | None = None`  
The background color for the column labels. A color name or a hexadecimal color code should be provided.

`column_labels_font_size: str | None = None`  
The font size to use for all column labels.

`column_labels_font_weight: str | float | None = None`  
The font weight of the table's column labels.

`column_labels_text_transform: str | None = None`  
The text transformation for the column labels. Either of the `"uppercase"`, `"lowercase"`, or `"capitalize"` keywords can be used.

`column_labels_padding: str | None = None`  
The amount of vertical padding to incorporate in the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) (this includes the column spanners).

`column_labels_padding_horizontal: str | None = None`  
The amount of horizontal padding to incorporate in the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) (this includes the column spanners).

`column_labels_vlines_style: str | None = None`  
The style of all vertical lines ('vlines') of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels).

`column_labels_vlines_width: str | None = None`  
The width of all vertical lines ('vlines') of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels).

`column_labels_vlines_color: str | None = None`  
The color of all vertical lines ('vlines') of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels).

`column_labels_border_top_style: str | None = None`  
The style of the top border of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location.

`column_labels_border_top_width: str | None = None`  
The width of the top border of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location. If the `width` of this border is larger, then it will be the visible border.

`column_labels_border_top_color: str | None = None`  
The color of the top border of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location.

`column_labels_border_bottom_style: str | None = None`  
The style of the bottom border of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location.

`column_labels_border_bottom_width: str | None = None`  
The width of the bottom border of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location. If the `width` of this border is larger, then it will be the visible border.

`column_labels_border_bottom_color: str | None = None`  
The color of the bottom border of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location.

`column_labels_border_lr_style: str | None = None`  
The style of the left and right borders of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location.

`column_labels_border_lr_width: str | None = None`  
The width of the left and right borders of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location. If the `width` of this border is larger, then it will be the visible border.

`column_labels_border_lr_color: str | None = None`  
The color of the left and right borders of the [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location.

`column_labels_hidden: bool | None = None`  
An option to hide the column labels. If providing `True` then the entire [column_labels](loc.column_labels.md#great_tables.loc.column_labels) location won't be seen and the table header (if present) will collapse downward.

`row_group_background_color: str | None = None`  
The background color for the row group labels. A color name or a hexadecimal color code should be provided.

`row_group_font_weight: str | float | None = None`  
The font weight for all row group labels present in the table.

`row_group_font_size: str | None = None`  
The font size to use for all row group labels.

`row_group_padding: str | None = None`  
The amount of vertical padding to incorporate in the row group labels.

`row_group_border_top_style: str | None = None`  
The style of the top border of the `row_group` location.

`row_group_border_top_width: str | None = None`  
The width of the top border of the `row_group` location. If the `width` of this border is larger, then it will be the visible border.

`row_group_border_top_color: str | None = None`  
The color of the top border of the `row_group` location.

`row_group_border_bottom_style: str | None = None`  
The style of the bottom border of the `row_group` location.

`row_group_border_bottom_width: str | None = None`  
The width of the bottom border of the `row_group` location. If the `width` of this border is larger, then it will be the visible border.

`row_group_border_bottom_color: str | None = None`  
The color of the bottom border of the `row_group` location.

`row_group_border_left_style: str | None = None`  
The style of the left border of the `row_group` location.

`row_group_border_left_width: str | None = None`  
The width of the left border of the `row_group` location. If the `width` of this border is larger, then it will be the visible border.

`row_group_border_left_color: str | None = None`  
The color of the left border of the `row_group` location.

`row_group_border_right_style: str | None = None`  
The style of the right border of the `row_group` location.

`row_group_border_right_width: str | None = None`  
The width of the right border of the `row_group` location. If the `width` of this border is

`row_group_border_right_color: str | None = None`  
The color of the right border of the `row_group` location.

`row_group_as_column: bool | None = None`  
An option to render the row group labels as a column. If `True`, then the row group labels will be rendered as a column to the left of the table body. If `False`, then the row group labels will be rendered as a separate row above the grouping of rows.

`table_body_hlines_style: str | None = None`  
The style of all horizontal lines ('hlines') in the `table_body`.

`table_body_hlines_width: str | None = None`  
The width of all horizontal lines ('hlines') in the `table_body`.

`table_body_hlines_color: str | None = None`  
The color of all horizontal lines ('hlines') in the `table_body`.

`table_body_vlines_style: str | None = None`  
The style of all vertical lines ('vlines') in the `table_body`.

`table_body_vlines_width: str | None = None`  
The width of all vertical lines ('vlines') in the `table_body`.

`table_body_vlines_color: str | None = None`  
The color of all vertical lines ('vlines') in the `table_body`.

`table_body_border_top_style: str | None = None`  
The style of the top border of the `table_body` location.

`table_body_border_top_width: str | None = None`  
The width of the top border of the `table_body` location. If the `width` of this border is larger, then it will be the visible border.

`table_body_border_top_color: str | None = None`  
The color of the top border of the `table_body` location.

`table_body_border_bottom_style: str | None = None`  
The style of the bottom border of the `table_body` location.

`table_body_border_bottom_width: str | None = None`  
The width of the bottom border of the `table_body` location. If the `width` of this border

`table_body_border_bottom_color: str | None = None`  
The color of the bottom border of the `table_body` location.

`stub_background_color: str | None = None`  
The background color for the stub. A color name or a hexadecimal color code should be provided.

`stub_font_size: str | None = None`  
The font size to use for all row labels present in the table stub.

`stub_font_weight: str | float | None = None`  
The font weight for all row labels present in the table stub.

`stub_text_transform: str | None = None`  
The text transformation for the row labels present in the table stub.

`stub_border_style: str | None = None`  
The style of the vertical border of the table stub.

`stub_border_width: str | None = None`  
The width of the vertical border of the table stub.

`stub_border_color: str | None = None`  
The color of the vertical border of the table stub.

`stub_indent_length: str | None = None`  
The width of each indentation level for row labels set by <a href="../reference/GT.tab_stub_indent.html#great_tables.GT.tab_stub_indent" class="gdls-link"><code>tab_stub_indent()</code></a>. Defaults to `"5px"`.

`stub_row_group_font_size: str | None = None`  
The font size for the row group column in the stub.

`stub_row_group_font_weight: str | float | None = None`  
The font weight for the row group column in the stub.

`stub_row_group_text_transform: str | None = None`  
The text transformation for the row group column in the stub.

`stub_row_group_border_style: str | None = None`  
The style of the vertical border of the row group column in the stub.

`stub_row_group_border_width: str | None = None`  
The width of the vertical border of the row group column in the stub.

`stub_row_group_border_color: str | None = None`  
The color of the vertical border of the row group column in the stub.

`data_row_padding: str | None = None`  
The amount of vertical padding to incorporate in the body/stub rows.

`data_row_padding_horizontal: str | None = None`  
The amount of horizontal padding to incorporate in the body/stub rows.

`source_notes_background_color: str | None = None`  
The background color for the source notes. A color name or a hexadecimal color code should be provided.

`source_notes_font_size: str | None = None`  
The font size to use for all source note text.

`source_notes_padding: str | None = None`  
The amount of vertical padding to incorporate in the source notes.

`source_notes_padding_horizontal: str | None = None`  
The amount of horizontal padding to incorporate in the source notes.

`source_notes_multiline: bool | None = None`  
An option to either put source notes in separate lines (the default, or `True`) or render them as a continuous line of text with `source_notes_sep` providing the separator (by default `" "`) between notes.

`source_notes_sep: str | None = None`  
The separating characters between adjacent source notes when rendered as a continuous line of text (when `source_notes_multiline` is `False`). The default value is a single space character (`" "`).

`source_notes_border_bottom_style: str | None = None`  
The style of the bottom border of the [source_notes](loc.source_notes.md#great_tables.loc.source_notes) location.

`source_notes_border_bottom_width: str | None = None`  
The width of the bottom border of the [source_notes](loc.source_notes.md#great_tables.loc.source_notes) location. If the `width` of this border is larger, then it will be the visible border.

`source_notes_border_bottom_color: str | None = None`  
The color of the bottom border of the [source_notes](loc.source_notes.md#great_tables.loc.source_notes) location.

`source_notes_border_lr_style: str | None = None`  
The style of the left and right borders of the [source_notes](loc.source_notes.md#great_tables.loc.source_notes) location.

`source_notes_border_lr_width: str | None = None`  
The width of the left and right borders of the [source_notes](loc.source_notes.md#great_tables.loc.source_notes) location. If the `width` of this border is larger, then it will be the visible border.

`source_notes_border_lr_color: str | None = None`  
The color of the left and right borders of the [source_notes](loc.source_notes.md#great_tables.loc.source_notes) location.

`row_striping_background_color: str | None = None`  
The background color for striped table body rows. A color name or a hexadecimal color code should be provided.

`row_striping_include_stub: bool | None = None`  
An option for whether to include the stub when striping rows.

`row_striping_include_table_body: bool | None = None`  
An option for whether to include the table body when striping rows.

`quarto_disable_processing: bool | None = None`  
Whether to disable Quarto table processing.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using select columns from the [exibble](data.exibble.md#great_tables.data.exibble) dataset, let's create a new table with a number of table components added. We can use this object going forward to demonstrate some of the features available in the [tab_options()](GT.tab_options.md#great_tables.GT.tab_options) method.


``` python
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


<style>
#vpgedyjvzp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vpgedyjvzp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vpgedyjvzp p { margin: 0; padding: 0; }
 #vpgedyjvzp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vpgedyjvzp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vpgedyjvzp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vpgedyjvzp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vpgedyjvzp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vpgedyjvzp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vpgedyjvzp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vpgedyjvzp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vpgedyjvzp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vpgedyjvzp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vpgedyjvzp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vpgedyjvzp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vpgedyjvzp .gt_spanner_row { border-bottom-style: hidden; }
 #vpgedyjvzp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vpgedyjvzp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vpgedyjvzp .gt_from_md> :first-child { margin-top: 0; }
 #vpgedyjvzp .gt_from_md> :last-child { margin-bottom: 0; }
 #vpgedyjvzp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vpgedyjvzp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vpgedyjvzp .gt_indent_1 { text-indent: 5px; }
 #vpgedyjvzp .gt_indent_2 { text-indent: calc(5px * 2); }
 #vpgedyjvzp .gt_indent_3 { text-indent: calc(5px * 3); }
 #vpgedyjvzp .gt_indent_4 { text-indent: calc(5px * 4); }
 #vpgedyjvzp .gt_indent_5 { text-indent: calc(5px * 5); }
 #vpgedyjvzp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vpgedyjvzp .gt_row_group_first td { border-top-width: 2px; }
 #vpgedyjvzp .gt_row_group_first th { border-top-width: 2px; }
 #vpgedyjvzp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vpgedyjvzp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vpgedyjvzp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vpgedyjvzp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vpgedyjvzp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vpgedyjvzp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vpgedyjvzp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vpgedyjvzp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vpgedyjvzp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vpgedyjvzp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vpgedyjvzp .gt_left { text-align: left; }
 #vpgedyjvzp .gt_center { text-align: center; }
 #vpgedyjvzp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vpgedyjvzp .gt_font_normal { font-weight: normal; }
 #vpgedyjvzp .gt_font_bold { font-weight: bold; }
 #vpgedyjvzp .gt_font_italic { font-style: italic; }
 #vpgedyjvzp .gt_super { font-size: 65%; }
 #vpgedyjvzp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vpgedyjvzp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vpgedyjvzp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vpgedyjvzp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vpgedyjvzp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vpgedyjvzp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><code>exibble</code> is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.11</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">$49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.22</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">$17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">$1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.40</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5,550.00</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">$1,325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">$13.26</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8,880,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>


We can modify the table width to be set as `"100%`". In effect, this spans the table to entirely fill the content width area. This is done with the `table_width` option.


``` python
gt_tbl.tab_options(table_width="100%")
```


<style>
#vsfhrmjfry table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vsfhrmjfry thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vsfhrmjfry p { margin: 0; padding: 0; }
 #vsfhrmjfry .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: 100%; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vsfhrmjfry .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vsfhrmjfry .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vsfhrmjfry .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vsfhrmjfry .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vsfhrmjfry .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vsfhrmjfry .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vsfhrmjfry .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vsfhrmjfry .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vsfhrmjfry .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vsfhrmjfry .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vsfhrmjfry .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vsfhrmjfry .gt_spanner_row { border-bottom-style: hidden; }
 #vsfhrmjfry .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vsfhrmjfry .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vsfhrmjfry .gt_from_md> :first-child { margin-top: 0; }
 #vsfhrmjfry .gt_from_md> :last-child { margin-bottom: 0; }
 #vsfhrmjfry .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vsfhrmjfry .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vsfhrmjfry .gt_indent_1 { text-indent: 5px; }
 #vsfhrmjfry .gt_indent_2 { text-indent: calc(5px * 2); }
 #vsfhrmjfry .gt_indent_3 { text-indent: calc(5px * 3); }
 #vsfhrmjfry .gt_indent_4 { text-indent: calc(5px * 4); }
 #vsfhrmjfry .gt_indent_5 { text-indent: calc(5px * 5); }
 #vsfhrmjfry .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vsfhrmjfry .gt_row_group_first td { border-top-width: 2px; }
 #vsfhrmjfry .gt_row_group_first th { border-top-width: 2px; }
 #vsfhrmjfry .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vsfhrmjfry .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vsfhrmjfry .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vsfhrmjfry .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vsfhrmjfry .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vsfhrmjfry .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vsfhrmjfry .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vsfhrmjfry .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vsfhrmjfry .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vsfhrmjfry .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vsfhrmjfry .gt_left { text-align: left; }
 #vsfhrmjfry .gt_center { text-align: center; }
 #vsfhrmjfry .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vsfhrmjfry .gt_font_normal { font-weight: normal; }
 #vsfhrmjfry .gt_font_bold { font-weight: bold; }
 #vsfhrmjfry .gt_font_italic { font-style: italic; }
 #vsfhrmjfry .gt_super { font-size: 65%; }
 #vsfhrmjfry .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vsfhrmjfry .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vsfhrmjfry .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vsfhrmjfry .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vsfhrmjfry .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vsfhrmjfry .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><code>exibble</code> is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.11</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">$49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.22</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">$17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">$1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.40</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5,550.00</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">$1,325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">$13.26</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8,880,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>


With the `table_background_color` option, we can modify the table's background color. Here, we want that to be `"lightcyan"`.


``` python
gt_tbl.tab_options(table_background_color="lightcyan")
```


<style>
#gninpccayq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gninpccayq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gninpccayq p { margin: 0; padding: 0; }
 #gninpccayq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: lightcyan; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gninpccayq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gninpccayq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: lightcyan; border-bottom-width: 0; }
 #gninpccayq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: lightcyan; border-top-width: 0; }
 #gninpccayq .gt_heading { background-color: lightcyan; text-align: center; border-bottom-color: lightcyan; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gninpccayq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gninpccayq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gninpccayq .gt_col_heading { color: #333333; background-color: lightcyan; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gninpccayq .gt_column_spanner_outer { color: #333333; background-color: lightcyan; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gninpccayq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gninpccayq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gninpccayq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gninpccayq .gt_spanner_row { border-bottom-style: hidden; }
 #gninpccayq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: lightcyan; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gninpccayq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: lightcyan; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gninpccayq .gt_from_md> :first-child { margin-top: 0; }
 #gninpccayq .gt_from_md> :last-child { margin-bottom: 0; }
 #gninpccayq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gninpccayq .gt_stub { color: #333333; background-color: lightcyan; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gninpccayq .gt_indent_1 { text-indent: 5px; }
 #gninpccayq .gt_indent_2 { text-indent: calc(5px * 2); }
 #gninpccayq .gt_indent_3 { text-indent: calc(5px * 3); }
 #gninpccayq .gt_indent_4 { text-indent: calc(5px * 4); }
 #gninpccayq .gt_indent_5 { text-indent: calc(5px * 5); }
 #gninpccayq .gt_stub_row_group { color: #333333; background-color: lightcyan; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gninpccayq .gt_row_group_first td { border-top-width: 2px; }
 #gninpccayq .gt_row_group_first th { border-top-width: 2px; }
 #gninpccayq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gninpccayq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gninpccayq .gt_summary_row { color: #333333; background-color: lightcyan; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gninpccayq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gninpccayq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gninpccayq .gt_grand_summary_row { color: #333333; background-color: lightcyan; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gninpccayq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gninpccayq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gninpccayq .gt_sourcenotes { color: #333333; background-color: lightcyan; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gninpccayq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gninpccayq .gt_left { text-align: left; }
 #gninpccayq .gt_center { text-align: center; }
 #gninpccayq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gninpccayq .gt_font_normal { font-weight: normal; }
 #gninpccayq .gt_font_bold { font-weight: bold; }
 #gninpccayq .gt_font_italic { font-style: italic; }
 #gninpccayq .gt_super { font-size: 65%; }
 #gninpccayq .gt_footnotes { color: font-color(lightcyan); background-color: lightcyan; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gninpccayq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gninpccayq .gt_sourcenotes { color: #333333; background-color: lightcyan; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gninpccayq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gninpccayq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gninpccayq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><code>exibble</code> is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.11</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">$49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.22</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">$17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">$1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.40</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5,550.00</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">$1,325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">$13.26</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8,880,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>


The data rows of a table typically take up the most physical space but we have some control over the extent of that. With the `data_row_padding` option, it's possible to modify the top and bottom padding of data rows. We'll do just that in the following example, reducing the padding to a value of `"3px"`.


``` python
gt_tbl.tab_options(data_row_padding="3px")
```


<style>
#qayydozudt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qayydozudt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qayydozudt p { margin: 0; padding: 0; }
 #qayydozudt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qayydozudt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qayydozudt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qayydozudt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qayydozudt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qayydozudt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qayydozudt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qayydozudt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qayydozudt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qayydozudt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qayydozudt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qayydozudt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qayydozudt .gt_spanner_row { border-bottom-style: hidden; }
 #qayydozudt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qayydozudt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qayydozudt .gt_from_md> :first-child { margin-top: 0; }
 #qayydozudt .gt_from_md> :last-child { margin-bottom: 0; }
 #qayydozudt .gt_row { padding-top: 3px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qayydozudt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qayydozudt .gt_indent_1 { text-indent: 5px; }
 #qayydozudt .gt_indent_2 { text-indent: calc(5px * 2); }
 #qayydozudt .gt_indent_3 { text-indent: calc(5px * 3); }
 #qayydozudt .gt_indent_4 { text-indent: calc(5px * 4); }
 #qayydozudt .gt_indent_5 { text-indent: calc(5px * 5); }
 #qayydozudt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qayydozudt .gt_row_group_first td { border-top-width: 2px; }
 #qayydozudt .gt_row_group_first th { border-top-width: 2px; }
 #qayydozudt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qayydozudt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qayydozudt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qayydozudt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qayydozudt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qayydozudt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qayydozudt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qayydozudt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qayydozudt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qayydozudt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qayydozudt .gt_left { text-align: left; }
 #qayydozudt .gt_center { text-align: center; }
 #qayydozudt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qayydozudt .gt_font_normal { font-weight: normal; }
 #qayydozudt .gt_font_bold { font-weight: bold; }
 #qayydozudt .gt_font_italic { font-style: italic; }
 #qayydozudt .gt_super { font-size: 65%; }
 #qayydozudt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qayydozudt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qayydozudt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qayydozudt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qayydozudt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qayydozudt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><code>exibble</code> is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.11</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">$49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.22</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">$17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">$1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.40</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5,550.00</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">$1,325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">$13.26</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8,880,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>


The size of the title and the subtitle text in the header of the table can be altered with the `heading_title_font_size` and `heading_subtitle_font_size` options. Here, we'll use the `"small"` and `"x-small"` keyword values.


``` python
gt_tbl.tab_options(heading_title_font_size="small", heading_subtitle_font_size="x-small")
```


<style>
#lqlygaiwdr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lqlygaiwdr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lqlygaiwdr p { margin: 0; padding: 0; }
 #lqlygaiwdr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lqlygaiwdr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lqlygaiwdr .gt_title { color: #333333; font-size: small; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lqlygaiwdr .gt_subtitle { color: #333333; font-size: x-small; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lqlygaiwdr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lqlygaiwdr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lqlygaiwdr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lqlygaiwdr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lqlygaiwdr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lqlygaiwdr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lqlygaiwdr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lqlygaiwdr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lqlygaiwdr .gt_spanner_row { border-bottom-style: hidden; }
 #lqlygaiwdr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lqlygaiwdr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lqlygaiwdr .gt_from_md> :first-child { margin-top: 0; }
 #lqlygaiwdr .gt_from_md> :last-child { margin-bottom: 0; }
 #lqlygaiwdr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lqlygaiwdr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lqlygaiwdr .gt_indent_1 { text-indent: 5px; }
 #lqlygaiwdr .gt_indent_2 { text-indent: calc(5px * 2); }
 #lqlygaiwdr .gt_indent_3 { text-indent: calc(5px * 3); }
 #lqlygaiwdr .gt_indent_4 { text-indent: calc(5px * 4); }
 #lqlygaiwdr .gt_indent_5 { text-indent: calc(5px * 5); }
 #lqlygaiwdr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lqlygaiwdr .gt_row_group_first td { border-top-width: 2px; }
 #lqlygaiwdr .gt_row_group_first th { border-top-width: 2px; }
 #lqlygaiwdr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lqlygaiwdr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lqlygaiwdr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lqlygaiwdr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lqlygaiwdr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lqlygaiwdr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lqlygaiwdr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lqlygaiwdr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lqlygaiwdr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lqlygaiwdr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lqlygaiwdr .gt_left { text-align: left; }
 #lqlygaiwdr .gt_center { text-align: center; }
 #lqlygaiwdr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lqlygaiwdr .gt_font_normal { font-weight: normal; }
 #lqlygaiwdr .gt_font_bold { font-weight: bold; }
 #lqlygaiwdr .gt_font_italic { font-style: italic; }
 #lqlygaiwdr .gt_super { font-size: 65%; }
 #lqlygaiwdr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lqlygaiwdr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lqlygaiwdr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lqlygaiwdr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lqlygaiwdr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lqlygaiwdr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><code>exibble</code> is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.11</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">$49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.22</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">$17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">$1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.40</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5,550.00</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">$1,325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">$13.26</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8,880,000.00</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>
