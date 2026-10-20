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
#tuutqidsqn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tuutqidsqn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tuutqidsqn p { margin: 0; padding: 0; }
 #tuutqidsqn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tuutqidsqn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tuutqidsqn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tuutqidsqn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tuutqidsqn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tuutqidsqn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tuutqidsqn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tuutqidsqn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tuutqidsqn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tuutqidsqn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tuutqidsqn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tuutqidsqn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tuutqidsqn .gt_spanner_row { border-bottom-style: hidden; }
 #tuutqidsqn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tuutqidsqn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tuutqidsqn .gt_from_md> :first-child { margin-top: 0; }
 #tuutqidsqn .gt_from_md> :last-child { margin-bottom: 0; }
 #tuutqidsqn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tuutqidsqn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tuutqidsqn .gt_indent_1 { text-indent: 5px; }
 #tuutqidsqn .gt_indent_2 { text-indent: calc(5px * 2); }
 #tuutqidsqn .gt_indent_3 { text-indent: calc(5px * 3); }
 #tuutqidsqn .gt_indent_4 { text-indent: calc(5px * 4); }
 #tuutqidsqn .gt_indent_5 { text-indent: calc(5px * 5); }
 #tuutqidsqn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tuutqidsqn .gt_row_group_first td { border-top-width: 2px; }
 #tuutqidsqn .gt_row_group_first th { border-top-width: 2px; }
 #tuutqidsqn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tuutqidsqn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tuutqidsqn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tuutqidsqn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tuutqidsqn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tuutqidsqn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tuutqidsqn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tuutqidsqn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tuutqidsqn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tuutqidsqn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tuutqidsqn .gt_left { text-align: left; }
 #tuutqidsqn .gt_center { text-align: center; }
 #tuutqidsqn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tuutqidsqn .gt_font_normal { font-weight: normal; }
 #tuutqidsqn .gt_font_bold { font-weight: bold; }
 #tuutqidsqn .gt_font_italic { font-style: italic; }
 #tuutqidsqn .gt_super { font-size: 65%; }
 #tuutqidsqn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tuutqidsqn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tuutqidsqn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tuutqidsqn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tuutqidsqn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tuutqidsqn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wlbjguwhbf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wlbjguwhbf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wlbjguwhbf p { margin: 0; padding: 0; }
 #wlbjguwhbf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wlbjguwhbf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wlbjguwhbf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wlbjguwhbf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wlbjguwhbf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wlbjguwhbf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wlbjguwhbf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wlbjguwhbf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wlbjguwhbf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wlbjguwhbf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wlbjguwhbf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wlbjguwhbf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wlbjguwhbf .gt_spanner_row { border-bottom-style: hidden; }
 #wlbjguwhbf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wlbjguwhbf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wlbjguwhbf .gt_from_md> :first-child { margin-top: 0; }
 #wlbjguwhbf .gt_from_md> :last-child { margin-bottom: 0; }
 #wlbjguwhbf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wlbjguwhbf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wlbjguwhbf .gt_indent_1 { text-indent: 5px; }
 #wlbjguwhbf .gt_indent_2 { text-indent: calc(5px * 2); }
 #wlbjguwhbf .gt_indent_3 { text-indent: calc(5px * 3); }
 #wlbjguwhbf .gt_indent_4 { text-indent: calc(5px * 4); }
 #wlbjguwhbf .gt_indent_5 { text-indent: calc(5px * 5); }
 #wlbjguwhbf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wlbjguwhbf .gt_row_group_first td { border-top-width: 2px; }
 #wlbjguwhbf .gt_row_group_first th { border-top-width: 2px; }
 #wlbjguwhbf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wlbjguwhbf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wlbjguwhbf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wlbjguwhbf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wlbjguwhbf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wlbjguwhbf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wlbjguwhbf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wlbjguwhbf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wlbjguwhbf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wlbjguwhbf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wlbjguwhbf .gt_left { text-align: left; }
 #wlbjguwhbf .gt_center { text-align: center; }
 #wlbjguwhbf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wlbjguwhbf .gt_font_normal { font-weight: normal; }
 #wlbjguwhbf .gt_font_bold { font-weight: bold; }
 #wlbjguwhbf .gt_font_italic { font-style: italic; }
 #wlbjguwhbf .gt_super { font-size: 65%; }
 #wlbjguwhbf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wlbjguwhbf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wlbjguwhbf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wlbjguwhbf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wlbjguwhbf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wlbjguwhbf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lovnqmwdoh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lovnqmwdoh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lovnqmwdoh p { margin: 0; padding: 0; }
 #lovnqmwdoh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lovnqmwdoh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lovnqmwdoh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lovnqmwdoh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lovnqmwdoh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lovnqmwdoh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lovnqmwdoh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lovnqmwdoh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lovnqmwdoh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lovnqmwdoh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lovnqmwdoh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lovnqmwdoh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lovnqmwdoh .gt_spanner_row { border-bottom-style: hidden; }
 #lovnqmwdoh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lovnqmwdoh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lovnqmwdoh .gt_from_md> :first-child { margin-top: 0; }
 #lovnqmwdoh .gt_from_md> :last-child { margin-bottom: 0; }
 #lovnqmwdoh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lovnqmwdoh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lovnqmwdoh .gt_indent_1 { text-indent: 5px; }
 #lovnqmwdoh .gt_indent_2 { text-indent: calc(5px * 2); }
 #lovnqmwdoh .gt_indent_3 { text-indent: calc(5px * 3); }
 #lovnqmwdoh .gt_indent_4 { text-indent: calc(5px * 4); }
 #lovnqmwdoh .gt_indent_5 { text-indent: calc(5px * 5); }
 #lovnqmwdoh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lovnqmwdoh .gt_row_group_first td { border-top-width: 2px; }
 #lovnqmwdoh .gt_row_group_first th { border-top-width: 2px; }
 #lovnqmwdoh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lovnqmwdoh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lovnqmwdoh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lovnqmwdoh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lovnqmwdoh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lovnqmwdoh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lovnqmwdoh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lovnqmwdoh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lovnqmwdoh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lovnqmwdoh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lovnqmwdoh .gt_left { text-align: left; }
 #lovnqmwdoh .gt_center { text-align: center; }
 #lovnqmwdoh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lovnqmwdoh .gt_font_normal { font-weight: normal; }
 #lovnqmwdoh .gt_font_bold { font-weight: bold; }
 #lovnqmwdoh .gt_font_italic { font-style: italic; }
 #lovnqmwdoh .gt_super { font-size: 65%; }
 #lovnqmwdoh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lovnqmwdoh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lovnqmwdoh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lovnqmwdoh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lovnqmwdoh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lovnqmwdoh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#nhjxzftwcf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nhjxzftwcf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nhjxzftwcf p { margin: 0; padding: 0; }
 #nhjxzftwcf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nhjxzftwcf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nhjxzftwcf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nhjxzftwcf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nhjxzftwcf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nhjxzftwcf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nhjxzftwcf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nhjxzftwcf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nhjxzftwcf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nhjxzftwcf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nhjxzftwcf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nhjxzftwcf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nhjxzftwcf .gt_spanner_row { border-bottom-style: hidden; }
 #nhjxzftwcf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nhjxzftwcf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nhjxzftwcf .gt_from_md> :first-child { margin-top: 0; }
 #nhjxzftwcf .gt_from_md> :last-child { margin-bottom: 0; }
 #nhjxzftwcf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nhjxzftwcf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nhjxzftwcf .gt_indent_1 { text-indent: 5px; }
 #nhjxzftwcf .gt_indent_2 { text-indent: calc(5px * 2); }
 #nhjxzftwcf .gt_indent_3 { text-indent: calc(5px * 3); }
 #nhjxzftwcf .gt_indent_4 { text-indent: calc(5px * 4); }
 #nhjxzftwcf .gt_indent_5 { text-indent: calc(5px * 5); }
 #nhjxzftwcf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nhjxzftwcf .gt_row_group_first td { border-top-width: 2px; }
 #nhjxzftwcf .gt_row_group_first th { border-top-width: 2px; }
 #nhjxzftwcf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nhjxzftwcf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nhjxzftwcf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nhjxzftwcf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nhjxzftwcf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nhjxzftwcf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nhjxzftwcf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nhjxzftwcf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nhjxzftwcf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nhjxzftwcf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nhjxzftwcf .gt_left { text-align: left; }
 #nhjxzftwcf .gt_center { text-align: center; }
 #nhjxzftwcf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nhjxzftwcf .gt_font_normal { font-weight: normal; }
 #nhjxzftwcf .gt_font_bold { font-weight: bold; }
 #nhjxzftwcf .gt_font_italic { font-style: italic; }
 #nhjxzftwcf .gt_super { font-size: 65%; }
 #nhjxzftwcf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nhjxzftwcf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nhjxzftwcf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nhjxzftwcf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nhjxzftwcf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nhjxzftwcf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#foehoaydbh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#foehoaydbh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#foehoaydbh p { margin: 0; padding: 0; }
 #foehoaydbh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #foehoaydbh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #foehoaydbh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #foehoaydbh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #foehoaydbh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #foehoaydbh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #foehoaydbh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #foehoaydbh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #foehoaydbh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #foehoaydbh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #foehoaydbh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #foehoaydbh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #foehoaydbh .gt_spanner_row { border-bottom-style: hidden; }
 #foehoaydbh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #foehoaydbh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #foehoaydbh .gt_from_md> :first-child { margin-top: 0; }
 #foehoaydbh .gt_from_md> :last-child { margin-bottom: 0; }
 #foehoaydbh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #foehoaydbh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #foehoaydbh .gt_indent_1 { text-indent: 5px; }
 #foehoaydbh .gt_indent_2 { text-indent: calc(5px * 2); }
 #foehoaydbh .gt_indent_3 { text-indent: calc(5px * 3); }
 #foehoaydbh .gt_indent_4 { text-indent: calc(5px * 4); }
 #foehoaydbh .gt_indent_5 { text-indent: calc(5px * 5); }
 #foehoaydbh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #foehoaydbh .gt_row_group_first td { border-top-width: 2px; }
 #foehoaydbh .gt_row_group_first th { border-top-width: 2px; }
 #foehoaydbh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #foehoaydbh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #foehoaydbh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #foehoaydbh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #foehoaydbh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #foehoaydbh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #foehoaydbh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #foehoaydbh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #foehoaydbh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #foehoaydbh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #foehoaydbh .gt_left { text-align: left; }
 #foehoaydbh .gt_center { text-align: center; }
 #foehoaydbh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #foehoaydbh .gt_font_normal { font-weight: normal; }
 #foehoaydbh .gt_font_bold { font-weight: bold; }
 #foehoaydbh .gt_font_italic { font-style: italic; }
 #foehoaydbh .gt_super { font-size: 65%; }
 #foehoaydbh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #foehoaydbh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #foehoaydbh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #foehoaydbh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #foehoaydbh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #foehoaydbh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tktzuawgaa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tktzuawgaa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tktzuawgaa p { margin: 0; padding: 0; }
 #tktzuawgaa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tktzuawgaa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tktzuawgaa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tktzuawgaa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tktzuawgaa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tktzuawgaa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tktzuawgaa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tktzuawgaa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tktzuawgaa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tktzuawgaa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tktzuawgaa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tktzuawgaa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tktzuawgaa .gt_spanner_row { border-bottom-style: hidden; }
 #tktzuawgaa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tktzuawgaa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tktzuawgaa .gt_from_md> :first-child { margin-top: 0; }
 #tktzuawgaa .gt_from_md> :last-child { margin-bottom: 0; }
 #tktzuawgaa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tktzuawgaa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tktzuawgaa .gt_indent_1 { text-indent: 5px; }
 #tktzuawgaa .gt_indent_2 { text-indent: calc(5px * 2); }
 #tktzuawgaa .gt_indent_3 { text-indent: calc(5px * 3); }
 #tktzuawgaa .gt_indent_4 { text-indent: calc(5px * 4); }
 #tktzuawgaa .gt_indent_5 { text-indent: calc(5px * 5); }
 #tktzuawgaa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tktzuawgaa .gt_row_group_first td { border-top-width: 2px; }
 #tktzuawgaa .gt_row_group_first th { border-top-width: 2px; }
 #tktzuawgaa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tktzuawgaa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tktzuawgaa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tktzuawgaa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tktzuawgaa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tktzuawgaa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tktzuawgaa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tktzuawgaa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tktzuawgaa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tktzuawgaa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tktzuawgaa .gt_left { text-align: left; }
 #tktzuawgaa .gt_center { text-align: center; }
 #tktzuawgaa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tktzuawgaa .gt_font_normal { font-weight: normal; }
 #tktzuawgaa .gt_font_bold { font-weight: bold; }
 #tktzuawgaa .gt_font_italic { font-style: italic; }
 #tktzuawgaa .gt_super { font-size: 65%; }
 #tktzuawgaa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tktzuawgaa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tktzuawgaa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tktzuawgaa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tktzuawgaa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tktzuawgaa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ystuvfubei table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ystuvfubei thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ystuvfubei p { margin: 0; padding: 0; }
 #ystuvfubei .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ystuvfubei .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ystuvfubei .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ystuvfubei .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ystuvfubei .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ystuvfubei .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ystuvfubei .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ystuvfubei .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ystuvfubei .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ystuvfubei .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ystuvfubei .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ystuvfubei .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ystuvfubei .gt_spanner_row { border-bottom-style: hidden; }
 #ystuvfubei .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ystuvfubei .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ystuvfubei .gt_from_md> :first-child { margin-top: 0; }
 #ystuvfubei .gt_from_md> :last-child { margin-bottom: 0; }
 #ystuvfubei .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ystuvfubei .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ystuvfubei .gt_indent_1 { text-indent: 5px; }
 #ystuvfubei .gt_indent_2 { text-indent: calc(5px * 2); }
 #ystuvfubei .gt_indent_3 { text-indent: calc(5px * 3); }
 #ystuvfubei .gt_indent_4 { text-indent: calc(5px * 4); }
 #ystuvfubei .gt_indent_5 { text-indent: calc(5px * 5); }
 #ystuvfubei .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ystuvfubei .gt_row_group_first td { border-top-width: 2px; }
 #ystuvfubei .gt_row_group_first th { border-top-width: 2px; }
 #ystuvfubei .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ystuvfubei .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ystuvfubei .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ystuvfubei .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ystuvfubei .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ystuvfubei .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ystuvfubei .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ystuvfubei .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ystuvfubei .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ystuvfubei .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ystuvfubei .gt_left { text-align: left; }
 #ystuvfubei .gt_center { text-align: center; }
 #ystuvfubei .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ystuvfubei .gt_font_normal { font-weight: normal; }
 #ystuvfubei .gt_font_bold { font-weight: bold; }
 #ystuvfubei .gt_font_italic { font-style: italic; }
 #ystuvfubei .gt_super { font-size: 65%; }
 #ystuvfubei .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ystuvfubei .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ystuvfubei .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ystuvfubei .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ystuvfubei .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ystuvfubei .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ngmhwvduuq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ngmhwvduuq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ngmhwvduuq p { margin: 0; padding: 0; }
 #ngmhwvduuq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ngmhwvduuq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ngmhwvduuq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ngmhwvduuq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ngmhwvduuq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ngmhwvduuq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngmhwvduuq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ngmhwvduuq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ngmhwvduuq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ngmhwvduuq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ngmhwvduuq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ngmhwvduuq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ngmhwvduuq .gt_spanner_row { border-bottom-style: hidden; }
 #ngmhwvduuq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ngmhwvduuq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ngmhwvduuq .gt_from_md> :first-child { margin-top: 0; }
 #ngmhwvduuq .gt_from_md> :last-child { margin-bottom: 0; }
 #ngmhwvduuq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ngmhwvduuq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ngmhwvduuq .gt_indent_1 { text-indent: 5px; }
 #ngmhwvduuq .gt_indent_2 { text-indent: calc(5px * 2); }
 #ngmhwvduuq .gt_indent_3 { text-indent: calc(5px * 3); }
 #ngmhwvduuq .gt_indent_4 { text-indent: calc(5px * 4); }
 #ngmhwvduuq .gt_indent_5 { text-indent: calc(5px * 5); }
 #ngmhwvduuq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ngmhwvduuq .gt_row_group_first td { border-top-width: 2px; }
 #ngmhwvduuq .gt_row_group_first th { border-top-width: 2px; }
 #ngmhwvduuq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ngmhwvduuq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngmhwvduuq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ngmhwvduuq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ngmhwvduuq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngmhwvduuq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ngmhwvduuq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ngmhwvduuq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ngmhwvduuq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngmhwvduuq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ngmhwvduuq .gt_left { text-align: left; }
 #ngmhwvduuq .gt_center { text-align: center; }
 #ngmhwvduuq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ngmhwvduuq .gt_font_normal { font-weight: normal; }
 #ngmhwvduuq .gt_font_bold { font-weight: bold; }
 #ngmhwvduuq .gt_font_italic { font-style: italic; }
 #ngmhwvduuq .gt_super { font-size: 65%; }
 #ngmhwvduuq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngmhwvduuq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ngmhwvduuq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngmhwvduuq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ngmhwvduuq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ngmhwvduuq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#genkiqjcce table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#genkiqjcce thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#genkiqjcce p { margin: 0; padding: 0; }
 #genkiqjcce .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #genkiqjcce .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #genkiqjcce .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #genkiqjcce .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #genkiqjcce .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #genkiqjcce .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #genkiqjcce .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #genkiqjcce .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #genkiqjcce .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #genkiqjcce .gt_column_spanner_outer:first-child { padding-left: 0; }
 #genkiqjcce .gt_column_spanner_outer:last-child { padding-right: 0; }
 #genkiqjcce .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #genkiqjcce .gt_spanner_row { border-bottom-style: hidden; }
 #genkiqjcce .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #genkiqjcce .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #genkiqjcce .gt_from_md> :first-child { margin-top: 0; }
 #genkiqjcce .gt_from_md> :last-child { margin-bottom: 0; }
 #genkiqjcce .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #genkiqjcce .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #genkiqjcce .gt_indent_1 { text-indent: 5px; }
 #genkiqjcce .gt_indent_2 { text-indent: calc(5px * 2); }
 #genkiqjcce .gt_indent_3 { text-indent: calc(5px * 3); }
 #genkiqjcce .gt_indent_4 { text-indent: calc(5px * 4); }
 #genkiqjcce .gt_indent_5 { text-indent: calc(5px * 5); }
 #genkiqjcce .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #genkiqjcce .gt_row_group_first td { border-top-width: 2px; }
 #genkiqjcce .gt_row_group_first th { border-top-width: 2px; }
 #genkiqjcce .gt_striped { color: #333333; background-color: #F4F4F4; }
 #genkiqjcce .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #genkiqjcce .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #genkiqjcce .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #genkiqjcce .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #genkiqjcce .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #genkiqjcce .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #genkiqjcce .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #genkiqjcce .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #genkiqjcce .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #genkiqjcce .gt_left { text-align: left; }
 #genkiqjcce .gt_center { text-align: center; }
 #genkiqjcce .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #genkiqjcce .gt_font_normal { font-weight: normal; }
 #genkiqjcce .gt_font_bold { font-weight: bold; }
 #genkiqjcce .gt_font_italic { font-style: italic; }
 #genkiqjcce .gt_super { font-size: 65%; }
 #genkiqjcce .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #genkiqjcce .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #genkiqjcce .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #genkiqjcce .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #genkiqjcce .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #genkiqjcce .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
