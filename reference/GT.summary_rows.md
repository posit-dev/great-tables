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
#rklvzyipnx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rklvzyipnx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rklvzyipnx p { margin: 0; padding: 0; }
 #rklvzyipnx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rklvzyipnx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rklvzyipnx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rklvzyipnx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rklvzyipnx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rklvzyipnx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rklvzyipnx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rklvzyipnx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rklvzyipnx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rklvzyipnx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rklvzyipnx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rklvzyipnx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rklvzyipnx .gt_spanner_row { border-bottom-style: hidden; }
 #rklvzyipnx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rklvzyipnx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rklvzyipnx .gt_from_md> :first-child { margin-top: 0; }
 #rklvzyipnx .gt_from_md> :last-child { margin-bottom: 0; }
 #rklvzyipnx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rklvzyipnx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rklvzyipnx .gt_indent_1 { text-indent: 5px; }
 #rklvzyipnx .gt_indent_2 { text-indent: calc(5px * 2); }
 #rklvzyipnx .gt_indent_3 { text-indent: calc(5px * 3); }
 #rklvzyipnx .gt_indent_4 { text-indent: calc(5px * 4); }
 #rklvzyipnx .gt_indent_5 { text-indent: calc(5px * 5); }
 #rklvzyipnx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rklvzyipnx .gt_row_group_first td { border-top-width: 2px; }
 #rklvzyipnx .gt_row_group_first th { border-top-width: 2px; }
 #rklvzyipnx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rklvzyipnx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rklvzyipnx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rklvzyipnx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rklvzyipnx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rklvzyipnx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rklvzyipnx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rklvzyipnx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rklvzyipnx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rklvzyipnx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rklvzyipnx .gt_left { text-align: left; }
 #rklvzyipnx .gt_center { text-align: center; }
 #rklvzyipnx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rklvzyipnx .gt_font_normal { font-weight: normal; }
 #rklvzyipnx .gt_font_bold { font-weight: bold; }
 #rklvzyipnx .gt_font_italic { font-style: italic; }
 #rklvzyipnx .gt_super { font-size: 65%; }
 #rklvzyipnx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rklvzyipnx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rklvzyipnx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rklvzyipnx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rklvzyipnx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rklvzyipnx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#itqarjoecf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#itqarjoecf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#itqarjoecf p { margin: 0; padding: 0; }
 #itqarjoecf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #itqarjoecf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #itqarjoecf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #itqarjoecf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #itqarjoecf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #itqarjoecf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #itqarjoecf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #itqarjoecf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #itqarjoecf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #itqarjoecf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #itqarjoecf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #itqarjoecf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #itqarjoecf .gt_spanner_row { border-bottom-style: hidden; }
 #itqarjoecf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #itqarjoecf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #itqarjoecf .gt_from_md> :first-child { margin-top: 0; }
 #itqarjoecf .gt_from_md> :last-child { margin-bottom: 0; }
 #itqarjoecf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #itqarjoecf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #itqarjoecf .gt_indent_1 { text-indent: 5px; }
 #itqarjoecf .gt_indent_2 { text-indent: calc(5px * 2); }
 #itqarjoecf .gt_indent_3 { text-indent: calc(5px * 3); }
 #itqarjoecf .gt_indent_4 { text-indent: calc(5px * 4); }
 #itqarjoecf .gt_indent_5 { text-indent: calc(5px * 5); }
 #itqarjoecf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #itqarjoecf .gt_row_group_first td { border-top-width: 2px; }
 #itqarjoecf .gt_row_group_first th { border-top-width: 2px; }
 #itqarjoecf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #itqarjoecf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #itqarjoecf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #itqarjoecf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #itqarjoecf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #itqarjoecf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #itqarjoecf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #itqarjoecf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #itqarjoecf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #itqarjoecf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #itqarjoecf .gt_left { text-align: left; }
 #itqarjoecf .gt_center { text-align: center; }
 #itqarjoecf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #itqarjoecf .gt_font_normal { font-weight: normal; }
 #itqarjoecf .gt_font_bold { font-weight: bold; }
 #itqarjoecf .gt_font_italic { font-style: italic; }
 #itqarjoecf .gt_super { font-size: 65%; }
 #itqarjoecf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #itqarjoecf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #itqarjoecf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #itqarjoecf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #itqarjoecf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #itqarjoecf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#utbmlfelte table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#utbmlfelte thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#utbmlfelte p { margin: 0; padding: 0; }
 #utbmlfelte .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #utbmlfelte .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #utbmlfelte .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #utbmlfelte .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #utbmlfelte .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #utbmlfelte .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #utbmlfelte .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #utbmlfelte .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #utbmlfelte .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #utbmlfelte .gt_column_spanner_outer:first-child { padding-left: 0; }
 #utbmlfelte .gt_column_spanner_outer:last-child { padding-right: 0; }
 #utbmlfelte .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #utbmlfelte .gt_spanner_row { border-bottom-style: hidden; }
 #utbmlfelte .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #utbmlfelte .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #utbmlfelte .gt_from_md> :first-child { margin-top: 0; }
 #utbmlfelte .gt_from_md> :last-child { margin-bottom: 0; }
 #utbmlfelte .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #utbmlfelte .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #utbmlfelte .gt_indent_1 { text-indent: 5px; }
 #utbmlfelte .gt_indent_2 { text-indent: calc(5px * 2); }
 #utbmlfelte .gt_indent_3 { text-indent: calc(5px * 3); }
 #utbmlfelte .gt_indent_4 { text-indent: calc(5px * 4); }
 #utbmlfelte .gt_indent_5 { text-indent: calc(5px * 5); }
 #utbmlfelte .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #utbmlfelte .gt_row_group_first td { border-top-width: 2px; }
 #utbmlfelte .gt_row_group_first th { border-top-width: 2px; }
 #utbmlfelte .gt_striped { color: #333333; background-color: #F4F4F4; }
 #utbmlfelte .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #utbmlfelte .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #utbmlfelte .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #utbmlfelte .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #utbmlfelte .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #utbmlfelte .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #utbmlfelte .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #utbmlfelte .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #utbmlfelte .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #utbmlfelte .gt_left { text-align: left; }
 #utbmlfelte .gt_center { text-align: center; }
 #utbmlfelte .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #utbmlfelte .gt_font_normal { font-weight: normal; }
 #utbmlfelte .gt_font_bold { font-weight: bold; }
 #utbmlfelte .gt_font_italic { font-style: italic; }
 #utbmlfelte .gt_super { font-size: 65%; }
 #utbmlfelte .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #utbmlfelte .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #utbmlfelte .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #utbmlfelte .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #utbmlfelte .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #utbmlfelte .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tztklecorg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tztklecorg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tztklecorg p { margin: 0; padding: 0; }
 #tztklecorg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tztklecorg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tztklecorg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tztklecorg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tztklecorg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tztklecorg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tztklecorg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tztklecorg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tztklecorg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tztklecorg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tztklecorg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tztklecorg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tztklecorg .gt_spanner_row { border-bottom-style: hidden; }
 #tztklecorg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tztklecorg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tztklecorg .gt_from_md> :first-child { margin-top: 0; }
 #tztklecorg .gt_from_md> :last-child { margin-bottom: 0; }
 #tztklecorg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tztklecorg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tztklecorg .gt_indent_1 { text-indent: 5px; }
 #tztklecorg .gt_indent_2 { text-indent: calc(5px * 2); }
 #tztklecorg .gt_indent_3 { text-indent: calc(5px * 3); }
 #tztklecorg .gt_indent_4 { text-indent: calc(5px * 4); }
 #tztklecorg .gt_indent_5 { text-indent: calc(5px * 5); }
 #tztklecorg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tztklecorg .gt_row_group_first td { border-top-width: 2px; }
 #tztklecorg .gt_row_group_first th { border-top-width: 2px; }
 #tztklecorg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tztklecorg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tztklecorg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tztklecorg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tztklecorg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tztklecorg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tztklecorg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tztklecorg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tztklecorg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tztklecorg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tztklecorg .gt_left { text-align: left; }
 #tztklecorg .gt_center { text-align: center; }
 #tztklecorg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tztklecorg .gt_font_normal { font-weight: normal; }
 #tztklecorg .gt_font_bold { font-weight: bold; }
 #tztklecorg .gt_font_italic { font-style: italic; }
 #tztklecorg .gt_super { font-size: 65%; }
 #tztklecorg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tztklecorg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tztklecorg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tztklecorg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tztklecorg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tztklecorg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wnqmfxhtcx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wnqmfxhtcx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wnqmfxhtcx p { margin: 0; padding: 0; }
 #wnqmfxhtcx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wnqmfxhtcx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wnqmfxhtcx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wnqmfxhtcx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wnqmfxhtcx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnqmfxhtcx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnqmfxhtcx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnqmfxhtcx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wnqmfxhtcx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wnqmfxhtcx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wnqmfxhtcx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wnqmfxhtcx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wnqmfxhtcx .gt_spanner_row { border-bottom-style: hidden; }
 #wnqmfxhtcx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wnqmfxhtcx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wnqmfxhtcx .gt_from_md> :first-child { margin-top: 0; }
 #wnqmfxhtcx .gt_from_md> :last-child { margin-bottom: 0; }
 #wnqmfxhtcx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wnqmfxhtcx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wnqmfxhtcx .gt_indent_1 { text-indent: 5px; }
 #wnqmfxhtcx .gt_indent_2 { text-indent: calc(5px * 2); }
 #wnqmfxhtcx .gt_indent_3 { text-indent: calc(5px * 3); }
 #wnqmfxhtcx .gt_indent_4 { text-indent: calc(5px * 4); }
 #wnqmfxhtcx .gt_indent_5 { text-indent: calc(5px * 5); }
 #wnqmfxhtcx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wnqmfxhtcx .gt_row_group_first td { border-top-width: 2px; }
 #wnqmfxhtcx .gt_row_group_first th { border-top-width: 2px; }
 #wnqmfxhtcx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wnqmfxhtcx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnqmfxhtcx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnqmfxhtcx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wnqmfxhtcx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnqmfxhtcx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnqmfxhtcx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wnqmfxhtcx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wnqmfxhtcx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnqmfxhtcx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnqmfxhtcx .gt_left { text-align: left; }
 #wnqmfxhtcx .gt_center { text-align: center; }
 #wnqmfxhtcx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wnqmfxhtcx .gt_font_normal { font-weight: normal; }
 #wnqmfxhtcx .gt_font_bold { font-weight: bold; }
 #wnqmfxhtcx .gt_font_italic { font-style: italic; }
 #wnqmfxhtcx .gt_super { font-size: 65%; }
 #wnqmfxhtcx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnqmfxhtcx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wnqmfxhtcx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnqmfxhtcx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnqmfxhtcx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wnqmfxhtcx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pecsaovwph table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pecsaovwph thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pecsaovwph p { margin: 0; padding: 0; }
 #pecsaovwph .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pecsaovwph .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pecsaovwph .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pecsaovwph .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pecsaovwph .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pecsaovwph .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pecsaovwph .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pecsaovwph .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pecsaovwph .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pecsaovwph .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pecsaovwph .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pecsaovwph .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pecsaovwph .gt_spanner_row { border-bottom-style: hidden; }
 #pecsaovwph .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pecsaovwph .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pecsaovwph .gt_from_md> :first-child { margin-top: 0; }
 #pecsaovwph .gt_from_md> :last-child { margin-bottom: 0; }
 #pecsaovwph .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pecsaovwph .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pecsaovwph .gt_indent_1 { text-indent: 5px; }
 #pecsaovwph .gt_indent_2 { text-indent: calc(5px * 2); }
 #pecsaovwph .gt_indent_3 { text-indent: calc(5px * 3); }
 #pecsaovwph .gt_indent_4 { text-indent: calc(5px * 4); }
 #pecsaovwph .gt_indent_5 { text-indent: calc(5px * 5); }
 #pecsaovwph .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pecsaovwph .gt_row_group_first td { border-top-width: 2px; }
 #pecsaovwph .gt_row_group_first th { border-top-width: 2px; }
 #pecsaovwph .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pecsaovwph .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pecsaovwph .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pecsaovwph .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pecsaovwph .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pecsaovwph .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pecsaovwph .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pecsaovwph .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pecsaovwph .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pecsaovwph .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pecsaovwph .gt_left { text-align: left; }
 #pecsaovwph .gt_center { text-align: center; }
 #pecsaovwph .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pecsaovwph .gt_font_normal { font-weight: normal; }
 #pecsaovwph .gt_font_bold { font-weight: bold; }
 #pecsaovwph .gt_font_italic { font-style: italic; }
 #pecsaovwph .gt_super { font-size: 65%; }
 #pecsaovwph .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pecsaovwph .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pecsaovwph .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pecsaovwph .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pecsaovwph .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pecsaovwph .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
