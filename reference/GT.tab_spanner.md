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
#hcagsrgtbg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hcagsrgtbg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hcagsrgtbg p { margin: 0; padding: 0; }
 #hcagsrgtbg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hcagsrgtbg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hcagsrgtbg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hcagsrgtbg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hcagsrgtbg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hcagsrgtbg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hcagsrgtbg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hcagsrgtbg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hcagsrgtbg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hcagsrgtbg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hcagsrgtbg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hcagsrgtbg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hcagsrgtbg .gt_spanner_row { border-bottom-style: hidden; }
 #hcagsrgtbg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hcagsrgtbg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hcagsrgtbg .gt_from_md> :first-child { margin-top: 0; }
 #hcagsrgtbg .gt_from_md> :last-child { margin-bottom: 0; }
 #hcagsrgtbg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hcagsrgtbg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hcagsrgtbg .gt_indent_1 { text-indent: 5px; }
 #hcagsrgtbg .gt_indent_2 { text-indent: calc(5px * 2); }
 #hcagsrgtbg .gt_indent_3 { text-indent: calc(5px * 3); }
 #hcagsrgtbg .gt_indent_4 { text-indent: calc(5px * 4); }
 #hcagsrgtbg .gt_indent_5 { text-indent: calc(5px * 5); }
 #hcagsrgtbg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hcagsrgtbg .gt_row_group_first td { border-top-width: 2px; }
 #hcagsrgtbg .gt_row_group_first th { border-top-width: 2px; }
 #hcagsrgtbg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hcagsrgtbg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hcagsrgtbg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hcagsrgtbg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hcagsrgtbg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hcagsrgtbg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hcagsrgtbg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hcagsrgtbg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hcagsrgtbg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hcagsrgtbg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hcagsrgtbg .gt_left { text-align: left; }
 #hcagsrgtbg .gt_center { text-align: center; }
 #hcagsrgtbg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hcagsrgtbg .gt_font_normal { font-weight: normal; }
 #hcagsrgtbg .gt_font_bold { font-weight: bold; }
 #hcagsrgtbg .gt_font_italic { font-style: italic; }
 #hcagsrgtbg .gt_super { font-size: 65%; }
 #hcagsrgtbg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hcagsrgtbg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hcagsrgtbg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hcagsrgtbg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hcagsrgtbg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hcagsrgtbg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ghhvdtqpqj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ghhvdtqpqj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ghhvdtqpqj p { margin: 0; padding: 0; }
 #ghhvdtqpqj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ghhvdtqpqj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ghhvdtqpqj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ghhvdtqpqj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ghhvdtqpqj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ghhvdtqpqj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghhvdtqpqj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ghhvdtqpqj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ghhvdtqpqj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ghhvdtqpqj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ghhvdtqpqj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ghhvdtqpqj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ghhvdtqpqj .gt_spanner_row { border-bottom-style: hidden; }
 #ghhvdtqpqj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ghhvdtqpqj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ghhvdtqpqj .gt_from_md> :first-child { margin-top: 0; }
 #ghhvdtqpqj .gt_from_md> :last-child { margin-bottom: 0; }
 #ghhvdtqpqj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ghhvdtqpqj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ghhvdtqpqj .gt_indent_1 { text-indent: 5px; }
 #ghhvdtqpqj .gt_indent_2 { text-indent: calc(5px * 2); }
 #ghhvdtqpqj .gt_indent_3 { text-indent: calc(5px * 3); }
 #ghhvdtqpqj .gt_indent_4 { text-indent: calc(5px * 4); }
 #ghhvdtqpqj .gt_indent_5 { text-indent: calc(5px * 5); }
 #ghhvdtqpqj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ghhvdtqpqj .gt_row_group_first td { border-top-width: 2px; }
 #ghhvdtqpqj .gt_row_group_first th { border-top-width: 2px; }
 #ghhvdtqpqj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ghhvdtqpqj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghhvdtqpqj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ghhvdtqpqj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ghhvdtqpqj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghhvdtqpqj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ghhvdtqpqj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ghhvdtqpqj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ghhvdtqpqj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghhvdtqpqj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ghhvdtqpqj .gt_left { text-align: left; }
 #ghhvdtqpqj .gt_center { text-align: center; }
 #ghhvdtqpqj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ghhvdtqpqj .gt_font_normal { font-weight: normal; }
 #ghhvdtqpqj .gt_font_bold { font-weight: bold; }
 #ghhvdtqpqj .gt_font_italic { font-style: italic; }
 #ghhvdtqpqj .gt_super { font-size: 65%; }
 #ghhvdtqpqj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghhvdtqpqj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ghhvdtqpqj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghhvdtqpqj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ghhvdtqpqj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ghhvdtqpqj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jmismlmzpr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jmismlmzpr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jmismlmzpr p { margin: 0; padding: 0; }
 #jmismlmzpr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jmismlmzpr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jmismlmzpr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jmismlmzpr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jmismlmzpr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jmismlmzpr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jmismlmzpr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jmismlmzpr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jmismlmzpr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jmismlmzpr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jmismlmzpr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jmismlmzpr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jmismlmzpr .gt_spanner_row { border-bottom-style: hidden; }
 #jmismlmzpr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jmismlmzpr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jmismlmzpr .gt_from_md> :first-child { margin-top: 0; }
 #jmismlmzpr .gt_from_md> :last-child { margin-bottom: 0; }
 #jmismlmzpr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jmismlmzpr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jmismlmzpr .gt_indent_1 { text-indent: 5px; }
 #jmismlmzpr .gt_indent_2 { text-indent: calc(5px * 2); }
 #jmismlmzpr .gt_indent_3 { text-indent: calc(5px * 3); }
 #jmismlmzpr .gt_indent_4 { text-indent: calc(5px * 4); }
 #jmismlmzpr .gt_indent_5 { text-indent: calc(5px * 5); }
 #jmismlmzpr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jmismlmzpr .gt_row_group_first td { border-top-width: 2px; }
 #jmismlmzpr .gt_row_group_first th { border-top-width: 2px; }
 #jmismlmzpr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jmismlmzpr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jmismlmzpr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jmismlmzpr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jmismlmzpr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jmismlmzpr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jmismlmzpr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jmismlmzpr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jmismlmzpr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jmismlmzpr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jmismlmzpr .gt_left { text-align: left; }
 #jmismlmzpr .gt_center { text-align: center; }
 #jmismlmzpr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jmismlmzpr .gt_font_normal { font-weight: normal; }
 #jmismlmzpr .gt_font_bold { font-weight: bold; }
 #jmismlmzpr .gt_font_italic { font-style: italic; }
 #jmismlmzpr .gt_super { font-size: 65%; }
 #jmismlmzpr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jmismlmzpr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jmismlmzpr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jmismlmzpr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jmismlmzpr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jmismlmzpr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vomdqasrfn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vomdqasrfn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vomdqasrfn p { margin: 0; padding: 0; }
 #vomdqasrfn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vomdqasrfn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vomdqasrfn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vomdqasrfn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vomdqasrfn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vomdqasrfn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vomdqasrfn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vomdqasrfn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vomdqasrfn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vomdqasrfn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vomdqasrfn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vomdqasrfn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vomdqasrfn .gt_spanner_row { border-bottom-style: hidden; }
 #vomdqasrfn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vomdqasrfn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vomdqasrfn .gt_from_md> :first-child { margin-top: 0; }
 #vomdqasrfn .gt_from_md> :last-child { margin-bottom: 0; }
 #vomdqasrfn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vomdqasrfn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vomdqasrfn .gt_indent_1 { text-indent: 5px; }
 #vomdqasrfn .gt_indent_2 { text-indent: calc(5px * 2); }
 #vomdqasrfn .gt_indent_3 { text-indent: calc(5px * 3); }
 #vomdqasrfn .gt_indent_4 { text-indent: calc(5px * 4); }
 #vomdqasrfn .gt_indent_5 { text-indent: calc(5px * 5); }
 #vomdqasrfn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vomdqasrfn .gt_row_group_first td { border-top-width: 2px; }
 #vomdqasrfn .gt_row_group_first th { border-top-width: 2px; }
 #vomdqasrfn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vomdqasrfn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vomdqasrfn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vomdqasrfn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vomdqasrfn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vomdqasrfn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vomdqasrfn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vomdqasrfn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vomdqasrfn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vomdqasrfn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vomdqasrfn .gt_left { text-align: left; }
 #vomdqasrfn .gt_center { text-align: center; }
 #vomdqasrfn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vomdqasrfn .gt_font_normal { font-weight: normal; }
 #vomdqasrfn .gt_font_bold { font-weight: bold; }
 #vomdqasrfn .gt_font_italic { font-style: italic; }
 #vomdqasrfn .gt_super { font-size: 65%; }
 #vomdqasrfn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vomdqasrfn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vomdqasrfn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vomdqasrfn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vomdqasrfn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vomdqasrfn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
