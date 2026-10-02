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
#ekkfxutzld table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ekkfxutzld thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ekkfxutzld p { margin: 0; padding: 0; }
 #ekkfxutzld .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ekkfxutzld .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ekkfxutzld .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ekkfxutzld .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ekkfxutzld .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ekkfxutzld .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ekkfxutzld .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ekkfxutzld .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ekkfxutzld .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ekkfxutzld .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ekkfxutzld .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ekkfxutzld .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ekkfxutzld .gt_spanner_row { border-bottom-style: hidden; }
 #ekkfxutzld .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ekkfxutzld .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ekkfxutzld .gt_from_md> :first-child { margin-top: 0; }
 #ekkfxutzld .gt_from_md> :last-child { margin-bottom: 0; }
 #ekkfxutzld .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ekkfxutzld .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ekkfxutzld .gt_indent_1 { text-indent: 5px; }
 #ekkfxutzld .gt_indent_2 { text-indent: calc(5px * 2); }
 #ekkfxutzld .gt_indent_3 { text-indent: calc(5px * 3); }
 #ekkfxutzld .gt_indent_4 { text-indent: calc(5px * 4); }
 #ekkfxutzld .gt_indent_5 { text-indent: calc(5px * 5); }
 #ekkfxutzld .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ekkfxutzld .gt_row_group_first td { border-top-width: 2px; }
 #ekkfxutzld .gt_row_group_first th { border-top-width: 2px; }
 #ekkfxutzld .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ekkfxutzld .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ekkfxutzld .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ekkfxutzld .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ekkfxutzld .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ekkfxutzld .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ekkfxutzld .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ekkfxutzld .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ekkfxutzld .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ekkfxutzld .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ekkfxutzld .gt_left { text-align: left; }
 #ekkfxutzld .gt_center { text-align: center; }
 #ekkfxutzld .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ekkfxutzld .gt_font_normal { font-weight: normal; }
 #ekkfxutzld .gt_font_bold { font-weight: bold; }
 #ekkfxutzld .gt_font_italic { font-style: italic; }
 #ekkfxutzld .gt_super { font-size: 65%; }
 #ekkfxutzld .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ekkfxutzld .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ekkfxutzld .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ekkfxutzld .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ekkfxutzld .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ekkfxutzld .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pccfabzidg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pccfabzidg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pccfabzidg p { margin: 0; padding: 0; }
 #pccfabzidg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pccfabzidg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pccfabzidg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pccfabzidg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pccfabzidg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pccfabzidg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pccfabzidg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pccfabzidg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pccfabzidg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pccfabzidg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pccfabzidg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pccfabzidg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pccfabzidg .gt_spanner_row { border-bottom-style: hidden; }
 #pccfabzidg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pccfabzidg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pccfabzidg .gt_from_md> :first-child { margin-top: 0; }
 #pccfabzidg .gt_from_md> :last-child { margin-bottom: 0; }
 #pccfabzidg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pccfabzidg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pccfabzidg .gt_indent_1 { text-indent: 5px; }
 #pccfabzidg .gt_indent_2 { text-indent: calc(5px * 2); }
 #pccfabzidg .gt_indent_3 { text-indent: calc(5px * 3); }
 #pccfabzidg .gt_indent_4 { text-indent: calc(5px * 4); }
 #pccfabzidg .gt_indent_5 { text-indent: calc(5px * 5); }
 #pccfabzidg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pccfabzidg .gt_row_group_first td { border-top-width: 2px; }
 #pccfabzidg .gt_row_group_first th { border-top-width: 2px; }
 #pccfabzidg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pccfabzidg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pccfabzidg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pccfabzidg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pccfabzidg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pccfabzidg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pccfabzidg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pccfabzidg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pccfabzidg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pccfabzidg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pccfabzidg .gt_left { text-align: left; }
 #pccfabzidg .gt_center { text-align: center; }
 #pccfabzidg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pccfabzidg .gt_font_normal { font-weight: normal; }
 #pccfabzidg .gt_font_bold { font-weight: bold; }
 #pccfabzidg .gt_font_italic { font-style: italic; }
 #pccfabzidg .gt_super { font-size: 65%; }
 #pccfabzidg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pccfabzidg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pccfabzidg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pccfabzidg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pccfabzidg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pccfabzidg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#azqzimwhum table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#azqzimwhum thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#azqzimwhum p { margin: 0; padding: 0; }
 #azqzimwhum .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #azqzimwhum .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #azqzimwhum .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #azqzimwhum .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #azqzimwhum .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #azqzimwhum .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #azqzimwhum .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #azqzimwhum .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #azqzimwhum .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #azqzimwhum .gt_column_spanner_outer:first-child { padding-left: 0; }
 #azqzimwhum .gt_column_spanner_outer:last-child { padding-right: 0; }
 #azqzimwhum .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #azqzimwhum .gt_spanner_row { border-bottom-style: hidden; }
 #azqzimwhum .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #azqzimwhum .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #azqzimwhum .gt_from_md> :first-child { margin-top: 0; }
 #azqzimwhum .gt_from_md> :last-child { margin-bottom: 0; }
 #azqzimwhum .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #azqzimwhum .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #azqzimwhum .gt_indent_1 { text-indent: 5px; }
 #azqzimwhum .gt_indent_2 { text-indent: calc(5px * 2); }
 #azqzimwhum .gt_indent_3 { text-indent: calc(5px * 3); }
 #azqzimwhum .gt_indent_4 { text-indent: calc(5px * 4); }
 #azqzimwhum .gt_indent_5 { text-indent: calc(5px * 5); }
 #azqzimwhum .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #azqzimwhum .gt_row_group_first td { border-top-width: 2px; }
 #azqzimwhum .gt_row_group_first th { border-top-width: 2px; }
 #azqzimwhum .gt_striped { color: #333333; background-color: #F4F4F4; }
 #azqzimwhum .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #azqzimwhum .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #azqzimwhum .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #azqzimwhum .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #azqzimwhum .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #azqzimwhum .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #azqzimwhum .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #azqzimwhum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #azqzimwhum .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #azqzimwhum .gt_left { text-align: left; }
 #azqzimwhum .gt_center { text-align: center; }
 #azqzimwhum .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #azqzimwhum .gt_font_normal { font-weight: normal; }
 #azqzimwhum .gt_font_bold { font-weight: bold; }
 #azqzimwhum .gt_font_italic { font-style: italic; }
 #azqzimwhum .gt_super { font-size: 65%; }
 #azqzimwhum .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #azqzimwhum .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #azqzimwhum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #azqzimwhum .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #azqzimwhum .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #azqzimwhum .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#psmdqtzlqd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#psmdqtzlqd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#psmdqtzlqd p { margin: 0; padding: 0; }
 #psmdqtzlqd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #psmdqtzlqd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #psmdqtzlqd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #psmdqtzlqd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #psmdqtzlqd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #psmdqtzlqd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #psmdqtzlqd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #psmdqtzlqd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #psmdqtzlqd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #psmdqtzlqd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #psmdqtzlqd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #psmdqtzlqd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #psmdqtzlqd .gt_spanner_row { border-bottom-style: hidden; }
 #psmdqtzlqd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #psmdqtzlqd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #psmdqtzlqd .gt_from_md> :first-child { margin-top: 0; }
 #psmdqtzlqd .gt_from_md> :last-child { margin-bottom: 0; }
 #psmdqtzlqd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #psmdqtzlqd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #psmdqtzlqd .gt_indent_1 { text-indent: 5px; }
 #psmdqtzlqd .gt_indent_2 { text-indent: calc(5px * 2); }
 #psmdqtzlqd .gt_indent_3 { text-indent: calc(5px * 3); }
 #psmdqtzlqd .gt_indent_4 { text-indent: calc(5px * 4); }
 #psmdqtzlqd .gt_indent_5 { text-indent: calc(5px * 5); }
 #psmdqtzlqd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #psmdqtzlqd .gt_row_group_first td { border-top-width: 2px; }
 #psmdqtzlqd .gt_row_group_first th { border-top-width: 2px; }
 #psmdqtzlqd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #psmdqtzlqd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #psmdqtzlqd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #psmdqtzlqd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #psmdqtzlqd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #psmdqtzlqd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #psmdqtzlqd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #psmdqtzlqd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #psmdqtzlqd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #psmdqtzlqd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #psmdqtzlqd .gt_left { text-align: left; }
 #psmdqtzlqd .gt_center { text-align: center; }
 #psmdqtzlqd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #psmdqtzlqd .gt_font_normal { font-weight: normal; }
 #psmdqtzlqd .gt_font_bold { font-weight: bold; }
 #psmdqtzlqd .gt_font_italic { font-style: italic; }
 #psmdqtzlqd .gt_super { font-size: 65%; }
 #psmdqtzlqd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #psmdqtzlqd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #psmdqtzlqd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #psmdqtzlqd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #psmdqtzlqd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #psmdqtzlqd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#usokvyfsmk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#usokvyfsmk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#usokvyfsmk p { margin: 0; padding: 0; }
 #usokvyfsmk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #usokvyfsmk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #usokvyfsmk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #usokvyfsmk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #usokvyfsmk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #usokvyfsmk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #usokvyfsmk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #usokvyfsmk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #usokvyfsmk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #usokvyfsmk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #usokvyfsmk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #usokvyfsmk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #usokvyfsmk .gt_spanner_row { border-bottom-style: hidden; }
 #usokvyfsmk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #usokvyfsmk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #usokvyfsmk .gt_from_md> :first-child { margin-top: 0; }
 #usokvyfsmk .gt_from_md> :last-child { margin-bottom: 0; }
 #usokvyfsmk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #usokvyfsmk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #usokvyfsmk .gt_indent_1 { text-indent: 5px; }
 #usokvyfsmk .gt_indent_2 { text-indent: calc(5px * 2); }
 #usokvyfsmk .gt_indent_3 { text-indent: calc(5px * 3); }
 #usokvyfsmk .gt_indent_4 { text-indent: calc(5px * 4); }
 #usokvyfsmk .gt_indent_5 { text-indent: calc(5px * 5); }
 #usokvyfsmk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #usokvyfsmk .gt_row_group_first td { border-top-width: 2px; }
 #usokvyfsmk .gt_row_group_first th { border-top-width: 2px; }
 #usokvyfsmk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #usokvyfsmk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #usokvyfsmk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #usokvyfsmk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #usokvyfsmk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #usokvyfsmk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #usokvyfsmk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #usokvyfsmk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #usokvyfsmk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #usokvyfsmk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #usokvyfsmk .gt_left { text-align: left; }
 #usokvyfsmk .gt_center { text-align: center; }
 #usokvyfsmk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #usokvyfsmk .gt_font_normal { font-weight: normal; }
 #usokvyfsmk .gt_font_bold { font-weight: bold; }
 #usokvyfsmk .gt_font_italic { font-style: italic; }
 #usokvyfsmk .gt_super { font-size: 65%; }
 #usokvyfsmk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #usokvyfsmk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #usokvyfsmk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #usokvyfsmk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #usokvyfsmk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #usokvyfsmk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xggxnfjdvl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xggxnfjdvl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xggxnfjdvl p { margin: 0; padding: 0; }
 #xggxnfjdvl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xggxnfjdvl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xggxnfjdvl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xggxnfjdvl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xggxnfjdvl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xggxnfjdvl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xggxnfjdvl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xggxnfjdvl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xggxnfjdvl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xggxnfjdvl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xggxnfjdvl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xggxnfjdvl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xggxnfjdvl .gt_spanner_row { border-bottom-style: hidden; }
 #xggxnfjdvl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xggxnfjdvl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xggxnfjdvl .gt_from_md> :first-child { margin-top: 0; }
 #xggxnfjdvl .gt_from_md> :last-child { margin-bottom: 0; }
 #xggxnfjdvl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xggxnfjdvl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xggxnfjdvl .gt_indent_1 { text-indent: 5px; }
 #xggxnfjdvl .gt_indent_2 { text-indent: calc(5px * 2); }
 #xggxnfjdvl .gt_indent_3 { text-indent: calc(5px * 3); }
 #xggxnfjdvl .gt_indent_4 { text-indent: calc(5px * 4); }
 #xggxnfjdvl .gt_indent_5 { text-indent: calc(5px * 5); }
 #xggxnfjdvl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xggxnfjdvl .gt_row_group_first td { border-top-width: 2px; }
 #xggxnfjdvl .gt_row_group_first th { border-top-width: 2px; }
 #xggxnfjdvl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xggxnfjdvl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xggxnfjdvl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xggxnfjdvl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xggxnfjdvl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xggxnfjdvl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xggxnfjdvl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xggxnfjdvl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xggxnfjdvl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xggxnfjdvl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xggxnfjdvl .gt_left { text-align: left; }
 #xggxnfjdvl .gt_center { text-align: center; }
 #xggxnfjdvl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xggxnfjdvl .gt_font_normal { font-weight: normal; }
 #xggxnfjdvl .gt_font_bold { font-weight: bold; }
 #xggxnfjdvl .gt_font_italic { font-style: italic; }
 #xggxnfjdvl .gt_super { font-size: 65%; }
 #xggxnfjdvl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xggxnfjdvl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xggxnfjdvl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xggxnfjdvl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xggxnfjdvl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xggxnfjdvl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
