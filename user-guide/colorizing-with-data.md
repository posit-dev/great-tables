# Colorizing with Data

You sometimes come across heat maps in data visualization, and they're used to represent data values with color gradients. This technique is great for identifying patterns, trends, outliers, and missing data when there's lots of data. Tables can have this sort of treatment as well! Typically, formatted numeric values are shown along with some color treatment coinciding with the underlying data values.

Data coloring works best when you want readers to spot patterns across many values at once (e.g., trends over time, outliers, relative magnitude, etc.). For tables with just a few rows, explicit formatting or footnotes may be more effective since the reader can take in all the values directly. But when a table has dozens or hundreds of cells, color provides a visual shortcut that no amount of bold or italics can match.

We can make this possible in **Great Tables** by using the [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) method. Let's start with a simple example, using a Polars DataFrame with three columns of values. We can introduce that data to [GT](../reference/GT.md#great_tables.GT) and use [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) without any arguments.


``` python
from great_tables import GT
import polars as pl

simple_df = pl.DataFrame(
    {
        "integer": [1, 2, 3, 4, 5],
        "float": [2.3, 1.3, 5.1, None, 4.4],
        "category": ["one", "two", "three", "one", "three"],
    }
)

GT(simple_df).data_color()
```


<style>
#vxxgbgvois table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vxxgbgvois thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vxxgbgvois p { margin: 0; padding: 0; }
 #vxxgbgvois .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vxxgbgvois .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vxxgbgvois .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vxxgbgvois .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vxxgbgvois .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vxxgbgvois .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vxxgbgvois .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vxxgbgvois .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vxxgbgvois .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vxxgbgvois .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vxxgbgvois .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vxxgbgvois .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vxxgbgvois .gt_spanner_row { border-bottom-style: hidden; }
 #vxxgbgvois .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vxxgbgvois .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vxxgbgvois .gt_from_md> :first-child { margin-top: 0; }
 #vxxgbgvois .gt_from_md> :last-child { margin-bottom: 0; }
 #vxxgbgvois .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vxxgbgvois .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vxxgbgvois .gt_indent_1 { text-indent: 5px; }
 #vxxgbgvois .gt_indent_2 { text-indent: calc(5px * 2); }
 #vxxgbgvois .gt_indent_3 { text-indent: calc(5px * 3); }
 #vxxgbgvois .gt_indent_4 { text-indent: calc(5px * 4); }
 #vxxgbgvois .gt_indent_5 { text-indent: calc(5px * 5); }
 #vxxgbgvois .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vxxgbgvois .gt_row_group_first td { border-top-width: 2px; }
 #vxxgbgvois .gt_row_group_first th { border-top-width: 2px; }
 #vxxgbgvois .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vxxgbgvois .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vxxgbgvois .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vxxgbgvois .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vxxgbgvois .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vxxgbgvois .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vxxgbgvois .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vxxgbgvois .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vxxgbgvois .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vxxgbgvois .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vxxgbgvois .gt_left { text-align: left; }
 #vxxgbgvois .gt_center { text-align: center; }
 #vxxgbgvois .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vxxgbgvois .gt_font_normal { font-weight: normal; }
 #vxxgbgvois .gt_font_bold { font-weight: bold; }
 #vxxgbgvois .gt_font_italic { font-style: italic; }
 #vxxgbgvois .gt_super { font-size: 65%; }
 #vxxgbgvois .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vxxgbgvois .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vxxgbgvois .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vxxgbgvois .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vxxgbgvois .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vxxgbgvois .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| integer | float | category |
|---------|-------|----------|
| 1       | 2.3   | one      |
| 2       | 1.3   | two      |
| 3       | 5.1   | three    |
| 4       | None  | one      |
| 5       | 4.4   | three    |


This works but doesn't look all too appealing. However, we can take note of a few things straight away. The first thing is that [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) doesn't format the values but rather it applies color fill values to the cells. The second thing is that you don't have to intervene and modify the text color so that there's enough contrast, **Great Tables** will do that for you (this behavior *can* be deactivated with the `autocolor_text=` argument though).


# Setting palette colors

While this first example illustrated some basic things, the common thing to do in practices to provide a list of colors to the `palette=` argument. Let's choose two colors `"green"` and `"red"` and place them in that order.


``` python
GT(simple_df).data_color(palette=["blue", "red"])
```


<style>
#epgmvgvwqx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#epgmvgvwqx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#epgmvgvwqx p { margin: 0; padding: 0; }
 #epgmvgvwqx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #epgmvgvwqx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #epgmvgvwqx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #epgmvgvwqx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #epgmvgvwqx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epgmvgvwqx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epgmvgvwqx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epgmvgvwqx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #epgmvgvwqx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #epgmvgvwqx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #epgmvgvwqx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #epgmvgvwqx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #epgmvgvwqx .gt_spanner_row { border-bottom-style: hidden; }
 #epgmvgvwqx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #epgmvgvwqx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #epgmvgvwqx .gt_from_md> :first-child { margin-top: 0; }
 #epgmvgvwqx .gt_from_md> :last-child { margin-bottom: 0; }
 #epgmvgvwqx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #epgmvgvwqx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #epgmvgvwqx .gt_indent_1 { text-indent: 5px; }
 #epgmvgvwqx .gt_indent_2 { text-indent: calc(5px * 2); }
 #epgmvgvwqx .gt_indent_3 { text-indent: calc(5px * 3); }
 #epgmvgvwqx .gt_indent_4 { text-indent: calc(5px * 4); }
 #epgmvgvwqx .gt_indent_5 { text-indent: calc(5px * 5); }
 #epgmvgvwqx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #epgmvgvwqx .gt_row_group_first td { border-top-width: 2px; }
 #epgmvgvwqx .gt_row_group_first th { border-top-width: 2px; }
 #epgmvgvwqx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #epgmvgvwqx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epgmvgvwqx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #epgmvgvwqx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #epgmvgvwqx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epgmvgvwqx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #epgmvgvwqx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #epgmvgvwqx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #epgmvgvwqx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epgmvgvwqx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #epgmvgvwqx .gt_left { text-align: left; }
 #epgmvgvwqx .gt_center { text-align: center; }
 #epgmvgvwqx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #epgmvgvwqx .gt_font_normal { font-weight: normal; }
 #epgmvgvwqx .gt_font_bold { font-weight: bold; }
 #epgmvgvwqx .gt_font_italic { font-style: italic; }
 #epgmvgvwqx .gt_super { font-size: 65%; }
 #epgmvgvwqx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epgmvgvwqx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #epgmvgvwqx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epgmvgvwqx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #epgmvgvwqx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #epgmvgvwqx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| integer | float | category |
|---------|-------|----------|
| 1       | 2.3   | one      |
| 2       | 1.3   | two      |
| 3       | 5.1   | three    |
| 4       | None  | one      |
| 5       | 4.4   | three    |


Now that we've moved away from the default palette and specified colors, we can see that lower numerical values are closer to blue and higher values are closer to red (those in the middle have colors that are a blend of the two and, in this case, more in the purple range). Categorical values behave similarly, they take on ordinal values based on their first appearance (from top to bottom) and those values are used to generate the background colors.

When choosing palette colors, consider the nature of your data. For sequential data (low to high), use a single-hue gradient or a well-known sequential palette. For diverging data (values above and below a midpoint), use a diverging palette with a neutral middle color. Avoid using red-green combinations, which are difficult for colorblind readers (blue-orange or purple-green are safer alternatives).


# Coloring missing values with `na_color`

There is a lone `"None"` value in the `float` column, and it has a gray background. Throughout the **Great Tables** package, missing values are treated in different ways and, in this case, it's given a default color value. We can change that with the `na_color=` argument. Let's try it now:


``` python
GT(simple_df).data_color(palette=["blue", "red"], na_color="#FFE4C4")
```


