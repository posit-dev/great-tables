# Summary Rows

Summary rows provide aggregated values (such as totals, means, or counts) directly in the table, adjacent to the data they summarize. **Great Tables** supports two types: group-level summaries that appear next to each row group, and grand summaries that aggregate across the entire table. Both types let you define multiple aggregation functions at once and control where the summary appears.


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
#comwghkcla table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#comwghkcla thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#comwghkcla p { margin: 0; padding: 0; }
 #comwghkcla .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #comwghkcla .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #comwghkcla .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #comwghkcla .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #comwghkcla .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #comwghkcla .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #comwghkcla .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #comwghkcla .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #comwghkcla .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #comwghkcla .gt_column_spanner_outer:first-child { padding-left: 0; }
 #comwghkcla .gt_column_spanner_outer:last-child { padding-right: 0; }
 #comwghkcla .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #comwghkcla .gt_spanner_row { border-bottom-style: hidden; }
 #comwghkcla .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #comwghkcla .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #comwghkcla .gt_from_md> :first-child { margin-top: 0; }
 #comwghkcla .gt_from_md> :last-child { margin-bottom: 0; }
 #comwghkcla .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #comwghkcla .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #comwghkcla .gt_indent_1 { text-indent: 5px; }
 #comwghkcla .gt_indent_2 { text-indent: calc(5px * 2); }
 #comwghkcla .gt_indent_3 { text-indent: calc(5px * 3); }
 #comwghkcla .gt_indent_4 { text-indent: calc(5px * 4); }
 #comwghkcla .gt_indent_5 { text-indent: calc(5px * 5); }
 #comwghkcla .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #comwghkcla .gt_row_group_first td { border-top-width: 2px; }
 #comwghkcla .gt_row_group_first th { border-top-width: 2px; }
 #comwghkcla .gt_striped { color: #333333; background-color: #F4F4F4; }
 #comwghkcla .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #comwghkcla .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #comwghkcla .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #comwghkcla .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #comwghkcla .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #comwghkcla .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #comwghkcla .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #comwghkcla .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #comwghkcla .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #comwghkcla .gt_left { text-align: left; }
 #comwghkcla .gt_center { text-align: center; }
 #comwghkcla .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #comwghkcla .gt_font_normal { font-weight: normal; }
 #comwghkcla .gt_font_bold { font-weight: bold; }
 #comwghkcla .gt_font_italic { font-style: italic; }
 #comwghkcla .gt_super { font-size: 65%; }
 #comwghkcla .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #comwghkcla .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #comwghkcla .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #comwghkcla .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #comwghkcla .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #comwghkcla .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Computing</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Laptop</td>
<td class="gt_row gt_right">45</td>
<td class="gt_row gt_right">67,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mouse</td>
<td class="gt_row gt_right">230</td>
<td class="gt_row gt_right">4,600</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Keyboard</td>
<td class="gt_row gt_right">180</td>
<td class="gt_row gt_right">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Peripherals</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Monitor</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right">19,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Webcam</td>
<td class="gt_row gt_right">120</td>
<td class="gt_row gt_right">6,000</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Headset</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right">7,125</td>
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
#sysrqrlmyy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sysrqrlmyy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sysrqrlmyy p { margin: 0; padding: 0; }
 #sysrqrlmyy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sysrqrlmyy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sysrqrlmyy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sysrqrlmyy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sysrqrlmyy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sysrqrlmyy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sysrqrlmyy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sysrqrlmyy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sysrqrlmyy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sysrqrlmyy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sysrqrlmyy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sysrqrlmyy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sysrqrlmyy .gt_spanner_row { border-bottom-style: hidden; }
 #sysrqrlmyy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sysrqrlmyy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sysrqrlmyy .gt_from_md> :first-child { margin-top: 0; }
 #sysrqrlmyy .gt_from_md> :last-child { margin-bottom: 0; }
 #sysrqrlmyy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sysrqrlmyy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sysrqrlmyy .gt_indent_1 { text-indent: 5px; }
 #sysrqrlmyy .gt_indent_2 { text-indent: calc(5px * 2); }
 #sysrqrlmyy .gt_indent_3 { text-indent: calc(5px * 3); }
 #sysrqrlmyy .gt_indent_4 { text-indent: calc(5px * 4); }
 #sysrqrlmyy .gt_indent_5 { text-indent: calc(5px * 5); }
 #sysrqrlmyy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sysrqrlmyy .gt_row_group_first td { border-top-width: 2px; }
 #sysrqrlmyy .gt_row_group_first th { border-top-width: 2px; }
 #sysrqrlmyy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sysrqrlmyy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sysrqrlmyy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sysrqrlmyy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sysrqrlmyy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sysrqrlmyy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sysrqrlmyy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sysrqrlmyy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sysrqrlmyy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sysrqrlmyy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sysrqrlmyy .gt_left { text-align: left; }
 #sysrqrlmyy .gt_center { text-align: center; }
 #sysrqrlmyy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sysrqrlmyy .gt_font_normal { font-weight: normal; }
 #sysrqrlmyy .gt_font_bold { font-weight: bold; }
 #sysrqrlmyy .gt_font_italic { font-style: italic; }
 #sysrqrlmyy .gt_super { font-size: 65%; }
 #sysrqrlmyy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sysrqrlmyy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sysrqrlmyy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sysrqrlmyy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sysrqrlmyy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sysrqrlmyy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Computing</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Laptop</td>
