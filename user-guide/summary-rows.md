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
#dxmwtsvvxi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dxmwtsvvxi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dxmwtsvvxi p { margin: 0; padding: 0; }
 #dxmwtsvvxi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dxmwtsvvxi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dxmwtsvvxi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dxmwtsvvxi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dxmwtsvvxi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxmwtsvvxi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxmwtsvvxi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxmwtsvvxi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dxmwtsvvxi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dxmwtsvvxi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dxmwtsvvxi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dxmwtsvvxi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dxmwtsvvxi .gt_spanner_row { border-bottom-style: hidden; }
 #dxmwtsvvxi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dxmwtsvvxi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dxmwtsvvxi .gt_from_md> :first-child { margin-top: 0; }
 #dxmwtsvvxi .gt_from_md> :last-child { margin-bottom: 0; }
 #dxmwtsvvxi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dxmwtsvvxi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dxmwtsvvxi .gt_indent_1 { text-indent: 5px; }
 #dxmwtsvvxi .gt_indent_2 { text-indent: calc(5px * 2); }
 #dxmwtsvvxi .gt_indent_3 { text-indent: calc(5px * 3); }
 #dxmwtsvvxi .gt_indent_4 { text-indent: calc(5px * 4); }
 #dxmwtsvvxi .gt_indent_5 { text-indent: calc(5px * 5); }
 #dxmwtsvvxi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dxmwtsvvxi .gt_row_group_first td { border-top-width: 2px; }
 #dxmwtsvvxi .gt_row_group_first th { border-top-width: 2px; }
 #dxmwtsvvxi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dxmwtsvvxi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxmwtsvvxi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxmwtsvvxi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dxmwtsvvxi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxmwtsvvxi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxmwtsvvxi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dxmwtsvvxi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dxmwtsvvxi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxmwtsvvxi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxmwtsvvxi .gt_left { text-align: left; }
 #dxmwtsvvxi .gt_center { text-align: center; }
 #dxmwtsvvxi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dxmwtsvvxi .gt_font_normal { font-weight: normal; }
 #dxmwtsvvxi .gt_font_bold { font-weight: bold; }
 #dxmwtsvvxi .gt_font_italic { font-style: italic; }
 #dxmwtsvvxi .gt_super { font-size: 65%; }
 #dxmwtsvvxi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxmwtsvvxi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dxmwtsvvxi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxmwtsvvxi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxmwtsvvxi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dxmwtsvvxi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bsbylbzuht table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bsbylbzuht thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bsbylbzuht p { margin: 0; padding: 0; }
 #bsbylbzuht .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bsbylbzuht .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bsbylbzuht .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bsbylbzuht .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bsbylbzuht .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bsbylbzuht .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bsbylbzuht .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bsbylbzuht .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bsbylbzuht .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bsbylbzuht .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bsbylbzuht .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bsbylbzuht .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bsbylbzuht .gt_spanner_row { border-bottom-style: hidden; }
 #bsbylbzuht .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bsbylbzuht .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bsbylbzuht .gt_from_md> :first-child { margin-top: 0; }
 #bsbylbzuht .gt_from_md> :last-child { margin-bottom: 0; }
 #bsbylbzuht .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bsbylbzuht .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bsbylbzuht .gt_indent_1 { text-indent: 5px; }
 #bsbylbzuht .gt_indent_2 { text-indent: calc(5px * 2); }
 #bsbylbzuht .gt_indent_3 { text-indent: calc(5px * 3); }
 #bsbylbzuht .gt_indent_4 { text-indent: calc(5px * 4); }
 #bsbylbzuht .gt_indent_5 { text-indent: calc(5px * 5); }
 #bsbylbzuht .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bsbylbzuht .gt_row_group_first td { border-top-width: 2px; }
 #bsbylbzuht .gt_row_group_first th { border-top-width: 2px; }
 #bsbylbzuht .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bsbylbzuht .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bsbylbzuht .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bsbylbzuht .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bsbylbzuht .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bsbylbzuht .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bsbylbzuht .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bsbylbzuht .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bsbylbzuht .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bsbylbzuht .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bsbylbzuht .gt_left { text-align: left; }
 #bsbylbzuht .gt_center { text-align: center; }
 #bsbylbzuht .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bsbylbzuht .gt_font_normal { font-weight: normal; }
 #bsbylbzuht .gt_font_bold { font-weight: bold; }
 #bsbylbzuht .gt_font_italic { font-style: italic; }
 #bsbylbzuht .gt_super { font-size: 65%; }
 #bsbylbzuht .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bsbylbzuht .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bsbylbzuht .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bsbylbzuht .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bsbylbzuht .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bsbylbzuht .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#opggkabawh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#opggkabawh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#opggkabawh p { margin: 0; padding: 0; }
 #opggkabawh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #opggkabawh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #opggkabawh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #opggkabawh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #opggkabawh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #opggkabawh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #opggkabawh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #opggkabawh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #opggkabawh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #opggkabawh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #opggkabawh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #opggkabawh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #opggkabawh .gt_spanner_row { border-bottom-style: hidden; }
 #opggkabawh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #opggkabawh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #opggkabawh .gt_from_md> :first-child { margin-top: 0; }
 #opggkabawh .gt_from_md> :last-child { margin-bottom: 0; }
 #opggkabawh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #opggkabawh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #opggkabawh .gt_indent_1 { text-indent: 5px; }
 #opggkabawh .gt_indent_2 { text-indent: calc(5px * 2); }
 #opggkabawh .gt_indent_3 { text-indent: calc(5px * 3); }
 #opggkabawh .gt_indent_4 { text-indent: calc(5px * 4); }
 #opggkabawh .gt_indent_5 { text-indent: calc(5px * 5); }
 #opggkabawh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #opggkabawh .gt_row_group_first td { border-top-width: 2px; }
 #opggkabawh .gt_row_group_first th { border-top-width: 2px; }
 #opggkabawh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #opggkabawh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #opggkabawh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #opggkabawh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #opggkabawh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #opggkabawh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #opggkabawh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #opggkabawh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #opggkabawh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #opggkabawh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #opggkabawh .gt_left { text-align: left; }
 #opggkabawh .gt_center { text-align: center; }
 #opggkabawh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #opggkabawh .gt_font_normal { font-weight: normal; }
 #opggkabawh .gt_font_bold { font-weight: bold; }
 #opggkabawh .gt_font_italic { font-style: italic; }
 #opggkabawh .gt_super { font-size: 65%; }
 #opggkabawh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #opggkabawh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #opggkabawh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #opggkabawh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #opggkabawh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #opggkabawh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ophrayaops table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ophrayaops thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ophrayaops p { margin: 0; padding: 0; }
 #ophrayaops .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ophrayaops .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ophrayaops .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ophrayaops .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ophrayaops .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ophrayaops .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ophrayaops .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ophrayaops .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ophrayaops .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ophrayaops .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ophrayaops .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ophrayaops .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ophrayaops .gt_spanner_row { border-bottom-style: hidden; }
 #ophrayaops .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ophrayaops .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ophrayaops .gt_from_md> :first-child { margin-top: 0; }
 #ophrayaops .gt_from_md> :last-child { margin-bottom: 0; }
 #ophrayaops .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ophrayaops .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ophrayaops .gt_indent_1 { text-indent: 5px; }
 #ophrayaops .gt_indent_2 { text-indent: calc(5px * 2); }
 #ophrayaops .gt_indent_3 { text-indent: calc(5px * 3); }
 #ophrayaops .gt_indent_4 { text-indent: calc(5px * 4); }
 #ophrayaops .gt_indent_5 { text-indent: calc(5px * 5); }
 #ophrayaops .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ophrayaops .gt_row_group_first td { border-top-width: 2px; }
 #ophrayaops .gt_row_group_first th { border-top-width: 2px; }
 #ophrayaops .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ophrayaops .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ophrayaops .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ophrayaops .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ophrayaops .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ophrayaops .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ophrayaops .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ophrayaops .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ophrayaops .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ophrayaops .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ophrayaops .gt_left { text-align: left; }
 #ophrayaops .gt_center { text-align: center; }
 #ophrayaops .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ophrayaops .gt_font_normal { font-weight: normal; }
 #ophrayaops .gt_font_bold { font-weight: bold; }
 #ophrayaops .gt_font_italic { font-style: italic; }
 #ophrayaops .gt_super { font-size: 65%; }
 #ophrayaops .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ophrayaops .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ophrayaops .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ophrayaops .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ophrayaops .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ophrayaops .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ninrippmps table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ninrippmps thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ninrippmps p { margin: 0; padding: 0; }
 #ninrippmps .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ninrippmps .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ninrippmps .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ninrippmps .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ninrippmps .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ninrippmps .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ninrippmps .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ninrippmps .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ninrippmps .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ninrippmps .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ninrippmps .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ninrippmps .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ninrippmps .gt_spanner_row { border-bottom-style: hidden; }
 #ninrippmps .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ninrippmps .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ninrippmps .gt_from_md> :first-child { margin-top: 0; }
 #ninrippmps .gt_from_md> :last-child { margin-bottom: 0; }
 #ninrippmps .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ninrippmps .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ninrippmps .gt_indent_1 { text-indent: 5px; }
 #ninrippmps .gt_indent_2 { text-indent: calc(5px * 2); }
 #ninrippmps .gt_indent_3 { text-indent: calc(5px * 3); }
 #ninrippmps .gt_indent_4 { text-indent: calc(5px * 4); }
 #ninrippmps .gt_indent_5 { text-indent: calc(5px * 5); }
 #ninrippmps .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ninrippmps .gt_row_group_first td { border-top-width: 2px; }
 #ninrippmps .gt_row_group_first th { border-top-width: 2px; }
 #ninrippmps .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ninrippmps .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ninrippmps .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ninrippmps .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ninrippmps .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ninrippmps .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ninrippmps .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ninrippmps .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ninrippmps .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ninrippmps .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ninrippmps .gt_left { text-align: left; }
 #ninrippmps .gt_center { text-align: center; }
 #ninrippmps .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ninrippmps .gt_font_normal { font-weight: normal; }
 #ninrippmps .gt_font_bold { font-weight: bold; }
 #ninrippmps .gt_font_italic { font-style: italic; }
 #ninrippmps .gt_super { font-size: 65%; }
 #ninrippmps .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ninrippmps .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ninrippmps .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ninrippmps .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ninrippmps .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ninrippmps .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mmcjddmury table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mmcjddmury thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mmcjddmury p { margin: 0; padding: 0; }
 #mmcjddmury .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mmcjddmury .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mmcjddmury .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mmcjddmury .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mmcjddmury .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mmcjddmury .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mmcjddmury .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mmcjddmury .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mmcjddmury .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mmcjddmury .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mmcjddmury .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mmcjddmury .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mmcjddmury .gt_spanner_row { border-bottom-style: hidden; }
 #mmcjddmury .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mmcjddmury .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mmcjddmury .gt_from_md> :first-child { margin-top: 0; }
 #mmcjddmury .gt_from_md> :last-child { margin-bottom: 0; }
 #mmcjddmury .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mmcjddmury .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mmcjddmury .gt_indent_1 { text-indent: 5px; }
 #mmcjddmury .gt_indent_2 { text-indent: calc(5px * 2); }
 #mmcjddmury .gt_indent_3 { text-indent: calc(5px * 3); }
 #mmcjddmury .gt_indent_4 { text-indent: calc(5px * 4); }
 #mmcjddmury .gt_indent_5 { text-indent: calc(5px * 5); }
 #mmcjddmury .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mmcjddmury .gt_row_group_first td { border-top-width: 2px; }
 #mmcjddmury .gt_row_group_first th { border-top-width: 2px; }
 #mmcjddmury .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mmcjddmury .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mmcjddmury .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mmcjddmury .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mmcjddmury .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mmcjddmury .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mmcjddmury .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mmcjddmury .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mmcjddmury .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mmcjddmury .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mmcjddmury .gt_left { text-align: left; }
 #mmcjddmury .gt_center { text-align: center; }
 #mmcjddmury .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mmcjddmury .gt_font_normal { font-weight: normal; }
 #mmcjddmury .gt_font_bold { font-weight: bold; }
 #mmcjddmury .gt_font_italic { font-style: italic; }
 #mmcjddmury .gt_super { font-size: 65%; }
 #mmcjddmury .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mmcjddmury .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mmcjddmury .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mmcjddmury .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mmcjddmury .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mmcjddmury .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kopetwiywb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kopetwiywb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kopetwiywb p { margin: 0; padding: 0; }
 #kopetwiywb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kopetwiywb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kopetwiywb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kopetwiywb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kopetwiywb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kopetwiywb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kopetwiywb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kopetwiywb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kopetwiywb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kopetwiywb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kopetwiywb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kopetwiywb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kopetwiywb .gt_spanner_row { border-bottom-style: hidden; }
 #kopetwiywb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kopetwiywb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kopetwiywb .gt_from_md> :first-child { margin-top: 0; }
 #kopetwiywb .gt_from_md> :last-child { margin-bottom: 0; }
 #kopetwiywb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kopetwiywb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kopetwiywb .gt_indent_1 { text-indent: 5px; }
 #kopetwiywb .gt_indent_2 { text-indent: calc(5px * 2); }
 #kopetwiywb .gt_indent_3 { text-indent: calc(5px * 3); }
 #kopetwiywb .gt_indent_4 { text-indent: calc(5px * 4); }
 #kopetwiywb .gt_indent_5 { text-indent: calc(5px * 5); }
 #kopetwiywb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kopetwiywb .gt_row_group_first td { border-top-width: 2px; }
 #kopetwiywb .gt_row_group_first th { border-top-width: 2px; }
 #kopetwiywb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kopetwiywb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kopetwiywb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kopetwiywb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kopetwiywb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kopetwiywb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kopetwiywb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kopetwiywb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kopetwiywb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kopetwiywb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kopetwiywb .gt_left { text-align: left; }
 #kopetwiywb .gt_center { text-align: center; }
 #kopetwiywb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kopetwiywb .gt_font_normal { font-weight: normal; }
 #kopetwiywb .gt_font_bold { font-weight: bold; }
 #kopetwiywb .gt_font_italic { font-style: italic; }
 #kopetwiywb .gt_super { font-size: 65%; }
 #kopetwiywb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kopetwiywb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kopetwiywb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kopetwiywb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kopetwiywb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kopetwiywb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#eyyrdmbxvn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eyyrdmbxvn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eyyrdmbxvn p { margin: 0; padding: 0; }
 #eyyrdmbxvn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eyyrdmbxvn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eyyrdmbxvn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eyyrdmbxvn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eyyrdmbxvn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eyyrdmbxvn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyyrdmbxvn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eyyrdmbxvn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eyyrdmbxvn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eyyrdmbxvn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eyyrdmbxvn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eyyrdmbxvn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eyyrdmbxvn .gt_spanner_row { border-bottom-style: hidden; }
 #eyyrdmbxvn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eyyrdmbxvn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eyyrdmbxvn .gt_from_md> :first-child { margin-top: 0; }
 #eyyrdmbxvn .gt_from_md> :last-child { margin-bottom: 0; }
 #eyyrdmbxvn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eyyrdmbxvn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eyyrdmbxvn .gt_indent_1 { text-indent: 5px; }
 #eyyrdmbxvn .gt_indent_2 { text-indent: calc(5px * 2); }
 #eyyrdmbxvn .gt_indent_3 { text-indent: calc(5px * 3); }
 #eyyrdmbxvn .gt_indent_4 { text-indent: calc(5px * 4); }
 #eyyrdmbxvn .gt_indent_5 { text-indent: calc(5px * 5); }
 #eyyrdmbxvn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eyyrdmbxvn .gt_row_group_first td { border-top-width: 2px; }
 #eyyrdmbxvn .gt_row_group_first th { border-top-width: 2px; }
 #eyyrdmbxvn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eyyrdmbxvn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyyrdmbxvn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eyyrdmbxvn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eyyrdmbxvn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyyrdmbxvn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eyyrdmbxvn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eyyrdmbxvn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eyyrdmbxvn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyyrdmbxvn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eyyrdmbxvn .gt_left { text-align: left; }
 #eyyrdmbxvn .gt_center { text-align: center; }
 #eyyrdmbxvn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eyyrdmbxvn .gt_font_normal { font-weight: normal; }
 #eyyrdmbxvn .gt_font_bold { font-weight: bold; }
 #eyyrdmbxvn .gt_font_italic { font-style: italic; }
 #eyyrdmbxvn .gt_super { font-size: 65%; }
 #eyyrdmbxvn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyyrdmbxvn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eyyrdmbxvn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyyrdmbxvn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eyyrdmbxvn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eyyrdmbxvn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#czndrunwwj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#czndrunwwj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#czndrunwwj p { margin: 0; padding: 0; }
 #czndrunwwj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #czndrunwwj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #czndrunwwj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #czndrunwwj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #czndrunwwj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #czndrunwwj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #czndrunwwj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #czndrunwwj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #czndrunwwj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #czndrunwwj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #czndrunwwj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #czndrunwwj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #czndrunwwj .gt_spanner_row { border-bottom-style: hidden; }
 #czndrunwwj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #czndrunwwj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #czndrunwwj .gt_from_md> :first-child { margin-top: 0; }
 #czndrunwwj .gt_from_md> :last-child { margin-bottom: 0; }
 #czndrunwwj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #czndrunwwj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #czndrunwwj .gt_indent_1 { text-indent: 5px; }
 #czndrunwwj .gt_indent_2 { text-indent: calc(5px * 2); }
 #czndrunwwj .gt_indent_3 { text-indent: calc(5px * 3); }
 #czndrunwwj .gt_indent_4 { text-indent: calc(5px * 4); }
 #czndrunwwj .gt_indent_5 { text-indent: calc(5px * 5); }
 #czndrunwwj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #czndrunwwj .gt_row_group_first td { border-top-width: 2px; }
 #czndrunwwj .gt_row_group_first th { border-top-width: 2px; }
 #czndrunwwj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #czndrunwwj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #czndrunwwj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #czndrunwwj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #czndrunwwj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #czndrunwwj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #czndrunwwj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #czndrunwwj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #czndrunwwj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #czndrunwwj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #czndrunwwj .gt_left { text-align: left; }
 #czndrunwwj .gt_center { text-align: center; }
 #czndrunwwj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #czndrunwwj .gt_font_normal { font-weight: normal; }
 #czndrunwwj .gt_font_bold { font-weight: bold; }
 #czndrunwwj .gt_font_italic { font-style: italic; }
 #czndrunwwj .gt_super { font-size: 65%; }
 #czndrunwwj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #czndrunwwj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #czndrunwwj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #czndrunwwj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #czndrunwwj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #czndrunwwj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
