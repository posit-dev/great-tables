# Working with Datasets

**Great Tables** includes sixteen built-in datasets that are used throughout this User Guide and in the API documentation. These datasets cover a range of subject areas and sizes, from the small [exibble](../reference/data.exibble.md#great_tables.data.exibble) toy table (8 rows) to the larger [pizzaplace](../reference/data.pizzaplace.md#great_tables.data.pizzaplace) dataset (nearly 50,000 rows). You can load any of them as a Pandas DataFrame, a Polars DataFrame, or both, depending on how you prefer to work.

These built-in datasets exist so you can experiment with Great Tables features without needing to bring your own data. They make it easy to follow along with examples, test table-building code, and explore different formatting options. They also demonstrate the range of data types and structures that Great Tables handles well, from small categorical tables to large transactional datasets with dates, currencies, and numeric measurements.


# Accessing Datasets Directly

The simplest way to use a dataset is to import it by name from `great_tables.data`. This returns a Pandas DataFrame by default (or a Polars DataFrame if Pandas is not installed).


``` python
from great_tables import GT
from great_tables.data import exibble

GT(exibble)
```


<style>
#kqzgxebpyi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kqzgxebpyi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kqzgxebpyi p { margin: 0; padding: 0; }
 #kqzgxebpyi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kqzgxebpyi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kqzgxebpyi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kqzgxebpyi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kqzgxebpyi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kqzgxebpyi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqzgxebpyi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kqzgxebpyi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kqzgxebpyi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kqzgxebpyi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kqzgxebpyi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kqzgxebpyi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kqzgxebpyi .gt_spanner_row { border-bottom-style: hidden; }
 #kqzgxebpyi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kqzgxebpyi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kqzgxebpyi .gt_from_md> :first-child { margin-top: 0; }
 #kqzgxebpyi .gt_from_md> :last-child { margin-bottom: 0; }
 #kqzgxebpyi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kqzgxebpyi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kqzgxebpyi .gt_indent_1 { text-indent: 5px; }
 #kqzgxebpyi .gt_indent_2 { text-indent: calc(5px * 2); }
 #kqzgxebpyi .gt_indent_3 { text-indent: calc(5px * 3); }
 #kqzgxebpyi .gt_indent_4 { text-indent: calc(5px * 4); }
 #kqzgxebpyi .gt_indent_5 { text-indent: calc(5px * 5); }
 #kqzgxebpyi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kqzgxebpyi .gt_row_group_first td { border-top-width: 2px; }
 #kqzgxebpyi .gt_row_group_first th { border-top-width: 2px; }
 #kqzgxebpyi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kqzgxebpyi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqzgxebpyi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kqzgxebpyi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kqzgxebpyi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kqzgxebpyi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kqzgxebpyi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kqzgxebpyi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kqzgxebpyi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqzgxebpyi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kqzgxebpyi .gt_left { text-align: left; }
 #kqzgxebpyi .gt_center { text-align: center; }
 #kqzgxebpyi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kqzgxebpyi .gt_font_normal { font-weight: normal; }
 #kqzgxebpyi .gt_font_bold { font-weight: bold; }
 #kqzgxebpyi .gt_font_italic { font-style: italic; }
 #kqzgxebpyi .gt_super { font-size: 65%; }
 #kqzgxebpyi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqzgxebpyi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kqzgxebpyi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kqzgxebpyi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kqzgxebpyi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kqzgxebpyi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


The [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset is also available directly on the top-level `great_tables` module, which can be convenient for quick experimentation:


``` python
import great_tables as gt

GT(gt.exibble)
```


<style>
#dgxcvabqlk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dgxcvabqlk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dgxcvabqlk p { margin: 0; padding: 0; }
 #dgxcvabqlk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dgxcvabqlk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dgxcvabqlk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dgxcvabqlk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dgxcvabqlk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dgxcvabqlk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dgxcvabqlk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dgxcvabqlk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dgxcvabqlk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dgxcvabqlk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dgxcvabqlk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dgxcvabqlk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dgxcvabqlk .gt_spanner_row { border-bottom-style: hidden; }
 #dgxcvabqlk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dgxcvabqlk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dgxcvabqlk .gt_from_md> :first-child { margin-top: 0; }
 #dgxcvabqlk .gt_from_md> :last-child { margin-bottom: 0; }
 #dgxcvabqlk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dgxcvabqlk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dgxcvabqlk .gt_indent_1 { text-indent: 5px; }
 #dgxcvabqlk .gt_indent_2 { text-indent: calc(5px * 2); }
 #dgxcvabqlk .gt_indent_3 { text-indent: calc(5px * 3); }
 #dgxcvabqlk .gt_indent_4 { text-indent: calc(5px * 4); }
 #dgxcvabqlk .gt_indent_5 { text-indent: calc(5px * 5); }
 #dgxcvabqlk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dgxcvabqlk .gt_row_group_first td { border-top-width: 2px; }
 #dgxcvabqlk .gt_row_group_first th { border-top-width: 2px; }
 #dgxcvabqlk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dgxcvabqlk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dgxcvabqlk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dgxcvabqlk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dgxcvabqlk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dgxcvabqlk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dgxcvabqlk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dgxcvabqlk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dgxcvabqlk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dgxcvabqlk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dgxcvabqlk .gt_left { text-align: left; }
 #dgxcvabqlk .gt_center { text-align: center; }
 #dgxcvabqlk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dgxcvabqlk .gt_font_normal { font-weight: normal; }
 #dgxcvabqlk .gt_font_bold { font-weight: bold; }
 #dgxcvabqlk .gt_font_italic { font-style: italic; }
 #dgxcvabqlk .gt_super { font-size: 65%; }
 #dgxcvabqlk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dgxcvabqlk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dgxcvabqlk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dgxcvabqlk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dgxcvabqlk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dgxcvabqlk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


All sixteen datasets are available this way: [countrypops](../reference/data.countrypops.md#great_tables.data.countrypops), [sza](../reference/data.sza.md#great_tables.data.sza), [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars), [sp500](../reference/data.sp500.md#great_tables.data.sp500), [pizzaplace](../reference/data.pizzaplace.md#great_tables.data.pizzaplace), [exibble](../reference/data.exibble.md#great_tables.data.exibble), [towny](../reference/data.towny.md#great_tables.data.towny), [peeps](../reference/data.peeps.md#great_tables.data.peeps), [films](../reference/data.films.md#great_tables.data.films), [metro](../reference/data.metro.md#great_tables.data.metro), [gibraltar](../reference/data.gibraltar.md#great_tables.data.gibraltar), [constants](../reference/data.constants.md#great_tables.data.constants), [illness](../reference/data.illness.md#great_tables.data.illness), [reactions](../reference/data.reactions.md#great_tables.data.reactions), [photolysis](../reference/data.photolysis.md#great_tables.data.photolysis), and [nuclides](../reference/data.nuclides.md#great_tables.data.nuclides). Each one has its own documentation page in the API reference with a full description of its columns and contents.

This direct import approach is the most concise option and works well when you're writing examples or exploring the package. Since the default backend is Pandas, existing code that imports datasets this way will continue to work without any changes.


# Choosing a Backend with `data.pd` and `data.pl`

If you want to be explicit about whether you get a Pandas or Polars DataFrame, use the `data.pd` and `data.pl` namespaces. Being explicit about your backend is especially important in shared codebases or library code where you want to guarantee the DataFrame type, regardless of what packages happen to be installed in a given environment. Datasets accessed through these namespaces are loaded on first access and cached for subsequent use, so there's no performance penalty for repeated access.

To get a dataset as a Polars DataFrame, use `data.pl`:


``` python
from great_tables import GT, data

GT(data.pl.exibble)
```


<style>
#vsmreiexar table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vsmreiexar thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vsmreiexar p { margin: 0; padding: 0; }
 #vsmreiexar .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vsmreiexar .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vsmreiexar .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vsmreiexar .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vsmreiexar .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vsmreiexar .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vsmreiexar .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vsmreiexar .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vsmreiexar .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vsmreiexar .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vsmreiexar .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vsmreiexar .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vsmreiexar .gt_spanner_row { border-bottom-style: hidden; }
 #vsmreiexar .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vsmreiexar .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vsmreiexar .gt_from_md> :first-child { margin-top: 0; }
 #vsmreiexar .gt_from_md> :last-child { margin-bottom: 0; }
 #vsmreiexar .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vsmreiexar .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vsmreiexar .gt_indent_1 { text-indent: 5px; }
 #vsmreiexar .gt_indent_2 { text-indent: calc(5px * 2); }
 #vsmreiexar .gt_indent_3 { text-indent: calc(5px * 3); }
 #vsmreiexar .gt_indent_4 { text-indent: calc(5px * 4); }
 #vsmreiexar .gt_indent_5 { text-indent: calc(5px * 5); }
 #vsmreiexar .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vsmreiexar .gt_row_group_first td { border-top-width: 2px; }
 #vsmreiexar .gt_row_group_first th { border-top-width: 2px; }
 #vsmreiexar .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vsmreiexar .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vsmreiexar .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vsmreiexar .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vsmreiexar .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vsmreiexar .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vsmreiexar .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vsmreiexar .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vsmreiexar .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vsmreiexar .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vsmreiexar .gt_left { text-align: left; }
 #vsmreiexar .gt_center { text-align: center; }
 #vsmreiexar .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vsmreiexar .gt_font_normal { font-weight: normal; }
 #vsmreiexar .gt_font_bold { font-weight: bold; }
 #vsmreiexar .gt_font_italic { font-style: italic; }
 #vsmreiexar .gt_super { font-size: 65%; }
 #vsmreiexar .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vsmreiexar .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vsmreiexar .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vsmreiexar .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vsmreiexar .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vsmreiexar .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


To explicitly request a Pandas DataFrame, use `data.pd`:


``` python
GT(data.pd.exibble)
```


<style>
#wjumfuxenx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wjumfuxenx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wjumfuxenx p { margin: 0; padding: 0; }
 #wjumfuxenx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wjumfuxenx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wjumfuxenx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wjumfuxenx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wjumfuxenx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjumfuxenx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjumfuxenx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjumfuxenx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wjumfuxenx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wjumfuxenx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wjumfuxenx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wjumfuxenx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wjumfuxenx .gt_spanner_row { border-bottom-style: hidden; }
 #wjumfuxenx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wjumfuxenx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wjumfuxenx .gt_from_md> :first-child { margin-top: 0; }
 #wjumfuxenx .gt_from_md> :last-child { margin-bottom: 0; }
 #wjumfuxenx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wjumfuxenx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wjumfuxenx .gt_indent_1 { text-indent: 5px; }
 #wjumfuxenx .gt_indent_2 { text-indent: calc(5px * 2); }
 #wjumfuxenx .gt_indent_3 { text-indent: calc(5px * 3); }
 #wjumfuxenx .gt_indent_4 { text-indent: calc(5px * 4); }
 #wjumfuxenx .gt_indent_5 { text-indent: calc(5px * 5); }
 #wjumfuxenx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wjumfuxenx .gt_row_group_first td { border-top-width: 2px; }
 #wjumfuxenx .gt_row_group_first th { border-top-width: 2px; }
 #wjumfuxenx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wjumfuxenx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjumfuxenx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjumfuxenx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wjumfuxenx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjumfuxenx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjumfuxenx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wjumfuxenx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wjumfuxenx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjumfuxenx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjumfuxenx .gt_left { text-align: left; }
 #wjumfuxenx .gt_center { text-align: center; }
 #wjumfuxenx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wjumfuxenx .gt_font_normal { font-weight: normal; }
 #wjumfuxenx .gt_font_bold { font-weight: bold; }
 #wjumfuxenx .gt_font_italic { font-style: italic; }
 #wjumfuxenx .gt_super { font-size: 65%; }
 #wjumfuxenx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjumfuxenx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wjumfuxenx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjumfuxenx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjumfuxenx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wjumfuxenx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


The `data.pl` namespace is especially useful in Polars-only workflows. It reads directly from the underlying CSV files using Polars' own reader, so there is no dependency on Pandas and no need to convert with `pl.from_pandas()`. Similarly, `data.pd` always uses the Pandas CSV reader regardless of what other libraries are installed.


# Using [load_dataset()](../reference/load_dataset.md#great_tables.load_dataset)

The [load_dataset()](../reference/load_dataset.md#great_tables.load_dataset) function provides a programmatic way to load any dataset in a specific format. This is convenient when the dataset name or backend is determined at runtime, for example in a loop, a parameterized notebook, or a function that accepts the table type as an argument.


``` python
from great_tables import GT, load_dataset

gtcars_pl = load_dataset(dataset="gtcars", tbl_type="polars")

(
    GT(gtcars_pl.head(5))
    .cols_hide(columns=["trim", "trsmn", "drivetrain", "bdy_style"])
)
```


<style>
#rxcmfibsyh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rxcmfibsyh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rxcmfibsyh p { margin: 0; padding: 0; }
 #rxcmfibsyh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rxcmfibsyh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rxcmfibsyh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rxcmfibsyh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rxcmfibsyh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rxcmfibsyh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rxcmfibsyh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rxcmfibsyh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rxcmfibsyh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rxcmfibsyh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rxcmfibsyh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rxcmfibsyh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rxcmfibsyh .gt_spanner_row { border-bottom-style: hidden; }
 #rxcmfibsyh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rxcmfibsyh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rxcmfibsyh .gt_from_md> :first-child { margin-top: 0; }
 #rxcmfibsyh .gt_from_md> :last-child { margin-bottom: 0; }
 #rxcmfibsyh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rxcmfibsyh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rxcmfibsyh .gt_indent_1 { text-indent: 5px; }
 #rxcmfibsyh .gt_indent_2 { text-indent: calc(5px * 2); }
 #rxcmfibsyh .gt_indent_3 { text-indent: calc(5px * 3); }
 #rxcmfibsyh .gt_indent_4 { text-indent: calc(5px * 4); }
 #rxcmfibsyh .gt_indent_5 { text-indent: calc(5px * 5); }
 #rxcmfibsyh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rxcmfibsyh .gt_row_group_first td { border-top-width: 2px; }
 #rxcmfibsyh .gt_row_group_first th { border-top-width: 2px; }
 #rxcmfibsyh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rxcmfibsyh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rxcmfibsyh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rxcmfibsyh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rxcmfibsyh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rxcmfibsyh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rxcmfibsyh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rxcmfibsyh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rxcmfibsyh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rxcmfibsyh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rxcmfibsyh .gt_left { text-align: left; }
 #rxcmfibsyh .gt_center { text-align: center; }
 #rxcmfibsyh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rxcmfibsyh .gt_font_normal { font-weight: normal; }
 #rxcmfibsyh .gt_font_bold { font-weight: bold; }
 #rxcmfibsyh .gt_font_italic { font-style: italic; }
 #rxcmfibsyh .gt_super { font-size: 65%; }
 #rxcmfibsyh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rxcmfibsyh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rxcmfibsyh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rxcmfibsyh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rxcmfibsyh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rxcmfibsyh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| mfr | model | year | hp | hp_rpm | trq | trq_rpm | mpg_c | mpg_h | ctry_origin | msrp |
|----|----|----|----|----|----|----|----|----|----|----|
| Ford | GT | 2017 | 647.0 | 6250.0 | 550.0 | 5900.0 | 11.0 | 18.0 | United States | 447000.0 |
| Ferrari | 458 Speciale | 2015 | 597.0 | 9000.0 | 398.0 | 6000.0 | 13.0 | 17.0 | Italy | 291744.0 |
| Ferrari | 458 Spider | 2015 | 562.0 | 9000.0 | 398.0 | 6000.0 | 13.0 | 17.0 | Italy | 263553.0 |
| Ferrari | 458 Italia | 2014 | 562.0 | 9000.0 | 398.0 | 6000.0 | 13.0 | 17.0 | Italy | 233509.0 |
| Ferrari | 488 GTB | 2016 | 661.0 | 8000.0 | 561.0 | 3000.0 | 15.0 | 22.0 | Italy | 245400.0 |


The `tbl_type=` parameter accepts `"pandas"` (the default) or `"polars"`, and the `dataset=` parameter accepts any of the sixteen dataset names listed above. Here is the same idea with a Pandas DataFrame:


``` python
sp500_pd = load_dataset(dataset="sp500", tbl_type="pandas")

GT(sp500_pd.head(5))
```


<style>
#lrdfpslpvt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lrdfpslpvt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lrdfpslpvt p { margin: 0; padding: 0; }
 #lrdfpslpvt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lrdfpslpvt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lrdfpslpvt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lrdfpslpvt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lrdfpslpvt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lrdfpslpvt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lrdfpslpvt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lrdfpslpvt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lrdfpslpvt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lrdfpslpvt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lrdfpslpvt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lrdfpslpvt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lrdfpslpvt .gt_spanner_row { border-bottom-style: hidden; }
 #lrdfpslpvt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lrdfpslpvt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lrdfpslpvt .gt_from_md> :first-child { margin-top: 0; }
 #lrdfpslpvt .gt_from_md> :last-child { margin-bottom: 0; }
 #lrdfpslpvt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lrdfpslpvt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lrdfpslpvt .gt_indent_1 { text-indent: 5px; }
 #lrdfpslpvt .gt_indent_2 { text-indent: calc(5px * 2); }
 #lrdfpslpvt .gt_indent_3 { text-indent: calc(5px * 3); }
 #lrdfpslpvt .gt_indent_4 { text-indent: calc(5px * 4); }
 #lrdfpslpvt .gt_indent_5 { text-indent: calc(5px * 5); }
 #lrdfpslpvt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lrdfpslpvt .gt_row_group_first td { border-top-width: 2px; }
 #lrdfpslpvt .gt_row_group_first th { border-top-width: 2px; }
 #lrdfpslpvt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lrdfpslpvt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lrdfpslpvt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lrdfpslpvt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lrdfpslpvt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lrdfpslpvt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lrdfpslpvt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lrdfpslpvt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lrdfpslpvt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lrdfpslpvt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lrdfpslpvt .gt_left { text-align: left; }
 #lrdfpslpvt .gt_center { text-align: center; }
 #lrdfpslpvt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lrdfpslpvt .gt_font_normal { font-weight: normal; }
 #lrdfpslpvt .gt_font_bold { font-weight: bold; }
 #lrdfpslpvt .gt_font_italic { font-style: italic; }
 #lrdfpslpvt .gt_super { font-size: 65%; }
 #lrdfpslpvt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lrdfpslpvt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lrdfpslpvt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lrdfpslpvt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lrdfpslpvt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lrdfpslpvt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | open      | high      | low     | close     | volume       | adj_close |
|------------|-----------|-----------|---------|-----------|--------------|-----------|
| 2015-12-31 | 2060.5901 | 2062.54   | 2043.62 | 2043.9399 | 2655330000.0 | 2043.9399 |
| 2015-12-30 | 2077.3401 | 2077.3401 | 2061.97 | 2063.3601 | 2367430000.0 | 2063.3601 |
| 2015-12-29 | 2060.54   | 2081.5601 | 2060.54 | 2078.3601 | 2542000000.0 | 2078.3601 |
| 2015-12-28 | 2057.77   | 2057.77   | 2044.2  | 2056.5    | 2492510000.0 | 2056.5    |
| 2015-12-24 | 2063.52   | 2067.3601 | 2058.73 | 2060.99   | 1411860000.0 | 2060.99   |


If you pass an unrecognized dataset name or table type, [load_dataset()](../reference/load_dataset.md#great_tables.load_dataset) raises a `ValueError` with a message listing the valid options. This makes it safe to use in automated workflows where a typo might otherwise lead to a confusing `AttributeError`.


# Summary of Access Patterns

The table below summarizes the three approaches. All of them read directly from the package's bundled CSV files, so no network access is needed and the data is always available.

| Pattern | Returns | Use when… |
|----|----|----|
| [data.exibble](../reference/data.exibble.md#great_tables.data.exibble) | Pandas (default) | You want the simplest import |
| `data.pd.exibble` | Pandas (always) | You want to be explicit about Pandas |
| `data.pl.exibble` | Polars (always) | You're working in a Polars-only workflow |
| `load_dataset("exibble", tbl_type="polars")` | Polars | The dataset name or type is a variable |

Whichever approach you choose, the resulting DataFrame can be passed directly to [GT()](../reference/GT.md#great_tables.GT) to start building a table. In the rest of this User Guide we'll mostly use the simple `from great_tables.data import ...` style, but everything you see works just as well with a Polars DataFrame loaded through `data.pl` or [load_dataset()](../reference/load_dataset.md#great_tables.load_dataset).
