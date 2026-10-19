# GT.tab_stub()


Add a table stub, to emphasize row and group information.


Usage

``` python
GT.tab_stub(
    rowname_col=None,
    groupname_col=None,
)
```


## Parameters


`rowname_col: str | list[str] | None = None`  
The column to use for row names. By default, no row names added. A list of columns creates a hierarchical stub: the last column holds the row names, and the columns before it are outer levels (outermost first), with repeated values merged across adjacent rows.

`groupname_col: str | None = None`  
The column to use for group names. By default no group names added.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

By default, all data is together in the body of the table.


``` python
from great_tables import GT, exibble

GT(exibble)
```


<style>
#tuagebatck table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tuagebatck thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tuagebatck p { margin: 0; padding: 0; }
 #tuagebatck .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tuagebatck .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tuagebatck .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tuagebatck .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tuagebatck .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tuagebatck .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tuagebatck .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tuagebatck .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tuagebatck .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tuagebatck .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tuagebatck .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tuagebatck .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tuagebatck .gt_spanner_row { border-bottom-style: hidden; }
 #tuagebatck .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tuagebatck .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tuagebatck .gt_from_md> :first-child { margin-top: 0; }
 #tuagebatck .gt_from_md> :last-child { margin-bottom: 0; }
 #tuagebatck .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tuagebatck .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tuagebatck .gt_indent_1 { text-indent: 5px; }
 #tuagebatck .gt_indent_2 { text-indent: calc(5px * 2); }
 #tuagebatck .gt_indent_3 { text-indent: calc(5px * 3); }
 #tuagebatck .gt_indent_4 { text-indent: calc(5px * 4); }
 #tuagebatck .gt_indent_5 { text-indent: calc(5px * 5); }
 #tuagebatck .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tuagebatck .gt_row_group_first td { border-top-width: 2px; }
 #tuagebatck .gt_row_group_first th { border-top-width: 2px; }
 #tuagebatck .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tuagebatck .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tuagebatck .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tuagebatck .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tuagebatck .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tuagebatck .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tuagebatck .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tuagebatck .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tuagebatck .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tuagebatck .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tuagebatck .gt_left { text-align: left; }
 #tuagebatck .gt_center { text-align: center; }
 #tuagebatck .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tuagebatck .gt_font_normal { font-weight: normal; }
 #tuagebatck .gt_font_bold { font-weight: bold; }
 #tuagebatck .gt_font_italic { font-style: italic; }
 #tuagebatck .gt_super { font-size: 65%; }
 #tuagebatck .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tuagebatck .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tuagebatck .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tuagebatck .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tuagebatck .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tuagebatck .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


The table stub separates row names with a vertical line, and puts group names on their own line.


``` python
GT(exibble).tab_stub(rowname_col="row", groupname_col="group")
```


<style>
#qkucmjarem table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qkucmjarem thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qkucmjarem p { margin: 0; padding: 0; }
 #qkucmjarem .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qkucmjarem .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qkucmjarem .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qkucmjarem .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qkucmjarem .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qkucmjarem .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qkucmjarem .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qkucmjarem .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qkucmjarem .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qkucmjarem .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qkucmjarem .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qkucmjarem .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qkucmjarem .gt_spanner_row { border-bottom-style: hidden; }
 #qkucmjarem .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qkucmjarem .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qkucmjarem .gt_from_md> :first-child { margin-top: 0; }
 #qkucmjarem .gt_from_md> :last-child { margin-bottom: 0; }
 #qkucmjarem .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qkucmjarem .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qkucmjarem .gt_indent_1 { text-indent: 5px; }
 #qkucmjarem .gt_indent_2 { text-indent: calc(5px * 2); }
 #qkucmjarem .gt_indent_3 { text-indent: calc(5px * 3); }
 #qkucmjarem .gt_indent_4 { text-indent: calc(5px * 4); }
 #qkucmjarem .gt_indent_5 { text-indent: calc(5px * 5); }
 #qkucmjarem .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qkucmjarem .gt_row_group_first td { border-top-width: 2px; }
 #qkucmjarem .gt_row_group_first th { border-top-width: 2px; }
 #qkucmjarem .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qkucmjarem .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qkucmjarem .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qkucmjarem .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qkucmjarem .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qkucmjarem .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qkucmjarem .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qkucmjarem .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qkucmjarem .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qkucmjarem .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qkucmjarem .gt_left { text-align: left; }
 #qkucmjarem .gt_center { text-align: center; }
 #qkucmjarem .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qkucmjarem .gt_font_normal { font-weight: normal; }
 #qkucmjarem .gt_font_bold { font-weight: bold; }
 #qkucmjarem .gt_font_italic { font-style: italic; }
 #qkucmjarem .gt_super { font-size: 65%; }
 #qkucmjarem .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qkucmjarem .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qkucmjarem .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qkucmjarem .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qkucmjarem .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qkucmjarem .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
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


Passing a list of columns to `rowname_col=` creates a hierarchical stub. Here, the rows are labeled by `"group"` and then `"row"`, and the repeated group values are merged.


