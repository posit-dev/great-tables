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
#avgplezvru table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#avgplezvru thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#avgplezvru p { margin: 0; padding: 0; }
 #avgplezvru .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #avgplezvru .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #avgplezvru .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #avgplezvru .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #avgplezvru .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #avgplezvru .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #avgplezvru .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #avgplezvru .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #avgplezvru .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #avgplezvru .gt_column_spanner_outer:first-child { padding-left: 0; }
 #avgplezvru .gt_column_spanner_outer:last-child { padding-right: 0; }
 #avgplezvru .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #avgplezvru .gt_spanner_row { border-bottom-style: hidden; }
 #avgplezvru .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #avgplezvru .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #avgplezvru .gt_from_md> :first-child { margin-top: 0; }
 #avgplezvru .gt_from_md> :last-child { margin-bottom: 0; }
 #avgplezvru .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #avgplezvru .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #avgplezvru .gt_indent_1 { text-indent: 5px; }
 #avgplezvru .gt_indent_2 { text-indent: calc(5px * 2); }
 #avgplezvru .gt_indent_3 { text-indent: calc(5px * 3); }
 #avgplezvru .gt_indent_4 { text-indent: calc(5px * 4); }
 #avgplezvru .gt_indent_5 { text-indent: calc(5px * 5); }
 #avgplezvru .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #avgplezvru .gt_row_group_first td { border-top-width: 2px; }
 #avgplezvru .gt_row_group_first th { border-top-width: 2px; }
 #avgplezvru .gt_striped { color: #333333; background-color: #F4F4F4; }
 #avgplezvru .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #avgplezvru .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #avgplezvru .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #avgplezvru .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #avgplezvru .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #avgplezvru .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #avgplezvru .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #avgplezvru .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #avgplezvru .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #avgplezvru .gt_left { text-align: left; }
 #avgplezvru .gt_center { text-align: center; }
 #avgplezvru .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #avgplezvru .gt_font_normal { font-weight: normal; }
 #avgplezvru .gt_font_bold { font-weight: bold; }
 #avgplezvru .gt_font_italic { font-style: italic; }
 #avgplezvru .gt_super { font-size: 65%; }
 #avgplezvru .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #avgplezvru .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #avgplezvru .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #avgplezvru .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #avgplezvru .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #avgplezvru .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ivanajemau table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ivanajemau thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ivanajemau p { margin: 0; padding: 0; }
 #ivanajemau .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ivanajemau .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ivanajemau .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ivanajemau .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ivanajemau .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ivanajemau .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ivanajemau .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ivanajemau .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ivanajemau .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ivanajemau .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ivanajemau .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ivanajemau .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ivanajemau .gt_spanner_row { border-bottom-style: hidden; }
 #ivanajemau .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ivanajemau .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ivanajemau .gt_from_md> :first-child { margin-top: 0; }
 #ivanajemau .gt_from_md> :last-child { margin-bottom: 0; }
 #ivanajemau .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ivanajemau .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ivanajemau .gt_indent_1 { text-indent: 5px; }
 #ivanajemau .gt_indent_2 { text-indent: calc(5px * 2); }
 #ivanajemau .gt_indent_3 { text-indent: calc(5px * 3); }
 #ivanajemau .gt_indent_4 { text-indent: calc(5px * 4); }
 #ivanajemau .gt_indent_5 { text-indent: calc(5px * 5); }
 #ivanajemau .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ivanajemau .gt_row_group_first td { border-top-width: 2px; }
 #ivanajemau .gt_row_group_first th { border-top-width: 2px; }
 #ivanajemau .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ivanajemau .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ivanajemau .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ivanajemau .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ivanajemau .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ivanajemau .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ivanajemau .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ivanajemau .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ivanajemau .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ivanajemau .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ivanajemau .gt_left { text-align: left; }
 #ivanajemau .gt_center { text-align: center; }
 #ivanajemau .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ivanajemau .gt_font_normal { font-weight: normal; }
 #ivanajemau .gt_font_bold { font-weight: bold; }
 #ivanajemau .gt_font_italic { font-style: italic; }
 #ivanajemau .gt_super { font-size: 65%; }
 #ivanajemau .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ivanajemau .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ivanajemau .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ivanajemau .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ivanajemau .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ivanajemau .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qeiqvahfqq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qeiqvahfqq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qeiqvahfqq p { margin: 0; padding: 0; }
 #qeiqvahfqq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qeiqvahfqq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qeiqvahfqq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qeiqvahfqq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qeiqvahfqq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qeiqvahfqq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeiqvahfqq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qeiqvahfqq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qeiqvahfqq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qeiqvahfqq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qeiqvahfqq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qeiqvahfqq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qeiqvahfqq .gt_spanner_row { border-bottom-style: hidden; }
 #qeiqvahfqq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qeiqvahfqq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qeiqvahfqq .gt_from_md> :first-child { margin-top: 0; }
 #qeiqvahfqq .gt_from_md> :last-child { margin-bottom: 0; }
 #qeiqvahfqq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qeiqvahfqq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qeiqvahfqq .gt_indent_1 { text-indent: 5px; }
 #qeiqvahfqq .gt_indent_2 { text-indent: calc(5px * 2); }
 #qeiqvahfqq .gt_indent_3 { text-indent: calc(5px * 3); }
 #qeiqvahfqq .gt_indent_4 { text-indent: calc(5px * 4); }
 #qeiqvahfqq .gt_indent_5 { text-indent: calc(5px * 5); }
 #qeiqvahfqq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qeiqvahfqq .gt_row_group_first td { border-top-width: 2px; }
 #qeiqvahfqq .gt_row_group_first th { border-top-width: 2px; }
 #qeiqvahfqq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qeiqvahfqq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeiqvahfqq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qeiqvahfqq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qeiqvahfqq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeiqvahfqq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qeiqvahfqq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qeiqvahfqq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qeiqvahfqq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeiqvahfqq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qeiqvahfqq .gt_left { text-align: left; }
 #qeiqvahfqq .gt_center { text-align: center; }
 #qeiqvahfqq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qeiqvahfqq .gt_font_normal { font-weight: normal; }
 #qeiqvahfqq .gt_font_bold { font-weight: bold; }
 #qeiqvahfqq .gt_font_italic { font-style: italic; }
 #qeiqvahfqq .gt_super { font-size: 65%; }
 #qeiqvahfqq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeiqvahfqq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qeiqvahfqq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeiqvahfqq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qeiqvahfqq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qeiqvahfqq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ugxrjkcxkj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ugxrjkcxkj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ugxrjkcxkj p { margin: 0; padding: 0; }
 #ugxrjkcxkj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ugxrjkcxkj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ugxrjkcxkj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ugxrjkcxkj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ugxrjkcxkj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ugxrjkcxkj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ugxrjkcxkj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ugxrjkcxkj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ugxrjkcxkj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ugxrjkcxkj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ugxrjkcxkj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ugxrjkcxkj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ugxrjkcxkj .gt_spanner_row { border-bottom-style: hidden; }
 #ugxrjkcxkj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ugxrjkcxkj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ugxrjkcxkj .gt_from_md> :first-child { margin-top: 0; }
 #ugxrjkcxkj .gt_from_md> :last-child { margin-bottom: 0; }
 #ugxrjkcxkj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ugxrjkcxkj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ugxrjkcxkj .gt_indent_1 { text-indent: 5px; }
 #ugxrjkcxkj .gt_indent_2 { text-indent: calc(5px * 2); }
 #ugxrjkcxkj .gt_indent_3 { text-indent: calc(5px * 3); }
 #ugxrjkcxkj .gt_indent_4 { text-indent: calc(5px * 4); }
 #ugxrjkcxkj .gt_indent_5 { text-indent: calc(5px * 5); }
 #ugxrjkcxkj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ugxrjkcxkj .gt_row_group_first td { border-top-width: 2px; }
 #ugxrjkcxkj .gt_row_group_first th { border-top-width: 2px; }
 #ugxrjkcxkj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ugxrjkcxkj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ugxrjkcxkj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ugxrjkcxkj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ugxrjkcxkj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ugxrjkcxkj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ugxrjkcxkj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ugxrjkcxkj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ugxrjkcxkj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ugxrjkcxkj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ugxrjkcxkj .gt_left { text-align: left; }
 #ugxrjkcxkj .gt_center { text-align: center; }
 #ugxrjkcxkj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ugxrjkcxkj .gt_font_normal { font-weight: normal; }
 #ugxrjkcxkj .gt_font_bold { font-weight: bold; }
 #ugxrjkcxkj .gt_font_italic { font-style: italic; }
 #ugxrjkcxkj .gt_super { font-size: 65%; }
 #ugxrjkcxkj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ugxrjkcxkj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ugxrjkcxkj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ugxrjkcxkj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ugxrjkcxkj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ugxrjkcxkj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| char    | fctr  | num    | date       | time  |
|---------|-------|--------|------------|-------|
| apricot | one   | 0.1111 | 2015-01-15 | 13:35 |
| banana  | two   | 2.222  | 2015-02-15 | 14:40 |
| coconut | three | 33.33  | 2015-03-15 | 15:45 |
| durian  | four  | 444.4  | 2015-04-15 | 16:50 |


To summarize when to reach for each approach: use a plain list of names when you know exactly which columns you want and the list is short. Use Polars selectors when you want to match by dtype, prefix, suffix, or other structural properties of the columns. Use a function when you need custom logic that doesn't fit neatly into a selector (e.g., matching against an external list or applying a complex naming convention rule).

These selection methods work consistently across all **Great Tables** methods that accept a `columns=` argument. Whether you prefer explicit column names, positional indexing, Polars selectors, or custom functions, you can choose the approach that best fits your workflow and data.
