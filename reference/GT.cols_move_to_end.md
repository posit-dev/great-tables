# GT.cols_move_to_end()


Move one or more columns to the end.


Usage

``` python
GT.cols_move_to_end(columns)
```


We can easily move set of columns to the beginning of the column series and we only need to specify which `columns`. It's possible to do this upstream of **Great Tables**, however, it is easier with this method and it presents less possibility for error. The ordering of the `columns` that are moved to the end is preserved (same with the ordering of all other columns in the table).


## Parameters


`columns: SelectExpr`  
The columns to target. Can either be a single column name or a series of column names provided in a list.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

For this example, we'll use a portion of the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a simple table. Let's move the `year` column, which is the middle column, to the end of the column series with the [cols_move_to_end()](GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end) method.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Benin"][
    ["country_name", "year", "population"]
].tail(5)

GT(countrypops_mini).cols_move_to_end(columns="year")
```


<style>
#zdizrcapsr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zdizrcapsr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zdizrcapsr p { margin: 0; padding: 0; }
 #zdizrcapsr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zdizrcapsr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zdizrcapsr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zdizrcapsr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zdizrcapsr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zdizrcapsr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zdizrcapsr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zdizrcapsr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zdizrcapsr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zdizrcapsr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zdizrcapsr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zdizrcapsr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zdizrcapsr .gt_spanner_row { border-bottom-style: hidden; }
 #zdizrcapsr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zdizrcapsr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zdizrcapsr .gt_from_md> :first-child { margin-top: 0; }
 #zdizrcapsr .gt_from_md> :last-child { margin-bottom: 0; }
 #zdizrcapsr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zdizrcapsr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zdizrcapsr .gt_indent_1 { text-indent: 5px; }
 #zdizrcapsr .gt_indent_2 { text-indent: calc(5px * 2); }
 #zdizrcapsr .gt_indent_3 { text-indent: calc(5px * 3); }
 #zdizrcapsr .gt_indent_4 { text-indent: calc(5px * 4); }
 #zdizrcapsr .gt_indent_5 { text-indent: calc(5px * 5); }
 #zdizrcapsr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zdizrcapsr .gt_row_group_first td { border-top-width: 2px; }
 #zdizrcapsr .gt_row_group_first th { border-top-width: 2px; }
 #zdizrcapsr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zdizrcapsr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zdizrcapsr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zdizrcapsr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zdizrcapsr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zdizrcapsr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zdizrcapsr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zdizrcapsr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zdizrcapsr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zdizrcapsr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zdizrcapsr .gt_left { text-align: left; }
 #zdizrcapsr .gt_center { text-align: center; }
 #zdizrcapsr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zdizrcapsr .gt_font_normal { font-weight: normal; }
 #zdizrcapsr .gt_font_bold { font-weight: bold; }
 #zdizrcapsr .gt_font_italic { font-style: italic; }
 #zdizrcapsr .gt_super { font-size: 65%; }
 #zdizrcapsr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zdizrcapsr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zdizrcapsr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zdizrcapsr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zdizrcapsr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zdizrcapsr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| country_name | population | year |
|--------------|------------|------|
| Benin        | 11940683   | 2018 |
| Benin        | 12290444   | 2019 |
| Benin        | 12643123   | 2020 |
| Benin        | 12996895   | 2021 |
| Benin        | 13352864   | 2022 |


We can also move multiple columns at a time. With the same [countrypops](data.countrypops.md#great_tables.data.countrypops)-based table (`countrypops_mini`), let's move both the `year` and `country_name` columns to the end of the column series.


``` python
GT(countrypops_mini).cols_move_to_end(columns=["year", "country_name"])
```


<style>
#ztptlaolga table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ztptlaolga thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ztptlaolga p { margin: 0; padding: 0; }
 #ztptlaolga .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ztptlaolga .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ztptlaolga .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ztptlaolga .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ztptlaolga .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ztptlaolga .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ztptlaolga .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ztptlaolga .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ztptlaolga .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ztptlaolga .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ztptlaolga .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ztptlaolga .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ztptlaolga .gt_spanner_row { border-bottom-style: hidden; }
 #ztptlaolga .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ztptlaolga .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ztptlaolga .gt_from_md> :first-child { margin-top: 0; }
 #ztptlaolga .gt_from_md> :last-child { margin-bottom: 0; }
 #ztptlaolga .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ztptlaolga .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ztptlaolga .gt_indent_1 { text-indent: 5px; }
 #ztptlaolga .gt_indent_2 { text-indent: calc(5px * 2); }
 #ztptlaolga .gt_indent_3 { text-indent: calc(5px * 3); }
 #ztptlaolga .gt_indent_4 { text-indent: calc(5px * 4); }
 #ztptlaolga .gt_indent_5 { text-indent: calc(5px * 5); }
 #ztptlaolga .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ztptlaolga .gt_row_group_first td { border-top-width: 2px; }
 #ztptlaolga .gt_row_group_first th { border-top-width: 2px; }
 #ztptlaolga .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ztptlaolga .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ztptlaolga .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ztptlaolga .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ztptlaolga .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ztptlaolga .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ztptlaolga .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ztptlaolga .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ztptlaolga .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ztptlaolga .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ztptlaolga .gt_left { text-align: left; }
 #ztptlaolga .gt_center { text-align: center; }
 #ztptlaolga .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ztptlaolga .gt_font_normal { font-weight: normal; }
 #ztptlaolga .gt_font_bold { font-weight: bold; }
 #ztptlaolga .gt_font_italic { font-style: italic; }
 #ztptlaolga .gt_super { font-size: 65%; }
 #ztptlaolga .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ztptlaolga .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ztptlaolga .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ztptlaolga .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ztptlaolga .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ztptlaolga .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| population | year | country_name |
|------------|------|--------------|
| 11940683   | 2018 | Benin        |
| 12290444   | 2019 | Benin        |
| 12643123   | 2020 | Benin        |
| 12996895   | 2021 | Benin        |
| 13352864   | 2022 | Benin        |
