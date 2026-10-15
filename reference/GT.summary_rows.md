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
#suyfvzwtzn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#suyfvzwtzn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#suyfvzwtzn p { margin: 0; padding: 0; }
 #suyfvzwtzn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #suyfvzwtzn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #suyfvzwtzn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #suyfvzwtzn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #suyfvzwtzn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #suyfvzwtzn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #suyfvzwtzn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #suyfvzwtzn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #suyfvzwtzn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #suyfvzwtzn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #suyfvzwtzn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #suyfvzwtzn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #suyfvzwtzn .gt_spanner_row { border-bottom-style: hidden; }
 #suyfvzwtzn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #suyfvzwtzn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #suyfvzwtzn .gt_from_md> :first-child { margin-top: 0; }
 #suyfvzwtzn .gt_from_md> :last-child { margin-bottom: 0; }
 #suyfvzwtzn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #suyfvzwtzn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #suyfvzwtzn .gt_indent_1 { text-indent: 5px; }
 #suyfvzwtzn .gt_indent_2 { text-indent: calc(5px * 2); }
 #suyfvzwtzn .gt_indent_3 { text-indent: calc(5px * 3); }
 #suyfvzwtzn .gt_indent_4 { text-indent: calc(5px * 4); }
 #suyfvzwtzn .gt_indent_5 { text-indent: calc(5px * 5); }
 #suyfvzwtzn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #suyfvzwtzn .gt_row_group_first td { border-top-width: 2px; }
 #suyfvzwtzn .gt_row_group_first th { border-top-width: 2px; }
 #suyfvzwtzn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #suyfvzwtzn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #suyfvzwtzn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #suyfvzwtzn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #suyfvzwtzn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #suyfvzwtzn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #suyfvzwtzn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #suyfvzwtzn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #suyfvzwtzn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #suyfvzwtzn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #suyfvzwtzn .gt_left { text-align: left; }
 #suyfvzwtzn .gt_center { text-align: center; }
 #suyfvzwtzn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #suyfvzwtzn .gt_font_normal { font-weight: normal; }
 #suyfvzwtzn .gt_font_bold { font-weight: bold; }
 #suyfvzwtzn .gt_font_italic { font-style: italic; }
 #suyfvzwtzn .gt_super { font-size: 65%; }
 #suyfvzwtzn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #suyfvzwtzn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #suyfvzwtzn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #suyfvzwtzn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #suyfvzwtzn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #suyfvzwtzn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" id="Ford" class="gt_group_heading" scope="colgroup">Ford</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</td>
