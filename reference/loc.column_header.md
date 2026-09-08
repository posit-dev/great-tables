# loc.column_header


Target column spanners and column labels.


Usage

``` python
loc.column_header()
```


With [loc.column_header()](loc.column_header.md#great_tables.loc.column_header), we can target the column header which contains all of the column labels and any spanner labels that are present. This is useful for applying custom styling with the <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> method. That method has a `locations=` argument and this class should be used there to perform the targeting.


## Returns


`LocColumnHeader`  
A LocColumnHeader object, which is used for a `locations=` argument if specifying the column header of the table.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We create spanner labels through use of the <a href="GT.tab_spanner.html#great_tables.GT.tab_spanner" class="gdls-link"><code>tab_spanner()</code></a> method; this gives us a column header with a mix of column labels and spanner labels. We will style the entire column header at once by using `locations=loc.column_header()` within <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>.


``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5))
    .tab_spanner(
        label="performance",
        columns=["hp", "trq"]
    )
    .tab_spanner(
        label="make and model",
        columns=["mfr", "model"]
    )
    .tab_style(
        style=[
            style.text(color="white", weight="bold"),
            style.fill(color="steelblue")
        ],
        locations=loc.column_header()
    )
    .fmt_integer(columns=["hp", "trq"])
    .fmt_currency(columns="msrp", decimals=0)
)
```


<style>
#qvrojwvybd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qvrojwvybd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qvrojwvybd p { margin: 0; padding: 0; }
 #qvrojwvybd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qvrojwvybd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qvrojwvybd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qvrojwvybd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qvrojwvybd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qvrojwvybd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvrojwvybd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qvrojwvybd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qvrojwvybd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qvrojwvybd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qvrojwvybd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qvrojwvybd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qvrojwvybd .gt_spanner_row { border-bottom-style: hidden; }
 #qvrojwvybd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qvrojwvybd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qvrojwvybd .gt_from_md> :first-child { margin-top: 0; }
 #qvrojwvybd .gt_from_md> :last-child { margin-bottom: 0; }
 #qvrojwvybd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qvrojwvybd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qvrojwvybd .gt_indent_1 { text-indent: 5px; }
 #qvrojwvybd .gt_indent_2 { text-indent: calc(5px * 2); }
 #qvrojwvybd .gt_indent_3 { text-indent: calc(5px * 3); }
 #qvrojwvybd .gt_indent_4 { text-indent: calc(5px * 4); }
 #qvrojwvybd .gt_indent_5 { text-indent: calc(5px * 5); }
 #qvrojwvybd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qvrojwvybd .gt_row_group_first td { border-top-width: 2px; }
 #qvrojwvybd .gt_row_group_first th { border-top-width: 2px; }
 #qvrojwvybd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qvrojwvybd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvrojwvybd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qvrojwvybd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qvrojwvybd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvrojwvybd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qvrojwvybd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qvrojwvybd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qvrojwvybd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvrojwvybd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qvrojwvybd .gt_left { text-align: left; }
 #qvrojwvybd .gt_center { text-align: center; }
 #qvrojwvybd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qvrojwvybd .gt_font_normal { font-weight: normal; }
 #qvrojwvybd .gt_font_bold { font-weight: bold; }
 #qvrojwvybd .gt_font_italic { font-style: italic; }
 #qvrojwvybd .gt_super { font-size: 65%; }
 #qvrojwvybd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvrojwvybd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qvrojwvybd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvrojwvybd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qvrojwvybd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qvrojwvybd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="2" id="make-and-model" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="color: white; font-weight: bold; background-color: steelblue" scope="colgroup">make and model</th>
<th colspan="2" id="performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="color: white; font-weight: bold; background-color: steelblue" scope="colgroup">performance</th>
<th rowspan="2" id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" style="color: white; font-weight: bold; background-color: steelblue" scope="col">msrp</th>
</tr>
<tr class="gt_col_headings">
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" style="color: white; font-weight: bold; background-color: steelblue" scope="col">mfr</th>
<th id="model" class="gt_col_heading gt_columns_bottom_border gt_left" style="color: white; font-weight: bold; background-color: steelblue" scope="col">model</th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" style="color: white; font-weight: bold; background-color: steelblue" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" style="color: white; font-weight: bold; background-color: steelblue" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">647</td>
<td class="gt_row gt_right">550</td>
<td class="gt_row gt_right">$447,000</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">597</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$291,744</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$263,553</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$233,509</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">661</td>
<td class="gt_row gt_right">561</td>
<td class="gt_row gt_right">$245,400</td>
</tr>
</tbody>
</table>
