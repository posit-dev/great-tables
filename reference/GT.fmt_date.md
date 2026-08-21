# GT.fmt_date()


Format values as dates.


Usage

``` python
GT.fmt_date(
    columns=None, rows=None, date_style="iso", pattern="{x}", locale=None
)
```


Format input values to time values using one of 17 preset date styles. Input can be in the form of `date` type or as a ISO-8601 string (in the form of `YYYY-MM-DD HH:MM:SS` or `YYYY-MM-DD`).


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`date_style: DateStyle = ``"iso"`  
The date style to use. By default this is the short name `"iso"` which corresponds to ISO 8601 date formatting. There are 41 date styles in total.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Formatting With The `date_style=` Argument

We need to supply a preset date style to the `date_style=` argument. The date styles are numerous and can handle localization to any supported locale. The following table provides a listing of all date styles and their output values (corresponding to an input date of `2000-02-29`).

|     | Date Style              | Output                         |
|-----|-------------------------|--------------------------------|
| 1   | `"iso"`                 | `"2000-02-29"`                 |
| 2   | `"wday_month_day_year"` | `"Tuesday, February 29, 2000"` |
| 3   | `"wd_m_day_year"`       | `"Tue, Feb 29, 2000"`          |
| 4   | `"wday_day_month_year"` | `"Tuesday 29 February 2000"`   |
| 5   | `"month_day_year"`      | `"February 29, 2000"`          |
| 6   | `"m_day_year"`          | `"Feb 29, 2000"`               |
| 7   | `"day_m_year"`          | `"29 Feb 2000"`                |
| 8   | `"day_month_year"`      | `"29 February 2000"`           |
| 9   | `"day_month"`           | `"29 February"`                |
| 10  | `"day_m"`               | `"29 Feb"`                     |
| 11  | `"year"`                | `"2000"`                       |
| 12  | `"month"`               | `"February"`                   |
| 13  | `"day"`                 | `"29"`                         |
| 14  | `"year.mn.day"`         | `"2000/02/29"`                 |
| 15  | `"y.mn.day"`            | `"00/02/29"`                   |
| 16  | `"year_week"`           | `"2000-W09"`                   |
| 17  | `"year_quarter"`        | `"2000-Q1"`                    |


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). Note that a `locale` value provided here will override any global locale setting performed in <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `date` and `time` columns). With the [fmt_date()](GT.fmt_date.md#great_tables.GT.fmt_date) method, we'll format the `date` column to display dates formatted with the `"month_day_year"` date style.


``` python
from great_tables import GT, exibble

exibble_mini = exibble[["date", "time"]]

(
    GT(exibble_mini)
    .fmt_date(columns="date", date_style="month_day_year")
)
```


<style>
#nnydssyvpk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nnydssyvpk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nnydssyvpk p { margin: 0; padding: 0; }
 #nnydssyvpk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nnydssyvpk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nnydssyvpk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nnydssyvpk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nnydssyvpk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nnydssyvpk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nnydssyvpk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nnydssyvpk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nnydssyvpk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nnydssyvpk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nnydssyvpk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nnydssyvpk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nnydssyvpk .gt_spanner_row { border-bottom-style: hidden; }
 #nnydssyvpk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nnydssyvpk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nnydssyvpk .gt_from_md> :first-child { margin-top: 0; }
 #nnydssyvpk .gt_from_md> :last-child { margin-bottom: 0; }
 #nnydssyvpk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nnydssyvpk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nnydssyvpk .gt_indent_1 { text-indent: 5px; }
 #nnydssyvpk .gt_indent_2 { text-indent: calc(5px * 2); }
 #nnydssyvpk .gt_indent_3 { text-indent: calc(5px * 3); }
 #nnydssyvpk .gt_indent_4 { text-indent: calc(5px * 4); }
 #nnydssyvpk .gt_indent_5 { text-indent: calc(5px * 5); }
 #nnydssyvpk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nnydssyvpk .gt_row_group_first td { border-top-width: 2px; }
 #nnydssyvpk .gt_row_group_first th { border-top-width: 2px; }
 #nnydssyvpk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nnydssyvpk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nnydssyvpk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nnydssyvpk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nnydssyvpk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nnydssyvpk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nnydssyvpk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nnydssyvpk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nnydssyvpk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nnydssyvpk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nnydssyvpk .gt_left { text-align: left; }
 #nnydssyvpk .gt_center { text-align: center; }
 #nnydssyvpk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nnydssyvpk .gt_font_normal { font-weight: normal; }
 #nnydssyvpk .gt_font_bold { font-weight: bold; }
 #nnydssyvpk .gt_font_italic { font-style: italic; }
 #nnydssyvpk .gt_super { font-size: 65%; }
 #nnydssyvpk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nnydssyvpk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nnydssyvpk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nnydssyvpk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nnydssyvpk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nnydssyvpk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date              | time  |
|-------------------|-------|
| January 15, 2015  | 13:35 |
| February 15, 2015 | 14:40 |
| March 15, 2015    | 15:45 |
| April 15, 2015    | 16:50 |
| May 15, 2015      | 17:55 |
| June 15, 2015     |       |
|                   | 19:10 |
| August 15, 2015   | 20:20 |
