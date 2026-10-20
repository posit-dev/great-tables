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
#fvpancjhlg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fvpancjhlg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fvpancjhlg p { margin: 0; padding: 0; }
 #fvpancjhlg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fvpancjhlg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fvpancjhlg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fvpancjhlg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fvpancjhlg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fvpancjhlg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fvpancjhlg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fvpancjhlg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fvpancjhlg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fvpancjhlg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fvpancjhlg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fvpancjhlg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fvpancjhlg .gt_spanner_row { border-bottom-style: hidden; }
 #fvpancjhlg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fvpancjhlg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fvpancjhlg .gt_from_md> :first-child { margin-top: 0; }
 #fvpancjhlg .gt_from_md> :last-child { margin-bottom: 0; }
 #fvpancjhlg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fvpancjhlg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fvpancjhlg .gt_indent_1 { text-indent: 5px; }
 #fvpancjhlg .gt_indent_2 { text-indent: calc(5px * 2); }
 #fvpancjhlg .gt_indent_3 { text-indent: calc(5px * 3); }
 #fvpancjhlg .gt_indent_4 { text-indent: calc(5px * 4); }
 #fvpancjhlg .gt_indent_5 { text-indent: calc(5px * 5); }
 #fvpancjhlg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fvpancjhlg .gt_row_group_first td { border-top-width: 2px; }
 #fvpancjhlg .gt_row_group_first th { border-top-width: 2px; }
 #fvpancjhlg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fvpancjhlg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fvpancjhlg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fvpancjhlg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fvpancjhlg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fvpancjhlg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fvpancjhlg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fvpancjhlg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fvpancjhlg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fvpancjhlg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fvpancjhlg .gt_left { text-align: left; }
 #fvpancjhlg .gt_center { text-align: center; }
 #fvpancjhlg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fvpancjhlg .gt_font_normal { font-weight: normal; }
 #fvpancjhlg .gt_font_bold { font-weight: bold; }
 #fvpancjhlg .gt_font_italic { font-style: italic; }
 #fvpancjhlg .gt_super { font-size: 65%; }
 #fvpancjhlg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fvpancjhlg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fvpancjhlg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fvpancjhlg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fvpancjhlg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fvpancjhlg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dikckzhqxa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dikckzhqxa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dikckzhqxa p { margin: 0; padding: 0; }
 #dikckzhqxa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dikckzhqxa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dikckzhqxa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dikckzhqxa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dikckzhqxa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dikckzhqxa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dikckzhqxa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dikckzhqxa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dikckzhqxa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dikckzhqxa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dikckzhqxa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dikckzhqxa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dikckzhqxa .gt_spanner_row { border-bottom-style: hidden; }
 #dikckzhqxa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dikckzhqxa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dikckzhqxa .gt_from_md> :first-child { margin-top: 0; }
 #dikckzhqxa .gt_from_md> :last-child { margin-bottom: 0; }
 #dikckzhqxa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dikckzhqxa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dikckzhqxa .gt_indent_1 { text-indent: 5px; }
 #dikckzhqxa .gt_indent_2 { text-indent: calc(5px * 2); }
 #dikckzhqxa .gt_indent_3 { text-indent: calc(5px * 3); }
 #dikckzhqxa .gt_indent_4 { text-indent: calc(5px * 4); }
 #dikckzhqxa .gt_indent_5 { text-indent: calc(5px * 5); }
 #dikckzhqxa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dikckzhqxa .gt_row_group_first td { border-top-width: 2px; }
 #dikckzhqxa .gt_row_group_first th { border-top-width: 2px; }
 #dikckzhqxa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dikckzhqxa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dikckzhqxa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dikckzhqxa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dikckzhqxa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dikckzhqxa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dikckzhqxa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dikckzhqxa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dikckzhqxa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dikckzhqxa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dikckzhqxa .gt_left { text-align: left; }
 #dikckzhqxa .gt_center { text-align: center; }
 #dikckzhqxa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dikckzhqxa .gt_font_normal { font-weight: normal; }
 #dikckzhqxa .gt_font_bold { font-weight: bold; }
 #dikckzhqxa .gt_font_italic { font-style: italic; }
 #dikckzhqxa .gt_super { font-size: 65%; }
 #dikckzhqxa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dikckzhqxa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dikckzhqxa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dikckzhqxa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dikckzhqxa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dikckzhqxa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dtjipobfng table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dtjipobfng thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dtjipobfng p { margin: 0; padding: 0; }
 #dtjipobfng .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dtjipobfng .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dtjipobfng .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dtjipobfng .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dtjipobfng .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dtjipobfng .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dtjipobfng .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dtjipobfng .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dtjipobfng .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dtjipobfng .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dtjipobfng .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dtjipobfng .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dtjipobfng .gt_spanner_row { border-bottom-style: hidden; }
 #dtjipobfng .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dtjipobfng .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dtjipobfng .gt_from_md> :first-child { margin-top: 0; }
 #dtjipobfng .gt_from_md> :last-child { margin-bottom: 0; }
 #dtjipobfng .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dtjipobfng .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dtjipobfng .gt_indent_1 { text-indent: 5px; }
 #dtjipobfng .gt_indent_2 { text-indent: calc(5px * 2); }
 #dtjipobfng .gt_indent_3 { text-indent: calc(5px * 3); }
 #dtjipobfng .gt_indent_4 { text-indent: calc(5px * 4); }
 #dtjipobfng .gt_indent_5 { text-indent: calc(5px * 5); }
 #dtjipobfng .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dtjipobfng .gt_row_group_first td { border-top-width: 2px; }
 #dtjipobfng .gt_row_group_first th { border-top-width: 2px; }
 #dtjipobfng .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dtjipobfng .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dtjipobfng .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dtjipobfng .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dtjipobfng .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dtjipobfng .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dtjipobfng .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dtjipobfng .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dtjipobfng .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dtjipobfng .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dtjipobfng .gt_left { text-align: left; }
 #dtjipobfng .gt_center { text-align: center; }
 #dtjipobfng .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dtjipobfng .gt_font_normal { font-weight: normal; }
 #dtjipobfng .gt_font_bold { font-weight: bold; }
 #dtjipobfng .gt_font_italic { font-style: italic; }
 #dtjipobfng .gt_super { font-size: 65%; }
 #dtjipobfng .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dtjipobfng .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dtjipobfng .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dtjipobfng .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dtjipobfng .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dtjipobfng .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ksohrsyeon table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ksohrsyeon thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ksohrsyeon p { margin: 0; padding: 0; }
 #ksohrsyeon .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ksohrsyeon .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ksohrsyeon .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ksohrsyeon .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ksohrsyeon .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ksohrsyeon .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksohrsyeon .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ksohrsyeon .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ksohrsyeon .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ksohrsyeon .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ksohrsyeon .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ksohrsyeon .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ksohrsyeon .gt_spanner_row { border-bottom-style: hidden; }
 #ksohrsyeon .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ksohrsyeon .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ksohrsyeon .gt_from_md> :first-child { margin-top: 0; }
 #ksohrsyeon .gt_from_md> :last-child { margin-bottom: 0; }
 #ksohrsyeon .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ksohrsyeon .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ksohrsyeon .gt_indent_1 { text-indent: 5px; }
 #ksohrsyeon .gt_indent_2 { text-indent: calc(5px * 2); }
 #ksohrsyeon .gt_indent_3 { text-indent: calc(5px * 3); }
 #ksohrsyeon .gt_indent_4 { text-indent: calc(5px * 4); }
 #ksohrsyeon .gt_indent_5 { text-indent: calc(5px * 5); }
 #ksohrsyeon .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ksohrsyeon .gt_row_group_first td { border-top-width: 2px; }
 #ksohrsyeon .gt_row_group_first th { border-top-width: 2px; }
 #ksohrsyeon .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ksohrsyeon .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksohrsyeon .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ksohrsyeon .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ksohrsyeon .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksohrsyeon .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ksohrsyeon .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ksohrsyeon .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ksohrsyeon .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksohrsyeon .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ksohrsyeon .gt_left { text-align: left; }
 #ksohrsyeon .gt_center { text-align: center; }
 #ksohrsyeon .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ksohrsyeon .gt_font_normal { font-weight: normal; }
 #ksohrsyeon .gt_font_bold { font-weight: bold; }
 #ksohrsyeon .gt_font_italic { font-style: italic; }
 #ksohrsyeon .gt_super { font-size: 65%; }
 #ksohrsyeon .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksohrsyeon .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ksohrsyeon .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksohrsyeon .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ksohrsyeon .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ksohrsyeon .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xsqnflvxel table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xsqnflvxel thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xsqnflvxel p { margin: 0; padding: 0; }
 #xsqnflvxel .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xsqnflvxel .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xsqnflvxel .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xsqnflvxel .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xsqnflvxel .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xsqnflvxel .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xsqnflvxel .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xsqnflvxel .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xsqnflvxel .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xsqnflvxel .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xsqnflvxel .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xsqnflvxel .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xsqnflvxel .gt_spanner_row { border-bottom-style: hidden; }
 #xsqnflvxel .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xsqnflvxel .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xsqnflvxel .gt_from_md> :first-child { margin-top: 0; }
 #xsqnflvxel .gt_from_md> :last-child { margin-bottom: 0; }
 #xsqnflvxel .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xsqnflvxel .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xsqnflvxel .gt_indent_1 { text-indent: 5px; }
 #xsqnflvxel .gt_indent_2 { text-indent: calc(5px * 2); }
 #xsqnflvxel .gt_indent_3 { text-indent: calc(5px * 3); }
 #xsqnflvxel .gt_indent_4 { text-indent: calc(5px * 4); }
 #xsqnflvxel .gt_indent_5 { text-indent: calc(5px * 5); }
 #xsqnflvxel .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xsqnflvxel .gt_row_group_first td { border-top-width: 2px; }
 #xsqnflvxel .gt_row_group_first th { border-top-width: 2px; }
 #xsqnflvxel .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xsqnflvxel .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xsqnflvxel .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xsqnflvxel .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xsqnflvxel .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xsqnflvxel .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xsqnflvxel .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xsqnflvxel .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xsqnflvxel .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xsqnflvxel .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xsqnflvxel .gt_left { text-align: left; }
 #xsqnflvxel .gt_center { text-align: center; }
 #xsqnflvxel .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xsqnflvxel .gt_font_normal { font-weight: normal; }
 #xsqnflvxel .gt_font_bold { font-weight: bold; }
 #xsqnflvxel .gt_font_italic { font-style: italic; }
 #xsqnflvxel .gt_super { font-size: 65%; }
 #xsqnflvxel .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xsqnflvxel .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xsqnflvxel .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xsqnflvxel .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xsqnflvxel .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xsqnflvxel .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rdswbhhcrd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rdswbhhcrd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rdswbhhcrd p { margin: 0; padding: 0; }
 #rdswbhhcrd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rdswbhhcrd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rdswbhhcrd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rdswbhhcrd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rdswbhhcrd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rdswbhhcrd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdswbhhcrd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rdswbhhcrd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rdswbhhcrd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rdswbhhcrd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rdswbhhcrd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rdswbhhcrd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rdswbhhcrd .gt_spanner_row { border-bottom-style: hidden; }
 #rdswbhhcrd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rdswbhhcrd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rdswbhhcrd .gt_from_md> :first-child { margin-top: 0; }
 #rdswbhhcrd .gt_from_md> :last-child { margin-bottom: 0; }
 #rdswbhhcrd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rdswbhhcrd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rdswbhhcrd .gt_indent_1 { text-indent: 5px; }
 #rdswbhhcrd .gt_indent_2 { text-indent: calc(5px * 2); }
 #rdswbhhcrd .gt_indent_3 { text-indent: calc(5px * 3); }
 #rdswbhhcrd .gt_indent_4 { text-indent: calc(5px * 4); }
 #rdswbhhcrd .gt_indent_5 { text-indent: calc(5px * 5); }
 #rdswbhhcrd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rdswbhhcrd .gt_row_group_first td { border-top-width: 2px; }
 #rdswbhhcrd .gt_row_group_first th { border-top-width: 2px; }
 #rdswbhhcrd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rdswbhhcrd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdswbhhcrd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rdswbhhcrd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rdswbhhcrd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdswbhhcrd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rdswbhhcrd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rdswbhhcrd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rdswbhhcrd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdswbhhcrd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rdswbhhcrd .gt_left { text-align: left; }
 #rdswbhhcrd .gt_center { text-align: center; }
 #rdswbhhcrd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rdswbhhcrd .gt_font_normal { font-weight: normal; }
 #rdswbhhcrd .gt_font_bold { font-weight: bold; }
 #rdswbhhcrd .gt_font_italic { font-style: italic; }
 #rdswbhhcrd .gt_super { font-size: 65%; }
 #rdswbhhcrd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdswbhhcrd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rdswbhhcrd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdswbhhcrd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rdswbhhcrd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rdswbhhcrd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#nupeizyves table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nupeizyves thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nupeizyves p { margin: 0; padding: 0; }
 #nupeizyves .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nupeizyves .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nupeizyves .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nupeizyves .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nupeizyves .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nupeizyves .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nupeizyves .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nupeizyves .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nupeizyves .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nupeizyves .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nupeizyves .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nupeizyves .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nupeizyves .gt_spanner_row { border-bottom-style: hidden; }
 #nupeizyves .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nupeizyves .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nupeizyves .gt_from_md> :first-child { margin-top: 0; }
 #nupeizyves .gt_from_md> :last-child { margin-bottom: 0; }
 #nupeizyves .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nupeizyves .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nupeizyves .gt_indent_1 { text-indent: 5px; }
 #nupeizyves .gt_indent_2 { text-indent: calc(5px * 2); }
 #nupeizyves .gt_indent_3 { text-indent: calc(5px * 3); }
 #nupeizyves .gt_indent_4 { text-indent: calc(5px * 4); }
 #nupeizyves .gt_indent_5 { text-indent: calc(5px * 5); }
 #nupeizyves .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nupeizyves .gt_row_group_first td { border-top-width: 2px; }
 #nupeizyves .gt_row_group_first th { border-top-width: 2px; }
 #nupeizyves .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nupeizyves .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nupeizyves .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nupeizyves .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nupeizyves .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nupeizyves .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nupeizyves .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nupeizyves .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nupeizyves .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nupeizyves .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nupeizyves .gt_left { text-align: left; }
 #nupeizyves .gt_center { text-align: center; }
 #nupeizyves .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nupeizyves .gt_font_normal { font-weight: normal; }
 #nupeizyves .gt_font_bold { font-weight: bold; }
 #nupeizyves .gt_font_italic { font-style: italic; }
 #nupeizyves .gt_super { font-size: 65%; }
 #nupeizyves .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nupeizyves .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nupeizyves .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nupeizyves .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nupeizyves .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nupeizyves .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hcuzkacsde table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hcuzkacsde thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hcuzkacsde p { margin: 0; padding: 0; }
 #hcuzkacsde .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hcuzkacsde .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hcuzkacsde .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hcuzkacsde .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hcuzkacsde .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hcuzkacsde .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hcuzkacsde .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hcuzkacsde .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hcuzkacsde .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hcuzkacsde .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hcuzkacsde .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hcuzkacsde .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hcuzkacsde .gt_spanner_row { border-bottom-style: hidden; }
 #hcuzkacsde .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hcuzkacsde .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hcuzkacsde .gt_from_md> :first-child { margin-top: 0; }
 #hcuzkacsde .gt_from_md> :last-child { margin-bottom: 0; }
 #hcuzkacsde .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hcuzkacsde .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hcuzkacsde .gt_indent_1 { text-indent: 5px; }
 #hcuzkacsde .gt_indent_2 { text-indent: calc(5px * 2); }
 #hcuzkacsde .gt_indent_3 { text-indent: calc(5px * 3); }
 #hcuzkacsde .gt_indent_4 { text-indent: calc(5px * 4); }
 #hcuzkacsde .gt_indent_5 { text-indent: calc(5px * 5); }
 #hcuzkacsde .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hcuzkacsde .gt_row_group_first td { border-top-width: 2px; }
 #hcuzkacsde .gt_row_group_first th { border-top-width: 2px; }
 #hcuzkacsde .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hcuzkacsde .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hcuzkacsde .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hcuzkacsde .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hcuzkacsde .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hcuzkacsde .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hcuzkacsde .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hcuzkacsde .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hcuzkacsde .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hcuzkacsde .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hcuzkacsde .gt_left { text-align: left; }
 #hcuzkacsde .gt_center { text-align: center; }
 #hcuzkacsde .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hcuzkacsde .gt_font_normal { font-weight: normal; }
 #hcuzkacsde .gt_font_bold { font-weight: bold; }
 #hcuzkacsde .gt_font_italic { font-style: italic; }
 #hcuzkacsde .gt_super { font-size: 65%; }
 #hcuzkacsde .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hcuzkacsde .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hcuzkacsde .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hcuzkacsde .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hcuzkacsde .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hcuzkacsde .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#eykliblfje table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eykliblfje thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eykliblfje p { margin: 0; padding: 0; }
 #eykliblfje .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eykliblfje .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eykliblfje .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eykliblfje .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eykliblfje .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eykliblfje .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eykliblfje .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eykliblfje .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eykliblfje .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eykliblfje .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eykliblfje .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eykliblfje .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eykliblfje .gt_spanner_row { border-bottom-style: hidden; }
 #eykliblfje .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eykliblfje .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eykliblfje .gt_from_md> :first-child { margin-top: 0; }
 #eykliblfje .gt_from_md> :last-child { margin-bottom: 0; }
 #eykliblfje .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eykliblfje .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eykliblfje .gt_indent_1 { text-indent: 5px; }
 #eykliblfje .gt_indent_2 { text-indent: calc(5px * 2); }
 #eykliblfje .gt_indent_3 { text-indent: calc(5px * 3); }
 #eykliblfje .gt_indent_4 { text-indent: calc(5px * 4); }
 #eykliblfje .gt_indent_5 { text-indent: calc(5px * 5); }
 #eykliblfje .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eykliblfje .gt_row_group_first td { border-top-width: 2px; }
 #eykliblfje .gt_row_group_first th { border-top-width: 2px; }
 #eykliblfje .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eykliblfje .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eykliblfje .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eykliblfje .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eykliblfje .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eykliblfje .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eykliblfje .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eykliblfje .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eykliblfje .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eykliblfje .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eykliblfje .gt_left { text-align: left; }
 #eykliblfje .gt_center { text-align: center; }
 #eykliblfje .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eykliblfje .gt_font_normal { font-weight: normal; }
 #eykliblfje .gt_font_bold { font-weight: bold; }
 #eykliblfje .gt_font_italic { font-style: italic; }
 #eykliblfje .gt_super { font-size: 65%; }
 #eykliblfje .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eykliblfje .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eykliblfje .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eykliblfje .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eykliblfje .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eykliblfje .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xspegumqby table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xspegumqby thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xspegumqby p { margin: 0; padding: 0; }
 #xspegumqby .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xspegumqby .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xspegumqby .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xspegumqby .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xspegumqby .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xspegumqby .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xspegumqby .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xspegumqby .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xspegumqby .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xspegumqby .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xspegumqby .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xspegumqby .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xspegumqby .gt_spanner_row { border-bottom-style: hidden; }
 #xspegumqby .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xspegumqby .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xspegumqby .gt_from_md> :first-child { margin-top: 0; }
 #xspegumqby .gt_from_md> :last-child { margin-bottom: 0; }
 #xspegumqby .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xspegumqby .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xspegumqby .gt_indent_1 { text-indent: 5px; }
 #xspegumqby .gt_indent_2 { text-indent: calc(5px * 2); }
 #xspegumqby .gt_indent_3 { text-indent: calc(5px * 3); }
 #xspegumqby .gt_indent_4 { text-indent: calc(5px * 4); }
 #xspegumqby .gt_indent_5 { text-indent: calc(5px * 5); }
 #xspegumqby .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xspegumqby .gt_row_group_first td { border-top-width: 2px; }
 #xspegumqby .gt_row_group_first th { border-top-width: 2px; }
 #xspegumqby .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xspegumqby .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xspegumqby .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xspegumqby .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xspegumqby .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xspegumqby .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xspegumqby .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xspegumqby .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xspegumqby .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xspegumqby .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xspegumqby .gt_left { text-align: left; }
 #xspegumqby .gt_center { text-align: center; }
 #xspegumqby .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xspegumqby .gt_font_normal { font-weight: normal; }
 #xspegumqby .gt_font_bold { font-weight: bold; }
 #xspegumqby .gt_font_italic { font-style: italic; }
 #xspegumqby .gt_super { font-size: 65%; }
 #xspegumqby .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xspegumqby .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xspegumqby .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xspegumqby .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xspegumqby .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xspegumqby .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#edvyihldvf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#edvyihldvf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#edvyihldvf p { margin: 0; padding: 0; }
 #edvyihldvf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #edvyihldvf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #edvyihldvf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #edvyihldvf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #edvyihldvf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #edvyihldvf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #edvyihldvf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #edvyihldvf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #edvyihldvf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #edvyihldvf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #edvyihldvf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #edvyihldvf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #edvyihldvf .gt_spanner_row { border-bottom-style: hidden; }
 #edvyihldvf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #edvyihldvf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #edvyihldvf .gt_from_md> :first-child { margin-top: 0; }
 #edvyihldvf .gt_from_md> :last-child { margin-bottom: 0; }
 #edvyihldvf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #edvyihldvf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #edvyihldvf .gt_indent_1 { text-indent: 5px; }
 #edvyihldvf .gt_indent_2 { text-indent: calc(5px * 2); }
 #edvyihldvf .gt_indent_3 { text-indent: calc(5px * 3); }
 #edvyihldvf .gt_indent_4 { text-indent: calc(5px * 4); }
 #edvyihldvf .gt_indent_5 { text-indent: calc(5px * 5); }
 #edvyihldvf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #edvyihldvf .gt_row_group_first td { border-top-width: 2px; }
 #edvyihldvf .gt_row_group_first th { border-top-width: 2px; }
 #edvyihldvf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #edvyihldvf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #edvyihldvf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #edvyihldvf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #edvyihldvf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #edvyihldvf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #edvyihldvf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #edvyihldvf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #edvyihldvf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edvyihldvf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #edvyihldvf .gt_left { text-align: left; }
 #edvyihldvf .gt_center { text-align: center; }
 #edvyihldvf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #edvyihldvf .gt_font_normal { font-weight: normal; }
 #edvyihldvf .gt_font_bold { font-weight: bold; }
 #edvyihldvf .gt_font_italic { font-style: italic; }
 #edvyihldvf .gt_super { font-size: 65%; }
 #edvyihldvf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edvyihldvf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #edvyihldvf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edvyihldvf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #edvyihldvf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #edvyihldvf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#luytnvfdxr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#luytnvfdxr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#luytnvfdxr p { margin: 0; padding: 0; }
 #luytnvfdxr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #luytnvfdxr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #luytnvfdxr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #luytnvfdxr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #luytnvfdxr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #luytnvfdxr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #luytnvfdxr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #luytnvfdxr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #luytnvfdxr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #luytnvfdxr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #luytnvfdxr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #luytnvfdxr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #luytnvfdxr .gt_spanner_row { border-bottom-style: hidden; }
 #luytnvfdxr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #luytnvfdxr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #luytnvfdxr .gt_from_md> :first-child { margin-top: 0; }
 #luytnvfdxr .gt_from_md> :last-child { margin-bottom: 0; }
 #luytnvfdxr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #luytnvfdxr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #luytnvfdxr .gt_indent_1 { text-indent: 5px; }
 #luytnvfdxr .gt_indent_2 { text-indent: calc(5px * 2); }
 #luytnvfdxr .gt_indent_3 { text-indent: calc(5px * 3); }
 #luytnvfdxr .gt_indent_4 { text-indent: calc(5px * 4); }
 #luytnvfdxr .gt_indent_5 { text-indent: calc(5px * 5); }
 #luytnvfdxr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #luytnvfdxr .gt_row_group_first td { border-top-width: 2px; }
 #luytnvfdxr .gt_row_group_first th { border-top-width: 2px; }
 #luytnvfdxr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #luytnvfdxr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #luytnvfdxr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #luytnvfdxr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #luytnvfdxr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #luytnvfdxr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #luytnvfdxr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #luytnvfdxr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #luytnvfdxr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #luytnvfdxr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #luytnvfdxr .gt_left { text-align: left; }
 #luytnvfdxr .gt_center { text-align: center; }
 #luytnvfdxr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #luytnvfdxr .gt_font_normal { font-weight: normal; }
 #luytnvfdxr .gt_font_bold { font-weight: bold; }
 #luytnvfdxr .gt_font_italic { font-style: italic; }
 #luytnvfdxr .gt_super { font-size: 65%; }
 #luytnvfdxr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #luytnvfdxr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #luytnvfdxr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #luytnvfdxr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #luytnvfdxr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #luytnvfdxr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bwabnfwqfq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bwabnfwqfq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bwabnfwqfq p { margin: 0; padding: 0; }
 #bwabnfwqfq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bwabnfwqfq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bwabnfwqfq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bwabnfwqfq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bwabnfwqfq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bwabnfwqfq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bwabnfwqfq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bwabnfwqfq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bwabnfwqfq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bwabnfwqfq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bwabnfwqfq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bwabnfwqfq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bwabnfwqfq .gt_spanner_row { border-bottom-style: hidden; }
 #bwabnfwqfq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bwabnfwqfq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bwabnfwqfq .gt_from_md> :first-child { margin-top: 0; }
 #bwabnfwqfq .gt_from_md> :last-child { margin-bottom: 0; }
 #bwabnfwqfq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bwabnfwqfq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bwabnfwqfq .gt_indent_1 { text-indent: 5px; }
 #bwabnfwqfq .gt_indent_2 { text-indent: calc(5px * 2); }
 #bwabnfwqfq .gt_indent_3 { text-indent: calc(5px * 3); }
 #bwabnfwqfq .gt_indent_4 { text-indent: calc(5px * 4); }
 #bwabnfwqfq .gt_indent_5 { text-indent: calc(5px * 5); }
 #bwabnfwqfq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bwabnfwqfq .gt_row_group_first td { border-top-width: 2px; }
 #bwabnfwqfq .gt_row_group_first th { border-top-width: 2px; }
 #bwabnfwqfq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bwabnfwqfq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bwabnfwqfq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bwabnfwqfq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bwabnfwqfq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bwabnfwqfq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bwabnfwqfq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bwabnfwqfq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bwabnfwqfq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bwabnfwqfq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bwabnfwqfq .gt_left { text-align: left; }
 #bwabnfwqfq .gt_center { text-align: center; }
 #bwabnfwqfq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bwabnfwqfq .gt_font_normal { font-weight: normal; }
 #bwabnfwqfq .gt_font_bold { font-weight: bold; }
 #bwabnfwqfq .gt_font_italic { font-style: italic; }
 #bwabnfwqfq .gt_super { font-size: 65%; }
 #bwabnfwqfq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bwabnfwqfq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bwabnfwqfq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bwabnfwqfq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bwabnfwqfq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bwabnfwqfq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vizlgpupjm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vizlgpupjm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vizlgpupjm p { margin: 0; padding: 0; }
 #vizlgpupjm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vizlgpupjm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vizlgpupjm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vizlgpupjm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vizlgpupjm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vizlgpupjm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vizlgpupjm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vizlgpupjm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vizlgpupjm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vizlgpupjm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vizlgpupjm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vizlgpupjm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vizlgpupjm .gt_spanner_row { border-bottom-style: hidden; }
 #vizlgpupjm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vizlgpupjm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vizlgpupjm .gt_from_md> :first-child { margin-top: 0; }
 #vizlgpupjm .gt_from_md> :last-child { margin-bottom: 0; }
 #vizlgpupjm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vizlgpupjm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vizlgpupjm .gt_indent_1 { text-indent: 5px; }
 #vizlgpupjm .gt_indent_2 { text-indent: calc(5px * 2); }
 #vizlgpupjm .gt_indent_3 { text-indent: calc(5px * 3); }
 #vizlgpupjm .gt_indent_4 { text-indent: calc(5px * 4); }
 #vizlgpupjm .gt_indent_5 { text-indent: calc(5px * 5); }
 #vizlgpupjm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vizlgpupjm .gt_row_group_first td { border-top-width: 2px; }
 #vizlgpupjm .gt_row_group_first th { border-top-width: 2px; }
 #vizlgpupjm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vizlgpupjm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vizlgpupjm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vizlgpupjm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vizlgpupjm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vizlgpupjm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vizlgpupjm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vizlgpupjm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vizlgpupjm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vizlgpupjm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vizlgpupjm .gt_left { text-align: left; }
 #vizlgpupjm .gt_center { text-align: center; }
 #vizlgpupjm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vizlgpupjm .gt_font_normal { font-weight: normal; }
 #vizlgpupjm .gt_font_bold { font-weight: bold; }
 #vizlgpupjm .gt_font_italic { font-style: italic; }
 #vizlgpupjm .gt_super { font-size: 65%; }
 #vizlgpupjm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vizlgpupjm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vizlgpupjm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vizlgpupjm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vizlgpupjm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vizlgpupjm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cvjfuhmxgz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cvjfuhmxgz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cvjfuhmxgz p { margin: 0; padding: 0; }
 #cvjfuhmxgz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cvjfuhmxgz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cvjfuhmxgz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cvjfuhmxgz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cvjfuhmxgz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cvjfuhmxgz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvjfuhmxgz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cvjfuhmxgz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cvjfuhmxgz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cvjfuhmxgz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cvjfuhmxgz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cvjfuhmxgz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cvjfuhmxgz .gt_spanner_row { border-bottom-style: hidden; }
 #cvjfuhmxgz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cvjfuhmxgz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cvjfuhmxgz .gt_from_md> :first-child { margin-top: 0; }
 #cvjfuhmxgz .gt_from_md> :last-child { margin-bottom: 0; }
 #cvjfuhmxgz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cvjfuhmxgz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cvjfuhmxgz .gt_indent_1 { text-indent: 5px; }
 #cvjfuhmxgz .gt_indent_2 { text-indent: calc(5px * 2); }
 #cvjfuhmxgz .gt_indent_3 { text-indent: calc(5px * 3); }
 #cvjfuhmxgz .gt_indent_4 { text-indent: calc(5px * 4); }
 #cvjfuhmxgz .gt_indent_5 { text-indent: calc(5px * 5); }
 #cvjfuhmxgz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cvjfuhmxgz .gt_row_group_first td { border-top-width: 2px; }
 #cvjfuhmxgz .gt_row_group_first th { border-top-width: 2px; }
 #cvjfuhmxgz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cvjfuhmxgz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvjfuhmxgz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cvjfuhmxgz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cvjfuhmxgz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvjfuhmxgz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cvjfuhmxgz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cvjfuhmxgz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cvjfuhmxgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvjfuhmxgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cvjfuhmxgz .gt_left { text-align: left; }
 #cvjfuhmxgz .gt_center { text-align: center; }
 #cvjfuhmxgz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cvjfuhmxgz .gt_font_normal { font-weight: normal; }
 #cvjfuhmxgz .gt_font_bold { font-weight: bold; }
 #cvjfuhmxgz .gt_font_italic { font-style: italic; }
 #cvjfuhmxgz .gt_super { font-size: 65%; }
 #cvjfuhmxgz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvjfuhmxgz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cvjfuhmxgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvjfuhmxgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cvjfuhmxgz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cvjfuhmxgz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#olmyjsarqj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#olmyjsarqj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#olmyjsarqj p { margin: 0; padding: 0; }
 #olmyjsarqj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #olmyjsarqj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #olmyjsarqj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #olmyjsarqj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #olmyjsarqj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #olmyjsarqj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #olmyjsarqj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #olmyjsarqj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #olmyjsarqj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #olmyjsarqj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #olmyjsarqj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #olmyjsarqj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #olmyjsarqj .gt_spanner_row { border-bottom-style: hidden; }
 #olmyjsarqj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #olmyjsarqj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #olmyjsarqj .gt_from_md> :first-child { margin-top: 0; }
 #olmyjsarqj .gt_from_md> :last-child { margin-bottom: 0; }
 #olmyjsarqj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #olmyjsarqj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #olmyjsarqj .gt_indent_1 { text-indent: 5px; }
 #olmyjsarqj .gt_indent_2 { text-indent: calc(5px * 2); }
 #olmyjsarqj .gt_indent_3 { text-indent: calc(5px * 3); }
 #olmyjsarqj .gt_indent_4 { text-indent: calc(5px * 4); }
 #olmyjsarqj .gt_indent_5 { text-indent: calc(5px * 5); }
 #olmyjsarqj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #olmyjsarqj .gt_row_group_first td { border-top-width: 2px; }
 #olmyjsarqj .gt_row_group_first th { border-top-width: 2px; }
 #olmyjsarqj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #olmyjsarqj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #olmyjsarqj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #olmyjsarqj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #olmyjsarqj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #olmyjsarqj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #olmyjsarqj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #olmyjsarqj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #olmyjsarqj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #olmyjsarqj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #olmyjsarqj .gt_left { text-align: left; }
 #olmyjsarqj .gt_center { text-align: center; }
 #olmyjsarqj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #olmyjsarqj .gt_font_normal { font-weight: normal; }
 #olmyjsarqj .gt_font_bold { font-weight: bold; }
 #olmyjsarqj .gt_font_italic { font-style: italic; }
 #olmyjsarqj .gt_super { font-size: 65%; }
 #olmyjsarqj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #olmyjsarqj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #olmyjsarqj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #olmyjsarqj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #olmyjsarqj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #olmyjsarqj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#exagataiup table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#exagataiup thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#exagataiup p { margin: 0; padding: 0; }
 #exagataiup .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #exagataiup .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #exagataiup .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #exagataiup .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #exagataiup .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #exagataiup .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exagataiup .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #exagataiup .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #exagataiup .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #exagataiup .gt_column_spanner_outer:first-child { padding-left: 0; }
 #exagataiup .gt_column_spanner_outer:last-child { padding-right: 0; }
 #exagataiup .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #exagataiup .gt_spanner_row { border-bottom-style: hidden; }
 #exagataiup .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #exagataiup .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #exagataiup .gt_from_md> :first-child { margin-top: 0; }
 #exagataiup .gt_from_md> :last-child { margin-bottom: 0; }
 #exagataiup .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #exagataiup .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #exagataiup .gt_indent_1 { text-indent: 5px; }
 #exagataiup .gt_indent_2 { text-indent: calc(5px * 2); }
 #exagataiup .gt_indent_3 { text-indent: calc(5px * 3); }
 #exagataiup .gt_indent_4 { text-indent: calc(5px * 4); }
 #exagataiup .gt_indent_5 { text-indent: calc(5px * 5); }
 #exagataiup .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #exagataiup .gt_row_group_first td { border-top-width: 2px; }
 #exagataiup .gt_row_group_first th { border-top-width: 2px; }
 #exagataiup .gt_striped { color: #333333; background-color: #F4F4F4; }
 #exagataiup .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exagataiup .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #exagataiup .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #exagataiup .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exagataiup .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #exagataiup .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #exagataiup .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #exagataiup .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exagataiup .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #exagataiup .gt_left { text-align: left; }
 #exagataiup .gt_center { text-align: center; }
 #exagataiup .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #exagataiup .gt_font_normal { font-weight: normal; }
 #exagataiup .gt_font_bold { font-weight: bold; }
 #exagataiup .gt_font_italic { font-style: italic; }
 #exagataiup .gt_super { font-size: 65%; }
 #exagataiup .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exagataiup .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #exagataiup .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exagataiup .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #exagataiup .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #exagataiup .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#urcyibyuac table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#urcyibyuac thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#urcyibyuac p { margin: 0; padding: 0; }
 #urcyibyuac .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #urcyibyuac .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #urcyibyuac .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #urcyibyuac .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #urcyibyuac .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #urcyibyuac .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #urcyibyuac .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #urcyibyuac .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #urcyibyuac .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #urcyibyuac .gt_column_spanner_outer:first-child { padding-left: 0; }
 #urcyibyuac .gt_column_spanner_outer:last-child { padding-right: 0; }
 #urcyibyuac .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #urcyibyuac .gt_spanner_row { border-bottom-style: hidden; }
 #urcyibyuac .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #urcyibyuac .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #urcyibyuac .gt_from_md> :first-child { margin-top: 0; }
 #urcyibyuac .gt_from_md> :last-child { margin-bottom: 0; }
 #urcyibyuac .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #urcyibyuac .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #urcyibyuac .gt_indent_1 { text-indent: 5px; }
 #urcyibyuac .gt_indent_2 { text-indent: calc(5px * 2); }
 #urcyibyuac .gt_indent_3 { text-indent: calc(5px * 3); }
 #urcyibyuac .gt_indent_4 { text-indent: calc(5px * 4); }
 #urcyibyuac .gt_indent_5 { text-indent: calc(5px * 5); }
 #urcyibyuac .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #urcyibyuac .gt_row_group_first td { border-top-width: 2px; }
 #urcyibyuac .gt_row_group_first th { border-top-width: 2px; }
 #urcyibyuac .gt_striped { color: #333333; background-color: #F4F4F4; }
 #urcyibyuac .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #urcyibyuac .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #urcyibyuac .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #urcyibyuac .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #urcyibyuac .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #urcyibyuac .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #urcyibyuac .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #urcyibyuac .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #urcyibyuac .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #urcyibyuac .gt_left { text-align: left; }
 #urcyibyuac .gt_center { text-align: center; }
 #urcyibyuac .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #urcyibyuac .gt_font_normal { font-weight: normal; }
 #urcyibyuac .gt_font_bold { font-weight: bold; }
 #urcyibyuac .gt_font_italic { font-style: italic; }
 #urcyibyuac .gt_super { font-size: 65%; }
 #urcyibyuac .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #urcyibyuac .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #urcyibyuac .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #urcyibyuac .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #urcyibyuac .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #urcyibyuac .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
