# GT.fmt_partsper()


Format values as parts-per quantities.


Usage

``` python
GT.fmt_partsper(
    columns=None,
    rows=None,
    to_units="per-mille",
    symbol="auto",
    decimals=2,
    drop_trailing_zeros=False,
    drop_trailing_dec_mark=True,
    scale_values=True,
    use_seps=True,
    pattern="{x}",
    sep_mark=",",
    dec_mark=".",
    force_sign=False,
    incl_space="auto",
    locale=None,
)
```


With numeric values in a **gt** table, we can format the values so that they are rendered as parts-per quantities (per mille, ppm, ppb, etc.). The following keywords are available for the `to_units` parameter:

- `"per-mille"`: Per mille (1 part in 1,000)
- `"per-myriad"`: Per myriad (1 part in 10,000)
- `"pcm"`: Per cent mille (1 part in 100,000)
- `"ppm"`: Parts per million (1 part in 1,000,000)
- `"ppb"`: Parts per billion (1 part in 1,000,000,000)
- `"ppt"`: Parts per trillion (1 part in 1,000,000,000,000)
- `"ppq"`: Parts per quadrillion (1 part in 1,000,000,000,000,000)

The function provides a lot of formatting control and we can use the following options:

- custom symbol/units: override the automatic symbol or units display with a custom choice
- decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice of the decimal symbol
- digit grouping separators: options to enable/disable digit separators and provide a choice of separator symbol
- value scaling toggle: choose to disable automatic value scaling in the situation that values are already scaled coming in (and just require the appropriate symbol or unit display)
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: providing a locale ID will result in number formatting specific to the chosen locale


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`to_units: str = ``"per-mille"`  
A keyword that signifies the desired output quantity. This can be any from the following set: `"per-mille"`, `"per-myriad"`, `"pcm"`, `"ppm"`, `"ppb"`, `"ppt"`, or `"ppq"`.

`symbol: str = ``"auto"`  
The symbol/units to use for the quantity. By default, this is set to `"auto"` and the appropriate symbol will be chosen based on the `to_units` keyword and the output context. This can be changed by supplying a string (e.g., using `symbol="ppbV"` when `to_units="ppb"`).

`decimals: int = ``2`  
The `decimals` values corresponds to the exact number of decimal places to use. A value such as `2.34` can, for example, be formatted with `0` decimal places and it would result in `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros can be removed with `drop_trailing_zeros=True`.

`drop_trailing_zeros: bool = ``False`  
A boolean value that allows for removal of trailing zeros (those redundant zeros after the decimal mark).

`drop_trailing_dec_mark: bool = ``True`  
A boolean value that determines whether decimal marks should always appear even if there are no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By default trailing decimal marks are not shown.

`scale_values: bool = ``True`  
Should the values be scaled through multiplication according to the keyword set in `to_units`? By default this is `True` since the expectation is that normally values are proportions. Setting to `False` signifies that the values are already scaled and require only the appropriate symbol/units when formatted.

`use_seps: bool = ``True`  
The `use_seps` option allows for the use of digit group separators. The type of digit group separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This setting is `True` by default.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ``","`  
The string to use as a separator between groups of digits. For example, using `sep_mark=","` with a value of `1000` would result in a formatted value of `"1,000"`. This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`dec_mark: str = ``"."`  
The string to be used as the decimal mark. For example, using `dec_mark=","` with the value `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign: bool = ``False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option. The default is `False`, where only negative numbers will display a minus sign.

`incl_space: str | bool = ``"auto"`  
An option for whether to include a space between the value and the symbol/units. The default is `"auto"` which provides spacing dependent on the mark itself (symbols like `‰` get no space; text abbreviations like `ppm` get a space). This can be directly controlled by using either `True` or `False`.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). The use of a valid locale ID here means separator and decimal marks will be correct for the given locale. Should any values be provided in `sep_mark` or `dec_mark`, they will be overridden by the locale's preferred values.

Note that a `locale` value provided here will override any global locale setting performed in <a href="../reference/GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

Let's use a small dataset with proportional values and format them as parts-per-mille values.


``` python
from great_tables import GT
import pandas as pd

