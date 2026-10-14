# GT.cols_move_to_start()


Move one or more columns to the start.


Usage

``` python
GT.cols_move_to_start(columns)
```


We can easily move set of columns to the beginning of the column series and we only need to specify which `columns`. It's possible to do this upstream of **Great Tables**, however, it is easier with this method and it presents less possibility for error. The ordering of the `columns` that are moved to the start is preserved (same with the ordering of all other columns in the table).

The columns supplied in `columns` must all exist in the table. If you need to place one or columns at the end of the column series, the [cols_move_to_end()](GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end) method should be used. More control is offered with the [cols_move()](GT.cols_move.md#great_tables.GT.cols_move) method, where columns could be placed after a specific column.


## Parameters


`columns: SelectExpr`  
The columns to target. Can either be a single column name or a series of column names provided in a list.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

For this example, we'll use a portion of the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a simple table. Let's move the `year` column, which is the middle column, to the start of the column series with the [cols_move_to_start()](GT.cols_move_to_start.md#great_tables.GT.cols_move_to_start) method.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Fiji"][
    ["country_name", "year", "population"]
].tail(5)

GT(countrypops_mini).cols_move_to_start(columns="year")
```


<style>
#prhyecrpnq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#prhyecrpnq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#prhyecrpnq p { margin: 0; padding: 0; }
 #prhyecrpnq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #prhyecrpnq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #prhyecrpnq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #prhyecrpnq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #prhyecrpnq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #prhyecrpnq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #prhyecrpnq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #prhyecrpnq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #prhyecrpnq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #prhyecrpnq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #prhyecrpnq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #prhyecrpnq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #prhyecrpnq .gt_spanner_row { border-bottom-style: hidden; }
 #prhyecrpnq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #prhyecrpnq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #prhyecrpnq .gt_from_md> :first-child { margin-top: 0; }
 #prhyecrpnq .gt_from_md> :last-child { margin-bottom: 0; }
 #prhyecrpnq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #prhyecrpnq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #prhyecrpnq .gt_indent_1 { text-indent: 5px; }
 #prhyecrpnq .gt_indent_2 { text-indent: calc(5px * 2); }
 #prhyecrpnq .gt_indent_3 { text-indent: calc(5px * 3); }
 #prhyecrpnq .gt_indent_4 { text-indent: calc(5px * 4); }
 #prhyecrpnq .gt_indent_5 { text-indent: calc(5px * 5); }
 #prhyecrpnq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #prhyecrpnq .gt_row_group_first td { border-top-width: 2px; }
 #prhyecrpnq .gt_row_group_first th { border-top-width: 2px; }
 #prhyecrpnq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #prhyecrpnq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #prhyecrpnq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #prhyecrpnq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #prhyecrpnq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #prhyecrpnq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #prhyecrpnq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #prhyecrpnq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #prhyecrpnq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #prhyecrpnq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #prhyecrpnq .gt_left { text-align: left; }
 #prhyecrpnq .gt_center { text-align: center; }
 #prhyecrpnq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #prhyecrpnq .gt_font_normal { font-weight: normal; }
 #prhyecrpnq .gt_font_bold { font-weight: bold; }
 #prhyecrpnq .gt_font_italic { font-style: italic; }
 #prhyecrpnq .gt_super { font-size: 65%; }
 #prhyecrpnq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #prhyecrpnq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #prhyecrpnq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #prhyecrpnq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #prhyecrpnq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #prhyecrpnq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| year | country_name | population |
|------|--------------|------------|
| 2018 | Fiji         | 918996     |
| 2019 | Fiji         | 918465     |
| 2020 | Fiji         | 920422     |
| 2021 | Fiji         | 924610     |
| 2022 | Fiji         | 929766     |


We can also move multiple columns at a time. With the same [countrypops](data.countrypops.md#great_tables.data.countrypops)-based table (`countrypops_mini`), let's move both the `year` and `population` columns to the start of the column series.


``` python
GT(countrypops_mini).cols_move_to_start(columns=["year", "population"])
```


<style>
#nbksjazfxv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nbksjazfxv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nbksjazfxv p { margin: 0; padding: 0; }
 #nbksjazfxv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nbksjazfxv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nbksjazfxv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nbksjazfxv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nbksjazfxv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nbksjazfxv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nbksjazfxv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nbksjazfxv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nbksjazfxv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nbksjazfxv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nbksjazfxv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nbksjazfxv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nbksjazfxv .gt_spanner_row { border-bottom-style: hidden; }
 #nbksjazfxv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nbksjazfxv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nbksjazfxv .gt_from_md> :first-child { margin-top: 0; }
 #nbksjazfxv .gt_from_md> :last-child { margin-bottom: 0; }
 #nbksjazfxv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nbksjazfxv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nbksjazfxv .gt_indent_1 { text-indent: 5px; }
 #nbksjazfxv .gt_indent_2 { text-indent: calc(5px * 2); }
 #nbksjazfxv .gt_indent_3 { text-indent: calc(5px * 3); }
 #nbksjazfxv .gt_indent_4 { text-indent: calc(5px * 4); }
 #nbksjazfxv .gt_indent_5 { text-indent: calc(5px * 5); }
 #nbksjazfxv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nbksjazfxv .gt_row_group_first td { border-top-width: 2px; }
 #nbksjazfxv .gt_row_group_first th { border-top-width: 2px; }
 #nbksjazfxv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nbksjazfxv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nbksjazfxv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nbksjazfxv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nbksjazfxv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nbksjazfxv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nbksjazfxv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nbksjazfxv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nbksjazfxv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nbksjazfxv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nbksjazfxv .gt_left { text-align: left; }
 #nbksjazfxv .gt_center { text-align: center; }
 #nbksjazfxv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nbksjazfxv .gt_font_normal { font-weight: normal; }
 #nbksjazfxv .gt_font_bold { font-weight: bold; }
 #nbksjazfxv .gt_font_italic { font-style: italic; }
 #nbksjazfxv .gt_super { font-size: 65%; }
 #nbksjazfxv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nbksjazfxv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nbksjazfxv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nbksjazfxv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nbksjazfxv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nbksjazfxv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| year | population | country_name |
|------|------------|--------------|
| 2018 | 918996     | Fiji         |
| 2019 | 918465     | Fiji         |
| 2020 | 920422     | Fiji         |
| 2021 | 924610     | Fiji         |
| 2022 | 929766     | Fiji         |