<style>
#upmqfhxtgg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#upmqfhxtgg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#upmqfhxtgg p { margin: 0; padding: 0; }
 #upmqfhxtgg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #upmqfhxtgg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #upmqfhxtgg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #upmqfhxtgg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #upmqfhxtgg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #upmqfhxtgg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #upmqfhxtgg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #upmqfhxtgg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #upmqfhxtgg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #upmqfhxtgg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #upmqfhxtgg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #upmqfhxtgg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #upmqfhxtgg .gt_spanner_row { border-bottom-style: hidden; }
 #upmqfhxtgg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #upmqfhxtgg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #upmqfhxtgg .gt_from_md> :first-child { margin-top: 0; }
 #upmqfhxtgg .gt_from_md> :last-child { margin-bottom: 0; }
 #upmqfhxtgg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #upmqfhxtgg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #upmqfhxtgg .gt_indent_1 { text-indent: 5px; }
 #upmqfhxtgg .gt_indent_2 { text-indent: calc(5px * 2); }
 #upmqfhxtgg .gt_indent_3 { text-indent: calc(5px * 3); }
 #upmqfhxtgg .gt_indent_4 { text-indent: calc(5px * 4); }
 #upmqfhxtgg .gt_indent_5 { text-indent: calc(5px * 5); }
 #upmqfhxtgg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #upmqfhxtgg .gt_row_group_first td { border-top-width: 2px; }
 #upmqfhxtgg .gt_row_group_first th { border-top-width: 2px; }
 #upmqfhxtgg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #upmqfhxtgg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #upmqfhxtgg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #upmqfhxtgg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #upmqfhxtgg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #upmqfhxtgg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #upmqfhxtgg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #upmqfhxtgg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #upmqfhxtgg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #upmqfhxtgg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #upmqfhxtgg .gt_left { text-align: left; }
 #upmqfhxtgg .gt_center { text-align: center; }
 #upmqfhxtgg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #upmqfhxtgg .gt_font_normal { font-weight: normal; }
 #upmqfhxtgg .gt_font_bold { font-weight: bold; }
 #upmqfhxtgg .gt_font_italic { font-style: italic; }
 #upmqfhxtgg .gt_super { font-size: 65%; }
 #upmqfhxtgg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #upmqfhxtgg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #upmqfhxtgg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #upmqfhxtgg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #upmqfhxtgg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #upmqfhxtgg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| integer | float | category |
|---------|-------|----------|
| 1       | 2.3   | one      |
| 2       | 1.3   | two      |
| 3       | 5.1   | three    |
| 4       | None  | one      |
| 5       | 4.4   | three    |


Now, the gray color has been changed to Bisque. Note that when it comes to colors, you can use any combination of CSS/X11 color names and hexadecimal color codes.


# Using `domain=` to color values across columns

The previous usages of the [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) method were such that the color ranges encompassed the boundaries of the data values. That can be changed with the `domain=` argument, which expects a list of two values (a lower and an upper value). Let's use the range `[0, 10]` on the first two columns, `integer` and `float`, and not the third (since a numerical domain is incompatible with string-based values). Here's the table code for that:


``` python
(
    GT(simple_df)
    .data_color(
        columns=["integer", "float"],
        palette=["blue", "red"],
        domain=[0, 10],
        na_color="white"
    )
)
```


<style>
#knjypffixz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#knjypffixz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#knjypffixz p { margin: 0; padding: 0; }
 #knjypffixz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #knjypffixz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #knjypffixz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #knjypffixz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #knjypffixz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #knjypffixz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #knjypffixz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #knjypffixz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #knjypffixz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #knjypffixz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #knjypffixz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #knjypffixz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #knjypffixz .gt_spanner_row { border-bottom-style: hidden; }
 #knjypffixz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #knjypffixz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #knjypffixz .gt_from_md> :first-child { margin-top: 0; }
 #knjypffixz .gt_from_md> :last-child { margin-bottom: 0; }
 #knjypffixz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #knjypffixz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #knjypffixz .gt_indent_1 { text-indent: 5px; }
 #knjypffixz .gt_indent_2 { text-indent: calc(5px * 2); }
 #knjypffixz .gt_indent_3 { text-indent: calc(5px * 3); }
 #knjypffixz .gt_indent_4 { text-indent: calc(5px * 4); }
 #knjypffixz .gt_indent_5 { text-indent: calc(5px * 5); }
 #knjypffixz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #knjypffixz .gt_row_group_first td { border-top-width: 2px; }
 #knjypffixz .gt_row_group_first th { border-top-width: 2px; }
 #knjypffixz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #knjypffixz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #knjypffixz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #knjypffixz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #knjypffixz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #knjypffixz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #knjypffixz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #knjypffixz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #knjypffixz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #knjypffixz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #knjypffixz .gt_left { text-align: left; }
 #knjypffixz .gt_center { text-align: center; }
 #knjypffixz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #knjypffixz .gt_font_normal { font-weight: normal; }
 #knjypffixz .gt_font_bold { font-weight: bold; }
 #knjypffixz .gt_font_italic { font-style: italic; }
 #knjypffixz .gt_super { font-size: 65%; }
 #knjypffixz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #knjypffixz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #knjypffixz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #knjypffixz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #knjypffixz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #knjypffixz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| integer | float | category |
|---------|-------|----------|
| 1       | 2.3   | one      |
| 2       | 1.3   | two      |
| 3       | 5.1   | three    |
| 4       | None  | one      |
| 5       | 4.4   | three    |


Nice! We can clearly see that the color ramp in the first column (`integer`) only proceeds from blue (value: `1`) to purple (value: `5`) and there isn't a reddish color in sight (would need a value close to 10).

Setting an explicit domain matters because without one, each column scales independently (the same color can represent different values in different columns). By setting a shared domain, you ensure that colors are comparable across columns, which is critical when columns measure the same quantity. In this example, both `integer` and `float` use the `[0, 10]` range, so a given shade of purple means the same thing regardless of which column it appears in.


# Centering colors with `midpoint=`

Some values have a natural center: changes are centered on zero, ratios on one, and scores on some target. For these, a diverging palette (two colors with a neutral one in between) works well, but only if the neutral color lands on that center. By default it doesn't: the middle color of the palette goes to the middle of the domain, wherever that happens to be. The `midpoint=` argument pins the center of the palette to a value of your choosing.

Here's a table of changes, some negative and some positive. With `midpoint=0`, decreases become increasingly red and increases become increasingly green, the further they are from zero:


``` python
changes_df = pl.DataFrame(
    {
        "region": ["North", "South", "East", "West", "Central"],
        "change": [12.5, -8.1, 0.0, 3.2, -1.0],
    }
)

red_white_green = ["#D7191C", "white", "#1A9641"]

(
    GT(changes_df)
    .data_color(columns="change", palette=red_white_green, midpoint=0)
    .fmt_number(columns="change", decimals=1, force_sign=True)
)
```


<style>
#fucgsssmkk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fucgsssmkk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fucgsssmkk p { margin: 0; padding: 0; }
 #fucgsssmkk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fucgsssmkk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fucgsssmkk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fucgsssmkk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fucgsssmkk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fucgsssmkk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fucgsssmkk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fucgsssmkk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fucgsssmkk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fucgsssmkk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fucgsssmkk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fucgsssmkk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fucgsssmkk .gt_spanner_row { border-bottom-style: hidden; }
 #fucgsssmkk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fucgsssmkk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fucgsssmkk .gt_from_md> :first-child { margin-top: 0; }
 #fucgsssmkk .gt_from_md> :last-child { margin-bottom: 0; }
 #fucgsssmkk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fucgsssmkk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fucgsssmkk .gt_indent_1 { text-indent: 5px; }
 #fucgsssmkk .gt_indent_2 { text-indent: calc(5px * 2); }
 #fucgsssmkk .gt_indent_3 { text-indent: calc(5px * 3); }
 #fucgsssmkk .gt_indent_4 { text-indent: calc(5px * 4); }
 #fucgsssmkk .gt_indent_5 { text-indent: calc(5px * 5); }
 #fucgsssmkk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fucgsssmkk .gt_row_group_first td { border-top-width: 2px; }
 #fucgsssmkk .gt_row_group_first th { border-top-width: 2px; }
 #fucgsssmkk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fucgsssmkk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fucgsssmkk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fucgsssmkk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fucgsssmkk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fucgsssmkk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fucgsssmkk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fucgsssmkk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fucgsssmkk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fucgsssmkk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fucgsssmkk .gt_left { text-align: left; }
 #fucgsssmkk .gt_center { text-align: center; }
 #fucgsssmkk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fucgsssmkk .gt_font_normal { font-weight: normal; }
 #fucgsssmkk .gt_font_bold { font-weight: bold; }
 #fucgsssmkk .gt_font_italic { font-style: italic; }
 #fucgsssmkk .gt_super { font-size: 65%; }
 #fucgsssmkk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fucgsssmkk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fucgsssmkk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fucgsssmkk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fucgsssmkk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fucgsssmkk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | −1.0   |


