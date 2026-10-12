# GT.fmt_duration()


Format numeric or duration values as styled time duration strings.


Usage

``` python
GT.fmt_duration(
    columns=None,
    rows=None,
    input_units=None,
    output_units=None,
    duration_style="narrow",
    trim_zero_units=True,
    max_output_units=None,
    pattern="{x}",
    use_seps=True,
    sep_mark=",",
    force_sign=False,
    locale=None,
)
```


Format input values to time duration values whether those input values are numbers or of the `timedelta` class. We can specify which time units any numeric input values have (as weeks, days, hours, minutes, or seconds) and the output can be customized with a duration style (corresponding to narrow, wide, colon-separated, and ISO forms) and a choice of output units ranging from weeks to seconds.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`input_units: str | None = None`  
If one or more selected columns contains numeric values (not `timedelta` values, which contain the duration units), a keyword must be provided for `input_units` for the values to be interpreted in terms of duration. The accepted units are: `"seconds"`, `"minutes"`, `"hours"`, `"days"`, and `"weeks"`. This is required for numeric columns and ignored for `timedelta` columns.

`output_units: str | list[str] | None = None`  
Controls the output time units. The default (`None`) means that output units will be automatically chosen based on the input duration value. To control which time units are to be considered for output (before trimming with `trim_zero_units=`) we can specify a list of one or more of the following keywords: `"weeks"`, `"days"`, `"hours"`, `"minutes"`, or `"seconds"`.

`duration_style: DurationStyle = ``"narrow"`  
A choice of four formatting styles for the output duration values. With `"narrow"` (the default style), duration values will be formatted with single-letter time-part units (e.g., 1.35 days will be styled as `"1d 8h 24m"`). With `"wide"`, this example value will be expanded to `"1 day 8 hours 24 minutes"` after formatting. The `"colon-sep"` style will put days, hours, minutes, and seconds in the `"([D]/)[HH]:[MM]:[SS]"` format. The `"iso"` style will produce a value that conforms to the ISO 8601 rules for duration values (e.g., 1.35 days will become `"P1DT8H24M"`).

`trim_zero_units: bool | list[str] = ``True`  
Provides methods to remove output time units that have zero values. By default this is `True` and duration values that might otherwise be formatted as `"0w 1d 0h 4m 19s"` with `trim_zero_units=False` are instead displayed as `"1d 4m 19s"`. Aside from using `True`/`False` we could provide a list of keywords for more precise control. These keywords are: (1) `"leading"`, to omit all leading zero-value time units (e.g., `"0w 1d"` -\> `"1d"`), (2) `"trailing"`, to omit all trailing zero-value time units (e.g., `"3d 5h 0s"` -\> `"3d 5h"`), and (3) `"internal"`, which removes all internal zero-value time units (e.g., `"5d 0h 33m"` -\> `"5d 33m"`).

`max_output_units: int | None = None`  
If `output_units` is `None`, where the output time units are unspecified and left to be handled automatically, a numeric value provided for `max_output_units=` will be taken as the maximum number of time units to display in all output time duration values. By default, this is `None` and all possible time units will be displayed. This option has no effect when `duration_style="colon-sep"` (only `output_units` can be used to customize that type of duration output).

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`use_seps: bool = ``True`  
The `use_seps` option allows for the use of digit group separators. The type of digit group separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This setting is `True` by default.

`sep_mark: str = ``","`  
The string to use as a separator between groups of digits. For example, using `sep_mark=","` with a value of `1000` would result in a formatted value of `"1,000"`. This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign: bool = ``False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option. The default is `False`, where only negative numbers will display a minus sign.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Output Units For The Colon-Separated Duration Style

The colon-separated duration style (enabled when `duration_style="colon-sep"`) is essentially a clock-based output format which uses the display logic of chronograph watch functionality. It will, by default, display duration values in the `(D/)HH:MM:SS` format. Any duration values greater than or equal to 24 hours will have the number of days prepended with an adjoining slash mark. While this output format is versatile, it can be changed somewhat with the `output_units=` option. The following combinations of output units are permitted:

- `["minutes", "seconds"]` -\> `MM:SS`
- `["hours", "minutes"]` -\> `HH:MM`
- `["hours", "minutes", "seconds"]` -\> `HH:MM:SS`
- `["days", "hours", "minutes"]` -\> `(D/)HH:MM`

