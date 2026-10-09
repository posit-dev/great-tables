# GT.opt_horizontal_padding()


Option to scale the horizontal padding of the table.


Usage

``` python
GT.opt_horizontal_padding(scale=1.0)
```


This method allows us to scale the horizontal padding of the table by a factor of `scale`. The default value is `1.0` and this method serves as a convenient shortcut for `gt.tab_options( heading_padding_horizontal=<new_val>, column_labels_padding_horizontal=<new_val>, data_row_padding_horizontal=<new_val>, row_group_padding_horizontal=<new_val>, source_notes_padding_horizontal=<new_val>)`.


## Parameters


`scale: float = ``1.0`  
The factor by which to scale the horizontal padding. The default value is `1.0`. A value less than `1.0` will reduce the padding, and a value greater than `1.0` will increase the padding. The value must be between `0` and `3`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using select columns from the [exibble](data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll scale the horizontal padding of the table by a factor of `3` using the [opt_horizontal_padding()](GT.opt_horizontal_padding.md#great_tables.GT.opt_horizontal_padding) method.


``` python
from great_tables import GT, exibble, md

gt_tbl = (
    GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
    )
    .tab_header(
        title=md("Data listing from **exibble**"),
        subtitle=md("`exibble` is a **Great Tables** dataset.")
    )
    .fmt_number(columns="num")
    .fmt_currency(columns="currency")
    .tab_source_note(source_note="This is only a subset of the dataset.")
)

gt_tbl.opt_horizontal_padding(scale=3)
```


<style>
#zxlhygtfih table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zxlhygtfih thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zxlhygtfih p { margin: 0; padding: 0; }
 #zxlhygtfih .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zxlhygtfih .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zxlhygtfih .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zxlhygtfih .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 15px; padding-right: 15px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zxlhygtfih .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxlhygtfih .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxlhygtfih .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxlhygtfih .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 15px; padding-right: 15px; overflow-x: hidden; }
 #zxlhygtfih .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zxlhygtfih .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zxlhygtfih .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zxlhygtfih .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zxlhygtfih .gt_spanner_row { border-bottom-style: hidden; }
 #zxlhygtfih .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 15px; padding-right: 15px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zxlhygtfih .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zxlhygtfih .gt_from_md> :first-child { margin-top: 0; }
 #zxlhygtfih .gt_from_md> :last-child { margin-bottom: 0; }
 #zxlhygtfih .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 15px; padding-right: 15px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zxlhygtfih .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; }
 #zxlhygtfih .gt_indent_1 { text-indent: 5px; }
 #zxlhygtfih .gt_indent_2 { text-indent: calc(5px * 2); }
 #zxlhygtfih .gt_indent_3 { text-indent: calc(5px * 3); }
 #zxlhygtfih .gt_indent_4 { text-indent: calc(5px * 4); }
 #zxlhygtfih .gt_indent_5 { text-indent: calc(5px * 5); }
 #zxlhygtfih .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; vertical-align: top; }
 #zxlhygtfih .gt_row_group_first td { border-top-width: 2px; }
 #zxlhygtfih .gt_row_group_first th { border-top-width: 2px; }
 #zxlhygtfih .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zxlhygtfih .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxlhygtfih .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxlhygtfih .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zxlhygtfih .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxlhygtfih .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxlhygtfih .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zxlhygtfih .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zxlhygtfih .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxlhygtfih .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #zxlhygtfih .gt_left { text-align: left; }
 #zxlhygtfih .gt_center { text-align: center; }
 #zxlhygtfih .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zxlhygtfih .gt_font_normal { font-weight: normal; }
 #zxlhygtfih .gt_font_bold { font-weight: bold; }
 #zxlhygtfih .gt_font_italic { font-style: italic; }
 #zxlhygtfih .gt_super { font-size: 65%; }
 #zxlhygtfih .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxlhygtfih .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zxlhygtfih .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxlhygtfih .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #zxlhygtfih .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zxlhygtfih .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><code>exibble</code> is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>


The overall effect of scaling the horizontal padding is that the table will appear wider or and there will added buffer space between the table elements. The overall look of the table will be more spacious and neighboring pieces of text will be less cramped.

Let's go the other way and scale the horizontal padding of the table by a factor of `0.5` using the [opt_horizontal_padding()](GT.opt_horizontal_padding.md#great_tables.GT.opt_horizontal_padding) method.


``` python
gt_tbl.opt_horizontal_padding(scale=0.5)
```


<style>
#vszotdbdfj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vszotdbdfj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vszotdbdfj p { margin: 0; padding: 0; }
 #vszotdbdfj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vszotdbdfj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vszotdbdfj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 2.5px; padding-right: 2.5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vszotdbdfj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 2.5px; padding-right: 2.5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vszotdbdfj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vszotdbdfj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vszotdbdfj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vszotdbdfj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 2.5px; padding-right: 2.5px; overflow-x: hidden; }
 #vszotdbdfj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vszotdbdfj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vszotdbdfj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vszotdbdfj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vszotdbdfj .gt_spanner_row { border-bottom-style: hidden; }
 #vszotdbdfj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 2.5px; padding-right: 2.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vszotdbdfj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vszotdbdfj .gt_from_md> :first-child { margin-top: 0; }
 #vszotdbdfj .gt_from_md> :last-child { margin-bottom: 0; }
 #vszotdbdfj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 2.5px; padding-right: 2.5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vszotdbdfj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 2.5px; padding-right: 2.5px; }
 #vszotdbdfj .gt_indent_1 { text-indent: 5px; }
 #vszotdbdfj .gt_indent_2 { text-indent: calc(5px * 2); }
 #vszotdbdfj .gt_indent_3 { text-indent: calc(5px * 3); }
 #vszotdbdfj .gt_indent_4 { text-indent: calc(5px * 4); }
 #vszotdbdfj .gt_indent_5 { text-indent: calc(5px * 5); }
 #vszotdbdfj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 2.5px; padding-right: 2.5px; vertical-align: top; }
 #vszotdbdfj .gt_row_group_first td { border-top-width: 2px; }
 #vszotdbdfj .gt_row_group_first th { border-top-width: 2px; }
 #vszotdbdfj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vszotdbdfj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vszotdbdfj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vszotdbdfj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vszotdbdfj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vszotdbdfj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vszotdbdfj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vszotdbdfj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vszotdbdfj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vszotdbdfj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 2.5px; padding-right: 2.5px; text-align: left; }
 #vszotdbdfj .gt_left { text-align: left; }
 #vszotdbdfj .gt_center { text-align: center; }
 #vszotdbdfj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vszotdbdfj .gt_font_normal { font-weight: normal; }
 #vszotdbdfj .gt_font_bold { font-weight: bold; }
 #vszotdbdfj .gt_font_italic { font-style: italic; }
 #vszotdbdfj .gt_super { font-size: 65%; }
 #vszotdbdfj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vszotdbdfj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vszotdbdfj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vszotdbdfj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 2.5px; padding-right: 2.5px; text-align: left; }
 #vszotdbdfj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vszotdbdfj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><code>exibble</code> is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>


What you get in this case is more condensed text across the horizontal axis. This may not always be desired when cells consist mainly of text, but it could be useful when the table is more visual and the cells are filled with graphics or other non-textual elements.
