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
#ybazkxtylm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ybazkxtylm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ybazkxtylm p { margin: 0; padding: 0; }
 #ybazkxtylm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ybazkxtylm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ybazkxtylm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ybazkxtylm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ybazkxtylm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ybazkxtylm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ybazkxtylm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ybazkxtylm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ybazkxtylm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ybazkxtylm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ybazkxtylm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ybazkxtylm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ybazkxtylm .gt_spanner_row { border-bottom-style: hidden; }
 #ybazkxtylm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ybazkxtylm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ybazkxtylm .gt_from_md> :first-child { margin-top: 0; }
 #ybazkxtylm .gt_from_md> :last-child { margin-bottom: 0; }
 #ybazkxtylm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ybazkxtylm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ybazkxtylm .gt_indent_1 { text-indent: 5px; }
 #ybazkxtylm .gt_indent_2 { text-indent: calc(5px * 2); }
 #ybazkxtylm .gt_indent_3 { text-indent: calc(5px * 3); }
 #ybazkxtylm .gt_indent_4 { text-indent: calc(5px * 4); }
 #ybazkxtylm .gt_indent_5 { text-indent: calc(5px * 5); }
 #ybazkxtylm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ybazkxtylm .gt_row_group_first td { border-top-width: 2px; }
 #ybazkxtylm .gt_row_group_first th { border-top-width: 2px; }
 #ybazkxtylm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ybazkxtylm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ybazkxtylm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ybazkxtylm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ybazkxtylm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ybazkxtylm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ybazkxtylm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ybazkxtylm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ybazkxtylm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ybazkxtylm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ybazkxtylm .gt_left { text-align: left; }
 #ybazkxtylm .gt_center { text-align: center; }
 #ybazkxtylm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ybazkxtylm .gt_font_normal { font-weight: normal; }
 #ybazkxtylm .gt_font_bold { font-weight: bold; }
 #ybazkxtylm .gt_font_italic { font-style: italic; }
 #ybazkxtylm .gt_super { font-size: 65%; }
 #ybazkxtylm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ybazkxtylm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ybazkxtylm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ybazkxtylm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ybazkxtylm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ybazkxtylm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rigpqyrlsm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rigpqyrlsm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rigpqyrlsm p { margin: 0; padding: 0; }
 #rigpqyrlsm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rigpqyrlsm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rigpqyrlsm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rigpqyrlsm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rigpqyrlsm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rigpqyrlsm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rigpqyrlsm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rigpqyrlsm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rigpqyrlsm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rigpqyrlsm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rigpqyrlsm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rigpqyrlsm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rigpqyrlsm .gt_spanner_row { border-bottom-style: hidden; }
 #rigpqyrlsm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rigpqyrlsm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rigpqyrlsm .gt_from_md> :first-child { margin-top: 0; }
 #rigpqyrlsm .gt_from_md> :last-child { margin-bottom: 0; }
 #rigpqyrlsm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rigpqyrlsm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rigpqyrlsm .gt_indent_1 { text-indent: 5px; }
 #rigpqyrlsm .gt_indent_2 { text-indent: calc(5px * 2); }
 #rigpqyrlsm .gt_indent_3 { text-indent: calc(5px * 3); }
 #rigpqyrlsm .gt_indent_4 { text-indent: calc(5px * 4); }
 #rigpqyrlsm .gt_indent_5 { text-indent: calc(5px * 5); }
 #rigpqyrlsm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rigpqyrlsm .gt_row_group_first td { border-top-width: 2px; }
 #rigpqyrlsm .gt_row_group_first th { border-top-width: 2px; }
 #rigpqyrlsm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rigpqyrlsm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rigpqyrlsm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rigpqyrlsm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rigpqyrlsm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rigpqyrlsm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rigpqyrlsm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rigpqyrlsm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rigpqyrlsm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rigpqyrlsm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rigpqyrlsm .gt_left { text-align: left; }
 #rigpqyrlsm .gt_center { text-align: center; }
 #rigpqyrlsm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rigpqyrlsm .gt_font_normal { font-weight: normal; }
 #rigpqyrlsm .gt_font_bold { font-weight: bold; }
 #rigpqyrlsm .gt_font_italic { font-style: italic; }
 #rigpqyrlsm .gt_super { font-size: 65%; }
 #rigpqyrlsm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rigpqyrlsm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rigpqyrlsm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rigpqyrlsm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rigpqyrlsm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rigpqyrlsm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ypuvdjuebr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ypuvdjuebr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ypuvdjuebr p { margin: 0; padding: 0; }
 #ypuvdjuebr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ypuvdjuebr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ypuvdjuebr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ypuvdjuebr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ypuvdjuebr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ypuvdjuebr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ypuvdjuebr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ypuvdjuebr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ypuvdjuebr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ypuvdjuebr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ypuvdjuebr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ypuvdjuebr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ypuvdjuebr .gt_spanner_row { border-bottom-style: hidden; }
 #ypuvdjuebr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ypuvdjuebr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ypuvdjuebr .gt_from_md> :first-child { margin-top: 0; }
 #ypuvdjuebr .gt_from_md> :last-child { margin-bottom: 0; }
 #ypuvdjuebr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ypuvdjuebr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ypuvdjuebr .gt_indent_1 { text-indent: 5px; }
 #ypuvdjuebr .gt_indent_2 { text-indent: calc(5px * 2); }
 #ypuvdjuebr .gt_indent_3 { text-indent: calc(5px * 3); }
 #ypuvdjuebr .gt_indent_4 { text-indent: calc(5px * 4); }
 #ypuvdjuebr .gt_indent_5 { text-indent: calc(5px * 5); }
 #ypuvdjuebr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ypuvdjuebr .gt_row_group_first td { border-top-width: 2px; }
 #ypuvdjuebr .gt_row_group_first th { border-top-width: 2px; }
 #ypuvdjuebr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ypuvdjuebr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ypuvdjuebr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ypuvdjuebr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ypuvdjuebr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ypuvdjuebr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ypuvdjuebr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ypuvdjuebr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ypuvdjuebr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ypuvdjuebr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ypuvdjuebr .gt_left { text-align: left; }
 #ypuvdjuebr .gt_center { text-align: center; }
 #ypuvdjuebr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ypuvdjuebr .gt_font_normal { font-weight: normal; }
 #ypuvdjuebr .gt_font_bold { font-weight: bold; }
 #ypuvdjuebr .gt_font_italic { font-style: italic; }
 #ypuvdjuebr .gt_super { font-size: 65%; }
 #ypuvdjuebr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ypuvdjuebr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ypuvdjuebr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ypuvdjuebr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ypuvdjuebr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ypuvdjuebr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ckkvcdebos table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ckkvcdebos thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ckkvcdebos p { margin: 0; padding: 0; }
 #ckkvcdebos .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ckkvcdebos .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ckkvcdebos .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ckkvcdebos .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ckkvcdebos .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ckkvcdebos .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ckkvcdebos .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ckkvcdebos .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ckkvcdebos .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ckkvcdebos .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ckkvcdebos .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ckkvcdebos .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ckkvcdebos .gt_spanner_row { border-bottom-style: hidden; }
 #ckkvcdebos .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ckkvcdebos .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ckkvcdebos .gt_from_md> :first-child { margin-top: 0; }
 #ckkvcdebos .gt_from_md> :last-child { margin-bottom: 0; }
 #ckkvcdebos .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ckkvcdebos .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ckkvcdebos .gt_indent_1 { text-indent: 5px; }
 #ckkvcdebos .gt_indent_2 { text-indent: calc(5px * 2); }
 #ckkvcdebos .gt_indent_3 { text-indent: calc(5px * 3); }
 #ckkvcdebos .gt_indent_4 { text-indent: calc(5px * 4); }
 #ckkvcdebos .gt_indent_5 { text-indent: calc(5px * 5); }
 #ckkvcdebos .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ckkvcdebos .gt_row_group_first td { border-top-width: 2px; }
 #ckkvcdebos .gt_row_group_first th { border-top-width: 2px; }
 #ckkvcdebos .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ckkvcdebos .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ckkvcdebos .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ckkvcdebos .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ckkvcdebos .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ckkvcdebos .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ckkvcdebos .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ckkvcdebos .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ckkvcdebos .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ckkvcdebos .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ckkvcdebos .gt_left { text-align: left; }
 #ckkvcdebos .gt_center { text-align: center; }
 #ckkvcdebos .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ckkvcdebos .gt_font_normal { font-weight: normal; }
 #ckkvcdebos .gt_font_bold { font-weight: bold; }
 #ckkvcdebos .gt_font_italic { font-style: italic; }
 #ckkvcdebos .gt_super { font-size: 65%; }
 #ckkvcdebos .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ckkvcdebos .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ckkvcdebos .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ckkvcdebos .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ckkvcdebos .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ckkvcdebos .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jdrdnxixne table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jdrdnxixne thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jdrdnxixne p { margin: 0; padding: 0; }
 #jdrdnxixne .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jdrdnxixne .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jdrdnxixne .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jdrdnxixne .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jdrdnxixne .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jdrdnxixne .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jdrdnxixne .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jdrdnxixne .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jdrdnxixne .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jdrdnxixne .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jdrdnxixne .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jdrdnxixne .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jdrdnxixne .gt_spanner_row { border-bottom-style: hidden; }
 #jdrdnxixne .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jdrdnxixne .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jdrdnxixne .gt_from_md> :first-child { margin-top: 0; }
 #jdrdnxixne .gt_from_md> :last-child { margin-bottom: 0; }
 #jdrdnxixne .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jdrdnxixne .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jdrdnxixne .gt_indent_1 { text-indent: 5px; }
 #jdrdnxixne .gt_indent_2 { text-indent: calc(5px * 2); }
 #jdrdnxixne .gt_indent_3 { text-indent: calc(5px * 3); }
 #jdrdnxixne .gt_indent_4 { text-indent: calc(5px * 4); }
 #jdrdnxixne .gt_indent_5 { text-indent: calc(5px * 5); }
 #jdrdnxixne .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jdrdnxixne .gt_row_group_first td { border-top-width: 2px; }
 #jdrdnxixne .gt_row_group_first th { border-top-width: 2px; }
 #jdrdnxixne .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jdrdnxixne .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jdrdnxixne .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jdrdnxixne .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jdrdnxixne .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jdrdnxixne .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jdrdnxixne .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jdrdnxixne .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jdrdnxixne .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jdrdnxixne .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jdrdnxixne .gt_left { text-align: left; }
 #jdrdnxixne .gt_center { text-align: center; }
 #jdrdnxixne .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jdrdnxixne .gt_font_normal { font-weight: normal; }
 #jdrdnxixne .gt_font_bold { font-weight: bold; }
 #jdrdnxixne .gt_font_italic { font-style: italic; }
 #jdrdnxixne .gt_super { font-size: 65%; }
 #jdrdnxixne .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jdrdnxixne .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jdrdnxixne .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jdrdnxixne .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jdrdnxixne .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jdrdnxixne .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xmelfmskqs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xmelfmskqs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xmelfmskqs p { margin: 0; padding: 0; }
 #xmelfmskqs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xmelfmskqs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xmelfmskqs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xmelfmskqs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xmelfmskqs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xmelfmskqs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmelfmskqs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xmelfmskqs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xmelfmskqs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xmelfmskqs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xmelfmskqs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xmelfmskqs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xmelfmskqs .gt_spanner_row { border-bottom-style: hidden; }
 #xmelfmskqs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xmelfmskqs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xmelfmskqs .gt_from_md> :first-child { margin-top: 0; }
 #xmelfmskqs .gt_from_md> :last-child { margin-bottom: 0; }
 #xmelfmskqs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xmelfmskqs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xmelfmskqs .gt_indent_1 { text-indent: 5px; }
 #xmelfmskqs .gt_indent_2 { text-indent: calc(5px * 2); }
 #xmelfmskqs .gt_indent_3 { text-indent: calc(5px * 3); }
 #xmelfmskqs .gt_indent_4 { text-indent: calc(5px * 4); }
 #xmelfmskqs .gt_indent_5 { text-indent: calc(5px * 5); }
 #xmelfmskqs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xmelfmskqs .gt_row_group_first td { border-top-width: 2px; }
 #xmelfmskqs .gt_row_group_first th { border-top-width: 2px; }
 #xmelfmskqs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xmelfmskqs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmelfmskqs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xmelfmskqs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xmelfmskqs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmelfmskqs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xmelfmskqs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xmelfmskqs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xmelfmskqs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmelfmskqs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xmelfmskqs .gt_left { text-align: left; }
 #xmelfmskqs .gt_center { text-align: center; }
 #xmelfmskqs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xmelfmskqs .gt_font_normal { font-weight: normal; }
 #xmelfmskqs .gt_font_bold { font-weight: bold; }
 #xmelfmskqs .gt_font_italic { font-style: italic; }
 #xmelfmskqs .gt_super { font-size: 65%; }
 #xmelfmskqs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmelfmskqs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xmelfmskqs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmelfmskqs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xmelfmskqs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xmelfmskqs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xmdhfkwkme table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xmdhfkwkme thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xmdhfkwkme p { margin: 0; padding: 0; }
 #xmdhfkwkme .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xmdhfkwkme .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xmdhfkwkme .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xmdhfkwkme .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xmdhfkwkme .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xmdhfkwkme .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmdhfkwkme .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xmdhfkwkme .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xmdhfkwkme .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xmdhfkwkme .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xmdhfkwkme .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xmdhfkwkme .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xmdhfkwkme .gt_spanner_row { border-bottom-style: hidden; }
 #xmdhfkwkme .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xmdhfkwkme .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xmdhfkwkme .gt_from_md> :first-child { margin-top: 0; }
 #xmdhfkwkme .gt_from_md> :last-child { margin-bottom: 0; }
 #xmdhfkwkme .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xmdhfkwkme .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xmdhfkwkme .gt_indent_1 { text-indent: 5px; }
 #xmdhfkwkme .gt_indent_2 { text-indent: calc(5px * 2); }
 #xmdhfkwkme .gt_indent_3 { text-indent: calc(5px * 3); }
 #xmdhfkwkme .gt_indent_4 { text-indent: calc(5px * 4); }
 #xmdhfkwkme .gt_indent_5 { text-indent: calc(5px * 5); }
 #xmdhfkwkme .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xmdhfkwkme .gt_row_group_first td { border-top-width: 2px; }
 #xmdhfkwkme .gt_row_group_first th { border-top-width: 2px; }
 #xmdhfkwkme .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xmdhfkwkme .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmdhfkwkme .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xmdhfkwkme .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xmdhfkwkme .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmdhfkwkme .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xmdhfkwkme .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xmdhfkwkme .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xmdhfkwkme .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmdhfkwkme .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xmdhfkwkme .gt_left { text-align: left; }
 #xmdhfkwkme .gt_center { text-align: center; }
 #xmdhfkwkme .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xmdhfkwkme .gt_font_normal { font-weight: normal; }
 #xmdhfkwkme .gt_font_bold { font-weight: bold; }
 #xmdhfkwkme .gt_font_italic { font-style: italic; }
 #xmdhfkwkme .gt_super { font-size: 65%; }
 #xmdhfkwkme .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmdhfkwkme .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xmdhfkwkme .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmdhfkwkme .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xmdhfkwkme .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xmdhfkwkme .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wzqfzvwytl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wzqfzvwytl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wzqfzvwytl p { margin: 0; padding: 0; }
 #wzqfzvwytl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wzqfzvwytl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wzqfzvwytl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wzqfzvwytl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wzqfzvwytl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wzqfzvwytl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wzqfzvwytl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wzqfzvwytl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wzqfzvwytl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wzqfzvwytl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wzqfzvwytl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wzqfzvwytl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wzqfzvwytl .gt_spanner_row { border-bottom-style: hidden; }
 #wzqfzvwytl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wzqfzvwytl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wzqfzvwytl .gt_from_md> :first-child { margin-top: 0; }
 #wzqfzvwytl .gt_from_md> :last-child { margin-bottom: 0; }
 #wzqfzvwytl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wzqfzvwytl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wzqfzvwytl .gt_indent_1 { text-indent: 5px; }
 #wzqfzvwytl .gt_indent_2 { text-indent: calc(5px * 2); }
 #wzqfzvwytl .gt_indent_3 { text-indent: calc(5px * 3); }
 #wzqfzvwytl .gt_indent_4 { text-indent: calc(5px * 4); }
 #wzqfzvwytl .gt_indent_5 { text-indent: calc(5px * 5); }
 #wzqfzvwytl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wzqfzvwytl .gt_row_group_first td { border-top-width: 2px; }
 #wzqfzvwytl .gt_row_group_first th { border-top-width: 2px; }
 #wzqfzvwytl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wzqfzvwytl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wzqfzvwytl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wzqfzvwytl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wzqfzvwytl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wzqfzvwytl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wzqfzvwytl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wzqfzvwytl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wzqfzvwytl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wzqfzvwytl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wzqfzvwytl .gt_left { text-align: left; }
 #wzqfzvwytl .gt_center { text-align: center; }
 #wzqfzvwytl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wzqfzvwytl .gt_font_normal { font-weight: normal; }
 #wzqfzvwytl .gt_font_bold { font-weight: bold; }
 #wzqfzvwytl .gt_font_italic { font-style: italic; }
 #wzqfzvwytl .gt_super { font-size: 65%; }
 #wzqfzvwytl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wzqfzvwytl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wzqfzvwytl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wzqfzvwytl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wzqfzvwytl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wzqfzvwytl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#exuevjvwqt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#exuevjvwqt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#exuevjvwqt p { margin: 0; padding: 0; }
 #exuevjvwqt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #exuevjvwqt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #exuevjvwqt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #exuevjvwqt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #exuevjvwqt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #exuevjvwqt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exuevjvwqt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #exuevjvwqt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #exuevjvwqt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #exuevjvwqt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #exuevjvwqt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #exuevjvwqt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #exuevjvwqt .gt_spanner_row { border-bottom-style: hidden; }
 #exuevjvwqt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #exuevjvwqt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #exuevjvwqt .gt_from_md> :first-child { margin-top: 0; }
 #exuevjvwqt .gt_from_md> :last-child { margin-bottom: 0; }
 #exuevjvwqt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #exuevjvwqt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #exuevjvwqt .gt_indent_1 { text-indent: 5px; }
 #exuevjvwqt .gt_indent_2 { text-indent: calc(5px * 2); }
 #exuevjvwqt .gt_indent_3 { text-indent: calc(5px * 3); }
 #exuevjvwqt .gt_indent_4 { text-indent: calc(5px * 4); }
 #exuevjvwqt .gt_indent_5 { text-indent: calc(5px * 5); }
 #exuevjvwqt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #exuevjvwqt .gt_row_group_first td { border-top-width: 2px; }
 #exuevjvwqt .gt_row_group_first th { border-top-width: 2px; }
 #exuevjvwqt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #exuevjvwqt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exuevjvwqt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #exuevjvwqt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #exuevjvwqt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exuevjvwqt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #exuevjvwqt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #exuevjvwqt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #exuevjvwqt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exuevjvwqt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #exuevjvwqt .gt_left { text-align: left; }
 #exuevjvwqt .gt_center { text-align: center; }
 #exuevjvwqt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #exuevjvwqt .gt_font_normal { font-weight: normal; }
 #exuevjvwqt .gt_font_bold { font-weight: bold; }
 #exuevjvwqt .gt_font_italic { font-style: italic; }
 #exuevjvwqt .gt_super { font-size: 65%; }
 #exuevjvwqt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exuevjvwqt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #exuevjvwqt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exuevjvwqt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #exuevjvwqt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #exuevjvwqt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