Any other specialized combinations will result in the default set being used, which is `["days", "hours", "minutes", "seconds"]`.


## Compatibility Of Formatting Function With Data Values

`fmt_duration()` is compatible with body cells that are of `int`, `float`, or `datetime.timedelta` types. Any other types of body cells are ignored during formatting.


## Examples

Let's create a table with duration values in seconds and format them using the default narrow style. This produces compact output with single-letter unit abbreviations, ideal for space-constrained displays.


``` python
import pandas as pd
from great_tables import GT

df = pd.DataFrame({"duration_s": [3661, 86400, 172800, 60, 0]})

(
    GT(df)
    .fmt_duration(columns="duration_s", input_units="seconds")
)
```


<style>
#hrpbpezfxm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hrpbpezfxm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hrpbpezfxm p { margin: 0; padding: 0; }
 #hrpbpezfxm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hrpbpezfxm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hrpbpezfxm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hrpbpezfxm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hrpbpezfxm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hrpbpezfxm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hrpbpezfxm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hrpbpezfxm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hrpbpezfxm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hrpbpezfxm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hrpbpezfxm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hrpbpezfxm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hrpbpezfxm .gt_spanner_row { border-bottom-style: hidden; }
 #hrpbpezfxm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hrpbpezfxm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hrpbpezfxm .gt_from_md> :first-child { margin-top: 0; }
 #hrpbpezfxm .gt_from_md> :last-child { margin-bottom: 0; }
 #hrpbpezfxm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hrpbpezfxm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hrpbpezfxm .gt_indent_1 { text-indent: 5px; }
 #hrpbpezfxm .gt_indent_2 { text-indent: calc(5px * 2); }
 #hrpbpezfxm .gt_indent_3 { text-indent: calc(5px * 3); }
 #hrpbpezfxm .gt_indent_4 { text-indent: calc(5px * 4); }
 #hrpbpezfxm .gt_indent_5 { text-indent: calc(5px * 5); }
 #hrpbpezfxm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hrpbpezfxm .gt_row_group_first td { border-top-width: 2px; }
 #hrpbpezfxm .gt_row_group_first th { border-top-width: 2px; }
 #hrpbpezfxm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hrpbpezfxm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hrpbpezfxm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hrpbpezfxm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hrpbpezfxm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hrpbpezfxm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hrpbpezfxm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hrpbpezfxm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hrpbpezfxm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hrpbpezfxm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hrpbpezfxm .gt_left { text-align: left; }
 #hrpbpezfxm .gt_center { text-align: center; }
 #hrpbpezfxm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hrpbpezfxm .gt_font_normal { font-weight: normal; }
 #hrpbpezfxm .gt_font_bold { font-weight: bold; }
 #hrpbpezfxm .gt_font_italic { font-style: italic; }
 #hrpbpezfxm .gt_super { font-size: 65%; }
 #hrpbpezfxm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hrpbpezfxm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hrpbpezfxm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hrpbpezfxm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hrpbpezfxm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hrpbpezfxm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| duration_s |
|------------|
| 1h 1m 1s   |
| 1d         |
| 2d         |
| 1m         |
| 0s         |


Notice that zero-valued time units are automatically trimmed from the output, keeping the display clean. A value of `86400` seconds (exactly 1 day) simply shows `"1d"` rather than `"0w 1d 0h 0m 0s"`.

For reporting contexts where readability is more important than compactness, the wide style spells out the full unit names with proper singular/plural forms.


``` python
df = pd.DataFrame({"hours": [1.5, 24.0, 0.5, 100.75]})

(
    GT(df)
    .fmt_duration(columns="hours", input_units="hours", duration_style="wide")
)
```