Notice that the largest decrease (`-8.1`) is a less intense red than the largest increase (`12.5`) is green. Without a `domain=`, the domain is made symmetric around the midpoint (here, it becomes `[-12.5, 12.5]`), so the strength of a color reflects how far a value is from the midpoint, the same on both sides. A change of `-12.5` would get the full red.

If you supply a `domain=` as well, then each side of the midpoint is scaled separately, from the midpoint out to its end of the domain. This is how three-color scales work in spreadsheet software. It's useful when the two sides cover ranges of different sizes. Here, sales are shown as a fraction of a target, so the midpoint is `1`. The colors go from red to white over the wide range from 50% of the target up to the target, and from white to green over the narrower range from the target up to 120% of it:


``` python
sales_df = pl.DataFrame(
    {
        "rep": ["Ana", "Ben", "Cai", "Dee", "Eli"],
        "pct_of_target": [0.62, 0.88, 1.0, 1.08, 1.17],
    }
)

(
    GT(sales_df)
    .data_color(
        columns="pct_of_target",
        palette=red_white_green,
        domain=[0.5, 1.2],
        midpoint=1,
    )
    .fmt_percent(columns="pct_of_target", decimals=0)
)
```


<style>
#zbhtcmzbkv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zbhtcmzbkv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zbhtcmzbkv p { margin: 0; padding: 0; }
 #zbhtcmzbkv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zbhtcmzbkv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zbhtcmzbkv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zbhtcmzbkv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zbhtcmzbkv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zbhtcmzbkv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zbhtcmzbkv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zbhtcmzbkv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zbhtcmzbkv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zbhtcmzbkv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zbhtcmzbkv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zbhtcmzbkv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zbhtcmzbkv .gt_spanner_row { border-bottom-style: hidden; }
 #zbhtcmzbkv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zbhtcmzbkv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zbhtcmzbkv .gt_from_md> :first-child { margin-top: 0; }
 #zbhtcmzbkv .gt_from_md> :last-child { margin-bottom: 0; }
 #zbhtcmzbkv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zbhtcmzbkv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zbhtcmzbkv .gt_indent_1 { text-indent: 5px; }
 #zbhtcmzbkv .gt_indent_2 { text-indent: calc(5px * 2); }
 #zbhtcmzbkv .gt_indent_3 { text-indent: calc(5px * 3); }
 #zbhtcmzbkv .gt_indent_4 { text-indent: calc(5px * 4); }
 #zbhtcmzbkv .gt_indent_5 { text-indent: calc(5px * 5); }
 #zbhtcmzbkv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zbhtcmzbkv .gt_row_group_first td { border-top-width: 2px; }
 #zbhtcmzbkv .gt_row_group_first th { border-top-width: 2px; }
 #zbhtcmzbkv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zbhtcmzbkv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zbhtcmzbkv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zbhtcmzbkv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zbhtcmzbkv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zbhtcmzbkv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zbhtcmzbkv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zbhtcmzbkv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zbhtcmzbkv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zbhtcmzbkv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zbhtcmzbkv .gt_left { text-align: left; }
 #zbhtcmzbkv .gt_center { text-align: center; }
 #zbhtcmzbkv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zbhtcmzbkv .gt_font_normal { font-weight: normal; }
 #zbhtcmzbkv .gt_font_bold { font-weight: bold; }
 #zbhtcmzbkv .gt_font_italic { font-style: italic; }
 #zbhtcmzbkv .gt_super { font-size: 65%; }
 #zbhtcmzbkv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zbhtcmzbkv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zbhtcmzbkv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zbhtcmzbkv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zbhtcmzbkv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zbhtcmzbkv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| rep | pct_of_target |
|-----|---------------|
| Ana | 62%           |
| Ben | 88%           |
| Cai | 100%          |
| Dee | 108%          |
| Eli | 117%          |


Both sides now use their full range of colors. `1.17` is only 0.17 above the target, but it's about as strongly green as `0.62` (more than twice as far below the target) is red. Keep in mind that this makes equal distances from the midpoint look different on each side, so the symmetric behavior is usually the more honest choice when the two sides measure the same kind of change.


# Choosing a contrast algorithm with `contrast_algo=`

We noted earlier that [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) automatically picks a light or dark text color for each cell so that values remain legible against their background fill. How that choice gets made depends on the contrast algorithm in use, and that's settable with the `contrast_algo=` argument. There are two options:

- `"apca"` (the default): the Accessible Perceptual Contrast Algorithm, which models how people actually perceive the lightness contrast of text against a background
- `"wcag"`: the contrast ratio formula from the Web Content Accessibility Guidelines (WCAG 2.x)

The two algorithms agree on very light and very dark backgrounds but they can differ on mid-tone colors. The WCAG formula is known to overstate the contrast of dark text on saturated, medium-dark backgrounds (e.g., reds and blues), so it often selects black text where white text is easier to read. APCA does a better job with these colors. To see the difference, let's color the same set of values twice, once with each algorithm:


``` python
contrast_df = pl.DataFrame(
    {
        "apca": [1, 2, 3, 4, 5, 6, 7],
        "wcag": [1, 2, 3, 4, 5, 6, 7],
    }
)

palette = ["#2C7BB6", "#ABD9E9", "#FDAE61", "#D7191C"]

(
    GT(contrast_df)
    .data_color(columns="apca", palette=palette, contrast_algo="apca")
    .data_color(columns="wcag", palette=palette, contrast_algo="wcag")
)
```


<style>
#bdmfwivguq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bdmfwivguq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bdmfwivguq p { margin: 0; padding: 0; }
 #bdmfwivguq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bdmfwivguq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bdmfwivguq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bdmfwivguq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bdmfwivguq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bdmfwivguq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bdmfwivguq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bdmfwivguq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bdmfwivguq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bdmfwivguq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bdmfwivguq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bdmfwivguq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bdmfwivguq .gt_spanner_row { border-bottom-style: hidden; }
 #bdmfwivguq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bdmfwivguq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bdmfwivguq .gt_from_md> :first-child { margin-top: 0; }
 #bdmfwivguq .gt_from_md> :last-child { margin-bottom: 0; }
 #bdmfwivguq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bdmfwivguq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bdmfwivguq .gt_indent_1 { text-indent: 5px; }
 #bdmfwivguq .gt_indent_2 { text-indent: calc(5px * 2); }
 #bdmfwivguq .gt_indent_3 { text-indent: calc(5px * 3); }
 #bdmfwivguq .gt_indent_4 { text-indent: calc(5px * 4); }
 #bdmfwivguq .gt_indent_5 { text-indent: calc(5px * 5); }
 #bdmfwivguq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bdmfwivguq .gt_row_group_first td { border-top-width: 2px; }
 #bdmfwivguq .gt_row_group_first th { border-top-width: 2px; }
 #bdmfwivguq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bdmfwivguq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bdmfwivguq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bdmfwivguq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bdmfwivguq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bdmfwivguq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bdmfwivguq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bdmfwivguq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bdmfwivguq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bdmfwivguq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bdmfwivguq .gt_left { text-align: left; }
 #bdmfwivguq .gt_center { text-align: center; }
 #bdmfwivguq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bdmfwivguq .gt_font_normal { font-weight: normal; }
 #bdmfwivguq .gt_font_bold { font-weight: bold; }
 #bdmfwivguq .gt_font_italic { font-style: italic; }
 #bdmfwivguq .gt_super { font-size: 65%; }
 #bdmfwivguq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bdmfwivguq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bdmfwivguq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bdmfwivguq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bdmfwivguq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bdmfwivguq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| apca | wcag |
|------|------|
| 1    | 1    |
| 2    | 2    |
| 3    | 3    |
| 4    | 4    |
| 5    | 5    |
| 6    | 6    |
| 7    | 7    |


