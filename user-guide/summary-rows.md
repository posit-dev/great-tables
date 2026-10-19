# Summary Rows

Summary rows provide aggregated values (such as totals, means, or counts) directly in the table, adjacent to the data they summarize. **Great Tables** supports two types: group-level summaries that appear next to each row group, and grand summaries that aggregate across the entire table. Both types let you define multiple aggregation functions at once and control where the summary appears.

Embedding aggregations directly in the table keeps the reader's eye on the data. When a total or average lives in a separate paragraph or a footnote, the reader has to scan back and forth between the table and the surrounding text to compare a group's summary to its individual rows. Summary rows eliminate that friction by placing the computed values right next to the data they describe.


# Setting Up the Example Data

For these examples, we will use a sales dataset with row groups representing different product categories.


``` python
import polars as pl
from great_tables import GT

sales_df = pl.DataFrame({
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam", "Headset"],
    "category": ["Computing", "Computing", "Computing", "Peripherals", "Peripherals", "Peripherals"],
    "units_sold": [45, 230, 180, 65, 120, 95],
    "revenue": [67500, 4600, 9000, 19500, 6000, 7125],
})

gt_sales = (
    GT(sales_df, rowname_col="product", groupname_col="category")
    .tab_header(title="Q4 Product Sales", subtitle="By category")
    .fmt_number(columns="revenue", decimals=0, use_seps=True)
)

gt_sales
```


<style>
#eyukpuqmdo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eyukpuqmdo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eyukpuqmdo p { margin: 0; padding: 0; }
 #eyukpuqmdo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eyukpuqmdo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eyukpuqmdo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eyukpuqmdo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eyukpuqmdo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eyukpuqmdo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyukpuqmdo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eyukpuqmdo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eyukpuqmdo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eyukpuqmdo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eyukpuqmdo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eyukpuqmdo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eyukpuqmdo .gt_spanner_row { border-bottom-style: hidden; }
 #eyukpuqmdo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eyukpuqmdo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eyukpuqmdo .gt_from_md> :first-child { margin-top: 0; }
 #eyukpuqmdo .gt_from_md> :last-child { margin-bottom: 0; }
 #eyukpuqmdo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eyukpuqmdo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eyukpuqmdo .gt_indent_1 { text-indent: 5px; }
 #eyukpuqmdo .gt_indent_2 { text-indent: calc(5px * 2); }
 #eyukpuqmdo .gt_indent_3 { text-indent: calc(5px * 3); }
 #eyukpuqmdo .gt_indent_4 { text-indent: calc(5px * 4); }
 #eyukpuqmdo .gt_indent_5 { text-indent: calc(5px * 5); }
 #eyukpuqmdo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eyukpuqmdo .gt_row_group_first td { border-top-width: 2px; }
 #eyukpuqmdo .gt_row_group_first th { border-top-width: 2px; }
 #eyukpuqmdo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eyukpuqmdo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyukpuqmdo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eyukpuqmdo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eyukpuqmdo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyukpuqmdo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eyukpuqmdo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eyukpuqmdo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eyukpuqmdo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyukpuqmdo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eyukpuqmdo .gt_left { text-align: left; }
 #eyukpuqmdo .gt_center { text-align: center; }
 #eyukpuqmdo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eyukpuqmdo .gt_font_normal { font-weight: normal; }
 #eyukpuqmdo .gt_font_bold { font-weight: bold; }
 #eyukpuqmdo .gt_font_italic { font-style: italic; }
 #eyukpuqmdo .gt_super { font-size: 65%; }
 #eyukpuqmdo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyukpuqmdo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eyukpuqmdo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyukpuqmdo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eyukpuqmdo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eyukpuqmdo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="Computing" class="gt_group_heading" scope="colgroup">Computing</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Laptop</td>
<td class="gt_row gt_right" headers="Computing stub-1 units_sold">45</td>
<td class="gt_row gt_right" headers="Computing stub-1 revenue">67,500</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Mouse</td>
<td class="gt_row gt_right" headers="Computing stub-2 units_sold">230</td>
<td class="gt_row gt_right" headers="Computing stub-2 revenue">4,600</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Keyboard</td>
<td class="gt_row gt_right" headers="Computing stub-3 units_sold">180</td>
<td class="gt_row gt_right" headers="Computing stub-3 revenue">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Peripherals" class="gt_group_heading" scope="colgroup">Peripherals</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Monitor</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 units_sold">65</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 revenue">19,500</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Webcam</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 units_sold">120</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 revenue">6,000</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Headset</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 units_sold">95</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 revenue">7,125</td>
</tr>
</tbody>
</table>


This table has two row groups: `"Computing"` and `"Peripherals"`. We can now add summaries at the group level and at the grand level.


