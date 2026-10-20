# GT.tab_style_body()


Apply styles to body cells based on their data values.


Usage

``` python
GT.tab_style_body(
    style,
    columns=None,
    rows=None,
    values=None,
    pattern=None,
    fn=None,
    targets="cell",
    extents="body",
)
```


With [tab_style_body()](GT.tab_style_body.md#great_tables.GT.tab_style_body), we can target body cells for styling based on the *values* they contain rather than their positions. Three matching strategies are available: exact value matching (`values=`), regular-expression matching (`pattern=`), and arbitrary predicate functions (`fn=`). When more than one of these is supplied, the precedence is `fn` \> `pattern` \> `values`.

After matching cells are identified the styling can optionally be expanded to entire rows or columns via `targets=`, and projected into the stub region via `extents=`.


## Parameters


`style: CellStyle | list[CellStyle]`  
The styles to apply to matched cells. Use the [style.text()](style.text.md#great_tables.style.text), [style.fill()](style.fill.md#great_tables.style.fill), [style.borders()](style.borders.md#great_tables.style.borders), and [style.css()](style.css.md#great_tables.style.css) classes to define styles.

`columns: SelectExpr = None`  
The columns to consider for matching. Can be a single column name, a list of column names, or a column selection expression. By default, all columns in the body are considered.

`rows: RowSelectExpr = None`  
The rows to consider for matching. Can be a single row index or name, a list of row indices or names, or a row selection expression. By default, all rows are considered.

`values: list[Any] | None = None`  
A list of specific values to match against. A body cell whose value equals any element in this list will be styled. Ignored when `pattern` or `fn` is supplied.

`pattern: str | None = None`  
A regex pattern string. Body cells whose *string representation* matches this pattern will be styled. Takes precedence over `values`; ignored when `fn` is supplied.

`fn: Callable[[Any], bool] | None = None`  
A function that receives a cell's raw value and returns `True` (style the cell) or `False` (skip). This is the most flexible matching option and takes the highest precedence.

`targets: Literal[``"cell", `<span class="st">`"row"``, ``"column"``] | list[Literal[``"cell"``, ``"row"``, ``"column"``]]`</span>` = ``"cell"`  
How to expand matched cells. `"cell"` (the default) styles only matched cells; `"row"` styles the entire row of each match; `"column"` styles the entire column. A list can combine these (e.g., `["cell", "row"]`).

`extents: Literal[``"body", `<span class="st">`"stub"``] | list[Literal[``"body"``, ``"stub"``]]`</span>` = ``"body"`  
Where styling is applied. `"body"` (the default) styles only body cells; `"stub"` also projects the styling into the stub (row labels). A list can combine these (e.g., `["body", "stub"]`).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Use [tab_style_body()](GT.tab_style_body.md#great_tables.GT.tab_style_body) to highlight specific values in a table. Here we color the background of cells that contain the values `49.95` or `33.33`.


``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=style.fill(color="orange"),
        values=[49.95, 33.33],
    )
)
```


<style>
#rlibywuxoz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rlibywuxoz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rlibywuxoz p { margin: 0; padding: 0; }
 #rlibywuxoz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rlibywuxoz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rlibywuxoz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rlibywuxoz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rlibywuxoz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rlibywuxoz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rlibywuxoz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rlibywuxoz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rlibywuxoz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rlibywuxoz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rlibywuxoz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rlibywuxoz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rlibywuxoz .gt_spanner_row { border-bottom-style: hidden; }
 #rlibywuxoz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rlibywuxoz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rlibywuxoz .gt_from_md> :first-child { margin-top: 0; }
 #rlibywuxoz .gt_from_md> :last-child { margin-bottom: 0; }
 #rlibywuxoz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rlibywuxoz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rlibywuxoz .gt_indent_1 { text-indent: 5px; }
 #rlibywuxoz .gt_indent_2 { text-indent: calc(5px * 2); }
 #rlibywuxoz .gt_indent_3 { text-indent: calc(5px * 3); }
 #rlibywuxoz .gt_indent_4 { text-indent: calc(5px * 4); }
 #rlibywuxoz .gt_indent_5 { text-indent: calc(5px * 5); }
 #rlibywuxoz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rlibywuxoz .gt_row_group_first td { border-top-width: 2px; }
 #rlibywuxoz .gt_row_group_first th { border-top-width: 2px; }
 #rlibywuxoz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rlibywuxoz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rlibywuxoz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rlibywuxoz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rlibywuxoz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rlibywuxoz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rlibywuxoz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rlibywuxoz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rlibywuxoz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rlibywuxoz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rlibywuxoz .gt_left { text-align: left; }
 #rlibywuxoz .gt_center { text-align: center; }
 #rlibywuxoz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rlibywuxoz .gt_font_normal { font-weight: normal; }
 #rlibywuxoz .gt_font_bold { font-weight: bold; }
 #rlibywuxoz .gt_font_italic { font-style: italic; }
 #rlibywuxoz .gt_super { font-size: 65%; }
 #rlibywuxoz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rlibywuxoz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rlibywuxoz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rlibywuxoz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rlibywuxoz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rlibywuxoz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" style="background-color: orange" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: orange" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_left" headers="grp_b stub-6 fctr">six</td>
<td class="gt_row gt_right" headers="grp_b stub-6 date">2015-06-15</td>
<td class="gt_row gt_right" headers="grp_b stub-6 time">None</td>
<td class="gt_row gt_right" headers="grp_b stub-6 datetime">2018-06-06 16:11</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_left" headers="grp_b stub-7 fctr">seven</td>
<td class="gt_row gt_right" headers="grp_b stub-7 date">None</td>
<td class="gt_row gt_right" headers="grp_b stub-7 time">19:10</td>
<td class="gt_row gt_right" headers="grp_b stub-7 datetime">2018-07-07 05:22</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_left" headers="grp_b stub-8 fctr">eight</td>
<td class="gt_row gt_right" headers="grp_b stub-8 date">2015-08-15</td>
<td class="gt_row gt_right" headers="grp_b stub-8 time">20:20</td>
<td class="gt_row gt_right" headers="grp_b stub-8 datetime">None</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


Apply multiple styles to matched cells using a list of style objects.


``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=[
            style.text(color="white", weight="bold"),
            style.fill(color="red"),
        ],
        values=[49.95, 33.33],
    )
)
```


<style>
#ycecsriutz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ycecsriutz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ycecsriutz p { margin: 0; padding: 0; }
 #ycecsriutz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ycecsriutz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ycecsriutz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ycecsriutz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ycecsriutz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ycecsriutz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ycecsriutz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ycecsriutz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ycecsriutz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ycecsriutz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ycecsriutz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ycecsriutz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ycecsriutz .gt_spanner_row { border-bottom-style: hidden; }
 #ycecsriutz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ycecsriutz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ycecsriutz .gt_from_md> :first-child { margin-top: 0; }
 #ycecsriutz .gt_from_md> :last-child { margin-bottom: 0; }
 #ycecsriutz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ycecsriutz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ycecsriutz .gt_indent_1 { text-indent: 5px; }
 #ycecsriutz .gt_indent_2 { text-indent: calc(5px * 2); }
 #ycecsriutz .gt_indent_3 { text-indent: calc(5px * 3); }
 #ycecsriutz .gt_indent_4 { text-indent: calc(5px * 4); }
 #ycecsriutz .gt_indent_5 { text-indent: calc(5px * 5); }
 #ycecsriutz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ycecsriutz .gt_row_group_first td { border-top-width: 2px; }
 #ycecsriutz .gt_row_group_first th { border-top-width: 2px; }
 #ycecsriutz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ycecsriutz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ycecsriutz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ycecsriutz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ycecsriutz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ycecsriutz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ycecsriutz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ycecsriutz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ycecsriutz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ycecsriutz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ycecsriutz .gt_left { text-align: left; }
 #ycecsriutz .gt_center { text-align: center; }
 #ycecsriutz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ycecsriutz .gt_font_normal { font-weight: normal; }
 #ycecsriutz .gt_font_bold { font-weight: bold; }
 #ycecsriutz .gt_font_italic { font-style: italic; }
 #ycecsriutz .gt_super { font-size: 65%; }
 #ycecsriutz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ycecsriutz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ycecsriutz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ycecsriutz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ycecsriutz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ycecsriutz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" style="color: white; font-weight: bold; background-color: red" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="color: white; font-weight: bold; background-color: red" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_left" headers="grp_b stub-6 fctr">six</td>
<td class="gt_row gt_right" headers="grp_b stub-6 date">2015-06-15</td>
<td class="gt_row gt_right" headers="grp_b stub-6 time">None</td>
<td class="gt_row gt_right" headers="grp_b stub-6 datetime">2018-06-06 16:11</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_left" headers="grp_b stub-7 fctr">seven</td>
<td class="gt_row gt_right" headers="grp_b stub-7 date">None</td>
<td class="gt_row gt_right" headers="grp_b stub-7 time">19:10</td>
<td class="gt_row gt_right" headers="grp_b stub-7 datetime">2018-07-07 05:22</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_left" headers="grp_b stub-8 fctr">eight</td>
<td class="gt_row gt_right" headers="grp_b stub-8 date">2015-08-15</td>
<td class="gt_row gt_right" headers="grp_b stub-8 time">20:20</td>
<td class="gt_row gt_right" headers="grp_b stub-8 datetime">None</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


A predicate function (`fn=`) provides the most flexible matching. Below we style all numeric cells with a value between 0 and 50.


``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=style.fill(color="pink"),
        fn=lambda x: isinstance(x, (int, float)) and 0 <= x < 50,
    )
)
```


<style>
#dykeppjplv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dykeppjplv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dykeppjplv p { margin: 0; padding: 0; }
 #dykeppjplv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dykeppjplv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dykeppjplv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dykeppjplv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dykeppjplv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dykeppjplv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dykeppjplv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dykeppjplv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dykeppjplv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dykeppjplv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dykeppjplv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dykeppjplv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dykeppjplv .gt_spanner_row { border-bottom-style: hidden; }
 #dykeppjplv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dykeppjplv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dykeppjplv .gt_from_md> :first-child { margin-top: 0; }
 #dykeppjplv .gt_from_md> :last-child { margin-bottom: 0; }
 #dykeppjplv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dykeppjplv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dykeppjplv .gt_indent_1 { text-indent: 5px; }
 #dykeppjplv .gt_indent_2 { text-indent: calc(5px * 2); }
 #dykeppjplv .gt_indent_3 { text-indent: calc(5px * 3); }
 #dykeppjplv .gt_indent_4 { text-indent: calc(5px * 4); }
 #dykeppjplv .gt_indent_5 { text-indent: calc(5px * 5); }
 #dykeppjplv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dykeppjplv .gt_row_group_first td { border-top-width: 2px; }
 #dykeppjplv .gt_row_group_first th { border-top-width: 2px; }
 #dykeppjplv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dykeppjplv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dykeppjplv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dykeppjplv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dykeppjplv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dykeppjplv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dykeppjplv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dykeppjplv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dykeppjplv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dykeppjplv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dykeppjplv .gt_left { text-align: left; }
 #dykeppjplv .gt_center { text-align: center; }
 #dykeppjplv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dykeppjplv .gt_font_normal { font-weight: normal; }
 #dykeppjplv .gt_font_bold { font-weight: bold; }
 #dykeppjplv .gt_font_italic { font-style: italic; }
 #dykeppjplv .gt_super { font-size: 65%; }
 #dykeppjplv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dykeppjplv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dykeppjplv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dykeppjplv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dykeppjplv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dykeppjplv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: pink" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" style="background-color: pink" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: pink" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" style="background-color: pink" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: pink" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" style="background-color: pink" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_left" headers="grp_b stub-6 fctr">six</td>
<td class="gt_row gt_right" headers="grp_b stub-6 date">2015-06-15</td>
<td class="gt_row gt_right" headers="grp_b stub-6 time">None</td>
<td class="gt_row gt_right" headers="grp_b stub-6 datetime">2018-06-06 16:11</td>
<td class="gt_row gt_right" style="background-color: pink" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_left" headers="grp_b stub-7 fctr">seven</td>
<td class="gt_row gt_right" headers="grp_b stub-7 date">None</td>
<td class="gt_row gt_right" headers="grp_b stub-7 time">19:10</td>
<td class="gt_row gt_right" headers="grp_b stub-7 datetime">2018-07-07 05:22</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_left" headers="grp_b stub-8 fctr">eight</td>
<td class="gt_row gt_right" headers="grp_b stub-8 date">2015-08-15</td>
<td class="gt_row gt_right" headers="grp_b stub-8 time">20:20</td>
<td class="gt_row gt_right" headers="grp_b stub-8 datetime">None</td>
<td class="gt_row gt_right" style="background-color: pink" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


Use `pattern=` to target cells by regex. This matches any cell whose string value contains "ne" or "na".


``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=style.fill(color="green"),
        pattern="ne|na",
    )
)
```