<td class="gt_row gt_right">45</td>
<td class="gt_row gt_right">67,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mouse</td>
<td class="gt_row gt_right">230</td>
<td class="gt_row gt_right">4,600</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Keyboard</td>
<td class="gt_row gt_right">180</td>
<td class="gt_row gt_right">9,000</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">455</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">81100</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Peripherals</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Monitor</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right">19,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Webcam</td>
<td class="gt_row gt_right">120</td>
<td class="gt_row gt_right">6,000</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Headset</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right">7,125</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">280</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">32625</td>
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
#dtxkaesrny table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dtxkaesrny thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dtxkaesrny p { margin: 0; padding: 0; }
 #dtxkaesrny .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dtxkaesrny .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dtxkaesrny .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dtxkaesrny .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dtxkaesrny .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dtxkaesrny .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dtxkaesrny .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dtxkaesrny .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dtxkaesrny .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dtxkaesrny .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dtxkaesrny .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dtxkaesrny .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dtxkaesrny .gt_spanner_row { border-bottom-style: hidden; }
 #dtxkaesrny .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dtxkaesrny .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dtxkaesrny .gt_from_md> :first-child { margin-top: 0; }
 #dtxkaesrny .gt_from_md> :last-child { margin-bottom: 0; }
 #dtxkaesrny .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dtxkaesrny .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dtxkaesrny .gt_indent_1 { text-indent: 5px; }
 #dtxkaesrny .gt_indent_2 { text-indent: calc(5px * 2); }
 #dtxkaesrny .gt_indent_3 { text-indent: calc(5px * 3); }
 #dtxkaesrny .gt_indent_4 { text-indent: calc(5px * 4); }
 #dtxkaesrny .gt_indent_5 { text-indent: calc(5px * 5); }
 #dtxkaesrny .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dtxkaesrny .gt_row_group_first td { border-top-width: 2px; }
 #dtxkaesrny .gt_row_group_first th { border-top-width: 2px; }
 #dtxkaesrny .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dtxkaesrny .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dtxkaesrny .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dtxkaesrny .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dtxkaesrny .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dtxkaesrny .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dtxkaesrny .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dtxkaesrny .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dtxkaesrny .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dtxkaesrny .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dtxkaesrny .gt_left { text-align: left; }
 #dtxkaesrny .gt_center { text-align: center; }
 #dtxkaesrny .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dtxkaesrny .gt_font_normal { font-weight: normal; }
 #dtxkaesrny .gt_font_bold { font-weight: bold; }
 #dtxkaesrny .gt_font_italic { font-style: italic; }
 #dtxkaesrny .gt_super { font-size: 65%; }
 #dtxkaesrny .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dtxkaesrny .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dtxkaesrny .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dtxkaesrny .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dtxkaesrny .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dtxkaesrny .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Computing</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Laptop</td>