<style>
#dnnmujanye table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dnnmujanye thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dnnmujanye p { margin: 0; padding: 0; }
 #dnnmujanye .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dnnmujanye .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dnnmujanye .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dnnmujanye .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dnnmujanye .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dnnmujanye .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnnmujanye .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dnnmujanye .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dnnmujanye .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dnnmujanye .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dnnmujanye .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dnnmujanye .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dnnmujanye .gt_spanner_row { border-bottom-style: hidden; }
 #dnnmujanye .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dnnmujanye .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dnnmujanye .gt_from_md> :first-child { margin-top: 0; }
 #dnnmujanye .gt_from_md> :last-child { margin-bottom: 0; }
 #dnnmujanye .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dnnmujanye .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dnnmujanye .gt_indent_1 { text-indent: 5px; }
 #dnnmujanye .gt_indent_2 { text-indent: calc(5px * 2); }
 #dnnmujanye .gt_indent_3 { text-indent: calc(5px * 3); }
 #dnnmujanye .gt_indent_4 { text-indent: calc(5px * 4); }
 #dnnmujanye .gt_indent_5 { text-indent: calc(5px * 5); }
 #dnnmujanye .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dnnmujanye .gt_row_group_first td { border-top-width: 2px; }
 #dnnmujanye .gt_row_group_first th { border-top-width: 2px; }
 #dnnmujanye .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dnnmujanye .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnnmujanye .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dnnmujanye .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dnnmujanye .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnnmujanye .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dnnmujanye .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dnnmujanye .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dnnmujanye .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnnmujanye .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dnnmujanye .gt_left { text-align: left; }
 #dnnmujanye .gt_center { text-align: center; }
 #dnnmujanye .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dnnmujanye .gt_font_normal { font-weight: normal; }
 #dnnmujanye .gt_font_bold { font-weight: bold; }
 #dnnmujanye .gt_font_italic { font-style: italic; }
 #dnnmujanye .gt_super { font-size: 65%; }
 #dnnmujanye .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnnmujanye .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dnnmujanye .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnnmujanye .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dnnmujanye .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dnnmujanye .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| hours                     |
|---------------------------|
| 1 hour 30 minutes         |
| 1 day                     |
| 30 minutes                |
| 4 days 4 hours 45 minutes |


The colon-separated style is useful for timing data, race results, or any context where a clock-like display is expected. Days are shown with a slash prefix when the duration is 24 hours or more.


``` python
df = pd.DataFrame({
    "event": ["Marathon", "Half Marathon", "10K", "Mile"],
    "winning_time_s": [7377, 3542, 1620, 233],
})

(
    GT(df)
    .fmt_duration(
        columns="winning_time_s",
        input_units="seconds",
        duration_style="colon-sep",
        output_units=["hours", "minutes", "seconds"],
    )
)
```


<style>
#azgojvyfqa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#azgojvyfqa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#azgojvyfqa p { margin: 0; padding: 0; }
 #azgojvyfqa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #azgojvyfqa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #azgojvyfqa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #azgojvyfqa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #azgojvyfqa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #azgojvyfqa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #azgojvyfqa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #azgojvyfqa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #azgojvyfqa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #azgojvyfqa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #azgojvyfqa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #azgojvyfqa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #azgojvyfqa .gt_spanner_row { border-bottom-style: hidden; }
 #azgojvyfqa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #azgojvyfqa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #azgojvyfqa .gt_from_md> :first-child { margin-top: 0; }
 #azgojvyfqa .gt_from_md> :last-child { margin-bottom: 0; }
 #azgojvyfqa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #azgojvyfqa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #azgojvyfqa .gt_indent_1 { text-indent: 5px; }
 #azgojvyfqa .gt_indent_2 { text-indent: calc(5px * 2); }
 #azgojvyfqa .gt_indent_3 { text-indent: calc(5px * 3); }
 #azgojvyfqa .gt_indent_4 { text-indent: calc(5px * 4); }
 #azgojvyfqa .gt_indent_5 { text-indent: calc(5px * 5); }
 #azgojvyfqa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #azgojvyfqa .gt_row_group_first td { border-top-width: 2px; }
 #azgojvyfqa .gt_row_group_first th { border-top-width: 2px; }
 #azgojvyfqa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #azgojvyfqa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #azgojvyfqa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #azgojvyfqa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #azgojvyfqa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #azgojvyfqa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #azgojvyfqa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #azgojvyfqa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #azgojvyfqa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #azgojvyfqa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #azgojvyfqa .gt_left { text-align: left; }
 #azgojvyfqa .gt_center { text-align: center; }
 #azgojvyfqa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #azgojvyfqa .gt_font_normal { font-weight: normal; }
 #azgojvyfqa .gt_font_bold { font-weight: bold; }
 #azgojvyfqa .gt_font_italic { font-style: italic; }
 #azgojvyfqa .gt_super { font-size: 65%; }
 #azgojvyfqa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #azgojvyfqa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #azgojvyfqa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #azgojvyfqa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #azgojvyfqa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #azgojvyfqa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| event         | winning_time_s |
