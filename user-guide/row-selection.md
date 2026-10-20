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
#ymzexdfwtn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ymzexdfwtn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ymzexdfwtn p { margin: 0; padding: 0; }
 #ymzexdfwtn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ymzexdfwtn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ymzexdfwtn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ymzexdfwtn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ymzexdfwtn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ymzexdfwtn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ymzexdfwtn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ymzexdfwtn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ymzexdfwtn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ymzexdfwtn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ymzexdfwtn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ymzexdfwtn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ymzexdfwtn .gt_spanner_row { border-bottom-style: hidden; }
 #ymzexdfwtn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ymzexdfwtn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ymzexdfwtn .gt_from_md> :first-child { margin-top: 0; }
 #ymzexdfwtn .gt_from_md> :last-child { margin-bottom: 0; }
 #ymzexdfwtn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ymzexdfwtn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ymzexdfwtn .gt_indent_1 { text-indent: 5px; }
 #ymzexdfwtn .gt_indent_2 { text-indent: calc(5px * 2); }
 #ymzexdfwtn .gt_indent_3 { text-indent: calc(5px * 3); }
 #ymzexdfwtn .gt_indent_4 { text-indent: calc(5px * 4); }
 #ymzexdfwtn .gt_indent_5 { text-indent: calc(5px * 5); }
 #ymzexdfwtn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ymzexdfwtn .gt_row_group_first td { border-top-width: 2px; }
 #ymzexdfwtn .gt_row_group_first th { border-top-width: 2px; }
 #ymzexdfwtn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ymzexdfwtn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ymzexdfwtn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ymzexdfwtn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ymzexdfwtn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ymzexdfwtn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ymzexdfwtn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ymzexdfwtn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ymzexdfwtn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ymzexdfwtn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ymzexdfwtn .gt_left { text-align: left; }
 #ymzexdfwtn .gt_center { text-align: center; }
 #ymzexdfwtn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ymzexdfwtn .gt_font_normal { font-weight: normal; }
 #ymzexdfwtn .gt_font_bold { font-weight: bold; }
 #ymzexdfwtn .gt_font_italic { font-style: italic; }
 #ymzexdfwtn .gt_super { font-size: 65%; }
 #ymzexdfwtn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ymzexdfwtn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ymzexdfwtn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ymzexdfwtn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ymzexdfwtn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ymzexdfwtn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kkzjctyiaz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kkzjctyiaz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kkzjctyiaz p { margin: 0; padding: 0; }
 #kkzjctyiaz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kkzjctyiaz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kkzjctyiaz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kkzjctyiaz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kkzjctyiaz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkzjctyiaz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkzjctyiaz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkzjctyiaz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kkzjctyiaz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kkzjctyiaz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kkzjctyiaz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kkzjctyiaz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kkzjctyiaz .gt_spanner_row { border-bottom-style: hidden; }
 #kkzjctyiaz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kkzjctyiaz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kkzjctyiaz .gt_from_md> :first-child { margin-top: 0; }
 #kkzjctyiaz .gt_from_md> :last-child { margin-bottom: 0; }
 #kkzjctyiaz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kkzjctyiaz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kkzjctyiaz .gt_indent_1 { text-indent: 5px; }
 #kkzjctyiaz .gt_indent_2 { text-indent: calc(5px * 2); }
 #kkzjctyiaz .gt_indent_3 { text-indent: calc(5px * 3); }
 #kkzjctyiaz .gt_indent_4 { text-indent: calc(5px * 4); }
 #kkzjctyiaz .gt_indent_5 { text-indent: calc(5px * 5); }
 #kkzjctyiaz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kkzjctyiaz .gt_row_group_first td { border-top-width: 2px; }
 #kkzjctyiaz .gt_row_group_first th { border-top-width: 2px; }
 #kkzjctyiaz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kkzjctyiaz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkzjctyiaz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkzjctyiaz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kkzjctyiaz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkzjctyiaz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkzjctyiaz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kkzjctyiaz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kkzjctyiaz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkzjctyiaz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkzjctyiaz .gt_left { text-align: left; }
 #kkzjctyiaz .gt_center { text-align: center; }
 #kkzjctyiaz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kkzjctyiaz .gt_font_normal { font-weight: normal; }
 #kkzjctyiaz .gt_font_bold { font-weight: bold; }
 #kkzjctyiaz .gt_font_italic { font-style: italic; }
 #kkzjctyiaz .gt_super { font-size: 65%; }
 #kkzjctyiaz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkzjctyiaz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kkzjctyiaz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkzjctyiaz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkzjctyiaz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kkzjctyiaz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lcysiztoay table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lcysiztoay thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lcysiztoay p { margin: 0; padding: 0; }
 #lcysiztoay .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lcysiztoay .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lcysiztoay .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lcysiztoay .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lcysiztoay .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lcysiztoay .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lcysiztoay .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lcysiztoay .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lcysiztoay .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lcysiztoay .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lcysiztoay .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lcysiztoay .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lcysiztoay .gt_spanner_row { border-bottom-style: hidden; }
 #lcysiztoay .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lcysiztoay .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lcysiztoay .gt_from_md> :first-child { margin-top: 0; }
 #lcysiztoay .gt_from_md> :last-child { margin-bottom: 0; }
 #lcysiztoay .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lcysiztoay .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lcysiztoay .gt_indent_1 { text-indent: 5px; }
 #lcysiztoay .gt_indent_2 { text-indent: calc(5px * 2); }
 #lcysiztoay .gt_indent_3 { text-indent: calc(5px * 3); }
 #lcysiztoay .gt_indent_4 { text-indent: calc(5px * 4); }
 #lcysiztoay .gt_indent_5 { text-indent: calc(5px * 5); }
 #lcysiztoay .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lcysiztoay .gt_row_group_first td { border-top-width: 2px; }
 #lcysiztoay .gt_row_group_first th { border-top-width: 2px; }
 #lcysiztoay .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lcysiztoay .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lcysiztoay .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lcysiztoay .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lcysiztoay .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lcysiztoay .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lcysiztoay .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lcysiztoay .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lcysiztoay .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lcysiztoay .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lcysiztoay .gt_left { text-align: left; }
 #lcysiztoay .gt_center { text-align: center; }
 #lcysiztoay .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lcysiztoay .gt_font_normal { font-weight: normal; }
 #lcysiztoay .gt_font_bold { font-weight: bold; }
 #lcysiztoay .gt_font_italic { font-style: italic; }
 #lcysiztoay .gt_super { font-size: 65%; }
 #lcysiztoay .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lcysiztoay .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lcysiztoay .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lcysiztoay .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lcysiztoay .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lcysiztoay .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xlhbqavbpg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xlhbqavbpg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xlhbqavbpg p { margin: 0; padding: 0; }
 #xlhbqavbpg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xlhbqavbpg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xlhbqavbpg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xlhbqavbpg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xlhbqavbpg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xlhbqavbpg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xlhbqavbpg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xlhbqavbpg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xlhbqavbpg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xlhbqavbpg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xlhbqavbpg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xlhbqavbpg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xlhbqavbpg .gt_spanner_row { border-bottom-style: hidden; }
 #xlhbqavbpg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xlhbqavbpg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xlhbqavbpg .gt_from_md> :first-child { margin-top: 0; }
 #xlhbqavbpg .gt_from_md> :last-child { margin-bottom: 0; }
 #xlhbqavbpg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xlhbqavbpg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xlhbqavbpg .gt_indent_1 { text-indent: 5px; }
 #xlhbqavbpg .gt_indent_2 { text-indent: calc(5px * 2); }
 #xlhbqavbpg .gt_indent_3 { text-indent: calc(5px * 3); }
 #xlhbqavbpg .gt_indent_4 { text-indent: calc(5px * 4); }
 #xlhbqavbpg .gt_indent_5 { text-indent: calc(5px * 5); }
 #xlhbqavbpg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xlhbqavbpg .gt_row_group_first td { border-top-width: 2px; }
 #xlhbqavbpg .gt_row_group_first th { border-top-width: 2px; }
 #xlhbqavbpg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xlhbqavbpg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xlhbqavbpg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xlhbqavbpg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xlhbqavbpg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xlhbqavbpg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xlhbqavbpg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xlhbqavbpg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xlhbqavbpg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xlhbqavbpg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xlhbqavbpg .gt_left { text-align: left; }
 #xlhbqavbpg .gt_center { text-align: center; }
 #xlhbqavbpg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xlhbqavbpg .gt_font_normal { font-weight: normal; }
 #xlhbqavbpg .gt_font_bold { font-weight: bold; }
 #xlhbqavbpg .gt_font_italic { font-style: italic; }
 #xlhbqavbpg .gt_super { font-size: 65%; }
 #xlhbqavbpg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xlhbqavbpg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xlhbqavbpg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xlhbqavbpg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xlhbqavbpg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xlhbqavbpg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cwadbotduq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cwadbotduq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cwadbotduq p { margin: 0; padding: 0; }
 #cwadbotduq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cwadbotduq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cwadbotduq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cwadbotduq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cwadbotduq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cwadbotduq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cwadbotduq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cwadbotduq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cwadbotduq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cwadbotduq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cwadbotduq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cwadbotduq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cwadbotduq .gt_spanner_row { border-bottom-style: hidden; }
 #cwadbotduq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cwadbotduq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cwadbotduq .gt_from_md> :first-child { margin-top: 0; }
 #cwadbotduq .gt_from_md> :last-child { margin-bottom: 0; }
 #cwadbotduq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cwadbotduq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cwadbotduq .gt_indent_1 { text-indent: 5px; }
 #cwadbotduq .gt_indent_2 { text-indent: calc(5px * 2); }
 #cwadbotduq .gt_indent_3 { text-indent: calc(5px * 3); }
 #cwadbotduq .gt_indent_4 { text-indent: calc(5px * 4); }
 #cwadbotduq .gt_indent_5 { text-indent: calc(5px * 5); }
 #cwadbotduq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cwadbotduq .gt_row_group_first td { border-top-width: 2px; }
 #cwadbotduq .gt_row_group_first th { border-top-width: 2px; }
 #cwadbotduq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cwadbotduq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cwadbotduq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cwadbotduq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cwadbotduq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cwadbotduq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cwadbotduq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cwadbotduq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cwadbotduq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cwadbotduq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cwadbotduq .gt_left { text-align: left; }
 #cwadbotduq .gt_center { text-align: center; }
 #cwadbotduq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cwadbotduq .gt_font_normal { font-weight: normal; }
 #cwadbotduq .gt_font_bold { font-weight: bold; }
 #cwadbotduq .gt_font_italic { font-style: italic; }
 #cwadbotduq .gt_super { font-size: 65%; }
 #cwadbotduq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cwadbotduq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cwadbotduq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cwadbotduq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cwadbotduq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cwadbotduq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mwkwcabtlk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mwkwcabtlk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mwkwcabtlk p { margin: 0; padding: 0; }
 #mwkwcabtlk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mwkwcabtlk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mwkwcabtlk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mwkwcabtlk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mwkwcabtlk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mwkwcabtlk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mwkwcabtlk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mwkwcabtlk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mwkwcabtlk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mwkwcabtlk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mwkwcabtlk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mwkwcabtlk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mwkwcabtlk .gt_spanner_row { border-bottom-style: hidden; }
 #mwkwcabtlk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mwkwcabtlk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mwkwcabtlk .gt_from_md> :first-child { margin-top: 0; }
 #mwkwcabtlk .gt_from_md> :last-child { margin-bottom: 0; }
 #mwkwcabtlk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mwkwcabtlk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mwkwcabtlk .gt_indent_1 { text-indent: 5px; }
 #mwkwcabtlk .gt_indent_2 { text-indent: calc(5px * 2); }
 #mwkwcabtlk .gt_indent_3 { text-indent: calc(5px * 3); }
 #mwkwcabtlk .gt_indent_4 { text-indent: calc(5px * 4); }
 #mwkwcabtlk .gt_indent_5 { text-indent: calc(5px * 5); }
 #mwkwcabtlk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mwkwcabtlk .gt_row_group_first td { border-top-width: 2px; }
 #mwkwcabtlk .gt_row_group_first th { border-top-width: 2px; }
 #mwkwcabtlk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mwkwcabtlk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mwkwcabtlk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mwkwcabtlk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mwkwcabtlk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mwkwcabtlk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mwkwcabtlk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mwkwcabtlk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mwkwcabtlk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mwkwcabtlk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mwkwcabtlk .gt_left { text-align: left; }
 #mwkwcabtlk .gt_center { text-align: center; }
 #mwkwcabtlk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mwkwcabtlk .gt_font_normal { font-weight: normal; }
 #mwkwcabtlk .gt_font_bold { font-weight: bold; }
 #mwkwcabtlk .gt_font_italic { font-style: italic; }
 #mwkwcabtlk .gt_super { font-size: 65%; }
 #mwkwcabtlk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mwkwcabtlk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mwkwcabtlk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mwkwcabtlk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mwkwcabtlk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mwkwcabtlk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | currency |
|--------|---------|----------|
| 0.1111 | apricot | 49.95    |
| 2.222  | banana  | 17.95    |
| 33.33  | coconut | 1.39     |


Whether you prefer integer indexing for quick positional access, Polars expressions for declarative filtering, or functions for compatibility with pandas, the `rows=` argument adapts to your data workflow. Combined with column selection, these tools give you fine-grained control over exactly which cells your formatting and styling operations affect.