<td class="gt_row gt_right">45</td>
<td class="gt_row gt_right">67,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mouse</td>
<td class="gt_row gt_right">230</td>
<td class="gt_row gt_right">4,600</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Keyboard</td>
<td class="gt_row gt_right">180</td>
<td class="gt_row gt_right">9,000</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">455</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">81100</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Average</td>
<td class="gt_row gt_right gt_summary_row">151.66666666666666</td>
<td class="gt_row gt_right gt_summary_row">27033.333333333332</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Peripherals</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Monitor</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right">19,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Webcam</td>
<td class="gt_row gt_right">120</td>
<td class="gt_row gt_right">6,000</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Headset</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right">7,125</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">280</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">32625</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Average</td>
<td class="gt_row gt_right gt_summary_row">93.33333333333333</td>
<td class="gt_row gt_right gt_summary_row">10875.0</td>
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
#zxfjqpecbi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zxfjqpecbi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zxfjqpecbi p { margin: 0; padding: 0; }
 #zxfjqpecbi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zxfjqpecbi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zxfjqpecbi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zxfjqpecbi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zxfjqpecbi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxfjqpecbi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxfjqpecbi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxfjqpecbi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zxfjqpecbi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zxfjqpecbi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zxfjqpecbi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zxfjqpecbi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zxfjqpecbi .gt_spanner_row { border-bottom-style: hidden; }
 #zxfjqpecbi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zxfjqpecbi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zxfjqpecbi .gt_from_md> :first-child { margin-top: 0; }
 #zxfjqpecbi .gt_from_md> :last-child { margin-bottom: 0; }
 #zxfjqpecbi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zxfjqpecbi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zxfjqpecbi .gt_indent_1 { text-indent: 5px; }
 #zxfjqpecbi .gt_indent_2 { text-indent: calc(5px * 2); }
 #zxfjqpecbi .gt_indent_3 { text-indent: calc(5px * 3); }
 #zxfjqpecbi .gt_indent_4 { text-indent: calc(5px * 4); }
 #zxfjqpecbi .gt_indent_5 { text-indent: calc(5px * 5); }
 #zxfjqpecbi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zxfjqpecbi .gt_row_group_first td { border-top-width: 2px; }
 #zxfjqpecbi .gt_row_group_first th { border-top-width: 2px; }
 #zxfjqpecbi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zxfjqpecbi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxfjqpecbi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxfjqpecbi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zxfjqpecbi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxfjqpecbi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxfjqpecbi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zxfjqpecbi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zxfjqpecbi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxfjqpecbi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zxfjqpecbi .gt_left { text-align: left; }
 #zxfjqpecbi .gt_center { text-align: center; }
 #zxfjqpecbi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zxfjqpecbi .gt_font_normal { font-weight: normal; }
 #zxfjqpecbi .gt_font_bold { font-weight: bold; }
 #zxfjqpecbi .gt_font_italic { font-style: italic; }
 #zxfjqpecbi .gt_super { font-size: 65%; }
 #zxfjqpecbi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxfjqpecbi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zxfjqpecbi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxfjqpecbi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zxfjqpecbi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zxfjqpecbi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Computing</th>
</tr>

<tr>
<td class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row">Total</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">455</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">81100</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Laptop</td>
<td class="gt_row gt_right">45</td>
<td class="gt_row gt_right">67,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mouse</td>
<td class="gt_row gt_right">230</td>
<td class="gt_row gt_right">4,600</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Keyboard</td>
<td class="gt_row gt_right">180</td>
<td class="gt_row gt_right">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Peripherals</td>
</tr>
<tr>
<td class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row">Total</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">280</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">32625</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Monitor</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right">19,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Webcam</td>
<td class="gt_row gt_right">120</td>
<td class="gt_row gt_right">6,000</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Headset</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right">7,125</td>
</tr>
</tbody>
</table>


The summary row now sits above the data rows in each group rather than below them, making the totals immediately visible.


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
#hejiiseobq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hejiiseobq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hejiiseobq p { margin: 0; padding: 0; }
 #hejiiseobq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hejiiseobq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hejiiseobq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hejiiseobq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hejiiseobq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hejiiseobq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hejiiseobq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hejiiseobq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hejiiseobq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hejiiseobq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hejiiseobq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hejiiseobq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hejiiseobq .gt_spanner_row { border-bottom-style: hidden; }
 #hejiiseobq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hejiiseobq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hejiiseobq .gt_from_md> :first-child { margin-top: 0; }
 #hejiiseobq .gt_from_md> :last-child { margin-bottom: 0; }
 #hejiiseobq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hejiiseobq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hejiiseobq .gt_indent_1 { text-indent: 5px; }
 #hejiiseobq .gt_indent_2 { text-indent: calc(5px * 2); }
 #hejiiseobq .gt_indent_3 { text-indent: calc(5px * 3); }
 #hejiiseobq .gt_indent_4 { text-indent: calc(5px * 4); }
 #hejiiseobq .gt_indent_5 { text-indent: calc(5px * 5); }
 #hejiiseobq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hejiiseobq .gt_row_group_first td { border-top-width: 2px; }
 #hejiiseobq .gt_row_group_first th { border-top-width: 2px; }
 #hejiiseobq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hejiiseobq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hejiiseobq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hejiiseobq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hejiiseobq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hejiiseobq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hejiiseobq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hejiiseobq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hejiiseobq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hejiiseobq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hejiiseobq .gt_left { text-align: left; }
 #hejiiseobq .gt_center { text-align: center; }
 #hejiiseobq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hejiiseobq .gt_font_normal { font-weight: normal; }
 #hejiiseobq .gt_font_bold { font-weight: bold; }
 #hejiiseobq .gt_font_italic { font-style: italic; }
 #hejiiseobq .gt_super { font-size: 65%; }
 #hejiiseobq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hejiiseobq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hejiiseobq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hejiiseobq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hejiiseobq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hejiiseobq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Computing</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Laptop</td>
