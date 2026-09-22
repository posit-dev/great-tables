# GT.fmt_engineering()


Format values to engineering notation.


Usage

``` python
GT.fmt_engineering(
    columns=None,
    rows=None,
    decimals=2,
    n_sigfig=None,
    drop_trailing_zeros=False,
    drop_trailing_dec_mark=True,
    scale_by=1,
    exp_style="x10n",
    pattern="{x}",
    dec_mark=".",
    force_sign_m=False,
    force_sign_n=False,
    locale=None,
)
```


With numeric values in a table, we can perform formatting so that the targeted values are rendered in engineering notation, where numbers are written in the form of a mantissa (`m`) and an exponent (`n`). When combined the construction is either of the form *m* x 10^*n* or *m*E*n*. The mantissa is a number between `1` and `1000` and the exponent is a multiple of `3`. For example, the number `0.0000345` can be written in engineering notation as `34.50 x 10^-6`. This notation helps to simplify calculations and make it easier to compare numbers that are on very different scales.

Engineering notation is particularly useful as it aligns with SI prefixes (e.g., *milli-*, *micro-*, *kilo-*, *mega-*). For instance, numbers in engineering notation with exponent `-3` correspond to milli-units, while those with exponent `6` correspond to mega-units.

We have fine control over the formatting task, with the following options:

- decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice of the decimal symbol
- scaling: we can choose to scale targeted values by a multiplier value
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: providing a locale ID will result in formatting specific to the chosen locale


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`decimals: int = ``2`  
The `decimals` values corresponds to the exact number of decimal places to use. A value such as `2.34` can, for example, be formatted with `0` decimal places and it would result in `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros can be removed with `drop_trailing_zeros=True`.

`n_sigfig: int | None = None`  
A option to format numbers to *n* significant figures. By default, this is `None` and thus number values will be formatted according to the number of decimal places set via `decimals`. If opting to format according to the rules of significant figures, `n_sigfig` must be a number greater than or equal to `1`. Any values passed to the `decimals` and `drop_trailing_zeros` arguments will be ignored.

`drop_trailing_zeros: bool = ``False`  
A boolean value that allows for removal of trailing zeros (those redundant zeros after the decimal mark).

`drop_trailing_dec_mark: bool = ``True`  
A boolean value that determines whether decimal marks should always appear even if there are no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By default trailing decimal marks are not shown.

`scale_by: float = ``1`  
All numeric values will be multiplied by the `scale_by` value before undergoing formatting. Since the `default` value is `1`, no values will be changed unless a different multiplier value is supplied.

`exp_style: str = ``"x10n"`  
Style of formatting to use for the engineering notation formatting. By default this is `"x10n"` but other options include using a single letter (e.g., `"e"`, `"E"`, etc.), a letter followed by a `"1"` to signal a minimum digit width of one, or `"low-ten"` for using a stylized `"10"` marker.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`dec_mark: str = ``"."`  
The string to be used as the decimal mark. For example, using `dec_mark=","` with the value `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign_m: bool = ``False`  
Should the plus sign be shown for positive values of the mantissa (first component)? This would effectively show a sign for all values except zero on the first numeric component of the notation. If so, use `True` (the default for this is `False`), where only negative numbers will display a sign.

`force_sign_n: bool = ``False`  
Should the plus sign be shown for positive values of the exponent (second component)? This would effectively show a sign for all values except zero on the second numeric component of the notation. If so, use `True` (the default for this is `False`), where only negative numbers will display a sign.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). The use of a valid locale ID here means decimal marks will be correct for the given locale. Should a value be provided in `dec_mark` it will be overridden by the locale's preferred values.

Note that a `locale` value provided here will override any global locale setting performed in <a href="../reference/GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

With numeric values in a table, we can perform formatting so that the targeted values are rendered in engineering notation. For example, the number `0.0000345` can be written in engineering notation as `34.50 x 10^-6`.


``` python
import polars as pl
from great_tables import GT

numbers_df = pl.DataFrame({
    "numbers": [0.0000345, 3450, 3450000]
})

