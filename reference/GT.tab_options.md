## GT.tab_options()


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
    quarto_disable_processing=None
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

`table_font_weight: str | int | float | None = None`  
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

`heading_title_font_weight: str | int | float | None = None`  
The font weight of the heading title.

`heading_subtitle_font_size: str | None = None`  
The font size for the heading subtitle element.

`heading_subtitle_font_weight: str | int | float | None = None`  
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

`column_labels_font_weight: str | int | float | None = None`  
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

`row_group_font_weight: str | int | float | None = None`  
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

`stub_font_weight: str | int | float | None = None`  
The font weight for all row labels present in the table stub.

`stub_text_transform: str | None = None`  
The text transformation for the row labels present in the table stub.

`stub_border_style: str | None = None`  
The style of the vertical border of the table stub.

`stub_border_width: str | None = None`  
The width of the vertical border of the table stub.

`stub_border_color: str | None = None`  
The color of the vertical border of the table stub.

`stub_row_group_font_size: str | None = None`  
The font size for the row group column in the stub.

`stub_row_group_font_weight: str | int | float | None = None`  
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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
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
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
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
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
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
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
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
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
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
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>
