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
#eijngtkhgz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eijngtkhgz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eijngtkhgz p { margin: 0; padding: 0; }
 #eijngtkhgz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eijngtkhgz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eijngtkhgz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eijngtkhgz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eijngtkhgz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eijngtkhgz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eijngtkhgz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eijngtkhgz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eijngtkhgz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eijngtkhgz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eijngtkhgz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eijngtkhgz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eijngtkhgz .gt_spanner_row { border-bottom-style: hidden; }
 #eijngtkhgz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eijngtkhgz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eijngtkhgz .gt_from_md> :first-child { margin-top: 0; }
 #eijngtkhgz .gt_from_md> :last-child { margin-bottom: 0; }
 #eijngtkhgz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eijngtkhgz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eijngtkhgz .gt_indent_1 { text-indent: 5px; }
 #eijngtkhgz .gt_indent_2 { text-indent: calc(5px * 2); }
 #eijngtkhgz .gt_indent_3 { text-indent: calc(5px * 3); }
 #eijngtkhgz .gt_indent_4 { text-indent: calc(5px * 4); }
 #eijngtkhgz .gt_indent_5 { text-indent: calc(5px * 5); }
 #eijngtkhgz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eijngtkhgz .gt_row_group_first td { border-top-width: 2px; }
 #eijngtkhgz .gt_row_group_first th { border-top-width: 2px; }
 #eijngtkhgz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eijngtkhgz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eijngtkhgz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eijngtkhgz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eijngtkhgz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eijngtkhgz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eijngtkhgz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eijngtkhgz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eijngtkhgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eijngtkhgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eijngtkhgz .gt_left { text-align: left; }
 #eijngtkhgz .gt_center { text-align: center; }
 #eijngtkhgz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eijngtkhgz .gt_font_normal { font-weight: normal; }
 #eijngtkhgz .gt_font_bold { font-weight: bold; }
 #eijngtkhgz .gt_font_italic { font-style: italic; }
 #eijngtkhgz .gt_super { font-size: 65%; }
 #eijngtkhgz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eijngtkhgz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eijngtkhgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eijngtkhgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eijngtkhgz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eijngtkhgz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left" headers="model">GT</td>