GT(numbers_df).fmt_engineering()
```


<style>
#eexzdccrot table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eexzdccrot thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eexzdccrot p { margin: 0; padding: 0; }
 #eexzdccrot .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eexzdccrot .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eexzdccrot .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eexzdccrot .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eexzdccrot .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eexzdccrot .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eexzdccrot .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eexzdccrot .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eexzdccrot .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eexzdccrot .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eexzdccrot .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eexzdccrot .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eexzdccrot .gt_spanner_row { border-bottom-style: hidden; }
 #eexzdccrot .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eexzdccrot .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eexzdccrot .gt_from_md> :first-child { margin-top: 0; }
 #eexzdccrot .gt_from_md> :last-child { margin-bottom: 0; }
 #eexzdccrot .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eexzdccrot .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eexzdccrot .gt_indent_1 { text-indent: 5px; }
 #eexzdccrot .gt_indent_2 { text-indent: calc(5px * 2); }
 #eexzdccrot .gt_indent_3 { text-indent: calc(5px * 3); }
 #eexzdccrot .gt_indent_4 { text-indent: calc(5px * 4); }
 #eexzdccrot .gt_indent_5 { text-indent: calc(5px * 5); }
 #eexzdccrot .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eexzdccrot .gt_row_group_first td { border-top-width: 2px; }
 #eexzdccrot .gt_row_group_first th { border-top-width: 2px; }
 #eexzdccrot .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eexzdccrot .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eexzdccrot .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eexzdccrot .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eexzdccrot .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eexzdccrot .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eexzdccrot .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eexzdccrot .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eexzdccrot .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eexzdccrot .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eexzdccrot .gt_left { text-align: left; }
 #eexzdccrot .gt_center { text-align: center; }
 #eexzdccrot .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eexzdccrot .gt_font_normal { font-weight: normal; }
 #eexzdccrot .gt_font_bold { font-weight: bold; }
 #eexzdccrot .gt_font_italic { font-style: italic; }
 #eexzdccrot .gt_super { font-size: 65%; }
 #eexzdccrot .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eexzdccrot .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eexzdccrot .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eexzdccrot .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eexzdccrot .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eexzdccrot .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| numbers                 |
|-------------------------|
| 34.50 × 10<sup>−6</sup> |
| 3.45 × 10<sup>3</sup>   |
| 3.45 × 10<sup>6</sup>   |


Notice that in each case, the exponent is a multiple of `3`.

Let's define a DataFrame that contains two columns of values (one small and one large). After creating a simple table with [GT()](GT.md#great_tables.GT), we'll call `fmt_engineering()` on both columns.


``` python
small_large_df = pl.DataFrame({
    "small": [10**-i for i in range(12, 0, -1)],
    "large": [10**i for i in range(1, 13)]
})

GT(small_large_df).fmt_engineering()
```


<style>
#wmskjptmda table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wmskjptmda thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wmskjptmda p { margin: 0; padding: 0; }
 #wmskjptmda .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wmskjptmda .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wmskjptmda .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wmskjptmda .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wmskjptmda .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wmskjptmda .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wmskjptmda .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wmskjptmda .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wmskjptmda .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wmskjptmda .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wmskjptmda .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wmskjptmda .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wmskjptmda .gt_spanner_row { border-bottom-style: hidden; }
 #wmskjptmda .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wmskjptmda .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wmskjptmda .gt_from_md> :first-child { margin-top: 0; }
 #wmskjptmda .gt_from_md> :last-child { margin-bottom: 0; }
 #wmskjptmda .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wmskjptmda .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wmskjptmda .gt_indent_1 { text-indent: 5px; }
 #wmskjptmda .gt_indent_2 { text-indent: calc(5px * 2); }
 #wmskjptmda .gt_indent_3 { text-indent: calc(5px * 3); }
 #wmskjptmda .gt_indent_4 { text-indent: calc(5px * 4); }
 #wmskjptmda .gt_indent_5 { text-indent: calc(5px * 5); }
 #wmskjptmda .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wmskjptmda .gt_row_group_first td { border-top-width: 2px; }
 #wmskjptmda .gt_row_group_first th { border-top-width: 2px; }
 #wmskjptmda .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wmskjptmda .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wmskjptmda .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wmskjptmda .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wmskjptmda .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wmskjptmda .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wmskjptmda .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wmskjptmda .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wmskjptmda .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wmskjptmda .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wmskjptmda .gt_left { text-align: left; }
 #wmskjptmda .gt_center { text-align: center; }
 #wmskjptmda .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wmskjptmda .gt_font_normal { font-weight: normal; }
 #wmskjptmda .gt_font_bold { font-weight: bold; }
 #wmskjptmda .gt_font_italic { font-style: italic; }
 #wmskjptmda .gt_super { font-size: 65%; }
 #wmskjptmda .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wmskjptmda .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wmskjptmda .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wmskjptmda .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wmskjptmda .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wmskjptmda .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| small                     | large                   |
|---------------------------|-------------------------|
| 1.00 × 10<sup>−12</sup>   | 10.00                   |
| 10.00 × 10<sup>−12</sup>  | 100.00                  |
| 100.00 × 10<sup>−12</sup> | 1.00 × 10<sup>3</sup>   |
| 1.00 × 10<sup>−9</sup>    | 10.00 × 10<sup>3</sup>  |
| 10.00 × 10<sup>−9</sup>   | 100.00 × 10<sup>3</sup> |
| 100.00 × 10<sup>−9</sup>  | 1.00 × 10<sup>6</sup>   |
| 1.00 × 10<sup>−6</sup>    | 10.00 × 10<sup>6</sup>  |
| 10.00 × 10<sup>−6</sup>   | 100.00 × 10<sup>6</sup> |
| 100.00 × 10<sup>−6</sup>  | 1.00 × 10<sup>9</sup>   |
| 1.00 × 10<sup>−3</sup>    | 10.00 × 10<sup>9</sup>  |
| 10.00 × 10<sup>−3</sup>   | 100.00 × 10<sup>9</sup> |
| 100.00 × 10<sup>−3</sup>  | 1.00 × 10<sup>12</sup>  |


Notice that within the form of *m* x 10^*n*, the *n* values move in steps of 3 (away from 0), and *m* values can have 1-3 digits before the decimal. Further to this, any values where *n* is 0 results in a display of only *m* (the first two values in the `large` column demonstrates this).

Engineering notation expresses values so that they align to certain SI prefixes. Here is a table that compares select SI prefixes and their symbols to decimal and engineering-notation representations of the key numbers.


``` python
import polars as pl
from great_tables import GT

