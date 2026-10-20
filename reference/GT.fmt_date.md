# GT.fmt_date()


Format values as dates.


Usage

``` python
GT.fmt_date(
    columns=None,
    rows=None,
    date_style="iso",
    pattern="{x}",
    locale=None,
)
```


Format input values to date values using one of 41 preset date styles. Input can be in the form of `date` type or as a ISO-8601 string (in the form of `YYYY-MM-DD HH:MM:SS` or `YYYY-MM-DD`).


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`date_style: DateStyle = ``"iso"`  
The date style to use. By default this is the short name `"iso"` which corresponds to ISO 8601 date formatting. There are 41 date styles in total.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Formatting With The `date_style=` Argument

We need to supply a preset date style to the `date_style=` argument. The date styles are numerous and can handle localization to any supported locale. A large segment of date styles are termed flexible date formats and this means that their output will adapt to any `locale=` provided: the order of the fields, the punctuation, and even which fields are abbreviated follow the locale's conventions (e.g., `"yMMMd"` is `"Feb 29, 2000"` in English and `"29. Feb. 2000"` in German). That feature makes the flexible date formats a better option for locales other than `"en"` (the default locale).

The following table provides a listing of all date styles and their output values (corresponding to an input date of `2000-02-29`).

|     | Date Style              | Output                         | Notes    |
|-----|-------------------------|--------------------------------|----------|
| 1   | `"iso"`                 | `"2000-02-29"`                 | ISO 8601 |
| 2   | `"wday_month_day_year"` | `"Tuesday, February 29, 2000"` |          |
| 3   | `"wd_m_day_year"`       | `"Tue, Feb 29, 2000"`          |          |
| 4   | `"wday_day_month_year"` | `"Tuesday 29 February 2000"`   |          |
| 5   | `"month_day_year"`      | `"February 29, 2000"`          |          |
| 6   | `"m_day_year"`          | `"Feb 29, 2000"`               |          |
| 7   | `"day_m_year"`          | `"29 Feb 2000"`                |          |
| 8   | `"day_month_year"`      | `"29 February 2000"`           |          |
| 9   | `"day_month"`           | `"29 February"`                |          |
| 10  | `"day_m"`               | `"29 Feb"`                     |          |
| 11  | `"year"`                | `"2000"`                       |          |
| 12  | `"month"`               | `"February"`                   |          |
| 13  | `"day"`                 | `"29"`                         |          |
| 14  | `"year.mn.day"`         | `"2000/02/29"`                 |          |
| 15  | `"y.mn.day"`            | `"00/02/29"`                   |          |
| 16  | `"year_week"`           | `"2000-W09"`                   | ISO 8601 |
| 17  | `"year_quarter"`        | `"2000-Q1"`                    |          |
| 18  | `"yMd"`                 | `"2/29/2000"`                  | flexible |
| 19  | `"yMEd"`                | `"Tue, 2/29/2000"`             | flexible |
| 20  | `"yMMM"`                | `"Feb 2000"`                   | flexible |
| 21  | `"yMMMM"`               | `"February 2000"`              | flexible |
| 22  | `"yMMMd"`               | `"Feb 29, 2000"`               | flexible |
| 23  | `"yMMMEd"`              | `"Tue, Feb 29, 2000"`          | flexible |
| 24  | `"GyMd"`                | `"2/29/2000 AD"`               | flexible |
| 25  | `"GyMMMd"`              | `"Feb 29, 2000 AD"`            | flexible |
| 26  | `"GyMMMEd"`             | `"Tue, Feb 29, 2000 AD"`       | flexible |
| 27  | `"yM"`                  | `"2/2000"`                     | flexible |
| 28  | `"Md"`                  | `"2/29"`                       | flexible |
| 29  | `"MEd"`                 | `"Tue, 2/29"`                  | flexible |
| 30  | `"MMMd"`                | `"Feb 29"`                     | flexible |
| 31  | `"MMMEd"`               | `"Tue, Feb 29"`                | flexible |
| 32  | `"MMMMd"`               | `"February 29"`                | flexible |
| 33  | `"GyMMM"`               | `"Feb 2000 AD"`                | flexible |
| 34  | `"yQQQ"`                | `"Q1 2000"`                    | flexible |
| 35  | `"yQQQQ"`               | `"1st quarter 2000"`           | flexible |
| 36  | `"Gy"`                  | `"2000 AD"`                    | flexible |
| 37  | `"y"`                   | `"2000"`                       | flexible |
| 38  | `"M"`                   | `"2"`                          | flexible |
| 39  | `"MMM"`                 | `"Feb"`                        | flexible |
| 40  | `"d"`                   | `"29"`                         | flexible |
| 41  | `"Ed"`                  | `"29 Tue"`                     | flexible |

The `"year_week"` style gives the ISO 8601 week date in every locale: weeks start on Monday, week 1 is the week containing the first Thursday of the year, and the year shown is the one the week belongs to (so `2024-12-30` is `"2025-W01"`).

The names of the flexible date styles are CLDR skeletons, where each letter stands for a field: `G` is the era, `y` the year, `Q` the quarter, `M` the month, `d` the day of the month, and `E` the day of the week. A longer run of `Q`, `M`, or `E` gives a longer form of that field.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). Note that a `locale` value provided here will override any global locale setting performed in <a href="../reference/GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `date` and `time` columns). With the <a href="../reference/GT.fmt_date.html#great_tables.GT.fmt_date" class="gdls-link"><code>fmt_date()</code></a> method, we'll format the `date` column to display dates formatted with the `"month_day_year"` date style.