<td class="gt_row gt_right">45</td>
<td class="gt_row gt_right">67,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mouse</td>
<td class="gt_row gt_right">230</td>
<td class="gt_row gt_right">4,600</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Keyboard</td>
<td class="gt_row gt_right">180</td>
<td class="gt_row gt_right">9,000</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Total</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">455</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">81100</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Peripherals</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Monitor</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right">19,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Webcam</td>
<td class="gt_row gt_right">120</td>
<td class="gt_row gt_right">6,000</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Headset</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right">7,125</td>
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
#dxzdociely table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dxzdociely thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dxzdociely p { margin: 0; padding: 0; }
 #dxzdociely .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dxzdociely .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dxzdociely .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dxzdociely .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dxzdociely .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxzdociely .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxzdociely .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxzdociely .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dxzdociely .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dxzdociely .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dxzdociely .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dxzdociely .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dxzdociely .gt_spanner_row { border-bottom-style: hidden; }
 #dxzdociely .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dxzdociely .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dxzdociely .gt_from_md> :first-child { margin-top: 0; }
 #dxzdociely .gt_from_md> :last-child { margin-bottom: 0; }
 #dxzdociely .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dxzdociely .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dxzdociely .gt_indent_1 { text-indent: 5px; }
 #dxzdociely .gt_indent_2 { text-indent: calc(5px * 2); }
 #dxzdociely .gt_indent_3 { text-indent: calc(5px * 3); }
 #dxzdociely .gt_indent_4 { text-indent: calc(5px * 4); }
 #dxzdociely .gt_indent_5 { text-indent: calc(5px * 5); }
 #dxzdociely .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dxzdociely .gt_row_group_first td { border-top-width: 2px; }
 #dxzdociely .gt_row_group_first th { border-top-width: 2px; }
 #dxzdociely .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dxzdociely .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxzdociely .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxzdociely .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dxzdociely .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxzdociely .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxzdociely .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dxzdociely .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dxzdociely .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxzdociely .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxzdociely .gt_left { text-align: left; }
 #dxzdociely .gt_center { text-align: center; }
 #dxzdociely .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dxzdociely .gt_font_normal { font-weight: normal; }
 #dxzdociely .gt_font_bold { font-weight: bold; }
 #dxzdociely .gt_font_italic { font-style: italic; }
 #dxzdociely .gt_super { font-size: 65%; }
 #dxzdociely .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxzdociely .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dxzdociely .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxzdociely .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxzdociely .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dxzdociely .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Computing</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Laptop</td>
