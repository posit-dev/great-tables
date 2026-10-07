# GT.summary_rows()


Add group-wise summary rows to the table.


Usage

``` python
GT.summary_rows(
    *,
    fns,
    fmt=None,
    columns=None,
    groups=None,
    side="bottom",
    missing_text="---",
)
```


Add summary rows by using the table data and any suitable aggregation functions. With [summary_rows()](GT.summary_rows.md#great_tables.GT.summary_rows), the data within each row group is aggregated separately and summary rows are placed adjacent to each group. Multiple summary rows can be added via expressions given to `fns=`. You can selectively format the values in the resulting summary cells by use of formatting expressions from the `vals.fmt_*` class of functions.

Note that currently all arguments are keyword-only, since the final positions may change.


## Parameters


`fns: dict[str, PlExpr] | dict[str, Callable[[TblData], Any]]`  
A dictionary mapping row labels to aggregation expressions. Can be either Polars expressions or callable functions that take a DataFrame subset and return aggregated results. Each key becomes the label for a summary row within each group.

`fmt: FormatFn | None = None`  
A formatting function from the `vals.fmt_*` family (e.g., [vals.fmt_number](vals.fmt_number.md#great_tables.vals.fmt_number), [vals.fmt_currency](vals.fmt_currency.md#great_tables.vals.fmt_currency)) to apply to the summary row values. If `None`, no formatting is applied.

`columns: SelectExpr = None`  
Currently, this function does not support selection by columns. If you would like to choose which columns to summarize, you can select columns within the functions given to `fns=`. See examples below for more explicit cases.

`groups: list[str] | None = None`  
The groups to target for summary row insertion. Can be a list of group IDs as strings. By default (`None`), summary rows are generated for all groups.

`side: Literal[``"bottom", `<span class="st">`"top"``]`</span>` = ``"bottom"`  
Should the summary rows be placed at the `"bottom"` (the default) or the `"top"` of each group?

`missing_text: str = ``"--"`  
The text to be used in summary cells with no data outputs.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset to create a table with group summary rows. We'll group by manufacturer and show min and max values for horsepower and torque columns.


``` python
import polars as pl
from great_tables import GT, vals
from great_tables.data import gtcars

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "hp", "trq"])
    .head(12)
)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .summary_rows(
        fns={
            "Min": pl.col("hp", "trq").min(),
            "Max": pl.col("hp", "trq").max(),
        },
        fmt=vals.fmt_integer,
    )
)
```


<style>
#ccnpqziqse table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ccnpqziqse thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ccnpqziqse p { margin: 0; padding: 0; }
 #ccnpqziqse .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ccnpqziqse .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ccnpqziqse .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ccnpqziqse .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ccnpqziqse .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ccnpqziqse .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ccnpqziqse .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ccnpqziqse .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ccnpqziqse .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ccnpqziqse .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ccnpqziqse .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ccnpqziqse .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ccnpqziqse .gt_spanner_row { border-bottom-style: hidden; }
 #ccnpqziqse .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ccnpqziqse .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ccnpqziqse .gt_from_md> :first-child { margin-top: 0; }
 #ccnpqziqse .gt_from_md> :last-child { margin-bottom: 0; }
 #ccnpqziqse .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ccnpqziqse .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ccnpqziqse .gt_indent_1 { text-indent: 5px; }
 #ccnpqziqse .gt_indent_2 { text-indent: calc(5px * 2); }
 #ccnpqziqse .gt_indent_3 { text-indent: calc(5px * 3); }
 #ccnpqziqse .gt_indent_4 { text-indent: calc(5px * 4); }
 #ccnpqziqse .gt_indent_5 { text-indent: calc(5px * 5); }
 #ccnpqziqse .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ccnpqziqse .gt_row_group_first td { border-top-width: 2px; }
 #ccnpqziqse .gt_row_group_first th { border-top-width: 2px; }
 #ccnpqziqse .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ccnpqziqse .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ccnpqziqse .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ccnpqziqse .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ccnpqziqse .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ccnpqziqse .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ccnpqziqse .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ccnpqziqse .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ccnpqziqse .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ccnpqziqse .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ccnpqziqse .gt_left { text-align: left; }
 #ccnpqziqse .gt_center { text-align: center; }
 #ccnpqziqse .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ccnpqziqse .gt_font_normal { font-weight: normal; }
 #ccnpqziqse .gt_font_bold { font-weight: bold; }
 #ccnpqziqse .gt_font_italic { font-style: italic; }
 #ccnpqziqse .gt_super { font-size: 65%; }
 #ccnpqziqse .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ccnpqziqse .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ccnpqziqse .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ccnpqziqse .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ccnpqziqse .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ccnpqziqse .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Ford</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">550.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">647</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">550</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row">647</td>
<td class="gt_row gt_right gt_summary_row">550</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Ferrari</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">California</td>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">557.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GTC4Lusso</td>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">514.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">FF</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">504.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">F12Berlinetta</td>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">509.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">LaFerrari</td>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">664.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">553</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">398</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row">949</td>
<td class="gt_row gt_right gt_summary_row">664</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Acura</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">NSX</td>
<td class="gt_row gt_right">573.0</td>
<td class="gt_row gt_right">476.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">573</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">476</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row">573</td>
<td class="gt_row gt_right gt_summary_row">476</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Nissan</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GT-R</td>
<td class="gt_row gt_right">545.0</td>
<td class="gt_row gt_right">436.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">545</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">436</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row">545</td>
<td class="gt_row gt_right gt_summary_row">436</td>
</tr>
</tbody>
</table>


We can also target specific groups by using the `groups=` parameter. Here we only show summary rows for the `"Ferrari"` group:


``` python
(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .summary_rows(
        fns={
            "Average": pl.col("hp", "trq").mean(),
        },
        groups=["Ferrari"],
        fmt=vals.fmt_number,
    )
)
```


<style>
#rdbpjfxyzo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rdbpjfxyzo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rdbpjfxyzo p { margin: 0; padding: 0; }
 #rdbpjfxyzo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rdbpjfxyzo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rdbpjfxyzo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rdbpjfxyzo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rdbpjfxyzo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rdbpjfxyzo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdbpjfxyzo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rdbpjfxyzo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rdbpjfxyzo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rdbpjfxyzo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rdbpjfxyzo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rdbpjfxyzo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rdbpjfxyzo .gt_spanner_row { border-bottom-style: hidden; }
 #rdbpjfxyzo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rdbpjfxyzo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rdbpjfxyzo .gt_from_md> :first-child { margin-top: 0; }
 #rdbpjfxyzo .gt_from_md> :last-child { margin-bottom: 0; }
 #rdbpjfxyzo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rdbpjfxyzo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rdbpjfxyzo .gt_indent_1 { text-indent: 5px; }
 #rdbpjfxyzo .gt_indent_2 { text-indent: calc(5px * 2); }
 #rdbpjfxyzo .gt_indent_3 { text-indent: calc(5px * 3); }
 #rdbpjfxyzo .gt_indent_4 { text-indent: calc(5px * 4); }
 #rdbpjfxyzo .gt_indent_5 { text-indent: calc(5px * 5); }
 #rdbpjfxyzo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rdbpjfxyzo .gt_row_group_first td { border-top-width: 2px; }
 #rdbpjfxyzo .gt_row_group_first th { border-top-width: 2px; }
 #rdbpjfxyzo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rdbpjfxyzo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdbpjfxyzo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rdbpjfxyzo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rdbpjfxyzo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdbpjfxyzo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rdbpjfxyzo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rdbpjfxyzo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rdbpjfxyzo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdbpjfxyzo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rdbpjfxyzo .gt_left { text-align: left; }
 #rdbpjfxyzo .gt_center { text-align: center; }
 #rdbpjfxyzo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rdbpjfxyzo .gt_font_normal { font-weight: normal; }
 #rdbpjfxyzo .gt_font_bold { font-weight: bold; }
 #rdbpjfxyzo .gt_font_italic { font-style: italic; }
 #rdbpjfxyzo .gt_super { font-size: 65%; }
 #rdbpjfxyzo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdbpjfxyzo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rdbpjfxyzo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdbpjfxyzo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rdbpjfxyzo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rdbpjfxyzo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Ford</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">550.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Ferrari</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">California</td>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">557.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GTC4Lusso</td>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">514.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">FF</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">504.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">F12Berlinetta</td>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">509.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">LaFerrari</td>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">664.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Average</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">660.78</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">500.33</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Acura</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">NSX</td>
<td class="gt_row gt_right">573.0</td>
<td class="gt_row gt_right">476.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Nissan</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GT-R</td>
<td class="gt_row gt_right">545.0</td>
<td class="gt_row gt_right">436.0</td>
</tr>
</tbody>
</table>


Callable functions work with pandas DataFrames. Each function receives the subset of data for that group:


``` python
from great_tables import GT, vals
from great_tables.data import gtcars

(
    GT(
        gtcars[["mfr", "model", "hp", "trq"]].head(12),
        rowname_col="model",
        groupname_col="mfr",
    )
    .summary_rows(
        fns={
            "Min": lambda df: df.min(numeric_only=True),
            "Max": lambda df: df.max(numeric_only=True),
        },
        fmt=vals.fmt_integer,
    )
)
```


<style>
#ztsycnpsij table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ztsycnpsij thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ztsycnpsij p { margin: 0; padding: 0; }
 #ztsycnpsij .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ztsycnpsij .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ztsycnpsij .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ztsycnpsij .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ztsycnpsij .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ztsycnpsij .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ztsycnpsij .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ztsycnpsij .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ztsycnpsij .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ztsycnpsij .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ztsycnpsij .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ztsycnpsij .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ztsycnpsij .gt_spanner_row { border-bottom-style: hidden; }
 #ztsycnpsij .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ztsycnpsij .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ztsycnpsij .gt_from_md> :first-child { margin-top: 0; }
 #ztsycnpsij .gt_from_md> :last-child { margin-bottom: 0; }
 #ztsycnpsij .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ztsycnpsij .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ztsycnpsij .gt_indent_1 { text-indent: 5px; }
 #ztsycnpsij .gt_indent_2 { text-indent: calc(5px * 2); }
 #ztsycnpsij .gt_indent_3 { text-indent: calc(5px * 3); }
 #ztsycnpsij .gt_indent_4 { text-indent: calc(5px * 4); }
 #ztsycnpsij .gt_indent_5 { text-indent: calc(5px * 5); }
 #ztsycnpsij .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ztsycnpsij .gt_row_group_first td { border-top-width: 2px; }
 #ztsycnpsij .gt_row_group_first th { border-top-width: 2px; }
 #ztsycnpsij .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ztsycnpsij .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ztsycnpsij .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ztsycnpsij .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ztsycnpsij .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ztsycnpsij .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ztsycnpsij .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ztsycnpsij .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ztsycnpsij .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ztsycnpsij .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ztsycnpsij .gt_left { text-align: left; }
 #ztsycnpsij .gt_center { text-align: center; }
 #ztsycnpsij .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ztsycnpsij .gt_font_normal { font-weight: normal; }
 #ztsycnpsij .gt_font_bold { font-weight: bold; }
 #ztsycnpsij .gt_font_italic { font-style: italic; }
 #ztsycnpsij .gt_super { font-size: 65%; }
 #ztsycnpsij .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ztsycnpsij .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ztsycnpsij .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ztsycnpsij .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ztsycnpsij .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ztsycnpsij .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Ford</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">550.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">647</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">550</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row">647</td>
<td class="gt_row gt_right gt_summary_row">550</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Ferrari</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">California</td>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">557.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GTC4Lusso</td>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">514.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">FF</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">504.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">F12Berlinetta</td>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">509.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">LaFerrari</td>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">664.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">553</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">398</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row">949</td>
<td class="gt_row gt_right gt_summary_row">664</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Acura</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">NSX</td>
<td class="gt_row gt_right">573.0</td>
<td class="gt_row gt_right">476.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">573</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">476</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row">573</td>
<td class="gt_row gt_right gt_summary_row">476</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Nissan</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GT-R</td>
<td class="gt_row gt_right">545.0</td>
<td class="gt_row gt_right">436.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">545</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">436</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row">545</td>
<td class="gt_row gt_right gt_summary_row">436</td>
</tr>
</tbody>
</table>


Summary rows can be placed at the top of each group using `side="top"`:


``` python
import polars as pl
from great_tables import GT, vals
from great_tables.data import gtcars

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "hp", "trq"])
    .head(12)
)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .summary_rows(
        fns={"Mean": pl.col("hp", "trq").mean()},
        side="top",
        fmt=vals.fmt_number,
    )
)
```


<style>
#zesgjxmfum table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zesgjxmfum thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zesgjxmfum p { margin: 0; padding: 0; }
 #zesgjxmfum .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zesgjxmfum .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zesgjxmfum .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zesgjxmfum .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zesgjxmfum .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zesgjxmfum .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zesgjxmfum .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zesgjxmfum .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zesgjxmfum .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zesgjxmfum .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zesgjxmfum .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zesgjxmfum .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zesgjxmfum .gt_spanner_row { border-bottom-style: hidden; }
 #zesgjxmfum .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zesgjxmfum .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zesgjxmfum .gt_from_md> :first-child { margin-top: 0; }
 #zesgjxmfum .gt_from_md> :last-child { margin-bottom: 0; }
 #zesgjxmfum .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zesgjxmfum .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zesgjxmfum .gt_indent_1 { text-indent: 5px; }
 #zesgjxmfum .gt_indent_2 { text-indent: calc(5px * 2); }
 #zesgjxmfum .gt_indent_3 { text-indent: calc(5px * 3); }
 #zesgjxmfum .gt_indent_4 { text-indent: calc(5px * 4); }
 #zesgjxmfum .gt_indent_5 { text-indent: calc(5px * 5); }
 #zesgjxmfum .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zesgjxmfum .gt_row_group_first td { border-top-width: 2px; }
 #zesgjxmfum .gt_row_group_first th { border-top-width: 2px; }
 #zesgjxmfum .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zesgjxmfum .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zesgjxmfum .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zesgjxmfum .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zesgjxmfum .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zesgjxmfum .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zesgjxmfum .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zesgjxmfum .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zesgjxmfum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zesgjxmfum .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zesgjxmfum .gt_left { text-align: left; }
 #zesgjxmfum .gt_center { text-align: center; }
 #zesgjxmfum .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zesgjxmfum .gt_font_normal { font-weight: normal; }
 #zesgjxmfum .gt_font_bold { font-weight: bold; }
 #zesgjxmfum .gt_font_italic { font-style: italic; }
 #zesgjxmfum .gt_super { font-size: 65%; }
 #zesgjxmfum .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zesgjxmfum .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zesgjxmfum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zesgjxmfum .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zesgjxmfum .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zesgjxmfum .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Ford</th>
</tr>

<tr>
<td class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row">Mean</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">647.00</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">550.00</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">550.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Ferrari</td>
</tr>
<tr>
<td class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row">Mean</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">660.78</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">500.33</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">California</td>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">557.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GTC4Lusso</td>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">514.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">FF</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">504.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">F12Berlinetta</td>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">509.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">LaFerrari</td>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">664.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Acura</td>
</tr>
<tr>
<td class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row">Mean</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">573.00</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">476.00</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">NSX</td>
<td class="gt_row gt_right">573.0</td>
<td class="gt_row gt_right">476.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Nissan</td>
</tr>
<tr>
<td class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row">Mean</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">545.00</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row">436.00</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GT-R</td>
<td class="gt_row gt_right">545.0</td>
<td class="gt_row gt_right">436.0</td>
</tr>
</tbody>
</table>


Combining group summaries with grand summary rows and styling provides a comprehensive summary view of the data. Use `loc.summary()` to style all group summary cells:


``` python
import polars as pl
from great_tables import GT, vals, style, loc
from great_tables.data import gtcars

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "hp", "trq"])
    .head(12)
)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .summary_rows(
        fns={
            "Min": pl.col("hp", "trq").min(),
            "Max": pl.col("hp", "trq").max(),
        },
        fmt=vals.fmt_integer,
    )
    .grand_summary_rows(
        fns={"Overall Mean": pl.col("hp", "trq").mean()},
        fmt=vals.fmt_number,
    )
    .tab_style(
        style=[style.fill(color="lightyellow")],
        locations=loc.summary(),
    )
    .tab_style(
        style=[style.fill(color="lightblue")],
        locations=loc.grand_summary(),
    )
)
```


<style>
#klhvwzlspq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#klhvwzlspq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#klhvwzlspq p { margin: 0; padding: 0; }
 #klhvwzlspq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #klhvwzlspq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #klhvwzlspq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #klhvwzlspq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #klhvwzlspq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #klhvwzlspq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #klhvwzlspq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #klhvwzlspq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #klhvwzlspq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #klhvwzlspq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #klhvwzlspq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #klhvwzlspq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #klhvwzlspq .gt_spanner_row { border-bottom-style: hidden; }
 #klhvwzlspq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #klhvwzlspq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #klhvwzlspq .gt_from_md> :first-child { margin-top: 0; }
 #klhvwzlspq .gt_from_md> :last-child { margin-bottom: 0; }
 #klhvwzlspq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #klhvwzlspq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #klhvwzlspq .gt_indent_1 { text-indent: 5px; }
 #klhvwzlspq .gt_indent_2 { text-indent: calc(5px * 2); }
 #klhvwzlspq .gt_indent_3 { text-indent: calc(5px * 3); }
 #klhvwzlspq .gt_indent_4 { text-indent: calc(5px * 4); }
 #klhvwzlspq .gt_indent_5 { text-indent: calc(5px * 5); }
 #klhvwzlspq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #klhvwzlspq .gt_row_group_first td { border-top-width: 2px; }
 #klhvwzlspq .gt_row_group_first th { border-top-width: 2px; }
 #klhvwzlspq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #klhvwzlspq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #klhvwzlspq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #klhvwzlspq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #klhvwzlspq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #klhvwzlspq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #klhvwzlspq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #klhvwzlspq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #klhvwzlspq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #klhvwzlspq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #klhvwzlspq .gt_left { text-align: left; }
 #klhvwzlspq .gt_center { text-align: center; }
 #klhvwzlspq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #klhvwzlspq .gt_font_normal { font-weight: normal; }
 #klhvwzlspq .gt_font_bold { font-weight: bold; }
 #klhvwzlspq .gt_font_italic { font-style: italic; }
 #klhvwzlspq .gt_super { font-size: 65%; }
 #klhvwzlspq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #klhvwzlspq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #klhvwzlspq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #klhvwzlspq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #klhvwzlspq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #klhvwzlspq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">Ford</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">550.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">647</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">550</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">647</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">550</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Ferrari</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">California</td>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">557.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GTC4Lusso</td>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">514.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">FF</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">504.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">F12Berlinetta</td>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">509.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">LaFerrari</td>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">664.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">553</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">398</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">949</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">664</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Acura</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">NSX</td>
<td class="gt_row gt_right">573.0</td>
<td class="gt_row gt_right">476.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">573</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">476</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">573</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">476</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">Nissan</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">GT-R</td>
<td class="gt_row gt_right">545.0</td>
<td class="gt_row gt_right">436.0</td>
</tr>
<tr>
<td class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">545</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">436</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_summary_row">Max</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">545</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow">436</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Overall Mean</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightblue">642.67</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightblue">497.08</td>
</tr>
</tbody>
</table>


When groups are displayed as a column in the stub (using `row_group_as_column=True`), the summary row labels span the stub columns:


``` python
import polars as pl
from great_tables import GT, vals
from great_tables.data import gtcars

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "hp", "trq"])
    .head(12)
)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .tab_options(row_group_as_column=True)
    .summary_rows(
        fns={
            "Min": pl.col("hp", "trq").min(),
            "Max": pl.col("hp", "trq").max(),
        },
        fmt=vals.fmt_integer,
    )
)
```


<style>
#rbazhwrqdw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rbazhwrqdw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rbazhwrqdw p { margin: 0; padding: 0; }
 #rbazhwrqdw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rbazhwrqdw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rbazhwrqdw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rbazhwrqdw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rbazhwrqdw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rbazhwrqdw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rbazhwrqdw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rbazhwrqdw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rbazhwrqdw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rbazhwrqdw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rbazhwrqdw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rbazhwrqdw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rbazhwrqdw .gt_spanner_row { border-bottom-style: hidden; }
 #rbazhwrqdw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rbazhwrqdw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rbazhwrqdw .gt_from_md> :first-child { margin-top: 0; }
 #rbazhwrqdw .gt_from_md> :last-child { margin-bottom: 0; }
 #rbazhwrqdw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rbazhwrqdw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rbazhwrqdw .gt_indent_1 { text-indent: 5px; }
 #rbazhwrqdw .gt_indent_2 { text-indent: calc(5px * 2); }
 #rbazhwrqdw .gt_indent_3 { text-indent: calc(5px * 3); }
 #rbazhwrqdw .gt_indent_4 { text-indent: calc(5px * 4); }
 #rbazhwrqdw .gt_indent_5 { text-indent: calc(5px * 5); }
 #rbazhwrqdw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rbazhwrqdw .gt_row_group_first td { border-top-width: 2px; }
 #rbazhwrqdw .gt_row_group_first th { border-top-width: 2px; }
 #rbazhwrqdw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rbazhwrqdw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rbazhwrqdw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rbazhwrqdw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rbazhwrqdw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rbazhwrqdw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rbazhwrqdw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rbazhwrqdw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rbazhwrqdw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rbazhwrqdw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rbazhwrqdw .gt_left { text-align: left; }
 #rbazhwrqdw .gt_center { text-align: center; }
 #rbazhwrqdw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rbazhwrqdw .gt_font_normal { font-weight: normal; }
 #rbazhwrqdw .gt_font_bold { font-weight: bold; }
 #rbazhwrqdw .gt_font_italic { font-style: italic; }
 #rbazhwrqdw .gt_super { font-size: 65%; }
 #rbazhwrqdw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rbazhwrqdw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rbazhwrqdw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rbazhwrqdw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rbazhwrqdw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rbazhwrqdw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th colspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="colgroup"></th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_row_group_first">
<th rowspan="3" class="gt_row gt_left gt_stub_row_group">Ford</th>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">550.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub gt_summary_row gt_first_summary_row">Min</th>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">647</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">550</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub gt_summary_row">Max</th>
<td class="gt_row gt_right gt_summary_row">647</td>
<td class="gt_row gt_right gt_summary_row">550</td>
</tr>
<tr class="gt_row_group_first">
<th rowspan="11" class="gt_row gt_left gt_stub_row_group">Ferrari</th>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">California</th>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">557.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">GTC4Lusso</th>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">514.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">FF</th>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">504.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">F12Berlinetta</th>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">LaFerrari</th>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">664.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub gt_summary_row gt_first_summary_row">Min</th>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">553</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">398</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub gt_summary_row">Max</th>
<td class="gt_row gt_right gt_summary_row">949</td>
<td class="gt_row gt_right gt_summary_row">664</td>
</tr>
<tr class="gt_row_group_first">
<th rowspan="3" class="gt_row gt_left gt_stub_row_group">Acura</th>
<th class="gt_row gt_left gt_stub">NSX</th>
<td class="gt_row gt_right">573.0</td>
<td class="gt_row gt_right">476.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub gt_summary_row gt_first_summary_row">Min</th>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">573</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">476</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub gt_summary_row">Max</th>
<td class="gt_row gt_right gt_summary_row">573</td>
<td class="gt_row gt_right gt_summary_row">476</td>
</tr>
<tr class="gt_row_group_first">
<th rowspan="3" class="gt_row gt_left gt_stub_row_group">Nissan</th>
<th class="gt_row gt_left gt_stub">GT-R</th>
<td class="gt_row gt_right">545.0</td>
<td class="gt_row gt_right">436.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub gt_summary_row gt_first_summary_row">Min</th>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">545</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row">436</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub gt_summary_row">Max</th>
<td class="gt_row gt_right gt_summary_row">545</td>
<td class="gt_row gt_right gt_summary_row">436</td>
</tr>
</tbody>
</table>