``` python
from great_tables import GT, exibble

exibble_mini = exibble[["date", "time"]]

(
    GT(exibble_mini)
    .fmt_date(columns="date", date_style="month_day_year")
)
```


<style>
#peuyehvzjb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#peuyehvzjb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#peuyehvzjb p { margin: 0; padding: 0; }
 #peuyehvzjb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #peuyehvzjb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #peuyehvzjb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #peuyehvzjb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #peuyehvzjb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #peuyehvzjb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #peuyehvzjb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #peuyehvzjb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #peuyehvzjb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #peuyehvzjb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #peuyehvzjb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #peuyehvzjb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #peuyehvzjb .gt_spanner_row { border-bottom-style: hidden; }
 #peuyehvzjb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #peuyehvzjb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #peuyehvzjb .gt_from_md> :first-child { margin-top: 0; }
 #peuyehvzjb .gt_from_md> :last-child { margin-bottom: 0; }
 #peuyehvzjb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #peuyehvzjb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #peuyehvzjb .gt_indent_1 { text-indent: 5px; }
 #peuyehvzjb .gt_indent_2 { text-indent: calc(5px * 2); }
 #peuyehvzjb .gt_indent_3 { text-indent: calc(5px * 3); }
 #peuyehvzjb .gt_indent_4 { text-indent: calc(5px * 4); }
 #peuyehvzjb .gt_indent_5 { text-indent: calc(5px * 5); }
 #peuyehvzjb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #peuyehvzjb .gt_row_group_first td { border-top-width: 2px; }
 #peuyehvzjb .gt_row_group_first th { border-top-width: 2px; }
 #peuyehvzjb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #peuyehvzjb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #peuyehvzjb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #peuyehvzjb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #peuyehvzjb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #peuyehvzjb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #peuyehvzjb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #peuyehvzjb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #peuyehvzjb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #peuyehvzjb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #peuyehvzjb .gt_left { text-align: left; }
 #peuyehvzjb .gt_center { text-align: center; }
 #peuyehvzjb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #peuyehvzjb .gt_font_normal { font-weight: normal; }
 #peuyehvzjb .gt_font_bold { font-weight: bold; }
 #peuyehvzjb .gt_font_italic { font-style: italic; }
 #peuyehvzjb .gt_super { font-size: 65%; }
 #peuyehvzjb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #peuyehvzjb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #peuyehvzjb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #peuyehvzjb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #peuyehvzjb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #peuyehvzjb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date              | time  |
|-------------------|-------|
| January 15, 2015  | 13:35 |
| February 15, 2015 | 14:40 |
| March 15, 2015    | 15:45 |
| April 15, 2015    | 16:50 |
| May 15, 2015      | 17:55 |
| June 15, 2015     | None  |
| None              | 19:10 |
| August 15, 2015   | 20:20 |


A flexible date style adapts to the locale. Here, the `"yMMMEd"` style is used to format the dates for a table in German.


``` python
(
    GT(exibble_mini, locale="de")
    .fmt_date(columns="date", date_style="yMMMEd")
)
```


<style>
#cwcyfkplph table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cwcyfkplph thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cwcyfkplph p { margin: 0; padding: 0; }
 #cwcyfkplph .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cwcyfkplph .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cwcyfkplph .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cwcyfkplph .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cwcyfkplph .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cwcyfkplph .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cwcyfkplph .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cwcyfkplph .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cwcyfkplph .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cwcyfkplph .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cwcyfkplph .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cwcyfkplph .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cwcyfkplph .gt_spanner_row { border-bottom-style: hidden; }
 #cwcyfkplph .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cwcyfkplph .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cwcyfkplph .gt_from_md> :first-child { margin-top: 0; }
 #cwcyfkplph .gt_from_md> :last-child { margin-bottom: 0; }
 #cwcyfkplph .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cwcyfkplph .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cwcyfkplph .gt_indent_1 { text-indent: 5px; }
 #cwcyfkplph .gt_indent_2 { text-indent: calc(5px * 2); }
 #cwcyfkplph .gt_indent_3 { text-indent: calc(5px * 3); }
 #cwcyfkplph .gt_indent_4 { text-indent: calc(5px * 4); }
 #cwcyfkplph .gt_indent_5 { text-indent: calc(5px * 5); }
 #cwcyfkplph .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cwcyfkplph .gt_row_group_first td { border-top-width: 2px; }
 #cwcyfkplph .gt_row_group_first th { border-top-width: 2px; }
 #cwcyfkplph .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cwcyfkplph .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cwcyfkplph .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cwcyfkplph .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cwcyfkplph .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cwcyfkplph .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cwcyfkplph .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cwcyfkplph .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cwcyfkplph .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cwcyfkplph .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cwcyfkplph .gt_left { text-align: left; }
 #cwcyfkplph .gt_center { text-align: center; }
 #cwcyfkplph .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cwcyfkplph .gt_font_normal { font-weight: normal; }
 #cwcyfkplph .gt_font_bold { font-weight: bold; }
 #cwcyfkplph .gt_font_italic { font-style: italic; }
 #cwcyfkplph .gt_super { font-size: 65%; }
 #cwcyfkplph .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cwcyfkplph .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cwcyfkplph .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cwcyfkplph .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cwcyfkplph .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cwcyfkplph .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date               | time  |
|--------------------|-------|
| Do., 15. Jan. 2015 | 13:35 |
| So., 15. Feb. 2015 | 14:40 |
| So., 15. März 2015 | 15:45 |
| Mi., 15. Apr. 2015 | 16:50 |
| Fr., 15. Mai 2015  | 17:55 |
| Mo., 15. Juni 2015 | None  |
| None               | 19:10 |
| Sa., 15. Aug. 2015 | 20:20 |
