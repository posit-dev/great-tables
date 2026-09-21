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
#cnbtisfteg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cnbtisfteg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cnbtisfteg p { margin: 0; padding: 0; }
 #cnbtisfteg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cnbtisfteg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cnbtisfteg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cnbtisfteg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cnbtisfteg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cnbtisfteg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cnbtisfteg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cnbtisfteg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cnbtisfteg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cnbtisfteg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cnbtisfteg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cnbtisfteg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cnbtisfteg .gt_spanner_row { border-bottom-style: hidden; }
 #cnbtisfteg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cnbtisfteg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cnbtisfteg .gt_from_md> :first-child { margin-top: 0; }
 #cnbtisfteg .gt_from_md> :last-child { margin-bottom: 0; }
 #cnbtisfteg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cnbtisfteg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cnbtisfteg .gt_indent_1 { text-indent: 5px; }
 #cnbtisfteg .gt_indent_2 { text-indent: calc(5px * 2); }
 #cnbtisfteg .gt_indent_3 { text-indent: calc(5px * 3); }
 #cnbtisfteg .gt_indent_4 { text-indent: calc(5px * 4); }
 #cnbtisfteg .gt_indent_5 { text-indent: calc(5px * 5); }
 #cnbtisfteg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cnbtisfteg .gt_row_group_first td { border-top-width: 2px; }
 #cnbtisfteg .gt_row_group_first th { border-top-width: 2px; }
 #cnbtisfteg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cnbtisfteg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cnbtisfteg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cnbtisfteg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cnbtisfteg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cnbtisfteg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cnbtisfteg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cnbtisfteg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cnbtisfteg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cnbtisfteg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cnbtisfteg .gt_left { text-align: left; }
 #cnbtisfteg .gt_center { text-align: center; }
 #cnbtisfteg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cnbtisfteg .gt_font_normal { font-weight: normal; }
 #cnbtisfteg .gt_font_bold { font-weight: bold; }
 #cnbtisfteg .gt_font_italic { font-style: italic; }
 #cnbtisfteg .gt_super { font-size: 65%; }
 #cnbtisfteg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cnbtisfteg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cnbtisfteg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cnbtisfteg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cnbtisfteg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cnbtisfteg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#oxhcghkaxh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oxhcghkaxh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oxhcghkaxh p { margin: 0; padding: 0; }
 #oxhcghkaxh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oxhcghkaxh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oxhcghkaxh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oxhcghkaxh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oxhcghkaxh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oxhcghkaxh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxhcghkaxh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oxhcghkaxh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oxhcghkaxh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oxhcghkaxh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oxhcghkaxh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oxhcghkaxh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oxhcghkaxh .gt_spanner_row { border-bottom-style: hidden; }
 #oxhcghkaxh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oxhcghkaxh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oxhcghkaxh .gt_from_md> :first-child { margin-top: 0; }
 #oxhcghkaxh .gt_from_md> :last-child { margin-bottom: 0; }
 #oxhcghkaxh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oxhcghkaxh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oxhcghkaxh .gt_indent_1 { text-indent: 5px; }
 #oxhcghkaxh .gt_indent_2 { text-indent: calc(5px * 2); }
 #oxhcghkaxh .gt_indent_3 { text-indent: calc(5px * 3); }
 #oxhcghkaxh .gt_indent_4 { text-indent: calc(5px * 4); }
 #oxhcghkaxh .gt_indent_5 { text-indent: calc(5px * 5); }
 #oxhcghkaxh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oxhcghkaxh .gt_row_group_first td { border-top-width: 2px; }
 #oxhcghkaxh .gt_row_group_first th { border-top-width: 2px; }
 #oxhcghkaxh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oxhcghkaxh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxhcghkaxh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oxhcghkaxh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oxhcghkaxh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxhcghkaxh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oxhcghkaxh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oxhcghkaxh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oxhcghkaxh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxhcghkaxh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oxhcghkaxh .gt_left { text-align: left; }
 #oxhcghkaxh .gt_center { text-align: center; }
 #oxhcghkaxh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oxhcghkaxh .gt_font_normal { font-weight: normal; }
 #oxhcghkaxh .gt_font_bold { font-weight: bold; }
 #oxhcghkaxh .gt_font_italic { font-style: italic; }
 #oxhcghkaxh .gt_super { font-size: 65%; }
 #oxhcghkaxh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxhcghkaxh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oxhcghkaxh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxhcghkaxh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oxhcghkaxh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oxhcghkaxh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pwbzpbnozz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pwbzpbnozz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pwbzpbnozz p { margin: 0; padding: 0; }
 #pwbzpbnozz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pwbzpbnozz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pwbzpbnozz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pwbzpbnozz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pwbzpbnozz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pwbzpbnozz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pwbzpbnozz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pwbzpbnozz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pwbzpbnozz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pwbzpbnozz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pwbzpbnozz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pwbzpbnozz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pwbzpbnozz .gt_spanner_row { border-bottom-style: hidden; }
 #pwbzpbnozz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pwbzpbnozz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pwbzpbnozz .gt_from_md> :first-child { margin-top: 0; }
 #pwbzpbnozz .gt_from_md> :last-child { margin-bottom: 0; }
 #pwbzpbnozz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pwbzpbnozz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pwbzpbnozz .gt_indent_1 { text-indent: 5px; }
 #pwbzpbnozz .gt_indent_2 { text-indent: calc(5px * 2); }
 #pwbzpbnozz .gt_indent_3 { text-indent: calc(5px * 3); }
 #pwbzpbnozz .gt_indent_4 { text-indent: calc(5px * 4); }
 #pwbzpbnozz .gt_indent_5 { text-indent: calc(5px * 5); }
 #pwbzpbnozz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pwbzpbnozz .gt_row_group_first td { border-top-width: 2px; }
 #pwbzpbnozz .gt_row_group_first th { border-top-width: 2px; }
 #pwbzpbnozz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pwbzpbnozz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pwbzpbnozz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pwbzpbnozz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pwbzpbnozz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pwbzpbnozz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pwbzpbnozz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pwbzpbnozz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pwbzpbnozz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pwbzpbnozz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pwbzpbnozz .gt_left { text-align: left; }
 #pwbzpbnozz .gt_center { text-align: center; }
 #pwbzpbnozz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pwbzpbnozz .gt_font_normal { font-weight: normal; }
 #pwbzpbnozz .gt_font_bold { font-weight: bold; }
 #pwbzpbnozz .gt_font_italic { font-style: italic; }
 #pwbzpbnozz .gt_super { font-size: 65%; }
 #pwbzpbnozz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pwbzpbnozz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pwbzpbnozz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pwbzpbnozz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pwbzpbnozz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pwbzpbnozz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#iadweespoq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iadweespoq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iadweespoq p { margin: 0; padding: 0; }
 #iadweespoq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iadweespoq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iadweespoq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iadweespoq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iadweespoq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iadweespoq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iadweespoq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iadweespoq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iadweespoq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iadweespoq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iadweespoq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iadweespoq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iadweespoq .gt_spanner_row { border-bottom-style: hidden; }
 #iadweespoq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iadweespoq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iadweespoq .gt_from_md> :first-child { margin-top: 0; }
 #iadweespoq .gt_from_md> :last-child { margin-bottom: 0; }
 #iadweespoq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iadweespoq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iadweespoq .gt_indent_1 { text-indent: 5px; }
 #iadweespoq .gt_indent_2 { text-indent: calc(5px * 2); }
 #iadweespoq .gt_indent_3 { text-indent: calc(5px * 3); }
 #iadweespoq .gt_indent_4 { text-indent: calc(5px * 4); }
 #iadweespoq .gt_indent_5 { text-indent: calc(5px * 5); }
 #iadweespoq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iadweespoq .gt_row_group_first td { border-top-width: 2px; }
 #iadweespoq .gt_row_group_first th { border-top-width: 2px; }
 #iadweespoq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iadweespoq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iadweespoq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iadweespoq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iadweespoq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iadweespoq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iadweespoq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iadweespoq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iadweespoq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iadweespoq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iadweespoq .gt_left { text-align: left; }
 #iadweespoq .gt_center { text-align: center; }
 #iadweespoq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iadweespoq .gt_font_normal { font-weight: normal; }
 #iadweespoq .gt_font_bold { font-weight: bold; }
 #iadweespoq .gt_font_italic { font-style: italic; }
 #iadweespoq .gt_super { font-size: 65%; }
 #iadweespoq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iadweespoq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iadweespoq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iadweespoq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iadweespoq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iadweespoq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jvuvdqbigj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jvuvdqbigj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jvuvdqbigj p { margin: 0; padding: 0; }
 #jvuvdqbigj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jvuvdqbigj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jvuvdqbigj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jvuvdqbigj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jvuvdqbigj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jvuvdqbigj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jvuvdqbigj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jvuvdqbigj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jvuvdqbigj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jvuvdqbigj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jvuvdqbigj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jvuvdqbigj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jvuvdqbigj .gt_spanner_row { border-bottom-style: hidden; }
 #jvuvdqbigj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jvuvdqbigj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jvuvdqbigj .gt_from_md> :first-child { margin-top: 0; }
 #jvuvdqbigj .gt_from_md> :last-child { margin-bottom: 0; }
 #jvuvdqbigj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jvuvdqbigj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jvuvdqbigj .gt_indent_1 { text-indent: 5px; }
 #jvuvdqbigj .gt_indent_2 { text-indent: calc(5px * 2); }
 #jvuvdqbigj .gt_indent_3 { text-indent: calc(5px * 3); }
 #jvuvdqbigj .gt_indent_4 { text-indent: calc(5px * 4); }
 #jvuvdqbigj .gt_indent_5 { text-indent: calc(5px * 5); }
 #jvuvdqbigj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jvuvdqbigj .gt_row_group_first td { border-top-width: 2px; }
 #jvuvdqbigj .gt_row_group_first th { border-top-width: 2px; }
 #jvuvdqbigj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jvuvdqbigj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jvuvdqbigj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jvuvdqbigj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jvuvdqbigj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jvuvdqbigj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jvuvdqbigj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jvuvdqbigj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jvuvdqbigj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jvuvdqbigj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jvuvdqbigj .gt_left { text-align: left; }
 #jvuvdqbigj .gt_center { text-align: center; }
 #jvuvdqbigj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jvuvdqbigj .gt_font_normal { font-weight: normal; }
 #jvuvdqbigj .gt_font_bold { font-weight: bold; }
 #jvuvdqbigj .gt_font_italic { font-style: italic; }
 #jvuvdqbigj .gt_super { font-size: 65%; }
 #jvuvdqbigj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jvuvdqbigj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jvuvdqbigj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jvuvdqbigj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jvuvdqbigj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jvuvdqbigj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gbztorofrh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gbztorofrh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gbztorofrh p { margin: 0; padding: 0; }
 #gbztorofrh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gbztorofrh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gbztorofrh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gbztorofrh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gbztorofrh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gbztorofrh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gbztorofrh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gbztorofrh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gbztorofrh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gbztorofrh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gbztorofrh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gbztorofrh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gbztorofrh .gt_spanner_row { border-bottom-style: hidden; }
 #gbztorofrh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gbztorofrh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gbztorofrh .gt_from_md> :first-child { margin-top: 0; }
 #gbztorofrh .gt_from_md> :last-child { margin-bottom: 0; }
 #gbztorofrh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gbztorofrh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gbztorofrh .gt_indent_1 { text-indent: 5px; }
 #gbztorofrh .gt_indent_2 { text-indent: calc(5px * 2); }
 #gbztorofrh .gt_indent_3 { text-indent: calc(5px * 3); }
 #gbztorofrh .gt_indent_4 { text-indent: calc(5px * 4); }
 #gbztorofrh .gt_indent_5 { text-indent: calc(5px * 5); }
 #gbztorofrh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gbztorofrh .gt_row_group_first td { border-top-width: 2px; }
 #gbztorofrh .gt_row_group_first th { border-top-width: 2px; }
 #gbztorofrh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gbztorofrh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gbztorofrh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gbztorofrh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gbztorofrh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gbztorofrh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gbztorofrh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gbztorofrh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gbztorofrh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gbztorofrh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gbztorofrh .gt_left { text-align: left; }
 #gbztorofrh .gt_center { text-align: center; }
 #gbztorofrh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gbztorofrh .gt_font_normal { font-weight: normal; }
 #gbztorofrh .gt_font_bold { font-weight: bold; }
 #gbztorofrh .gt_font_italic { font-style: italic; }
 #gbztorofrh .gt_super { font-size: 65%; }
 #gbztorofrh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gbztorofrh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gbztorofrh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gbztorofrh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gbztorofrh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gbztorofrh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