Both columns have identical background colors, but the blue and red-orange cells get white text under APCA and black text under WCAG. The APCA choices are noticeably more legible for those cells. If you need to match the WCAG 2.x guidelines for compliance reasons, then use `contrast_algo="wcag"`. Otherwise, the default of `"apca"` is the better choice for readability.


# Custom color mapping with `fn=`

A palette spread across a domain covers many needs, but sometimes the rules for coloring are more specific: a color for every value above a threshold, different colors for positive and negative values, or a fixed color for each category. For these cases, [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) accepts a color-mapping function through its `fn=` argument.

The function is called once for each targeted column. It receives a list of that column's values and must return a list of colors of the same length. Here's a function that colors values in the `float` column according to whether they're below or above `3`:


``` python
def above_below_3(vals):
    return [None if x is None else "lightblue" if x < 3 else "orange" for x in vals]

GT(simple_df).data_color(columns="float", fn=above_below_3, na_color="lightgray")
```


<style>
#faguxmosjf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#faguxmosjf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#faguxmosjf p { margin: 0; padding: 0; }
 #faguxmosjf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #faguxmosjf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #faguxmosjf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #faguxmosjf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #faguxmosjf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #faguxmosjf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #faguxmosjf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #faguxmosjf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #faguxmosjf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #faguxmosjf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #faguxmosjf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #faguxmosjf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #faguxmosjf .gt_spanner_row { border-bottom-style: hidden; }
 #faguxmosjf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #faguxmosjf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #faguxmosjf .gt_from_md> :first-child { margin-top: 0; }
 #faguxmosjf .gt_from_md> :last-child { margin-bottom: 0; }
 #faguxmosjf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #faguxmosjf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #faguxmosjf .gt_indent_1 { text-indent: 5px; }
 #faguxmosjf .gt_indent_2 { text-indent: calc(5px * 2); }
 #faguxmosjf .gt_indent_3 { text-indent: calc(5px * 3); }
 #faguxmosjf .gt_indent_4 { text-indent: calc(5px * 4); }
 #faguxmosjf .gt_indent_5 { text-indent: calc(5px * 5); }
 #faguxmosjf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #faguxmosjf .gt_row_group_first td { border-top-width: 2px; }
 #faguxmosjf .gt_row_group_first th { border-top-width: 2px; }
 #faguxmosjf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #faguxmosjf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #faguxmosjf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #faguxmosjf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #faguxmosjf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #faguxmosjf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #faguxmosjf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #faguxmosjf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #faguxmosjf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #faguxmosjf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #faguxmosjf .gt_left { text-align: left; }
 #faguxmosjf .gt_center { text-align: center; }
 #faguxmosjf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #faguxmosjf .gt_font_normal { font-weight: normal; }
 #faguxmosjf .gt_font_bold { font-weight: bold; }
 #faguxmosjf .gt_font_italic { font-style: italic; }
 #faguxmosjf .gt_super { font-size: 65%; }
 #faguxmosjf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #faguxmosjf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #faguxmosjf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #faguxmosjf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #faguxmosjf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #faguxmosjf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| integer | float | category |
|---------|-------|----------|
| 1       | 2.3   | one      |
| 2       | 1.3   | two      |
| 3       | 5.1   | three    |
| 4       | None  | one      |
| 5       | 4.4   | three    |


There are a few things to know about how this works:

- **Missing values are passed to the function.** In a Polars DataFrame they arrive as `None` (with pandas, they usually arrive as `NaN`, and `pd.isna()` is a reliable way to check for missing values from either library). The function needs to handle them, or a comparison like `x < 3` will fail.
- **Returning `None` gives the `na_color=` color.** That's what happened to the missing value above. It's also a handy way to leave out any value you'd rather not color.
- **Some arguments step aside.** The `palette=`, `domain=`, `reverse=`, `truncate=`, and `midpoint=` arguments are ignored when `fn=` is used, since the function takes over their job. The `na_color=`, `alpha=`, and `autocolor_text=` arguments still apply, so text is automatically recolored for contrast as usual.
- **Any column type works.** The function decides what the values mean, so you can color columns that the built-in mapping can't handle, such as booleans.

Here's that last point in action, with a column of booleans and a translucent fill (through `alpha=`):


``` python
tasks_df = pl.DataFrame(
    {
        "task": ["Build", "Test", "Docs", "Release"],
        "done": [True, True, False, None],
    }
)

GT(tasks_df).data_color(
    columns="done",
    fn=lambda vals: [None if v is None else "seagreen" if v else "firebrick" for v in vals],
    na_color="#FFF3B0",
    alpha=0.6,
)
```


<style>
#xhfoeiimik table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xhfoeiimik thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xhfoeiimik p { margin: 0; padding: 0; }
 #xhfoeiimik .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xhfoeiimik .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xhfoeiimik .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xhfoeiimik .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xhfoeiimik .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xhfoeiimik .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xhfoeiimik .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xhfoeiimik .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xhfoeiimik .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xhfoeiimik .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xhfoeiimik .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xhfoeiimik .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xhfoeiimik .gt_spanner_row { border-bottom-style: hidden; }
 #xhfoeiimik .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xhfoeiimik .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xhfoeiimik .gt_from_md> :first-child { margin-top: 0; }
 #xhfoeiimik .gt_from_md> :last-child { margin-bottom: 0; }
 #xhfoeiimik .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xhfoeiimik .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xhfoeiimik .gt_indent_1 { text-indent: 5px; }
 #xhfoeiimik .gt_indent_2 { text-indent: calc(5px * 2); }
 #xhfoeiimik .gt_indent_3 { text-indent: calc(5px * 3); }
 #xhfoeiimik .gt_indent_4 { text-indent: calc(5px * 4); }
 #xhfoeiimik .gt_indent_5 { text-indent: calc(5px * 5); }
 #xhfoeiimik .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xhfoeiimik .gt_row_group_first td { border-top-width: 2px; }
 #xhfoeiimik .gt_row_group_first th { border-top-width: 2px; }
 #xhfoeiimik .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xhfoeiimik .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xhfoeiimik .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xhfoeiimik .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xhfoeiimik .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xhfoeiimik .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xhfoeiimik .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xhfoeiimik .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xhfoeiimik .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xhfoeiimik .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xhfoeiimik .gt_left { text-align: left; }
 #xhfoeiimik .gt_center { text-align: center; }
 #xhfoeiimik .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xhfoeiimik .gt_font_normal { font-weight: normal; }
 #xhfoeiimik .gt_font_bold { font-weight: bold; }
 #xhfoeiimik .gt_font_italic { font-style: italic; }
 #xhfoeiimik .gt_super { font-size: 65%; }
 #xhfoeiimik .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xhfoeiimik .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xhfoeiimik .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xhfoeiimik .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xhfoeiimik .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xhfoeiimik .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| task    | done  |
|---------|-------|
| Build   | True  |
| Test    | True  |
| Docs    | False |
| Release | None  |


A common use of a custom function is to call out the sign of values, perhaps in the table of changes from earlier:


``` python
def sign_colors(vals):
    return [
        None if x is None else "#1B9E77" if x > 0 else "#D95F02" if x < 0 else "#FFFFFF"
        for x in vals
    ]

(
    GT(changes_df)
    .data_color(columns="change", fn=sign_colors)
    .fmt_number(columns="change", decimals=1, force_sign=True)
)
```