prefixes_df = pl.DataFrame({
    "name": [
        "peta", "tera", "giga", "mega", "kilo",
        None,
        "milli", "micro", "nano", "pico", "femto"
    ],
    "symbol": [
        "P", "T", "G", "M", "k",
        None,
        "m", "μ", "n", "p", "f"
    ],
    "decimal": [float(10**i) for i in range(15, -18, -3)],
})

prefixes_df = prefixes_df.with_columns(
    engineering=pl.col("decimal")
)

(
    GT(prefixes_df)
    .fmt_number(columns="decimal", n_sigfig=1)
    .fmt_engineering(columns="engineering")
    .sub_missing()
)
```


<style>
#enmylirdgc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#enmylirdgc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#enmylirdgc p { margin: 0; padding: 0; }
 #enmylirdgc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #enmylirdgc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #enmylirdgc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #enmylirdgc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #enmylirdgc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #enmylirdgc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #enmylirdgc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #enmylirdgc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #enmylirdgc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #enmylirdgc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #enmylirdgc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #enmylirdgc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #enmylirdgc .gt_spanner_row { border-bottom-style: hidden; }
 #enmylirdgc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #enmylirdgc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #enmylirdgc .gt_from_md> :first-child { margin-top: 0; }
 #enmylirdgc .gt_from_md> :last-child { margin-bottom: 0; }
 #enmylirdgc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #enmylirdgc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #enmylirdgc .gt_indent_1 { text-indent: 5px; }
 #enmylirdgc .gt_indent_2 { text-indent: calc(5px * 2); }
 #enmylirdgc .gt_indent_3 { text-indent: calc(5px * 3); }
 #enmylirdgc .gt_indent_4 { text-indent: calc(5px * 4); }
 #enmylirdgc .gt_indent_5 { text-indent: calc(5px * 5); }
 #enmylirdgc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #enmylirdgc .gt_row_group_first td { border-top-width: 2px; }
 #enmylirdgc .gt_row_group_first th { border-top-width: 2px; }
 #enmylirdgc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #enmylirdgc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #enmylirdgc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #enmylirdgc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #enmylirdgc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #enmylirdgc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #enmylirdgc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #enmylirdgc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #enmylirdgc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #enmylirdgc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #enmylirdgc .gt_left { text-align: left; }
 #enmylirdgc .gt_center { text-align: center; }
 #enmylirdgc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #enmylirdgc .gt_font_normal { font-weight: normal; }
 #enmylirdgc .gt_font_bold { font-weight: bold; }
 #enmylirdgc .gt_font_italic { font-style: italic; }
 #enmylirdgc .gt_super { font-size: 65%; }
 #enmylirdgc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #enmylirdgc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #enmylirdgc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #enmylirdgc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #enmylirdgc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #enmylirdgc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| name  | symbol | decimal               | engineering             |
|-------|--------|-----------------------|-------------------------|
| peta  | P      | 1,000,000,000,000,000 | 1.00 × 10<sup>15</sup>  |
| tera  | T      | 1,000,000,000,000     | 1.00 × 10<sup>12</sup>  |
| giga  | G      | 1,000,000,000         | 1.00 × 10<sup>9</sup>   |
| mega  | M      | 1,000,000             | 1.00 × 10<sup>6</sup>   |
| kilo  | k      | 1,000                 | 1.00 × 10<sup>3</sup>   |
| --     | --      | 1                     | 1.00                    |
| milli | m      | 0.001                 | 1.00 × 10<sup>−3</sup>  |
| micro | μ      | 0.000001              | 1.00 × 10<sup>−6</sup>  |
| nano  | n      | 0.000000001           | 1.00 × 10<sup>−9</sup>  |
| pico  | p      | 0.000000000001        | 1.00 × 10<sup>−12</sup> |
| femto | f      | 0.000000000000001     | 1.00 × 10<sup>−15</sup> |
