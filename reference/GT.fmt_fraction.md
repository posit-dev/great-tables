# GT.fmt_fraction()


Format values as mixed fractions.


Usage

``` python
GT.fmt_fraction(
    columns=None,
    rows=None,
    accuracy="low",
    simplify=True,
    layout="inline",
    use_seps=True,
    pattern="{x}",
    sep_mark=",",
    locale=None,
)
```


With numeric values in a **gt** table, we can perform mixed-fraction-based formatting. There are several options for setting the accuracy of the fractions. Furthermore, there is an option for choosing a layout (i.e., typesetting style) for the mixed-fraction output.

The `accuracy=` parameter controls the type of fractions generated. It can be one of the keywords `"low"`, `"med"`, or `"high"` (to generate fractions with denominators of up to 1, 2, or 3 digits, respectively) or an integer value greater than zero to obtain fractions with a fixed denominator (`2` yields halves, `3` is for thirds, `4` is quarters, etc.). If choosing to provide a numeric value for `accuracy=`, the option to simplify the fraction (where possible) can be taken with `simplify=True` (the default for this is `True`).

For HTML output, the `"inline"` layout (the default) places the numerals of the fraction on the baseline and uses a standard slash character. The `"diagonal"` layout will generate fractions that are typeset with raised and lowered numerals and a virgule (i.e., a fraction slash).


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`accuracy: str | int = ``"low"`  
The accuracy of the fraction. Use `"low"` for denominators up to 1 digit (e.g., halves, thirds, quarters, etc.), `"med"` for up to 2-digit denominators, and `"high"` for up to 3-digit denominators. Alternatively, supply a positive integer to fix the denominator to that value (e.g., `accuracy=8` gives eighths). The default is `"low"`.

`simplify: bool = ``True`  
When `accuracy=` is an integer, should the fraction be simplified via GCD reduction? For while `simplify=False` yields `"2/4"`. Has no effect when `accuracy=` is a keyword example, with `accuracy=4` and a value of `0.5`, `simplify=True` yields a `"1/2"` string representation. The default is `True`.

`layout: str = ``"inline"`  
The layout of the fraction. `"inline"` renders the fraction on the baseline with a standard slash (e.g., `3/4`). `"diagonal"` renders a diagonal fraction with a raised numerator, lowered denominator, and a fraction slash character (HTML only and falls back to inline in other contexts). The default is `"inline"`.

`use_seps: bool = ``True`  
Whether to use digit grouping separators in the whole-number part. The default is `True`.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ``","`  
The mark to use as a thousands separator. The default is `","` and can be overridden by a locale setting.

`locale: str | None = None`  
An optional locale ID that can be used for applying a locale-specific thousands separator.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's format the `num` column of the [exibble](data.exibble.md#great_tables.data.exibble) dataset as fractions with the default `"low"` accuracy.


``` python
from great_tables import GT
from great_tables.data import exibble

