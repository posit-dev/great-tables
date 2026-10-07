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
#pzildqduzw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pzildqduzw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pzildqduzw p { margin: 0; padding: 0; }
 #pzildqduzw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pzildqduzw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pzildqduzw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pzildqduzw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pzildqduzw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pzildqduzw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pzildqduzw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pzildqduzw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pzildqduzw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pzildqduzw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pzildqduzw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pzildqduzw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pzildqduzw .gt_spanner_row { border-bottom-style: hidden; }
 #pzildqduzw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pzildqduzw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pzildqduzw .gt_from_md> :first-child { margin-top: 0; }
 #pzildqduzw .gt_from_md> :last-child { margin-bottom: 0; }
 #pzildqduzw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pzildqduzw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pzildqduzw .gt_indent_1 { text-indent: 5px; }
 #pzildqduzw .gt_indent_2 { text-indent: calc(5px * 2); }
 #pzildqduzw .gt_indent_3 { text-indent: calc(5px * 3); }
 #pzildqduzw .gt_indent_4 { text-indent: calc(5px * 4); }
 #pzildqduzw .gt_indent_5 { text-indent: calc(5px * 5); }
 #pzildqduzw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pzildqduzw .gt_row_group_first td { border-top-width: 2px; }
 #pzildqduzw .gt_row_group_first th { border-top-width: 2px; }
 #pzildqduzw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pzildqduzw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pzildqduzw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pzildqduzw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pzildqduzw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pzildqduzw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pzildqduzw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pzildqduzw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pzildqduzw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pzildqduzw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pzildqduzw .gt_left { text-align: left; }
 #pzildqduzw .gt_center { text-align: center; }
 #pzildqduzw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pzildqduzw .gt_font_normal { font-weight: normal; }
 #pzildqduzw .gt_font_bold { font-weight: bold; }
 #pzildqduzw .gt_font_italic { font-style: italic; }
 #pzildqduzw .gt_super { font-size: 65%; }
 #pzildqduzw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pzildqduzw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pzildqduzw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pzildqduzw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pzildqduzw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pzildqduzw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ababdiujkw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ababdiujkw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ababdiujkw p { margin: 0; padding: 0; }
 #ababdiujkw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ababdiujkw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ababdiujkw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ababdiujkw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ababdiujkw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ababdiujkw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ababdiujkw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ababdiujkw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ababdiujkw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ababdiujkw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ababdiujkw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ababdiujkw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ababdiujkw .gt_spanner_row { border-bottom-style: hidden; }
 #ababdiujkw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ababdiujkw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ababdiujkw .gt_from_md> :first-child { margin-top: 0; }
 #ababdiujkw .gt_from_md> :last-child { margin-bottom: 0; }
 #ababdiujkw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ababdiujkw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ababdiujkw .gt_indent_1 { text-indent: 5px; }
 #ababdiujkw .gt_indent_2 { text-indent: calc(5px * 2); }
 #ababdiujkw .gt_indent_3 { text-indent: calc(5px * 3); }
 #ababdiujkw .gt_indent_4 { text-indent: calc(5px * 4); }
 #ababdiujkw .gt_indent_5 { text-indent: calc(5px * 5); }
 #ababdiujkw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ababdiujkw .gt_row_group_first td { border-top-width: 2px; }
 #ababdiujkw .gt_row_group_first th { border-top-width: 2px; }
 #ababdiujkw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ababdiujkw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ababdiujkw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ababdiujkw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ababdiujkw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ababdiujkw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ababdiujkw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ababdiujkw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ababdiujkw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ababdiujkw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ababdiujkw .gt_left { text-align: left; }
 #ababdiujkw .gt_center { text-align: center; }
 #ababdiujkw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ababdiujkw .gt_font_normal { font-weight: normal; }
 #ababdiujkw .gt_font_bold { font-weight: bold; }
 #ababdiujkw .gt_font_italic { font-style: italic; }
 #ababdiujkw .gt_super { font-size: 65%; }
 #ababdiujkw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ababdiujkw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ababdiujkw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ababdiujkw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ababdiujkw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ababdiujkw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uvobppfrgs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uvobppfrgs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uvobppfrgs p { margin: 0; padding: 0; }
 #uvobppfrgs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uvobppfrgs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uvobppfrgs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uvobppfrgs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uvobppfrgs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvobppfrgs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvobppfrgs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvobppfrgs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uvobppfrgs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uvobppfrgs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uvobppfrgs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uvobppfrgs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uvobppfrgs .gt_spanner_row { border-bottom-style: hidden; }
 #uvobppfrgs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uvobppfrgs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uvobppfrgs .gt_from_md> :first-child { margin-top: 0; }
 #uvobppfrgs .gt_from_md> :last-child { margin-bottom: 0; }
 #uvobppfrgs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uvobppfrgs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uvobppfrgs .gt_indent_1 { text-indent: 5px; }
 #uvobppfrgs .gt_indent_2 { text-indent: calc(5px * 2); }
 #uvobppfrgs .gt_indent_3 { text-indent: calc(5px * 3); }
 #uvobppfrgs .gt_indent_4 { text-indent: calc(5px * 4); }
 #uvobppfrgs .gt_indent_5 { text-indent: calc(5px * 5); }
 #uvobppfrgs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uvobppfrgs .gt_row_group_first td { border-top-width: 2px; }
 #uvobppfrgs .gt_row_group_first th { border-top-width: 2px; }
 #uvobppfrgs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uvobppfrgs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvobppfrgs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvobppfrgs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uvobppfrgs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvobppfrgs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvobppfrgs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uvobppfrgs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uvobppfrgs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvobppfrgs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvobppfrgs .gt_left { text-align: left; }
 #uvobppfrgs .gt_center { text-align: center; }
 #uvobppfrgs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uvobppfrgs .gt_font_normal { font-weight: normal; }
 #uvobppfrgs .gt_font_bold { font-weight: bold; }
 #uvobppfrgs .gt_font_italic { font-style: italic; }
 #uvobppfrgs .gt_super { font-size: 65%; }
 #uvobppfrgs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvobppfrgs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uvobppfrgs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvobppfrgs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvobppfrgs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uvobppfrgs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#nvkrkodpth table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nvkrkodpth thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nvkrkodpth p { margin: 0; padding: 0; }
 #nvkrkodpth .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nvkrkodpth .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nvkrkodpth .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nvkrkodpth .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nvkrkodpth .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nvkrkodpth .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvkrkodpth .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nvkrkodpth .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nvkrkodpth .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nvkrkodpth .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nvkrkodpth .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nvkrkodpth .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nvkrkodpth .gt_spanner_row { border-bottom-style: hidden; }
 #nvkrkodpth .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nvkrkodpth .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nvkrkodpth .gt_from_md> :first-child { margin-top: 0; }
 #nvkrkodpth .gt_from_md> :last-child { margin-bottom: 0; }
 #nvkrkodpth .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nvkrkodpth .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nvkrkodpth .gt_indent_1 { text-indent: 5px; }
 #nvkrkodpth .gt_indent_2 { text-indent: calc(5px * 2); }
 #nvkrkodpth .gt_indent_3 { text-indent: calc(5px * 3); }
 #nvkrkodpth .gt_indent_4 { text-indent: calc(5px * 4); }
 #nvkrkodpth .gt_indent_5 { text-indent: calc(5px * 5); }
 #nvkrkodpth .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nvkrkodpth .gt_row_group_first td { border-top-width: 2px; }
 #nvkrkodpth .gt_row_group_first th { border-top-width: 2px; }
 #nvkrkodpth .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nvkrkodpth .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvkrkodpth .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nvkrkodpth .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nvkrkodpth .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvkrkodpth .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nvkrkodpth .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nvkrkodpth .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nvkrkodpth .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvkrkodpth .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nvkrkodpth .gt_left { text-align: left; }
 #nvkrkodpth .gt_center { text-align: center; }
 #nvkrkodpth .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nvkrkodpth .gt_font_normal { font-weight: normal; }
 #nvkrkodpth .gt_font_bold { font-weight: bold; }
 #nvkrkodpth .gt_font_italic { font-style: italic; }
 #nvkrkodpth .gt_super { font-size: 65%; }
 #nvkrkodpth .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvkrkodpth .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nvkrkodpth .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvkrkodpth .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nvkrkodpth .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nvkrkodpth .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#skruswrybg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#skruswrybg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#skruswrybg p { margin: 0; padding: 0; }
 #skruswrybg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #skruswrybg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #skruswrybg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #skruswrybg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #skruswrybg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #skruswrybg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #skruswrybg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #skruswrybg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #skruswrybg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #skruswrybg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #skruswrybg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #skruswrybg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #skruswrybg .gt_spanner_row { border-bottom-style: hidden; }
 #skruswrybg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #skruswrybg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #skruswrybg .gt_from_md> :first-child { margin-top: 0; }
 #skruswrybg .gt_from_md> :last-child { margin-bottom: 0; }
 #skruswrybg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #skruswrybg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #skruswrybg .gt_indent_1 { text-indent: 5px; }
 #skruswrybg .gt_indent_2 { text-indent: calc(5px * 2); }
 #skruswrybg .gt_indent_3 { text-indent: calc(5px * 3); }
 #skruswrybg .gt_indent_4 { text-indent: calc(5px * 4); }
 #skruswrybg .gt_indent_5 { text-indent: calc(5px * 5); }
 #skruswrybg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #skruswrybg .gt_row_group_first td { border-top-width: 2px; }
 #skruswrybg .gt_row_group_first th { border-top-width: 2px; }
 #skruswrybg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #skruswrybg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #skruswrybg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #skruswrybg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #skruswrybg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #skruswrybg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #skruswrybg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #skruswrybg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #skruswrybg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #skruswrybg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #skruswrybg .gt_left { text-align: left; }
 #skruswrybg .gt_center { text-align: center; }
 #skruswrybg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #skruswrybg .gt_font_normal { font-weight: normal; }
 #skruswrybg .gt_font_bold { font-weight: bold; }
 #skruswrybg .gt_font_italic { font-style: italic; }
 #skruswrybg .gt_super { font-size: 65%; }
 #skruswrybg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #skruswrybg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #skruswrybg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #skruswrybg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #skruswrybg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #skruswrybg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#imzuqlhkjw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#imzuqlhkjw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#imzuqlhkjw p { margin: 0; padding: 0; }
 #imzuqlhkjw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #imzuqlhkjw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #imzuqlhkjw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #imzuqlhkjw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #imzuqlhkjw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #imzuqlhkjw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #imzuqlhkjw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #imzuqlhkjw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #imzuqlhkjw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #imzuqlhkjw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #imzuqlhkjw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #imzuqlhkjw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #imzuqlhkjw .gt_spanner_row { border-bottom-style: hidden; }
 #imzuqlhkjw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #imzuqlhkjw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #imzuqlhkjw .gt_from_md> :first-child { margin-top: 0; }
 #imzuqlhkjw .gt_from_md> :last-child { margin-bottom: 0; }
 #imzuqlhkjw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #imzuqlhkjw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #imzuqlhkjw .gt_indent_1 { text-indent: 5px; }
 #imzuqlhkjw .gt_indent_2 { text-indent: calc(5px * 2); }
 #imzuqlhkjw .gt_indent_3 { text-indent: calc(5px * 3); }
 #imzuqlhkjw .gt_indent_4 { text-indent: calc(5px * 4); }
 #imzuqlhkjw .gt_indent_5 { text-indent: calc(5px * 5); }
 #imzuqlhkjw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #imzuqlhkjw .gt_row_group_first td { border-top-width: 2px; }
 #imzuqlhkjw .gt_row_group_first th { border-top-width: 2px; }
 #imzuqlhkjw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #imzuqlhkjw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #imzuqlhkjw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #imzuqlhkjw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #imzuqlhkjw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #imzuqlhkjw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #imzuqlhkjw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #imzuqlhkjw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #imzuqlhkjw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #imzuqlhkjw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #imzuqlhkjw .gt_left { text-align: left; }
 #imzuqlhkjw .gt_center { text-align: center; }
 #imzuqlhkjw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #imzuqlhkjw .gt_font_normal { font-weight: normal; }
 #imzuqlhkjw .gt_font_bold { font-weight: bold; }
 #imzuqlhkjw .gt_font_italic { font-style: italic; }
 #imzuqlhkjw .gt_super { font-size: 65%; }
 #imzuqlhkjw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #imzuqlhkjw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #imzuqlhkjw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #imzuqlhkjw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #imzuqlhkjw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #imzuqlhkjw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#deoqymsopl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#deoqymsopl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#deoqymsopl p { margin: 0; padding: 0; }
 #deoqymsopl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #deoqymsopl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #deoqymsopl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #deoqymsopl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #deoqymsopl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #deoqymsopl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #deoqymsopl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #deoqymsopl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #deoqymsopl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #deoqymsopl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #deoqymsopl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #deoqymsopl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #deoqymsopl .gt_spanner_row { border-bottom-style: hidden; }
 #deoqymsopl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #deoqymsopl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #deoqymsopl .gt_from_md> :first-child { margin-top: 0; }
 #deoqymsopl .gt_from_md> :last-child { margin-bottom: 0; }
 #deoqymsopl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #deoqymsopl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #deoqymsopl .gt_indent_1 { text-indent: 5px; }
 #deoqymsopl .gt_indent_2 { text-indent: calc(5px * 2); }
 #deoqymsopl .gt_indent_3 { text-indent: calc(5px * 3); }
 #deoqymsopl .gt_indent_4 { text-indent: calc(5px * 4); }
 #deoqymsopl .gt_indent_5 { text-indent: calc(5px * 5); }
 #deoqymsopl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #deoqymsopl .gt_row_group_first td { border-top-width: 2px; }
 #deoqymsopl .gt_row_group_first th { border-top-width: 2px; }
 #deoqymsopl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #deoqymsopl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #deoqymsopl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #deoqymsopl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #deoqymsopl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #deoqymsopl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #deoqymsopl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #deoqymsopl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #deoqymsopl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #deoqymsopl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #deoqymsopl .gt_left { text-align: left; }
 #deoqymsopl .gt_center { text-align: center; }
 #deoqymsopl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #deoqymsopl .gt_font_normal { font-weight: normal; }
 #deoqymsopl .gt_font_bold { font-weight: bold; }
 #deoqymsopl .gt_font_italic { font-style: italic; }
 #deoqymsopl .gt_super { font-size: 65%; }
 #deoqymsopl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #deoqymsopl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #deoqymsopl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #deoqymsopl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #deoqymsopl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #deoqymsopl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wnlhllqrxh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wnlhllqrxh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wnlhllqrxh p { margin: 0; padding: 0; }
 #wnlhllqrxh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wnlhllqrxh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wnlhllqrxh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wnlhllqrxh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wnlhllqrxh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnlhllqrxh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnlhllqrxh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnlhllqrxh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wnlhllqrxh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wnlhllqrxh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wnlhllqrxh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wnlhllqrxh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wnlhllqrxh .gt_spanner_row { border-bottom-style: hidden; }
 #wnlhllqrxh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wnlhllqrxh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wnlhllqrxh .gt_from_md> :first-child { margin-top: 0; }
 #wnlhllqrxh .gt_from_md> :last-child { margin-bottom: 0; }
 #wnlhllqrxh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wnlhllqrxh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wnlhllqrxh .gt_indent_1 { text-indent: 5px; }
 #wnlhllqrxh .gt_indent_2 { text-indent: calc(5px * 2); }
 #wnlhllqrxh .gt_indent_3 { text-indent: calc(5px * 3); }
 #wnlhllqrxh .gt_indent_4 { text-indent: calc(5px * 4); }
 #wnlhllqrxh .gt_indent_5 { text-indent: calc(5px * 5); }
 #wnlhllqrxh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wnlhllqrxh .gt_row_group_first td { border-top-width: 2px; }
 #wnlhllqrxh .gt_row_group_first th { border-top-width: 2px; }
 #wnlhllqrxh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wnlhllqrxh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnlhllqrxh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnlhllqrxh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wnlhllqrxh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnlhllqrxh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnlhllqrxh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wnlhllqrxh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wnlhllqrxh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnlhllqrxh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnlhllqrxh .gt_left { text-align: left; }
 #wnlhllqrxh .gt_center { text-align: center; }
 #wnlhllqrxh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wnlhllqrxh .gt_font_normal { font-weight: normal; }
 #wnlhllqrxh .gt_font_bold { font-weight: bold; }
 #wnlhllqrxh .gt_font_italic { font-style: italic; }
 #wnlhllqrxh .gt_super { font-size: 65%; }
 #wnlhllqrxh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnlhllqrxh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wnlhllqrxh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnlhllqrxh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnlhllqrxh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wnlhllqrxh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cfrwjuylid table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cfrwjuylid thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cfrwjuylid p { margin: 0; padding: 0; }
 #cfrwjuylid .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cfrwjuylid .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cfrwjuylid .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cfrwjuylid .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cfrwjuylid .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cfrwjuylid .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cfrwjuylid .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cfrwjuylid .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cfrwjuylid .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cfrwjuylid .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cfrwjuylid .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cfrwjuylid .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cfrwjuylid .gt_spanner_row { border-bottom-style: hidden; }
 #cfrwjuylid .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cfrwjuylid .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cfrwjuylid .gt_from_md> :first-child { margin-top: 0; }
 #cfrwjuylid .gt_from_md> :last-child { margin-bottom: 0; }
 #cfrwjuylid .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cfrwjuylid .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cfrwjuylid .gt_indent_1 { text-indent: 5px; }
 #cfrwjuylid .gt_indent_2 { text-indent: calc(5px * 2); }
 #cfrwjuylid .gt_indent_3 { text-indent: calc(5px * 3); }
 #cfrwjuylid .gt_indent_4 { text-indent: calc(5px * 4); }
 #cfrwjuylid .gt_indent_5 { text-indent: calc(5px * 5); }
 #cfrwjuylid .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cfrwjuylid .gt_row_group_first td { border-top-width: 2px; }
 #cfrwjuylid .gt_row_group_first th { border-top-width: 2px; }
 #cfrwjuylid .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cfrwjuylid .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cfrwjuylid .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cfrwjuylid .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cfrwjuylid .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cfrwjuylid .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cfrwjuylid .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cfrwjuylid .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cfrwjuylid .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cfrwjuylid .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cfrwjuylid .gt_left { text-align: left; }
 #cfrwjuylid .gt_center { text-align: center; }
 #cfrwjuylid .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cfrwjuylid .gt_font_normal { font-weight: normal; }
 #cfrwjuylid .gt_font_bold { font-weight: bold; }
 #cfrwjuylid .gt_font_italic { font-style: italic; }
 #cfrwjuylid .gt_super { font-size: 65%; }
 #cfrwjuylid .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cfrwjuylid .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cfrwjuylid .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cfrwjuylid .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cfrwjuylid .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cfrwjuylid .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
