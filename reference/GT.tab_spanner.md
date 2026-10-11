# GT.tab_spanner()


Insert a spanner above a selection of column headings.


Usage

``` python
GT.tab_spanner(
    label,
    columns=None,
    spanners=None,
    level=None,
    id=None,
    gather=True,
    replace=False,
)
```


This part of the table contains, at a minimum, column labels and, optionally, an unlimited number of levels for spanners. A spanner will occupy space over any number of contiguous column labels and it will have an associated label and ID value. This method allows for mapping to be defined by column names, existing spanner ID values, or a mixture of both.

The spanners are placed in the order of calling [tab_spanner()](GT.tab_spanner.md#great_tables.GT.tab_spanner) so if a later call uses the same columns in its definition (or even a subset) as the first invocation, the second spanner will be overlaid atop the first. Options exist for forcibly inserting a spanner underneath others (with `level` as space permits) and with `replace`, which allows for full or partial spanner replacement.


## Parameters


`label: str | BaseText`  
The text to use for the spanner label. We can optionally use the <a href="../reference/md.html#great_tables.md" class="gdls-link"><code>md()</code></a> and <a href="../reference/html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions to style the text as Markdown or to retain HTML elements in the text. Alternatively, units notation can be used (see <a href="../reference/define_units.html#great_tables.define_units" class="gdls-link"><code>define_units()</code></a> for details).

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`spanners: str | list[str] | None = None`  
The spanners that should be spanned over, should they already be defined. One or more spanner ID values (in quotes) can be supplied here. This argument works in tandem with the `columns` argument.

`level: int | None = None`  
An explicit level to which the spanner should be placed. If not provided, **Great Tables** will choose the level based on the inputs provided within `columns` and `spanners`, placing the spanner label where it will fit. The first spanner level (right above the column labels) is `0`.

`id: str | None = None`  
The ID for the spanner. When accessing a spanner through the `spanners` argument of [tab_spanner()](GT.tab_spanner.md#great_tables.GT.tab_spanner) the `id` value is used as the reference (and not the `label`). If an `id` is not explicitly provided here, it will be taken from the `label` value. It is advisable to set an explicit `id` value if you plan to access this cell in a later call and the label text is complicated (e.g., contains markup, is lengthy, or both). Finally, when providing an `id` value you must ensure that it is unique across all ID values set for spanner labels (the method will throw an error if `id` isn't unique).

`gather: bool = ``True`  
An option to move the specified `columns` such that they are unified under the spanner. Ordering of the moved-into-place columns will be preserved in all cases. By default, this is set to `True`.

`replace: bool = ``False`  
Should new spanners be allowed to partially or fully replace existing spanners? (This is a possibility if setting spanners at an already populated `level`.) By default, this is set to `False` and an error will occur if some replacement is attempted.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's create a table using a small portion of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset. Over several columns (`hp`, `hp_rpm`, `trq`, `trq_rpm`, `mpg_c`, `mpg_h`) we'll use [tab_spanner()](GT.tab_spanner.md#great_tables.GT.tab_spanner) to add a spanner with the label `"performance"`. This effectively groups together several columns related to car performance under a unifying label.


``` python
from great_tables import GT, md
from great_tables.data import gtcars

colnames = ["model", "hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
gtcars_mini = gtcars[colnames].head(10)

(
    GT(gtcars_mini)
    .tab_spanner(
        label="performance",
        columns=["hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
    )
)
```


<style>
#elzgxgzbaf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#elzgxgzbaf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#elzgxgzbaf p { margin: 0; padding: 0; }
 #elzgxgzbaf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #elzgxgzbaf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #elzgxgzbaf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #elzgxgzbaf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #elzgxgzbaf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #elzgxgzbaf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #elzgxgzbaf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #elzgxgzbaf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #elzgxgzbaf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #elzgxgzbaf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #elzgxgzbaf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #elzgxgzbaf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #elzgxgzbaf .gt_spanner_row { border-bottom-style: hidden; }
 #elzgxgzbaf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #elzgxgzbaf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #elzgxgzbaf .gt_from_md> :first-child { margin-top: 0; }
 #elzgxgzbaf .gt_from_md> :last-child { margin-bottom: 0; }
 #elzgxgzbaf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #elzgxgzbaf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #elzgxgzbaf .gt_indent_1 { text-indent: 5px; }
 #elzgxgzbaf .gt_indent_2 { text-indent: calc(5px * 2); }
 #elzgxgzbaf .gt_indent_3 { text-indent: calc(5px * 3); }
 #elzgxgzbaf .gt_indent_4 { text-indent: calc(5px * 4); }
 #elzgxgzbaf .gt_indent_5 { text-indent: calc(5px * 5); }
 #elzgxgzbaf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #elzgxgzbaf .gt_row_group_first td { border-top-width: 2px; }
 #elzgxgzbaf .gt_row_group_first th { border-top-width: 2px; }
 #elzgxgzbaf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #elzgxgzbaf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #elzgxgzbaf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #elzgxgzbaf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #elzgxgzbaf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #elzgxgzbaf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #elzgxgzbaf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #elzgxgzbaf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #elzgxgzbaf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #elzgxgzbaf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #elzgxgzbaf .gt_left { text-align: left; }
 #elzgxgzbaf .gt_center { text-align: center; }
 #elzgxgzbaf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #elzgxgzbaf .gt_font_normal { font-weight: normal; }
 #elzgxgzbaf .gt_font_bold { font-weight: bold; }
 #elzgxgzbaf .gt_font_italic { font-style: italic; }
 #elzgxgzbaf .gt_super { font-size: 65%; }
 #elzgxgzbaf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #elzgxgzbaf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #elzgxgzbaf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #elzgxgzbaf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #elzgxgzbaf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #elzgxgzbaf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th colspan="6" id="performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="hp_rpm" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp_rpm</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="trq_rpm" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq_rpm</th>
<th id="mpg_c" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_c</th>
<th id="mpg_h" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_h</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">6250.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">5900.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">18.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">8000.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">3000.0</td>
<td class="gt_row gt_right">15.0</td>
<td class="gt_row gt_right">22.0</td>
</tr>
<tr>
<td class="gt_row gt_left">California</td>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">7500.0</td>
<td class="gt_row gt_right">557.0</td>
<td class="gt_row gt_right">4750.0</td>
<td class="gt_row gt_right">16.0</td>
<td class="gt_row gt_right">23.0</td>
</tr>
<tr>
<td class="gt_row gt_left">GTC4Lusso</td>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">8250.0</td>
<td class="gt_row gt_right">514.0</td>
<td class="gt_row gt_right">5750.0</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">FF</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">8000.0</td>
<td class="gt_row gt_right">504.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left">F12Berlinetta</td>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">8250.0</td>
<td class="gt_row gt_right">509.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left">LaFerrari</td>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">664.0</td>
<td class="gt_row gt_right">6750.0</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
</tbody>
</table>


One cool feature of [tab_spanner()](GT.tab_spanner.md#great_tables.GT.tab_spanner) is its support for multiple levels, allowing you to group columns in various ways. For example, you can create three bottom spanners and a top spanner:


``` python
(
    GT(gtcars_mini)
    .tab_spanner(
        label="hp",
        columns=["hp", "hp_rpm"],
    )
    .tab_spanner(
        label="trq",
        columns=["trq", "trq_rpm"],
    )
    .tab_spanner(
        label="mpg",
        columns=["mpg_c", "mpg_h"],
    )
    .tab_spanner(
        label="performance",
        columns=["hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"],
    )
)
```


<style>
#bhgkifikqe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bhgkifikqe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bhgkifikqe p { margin: 0; padding: 0; }
 #bhgkifikqe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bhgkifikqe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bhgkifikqe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bhgkifikqe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bhgkifikqe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhgkifikqe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhgkifikqe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhgkifikqe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bhgkifikqe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bhgkifikqe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bhgkifikqe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bhgkifikqe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bhgkifikqe .gt_spanner_row { border-bottom-style: hidden; }
 #bhgkifikqe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bhgkifikqe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bhgkifikqe .gt_from_md> :first-child { margin-top: 0; }
 #bhgkifikqe .gt_from_md> :last-child { margin-bottom: 0; }
 #bhgkifikqe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bhgkifikqe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bhgkifikqe .gt_indent_1 { text-indent: 5px; }
 #bhgkifikqe .gt_indent_2 { text-indent: calc(5px * 2); }
 #bhgkifikqe .gt_indent_3 { text-indent: calc(5px * 3); }
 #bhgkifikqe .gt_indent_4 { text-indent: calc(5px * 4); }
 #bhgkifikqe .gt_indent_5 { text-indent: calc(5px * 5); }
 #bhgkifikqe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bhgkifikqe .gt_row_group_first td { border-top-width: 2px; }
 #bhgkifikqe .gt_row_group_first th { border-top-width: 2px; }
 #bhgkifikqe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bhgkifikqe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhgkifikqe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhgkifikqe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bhgkifikqe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhgkifikqe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhgkifikqe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bhgkifikqe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bhgkifikqe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhgkifikqe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhgkifikqe .gt_left { text-align: left; }
 #bhgkifikqe .gt_center { text-align: center; }
 #bhgkifikqe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bhgkifikqe .gt_font_normal { font-weight: normal; }
 #bhgkifikqe .gt_font_bold { font-weight: bold; }
 #bhgkifikqe .gt_font_italic { font-style: italic; }
 #bhgkifikqe .gt_super { font-size: 65%; }
 #bhgkifikqe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhgkifikqe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bhgkifikqe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhgkifikqe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhgkifikqe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bhgkifikqe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col"><span> </span></th>
<th colspan="6" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th colspan="2" id="hp" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">hp</th>
<th colspan="2" id="trq" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">trq</th>
<th colspan="2" id="mpg" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">mpg</th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="hp_rpm" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp_rpm</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="trq_rpm" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq_rpm</th>
<th id="mpg_c" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_c</th>
<th id="mpg_h" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_h</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">6250.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">5900.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">18.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">8000.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">3000.0</td>
<td class="gt_row gt_right">15.0</td>
<td class="gt_row gt_right">22.0</td>
</tr>
<tr>
<td class="gt_row gt_left">California</td>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">7500.0</td>
<td class="gt_row gt_right">557.0</td>
<td class="gt_row gt_right">4750.0</td>
<td class="gt_row gt_right">16.0</td>
<td class="gt_row gt_right">23.0</td>
</tr>
<tr>
<td class="gt_row gt_left">GTC4Lusso</td>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">8250.0</td>
<td class="gt_row gt_right">514.0</td>
<td class="gt_row gt_right">5750.0</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">FF</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">8000.0</td>
<td class="gt_row gt_right">504.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left">F12Berlinetta</td>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">8250.0</td>
<td class="gt_row gt_right">509.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left">LaFerrari</td>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">664.0</td>
<td class="gt_row gt_right">6750.0</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
</tbody>
</table>


Did you notice that the spanners stacked automatically? What if you want granular control to specify a spanner in a specific hierarchy? **Great Tables** has you covered. By using the `level=` parameter, you can easily adjust the hierarchy of spanners. For example, by specifying `level=0` for the last call of [tab_spanner()](GT.tab_spanner.md#great_tables.GT.tab_spanner), you can place that spanner at the bottom level (level `0`) instead of the top level (level `2`).


``` python
(
    GT(gtcars_mini)
    .tab_spanner(
        label="hp",
        columns=["hp", "hp_rpm"],
    )
    .tab_spanner(
        label="performance",
        columns=["hp", "hp_rpm", "trq", "trq_rpm"],
    )
    .tab_spanner(
        label="trq",
        columns=["trq", "trq_rpm"],
        level=0,
    )
)
```


<style>
#luaywczrqk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#luaywczrqk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#luaywczrqk p { margin: 0; padding: 0; }
 #luaywczrqk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #luaywczrqk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #luaywczrqk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #luaywczrqk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #luaywczrqk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #luaywczrqk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #luaywczrqk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #luaywczrqk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #luaywczrqk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #luaywczrqk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #luaywczrqk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #luaywczrqk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #luaywczrqk .gt_spanner_row { border-bottom-style: hidden; }
 #luaywczrqk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #luaywczrqk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #luaywczrqk .gt_from_md> :first-child { margin-top: 0; }
 #luaywczrqk .gt_from_md> :last-child { margin-bottom: 0; }
 #luaywczrqk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #luaywczrqk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #luaywczrqk .gt_indent_1 { text-indent: 5px; }
 #luaywczrqk .gt_indent_2 { text-indent: calc(5px * 2); }
 #luaywczrqk .gt_indent_3 { text-indent: calc(5px * 3); }
 #luaywczrqk .gt_indent_4 { text-indent: calc(5px * 4); }
 #luaywczrqk .gt_indent_5 { text-indent: calc(5px * 5); }
 #luaywczrqk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #luaywczrqk .gt_row_group_first td { border-top-width: 2px; }
 #luaywczrqk .gt_row_group_first th { border-top-width: 2px; }
 #luaywczrqk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #luaywczrqk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #luaywczrqk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #luaywczrqk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #luaywczrqk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #luaywczrqk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #luaywczrqk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #luaywczrqk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #luaywczrqk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #luaywczrqk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #luaywczrqk .gt_left { text-align: left; }
 #luaywczrqk .gt_center { text-align: center; }
 #luaywczrqk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #luaywczrqk .gt_font_normal { font-weight: normal; }
 #luaywczrqk .gt_font_bold { font-weight: bold; }
 #luaywczrqk .gt_font_italic { font-style: italic; }
 #luaywczrqk .gt_super { font-size: 65%; }
 #luaywczrqk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #luaywczrqk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #luaywczrqk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #luaywczrqk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #luaywczrqk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #luaywczrqk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col"><span> </span></th>
<th colspan="4" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
<th colspan="2" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="colgroup"><span> </span></th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th colspan="2" id="hp" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">hp</th>
<th colspan="2" id="trq" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">trq</th>
<th rowspan="2" id="mpg_c" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_c</th>
<th rowspan="2" id="mpg_h" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_h</th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="hp_rpm" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp_rpm</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="trq_rpm" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq_rpm</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">6250.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">5900.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">18.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">8000.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">3000.0</td>
<td class="gt_row gt_right">15.0</td>
<td class="gt_row gt_right">22.0</td>
</tr>
<tr>
<td class="gt_row gt_left">California</td>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">7500.0</td>
<td class="gt_row gt_right">557.0</td>
<td class="gt_row gt_right">4750.0</td>
<td class="gt_row gt_right">16.0</td>
<td class="gt_row gt_right">23.0</td>
</tr>
<tr>
<td class="gt_row gt_left">GTC4Lusso</td>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">8250.0</td>
<td class="gt_row gt_right">514.0</td>
<td class="gt_row gt_right">5750.0</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">FF</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">8000.0</td>
<td class="gt_row gt_right">504.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left">F12Berlinetta</td>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">8250.0</td>
<td class="gt_row gt_right">509.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left">LaFerrari</td>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">664.0</td>
<td class="gt_row gt_right">6750.0</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
</tbody>
</table>


We can also use Markdown formatting for the spanner label. In this example, we'll use `gt.md("*Performance*")` to make the label italicized.


``` python
(
    GT(gtcars_mini)
    .tab_spanner(
        label=md("*Performance*"),
        columns=["hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
    )
)
```


<style>
#qeatdmnpem table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qeatdmnpem thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qeatdmnpem p { margin: 0; padding: 0; }
 #qeatdmnpem .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qeatdmnpem .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qeatdmnpem .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qeatdmnpem .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qeatdmnpem .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qeatdmnpem .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeatdmnpem .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qeatdmnpem .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qeatdmnpem .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qeatdmnpem .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qeatdmnpem .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qeatdmnpem .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qeatdmnpem .gt_spanner_row { border-bottom-style: hidden; }
 #qeatdmnpem .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qeatdmnpem .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qeatdmnpem .gt_from_md> :first-child { margin-top: 0; }
 #qeatdmnpem .gt_from_md> :last-child { margin-bottom: 0; }
 #qeatdmnpem .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qeatdmnpem .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qeatdmnpem .gt_indent_1 { text-indent: 5px; }
 #qeatdmnpem .gt_indent_2 { text-indent: calc(5px * 2); }
 #qeatdmnpem .gt_indent_3 { text-indent: calc(5px * 3); }
 #qeatdmnpem .gt_indent_4 { text-indent: calc(5px * 4); }
 #qeatdmnpem .gt_indent_5 { text-indent: calc(5px * 5); }
 #qeatdmnpem .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qeatdmnpem .gt_row_group_first td { border-top-width: 2px; }
 #qeatdmnpem .gt_row_group_first th { border-top-width: 2px; }
 #qeatdmnpem .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qeatdmnpem .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeatdmnpem .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qeatdmnpem .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qeatdmnpem .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeatdmnpem .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qeatdmnpem .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qeatdmnpem .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qeatdmnpem .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeatdmnpem .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qeatdmnpem .gt_left { text-align: left; }
 #qeatdmnpem .gt_center { text-align: center; }
 #qeatdmnpem .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qeatdmnpem .gt_font_normal { font-weight: normal; }
 #qeatdmnpem .gt_font_bold { font-weight: bold; }
 #qeatdmnpem .gt_font_italic { font-style: italic; }
 #qeatdmnpem .gt_super { font-size: 65%; }
 #qeatdmnpem .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeatdmnpem .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qeatdmnpem .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeatdmnpem .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qeatdmnpem .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qeatdmnpem .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th colspan="6" id="<em>Performance</em>" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup"><em>Performance</em></th>
</tr>
<tr class="gt_col_headings">
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="hp_rpm" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp_rpm</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="trq_rpm" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq_rpm</th>
<th id="mpg_c" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_c</th>
<th id="mpg_h" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_h</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">6250.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">5900.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">18.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">13.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">8000.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">3000.0</td>
<td class="gt_row gt_right">15.0</td>
<td class="gt_row gt_right">22.0</td>
</tr>
<tr>
<td class="gt_row gt_left">California</td>
<td class="gt_row gt_right">553.0</td>
<td class="gt_row gt_right">7500.0</td>
<td class="gt_row gt_right">557.0</td>
<td class="gt_row gt_right">4750.0</td>
<td class="gt_row gt_right">16.0</td>
<td class="gt_row gt_right">23.0</td>
</tr>
<tr>
<td class="gt_row gt_left">GTC4Lusso</td>
<td class="gt_row gt_right">680.0</td>
<td class="gt_row gt_right">8250.0</td>
<td class="gt_row gt_right">514.0</td>
<td class="gt_row gt_right">5750.0</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left">FF</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">8000.0</td>
<td class="gt_row gt_right">504.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left">F12Berlinetta</td>
<td class="gt_row gt_right">731.0</td>
<td class="gt_row gt_right">8250.0</td>
<td class="gt_row gt_right">509.0</td>
<td class="gt_row gt_right">6000.0</td>
<td class="gt_row gt_right">11.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left">LaFerrari</td>
<td class="gt_row gt_right">949.0</td>
<td class="gt_row gt_right">9000.0</td>
<td class="gt_row gt_right">664.0</td>
<td class="gt_row gt_right">6750.0</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">16.0</td>
</tr>
</tbody>
</table>
