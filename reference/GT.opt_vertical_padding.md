# GT.opt_vertical_padding()


Option to scale the vertical padding of the table.


Usage

``` python
GT.opt_vertical_padding(scale=1.0)
```


This method allows us to scale the vertical padding of the table by a factor of `scale`. The default value is `1.0` and this method serves as a convenient shortcut for `gt.tab_options(heading_padding=<new_val>, column_labels_padding=<new_val>, data_row_padding=<new_val>, row_group_padding=<new_val>, source_notes_padding=<new_val>)`.


## Parameters


`scale: float = ``1.0`  
The factor by which to scale the vertical padding. The default value is `1.0`. A value less than `1.0` will reduce the padding, and a value greater than `1.0` will increase the padding. The value must be between `0` and `3`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using select columns from the [exibble](data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll scale the vertical padding of the table by a factor of `3` using the [opt_vertical_padding()](GT.opt_vertical_padding.md#great_tables.GT.opt_vertical_padding) method.


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

gt_tbl.opt_vertical_padding(scale=3)
```


<style>
#czblhbmoil table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#czblhbmoil thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#czblhbmoil p { margin: 0; padding: 0; }
 #czblhbmoil .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #czblhbmoil .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #czblhbmoil .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 12px; padding-bottom: 12px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #czblhbmoil .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 11px; padding-bottom: 13px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #czblhbmoil .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #czblhbmoil .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #czblhbmoil .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #czblhbmoil .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 15px; padding-bottom: 13px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #czblhbmoil .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #czblhbmoil .gt_column_spanner_outer:first-child { padding-left: 0; }
 #czblhbmoil .gt_column_spanner_outer:last-child { padding-right: 0; }
 #czblhbmoil .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 15px; padding-bottom: 15px; overflow-x: hidden; display: inline-block; width: 100%; }
 #czblhbmoil .gt_spanner_row { border-bottom-style: hidden; }
 #czblhbmoil .gt_group_heading { padding-top: 24px; padding-bottom: 24px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #czblhbmoil .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #czblhbmoil .gt_from_md> :first-child { margin-top: 0; }
 #czblhbmoil .gt_from_md> :last-child { margin-bottom: 0; }
 #czblhbmoil .gt_row { padding-top: 24px; padding-bottom: 24px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #czblhbmoil .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #czblhbmoil .gt_indent_1 { text-indent: 5px; }
 #czblhbmoil .gt_indent_2 { text-indent: calc(5px * 2); }
 #czblhbmoil .gt_indent_3 { text-indent: calc(5px * 3); }
 #czblhbmoil .gt_indent_4 { text-indent: calc(5px * 4); }
 #czblhbmoil .gt_indent_5 { text-indent: calc(5px * 5); }
 #czblhbmoil .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #czblhbmoil .gt_row_group_first td { border-top-width: 2px; }
 #czblhbmoil .gt_row_group_first th { border-top-width: 2px; }
 #czblhbmoil .gt_striped { color: #333333; background-color: #F4F4F4; }
 #czblhbmoil .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #czblhbmoil .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #czblhbmoil .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #czblhbmoil .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #czblhbmoil .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #czblhbmoil .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #czblhbmoil .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #czblhbmoil .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #czblhbmoil .gt_sourcenote { font-size: 90%; padding-top: 12px; padding-bottom: 12px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #czblhbmoil .gt_left { text-align: left; }
 #czblhbmoil .gt_center { text-align: center; }
 #czblhbmoil .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #czblhbmoil .gt_font_normal { font-weight: normal; }
 #czblhbmoil .gt_font_bold { font-weight: bold; }
 #czblhbmoil .gt_font_italic { font-style: italic; }
 #czblhbmoil .gt_super { font-size: 65%; }
 #czblhbmoil .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #czblhbmoil .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #czblhbmoil .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #czblhbmoil .gt_sourcenote { font-size: 90%; padding-top: 12px; padding-bottom: 12px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #czblhbmoil .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #czblhbmoil .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
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
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
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


Now that's a tall table! The overall effect of scaling the vertical padding is that the table will appear taller and there will be more buffer space between the table elements. A value of `3` is pretty extreme and is likely to be too much in most cases, so, feel free to experiment with different values when looking to increase the vertical padding.

Let's go the other way (using a value less than `1`) and try to condense the content vertically with a `scale` factor of `0.5`. This will reduce the top and bottom padding globally and make the table appear more compact.


``` python
gt_tbl.opt_vertical_padding(scale=0.5)
```


<style>
#eljxundhyw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eljxundhyw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eljxundhyw p { margin: 0; padding: 0; }
 #eljxundhyw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eljxundhyw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eljxundhyw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eljxundhyw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eljxundhyw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eljxundhyw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eljxundhyw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eljxundhyw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eljxundhyw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eljxundhyw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eljxundhyw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eljxundhyw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eljxundhyw .gt_spanner_row { border-bottom-style: hidden; }
 #eljxundhyw .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eljxundhyw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eljxundhyw .gt_from_md> :first-child { margin-top: 0; }
 #eljxundhyw .gt_from_md> :last-child { margin-bottom: 0; }
 #eljxundhyw .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eljxundhyw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eljxundhyw .gt_indent_1 { text-indent: 5px; }
 #eljxundhyw .gt_indent_2 { text-indent: calc(5px * 2); }
 #eljxundhyw .gt_indent_3 { text-indent: calc(5px * 3); }
 #eljxundhyw .gt_indent_4 { text-indent: calc(5px * 4); }
 #eljxundhyw .gt_indent_5 { text-indent: calc(5px * 5); }
 #eljxundhyw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eljxundhyw .gt_row_group_first td { border-top-width: 2px; }
 #eljxundhyw .gt_row_group_first th { border-top-width: 2px; }
 #eljxundhyw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eljxundhyw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eljxundhyw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eljxundhyw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eljxundhyw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eljxundhyw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eljxundhyw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eljxundhyw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eljxundhyw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eljxundhyw .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eljxundhyw .gt_left { text-align: left; }
 #eljxundhyw .gt_center { text-align: center; }
 #eljxundhyw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eljxundhyw .gt_font_normal { font-weight: normal; }
 #eljxundhyw .gt_font_bold { font-weight: bold; }
 #eljxundhyw .gt_font_italic { font-style: italic; }
 #eljxundhyw .gt_super { font-size: 65%; }
 #eljxundhyw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eljxundhyw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eljxundhyw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eljxundhyw .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eljxundhyw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eljxundhyw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
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
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
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


A value of `0.5` provides a reasonable amount of vertical padding and the table will appear more compact. This is useful when space is limited and, in such a situation, this is a practical solution to that problem.
