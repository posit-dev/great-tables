# Great Tables `v0.2.0`: Easy Data Coloring

We enjoy working on **Great Tables** because we want everybody to easily make beautiful tables. Tables don't have to be boring, they really could be captivating and insightful. With every release we get closer and closer to realizing our mission and, as such, we're happy to announce the `v0.2.0` release that's now on PyPI.

The really big feature that's available with this release is the [data_color()](../../reference/GT.data_color.md#great_tables.GT.data_color) method. It gives you several options for colorizing data cells based on the underlying data. The method automatically scales color values according to the data in order to emphasize differences or reveal trends. The example below emphasizes large currency values with a `"darkgreen"` fill color.


``` python
from great_tables import GT, exibble

(
    GT(exibble[["currency", "date", "row"]].head(4), rowname_col="row")
    .data_color(
        columns="currency",
        palette=["lightblue", "darkgreen"]
    )
)
```


<style>
#qcnfrusort table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qcnfrusort thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qcnfrusort p { margin: 0; padding: 0; }
 #qcnfrusort .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qcnfrusort .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qcnfrusort .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qcnfrusort .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qcnfrusort .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qcnfrusort .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qcnfrusort .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qcnfrusort .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qcnfrusort .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qcnfrusort .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qcnfrusort .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qcnfrusort .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qcnfrusort .gt_spanner_row { border-bottom-style: hidden; }
 #qcnfrusort .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qcnfrusort .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qcnfrusort .gt_from_md> :first-child { margin-top: 0; }
 #qcnfrusort .gt_from_md> :last-child { margin-bottom: 0; }
 #qcnfrusort .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qcnfrusort .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qcnfrusort .gt_indent_1 { text-indent: 5px; }
 #qcnfrusort .gt_indent_2 { text-indent: calc(5px * 2); }
 #qcnfrusort .gt_indent_3 { text-indent: calc(5px * 3); }
 #qcnfrusort .gt_indent_4 { text-indent: calc(5px * 4); }
 #qcnfrusort .gt_indent_5 { text-indent: calc(5px * 5); }
 #qcnfrusort .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qcnfrusort .gt_row_group_first td { border-top-width: 2px; }
 #qcnfrusort .gt_row_group_first th { border-top-width: 2px; }
 #qcnfrusort .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qcnfrusort .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qcnfrusort .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qcnfrusort .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qcnfrusort .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qcnfrusort .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qcnfrusort .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qcnfrusort .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qcnfrusort .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qcnfrusort .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qcnfrusort .gt_left { text-align: left; }
 #qcnfrusort .gt_center { text-align: center; }
 #qcnfrusort .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qcnfrusort .gt_font_normal { font-weight: normal; }
 #qcnfrusort .gt_font_bold { font-weight: bold; }
 #qcnfrusort .gt_font_italic { font-style: italic; }
 #qcnfrusort .gt_super { font-size: 65%; }
 #qcnfrusort .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qcnfrusort .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qcnfrusort .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qcnfrusort .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qcnfrusort .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qcnfrusort .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|       | currency | date       |
|-------|----------|------------|
| row_1 | 49.95    | 2015-01-15 |
| row_2 | 17.95    | 2015-02-15 |
| row_3 | 1.39     | 2015-03-15 |
| row_4 | 65100.0  | 2015-04-15 |


Note that we use `columns=` to specify which columns get the colorizing treatment (just `currency` here) and the `palette=` is given as a list of color values. From this we can see that the `65100.0` value polarizes the data coloring process; it is `"darkgreen"` while all other values are `"lightblue"` (with no interpolated colors in between). Also, isn't it nice that the text adapts to the background color?

The above example is suitable for emphasizing large values, but, maybe you consider the extreme value to be something that's out of bounds? For that, we can use the `domain=` and `na_value=` arguments to gray-out the extreme values. We'll also nicely format the `currency` column in this next example.


``` python
(
    GT(exibble[["currency", "date", "row"]].head(4), rowname_col="row")
    .data_color(
        columns="currency",
        palette=["lightblue", "darkgreen"],
        domain=[0, 50],
        na_color="lightgray"
    )
    .fmt_currency(
        columns="currency",
        currency="GBP",
        use_subunits=False
    )
)
```