``` python
GT(exibble[["group", "row", "num", "char"]]).tab_stub(rowname_col=["group", "row"])
```


<style>
#zmccvmikpo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zmccvmikpo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zmccvmikpo p { margin: 0; padding: 0; }
 #zmccvmikpo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zmccvmikpo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zmccvmikpo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zmccvmikpo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zmccvmikpo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zmccvmikpo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zmccvmikpo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zmccvmikpo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zmccvmikpo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zmccvmikpo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zmccvmikpo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zmccvmikpo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zmccvmikpo .gt_spanner_row { border-bottom-style: hidden; }
 #zmccvmikpo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zmccvmikpo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zmccvmikpo .gt_from_md> :first-child { margin-top: 0; }
 #zmccvmikpo .gt_from_md> :last-child { margin-bottom: 0; }
 #zmccvmikpo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zmccvmikpo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zmccvmikpo .gt_indent_1 { text-indent: 5px; }
 #zmccvmikpo .gt_indent_2 { text-indent: calc(5px * 2); }
 #zmccvmikpo .gt_indent_3 { text-indent: calc(5px * 3); }
 #zmccvmikpo .gt_indent_4 { text-indent: calc(5px * 4); }
 #zmccvmikpo .gt_indent_5 { text-indent: calc(5px * 5); }
 #zmccvmikpo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zmccvmikpo .gt_row_group_first td { border-top-width: 2px; }
 #zmccvmikpo .gt_row_group_first th { border-top-width: 2px; }
 #zmccvmikpo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zmccvmikpo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zmccvmikpo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zmccvmikpo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zmccvmikpo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zmccvmikpo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zmccvmikpo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zmccvmikpo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zmccvmikpo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zmccvmikpo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zmccvmikpo .gt_left { text-align: left; }
 #zmccvmikpo .gt_center { text-align: center; }
 #zmccvmikpo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zmccvmikpo .gt_font_normal { font-weight: normal; }
 #zmccvmikpo .gt_font_bold { font-weight: bold; }
 #zmccvmikpo .gt_font_italic { font-style: italic; }
 #zmccvmikpo .gt_super { font-size: 65%; }
 #zmccvmikpo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zmccvmikpo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zmccvmikpo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zmccvmikpo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zmccvmikpo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zmccvmikpo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th colspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="colgroup"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th rowspan="4" id="stub-1-1" class="gt_row gt_left gt_stub" scope="rowgroup">grp_a</th>
<th id="stub-1-2" class="gt_row gt_left gt_stub" scope="row">row_1</th>
<td class="gt_row gt_right" headers="stub-1-1 stub-1-2 num">0.1111</td>
<td class="gt_row gt_left" headers="stub-1-1 stub-1-2 char">apricot</td>
</tr>
<tr>
<th id="stub-2-2" class="gt_row gt_left gt_stub" scope="row">row_2</th>
<td class="gt_row gt_right" headers="stub-1-1 stub-2-2 num">2.222</td>
<td class="gt_row gt_left" headers="stub-1-1 stub-2-2 char">banana</td>
</tr>
<tr>
<th id="stub-3-2" class="gt_row gt_left gt_stub" scope="row">row_3</th>
<td class="gt_row gt_right" headers="stub-1-1 stub-3-2 num">33.33</td>
<td class="gt_row gt_left" headers="stub-1-1 stub-3-2 char">coconut</td>
</tr>
<tr>
<th id="stub-4-2" class="gt_row gt_left gt_stub" scope="row">row_4</th>
<td class="gt_row gt_right" headers="stub-1-1 stub-4-2 num">444.4</td>
<td class="gt_row gt_left" headers="stub-1-1 stub-4-2 char">durian</td>
</tr>
<tr>
<th rowspan="4" id="stub-5-1" class="gt_row gt_left gt_stub" scope="rowgroup">grp_b</th>
<th id="stub-5-2" class="gt_row gt_left gt_stub" scope="row">row_5</th>
<td class="gt_row gt_right" headers="stub-5-1 stub-5-2 num">5550.0</td>
<td class="gt_row gt_left" headers="stub-5-1 stub-5-2 char">None</td>
</tr>
<tr>
<th id="stub-6-2" class="gt_row gt_left gt_stub" scope="row">row_6</th>
<td class="gt_row gt_right" headers="stub-5-1 stub-6-2 num">None</td>
<td class="gt_row gt_left" headers="stub-5-1 stub-6-2 char">fig</td>
</tr>
<tr>
<th id="stub-7-2" class="gt_row gt_left gt_stub" scope="row">row_7</th>
<td class="gt_row gt_right" headers="stub-5-1 stub-7-2 num">777000.0</td>
<td class="gt_row gt_left" headers="stub-5-1 stub-7-2 char">grapefruit</td>
</tr>
<tr>
<th id="stub-8-2" class="gt_row gt_left gt_stub" scope="row">row_8</th>
<td class="gt_row gt_right" headers="stub-5-1 stub-8-2 num">8880000.0</td>
<td class="gt_row gt_left" headers="stub-5-1 stub-8-2 char">honeydew</td>
</tr>
</tbody>
</table>