<td class="gt_row gt_right" headers="Ford stub-1 hp">647.0</td>
<td class="gt_row gt_right" headers="Ford stub-1 trq">550.0</td>
</tr>
<tr>
<td id="summary-Ford-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Min hp">647</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Min trq">550</td>
</tr>
<tr>
<td id="summary-Ford-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Max hp">647</td>
<td class="gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Max trq">550</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Ferrari" class="gt_group_heading" scope="colgroup">Ferrari</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 hp">597.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 trq">398.0</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 trq">398.0</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 trq">398.0</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 hp">661.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 trq">561.0</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">California</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 hp">553.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 trq">557.0</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">GTC4Lusso</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 hp">680.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 trq">514.0</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">FF</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 hp">652.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 trq">504.0</td>
</tr>
<tr>
<td id="stub-9" class="gt_row gt_left gt_stub" scope="row">F12Berlinetta</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 hp">731.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 trq">509.0</td>
</tr>
<tr>
<td id="stub-10" class="gt_row gt_left gt_stub" scope="row">LaFerrari</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 hp">949.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 trq">664.0</td>
</tr>
<tr>
<td id="summary-Ferrari-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Min hp">553</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Min trq">398</td>
</tr>
<tr>
<td id="summary-Ferrari-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Max hp">949</td>
<td class="gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Max trq">664</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Acura" class="gt_group_heading" scope="colgroup">Acura</td>
</tr>
<tr>
<td id="stub-11" class="gt_row gt_left gt_stub" scope="row">NSX</td>
<td class="gt_row gt_right" headers="Acura stub-11 hp">573.0</td>
<td class="gt_row gt_right" headers="Acura stub-11 trq">476.0</td>
</tr>
<tr>
<td id="summary-Acura-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Min hp">573</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Min trq">476</td>
</tr>
<tr>
<td id="summary-Acura-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Max hp">573</td>
<td class="gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Max trq">476</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Nissan" class="gt_group_heading" scope="colgroup">Nissan</td>
</tr>
<tr>
<td id="stub-12" class="gt_row gt_left gt_stub" scope="row">GT-R</td>
<td class="gt_row gt_right" headers="Nissan stub-12 hp">545.0</td>
<td class="gt_row gt_right" headers="Nissan stub-12 trq">436.0</td>
</tr>
<tr>
<td id="summary-Nissan-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Min hp">545</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Min trq">436</td>
</tr>
<tr>
<td id="summary-Nissan-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Max hp">545</td>
<td class="gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Max trq">436</td>
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
#agkchilyqv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#agkchilyqv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#agkchilyqv p { margin: 0; padding: 0; }
 #agkchilyqv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #agkchilyqv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #agkchilyqv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #agkchilyqv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #agkchilyqv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #agkchilyqv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #agkchilyqv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #agkchilyqv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #agkchilyqv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #agkchilyqv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #agkchilyqv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #agkchilyqv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #agkchilyqv .gt_spanner_row { border-bottom-style: hidden; }
 #agkchilyqv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #agkchilyqv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #agkchilyqv .gt_from_md> :first-child { margin-top: 0; }
 #agkchilyqv .gt_from_md> :last-child { margin-bottom: 0; }
 #agkchilyqv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #agkchilyqv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #agkchilyqv .gt_indent_1 { text-indent: 5px; }
 #agkchilyqv .gt_indent_2 { text-indent: calc(5px * 2); }
 #agkchilyqv .gt_indent_3 { text-indent: calc(5px * 3); }
 #agkchilyqv .gt_indent_4 { text-indent: calc(5px * 4); }
 #agkchilyqv .gt_indent_5 { text-indent: calc(5px * 5); }
 #agkchilyqv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #agkchilyqv .gt_row_group_first td { border-top-width: 2px; }
 #agkchilyqv .gt_row_group_first th { border-top-width: 2px; }
 #agkchilyqv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #agkchilyqv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #agkchilyqv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #agkchilyqv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #agkchilyqv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #agkchilyqv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #agkchilyqv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #agkchilyqv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #agkchilyqv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #agkchilyqv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #agkchilyqv .gt_left { text-align: left; }
 #agkchilyqv .gt_center { text-align: center; }
 #agkchilyqv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #agkchilyqv .gt_font_normal { font-weight: normal; }
 #agkchilyqv .gt_font_bold { font-weight: bold; }
 #agkchilyqv .gt_font_italic { font-style: italic; }
 #agkchilyqv .gt_super { font-size: 65%; }
 #agkchilyqv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #agkchilyqv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #agkchilyqv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #agkchilyqv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #agkchilyqv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #agkchilyqv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" id="Ford" class="gt_group_heading" scope="colgroup">Ford</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</td>