(
    GT(exibble[["num", "char"]])
    .fmt_fraction(columns="num")
)
```


<style>
#iwokzphemx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iwokzphemx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iwokzphemx p { margin: 0; padding: 0; }
 #iwokzphemx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iwokzphemx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iwokzphemx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iwokzphemx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iwokzphemx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iwokzphemx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iwokzphemx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iwokzphemx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iwokzphemx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iwokzphemx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iwokzphemx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iwokzphemx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iwokzphemx .gt_spanner_row { border-bottom-style: hidden; }
 #iwokzphemx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iwokzphemx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iwokzphemx .gt_from_md> :first-child { margin-top: 0; }
 #iwokzphemx .gt_from_md> :last-child { margin-bottom: 0; }
 #iwokzphemx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iwokzphemx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iwokzphemx .gt_indent_1 { text-indent: 5px; }
 #iwokzphemx .gt_indent_2 { text-indent: calc(5px * 2); }
 #iwokzphemx .gt_indent_3 { text-indent: calc(5px * 3); }
 #iwokzphemx .gt_indent_4 { text-indent: calc(5px * 4); }
 #iwokzphemx .gt_indent_5 { text-indent: calc(5px * 5); }
 #iwokzphemx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iwokzphemx .gt_row_group_first td { border-top-width: 2px; }
 #iwokzphemx .gt_row_group_first th { border-top-width: 2px; }
 #iwokzphemx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iwokzphemx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iwokzphemx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iwokzphemx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iwokzphemx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iwokzphemx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iwokzphemx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iwokzphemx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iwokzphemx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iwokzphemx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iwokzphemx .gt_left { text-align: left; }
 #iwokzphemx .gt_center { text-align: center; }
 #iwokzphemx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iwokzphemx .gt_font_normal { font-weight: normal; }
 #iwokzphemx .gt_font_bold { font-weight: bold; }
 #iwokzphemx .gt_font_italic { font-style: italic; }
 #iwokzphemx .gt_super { font-size: 65%; }
 #iwokzphemx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iwokzphemx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iwokzphemx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iwokzphemx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iwokzphemx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iwokzphemx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num       | char       |
|-----------|------------|
| 1/9       | apricot    |
| 2 2/9     | banana     |
| 33 1/3    | coconut    |
| 444 2/5   | durian     |
| 5,550     | None       |
| None      | fig        |
| 777,000   | grapefruit |
| 8,880,000 | honeydew   |


We can increase the accuracy to `"med"` or `"high"` for more precise fractions. We can also use a fixed denominator (here, tenths) to get uniform fractions. With `simplify=False`, the denominator stays fixed even when the fraction could be reduced, and `layout="diagonal"` gives us a typeset diagonal-fraction style.


``` python
import polars as pl

df = pl.DataFrame({
    "item": ["Icate", "Octyl", "Sepal", "Unkel"],
    "frac_sales": [0.3, 0.1, 0.8, 0.5],
    "frac_revenue": [0.2, 0.4, 0.7, 0.9],
})

(
    GT(df, rowname_col="item")
    .fmt_fraction(
        columns=["frac_sales", "frac_revenue"],
        accuracy=10,
        simplify=False,
        layout="diagonal",
    )
)
```


<style>
#nvawyycdvj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nvawyycdvj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nvawyycdvj p { margin: 0; padding: 0; }
 #nvawyycdvj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nvawyycdvj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nvawyycdvj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nvawyycdvj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nvawyycdvj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nvawyycdvj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvawyycdvj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nvawyycdvj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nvawyycdvj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nvawyycdvj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nvawyycdvj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nvawyycdvj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nvawyycdvj .gt_spanner_row { border-bottom-style: hidden; }
 #nvawyycdvj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nvawyycdvj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nvawyycdvj .gt_from_md> :first-child { margin-top: 0; }
 #nvawyycdvj .gt_from_md> :last-child { margin-bottom: 0; }
 #nvawyycdvj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nvawyycdvj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nvawyycdvj .gt_indent_1 { text-indent: 5px; }
 #nvawyycdvj .gt_indent_2 { text-indent: calc(5px * 2); }
 #nvawyycdvj .gt_indent_3 { text-indent: calc(5px * 3); }
 #nvawyycdvj .gt_indent_4 { text-indent: calc(5px * 4); }
 #nvawyycdvj .gt_indent_5 { text-indent: calc(5px * 5); }
 #nvawyycdvj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nvawyycdvj .gt_row_group_first td { border-top-width: 2px; }
 #nvawyycdvj .gt_row_group_first th { border-top-width: 2px; }
 #nvawyycdvj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nvawyycdvj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvawyycdvj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nvawyycdvj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nvawyycdvj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvawyycdvj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nvawyycdvj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nvawyycdvj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nvawyycdvj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvawyycdvj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nvawyycdvj .gt_left { text-align: left; }
 #nvawyycdvj .gt_center { text-align: center; }
 #nvawyycdvj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nvawyycdvj .gt_font_normal { font-weight: normal; }
 #nvawyycdvj .gt_font_bold { font-weight: bold; }
 #nvawyycdvj .gt_font_italic { font-style: italic; }
 #nvawyycdvj .gt_super { font-size: 65%; }
 #nvawyycdvj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvawyycdvj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nvawyycdvj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvawyycdvj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nvawyycdvj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nvawyycdvj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | frac_sales | frac_revenue |
|----|----|----|
| Icate | <span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span> | <span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">2</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span> |
| Octyl | <span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">1</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span> | <span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">4</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span> |
| Sepal | <span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">8</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span> | <span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">7</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span> |
| Unkel | <span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">5</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span> | <span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">9</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span> |


The [pizzaplace](data.pizzaplace.md#great_tables.data.pizzaplace) dataset has a full year of sales data. We can summarize the sell count and revenue by pizza size within each type, then express those as fractions. Using `layout="diagonal"` with `accuracy=10` and `simplify=False` gives uniform tenths in a typeset style, and [text_transform()](GT.text_transform.md#great_tables.GT.text_transform) replaces any zero-fraction values with *nil*.


``` python
import polars as pl
import polars.selectors as cs
from great_tables import md, loc, data

