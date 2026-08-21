# GT.rm_spanners()


Remove column spanners.


Usage

``` python
GT.rm_spanners(
    spanners=None,
    levels=None,
)
```


Column spanners are added with the <a href="GT.tab_spanner.html#great_tables.GT.tab_spanner" class="gdls-link"><code>tab_spanner()</code></a> method. The [rm_spanners()](GT.rm_spanners.md#great_tables.GT.rm_spanners) method allows for the removal of spanners while leaving the columns themselves intact. We can either target spanners by their ID values (with the `spanners=` argument) or by their levels (with the `levels=` argument).


## Parameters


`spanners: str | list[str] | None = None`  
The spanners to remove. Supplied as a single spanner ID or a list of spanner ID values. If `None` (the default), then all spanners will be considered for removal (subject to any constraint imposed by `levels=`).

`levels: int | list[int] | None = None`  
The spanner levels to remove, supplied as a single level or a list of levels. Spanners are placed on levels starting from `0` (the level closest to the column labels). If `None` (the default), then no levels-based constraint is applied. When supplied, only spanners residing on the specified levels (and also matching `spanners=`) are removed.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, let's create a table with two spanners. We then remove the spanner with the ID `"performance"` while leaving the other spanner in place.


``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "hp", "trq", "mpg_c"]].head(5)

(
    GT(gtcars_mini)
    .tab_spanner(label="performance", columns=["hp", "trq"])
    .tab_spanner(label="economy", columns=["mpg_c"])
    .rm_spanners(spanners="performance")
)
```


<style>
#zcejjrjphv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zcejjrjphv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zcejjrjphv p { margin: 0; padding: 0; }
 #zcejjrjphv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zcejjrjphv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zcejjrjphv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zcejjrjphv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zcejjrjphv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zcejjrjphv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zcejjrjphv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zcejjrjphv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zcejjrjphv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zcejjrjphv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zcejjrjphv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zcejjrjphv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zcejjrjphv .gt_spanner_row { border-bottom-style: hidden; }
 #zcejjrjphv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zcejjrjphv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zcejjrjphv .gt_from_md> :first-child { margin-top: 0; }
 #zcejjrjphv .gt_from_md> :last-child { margin-bottom: 0; }
 #zcejjrjphv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zcejjrjphv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zcejjrjphv .gt_indent_1 { text-indent: 5px; }
 #zcejjrjphv .gt_indent_2 { text-indent: calc(5px * 2); }
 #zcejjrjphv .gt_indent_3 { text-indent: calc(5px * 3); }
 #zcejjrjphv .gt_indent_4 { text-indent: calc(5px * 4); }
 #zcejjrjphv .gt_indent_5 { text-indent: calc(5px * 5); }
 #zcejjrjphv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zcejjrjphv .gt_row_group_first td { border-top-width: 2px; }
 #zcejjrjphv .gt_row_group_first th { border-top-width: 2px; }
 #zcejjrjphv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zcejjrjphv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zcejjrjphv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zcejjrjphv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zcejjrjphv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zcejjrjphv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zcejjrjphv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zcejjrjphv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zcejjrjphv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zcejjrjphv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zcejjrjphv .gt_left { text-align: left; }
 #zcejjrjphv .gt_center { text-align: center; }
 #zcejjrjphv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zcejjrjphv .gt_font_normal { font-weight: normal; }
 #zcejjrjphv .gt_font_bold { font-weight: bold; }
 #zcejjrjphv .gt_font_italic { font-style: italic; }
 #zcejjrjphv .gt_super { font-size: 65%; }
 #zcejjrjphv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zcejjrjphv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zcejjrjphv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zcejjrjphv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zcejjrjphv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zcejjrjphv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th rowspan="2" id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th rowspan="2" id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th rowspan="2" id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="economy" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="col">economy</th>
</tr>
<tr class="gt_col_headings">
<th id="mpg_c" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_c</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">11.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">13.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">13.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">13.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">15.0</td>
</tr>
</tbody>
</table>


## See Also

<a href="GT.tab_spanner.html#great_tables.GT.tab_spanner" class="gdls-link"><code>tab_spanner()</code></a> to add a spanner to a table.
