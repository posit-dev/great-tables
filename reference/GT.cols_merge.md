# GT.cols_merge()


Merge data from two or more columns into a single column.


Usage

``` python
GT.cols_merge(
    columns,
    hide_columns=None,
    rows=None,
    pattern=None,
)
```


This method takes input from two or more columns and allows the contents to be merged into a single column by using a pattern that specifies the arrangement. The first column in the `columns=` parameter operates as the target column (i.e., the column that will undergo mutation) whereas all following columns will be untouched. There is the option to hide the non-target columns. The formatting of values in different columns will be preserved upon merging.


## Parameters


`columns: SelectExpr`  
The columns for which the merging operations should be applied. The first column name resolved will be the target column (i.e., undergo mutation) and the other columns will serve to provide input. Can be a list of column names or a selection expression, though a list is preferred here to ensure the order of columns is exactly as intended (since order matters for the `pattern=` parameter).

`hide_columns: SelectExpr | Literal[False] = None`  
Any column names provided here will have their state changed to hidden (via internal use of `.cols_hide()`) if they aren't already hidden. This is convenient if the shared purpose of these specified columns is only to provide string input to the target column. To suppress any hiding of columns, `False` can be used here. By default, all columns other than the first one specified in `columns=` will be hidden.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should participate in the merging process. The default is all rows, resulting in all rows in `columns=` being formatted. Alternatively, we can supply a list of row indices.

`pattern: str | None = None`  
A formatting pattern that specifies the arrangement of the column values and any string literals. The pattern uses numbers (within `{}`) that correspond to the indices of columns provided in `columns=`. If two columns are provided in `columns=` and we would like to combine the cell data onto the first column, `"{0} {1}"` could be used. If a pattern isn't provided then a space-separated pattern that includes all columns will be generated automatically. The pattern can also use `<<`/`>>` to surround spans of text that will be removed if any of the contained `{}` yields a missing value. Further details are provided in the *How the pattern works* section.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Details


### How the pattern works

There are two types of templating for the `pattern` string:

- `{` `}` for arranging single column values in a row-wise fashion
- `<<` `>>` to surround spans of text that will be removed if any of the contained `{` `}` yields a missing value

Integer values are placed in `{}` and those values correspond to the columns involved in the merge, in the order they are provided in the `columns=` argument. So the pattern `"{0} ({1}-{2})"` corresponds to the target column value listed first in `columns` and the second and third columns cited (formatted as a range in parentheses). With hypothetical values, this might result as the merged string `"38.2 (3-8)"`.

Because some values involved in merging may be missing, it is likely that something like `"38.2 (3-None)"` would be undesirable. For such cases, placing sections of text in `<<>>` results in the entire span being eliminated if there were to be an `None` value (arising from `{}` values). We could instead opt for a pattern like `"{0}<< ({1}-{2})>>"`, which results in `"38.2"` if either columns `{1}` or `{2}` have a `None` value. We can even use a more complex nesting pattern like `"{0}<< ({1}-<<{2}>>)>>"` to retain a lower limit in parentheses (where `{2}` is `None`) but remove the range altogether if `{1}` is `None`.

One more thing to note here is that if `.sub_missing()` is used on values in a column, those specific values affected won't be considered truly missing by `.cols_merge()` (since they have been explicitly handled with substitute text).


## Examples

Let's use a subset of the [sp500](data.sp500.md#great_tables.data.sp500) dataset to create a table. We'll merge the `open` & `close` columns together, and the `low` & `high` columns (putting an em dash between both).


``` python
from great_tables import GT
from great_tables.data import sp500
import polars as pl

sp500_mini = (
    pl.from_pandas(sp500)
    .slice(49, 6)
    .select("open", "close", "low", "high")
)

(
    GT(sp500_mini)
    .fmt_number(
        columns=["open", "close", "low", "high"],
        decimals=2,
        use_seps=False
    )
    .cols_merge(columns=["open", "close"], pattern="{0}--{1}")
    .cols_merge(columns=["low", "high"], pattern="{0}--{1}")
    .cols_label(open="open/close", low="low/high")
)
```


<style>
#syweyvwoby table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#syweyvwoby thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#syweyvwoby p { margin: 0; padding: 0; }
 #syweyvwoby .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #syweyvwoby .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #syweyvwoby .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #syweyvwoby .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #syweyvwoby .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #syweyvwoby .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #syweyvwoby .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #syweyvwoby .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #syweyvwoby .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #syweyvwoby .gt_column_spanner_outer:first-child { padding-left: 0; }
 #syweyvwoby .gt_column_spanner_outer:last-child { padding-right: 0; }
 #syweyvwoby .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #syweyvwoby .gt_spanner_row { border-bottom-style: hidden; }
 #syweyvwoby .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #syweyvwoby .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #syweyvwoby .gt_from_md> :first-child { margin-top: 0; }
 #syweyvwoby .gt_from_md> :last-child { margin-bottom: 0; }
 #syweyvwoby .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #syweyvwoby .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #syweyvwoby .gt_indent_1 { text-indent: 5px; }
 #syweyvwoby .gt_indent_2 { text-indent: calc(5px * 2); }
 #syweyvwoby .gt_indent_3 { text-indent: calc(5px * 3); }
 #syweyvwoby .gt_indent_4 { text-indent: calc(5px * 4); }
 #syweyvwoby .gt_indent_5 { text-indent: calc(5px * 5); }
 #syweyvwoby .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #syweyvwoby .gt_row_group_first td { border-top-width: 2px; }
 #syweyvwoby .gt_row_group_first th { border-top-width: 2px; }
 #syweyvwoby .gt_striped { color: #333333; background-color: #F4F4F4; }
 #syweyvwoby .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #syweyvwoby .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #syweyvwoby .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #syweyvwoby .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #syweyvwoby .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #syweyvwoby .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #syweyvwoby .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #syweyvwoby .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #syweyvwoby .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #syweyvwoby .gt_left { text-align: left; }
 #syweyvwoby .gt_center { text-align: center; }
 #syweyvwoby .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #syweyvwoby .gt_font_normal { font-weight: normal; }
 #syweyvwoby .gt_font_bold { font-weight: bold; }
 #syweyvwoby .gt_font_italic { font-style: italic; }
 #syweyvwoby .gt_super { font-size: 65%; }
 #syweyvwoby .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #syweyvwoby .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #syweyvwoby .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #syweyvwoby .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #syweyvwoby .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #syweyvwoby .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| open/close      | low/high        |