<td class="gt_row gt_right" headers="Ford stub-1 hp">647.0</td>
<td class="gt_row gt_right" headers="Ford stub-1 trq">550.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Ferrari" class="gt_group_heading" scope="colgroup">Ferrari</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 hp">597.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 trq">398.0</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 trq">398.0</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 trq">398.0</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 hp">661.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 trq">561.0</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">California</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 hp">553.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 trq">557.0</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">GTC4Lusso</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 hp">680.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 trq">514.0</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">FF</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 hp">652.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 trq">504.0</td>
</tr>
<tr>
<td id="stub-9" class="gt_row gt_left gt_stub" scope="row">F12Berlinetta</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 hp">731.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 trq">509.0</td>
</tr>
<tr>
<td id="stub-10" class="gt_row gt_left gt_stub" scope="row">LaFerrari</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 hp">949.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 trq">664.0</td>
</tr>
<tr>
<td id="summary-Ferrari-Average" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Average</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Average hp">660.78</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Average trq">500.33</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Acura" class="gt_group_heading" scope="colgroup">Acura</td>
</tr>
<tr>
<td id="stub-11" class="gt_row gt_left gt_stub" scope="row">NSX</td>
<td class="gt_row gt_right" headers="Acura stub-11 hp">573.0</td>
<td class="gt_row gt_right" headers="Acura stub-11 trq">476.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Nissan" class="gt_group_heading" scope="colgroup">Nissan</td>
</tr>
<tr>
<td id="stub-12" class="gt_row gt_left gt_stub" scope="row">GT-R</td>
<td class="gt_row gt_right" headers="Nissan stub-12 hp">545.0</td>
<td class="gt_row gt_right" headers="Nissan stub-12 trq">436.0</td>
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
#aaijddstry table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aaijddstry thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aaijddstry p { margin: 0; padding: 0; }
 #aaijddstry .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aaijddstry .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aaijddstry .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aaijddstry .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aaijddstry .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aaijddstry .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aaijddstry .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aaijddstry .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #aaijddstry .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aaijddstry .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aaijddstry .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aaijddstry .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aaijddstry .gt_spanner_row { border-bottom-style: hidden; }
 #aaijddstry .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aaijddstry .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aaijddstry .gt_from_md> :first-child { margin-top: 0; }
 #aaijddstry .gt_from_md> :last-child { margin-bottom: 0; }
 #aaijddstry .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aaijddstry .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #aaijddstry .gt_indent_1 { text-indent: 5px; }
 #aaijddstry .gt_indent_2 { text-indent: calc(5px * 2); }
 #aaijddstry .gt_indent_3 { text-indent: calc(5px * 3); }
 #aaijddstry .gt_indent_4 { text-indent: calc(5px * 4); }
 #aaijddstry .gt_indent_5 { text-indent: calc(5px * 5); }
 #aaijddstry .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #aaijddstry .gt_row_group_first td { border-top-width: 2px; }
 #aaijddstry .gt_row_group_first th { border-top-width: 2px; }
 #aaijddstry .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aaijddstry .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aaijddstry .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aaijddstry .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aaijddstry .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aaijddstry .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aaijddstry .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aaijddstry .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aaijddstry .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aaijddstry .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aaijddstry .gt_left { text-align: left; }
 #aaijddstry .gt_center { text-align: center; }
 #aaijddstry .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aaijddstry .gt_font_normal { font-weight: normal; }
 #aaijddstry .gt_font_bold { font-weight: bold; }
 #aaijddstry .gt_font_italic { font-style: italic; }
 #aaijddstry .gt_super { font-size: 65%; }
 #aaijddstry .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aaijddstry .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aaijddstry .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aaijddstry .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aaijddstry .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aaijddstry .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" id="Ford" class="gt_group_heading" scope="colgroup">Ford</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</td>
