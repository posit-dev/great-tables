## GT.fmt_integer()


Format values as integers.


Usage

``` python
GT.fmt_integer(
    columns=None,
    rows=None,
    use_seps=True,
    scale_by=1,
    accounting=False,
    compact=False,
    pattern="{x}",
    sep_mark=",",
    force_sign=False,
    locale=None
)
```


With numeric values in one or more table columns, we can perform number-based formatting so that the targeted values are always rendered as integer values.

We can have fine control over integer formatting with the following options:

- digit grouping separators: options to enable/disable digit separators and provide a choice of separator symbol
- scaling: we can choose to scale targeted values by a multiplier value
- large-number suffixing: larger figures (thousands, millions, etc.) can be autoscaled and decorated with the appropriate suffixes
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: providing a locale ID will result in number formatting specific to the chosen locale


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`use_seps: bool = ``True`  
The `use_seps` option allows for the use of digit group separators. The type of digit group separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This setting is `True` by default.

`scale_by: float = ``1`  
All numeric values will be multiplied by the `scale_by` value before undergoing formatting. Since the `default` value is `1`, no values will be changed unless a different multiplier value is supplied.

`accounting: bool = ``False`  
Whether to use accounting style, which wraps negative numbers in parentheses instead of using a minus sign.

`compact: bool = ``False`  
A boolean value that allows for compact formatting of numeric values. Values will be scaled and decorated with the appropriate suffixes (e.g., `1230` becomes `1K`, and `1230000` becomes `1M`). The `compact` option is `False` by default.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ``","`  
The string to use as a separator between groups of digits. For example, using `sep_mark=","` with a value of `1000` would result in a formatted value of `"1,000"`. This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign: bool = ``False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option. The default is `False`, where only negative numbers will display a minus sign.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). The use of a valid locale ID here means separator marks will be correct for the given locale. Should any value be provided in `sep_mark`, it will be overridden by the locale's preferred value.

Note that a `locale` value provided here will override any global locale setting performed in <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

For this example, we'll use the [exibble](data.exibble.md#great_tables.data.exibble) dataset as the input table. With the [fmt_integer()](GT.fmt_integer.md#great_tables.GT.fmt_integer) method, we'll format the `num` column as integer values having no digit separators (with the `use_seps=False` option).


``` python
from great_tables import GT, exibble

(
    GT(exibble)
    .fmt_integer(columns="num", use_seps=False)
)
```


<style>
#xwobttjwhl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xwobttjwhl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xwobttjwhl p { margin: 0; padding: 0; }
 #xwobttjwhl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xwobttjwhl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xwobttjwhl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xwobttjwhl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xwobttjwhl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xwobttjwhl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xwobttjwhl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xwobttjwhl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xwobttjwhl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xwobttjwhl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xwobttjwhl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xwobttjwhl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xwobttjwhl .gt_spanner_row { border-bottom-style: hidden; }
 #xwobttjwhl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xwobttjwhl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xwobttjwhl .gt_from_md> :first-child { margin-top: 0; }
 #xwobttjwhl .gt_from_md> :last-child { margin-bottom: 0; }
 #xwobttjwhl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xwobttjwhl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xwobttjwhl .gt_indent_1 { text-indent: 5px; }
 #xwobttjwhl .gt_indent_2 { text-indent: calc(5px * 2); }
 #xwobttjwhl .gt_indent_3 { text-indent: calc(5px * 3); }
 #xwobttjwhl .gt_indent_4 { text-indent: calc(5px * 4); }
 #xwobttjwhl .gt_indent_5 { text-indent: calc(5px * 5); }
 #xwobttjwhl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xwobttjwhl .gt_row_group_first td { border-top-width: 2px; }
 #xwobttjwhl .gt_row_group_first th { border-top-width: 2px; }
 #xwobttjwhl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xwobttjwhl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xwobttjwhl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xwobttjwhl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xwobttjwhl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xwobttjwhl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xwobttjwhl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xwobttjwhl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xwobttjwhl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xwobttjwhl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xwobttjwhl .gt_left { text-align: left; }
 #xwobttjwhl .gt_center { text-align: center; }
 #xwobttjwhl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xwobttjwhl .gt_font_normal { font-weight: normal; }
 #xwobttjwhl .gt_font_bold { font-weight: bold; }
 #xwobttjwhl .gt_font_italic { font-style: italic; }
 #xwobttjwhl .gt_super { font-size: 65%; }
 #xwobttjwhl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xwobttjwhl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xwobttjwhl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xwobttjwhl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xwobttjwhl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xwobttjwhl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num     | char       | fctr  | date       | time  | datetime         | currency | row   | group |
|---------|------------|-------|------------|-------|------------------|----------|-------|-------|
| 0       | apricot    | one   | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95    | row_1 | grp_a |
| 2       | banana     | two   | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95    | row_2 | grp_a |
| 33      | coconut    | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39     | row_3 | grp_a |
| 444     | durian     | four  | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0  | row_4 | grp_a |
| 5550    |            | five  | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81  | row_5 | grp_b |
|         | fig        | six   | 2015-06-15 |       | 2018-06-06 16:11 | 13.255   | row_6 | grp_b |
| 777000  | grapefruit | seven |            | 19:10 | 2018-07-07 05:22 |          | row_7 | grp_b |
| 8880000 | honeydew   | eight | 2015-08-15 | 20:20 |                  | 0.44     | row_8 | grp_b |
