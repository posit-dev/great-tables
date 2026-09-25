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
#lxapekpbks table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lxapekpbks thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lxapekpbks p { margin: 0; padding: 0; }
 #lxapekpbks .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lxapekpbks .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lxapekpbks .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lxapekpbks .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lxapekpbks .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lxapekpbks .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lxapekpbks .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lxapekpbks .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lxapekpbks .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lxapekpbks .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lxapekpbks .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lxapekpbks .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lxapekpbks .gt_spanner_row { border-bottom-style: hidden; }
 #lxapekpbks .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lxapekpbks .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lxapekpbks .gt_from_md> :first-child { margin-top: 0; }
 #lxapekpbks .gt_from_md> :last-child { margin-bottom: 0; }
 #lxapekpbks .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lxapekpbks .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lxapekpbks .gt_indent_1 { text-indent: 5px; }
 #lxapekpbks .gt_indent_2 { text-indent: calc(5px * 2); }
 #lxapekpbks .gt_indent_3 { text-indent: calc(5px * 3); }
 #lxapekpbks .gt_indent_4 { text-indent: calc(5px * 4); }
 #lxapekpbks .gt_indent_5 { text-indent: calc(5px * 5); }
 #lxapekpbks .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lxapekpbks .gt_row_group_first td { border-top-width: 2px; }
 #lxapekpbks .gt_row_group_first th { border-top-width: 2px; }
 #lxapekpbks .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lxapekpbks .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lxapekpbks .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lxapekpbks .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lxapekpbks .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lxapekpbks .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lxapekpbks .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lxapekpbks .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lxapekpbks .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lxapekpbks .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lxapekpbks .gt_left { text-align: left; }
 #lxapekpbks .gt_center { text-align: center; }
 #lxapekpbks .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lxapekpbks .gt_font_normal { font-weight: normal; }
 #lxapekpbks .gt_font_bold { font-weight: bold; }
 #lxapekpbks .gt_font_italic { font-style: italic; }
 #lxapekpbks .gt_super { font-size: 65%; }
 #lxapekpbks .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lxapekpbks .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lxapekpbks .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lxapekpbks .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lxapekpbks .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lxapekpbks .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mlfjpxyzaz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mlfjpxyzaz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mlfjpxyzaz p { margin: 0; padding: 0; }
 #mlfjpxyzaz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mlfjpxyzaz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mlfjpxyzaz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mlfjpxyzaz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mlfjpxyzaz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mlfjpxyzaz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mlfjpxyzaz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mlfjpxyzaz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mlfjpxyzaz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mlfjpxyzaz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mlfjpxyzaz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mlfjpxyzaz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mlfjpxyzaz .gt_spanner_row { border-bottom-style: hidden; }
 #mlfjpxyzaz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mlfjpxyzaz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mlfjpxyzaz .gt_from_md> :first-child { margin-top: 0; }
 #mlfjpxyzaz .gt_from_md> :last-child { margin-bottom: 0; }
 #mlfjpxyzaz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mlfjpxyzaz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mlfjpxyzaz .gt_indent_1 { text-indent: 5px; }
 #mlfjpxyzaz .gt_indent_2 { text-indent: calc(5px * 2); }
 #mlfjpxyzaz .gt_indent_3 { text-indent: calc(5px * 3); }
 #mlfjpxyzaz .gt_indent_4 { text-indent: calc(5px * 4); }
 #mlfjpxyzaz .gt_indent_5 { text-indent: calc(5px * 5); }
 #mlfjpxyzaz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mlfjpxyzaz .gt_row_group_first td { border-top-width: 2px; }
 #mlfjpxyzaz .gt_row_group_first th { border-top-width: 2px; }
 #mlfjpxyzaz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mlfjpxyzaz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mlfjpxyzaz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mlfjpxyzaz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mlfjpxyzaz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mlfjpxyzaz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mlfjpxyzaz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mlfjpxyzaz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mlfjpxyzaz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mlfjpxyzaz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mlfjpxyzaz .gt_left { text-align: left; }
 #mlfjpxyzaz .gt_center { text-align: center; }
 #mlfjpxyzaz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mlfjpxyzaz .gt_font_normal { font-weight: normal; }
 #mlfjpxyzaz .gt_font_bold { font-weight: bold; }
 #mlfjpxyzaz .gt_font_italic { font-style: italic; }
 #mlfjpxyzaz .gt_super { font-size: 65%; }
 #mlfjpxyzaz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mlfjpxyzaz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mlfjpxyzaz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mlfjpxyzaz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mlfjpxyzaz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mlfjpxyzaz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ohzivwtmef table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ohzivwtmef thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ohzivwtmef p { margin: 0; padding: 0; }
 #ohzivwtmef .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ohzivwtmef .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ohzivwtmef .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ohzivwtmef .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ohzivwtmef .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ohzivwtmef .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ohzivwtmef .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ohzivwtmef .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ohzivwtmef .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ohzivwtmef .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ohzivwtmef .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ohzivwtmef .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ohzivwtmef .gt_spanner_row { border-bottom-style: hidden; }
 #ohzivwtmef .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ohzivwtmef .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ohzivwtmef .gt_from_md> :first-child { margin-top: 0; }
 #ohzivwtmef .gt_from_md> :last-child { margin-bottom: 0; }
 #ohzivwtmef .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ohzivwtmef .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ohzivwtmef .gt_indent_1 { text-indent: 5px; }
 #ohzivwtmef .gt_indent_2 { text-indent: calc(5px * 2); }
 #ohzivwtmef .gt_indent_3 { text-indent: calc(5px * 3); }
 #ohzivwtmef .gt_indent_4 { text-indent: calc(5px * 4); }
 #ohzivwtmef .gt_indent_5 { text-indent: calc(5px * 5); }
 #ohzivwtmef .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ohzivwtmef .gt_row_group_first td { border-top-width: 2px; }
 #ohzivwtmef .gt_row_group_first th { border-top-width: 2px; }
 #ohzivwtmef .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ohzivwtmef .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ohzivwtmef .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ohzivwtmef .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ohzivwtmef .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ohzivwtmef .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ohzivwtmef .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ohzivwtmef .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ohzivwtmef .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ohzivwtmef .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ohzivwtmef .gt_left { text-align: left; }
 #ohzivwtmef .gt_center { text-align: center; }
 #ohzivwtmef .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ohzivwtmef .gt_font_normal { font-weight: normal; }
 #ohzivwtmef .gt_font_bold { font-weight: bold; }
 #ohzivwtmef .gt_font_italic { font-style: italic; }
 #ohzivwtmef .gt_super { font-size: 65%; }
 #ohzivwtmef .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ohzivwtmef .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ohzivwtmef .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ohzivwtmef .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ohzivwtmef .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ohzivwtmef .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bpshoxvigp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bpshoxvigp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bpshoxvigp p { margin: 0; padding: 0; }
 #bpshoxvigp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bpshoxvigp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bpshoxvigp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bpshoxvigp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bpshoxvigp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpshoxvigp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpshoxvigp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpshoxvigp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bpshoxvigp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bpshoxvigp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bpshoxvigp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bpshoxvigp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bpshoxvigp .gt_spanner_row { border-bottom-style: hidden; }
 #bpshoxvigp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bpshoxvigp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bpshoxvigp .gt_from_md> :first-child { margin-top: 0; }
 #bpshoxvigp .gt_from_md> :last-child { margin-bottom: 0; }
 #bpshoxvigp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bpshoxvigp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bpshoxvigp .gt_indent_1 { text-indent: 5px; }
 #bpshoxvigp .gt_indent_2 { text-indent: calc(5px * 2); }
 #bpshoxvigp .gt_indent_3 { text-indent: calc(5px * 3); }
 #bpshoxvigp .gt_indent_4 { text-indent: calc(5px * 4); }
 #bpshoxvigp .gt_indent_5 { text-indent: calc(5px * 5); }
 #bpshoxvigp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bpshoxvigp .gt_row_group_first td { border-top-width: 2px; }
 #bpshoxvigp .gt_row_group_first th { border-top-width: 2px; }
 #bpshoxvigp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bpshoxvigp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpshoxvigp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpshoxvigp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bpshoxvigp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpshoxvigp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpshoxvigp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bpshoxvigp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bpshoxvigp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpshoxvigp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpshoxvigp .gt_left { text-align: left; }
 #bpshoxvigp .gt_center { text-align: center; }
 #bpshoxvigp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bpshoxvigp .gt_font_normal { font-weight: normal; }
 #bpshoxvigp .gt_font_bold { font-weight: bold; }
 #bpshoxvigp .gt_font_italic { font-style: italic; }
 #bpshoxvigp .gt_super { font-size: 65%; }
 #bpshoxvigp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpshoxvigp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bpshoxvigp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpshoxvigp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpshoxvigp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bpshoxvigp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| char    | fctr  | num    | date       | time  |
|---------|-------|--------|------------|-------|
| apricot | one   | 0.1111 | 2015-01-15 | 13:35 |
| banana  | two   | 2.222  | 2015-02-15 | 14:40 |
| coconut | three | 33.33  | 2015-03-15 | 15:45 |
| durian  | four  | 444.4  | 2015-04-15 | 16:50 |


To summarize when to reach for each approach: use a plain list of names when you know exactly which columns you want and the list is short. Use Polars selectors when you want to match by dtype, prefix, suffix, or other structural properties of the columns. Use a function when you need custom logic that doesn't fit neatly into a selector (e.g., matching against an external list or applying a complex naming convention rule).

These selection methods work consistently across all **Great Tables** methods that accept a `columns=` argument. Whether you prefer explicit column names, positional indexing, Polars selectors, or custom functions, you can choose the approach that best fits your workflow and data.
