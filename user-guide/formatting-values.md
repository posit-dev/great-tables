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
#fxoxjofzsv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fxoxjofzsv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fxoxjofzsv p { margin: 0; padding: 0; }
 #fxoxjofzsv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fxoxjofzsv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fxoxjofzsv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fxoxjofzsv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fxoxjofzsv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fxoxjofzsv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fxoxjofzsv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fxoxjofzsv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fxoxjofzsv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fxoxjofzsv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fxoxjofzsv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fxoxjofzsv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fxoxjofzsv .gt_spanner_row { border-bottom-style: hidden; }
 #fxoxjofzsv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fxoxjofzsv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fxoxjofzsv .gt_from_md> :first-child { margin-top: 0; }
 #fxoxjofzsv .gt_from_md> :last-child { margin-bottom: 0; }
 #fxoxjofzsv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fxoxjofzsv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fxoxjofzsv .gt_indent_1 { text-indent: 5px; }
 #fxoxjofzsv .gt_indent_2 { text-indent: calc(5px * 2); }
 #fxoxjofzsv .gt_indent_3 { text-indent: calc(5px * 3); }
 #fxoxjofzsv .gt_indent_4 { text-indent: calc(5px * 4); }
 #fxoxjofzsv .gt_indent_5 { text-indent: calc(5px * 5); }
 #fxoxjofzsv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fxoxjofzsv .gt_row_group_first td { border-top-width: 2px; }
 #fxoxjofzsv .gt_row_group_first th { border-top-width: 2px; }
 #fxoxjofzsv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fxoxjofzsv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fxoxjofzsv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fxoxjofzsv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fxoxjofzsv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fxoxjofzsv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fxoxjofzsv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fxoxjofzsv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fxoxjofzsv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fxoxjofzsv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fxoxjofzsv .gt_left { text-align: left; }
 #fxoxjofzsv .gt_center { text-align: center; }
 #fxoxjofzsv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fxoxjofzsv .gt_font_normal { font-weight: normal; }
 #fxoxjofzsv .gt_font_bold { font-weight: bold; }
 #fxoxjofzsv .gt_font_italic { font-style: italic; }
 #fxoxjofzsv .gt_super { font-size: 65%; }
 #fxoxjofzsv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fxoxjofzsv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fxoxjofzsv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fxoxjofzsv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fxoxjofzsv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fxoxjofzsv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bhdbzxvdno table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bhdbzxvdno thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bhdbzxvdno p { margin: 0; padding: 0; }
 #bhdbzxvdno .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bhdbzxvdno .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bhdbzxvdno .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bhdbzxvdno .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bhdbzxvdno .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhdbzxvdno .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhdbzxvdno .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhdbzxvdno .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bhdbzxvdno .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bhdbzxvdno .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bhdbzxvdno .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bhdbzxvdno .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bhdbzxvdno .gt_spanner_row { border-bottom-style: hidden; }
 #bhdbzxvdno .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bhdbzxvdno .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bhdbzxvdno .gt_from_md> :first-child { margin-top: 0; }
 #bhdbzxvdno .gt_from_md> :last-child { margin-bottom: 0; }
 #bhdbzxvdno .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bhdbzxvdno .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bhdbzxvdno .gt_indent_1 { text-indent: 5px; }
 #bhdbzxvdno .gt_indent_2 { text-indent: calc(5px * 2); }
 #bhdbzxvdno .gt_indent_3 { text-indent: calc(5px * 3); }
 #bhdbzxvdno .gt_indent_4 { text-indent: calc(5px * 4); }
 #bhdbzxvdno .gt_indent_5 { text-indent: calc(5px * 5); }
 #bhdbzxvdno .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bhdbzxvdno .gt_row_group_first td { border-top-width: 2px; }
 #bhdbzxvdno .gt_row_group_first th { border-top-width: 2px; }
 #bhdbzxvdno .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bhdbzxvdno .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhdbzxvdno .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhdbzxvdno .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bhdbzxvdno .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhdbzxvdno .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhdbzxvdno .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bhdbzxvdno .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bhdbzxvdno .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhdbzxvdno .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhdbzxvdno .gt_left { text-align: left; }
 #bhdbzxvdno .gt_center { text-align: center; }
 #bhdbzxvdno .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bhdbzxvdno .gt_font_normal { font-weight: normal; }
 #bhdbzxvdno .gt_font_bold { font-weight: bold; }
 #bhdbzxvdno .gt_font_italic { font-style: italic; }
 #bhdbzxvdno .gt_super { font-size: 65%; }
 #bhdbzxvdno .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhdbzxvdno .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bhdbzxvdno .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhdbzxvdno .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhdbzxvdno .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bhdbzxvdno .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ohqwoetiif table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ohqwoetiif thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ohqwoetiif p { margin: 0; padding: 0; }
 #ohqwoetiif .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ohqwoetiif .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ohqwoetiif .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ohqwoetiif .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ohqwoetiif .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ohqwoetiif .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ohqwoetiif .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ohqwoetiif .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ohqwoetiif .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ohqwoetiif .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ohqwoetiif .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ohqwoetiif .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ohqwoetiif .gt_spanner_row { border-bottom-style: hidden; }
 #ohqwoetiif .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ohqwoetiif .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ohqwoetiif .gt_from_md> :first-child { margin-top: 0; }
 #ohqwoetiif .gt_from_md> :last-child { margin-bottom: 0; }
 #ohqwoetiif .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ohqwoetiif .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ohqwoetiif .gt_indent_1 { text-indent: 5px; }
 #ohqwoetiif .gt_indent_2 { text-indent: calc(5px * 2); }
 #ohqwoetiif .gt_indent_3 { text-indent: calc(5px * 3); }
 #ohqwoetiif .gt_indent_4 { text-indent: calc(5px * 4); }
 #ohqwoetiif .gt_indent_5 { text-indent: calc(5px * 5); }
 #ohqwoetiif .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ohqwoetiif .gt_row_group_first td { border-top-width: 2px; }
 #ohqwoetiif .gt_row_group_first th { border-top-width: 2px; }
 #ohqwoetiif .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ohqwoetiif .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ohqwoetiif .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ohqwoetiif .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ohqwoetiif .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ohqwoetiif .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ohqwoetiif .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ohqwoetiif .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ohqwoetiif .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ohqwoetiif .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ohqwoetiif .gt_left { text-align: left; }
 #ohqwoetiif .gt_center { text-align: center; }
 #ohqwoetiif .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ohqwoetiif .gt_font_normal { font-weight: normal; }
 #ohqwoetiif .gt_font_bold { font-weight: bold; }
 #ohqwoetiif .gt_font_italic { font-style: italic; }
 #ohqwoetiif .gt_super { font-size: 65%; }
 #ohqwoetiif .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ohqwoetiif .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ohqwoetiif .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ohqwoetiif .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ohqwoetiif .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ohqwoetiif .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tgollwmxnj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tgollwmxnj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tgollwmxnj p { margin: 0; padding: 0; }
 #tgollwmxnj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tgollwmxnj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tgollwmxnj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tgollwmxnj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tgollwmxnj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tgollwmxnj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgollwmxnj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tgollwmxnj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tgollwmxnj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tgollwmxnj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tgollwmxnj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tgollwmxnj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tgollwmxnj .gt_spanner_row { border-bottom-style: hidden; }
 #tgollwmxnj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tgollwmxnj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tgollwmxnj .gt_from_md> :first-child { margin-top: 0; }
 #tgollwmxnj .gt_from_md> :last-child { margin-bottom: 0; }
 #tgollwmxnj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tgollwmxnj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tgollwmxnj .gt_indent_1 { text-indent: 5px; }
 #tgollwmxnj .gt_indent_2 { text-indent: calc(5px * 2); }
 #tgollwmxnj .gt_indent_3 { text-indent: calc(5px * 3); }
 #tgollwmxnj .gt_indent_4 { text-indent: calc(5px * 4); }
 #tgollwmxnj .gt_indent_5 { text-indent: calc(5px * 5); }
 #tgollwmxnj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tgollwmxnj .gt_row_group_first td { border-top-width: 2px; }
 #tgollwmxnj .gt_row_group_first th { border-top-width: 2px; }
 #tgollwmxnj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tgollwmxnj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgollwmxnj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tgollwmxnj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tgollwmxnj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgollwmxnj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tgollwmxnj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tgollwmxnj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tgollwmxnj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgollwmxnj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tgollwmxnj .gt_left { text-align: left; }
 #tgollwmxnj .gt_center { text-align: center; }
 #tgollwmxnj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tgollwmxnj .gt_font_normal { font-weight: normal; }
 #tgollwmxnj .gt_font_bold { font-weight: bold; }
 #tgollwmxnj .gt_font_italic { font-style: italic; }
 #tgollwmxnj .gt_super { font-size: 65%; }
 #tgollwmxnj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgollwmxnj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tgollwmxnj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgollwmxnj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tgollwmxnj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tgollwmxnj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#niiouwvuzb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#niiouwvuzb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#niiouwvuzb p { margin: 0; padding: 0; }
 #niiouwvuzb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #niiouwvuzb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #niiouwvuzb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #niiouwvuzb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #niiouwvuzb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #niiouwvuzb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #niiouwvuzb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #niiouwvuzb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #niiouwvuzb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #niiouwvuzb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #niiouwvuzb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #niiouwvuzb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #niiouwvuzb .gt_spanner_row { border-bottom-style: hidden; }
 #niiouwvuzb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #niiouwvuzb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #niiouwvuzb .gt_from_md> :first-child { margin-top: 0; }
 #niiouwvuzb .gt_from_md> :last-child { margin-bottom: 0; }
 #niiouwvuzb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #niiouwvuzb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #niiouwvuzb .gt_indent_1 { text-indent: 5px; }
 #niiouwvuzb .gt_indent_2 { text-indent: calc(5px * 2); }
 #niiouwvuzb .gt_indent_3 { text-indent: calc(5px * 3); }
 #niiouwvuzb .gt_indent_4 { text-indent: calc(5px * 4); }
 #niiouwvuzb .gt_indent_5 { text-indent: calc(5px * 5); }
 #niiouwvuzb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #niiouwvuzb .gt_row_group_first td { border-top-width: 2px; }
 #niiouwvuzb .gt_row_group_first th { border-top-width: 2px; }
 #niiouwvuzb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #niiouwvuzb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #niiouwvuzb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #niiouwvuzb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #niiouwvuzb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #niiouwvuzb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #niiouwvuzb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #niiouwvuzb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #niiouwvuzb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #niiouwvuzb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #niiouwvuzb .gt_left { text-align: left; }
 #niiouwvuzb .gt_center { text-align: center; }
 #niiouwvuzb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #niiouwvuzb .gt_font_normal { font-weight: normal; }
 #niiouwvuzb .gt_font_bold { font-weight: bold; }
 #niiouwvuzb .gt_font_italic { font-style: italic; }
 #niiouwvuzb .gt_super { font-size: 65%; }
 #niiouwvuzb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #niiouwvuzb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #niiouwvuzb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #niiouwvuzb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #niiouwvuzb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #niiouwvuzb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ejhcrufzon table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ejhcrufzon thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ejhcrufzon p { margin: 0; padding: 0; }
 #ejhcrufzon .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ejhcrufzon .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ejhcrufzon .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ejhcrufzon .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ejhcrufzon .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ejhcrufzon .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ejhcrufzon .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ejhcrufzon .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ejhcrufzon .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ejhcrufzon .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ejhcrufzon .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ejhcrufzon .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ejhcrufzon .gt_spanner_row { border-bottom-style: hidden; }
 #ejhcrufzon .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ejhcrufzon .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ejhcrufzon .gt_from_md> :first-child { margin-top: 0; }
 #ejhcrufzon .gt_from_md> :last-child { margin-bottom: 0; }
 #ejhcrufzon .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ejhcrufzon .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ejhcrufzon .gt_indent_1 { text-indent: 5px; }
 #ejhcrufzon .gt_indent_2 { text-indent: calc(5px * 2); }
 #ejhcrufzon .gt_indent_3 { text-indent: calc(5px * 3); }
 #ejhcrufzon .gt_indent_4 { text-indent: calc(5px * 4); }
 #ejhcrufzon .gt_indent_5 { text-indent: calc(5px * 5); }
 #ejhcrufzon .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ejhcrufzon .gt_row_group_first td { border-top-width: 2px; }
 #ejhcrufzon .gt_row_group_first th { border-top-width: 2px; }
 #ejhcrufzon .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ejhcrufzon .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ejhcrufzon .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ejhcrufzon .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ejhcrufzon .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ejhcrufzon .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ejhcrufzon .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ejhcrufzon .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ejhcrufzon .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ejhcrufzon .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ejhcrufzon .gt_left { text-align: left; }
 #ejhcrufzon .gt_center { text-align: center; }
 #ejhcrufzon .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ejhcrufzon .gt_font_normal { font-weight: normal; }
 #ejhcrufzon .gt_font_bold { font-weight: bold; }
 #ejhcrufzon .gt_font_italic { font-style: italic; }
 #ejhcrufzon .gt_super { font-size: 65%; }
 #ejhcrufzon .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ejhcrufzon .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ejhcrufzon .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ejhcrufzon .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ejhcrufzon .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ejhcrufzon .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sstkhjtwae table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sstkhjtwae thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sstkhjtwae p { margin: 0; padding: 0; }
 #sstkhjtwae .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sstkhjtwae .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sstkhjtwae .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sstkhjtwae .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sstkhjtwae .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sstkhjtwae .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sstkhjtwae .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sstkhjtwae .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sstkhjtwae .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sstkhjtwae .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sstkhjtwae .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sstkhjtwae .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sstkhjtwae .gt_spanner_row { border-bottom-style: hidden; }
 #sstkhjtwae .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sstkhjtwae .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sstkhjtwae .gt_from_md> :first-child { margin-top: 0; }
 #sstkhjtwae .gt_from_md> :last-child { margin-bottom: 0; }
 #sstkhjtwae .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sstkhjtwae .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sstkhjtwae .gt_indent_1 { text-indent: 5px; }
 #sstkhjtwae .gt_indent_2 { text-indent: calc(5px * 2); }
 #sstkhjtwae .gt_indent_3 { text-indent: calc(5px * 3); }
 #sstkhjtwae .gt_indent_4 { text-indent: calc(5px * 4); }
 #sstkhjtwae .gt_indent_5 { text-indent: calc(5px * 5); }
 #sstkhjtwae .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sstkhjtwae .gt_row_group_first td { border-top-width: 2px; }
 #sstkhjtwae .gt_row_group_first th { border-top-width: 2px; }
 #sstkhjtwae .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sstkhjtwae .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sstkhjtwae .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sstkhjtwae .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sstkhjtwae .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sstkhjtwae .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sstkhjtwae .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sstkhjtwae .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sstkhjtwae .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sstkhjtwae .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sstkhjtwae .gt_left { text-align: left; }
 #sstkhjtwae .gt_center { text-align: center; }
 #sstkhjtwae .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sstkhjtwae .gt_font_normal { font-weight: normal; }
 #sstkhjtwae .gt_font_bold { font-weight: bold; }
 #sstkhjtwae .gt_font_italic { font-style: italic; }
 #sstkhjtwae .gt_super { font-size: 65%; }
 #sstkhjtwae .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sstkhjtwae .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sstkhjtwae .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sstkhjtwae .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sstkhjtwae .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sstkhjtwae .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| safe_text | raw_html | decorated |
|-----------|----------|-----------|
| x & y     | **bold** | \[ABC\]   |
| a \< b    | *italic* | \[DEF\]   |


The same escaping applies to group labels and summary row labels. Column headers, titles, footnotes, and source notes were already escaped in prior versions.


# Conclusion

Formatting is one of the most impactful things you can do to improve a table's readability. With the `fmt_*()` methods on a [GT](../reference/GT.md#great_tables.GT) object and the corresponding functions in the `vals` module, you have a comprehensive toolkit for turning raw values into polished, publication-ready content.