<style>
#bxqjdvaoqx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bxqjdvaoqx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bxqjdvaoqx p { margin: 0; padding: 0; }
 #bxqjdvaoqx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bxqjdvaoqx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bxqjdvaoqx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bxqjdvaoqx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bxqjdvaoqx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bxqjdvaoqx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxqjdvaoqx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bxqjdvaoqx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bxqjdvaoqx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bxqjdvaoqx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bxqjdvaoqx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bxqjdvaoqx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bxqjdvaoqx .gt_spanner_row { border-bottom-style: hidden; }
 #bxqjdvaoqx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bxqjdvaoqx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bxqjdvaoqx .gt_from_md> :first-child { margin-top: 0; }
 #bxqjdvaoqx .gt_from_md> :last-child { margin-bottom: 0; }
 #bxqjdvaoqx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bxqjdvaoqx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bxqjdvaoqx .gt_indent_1 { text-indent: 5px; }
 #bxqjdvaoqx .gt_indent_2 { text-indent: calc(5px * 2); }
 #bxqjdvaoqx .gt_indent_3 { text-indent: calc(5px * 3); }
 #bxqjdvaoqx .gt_indent_4 { text-indent: calc(5px * 4); }
 #bxqjdvaoqx .gt_indent_5 { text-indent: calc(5px * 5); }
 #bxqjdvaoqx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bxqjdvaoqx .gt_row_group_first td { border-top-width: 2px; }
 #bxqjdvaoqx .gt_row_group_first th { border-top-width: 2px; }
 #bxqjdvaoqx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bxqjdvaoqx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxqjdvaoqx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bxqjdvaoqx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bxqjdvaoqx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxqjdvaoqx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bxqjdvaoqx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bxqjdvaoqx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bxqjdvaoqx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxqjdvaoqx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bxqjdvaoqx .gt_left { text-align: left; }
 #bxqjdvaoqx .gt_center { text-align: center; }
 #bxqjdvaoqx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bxqjdvaoqx .gt_font_normal { font-weight: normal; }
 #bxqjdvaoqx .gt_font_bold { font-weight: bold; }
 #bxqjdvaoqx .gt_font_italic { font-style: italic; }
 #bxqjdvaoqx .gt_super { font-size: 65%; }
 #bxqjdvaoqx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxqjdvaoqx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bxqjdvaoqx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxqjdvaoqx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bxqjdvaoqx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bxqjdvaoqx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | −1.0   |


# Color-mapping helpers

Writing a function by hand is fine for a few fixed colors, but interpolating along a gradient or cutting values into bins takes more work. **Great Tables** provides three helpers that create color-mapping functions for you, ready to be passed to `fn=`:

- [col_numeric()](../reference/col_numeric.md#great_tables.col_numeric) maps numeric values to a continuous gradient
- [col_bin()](../reference/col_bin.md#great_tables.col_bin) cuts numeric values into bins and gives each bin a color
- [col_factor()](../reference/col_factor.md#great_tables.col_factor) gives each category its own color

If you've used gt in R, these will be familiar: they're modeled on the [col_numeric()](../reference/col_numeric.md#great_tables.col_numeric), [col_bin()](../reference/col_bin.md#great_tables.col_bin), and [col_factor()](../reference/col_factor.md#great_tables.col_factor) functions from the **scales** package. Each one takes a `palette=`, which can be a list of colors or the name of a ColorBrewer or viridis palette (e.g., `"Blues"` or `"viridis"`), just as with [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color).


## Continuous gradients with [col_numeric()](../reference/col_numeric.md#great_tables.col_numeric)

The [col_numeric()](../reference/col_numeric.md#great_tables.col_numeric) helper interpolates along a palette, much like [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) does with a numeric column, and it has the same `domain=`, `midpoint=`, and `truncate=` arguments. Here's a diverging scale with a domain centered on zero:


``` python
from great_tables import col_numeric

(
    GT(changes_df)
    .data_color(columns="change", fn=col_numeric(palette=red_white_green, domain=[-15, 15]))
    .fmt_number(columns="change", decimals=1, force_sign=True)
)
```


<style>
#rgctjmjlxp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rgctjmjlxp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rgctjmjlxp p { margin: 0; padding: 0; }
 #rgctjmjlxp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rgctjmjlxp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rgctjmjlxp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rgctjmjlxp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rgctjmjlxp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rgctjmjlxp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rgctjmjlxp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rgctjmjlxp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rgctjmjlxp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rgctjmjlxp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rgctjmjlxp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rgctjmjlxp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rgctjmjlxp .gt_spanner_row { border-bottom-style: hidden; }
 #rgctjmjlxp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rgctjmjlxp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rgctjmjlxp .gt_from_md> :first-child { margin-top: 0; }
 #rgctjmjlxp .gt_from_md> :last-child { margin-bottom: 0; }
 #rgctjmjlxp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rgctjmjlxp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rgctjmjlxp .gt_indent_1 { text-indent: 5px; }
 #rgctjmjlxp .gt_indent_2 { text-indent: calc(5px * 2); }
 #rgctjmjlxp .gt_indent_3 { text-indent: calc(5px * 3); }
 #rgctjmjlxp .gt_indent_4 { text-indent: calc(5px * 4); }
 #rgctjmjlxp .gt_indent_5 { text-indent: calc(5px * 5); }
 #rgctjmjlxp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rgctjmjlxp .gt_row_group_first td { border-top-width: 2px; }
 #rgctjmjlxp .gt_row_group_first th { border-top-width: 2px; }
 #rgctjmjlxp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rgctjmjlxp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rgctjmjlxp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rgctjmjlxp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rgctjmjlxp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rgctjmjlxp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rgctjmjlxp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rgctjmjlxp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rgctjmjlxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rgctjmjlxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rgctjmjlxp .gt_left { text-align: left; }
 #rgctjmjlxp .gt_center { text-align: center; }
 #rgctjmjlxp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rgctjmjlxp .gt_font_normal { font-weight: normal; }
 #rgctjmjlxp .gt_font_bold { font-weight: bold; }
 #rgctjmjlxp .gt_font_italic { font-style: italic; }
 #rgctjmjlxp .gt_super { font-size: 65%; }
 #rgctjmjlxp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rgctjmjlxp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rgctjmjlxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rgctjmjlxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rgctjmjlxp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rgctjmjlxp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | −1.0   |


Values outside of the domain are treated as missing by default and receive the `na_color=` color. If you'd rather they took on the colors at the ends of the palette, use `truncate=True`. Here, the domain is narrowed to `[-5, 5]`, so both `12.5` and `-8.1` are fully saturated:


``` python
(
    GT(changes_df)
    .data_color(
        columns="change",
        fn=col_numeric(palette=red_white_green, domain=[-5, 5], truncate=True),
    )
    .fmt_number(columns="change", decimals=1, force_sign=True)
)
```


<style>
#egxzqboafh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#egxzqboafh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#egxzqboafh p { margin: 0; padding: 0; }
 #egxzqboafh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #egxzqboafh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #egxzqboafh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #egxzqboafh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #egxzqboafh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #egxzqboafh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #egxzqboafh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #egxzqboafh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #egxzqboafh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #egxzqboafh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #egxzqboafh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #egxzqboafh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #egxzqboafh .gt_spanner_row { border-bottom-style: hidden; }
 #egxzqboafh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #egxzqboafh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #egxzqboafh .gt_from_md> :first-child { margin-top: 0; }
 #egxzqboafh .gt_from_md> :last-child { margin-bottom: 0; }
 #egxzqboafh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #egxzqboafh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #egxzqboafh .gt_indent_1 { text-indent: 5px; }
 #egxzqboafh .gt_indent_2 { text-indent: calc(5px * 2); }
 #egxzqboafh .gt_indent_3 { text-indent: calc(5px * 3); }
 #egxzqboafh .gt_indent_4 { text-indent: calc(5px * 4); }
 #egxzqboafh .gt_indent_5 { text-indent: calc(5px * 5); }
 #egxzqboafh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #egxzqboafh .gt_row_group_first td { border-top-width: 2px; }
 #egxzqboafh .gt_row_group_first th { border-top-width: 2px; }
 #egxzqboafh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #egxzqboafh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #egxzqboafh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #egxzqboafh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #egxzqboafh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #egxzqboafh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #egxzqboafh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #egxzqboafh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #egxzqboafh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #egxzqboafh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #egxzqboafh .gt_left { text-align: left; }
 #egxzqboafh .gt_center { text-align: center; }
 #egxzqboafh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #egxzqboafh .gt_font_normal { font-weight: normal; }
 #egxzqboafh .gt_font_bold { font-weight: bold; }
 #egxzqboafh .gt_font_italic { font-style: italic; }
 #egxzqboafh .gt_super { font-size: 65%; }
 #egxzqboafh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #egxzqboafh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #egxzqboafh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #egxzqboafh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #egxzqboafh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #egxzqboafh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | −1.0   |


If `domain=` isn't given, then the domain is taken from the range of values in each column. That's often useful, but for a diverging scale it would put the middle color at the middle of the data rather than at zero. As with [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color), the fix is `midpoint=0`.


## Pinning colors to values with `stops=`

What [col_numeric()](../reference/col_numeric.md#great_tables.col_numeric) adds is the `stops=` argument, which pins each color in the palette to a value. It takes one stop per color, and colors are interpolated between neighboring stops. A stop can be a data value (a number) or a position within the range of values in the column (a percentage string, from `"0%"` to `"100%"`). Mixing the two is where this gets useful. Here, the lowest value is fully red, zero is white, and the highest value is fully green:


``` python
(
    GT(changes_df)
    .data_color(
        columns="change",
        fn=col_numeric(palette=red_white_green, stops=["0%", 0, "100%"]),
    )
    .fmt_number(columns="change", decimals=1, force_sign=True)
)
```


<style>
#lwrbpxbqlo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lwrbpxbqlo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lwrbpxbqlo p { margin: 0; padding: 0; }
 #lwrbpxbqlo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lwrbpxbqlo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lwrbpxbqlo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lwrbpxbqlo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lwrbpxbqlo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lwrbpxbqlo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lwrbpxbqlo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lwrbpxbqlo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lwrbpxbqlo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lwrbpxbqlo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lwrbpxbqlo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lwrbpxbqlo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lwrbpxbqlo .gt_spanner_row { border-bottom-style: hidden; }
 #lwrbpxbqlo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lwrbpxbqlo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lwrbpxbqlo .gt_from_md> :first-child { margin-top: 0; }
 #lwrbpxbqlo .gt_from_md> :last-child { margin-bottom: 0; }
 #lwrbpxbqlo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lwrbpxbqlo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lwrbpxbqlo .gt_indent_1 { text-indent: 5px; }
 #lwrbpxbqlo .gt_indent_2 { text-indent: calc(5px * 2); }
 #lwrbpxbqlo .gt_indent_3 { text-indent: calc(5px * 3); }
 #lwrbpxbqlo .gt_indent_4 { text-indent: calc(5px * 4); }
 #lwrbpxbqlo .gt_indent_5 { text-indent: calc(5px * 5); }
 #lwrbpxbqlo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lwrbpxbqlo .gt_row_group_first td { border-top-width: 2px; }
 #lwrbpxbqlo .gt_row_group_first th { border-top-width: 2px; }
 #lwrbpxbqlo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lwrbpxbqlo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lwrbpxbqlo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lwrbpxbqlo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lwrbpxbqlo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lwrbpxbqlo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lwrbpxbqlo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lwrbpxbqlo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lwrbpxbqlo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lwrbpxbqlo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lwrbpxbqlo .gt_left { text-align: left; }
 #lwrbpxbqlo .gt_center { text-align: center; }
 #lwrbpxbqlo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lwrbpxbqlo .gt_font_normal { font-weight: normal; }
 #lwrbpxbqlo .gt_font_bold { font-weight: bold; }
 #lwrbpxbqlo .gt_font_italic { font-style: italic; }
 #lwrbpxbqlo .gt_super { font-size: 65%; }
 #lwrbpxbqlo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lwrbpxbqlo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lwrbpxbqlo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lwrbpxbqlo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lwrbpxbqlo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lwrbpxbqlo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | −1.0   |


Because the percentages are worked out separately for each column, the same function can be used on columns with very different ranges, and zero will be white in all of them. (The range that the percentages refer to also stretches to include any numeric stops, so a column with no negative values is colored from white up to green, with no red at all.)

Repeating a stop makes a sharp change in color at that value, rather than a gradual one. Here, decreases are shades of orange and increases are shades of purple, with no blending across zero:


``` python
(
    GT(changes_df)
    .data_color(
        columns="change",
        fn=col_numeric(
            palette=["#E66101", "#FDB863", "#B2ABD2", "#5E3C99"],
            stops=["0%", 0, 0, "100%"],
        ),
    )
    .fmt_number(columns="change", decimals=1, force_sign=True)
)
```


<style>
#ufcygfaoez table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ufcygfaoez thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ufcygfaoez p { margin: 0; padding: 0; }
 #ufcygfaoez .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ufcygfaoez .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ufcygfaoez .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ufcygfaoez .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ufcygfaoez .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ufcygfaoez .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ufcygfaoez .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ufcygfaoez .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ufcygfaoez .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ufcygfaoez .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ufcygfaoez .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ufcygfaoez .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ufcygfaoez .gt_spanner_row { border-bottom-style: hidden; }
 #ufcygfaoez .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ufcygfaoez .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ufcygfaoez .gt_from_md> :first-child { margin-top: 0; }
 #ufcygfaoez .gt_from_md> :last-child { margin-bottom: 0; }
 #ufcygfaoez .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ufcygfaoez .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ufcygfaoez .gt_indent_1 { text-indent: 5px; }
 #ufcygfaoez .gt_indent_2 { text-indent: calc(5px * 2); }
 #ufcygfaoez .gt_indent_3 { text-indent: calc(5px * 3); }
 #ufcygfaoez .gt_indent_4 { text-indent: calc(5px * 4); }
 #ufcygfaoez .gt_indent_5 { text-indent: calc(5px * 5); }
 #ufcygfaoez .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ufcygfaoez .gt_row_group_first td { border-top-width: 2px; }
 #ufcygfaoez .gt_row_group_first th { border-top-width: 2px; }
 #ufcygfaoez .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ufcygfaoez .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ufcygfaoez .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ufcygfaoez .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ufcygfaoez .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ufcygfaoez .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ufcygfaoez .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ufcygfaoez .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ufcygfaoez .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ufcygfaoez .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ufcygfaoez .gt_left { text-align: left; }
 #ufcygfaoez .gt_center { text-align: center; }
 #ufcygfaoez .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ufcygfaoez .gt_font_normal { font-weight: normal; }
 #ufcygfaoez .gt_font_bold { font-weight: bold; }
 #ufcygfaoez .gt_font_italic { font-style: italic; }
 #ufcygfaoez .gt_super { font-size: 65%; }
 #ufcygfaoez .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ufcygfaoez .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ufcygfaoez .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ufcygfaoez .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ufcygfaoez .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ufcygfaoez .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | −1.0   |


A value that sits exactly on a repeated stop takes the later color, so the `0.0` change is light purple. Stops beyond the range of the values work too: the outermost stops act as the domain, so values outside of them are treated as missing unless `truncate=True` is used.


## Bins with [col_bin()](../reference/col_bin.md#great_tables.col_bin)

Sometimes it's clearer to group values into a few ranges than to show a smooth gradient. The [col_bin()](../reference/col_bin.md#great_tables.col_bin) helper does this. Its `bins=` argument is either a number of equal-width bins, or a list of bin boundaries:


``` python
from great_tables import col_bin

scores_df = pl.DataFrame(
    {
        "student": ["Ana", "Ben", "Cai", "Dee", "Eli", "Fay"],
        "score": [38, 45, 62, 78, 95, 100],
    }
)

GT(scores_df).data_color(columns="score", fn=col_bin(palette="YlGn", bins=[0, 50, 70, 90, 100]))
```


<style>
#pdpfkuexpj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pdpfkuexpj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pdpfkuexpj p { margin: 0; padding: 0; }
 #pdpfkuexpj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pdpfkuexpj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pdpfkuexpj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pdpfkuexpj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pdpfkuexpj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pdpfkuexpj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pdpfkuexpj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pdpfkuexpj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pdpfkuexpj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pdpfkuexpj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pdpfkuexpj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pdpfkuexpj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pdpfkuexpj .gt_spanner_row { border-bottom-style: hidden; }
 #pdpfkuexpj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pdpfkuexpj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pdpfkuexpj .gt_from_md> :first-child { margin-top: 0; }
 #pdpfkuexpj .gt_from_md> :last-child { margin-bottom: 0; }
 #pdpfkuexpj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pdpfkuexpj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pdpfkuexpj .gt_indent_1 { text-indent: 5px; }
 #pdpfkuexpj .gt_indent_2 { text-indent: calc(5px * 2); }
 #pdpfkuexpj .gt_indent_3 { text-indent: calc(5px * 3); }
 #pdpfkuexpj .gt_indent_4 { text-indent: calc(5px * 4); }
 #pdpfkuexpj .gt_indent_5 { text-indent: calc(5px * 5); }
 #pdpfkuexpj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pdpfkuexpj .gt_row_group_first td { border-top-width: 2px; }
 #pdpfkuexpj .gt_row_group_first th { border-top-width: 2px; }
 #pdpfkuexpj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pdpfkuexpj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pdpfkuexpj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pdpfkuexpj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pdpfkuexpj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pdpfkuexpj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pdpfkuexpj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pdpfkuexpj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pdpfkuexpj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pdpfkuexpj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pdpfkuexpj .gt_left { text-align: left; }
 #pdpfkuexpj .gt_center { text-align: center; }
 #pdpfkuexpj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pdpfkuexpj .gt_font_normal { font-weight: normal; }
 #pdpfkuexpj .gt_font_bold { font-weight: bold; }
 #pdpfkuexpj .gt_font_italic { font-style: italic; }
 #pdpfkuexpj .gt_super { font-size: 65%; }
 #pdpfkuexpj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pdpfkuexpj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pdpfkuexpj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pdpfkuexpj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pdpfkuexpj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pdpfkuexpj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| student | score |
|---------|-------|
| Ana     | 38    |
| Ben     | 45    |
| Cai     | 62    |
| Dee     | 78    |
| Eli     | 95    |
| Fay     | 100   |


By default, each bin includes its lower boundary but not its upper one, so a score of exactly `70` falls in the `[70, 90)` bin. The last bin includes both of its boundaries, so the perfect score of `100` is still colored. Use `right=True` to flip this, so that bins include their upper boundaries instead. And as with [col_numeric()](../reference/col_numeric.md#great_tables.col_numeric), values outside of the outermost boundaries are treated as missing unless `truncate=True` is used.


## Categories with [col_factor()](../reference/col_factor.md#great_tables.col_factor)

The [col_factor()](../reference/col_factor.md#great_tables.col_factor) helper gives each distinct value its own color. On its own that's similar to what [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) does with a string column, but [col_factor()](../reference/col_factor.md#great_tables.col_factor) lets you fix the set of levels and their order with `domain=`. This means a level always receives the same color, no matter which levels are present in the column or in what order they appear. That's important when building several tables that should be colored consistently. Any value not in the domain receives the missing-value color, which we can use here to flag an unexpected value:


``` python
from great_tables import col_factor

tickets_df = pl.DataFrame(
    {
        "ticket": [101, 102, 103, 104, 105],
        "priority": ["low", "high", "medium", "high", "urgent"],
    }
)

GT(tickets_df).data_color(
    columns="priority",
    fn=col_factor(palette=["#FEF0D9", "#FDCC8A", "#FC8D59"], domain=["low", "medium", "high"]),
    na_color="#D7301F",
)
```


<style>
#xiuxcdcvmd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xiuxcdcvmd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xiuxcdcvmd p { margin: 0; padding: 0; }
 #xiuxcdcvmd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xiuxcdcvmd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xiuxcdcvmd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xiuxcdcvmd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xiuxcdcvmd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xiuxcdcvmd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xiuxcdcvmd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xiuxcdcvmd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xiuxcdcvmd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xiuxcdcvmd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xiuxcdcvmd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xiuxcdcvmd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xiuxcdcvmd .gt_spanner_row { border-bottom-style: hidden; }
 #xiuxcdcvmd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xiuxcdcvmd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xiuxcdcvmd .gt_from_md> :first-child { margin-top: 0; }
 #xiuxcdcvmd .gt_from_md> :last-child { margin-bottom: 0; }
 #xiuxcdcvmd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xiuxcdcvmd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xiuxcdcvmd .gt_indent_1 { text-indent: 5px; }
 #xiuxcdcvmd .gt_indent_2 { text-indent: calc(5px * 2); }
 #xiuxcdcvmd .gt_indent_3 { text-indent: calc(5px * 3); }
 #xiuxcdcvmd .gt_indent_4 { text-indent: calc(5px * 4); }
 #xiuxcdcvmd .gt_indent_5 { text-indent: calc(5px * 5); }
 #xiuxcdcvmd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xiuxcdcvmd .gt_row_group_first td { border-top-width: 2px; }
 #xiuxcdcvmd .gt_row_group_first th { border-top-width: 2px; }
 #xiuxcdcvmd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xiuxcdcvmd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xiuxcdcvmd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xiuxcdcvmd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xiuxcdcvmd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xiuxcdcvmd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xiuxcdcvmd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xiuxcdcvmd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xiuxcdcvmd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xiuxcdcvmd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xiuxcdcvmd .gt_left { text-align: left; }
 #xiuxcdcvmd .gt_center { text-align: center; }
 #xiuxcdcvmd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xiuxcdcvmd .gt_font_normal { font-weight: normal; }
 #xiuxcdcvmd .gt_font_bold { font-weight: bold; }
 #xiuxcdcvmd .gt_font_italic { font-style: italic; }
 #xiuxcdcvmd .gt_super { font-size: 65%; }
 #xiuxcdcvmd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xiuxcdcvmd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xiuxcdcvmd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xiuxcdcvmd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xiuxcdcvmd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xiuxcdcvmd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| ticket | priority |
|--------|----------|
| 101    | low      |
| 102    | high     |
| 103    | medium   |
| 104    | high     |
| 105    | urgent   |


If the palette has fewer colors than there are levels, then the in-between colors are interpolated along the palette.


## Combining helpers with your own logic

The helpers return ordinary functions, so they can be called from inside a function of your own. This is handy when you want to adjust some of the colors a helper gives. For example, to draw attention only to the larger changes, we can color the values with [col_numeric()](../reference/col_numeric.md#great_tables.col_numeric) and then replace the colors of any small changes (less than 2 in either direction) with `None`, so that they get the plain `na_color=` color:


``` python
color_change = col_numeric(palette=red_white_green, midpoint=0)

def large_changes_only(vals):
    colors = color_change(vals)
    return [None if x is None or abs(x) < 2 else color for x, color in zip(vals, colors)]

(
    GT(changes_df)
    .data_color(columns="change", fn=large_changes_only, na_color="white")
    .fmt_number(columns="change", decimals=1, force_sign=True)
)
```


<style>
#cvklnfikme table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cvklnfikme thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cvklnfikme p { margin: 0; padding: 0; }
 #cvklnfikme .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cvklnfikme .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cvklnfikme .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cvklnfikme .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cvklnfikme .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cvklnfikme .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvklnfikme .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cvklnfikme .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cvklnfikme .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cvklnfikme .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cvklnfikme .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cvklnfikme .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cvklnfikme .gt_spanner_row { border-bottom-style: hidden; }
 #cvklnfikme .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cvklnfikme .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cvklnfikme .gt_from_md> :first-child { margin-top: 0; }
 #cvklnfikme .gt_from_md> :last-child { margin-bottom: 0; }
 #cvklnfikme .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cvklnfikme .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cvklnfikme .gt_indent_1 { text-indent: 5px; }
 #cvklnfikme .gt_indent_2 { text-indent: calc(5px * 2); }
 #cvklnfikme .gt_indent_3 { text-indent: calc(5px * 3); }
 #cvklnfikme .gt_indent_4 { text-indent: calc(5px * 4); }
 #cvklnfikme .gt_indent_5 { text-indent: calc(5px * 5); }
 #cvklnfikme .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cvklnfikme .gt_row_group_first td { border-top-width: 2px; }
 #cvklnfikme .gt_row_group_first th { border-top-width: 2px; }
 #cvklnfikme .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cvklnfikme .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvklnfikme .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cvklnfikme .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cvklnfikme .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvklnfikme .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cvklnfikme .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cvklnfikme .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cvklnfikme .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvklnfikme .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cvklnfikme .gt_left { text-align: left; }
 #cvklnfikme .gt_center { text-align: center; }
 #cvklnfikme .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cvklnfikme .gt_font_normal { font-weight: normal; }
 #cvklnfikme .gt_font_bold { font-weight: bold; }
 #cvklnfikme .gt_font_italic { font-style: italic; }
 #cvklnfikme .gt_super { font-size: 65%; }
 #cvklnfikme .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvklnfikme .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cvklnfikme .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvklnfikme .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cvklnfikme .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cvklnfikme .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | −1.0   |


The `-1.0` and `0.0` changes are left white, while the others keep the colors they'd have had on the full scale.


# Bringing it all together

For a more advanced treatment of data colorization in the table, let's take the [sza](../reference/data.sza.md#great_tables.data.sza) dataset (available in the `great_tables.data` submodule) and vigorously reshape it with **Polars** so that solar zenith angles are arranged as rows by month, and the half-hourly clock times are the columns (from early morning to solar noon).

Once the `pivot()`ing is done, we can introduce that that table to the [GT](../reference/GT.md#great_tables.GT) class, placing the names of the months in the table stub. We will use [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) with a domain that runs from `90` to `0` (here, 90° is sunrise, and 0° is represents the sun angle that's directly overhead). There are months where the sun rises later in the morning, before the sunrise times we'll see missing values in the dataset, and `na_color="white"` will handle those cases. Okay, that's the plan, and now here's the code:


``` python
from great_tables import html
from great_tables.data import sza
import polars.selectors as cs

sza_pivot = (
    pl.from_pandas(sza)
    .filter((pl.col("latitude") == "20") & (pl.col("tst") <= "1200"))
    .select(pl.col("*").exclude("latitude"))
    .drop_nulls()
    .pivot(values="sza", index="month", on="tst", sort_columns=True)
)

(
    GT(sza_pivot, rowname_col="month")
    .data_color(
        domain=[90, 0],
        palette=["rebeccapurple", "white", "orange"],
        na_color="white",
    )
    .tab_header(
        title="Solar Zenith Angles from 05:30 to 12:00",
        subtitle=html("Average monthly values at latitude of 20°N."),
    )
)
```


<style>
#ivsmpknrdt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ivsmpknrdt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ivsmpknrdt p { margin: 0; padding: 0; }
 #ivsmpknrdt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ivsmpknrdt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ivsmpknrdt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ivsmpknrdt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ivsmpknrdt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ivsmpknrdt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ivsmpknrdt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ivsmpknrdt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ivsmpknrdt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ivsmpknrdt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ivsmpknrdt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ivsmpknrdt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ivsmpknrdt .gt_spanner_row { border-bottom-style: hidden; }
 #ivsmpknrdt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ivsmpknrdt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ivsmpknrdt .gt_from_md> :first-child { margin-top: 0; }
 #ivsmpknrdt .gt_from_md> :last-child { margin-bottom: 0; }
 #ivsmpknrdt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ivsmpknrdt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ivsmpknrdt .gt_indent_1 { text-indent: 5px; }
 #ivsmpknrdt .gt_indent_2 { text-indent: calc(5px * 2); }
 #ivsmpknrdt .gt_indent_3 { text-indent: calc(5px * 3); }
 #ivsmpknrdt .gt_indent_4 { text-indent: calc(5px * 4); }
 #ivsmpknrdt .gt_indent_5 { text-indent: calc(5px * 5); }
 #ivsmpknrdt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ivsmpknrdt .gt_row_group_first td { border-top-width: 2px; }
 #ivsmpknrdt .gt_row_group_first th { border-top-width: 2px; }
 #ivsmpknrdt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ivsmpknrdt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ivsmpknrdt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ivsmpknrdt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ivsmpknrdt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ivsmpknrdt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ivsmpknrdt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ivsmpknrdt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ivsmpknrdt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ivsmpknrdt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ivsmpknrdt .gt_left { text-align: left; }
 #ivsmpknrdt .gt_center { text-align: center; }
 #ivsmpknrdt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ivsmpknrdt .gt_font_normal { font-weight: normal; }
 #ivsmpknrdt .gt_font_bold { font-weight: bold; }
 #ivsmpknrdt .gt_font_italic { font-style: italic; }
 #ivsmpknrdt .gt_super { font-size: 65%; }
 #ivsmpknrdt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ivsmpknrdt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ivsmpknrdt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ivsmpknrdt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ivsmpknrdt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ivsmpknrdt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="15" class="gt_heading gt_title gt_font_normal">Solar Zenith Angles from 05:30 to 12:00</th>
</tr>
<tr class="gt_heading">
<th colspan="15" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Average monthly values at latitude of 20°N.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="0530" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0530</th>
<th id="0600" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0600</th>
<th id="0630" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0630</th>
<th id="0700" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0700</th>
<th id="0730" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0730</th>
<th id="0800" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0800</th>
<th id="0830" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0830</th>
<th id="0900" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0900</th>
<th id="0930" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">0930</th>
<th id="1000" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1000</th>
<th id="1030" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1030</th>
<th id="1100" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1100</th>
<th id="1130" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1130</th>
<th id="1200" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1200</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">jan</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #774aa5">84.9</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8c66b3">78.7</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a181c0">72.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #b79fcf">66.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c7b4da">61.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d8cbe5">56.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e7dfef">52.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f4f0f8">48.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fdfdfe">45.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffcf7">43.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffbf4">43.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">feb</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #6a389b">88.9</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8055aa">82.5</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9673b9">75.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #ab8fc7">69.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c1acd6">63.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d4c5e2">57.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e7deef">52.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f7f4fa">47.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffbf4">43.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff5e3">40.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff1d6">37.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffefd3">37.2</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">mar</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #7546a3">85.7</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8c66b2">78.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a385c2">72.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #baa3d1">65.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d1c1e0">58.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e6deee">52.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fbfafc">46.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff6e5">40.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffecc9">35.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffe4b2">31.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdea2">28.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdc9d">27.7</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">apr</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #6b3a9c">88.5</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #835aac">81.5</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9b7abc">74.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #b399cc">67.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #cbbadc">60.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e2d9ec">53.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #faf8fc">46.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff4e1">39.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffe7bc">33.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdb98">26.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd079">21.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc761">17.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc458">15.5</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">may</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #774aa4">85.0</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8e68b4">78.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a688c4">71.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #bda8d3">64.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d6c8e3">57.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ede7f3">50.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffbf5">43.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffedcd">36.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdfa5">29.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd994">26.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc356">15.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffb732">8.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffaf1c">5.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">jun</th>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #69379b">89.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #7f54aa">82.7</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9672b9">76.0</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #ac91c8">69.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4b0d7">62.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #dbcee7">55.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f2eef6">48.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff9ed">41.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffebc6">35.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdd9f">28.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffcf78">21.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc150">14.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffb429">7.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffa90b">2.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">jul</th>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #6a389c">88.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8056aa">82.3</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9774b9">75.7</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #ad92c8">69.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4b1d8">62.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #dbcfe7">55.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f2eef7">48.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff9ed">41.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffebc6">35.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdd9f">28.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffcf78">21.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc251">14.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffb42c">7.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffab12">3.1</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">aug</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #7b4fa7">83.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #926db6">77.1</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a98dc6">70.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c1acd6">63.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d8cbe5">56.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f0ebf5">49.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffaf0">42.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffecc9">35.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdea0">28.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd079">21.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc251">14.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffb429">7.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffa90b">1.9</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">sep</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #70409f">87.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #875faf">80.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9f7fbf">73.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #b79fcf">66.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #cfbfdf">59.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e7dfef">52.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffffff">45.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff1d8">38.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffe4b1">31.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd68c">24.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffca69">18.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc04e">13.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffbc42">11.6</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">oct</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #7a4ea6">84.1</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #926db6">77.1</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a98dc6">70.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c1acd6">63.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d8cbe5">56.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #eee9f4">49.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffcf6">43.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff0d4">37.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffe5b5">32.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdc9b">27.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd68a">24.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd383">23.1</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">nov</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #6d3d9e">87.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #845aad">81.3</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9b79bc">74.5</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #b095ca">68.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c6b3d9">61.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #dacde6">56.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ede7f3">50.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fefefe">45.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff6e7">40.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff0d4">37.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffebc7">35.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffeac3">34.4</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #FFFFFF">dec</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #794da6">84.3</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8f69b4">78.0</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a486c2">71.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #b79fcf">66.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #cab9dc">60.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #dbcfe7">55.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ebe4f2">50.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f8f5fa">47.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffdfa">44.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffaf0">42.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff9ed">41.8</td>
</tr>
</tbody>
</table>


Because this is a table for presentation, we can't neglect using [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header). A *title* and *subtitle* can provide just enough information to guide the reader out through your table visualization.
