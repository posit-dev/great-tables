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
#khidxwfjkb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#khidxwfjkb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#khidxwfjkb p { margin: 0; padding: 0; }
 #khidxwfjkb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #khidxwfjkb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #khidxwfjkb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #khidxwfjkb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #khidxwfjkb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khidxwfjkb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khidxwfjkb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khidxwfjkb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #khidxwfjkb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #khidxwfjkb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #khidxwfjkb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #khidxwfjkb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #khidxwfjkb .gt_spanner_row { border-bottom-style: hidden; }
 #khidxwfjkb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #khidxwfjkb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #khidxwfjkb .gt_from_md> :first-child { margin-top: 0; }
 #khidxwfjkb .gt_from_md> :last-child { margin-bottom: 0; }
 #khidxwfjkb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #khidxwfjkb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #khidxwfjkb .gt_indent_1 { text-indent: 5px; }
 #khidxwfjkb .gt_indent_2 { text-indent: calc(5px * 2); }
 #khidxwfjkb .gt_indent_3 { text-indent: calc(5px * 3); }
 #khidxwfjkb .gt_indent_4 { text-indent: calc(5px * 4); }
 #khidxwfjkb .gt_indent_5 { text-indent: calc(5px * 5); }
 #khidxwfjkb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #khidxwfjkb .gt_row_group_first td { border-top-width: 2px; }
 #khidxwfjkb .gt_row_group_first th { border-top-width: 2px; }
 #khidxwfjkb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #khidxwfjkb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khidxwfjkb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khidxwfjkb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #khidxwfjkb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khidxwfjkb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khidxwfjkb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #khidxwfjkb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #khidxwfjkb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khidxwfjkb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khidxwfjkb .gt_left { text-align: left; }
 #khidxwfjkb .gt_center { text-align: center; }
 #khidxwfjkb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #khidxwfjkb .gt_font_normal { font-weight: normal; }
 #khidxwfjkb .gt_font_bold { font-weight: bold; }
 #khidxwfjkb .gt_font_italic { font-style: italic; }
 #khidxwfjkb .gt_super { font-size: 65%; }
 #khidxwfjkb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khidxwfjkb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #khidxwfjkb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khidxwfjkb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khidxwfjkb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #khidxwfjkb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#diypmldvmg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#diypmldvmg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#diypmldvmg p { margin: 0; padding: 0; }
 #diypmldvmg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #diypmldvmg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #diypmldvmg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #diypmldvmg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #diypmldvmg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #diypmldvmg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #diypmldvmg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #diypmldvmg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #diypmldvmg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #diypmldvmg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #diypmldvmg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #diypmldvmg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #diypmldvmg .gt_spanner_row { border-bottom-style: hidden; }
 #diypmldvmg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #diypmldvmg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #diypmldvmg .gt_from_md> :first-child { margin-top: 0; }
 #diypmldvmg .gt_from_md> :last-child { margin-bottom: 0; }
 #diypmldvmg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #diypmldvmg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #diypmldvmg .gt_indent_1 { text-indent: 5px; }
 #diypmldvmg .gt_indent_2 { text-indent: calc(5px * 2); }
 #diypmldvmg .gt_indent_3 { text-indent: calc(5px * 3); }
 #diypmldvmg .gt_indent_4 { text-indent: calc(5px * 4); }
 #diypmldvmg .gt_indent_5 { text-indent: calc(5px * 5); }
 #diypmldvmg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #diypmldvmg .gt_row_group_first td { border-top-width: 2px; }
 #diypmldvmg .gt_row_group_first th { border-top-width: 2px; }
 #diypmldvmg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #diypmldvmg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #diypmldvmg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #diypmldvmg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #diypmldvmg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #diypmldvmg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #diypmldvmg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #diypmldvmg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #diypmldvmg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #diypmldvmg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #diypmldvmg .gt_left { text-align: left; }
 #diypmldvmg .gt_center { text-align: center; }
 #diypmldvmg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #diypmldvmg .gt_font_normal { font-weight: normal; }
 #diypmldvmg .gt_font_bold { font-weight: bold; }
 #diypmldvmg .gt_font_italic { font-style: italic; }
 #diypmldvmg .gt_super { font-size: 65%; }
 #diypmldvmg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #diypmldvmg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #diypmldvmg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #diypmldvmg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #diypmldvmg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #diypmldvmg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qsbbgvmhip table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qsbbgvmhip thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qsbbgvmhip p { margin: 0; padding: 0; }
 #qsbbgvmhip .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qsbbgvmhip .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qsbbgvmhip .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qsbbgvmhip .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qsbbgvmhip .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qsbbgvmhip .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qsbbgvmhip .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qsbbgvmhip .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qsbbgvmhip .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qsbbgvmhip .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qsbbgvmhip .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qsbbgvmhip .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qsbbgvmhip .gt_spanner_row { border-bottom-style: hidden; }
 #qsbbgvmhip .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qsbbgvmhip .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qsbbgvmhip .gt_from_md> :first-child { margin-top: 0; }
 #qsbbgvmhip .gt_from_md> :last-child { margin-bottom: 0; }
 #qsbbgvmhip .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qsbbgvmhip .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qsbbgvmhip .gt_indent_1 { text-indent: 5px; }
 #qsbbgvmhip .gt_indent_2 { text-indent: calc(5px * 2); }
 #qsbbgvmhip .gt_indent_3 { text-indent: calc(5px * 3); }
 #qsbbgvmhip .gt_indent_4 { text-indent: calc(5px * 4); }
 #qsbbgvmhip .gt_indent_5 { text-indent: calc(5px * 5); }
 #qsbbgvmhip .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qsbbgvmhip .gt_row_group_first td { border-top-width: 2px; }
 #qsbbgvmhip .gt_row_group_first th { border-top-width: 2px; }
 #qsbbgvmhip .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qsbbgvmhip .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qsbbgvmhip .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qsbbgvmhip .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qsbbgvmhip .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qsbbgvmhip .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qsbbgvmhip .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qsbbgvmhip .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qsbbgvmhip .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qsbbgvmhip .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qsbbgvmhip .gt_left { text-align: left; }
 #qsbbgvmhip .gt_center { text-align: center; }
 #qsbbgvmhip .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qsbbgvmhip .gt_font_normal { font-weight: normal; }
 #qsbbgvmhip .gt_font_bold { font-weight: bold; }
 #qsbbgvmhip .gt_font_italic { font-style: italic; }
 #qsbbgvmhip .gt_super { font-size: 65%; }
 #qsbbgvmhip .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qsbbgvmhip .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qsbbgvmhip .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qsbbgvmhip .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qsbbgvmhip .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qsbbgvmhip .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cckklafcqm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cckklafcqm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cckklafcqm p { margin: 0; padding: 0; }
 #cckklafcqm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cckklafcqm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cckklafcqm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cckklafcqm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cckklafcqm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cckklafcqm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cckklafcqm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cckklafcqm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cckklafcqm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cckklafcqm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cckklafcqm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cckklafcqm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cckklafcqm .gt_spanner_row { border-bottom-style: hidden; }
 #cckklafcqm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cckklafcqm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cckklafcqm .gt_from_md> :first-child { margin-top: 0; }
 #cckklafcqm .gt_from_md> :last-child { margin-bottom: 0; }
 #cckklafcqm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cckklafcqm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cckklafcqm .gt_indent_1 { text-indent: 5px; }
 #cckklafcqm .gt_indent_2 { text-indent: calc(5px * 2); }
 #cckklafcqm .gt_indent_3 { text-indent: calc(5px * 3); }
 #cckklafcqm .gt_indent_4 { text-indent: calc(5px * 4); }
 #cckklafcqm .gt_indent_5 { text-indent: calc(5px * 5); }
 #cckklafcqm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cckklafcqm .gt_row_group_first td { border-top-width: 2px; }
 #cckklafcqm .gt_row_group_first th { border-top-width: 2px; }
 #cckklafcqm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cckklafcqm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cckklafcqm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cckklafcqm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cckklafcqm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cckklafcqm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cckklafcqm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cckklafcqm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cckklafcqm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cckklafcqm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cckklafcqm .gt_left { text-align: left; }
 #cckklafcqm .gt_center { text-align: center; }
 #cckklafcqm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cckklafcqm .gt_font_normal { font-weight: normal; }
 #cckklafcqm .gt_font_bold { font-weight: bold; }
 #cckklafcqm .gt_font_italic { font-style: italic; }
 #cckklafcqm .gt_super { font-size: 65%; }
 #cckklafcqm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cckklafcqm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cckklafcqm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cckklafcqm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cckklafcqm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cckklafcqm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bpbzgknaba table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bpbzgknaba thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bpbzgknaba p { margin: 0; padding: 0; }
 #bpbzgknaba .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bpbzgknaba .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bpbzgknaba .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bpbzgknaba .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bpbzgknaba .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpbzgknaba .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpbzgknaba .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpbzgknaba .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bpbzgknaba .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bpbzgknaba .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bpbzgknaba .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bpbzgknaba .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bpbzgknaba .gt_spanner_row { border-bottom-style: hidden; }
 #bpbzgknaba .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bpbzgknaba .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bpbzgknaba .gt_from_md> :first-child { margin-top: 0; }
 #bpbzgknaba .gt_from_md> :last-child { margin-bottom: 0; }
 #bpbzgknaba .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bpbzgknaba .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bpbzgknaba .gt_indent_1 { text-indent: 5px; }
 #bpbzgknaba .gt_indent_2 { text-indent: calc(5px * 2); }
 #bpbzgknaba .gt_indent_3 { text-indent: calc(5px * 3); }
 #bpbzgknaba .gt_indent_4 { text-indent: calc(5px * 4); }
 #bpbzgknaba .gt_indent_5 { text-indent: calc(5px * 5); }
 #bpbzgknaba .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bpbzgknaba .gt_row_group_first td { border-top-width: 2px; }
 #bpbzgknaba .gt_row_group_first th { border-top-width: 2px; }
 #bpbzgknaba .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bpbzgknaba .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpbzgknaba .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpbzgknaba .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bpbzgknaba .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpbzgknaba .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpbzgknaba .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bpbzgknaba .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bpbzgknaba .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpbzgknaba .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpbzgknaba .gt_left { text-align: left; }
 #bpbzgknaba .gt_center { text-align: center; }
 #bpbzgknaba .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bpbzgknaba .gt_font_normal { font-weight: normal; }
 #bpbzgknaba .gt_font_bold { font-weight: bold; }
 #bpbzgknaba .gt_font_italic { font-style: italic; }
 #bpbzgknaba .gt_super { font-size: 65%; }
 #bpbzgknaba .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpbzgknaba .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bpbzgknaba .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpbzgknaba .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpbzgknaba .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bpbzgknaba .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hakmrxjugm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hakmrxjugm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hakmrxjugm p { margin: 0; padding: 0; }
 #hakmrxjugm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hakmrxjugm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hakmrxjugm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hakmrxjugm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hakmrxjugm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hakmrxjugm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hakmrxjugm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hakmrxjugm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hakmrxjugm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hakmrxjugm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hakmrxjugm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hakmrxjugm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hakmrxjugm .gt_spanner_row { border-bottom-style: hidden; }
 #hakmrxjugm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hakmrxjugm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hakmrxjugm .gt_from_md> :first-child { margin-top: 0; }
 #hakmrxjugm .gt_from_md> :last-child { margin-bottom: 0; }
 #hakmrxjugm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hakmrxjugm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hakmrxjugm .gt_indent_1 { text-indent: 5px; }
 #hakmrxjugm .gt_indent_2 { text-indent: calc(5px * 2); }
 #hakmrxjugm .gt_indent_3 { text-indent: calc(5px * 3); }
 #hakmrxjugm .gt_indent_4 { text-indent: calc(5px * 4); }
 #hakmrxjugm .gt_indent_5 { text-indent: calc(5px * 5); }
 #hakmrxjugm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hakmrxjugm .gt_row_group_first td { border-top-width: 2px; }
 #hakmrxjugm .gt_row_group_first th { border-top-width: 2px; }
 #hakmrxjugm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hakmrxjugm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hakmrxjugm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hakmrxjugm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hakmrxjugm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hakmrxjugm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hakmrxjugm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hakmrxjugm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hakmrxjugm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hakmrxjugm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hakmrxjugm .gt_left { text-align: left; }
 #hakmrxjugm .gt_center { text-align: center; }
 #hakmrxjugm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hakmrxjugm .gt_font_normal { font-weight: normal; }
 #hakmrxjugm .gt_font_bold { font-weight: bold; }
 #hakmrxjugm .gt_font_italic { font-style: italic; }
 #hakmrxjugm .gt_super { font-size: 65%; }
 #hakmrxjugm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hakmrxjugm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hakmrxjugm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hakmrxjugm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hakmrxjugm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hakmrxjugm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#aruxiflvhs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aruxiflvhs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aruxiflvhs p { margin: 0; padding: 0; }
 #aruxiflvhs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aruxiflvhs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aruxiflvhs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aruxiflvhs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aruxiflvhs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aruxiflvhs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aruxiflvhs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aruxiflvhs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #aruxiflvhs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aruxiflvhs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aruxiflvhs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aruxiflvhs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aruxiflvhs .gt_spanner_row { border-bottom-style: hidden; }
 #aruxiflvhs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aruxiflvhs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aruxiflvhs .gt_from_md> :first-child { margin-top: 0; }
 #aruxiflvhs .gt_from_md> :last-child { margin-bottom: 0; }
 #aruxiflvhs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aruxiflvhs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #aruxiflvhs .gt_indent_1 { text-indent: 5px; }
 #aruxiflvhs .gt_indent_2 { text-indent: calc(5px * 2); }
 #aruxiflvhs .gt_indent_3 { text-indent: calc(5px * 3); }
 #aruxiflvhs .gt_indent_4 { text-indent: calc(5px * 4); }
 #aruxiflvhs .gt_indent_5 { text-indent: calc(5px * 5); }
 #aruxiflvhs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #aruxiflvhs .gt_row_group_first td { border-top-width: 2px; }
 #aruxiflvhs .gt_row_group_first th { border-top-width: 2px; }
 #aruxiflvhs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aruxiflvhs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aruxiflvhs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aruxiflvhs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aruxiflvhs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aruxiflvhs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aruxiflvhs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aruxiflvhs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aruxiflvhs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aruxiflvhs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aruxiflvhs .gt_left { text-align: left; }
 #aruxiflvhs .gt_center { text-align: center; }
 #aruxiflvhs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aruxiflvhs .gt_font_normal { font-weight: normal; }
 #aruxiflvhs .gt_font_bold { font-weight: bold; }
 #aruxiflvhs .gt_font_italic { font-style: italic; }
 #aruxiflvhs .gt_super { font-size: 65%; }
 #aruxiflvhs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aruxiflvhs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aruxiflvhs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aruxiflvhs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aruxiflvhs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aruxiflvhs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gkvnhhbsib table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gkvnhhbsib thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gkvnhhbsib p { margin: 0; padding: 0; }
 #gkvnhhbsib .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gkvnhhbsib .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gkvnhhbsib .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gkvnhhbsib .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gkvnhhbsib .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gkvnhhbsib .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gkvnhhbsib .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gkvnhhbsib .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gkvnhhbsib .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gkvnhhbsib .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gkvnhhbsib .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gkvnhhbsib .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gkvnhhbsib .gt_spanner_row { border-bottom-style: hidden; }
 #gkvnhhbsib .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gkvnhhbsib .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gkvnhhbsib .gt_from_md> :first-child { margin-top: 0; }
 #gkvnhhbsib .gt_from_md> :last-child { margin-bottom: 0; }
 #gkvnhhbsib .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gkvnhhbsib .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gkvnhhbsib .gt_indent_1 { text-indent: 5px; }
 #gkvnhhbsib .gt_indent_2 { text-indent: calc(5px * 2); }
 #gkvnhhbsib .gt_indent_3 { text-indent: calc(5px * 3); }
 #gkvnhhbsib .gt_indent_4 { text-indent: calc(5px * 4); }
 #gkvnhhbsib .gt_indent_5 { text-indent: calc(5px * 5); }
 #gkvnhhbsib .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gkvnhhbsib .gt_row_group_first td { border-top-width: 2px; }
 #gkvnhhbsib .gt_row_group_first th { border-top-width: 2px; }
 #gkvnhhbsib .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gkvnhhbsib .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gkvnhhbsib .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gkvnhhbsib .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gkvnhhbsib .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gkvnhhbsib .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gkvnhhbsib .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gkvnhhbsib .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gkvnhhbsib .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gkvnhhbsib .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gkvnhhbsib .gt_left { text-align: left; }
 #gkvnhhbsib .gt_center { text-align: center; }
 #gkvnhhbsib .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gkvnhhbsib .gt_font_normal { font-weight: normal; }
 #gkvnhhbsib .gt_font_bold { font-weight: bold; }
 #gkvnhhbsib .gt_font_italic { font-style: italic; }
 #gkvnhhbsib .gt_super { font-size: 65%; }
 #gkvnhhbsib .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gkvnhhbsib .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gkvnhhbsib .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gkvnhhbsib .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gkvnhhbsib .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gkvnhhbsib .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tvgslrwqlw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tvgslrwqlw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tvgslrwqlw p { margin: 0; padding: 0; }
 #tvgslrwqlw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tvgslrwqlw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tvgslrwqlw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tvgslrwqlw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tvgslrwqlw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tvgslrwqlw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tvgslrwqlw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tvgslrwqlw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tvgslrwqlw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tvgslrwqlw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tvgslrwqlw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tvgslrwqlw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tvgslrwqlw .gt_spanner_row { border-bottom-style: hidden; }
 #tvgslrwqlw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tvgslrwqlw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tvgslrwqlw .gt_from_md> :first-child { margin-top: 0; }
 #tvgslrwqlw .gt_from_md> :last-child { margin-bottom: 0; }
 #tvgslrwqlw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tvgslrwqlw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tvgslrwqlw .gt_indent_1 { text-indent: 5px; }
 #tvgslrwqlw .gt_indent_2 { text-indent: calc(5px * 2); }
 #tvgslrwqlw .gt_indent_3 { text-indent: calc(5px * 3); }
 #tvgslrwqlw .gt_indent_4 { text-indent: calc(5px * 4); }
 #tvgslrwqlw .gt_indent_5 { text-indent: calc(5px * 5); }
 #tvgslrwqlw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tvgslrwqlw .gt_row_group_first td { border-top-width: 2px; }
 #tvgslrwqlw .gt_row_group_first th { border-top-width: 2px; }
 #tvgslrwqlw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tvgslrwqlw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tvgslrwqlw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tvgslrwqlw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tvgslrwqlw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tvgslrwqlw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tvgslrwqlw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tvgslrwqlw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tvgslrwqlw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tvgslrwqlw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tvgslrwqlw .gt_left { text-align: left; }
 #tvgslrwqlw .gt_center { text-align: center; }
 #tvgslrwqlw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tvgslrwqlw .gt_font_normal { font-weight: normal; }
 #tvgslrwqlw .gt_font_bold { font-weight: bold; }
 #tvgslrwqlw .gt_font_italic { font-style: italic; }
 #tvgslrwqlw .gt_super { font-size: 65%; }
 #tvgslrwqlw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tvgslrwqlw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tvgslrwqlw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tvgslrwqlw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tvgslrwqlw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tvgslrwqlw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zntzhmzxjl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zntzhmzxjl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zntzhmzxjl p { margin: 0; padding: 0; }
 #zntzhmzxjl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zntzhmzxjl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zntzhmzxjl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zntzhmzxjl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zntzhmzxjl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zntzhmzxjl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zntzhmzxjl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zntzhmzxjl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zntzhmzxjl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zntzhmzxjl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zntzhmzxjl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zntzhmzxjl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zntzhmzxjl .gt_spanner_row { border-bottom-style: hidden; }
 #zntzhmzxjl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zntzhmzxjl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zntzhmzxjl .gt_from_md> :first-child { margin-top: 0; }
 #zntzhmzxjl .gt_from_md> :last-child { margin-bottom: 0; }
 #zntzhmzxjl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zntzhmzxjl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zntzhmzxjl .gt_indent_1 { text-indent: 5px; }
 #zntzhmzxjl .gt_indent_2 { text-indent: calc(5px * 2); }
 #zntzhmzxjl .gt_indent_3 { text-indent: calc(5px * 3); }
 #zntzhmzxjl .gt_indent_4 { text-indent: calc(5px * 4); }
 #zntzhmzxjl .gt_indent_5 { text-indent: calc(5px * 5); }
 #zntzhmzxjl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zntzhmzxjl .gt_row_group_first td { border-top-width: 2px; }
 #zntzhmzxjl .gt_row_group_first th { border-top-width: 2px; }
 #zntzhmzxjl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zntzhmzxjl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zntzhmzxjl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zntzhmzxjl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zntzhmzxjl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zntzhmzxjl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zntzhmzxjl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zntzhmzxjl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zntzhmzxjl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zntzhmzxjl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zntzhmzxjl .gt_left { text-align: left; }
 #zntzhmzxjl .gt_center { text-align: center; }
 #zntzhmzxjl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zntzhmzxjl .gt_font_normal { font-weight: normal; }
 #zntzhmzxjl .gt_font_bold { font-weight: bold; }
 #zntzhmzxjl .gt_font_italic { font-style: italic; }
 #zntzhmzxjl .gt_super { font-size: 65%; }
 #zntzhmzxjl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zntzhmzxjl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zntzhmzxjl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zntzhmzxjl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zntzhmzxjl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zntzhmzxjl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rxwugohnko table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rxwugohnko thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rxwugohnko p { margin: 0; padding: 0; }
 #rxwugohnko .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rxwugohnko .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rxwugohnko .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rxwugohnko .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rxwugohnko .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rxwugohnko .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rxwugohnko .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rxwugohnko .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rxwugohnko .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rxwugohnko .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rxwugohnko .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rxwugohnko .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rxwugohnko .gt_spanner_row { border-bottom-style: hidden; }
 #rxwugohnko .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rxwugohnko .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rxwugohnko .gt_from_md> :first-child { margin-top: 0; }
 #rxwugohnko .gt_from_md> :last-child { margin-bottom: 0; }
 #rxwugohnko .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rxwugohnko .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rxwugohnko .gt_indent_1 { text-indent: 5px; }
 #rxwugohnko .gt_indent_2 { text-indent: calc(5px * 2); }
 #rxwugohnko .gt_indent_3 { text-indent: calc(5px * 3); }
 #rxwugohnko .gt_indent_4 { text-indent: calc(5px * 4); }
 #rxwugohnko .gt_indent_5 { text-indent: calc(5px * 5); }
 #rxwugohnko .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rxwugohnko .gt_row_group_first td { border-top-width: 2px; }
 #rxwugohnko .gt_row_group_first th { border-top-width: 2px; }
 #rxwugohnko .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rxwugohnko .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rxwugohnko .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rxwugohnko .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rxwugohnko .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rxwugohnko .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rxwugohnko .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rxwugohnko .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rxwugohnko .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rxwugohnko .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rxwugohnko .gt_left { text-align: left; }
 #rxwugohnko .gt_center { text-align: center; }
 #rxwugohnko .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rxwugohnko .gt_font_normal { font-weight: normal; }
 #rxwugohnko .gt_font_bold { font-weight: bold; }
 #rxwugohnko .gt_font_italic { font-style: italic; }
 #rxwugohnko .gt_super { font-size: 65%; }
 #rxwugohnko .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rxwugohnko .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rxwugohnko .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rxwugohnko .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rxwugohnko .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rxwugohnko .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hwsjdsfror table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hwsjdsfror thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hwsjdsfror p { margin: 0; padding: 0; }
 #hwsjdsfror .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hwsjdsfror .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hwsjdsfror .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hwsjdsfror .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hwsjdsfror .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hwsjdsfror .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hwsjdsfror .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hwsjdsfror .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hwsjdsfror .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hwsjdsfror .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hwsjdsfror .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hwsjdsfror .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hwsjdsfror .gt_spanner_row { border-bottom-style: hidden; }
 #hwsjdsfror .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hwsjdsfror .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hwsjdsfror .gt_from_md> :first-child { margin-top: 0; }
 #hwsjdsfror .gt_from_md> :last-child { margin-bottom: 0; }
 #hwsjdsfror .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hwsjdsfror .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hwsjdsfror .gt_indent_1 { text-indent: 5px; }
 #hwsjdsfror .gt_indent_2 { text-indent: calc(5px * 2); }
 #hwsjdsfror .gt_indent_3 { text-indent: calc(5px * 3); }
 #hwsjdsfror .gt_indent_4 { text-indent: calc(5px * 4); }
 #hwsjdsfror .gt_indent_5 { text-indent: calc(5px * 5); }
 #hwsjdsfror .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hwsjdsfror .gt_row_group_first td { border-top-width: 2px; }
 #hwsjdsfror .gt_row_group_first th { border-top-width: 2px; }
 #hwsjdsfror .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hwsjdsfror .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hwsjdsfror .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hwsjdsfror .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hwsjdsfror .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hwsjdsfror .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hwsjdsfror .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hwsjdsfror .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hwsjdsfror .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hwsjdsfror .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hwsjdsfror .gt_left { text-align: left; }
 #hwsjdsfror .gt_center { text-align: center; }
 #hwsjdsfror .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hwsjdsfror .gt_font_normal { font-weight: normal; }
 #hwsjdsfror .gt_font_bold { font-weight: bold; }
 #hwsjdsfror .gt_font_italic { font-style: italic; }
 #hwsjdsfror .gt_super { font-size: 65%; }
 #hwsjdsfror .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hwsjdsfror .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hwsjdsfror .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hwsjdsfror .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hwsjdsfror .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hwsjdsfror .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ybuxfaxquv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ybuxfaxquv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ybuxfaxquv p { margin: 0; padding: 0; }
 #ybuxfaxquv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ybuxfaxquv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ybuxfaxquv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ybuxfaxquv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ybuxfaxquv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ybuxfaxquv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ybuxfaxquv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ybuxfaxquv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ybuxfaxquv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ybuxfaxquv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ybuxfaxquv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ybuxfaxquv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ybuxfaxquv .gt_spanner_row { border-bottom-style: hidden; }
 #ybuxfaxquv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ybuxfaxquv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ybuxfaxquv .gt_from_md> :first-child { margin-top: 0; }
 #ybuxfaxquv .gt_from_md> :last-child { margin-bottom: 0; }
 #ybuxfaxquv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ybuxfaxquv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ybuxfaxquv .gt_indent_1 { text-indent: 5px; }
 #ybuxfaxquv .gt_indent_2 { text-indent: calc(5px * 2); }
 #ybuxfaxquv .gt_indent_3 { text-indent: calc(5px * 3); }
 #ybuxfaxquv .gt_indent_4 { text-indent: calc(5px * 4); }
 #ybuxfaxquv .gt_indent_5 { text-indent: calc(5px * 5); }
 #ybuxfaxquv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ybuxfaxquv .gt_row_group_first td { border-top-width: 2px; }
 #ybuxfaxquv .gt_row_group_first th { border-top-width: 2px; }
 #ybuxfaxquv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ybuxfaxquv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ybuxfaxquv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ybuxfaxquv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ybuxfaxquv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ybuxfaxquv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ybuxfaxquv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ybuxfaxquv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ybuxfaxquv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ybuxfaxquv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ybuxfaxquv .gt_left { text-align: left; }
 #ybuxfaxquv .gt_center { text-align: center; }
 #ybuxfaxquv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ybuxfaxquv .gt_font_normal { font-weight: normal; }
 #ybuxfaxquv .gt_font_bold { font-weight: bold; }
 #ybuxfaxquv .gt_font_italic { font-style: italic; }
 #ybuxfaxquv .gt_super { font-size: 65%; }
 #ybuxfaxquv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ybuxfaxquv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ybuxfaxquv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ybuxfaxquv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ybuxfaxquv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ybuxfaxquv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vpcnouhbjy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vpcnouhbjy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vpcnouhbjy p { margin: 0; padding: 0; }
 #vpcnouhbjy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vpcnouhbjy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vpcnouhbjy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vpcnouhbjy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vpcnouhbjy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vpcnouhbjy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vpcnouhbjy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vpcnouhbjy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vpcnouhbjy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vpcnouhbjy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vpcnouhbjy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vpcnouhbjy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vpcnouhbjy .gt_spanner_row { border-bottom-style: hidden; }
 #vpcnouhbjy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vpcnouhbjy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vpcnouhbjy .gt_from_md> :first-child { margin-top: 0; }
 #vpcnouhbjy .gt_from_md> :last-child { margin-bottom: 0; }
 #vpcnouhbjy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vpcnouhbjy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vpcnouhbjy .gt_indent_1 { text-indent: 5px; }
 #vpcnouhbjy .gt_indent_2 { text-indent: calc(5px * 2); }
 #vpcnouhbjy .gt_indent_3 { text-indent: calc(5px * 3); }
 #vpcnouhbjy .gt_indent_4 { text-indent: calc(5px * 4); }
 #vpcnouhbjy .gt_indent_5 { text-indent: calc(5px * 5); }
 #vpcnouhbjy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vpcnouhbjy .gt_row_group_first td { border-top-width: 2px; }
 #vpcnouhbjy .gt_row_group_first th { border-top-width: 2px; }
 #vpcnouhbjy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vpcnouhbjy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vpcnouhbjy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vpcnouhbjy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vpcnouhbjy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vpcnouhbjy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vpcnouhbjy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vpcnouhbjy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vpcnouhbjy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vpcnouhbjy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vpcnouhbjy .gt_left { text-align: left; }
 #vpcnouhbjy .gt_center { text-align: center; }
 #vpcnouhbjy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vpcnouhbjy .gt_font_normal { font-weight: normal; }
 #vpcnouhbjy .gt_font_bold { font-weight: bold; }
 #vpcnouhbjy .gt_font_italic { font-style: italic; }
 #vpcnouhbjy .gt_super { font-size: 65%; }
 #vpcnouhbjy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vpcnouhbjy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vpcnouhbjy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vpcnouhbjy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vpcnouhbjy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vpcnouhbjy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hehifrqmid table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hehifrqmid thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hehifrqmid p { margin: 0; padding: 0; }
 #hehifrqmid .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hehifrqmid .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hehifrqmid .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hehifrqmid .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hehifrqmid .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hehifrqmid .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hehifrqmid .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hehifrqmid .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hehifrqmid .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hehifrqmid .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hehifrqmid .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hehifrqmid .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hehifrqmid .gt_spanner_row { border-bottom-style: hidden; }
 #hehifrqmid .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hehifrqmid .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hehifrqmid .gt_from_md> :first-child { margin-top: 0; }
 #hehifrqmid .gt_from_md> :last-child { margin-bottom: 0; }
 #hehifrqmid .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hehifrqmid .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hehifrqmid .gt_indent_1 { text-indent: 5px; }
 #hehifrqmid .gt_indent_2 { text-indent: calc(5px * 2); }
 #hehifrqmid .gt_indent_3 { text-indent: calc(5px * 3); }
 #hehifrqmid .gt_indent_4 { text-indent: calc(5px * 4); }
 #hehifrqmid .gt_indent_5 { text-indent: calc(5px * 5); }
 #hehifrqmid .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hehifrqmid .gt_row_group_first td { border-top-width: 2px; }
 #hehifrqmid .gt_row_group_first th { border-top-width: 2px; }
 #hehifrqmid .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hehifrqmid .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hehifrqmid .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hehifrqmid .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hehifrqmid .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hehifrqmid .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hehifrqmid .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hehifrqmid .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hehifrqmid .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hehifrqmid .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hehifrqmid .gt_left { text-align: left; }
 #hehifrqmid .gt_center { text-align: center; }
 #hehifrqmid .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hehifrqmid .gt_font_normal { font-weight: normal; }
 #hehifrqmid .gt_font_bold { font-weight: bold; }
 #hehifrqmid .gt_font_italic { font-style: italic; }
 #hehifrqmid .gt_super { font-size: 65%; }
 #hehifrqmid .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hehifrqmid .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hehifrqmid .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hehifrqmid .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hehifrqmid .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hehifrqmid .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#giuaexsiww table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#giuaexsiww thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#giuaexsiww p { margin: 0; padding: 0; }
 #giuaexsiww .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #giuaexsiww .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #giuaexsiww .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #giuaexsiww .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #giuaexsiww .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #giuaexsiww .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #giuaexsiww .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #giuaexsiww .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #giuaexsiww .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #giuaexsiww .gt_column_spanner_outer:first-child { padding-left: 0; }
 #giuaexsiww .gt_column_spanner_outer:last-child { padding-right: 0; }
 #giuaexsiww .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #giuaexsiww .gt_spanner_row { border-bottom-style: hidden; }
 #giuaexsiww .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #giuaexsiww .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #giuaexsiww .gt_from_md> :first-child { margin-top: 0; }
 #giuaexsiww .gt_from_md> :last-child { margin-bottom: 0; }
 #giuaexsiww .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #giuaexsiww .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #giuaexsiww .gt_indent_1 { text-indent: 5px; }
 #giuaexsiww .gt_indent_2 { text-indent: calc(5px * 2); }
 #giuaexsiww .gt_indent_3 { text-indent: calc(5px * 3); }
 #giuaexsiww .gt_indent_4 { text-indent: calc(5px * 4); }
 #giuaexsiww .gt_indent_5 { text-indent: calc(5px * 5); }
 #giuaexsiww .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #giuaexsiww .gt_row_group_first td { border-top-width: 2px; }
 #giuaexsiww .gt_row_group_first th { border-top-width: 2px; }
 #giuaexsiww .gt_striped { color: #333333; background-color: #F4F4F4; }
 #giuaexsiww .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #giuaexsiww .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #giuaexsiww .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #giuaexsiww .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #giuaexsiww .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #giuaexsiww .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #giuaexsiww .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #giuaexsiww .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #giuaexsiww .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #giuaexsiww .gt_left { text-align: left; }
 #giuaexsiww .gt_center { text-align: center; }
 #giuaexsiww .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #giuaexsiww .gt_font_normal { font-weight: normal; }
 #giuaexsiww .gt_font_bold { font-weight: bold; }
 #giuaexsiww .gt_font_italic { font-style: italic; }
 #giuaexsiww .gt_super { font-size: 65%; }
 #giuaexsiww .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #giuaexsiww .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #giuaexsiww .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #giuaexsiww .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #giuaexsiww .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #giuaexsiww .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dgbrbramnf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dgbrbramnf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dgbrbramnf p { margin: 0; padding: 0; }
 #dgbrbramnf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dgbrbramnf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dgbrbramnf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dgbrbramnf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dgbrbramnf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dgbrbramnf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dgbrbramnf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dgbrbramnf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dgbrbramnf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dgbrbramnf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dgbrbramnf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dgbrbramnf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dgbrbramnf .gt_spanner_row { border-bottom-style: hidden; }
 #dgbrbramnf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dgbrbramnf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dgbrbramnf .gt_from_md> :first-child { margin-top: 0; }
 #dgbrbramnf .gt_from_md> :last-child { margin-bottom: 0; }
 #dgbrbramnf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dgbrbramnf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dgbrbramnf .gt_indent_1 { text-indent: 5px; }
 #dgbrbramnf .gt_indent_2 { text-indent: calc(5px * 2); }
 #dgbrbramnf .gt_indent_3 { text-indent: calc(5px * 3); }
 #dgbrbramnf .gt_indent_4 { text-indent: calc(5px * 4); }
 #dgbrbramnf .gt_indent_5 { text-indent: calc(5px * 5); }
 #dgbrbramnf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dgbrbramnf .gt_row_group_first td { border-top-width: 2px; }
 #dgbrbramnf .gt_row_group_first th { border-top-width: 2px; }
 #dgbrbramnf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dgbrbramnf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dgbrbramnf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dgbrbramnf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dgbrbramnf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dgbrbramnf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dgbrbramnf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dgbrbramnf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dgbrbramnf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dgbrbramnf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dgbrbramnf .gt_left { text-align: left; }
 #dgbrbramnf .gt_center { text-align: center; }
 #dgbrbramnf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dgbrbramnf .gt_font_normal { font-weight: normal; }
 #dgbrbramnf .gt_font_bold { font-weight: bold; }
 #dgbrbramnf .gt_font_italic { font-style: italic; }
 #dgbrbramnf .gt_super { font-size: 65%; }
 #dgbrbramnf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dgbrbramnf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dgbrbramnf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dgbrbramnf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dgbrbramnf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dgbrbramnf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kqbdenfwma table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kqbdenfwma thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kqbdenfwma p { margin: 0; padding: 0; }
 #kqbdenfwma .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kqbdenfwma .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kqbdenfwma .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kqbdenfwma .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kqbdenfwma .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kqbdenfwma .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqbdenfwma .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kqbdenfwma .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kqbdenfwma .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kqbdenfwma .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kqbdenfwma .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kqbdenfwma .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kqbdenfwma .gt_spanner_row { border-bottom-style: hidden; }
 #kqbdenfwma .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kqbdenfwma .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kqbdenfwma .gt_from_md> :first-child { margin-top: 0; }
 #kqbdenfwma .gt_from_md> :last-child { margin-bottom: 0; }
 #kqbdenfwma .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kqbdenfwma .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kqbdenfwma .gt_indent_1 { text-indent: 5px; }
 #kqbdenfwma .gt_indent_2 { text-indent: calc(5px * 2); }
 #kqbdenfwma .gt_indent_3 { text-indent: calc(5px * 3); }
 #kqbdenfwma .gt_indent_4 { text-indent: calc(5px * 4); }
 #kqbdenfwma .gt_indent_5 { text-indent: calc(5px * 5); }
 #kqbdenfwma .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kqbdenfwma .gt_row_group_first td { border-top-width: 2px; }
 #kqbdenfwma .gt_row_group_first th { border-top-width: 2px; }
 #kqbdenfwma .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kqbdenfwma .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqbdenfwma .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kqbdenfwma .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kqbdenfwma .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqbdenfwma .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kqbdenfwma .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kqbdenfwma .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kqbdenfwma .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqbdenfwma .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kqbdenfwma .gt_left { text-align: left; }
 #kqbdenfwma .gt_center { text-align: center; }
 #kqbdenfwma .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kqbdenfwma .gt_font_normal { font-weight: normal; }
 #kqbdenfwma .gt_font_bold { font-weight: bold; }
 #kqbdenfwma .gt_font_italic { font-style: italic; }
 #kqbdenfwma .gt_super { font-size: 65%; }
 #kqbdenfwma .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqbdenfwma .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kqbdenfwma .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqbdenfwma .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kqbdenfwma .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kqbdenfwma .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