df = pd.DataFrame({"x": [0.001, 0.0001, 0.00001, 0.5, -0.005]})

GT(df).fmt_partsper(columns="x", to_units="per-mille")
```


<style>
#icnkmvumij table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#icnkmvumij thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#icnkmvumij p { margin: 0; padding: 0; }
 #icnkmvumij .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #icnkmvumij .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #icnkmvumij .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #icnkmvumij .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #icnkmvumij .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #icnkmvumij .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #icnkmvumij .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #icnkmvumij .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #icnkmvumij .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #icnkmvumij .gt_column_spanner_outer:first-child { padding-left: 0; }
 #icnkmvumij .gt_column_spanner_outer:last-child { padding-right: 0; }
 #icnkmvumij .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #icnkmvumij .gt_spanner_row { border-bottom-style: hidden; }
 #icnkmvumij .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #icnkmvumij .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #icnkmvumij .gt_from_md> :first-child { margin-top: 0; }
 #icnkmvumij .gt_from_md> :last-child { margin-bottom: 0; }
 #icnkmvumij .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #icnkmvumij .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #icnkmvumij .gt_indent_1 { text-indent: 5px; }
 #icnkmvumij .gt_indent_2 { text-indent: calc(5px * 2); }
 #icnkmvumij .gt_indent_3 { text-indent: calc(5px * 3); }
 #icnkmvumij .gt_indent_4 { text-indent: calc(5px * 4); }
 #icnkmvumij .gt_indent_5 { text-indent: calc(5px * 5); }
 #icnkmvumij .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #icnkmvumij .gt_row_group_first td { border-top-width: 2px; }
 #icnkmvumij .gt_row_group_first th { border-top-width: 2px; }
 #icnkmvumij .gt_striped { color: #333333; background-color: #F4F4F4; }
 #icnkmvumij .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #icnkmvumij .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #icnkmvumij .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #icnkmvumij .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #icnkmvumij .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #icnkmvumij .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #icnkmvumij .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #icnkmvumij .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #icnkmvumij .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #icnkmvumij .gt_left { text-align: left; }
 #icnkmvumij .gt_center { text-align: center; }
 #icnkmvumij .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #icnkmvumij .gt_font_normal { font-weight: normal; }
 #icnkmvumij .gt_font_bold { font-weight: bold; }
 #icnkmvumij .gt_font_italic { font-style: italic; }
 #icnkmvumij .gt_super { font-size: 65%; }
 #icnkmvumij .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #icnkmvumij .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #icnkmvumij .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #icnkmvumij .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #icnkmvumij .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #icnkmvumij .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| x       |
|---------|
| 1.00‰   |
| 0.10‰   |
| 0.01‰   |
| 500.00‰ |
| −5.00‰  |


We can also format values as parts per million (ppm) using a Polars DataFrame:


``` python
import polars as pl
from great_tables import GT

df = pl.DataFrame({"x": [0.0000015, 0.00035, 0.0001]})