<style>
#pjndjudmoh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pjndjudmoh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pjndjudmoh p { margin: 0; padding: 0; }
 #pjndjudmoh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pjndjudmoh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pjndjudmoh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pjndjudmoh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pjndjudmoh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pjndjudmoh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pjndjudmoh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pjndjudmoh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pjndjudmoh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pjndjudmoh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pjndjudmoh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pjndjudmoh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pjndjudmoh .gt_spanner_row { border-bottom-style: hidden; }
 #pjndjudmoh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pjndjudmoh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pjndjudmoh .gt_from_md> :first-child { margin-top: 0; }
 #pjndjudmoh .gt_from_md> :last-child { margin-bottom: 0; }
 #pjndjudmoh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pjndjudmoh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pjndjudmoh .gt_indent_1 { text-indent: 5px; }
 #pjndjudmoh .gt_indent_2 { text-indent: calc(5px * 2); }
 #pjndjudmoh .gt_indent_3 { text-indent: calc(5px * 3); }
 #pjndjudmoh .gt_indent_4 { text-indent: calc(5px * 4); }
 #pjndjudmoh .gt_indent_5 { text-indent: calc(5px * 5); }
 #pjndjudmoh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pjndjudmoh .gt_row_group_first td { border-top-width: 2px; }
 #pjndjudmoh .gt_row_group_first th { border-top-width: 2px; }
 #pjndjudmoh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pjndjudmoh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pjndjudmoh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pjndjudmoh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pjndjudmoh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pjndjudmoh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pjndjudmoh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pjndjudmoh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pjndjudmoh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pjndjudmoh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pjndjudmoh .gt_left { text-align: left; }
 #pjndjudmoh .gt_center { text-align: center; }
 #pjndjudmoh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pjndjudmoh .gt_font_normal { font-weight: normal; }
 #pjndjudmoh .gt_font_bold { font-weight: bold; }
 #pjndjudmoh .gt_font_italic { font-style: italic; }
 #pjndjudmoh .gt_super { font-size: 65%; }
 #pjndjudmoh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pjndjudmoh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pjndjudmoh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pjndjudmoh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pjndjudmoh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pjndjudmoh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" style="background-color: green" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" style="background-color: green" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_left" headers="grp_b stub-6 fctr">six</td>
