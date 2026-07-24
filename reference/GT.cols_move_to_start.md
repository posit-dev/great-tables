## GT.cols_move_to_start()


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
#xdvpkqmvvy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xdvpkqmvvy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xdvpkqmvvy p { margin: 0; padding: 0; }
 #xdvpkqmvvy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xdvpkqmvvy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xdvpkqmvvy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xdvpkqmvvy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xdvpkqmvvy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xdvpkqmvvy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xdvpkqmvvy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xdvpkqmvvy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xdvpkqmvvy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xdvpkqmvvy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xdvpkqmvvy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xdvpkqmvvy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xdvpkqmvvy .gt_spanner_row { border-bottom-style: hidden; }
 #xdvpkqmvvy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xdvpkqmvvy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xdvpkqmvvy .gt_from_md> :first-child { margin-top: 0; }
 #xdvpkqmvvy .gt_from_md> :last-child { margin-bottom: 0; }
 #xdvpkqmvvy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xdvpkqmvvy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xdvpkqmvvy .gt_indent_1 { text-indent: 5px; }
 #xdvpkqmvvy .gt_indent_2 { text-indent: calc(5px * 2); }
 #xdvpkqmvvy .gt_indent_3 { text-indent: calc(5px * 3); }
 #xdvpkqmvvy .gt_indent_4 { text-indent: calc(5px * 4); }
 #xdvpkqmvvy .gt_indent_5 { text-indent: calc(5px * 5); }
 #xdvpkqmvvy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xdvpkqmvvy .gt_row_group_first td { border-top-width: 2px; }
 #xdvpkqmvvy .gt_row_group_first th { border-top-width: 2px; }
 #xdvpkqmvvy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xdvpkqmvvy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xdvpkqmvvy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xdvpkqmvvy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xdvpkqmvvy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xdvpkqmvvy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xdvpkqmvvy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xdvpkqmvvy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xdvpkqmvvy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xdvpkqmvvy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xdvpkqmvvy .gt_left { text-align: left; }
 #xdvpkqmvvy .gt_center { text-align: center; }
 #xdvpkqmvvy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xdvpkqmvvy .gt_font_normal { font-weight: normal; }
 #xdvpkqmvvy .gt_font_bold { font-weight: bold; }
 #xdvpkqmvvy .gt_font_italic { font-style: italic; }
 #xdvpkqmvvy .gt_super { font-size: 65%; }
 #xdvpkqmvvy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xdvpkqmvvy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xdvpkqmvvy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xdvpkqmvvy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xdvpkqmvvy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xdvpkqmvvy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fuvskslita table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fuvskslita thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fuvskslita p { margin: 0; padding: 0; }
 #fuvskslita .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fuvskslita .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fuvskslita .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fuvskslita .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fuvskslita .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fuvskslita .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fuvskslita .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fuvskslita .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fuvskslita .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fuvskslita .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fuvskslita .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fuvskslita .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fuvskslita .gt_spanner_row { border-bottom-style: hidden; }
 #fuvskslita .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fuvskslita .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fuvskslita .gt_from_md> :first-child { margin-top: 0; }
 #fuvskslita .gt_from_md> :last-child { margin-bottom: 0; }
 #fuvskslita .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fuvskslita .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fuvskslita .gt_indent_1 { text-indent: 5px; }
 #fuvskslita .gt_indent_2 { text-indent: calc(5px * 2); }
 #fuvskslita .gt_indent_3 { text-indent: calc(5px * 3); }
 #fuvskslita .gt_indent_4 { text-indent: calc(5px * 4); }
 #fuvskslita .gt_indent_5 { text-indent: calc(5px * 5); }
 #fuvskslita .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fuvskslita .gt_row_group_first td { border-top-width: 2px; }
 #fuvskslita .gt_row_group_first th { border-top-width: 2px; }
 #fuvskslita .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fuvskslita .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fuvskslita .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fuvskslita .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fuvskslita .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fuvskslita .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fuvskslita .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fuvskslita .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fuvskslita .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fuvskslita .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fuvskslita .gt_left { text-align: left; }
 #fuvskslita .gt_center { text-align: center; }
 #fuvskslita .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fuvskslita .gt_font_normal { font-weight: normal; }
 #fuvskslita .gt_font_bold { font-weight: bold; }
 #fuvskslita .gt_font_italic { font-style: italic; }
 #fuvskslita .gt_super { font-size: 65%; }
 #fuvskslita .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fuvskslita .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fuvskslita .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fuvskslita .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fuvskslita .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fuvskslita .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| year | population | country_name |
|------|------------|--------------|
| 2018 | 918996     | Fiji         |
| 2019 | 918465     | Fiji         |
| 2020 | 920422     | Fiji         |
| 2021 | 924610     | Fiji         |
| 2022 | 929766     | Fiji         |
