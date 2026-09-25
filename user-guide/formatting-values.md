# Formatting Values

Raw data values in a table are rarely in their ideal presentation form. Numbers might need consistent decimal places, dates should appear in a readable format, and currencies require the appropriate symbols. The `fmt_*()` family of methods in **Great Tables** handles all of this, letting you transform cell values into well-formatted text while preserving the underlying data for things like sorting and colorization.

Unformatted numbers are hard to scan. When every number has a different number of decimal places, or when large numbers lack digit separators, readers slow down as they try to parse each value. Consistent formatting reduces cognitive load and makes comparisons across rows immediate. The same principle applies to dates and currencies: a reader should never have to guess whether "03/04" means March 4th or April 3rd.


# Formatting Cells in the Table Body

The values within the table body, specifically those within the body cells, can be formatted with a large selection of `fmt_*()` methods like [fmt_number()](../reference/GT.fmt_number.md#great_tables.GT.fmt_number), [fmt_integer()](../reference/GT.fmt_integer.md#great_tables.GT.fmt_integer), [fmt_scientific()](../reference/GT.fmt_scientific.md#great_tables.GT.fmt_scientific), and more. Let's use a portion of the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset and introduce some formatting to the cell values. First, we'll generate the basic GT object and take a look at the table without any cell formatting applied.


``` python
from great_tables import GT, vals
from great_tables.data import exibble

gt_ex = GT(exibble[["num", "date", "time", "currency"]].head(5))

gt_ex
```


<style>
#ngttkrevez table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ngttkrevez thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ngttkrevez p { margin: 0; padding: 0; }
 #ngttkrevez .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ngttkrevez .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ngttkrevez .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ngttkrevez .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ngttkrevez .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ngttkrevez .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngttkrevez .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ngttkrevez .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ngttkrevez .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ngttkrevez .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ngttkrevez .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ngttkrevez .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ngttkrevez .gt_spanner_row { border-bottom-style: hidden; }
 #ngttkrevez .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ngttkrevez .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ngttkrevez .gt_from_md> :first-child { margin-top: 0; }
 #ngttkrevez .gt_from_md> :last-child { margin-bottom: 0; }
 #ngttkrevez .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ngttkrevez .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ngttkrevez .gt_indent_1 { text-indent: 5px; }
 #ngttkrevez .gt_indent_2 { text-indent: calc(5px * 2); }
 #ngttkrevez .gt_indent_3 { text-indent: calc(5px * 3); }
 #ngttkrevez .gt_indent_4 { text-indent: calc(5px * 4); }
 #ngttkrevez .gt_indent_5 { text-indent: calc(5px * 5); }
 #ngttkrevez .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ngttkrevez .gt_row_group_first td { border-top-width: 2px; }
 #ngttkrevez .gt_row_group_first th { border-top-width: 2px; }
 #ngttkrevez .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ngttkrevez .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngttkrevez .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ngttkrevez .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ngttkrevez .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngttkrevez .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ngttkrevez .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ngttkrevez .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ngttkrevez .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngttkrevez .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ngttkrevez .gt_left { text-align: left; }
 #ngttkrevez .gt_center { text-align: center; }
 #ngttkrevez .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ngttkrevez .gt_font_normal { font-weight: normal; }
 #ngttkrevez .gt_font_bold { font-weight: bold; }
 #ngttkrevez .gt_font_italic { font-style: italic; }
 #ngttkrevez .gt_super { font-size: 65%; }
 #ngttkrevez .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngttkrevez .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ngttkrevez .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngttkrevez .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ngttkrevez .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ngttkrevez .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | date       | time  | currency |
|--------|------------|-------|----------|
| 0.1111 | 2015-01-15 | 13:35 | 49.95    |
| 2.222  | 2015-02-15 | 14:40 | 17.95    |
| 33.33  | 2015-03-15 | 15:45 | 1.39     |
| 444.4  | 2015-04-15 | 16:50 | 65100.0  |
| 5550.0 | 2015-05-15 | 17:55 | 1325.81  |


The `num` column contains both small and much larger numbers. We can use the [fmt_number()](../reference/GT.fmt_number.md#great_tables.GT.fmt_number) method to obtain formatted values have a fixed level of decimal precision and grouping separators. At the same time, we'll format the numeric values in `currency` column to get monetary values.


``` python
gt_ex = gt_ex.fmt_number(columns="num", decimals=2).fmt_currency(columns="currency")

gt_ex
```


<style>
#qxyhmotfmm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qxyhmotfmm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qxyhmotfmm p { margin: 0; padding: 0; }
 #qxyhmotfmm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qxyhmotfmm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qxyhmotfmm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qxyhmotfmm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qxyhmotfmm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qxyhmotfmm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qxyhmotfmm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qxyhmotfmm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qxyhmotfmm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qxyhmotfmm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qxyhmotfmm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qxyhmotfmm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qxyhmotfmm .gt_spanner_row { border-bottom-style: hidden; }
 #qxyhmotfmm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qxyhmotfmm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qxyhmotfmm .gt_from_md> :first-child { margin-top: 0; }
 #qxyhmotfmm .gt_from_md> :last-child { margin-bottom: 0; }
 #qxyhmotfmm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qxyhmotfmm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qxyhmotfmm .gt_indent_1 { text-indent: 5px; }
 #qxyhmotfmm .gt_indent_2 { text-indent: calc(5px * 2); }
 #qxyhmotfmm .gt_indent_3 { text-indent: calc(5px * 3); }
 #qxyhmotfmm .gt_indent_4 { text-indent: calc(5px * 4); }
 #qxyhmotfmm .gt_indent_5 { text-indent: calc(5px * 5); }
 #qxyhmotfmm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qxyhmotfmm .gt_row_group_first td { border-top-width: 2px; }
 #qxyhmotfmm .gt_row_group_first th { border-top-width: 2px; }
 #qxyhmotfmm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qxyhmotfmm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qxyhmotfmm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qxyhmotfmm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qxyhmotfmm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qxyhmotfmm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qxyhmotfmm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qxyhmotfmm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qxyhmotfmm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qxyhmotfmm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qxyhmotfmm .gt_left { text-align: left; }
 #qxyhmotfmm .gt_center { text-align: center; }
 #qxyhmotfmm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qxyhmotfmm .gt_font_normal { font-weight: normal; }
 #qxyhmotfmm .gt_font_bold { font-weight: bold; }
 #qxyhmotfmm .gt_font_italic { font-style: italic; }
 #qxyhmotfmm .gt_super { font-size: 65%; }
 #qxyhmotfmm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qxyhmotfmm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qxyhmotfmm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qxyhmotfmm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qxyhmotfmm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qxyhmotfmm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num      | date       | time  | currency    |
|----------|------------|-------|-------------|
| 0.11     | 2015-01-15 | 13:35 | \$49.95     |
| 2.22     | 2015-02-15 | 14:40 | \$17.95     |
| 33.33    | 2015-03-15 | 15:45 | \$1.39      |
| 444.40   | 2015-04-15 | 16:50 | \$65,100.00 |
| 5,550.00 | 2015-05-15 | 17:55 | \$1,325.81  |


Formatting methods can be called in any order and on overlapping column selections. The last formatter to touch a given cell wins, which gives you flexibility to set a broad default across an entire column and then override specific rows or subsets afterward.

Dates and times can be formatted as well. As long as they are in ISO 8601 form, the [fmt_date()](../reference/GT.fmt_date.md#great_tables.GT.fmt_date) and [fmt_time()](../reference/GT.fmt_time.md#great_tables.GT.fmt_time) methods can be used to format such values. These methods have corresponding `date_style=` and `time_style=` arguments that accept a number of keywords that act as preset formatting styles.


``` python
gt_ex = (
    gt_ex.fmt_date(columns="date", date_style="m_day_year")
    .fmt_time(columns="time", time_style="h_m_p")
)

gt_ex
```


<style>
#quvxqrstcu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#quvxqrstcu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#quvxqrstcu p { margin: 0; padding: 0; }
 #quvxqrstcu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #quvxqrstcu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #quvxqrstcu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #quvxqrstcu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #quvxqrstcu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #quvxqrstcu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #quvxqrstcu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #quvxqrstcu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #quvxqrstcu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #quvxqrstcu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #quvxqrstcu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #quvxqrstcu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #quvxqrstcu .gt_spanner_row { border-bottom-style: hidden; }
 #quvxqrstcu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #quvxqrstcu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #quvxqrstcu .gt_from_md> :first-child { margin-top: 0; }
 #quvxqrstcu .gt_from_md> :last-child { margin-bottom: 0; }
 #quvxqrstcu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #quvxqrstcu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #quvxqrstcu .gt_indent_1 { text-indent: 5px; }
 #quvxqrstcu .gt_indent_2 { text-indent: calc(5px * 2); }
 #quvxqrstcu .gt_indent_3 { text-indent: calc(5px * 3); }
 #quvxqrstcu .gt_indent_4 { text-indent: calc(5px * 4); }
 #quvxqrstcu .gt_indent_5 { text-indent: calc(5px * 5); }
 #quvxqrstcu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #quvxqrstcu .gt_row_group_first td { border-top-width: 2px; }
 #quvxqrstcu .gt_row_group_first th { border-top-width: 2px; }
 #quvxqrstcu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #quvxqrstcu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #quvxqrstcu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #quvxqrstcu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #quvxqrstcu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #quvxqrstcu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #quvxqrstcu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #quvxqrstcu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #quvxqrstcu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #quvxqrstcu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #quvxqrstcu .gt_left { text-align: left; }
 #quvxqrstcu .gt_center { text-align: center; }
 #quvxqrstcu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #quvxqrstcu .gt_font_normal { font-weight: normal; }
 #quvxqrstcu .gt_font_bold { font-weight: bold; }
 #quvxqrstcu .gt_font_italic { font-style: italic; }
 #quvxqrstcu .gt_super { font-size: 65%; }
 #quvxqrstcu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #quvxqrstcu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #quvxqrstcu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #quvxqrstcu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #quvxqrstcu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #quvxqrstcu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num      | date         | time    | currency    |
|----------|--------------|---------|-------------|
| 0.11     | Jan 15, 2015 | 1:35 PM | \$49.95     |
| 2.22     | Feb 15, 2015 | 2:40 PM | \$17.95     |
| 33.33    | Mar 15, 2015 | 3:45 PM | \$1.39      |
| 444.40   | Apr 15, 2015 | 4:50 PM | \$65,100.00 |
| 5,550.00 | May 15, 2015 | 5:55 PM | \$1,325.81  |


It's possible to format cells that have already been formatted. Using a formatting method again on previously formatted cells will always work within the 'last-formatted-wins' rule.


``` python
gt_ex = gt_ex.fmt_date(columns="date", date_style="wday_day_month_year")

gt_ex
```


<style>
#tkcsmaykrp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tkcsmaykrp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tkcsmaykrp p { margin: 0; padding: 0; }
 #tkcsmaykrp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tkcsmaykrp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tkcsmaykrp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tkcsmaykrp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tkcsmaykrp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tkcsmaykrp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tkcsmaykrp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tkcsmaykrp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tkcsmaykrp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tkcsmaykrp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tkcsmaykrp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tkcsmaykrp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tkcsmaykrp .gt_spanner_row { border-bottom-style: hidden; }
 #tkcsmaykrp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tkcsmaykrp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tkcsmaykrp .gt_from_md> :first-child { margin-top: 0; }
 #tkcsmaykrp .gt_from_md> :last-child { margin-bottom: 0; }
 #tkcsmaykrp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tkcsmaykrp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tkcsmaykrp .gt_indent_1 { text-indent: 5px; }
 #tkcsmaykrp .gt_indent_2 { text-indent: calc(5px * 2); }
 #tkcsmaykrp .gt_indent_3 { text-indent: calc(5px * 3); }
 #tkcsmaykrp .gt_indent_4 { text-indent: calc(5px * 4); }
 #tkcsmaykrp .gt_indent_5 { text-indent: calc(5px * 5); }
 #tkcsmaykrp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tkcsmaykrp .gt_row_group_first td { border-top-width: 2px; }
 #tkcsmaykrp .gt_row_group_first th { border-top-width: 2px; }
 #tkcsmaykrp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tkcsmaykrp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tkcsmaykrp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tkcsmaykrp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tkcsmaykrp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tkcsmaykrp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tkcsmaykrp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tkcsmaykrp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tkcsmaykrp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tkcsmaykrp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tkcsmaykrp .gt_left { text-align: left; }
 #tkcsmaykrp .gt_center { text-align: center; }
 #tkcsmaykrp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tkcsmaykrp .gt_font_normal { font-weight: normal; }
 #tkcsmaykrp .gt_font_bold { font-weight: bold; }
 #tkcsmaykrp .gt_font_italic { font-style: italic; }
 #tkcsmaykrp .gt_super { font-size: 65%; }
 #tkcsmaykrp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tkcsmaykrp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tkcsmaykrp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tkcsmaykrp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tkcsmaykrp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tkcsmaykrp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num      | date                     | time    | currency    |
|----------|--------------------------|---------|-------------|
| 0.11     | Thursday 15 January 2015 | 1:35 PM | \$49.95     |
| 2.22     | Sunday 15 February 2015  | 2:40 PM | \$17.95     |
| 33.33    | Sunday 15 March 2015     | 3:45 PM | \$1.39      |
| 444.40   | Wednesday 15 April 2015  | 4:50 PM | \$65,100.00 |
| 5,550.00 | Friday 15 May 2015       | 5:55 PM | \$1,325.81  |


Within the selected `columns=` we can choose to target specific cells with the `rows=` argument. The latter argument allows us to pass in a list of row indices.


``` python
gt_ex = gt_ex.fmt_currency(columns="currency", rows=[2, 3, 4], currency="GBP")

gt_ex
```


<style>
#duifclfhec table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#duifclfhec thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#duifclfhec p { margin: 0; padding: 0; }
 #duifclfhec .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #duifclfhec .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #duifclfhec .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #duifclfhec .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #duifclfhec .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #duifclfhec .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #duifclfhec .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #duifclfhec .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #duifclfhec .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #duifclfhec .gt_column_spanner_outer:first-child { padding-left: 0; }
 #duifclfhec .gt_column_spanner_outer:last-child { padding-right: 0; }
 #duifclfhec .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #duifclfhec .gt_spanner_row { border-bottom-style: hidden; }
 #duifclfhec .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #duifclfhec .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #duifclfhec .gt_from_md> :first-child { margin-top: 0; }
 #duifclfhec .gt_from_md> :last-child { margin-bottom: 0; }
 #duifclfhec .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #duifclfhec .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #duifclfhec .gt_indent_1 { text-indent: 5px; }
 #duifclfhec .gt_indent_2 { text-indent: calc(5px * 2); }
 #duifclfhec .gt_indent_3 { text-indent: calc(5px * 3); }
 #duifclfhec .gt_indent_4 { text-indent: calc(5px * 4); }
 #duifclfhec .gt_indent_5 { text-indent: calc(5px * 5); }
 #duifclfhec .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #duifclfhec .gt_row_group_first td { border-top-width: 2px; }
 #duifclfhec .gt_row_group_first th { border-top-width: 2px; }
 #duifclfhec .gt_striped { color: #333333; background-color: #F4F4F4; }
 #duifclfhec .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #duifclfhec .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #duifclfhec .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #duifclfhec .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #duifclfhec .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #duifclfhec .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #duifclfhec .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #duifclfhec .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #duifclfhec .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #duifclfhec .gt_left { text-align: left; }
 #duifclfhec .gt_center { text-align: center; }
 #duifclfhec .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #duifclfhec .gt_font_normal { font-weight: normal; }
 #duifclfhec .gt_font_bold { font-weight: bold; }
 #duifclfhec .gt_font_italic { font-style: italic; }
 #duifclfhec .gt_super { font-size: 65%; }
 #duifclfhec .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #duifclfhec .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #duifclfhec .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #duifclfhec .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #duifclfhec .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #duifclfhec .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num      | date                     | time    | currency   |
|----------|--------------------------|---------|------------|
| 0.11     | Thursday 15 January 2015 | 1:35 PM | \$49.95    |
| 2.22     | Sunday 15 February 2015  | 2:40 PM | \$17.95    |
| 33.33    | Sunday 15 March 2015     | 3:45 PM | £1.39      |
| 444.40   | Wednesday 15 April 2015  | 4:50 PM | £65,100.00 |
| 5,550.00 | Friday 15 May 2015       | 5:55 PM | £1,325.81  |


Now the first two rows display in USD and the last three in GBP, demonstrating how the same column can present different currencies by targeting specific rows.

Per-row formatting like this is particularly useful for international datasets where different rows may need different currency symbols, date formats, or number conventions. Rather than splitting the data into separate tables by locale, you can handle everything in a single table with targeted formatting calls.


# Arguments Common to Several Formatting Methods/Functions

While we can use the `fmt_*()` methods on a table, we can also use the functional versions of these methods on scalar values or lists of values. These variants exist within the `vals` module. While arguments across these functions and their corresponding method aren't exactly the same, there are nonetheless many arguments that are shared amongst them. Here are some of the most commonly used arguments:

- `decimals=`: set a fixed precision of decimal places
- `sep_mark=`, `dec_mark=`: set digit separators and the decimal symbol (defaults are `","` and `"."`)
- `scale_by=`: we can choose to scale targeted values by a multiplier value
- `compact=`: larger figures (thousands, millions, etc.) can be autoscaled and decorated with the appropriate suffixes (e.g., `"10000"` becomes `"10K"`)
- `pattern=`: option to use a text pattern for decoration of the formatted values
- `locale=`: providing a locale ID (e.g., `"en"`, `"fr"`, `"de-AT"`, etc.) will result in numeric formatting specific to the chosen locale

Here are a number of examples that use [vals.fmt_number()](../reference/vals.fmt_number.md#great_tables.vals.fmt_number).


``` python
fmt_number_1 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37])
fmt_number_2 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37], compact=True)
fmt_number_3 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37], decimals=3)
fmt_number_4 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37], pattern="[{x}]")
fmt_number_5 = vals.fmt_number([1.64, 3.26, 3000.63, 236742.37], locale="es")

print(fmt_number_1, fmt_number_2, fmt_number_3, fmt_number_4, fmt_number_5, sep="\n")
```


    ['1.64', '3.26', '3,000.63', '236,742.37']
    ['1.64', '3.26', '3.00K', '236.74K']
    ['1.640', '3.260', '3,000.630', '236,742.370']
    ['[1.64]', '[3.26]', '[3,000.63]', '[236,742.37]']
    ['1,64', '3,26', '3.000,63', '236.742,37']


Scientific notation can be done with [vals.fmt_scientific()](../reference/vals.fmt_scientific.md#great_tables.vals.fmt_scientific).


``` python
fmt_sci_1 = vals.fmt_scientific([0.00064, 7.353, 863454.63])
fmt_sci_2 = vals.fmt_scientific([1.64, 3.26, 3000.63], decimals=3)
fmt_sci_3 = vals.fmt_scientific([1.64, 3.26, 3000.63], exp_style="E")
fmt_sci_4 = vals.fmt_scientific([1.64, 3.26, 3000.63], locale="de")

print(fmt_sci_1, fmt_sci_2, fmt_sci_3, fmt_sci_4, sep="\n")
```


    ["6.40 × 10<sup style='font-size: 65%;'>−4</sup>", '7.35', "8.63 × 10<sup style='font-size: 65%;'>5</sup>"]
    ['1.640', '3.260', "3.001 × 10<sup style='font-size: 65%;'>3</sup>"]
    ['1.64E00', '3.26E00', '3.00E03']
    ['1,64', '3,26', "3,00 × 10<sup style='font-size: 65%;'>3</sup>"]


Dates and times are handled with [vals.fmt_date()](../reference/vals.fmt_date.md#great_tables.vals.fmt_date) and [vals.fmt_time()](../reference/vals.fmt_time.md#great_tables.vals.fmt_time).


``` python
fmt_date_1 = vals.fmt_date(
    ["2015-03-15", "2017-08-18", "2020-04-12"], date_style="wday_month_day_year"
)
fmt_date_2 = vals.fmt_date(["2015-03-15", "2017-08-18", "2020-04-12"], date_style="month_day_year")
fmt_time_1 = vals.fmt_time(["23:03", "00:55", "08:23"], time_style="h_m_p")
fmt_time_2 = vals.fmt_time(["23:03", "00:55", "08:23"], time_style="h_p")

print(fmt_date_1, fmt_date_2, fmt_time_1, fmt_time_2, sep="\n")
```


    ['Sunday, March 15, 2015', 'Friday, August 18, 2017', 'Sunday, April 12, 2020']
    ['March 15, 2015', 'August 18, 2017', 'April 12, 2020']
    ['11:03 PM', '12:55 AM', '8:23 AM']
    ['11 PM', '12 AM', '8 AM']


The `vals` functions are especially handy during development, when you want to quickly test how a formatting option looks without building a full table. Sometimes it's easier and more convenient to experiment with formatting using the formatting functions in the `vals` module. There are many options to explore with each type of formatting and so visiting the [API Reference](../reference/) is certainly worthwhile.


# HTML Escaping of Cell Values

When rendering to HTML, **Great Tables** automatically escapes special characters (`<`, `>`, `&`, `"`, `'`) in body cells that have *not* been processed by a `fmt_*()` method. This prevents cross-site scripting (XSS) when displaying untrusted data (e.g., user-submitted text, CSV uploads) in web applications, dashboards, or reports.

Cells that *have* been formatted (e.g., with `fmt_number()`, `fmt_markdown()`, `fmt_image()`, etc.) are treated as trusted HTML and are not escaped. This allows formatters to produce rich HTML content like images, links, and styled text.

To include raw HTML or Markdown in cells that would otherwise be escaped, use a formatting method with the [html()](../reference/html.md#great_tables.html) or [md()](../reference/md.md#great_tables.md) helpers:


``` python
from great_tables import html, md
import pandas as pd

df = pd.DataFrame({
    "plain": ["x & y", "a < b"],
    "rich_html": ["<b>bold</b>", "<em>italic</em>"],
    "rich_md": ["**bold**", "*italic*"],
})

(
    GT(df)
    .fmt(columns="rich_html", fns=lambda x: html(x).to_html())
    .fmt(columns="rich_md", fns=lambda x: md(x).to_html())
)
```


<style>
#jemotcldkt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jemotcldkt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jemotcldkt p { margin: 0; padding: 0; }
 #jemotcldkt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jemotcldkt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jemotcldkt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jemotcldkt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jemotcldkt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jemotcldkt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jemotcldkt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jemotcldkt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jemotcldkt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jemotcldkt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jemotcldkt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jemotcldkt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jemotcldkt .gt_spanner_row { border-bottom-style: hidden; }
 #jemotcldkt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jemotcldkt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jemotcldkt .gt_from_md> :first-child { margin-top: 0; }
 #jemotcldkt .gt_from_md> :last-child { margin-bottom: 0; }
 #jemotcldkt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jemotcldkt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jemotcldkt .gt_indent_1 { text-indent: 5px; }
 #jemotcldkt .gt_indent_2 { text-indent: calc(5px * 2); }
 #jemotcldkt .gt_indent_3 { text-indent: calc(5px * 3); }
 #jemotcldkt .gt_indent_4 { text-indent: calc(5px * 4); }
 #jemotcldkt .gt_indent_5 { text-indent: calc(5px * 5); }
 #jemotcldkt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jemotcldkt .gt_row_group_first td { border-top-width: 2px; }
 #jemotcldkt .gt_row_group_first th { border-top-width: 2px; }
 #jemotcldkt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jemotcldkt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jemotcldkt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jemotcldkt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jemotcldkt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jemotcldkt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jemotcldkt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jemotcldkt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jemotcldkt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jemotcldkt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jemotcldkt .gt_left { text-align: left; }
 #jemotcldkt .gt_center { text-align: center; }
 #jemotcldkt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jemotcldkt .gt_font_normal { font-weight: normal; }
 #jemotcldkt .gt_font_bold { font-weight: bold; }
 #jemotcldkt .gt_font_italic { font-style: italic; }
 #jemotcldkt .gt_super { font-size: 65%; }
 #jemotcldkt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jemotcldkt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jemotcldkt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jemotcldkt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jemotcldkt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jemotcldkt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| plain  | rich_html | rich_md  |
|--------|-----------|----------|
| x & y  | **bold**  | **bold** |
| a \< b | *italic*  | *italic* |


In the table above, the `plain` column values are automatically escaped (e.g., `&` becomes `&`), while the `rich_html` and `rich_md` column values are rendered as HTML because they were processed through [fmt()](../reference/GT.fmt.md#great_tables.GT.fmt) with the [html()](../reference/html.md#great_tables.html) and [md()](../reference/md.md#great_tables.md) helpers respectively.

For finer control, [fmt_passthrough()](../reference/GT.fmt_passthrough.md#great_tables.GT.fmt_passthrough) marks cells as formatted without transforming their values. By default it escapes special characters (just like unformatted cells), but you can set `escape=False` to pass values through as raw HTML. It also accepts a `pattern=` argument for decorating values:


``` python
df = pd.DataFrame({
    "safe_text": ["x & y", "a < b"],
    "raw_html": ["<b>bold</b>", "<em>italic</em>"],
    "decorated": ["ABC", "DEF"],
})

(
    GT(df)
    .fmt_passthrough(columns="safe_text")
    .fmt_passthrough(columns="raw_html", escape=False)
    .fmt_passthrough(columns="decorated", pattern="[{x}]")
)
```


<style>
#coswsfdghb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#coswsfdghb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#coswsfdghb p { margin: 0; padding: 0; }
 #coswsfdghb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #coswsfdghb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #coswsfdghb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #coswsfdghb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #coswsfdghb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #coswsfdghb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #coswsfdghb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #coswsfdghb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #coswsfdghb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #coswsfdghb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #coswsfdghb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #coswsfdghb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #coswsfdghb .gt_spanner_row { border-bottom-style: hidden; }
 #coswsfdghb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #coswsfdghb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #coswsfdghb .gt_from_md> :first-child { margin-top: 0; }
 #coswsfdghb .gt_from_md> :last-child { margin-bottom: 0; }
 #coswsfdghb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #coswsfdghb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #coswsfdghb .gt_indent_1 { text-indent: 5px; }
 #coswsfdghb .gt_indent_2 { text-indent: calc(5px * 2); }
 #coswsfdghb .gt_indent_3 { text-indent: calc(5px * 3); }
 #coswsfdghb .gt_indent_4 { text-indent: calc(5px * 4); }
 #coswsfdghb .gt_indent_5 { text-indent: calc(5px * 5); }
 #coswsfdghb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #coswsfdghb .gt_row_group_first td { border-top-width: 2px; }
 #coswsfdghb .gt_row_group_first th { border-top-width: 2px; }
 #coswsfdghb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #coswsfdghb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #coswsfdghb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #coswsfdghb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #coswsfdghb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #coswsfdghb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #coswsfdghb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #coswsfdghb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #coswsfdghb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #coswsfdghb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #coswsfdghb .gt_left { text-align: left; }
 #coswsfdghb .gt_center { text-align: center; }
 #coswsfdghb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #coswsfdghb .gt_font_normal { font-weight: normal; }
 #coswsfdghb .gt_font_bold { font-weight: bold; }
 #coswsfdghb .gt_font_italic { font-style: italic; }
 #coswsfdghb .gt_super { font-size: 65%; }
 #coswsfdghb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #coswsfdghb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #coswsfdghb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #coswsfdghb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #coswsfdghb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #coswsfdghb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| safe_text | raw_html | decorated |
|-----------|----------|-----------|
| x & y     | **bold** | \[ABC\]   |
| a \< b    | *italic* | \[DEF\]   |


The same escaping applies to group labels and summary row labels. Column headers, titles, footnotes, and source notes were already escaped in prior versions.


# Conclusion

Formatting is one of the most impactful things you can do to improve a table's readability. With the `fmt_*()` methods on a [GT](../reference/GT.md#great_tables.GT) object and the corresponding functions in the `vals` module, you have a comprehensive toolkit for turning raw values into polished, publication-ready content.
