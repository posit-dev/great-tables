## GT.cols_label_rotate()


Rotate the column label for one or more columns.


Usage

``` python
GT.cols_label_rotate(
    columns=None,
    dir="sideways-lr",
    align=None,
    padding=8,
)
```


The [cols_label_rotate()](GT.cols_label_rotate.md#great_tables.GT.cols_label_rotate) method sets the orientation of the column label text to make it flow vertically. The `dir` argument can be set to one of `"sideways-lr"`, `"sideways-rl"`, or `"vertical-lr"`, and the `columns` argument can be used to specify which columns to apply the alignment to. If `columns` is not specified, the alignment is applied to all columns.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. If `None`, the alignment is applied to all columns.

`dir: Literal[``"sideways-lr", `<span class="st">`"sideways-rl"``, ``"vertical-lr"``]`</span>` = ``"sideways-lr"`  
A string that gives the direction of the text. Options: `"sideways-lr"`, `"sideways-rl"`, `"vertical-lr"`. See note for information on text layout.

`align: Literal[``"left", `<span class="st">`"center"``, ``"right"``] | None`</span>` = None`  
The alignment to apply. Must be one of `"left"`, `"center"`, `"right"`, or `"none"`. If text is laid out vertically, this affects alignment along the vertical axis.

`padding: int = ``8`  
The vertical padding to apply to the column labels.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

The example below rotates column labels such that the text is set to the left.


``` python
from great_tables import GT, style, loc, exibble

exibble_sm = exibble[["num", "fctr", "row", "group"]]

(
    GT(exibble_sm, rowname_col="row", groupname_col="group")
    .cols_label_rotate(columns=["num", "fctr"])
)
```


<style>
#qqnwymephg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qqnwymephg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qqnwymephg p { margin: 0; padding: 0; }
 #qqnwymephg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qqnwymephg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qqnwymephg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qqnwymephg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qqnwymephg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qqnwymephg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qqnwymephg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qqnwymephg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qqnwymephg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qqnwymephg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qqnwymephg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qqnwymephg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qqnwymephg .gt_spanner_row { border-bottom-style: hidden; }
 #qqnwymephg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qqnwymephg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qqnwymephg .gt_from_md> :first-child { margin-top: 0; }
 #qqnwymephg .gt_from_md> :last-child { margin-bottom: 0; }
 #qqnwymephg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qqnwymephg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qqnwymephg .gt_indent_1 { text-indent: 5px; }
 #qqnwymephg .gt_indent_2 { text-indent: calc(5px * 2); }
 #qqnwymephg .gt_indent_3 { text-indent: calc(5px * 3); }
 #qqnwymephg .gt_indent_4 { text-indent: calc(5px * 4); }
 #qqnwymephg .gt_indent_5 { text-indent: calc(5px * 5); }
 #qqnwymephg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qqnwymephg .gt_row_group_first td { border-top-width: 2px; }
 #qqnwymephg .gt_row_group_first th { border-top-width: 2px; }
 #qqnwymephg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qqnwymephg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qqnwymephg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qqnwymephg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qqnwymephg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qqnwymephg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qqnwymephg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qqnwymephg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qqnwymephg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qqnwymephg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qqnwymephg .gt_left { text-align: left; }
 #qqnwymephg .gt_center { text-align: center; }
 #qqnwymephg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qqnwymephg .gt_font_normal { font-weight: normal; }
 #qqnwymephg .gt_font_bold { font-weight: bold; }
 #qqnwymephg .gt_font_italic { font-style: italic; }
 #qqnwymephg .gt_super { font-size: 65%; }
 #qqnwymephg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qqnwymephg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qqnwymephg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qqnwymephg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qqnwymephg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qqnwymephg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" style="text-align: left; writing-mode: sideways-lr; vertical-align: middle; padding: 8px 0px;" scope="col">num</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" style="text-align: left; writing-mode: sideways-lr; vertical-align: middle; padding: 8px 0px;" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">three</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">four</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">five</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">six</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">seven</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">eight</td>
</tr>
</tbody>
</table>


Other styles you provide won't override the column label rotation directives. Here we set the text to the right.


``` python
(
    GT(exibble_sm, rowname_col="row", groupname_col="group")
    .cols_label_rotate(columns=["num", "fctr"], dir="vertical-lr")
    .tab_style(style=style.text(weight="bold"), locations=loc.column_labels(["fctr"]))
)
```


<style>
#yzpdgxlplc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yzpdgxlplc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yzpdgxlplc p { margin: 0; padding: 0; }
 #yzpdgxlplc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yzpdgxlplc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yzpdgxlplc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yzpdgxlplc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yzpdgxlplc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yzpdgxlplc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yzpdgxlplc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yzpdgxlplc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yzpdgxlplc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yzpdgxlplc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yzpdgxlplc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yzpdgxlplc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yzpdgxlplc .gt_spanner_row { border-bottom-style: hidden; }
 #yzpdgxlplc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yzpdgxlplc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yzpdgxlplc .gt_from_md> :first-child { margin-top: 0; }
 #yzpdgxlplc .gt_from_md> :last-child { margin-bottom: 0; }
 #yzpdgxlplc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yzpdgxlplc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yzpdgxlplc .gt_indent_1 { text-indent: 5px; }
 #yzpdgxlplc .gt_indent_2 { text-indent: calc(5px * 2); }
 #yzpdgxlplc .gt_indent_3 { text-indent: calc(5px * 3); }
 #yzpdgxlplc .gt_indent_4 { text-indent: calc(5px * 4); }
 #yzpdgxlplc .gt_indent_5 { text-indent: calc(5px * 5); }
 #yzpdgxlplc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yzpdgxlplc .gt_row_group_first td { border-top-width: 2px; }
 #yzpdgxlplc .gt_row_group_first th { border-top-width: 2px; }
 #yzpdgxlplc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yzpdgxlplc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yzpdgxlplc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yzpdgxlplc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yzpdgxlplc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yzpdgxlplc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yzpdgxlplc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yzpdgxlplc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yzpdgxlplc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yzpdgxlplc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yzpdgxlplc .gt_left { text-align: left; }
 #yzpdgxlplc .gt_center { text-align: center; }
 #yzpdgxlplc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yzpdgxlplc .gt_font_normal { font-weight: normal; }
 #yzpdgxlplc .gt_font_bold { font-weight: bold; }
 #yzpdgxlplc .gt_font_italic { font-style: italic; }
 #yzpdgxlplc .gt_super { font-size: 65%; }
 #yzpdgxlplc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yzpdgxlplc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yzpdgxlplc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yzpdgxlplc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yzpdgxlplc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yzpdgxlplc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" style="text-align: right; writing-mode: vertical-lr; vertical-align: middle; padding: 8px 0px;" scope="col">num</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" style="text-align: right; writing-mode: vertical-lr; vertical-align: middle; padding: 8px 0px; font-weight: bold;" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">three</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">four</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">five</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">six</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">seven</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">eight</td>
</tr>
</tbody>
</table>


Labels that are restricted by the height of the stub head will wrap horizontally.


``` python
(
    GT(exibble_sm, rowname_col="row", groupname_col="group")
    .cols_label({"fctr": "A longer description of the values in the column below"})
    .cols_label_rotate(columns=["num", "fctr"], dir="sideways-lr")
    .tab_style(
        style=[style.text(weight="bold"), style.css(rule="height: 200px;")],
        locations=loc.column_labels(["fctr"])
    )
)
```


<style>
#mnswrhttpx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mnswrhttpx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mnswrhttpx p { margin: 0; padding: 0; }
 #mnswrhttpx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mnswrhttpx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mnswrhttpx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mnswrhttpx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mnswrhttpx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mnswrhttpx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mnswrhttpx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mnswrhttpx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mnswrhttpx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mnswrhttpx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mnswrhttpx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mnswrhttpx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mnswrhttpx .gt_spanner_row { border-bottom-style: hidden; }
 #mnswrhttpx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mnswrhttpx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mnswrhttpx .gt_from_md> :first-child { margin-top: 0; }
 #mnswrhttpx .gt_from_md> :last-child { margin-bottom: 0; }
 #mnswrhttpx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mnswrhttpx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mnswrhttpx .gt_indent_1 { text-indent: 5px; }
 #mnswrhttpx .gt_indent_2 { text-indent: calc(5px * 2); }
 #mnswrhttpx .gt_indent_3 { text-indent: calc(5px * 3); }
 #mnswrhttpx .gt_indent_4 { text-indent: calc(5px * 4); }
 #mnswrhttpx .gt_indent_5 { text-indent: calc(5px * 5); }
 #mnswrhttpx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mnswrhttpx .gt_row_group_first td { border-top-width: 2px; }
 #mnswrhttpx .gt_row_group_first th { border-top-width: 2px; }
 #mnswrhttpx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mnswrhttpx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mnswrhttpx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mnswrhttpx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mnswrhttpx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mnswrhttpx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mnswrhttpx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mnswrhttpx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mnswrhttpx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mnswrhttpx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mnswrhttpx .gt_left { text-align: left; }
 #mnswrhttpx .gt_center { text-align: center; }
 #mnswrhttpx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mnswrhttpx .gt_font_normal { font-weight: normal; }
 #mnswrhttpx .gt_font_bold { font-weight: bold; }
 #mnswrhttpx .gt_font_italic { font-style: italic; }
 #mnswrhttpx .gt_super { font-size: 65%; }
 #mnswrhttpx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mnswrhttpx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mnswrhttpx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mnswrhttpx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mnswrhttpx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mnswrhttpx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" style="text-align: left; writing-mode: sideways-lr; vertical-align: middle; padding: 8px 0px;" scope="col">num</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" style="text-align: left; writing-mode: sideways-lr; vertical-align: middle; padding: 8px 0px; font-weight: bold; height: 200px;" scope="col">A longer description of the values in the column below</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">three</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">four</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">five</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">six</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">seven</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">eight</td>
</tr>
</tbody>
</table>


## Note

The `dir` parameter uses the following keywords to alter the direction of the column label text.


##### `"sideways-lr"`

For ltr scripts, content flows vertically from bottom to top. For rtl scripts, content flows vertically from top to bottom. Characters are set sideways toward the left. Overflow lines are appended to the right.


##### `"sideways-rl"`

For ltr scripts, content flows vertically from top to bottom. For rtl scripts, content flows vertically from bottom to top. Characters are set sideways toward the right. Overflow lines are appended to the left.


##### `"vertical-lr"`

Identical to `"sideways-rl"`, but overflow lines are appended to the right.
