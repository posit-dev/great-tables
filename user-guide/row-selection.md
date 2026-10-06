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
#tmabjemkqy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tmabjemkqy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tmabjemkqy p { margin: 0; padding: 0; }
 #tmabjemkqy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tmabjemkqy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tmabjemkqy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tmabjemkqy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tmabjemkqy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tmabjemkqy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tmabjemkqy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tmabjemkqy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tmabjemkqy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tmabjemkqy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tmabjemkqy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tmabjemkqy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tmabjemkqy .gt_spanner_row { border-bottom-style: hidden; }
 #tmabjemkqy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tmabjemkqy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tmabjemkqy .gt_from_md> :first-child { margin-top: 0; }
 #tmabjemkqy .gt_from_md> :last-child { margin-bottom: 0; }
 #tmabjemkqy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tmabjemkqy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tmabjemkqy .gt_indent_1 { text-indent: 5px; }
 #tmabjemkqy .gt_indent_2 { text-indent: calc(5px * 2); }
 #tmabjemkqy .gt_indent_3 { text-indent: calc(5px * 3); }
 #tmabjemkqy .gt_indent_4 { text-indent: calc(5px * 4); }
 #tmabjemkqy .gt_indent_5 { text-indent: calc(5px * 5); }
 #tmabjemkqy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tmabjemkqy .gt_row_group_first td { border-top-width: 2px; }
 #tmabjemkqy .gt_row_group_first th { border-top-width: 2px; }
 #tmabjemkqy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tmabjemkqy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tmabjemkqy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tmabjemkqy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tmabjemkqy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tmabjemkqy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tmabjemkqy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tmabjemkqy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tmabjemkqy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tmabjemkqy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tmabjemkqy .gt_left { text-align: left; }
 #tmabjemkqy .gt_center { text-align: center; }
 #tmabjemkqy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tmabjemkqy .gt_font_normal { font-weight: normal; }
 #tmabjemkqy .gt_font_bold { font-weight: bold; }
 #tmabjemkqy .gt_font_italic { font-style: italic; }
 #tmabjemkqy .gt_super { font-size: 65%; }
 #tmabjemkqy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tmabjemkqy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tmabjemkqy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tmabjemkqy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tmabjemkqy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tmabjemkqy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lfdkwvohxp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lfdkwvohxp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lfdkwvohxp p { margin: 0; padding: 0; }
 #lfdkwvohxp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lfdkwvohxp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lfdkwvohxp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lfdkwvohxp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lfdkwvohxp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lfdkwvohxp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lfdkwvohxp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lfdkwvohxp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lfdkwvohxp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lfdkwvohxp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lfdkwvohxp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lfdkwvohxp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lfdkwvohxp .gt_spanner_row { border-bottom-style: hidden; }
 #lfdkwvohxp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lfdkwvohxp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lfdkwvohxp .gt_from_md> :first-child { margin-top: 0; }
 #lfdkwvohxp .gt_from_md> :last-child { margin-bottom: 0; }
 #lfdkwvohxp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lfdkwvohxp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lfdkwvohxp .gt_indent_1 { text-indent: 5px; }
 #lfdkwvohxp .gt_indent_2 { text-indent: calc(5px * 2); }
 #lfdkwvohxp .gt_indent_3 { text-indent: calc(5px * 3); }
 #lfdkwvohxp .gt_indent_4 { text-indent: calc(5px * 4); }
 #lfdkwvohxp .gt_indent_5 { text-indent: calc(5px * 5); }
 #lfdkwvohxp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lfdkwvohxp .gt_row_group_first td { border-top-width: 2px; }
 #lfdkwvohxp .gt_row_group_first th { border-top-width: 2px; }
 #lfdkwvohxp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lfdkwvohxp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lfdkwvohxp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lfdkwvohxp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lfdkwvohxp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lfdkwvohxp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lfdkwvohxp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lfdkwvohxp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lfdkwvohxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lfdkwvohxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lfdkwvohxp .gt_left { text-align: left; }
 #lfdkwvohxp .gt_center { text-align: center; }
 #lfdkwvohxp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lfdkwvohxp .gt_font_normal { font-weight: normal; }
 #lfdkwvohxp .gt_font_bold { font-weight: bold; }
 #lfdkwvohxp .gt_font_italic { font-style: italic; }
 #lfdkwvohxp .gt_super { font-size: 65%; }
 #lfdkwvohxp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lfdkwvohxp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lfdkwvohxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lfdkwvohxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lfdkwvohxp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lfdkwvohxp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xmdfukjfjg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xmdfukjfjg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xmdfukjfjg p { margin: 0; padding: 0; }
 #xmdfukjfjg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xmdfukjfjg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xmdfukjfjg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xmdfukjfjg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xmdfukjfjg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xmdfukjfjg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmdfukjfjg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xmdfukjfjg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xmdfukjfjg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xmdfukjfjg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xmdfukjfjg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xmdfukjfjg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xmdfukjfjg .gt_spanner_row { border-bottom-style: hidden; }
 #xmdfukjfjg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xmdfukjfjg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xmdfukjfjg .gt_from_md> :first-child { margin-top: 0; }
 #xmdfukjfjg .gt_from_md> :last-child { margin-bottom: 0; }
 #xmdfukjfjg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xmdfukjfjg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xmdfukjfjg .gt_indent_1 { text-indent: 5px; }
 #xmdfukjfjg .gt_indent_2 { text-indent: calc(5px * 2); }
 #xmdfukjfjg .gt_indent_3 { text-indent: calc(5px * 3); }
 #xmdfukjfjg .gt_indent_4 { text-indent: calc(5px * 4); }
 #xmdfukjfjg .gt_indent_5 { text-indent: calc(5px * 5); }
 #xmdfukjfjg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xmdfukjfjg .gt_row_group_first td { border-top-width: 2px; }
 #xmdfukjfjg .gt_row_group_first th { border-top-width: 2px; }
 #xmdfukjfjg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xmdfukjfjg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmdfukjfjg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xmdfukjfjg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xmdfukjfjg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmdfukjfjg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xmdfukjfjg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xmdfukjfjg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xmdfukjfjg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmdfukjfjg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xmdfukjfjg .gt_left { text-align: left; }
 #xmdfukjfjg .gt_center { text-align: center; }
 #xmdfukjfjg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xmdfukjfjg .gt_font_normal { font-weight: normal; }
 #xmdfukjfjg .gt_font_bold { font-weight: bold; }
 #xmdfukjfjg .gt_font_italic { font-style: italic; }
 #xmdfukjfjg .gt_super { font-size: 65%; }
 #xmdfukjfjg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmdfukjfjg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xmdfukjfjg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmdfukjfjg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xmdfukjfjg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xmdfukjfjg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xmojwuydjd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xmojwuydjd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xmojwuydjd p { margin: 0; padding: 0; }
 #xmojwuydjd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xmojwuydjd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xmojwuydjd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xmojwuydjd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xmojwuydjd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xmojwuydjd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmojwuydjd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xmojwuydjd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xmojwuydjd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xmojwuydjd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xmojwuydjd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xmojwuydjd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xmojwuydjd .gt_spanner_row { border-bottom-style: hidden; }
 #xmojwuydjd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xmojwuydjd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xmojwuydjd .gt_from_md> :first-child { margin-top: 0; }
 #xmojwuydjd .gt_from_md> :last-child { margin-bottom: 0; }
 #xmojwuydjd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xmojwuydjd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xmojwuydjd .gt_indent_1 { text-indent: 5px; }
 #xmojwuydjd .gt_indent_2 { text-indent: calc(5px * 2); }
 #xmojwuydjd .gt_indent_3 { text-indent: calc(5px * 3); }
 #xmojwuydjd .gt_indent_4 { text-indent: calc(5px * 4); }
 #xmojwuydjd .gt_indent_5 { text-indent: calc(5px * 5); }
 #xmojwuydjd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xmojwuydjd .gt_row_group_first td { border-top-width: 2px; }
 #xmojwuydjd .gt_row_group_first th { border-top-width: 2px; }
 #xmojwuydjd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xmojwuydjd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmojwuydjd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xmojwuydjd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xmojwuydjd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xmojwuydjd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xmojwuydjd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xmojwuydjd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xmojwuydjd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmojwuydjd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xmojwuydjd .gt_left { text-align: left; }
 #xmojwuydjd .gt_center { text-align: center; }
 #xmojwuydjd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xmojwuydjd .gt_font_normal { font-weight: normal; }
 #xmojwuydjd .gt_font_bold { font-weight: bold; }
 #xmojwuydjd .gt_font_italic { font-style: italic; }
 #xmojwuydjd .gt_super { font-size: 65%; }
 #xmojwuydjd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmojwuydjd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xmojwuydjd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xmojwuydjd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xmojwuydjd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xmojwuydjd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ewbkmshbep table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ewbkmshbep thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ewbkmshbep p { margin: 0; padding: 0; }
 #ewbkmshbep .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ewbkmshbep .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ewbkmshbep .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ewbkmshbep .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ewbkmshbep .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ewbkmshbep .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ewbkmshbep .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ewbkmshbep .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ewbkmshbep .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ewbkmshbep .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ewbkmshbep .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ewbkmshbep .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ewbkmshbep .gt_spanner_row { border-bottom-style: hidden; }
 #ewbkmshbep .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ewbkmshbep .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ewbkmshbep .gt_from_md> :first-child { margin-top: 0; }
 #ewbkmshbep .gt_from_md> :last-child { margin-bottom: 0; }
 #ewbkmshbep .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ewbkmshbep .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ewbkmshbep .gt_indent_1 { text-indent: 5px; }
 #ewbkmshbep .gt_indent_2 { text-indent: calc(5px * 2); }
 #ewbkmshbep .gt_indent_3 { text-indent: calc(5px * 3); }
 #ewbkmshbep .gt_indent_4 { text-indent: calc(5px * 4); }
 #ewbkmshbep .gt_indent_5 { text-indent: calc(5px * 5); }
 #ewbkmshbep .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ewbkmshbep .gt_row_group_first td { border-top-width: 2px; }
 #ewbkmshbep .gt_row_group_first th { border-top-width: 2px; }
 #ewbkmshbep .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ewbkmshbep .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ewbkmshbep .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ewbkmshbep .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ewbkmshbep .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ewbkmshbep .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ewbkmshbep .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ewbkmshbep .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ewbkmshbep .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ewbkmshbep .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ewbkmshbep .gt_left { text-align: left; }
 #ewbkmshbep .gt_center { text-align: center; }
 #ewbkmshbep .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ewbkmshbep .gt_font_normal { font-weight: normal; }
 #ewbkmshbep .gt_font_bold { font-weight: bold; }
 #ewbkmshbep .gt_font_italic { font-style: italic; }
 #ewbkmshbep .gt_super { font-size: 65%; }
 #ewbkmshbep .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ewbkmshbep .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ewbkmshbep .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ewbkmshbep .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ewbkmshbep .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ewbkmshbep .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#znyagduear table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#znyagduear thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#znyagduear p { margin: 0; padding: 0; }
 #znyagduear .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #znyagduear .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #znyagduear .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #znyagduear .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #znyagduear .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #znyagduear .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #znyagduear .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #znyagduear .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #znyagduear .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #znyagduear .gt_column_spanner_outer:first-child { padding-left: 0; }
 #znyagduear .gt_column_spanner_outer:last-child { padding-right: 0; }
 #znyagduear .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #znyagduear .gt_spanner_row { border-bottom-style: hidden; }
 #znyagduear .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #znyagduear .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #znyagduear .gt_from_md> :first-child { margin-top: 0; }
 #znyagduear .gt_from_md> :last-child { margin-bottom: 0; }
 #znyagduear .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #znyagduear .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #znyagduear .gt_indent_1 { text-indent: 5px; }
 #znyagduear .gt_indent_2 { text-indent: calc(5px * 2); }
 #znyagduear .gt_indent_3 { text-indent: calc(5px * 3); }
 #znyagduear .gt_indent_4 { text-indent: calc(5px * 4); }
 #znyagduear .gt_indent_5 { text-indent: calc(5px * 5); }
 #znyagduear .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #znyagduear .gt_row_group_first td { border-top-width: 2px; }
 #znyagduear .gt_row_group_first th { border-top-width: 2px; }
 #znyagduear .gt_striped { color: #333333; background-color: #F4F4F4; }
 #znyagduear .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #znyagduear .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #znyagduear .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #znyagduear .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #znyagduear .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #znyagduear .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #znyagduear .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #znyagduear .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #znyagduear .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #znyagduear .gt_left { text-align: left; }
 #znyagduear .gt_center { text-align: center; }
 #znyagduear .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #znyagduear .gt_font_normal { font-weight: normal; }
 #znyagduear .gt_font_bold { font-weight: bold; }
 #znyagduear .gt_font_italic { font-style: italic; }
 #znyagduear .gt_super { font-size: 65%; }
 #znyagduear .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #znyagduear .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #znyagduear .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #znyagduear .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #znyagduear .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #znyagduear .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | currency |
|--------|---------|----------|
| 0.1111 | apricot | 49.95    |
| 2.222  | banana  | 17.95    |
| 33.33  | coconut | 1.39     |


Whether you prefer integer indexing for quick positional access, Polars expressions for declarative filtering, or functions for compatibility with pandas, the `rows=` argument adapts to your data workflow. Combined with column selection, these tools give you fine-grained control over exactly which cells your formatting and styling operations affect.
