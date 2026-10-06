# GT.fmt_number_si()


Format values with SI (metric) prefixes.


Usage

``` python
GT.fmt_number_si(
    columns=None,
    rows=None,
    unit=None,
    decimals=2,
    n_sigfig=None,
    drop_trailing_zeros=False,
    drop_trailing_dec_mark=True,
    scale_by=1,
    prefix_mode="engineering",
    pattern="{x}",
    sep_mark=",",
    dec_mark=".",
    force_sign=False,
    incl_space=True,
    locale=None,
)
```


Format numeric values with SI (International System of Units) prefixes, automatically selecting the appropriate prefix to keep the mantissa in a readable range. SI prefixes range from quetta (Q, 10^30) to quecto (q, 10^-30) and are commonly used in scientific and engineering contexts to represent very large or very small quantities with units (e.g., `"5.2 kW"`, `"3.8 ng"`, `"1.2 GHz"`, etc.).

This function provides fine control over SI prefix formatting with the following options:

- unit specification: define a unit to append after the SI prefix (e.g., `"g"` for grams, `"W"` for watts, `"Hz"` for hertz, `"m"` for meters)
- prefix selection: choose between all SI prefixes or only engineering prefixes (powers of

1000. 

- precision control: specify decimal places for consistent formatting
- spacing: customize the separator between number, prefix, and unit
- scaling: we can choose to scale targeted values by a multiplier value (useful for unit conversions)
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: use locale-specific decimal and thousands separators


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`unit: str | None = None`  
A character string specifying the unit to append after the SI prefix (e.g., `"g"` for grams, `"W"` for watts, `"Hz"` for hertz, `"m"` for meters). If `None`, only the prefix will be shown.

`decimals: int = ``2`  
The `decimals=` values corresponds to the exact number of decimal places to use. A value such as `2.34` can, for example, be formatted with `0` decimal places and it would result in `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros can be removed with `drop_trailing_zeros=True`. If `n_sigfig` is provided, `decimals` is ignored.

`n_sigfig: int | None = None`  
A option to format numbers to *n* significant figures. By default, this is `None` and thus number values will be formatted according to the number of decimal places set via `decimals=`. If opting to format according to the rules of significant figures, `n_sigfig=` must be a number greater than or equal to `1`. Any values passed to the `decimals=` and `drop_trailing_zeros=` arguments will be ignored.

`drop_trailing_zeros: bool = ``False`  
A boolean value that allows for removal of trailing zeros (those redundant zeros after the decimal mark).

`drop_trailing_dec_mark: bool = ``True`  
A boolean value that determines whether decimal marks should always appear even if there are no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By default trailing decimal marks are not shown.

`scale_by: float = ``1`  
All numeric values will be multiplied by the `scale_by` value before undergoing formatting. Since the `default` value is `1`, no values will be changed unless a different multiplier value is supplied. This is useful for unit conversions (e.g., converting metric tons to grams by using `scale_by=1_000_000`).

`prefix_mode: str = ``"engineering"`  
The type of SI prefixes to use. Use `"engineering"` (the default) for prefixes that correspond to powers of 1000 only. Use `"decimal"` to include all SI prefixes (also those for powers of 10 and 100). See the *SI Prefix Modes* section for details.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ``","`  
The string to use as a separator between groups of digits. For example, using `sep_mark=","` with a value of `1000` would result in a formatted value of `"1,000"`. This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`dec_mark: str = ``"."`  
The string to be used as the decimal mark. For example, using `dec_mark=","` with the value `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign: bool = ``False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option. The default is `False`, where only negative numbers will display a minus sign.

`incl_space: bool = ``True`  
An option for whether to include a space between the numerical value and the SI prefix + unit (e.g., `True` for `"1.5 kW"`, `False` for `"1.5kW"`). Per SI convention, there should be a space between the value and the unit symbol. The default is `True`.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France). When provided, overrides `sep_mark` and `dec_mark` with locale-appropriate values.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Si Prefix Modes

The `prefix_mode=` argument controls which SI prefixes are used:

- `"engineering"`: Uses only prefixes for powers of 1000. This includes:

  - greater than 1: k (kilo), M (mega), G (giga), T (tera), P (peta), E (exa), Z (zetta), Y (yotta), R (ronna), Q (quetta)
  - less than 1: m (milli), µ (micro), n (nano), p (pico), f (femto), a (atto), z (zepto), y (yocto), r (ronto), q (quecto)
  - this is the most common convention in scientific and engineering contexts

- `"decimal"`: Uses all SI prefixes including those for powers of 10 and 100:

  - additional prefixes for greater-than-1 values: da (deca), h (hecto)
  - additional prefixes for less-than-1 values: d (deci), c (centi)
  - this mode is less commonly used but follows the complete SI standard


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). The use of a valid locale ID here means separator and decimal marks will be correct for the given locale. Should any values be provided in `sep_mark` or `dec_mark`, they will be overridden by the locale's preferred values.

Note that a `locale=` value provided here will override any global locale setting performed in <a href="../reference/GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale=` argument (it is settable there as a value received by all other methods that have a `locale=` argument).


## Examples

Create a table showing the masses of obelisks located in Rome. The masses are initially in metric tons, which we'll convert to grams using `scale_by=1_000_000`. The resulting values are then formatted with SI prefixes, which are all here as `M` (mega).


``` python
import polars as pl
from great_tables import GT

obelisks_df = pl.DataFrame(
    {
        "obelisk": [
            "Lateran Obelisk",
            "Vatican Obelisk",
            "Flaminio Obelisk",
            "Pantheon Obelisk",
        ],
        "mass_ton": [455, 331, 235, 30],
    }
)

(
    GT(obelisks_df)
    .fmt_number_si(
        columns="mass_ton",
        unit="g",
        decimals=0,
        scale_by=1_000_000,
    )
    .cols_label(obelisk="Obelisk", mass_ton="Mass")
)
```


<style>
#afqawzetqr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#afqawzetqr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#afqawzetqr p { margin: 0; padding: 0; }
 #afqawzetqr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #afqawzetqr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #afqawzetqr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #afqawzetqr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #afqawzetqr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #afqawzetqr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #afqawzetqr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #afqawzetqr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #afqawzetqr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #afqawzetqr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #afqawzetqr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #afqawzetqr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #afqawzetqr .gt_spanner_row { border-bottom-style: hidden; }
 #afqawzetqr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #afqawzetqr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #afqawzetqr .gt_from_md> :first-child { margin-top: 0; }
 #afqawzetqr .gt_from_md> :last-child { margin-bottom: 0; }
 #afqawzetqr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #afqawzetqr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #afqawzetqr .gt_indent_1 { text-indent: 5px; }
 #afqawzetqr .gt_indent_2 { text-indent: calc(5px * 2); }
 #afqawzetqr .gt_indent_3 { text-indent: calc(5px * 3); }
 #afqawzetqr .gt_indent_4 { text-indent: calc(5px * 4); }
 #afqawzetqr .gt_indent_5 { text-indent: calc(5px * 5); }
 #afqawzetqr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #afqawzetqr .gt_row_group_first td { border-top-width: 2px; }
 #afqawzetqr .gt_row_group_first th { border-top-width: 2px; }
 #afqawzetqr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #afqawzetqr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #afqawzetqr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #afqawzetqr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #afqawzetqr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #afqawzetqr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #afqawzetqr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #afqawzetqr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #afqawzetqr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #afqawzetqr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #afqawzetqr .gt_left { text-align: left; }
 #afqawzetqr .gt_center { text-align: center; }
 #afqawzetqr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #afqawzetqr .gt_font_normal { font-weight: normal; }
 #afqawzetqr .gt_font_bold { font-weight: bold; }
 #afqawzetqr .gt_font_italic { font-style: italic; }
 #afqawzetqr .gt_super { font-size: 65%; }
 #afqawzetqr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #afqawzetqr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #afqawzetqr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #afqawzetqr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #afqawzetqr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #afqawzetqr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Obelisk          | Mass   |
|------------------|--------|
| Lateran Obelisk  | 455 Mg |
| Vatican Obelisk  | 331 Mg |
| Flaminio Obelisk | 235 Mg |
| Pantheon Obelisk | 30 Mg  |


Create a table showing measurements of different substances. Each value is formatted with the appropriate SI prefix and unit.


``` python
substances_df = pl.DataFrame(
    {
        "substance": ["Glucose", "Vitamin C", "Caffeine"],
        "amount": [0.0051, 0.000075, 0.0002],
    }
)

(
    GT(substances_df)
    .fmt_number_si(columns="amount", unit="g", n_sigfig=2)
)
```


<style>
#qunhxxejhm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qunhxxejhm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qunhxxejhm p { margin: 0; padding: 0; }
 #qunhxxejhm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qunhxxejhm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qunhxxejhm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qunhxxejhm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qunhxxejhm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qunhxxejhm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qunhxxejhm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qunhxxejhm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qunhxxejhm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qunhxxejhm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qunhxxejhm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qunhxxejhm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qunhxxejhm .gt_spanner_row { border-bottom-style: hidden; }
 #qunhxxejhm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qunhxxejhm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qunhxxejhm .gt_from_md> :first-child { margin-top: 0; }
 #qunhxxejhm .gt_from_md> :last-child { margin-bottom: 0; }
 #qunhxxejhm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qunhxxejhm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qunhxxejhm .gt_indent_1 { text-indent: 5px; }
 #qunhxxejhm .gt_indent_2 { text-indent: calc(5px * 2); }
 #qunhxxejhm .gt_indent_3 { text-indent: calc(5px * 3); }
 #qunhxxejhm .gt_indent_4 { text-indent: calc(5px * 4); }
 #qunhxxejhm .gt_indent_5 { text-indent: calc(5px * 5); }
 #qunhxxejhm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qunhxxejhm .gt_row_group_first td { border-top-width: 2px; }
 #qunhxxejhm .gt_row_group_first th { border-top-width: 2px; }
 #qunhxxejhm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qunhxxejhm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qunhxxejhm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qunhxxejhm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qunhxxejhm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qunhxxejhm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qunhxxejhm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qunhxxejhm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qunhxxejhm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qunhxxejhm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qunhxxejhm .gt_left { text-align: left; }
 #qunhxxejhm .gt_center { text-align: center; }
 #qunhxxejhm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qunhxxejhm .gt_font_normal { font-weight: normal; }
 #qunhxxejhm .gt_font_bold { font-weight: bold; }
 #qunhxxejhm .gt_font_italic { font-style: italic; }
 #qunhxxejhm .gt_super { font-size: 65%; }
 #qunhxxejhm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qunhxxejhm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qunhxxejhm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qunhxxejhm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qunhxxejhm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qunhxxejhm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| substance | amount |
|-----------|--------|
| Glucose   | 5.1 mg |
| Vitamin C | 75 µg  |
| Caffeine  | 200 µg |


You can combine `fmt_number_si()` with [fmt_units()](GT.fmt_units.md#great_tables.GT.fmt_units) and [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge) to format measurements with SI prefixes on units that need special typesetting.


``` python
measurements_df = pl.DataFrame(
    {
        "measurement": ["Power", "Resistance", "Energy", "Fall Velocity"],
        "value": [1500.0, 2400000.0, 3600000.0, 0.033],
        "unit": ["W", "Ω", "J", "m/s"],
    }
)

(
    GT(measurements_df)
    .fmt_number_si(columns="value", decimals=1)
)
```


<style>
#xuvikpjbje table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xuvikpjbje thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xuvikpjbje p { margin: 0; padding: 0; }
 #xuvikpjbje .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xuvikpjbje .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xuvikpjbje .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xuvikpjbje .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xuvikpjbje .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xuvikpjbje .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xuvikpjbje .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xuvikpjbje .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xuvikpjbje .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xuvikpjbje .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xuvikpjbje .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xuvikpjbje .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xuvikpjbje .gt_spanner_row { border-bottom-style: hidden; }
 #xuvikpjbje .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xuvikpjbje .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xuvikpjbje .gt_from_md> :first-child { margin-top: 0; }
 #xuvikpjbje .gt_from_md> :last-child { margin-bottom: 0; }
 #xuvikpjbje .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xuvikpjbje .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xuvikpjbje .gt_indent_1 { text-indent: 5px; }
 #xuvikpjbje .gt_indent_2 { text-indent: calc(5px * 2); }
 #xuvikpjbje .gt_indent_3 { text-indent: calc(5px * 3); }
 #xuvikpjbje .gt_indent_4 { text-indent: calc(5px * 4); }
 #xuvikpjbje .gt_indent_5 { text-indent: calc(5px * 5); }
 #xuvikpjbje .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xuvikpjbje .gt_row_group_first td { border-top-width: 2px; }
 #xuvikpjbje .gt_row_group_first th { border-top-width: 2px; }
 #xuvikpjbje .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xuvikpjbje .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xuvikpjbje .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xuvikpjbje .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xuvikpjbje .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xuvikpjbje .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xuvikpjbje .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xuvikpjbje .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xuvikpjbje .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xuvikpjbje .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xuvikpjbje .gt_left { text-align: left; }
 #xuvikpjbje .gt_center { text-align: center; }
 #xuvikpjbje .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xuvikpjbje .gt_font_normal { font-weight: normal; }
 #xuvikpjbje .gt_font_bold { font-weight: bold; }
 #xuvikpjbje .gt_font_italic { font-style: italic; }
 #xuvikpjbje .gt_super { font-size: 65%; }
 #xuvikpjbje .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xuvikpjbje .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xuvikpjbje .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xuvikpjbje .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xuvikpjbje .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xuvikpjbje .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| measurement   | value  | unit |
|---------------|--------|------|
| Power         | 1.5 k  | W    |
| Resistance    | 2.4 M  | Ω    |
| Energy        | 3.6 M  | J    |
| Fall Velocity | 33.0 m | m/s  |


We can control the space between the number and prefix/unit with `incl_space`.


``` python
freqs_df = pl.DataFrame({"frequency": [2.4e9, 5.0e9, 900e6]})

(
    GT(freqs_df)
    .fmt_number_si(columns="frequency", unit="Hz", incl_space=False, decimals=1)
)
```


<style>
#zybnubcars table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zybnubcars thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zybnubcars p { margin: 0; padding: 0; }
 #zybnubcars .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zybnubcars .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zybnubcars .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zybnubcars .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zybnubcars .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zybnubcars .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zybnubcars .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zybnubcars .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zybnubcars .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zybnubcars .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zybnubcars .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zybnubcars .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zybnubcars .gt_spanner_row { border-bottom-style: hidden; }
 #zybnubcars .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zybnubcars .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zybnubcars .gt_from_md> :first-child { margin-top: 0; }
 #zybnubcars .gt_from_md> :last-child { margin-bottom: 0; }
 #zybnubcars .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zybnubcars .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zybnubcars .gt_indent_1 { text-indent: 5px; }
 #zybnubcars .gt_indent_2 { text-indent: calc(5px * 2); }
 #zybnubcars .gt_indent_3 { text-indent: calc(5px * 3); }
 #zybnubcars .gt_indent_4 { text-indent: calc(5px * 4); }
 #zybnubcars .gt_indent_5 { text-indent: calc(5px * 5); }
 #zybnubcars .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zybnubcars .gt_row_group_first td { border-top-width: 2px; }
 #zybnubcars .gt_row_group_first th { border-top-width: 2px; }
 #zybnubcars .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zybnubcars .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zybnubcars .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zybnubcars .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zybnubcars .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zybnubcars .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zybnubcars .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zybnubcars .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zybnubcars .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zybnubcars .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zybnubcars .gt_left { text-align: left; }
 #zybnubcars .gt_center { text-align: center; }
 #zybnubcars .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zybnubcars .gt_font_normal { font-weight: normal; }
 #zybnubcars .gt_font_bold { font-weight: bold; }
 #zybnubcars .gt_font_italic { font-style: italic; }
 #zybnubcars .gt_super { font-size: 65%; }
 #zybnubcars .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zybnubcars .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zybnubcars .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zybnubcars .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zybnubcars .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zybnubcars .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| frequency |
|-----------|
| 2.4GHz    |
| 5.0GHz    |
| 900.0MHz  |
