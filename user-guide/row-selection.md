# Row Selection

Just as you can target specific columns, **Great Tables** also provides flexible ways to select rows. The `rows=` argument appears in formatting methods, location specifiers, and styling calls, allowing you to apply operations to a precise subset of your data. This page covers each of the available selection mechanisms.

Row selection matters because many table operations (formatting, styling, footnotes) need to target specific rows. Without it, you would need to pre-filter your DataFrame or apply formatting to an entire column and then somehow undo it for the rows that don't apply. Row selection keeps the logic in the table layer, close to where it's used, so your data preparation stays clean and your formatting intent is expressed declaratively alongside the styling calls.


# Selection Options

Location and formatter functions (e.g. [loc.body()](../reference/loc.body.md#great_tables.loc.body) and [fmt_number()](../reference/GT.fmt_number.md#great_tables.GT.fmt_number)) can be applied to specific rows, using the `rows=` argument.

Rows may be specified using any of the following:

- None (the default), to select everything.
- an integer for the row's position.
- a list of or integers.
- a **Polars** selector for filtering.
- a function that takes a DataFrame and returns a boolean Series.

The following sections will use a subset of the [exibble](../reference/data.exibble.md#great_tables.data.exibble) data, to demonstrate these options.


``` python
from great_tables import GT, exibble, loc, style

lil_exibble = exibble[["num", "char", "currency"]].head(3)
gt_ex = GT(lil_exibble)
```


# Using integers

Use a single integer, or a list of integers, to select rows by position.


``` python
gt_ex.fmt_currency("currency", rows=0, decimals=1)
```


<style>
#oczskyyfob table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oczskyyfob thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oczskyyfob p { margin: 0; padding: 0; }
 #oczskyyfob .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oczskyyfob .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oczskyyfob .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oczskyyfob .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oczskyyfob .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oczskyyfob .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oczskyyfob .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oczskyyfob .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oczskyyfob .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oczskyyfob .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oczskyyfob .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oczskyyfob .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oczskyyfob .gt_spanner_row { border-bottom-style: hidden; }
 #oczskyyfob .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oczskyyfob .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oczskyyfob .gt_from_md> :first-child { margin-top: 0; }
 #oczskyyfob .gt_from_md> :last-child { margin-bottom: 0; }
 #oczskyyfob .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oczskyyfob .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oczskyyfob .gt_indent_1 { text-indent: 5px; }
 #oczskyyfob .gt_indent_2 { text-indent: calc(5px * 2); }
 #oczskyyfob .gt_indent_3 { text-indent: calc(5px * 3); }
 #oczskyyfob .gt_indent_4 { text-indent: calc(5px * 4); }
 #oczskyyfob .gt_indent_5 { text-indent: calc(5px * 5); }
 #oczskyyfob .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oczskyyfob .gt_row_group_first td { border-top-width: 2px; }
 #oczskyyfob .gt_row_group_first th { border-top-width: 2px; }
 #oczskyyfob .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oczskyyfob .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oczskyyfob .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oczskyyfob .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oczskyyfob .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oczskyyfob .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oczskyyfob .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oczskyyfob .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oczskyyfob .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oczskyyfob .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oczskyyfob .gt_left { text-align: left; }
 #oczskyyfob .gt_center { text-align: center; }
 #oczskyyfob .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oczskyyfob .gt_font_normal { font-weight: normal; }
 #oczskyyfob .gt_font_bold { font-weight: bold; }
 #oczskyyfob .gt_font_italic { font-style: italic; }
 #oczskyyfob .gt_super { font-size: 65%; }
 #oczskyyfob .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oczskyyfob .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oczskyyfob .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oczskyyfob .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oczskyyfob .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oczskyyfob .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | currency |
|--------|---------|----------|
| 0.1111 | apricot | \$50.0   |
| 2.222  | banana  | 17.95    |
| 33.33  | coconut | 1.39     |


Notice that a dollar sign (`$`) was only added to the first row (index `0` in python).

Indexing works the same as selecting items from a python list. This negative integers select relative to the final row.


``` python
gt_ex.fmt_currency("currency", rows=[0, -1], decimals=1)
```


<style>
#lirutjrwjv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lirutjrwjv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lirutjrwjv p { margin: 0; padding: 0; }
 #lirutjrwjv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lirutjrwjv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lirutjrwjv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lirutjrwjv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lirutjrwjv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lirutjrwjv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lirutjrwjv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lirutjrwjv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lirutjrwjv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lirutjrwjv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lirutjrwjv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lirutjrwjv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lirutjrwjv .gt_spanner_row { border-bottom-style: hidden; }
 #lirutjrwjv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lirutjrwjv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lirutjrwjv .gt_from_md> :first-child { margin-top: 0; }
 #lirutjrwjv .gt_from_md> :last-child { margin-bottom: 0; }
 #lirutjrwjv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lirutjrwjv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lirutjrwjv .gt_indent_1 { text-indent: 5px; }
 #lirutjrwjv .gt_indent_2 { text-indent: calc(5px * 2); }
 #lirutjrwjv .gt_indent_3 { text-indent: calc(5px * 3); }
 #lirutjrwjv .gt_indent_4 { text-indent: calc(5px * 4); }
 #lirutjrwjv .gt_indent_5 { text-indent: calc(5px * 5); }
 #lirutjrwjv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lirutjrwjv .gt_row_group_first td { border-top-width: 2px; }
 #lirutjrwjv .gt_row_group_first th { border-top-width: 2px; }
 #lirutjrwjv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lirutjrwjv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lirutjrwjv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lirutjrwjv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lirutjrwjv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lirutjrwjv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lirutjrwjv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lirutjrwjv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lirutjrwjv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lirutjrwjv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lirutjrwjv .gt_left { text-align: left; }
 #lirutjrwjv .gt_center { text-align: center; }
 #lirutjrwjv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lirutjrwjv .gt_font_normal { font-weight: normal; }
 #lirutjrwjv .gt_font_bold { font-weight: bold; }
 #lirutjrwjv .gt_font_italic { font-style: italic; }
 #lirutjrwjv .gt_super { font-size: 65%; }
 #lirutjrwjv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lirutjrwjv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lirutjrwjv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lirutjrwjv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lirutjrwjv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lirutjrwjv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | currency |
|--------|---------|----------|
| 0.1111 | apricot | \$50.0   |
| 2.222  | banana  | 17.95    |
| 33.33  | coconut | \$1.4    |


The first and last rows now show currency formatting, while the middle row remains unchanged. Negative indices count backward from the end, just as with Python lists.


# Using polars expressions

The `rows=` argument accepts polars expressions, which return a boolean Series, indicating which rows to operate on.

For example, the code below only formats the `num` column, but only when currency is less than 40.


``` python
import polars as pl

gt_polars = GT(pl.from_pandas(lil_exibble))

gt_polars.fmt_integer("num", rows=pl.col("currency") < 40)
```


<style>
#clzwwhcies table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#clzwwhcies thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#clzwwhcies p { margin: 0; padding: 0; }
 #clzwwhcies .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #clzwwhcies .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #clzwwhcies .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #clzwwhcies .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #clzwwhcies .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #clzwwhcies .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #clzwwhcies .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #clzwwhcies .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #clzwwhcies .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #clzwwhcies .gt_column_spanner_outer:first-child { padding-left: 0; }
 #clzwwhcies .gt_column_spanner_outer:last-child { padding-right: 0; }
 #clzwwhcies .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #clzwwhcies .gt_spanner_row { border-bottom-style: hidden; }
 #clzwwhcies .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #clzwwhcies .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #clzwwhcies .gt_from_md> :first-child { margin-top: 0; }
 #clzwwhcies .gt_from_md> :last-child { margin-bottom: 0; }
 #clzwwhcies .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #clzwwhcies .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #clzwwhcies .gt_indent_1 { text-indent: 5px; }
 #clzwwhcies .gt_indent_2 { text-indent: calc(5px * 2); }
 #clzwwhcies .gt_indent_3 { text-indent: calc(5px * 3); }
 #clzwwhcies .gt_indent_4 { text-indent: calc(5px * 4); }
 #clzwwhcies .gt_indent_5 { text-indent: calc(5px * 5); }
 #clzwwhcies .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #clzwwhcies .gt_row_group_first td { border-top-width: 2px; }
 #clzwwhcies .gt_row_group_first th { border-top-width: 2px; }
 #clzwwhcies .gt_striped { color: #333333; background-color: #F4F4F4; }
 #clzwwhcies .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #clzwwhcies .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #clzwwhcies .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #clzwwhcies .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #clzwwhcies .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #clzwwhcies .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #clzwwhcies .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #clzwwhcies .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #clzwwhcies .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #clzwwhcies .gt_left { text-align: left; }
 #clzwwhcies .gt_center { text-align: center; }
 #clzwwhcies .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #clzwwhcies .gt_font_normal { font-weight: normal; }
 #clzwwhcies .gt_font_bold { font-weight: bold; }
 #clzwwhcies .gt_font_italic { font-style: italic; }
 #clzwwhcies .gt_super { font-size: 65%; }
 #clzwwhcies .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #clzwwhcies .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #clzwwhcies .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #clzwwhcies .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #clzwwhcies .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #clzwwhcies .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | currency |
|--------|---------|----------|
| 0.1111 | apricot | 49.95    |
| 2      | banana  | 17.95    |
| 33     | coconut | 1.39     |


Here's a more realistic example, which highlights the row with the highest value for currency.


``` python
import polars.selectors as cs

gt_polars.tab_style(
    style.fill("yellow"),
    loc.body(
        columns=cs.all(),
        rows=pl.col("currency") == pl.col("currency").max()
    )
)
```


<style>
#jgevrnrobk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jgevrnrobk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jgevrnrobk p { margin: 0; padding: 0; }
 #jgevrnrobk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jgevrnrobk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jgevrnrobk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jgevrnrobk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jgevrnrobk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jgevrnrobk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jgevrnrobk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jgevrnrobk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jgevrnrobk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jgevrnrobk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jgevrnrobk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jgevrnrobk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jgevrnrobk .gt_spanner_row { border-bottom-style: hidden; }
 #jgevrnrobk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jgevrnrobk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jgevrnrobk .gt_from_md> :first-child { margin-top: 0; }
 #jgevrnrobk .gt_from_md> :last-child { margin-bottom: 0; }
 #jgevrnrobk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jgevrnrobk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jgevrnrobk .gt_indent_1 { text-indent: 5px; }
 #jgevrnrobk .gt_indent_2 { text-indent: calc(5px * 2); }
 #jgevrnrobk .gt_indent_3 { text-indent: calc(5px * 3); }
 #jgevrnrobk .gt_indent_4 { text-indent: calc(5px * 4); }
 #jgevrnrobk .gt_indent_5 { text-indent: calc(5px * 5); }
 #jgevrnrobk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jgevrnrobk .gt_row_group_first td { border-top-width: 2px; }
 #jgevrnrobk .gt_row_group_first th { border-top-width: 2px; }
 #jgevrnrobk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jgevrnrobk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jgevrnrobk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jgevrnrobk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jgevrnrobk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jgevrnrobk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jgevrnrobk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jgevrnrobk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jgevrnrobk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jgevrnrobk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jgevrnrobk .gt_left { text-align: left; }
 #jgevrnrobk .gt_center { text-align: center; }
 #jgevrnrobk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jgevrnrobk .gt_font_normal { font-weight: normal; }
 #jgevrnrobk .gt_font_bold { font-weight: bold; }
 #jgevrnrobk .gt_font_italic { font-style: italic; }
 #jgevrnrobk .gt_super { font-size: 65%; }
 #jgevrnrobk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jgevrnrobk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jgevrnrobk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jgevrnrobk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jgevrnrobk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jgevrnrobk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | currency |
|--------|---------|----------|
| 0.1111 | apricot | 49.95    |
| 2.222  | banana  | 17.95    |
| 33.33  | coconut | 1.39     |


The row with the maximum currency value is highlighted with a yellow background. Using expressions for row selection keeps the logic declarative and close to the styling call.

Expression-based row selection is especially powerful for conditional formatting, where the styling rule depends on the data itself. For example, you can highlight rows where a metric exceeds a threshold, format only the rows that contain the maximum or minimum value, or apply different styles based on category membership (all without any imperative filtering logic).


# Using a function

Since libraries like `pandas` don't have lazy expressions, the `rows=` argument also accepts a function for selecting rows. The function should take a DataFrame and return a boolean series.

Here's the same example as the previous polars section, but with pandas data, and a lambda for selecting rows.


``` python
gt_ex.fmt_integer("num", rows=lambda D: D["currency"] < 40)
```


<style>
#ioggiyzdww table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ioggiyzdww thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ioggiyzdww p { margin: 0; padding: 0; }
 #ioggiyzdww .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ioggiyzdww .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ioggiyzdww .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ioggiyzdww .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ioggiyzdww .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ioggiyzdww .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ioggiyzdww .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ioggiyzdww .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ioggiyzdww .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ioggiyzdww .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ioggiyzdww .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ioggiyzdww .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ioggiyzdww .gt_spanner_row { border-bottom-style: hidden; }
 #ioggiyzdww .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ioggiyzdww .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ioggiyzdww .gt_from_md> :first-child { margin-top: 0; }
 #ioggiyzdww .gt_from_md> :last-child { margin-bottom: 0; }
 #ioggiyzdww .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ioggiyzdww .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ioggiyzdww .gt_indent_1 { text-indent: 5px; }
 #ioggiyzdww .gt_indent_2 { text-indent: calc(5px * 2); }
 #ioggiyzdww .gt_indent_3 { text-indent: calc(5px * 3); }
 #ioggiyzdww .gt_indent_4 { text-indent: calc(5px * 4); }
 #ioggiyzdww .gt_indent_5 { text-indent: calc(5px * 5); }
 #ioggiyzdww .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ioggiyzdww .gt_row_group_first td { border-top-width: 2px; }
 #ioggiyzdww .gt_row_group_first th { border-top-width: 2px; }
 #ioggiyzdww .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ioggiyzdww .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ioggiyzdww .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ioggiyzdww .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ioggiyzdww .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ioggiyzdww .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ioggiyzdww .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ioggiyzdww .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ioggiyzdww .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ioggiyzdww .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ioggiyzdww .gt_left { text-align: left; }
 #ioggiyzdww .gt_center { text-align: center; }
 #ioggiyzdww .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ioggiyzdww .gt_font_normal { font-weight: normal; }
 #ioggiyzdww .gt_font_bold { font-weight: bold; }
 #ioggiyzdww .gt_font_italic { font-style: italic; }
 #ioggiyzdww .gt_super { font-size: 65%; }
 #ioggiyzdww .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ioggiyzdww .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ioggiyzdww .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ioggiyzdww .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ioggiyzdww .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ioggiyzdww .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | currency |
|--------|---------|----------|
| 0.1111 | apricot | 49.95    |
| 2      | banana  | 17.95    |
| 33     | coconut | 1.39     |


Here's the styling example from the previous polars section.


``` python
import polars.selectors as cs

gt_ex.tab_style(
    style.fill("yellow"),
    loc.body(
        columns=lambda colname: True,
        rows=lambda D: D["currency"] == D["currency"].max()
    )
)
```


<style>
#dkhefrcenq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dkhefrcenq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dkhefrcenq p { margin: 0; padding: 0; }
 #dkhefrcenq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dkhefrcenq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dkhefrcenq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dkhefrcenq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dkhefrcenq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dkhefrcenq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dkhefrcenq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dkhefrcenq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dkhefrcenq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dkhefrcenq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dkhefrcenq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dkhefrcenq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dkhefrcenq .gt_spanner_row { border-bottom-style: hidden; }
 #dkhefrcenq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dkhefrcenq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dkhefrcenq .gt_from_md> :first-child { margin-top: 0; }
 #dkhefrcenq .gt_from_md> :last-child { margin-bottom: 0; }
 #dkhefrcenq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dkhefrcenq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dkhefrcenq .gt_indent_1 { text-indent: 5px; }
 #dkhefrcenq .gt_indent_2 { text-indent: calc(5px * 2); }
 #dkhefrcenq .gt_indent_3 { text-indent: calc(5px * 3); }
 #dkhefrcenq .gt_indent_4 { text-indent: calc(5px * 4); }
 #dkhefrcenq .gt_indent_5 { text-indent: calc(5px * 5); }
 #dkhefrcenq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dkhefrcenq .gt_row_group_first td { border-top-width: 2px; }
 #dkhefrcenq .gt_row_group_first th { border-top-width: 2px; }
 #dkhefrcenq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dkhefrcenq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dkhefrcenq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dkhefrcenq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dkhefrcenq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dkhefrcenq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dkhefrcenq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dkhefrcenq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dkhefrcenq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dkhefrcenq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dkhefrcenq .gt_left { text-align: left; }
 #dkhefrcenq .gt_center { text-align: center; }
 #dkhefrcenq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dkhefrcenq .gt_font_normal { font-weight: normal; }
 #dkhefrcenq .gt_font_bold { font-weight: bold; }
 #dkhefrcenq .gt_font_italic { font-style: italic; }
 #dkhefrcenq .gt_super { font-size: 65%; }
 #dkhefrcenq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dkhefrcenq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dkhefrcenq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dkhefrcenq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dkhefrcenq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dkhefrcenq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | currency |
|--------|---------|----------|
| 0.1111 | apricot | 49.95    |
| 2.222  | banana  | 17.95    |
| 33.33  | coconut | 1.39     |


Whether you prefer integer indexing for quick positional access, Polars expressions for declarative filtering, or functions for compatibility with pandas, the `rows=` argument adapts to your data workflow. Combined with column selection, these tools give you fine-grained control over exactly which cells your formatting and styling operations affect.
