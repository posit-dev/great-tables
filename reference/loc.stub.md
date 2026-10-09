# loc.stub


Target the table stub.


Usage

``` python
loc.stub(
    rows=None,
    columns=None,
)
```


With [loc.stub()](loc.stub.md#great_tables.loc.stub) we can target the cells containing the row labels, which reside in the table stub. This is useful for applying custom styling with the <a href="../reference/GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> method. That method has a `locations=` argument and this class should be used there to perform the targeting.


## Parameters


`rows: RowSelectExpr = None`  
The rows to target within the stub. Can either be a single row name or a series of row names provided in a list. If no rows are specified, all rows are targeted. With a hierarchical stub and no `columns=`, row names are matched against the values in every stub column, so the name of an outer level targets all of the rows under it.

`columns: str | list[str] | None = None`  
For a hierarchical stub (where `rowname_col=` is a list of columns), the stub column(s) to target, as a column name or a list of names. By default, all of the stub columns are targeted. When `columns=` is given, row names in `rows=` are matched against the values in those columns (rather than against the row labels), and a cell that is merged across several rows is targeted if any of its rows are.


## Returns


`LocStub`  
A LocStub object, which is used for a `locations=` argument if specifying the table's stub.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style the entire table stub (the row labels) by using `locations=loc.stub()` within <a href="../reference/GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>.


``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(
        gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
        rowname_col="model",
        groupname_col="mfr"
    )
    .tab_stubhead(label="car")
    .tab_style(
        style=[
            style.text(color="crimson", weight="bold"),
            style.fill(color="lightgray")
        ],
        locations=loc.stub()
    )
    .fmt_integer(columns=["hp", "trq"])
    .fmt_currency(columns="msrp", decimals=0)
)
```


<style>
#tgxdzfxfut table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tgxdzfxfut thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tgxdzfxfut p { margin: 0; padding: 0; }
 #tgxdzfxfut .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tgxdzfxfut .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tgxdzfxfut .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tgxdzfxfut .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tgxdzfxfut .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tgxdzfxfut .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgxdzfxfut .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tgxdzfxfut .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tgxdzfxfut .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tgxdzfxfut .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tgxdzfxfut .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tgxdzfxfut .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tgxdzfxfut .gt_spanner_row { border-bottom-style: hidden; }
 #tgxdzfxfut .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tgxdzfxfut .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tgxdzfxfut .gt_from_md> :first-child { margin-top: 0; }
 #tgxdzfxfut .gt_from_md> :last-child { margin-bottom: 0; }
 #tgxdzfxfut .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tgxdzfxfut .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tgxdzfxfut .gt_indent_1 { text-indent: 5px; }
 #tgxdzfxfut .gt_indent_2 { text-indent: calc(5px * 2); }
 #tgxdzfxfut .gt_indent_3 { text-indent: calc(5px * 3); }
 #tgxdzfxfut .gt_indent_4 { text-indent: calc(5px * 4); }
 #tgxdzfxfut .gt_indent_5 { text-indent: calc(5px * 5); }
 #tgxdzfxfut .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tgxdzfxfut .gt_row_group_first td { border-top-width: 2px; }
 #tgxdzfxfut .gt_row_group_first th { border-top-width: 2px; }
 #tgxdzfxfut .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tgxdzfxfut .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgxdzfxfut .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tgxdzfxfut .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tgxdzfxfut .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgxdzfxfut .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tgxdzfxfut .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tgxdzfxfut .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tgxdzfxfut .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgxdzfxfut .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tgxdzfxfut .gt_left { text-align: left; }
 #tgxdzfxfut .gt_center { text-align: center; }
 #tgxdzfxfut .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tgxdzfxfut .gt_font_normal { font-weight: normal; }
 #tgxdzfxfut .gt_font_bold { font-weight: bold; }
 #tgxdzfxfut .gt_font_italic { font-style: italic; }
 #tgxdzfxfut .gt_super { font-size: 65%; }
 #tgxdzfxfut .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgxdzfxfut .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tgxdzfxfut .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgxdzfxfut .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tgxdzfxfut .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tgxdzfxfut .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th id="car" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">car</th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading" scope="colgroup">Ford</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray" scope="row">GT</td>
<td class="gt_row gt_right">647</td>
<td class="gt_row gt_right">550</td>
<td class="gt_row gt_right">$447,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">Ferrari</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray" scope="row">458 Speciale</td>
<td class="gt_row gt_right">597</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$291,744</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray" scope="row">458 Spider</td>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$263,553</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray" scope="row">458 Italia</td>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$233,509</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray" scope="row">488 GTB</td>
<td class="gt_row gt_right">661</td>
<td class="gt_row gt_right">561</td>
<td class="gt_row gt_right">$245,400</td>
</tr>
</tbody>
</table>


With a hierarchical stub, `columns=` targets a single level. Here, the manufacturer cells for the Ferrari rows are highlighted, leaving the model names as they are.


``` python
(
    GT(gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(6), rowname_col=["mfr", "model"])
    .tab_style(
        style=style.fill(color="lightgray"),
        locations=loc.stub(rows="Ferrari", columns="mfr")
    )
    .fmt_integer(columns=["hp", "trq"])
    .fmt_currency(columns="msrp", decimals=0)
)
```


<style>
#pcdnbheqgk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pcdnbheqgk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pcdnbheqgk p { margin: 0; padding: 0; }
 #pcdnbheqgk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pcdnbheqgk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pcdnbheqgk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pcdnbheqgk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pcdnbheqgk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pcdnbheqgk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pcdnbheqgk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pcdnbheqgk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pcdnbheqgk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pcdnbheqgk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pcdnbheqgk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pcdnbheqgk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pcdnbheqgk .gt_spanner_row { border-bottom-style: hidden; }
 #pcdnbheqgk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pcdnbheqgk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pcdnbheqgk .gt_from_md> :first-child { margin-top: 0; }
 #pcdnbheqgk .gt_from_md> :last-child { margin-bottom: 0; }
 #pcdnbheqgk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pcdnbheqgk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pcdnbheqgk .gt_indent_1 { text-indent: 5px; }
 #pcdnbheqgk .gt_indent_2 { text-indent: calc(5px * 2); }
 #pcdnbheqgk .gt_indent_3 { text-indent: calc(5px * 3); }
 #pcdnbheqgk .gt_indent_4 { text-indent: calc(5px * 4); }
 #pcdnbheqgk .gt_indent_5 { text-indent: calc(5px * 5); }
 #pcdnbheqgk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pcdnbheqgk .gt_row_group_first td { border-top-width: 2px; }
 #pcdnbheqgk .gt_row_group_first th { border-top-width: 2px; }
 #pcdnbheqgk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pcdnbheqgk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pcdnbheqgk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pcdnbheqgk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pcdnbheqgk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pcdnbheqgk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pcdnbheqgk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pcdnbheqgk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pcdnbheqgk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pcdnbheqgk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pcdnbheqgk .gt_left { text-align: left; }
 #pcdnbheqgk .gt_center { text-align: center; }
 #pcdnbheqgk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pcdnbheqgk .gt_font_normal { font-weight: normal; }
 #pcdnbheqgk .gt_font_bold { font-weight: bold; }
 #pcdnbheqgk .gt_font_italic { font-style: italic; }
 #pcdnbheqgk .gt_super { font-size: 65%; }
 #pcdnbheqgk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pcdnbheqgk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pcdnbheqgk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pcdnbheqgk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pcdnbheqgk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pcdnbheqgk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th colspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="colgroup"></th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" scope="row">Ford</th>
<th class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_right">647</td>
<td class="gt_row gt_right">550</td>
<td class="gt_row gt_right">$447,000</td>
</tr>
<tr>
<th rowspan="5" class="gt_row gt_left gt_stub" style="background-color: lightgray" scope="rowgroup">Ferrari</th>
<th class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_right">597</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$291,744</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$263,553</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$233,509</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_right">661</td>
<td class="gt_row gt_right">561</td>
<td class="gt_row gt_right">$245,400</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" scope="row">California</th>
<td class="gt_row gt_right">553</td>
<td class="gt_row gt_right">557</td>
<td class="gt_row gt_right">$198,973</td>
</tr>
</tbody>
</table>