<td class="gt_row gt_right" headers="Ford stub-1 hp">647.0</td>
<td class="gt_row gt_right" headers="Ford stub-1 trq">550.0</td>
</tr>
<tr>
<td id="summary-Ford-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Min hp">647</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Min trq">550</td>
</tr>
<tr>
<td id="summary-Ford-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Max hp">647</td>
<td class="gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Max trq">550</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Ferrari" class="gt_group_heading" scope="colgroup">Ferrari</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 hp">597.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 trq">398.0</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 trq">398.0</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 trq">398.0</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 hp">661.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 trq">561.0</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">California</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 hp">553.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 trq">557.0</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">GTC4Lusso</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 hp">680.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 trq">514.0</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">FF</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 hp">652.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 trq">504.0</td>
</tr>
<tr>
<td id="stub-9" class="gt_row gt_left gt_stub" scope="row">F12Berlinetta</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 hp">731.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 trq">509.0</td>
</tr>
<tr>
<td id="stub-10" class="gt_row gt_left gt_stub" scope="row">LaFerrari</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 hp">949.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 trq">664.0</td>
</tr>
<tr>
<td id="summary-Ferrari-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Min hp">553</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Min trq">398</td>
</tr>
<tr>
<td id="summary-Ferrari-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Max hp">949</td>
<td class="gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Max trq">664</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Acura" class="gt_group_heading" scope="colgroup">Acura</td>
</tr>
<tr>
<td id="stub-11" class="gt_row gt_left gt_stub" scope="row">NSX</td>
<td class="gt_row gt_right" headers="Acura stub-11 hp">573.0</td>
<td class="gt_row gt_right" headers="Acura stub-11 trq">476.0</td>
</tr>
<tr>
<td id="summary-Acura-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Min hp">573</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Min trq">476</td>
</tr>
<tr>
<td id="summary-Acura-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Max hp">573</td>
<td class="gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Max trq">476</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Nissan" class="gt_group_heading" scope="colgroup">Nissan</td>
</tr>
<tr>
<td id="stub-12" class="gt_row gt_left gt_stub" scope="row">GT-R</td>
<td class="gt_row gt_right" headers="Nissan stub-12 hp">545.0</td>
<td class="gt_row gt_right" headers="Nissan stub-12 trq">436.0</td>
</tr>
<tr>
<td id="summary-Nissan-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Min hp">545</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Min trq">436</td>
</tr>
<tr>
<td id="summary-Nissan-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Max hp">545</td>
<td class="gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Max trq">436</td>
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
#naemdoiuys table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#naemdoiuys thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#naemdoiuys p { margin: 0; padding: 0; }
 #naemdoiuys .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #naemdoiuys .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #naemdoiuys .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #naemdoiuys .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #naemdoiuys .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #naemdoiuys .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #naemdoiuys .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #naemdoiuys .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #naemdoiuys .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #naemdoiuys .gt_column_spanner_outer:first-child { padding-left: 0; }
 #naemdoiuys .gt_column_spanner_outer:last-child { padding-right: 0; }
 #naemdoiuys .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #naemdoiuys .gt_spanner_row { border-bottom-style: hidden; }
 #naemdoiuys .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #naemdoiuys .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #naemdoiuys .gt_from_md> :first-child { margin-top: 0; }
 #naemdoiuys .gt_from_md> :last-child { margin-bottom: 0; }
 #naemdoiuys .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #naemdoiuys .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #naemdoiuys .gt_indent_1 { text-indent: 5px; }
 #naemdoiuys .gt_indent_2 { text-indent: calc(5px * 2); }
 #naemdoiuys .gt_indent_3 { text-indent: calc(5px * 3); }
 #naemdoiuys .gt_indent_4 { text-indent: calc(5px * 4); }
 #naemdoiuys .gt_indent_5 { text-indent: calc(5px * 5); }
 #naemdoiuys .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #naemdoiuys .gt_row_group_first td { border-top-width: 2px; }
 #naemdoiuys .gt_row_group_first th { border-top-width: 2px; }
 #naemdoiuys .gt_striped { color: #333333; background-color: #F4F4F4; }
 #naemdoiuys .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #naemdoiuys .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #naemdoiuys .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #naemdoiuys .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #naemdoiuys .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #naemdoiuys .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #naemdoiuys .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #naemdoiuys .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #naemdoiuys .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #naemdoiuys .gt_left { text-align: left; }
 #naemdoiuys .gt_center { text-align: center; }
 #naemdoiuys .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #naemdoiuys .gt_font_normal { font-weight: normal; }
 #naemdoiuys .gt_font_bold { font-weight: bold; }
 #naemdoiuys .gt_font_italic { font-style: italic; }
 #naemdoiuys .gt_super { font-size: 65%; }
 #naemdoiuys .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #naemdoiuys .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #naemdoiuys .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #naemdoiuys .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #naemdoiuys .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #naemdoiuys .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" id="Ford" class="gt_group_heading" scope="colgroup">Ford</th>