grouped = (
    data.pl.pizzaplace
    .group_by("type", "size")
    .agg(
        pl.col("id").count().alias("sold"),
        pl.col("price").sum().alias("income"),
    )
    .with_columns(
        (pl.col("sold") / pl.col("sold").sum().over("type")).alias("f_sold"),
        (pl.col("income") / pl.col("income").sum().over("type")).alias("f_income"),
    )
    .sort(["type", "income"], descending=[False, True])
)

(
    GT(grouped, rowname_col="size", groupname_col="type")
    .tab_header(
        title="Pizzas Sold in 2015",
        subtitle="Fraction of Sell Count and Revenue by Size per Type",
    )
    .fmt_integer(columns="sold")
    .fmt_currency(columns="income")
    .fmt_fraction(
        columns=cs.starts_with("f_"),
        accuracy=10,
        simplify=False,
        layout="diagonal",
    )
    .sub_missing(missing_text="")
    .tab_spanner(label="Sold", columns=cs.contains("sold"))
    .tab_spanner(label="Revenue", columns=cs.contains("income"))
    .text_transform(
        locations=loc.body(),
        fn=lambda x: "<em>nil</em>" if x == "0" else x,
    )
    .cols_label(
        sold="Amount",
        income="Amount",
        f_sold=md("_f_"),
        f_income=md("_f_"),
    )
    .cols_align(align="center", columns=cs.starts_with("f"))
    .tab_options(
        table_width="400px",
        row_group_as_column=True,
    )
)
```


<style>
#meaczwfygd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#meaczwfygd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#meaczwfygd p { margin: 0; padding: 0; }
 #meaczwfygd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: 400px; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #meaczwfygd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #meaczwfygd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #meaczwfygd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #meaczwfygd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #meaczwfygd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #meaczwfygd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #meaczwfygd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #meaczwfygd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #meaczwfygd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #meaczwfygd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #meaczwfygd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #meaczwfygd .gt_spanner_row { border-bottom-style: hidden; }
 #meaczwfygd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #meaczwfygd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #meaczwfygd .gt_from_md> :first-child { margin-top: 0; }
 #meaczwfygd .gt_from_md> :last-child { margin-bottom: 0; }
 #meaczwfygd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #meaczwfygd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #meaczwfygd .gt_indent_1 { text-indent: 5px; }
 #meaczwfygd .gt_indent_2 { text-indent: calc(5px * 2); }
 #meaczwfygd .gt_indent_3 { text-indent: calc(5px * 3); }
 #meaczwfygd .gt_indent_4 { text-indent: calc(5px * 4); }
 #meaczwfygd .gt_indent_5 { text-indent: calc(5px * 5); }
 #meaczwfygd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #meaczwfygd .gt_row_group_first td { border-top-width: 2px; }
 #meaczwfygd .gt_row_group_first th { border-top-width: 2px; }
 #meaczwfygd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #meaczwfygd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #meaczwfygd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #meaczwfygd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #meaczwfygd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #meaczwfygd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #meaczwfygd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #meaczwfygd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #meaczwfygd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #meaczwfygd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #meaczwfygd .gt_left { text-align: left; }
 #meaczwfygd .gt_center { text-align: center; }
 #meaczwfygd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #meaczwfygd .gt_font_normal { font-weight: normal; }
 #meaczwfygd .gt_font_bold { font-weight: bold; }
 #meaczwfygd .gt_font_italic { font-style: italic; }
 #meaczwfygd .gt_super { font-size: 65%; }
 #meaczwfygd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #meaczwfygd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #meaczwfygd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #meaczwfygd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #meaczwfygd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #meaczwfygd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Pizzas Sold in 2015</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Fraction of Sell Count and Revenue by Size per Type</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="2" rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="colgroup"></th>
<th colspan="2" id="Sold" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Sold</th>
<th colspan="2" id="Revenue" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Revenue</th>
</tr>
<tr class="gt_col_headings">
<th id="sold" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Amount</th>
<th id="f_sold" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col"><em>f</em></th>
<th id="income" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Amount</th>
<th id="f_income" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col"><em>f</em></th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_row_group_first">
<th rowspan="3" class="gt_row gt_left gt_stub_row_group">chicken</th>
<th class="gt_row gt_left gt_stub">L</th>
<td class="gt_row gt_right">4,932</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">4</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$102,339.00</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">5</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">M</th>
<td class="gt_row gt_right">3,894</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">4</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$65,224.50</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">S</th>
<td class="gt_row gt_right">2,224</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">2</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$28,356.00</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">1</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr class="gt_row_group_first">
<th rowspan="5" class="gt_row gt_left gt_stub_row_group">classic</th>
<th class="gt_row gt_left gt_stub">L</th>
<td class="gt_row gt_right">4,057</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$74,518.50</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">S</th>
<td class="gt_row gt_right">6,139</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">4</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$69,870.25</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">M</th>
<td class="gt_row gt_right">4,112</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$60,581.75</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">XL</th>
<td class="gt_row gt_right">552</td>
<td class="gt_row gt_center"><em>nil</em></td>
<td class="gt_row gt_right">$14,076.00</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">1</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">XXL</th>
<td class="gt_row gt_right">28</td>
<td class="gt_row gt_center"><em>nil</em></td>
<td class="gt_row gt_right">$1,006.60</td>
<td class="gt_row gt_center"><em>nil</em></td>
</tr>
<tr class="gt_row_group_first">
<th rowspan="3" class="gt_row gt_left gt_stub_row_group">supreme</th>
<th class="gt_row gt_left gt_stub">L</th>
<td class="gt_row gt_right">4,564</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">4</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$94,258.50</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">5</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">M</th>
<td class="gt_row gt_right">4,046</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$66,475.00</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">S</th>
<td class="gt_row gt_right">3,377</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$47,463.50</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">2</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr class="gt_row_group_first">
<th rowspan="3" class="gt_row gt_left gt_stub_row_group">veggie</th>
<th class="gt_row gt_left gt_stub">L</th>
<td class="gt_row gt_right">5,403</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">5</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$104,202.70</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">5</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">M</th>
<td class="gt_row gt_right">3,583</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$57,101.00</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">3</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">S</th>
<td class="gt_row gt_right">2,663</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">2</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
<td class="gt_row gt_right">$32,386.75</td>
<td class="gt_row gt_center"><span style="font-size:0.6em;line-height:0.6em;vertical-align:0.45em;">2</span><span style="font-size:0.7em;line-height:0.7em;vertical-align:0.15em;">⁄</span><span style="font-size:0.6em;line-height:0.6em;vertical-align:-0.05em;">10</span></td>
</tr>
</tbody>
</table>
