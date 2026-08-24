# GT.fmt_tf()


Format True and False values


Usage

``` python
GT.fmt_tf(
    columns=None,
    rows=None,
    tf_style="true-false",
    pattern="{x}",
    true_val=None,
    false_val=None,
    na_val=None,
    colors=None
)
```


There can be times where boolean values are useful in a display table. You might want to express a 'yes' or 'no', a 'true' or 'false', or, perhaps use pairings of complementary symbols that make sense in a table. The [fmt_tf()](GT.fmt_tf.md#great_tables.GT.fmt_tf) method has a set of `tf_style=` presets that can be used to quickly map `True`/`False` values to strings, or, symbols like up/down or left/right arrows and open/closed shapes.

While the presets are nice, you can provide your own mappings through the `true_val=` and `false_val=` arguments. For extra customization, you can also apply color to the individual `True`, `False`, and NA mappings. Just supply a list of colors (up to a length of 3) to the `colors=` argument.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`tf_style: str = ``"true-false"`  
The `True`/`False` mapping style to use. By default this is the short name `"true-false"` which corresponds to the words `"true"` and `"false"`. Two other `tf_style=` values produce words: `"yes-no"` and `"up-down"`. The remaining options involve pairs of symbols (e.g., `"check-mark"` displays a check mark for `True` and an ✗ symbol for `False`).

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`true_val: str | None = None`  
While the choice of a `tf_style=` will typically supply the `true_val=` and `false_val=` text, we could override this and supply text for any `True` values. This doesn't need to be used in conjunction with `false_val=`.

`false_val: str | None = None`  
While the choice of a `tf_style=` will typically supply the `true_val=` and `false_val=` text, we could override this and supply text for any `False` values. This doesn't need to be used in conjunction with `true_val=`.

`na_val: str | None = None`  
None of the `tf_style` presets will replace any missing values encountered in the targeted cells. While we always have the option to use [sub_missing()](GT.sub_missing.md#great_tables.GT.sub_missing) for NA replacement, we have the opportunity handle missing values here with the `na_val=` option. This is useful because we also have the means to add color to the `na_val=` text or symbol and doing that requires that a replacement value for NAs is specified here.

`colors: list[str] | None = None`  
Providing a list of color values to colors will progressively add color to the formatted result depending on the number of colors provided. With a single color, all formatted values will be in that color. Using two colors results in `True` values being the first color, and `False` values receiving the second. With the three-color option, the final color will be given to any missing values replaced through `na_val=`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Formatting With The `tf_style=` Argument

We need to supply a preset `tf_style=` value. The following table provides a listing of all `tf_style=` values and their output `True` and `False` values.

|     | TF Style       | Output                                              |
|-----|----------------|-----------------------------------------------------|
| 1   | `"true-false"` | `"true" /`"false"`| | 2 |`"yes-no"`|`"yes" / `"no"` |
| 3   | `"up-down"`    | `"up" /`"down"`| | 4 |`"check-mark"`|`"✓" / `"✗"`   |
| 5   | `"circles"`    | `"●" /`"○"`| | 6 |`"squares"`|`"■" / `"□"`          |
| 7   | `"diamonds"`   | `"◆" /`"◇"`| | 8 |`"arrows"`|`"↑" / `"↓"`           |
| 9   | `"triangles"`  | `"▲" /`"▼"`| | 10 |`"triangles-lr"`|`"▶" / `"◀"`    |


## Examples

Let's use a subset of the [sp500](data.sp500.md#great_tables.data.sp500) dataset to create a small table containing opening and closing price data for the last few days in 2015. We added a boolean column (`dir`) where `True` indicates a price increase from opening to closing and `False` is the opposite. Using [fmt_tf()](GT.fmt_tf.md#great_tables.GT.fmt_tf) generates up and down arrows in the `dir` column. We elect to use green upward arrows and red downward arrows (through the `colors=` option).


``` python
from great_tables import GT
from great_tables.data import sp500
import polars as pl

sp500_mini = (
    pl.from_pandas(sp500)
    .slice(0, 5)
    .drop(["volume", "adj_close", "high", "low"])
    .with_columns(dir = pl.col("close") > pl.col("open"))
)

(
    GT(sp500_mini, rowname_col="date")
    .fmt_tf(columns="dir", tf_style="arrows", colors=["green", "red"])
    .fmt_currency(columns=["open", "close"])
    .cols_label(
        open="Opening",
        close="Closing",
        dir=""
    )
)
```


<style>
#dqukbitetx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dqukbitetx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dqukbitetx p { margin: 0; padding: 0; }
 #dqukbitetx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dqukbitetx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dqukbitetx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dqukbitetx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dqukbitetx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dqukbitetx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dqukbitetx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dqukbitetx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dqukbitetx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dqukbitetx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dqukbitetx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dqukbitetx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dqukbitetx .gt_spanner_row { border-bottom-style: hidden; }
 #dqukbitetx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dqukbitetx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dqukbitetx .gt_from_md> :first-child { margin-top: 0; }
 #dqukbitetx .gt_from_md> :last-child { margin-bottom: 0; }
 #dqukbitetx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dqukbitetx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dqukbitetx .gt_indent_1 { text-indent: 5px; }
 #dqukbitetx .gt_indent_2 { text-indent: calc(5px * 2); }
 #dqukbitetx .gt_indent_3 { text-indent: calc(5px * 3); }
 #dqukbitetx .gt_indent_4 { text-indent: calc(5px * 4); }
 #dqukbitetx .gt_indent_5 { text-indent: calc(5px * 5); }
 #dqukbitetx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dqukbitetx .gt_row_group_first td { border-top-width: 2px; }
 #dqukbitetx .gt_row_group_first th { border-top-width: 2px; }
 #dqukbitetx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dqukbitetx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dqukbitetx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dqukbitetx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dqukbitetx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dqukbitetx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dqukbitetx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dqukbitetx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dqukbitetx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dqukbitetx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dqukbitetx .gt_left { text-align: left; }
 #dqukbitetx .gt_center { text-align: center; }
 #dqukbitetx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dqukbitetx .gt_font_normal { font-weight: normal; }
 #dqukbitetx .gt_font_bold { font-weight: bold; }
 #dqukbitetx .gt_font_italic { font-style: italic; }
 #dqukbitetx .gt_super { font-size: 65%; }
 #dqukbitetx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dqukbitetx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dqukbitetx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dqukbitetx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dqukbitetx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dqukbitetx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|            | Opening    | Closing    |                                    |
|------------|------------|------------|------------------------------------|
| 2015-12-31 | \$2,060.59 | \$2,043.94 | <span style="color:red">↓</span>   |
| 2015-12-30 | \$2,077.34 | \$2,063.36 | <span style="color:red">↓</span>   |
| 2015-12-29 | \$2,060.54 | \$2,078.36 | <span style="color:green">↑</span> |
| 2015-12-28 | \$2,057.77 | \$2,056.50 | <span style="color:red">↓</span>   |
| 2015-12-24 | \$2,063.52 | \$2,060.99 | <span style="color:red">↓</span>   |