</tr>

<tr>
<td id="summary-Ford-Mean" class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row" scope="row">Mean</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Mean hp">647.00</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Mean trq">550.00</td>
</tr>
<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</td>
<td class="gt_row gt_right" headers="Ford stub-1 hp">647.0</td>
<td class="gt_row gt_right" headers="Ford stub-1 trq">550.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Ferrari" class="gt_group_heading" scope="colgroup">Ferrari</td>
</tr>
<tr>
<td id="summary-Ferrari-Mean" class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row" scope="row">Mean</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Mean hp">660.78</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Mean trq">500.33</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 hp">597.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 trq">398.0</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 trq">398.0</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 trq">398.0</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 hp">661.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 trq">561.0</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">California</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 hp">553.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 trq">557.0</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">GTC4Lusso</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 hp">680.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 trq">514.0</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">FF</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 hp">652.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 trq">504.0</td>
</tr>
<tr>
<td id="stub-9" class="gt_row gt_left gt_stub" scope="row">F12Berlinetta</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 hp">731.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 trq">509.0</td>
</tr>
<tr>
<td id="stub-10" class="gt_row gt_left gt_stub" scope="row">LaFerrari</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 hp">949.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 trq">664.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Acura" class="gt_group_heading" scope="colgroup">Acura</td>
</tr>
<tr>
<td id="summary-Acura-Mean" class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row" scope="row">Mean</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Mean hp">573.00</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Mean trq">476.00</td>
</tr>
<tr>
<td id="stub-11" class="gt_row gt_left gt_stub" scope="row">NSX</td>
<td class="gt_row gt_right" headers="Acura stub-11 hp">573.0</td>
<td class="gt_row gt_right" headers="Acura stub-11 trq">476.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Nissan" class="gt_group_heading" scope="colgroup">Nissan</td>
</tr>
<tr>
<td id="summary-Nissan-Mean" class="gt_last_summary_row_top gt_row gt_left gt_stub gt_summary_row" scope="row">Mean</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Mean hp">545.00</td>
<td class="gt_last_summary_row_top gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Mean trq">436.00</td>
</tr>
<tr>
<td id="stub-12" class="gt_row gt_left gt_stub" scope="row">GT-R</td>
<td class="gt_row gt_right" headers="Nissan stub-12 hp">545.0</td>
<td class="gt_row gt_right" headers="Nissan stub-12 trq">436.0</td>
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
#mzmwyurgye table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mzmwyurgye thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mzmwyurgye p { margin: 0; padding: 0; }
 #mzmwyurgye .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mzmwyurgye .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mzmwyurgye .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mzmwyurgye .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mzmwyurgye .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mzmwyurgye .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mzmwyurgye .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mzmwyurgye .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mzmwyurgye .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mzmwyurgye .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mzmwyurgye .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mzmwyurgye .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mzmwyurgye .gt_spanner_row { border-bottom-style: hidden; }
 #mzmwyurgye .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mzmwyurgye .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mzmwyurgye .gt_from_md> :first-child { margin-top: 0; }
 #mzmwyurgye .gt_from_md> :last-child { margin-bottom: 0; }
 #mzmwyurgye .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mzmwyurgye .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mzmwyurgye .gt_indent_1 { text-indent: 5px; }
 #mzmwyurgye .gt_indent_2 { text-indent: calc(5px * 2); }
 #mzmwyurgye .gt_indent_3 { text-indent: calc(5px * 3); }
 #mzmwyurgye .gt_indent_4 { text-indent: calc(5px * 4); }
 #mzmwyurgye .gt_indent_5 { text-indent: calc(5px * 5); }
 #mzmwyurgye .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mzmwyurgye .gt_row_group_first td { border-top-width: 2px; }
 #mzmwyurgye .gt_row_group_first th { border-top-width: 2px; }
 #mzmwyurgye .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mzmwyurgye .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mzmwyurgye .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mzmwyurgye .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mzmwyurgye .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mzmwyurgye .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mzmwyurgye .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mzmwyurgye .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mzmwyurgye .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mzmwyurgye .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mzmwyurgye .gt_left { text-align: left; }
 #mzmwyurgye .gt_center { text-align: center; }
 #mzmwyurgye .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mzmwyurgye .gt_font_normal { font-weight: normal; }
 #mzmwyurgye .gt_font_bold { font-weight: bold; }
 #mzmwyurgye .gt_font_italic { font-style: italic; }
 #mzmwyurgye .gt_super { font-size: 65%; }
 #mzmwyurgye .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mzmwyurgye .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mzmwyurgye .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mzmwyurgye .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mzmwyurgye .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mzmwyurgye .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" id="Ford" class="gt_group_heading" scope="colgroup">Ford</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</td>
