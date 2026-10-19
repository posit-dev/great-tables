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
#cwgwtfxhze table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cwgwtfxhze thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cwgwtfxhze p { margin: 0; padding: 0; }
 #cwgwtfxhze .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cwgwtfxhze .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cwgwtfxhze .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cwgwtfxhze .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cwgwtfxhze .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cwgwtfxhze .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cwgwtfxhze .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cwgwtfxhze .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cwgwtfxhze .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cwgwtfxhze .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cwgwtfxhze .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cwgwtfxhze .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cwgwtfxhze .gt_spanner_row { border-bottom-style: hidden; }
 #cwgwtfxhze .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cwgwtfxhze .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cwgwtfxhze .gt_from_md> :first-child { margin-top: 0; }
 #cwgwtfxhze .gt_from_md> :last-child { margin-bottom: 0; }
 #cwgwtfxhze .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cwgwtfxhze .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cwgwtfxhze .gt_indent_1 { text-indent: 5px; }
 #cwgwtfxhze .gt_indent_2 { text-indent: calc(5px * 2); }
 #cwgwtfxhze .gt_indent_3 { text-indent: calc(5px * 3); }
 #cwgwtfxhze .gt_indent_4 { text-indent: calc(5px * 4); }
 #cwgwtfxhze .gt_indent_5 { text-indent: calc(5px * 5); }
 #cwgwtfxhze .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cwgwtfxhze .gt_row_group_first td { border-top-width: 2px; }
 #cwgwtfxhze .gt_row_group_first th { border-top-width: 2px; }
 #cwgwtfxhze .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cwgwtfxhze .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cwgwtfxhze .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cwgwtfxhze .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cwgwtfxhze .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cwgwtfxhze .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cwgwtfxhze .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cwgwtfxhze .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cwgwtfxhze .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cwgwtfxhze .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cwgwtfxhze .gt_left { text-align: left; }
 #cwgwtfxhze .gt_center { text-align: center; }
 #cwgwtfxhze .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cwgwtfxhze .gt_font_normal { font-weight: normal; }
 #cwgwtfxhze .gt_font_bold { font-weight: bold; }
 #cwgwtfxhze .gt_font_italic { font-style: italic; }
 #cwgwtfxhze .gt_super { font-size: 65%; }
 #cwgwtfxhze .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cwgwtfxhze .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cwgwtfxhze .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cwgwtfxhze .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cwgwtfxhze .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cwgwtfxhze .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qjgkbnyyom table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qjgkbnyyom thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qjgkbnyyom p { margin: 0; padding: 0; }
 #qjgkbnyyom .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qjgkbnyyom .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qjgkbnyyom .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qjgkbnyyom .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qjgkbnyyom .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qjgkbnyyom .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qjgkbnyyom .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qjgkbnyyom .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qjgkbnyyom .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qjgkbnyyom .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qjgkbnyyom .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qjgkbnyyom .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qjgkbnyyom .gt_spanner_row { border-bottom-style: hidden; }
 #qjgkbnyyom .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qjgkbnyyom .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qjgkbnyyom .gt_from_md> :first-child { margin-top: 0; }
 #qjgkbnyyom .gt_from_md> :last-child { margin-bottom: 0; }
 #qjgkbnyyom .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qjgkbnyyom .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qjgkbnyyom .gt_indent_1 { text-indent: 5px; }
 #qjgkbnyyom .gt_indent_2 { text-indent: calc(5px * 2); }
 #qjgkbnyyom .gt_indent_3 { text-indent: calc(5px * 3); }
 #qjgkbnyyom .gt_indent_4 { text-indent: calc(5px * 4); }
 #qjgkbnyyom .gt_indent_5 { text-indent: calc(5px * 5); }
 #qjgkbnyyom .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qjgkbnyyom .gt_row_group_first td { border-top-width: 2px; }
 #qjgkbnyyom .gt_row_group_first th { border-top-width: 2px; }
 #qjgkbnyyom .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qjgkbnyyom .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qjgkbnyyom .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qjgkbnyyom .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qjgkbnyyom .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qjgkbnyyom .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qjgkbnyyom .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qjgkbnyyom .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qjgkbnyyom .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qjgkbnyyom .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qjgkbnyyom .gt_left { text-align: left; }
 #qjgkbnyyom .gt_center { text-align: center; }
 #qjgkbnyyom .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qjgkbnyyom .gt_font_normal { font-weight: normal; }
 #qjgkbnyyom .gt_font_bold { font-weight: bold; }
 #qjgkbnyyom .gt_font_italic { font-style: italic; }
 #qjgkbnyyom .gt_super { font-size: 65%; }
 #qjgkbnyyom .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qjgkbnyyom .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qjgkbnyyom .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qjgkbnyyom .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qjgkbnyyom .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qjgkbnyyom .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vurhtyinjw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vurhtyinjw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vurhtyinjw p { margin: 0; padding: 0; }
 #vurhtyinjw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vurhtyinjw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vurhtyinjw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vurhtyinjw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vurhtyinjw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vurhtyinjw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vurhtyinjw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vurhtyinjw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vurhtyinjw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vurhtyinjw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vurhtyinjw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vurhtyinjw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vurhtyinjw .gt_spanner_row { border-bottom-style: hidden; }
 #vurhtyinjw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vurhtyinjw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vurhtyinjw .gt_from_md> :first-child { margin-top: 0; }
 #vurhtyinjw .gt_from_md> :last-child { margin-bottom: 0; }
 #vurhtyinjw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vurhtyinjw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vurhtyinjw .gt_indent_1 { text-indent: 5px; }
 #vurhtyinjw .gt_indent_2 { text-indent: calc(5px * 2); }
 #vurhtyinjw .gt_indent_3 { text-indent: calc(5px * 3); }
 #vurhtyinjw .gt_indent_4 { text-indent: calc(5px * 4); }
 #vurhtyinjw .gt_indent_5 { text-indent: calc(5px * 5); }
 #vurhtyinjw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vurhtyinjw .gt_row_group_first td { border-top-width: 2px; }
 #vurhtyinjw .gt_row_group_first th { border-top-width: 2px; }
 #vurhtyinjw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vurhtyinjw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vurhtyinjw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vurhtyinjw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vurhtyinjw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vurhtyinjw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vurhtyinjw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vurhtyinjw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vurhtyinjw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vurhtyinjw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vurhtyinjw .gt_left { text-align: left; }
 #vurhtyinjw .gt_center { text-align: center; }
 #vurhtyinjw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vurhtyinjw .gt_font_normal { font-weight: normal; }
 #vurhtyinjw .gt_font_bold { font-weight: bold; }
 #vurhtyinjw .gt_font_italic { font-style: italic; }
 #vurhtyinjw .gt_super { font-size: 65%; }
 #vurhtyinjw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vurhtyinjw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vurhtyinjw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vurhtyinjw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vurhtyinjw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vurhtyinjw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#koluxcfnji table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#koluxcfnji thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#koluxcfnji p { margin: 0; padding: 0; }
 #koluxcfnji .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #koluxcfnji .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #koluxcfnji .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #koluxcfnji .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #koluxcfnji .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #koluxcfnji .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #koluxcfnji .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #koluxcfnji .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #koluxcfnji .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #koluxcfnji .gt_column_spanner_outer:first-child { padding-left: 0; }
 #koluxcfnji .gt_column_spanner_outer:last-child { padding-right: 0; }
 #koluxcfnji .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #koluxcfnji .gt_spanner_row { border-bottom-style: hidden; }
 #koluxcfnji .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #koluxcfnji .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #koluxcfnji .gt_from_md> :first-child { margin-top: 0; }
 #koluxcfnji .gt_from_md> :last-child { margin-bottom: 0; }
 #koluxcfnji .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #koluxcfnji .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #koluxcfnji .gt_indent_1 { text-indent: 5px; }
 #koluxcfnji .gt_indent_2 { text-indent: calc(5px * 2); }
 #koluxcfnji .gt_indent_3 { text-indent: calc(5px * 3); }
 #koluxcfnji .gt_indent_4 { text-indent: calc(5px * 4); }
 #koluxcfnji .gt_indent_5 { text-indent: calc(5px * 5); }
 #koluxcfnji .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #koluxcfnji .gt_row_group_first td { border-top-width: 2px; }
 #koluxcfnji .gt_row_group_first th { border-top-width: 2px; }
 #koluxcfnji .gt_striped { color: #333333; background-color: #F4F4F4; }
 #koluxcfnji .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #koluxcfnji .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #koluxcfnji .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #koluxcfnji .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #koluxcfnji .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #koluxcfnji .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #koluxcfnji .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #koluxcfnji .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #koluxcfnji .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #koluxcfnji .gt_left { text-align: left; }
 #koluxcfnji .gt_center { text-align: center; }
 #koluxcfnji .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #koluxcfnji .gt_font_normal { font-weight: normal; }
 #koluxcfnji .gt_font_bold { font-weight: bold; }
 #koluxcfnji .gt_font_italic { font-style: italic; }
 #koluxcfnji .gt_super { font-size: 65%; }
 #koluxcfnji .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #koluxcfnji .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #koluxcfnji .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #koluxcfnji .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #koluxcfnji .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #koluxcfnji .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bcauclzqax table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bcauclzqax thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bcauclzqax p { margin: 0; padding: 0; }
 #bcauclzqax .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bcauclzqax .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bcauclzqax .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bcauclzqax .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bcauclzqax .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bcauclzqax .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bcauclzqax .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bcauclzqax .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bcauclzqax .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bcauclzqax .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bcauclzqax .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bcauclzqax .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bcauclzqax .gt_spanner_row { border-bottom-style: hidden; }
 #bcauclzqax .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bcauclzqax .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bcauclzqax .gt_from_md> :first-child { margin-top: 0; }
 #bcauclzqax .gt_from_md> :last-child { margin-bottom: 0; }
 #bcauclzqax .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bcauclzqax .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bcauclzqax .gt_indent_1 { text-indent: 5px; }
 #bcauclzqax .gt_indent_2 { text-indent: calc(5px * 2); }
 #bcauclzqax .gt_indent_3 { text-indent: calc(5px * 3); }
 #bcauclzqax .gt_indent_4 { text-indent: calc(5px * 4); }
 #bcauclzqax .gt_indent_5 { text-indent: calc(5px * 5); }
 #bcauclzqax .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bcauclzqax .gt_row_group_first td { border-top-width: 2px; }
 #bcauclzqax .gt_row_group_first th { border-top-width: 2px; }
 #bcauclzqax .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bcauclzqax .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bcauclzqax .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bcauclzqax .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bcauclzqax .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bcauclzqax .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bcauclzqax .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bcauclzqax .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bcauclzqax .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bcauclzqax .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bcauclzqax .gt_left { text-align: left; }
 #bcauclzqax .gt_center { text-align: center; }
 #bcauclzqax .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bcauclzqax .gt_font_normal { font-weight: normal; }
 #bcauclzqax .gt_font_bold { font-weight: bold; }
 #bcauclzqax .gt_font_italic { font-style: italic; }
 #bcauclzqax .gt_super { font-size: 65%; }
 #bcauclzqax .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bcauclzqax .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bcauclzqax .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bcauclzqax .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bcauclzqax .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bcauclzqax .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#snibxucyhs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#snibxucyhs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#snibxucyhs p { margin: 0; padding: 0; }
 #snibxucyhs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #snibxucyhs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #snibxucyhs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #snibxucyhs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #snibxucyhs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #snibxucyhs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #snibxucyhs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #snibxucyhs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #snibxucyhs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #snibxucyhs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #snibxucyhs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #snibxucyhs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #snibxucyhs .gt_spanner_row { border-bottom-style: hidden; }
 #snibxucyhs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #snibxucyhs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #snibxucyhs .gt_from_md> :first-child { margin-top: 0; }
 #snibxucyhs .gt_from_md> :last-child { margin-bottom: 0; }
 #snibxucyhs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #snibxucyhs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #snibxucyhs .gt_indent_1 { text-indent: 5px; }
 #snibxucyhs .gt_indent_2 { text-indent: calc(5px * 2); }
 #snibxucyhs .gt_indent_3 { text-indent: calc(5px * 3); }
 #snibxucyhs .gt_indent_4 { text-indent: calc(5px * 4); }
 #snibxucyhs .gt_indent_5 { text-indent: calc(5px * 5); }
 #snibxucyhs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #snibxucyhs .gt_row_group_first td { border-top-width: 2px; }
 #snibxucyhs .gt_row_group_first th { border-top-width: 2px; }
 #snibxucyhs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #snibxucyhs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #snibxucyhs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #snibxucyhs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #snibxucyhs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #snibxucyhs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #snibxucyhs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #snibxucyhs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #snibxucyhs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #snibxucyhs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #snibxucyhs .gt_left { text-align: left; }
 #snibxucyhs .gt_center { text-align: center; }
 #snibxucyhs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #snibxucyhs .gt_font_normal { font-weight: normal; }
 #snibxucyhs .gt_font_bold { font-weight: bold; }
 #snibxucyhs .gt_font_italic { font-style: italic; }
 #snibxucyhs .gt_super { font-size: 65%; }
 #snibxucyhs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #snibxucyhs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #snibxucyhs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #snibxucyhs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #snibxucyhs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #snibxucyhs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#icmejswyhj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#icmejswyhj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#icmejswyhj p { margin: 0; padding: 0; }
 #icmejswyhj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #icmejswyhj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #icmejswyhj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #icmejswyhj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #icmejswyhj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #icmejswyhj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #icmejswyhj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #icmejswyhj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #icmejswyhj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #icmejswyhj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #icmejswyhj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #icmejswyhj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #icmejswyhj .gt_spanner_row { border-bottom-style: hidden; }
 #icmejswyhj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #icmejswyhj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #icmejswyhj .gt_from_md> :first-child { margin-top: 0; }
 #icmejswyhj .gt_from_md> :last-child { margin-bottom: 0; }
 #icmejswyhj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #icmejswyhj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #icmejswyhj .gt_indent_1 { text-indent: 5px; }
 #icmejswyhj .gt_indent_2 { text-indent: calc(5px * 2); }
 #icmejswyhj .gt_indent_3 { text-indent: calc(5px * 3); }
 #icmejswyhj .gt_indent_4 { text-indent: calc(5px * 4); }
 #icmejswyhj .gt_indent_5 { text-indent: calc(5px * 5); }
 #icmejswyhj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #icmejswyhj .gt_row_group_first td { border-top-width: 2px; }
 #icmejswyhj .gt_row_group_first th { border-top-width: 2px; }
 #icmejswyhj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #icmejswyhj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #icmejswyhj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #icmejswyhj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #icmejswyhj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #icmejswyhj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #icmejswyhj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #icmejswyhj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #icmejswyhj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #icmejswyhj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #icmejswyhj .gt_left { text-align: left; }
 #icmejswyhj .gt_center { text-align: center; }
 #icmejswyhj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #icmejswyhj .gt_font_normal { font-weight: normal; }
 #icmejswyhj .gt_font_bold { font-weight: bold; }
 #icmejswyhj .gt_font_italic { font-style: italic; }
 #icmejswyhj .gt_super { font-size: 65%; }
 #icmejswyhj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #icmejswyhj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #icmejswyhj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #icmejswyhj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #icmejswyhj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #icmejswyhj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uefycveqsx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uefycveqsx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uefycveqsx p { margin: 0; padding: 0; }
 #uefycveqsx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uefycveqsx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uefycveqsx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uefycveqsx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uefycveqsx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uefycveqsx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uefycveqsx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uefycveqsx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uefycveqsx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uefycveqsx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uefycveqsx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uefycveqsx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uefycveqsx .gt_spanner_row { border-bottom-style: hidden; }
 #uefycveqsx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uefycveqsx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uefycveqsx .gt_from_md> :first-child { margin-top: 0; }
 #uefycveqsx .gt_from_md> :last-child { margin-bottom: 0; }
 #uefycveqsx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uefycveqsx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uefycveqsx .gt_indent_1 { text-indent: 5px; }
 #uefycveqsx .gt_indent_2 { text-indent: calc(5px * 2); }
 #uefycveqsx .gt_indent_3 { text-indent: calc(5px * 3); }
 #uefycveqsx .gt_indent_4 { text-indent: calc(5px * 4); }
 #uefycveqsx .gt_indent_5 { text-indent: calc(5px * 5); }
 #uefycveqsx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uefycveqsx .gt_row_group_first td { border-top-width: 2px; }
 #uefycveqsx .gt_row_group_first th { border-top-width: 2px; }
 #uefycveqsx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uefycveqsx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uefycveqsx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uefycveqsx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uefycveqsx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uefycveqsx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uefycveqsx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uefycveqsx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uefycveqsx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uefycveqsx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uefycveqsx .gt_left { text-align: left; }
 #uefycveqsx .gt_center { text-align: center; }
 #uefycveqsx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uefycveqsx .gt_font_normal { font-weight: normal; }
 #uefycveqsx .gt_font_bold { font-weight: bold; }
 #uefycveqsx .gt_font_italic { font-style: italic; }
 #uefycveqsx .gt_super { font-size: 65%; }
 #uefycveqsx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uefycveqsx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uefycveqsx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uefycveqsx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uefycveqsx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uefycveqsx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uilmyvrxtj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uilmyvrxtj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uilmyvrxtj p { margin: 0; padding: 0; }
 #uilmyvrxtj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uilmyvrxtj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uilmyvrxtj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uilmyvrxtj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uilmyvrxtj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uilmyvrxtj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uilmyvrxtj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uilmyvrxtj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uilmyvrxtj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uilmyvrxtj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uilmyvrxtj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uilmyvrxtj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uilmyvrxtj .gt_spanner_row { border-bottom-style: hidden; }
 #uilmyvrxtj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uilmyvrxtj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uilmyvrxtj .gt_from_md> :first-child { margin-top: 0; }
 #uilmyvrxtj .gt_from_md> :last-child { margin-bottom: 0; }
 #uilmyvrxtj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uilmyvrxtj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uilmyvrxtj .gt_indent_1 { text-indent: 5px; }
 #uilmyvrxtj .gt_indent_2 { text-indent: calc(5px * 2); }
 #uilmyvrxtj .gt_indent_3 { text-indent: calc(5px * 3); }
 #uilmyvrxtj .gt_indent_4 { text-indent: calc(5px * 4); }
 #uilmyvrxtj .gt_indent_5 { text-indent: calc(5px * 5); }
 #uilmyvrxtj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uilmyvrxtj .gt_row_group_first td { border-top-width: 2px; }
 #uilmyvrxtj .gt_row_group_first th { border-top-width: 2px; }
 #uilmyvrxtj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uilmyvrxtj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uilmyvrxtj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uilmyvrxtj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uilmyvrxtj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uilmyvrxtj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uilmyvrxtj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uilmyvrxtj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uilmyvrxtj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uilmyvrxtj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uilmyvrxtj .gt_left { text-align: left; }
 #uilmyvrxtj .gt_center { text-align: center; }
 #uilmyvrxtj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uilmyvrxtj .gt_font_normal { font-weight: normal; }
 #uilmyvrxtj .gt_font_bold { font-weight: bold; }
 #uilmyvrxtj .gt_font_italic { font-style: italic; }
 #uilmyvrxtj .gt_super { font-size: 65%; }
 #uilmyvrxtj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uilmyvrxtj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uilmyvrxtj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uilmyvrxtj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uilmyvrxtj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uilmyvrxtj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ekvdtuaepm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ekvdtuaepm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ekvdtuaepm p { margin: 0; padding: 0; }
 #ekvdtuaepm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ekvdtuaepm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ekvdtuaepm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ekvdtuaepm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ekvdtuaepm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ekvdtuaepm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ekvdtuaepm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ekvdtuaepm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ekvdtuaepm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ekvdtuaepm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ekvdtuaepm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ekvdtuaepm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ekvdtuaepm .gt_spanner_row { border-bottom-style: hidden; }
 #ekvdtuaepm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ekvdtuaepm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ekvdtuaepm .gt_from_md> :first-child { margin-top: 0; }
 #ekvdtuaepm .gt_from_md> :last-child { margin-bottom: 0; }
 #ekvdtuaepm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ekvdtuaepm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ekvdtuaepm .gt_indent_1 { text-indent: 5px; }
 #ekvdtuaepm .gt_indent_2 { text-indent: calc(5px * 2); }
 #ekvdtuaepm .gt_indent_3 { text-indent: calc(5px * 3); }
 #ekvdtuaepm .gt_indent_4 { text-indent: calc(5px * 4); }
 #ekvdtuaepm .gt_indent_5 { text-indent: calc(5px * 5); }
 #ekvdtuaepm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ekvdtuaepm .gt_row_group_first td { border-top-width: 2px; }
 #ekvdtuaepm .gt_row_group_first th { border-top-width: 2px; }
 #ekvdtuaepm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ekvdtuaepm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ekvdtuaepm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ekvdtuaepm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ekvdtuaepm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ekvdtuaepm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ekvdtuaepm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ekvdtuaepm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ekvdtuaepm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ekvdtuaepm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ekvdtuaepm .gt_left { text-align: left; }
 #ekvdtuaepm .gt_center { text-align: center; }
 #ekvdtuaepm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ekvdtuaepm .gt_font_normal { font-weight: normal; }
 #ekvdtuaepm .gt_font_bold { font-weight: bold; }
 #ekvdtuaepm .gt_font_italic { font-style: italic; }
 #ekvdtuaepm .gt_super { font-size: 65%; }
 #ekvdtuaepm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ekvdtuaepm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ekvdtuaepm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ekvdtuaepm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ekvdtuaepm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ekvdtuaepm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vylzmkjzal table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vylzmkjzal thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vylzmkjzal p { margin: 0; padding: 0; }
 #vylzmkjzal .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vylzmkjzal .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vylzmkjzal .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vylzmkjzal .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vylzmkjzal .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vylzmkjzal .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vylzmkjzal .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vylzmkjzal .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vylzmkjzal .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vylzmkjzal .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vylzmkjzal .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vylzmkjzal .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vylzmkjzal .gt_spanner_row { border-bottom-style: hidden; }
 #vylzmkjzal .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vylzmkjzal .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vylzmkjzal .gt_from_md> :first-child { margin-top: 0; }
 #vylzmkjzal .gt_from_md> :last-child { margin-bottom: 0; }
 #vylzmkjzal .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vylzmkjzal .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vylzmkjzal .gt_indent_1 { text-indent: 5px; }
 #vylzmkjzal .gt_indent_2 { text-indent: calc(5px * 2); }
 #vylzmkjzal .gt_indent_3 { text-indent: calc(5px * 3); }
 #vylzmkjzal .gt_indent_4 { text-indent: calc(5px * 4); }
 #vylzmkjzal .gt_indent_5 { text-indent: calc(5px * 5); }
 #vylzmkjzal .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vylzmkjzal .gt_row_group_first td { border-top-width: 2px; }
 #vylzmkjzal .gt_row_group_first th { border-top-width: 2px; }
 #vylzmkjzal .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vylzmkjzal .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vylzmkjzal .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vylzmkjzal .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vylzmkjzal .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vylzmkjzal .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vylzmkjzal .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vylzmkjzal .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vylzmkjzal .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vylzmkjzal .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vylzmkjzal .gt_left { text-align: left; }
 #vylzmkjzal .gt_center { text-align: center; }
 #vylzmkjzal .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vylzmkjzal .gt_font_normal { font-weight: normal; }
 #vylzmkjzal .gt_font_bold { font-weight: bold; }
 #vylzmkjzal .gt_font_italic { font-style: italic; }
 #vylzmkjzal .gt_super { font-size: 65%; }
 #vylzmkjzal .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vylzmkjzal .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vylzmkjzal .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vylzmkjzal .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vylzmkjzal .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vylzmkjzal .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cetbgoaheu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cetbgoaheu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cetbgoaheu p { margin: 0; padding: 0; }
 #cetbgoaheu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cetbgoaheu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cetbgoaheu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cetbgoaheu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cetbgoaheu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cetbgoaheu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cetbgoaheu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cetbgoaheu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cetbgoaheu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cetbgoaheu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cetbgoaheu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cetbgoaheu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cetbgoaheu .gt_spanner_row { border-bottom-style: hidden; }
 #cetbgoaheu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cetbgoaheu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cetbgoaheu .gt_from_md> :first-child { margin-top: 0; }
 #cetbgoaheu .gt_from_md> :last-child { margin-bottom: 0; }
 #cetbgoaheu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cetbgoaheu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cetbgoaheu .gt_indent_1 { text-indent: 5px; }
 #cetbgoaheu .gt_indent_2 { text-indent: calc(5px * 2); }
 #cetbgoaheu .gt_indent_3 { text-indent: calc(5px * 3); }
 #cetbgoaheu .gt_indent_4 { text-indent: calc(5px * 4); }
 #cetbgoaheu .gt_indent_5 { text-indent: calc(5px * 5); }
 #cetbgoaheu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cetbgoaheu .gt_row_group_first td { border-top-width: 2px; }
 #cetbgoaheu .gt_row_group_first th { border-top-width: 2px; }
 #cetbgoaheu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cetbgoaheu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cetbgoaheu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cetbgoaheu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cetbgoaheu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cetbgoaheu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cetbgoaheu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cetbgoaheu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cetbgoaheu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cetbgoaheu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cetbgoaheu .gt_left { text-align: left; }
 #cetbgoaheu .gt_center { text-align: center; }
 #cetbgoaheu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cetbgoaheu .gt_font_normal { font-weight: normal; }
 #cetbgoaheu .gt_font_bold { font-weight: bold; }
 #cetbgoaheu .gt_font_italic { font-style: italic; }
 #cetbgoaheu .gt_super { font-size: 65%; }
 #cetbgoaheu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cetbgoaheu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cetbgoaheu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cetbgoaheu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cetbgoaheu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cetbgoaheu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#edbccvfigv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#edbccvfigv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#edbccvfigv p { margin: 0; padding: 0; }
 #edbccvfigv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #edbccvfigv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #edbccvfigv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #edbccvfigv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #edbccvfigv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #edbccvfigv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #edbccvfigv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #edbccvfigv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #edbccvfigv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #edbccvfigv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #edbccvfigv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #edbccvfigv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #edbccvfigv .gt_spanner_row { border-bottom-style: hidden; }
 #edbccvfigv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #edbccvfigv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #edbccvfigv .gt_from_md> :first-child { margin-top: 0; }
 #edbccvfigv .gt_from_md> :last-child { margin-bottom: 0; }
 #edbccvfigv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #edbccvfigv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #edbccvfigv .gt_indent_1 { text-indent: 5px; }
 #edbccvfigv .gt_indent_2 { text-indent: calc(5px * 2); }
 #edbccvfigv .gt_indent_3 { text-indent: calc(5px * 3); }
 #edbccvfigv .gt_indent_4 { text-indent: calc(5px * 4); }
 #edbccvfigv .gt_indent_5 { text-indent: calc(5px * 5); }
 #edbccvfigv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #edbccvfigv .gt_row_group_first td { border-top-width: 2px; }
 #edbccvfigv .gt_row_group_first th { border-top-width: 2px; }
 #edbccvfigv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #edbccvfigv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #edbccvfigv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #edbccvfigv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #edbccvfigv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #edbccvfigv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #edbccvfigv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #edbccvfigv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #edbccvfigv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edbccvfigv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #edbccvfigv .gt_left { text-align: left; }
 #edbccvfigv .gt_center { text-align: center; }
 #edbccvfigv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #edbccvfigv .gt_font_normal { font-weight: normal; }
 #edbccvfigv .gt_font_bold { font-weight: bold; }
 #edbccvfigv .gt_font_italic { font-style: italic; }
 #edbccvfigv .gt_super { font-size: 65%; }
 #edbccvfigv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edbccvfigv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #edbccvfigv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edbccvfigv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #edbccvfigv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #edbccvfigv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jachudiuri table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jachudiuri thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jachudiuri p { margin: 0; padding: 0; }
 #jachudiuri .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jachudiuri .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jachudiuri .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jachudiuri .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jachudiuri .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jachudiuri .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jachudiuri .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jachudiuri .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jachudiuri .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jachudiuri .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jachudiuri .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jachudiuri .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jachudiuri .gt_spanner_row { border-bottom-style: hidden; }
 #jachudiuri .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jachudiuri .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jachudiuri .gt_from_md> :first-child { margin-top: 0; }
 #jachudiuri .gt_from_md> :last-child { margin-bottom: 0; }
 #jachudiuri .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jachudiuri .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jachudiuri .gt_indent_1 { text-indent: 5px; }
 #jachudiuri .gt_indent_2 { text-indent: calc(5px * 2); }
 #jachudiuri .gt_indent_3 { text-indent: calc(5px * 3); }
 #jachudiuri .gt_indent_4 { text-indent: calc(5px * 4); }
 #jachudiuri .gt_indent_5 { text-indent: calc(5px * 5); }
 #jachudiuri .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jachudiuri .gt_row_group_first td { border-top-width: 2px; }
 #jachudiuri .gt_row_group_first th { border-top-width: 2px; }
 #jachudiuri .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jachudiuri .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jachudiuri .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jachudiuri .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jachudiuri .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jachudiuri .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jachudiuri .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jachudiuri .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jachudiuri .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jachudiuri .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jachudiuri .gt_left { text-align: left; }
 #jachudiuri .gt_center { text-align: center; }
 #jachudiuri .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jachudiuri .gt_font_normal { font-weight: normal; }
 #jachudiuri .gt_font_bold { font-weight: bold; }
 #jachudiuri .gt_font_italic { font-style: italic; }
 #jachudiuri .gt_super { font-size: 65%; }
 #jachudiuri .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jachudiuri .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jachudiuri .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jachudiuri .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jachudiuri .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jachudiuri .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hinknjzokf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hinknjzokf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hinknjzokf p { margin: 0; padding: 0; }
 #hinknjzokf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hinknjzokf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hinknjzokf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hinknjzokf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hinknjzokf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hinknjzokf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hinknjzokf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hinknjzokf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hinknjzokf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hinknjzokf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hinknjzokf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hinknjzokf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hinknjzokf .gt_spanner_row { border-bottom-style: hidden; }
 #hinknjzokf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hinknjzokf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hinknjzokf .gt_from_md> :first-child { margin-top: 0; }
 #hinknjzokf .gt_from_md> :last-child { margin-bottom: 0; }
 #hinknjzokf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hinknjzokf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hinknjzokf .gt_indent_1 { text-indent: 5px; }
 #hinknjzokf .gt_indent_2 { text-indent: calc(5px * 2); }
 #hinknjzokf .gt_indent_3 { text-indent: calc(5px * 3); }
 #hinknjzokf .gt_indent_4 { text-indent: calc(5px * 4); }
 #hinknjzokf .gt_indent_5 { text-indent: calc(5px * 5); }
 #hinknjzokf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hinknjzokf .gt_row_group_first td { border-top-width: 2px; }
 #hinknjzokf .gt_row_group_first th { border-top-width: 2px; }
 #hinknjzokf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hinknjzokf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hinknjzokf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hinknjzokf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hinknjzokf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hinknjzokf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hinknjzokf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hinknjzokf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hinknjzokf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hinknjzokf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hinknjzokf .gt_left { text-align: left; }
 #hinknjzokf .gt_center { text-align: center; }
 #hinknjzokf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hinknjzokf .gt_font_normal { font-weight: normal; }
 #hinknjzokf .gt_font_bold { font-weight: bold; }
 #hinknjzokf .gt_font_italic { font-style: italic; }
 #hinknjzokf .gt_super { font-size: 65%; }
 #hinknjzokf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hinknjzokf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hinknjzokf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hinknjzokf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hinknjzokf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hinknjzokf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wwzdvxsbft table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wwzdvxsbft thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wwzdvxsbft p { margin: 0; padding: 0; }
 #wwzdvxsbft .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wwzdvxsbft .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wwzdvxsbft .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wwzdvxsbft .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wwzdvxsbft .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wwzdvxsbft .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wwzdvxsbft .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wwzdvxsbft .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wwzdvxsbft .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wwzdvxsbft .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wwzdvxsbft .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wwzdvxsbft .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wwzdvxsbft .gt_spanner_row { border-bottom-style: hidden; }
 #wwzdvxsbft .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wwzdvxsbft .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wwzdvxsbft .gt_from_md> :first-child { margin-top: 0; }
 #wwzdvxsbft .gt_from_md> :last-child { margin-bottom: 0; }
 #wwzdvxsbft .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wwzdvxsbft .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wwzdvxsbft .gt_indent_1 { text-indent: 5px; }
 #wwzdvxsbft .gt_indent_2 { text-indent: calc(5px * 2); }
 #wwzdvxsbft .gt_indent_3 { text-indent: calc(5px * 3); }
 #wwzdvxsbft .gt_indent_4 { text-indent: calc(5px * 4); }
 #wwzdvxsbft .gt_indent_5 { text-indent: calc(5px * 5); }
 #wwzdvxsbft .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wwzdvxsbft .gt_row_group_first td { border-top-width: 2px; }
 #wwzdvxsbft .gt_row_group_first th { border-top-width: 2px; }
 #wwzdvxsbft .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wwzdvxsbft .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wwzdvxsbft .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wwzdvxsbft .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wwzdvxsbft .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wwzdvxsbft .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wwzdvxsbft .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wwzdvxsbft .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wwzdvxsbft .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wwzdvxsbft .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wwzdvxsbft .gt_left { text-align: left; }
 #wwzdvxsbft .gt_center { text-align: center; }
 #wwzdvxsbft .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wwzdvxsbft .gt_font_normal { font-weight: normal; }
 #wwzdvxsbft .gt_font_bold { font-weight: bold; }
 #wwzdvxsbft .gt_font_italic { font-style: italic; }
 #wwzdvxsbft .gt_super { font-size: 65%; }
 #wwzdvxsbft .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wwzdvxsbft .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wwzdvxsbft .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wwzdvxsbft .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wwzdvxsbft .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wwzdvxsbft .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qtlmmjwnff table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qtlmmjwnff thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qtlmmjwnff p { margin: 0; padding: 0; }
 #qtlmmjwnff .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qtlmmjwnff .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qtlmmjwnff .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qtlmmjwnff .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qtlmmjwnff .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qtlmmjwnff .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qtlmmjwnff .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qtlmmjwnff .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qtlmmjwnff .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qtlmmjwnff .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qtlmmjwnff .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qtlmmjwnff .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qtlmmjwnff .gt_spanner_row { border-bottom-style: hidden; }
 #qtlmmjwnff .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qtlmmjwnff .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qtlmmjwnff .gt_from_md> :first-child { margin-top: 0; }
 #qtlmmjwnff .gt_from_md> :last-child { margin-bottom: 0; }
 #qtlmmjwnff .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qtlmmjwnff .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qtlmmjwnff .gt_indent_1 { text-indent: 5px; }
 #qtlmmjwnff .gt_indent_2 { text-indent: calc(5px * 2); }
 #qtlmmjwnff .gt_indent_3 { text-indent: calc(5px * 3); }
 #qtlmmjwnff .gt_indent_4 { text-indent: calc(5px * 4); }
 #qtlmmjwnff .gt_indent_5 { text-indent: calc(5px * 5); }
 #qtlmmjwnff .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qtlmmjwnff .gt_row_group_first td { border-top-width: 2px; }
 #qtlmmjwnff .gt_row_group_first th { border-top-width: 2px; }
 #qtlmmjwnff .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qtlmmjwnff .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qtlmmjwnff .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qtlmmjwnff .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qtlmmjwnff .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qtlmmjwnff .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qtlmmjwnff .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qtlmmjwnff .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qtlmmjwnff .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qtlmmjwnff .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qtlmmjwnff .gt_left { text-align: left; }
 #qtlmmjwnff .gt_center { text-align: center; }
 #qtlmmjwnff .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qtlmmjwnff .gt_font_normal { font-weight: normal; }
 #qtlmmjwnff .gt_font_bold { font-weight: bold; }
 #qtlmmjwnff .gt_font_italic { font-style: italic; }
 #qtlmmjwnff .gt_super { font-size: 65%; }
 #qtlmmjwnff .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qtlmmjwnff .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qtlmmjwnff .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qtlmmjwnff .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qtlmmjwnff .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qtlmmjwnff .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ulscacvdrd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ulscacvdrd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ulscacvdrd p { margin: 0; padding: 0; }
 #ulscacvdrd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ulscacvdrd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ulscacvdrd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ulscacvdrd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ulscacvdrd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ulscacvdrd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ulscacvdrd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ulscacvdrd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ulscacvdrd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ulscacvdrd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ulscacvdrd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ulscacvdrd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ulscacvdrd .gt_spanner_row { border-bottom-style: hidden; }
 #ulscacvdrd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ulscacvdrd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ulscacvdrd .gt_from_md> :first-child { margin-top: 0; }
 #ulscacvdrd .gt_from_md> :last-child { margin-bottom: 0; }
 #ulscacvdrd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ulscacvdrd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ulscacvdrd .gt_indent_1 { text-indent: 5px; }
 #ulscacvdrd .gt_indent_2 { text-indent: calc(5px * 2); }
 #ulscacvdrd .gt_indent_3 { text-indent: calc(5px * 3); }
 #ulscacvdrd .gt_indent_4 { text-indent: calc(5px * 4); }
 #ulscacvdrd .gt_indent_5 { text-indent: calc(5px * 5); }
 #ulscacvdrd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ulscacvdrd .gt_row_group_first td { border-top-width: 2px; }
 #ulscacvdrd .gt_row_group_first th { border-top-width: 2px; }
 #ulscacvdrd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ulscacvdrd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ulscacvdrd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ulscacvdrd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ulscacvdrd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ulscacvdrd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ulscacvdrd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ulscacvdrd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ulscacvdrd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ulscacvdrd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ulscacvdrd .gt_left { text-align: left; }
 #ulscacvdrd .gt_center { text-align: center; }
 #ulscacvdrd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ulscacvdrd .gt_font_normal { font-weight: normal; }
 #ulscacvdrd .gt_font_bold { font-weight: bold; }
 #ulscacvdrd .gt_font_italic { font-style: italic; }
 #ulscacvdrd .gt_super { font-size: 65%; }
 #ulscacvdrd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ulscacvdrd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ulscacvdrd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ulscacvdrd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ulscacvdrd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ulscacvdrd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="15" id="title" class="gt_heading gt_title gt_font_normal">Solar Zenith Angles from 05:30 to 12:00</th>