<td class="gt_row gt_right">45</td>
<td class="gt_row gt_right">67,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mouse</td>
<td class="gt_row gt_right">230</td>
<td class="gt_row gt_right">4,600</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Keyboard</td>
<td class="gt_row gt_right">180</td>
<td class="gt_row gt_right">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Peripherals</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Monitor</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right">19,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Webcam</td>
<td class="gt_row gt_right">120</td>
<td class="gt_row gt_right">6,000</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Headset</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right">7,125</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Grand Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">735</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">113725</td>
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
#onpvcdjdjj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#onpvcdjdjj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#onpvcdjdjj p { margin: 0; padding: 0; }
 #onpvcdjdjj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #onpvcdjdjj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #onpvcdjdjj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #onpvcdjdjj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #onpvcdjdjj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #onpvcdjdjj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #onpvcdjdjj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #onpvcdjdjj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #onpvcdjdjj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #onpvcdjdjj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #onpvcdjdjj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #onpvcdjdjj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #onpvcdjdjj .gt_spanner_row { border-bottom-style: hidden; }
 #onpvcdjdjj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #onpvcdjdjj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #onpvcdjdjj .gt_from_md> :first-child { margin-top: 0; }
 #onpvcdjdjj .gt_from_md> :last-child { margin-bottom: 0; }
 #onpvcdjdjj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #onpvcdjdjj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #onpvcdjdjj .gt_indent_1 { text-indent: 5px; }
 #onpvcdjdjj .gt_indent_2 { text-indent: calc(5px * 2); }
 #onpvcdjdjj .gt_indent_3 { text-indent: calc(5px * 3); }
 #onpvcdjdjj .gt_indent_4 { text-indent: calc(5px * 4); }
 #onpvcdjdjj .gt_indent_5 { text-indent: calc(5px * 5); }
 #onpvcdjdjj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #onpvcdjdjj .gt_row_group_first td { border-top-width: 2px; }
 #onpvcdjdjj .gt_row_group_first th { border-top-width: 2px; }
 #onpvcdjdjj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #onpvcdjdjj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #onpvcdjdjj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #onpvcdjdjj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #onpvcdjdjj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #onpvcdjdjj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #onpvcdjdjj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #onpvcdjdjj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #onpvcdjdjj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #onpvcdjdjj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #onpvcdjdjj .gt_left { text-align: left; }
 #onpvcdjdjj .gt_center { text-align: center; }
 #onpvcdjdjj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #onpvcdjdjj .gt_font_normal { font-weight: normal; }
 #onpvcdjdjj .gt_font_bold { font-weight: bold; }
 #onpvcdjdjj .gt_font_italic { font-style: italic; }
 #onpvcdjdjj .gt_super { font-size: 65%; }
 #onpvcdjdjj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #onpvcdjdjj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #onpvcdjdjj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #onpvcdjdjj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #onpvcdjdjj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #onpvcdjdjj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Computing</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Laptop</td>
<td class="gt_row gt_right">45</td>
<td class="gt_row gt_right">67,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mouse</td>
<td class="gt_row gt_right">230</td>
<td class="gt_row gt_right">4,600</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Keyboard</td>
<td class="gt_row gt_right">180</td>
<td class="gt_row gt_right">9,000</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Subtotal</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">455</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">81100</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Peripherals</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Monitor</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right">19,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Webcam</td>
<td class="gt_row gt_right">120</td>
<td class="gt_row gt_right">6,000</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Headset</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right">7,125</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Subtotal</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">280</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">32625</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Grand Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">735</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">113725</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_grand_summary_row">Overall Average</td>
<td class="gt_row gt_right gt_grand_summary_row">122.5</td>
<td class="gt_row gt_right gt_grand_summary_row">18954.166666666668</td>
</tr>
</tbody>
</table>


Each group now has a `"Subtotal"` row, and the table finishes with a `"Grand Total"` and `"Overall Average"` row that span across all groups.


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
#tosqgzqnmu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tosqgzqnmu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tosqgzqnmu p { margin: 0; padding: 0; }
 #tosqgzqnmu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tosqgzqnmu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tosqgzqnmu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tosqgzqnmu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tosqgzqnmu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tosqgzqnmu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tosqgzqnmu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tosqgzqnmu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tosqgzqnmu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tosqgzqnmu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tosqgzqnmu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tosqgzqnmu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tosqgzqnmu .gt_spanner_row { border-bottom-style: hidden; }
 #tosqgzqnmu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tosqgzqnmu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tosqgzqnmu .gt_from_md> :first-child { margin-top: 0; }
 #tosqgzqnmu .gt_from_md> :last-child { margin-bottom: 0; }
 #tosqgzqnmu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tosqgzqnmu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tosqgzqnmu .gt_indent_1 { text-indent: 5px; }
 #tosqgzqnmu .gt_indent_2 { text-indent: calc(5px * 2); }
 #tosqgzqnmu .gt_indent_3 { text-indent: calc(5px * 3); }
 #tosqgzqnmu .gt_indent_4 { text-indent: calc(5px * 4); }
 #tosqgzqnmu .gt_indent_5 { text-indent: calc(5px * 5); }
 #tosqgzqnmu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tosqgzqnmu .gt_row_group_first td { border-top-width: 2px; }
 #tosqgzqnmu .gt_row_group_first th { border-top-width: 2px; }
 #tosqgzqnmu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tosqgzqnmu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tosqgzqnmu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tosqgzqnmu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tosqgzqnmu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tosqgzqnmu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tosqgzqnmu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tosqgzqnmu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tosqgzqnmu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tosqgzqnmu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tosqgzqnmu .gt_left { text-align: left; }
 #tosqgzqnmu .gt_center { text-align: center; }
 #tosqgzqnmu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tosqgzqnmu .gt_font_normal { font-weight: normal; }
 #tosqgzqnmu .gt_font_bold { font-weight: bold; }
 #tosqgzqnmu .gt_font_italic { font-style: italic; }
 #tosqgzqnmu .gt_super { font-size: 65%; }
 #tosqgzqnmu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tosqgzqnmu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tosqgzqnmu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tosqgzqnmu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tosqgzqnmu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tosqgzqnmu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading">Computing</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Laptop</td>