<style>
#fvcsibrbkl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fvcsibrbkl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fvcsibrbkl p { margin: 0; padding: 0; }
 #fvcsibrbkl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fvcsibrbkl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fvcsibrbkl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fvcsibrbkl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fvcsibrbkl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fvcsibrbkl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fvcsibrbkl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fvcsibrbkl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fvcsibrbkl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fvcsibrbkl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fvcsibrbkl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fvcsibrbkl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fvcsibrbkl .gt_spanner_row { border-bottom-style: hidden; }
 #fvcsibrbkl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fvcsibrbkl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fvcsibrbkl .gt_from_md> :first-child { margin-top: 0; }
 #fvcsibrbkl .gt_from_md> :last-child { margin-bottom: 0; }
 #fvcsibrbkl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fvcsibrbkl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fvcsibrbkl .gt_indent_1 { text-indent: 5px; }
 #fvcsibrbkl .gt_indent_2 { text-indent: calc(5px * 2); }
 #fvcsibrbkl .gt_indent_3 { text-indent: calc(5px * 3); }
 #fvcsibrbkl .gt_indent_4 { text-indent: calc(5px * 4); }
 #fvcsibrbkl .gt_indent_5 { text-indent: calc(5px * 5); }
 #fvcsibrbkl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fvcsibrbkl .gt_row_group_first td { border-top-width: 2px; }
 #fvcsibrbkl .gt_row_group_first th { border-top-width: 2px; }
 #fvcsibrbkl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fvcsibrbkl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fvcsibrbkl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fvcsibrbkl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fvcsibrbkl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fvcsibrbkl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fvcsibrbkl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fvcsibrbkl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fvcsibrbkl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fvcsibrbkl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fvcsibrbkl .gt_left { text-align: left; }
 #fvcsibrbkl .gt_center { text-align: center; }
 #fvcsibrbkl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fvcsibrbkl .gt_font_normal { font-weight: normal; }
 #fvcsibrbkl .gt_font_bold { font-weight: bold; }
 #fvcsibrbkl .gt_font_italic { font-style: italic; }
 #fvcsibrbkl .gt_super { font-size: 65%; }
 #fvcsibrbkl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fvcsibrbkl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fvcsibrbkl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fvcsibrbkl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fvcsibrbkl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fvcsibrbkl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|       | currency | date       |
|-------|----------|------------|
| row_1 | £50      | 2015-01-15 |
| row_2 | £18      | 2015-02-15 |
| row_3 | £1       | 2015-03-15 |
| row_4 | £65,100  | 2015-04-15 |