|-----------------|-----------------|
| 2033.47--2018.94 | 2017.22--2037.97 |
| 2033.13--2030.77 | 2026.61--2039.12 |
| 2031.73--2033.66 | 2022.31--2034.45 |
| 2024.37--2033.11 | 2020.46--2033.54 |
| 1996.47--2023.86 | 1996.47--2024.15 |
| 2003.66--1994.24 | 1990.73--2009.56 |


Now we'll use a portion of the [gtcars](data.gtcars.md#great_tables.data.gtcars) for the next example that accounts for missing values in the `pattern=` parameter. Use the `.cols_merge()` method twice to merge together the: (1) `trq` and `trq_rpm` columns, and (2) `mpg_c` & `mpg_h` columns. Given the presence of missing values, we can use patterns with `<<`/`>>` to create conditional text spans, avoiding results where any of the merged columns have missing values.


``` python
from great_tables.data import gtcars
import polars.selectors as cs

gtcars_pl = (
    pl.from_pandas(gtcars)
    .filter(pl.col("year") == 2017)
    .select(["mfr", "model", "trq", "trq_rpm", "mpg_c", "mpg_h"])
)

(
    GT(gtcars_pl)
    .fmt_integer(columns=[cs.starts_with("trq"), cs.starts_with("mpg")])
    .cols_merge(columns=["trq", "trq_rpm"], pattern="{0}<< ({1} rpm)>>")
    .cols_merge(columns=["mpg_c", "mpg_h"], pattern="<<{0} city<</{1} hwy>>>>")
    .cols_label(mfr="Manufacturer", model="Car Model", trq="Torque", mpg_c="MPG")
)
```


<style>
#qawbdzkike table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qawbdzkike thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qawbdzkike p { margin: 0; padding: 0; }
 #qawbdzkike .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qawbdzkike .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qawbdzkike .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qawbdzkike .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qawbdzkike .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qawbdzkike .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qawbdzkike .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qawbdzkike .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qawbdzkike .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qawbdzkike .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qawbdzkike .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qawbdzkike .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qawbdzkike .gt_spanner_row { border-bottom-style: hidden; }
 #qawbdzkike .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qawbdzkike .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qawbdzkike .gt_from_md> :first-child { margin-top: 0; }
 #qawbdzkike .gt_from_md> :last-child { margin-bottom: 0; }
 #qawbdzkike .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qawbdzkike .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qawbdzkike .gt_indent_1 { text-indent: 5px; }
 #qawbdzkike .gt_indent_2 { text-indent: calc(5px * 2); }
 #qawbdzkike .gt_indent_3 { text-indent: calc(5px * 3); }
 #qawbdzkike .gt_indent_4 { text-indent: calc(5px * 4); }
 #qawbdzkike .gt_indent_5 { text-indent: calc(5px * 5); }
 #qawbdzkike .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qawbdzkike .gt_row_group_first td { border-top-width: 2px; }
 #qawbdzkike .gt_row_group_first th { border-top-width: 2px; }
 #qawbdzkike .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qawbdzkike .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qawbdzkike .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qawbdzkike .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qawbdzkike .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qawbdzkike .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qawbdzkike .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qawbdzkike .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qawbdzkike .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qawbdzkike .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qawbdzkike .gt_left { text-align: left; }
 #qawbdzkike .gt_center { text-align: center; }
 #qawbdzkike .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qawbdzkike .gt_font_normal { font-weight: normal; }
 #qawbdzkike .gt_font_bold { font-weight: bold; }
 #qawbdzkike .gt_font_italic { font-style: italic; }
 #qawbdzkike .gt_super { font-size: 65%; }
 #qawbdzkike .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qawbdzkike .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qawbdzkike .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qawbdzkike .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qawbdzkike .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qawbdzkike .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Manufacturer | Car Model   | Torque          | MPG            |
|--------------|-------------|-----------------|----------------|
| Ford         | GT          | 550 (5,900 rpm) | 11 city/18 hwy |
| Ferrari      | GTC4Lusso   | 514 (5,750 rpm) | 12 city/17 hwy |
| Acura        | NSX         | 476 (2,000 rpm) | 21 city/22 hwy |
| Aston Martin | DB11        | 516 (1,500 rpm) | 15 city/21 hwy |
| Dodge        | Viper       | 600 (5,000 rpm) | 12 city/19 hwy |
| Lotus        | Evora       | 302 (3,500 rpm) | 16 city/24 hwy |
| Tesla        | Model S     | 243             |                |
| Porsche      | 718 Boxster | 280 (1,950 rpm) | 21 city/28 hwy |
| Porsche      | 718 Cayman  | 280 (1,950 rpm) | 20 city/29 hwy |