<td class="gt_row gt_right" headers="Ford stub-1 hp">647.0</td>
<td class="gt_row gt_right" headers="Ford stub-1 trq">550.0</td>
</tr>
<tr>
<td id="summary-Ford-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Ford summary-Ford-Min hp">647</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Ford summary-Ford-Min trq">550</td>
</tr>
<tr>
<td id="summary-Ford-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Ford summary-Ford-Max hp">647</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Ford summary-Ford-Max trq">550</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Ferrari" class="gt_group_heading" scope="colgroup">Ferrari</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 hp">597.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 trq">398.0</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 trq">398.0</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 trq">398.0</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 hp">661.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 trq">561.0</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">California</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 hp">553.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 trq">557.0</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">GTC4Lusso</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 hp">680.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 trq">514.0</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">FF</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 hp">652.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 trq">504.0</td>
</tr>
<tr>
<td id="stub-9" class="gt_row gt_left gt_stub" scope="row">F12Berlinetta</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 hp">731.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 trq">509.0</td>
</tr>
<tr>
<td id="stub-10" class="gt_row gt_left gt_stub" scope="row">LaFerrari</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 hp">949.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 trq">664.0</td>
</tr>
<tr>
<td id="summary-Ferrari-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Ferrari summary-Ferrari-Min hp">553</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Ferrari summary-Ferrari-Min trq">398</td>
</tr>
<tr>
<td id="summary-Ferrari-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Ferrari summary-Ferrari-Max hp">949</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Ferrari summary-Ferrari-Max trq">664</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Acura" class="gt_group_heading" scope="colgroup">Acura</td>
</tr>
<tr>
<td id="stub-11" class="gt_row gt_left gt_stub" scope="row">NSX</td>
<td class="gt_row gt_right" headers="Acura stub-11 hp">573.0</td>
<td class="gt_row gt_right" headers="Acura stub-11 trq">476.0</td>
</tr>
<tr>
<td id="summary-Acura-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Acura summary-Acura-Min hp">573</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Acura summary-Acura-Min trq">476</td>
</tr>
<tr>
<td id="summary-Acura-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Acura summary-Acura-Max hp">573</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Acura summary-Acura-Max trq">476</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="Nissan" class="gt_group_heading" scope="colgroup">Nissan</td>
</tr>
<tr>
<td id="stub-12" class="gt_row gt_left gt_stub" scope="row">GT-R</td>
<td class="gt_row gt_right" headers="Nissan stub-12 hp">545.0</td>
<td class="gt_row gt_right" headers="Nissan stub-12 trq">436.0</td>
</tr>
<tr>
<td id="summary-Nissan-Min" class="gt_first_summary_row gt_row gt_left gt_stub gt_summary_row" scope="row">Min</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Nissan summary-Nissan-Min hp">545</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Nissan summary-Nissan-Min trq">436</td>
</tr>
<tr>
<td id="summary-Nissan-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Nissan summary-Nissan-Max hp">545</td>
<td class="gt_row gt_right gt_summary_row" style="background-color: lightyellow; background-color: lightyellow; background-color: lightyellow; background-color: lightyellow" headers="Nissan summary-Nissan-Max trq">436</td>
</tr>
<tr>
<td id="grand-summary-Overall-Mean" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Overall Mean</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightblue" headers="grand-summary-Overall-Mean hp">642.67</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightblue" headers="grand-summary-Overall-Mean trq">497.08</td>
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
#wfpahksdpj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wfpahksdpj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wfpahksdpj p { margin: 0; padding: 0; }
 #wfpahksdpj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wfpahksdpj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wfpahksdpj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wfpahksdpj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wfpahksdpj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wfpahksdpj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wfpahksdpj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wfpahksdpj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wfpahksdpj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wfpahksdpj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wfpahksdpj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wfpahksdpj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wfpahksdpj .gt_spanner_row { border-bottom-style: hidden; }
 #wfpahksdpj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wfpahksdpj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wfpahksdpj .gt_from_md> :first-child { margin-top: 0; }
 #wfpahksdpj .gt_from_md> :last-child { margin-bottom: 0; }
 #wfpahksdpj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wfpahksdpj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wfpahksdpj .gt_indent_1 { text-indent: 5px; }
 #wfpahksdpj .gt_indent_2 { text-indent: calc(5px * 2); }
 #wfpahksdpj .gt_indent_3 { text-indent: calc(5px * 3); }
 #wfpahksdpj .gt_indent_4 { text-indent: calc(5px * 4); }
 #wfpahksdpj .gt_indent_5 { text-indent: calc(5px * 5); }
 #wfpahksdpj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wfpahksdpj .gt_row_group_first td { border-top-width: 2px; }
 #wfpahksdpj .gt_row_group_first th { border-top-width: 2px; }
 #wfpahksdpj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wfpahksdpj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wfpahksdpj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wfpahksdpj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wfpahksdpj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wfpahksdpj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wfpahksdpj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wfpahksdpj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wfpahksdpj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wfpahksdpj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wfpahksdpj .gt_left { text-align: left; }
 #wfpahksdpj .gt_center { text-align: center; }
 #wfpahksdpj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wfpahksdpj .gt_font_normal { font-weight: normal; }
 #wfpahksdpj .gt_font_bold { font-weight: bold; }
 #wfpahksdpj .gt_font_italic { font-style: italic; }
 #wfpahksdpj .gt_super { font-size: 65%; }
 #wfpahksdpj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wfpahksdpj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wfpahksdpj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wfpahksdpj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wfpahksdpj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wfpahksdpj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th rowspan="3" id="Ford" class="gt_row gt_left gt_stub_row_group" scope="rowgroup">Ford</th>
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_right" headers="Ford stub-1 hp">647.0</td>
<td class="gt_row gt_right" headers="Ford stub-1 trq">550.0</td>
</tr>
<tr>
<th id="summary-Ford-Min" class="gt_row gt_left gt_stub gt_summary_row gt_first_summary_row" scope="row">Min</th>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Min hp">647</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Min trq">550</td>
</tr>
<tr>
<th id="summary-Ford-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</th>
<td class="gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Max hp">647</td>
<td class="gt_row gt_right gt_summary_row" headers="Ford summary-Ford-Max trq">550</td>
</tr>
<tr class="gt_row_group_first">
<th rowspan="11" id="Ferrari" class="gt_row gt_left gt_stub_row_group" scope="rowgroup">Ferrari</th>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_right" headers="Ferrari stub-2 hp">597.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-2 trq">398.0</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_right" headers="Ferrari stub-3 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-3 trq">398.0</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_right" headers="Ferrari stub-4 hp">562.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-4 trq">398.0</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_right" headers="Ferrari stub-5 hp">661.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-5 trq">561.0</td>
</tr>
<tr>
<th id="stub-6" class="gt_row gt_left gt_stub" scope="row">California</th>
<td class="gt_row gt_right" headers="Ferrari stub-6 hp">553.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-6 trq">557.0</td>
</tr>
<tr>
<th id="stub-7" class="gt_row gt_left gt_stub" scope="row">GTC4Lusso</th>
<td class="gt_row gt_right" headers="Ferrari stub-7 hp">680.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-7 trq">514.0</td>
</tr>
<tr>
<th id="stub-8" class="gt_row gt_left gt_stub" scope="row">FF</th>
<td class="gt_row gt_right" headers="Ferrari stub-8 hp">652.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-8 trq">504.0</td>
</tr>
<tr>
<th id="stub-9" class="gt_row gt_left gt_stub" scope="row">F12Berlinetta</th>
<td class="gt_row gt_right" headers="Ferrari stub-9 hp">731.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-9 trq">509.0</td>
</tr>
<tr>
<th id="stub-10" class="gt_row gt_left gt_stub" scope="row">LaFerrari</th>
<td class="gt_row gt_right" headers="Ferrari stub-10 hp">949.0</td>
<td class="gt_row gt_right" headers="Ferrari stub-10 trq">664.0</td>
</tr>
<tr>
<th id="summary-Ferrari-Min" class="gt_row gt_left gt_stub gt_summary_row gt_first_summary_row" scope="row">Min</th>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Min hp">553</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Min trq">398</td>
</tr>
<tr>
<th id="summary-Ferrari-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</th>
<td class="gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Max hp">949</td>
<td class="gt_row gt_right gt_summary_row" headers="Ferrari summary-Ferrari-Max trq">664</td>
</tr>
<tr class="gt_row_group_first">
<th rowspan="3" id="Acura" class="gt_row gt_left gt_stub_row_group" scope="rowgroup">Acura</th>
<th id="stub-11" class="gt_row gt_left gt_stub" scope="row">NSX</th>
<td class="gt_row gt_right" headers="Acura stub-11 hp">573.0</td>
<td class="gt_row gt_right" headers="Acura stub-11 trq">476.0</td>
</tr>
<tr>
<th id="summary-Acura-Min" class="gt_row gt_left gt_stub gt_summary_row gt_first_summary_row" scope="row">Min</th>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Min hp">573</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Min trq">476</td>
</tr>
<tr>
<th id="summary-Acura-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</th>
<td class="gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Max hp">573</td>
<td class="gt_row gt_right gt_summary_row" headers="Acura summary-Acura-Max trq">476</td>
</tr>
<tr class="gt_row_group_first">
<th rowspan="3" id="Nissan" class="gt_row gt_left gt_stub_row_group" scope="rowgroup">Nissan</th>
<th id="stub-12" class="gt_row gt_left gt_stub" scope="row">GT-R</th>
<td class="gt_row gt_right" headers="Nissan stub-12 hp">545.0</td>
<td class="gt_row gt_right" headers="Nissan stub-12 trq">436.0</td>
</tr>
<tr>
<th id="summary-Nissan-Min" class="gt_row gt_left gt_stub gt_summary_row gt_first_summary_row" scope="row">Min</th>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Min hp">545</td>
<td class="gt_first_summary_row gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Min trq">436</td>
</tr>
<tr>
<th id="summary-Nissan-Max" class="gt_row gt_left gt_stub gt_summary_row" scope="row">Max</th>
<td class="gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Max hp">545</td>
<td class="gt_row gt_right gt_summary_row" headers="Nissan summary-Nissan-Max trq">436</td>
</tr>
</tbody>
</table>
