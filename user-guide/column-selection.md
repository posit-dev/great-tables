# Column Selection

Many **Great Tables** methods accept a `columns=` argument for targeting specific columns. Rather than limiting you to a simple list of column names, the package supports a flexible selection system that includes positional indexing, pattern-matching functions, and Polars selectors. This page demonstrates each of these approaches.

As your table-building code grows, hardcoding column names becomes fragile. If a column is renamed or added upstream, your table code breaks silently or raises an error. Pattern-based selection (whether through functions or Polars selectors) makes your code more resilient to upstream changes and more expressive about intent. Instead of listing every column by name, you can declare *what kind* of columns you want (e.g., all numeric columns, all columns starting with a prefix), and the selection adapts automatically as the data evolves.


# Selection Options

The `columns=` argument for methods like [tab_spanner()](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner), [cols_move()](../reference/GT.cols_move.md#great_tables.GT.cols_move), and [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) allows a range of options for selecting columns.

The simplest approach is just a list of strings with the exact column names. However, we can specify columns using any of the following:

- a single string column name.
- an integer for the column's position.
- a list of strings or integers.
- a **Polars** selector.
- a function that takes a string and returns `True` or `False`.


``` python
from great_tables import GT
from great_tables.data import exibble

lil_exibble = exibble[["num", "char", "fctr", "date", "time"]].head(4)
gt_ex = GT(lil_exibble)

gt_ex
```


<style>
#xgxltxidao table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xgxltxidao thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xgxltxidao p { margin: 0; padding: 0; }
 #xgxltxidao .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xgxltxidao .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xgxltxidao .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xgxltxidao .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xgxltxidao .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xgxltxidao .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xgxltxidao .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xgxltxidao .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xgxltxidao .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xgxltxidao .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xgxltxidao .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xgxltxidao .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xgxltxidao .gt_spanner_row { border-bottom-style: hidden; }
 #xgxltxidao .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xgxltxidao .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xgxltxidao .gt_from_md> :first-child { margin-top: 0; }
 #xgxltxidao .gt_from_md> :last-child { margin-bottom: 0; }
 #xgxltxidao .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xgxltxidao .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xgxltxidao .gt_indent_1 { text-indent: 5px; }
 #xgxltxidao .gt_indent_2 { text-indent: calc(5px * 2); }
 #xgxltxidao .gt_indent_3 { text-indent: calc(5px * 3); }
 #xgxltxidao .gt_indent_4 { text-indent: calc(5px * 4); }
 #xgxltxidao .gt_indent_5 { text-indent: calc(5px * 5); }
 #xgxltxidao .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xgxltxidao .gt_row_group_first td { border-top-width: 2px; }
 #xgxltxidao .gt_row_group_first th { border-top-width: 2px; }
 #xgxltxidao .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xgxltxidao .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xgxltxidao .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xgxltxidao .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xgxltxidao .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xgxltxidao .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xgxltxidao .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xgxltxidao .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xgxltxidao .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xgxltxidao .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xgxltxidao .gt_left { text-align: left; }
 #xgxltxidao .gt_center { text-align: center; }
 #xgxltxidao .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xgxltxidao .gt_font_normal { font-weight: normal; }
 #xgxltxidao .gt_font_bold { font-weight: bold; }
 #xgxltxidao .gt_font_italic { font-style: italic; }
 #xgxltxidao .gt_super { font-size: 65%; }
 #xgxltxidao .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xgxltxidao .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xgxltxidao .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xgxltxidao .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xgxltxidao .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xgxltxidao .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | fctr  | date       | time  |
|--------|---------|-------|------------|-------|
| 0.1111 | apricot | one   | 2015-01-15 | 13:35 |
| 2.222  | banana  | two   | 2015-02-15 | 14:40 |
| 33.33  | coconut | three | 2015-03-15 | 15:45 |
| 444.4  | durian  | four  | 2015-04-15 | 16:50 |


This five-column table will serve as the basis for demonstrating each selection approach.


# Using integers

We can use a list of strings or integers to select columns by name or position, respectively.


``` python
gt_ex.cols_move_to_start(columns=["date", 1, -1])
```


<style>
#rixpihfoiy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rixpihfoiy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rixpihfoiy p { margin: 0; padding: 0; }
 #rixpihfoiy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rixpihfoiy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rixpihfoiy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rixpihfoiy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rixpihfoiy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rixpihfoiy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rixpihfoiy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rixpihfoiy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rixpihfoiy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rixpihfoiy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rixpihfoiy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rixpihfoiy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rixpihfoiy .gt_spanner_row { border-bottom-style: hidden; }
 #rixpihfoiy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rixpihfoiy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rixpihfoiy .gt_from_md> :first-child { margin-top: 0; }
 #rixpihfoiy .gt_from_md> :last-child { margin-bottom: 0; }
 #rixpihfoiy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rixpihfoiy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rixpihfoiy .gt_indent_1 { text-indent: 5px; }
 #rixpihfoiy .gt_indent_2 { text-indent: calc(5px * 2); }
 #rixpihfoiy .gt_indent_3 { text-indent: calc(5px * 3); }
 #rixpihfoiy .gt_indent_4 { text-indent: calc(5px * 4); }
 #rixpihfoiy .gt_indent_5 { text-indent: calc(5px * 5); }
 #rixpihfoiy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rixpihfoiy .gt_row_group_first td { border-top-width: 2px; }
 #rixpihfoiy .gt_row_group_first th { border-top-width: 2px; }
 #rixpihfoiy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rixpihfoiy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rixpihfoiy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rixpihfoiy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rixpihfoiy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rixpihfoiy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rixpihfoiy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rixpihfoiy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rixpihfoiy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rixpihfoiy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rixpihfoiy .gt_left { text-align: left; }
 #rixpihfoiy .gt_center { text-align: center; }
 #rixpihfoiy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rixpihfoiy .gt_font_normal { font-weight: normal; }
 #rixpihfoiy .gt_font_bold { font-weight: bold; }
 #rixpihfoiy .gt_font_italic { font-style: italic; }
 #rixpihfoiy .gt_super { font-size: 65%; }
 #rixpihfoiy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rixpihfoiy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rixpihfoiy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rixpihfoiy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rixpihfoiy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rixpihfoiy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | char    | time  | num    | fctr  |
|------------|---------|-------|--------|-------|
| 2015-01-15 | apricot | 13:35 | 0.1111 | one   |
| 2015-02-15 | banana  | 14:40 | 2.222  | two   |
| 2015-03-15 | coconut | 15:45 | 33.33  | three |
| 2015-04-15 | durian  | 16:50 | 444.4  | four  |


Note the code above moved the following columns:

- The string `"date"` matched the column of the same name.
- The integer `1` matched the second column (this is similar to list indexing).
- The integer `-1` matched the last column.

Moreover, the order of the list defines the order of selected columns. In this case, `"data"` was the first entry, so it's the very first column in the new table.


# Using **Polars** selectors

When using a **Polars** DataFrame, you can select columns using [**Polars** selectors](https://pola-rs.github.io/polars/py-polars/html/reference/selectors.html). The example below uses **Polars** selectors to move all columns that start with `"c"` or `"f"` to the start of the table.


``` python
import polars as pl
import polars.selectors as cs

pl_df = pl.from_pandas(lil_exibble)

GT(pl_df).cols_move_to_start(columns=cs.starts_with("c") | cs.starts_with("f"))
```


<style>
#rotsvphqpo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rotsvphqpo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rotsvphqpo p { margin: 0; padding: 0; }
 #rotsvphqpo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rotsvphqpo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rotsvphqpo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rotsvphqpo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rotsvphqpo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rotsvphqpo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rotsvphqpo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rotsvphqpo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rotsvphqpo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rotsvphqpo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rotsvphqpo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rotsvphqpo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rotsvphqpo .gt_spanner_row { border-bottom-style: hidden; }
 #rotsvphqpo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rotsvphqpo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rotsvphqpo .gt_from_md> :first-child { margin-top: 0; }
 #rotsvphqpo .gt_from_md> :last-child { margin-bottom: 0; }
 #rotsvphqpo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rotsvphqpo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rotsvphqpo .gt_indent_1 { text-indent: 5px; }
 #rotsvphqpo .gt_indent_2 { text-indent: calc(5px * 2); }
 #rotsvphqpo .gt_indent_3 { text-indent: calc(5px * 3); }
 #rotsvphqpo .gt_indent_4 { text-indent: calc(5px * 4); }
 #rotsvphqpo .gt_indent_5 { text-indent: calc(5px * 5); }
 #rotsvphqpo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rotsvphqpo .gt_row_group_first td { border-top-width: 2px; }
 #rotsvphqpo .gt_row_group_first th { border-top-width: 2px; }
 #rotsvphqpo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rotsvphqpo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rotsvphqpo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rotsvphqpo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rotsvphqpo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rotsvphqpo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rotsvphqpo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rotsvphqpo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rotsvphqpo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rotsvphqpo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rotsvphqpo .gt_left { text-align: left; }
 #rotsvphqpo .gt_center { text-align: center; }
 #rotsvphqpo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rotsvphqpo .gt_font_normal { font-weight: normal; }
 #rotsvphqpo .gt_font_bold { font-weight: bold; }
 #rotsvphqpo .gt_font_italic { font-style: italic; }
 #rotsvphqpo .gt_super { font-size: 65%; }
 #rotsvphqpo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rotsvphqpo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rotsvphqpo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rotsvphqpo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rotsvphqpo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rotsvphqpo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| char    | fctr  | num    | date       | time  |
|---------|-------|--------|------------|-------|
| apricot | one   | 0.1111 | 2015-01-15 | 13:35 |
| banana  | two   | 2.222  | 2015-02-15 | 14:40 |
| coconut | three | 33.33  | 2015-03-15 | 15:45 |
| durian  | four  | 444.4  | 2015-04-15 | 16:50 |


In general, selection should match the behaviors of the **Polars** `DataFrame.select()` method.


``` python
pl_df.select(cs.starts_with("c") | cs.starts_with("f")).columns
```


    ['char', 'fctr']


See the [Selectors page in the polars docs](https://pola-rs.github.io/polars/py-polars/html/reference/selectors.html) for more information on this.


# Using functions

A function can be used to select columns. It should take a column name as a string and return `True` or `False`.


``` python
gt_ex.cols_move_to_start(columns=lambda x: "c" in x)
```


<style>
#qozzihyxed table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qozzihyxed thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qozzihyxed p { margin: 0; padding: 0; }
 #qozzihyxed .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qozzihyxed .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qozzihyxed .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qozzihyxed .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qozzihyxed .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qozzihyxed .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qozzihyxed .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qozzihyxed .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qozzihyxed .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qozzihyxed .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qozzihyxed .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qozzihyxed .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qozzihyxed .gt_spanner_row { border-bottom-style: hidden; }
 #qozzihyxed .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qozzihyxed .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qozzihyxed .gt_from_md> :first-child { margin-top: 0; }
 #qozzihyxed .gt_from_md> :last-child { margin-bottom: 0; }
 #qozzihyxed .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qozzihyxed .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qozzihyxed .gt_indent_1 { text-indent: 5px; }
 #qozzihyxed .gt_indent_2 { text-indent: calc(5px * 2); }
 #qozzihyxed .gt_indent_3 { text-indent: calc(5px * 3); }
 #qozzihyxed .gt_indent_4 { text-indent: calc(5px * 4); }
 #qozzihyxed .gt_indent_5 { text-indent: calc(5px * 5); }
 #qozzihyxed .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qozzihyxed .gt_row_group_first td { border-top-width: 2px; }
 #qozzihyxed .gt_row_group_first th { border-top-width: 2px; }
 #qozzihyxed .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qozzihyxed .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qozzihyxed .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qozzihyxed .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qozzihyxed .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qozzihyxed .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qozzihyxed .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qozzihyxed .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qozzihyxed .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qozzihyxed .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qozzihyxed .gt_left { text-align: left; }
 #qozzihyxed .gt_center { text-align: center; }
 #qozzihyxed .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qozzihyxed .gt_font_normal { font-weight: normal; }
 #qozzihyxed .gt_font_bold { font-weight: bold; }
 #qozzihyxed .gt_font_italic { font-style: italic; }
 #qozzihyxed .gt_super { font-size: 65%; }
 #qozzihyxed .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qozzihyxed .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qozzihyxed .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qozzihyxed .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qozzihyxed .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qozzihyxed .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| char    | fctr  | num    | date       | time  |
|---------|-------|--------|------------|-------|
| apricot | one   | 0.1111 | 2015-01-15 | 13:35 |
| banana  | two   | 2.222  | 2015-02-15 | 14:40 |
| coconut | three | 33.33  | 2015-03-15 | 15:45 |
| durian  | four  | 444.4  | 2015-04-15 | 16:50 |


To summarize when to reach for each approach: use a plain list of names when you know exactly which columns you want and the list is short. Use Polars selectors when you want to match by dtype, prefix, suffix, or other structural properties of the columns. Use a function when you need custom logic that doesn't fit neatly into a selector (e.g., matching against an external list or applying a complex naming convention rule).

These selection methods work consistently across all **Great Tables** methods that accept a `columns=` argument. Whether you prefer explicit column names, positional indexing, Polars selectors, or custom functions, you can choose the approach that best fits your workflow and data.
