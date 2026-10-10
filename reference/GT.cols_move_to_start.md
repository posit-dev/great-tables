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
#gpeludbkqu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gpeludbkqu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gpeludbkqu p { margin: 0; padding: 0; }
 #gpeludbkqu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gpeludbkqu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gpeludbkqu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gpeludbkqu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gpeludbkqu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gpeludbkqu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gpeludbkqu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gpeludbkqu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gpeludbkqu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gpeludbkqu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gpeludbkqu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gpeludbkqu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gpeludbkqu .gt_spanner_row { border-bottom-style: hidden; }
 #gpeludbkqu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gpeludbkqu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gpeludbkqu .gt_from_md> :first-child { margin-top: 0; }
 #gpeludbkqu .gt_from_md> :last-child { margin-bottom: 0; }
 #gpeludbkqu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gpeludbkqu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gpeludbkqu .gt_indent_1 { text-indent: 5px; }
 #gpeludbkqu .gt_indent_2 { text-indent: calc(5px * 2); }
 #gpeludbkqu .gt_indent_3 { text-indent: calc(5px * 3); }
 #gpeludbkqu .gt_indent_4 { text-indent: calc(5px * 4); }
 #gpeludbkqu .gt_indent_5 { text-indent: calc(5px * 5); }
 #gpeludbkqu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gpeludbkqu .gt_row_group_first td { border-top-width: 2px; }
 #gpeludbkqu .gt_row_group_first th { border-top-width: 2px; }
 #gpeludbkqu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gpeludbkqu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gpeludbkqu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gpeludbkqu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gpeludbkqu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gpeludbkqu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gpeludbkqu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gpeludbkqu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gpeludbkqu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gpeludbkqu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gpeludbkqu .gt_left { text-align: left; }
 #gpeludbkqu .gt_center { text-align: center; }
 #gpeludbkqu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gpeludbkqu .gt_font_normal { font-weight: normal; }
 #gpeludbkqu .gt_font_bold { font-weight: bold; }
 #gpeludbkqu .gt_font_italic { font-style: italic; }
 #gpeludbkqu .gt_super { font-size: 65%; }
 #gpeludbkqu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gpeludbkqu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gpeludbkqu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gpeludbkqu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gpeludbkqu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gpeludbkqu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ixjzmgbarl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ixjzmgbarl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ixjzmgbarl p { margin: 0; padding: 0; }
 #ixjzmgbarl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ixjzmgbarl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ixjzmgbarl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ixjzmgbarl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ixjzmgbarl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ixjzmgbarl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixjzmgbarl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ixjzmgbarl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ixjzmgbarl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ixjzmgbarl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ixjzmgbarl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ixjzmgbarl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ixjzmgbarl .gt_spanner_row { border-bottom-style: hidden; }
 #ixjzmgbarl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ixjzmgbarl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ixjzmgbarl .gt_from_md> :first-child { margin-top: 0; }
 #ixjzmgbarl .gt_from_md> :last-child { margin-bottom: 0; }
 #ixjzmgbarl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ixjzmgbarl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ixjzmgbarl .gt_indent_1 { text-indent: 5px; }
 #ixjzmgbarl .gt_indent_2 { text-indent: calc(5px * 2); }
 #ixjzmgbarl .gt_indent_3 { text-indent: calc(5px * 3); }
 #ixjzmgbarl .gt_indent_4 { text-indent: calc(5px * 4); }
 #ixjzmgbarl .gt_indent_5 { text-indent: calc(5px * 5); }
 #ixjzmgbarl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ixjzmgbarl .gt_row_group_first td { border-top-width: 2px; }
 #ixjzmgbarl .gt_row_group_first th { border-top-width: 2px; }
 #ixjzmgbarl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ixjzmgbarl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixjzmgbarl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ixjzmgbarl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ixjzmgbarl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixjzmgbarl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ixjzmgbarl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ixjzmgbarl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ixjzmgbarl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixjzmgbarl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ixjzmgbarl .gt_left { text-align: left; }
 #ixjzmgbarl .gt_center { text-align: center; }
 #ixjzmgbarl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ixjzmgbarl .gt_font_normal { font-weight: normal; }
 #ixjzmgbarl .gt_font_bold { font-weight: bold; }
 #ixjzmgbarl .gt_font_italic { font-style: italic; }
 #ixjzmgbarl .gt_super { font-size: 65%; }
 #ixjzmgbarl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixjzmgbarl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ixjzmgbarl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixjzmgbarl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ixjzmgbarl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ixjzmgbarl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| year | population | country_name |
|------|------------|--------------|
| 2018 | 918996     | Fiji         |
| 2019 | 918465     | Fiji         |
| 2020 | 920422     | Fiji         |
| 2021 | 924610     | Fiji         |
| 2022 | 929766     | Fiji         |
