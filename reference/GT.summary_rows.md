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
#hvztqrokcd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hvztqrokcd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hvztqrokcd p { margin: 0; padding: 0; }
 #hvztqrokcd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hvztqrokcd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hvztqrokcd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hvztqrokcd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hvztqrokcd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hvztqrokcd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvztqrokcd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hvztqrokcd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hvztqrokcd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hvztqrokcd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hvztqrokcd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hvztqrokcd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hvztqrokcd .gt_spanner_row { border-bottom-style: hidden; }
 #hvztqrokcd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hvztqrokcd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hvztqrokcd .gt_from_md> :first-child { margin-top: 0; }
 #hvztqrokcd .gt_from_md> :last-child { margin-bottom: 0; }
 #hvztqrokcd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hvztqrokcd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hvztqrokcd .gt_indent_1 { text-indent: 5px; }
 #hvztqrokcd .gt_indent_2 { text-indent: calc(5px * 2); }
 #hvztqrokcd .gt_indent_3 { text-indent: calc(5px * 3); }
 #hvztqrokcd .gt_indent_4 { text-indent: calc(5px * 4); }
 #hvztqrokcd .gt_indent_5 { text-indent: calc(5px * 5); }
 #hvztqrokcd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hvztqrokcd .gt_row_group_first td { border-top-width: 2px; }
 #hvztqrokcd .gt_row_group_first th { border-top-width: 2px; }
 #hvztqrokcd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hvztqrokcd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvztqrokcd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hvztqrokcd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hvztqrokcd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvztqrokcd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hvztqrokcd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hvztqrokcd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hvztqrokcd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvztqrokcd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hvztqrokcd .gt_left { text-align: left; }
 #hvztqrokcd .gt_center { text-align: center; }
 #hvztqrokcd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hvztqrokcd .gt_font_normal { font-weight: normal; }
 #hvztqrokcd .gt_font_bold { font-weight: bold; }
 #hvztqrokcd .gt_font_italic { font-style: italic; }
 #hvztqrokcd .gt_super { font-size: 65%; }
 #hvztqrokcd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvztqrokcd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hvztqrokcd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvztqrokcd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hvztqrokcd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hvztqrokcd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sbtoudifap table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sbtoudifap thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sbtoudifap p { margin: 0; padding: 0; }
 #sbtoudifap .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sbtoudifap .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sbtoudifap .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sbtoudifap .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sbtoudifap .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sbtoudifap .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbtoudifap .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sbtoudifap .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sbtoudifap .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sbtoudifap .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sbtoudifap .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sbtoudifap .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sbtoudifap .gt_spanner_row { border-bottom-style: hidden; }
 #sbtoudifap .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sbtoudifap .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sbtoudifap .gt_from_md> :first-child { margin-top: 0; }
 #sbtoudifap .gt_from_md> :last-child { margin-bottom: 0; }
 #sbtoudifap .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sbtoudifap .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sbtoudifap .gt_indent_1 { text-indent: 5px; }
 #sbtoudifap .gt_indent_2 { text-indent: calc(5px * 2); }
 #sbtoudifap .gt_indent_3 { text-indent: calc(5px * 3); }
 #sbtoudifap .gt_indent_4 { text-indent: calc(5px * 4); }
 #sbtoudifap .gt_indent_5 { text-indent: calc(5px * 5); }
 #sbtoudifap .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sbtoudifap .gt_row_group_first td { border-top-width: 2px; }
 #sbtoudifap .gt_row_group_first th { border-top-width: 2px; }
 #sbtoudifap .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sbtoudifap .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbtoudifap .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sbtoudifap .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sbtoudifap .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbtoudifap .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sbtoudifap .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sbtoudifap .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sbtoudifap .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbtoudifap .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sbtoudifap .gt_left { text-align: left; }
 #sbtoudifap .gt_center { text-align: center; }
 #sbtoudifap .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sbtoudifap .gt_font_normal { font-weight: normal; }
 #sbtoudifap .gt_font_bold { font-weight: bold; }
 #sbtoudifap .gt_font_italic { font-style: italic; }
 #sbtoudifap .gt_super { font-size: 65%; }
 #sbtoudifap .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbtoudifap .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sbtoudifap .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbtoudifap .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sbtoudifap .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sbtoudifap .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zgduhpfsmg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zgduhpfsmg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zgduhpfsmg p { margin: 0; padding: 0; }
 #zgduhpfsmg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zgduhpfsmg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zgduhpfsmg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zgduhpfsmg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zgduhpfsmg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zgduhpfsmg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zgduhpfsmg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zgduhpfsmg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zgduhpfsmg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zgduhpfsmg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zgduhpfsmg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zgduhpfsmg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zgduhpfsmg .gt_spanner_row { border-bottom-style: hidden; }
 #zgduhpfsmg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zgduhpfsmg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zgduhpfsmg .gt_from_md> :first-child { margin-top: 0; }
 #zgduhpfsmg .gt_from_md> :last-child { margin-bottom: 0; }
 #zgduhpfsmg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zgduhpfsmg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zgduhpfsmg .gt_indent_1 { text-indent: 5px; }
 #zgduhpfsmg .gt_indent_2 { text-indent: calc(5px * 2); }
 #zgduhpfsmg .gt_indent_3 { text-indent: calc(5px * 3); }
 #zgduhpfsmg .gt_indent_4 { text-indent: calc(5px * 4); }
 #zgduhpfsmg .gt_indent_5 { text-indent: calc(5px * 5); }
 #zgduhpfsmg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zgduhpfsmg .gt_row_group_first td { border-top-width: 2px; }
 #zgduhpfsmg .gt_row_group_first th { border-top-width: 2px; }
 #zgduhpfsmg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zgduhpfsmg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zgduhpfsmg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zgduhpfsmg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zgduhpfsmg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zgduhpfsmg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zgduhpfsmg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zgduhpfsmg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zgduhpfsmg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zgduhpfsmg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zgduhpfsmg .gt_left { text-align: left; }
 #zgduhpfsmg .gt_center { text-align: center; }
 #zgduhpfsmg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zgduhpfsmg .gt_font_normal { font-weight: normal; }
 #zgduhpfsmg .gt_font_bold { font-weight: bold; }
 #zgduhpfsmg .gt_font_italic { font-style: italic; }
 #zgduhpfsmg .gt_super { font-size: 65%; }
 #zgduhpfsmg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zgduhpfsmg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zgduhpfsmg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zgduhpfsmg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zgduhpfsmg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zgduhpfsmg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ctygovaabn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ctygovaabn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ctygovaabn p { margin: 0; padding: 0; }
 #ctygovaabn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ctygovaabn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ctygovaabn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ctygovaabn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ctygovaabn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ctygovaabn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ctygovaabn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ctygovaabn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ctygovaabn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ctygovaabn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ctygovaabn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ctygovaabn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ctygovaabn .gt_spanner_row { border-bottom-style: hidden; }
 #ctygovaabn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ctygovaabn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ctygovaabn .gt_from_md> :first-child { margin-top: 0; }
 #ctygovaabn .gt_from_md> :last-child { margin-bottom: 0; }
 #ctygovaabn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ctygovaabn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ctygovaabn .gt_indent_1 { text-indent: 5px; }
 #ctygovaabn .gt_indent_2 { text-indent: calc(5px * 2); }
 #ctygovaabn .gt_indent_3 { text-indent: calc(5px * 3); }
 #ctygovaabn .gt_indent_4 { text-indent: calc(5px * 4); }
 #ctygovaabn .gt_indent_5 { text-indent: calc(5px * 5); }
 #ctygovaabn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ctygovaabn .gt_row_group_first td { border-top-width: 2px; }
 #ctygovaabn .gt_row_group_first th { border-top-width: 2px; }
 #ctygovaabn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ctygovaabn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ctygovaabn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ctygovaabn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ctygovaabn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ctygovaabn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ctygovaabn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ctygovaabn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ctygovaabn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ctygovaabn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ctygovaabn .gt_left { text-align: left; }
 #ctygovaabn .gt_center { text-align: center; }
 #ctygovaabn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ctygovaabn .gt_font_normal { font-weight: normal; }
 #ctygovaabn .gt_font_bold { font-weight: bold; }
 #ctygovaabn .gt_font_italic { font-style: italic; }
 #ctygovaabn .gt_super { font-size: 65%; }
 #ctygovaabn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ctygovaabn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ctygovaabn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ctygovaabn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ctygovaabn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ctygovaabn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kqesulpqnu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kqesulpqnu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kqesulpqnu p { margin: 0; padding: 0; }
 #kqesulpqnu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kqesulpqnu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kqesulpqnu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kqesulpqnu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kqesulpqnu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kqesulpqnu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqesulpqnu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kqesulpqnu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kqesulpqnu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kqesulpqnu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kqesulpqnu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kqesulpqnu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kqesulpqnu .gt_spanner_row { border-bottom-style: hidden; }
 #kqesulpqnu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kqesulpqnu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kqesulpqnu .gt_from_md> :first-child { margin-top: 0; }
 #kqesulpqnu .gt_from_md> :last-child { margin-bottom: 0; }
 #kqesulpqnu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kqesulpqnu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kqesulpqnu .gt_indent_1 { text-indent: 5px; }
 #kqesulpqnu .gt_indent_2 { text-indent: calc(5px * 2); }
 #kqesulpqnu .gt_indent_3 { text-indent: calc(5px * 3); }
 #kqesulpqnu .gt_indent_4 { text-indent: calc(5px * 4); }
 #kqesulpqnu .gt_indent_5 { text-indent: calc(5px * 5); }
 #kqesulpqnu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kqesulpqnu .gt_row_group_first td { border-top-width: 2px; }
 #kqesulpqnu .gt_row_group_first th { border-top-width: 2px; }
 #kqesulpqnu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kqesulpqnu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqesulpqnu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kqesulpqnu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kqesulpqnu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqesulpqnu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kqesulpqnu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kqesulpqnu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kqesulpqnu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqesulpqnu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kqesulpqnu .gt_left { text-align: left; }
 #kqesulpqnu .gt_center { text-align: center; }
 #kqesulpqnu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kqesulpqnu .gt_font_normal { font-weight: normal; }
 #kqesulpqnu .gt_font_bold { font-weight: bold; }
 #kqesulpqnu .gt_font_italic { font-style: italic; }
 #kqesulpqnu .gt_super { font-size: 65%; }
 #kqesulpqnu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqesulpqnu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kqesulpqnu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqesulpqnu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kqesulpqnu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kqesulpqnu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ysaeoitzht table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ysaeoitzht thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ysaeoitzht p { margin: 0; padding: 0; }
 #ysaeoitzht .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ysaeoitzht .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ysaeoitzht .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ysaeoitzht .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ysaeoitzht .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ysaeoitzht .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ysaeoitzht .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ysaeoitzht .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ysaeoitzht .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ysaeoitzht .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ysaeoitzht .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ysaeoitzht .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ysaeoitzht .gt_spanner_row { border-bottom-style: hidden; }
 #ysaeoitzht .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ysaeoitzht .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ysaeoitzht .gt_from_md> :first-child { margin-top: 0; }
 #ysaeoitzht .gt_from_md> :last-child { margin-bottom: 0; }
 #ysaeoitzht .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ysaeoitzht .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ysaeoitzht .gt_indent_1 { text-indent: 5px; }
 #ysaeoitzht .gt_indent_2 { text-indent: calc(5px * 2); }
 #ysaeoitzht .gt_indent_3 { text-indent: calc(5px * 3); }
 #ysaeoitzht .gt_indent_4 { text-indent: calc(5px * 4); }
 #ysaeoitzht .gt_indent_5 { text-indent: calc(5px * 5); }
 #ysaeoitzht .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ysaeoitzht .gt_row_group_first td { border-top-width: 2px; }
 #ysaeoitzht .gt_row_group_first th { border-top-width: 2px; }
 #ysaeoitzht .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ysaeoitzht .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ysaeoitzht .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ysaeoitzht .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ysaeoitzht .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ysaeoitzht .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ysaeoitzht .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ysaeoitzht .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ysaeoitzht .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ysaeoitzht .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ysaeoitzht .gt_left { text-align: left; }
 #ysaeoitzht .gt_center { text-align: center; }
 #ysaeoitzht .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ysaeoitzht .gt_font_normal { font-weight: normal; }
 #ysaeoitzht .gt_font_bold { font-weight: bold; }
 #ysaeoitzht .gt_font_italic { font-style: italic; }
 #ysaeoitzht .gt_super { font-size: 65%; }
 #ysaeoitzht .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ysaeoitzht .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ysaeoitzht .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ysaeoitzht .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ysaeoitzht .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ysaeoitzht .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
