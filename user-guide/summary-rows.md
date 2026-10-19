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
#zyfmttnekp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zyfmttnekp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zyfmttnekp p { margin: 0; padding: 0; }
 #zyfmttnekp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zyfmttnekp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zyfmttnekp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zyfmttnekp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zyfmttnekp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zyfmttnekp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zyfmttnekp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zyfmttnekp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zyfmttnekp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zyfmttnekp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zyfmttnekp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zyfmttnekp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zyfmttnekp .gt_spanner_row { border-bottom-style: hidden; }
 #zyfmttnekp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zyfmttnekp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zyfmttnekp .gt_from_md> :first-child { margin-top: 0; }
 #zyfmttnekp .gt_from_md> :last-child { margin-bottom: 0; }
 #zyfmttnekp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zyfmttnekp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zyfmttnekp .gt_indent_1 { text-indent: 5px; }
 #zyfmttnekp .gt_indent_2 { text-indent: calc(5px * 2); }
 #zyfmttnekp .gt_indent_3 { text-indent: calc(5px * 3); }
 #zyfmttnekp .gt_indent_4 { text-indent: calc(5px * 4); }
 #zyfmttnekp .gt_indent_5 { text-indent: calc(5px * 5); }
 #zyfmttnekp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zyfmttnekp .gt_row_group_first td { border-top-width: 2px; }
 #zyfmttnekp .gt_row_group_first th { border-top-width: 2px; }
 #zyfmttnekp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zyfmttnekp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zyfmttnekp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zyfmttnekp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zyfmttnekp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zyfmttnekp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zyfmttnekp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zyfmttnekp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zyfmttnekp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zyfmttnekp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zyfmttnekp .gt_left { text-align: left; }
 #zyfmttnekp .gt_center { text-align: center; }
 #zyfmttnekp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zyfmttnekp .gt_font_normal { font-weight: normal; }
 #zyfmttnekp .gt_font_bold { font-weight: bold; }
 #zyfmttnekp .gt_font_italic { font-style: italic; }
 #zyfmttnekp .gt_super { font-size: 65%; }
 #zyfmttnekp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zyfmttnekp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zyfmttnekp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zyfmttnekp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zyfmttnekp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zyfmttnekp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kbfscjctva table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kbfscjctva thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kbfscjctva p { margin: 0; padding: 0; }
 #kbfscjctva .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kbfscjctva .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kbfscjctva .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kbfscjctva .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kbfscjctva .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kbfscjctva .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kbfscjctva .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kbfscjctva .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kbfscjctva .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kbfscjctva .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kbfscjctva .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kbfscjctva .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kbfscjctva .gt_spanner_row { border-bottom-style: hidden; }
 #kbfscjctva .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kbfscjctva .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kbfscjctva .gt_from_md> :first-child { margin-top: 0; }
 #kbfscjctva .gt_from_md> :last-child { margin-bottom: 0; }
 #kbfscjctva .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kbfscjctva .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kbfscjctva .gt_indent_1 { text-indent: 5px; }
 #kbfscjctva .gt_indent_2 { text-indent: calc(5px * 2); }
 #kbfscjctva .gt_indent_3 { text-indent: calc(5px * 3); }
 #kbfscjctva .gt_indent_4 { text-indent: calc(5px * 4); }
 #kbfscjctva .gt_indent_5 { text-indent: calc(5px * 5); }
 #kbfscjctva .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kbfscjctva .gt_row_group_first td { border-top-width: 2px; }
 #kbfscjctva .gt_row_group_first th { border-top-width: 2px; }
 #kbfscjctva .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kbfscjctva .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kbfscjctva .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kbfscjctva .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kbfscjctva .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kbfscjctva .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kbfscjctva .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kbfscjctva .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kbfscjctva .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kbfscjctva .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kbfscjctva .gt_left { text-align: left; }
 #kbfscjctva .gt_center { text-align: center; }
 #kbfscjctva .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kbfscjctva .gt_font_normal { font-weight: normal; }
 #kbfscjctva .gt_font_bold { font-weight: bold; }
 #kbfscjctva .gt_font_italic { font-style: italic; }
 #kbfscjctva .gt_super { font-size: 65%; }
 #kbfscjctva .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kbfscjctva .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kbfscjctva .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kbfscjctva .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kbfscjctva .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kbfscjctva .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bgaxcqycmi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bgaxcqycmi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bgaxcqycmi p { margin: 0; padding: 0; }
 #bgaxcqycmi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bgaxcqycmi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bgaxcqycmi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bgaxcqycmi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bgaxcqycmi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bgaxcqycmi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bgaxcqycmi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bgaxcqycmi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bgaxcqycmi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bgaxcqycmi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bgaxcqycmi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bgaxcqycmi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bgaxcqycmi .gt_spanner_row { border-bottom-style: hidden; }
 #bgaxcqycmi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bgaxcqycmi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bgaxcqycmi .gt_from_md> :first-child { margin-top: 0; }
 #bgaxcqycmi .gt_from_md> :last-child { margin-bottom: 0; }
 #bgaxcqycmi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bgaxcqycmi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bgaxcqycmi .gt_indent_1 { text-indent: 5px; }
 #bgaxcqycmi .gt_indent_2 { text-indent: calc(5px * 2); }
 #bgaxcqycmi .gt_indent_3 { text-indent: calc(5px * 3); }
 #bgaxcqycmi .gt_indent_4 { text-indent: calc(5px * 4); }
 #bgaxcqycmi .gt_indent_5 { text-indent: calc(5px * 5); }
 #bgaxcqycmi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bgaxcqycmi .gt_row_group_first td { border-top-width: 2px; }
 #bgaxcqycmi .gt_row_group_first th { border-top-width: 2px; }
 #bgaxcqycmi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bgaxcqycmi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bgaxcqycmi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bgaxcqycmi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bgaxcqycmi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bgaxcqycmi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bgaxcqycmi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bgaxcqycmi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bgaxcqycmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bgaxcqycmi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bgaxcqycmi .gt_left { text-align: left; }
 #bgaxcqycmi .gt_center { text-align: center; }
 #bgaxcqycmi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bgaxcqycmi .gt_font_normal { font-weight: normal; }
 #bgaxcqycmi .gt_font_bold { font-weight: bold; }
 #bgaxcqycmi .gt_font_italic { font-style: italic; }
 #bgaxcqycmi .gt_super { font-size: 65%; }
 #bgaxcqycmi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bgaxcqycmi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bgaxcqycmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bgaxcqycmi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bgaxcqycmi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bgaxcqycmi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tfdjsxwcwq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tfdjsxwcwq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tfdjsxwcwq p { margin: 0; padding: 0; }
 #tfdjsxwcwq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tfdjsxwcwq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tfdjsxwcwq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tfdjsxwcwq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tfdjsxwcwq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tfdjsxwcwq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tfdjsxwcwq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tfdjsxwcwq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tfdjsxwcwq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tfdjsxwcwq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tfdjsxwcwq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tfdjsxwcwq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tfdjsxwcwq .gt_spanner_row { border-bottom-style: hidden; }
 #tfdjsxwcwq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tfdjsxwcwq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tfdjsxwcwq .gt_from_md> :first-child { margin-top: 0; }
 #tfdjsxwcwq .gt_from_md> :last-child { margin-bottom: 0; }
 #tfdjsxwcwq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tfdjsxwcwq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tfdjsxwcwq .gt_indent_1 { text-indent: 5px; }
 #tfdjsxwcwq .gt_indent_2 { text-indent: calc(5px * 2); }
 #tfdjsxwcwq .gt_indent_3 { text-indent: calc(5px * 3); }
 #tfdjsxwcwq .gt_indent_4 { text-indent: calc(5px * 4); }
 #tfdjsxwcwq .gt_indent_5 { text-indent: calc(5px * 5); }
 #tfdjsxwcwq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tfdjsxwcwq .gt_row_group_first td { border-top-width: 2px; }
 #tfdjsxwcwq .gt_row_group_first th { border-top-width: 2px; }
 #tfdjsxwcwq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tfdjsxwcwq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tfdjsxwcwq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tfdjsxwcwq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tfdjsxwcwq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tfdjsxwcwq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tfdjsxwcwq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tfdjsxwcwq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tfdjsxwcwq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tfdjsxwcwq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tfdjsxwcwq .gt_left { text-align: left; }
 #tfdjsxwcwq .gt_center { text-align: center; }
 #tfdjsxwcwq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tfdjsxwcwq .gt_font_normal { font-weight: normal; }
 #tfdjsxwcwq .gt_font_bold { font-weight: bold; }
 #tfdjsxwcwq .gt_font_italic { font-style: italic; }
 #tfdjsxwcwq .gt_super { font-size: 65%; }
 #tfdjsxwcwq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tfdjsxwcwq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tfdjsxwcwq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tfdjsxwcwq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tfdjsxwcwq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tfdjsxwcwq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ckeoehfkfa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ckeoehfkfa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ckeoehfkfa p { margin: 0; padding: 0; }
 #ckeoehfkfa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ckeoehfkfa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ckeoehfkfa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ckeoehfkfa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ckeoehfkfa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ckeoehfkfa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ckeoehfkfa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ckeoehfkfa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ckeoehfkfa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ckeoehfkfa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ckeoehfkfa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ckeoehfkfa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ckeoehfkfa .gt_spanner_row { border-bottom-style: hidden; }
 #ckeoehfkfa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ckeoehfkfa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ckeoehfkfa .gt_from_md> :first-child { margin-top: 0; }
 #ckeoehfkfa .gt_from_md> :last-child { margin-bottom: 0; }
 #ckeoehfkfa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ckeoehfkfa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ckeoehfkfa .gt_indent_1 { text-indent: 5px; }
 #ckeoehfkfa .gt_indent_2 { text-indent: calc(5px * 2); }
 #ckeoehfkfa .gt_indent_3 { text-indent: calc(5px * 3); }
 #ckeoehfkfa .gt_indent_4 { text-indent: calc(5px * 4); }
 #ckeoehfkfa .gt_indent_5 { text-indent: calc(5px * 5); }
 #ckeoehfkfa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ckeoehfkfa .gt_row_group_first td { border-top-width: 2px; }
 #ckeoehfkfa .gt_row_group_first th { border-top-width: 2px; }
 #ckeoehfkfa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ckeoehfkfa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ckeoehfkfa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ckeoehfkfa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ckeoehfkfa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ckeoehfkfa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ckeoehfkfa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ckeoehfkfa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ckeoehfkfa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ckeoehfkfa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ckeoehfkfa .gt_left { text-align: left; }
 #ckeoehfkfa .gt_center { text-align: center; }
 #ckeoehfkfa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ckeoehfkfa .gt_font_normal { font-weight: normal; }
 #ckeoehfkfa .gt_font_bold { font-weight: bold; }
 #ckeoehfkfa .gt_font_italic { font-style: italic; }
 #ckeoehfkfa .gt_super { font-size: 65%; }
 #ckeoehfkfa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ckeoehfkfa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ckeoehfkfa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ckeoehfkfa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ckeoehfkfa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ckeoehfkfa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ipvbgeqyil table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ipvbgeqyil thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ipvbgeqyil p { margin: 0; padding: 0; }
 #ipvbgeqyil .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ipvbgeqyil .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ipvbgeqyil .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ipvbgeqyil .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ipvbgeqyil .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ipvbgeqyil .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ipvbgeqyil .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ipvbgeqyil .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ipvbgeqyil .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ipvbgeqyil .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ipvbgeqyil .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ipvbgeqyil .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ipvbgeqyil .gt_spanner_row { border-bottom-style: hidden; }
 #ipvbgeqyil .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ipvbgeqyil .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ipvbgeqyil .gt_from_md> :first-child { margin-top: 0; }
 #ipvbgeqyil .gt_from_md> :last-child { margin-bottom: 0; }
 #ipvbgeqyil .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ipvbgeqyil .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ipvbgeqyil .gt_indent_1 { text-indent: 5px; }
 #ipvbgeqyil .gt_indent_2 { text-indent: calc(5px * 2); }
 #ipvbgeqyil .gt_indent_3 { text-indent: calc(5px * 3); }
 #ipvbgeqyil .gt_indent_4 { text-indent: calc(5px * 4); }
 #ipvbgeqyil .gt_indent_5 { text-indent: calc(5px * 5); }
 #ipvbgeqyil .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ipvbgeqyil .gt_row_group_first td { border-top-width: 2px; }
 #ipvbgeqyil .gt_row_group_first th { border-top-width: 2px; }
 #ipvbgeqyil .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ipvbgeqyil .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ipvbgeqyil .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ipvbgeqyil .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ipvbgeqyil .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ipvbgeqyil .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ipvbgeqyil .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ipvbgeqyil .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ipvbgeqyil .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ipvbgeqyil .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ipvbgeqyil .gt_left { text-align: left; }
 #ipvbgeqyil .gt_center { text-align: center; }
 #ipvbgeqyil .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ipvbgeqyil .gt_font_normal { font-weight: normal; }
 #ipvbgeqyil .gt_font_bold { font-weight: bold; }
 #ipvbgeqyil .gt_font_italic { font-style: italic; }
 #ipvbgeqyil .gt_super { font-size: 65%; }
 #ipvbgeqyil .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ipvbgeqyil .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ipvbgeqyil .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ipvbgeqyil .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ipvbgeqyil .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ipvbgeqyil .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bhbotybwhy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bhbotybwhy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bhbotybwhy p { margin: 0; padding: 0; }
 #bhbotybwhy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bhbotybwhy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bhbotybwhy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bhbotybwhy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bhbotybwhy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhbotybwhy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhbotybwhy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhbotybwhy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bhbotybwhy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bhbotybwhy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bhbotybwhy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bhbotybwhy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bhbotybwhy .gt_spanner_row { border-bottom-style: hidden; }
 #bhbotybwhy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bhbotybwhy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bhbotybwhy .gt_from_md> :first-child { margin-top: 0; }
 #bhbotybwhy .gt_from_md> :last-child { margin-bottom: 0; }
 #bhbotybwhy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bhbotybwhy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bhbotybwhy .gt_indent_1 { text-indent: 5px; }
 #bhbotybwhy .gt_indent_2 { text-indent: calc(5px * 2); }
 #bhbotybwhy .gt_indent_3 { text-indent: calc(5px * 3); }
 #bhbotybwhy .gt_indent_4 { text-indent: calc(5px * 4); }
 #bhbotybwhy .gt_indent_5 { text-indent: calc(5px * 5); }
 #bhbotybwhy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bhbotybwhy .gt_row_group_first td { border-top-width: 2px; }
 #bhbotybwhy .gt_row_group_first th { border-top-width: 2px; }
 #bhbotybwhy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bhbotybwhy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhbotybwhy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhbotybwhy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bhbotybwhy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhbotybwhy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhbotybwhy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bhbotybwhy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bhbotybwhy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhbotybwhy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhbotybwhy .gt_left { text-align: left; }
 #bhbotybwhy .gt_center { text-align: center; }
 #bhbotybwhy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bhbotybwhy .gt_font_normal { font-weight: normal; }
 #bhbotybwhy .gt_font_bold { font-weight: bold; }
 #bhbotybwhy .gt_font_italic { font-style: italic; }
 #bhbotybwhy .gt_super { font-size: 65%; }
 #bhbotybwhy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhbotybwhy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bhbotybwhy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhbotybwhy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhbotybwhy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bhbotybwhy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bqkbwvgzxu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bqkbwvgzxu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bqkbwvgzxu p { margin: 0; padding: 0; }
 #bqkbwvgzxu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bqkbwvgzxu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bqkbwvgzxu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bqkbwvgzxu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bqkbwvgzxu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bqkbwvgzxu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bqkbwvgzxu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bqkbwvgzxu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bqkbwvgzxu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bqkbwvgzxu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bqkbwvgzxu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bqkbwvgzxu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bqkbwvgzxu .gt_spanner_row { border-bottom-style: hidden; }
 #bqkbwvgzxu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bqkbwvgzxu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bqkbwvgzxu .gt_from_md> :first-child { margin-top: 0; }
 #bqkbwvgzxu .gt_from_md> :last-child { margin-bottom: 0; }
 #bqkbwvgzxu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bqkbwvgzxu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bqkbwvgzxu .gt_indent_1 { text-indent: 5px; }
 #bqkbwvgzxu .gt_indent_2 { text-indent: calc(5px * 2); }
 #bqkbwvgzxu .gt_indent_3 { text-indent: calc(5px * 3); }
 #bqkbwvgzxu .gt_indent_4 { text-indent: calc(5px * 4); }
 #bqkbwvgzxu .gt_indent_5 { text-indent: calc(5px * 5); }
 #bqkbwvgzxu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bqkbwvgzxu .gt_row_group_first td { border-top-width: 2px; }
 #bqkbwvgzxu .gt_row_group_first th { border-top-width: 2px; }
 #bqkbwvgzxu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bqkbwvgzxu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bqkbwvgzxu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bqkbwvgzxu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bqkbwvgzxu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bqkbwvgzxu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bqkbwvgzxu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bqkbwvgzxu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bqkbwvgzxu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bqkbwvgzxu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bqkbwvgzxu .gt_left { text-align: left; }
 #bqkbwvgzxu .gt_center { text-align: center; }
 #bqkbwvgzxu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bqkbwvgzxu .gt_font_normal { font-weight: normal; }
 #bqkbwvgzxu .gt_font_bold { font-weight: bold; }
 #bqkbwvgzxu .gt_font_italic { font-style: italic; }
 #bqkbwvgzxu .gt_super { font-size: 65%; }
 #bqkbwvgzxu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bqkbwvgzxu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bqkbwvgzxu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bqkbwvgzxu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bqkbwvgzxu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bqkbwvgzxu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pvztbhngym table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pvztbhngym thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pvztbhngym p { margin: 0; padding: 0; }
 #pvztbhngym .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pvztbhngym .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pvztbhngym .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pvztbhngym .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pvztbhngym .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pvztbhngym .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pvztbhngym .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pvztbhngym .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pvztbhngym .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pvztbhngym .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pvztbhngym .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pvztbhngym .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pvztbhngym .gt_spanner_row { border-bottom-style: hidden; }
 #pvztbhngym .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pvztbhngym .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pvztbhngym .gt_from_md> :first-child { margin-top: 0; }
 #pvztbhngym .gt_from_md> :last-child { margin-bottom: 0; }
 #pvztbhngym .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pvztbhngym .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pvztbhngym .gt_indent_1 { text-indent: 5px; }
 #pvztbhngym .gt_indent_2 { text-indent: calc(5px * 2); }
 #pvztbhngym .gt_indent_3 { text-indent: calc(5px * 3); }
 #pvztbhngym .gt_indent_4 { text-indent: calc(5px * 4); }
 #pvztbhngym .gt_indent_5 { text-indent: calc(5px * 5); }
 #pvztbhngym .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pvztbhngym .gt_row_group_first td { border-top-width: 2px; }
 #pvztbhngym .gt_row_group_first th { border-top-width: 2px; }
 #pvztbhngym .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pvztbhngym .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pvztbhngym .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pvztbhngym .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pvztbhngym .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pvztbhngym .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pvztbhngym .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pvztbhngym .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pvztbhngym .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pvztbhngym .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pvztbhngym .gt_left { text-align: left; }
 #pvztbhngym .gt_center { text-align: center; }
 #pvztbhngym .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pvztbhngym .gt_font_normal { font-weight: normal; }
 #pvztbhngym .gt_font_bold { font-weight: bold; }
 #pvztbhngym .gt_font_italic { font-style: italic; }
 #pvztbhngym .gt_super { font-size: 65%; }
 #pvztbhngym .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pvztbhngym .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pvztbhngym .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pvztbhngym .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pvztbhngym .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pvztbhngym .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
