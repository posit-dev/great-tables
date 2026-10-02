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

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

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
#rkayfzqoaj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rkayfzqoaj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rkayfzqoaj p { margin: 0; padding: 0; }
 #rkayfzqoaj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rkayfzqoaj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rkayfzqoaj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rkayfzqoaj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rkayfzqoaj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rkayfzqoaj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rkayfzqoaj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rkayfzqoaj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rkayfzqoaj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rkayfzqoaj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rkayfzqoaj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rkayfzqoaj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rkayfzqoaj .gt_spanner_row { border-bottom-style: hidden; }
 #rkayfzqoaj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rkayfzqoaj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rkayfzqoaj .gt_from_md> :first-child { margin-top: 0; }
 #rkayfzqoaj .gt_from_md> :last-child { margin-bottom: 0; }
 #rkayfzqoaj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rkayfzqoaj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rkayfzqoaj .gt_indent_1 { text-indent: 5px; }
 #rkayfzqoaj .gt_indent_2 { text-indent: calc(5px * 2); }
 #rkayfzqoaj .gt_indent_3 { text-indent: calc(5px * 3); }
 #rkayfzqoaj .gt_indent_4 { text-indent: calc(5px * 4); }
 #rkayfzqoaj .gt_indent_5 { text-indent: calc(5px * 5); }
 #rkayfzqoaj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rkayfzqoaj .gt_row_group_first td { border-top-width: 2px; }
 #rkayfzqoaj .gt_row_group_first th { border-top-width: 2px; }
 #rkayfzqoaj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rkayfzqoaj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rkayfzqoaj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rkayfzqoaj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rkayfzqoaj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rkayfzqoaj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rkayfzqoaj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rkayfzqoaj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rkayfzqoaj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rkayfzqoaj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rkayfzqoaj .gt_left { text-align: left; }
 #rkayfzqoaj .gt_center { text-align: center; }
 #rkayfzqoaj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rkayfzqoaj .gt_font_normal { font-weight: normal; }
 #rkayfzqoaj .gt_font_bold { font-weight: bold; }
 #rkayfzqoaj .gt_font_italic { font-style: italic; }
 #rkayfzqoaj .gt_super { font-size: 65%; }
 #rkayfzqoaj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rkayfzqoaj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rkayfzqoaj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rkayfzqoaj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rkayfzqoaj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rkayfzqoaj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ikgcrxisrb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ikgcrxisrb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ikgcrxisrb p { margin: 0; padding: 0; }
 #ikgcrxisrb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ikgcrxisrb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ikgcrxisrb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ikgcrxisrb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ikgcrxisrb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ikgcrxisrb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ikgcrxisrb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ikgcrxisrb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ikgcrxisrb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ikgcrxisrb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ikgcrxisrb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ikgcrxisrb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ikgcrxisrb .gt_spanner_row { border-bottom-style: hidden; }
 #ikgcrxisrb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ikgcrxisrb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ikgcrxisrb .gt_from_md> :first-child { margin-top: 0; }
 #ikgcrxisrb .gt_from_md> :last-child { margin-bottom: 0; }
 #ikgcrxisrb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ikgcrxisrb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ikgcrxisrb .gt_indent_1 { text-indent: 5px; }
 #ikgcrxisrb .gt_indent_2 { text-indent: calc(5px * 2); }
 #ikgcrxisrb .gt_indent_3 { text-indent: calc(5px * 3); }
 #ikgcrxisrb .gt_indent_4 { text-indent: calc(5px * 4); }
 #ikgcrxisrb .gt_indent_5 { text-indent: calc(5px * 5); }
 #ikgcrxisrb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ikgcrxisrb .gt_row_group_first td { border-top-width: 2px; }
 #ikgcrxisrb .gt_row_group_first th { border-top-width: 2px; }
 #ikgcrxisrb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ikgcrxisrb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ikgcrxisrb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ikgcrxisrb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ikgcrxisrb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ikgcrxisrb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ikgcrxisrb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ikgcrxisrb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ikgcrxisrb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ikgcrxisrb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ikgcrxisrb .gt_left { text-align: left; }
 #ikgcrxisrb .gt_center { text-align: center; }
 #ikgcrxisrb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ikgcrxisrb .gt_font_normal { font-weight: normal; }
 #ikgcrxisrb .gt_font_bold { font-weight: bold; }
 #ikgcrxisrb .gt_font_italic { font-style: italic; }
 #ikgcrxisrb .gt_super { font-size: 65%; }
 #ikgcrxisrb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ikgcrxisrb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ikgcrxisrb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ikgcrxisrb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ikgcrxisrb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ikgcrxisrb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lljothwbqs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lljothwbqs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lljothwbqs p { margin: 0; padding: 0; }
 #lljothwbqs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lljothwbqs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lljothwbqs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lljothwbqs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lljothwbqs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lljothwbqs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lljothwbqs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lljothwbqs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lljothwbqs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lljothwbqs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lljothwbqs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lljothwbqs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lljothwbqs .gt_spanner_row { border-bottom-style: hidden; }
 #lljothwbqs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lljothwbqs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lljothwbqs .gt_from_md> :first-child { margin-top: 0; }
 #lljothwbqs .gt_from_md> :last-child { margin-bottom: 0; }
 #lljothwbqs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lljothwbqs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lljothwbqs .gt_indent_1 { text-indent: 5px; }
 #lljothwbqs .gt_indent_2 { text-indent: calc(5px * 2); }
 #lljothwbqs .gt_indent_3 { text-indent: calc(5px * 3); }
 #lljothwbqs .gt_indent_4 { text-indent: calc(5px * 4); }
 #lljothwbqs .gt_indent_5 { text-indent: calc(5px * 5); }
 #lljothwbqs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lljothwbqs .gt_row_group_first td { border-top-width: 2px; }
 #lljothwbqs .gt_row_group_first th { border-top-width: 2px; }
 #lljothwbqs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lljothwbqs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lljothwbqs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lljothwbqs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lljothwbqs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lljothwbqs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lljothwbqs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lljothwbqs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lljothwbqs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lljothwbqs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lljothwbqs .gt_left { text-align: left; }
 #lljothwbqs .gt_center { text-align: center; }
 #lljothwbqs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lljothwbqs .gt_font_normal { font-weight: normal; }
 #lljothwbqs .gt_font_bold { font-weight: bold; }
 #lljothwbqs .gt_font_italic { font-style: italic; }
 #lljothwbqs .gt_super { font-size: 65%; }
 #lljothwbqs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lljothwbqs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lljothwbqs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lljothwbqs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lljothwbqs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lljothwbqs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gzoxemnrlr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gzoxemnrlr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gzoxemnrlr p { margin: 0; padding: 0; }
 #gzoxemnrlr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gzoxemnrlr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gzoxemnrlr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gzoxemnrlr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gzoxemnrlr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gzoxemnrlr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gzoxemnrlr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gzoxemnrlr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gzoxemnrlr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gzoxemnrlr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gzoxemnrlr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gzoxemnrlr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gzoxemnrlr .gt_spanner_row { border-bottom-style: hidden; }
 #gzoxemnrlr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gzoxemnrlr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gzoxemnrlr .gt_from_md> :first-child { margin-top: 0; }
 #gzoxemnrlr .gt_from_md> :last-child { margin-bottom: 0; }
 #gzoxemnrlr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gzoxemnrlr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gzoxemnrlr .gt_indent_1 { text-indent: 5px; }
 #gzoxemnrlr .gt_indent_2 { text-indent: calc(5px * 2); }
 #gzoxemnrlr .gt_indent_3 { text-indent: calc(5px * 3); }
 #gzoxemnrlr .gt_indent_4 { text-indent: calc(5px * 4); }
 #gzoxemnrlr .gt_indent_5 { text-indent: calc(5px * 5); }
 #gzoxemnrlr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gzoxemnrlr .gt_row_group_first td { border-top-width: 2px; }
 #gzoxemnrlr .gt_row_group_first th { border-top-width: 2px; }
 #gzoxemnrlr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gzoxemnrlr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gzoxemnrlr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gzoxemnrlr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gzoxemnrlr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gzoxemnrlr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gzoxemnrlr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gzoxemnrlr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gzoxemnrlr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gzoxemnrlr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gzoxemnrlr .gt_left { text-align: left; }
 #gzoxemnrlr .gt_center { text-align: center; }
 #gzoxemnrlr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gzoxemnrlr .gt_font_normal { font-weight: normal; }
 #gzoxemnrlr .gt_font_bold { font-weight: bold; }
 #gzoxemnrlr .gt_font_italic { font-style: italic; }
 #gzoxemnrlr .gt_super { font-size: 65%; }
 #gzoxemnrlr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gzoxemnrlr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gzoxemnrlr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gzoxemnrlr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gzoxemnrlr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gzoxemnrlr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ixcclkjnwj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ixcclkjnwj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ixcclkjnwj p { margin: 0; padding: 0; }
 #ixcclkjnwj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ixcclkjnwj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ixcclkjnwj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ixcclkjnwj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ixcclkjnwj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ixcclkjnwj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixcclkjnwj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ixcclkjnwj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ixcclkjnwj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ixcclkjnwj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ixcclkjnwj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ixcclkjnwj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ixcclkjnwj .gt_spanner_row { border-bottom-style: hidden; }
 #ixcclkjnwj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ixcclkjnwj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ixcclkjnwj .gt_from_md> :first-child { margin-top: 0; }
 #ixcclkjnwj .gt_from_md> :last-child { margin-bottom: 0; }
 #ixcclkjnwj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ixcclkjnwj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ixcclkjnwj .gt_indent_1 { text-indent: 5px; }
 #ixcclkjnwj .gt_indent_2 { text-indent: calc(5px * 2); }
 #ixcclkjnwj .gt_indent_3 { text-indent: calc(5px * 3); }
 #ixcclkjnwj .gt_indent_4 { text-indent: calc(5px * 4); }
 #ixcclkjnwj .gt_indent_5 { text-indent: calc(5px * 5); }
 #ixcclkjnwj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ixcclkjnwj .gt_row_group_first td { border-top-width: 2px; }
 #ixcclkjnwj .gt_row_group_first th { border-top-width: 2px; }
 #ixcclkjnwj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ixcclkjnwj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixcclkjnwj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ixcclkjnwj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ixcclkjnwj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixcclkjnwj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ixcclkjnwj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ixcclkjnwj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ixcclkjnwj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixcclkjnwj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ixcclkjnwj .gt_left { text-align: left; }
 #ixcclkjnwj .gt_center { text-align: center; }
 #ixcclkjnwj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ixcclkjnwj .gt_font_normal { font-weight: normal; }
 #ixcclkjnwj .gt_font_bold { font-weight: bold; }
 #ixcclkjnwj .gt_font_italic { font-style: italic; }
 #ixcclkjnwj .gt_super { font-size: 65%; }
 #ixcclkjnwj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixcclkjnwj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ixcclkjnwj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixcclkjnwj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ixcclkjnwj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ixcclkjnwj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| activity | seconds |