|---------------|----------------|
| Marathon      | 02:02:57       |
| Half Marathon | 00:59:02       |
| 10K           | 00:27:00       |
| Mile          | 00:03:53       |


The output is zero-padded in the familiar `HH:MM:SS` format. By specifying `output_units` we control exactly which components appear in the colon-separated output.

When working with `timedelta` columns (common in Pandas when computing differences between timestamps), `fmt_duration()` automatically detects the units--no `input_units` argument is needed.


``` python
from datetime import datetime

events = pd.DataFrame({
    "task": ["Build", "Test suite", "Deploy", "Full pipeline"],
    "elapsed": [
        datetime(2024, 1, 1, 0, 12, 45) - datetime(2024, 1, 1, 0, 0, 0),
        datetime(2024, 1, 1, 1, 5, 30) - datetime(2024, 1, 1, 0, 0, 0),
        datetime(2024, 1, 1, 0, 3, 15) - datetime(2024, 1, 1, 0, 0, 0),
        datetime(2024, 1, 1, 1, 21, 30) - datetime(2024, 1, 1, 0, 0, 0),
    ],
})

(
    GT(events, rowname_col="task")
    .fmt_duration(columns="elapsed", duration_style="narrow")
)
```


<style>
#irreugwfdr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#irreugwfdr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#irreugwfdr p { margin: 0; padding: 0; }
 #irreugwfdr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #irreugwfdr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #irreugwfdr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #irreugwfdr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #irreugwfdr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #irreugwfdr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #irreugwfdr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #irreugwfdr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #irreugwfdr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #irreugwfdr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #irreugwfdr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #irreugwfdr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #irreugwfdr .gt_spanner_row { border-bottom-style: hidden; }
 #irreugwfdr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #irreugwfdr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #irreugwfdr .gt_from_md> :first-child { margin-top: 0; }
 #irreugwfdr .gt_from_md> :last-child { margin-bottom: 0; }
 #irreugwfdr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #irreugwfdr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #irreugwfdr .gt_indent_1 { text-indent: 5px; }
 #irreugwfdr .gt_indent_2 { text-indent: calc(5px * 2); }
 #irreugwfdr .gt_indent_3 { text-indent: calc(5px * 3); }
 #irreugwfdr .gt_indent_4 { text-indent: calc(5px * 4); }
 #irreugwfdr .gt_indent_5 { text-indent: calc(5px * 5); }
 #irreugwfdr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #irreugwfdr .gt_row_group_first td { border-top-width: 2px; }
 #irreugwfdr .gt_row_group_first th { border-top-width: 2px; }
 #irreugwfdr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #irreugwfdr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #irreugwfdr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #irreugwfdr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #irreugwfdr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #irreugwfdr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #irreugwfdr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #irreugwfdr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #irreugwfdr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #irreugwfdr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #irreugwfdr .gt_left { text-align: left; }
 #irreugwfdr .gt_center { text-align: center; }
 #irreugwfdr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #irreugwfdr .gt_font_normal { font-weight: normal; }
 #irreugwfdr .gt_font_bold { font-weight: bold; }
 #irreugwfdr .gt_font_italic { font-style: italic; }
 #irreugwfdr .gt_super { font-size: 65%; }
 #irreugwfdr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #irreugwfdr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #irreugwfdr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #irreugwfdr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #irreugwfdr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #irreugwfdr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|               | elapsed    |
|---------------|------------|
| Build         | 12m 45s    |
| Test suite    | 1h 5m 30s  |
| Deploy        | 3m 15s     |
| Full pipeline | 1h 21m 30s |


Polars DataFrames work the same way. Here we format numeric duration values using the ISO 8601 duration style, which is useful for machine-readable output or standards-compliant reporting.


``` python
import polars as pl
from great_tables import GT

df = pl.DataFrame({"activity": ["Flight", "Layover", "Drive"], "seconds": [14400, 5400, 1830]})

(
    GT(df)
    .fmt_duration(columns="seconds", input_units="seconds", duration_style="iso")
)
```