Now the very large value is in `"lightgray"`, making all other values easier to compare. We did setting `domain=[0, 50]` and specifying `na_color="lightgray"`. This caused the out-of-bounds value of `65100` to have a light gray background. Notice that the values are also formatted as currencies, and this is thanks to [fmt_currency()](../../reference/GT.fmt_currency.md#great_tables.GT.fmt_currency) which never interferes with styling.

Here's a more inspirational example that uses a heavily-manipulated version of the [countrypops](../../reference/data.countrypops.md#great_tables.data.countrypops) dataset (thanks again, **Polars**!) along with a color treatment that's mediated by [data_color()](../../reference/GT.data_color.md#great_tables.GT.data_color). Here, the population values can be easily compared by the amount of `"purple"` within them.


``` python
from great_tables.data import countrypops
import polars as pl
import polars.selectors as cs

wide_pops = (
    pl.from_pandas(countrypops)
    .filter(
        pl.col("country_code_2").is_in(["FM", "GU", "KI", "MH", "MP", "NR", "PW"])
        & pl.col("year").is_in([2000, 2010, 2020])
    )
    .pivot(index="country_name", on="year", values="population")
    .sort("2020", descending=True)
)

(
    GT(wide_pops, rowname_col="country_name")
    .tab_header(
        title="Populations of Select Countries in Oceania",
        subtitle="Population values are from 2000, 2010, and 2020.",
    )
    .tab_spanner(label="Total Population", columns=cs.all())
    .fmt_integer(columns=["2000", "2010", "2020"])
    .data_color(palette=["white", "purple"], domain=[0, 1.7e5])
)
```


<style>
#lyeglclspc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lyeglclspc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lyeglclspc p { margin: 0; padding: 0; }
 #lyeglclspc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lyeglclspc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lyeglclspc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lyeglclspc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lyeglclspc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lyeglclspc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lyeglclspc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lyeglclspc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lyeglclspc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lyeglclspc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lyeglclspc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lyeglclspc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lyeglclspc .gt_spanner_row { border-bottom-style: hidden; }
 #lyeglclspc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lyeglclspc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lyeglclspc .gt_from_md> :first-child { margin-top: 0; }
 #lyeglclspc .gt_from_md> :last-child { margin-bottom: 0; }
 #lyeglclspc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lyeglclspc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lyeglclspc .gt_indent_1 { text-indent: 5px; }
 #lyeglclspc .gt_indent_2 { text-indent: calc(5px * 2); }
 #lyeglclspc .gt_indent_3 { text-indent: calc(5px * 3); }
 #lyeglclspc .gt_indent_4 { text-indent: calc(5px * 4); }
 #lyeglclspc .gt_indent_5 { text-indent: calc(5px * 5); }
 #lyeglclspc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lyeglclspc .gt_row_group_first td { border-top-width: 2px; }
 #lyeglclspc .gt_row_group_first th { border-top-width: 2px; }
 #lyeglclspc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lyeglclspc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lyeglclspc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lyeglclspc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lyeglclspc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lyeglclspc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lyeglclspc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lyeglclspc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lyeglclspc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lyeglclspc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lyeglclspc .gt_left { text-align: left; }
 #lyeglclspc .gt_center { text-align: center; }
 #lyeglclspc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lyeglclspc .gt_font_normal { font-weight: normal; }
 #lyeglclspc .gt_font_bold { font-weight: bold; }
 #lyeglclspc .gt_font_italic { font-style: italic; }
 #lyeglclspc .gt_super { font-size: 65%; }
 #lyeglclspc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lyeglclspc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lyeglclspc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lyeglclspc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lyeglclspc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lyeglclspc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Populations of Select Countries in Oceania</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Population values are from 2000, 2010, and 2020.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th colspan="3" id="Total-Population" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Total Population</th>
</tr>
<tr class="gt_col_headings">
<th id="2000" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2000</th>
<th id="2010" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2010</th>
<th id="2020" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2020</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">Guam</th>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a52df1">160,188</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a327f0">164,905</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a021f0">169,231</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">Kiribati</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #cd8af7">88,826</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c371f5">107,995</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #b859f4">126,463</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">Micronesia (Federated States)</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #c16cf5">111,709</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c372f6">107,588</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c06cf5">112,106</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">Northern Mariana Islands</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #d296f8">80,338</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e1b8fa">54,087</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e3befb">49,587</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">Marshall Islands</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #e1b8fa">54,224</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e1b9fa">53,416</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e7c6fb">43,413</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">Palau</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #f4e5fd">19,726</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f5e7fd">18,540</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f5e7fd">17,972</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="color: #000000; background-color: #808080">Nauru</th>
<td class="gt_row gt_right" style="color: #000000; background-color: #f9f1fe">10,377</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f9f2fe">10,241</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f8effe">12,315</td>
</tr>
</tbody>
</table>


This was just a sampler of what you can do with the all-new [data_color()](../../reference/GT.data_color.md#great_tables.GT.data_color) method. Take a look at these pages for more information:

- The [*Colorizing with Data*](../../user-guide/colorizing-with-data.md) page in the *User Guide*, which provides more details on how to use [data_color()](../../reference/GT.data_color.md#great_tables.GT.data_color)
- The guide on [Basic Styling](https://posit-dev.github.io/great-tables/get-started/basic-styling.html) covers general styling (e.g., bold text, underlines, etc.) with [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style)
- The reference pages for [`data_color()`](https://posit-dev.github.io/great-tables/reference/GT.data_color.html) and [`tab_style()`](https://posit-dev.github.io/great-tables/reference/GT.tab_style.html)

To conclude, we're happy that this new functionality is now in the **Great Tables** package! We hope you find it useful for your table-generation work. And we'll keep improving upon it so that you'll have more possibilities to make beautiful, and colorful, tables for presentation.