|----------|---------|
| Flight   | P4H     |
| Layover  | P1H30M  |
| Drive    | P30M30S |


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
#zwdtsrzbwc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zwdtsrzbwc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zwdtsrzbwc p { margin: 0; padding: 0; }
 #zwdtsrzbwc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zwdtsrzbwc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zwdtsrzbwc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zwdtsrzbwc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zwdtsrzbwc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zwdtsrzbwc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zwdtsrzbwc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zwdtsrzbwc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zwdtsrzbwc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zwdtsrzbwc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zwdtsrzbwc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zwdtsrzbwc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zwdtsrzbwc .gt_spanner_row { border-bottom-style: hidden; }
 #zwdtsrzbwc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zwdtsrzbwc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zwdtsrzbwc .gt_from_md> :first-child { margin-top: 0; }
 #zwdtsrzbwc .gt_from_md> :last-child { margin-bottom: 0; }
 #zwdtsrzbwc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zwdtsrzbwc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zwdtsrzbwc .gt_indent_1 { text-indent: 5px; }
 #zwdtsrzbwc .gt_indent_2 { text-indent: calc(5px * 2); }
 #zwdtsrzbwc .gt_indent_3 { text-indent: calc(5px * 3); }
 #zwdtsrzbwc .gt_indent_4 { text-indent: calc(5px * 4); }
 #zwdtsrzbwc .gt_indent_5 { text-indent: calc(5px * 5); }
 #zwdtsrzbwc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zwdtsrzbwc .gt_row_group_first td { border-top-width: 2px; }
 #zwdtsrzbwc .gt_row_group_first th { border-top-width: 2px; }
 #zwdtsrzbwc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zwdtsrzbwc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zwdtsrzbwc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zwdtsrzbwc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zwdtsrzbwc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zwdtsrzbwc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zwdtsrzbwc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zwdtsrzbwc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zwdtsrzbwc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zwdtsrzbwc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zwdtsrzbwc .gt_left { text-align: left; }
 #zwdtsrzbwc .gt_center { text-align: center; }
 #zwdtsrzbwc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zwdtsrzbwc .gt_font_normal { font-weight: normal; }
 #zwdtsrzbwc .gt_font_bold { font-weight: bold; }
 #zwdtsrzbwc .gt_font_italic { font-style: italic; }
 #zwdtsrzbwc .gt_super { font-size: 65%; }
 #zwdtsrzbwc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zwdtsrzbwc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zwdtsrzbwc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zwdtsrzbwc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zwdtsrzbwc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zwdtsrzbwc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| segment   | duration              |
|-----------|-----------------------|
| Warm-up   | 10 minutes            |
| Main set  | 45 minutes 30 seconds |
| Cool-down | 5 minutes             |