<td class="gt_row gt_right" headers="performance hp">647.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">6250.0</td>
<td class="gt_row gt_right" headers="performance trq">550.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">5900.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">11.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">18.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Speciale</td>
<td class="gt_row gt_right" headers="performance hp">597.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq">398.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">13.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Spider</td>
<td class="gt_row gt_right" headers="performance hp">562.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq">398.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">13.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Italia</td>
<td class="gt_row gt_right" headers="performance hp">562.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq">398.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">13.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">488 GTB</td>
<td class="gt_row gt_right" headers="performance hp">661.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">8000.0</td>
<td class="gt_row gt_right" headers="performance trq">561.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">3000.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">15.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">22.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">California</td>
<td class="gt_row gt_right" headers="performance hp">553.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">7500.0</td>
<td class="gt_row gt_right" headers="performance trq">557.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">4750.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">16.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">23.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">GTC4Lusso</td>
<td class="gt_row gt_right" headers="performance hp">680.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">8250.0</td>
<td class="gt_row gt_right" headers="performance trq">514.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">5750.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">12.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">FF</td>
<td class="gt_row gt_right" headers="performance hp">652.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">8000.0</td>
<td class="gt_row gt_right" headers="performance trq">504.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">11.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">F12Berlinetta</td>
<td class="gt_row gt_right" headers="performance hp">731.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">8250.0</td>
<td class="gt_row gt_right" headers="performance trq">509.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">11.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">LaFerrari</td>
<td class="gt_row gt_right" headers="performance hp">949.0</td>
<td class="gt_row gt_right" headers="performance hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq">664.0</td>
<td class="gt_row gt_right" headers="performance trq_rpm">6750.0</td>
<td class="gt_row gt_right" headers="performance mpg_c">12.0</td>
<td class="gt_row gt_right" headers="performance mpg_h">16.0</td>
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
#ocfrjcocup table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ocfrjcocup thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ocfrjcocup p { margin: 0; padding: 0; }
 #ocfrjcocup .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ocfrjcocup .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ocfrjcocup .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ocfrjcocup .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ocfrjcocup .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ocfrjcocup .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ocfrjcocup .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ocfrjcocup .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ocfrjcocup .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ocfrjcocup .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ocfrjcocup .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ocfrjcocup .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ocfrjcocup .gt_spanner_row { border-bottom-style: hidden; }
 #ocfrjcocup .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ocfrjcocup .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ocfrjcocup .gt_from_md> :first-child { margin-top: 0; }
 #ocfrjcocup .gt_from_md> :last-child { margin-bottom: 0; }
 #ocfrjcocup .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ocfrjcocup .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ocfrjcocup .gt_indent_1 { text-indent: 5px; }
 #ocfrjcocup .gt_indent_2 { text-indent: calc(5px * 2); }
 #ocfrjcocup .gt_indent_3 { text-indent: calc(5px * 3); }
 #ocfrjcocup .gt_indent_4 { text-indent: calc(5px * 4); }
 #ocfrjcocup .gt_indent_5 { text-indent: calc(5px * 5); }
 #ocfrjcocup .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ocfrjcocup .gt_row_group_first td { border-top-width: 2px; }
 #ocfrjcocup .gt_row_group_first th { border-top-width: 2px; }
 #ocfrjcocup .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ocfrjcocup .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ocfrjcocup .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ocfrjcocup .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ocfrjcocup .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ocfrjcocup .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ocfrjcocup .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ocfrjcocup .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ocfrjcocup .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ocfrjcocup .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ocfrjcocup .gt_left { text-align: left; }
 #ocfrjcocup .gt_center { text-align: center; }
 #ocfrjcocup .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ocfrjcocup .gt_font_normal { font-weight: normal; }
 #ocfrjcocup .gt_font_bold { font-weight: bold; }
 #ocfrjcocup .gt_font_italic { font-style: italic; }
 #ocfrjcocup .gt_super { font-size: 65%; }
 #ocfrjcocup .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ocfrjcocup .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ocfrjcocup .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ocfrjcocup .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ocfrjcocup .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ocfrjcocup .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col"><span> </span></th>
<th colspan="6" id="performance" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th colspan="2" id="hp-2" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">hp</th>
<th colspan="2" id="trq-2" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">trq</th>
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
<td class="gt_row gt_left" headers="model">GT</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">647.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">6250.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">550.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">5900.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">11.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">18.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Speciale</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">597.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">398.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">13.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Spider</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">562.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">398.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">13.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Italia</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">562.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">398.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">13.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">488 GTB</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">661.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">8000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">561.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">3000.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">15.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">22.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">California</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">553.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">7500.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">557.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">4750.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">16.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">23.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">GTC4Lusso</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">680.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">8250.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">514.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">5750.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">12.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">FF</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">652.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">8000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">504.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">11.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">F12Berlinetta</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">731.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">8250.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">509.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">11.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">LaFerrari</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">949.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">664.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6750.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_c">12.0</td>
<td class="gt_row gt_right" headers="performance mpg mpg_h">16.0</td>
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
#kwfkfraxwv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kwfkfraxwv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kwfkfraxwv p { margin: 0; padding: 0; }
 #kwfkfraxwv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kwfkfraxwv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kwfkfraxwv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kwfkfraxwv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kwfkfraxwv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kwfkfraxwv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kwfkfraxwv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kwfkfraxwv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kwfkfraxwv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kwfkfraxwv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kwfkfraxwv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kwfkfraxwv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kwfkfraxwv .gt_spanner_row { border-bottom-style: hidden; }
 #kwfkfraxwv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kwfkfraxwv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kwfkfraxwv .gt_from_md> :first-child { margin-top: 0; }
 #kwfkfraxwv .gt_from_md> :last-child { margin-bottom: 0; }
 #kwfkfraxwv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kwfkfraxwv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kwfkfraxwv .gt_indent_1 { text-indent: 5px; }
 #kwfkfraxwv .gt_indent_2 { text-indent: calc(5px * 2); }
 #kwfkfraxwv .gt_indent_3 { text-indent: calc(5px * 3); }
 #kwfkfraxwv .gt_indent_4 { text-indent: calc(5px * 4); }
 #kwfkfraxwv .gt_indent_5 { text-indent: calc(5px * 5); }
 #kwfkfraxwv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kwfkfraxwv .gt_row_group_first td { border-top-width: 2px; }
 #kwfkfraxwv .gt_row_group_first th { border-top-width: 2px; }
 #kwfkfraxwv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kwfkfraxwv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kwfkfraxwv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kwfkfraxwv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kwfkfraxwv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kwfkfraxwv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kwfkfraxwv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kwfkfraxwv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kwfkfraxwv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kwfkfraxwv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kwfkfraxwv .gt_left { text-align: left; }
 #kwfkfraxwv .gt_center { text-align: center; }
 #kwfkfraxwv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kwfkfraxwv .gt_font_normal { font-weight: normal; }
 #kwfkfraxwv .gt_font_bold { font-weight: bold; }
 #kwfkfraxwv .gt_font_italic { font-style: italic; }
 #kwfkfraxwv .gt_super { font-size: 65%; }
 #kwfkfraxwv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kwfkfraxwv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kwfkfraxwv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kwfkfraxwv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kwfkfraxwv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kwfkfraxwv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col"><span> </span></th>
