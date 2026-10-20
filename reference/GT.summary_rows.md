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
#cxvvmdacoz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cxvvmdacoz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cxvvmdacoz p { margin: 0; padding: 0; }
 #cxvvmdacoz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cxvvmdacoz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cxvvmdacoz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cxvvmdacoz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cxvvmdacoz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cxvvmdacoz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cxvvmdacoz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cxvvmdacoz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cxvvmdacoz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cxvvmdacoz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cxvvmdacoz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cxvvmdacoz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cxvvmdacoz .gt_spanner_row { border-bottom-style: hidden; }
 #cxvvmdacoz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cxvvmdacoz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cxvvmdacoz .gt_from_md> :first-child { margin-top: 0; }
 #cxvvmdacoz .gt_from_md> :last-child { margin-bottom: 0; }
 #cxvvmdacoz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cxvvmdacoz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cxvvmdacoz .gt_indent_1 { text-indent: 5px; }
 #cxvvmdacoz .gt_indent_2 { text-indent: calc(5px * 2); }
 #cxvvmdacoz .gt_indent_3 { text-indent: calc(5px * 3); }
 #cxvvmdacoz .gt_indent_4 { text-indent: calc(5px * 4); }
 #cxvvmdacoz .gt_indent_5 { text-indent: calc(5px * 5); }
 #cxvvmdacoz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cxvvmdacoz .gt_row_group_first td { border-top-width: 2px; }
 #cxvvmdacoz .gt_row_group_first th { border-top-width: 2px; }
 #cxvvmdacoz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cxvvmdacoz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cxvvmdacoz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cxvvmdacoz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cxvvmdacoz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cxvvmdacoz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cxvvmdacoz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cxvvmdacoz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cxvvmdacoz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cxvvmdacoz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cxvvmdacoz .gt_left { text-align: left; }
 #cxvvmdacoz .gt_center { text-align: center; }
 #cxvvmdacoz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cxvvmdacoz .gt_font_normal { font-weight: normal; }
 #cxvvmdacoz .gt_font_bold { font-weight: bold; }
 #cxvvmdacoz .gt_font_italic { font-style: italic; }
 #cxvvmdacoz .gt_super { font-size: 65%; }
 #cxvvmdacoz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cxvvmdacoz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cxvvmdacoz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cxvvmdacoz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cxvvmdacoz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cxvvmdacoz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rcsndvjofs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rcsndvjofs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rcsndvjofs p { margin: 0; padding: 0; }
 #rcsndvjofs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rcsndvjofs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rcsndvjofs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rcsndvjofs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rcsndvjofs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rcsndvjofs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rcsndvjofs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rcsndvjofs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rcsndvjofs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rcsndvjofs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rcsndvjofs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rcsndvjofs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rcsndvjofs .gt_spanner_row { border-bottom-style: hidden; }
 #rcsndvjofs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rcsndvjofs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rcsndvjofs .gt_from_md> :first-child { margin-top: 0; }
 #rcsndvjofs .gt_from_md> :last-child { margin-bottom: 0; }
 #rcsndvjofs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rcsndvjofs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rcsndvjofs .gt_indent_1 { text-indent: 5px; }
 #rcsndvjofs .gt_indent_2 { text-indent: calc(5px * 2); }
 #rcsndvjofs .gt_indent_3 { text-indent: calc(5px * 3); }
 #rcsndvjofs .gt_indent_4 { text-indent: calc(5px * 4); }
 #rcsndvjofs .gt_indent_5 { text-indent: calc(5px * 5); }
 #rcsndvjofs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rcsndvjofs .gt_row_group_first td { border-top-width: 2px; }
 #rcsndvjofs .gt_row_group_first th { border-top-width: 2px; }
 #rcsndvjofs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rcsndvjofs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rcsndvjofs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rcsndvjofs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rcsndvjofs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rcsndvjofs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rcsndvjofs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rcsndvjofs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rcsndvjofs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rcsndvjofs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rcsndvjofs .gt_left { text-align: left; }
 #rcsndvjofs .gt_center { text-align: center; }
 #rcsndvjofs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rcsndvjofs .gt_font_normal { font-weight: normal; }
 #rcsndvjofs .gt_font_bold { font-weight: bold; }
 #rcsndvjofs .gt_font_italic { font-style: italic; }
 #rcsndvjofs .gt_super { font-size: 65%; }
 #rcsndvjofs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rcsndvjofs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rcsndvjofs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rcsndvjofs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rcsndvjofs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rcsndvjofs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vaucosadhw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vaucosadhw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vaucosadhw p { margin: 0; padding: 0; }
 #vaucosadhw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vaucosadhw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vaucosadhw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vaucosadhw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vaucosadhw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vaucosadhw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vaucosadhw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vaucosadhw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vaucosadhw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vaucosadhw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vaucosadhw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vaucosadhw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vaucosadhw .gt_spanner_row { border-bottom-style: hidden; }
 #vaucosadhw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vaucosadhw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vaucosadhw .gt_from_md> :first-child { margin-top: 0; }
 #vaucosadhw .gt_from_md> :last-child { margin-bottom: 0; }
 #vaucosadhw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vaucosadhw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vaucosadhw .gt_indent_1 { text-indent: 5px; }
 #vaucosadhw .gt_indent_2 { text-indent: calc(5px * 2); }
 #vaucosadhw .gt_indent_3 { text-indent: calc(5px * 3); }
 #vaucosadhw .gt_indent_4 { text-indent: calc(5px * 4); }
 #vaucosadhw .gt_indent_5 { text-indent: calc(5px * 5); }
 #vaucosadhw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vaucosadhw .gt_row_group_first td { border-top-width: 2px; }
 #vaucosadhw .gt_row_group_first th { border-top-width: 2px; }
 #vaucosadhw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vaucosadhw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vaucosadhw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vaucosadhw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vaucosadhw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vaucosadhw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vaucosadhw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vaucosadhw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vaucosadhw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vaucosadhw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vaucosadhw .gt_left { text-align: left; }
 #vaucosadhw .gt_center { text-align: center; }
 #vaucosadhw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vaucosadhw .gt_font_normal { font-weight: normal; }
 #vaucosadhw .gt_font_bold { font-weight: bold; }
 #vaucosadhw .gt_font_italic { font-style: italic; }
 #vaucosadhw .gt_super { font-size: 65%; }
 #vaucosadhw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vaucosadhw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vaucosadhw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vaucosadhw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vaucosadhw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vaucosadhw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sbwwrpewgy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sbwwrpewgy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sbwwrpewgy p { margin: 0; padding: 0; }
 #sbwwrpewgy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sbwwrpewgy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sbwwrpewgy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sbwwrpewgy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sbwwrpewgy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sbwwrpewgy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbwwrpewgy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sbwwrpewgy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sbwwrpewgy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sbwwrpewgy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sbwwrpewgy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sbwwrpewgy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sbwwrpewgy .gt_spanner_row { border-bottom-style: hidden; }
 #sbwwrpewgy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sbwwrpewgy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sbwwrpewgy .gt_from_md> :first-child { margin-top: 0; }
 #sbwwrpewgy .gt_from_md> :last-child { margin-bottom: 0; }
 #sbwwrpewgy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sbwwrpewgy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sbwwrpewgy .gt_indent_1 { text-indent: 5px; }
 #sbwwrpewgy .gt_indent_2 { text-indent: calc(5px * 2); }
 #sbwwrpewgy .gt_indent_3 { text-indent: calc(5px * 3); }
 #sbwwrpewgy .gt_indent_4 { text-indent: calc(5px * 4); }
 #sbwwrpewgy .gt_indent_5 { text-indent: calc(5px * 5); }
 #sbwwrpewgy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sbwwrpewgy .gt_row_group_first td { border-top-width: 2px; }
 #sbwwrpewgy .gt_row_group_first th { border-top-width: 2px; }
 #sbwwrpewgy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sbwwrpewgy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbwwrpewgy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sbwwrpewgy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sbwwrpewgy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbwwrpewgy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sbwwrpewgy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sbwwrpewgy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sbwwrpewgy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbwwrpewgy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sbwwrpewgy .gt_left { text-align: left; }
 #sbwwrpewgy .gt_center { text-align: center; }
 #sbwwrpewgy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sbwwrpewgy .gt_font_normal { font-weight: normal; }
 #sbwwrpewgy .gt_font_bold { font-weight: bold; }
 #sbwwrpewgy .gt_font_italic { font-style: italic; }
 #sbwwrpewgy .gt_super { font-size: 65%; }
 #sbwwrpewgy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbwwrpewgy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sbwwrpewgy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbwwrpewgy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sbwwrpewgy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sbwwrpewgy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pwibhmshap table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pwibhmshap thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pwibhmshap p { margin: 0; padding: 0; }
 #pwibhmshap .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pwibhmshap .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pwibhmshap .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pwibhmshap .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pwibhmshap .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pwibhmshap .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pwibhmshap .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pwibhmshap .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pwibhmshap .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pwibhmshap .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pwibhmshap .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pwibhmshap .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pwibhmshap .gt_spanner_row { border-bottom-style: hidden; }
 #pwibhmshap .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pwibhmshap .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pwibhmshap .gt_from_md> :first-child { margin-top: 0; }
 #pwibhmshap .gt_from_md> :last-child { margin-bottom: 0; }
 #pwibhmshap .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pwibhmshap .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pwibhmshap .gt_indent_1 { text-indent: 5px; }
 #pwibhmshap .gt_indent_2 { text-indent: calc(5px * 2); }
 #pwibhmshap .gt_indent_3 { text-indent: calc(5px * 3); }
 #pwibhmshap .gt_indent_4 { text-indent: calc(5px * 4); }
 #pwibhmshap .gt_indent_5 { text-indent: calc(5px * 5); }
 #pwibhmshap .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pwibhmshap .gt_row_group_first td { border-top-width: 2px; }
 #pwibhmshap .gt_row_group_first th { border-top-width: 2px; }
 #pwibhmshap .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pwibhmshap .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pwibhmshap .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pwibhmshap .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pwibhmshap .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pwibhmshap .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pwibhmshap .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pwibhmshap .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pwibhmshap .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pwibhmshap .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pwibhmshap .gt_left { text-align: left; }
 #pwibhmshap .gt_center { text-align: center; }
 #pwibhmshap .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pwibhmshap .gt_font_normal { font-weight: normal; }
 #pwibhmshap .gt_font_bold { font-weight: bold; }
 #pwibhmshap .gt_font_italic { font-style: italic; }
 #pwibhmshap .gt_super { font-size: 65%; }
 #pwibhmshap .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pwibhmshap .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pwibhmshap .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pwibhmshap .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pwibhmshap .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pwibhmshap .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vbenfhgskv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vbenfhgskv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vbenfhgskv p { margin: 0; padding: 0; }
 #vbenfhgskv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vbenfhgskv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vbenfhgskv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vbenfhgskv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vbenfhgskv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vbenfhgskv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vbenfhgskv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vbenfhgskv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vbenfhgskv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vbenfhgskv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vbenfhgskv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vbenfhgskv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vbenfhgskv .gt_spanner_row { border-bottom-style: hidden; }
 #vbenfhgskv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vbenfhgskv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vbenfhgskv .gt_from_md> :first-child { margin-top: 0; }
 #vbenfhgskv .gt_from_md> :last-child { margin-bottom: 0; }
 #vbenfhgskv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vbenfhgskv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vbenfhgskv .gt_indent_1 { text-indent: 5px; }
 #vbenfhgskv .gt_indent_2 { text-indent: calc(5px * 2); }
 #vbenfhgskv .gt_indent_3 { text-indent: calc(5px * 3); }
 #vbenfhgskv .gt_indent_4 { text-indent: calc(5px * 4); }
 #vbenfhgskv .gt_indent_5 { text-indent: calc(5px * 5); }
 #vbenfhgskv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vbenfhgskv .gt_row_group_first td { border-top-width: 2px; }
 #vbenfhgskv .gt_row_group_first th { border-top-width: 2px; }
 #vbenfhgskv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vbenfhgskv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vbenfhgskv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vbenfhgskv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vbenfhgskv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vbenfhgskv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vbenfhgskv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vbenfhgskv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vbenfhgskv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vbenfhgskv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vbenfhgskv .gt_left { text-align: left; }
 #vbenfhgskv .gt_center { text-align: center; }
 #vbenfhgskv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vbenfhgskv .gt_font_normal { font-weight: normal; }
 #vbenfhgskv .gt_font_bold { font-weight: bold; }
 #vbenfhgskv .gt_font_italic { font-style: italic; }
 #vbenfhgskv .gt_super { font-size: 65%; }
 #vbenfhgskv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vbenfhgskv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vbenfhgskv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vbenfhgskv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vbenfhgskv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vbenfhgskv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
