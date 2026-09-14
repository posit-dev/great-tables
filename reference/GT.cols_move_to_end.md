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
#muewfnsdzw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#muewfnsdzw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#muewfnsdzw p { margin: 0; padding: 0; }
 #muewfnsdzw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #muewfnsdzw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #muewfnsdzw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #muewfnsdzw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #muewfnsdzw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muewfnsdzw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muewfnsdzw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muewfnsdzw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #muewfnsdzw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #muewfnsdzw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #muewfnsdzw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #muewfnsdzw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #muewfnsdzw .gt_spanner_row { border-bottom-style: hidden; }
 #muewfnsdzw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #muewfnsdzw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #muewfnsdzw .gt_from_md> :first-child { margin-top: 0; }
 #muewfnsdzw .gt_from_md> :last-child { margin-bottom: 0; }
 #muewfnsdzw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #muewfnsdzw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #muewfnsdzw .gt_indent_1 { text-indent: 5px; }
 #muewfnsdzw .gt_indent_2 { text-indent: calc(5px * 2); }
 #muewfnsdzw .gt_indent_3 { text-indent: calc(5px * 3); }
 #muewfnsdzw .gt_indent_4 { text-indent: calc(5px * 4); }
 #muewfnsdzw .gt_indent_5 { text-indent: calc(5px * 5); }
 #muewfnsdzw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #muewfnsdzw .gt_row_group_first td { border-top-width: 2px; }
 #muewfnsdzw .gt_row_group_first th { border-top-width: 2px; }
 #muewfnsdzw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #muewfnsdzw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muewfnsdzw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muewfnsdzw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #muewfnsdzw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muewfnsdzw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muewfnsdzw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #muewfnsdzw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #muewfnsdzw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muewfnsdzw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muewfnsdzw .gt_left { text-align: left; }
 #muewfnsdzw .gt_center { text-align: center; }
 #muewfnsdzw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #muewfnsdzw .gt_font_normal { font-weight: normal; }
 #muewfnsdzw .gt_font_bold { font-weight: bold; }
 #muewfnsdzw .gt_font_italic { font-style: italic; }
 #muewfnsdzw .gt_super { font-size: 65%; }
 #muewfnsdzw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muewfnsdzw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #muewfnsdzw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muewfnsdzw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muewfnsdzw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #muewfnsdzw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qiryozqyhw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qiryozqyhw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qiryozqyhw p { margin: 0; padding: 0; }
 #qiryozqyhw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qiryozqyhw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qiryozqyhw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qiryozqyhw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qiryozqyhw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qiryozqyhw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qiryozqyhw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qiryozqyhw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qiryozqyhw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qiryozqyhw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qiryozqyhw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qiryozqyhw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qiryozqyhw .gt_spanner_row { border-bottom-style: hidden; }
 #qiryozqyhw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qiryozqyhw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qiryozqyhw .gt_from_md> :first-child { margin-top: 0; }
 #qiryozqyhw .gt_from_md> :last-child { margin-bottom: 0; }
 #qiryozqyhw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qiryozqyhw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qiryozqyhw .gt_indent_1 { text-indent: 5px; }
 #qiryozqyhw .gt_indent_2 { text-indent: calc(5px * 2); }
 #qiryozqyhw .gt_indent_3 { text-indent: calc(5px * 3); }
 #qiryozqyhw .gt_indent_4 { text-indent: calc(5px * 4); }
 #qiryozqyhw .gt_indent_5 { text-indent: calc(5px * 5); }
 #qiryozqyhw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qiryozqyhw .gt_row_group_first td { border-top-width: 2px; }
 #qiryozqyhw .gt_row_group_first th { border-top-width: 2px; }
 #qiryozqyhw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qiryozqyhw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qiryozqyhw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qiryozqyhw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qiryozqyhw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qiryozqyhw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qiryozqyhw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qiryozqyhw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qiryozqyhw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qiryozqyhw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qiryozqyhw .gt_left { text-align: left; }
 #qiryozqyhw .gt_center { text-align: center; }
 #qiryozqyhw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qiryozqyhw .gt_font_normal { font-weight: normal; }
 #qiryozqyhw .gt_font_bold { font-weight: bold; }
 #qiryozqyhw .gt_font_italic { font-style: italic; }
 #qiryozqyhw .gt_super { font-size: 65%; }
 #qiryozqyhw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qiryozqyhw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qiryozqyhw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qiryozqyhw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qiryozqyhw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qiryozqyhw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| population | year | country_name |
|------------|------|--------------|
| 11940683   | 2018 | Benin        |
| 12290444   | 2019 | Benin        |
| 12643123   | 2020 | Benin        |
| 12996895   | 2021 | Benin        |
| 13352864   | 2022 | Benin        |