<th colspan="4" id="performance" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="colgroup">performance</th>
<th colspan="2" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="colgroup"><span> </span></th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th colspan="2" id="hp-2" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">hp</th>
<th colspan="2" id="trq-2" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">trq</th>
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
<td class="gt_row gt_left" headers="model">GT</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">647.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">6250.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">550.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">5900.0</td>
<td class="gt_row gt_right" headers="mpg_c">11.0</td>
<td class="gt_row gt_right" headers="mpg_h">18.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Speciale</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">597.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">398.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="mpg_c">13.0</td>
<td class="gt_row gt_right" headers="mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Spider</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">562.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">398.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="mpg_c">13.0</td>
<td class="gt_row gt_right" headers="mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Italia</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">562.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">398.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="mpg_c">13.0</td>
<td class="gt_row gt_right" headers="mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">488 GTB</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">661.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">8000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">561.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">3000.0</td>
<td class="gt_row gt_right" headers="mpg_c">15.0</td>
<td class="gt_row gt_right" headers="mpg_h">22.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">California</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">553.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">7500.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">557.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">4750.0</td>
<td class="gt_row gt_right" headers="mpg_c">16.0</td>
<td class="gt_row gt_right" headers="mpg_h">23.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">GTC4Lusso</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">680.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">8250.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">514.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">5750.0</td>
<td class="gt_row gt_right" headers="mpg_c">12.0</td>
<td class="gt_row gt_right" headers="mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">FF</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">652.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">8000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">504.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="mpg_c">11.0</td>
<td class="gt_row gt_right" headers="mpg_h">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">F12Berlinetta</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">731.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">8250.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">509.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="mpg_c">11.0</td>
<td class="gt_row gt_right" headers="mpg_h">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">LaFerrari</td>
<td class="gt_row gt_right" headers="performance hp-2 hp">949.0</td>
<td class="gt_row gt_right" headers="performance hp-2 hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq">664.0</td>
<td class="gt_row gt_right" headers="performance trq-2 trq_rpm">6750.0</td>
<td class="gt_row gt_right" headers="mpg_c">12.0</td>
<td class="gt_row gt_right" headers="mpg_h">16.0</td>
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
#ixunbxvuzz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ixunbxvuzz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ixunbxvuzz p { margin: 0; padding: 0; }
 #ixunbxvuzz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ixunbxvuzz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ixunbxvuzz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ixunbxvuzz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ixunbxvuzz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ixunbxvuzz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixunbxvuzz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ixunbxvuzz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ixunbxvuzz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ixunbxvuzz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ixunbxvuzz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ixunbxvuzz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ixunbxvuzz .gt_spanner_row { border-bottom-style: hidden; }
 #ixunbxvuzz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ixunbxvuzz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ixunbxvuzz .gt_from_md> :first-child { margin-top: 0; }
 #ixunbxvuzz .gt_from_md> :last-child { margin-bottom: 0; }
 #ixunbxvuzz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ixunbxvuzz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ixunbxvuzz .gt_indent_1 { text-indent: 5px; }
 #ixunbxvuzz .gt_indent_2 { text-indent: calc(5px * 2); }
 #ixunbxvuzz .gt_indent_3 { text-indent: calc(5px * 3); }
 #ixunbxvuzz .gt_indent_4 { text-indent: calc(5px * 4); }
 #ixunbxvuzz .gt_indent_5 { text-indent: calc(5px * 5); }
 #ixunbxvuzz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ixunbxvuzz .gt_row_group_first td { border-top-width: 2px; }
 #ixunbxvuzz .gt_row_group_first th { border-top-width: 2px; }
 #ixunbxvuzz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ixunbxvuzz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixunbxvuzz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ixunbxvuzz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ixunbxvuzz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixunbxvuzz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ixunbxvuzz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ixunbxvuzz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ixunbxvuzz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixunbxvuzz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ixunbxvuzz .gt_left { text-align: left; }
 #ixunbxvuzz .gt_center { text-align: center; }
 #ixunbxvuzz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ixunbxvuzz .gt_font_normal { font-weight: normal; }
 #ixunbxvuzz .gt_font_bold { font-weight: bold; }
 #ixunbxvuzz .gt_font_italic { font-style: italic; }
 #ixunbxvuzz .gt_super { font-size: 65%; }
 #ixunbxvuzz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixunbxvuzz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ixunbxvuzz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixunbxvuzz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ixunbxvuzz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ixunbxvuzz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th colspan="6" id="Performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup"><em>Performance</em></th>
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
<td class="gt_row gt_left" headers="model">GT</td>
<td class="gt_row gt_right" headers="Performance hp">647.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">6250.0</td>
<td class="gt_row gt_right" headers="Performance trq">550.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">5900.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">11.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">18.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Speciale</td>
<td class="gt_row gt_right" headers="Performance hp">597.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="Performance trq">398.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">13.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Spider</td>
<td class="gt_row gt_right" headers="Performance hp">562.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="Performance trq">398.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">13.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">458 Italia</td>
<td class="gt_row gt_right" headers="Performance hp">562.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="Performance trq">398.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">13.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">488 GTB</td>
<td class="gt_row gt_right" headers="Performance hp">661.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">8000.0</td>
<td class="gt_row gt_right" headers="Performance trq">561.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">3000.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">15.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">22.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">California</td>
<td class="gt_row gt_right" headers="Performance hp">553.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">7500.0</td>
<td class="gt_row gt_right" headers="Performance trq">557.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">4750.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">16.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">23.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">GTC4Lusso</td>
<td class="gt_row gt_right" headers="Performance hp">680.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">8250.0</td>
<td class="gt_row gt_right" headers="Performance trq">514.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">5750.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">12.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">17.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">FF</td>
<td class="gt_row gt_right" headers="Performance hp">652.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">8000.0</td>
<td class="gt_row gt_right" headers="Performance trq">504.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">11.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">F12Berlinetta</td>
<td class="gt_row gt_right" headers="Performance hp">731.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">8250.0</td>
<td class="gt_row gt_right" headers="Performance trq">509.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">6000.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">11.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">16.0</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="model">LaFerrari</td>
<td class="gt_row gt_right" headers="Performance hp">949.0</td>
<td class="gt_row gt_right" headers="Performance hp_rpm">9000.0</td>
<td class="gt_row gt_right" headers="Performance trq">664.0</td>
<td class="gt_row gt_right" headers="Performance trq_rpm">6750.0</td>
<td class="gt_row gt_right" headers="Performance mpg_c">12.0</td>
<td class="gt_row gt_right" headers="Performance mpg_h">16.0</td>
</tr>
</tbody>
</table>