<td class="gt_row gt_right" headers="grp_b stub-6 date">2015-06-15</td>
<td class="gt_row gt_right" headers="grp_b stub-6 time">None</td>
<td class="gt_row gt_right" headers="grp_b stub-6 datetime">2018-06-06 16:11</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_left" headers="grp_b stub-7 fctr">seven</td>
<td class="gt_row gt_right" headers="grp_b stub-7 date">None</td>
<td class="gt_row gt_right" headers="grp_b stub-7 time">19:10</td>
<td class="gt_row gt_right" headers="grp_b stub-7 datetime">2018-07-07 05:22</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" style="background-color: green" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_left" headers="grp_b stub-8 fctr">eight</td>
<td class="gt_row gt_right" headers="grp_b stub-8 date">2015-08-15</td>
<td class="gt_row gt_right" headers="grp_b stub-8 time">20:20</td>
<td class="gt_row gt_right" headers="grp_b stub-8 datetime">None</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


Expand the styling to entire rows using `targets="row"`, and project into the stub with `extents=["body", "stub"]`.


``` python
from great_tables import GT, style, exibble

(
    GT(exibble, rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=style.fill(color="lightblue"),
        values=[49.95],
        targets="row",
        extents=["body", "stub"],
    )
)
```


<style>
#eqtfojfire table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eqtfojfire thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eqtfojfire p { margin: 0; padding: 0; }
 #eqtfojfire .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eqtfojfire .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eqtfojfire .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eqtfojfire .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eqtfojfire .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eqtfojfire .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eqtfojfire .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eqtfojfire .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eqtfojfire .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eqtfojfire .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eqtfojfire .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eqtfojfire .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eqtfojfire .gt_spanner_row { border-bottom-style: hidden; }
 #eqtfojfire .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eqtfojfire .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eqtfojfire .gt_from_md> :first-child { margin-top: 0; }
 #eqtfojfire .gt_from_md> :last-child { margin-bottom: 0; }
 #eqtfojfire .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eqtfojfire .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eqtfojfire .gt_indent_1 { text-indent: 5px; }
 #eqtfojfire .gt_indent_2 { text-indent: calc(5px * 2); }
 #eqtfojfire .gt_indent_3 { text-indent: calc(5px * 3); }
 #eqtfojfire .gt_indent_4 { text-indent: calc(5px * 4); }
 #eqtfojfire .gt_indent_5 { text-indent: calc(5px * 5); }
 #eqtfojfire .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eqtfojfire .gt_row_group_first td { border-top-width: 2px; }
 #eqtfojfire .gt_row_group_first th { border-top-width: 2px; }
 #eqtfojfire .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eqtfojfire .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eqtfojfire .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eqtfojfire .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eqtfojfire .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eqtfojfire .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eqtfojfire .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eqtfojfire .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eqtfojfire .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eqtfojfire .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eqtfojfire .gt_left { text-align: left; }
 #eqtfojfire .gt_center { text-align: center; }
 #eqtfojfire .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eqtfojfire .gt_font_normal { font-weight: normal; }
 #eqtfojfire .gt_font_bold { font-weight: bold; }
 #eqtfojfire .gt_font_italic { font-style: italic; }
 #eqtfojfire .gt_super { font-size: 65%; }
 #eqtfojfire .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eqtfojfire .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eqtfojfire .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eqtfojfire .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eqtfojfire .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eqtfojfire .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" style="background-color: lightblue" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightblue" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" style="background-color: lightblue" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" style="background-color: lightblue" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" style="background-color: lightblue" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" style="background-color: lightblue" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" style="background-color: lightblue" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" style="background-color: lightblue" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_left" headers="grp_b stub-6 fctr">six</td>
<td class="gt_row gt_right" headers="grp_b stub-6 date">2015-06-15</td>
<td class="gt_row gt_right" headers="grp_b stub-6 time">None</td>
<td class="gt_row gt_right" headers="grp_b stub-6 datetime">2018-06-06 16:11</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_left" headers="grp_b stub-7 fctr">seven</td>
<td class="gt_row gt_right" headers="grp_b stub-7 date">None</td>
<td class="gt_row gt_right" headers="grp_b stub-7 time">19:10</td>
<td class="gt_row gt_right" headers="grp_b stub-7 datetime">2018-07-07 05:22</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_left" headers="grp_b stub-8 fctr">eight</td>
<td class="gt_row gt_right" headers="grp_b stub-8 date">2015-08-15</td>
<td class="gt_row gt_right" headers="grp_b stub-8 time">20:20</td>
<td class="gt_row gt_right" headers="grp_b stub-8 datetime">None</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>