<style>
#jetyckqcfp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jetyckqcfp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jetyckqcfp p { margin: 0; padding: 0; }
 #jetyckqcfp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jetyckqcfp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jetyckqcfp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jetyckqcfp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jetyckqcfp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jetyckqcfp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jetyckqcfp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jetyckqcfp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jetyckqcfp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jetyckqcfp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jetyckqcfp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jetyckqcfp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jetyckqcfp .gt_spanner_row { border-bottom-style: hidden; }
 #jetyckqcfp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jetyckqcfp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jetyckqcfp .gt_from_md> :first-child { margin-top: 0; }
 #jetyckqcfp .gt_from_md> :last-child { margin-bottom: 0; }
 #jetyckqcfp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jetyckqcfp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jetyckqcfp .gt_indent_1 { text-indent: 5px; }
 #jetyckqcfp .gt_indent_2 { text-indent: calc(5px * 2); }
 #jetyckqcfp .gt_indent_3 { text-indent: calc(5px * 3); }
 #jetyckqcfp .gt_indent_4 { text-indent: calc(5px * 4); }
 #jetyckqcfp .gt_indent_5 { text-indent: calc(5px * 5); }
 #jetyckqcfp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jetyckqcfp .gt_row_group_first td { border-top-width: 2px; }
 #jetyckqcfp .gt_row_group_first th { border-top-width: 2px; }
 #jetyckqcfp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jetyckqcfp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jetyckqcfp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jetyckqcfp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jetyckqcfp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jetyckqcfp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jetyckqcfp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jetyckqcfp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jetyckqcfp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jetyckqcfp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jetyckqcfp .gt_left { text-align: left; }
 #jetyckqcfp .gt_center { text-align: center; }
 #jetyckqcfp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jetyckqcfp .gt_font_normal { font-weight: normal; }
 #jetyckqcfp .gt_font_bold { font-weight: bold; }
 #jetyckqcfp .gt_font_italic { font-style: italic; }
 #jetyckqcfp .gt_super { font-size: 65%; }
 #jetyckqcfp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jetyckqcfp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jetyckqcfp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jetyckqcfp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jetyckqcfp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jetyckqcfp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| activity | seconds  |
|----------|----------|
| Flight   | PT4H     |
| Layover  | PT1H30M  |
| Drive    | PT30M30S |


Polars also has native `Duration` dtype columns (created via temporal arithmetic or `timedelta` values). These are handled automatically without needing to specify `input_units`.


``` python
from datetime import timedelta

df = pl.DataFrame({
    "segment": ["Warm-up", "Main set", "Cool-down"],
    "duration": [timedelta(minutes=10), timedelta(minutes=45, seconds=30), timedelta(minutes=5)],
})

(
    GT(df)
    .fmt_duration(columns="duration", duration_style="wide")
)
```


<style>
#qballadzah table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qballadzah thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qballadzah p { margin: 0; padding: 0; }
 #qballadzah .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qballadzah .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qballadzah .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qballadzah .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qballadzah .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qballadzah .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qballadzah .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qballadzah .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qballadzah .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qballadzah .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qballadzah .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qballadzah .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qballadzah .gt_spanner_row { border-bottom-style: hidden; }
 #qballadzah .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qballadzah .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qballadzah .gt_from_md> :first-child { margin-top: 0; }
 #qballadzah .gt_from_md> :last-child { margin-bottom: 0; }
 #qballadzah .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qballadzah .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qballadzah .gt_indent_1 { text-indent: 5px; }
 #qballadzah .gt_indent_2 { text-indent: calc(5px * 2); }
 #qballadzah .gt_indent_3 { text-indent: calc(5px * 3); }
 #qballadzah .gt_indent_4 { text-indent: calc(5px * 4); }
 #qballadzah .gt_indent_5 { text-indent: calc(5px * 5); }
 #qballadzah .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qballadzah .gt_row_group_first td { border-top-width: 2px; }
 #qballadzah .gt_row_group_first th { border-top-width: 2px; }
 #qballadzah .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qballadzah .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qballadzah .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qballadzah .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qballadzah .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qballadzah .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qballadzah .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qballadzah .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qballadzah .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qballadzah .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qballadzah .gt_left { text-align: left; }
 #qballadzah .gt_center { text-align: center; }
 #qballadzah .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qballadzah .gt_font_normal { font-weight: normal; }
 #qballadzah .gt_font_bold { font-weight: bold; }
 #qballadzah .gt_font_italic { font-style: italic; }
 #qballadzah .gt_super { font-size: 65%; }
 #qballadzah .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qballadzah .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qballadzah .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qballadzah .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qballadzah .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qballadzah .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| segment   | duration              |
|-----------|-----------------------|
| Warm-up   | 10 minutes            |
| Main set  | 45 minutes 30 seconds |
| Cool-down | 5 minutes             |