<td class="gt_row gt_right">45</td>
<td class="gt_row gt_right">67,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mouse</td>
<td class="gt_row gt_right">230</td>
<td class="gt_row gt_right">4,600</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Keyboard</td>
<td class="gt_row gt_right">180</td>
<td class="gt_row gt_right">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Peripherals</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Monitor</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right">19,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Webcam</td>
<td class="gt_row gt_right">120</td>
<td class="gt_row gt_right">6,000</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Headset</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right">7,125</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">735</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">113725</td>
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
#pymluqxowk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pymluqxowk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pymluqxowk p { margin: 0; padding: 0; }
 #pymluqxowk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pymluqxowk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pymluqxowk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pymluqxowk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pymluqxowk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pymluqxowk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pymluqxowk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pymluqxowk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pymluqxowk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pymluqxowk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pymluqxowk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pymluqxowk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pymluqxowk .gt_spanner_row { border-bottom-style: hidden; }
 #pymluqxowk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pymluqxowk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pymluqxowk .gt_from_md> :first-child { margin-top: 0; }
 #pymluqxowk .gt_from_md> :last-child { margin-bottom: 0; }
 #pymluqxowk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pymluqxowk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pymluqxowk .gt_indent_1 { text-indent: 5px; }
 #pymluqxowk .gt_indent_2 { text-indent: calc(5px * 2); }
 #pymluqxowk .gt_indent_3 { text-indent: calc(5px * 3); }
 #pymluqxowk .gt_indent_4 { text-indent: calc(5px * 4); }
 #pymluqxowk .gt_indent_5 { text-indent: calc(5px * 5); }
 #pymluqxowk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pymluqxowk .gt_row_group_first td { border-top-width: 2px; }
 #pymluqxowk .gt_row_group_first th { border-top-width: 2px; }
 #pymluqxowk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pymluqxowk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pymluqxowk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pymluqxowk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pymluqxowk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pymluqxowk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pymluqxowk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pymluqxowk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pymluqxowk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pymluqxowk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pymluqxowk .gt_left { text-align: left; }
 #pymluqxowk .gt_center { text-align: center; }
 #pymluqxowk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pymluqxowk .gt_font_normal { font-weight: normal; }
 #pymluqxowk .gt_font_bold { font-weight: bold; }
 #pymluqxowk .gt_font_italic { font-style: italic; }
 #pymluqxowk .gt_super { font-size: 65%; }
 #pymluqxowk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pymluqxowk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pymluqxowk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pymluqxowk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pymluqxowk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pymluqxowk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Q4 Product Sales</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">By category</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="units_sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">units_sold</th>
<th id="revenue" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">revenue</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Computing</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Laptop</td>
<td class="gt_row gt_right">45</td>
<td class="gt_row gt_right">67,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Mouse</td>
<td class="gt_row gt_right">230</td>
<td class="gt_row gt_right">4,600</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Keyboard</td>
<td class="gt_row gt_right">180</td>
<td class="gt_row gt_right">9,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Peripherals</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Monitor</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right">19,500</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Webcam</td>
<td class="gt_row gt_right">120</td>
<td class="gt_row gt_right">6,000</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Headset</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right">7,125</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Grand Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightyellow">735</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightyellow">113725</td>
</tr>
</tbody>
</table>


Summary rows are a natural companion to row groups, providing the aggregated context that readers need to interpret grouped data. By combining group-level and grand summaries, formatting, and targeted styling, you can build tables that tell a complete analytical story.