</tr>
<tr class="gt_heading">
<th colspan="15" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Average monthly values at latitude of 20°N.</th>
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
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">jan</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-1 0530">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-1 0600">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-1 0630">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #784aa5" headers="stub-1 0700">84.9</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8e64b3" headers="stub-1 0730">78.7</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a37fc0" headers="stub-1 0800">72.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #b99ccf" headers="stub-1 0830">66.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8b1da" headers="stub-1 0900">61.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d9c8e5" headers="stub-1 0930">56.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e8ddef" headers="stub-1 1000">52.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f4eff8" headers="stub-1 1030">48.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fdfdfe" headers="stub-1 1100">45.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffcf8" headers="stub-1 1130">43.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffbf5" headers="stub-1 1200">43.0</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">feb</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-2 0530">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-2 0600">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #6a389c" headers="stub-2 0630">88.9</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8154aa" headers="stub-2 0700">82.5</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9871b9" headers="stub-2 0730">75.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #ad8dc7" headers="stub-2 0800">69.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c2a9d6" headers="stub-2 0830">63.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d5c3e2" headers="stub-2 0900">57.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e7ddef" headers="stub-2 0930">52.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f7f3fa" headers="stub-2 1000">47.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffbf6" headers="stub-2 1030">43.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff5e6" headers="stub-2 1100">40.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff0db" headers="stub-2 1130">37.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffefd8" headers="stub-2 1200">37.2</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">mar</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-3 0530">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-3 0600">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #7646a3" headers="stub-3 0630">85.7</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8e64b2" headers="stub-3 0700">78.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a582c2" headers="stub-3 0730">72.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #bca0d1" headers="stub-3 0800">65.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d2bfe0" headers="stub-3 0830">58.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e7dcee" headers="stub-3 0900">52.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fbf9fc" headers="stub-3 0930">46.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff6e9" headers="stub-3 1000">40.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffebd0" headers="stub-3 1030">35.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffe3bc" headers="stub-3 1100">31.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffddae" headers="stub-3 1130">28.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdcaa" headers="stub-3 1200">27.7</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">apr</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-4 0530">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #6b3a9c" headers="stub-4 0600">88.5</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8458ac" headers="stub-4 0630">81.5</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9d77bc" headers="stub-4 0700">74.4</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #b596cc" headers="stub-4 0730">67.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ccb7dc" headers="stub-4 0800">60.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e3d7ec" headers="stub-4 0830">53.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #faf8fc" headers="stub-4 0900">46.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff4e5" headers="stub-4 0930">39.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffe7c5" headers="stub-4 1000">33.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdaa6" headers="stub-4 1030">26.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffcf8b" headers="stub-4 1100">21.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc777" headers="stub-4 1130">17.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc36e" headers="stub-4 1200">15.5</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">may</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-5 0530">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #7849a4" headers="stub-5 0600">85.0</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9067b4" headers="stub-5 0630">78.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a885c4" headers="stub-5 0700">71.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #bfa4d3" headers="stub-5 0730">64.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d7c5e3" headers="stub-5 0800">57.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #eee6f3" headers="stub-5 0830">50.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffbf6" headers="stub-5 0900">43.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffedd3" headers="stub-5 0930">36.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdeb1" headers="stub-5 1000">29.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd8a2" headers="stub-5 1030">26.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc36d" headers="stub-5 1100">15.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffb64b" headers="stub-5 1130">8.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffaf34" headers="stub-5 1200">5.0</td>
</tr>
<tr>
<th id="stub-6" class="gt_row gt_left gt_stub" scope="row">jun</th>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #69379b" headers="stub-6 0530">89.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8053aa" headers="stub-6 0600">82.7</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9770b9" headers="stub-6 0630">76.0</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #ae8ec8" headers="stub-6 0700">69.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c5add7" headers="stub-6 0730">62.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #dccce7" headers="stub-6 0800">55.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f2edf6" headers="stub-6 0830">48.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff9f0" headers="stub-6 0900">41.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffeace" headers="stub-6 0930">35.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdcac" headers="stub-6 1000">28.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffce8a" headers="stub-6 1030">21.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc168" headers="stub-6 1100">14.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffb343" headers="stub-6 1130">7.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffa91d" headers="stub-6 1200">2.0</td>
</tr>
<tr>
<th id="stub-7" class="gt_row gt_left gt_stub" scope="row">jul</th>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #6a389c" headers="stub-7 0530">88.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8255ab" headers="stub-7 0600">82.3</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9872b9" headers="stub-7 0630">75.7</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #af8fc8" headers="stub-7 0700">69.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c6aed8" headers="stub-7 0730">62.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #dccde7" headers="stub-7 0800">55.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f3edf7" headers="stub-7 0830">48.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff8ef" headers="stub-7 0900">41.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffeace" headers="stub-7 0930">35.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdcac" headers="stub-7 1000">28.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffcf8a" headers="stub-7 1030">21.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc168" headers="stub-7 1100">14.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffb445" headers="stub-7 1130">7.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffab27" headers="stub-7 1200">3.1</td>
</tr>
<tr>
<th id="stub-8" class="gt_row gt_left gt_stub" scope="row">aug</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-8 0530">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #7c4ea7" headers="stub-8 0600">83.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #946bb6" headers="stub-8 0630">77.1</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #ab8ac6" headers="stub-8 0700">70.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c2a9d6" headers="stub-8 0730">63.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d9c9e5" headers="stub-8 0800">56.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f0eaf5" headers="stub-8 0830">49.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffaf2" headers="stub-8 0900">42.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffebd0" headers="stub-8 0930">35.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffddad" headers="stub-8 1000">28.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffcf8b" headers="stub-8 1030">21.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc168" headers="stub-8 1100">14.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffb343" headers="stub-8 1130">7.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffa91c" headers="stub-8 1200">1.9</td>
</tr>
<tr>
<th id="stub-9" class="gt_row gt_left gt_stub" scope="row">sep</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-9 0530">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #703f9f" headers="stub-9 0600">87.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #895eaf" headers="stub-9 0630">80.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a17dbf" headers="stub-9 0700">73.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #b99ccf" headers="stub-9 0730">66.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d0bcdf" headers="stub-9 0800">59.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e8ddef" headers="stub-9 0830">52.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffffff" headers="stub-9 0900">45.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff1dd" headers="stub-9 0930">38.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffe3bb" headers="stub-9 1000">31.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd69b" headers="stub-9 1030">24.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc97e" headers="stub-9 1100">18.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffc065" headers="stub-9 1130">13.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffbc5a" headers="stub-9 1200">11.6</td>
</tr>
<tr>
<th id="stub-10" class="gt_row gt_left gt_stub" scope="row">oct</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-10 0530">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-10 0600">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #7b4da6" headers="stub-10 0630">84.1</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #946bb6" headers="stub-10 0700">77.1</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #ab8ac6" headers="stub-10 0730">70.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c2a9d6" headers="stub-10 0800">63.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d9c8e5" headers="stub-10 0830">56.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #efe7f4" headers="stub-10 0900">49.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffcf8" headers="stub-10 0930">43.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff0da" headers="stub-10 1000">37.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffe4bf" headers="stub-10 1030">32.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffdba8" headers="stub-10 1100">27.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd599" headers="stub-10 1130">24.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffd294" headers="stub-10 1200">23.1</td>
</tr>
<tr>
<th id="stub-11" class="gt_row gt_left gt_stub" scope="row">nov</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-11 0530">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-11 0600">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #6e3d9e" headers="stub-11 0630">87.8</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #8559ad" headers="stub-11 0700">81.3</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9d77bc" headers="stub-11 0730">74.5</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #b292ca" headers="stub-11 0800">68.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c7b0d9" headers="stub-11 0830">61.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #dbcbe6" headers="stub-11 0900">56.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #eee6f3" headers="stub-11 0930">50.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fefefe" headers="stub-11 1000">45.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff6ea" headers="stub-11 1030">40.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffefd9" headers="stub-11 1100">37.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffebce" headers="stub-11 1130">35.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffe9cb" headers="stub-11 1200">34.4</td>
</tr>
<tr>
<th id="stub-12" class="gt_row gt_left gt_stub" scope="row">dec</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-12 0530">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-12 0600">None</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #FFFFFF" headers="stub-12 0630">None</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #7b4ca6" headers="stub-12 0700">84.3</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #9168b4" headers="stub-12 0730">78.0</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a683c2" headers="stub-12 0800">71.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #b99ccf" headers="stub-12 0830">66.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ccb6dc" headers="stub-12 0900">60.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #dccde7" headers="stub-12 0930">55.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ebe3f2" headers="stub-12 1000">50.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f8f4fa" headers="stub-12 1030">47.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffdfb" headers="stub-12 1100">44.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fffaf2" headers="stub-12 1130">42.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #fff8ef" headers="stub-12 1200">41.8</td>
</tr>
</tbody>
</table>


Because this is a table for presentation, we can't neglect using [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header). A *title* and *subtitle* can provide just enough information to guide the reader out through your table visualization.