GT(df).fmt_partsper(columns="x", to_units="ppm")
```


<style>
#wnvoefrtes table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wnvoefrtes thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wnvoefrtes p { margin: 0; padding: 0; }
 #wnvoefrtes .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wnvoefrtes .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wnvoefrtes .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wnvoefrtes .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wnvoefrtes .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnvoefrtes .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnvoefrtes .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnvoefrtes .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wnvoefrtes .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wnvoefrtes .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wnvoefrtes .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wnvoefrtes .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wnvoefrtes .gt_spanner_row { border-bottom-style: hidden; }
 #wnvoefrtes .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wnvoefrtes .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wnvoefrtes .gt_from_md> :first-child { margin-top: 0; }
 #wnvoefrtes .gt_from_md> :last-child { margin-bottom: 0; }
 #wnvoefrtes .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wnvoefrtes .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wnvoefrtes .gt_indent_1 { text-indent: 5px; }
 #wnvoefrtes .gt_indent_2 { text-indent: calc(5px * 2); }
 #wnvoefrtes .gt_indent_3 { text-indent: calc(5px * 3); }
 #wnvoefrtes .gt_indent_4 { text-indent: calc(5px * 4); }
 #wnvoefrtes .gt_indent_5 { text-indent: calc(5px * 5); }
 #wnvoefrtes .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wnvoefrtes .gt_row_group_first td { border-top-width: 2px; }
 #wnvoefrtes .gt_row_group_first th { border-top-width: 2px; }
 #wnvoefrtes .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wnvoefrtes .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnvoefrtes .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnvoefrtes .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wnvoefrtes .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnvoefrtes .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnvoefrtes .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wnvoefrtes .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wnvoefrtes .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnvoefrtes .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnvoefrtes .gt_left { text-align: left; }
 #wnvoefrtes .gt_center { text-align: center; }
 #wnvoefrtes .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wnvoefrtes .gt_font_normal { font-weight: normal; }
 #wnvoefrtes .gt_font_bold { font-weight: bold; }
 #wnvoefrtes .gt_font_italic { font-style: italic; }
 #wnvoefrtes .gt_super { font-size: 65%; }
 #wnvoefrtes .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnvoefrtes .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wnvoefrtes .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnvoefrtes .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnvoefrtes .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wnvoefrtes .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| x          |
|------------|
| 1.50 ppm   |
| 350.00 ppm |
| 100.00 ppm |


If the values are already scaled (not proportions), set `scale_values=False` and use a custom symbol:


``` python
import polars as pl
from great_tables import GT

concentrations = pl.DataFrame({"gas": ["CO", "NO2", "O3"], "conc": [1.5, 35.0, 120.0]})

GT(concentrations).fmt_partsper(columns="conc", to_units="ppb", scale_values=False, symbol="ppbV")
```


<style>
#lyhdvfzjdm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lyhdvfzjdm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lyhdvfzjdm p { margin: 0; padding: 0; }
 #lyhdvfzjdm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lyhdvfzjdm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lyhdvfzjdm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lyhdvfzjdm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lyhdvfzjdm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lyhdvfzjdm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lyhdvfzjdm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lyhdvfzjdm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lyhdvfzjdm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lyhdvfzjdm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lyhdvfzjdm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lyhdvfzjdm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lyhdvfzjdm .gt_spanner_row { border-bottom-style: hidden; }
 #lyhdvfzjdm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lyhdvfzjdm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lyhdvfzjdm .gt_from_md> :first-child { margin-top: 0; }
 #lyhdvfzjdm .gt_from_md> :last-child { margin-bottom: 0; }
 #lyhdvfzjdm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lyhdvfzjdm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lyhdvfzjdm .gt_indent_1 { text-indent: 5px; }
 #lyhdvfzjdm .gt_indent_2 { text-indent: calc(5px * 2); }
 #lyhdvfzjdm .gt_indent_3 { text-indent: calc(5px * 3); }
 #lyhdvfzjdm .gt_indent_4 { text-indent: calc(5px * 4); }
 #lyhdvfzjdm .gt_indent_5 { text-indent: calc(5px * 5); }
 #lyhdvfzjdm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lyhdvfzjdm .gt_row_group_first td { border-top-width: 2px; }
 #lyhdvfzjdm .gt_row_group_first th { border-top-width: 2px; }
 #lyhdvfzjdm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lyhdvfzjdm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lyhdvfzjdm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lyhdvfzjdm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lyhdvfzjdm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lyhdvfzjdm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lyhdvfzjdm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lyhdvfzjdm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lyhdvfzjdm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lyhdvfzjdm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lyhdvfzjdm .gt_left { text-align: left; }
 #lyhdvfzjdm .gt_center { text-align: center; }
 #lyhdvfzjdm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lyhdvfzjdm .gt_font_normal { font-weight: normal; }
 #lyhdvfzjdm .gt_font_bold { font-weight: bold; }
 #lyhdvfzjdm .gt_font_italic { font-style: italic; }
 #lyhdvfzjdm .gt_super { font-size: 65%; }
 #lyhdvfzjdm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lyhdvfzjdm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lyhdvfzjdm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lyhdvfzjdm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lyhdvfzjdm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lyhdvfzjdm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| gas | conc        |
|-----|-------------|
| CO  | 1.50 ppbV   |
| NO2 | 35.00 ppbV  |
| O3  | 120.00 ppbV |