# Group-Level Summary Rows

The [summary_rows()](../reference/GT.summary_rows.md#great_tables.GT.summary_rows) method adds summary rows to each row group. You provide aggregation functions through the `fns=` argument as a dictionary, where keys become the summary row labels and values are the aggregation logic.

When using a **Polars** DataFrame, the aggregation values should be Polars expressions.


``` python
(
    gt_sales
    .summary_rows(
        fns={"Total": pl.col("units_sold", "revenue").sum()}
    )
)
```


<style>
#hvrpncoerz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hvrpncoerz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hvrpncoerz p { margin: 0; padding: 0; }
 #hvrpncoerz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hvrpncoerz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hvrpncoerz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hvrpncoerz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hvrpncoerz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hvrpncoerz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvrpncoerz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hvrpncoerz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hvrpncoerz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hvrpncoerz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hvrpncoerz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hvrpncoerz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hvrpncoerz .gt_spanner_row { border-bottom-style: hidden; }
 #hvrpncoerz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hvrpncoerz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hvrpncoerz .gt_from_md> :first-child { margin-top: 0; }
 #hvrpncoerz .gt_from_md> :last-child { margin-bottom: 0; }
 #hvrpncoerz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hvrpncoerz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hvrpncoerz .gt_indent_1 { text-indent: 5px; }
 #hvrpncoerz .gt_indent_2 { text-indent: calc(5px * 2); }
 #hvrpncoerz .gt_indent_3 { text-indent: calc(5px * 3); }
 #hvrpncoerz .gt_indent_4 { text-indent: calc(5px * 4); }
 #hvrpncoerz .gt_indent_5 { text-indent: calc(5px * 5); }
 #hvrpncoerz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hvrpncoerz .gt_row_group_first td { border-top-width: 2px; }
 #hvrpncoerz .gt_row_group_first th { border-top-width: 2px; }
 #hvrpncoerz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hvrpncoerz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvrpncoerz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hvrpncoerz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hvrpncoerz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvrpncoerz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hvrpncoerz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hvrpncoerz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hvrpncoerz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvrpncoerz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hvrpncoerz .gt_left { text-align: left; }
 #hvrpncoerz .gt_center { text-align: center; }
 #hvrpncoerz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hvrpncoerz .gt_font_normal { font-weight: normal; }
 #hvrpncoerz .gt_font_bold { font-weight: bold; }
 #hvrpncoerz .gt_font_italic { font-style: italic; }
 #hvrpncoerz .gt_super { font-size: 65%; }
 #hvrpncoerz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvrpncoerz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hvrpncoerz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvrpncoerz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hvrpncoerz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hvrpncoerz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="Computing" class="gt_group_heading" scope="colgroup">Computing</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Laptop</td>
<td class="gt_row gt_right" headers="Computing stub-1 units_sold">45</td>
<td class="gt_row gt_right" headers="Computing stub-1 revenue">67,500</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Mouse</td>
<td class="gt_row gt_right" headers="Computing stub-2 units_sold">230</td>
<td class="gt_row gt_right" headers="Computing stub-2 revenue">4,600</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Keyboard</td>
<td class="gt_row gt_right" headers="Computing stub-3 units_sold">180</td>
<td class="gt_row gt_right" headers="Computing stub-3 revenue">9,000</td>
</tr>
<tr>
<td id="summary-Computing-Total" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Total units_sold">455</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Total revenue">81100</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Peripherals" class="gt_group_heading" scope="colgroup">Peripherals</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Monitor</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 units_sold">65</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 revenue">19,500</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Webcam</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 units_sold">120</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 revenue">6,000</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Headset</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 units_sold">95</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 revenue">7,125</td>
</tr>
<tr>
<td id="summary-Peripherals-Total" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Total units_sold">280</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Total revenue">32625</td>
</tr>
</tbody>
</table>


Each row group now has a `"Total"` summary row at the bottom showing the sum of numeric columns within that group.


## Multiple Aggregation Functions

You can include several functions in the `fns=` dictionary to produce multiple summary rows per group.


``` python
(
    gt_sales
    .summary_rows(
        fns={
            "Total": pl.col("units_sold", "revenue").sum(),
            "Average": pl.col("units_sold", "revenue").mean(),
        }
    )
)
```


<style>
#mdfdshhveb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mdfdshhveb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mdfdshhveb p { margin: 0; padding: 0; }
 #mdfdshhveb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mdfdshhveb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mdfdshhveb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mdfdshhveb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mdfdshhveb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mdfdshhveb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mdfdshhveb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mdfdshhveb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mdfdshhveb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mdfdshhveb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mdfdshhveb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mdfdshhveb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mdfdshhveb .gt_spanner_row { border-bottom-style: hidden; }
 #mdfdshhveb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mdfdshhveb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mdfdshhveb .gt_from_md> :first-child { margin-top: 0; }
 #mdfdshhveb .gt_from_md> :last-child { margin-bottom: 0; }
 #mdfdshhveb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mdfdshhveb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mdfdshhveb .gt_indent_1 { text-indent: 5px; }
 #mdfdshhveb .gt_indent_2 { text-indent: calc(5px * 2); }
 #mdfdshhveb .gt_indent_3 { text-indent: calc(5px * 3); }
 #mdfdshhveb .gt_indent_4 { text-indent: calc(5px * 4); }
 #mdfdshhveb .gt_indent_5 { text-indent: calc(5px * 5); }
 #mdfdshhveb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mdfdshhveb .gt_row_group_first td { border-top-width: 2px; }
 #mdfdshhveb .gt_row_group_first th { border-top-width: 2px; }
 #mdfdshhveb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mdfdshhveb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mdfdshhveb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mdfdshhveb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mdfdshhveb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mdfdshhveb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mdfdshhveb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mdfdshhveb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mdfdshhveb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mdfdshhveb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mdfdshhveb .gt_left { text-align: left; }
 #mdfdshhveb .gt_center { text-align: center; }
 #mdfdshhveb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mdfdshhveb .gt_font_normal { font-weight: normal; }
 #mdfdshhveb .gt_font_bold { font-weight: bold; }
 #mdfdshhveb .gt_font_italic { font-style: italic; }
 #mdfdshhveb .gt_super { font-size: 65%; }
 #mdfdshhveb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mdfdshhveb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mdfdshhveb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mdfdshhveb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mdfdshhveb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mdfdshhveb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="Computing" class="gt_group_heading" scope="colgroup">Computing</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Laptop</td>
<td class="gt_row gt_right" headers="Computing stub-1 units_sold">45</td>
<td class="gt_row gt_right" headers="Computing stub-1 revenue">67,500</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Mouse</td>
<td class="gt_row gt_right" headers="Computing stub-2 units_sold">230</td>
<td class="gt_row gt_right" headers="Computing stub-2 revenue">4,600</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Keyboard</td>
<td class="gt_row gt_right" headers="Computing stub-3 units_sold">180</td>
<td class="gt_row gt_right" headers="Computing stub-3 revenue">9,000</td>
</tr>
<tr>
<td id="summary-Computing-Total" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Total units_sold">455</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Total revenue">81100</td>
</tr>
<tr>
<td id="summary-Computing-Average" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Average</td>
<td class="gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Average units_sold">151.66666666666666</td>
<td class="gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Average revenue">27033.333333333332</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Peripherals" class="gt_group_heading" scope="colgroup">Peripherals</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Monitor</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 units_sold">65</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 revenue">19,500</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Webcam</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 units_sold">120</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 revenue">6,000</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Headset</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 units_sold">95</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 revenue">7,125</td>
</tr>
<tr>
<td id="summary-Peripherals-Total" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Total units_sold">280</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Total revenue">32625</td>
</tr>
<tr>
<td id="summary-Peripherals-Average" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Average</td>
<td class="gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Average units_sold">93.33333333333333</td>
<td class="gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Average revenue">10875.0</td>
</tr>
</tbody>
</table>


Both a `"Total"` and an `"Average"` row now appear at the bottom of each group.


## Placing Summaries at the Top

By default, summary rows appear at the bottom of each group. You can place them at the top instead by setting `side="top"`.


``` python
(
    gt_sales
    .summary_rows(
        fns={"Total": pl.col("units_sold", "revenue").sum()},
        side="top"
    )
)
```


<style>
#evndewjeuj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#evndewjeuj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#evndewjeuj p { margin: 0; padding: 0; }
 #evndewjeuj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #evndewjeuj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #evndewjeuj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #evndewjeuj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #evndewjeuj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #evndewjeuj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #evndewjeuj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #evndewjeuj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #evndewjeuj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #evndewjeuj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #evndewjeuj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #evndewjeuj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #evndewjeuj .gt_spanner_row { border-bottom-style: hidden; }
 #evndewjeuj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #evndewjeuj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #evndewjeuj .gt_from_md> :first-child { margin-top: 0; }
 #evndewjeuj .gt_from_md> :last-child { margin-bottom: 0; }
 #evndewjeuj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #evndewjeuj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #evndewjeuj .gt_indent_1 { text-indent: 5px; }
 #evndewjeuj .gt_indent_2 { text-indent: calc(5px * 2); }
 #evndewjeuj .gt_indent_3 { text-indent: calc(5px * 3); }
 #evndewjeuj .gt_indent_4 { text-indent: calc(5px * 4); }
 #evndewjeuj .gt_indent_5 { text-indent: calc(5px * 5); }
 #evndewjeuj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #evndewjeuj .gt_row_group_first td { border-top-width: 2px; }
 #evndewjeuj .gt_row_group_first th { border-top-width: 2px; }
 #evndewjeuj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #evndewjeuj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #evndewjeuj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #evndewjeuj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #evndewjeuj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #evndewjeuj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #evndewjeuj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #evndewjeuj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #evndewjeuj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #evndewjeuj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #evndewjeuj .gt_left { text-align: left; }
 #evndewjeuj .gt_center { text-align: center; }
 #evndewjeuj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #evndewjeuj .gt_font_normal { font-weight: normal; }
 #evndewjeuj .gt_font_bold { font-weight: bold; }
 #evndewjeuj .gt_font_italic { font-style: italic; }
 #evndewjeuj .gt_super { font-size: 65%; }
 #evndewjeuj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #evndewjeuj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #evndewjeuj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #evndewjeuj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #evndewjeuj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #evndewjeuj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="Computing" class="gt_group_heading" scope="colgroup">Computing</th>
</tr>

<tr>
<td id="summary-Computing-Total" class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row" scope="row">Total</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Total units_sold">455</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Total revenue">81100</td>
</tr>
<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Laptop</td>
<td class="gt_row gt_right" headers="Computing stub-1 units_sold">45</td>
<td class="gt_row gt_right" headers="Computing stub-1 revenue">67,500</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Mouse</td>
<td class="gt_row gt_right" headers="Computing stub-2 units_sold">230</td>
<td class="gt_row gt_right" headers="Computing stub-2 revenue">4,600</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Keyboard</td>
<td class="gt_row gt_right" headers="Computing stub-3 units_sold">180</td>
<td class="gt_row gt_right" headers="Computing stub-3 revenue">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Peripherals" class="gt_group_heading" scope="colgroup">Peripherals</td>
</tr>
<tr>
<td id="summary-Peripherals-Total" class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row" scope="row">Total</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Total units_sold">280</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Total revenue">32625</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Monitor</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 units_sold">65</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 revenue">19,500</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Webcam</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 units_sold">120</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 revenue">6,000</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Headset</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 units_sold">95</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 revenue">7,125</td>
</tr>
</tbody>
</table>


The summary row now sits above the data rows in each group rather than below them, making the totals immediately visible.

Top placement works well when the summary is the main takeaway and the detail rows serve as supporting evidence. Readers see the headline number first and can drill into the breakdown below it. Bottom placement (the default) follows the more conventional reading order where you examine the data first and arrive at the summary as a natural conclusion.


## Targeting Specific Groups

If you only want summaries for certain groups, use the `groups=` argument with a list of group names.


``` python
(
    gt_sales
    .summary_rows(
        fns={"Total": pl.col("units_sold", "revenue").sum()},
        groups=["Computing"]
    )
)
```


<style>
#nneheautmx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nneheautmx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nneheautmx p { margin: 0; padding: 0; }
 #nneheautmx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nneheautmx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nneheautmx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nneheautmx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nneheautmx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nneheautmx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nneheautmx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nneheautmx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nneheautmx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nneheautmx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nneheautmx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nneheautmx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nneheautmx .gt_spanner_row { border-bottom-style: hidden; }
 #nneheautmx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nneheautmx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nneheautmx .gt_from_md> :first-child { margin-top: 0; }
 #nneheautmx .gt_from_md> :last-child { margin-bottom: 0; }
 #nneheautmx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nneheautmx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nneheautmx .gt_indent_1 { text-indent: 5px; }
 #nneheautmx .gt_indent_2 { text-indent: calc(5px * 2); }
 #nneheautmx .gt_indent_3 { text-indent: calc(5px * 3); }
 #nneheautmx .gt_indent_4 { text-indent: calc(5px * 4); }
 #nneheautmx .gt_indent_5 { text-indent: calc(5px * 5); }
 #nneheautmx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nneheautmx .gt_row_group_first td { border-top-width: 2px; }
 #nneheautmx .gt_row_group_first th { border-top-width: 2px; }
 #nneheautmx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nneheautmx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nneheautmx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nneheautmx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nneheautmx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nneheautmx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nneheautmx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nneheautmx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nneheautmx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nneheautmx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nneheautmx .gt_left { text-align: left; }
 #nneheautmx .gt_center { text-align: center; }
 #nneheautmx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nneheautmx .gt_font_normal { font-weight: normal; }
 #nneheautmx .gt_font_bold { font-weight: bold; }
 #nneheautmx .gt_font_italic { font-style: italic; }
 #nneheautmx .gt_super { font-size: 65%; }
 #nneheautmx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nneheautmx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nneheautmx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nneheautmx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nneheautmx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nneheautmx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="Computing" class="gt_group_heading" scope="colgroup">Computing</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Laptop</td>
<td class="gt_row gt_right" headers="Computing stub-1 units_sold">45</td>
<td class="gt_row gt_right" headers="Computing stub-1 revenue">67,500</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Mouse</td>
<td class="gt_row gt_right" headers="Computing stub-2 units_sold">230</td>
<td class="gt_row gt_right" headers="Computing stub-2 revenue">4,600</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Keyboard</td>
<td class="gt_row gt_right" headers="Computing stub-3 units_sold">180</td>
<td class="gt_row gt_right" headers="Computing stub-3 revenue">9,000</td>
</tr>
<tr>
<td id="summary-Computing-Total" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Total units_sold">455</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Total revenue">81100</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Peripherals" class="gt_group_heading" scope="colgroup">Peripherals</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Monitor</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 units_sold">65</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 revenue">19,500</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Webcam</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 units_sold">120</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 revenue">6,000</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Headset</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 units_sold">95</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 revenue">7,125</td>
</tr>
</tbody>
</table>


Only the `"Computing"` group receives a summary row.


# Grand Summary Rows

The [grand_summary_rows()](../reference/GT.grand_summary_rows.md#great_tables.GT.grand_summary_rows) method works the same way as [summary_rows()](../reference/GT.summary_rows.md#great_tables.GT.summary_rows), but it aggregates across all data in the table regardless of row groups. The resulting summary rows appear at the very bottom (or top) of the table.


``` python
(
    gt_sales
    .grand_summary_rows(
        fns={"Grand Total": pl.col("units_sold", "revenue").sum()}
    )
)
```


<style>
#fqgejbnzwh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fqgejbnzwh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fqgejbnzwh p { margin: 0; padding: 0; }
 #fqgejbnzwh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fqgejbnzwh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fqgejbnzwh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fqgejbnzwh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fqgejbnzwh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fqgejbnzwh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fqgejbnzwh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fqgejbnzwh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fqgejbnzwh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fqgejbnzwh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fqgejbnzwh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fqgejbnzwh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fqgejbnzwh .gt_spanner_row { border-bottom-style: hidden; }
 #fqgejbnzwh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fqgejbnzwh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fqgejbnzwh .gt_from_md> :first-child { margin-top: 0; }
 #fqgejbnzwh .gt_from_md> :last-child { margin-bottom: 0; }
 #fqgejbnzwh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fqgejbnzwh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fqgejbnzwh .gt_indent_1 { text-indent: 5px; }
 #fqgejbnzwh .gt_indent_2 { text-indent: calc(5px * 2); }
 #fqgejbnzwh .gt_indent_3 { text-indent: calc(5px * 3); }
 #fqgejbnzwh .gt_indent_4 { text-indent: calc(5px * 4); }
 #fqgejbnzwh .gt_indent_5 { text-indent: calc(5px * 5); }
 #fqgejbnzwh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fqgejbnzwh .gt_row_group_first td { border-top-width: 2px; }
 #fqgejbnzwh .gt_row_group_first th { border-top-width: 2px; }
 #fqgejbnzwh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fqgejbnzwh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fqgejbnzwh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fqgejbnzwh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fqgejbnzwh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fqgejbnzwh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fqgejbnzwh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fqgejbnzwh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fqgejbnzwh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fqgejbnzwh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fqgejbnzwh .gt_left { text-align: left; }
 #fqgejbnzwh .gt_center { text-align: center; }
 #fqgejbnzwh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fqgejbnzwh .gt_font_normal { font-weight: normal; }
 #fqgejbnzwh .gt_font_bold { font-weight: bold; }
 #fqgejbnzwh .gt_font_italic { font-style: italic; }
 #fqgejbnzwh .gt_super { font-size: 65%; }
 #fqgejbnzwh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fqgejbnzwh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fqgejbnzwh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fqgejbnzwh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fqgejbnzwh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fqgejbnzwh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="Computing" class="gt_group_heading" scope="colgroup">Computing</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Laptop</td>
<td class="gt_row gt_right" headers="Computing stub-1 units_sold">45</td>
<td class="gt_row gt_right" headers="Computing stub-1 revenue">67,500</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Mouse</td>
<td class="gt_row gt_right" headers="Computing stub-2 units_sold">230</td>
<td class="gt_row gt_right" headers="Computing stub-2 revenue">4,600</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Keyboard</td>
<td class="gt_row gt_right" headers="Computing stub-3 units_sold">180</td>
<td class="gt_row gt_right" headers="Computing stub-3 revenue">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Peripherals" class="gt_group_heading" scope="colgroup">Peripherals</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Monitor</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 units_sold">65</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 revenue">19,500</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Webcam</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 units_sold">120</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 revenue">6,000</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Headset</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 units_sold">95</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 revenue">7,125</td>
</tr>
<tr>
<td id="grand-summary-Grand-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Grand Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Grand-Total units_sold">735</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Grand-Total revenue">113725</td>
</tr>
</tbody>
</table>


A single `"Grand Total"` row appears below all row groups, showing the overall totals.


## Combining Group and Grand Summaries

You can use both [summary_rows()](../reference/GT.summary_rows.md#great_tables.GT.summary_rows) and [grand_summary_rows()](../reference/GT.grand_summary_rows.md#great_tables.GT.grand_summary_rows) on the same table to provide aggregation at both levels.


``` python
(
    gt_sales
    .summary_rows(
        fns={"Subtotal": pl.col("units_sold", "revenue").sum()}
    )
    .grand_summary_rows(
        fns={
            "Grand Total": pl.col("units_sold", "revenue").sum(),
            "Overall Average": pl.col("units_sold", "revenue").mean(),
        }
    )
)
```


<style>
#qgndeprksh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qgndeprksh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qgndeprksh p { margin: 0; padding: 0; }
 #qgndeprksh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qgndeprksh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qgndeprksh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qgndeprksh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qgndeprksh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qgndeprksh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgndeprksh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qgndeprksh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qgndeprksh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qgndeprksh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qgndeprksh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qgndeprksh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qgndeprksh .gt_spanner_row { border-bottom-style: hidden; }
 #qgndeprksh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qgndeprksh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qgndeprksh .gt_from_md> :first-child { margin-top: 0; }
 #qgndeprksh .gt_from_md> :last-child { margin-bottom: 0; }
 #qgndeprksh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qgndeprksh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qgndeprksh .gt_indent_1 { text-indent: 5px; }
 #qgndeprksh .gt_indent_2 { text-indent: calc(5px * 2); }
 #qgndeprksh .gt_indent_3 { text-indent: calc(5px * 3); }
 #qgndeprksh .gt_indent_4 { text-indent: calc(5px * 4); }
 #qgndeprksh .gt_indent_5 { text-indent: calc(5px * 5); }
 #qgndeprksh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qgndeprksh .gt_row_group_first td { border-top-width: 2px; }
 #qgndeprksh .gt_row_group_first th { border-top-width: 2px; }
 #qgndeprksh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qgndeprksh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgndeprksh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qgndeprksh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qgndeprksh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgndeprksh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qgndeprksh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qgndeprksh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qgndeprksh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgndeprksh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qgndeprksh .gt_left { text-align: left; }
 #qgndeprksh .gt_center { text-align: center; }
 #qgndeprksh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qgndeprksh .gt_font_normal { font-weight: normal; }
 #qgndeprksh .gt_font_bold { font-weight: bold; }
 #qgndeprksh .gt_font_italic { font-style: italic; }
 #qgndeprksh .gt_super { font-size: 65%; }
 #qgndeprksh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgndeprksh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qgndeprksh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgndeprksh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qgndeprksh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qgndeprksh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="Computing" class="gt_group_heading" scope="colgroup">Computing</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Laptop</td>
<td class="gt_row gt_right" headers="Computing stub-1 units_sold">45</td>
<td class="gt_row gt_right" headers="Computing stub-1 revenue">67,500</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Mouse</td>
<td class="gt_row gt_right" headers="Computing stub-2 units_sold">230</td>
<td class="gt_row gt_right" headers="Computing stub-2 revenue">4,600</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Keyboard</td>
<td class="gt_row gt_right" headers="Computing stub-3 units_sold">180</td>
<td class="gt_row gt_right" headers="Computing stub-3 revenue">9,000</td>
</tr>
<tr>
<td id="summary-Computing-Subtotal" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Subtotal</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Subtotal units_sold">455</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Computing summary-Computing-Subtotal revenue">81100</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Peripherals" class="gt_group_heading" scope="colgroup">Peripherals</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Monitor</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 units_sold">65</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 revenue">19,500</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Webcam</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 units_sold">120</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 revenue">6,000</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Headset</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 units_sold">95</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 revenue">7,125</td>
</tr>
<tr>
<td id="summary-Peripherals-Subtotal" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Subtotal</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Subtotal units_sold">280</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Peripherals summary-Peripherals-Subtotal revenue">32625</td>
</tr>
<tr>
<td id="grand-summary-Grand-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Grand Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Grand-Total units_sold">735</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Grand-Total revenue">113725</td>
</tr>
<tr>
<td id="grand-summary-Overall-Average" class="gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Overall Average</td>
<td class="gt_row gt_right gt_grand_summary_row" headers="grand-summary-Overall-Average units_sold">122.5</td>
<td class="gt_row gt_right gt_grand_summary_row" headers="grand-summary-Overall-Average revenue">18954.166666666668</td>
</tr>
</tbody>
</table>


Each group now has a `"Subtotal"` row, and the table finishes with a `"Grand Total"` and `"Overall Average"` row that span across all groups.

This combination of group and grand summaries is common in financial and sales reporting, where readers expect both subtotals per category and an overall total. The visual hierarchy (group summaries, then a grand summary at the bottom) mirrors how people naturally reason about grouped data: understand the parts first, then see how they add up to the whole.


# Working with Pandas DataFrames

When using a **Pandas** DataFrame, the aggregation functions receive a Pandas DataFrame and should work accordingly.


``` python
import pandas as pd

sales_pd = pd.DataFrame({
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam", "Headset"],
    "category": ["Computing", "Computing", "Computing", "Peripherals", "Peripherals", "Peripherals"],
    "units_sold": [45, 230, 180, 65, 120, 95],
    "revenue": [67500, 4600, 9000, 19500, 6000, 7125],
})

(
    GT(sales_pd, rowname_col="product", groupname_col="category")
    .fmt_number(columns="revenue", decimals=0, use_seps=True)
    .grand_summary_rows(
        fns={"Total": lambda df: df.sum(numeric_only=True)}
    )
)
```


<style>
#dhhpsydljo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dhhpsydljo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dhhpsydljo p { margin: 0; padding: 0; }
 #dhhpsydljo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dhhpsydljo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dhhpsydljo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dhhpsydljo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dhhpsydljo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dhhpsydljo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dhhpsydljo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dhhpsydljo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dhhpsydljo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dhhpsydljo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dhhpsydljo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dhhpsydljo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dhhpsydljo .gt_spanner_row { border-bottom-style: hidden; }
 #dhhpsydljo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dhhpsydljo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dhhpsydljo .gt_from_md> :first-child { margin-top: 0; }
 #dhhpsydljo .gt_from_md> :last-child { margin-bottom: 0; }
 #dhhpsydljo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dhhpsydljo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dhhpsydljo .gt_indent_1 { text-indent: 5px; }
 #dhhpsydljo .gt_indent_2 { text-indent: calc(5px * 2); }
 #dhhpsydljo .gt_indent_3 { text-indent: calc(5px * 3); }
 #dhhpsydljo .gt_indent_4 { text-indent: calc(5px * 4); }
 #dhhpsydljo .gt_indent_5 { text-indent: calc(5px * 5); }
 #dhhpsydljo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dhhpsydljo .gt_row_group_first td { border-top-width: 2px; }
 #dhhpsydljo .gt_row_group_first th { border-top-width: 2px; }
 #dhhpsydljo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dhhpsydljo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dhhpsydljo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dhhpsydljo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dhhpsydljo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dhhpsydljo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dhhpsydljo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dhhpsydljo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dhhpsydljo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dhhpsydljo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dhhpsydljo .gt_left { text-align: left; }
 #dhhpsydljo .gt_center { text-align: center; }
 #dhhpsydljo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dhhpsydljo .gt_font_normal { font-weight: normal; }
 #dhhpsydljo .gt_font_bold { font-weight: bold; }
 #dhhpsydljo .gt_font_italic { font-style: italic; }
 #dhhpsydljo .gt_super { font-size: 65%; }
 #dhhpsydljo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dhhpsydljo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dhhpsydljo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dhhpsydljo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dhhpsydljo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dhhpsydljo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="Computing" class="gt_group_heading" scope="colgroup">Computing</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Laptop</td>
<td class="gt_row gt_right" headers="Computing stub-1 units_sold">45</td>
<td class="gt_row gt_right" headers="Computing stub-1 revenue">67,500</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Mouse</td>
<td class="gt_row gt_right" headers="Computing stub-2 units_sold">230</td>
<td class="gt_row gt_right" headers="Computing stub-2 revenue">4,600</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Keyboard</td>
<td class="gt_row gt_right" headers="Computing stub-3 units_sold">180</td>
<td class="gt_row gt_right" headers="Computing stub-3 revenue">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Peripherals" class="gt_group_heading" scope="colgroup">Peripherals</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Monitor</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 units_sold">65</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 revenue">19,500</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Webcam</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 units_sold">120</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 revenue">6,000</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Headset</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 units_sold">95</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 revenue">7,125</td>
</tr>
<tr>
<td id="grand-summary-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Total units_sold">735</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Total revenue">113725</td>
</tr>
</tbody>
</table>


The `numeric_only=True` argument ensures that only numeric columns are summed, avoiding errors with string columns.


# Styling Summary Rows

Summary rows can be styled using [loc.grand_summary()](../reference/loc.grand_summary.md#great_tables.loc.grand_summary) and `loc.summary()` with [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style). This lets you visually distinguish summary rows from data rows.


``` python
from great_tables import loc, style

(
    gt_sales
    .grand_summary_rows(
        fns={"Grand Total": pl.col("units_sold", "revenue").sum()}
    )
    .tab_style(
        style=style.fill(color="lightyellow"),
        locations=loc.grand_summary()
    )
)
```


<style>
#mbmoeszdpy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mbmoeszdpy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mbmoeszdpy p { margin: 0; padding: 0; }
 #mbmoeszdpy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mbmoeszdpy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mbmoeszdpy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mbmoeszdpy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mbmoeszdpy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mbmoeszdpy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mbmoeszdpy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mbmoeszdpy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mbmoeszdpy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mbmoeszdpy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mbmoeszdpy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mbmoeszdpy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mbmoeszdpy .gt_spanner_row { border-bottom-style: hidden; }
 #mbmoeszdpy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mbmoeszdpy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mbmoeszdpy .gt_from_md> :first-child { margin-top: 0; }
 #mbmoeszdpy .gt_from_md> :last-child { margin-bottom: 0; }
 #mbmoeszdpy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mbmoeszdpy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mbmoeszdpy .gt_indent_1 { text-indent: 5px; }
 #mbmoeszdpy .gt_indent_2 { text-indent: calc(5px * 2); }
 #mbmoeszdpy .gt_indent_3 { text-indent: calc(5px * 3); }
 #mbmoeszdpy .gt_indent_4 { text-indent: calc(5px * 4); }
 #mbmoeszdpy .gt_indent_5 { text-indent: calc(5px * 5); }
 #mbmoeszdpy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mbmoeszdpy .gt_row_group_first td { border-top-width: 2px; }
 #mbmoeszdpy .gt_row_group_first th { border-top-width: 2px; }
 #mbmoeszdpy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mbmoeszdpy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mbmoeszdpy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mbmoeszdpy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mbmoeszdpy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mbmoeszdpy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mbmoeszdpy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mbmoeszdpy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mbmoeszdpy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mbmoeszdpy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mbmoeszdpy .gt_left { text-align: left; }
 #mbmoeszdpy .gt_center { text-align: center; }
 #mbmoeszdpy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mbmoeszdpy .gt_font_normal { font-weight: normal; }
 #mbmoeszdpy .gt_font_bold { font-weight: bold; }
 #mbmoeszdpy .gt_font_italic { font-style: italic; }
 #mbmoeszdpy .gt_super { font-size: 65%; }
 #mbmoeszdpy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mbmoeszdpy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mbmoeszdpy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mbmoeszdpy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mbmoeszdpy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mbmoeszdpy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="Computing" class="gt_group_heading" scope="colgroup">Computing</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Laptop</td>
<td class="gt_row gt_right" headers="Computing stub-1 units_sold">45</td>
<td class="gt_row gt_right" headers="Computing stub-1 revenue">67,500</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Mouse</td>
<td class="gt_row gt_right" headers="Computing stub-2 units_sold">230</td>
<td class="gt_row gt_right" headers="Computing stub-2 revenue">4,600</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Keyboard</td>
<td class="gt_row gt_right" headers="Computing stub-3 units_sold">180</td>
<td class="gt_row gt_right" headers="Computing stub-3 revenue">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Peripherals" class="gt_group_heading" scope="colgroup">Peripherals</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Monitor</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 units_sold">65</td>
<td class="gt_row gt_right" headers="Peripherals stub-4 revenue">19,500</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Webcam</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 units_sold">120</td>
<td class="gt_row gt_right" headers="Peripherals stub-5 revenue">6,000</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Headset</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 units_sold">95</td>
<td class="gt_row gt_right" headers="Peripherals stub-6 revenue">7,125</td>
</tr>
<tr>
<td id="grand-summary-Grand-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Grand Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightyellow" headers="grand-summary-Grand-Total units_sold">735</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightyellow" headers="grand-summary-Grand-Total revenue">113725</td>
</tr>
</tbody>
</table>


Summary rows are a natural companion to row groups, providing the aggregated context that readers need to interpret grouped data. By combining group-level and grand summaries, formatting, and targeted styling, you can build tables that tell a complete analytical story.
