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
#qvasjtqnfm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qvasjtqnfm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qvasjtqnfm p { margin: 0; padding: 0; }
 #qvasjtqnfm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qvasjtqnfm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qvasjtqnfm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qvasjtqnfm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qvasjtqnfm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qvasjtqnfm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvasjtqnfm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qvasjtqnfm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qvasjtqnfm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qvasjtqnfm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qvasjtqnfm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qvasjtqnfm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qvasjtqnfm .gt_spanner_row { border-bottom-style: hidden; }
 #qvasjtqnfm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qvasjtqnfm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qvasjtqnfm .gt_from_md> :first-child { margin-top: 0; }
 #qvasjtqnfm .gt_from_md> :last-child { margin-bottom: 0; }
 #qvasjtqnfm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qvasjtqnfm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qvasjtqnfm .gt_indent_1 { text-indent: 5px; }
 #qvasjtqnfm .gt_indent_2 { text-indent: calc(5px * 2); }
 #qvasjtqnfm .gt_indent_3 { text-indent: calc(5px * 3); }
 #qvasjtqnfm .gt_indent_4 { text-indent: calc(5px * 4); }
 #qvasjtqnfm .gt_indent_5 { text-indent: calc(5px * 5); }
 #qvasjtqnfm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qvasjtqnfm .gt_row_group_first td { border-top-width: 2px; }
 #qvasjtqnfm .gt_row_group_first th { border-top-width: 2px; }
 #qvasjtqnfm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qvasjtqnfm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvasjtqnfm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qvasjtqnfm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qvasjtqnfm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvasjtqnfm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qvasjtqnfm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qvasjtqnfm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qvasjtqnfm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvasjtqnfm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qvasjtqnfm .gt_left { text-align: left; }
 #qvasjtqnfm .gt_center { text-align: center; }
 #qvasjtqnfm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qvasjtqnfm .gt_font_normal { font-weight: normal; }
 #qvasjtqnfm .gt_font_bold { font-weight: bold; }
 #qvasjtqnfm .gt_font_italic { font-style: italic; }
 #qvasjtqnfm .gt_super { font-size: 65%; }
 #qvasjtqnfm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvasjtqnfm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qvasjtqnfm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvasjtqnfm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qvasjtqnfm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qvasjtqnfm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#simdwlgsxy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#simdwlgsxy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#simdwlgsxy p { margin: 0; padding: 0; }
 #simdwlgsxy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #simdwlgsxy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #simdwlgsxy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #simdwlgsxy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #simdwlgsxy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #simdwlgsxy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #simdwlgsxy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #simdwlgsxy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #simdwlgsxy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #simdwlgsxy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #simdwlgsxy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #simdwlgsxy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #simdwlgsxy .gt_spanner_row { border-bottom-style: hidden; }
 #simdwlgsxy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #simdwlgsxy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #simdwlgsxy .gt_from_md> :first-child { margin-top: 0; }
 #simdwlgsxy .gt_from_md> :last-child { margin-bottom: 0; }
 #simdwlgsxy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #simdwlgsxy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #simdwlgsxy .gt_indent_1 { text-indent: 5px; }
 #simdwlgsxy .gt_indent_2 { text-indent: calc(5px * 2); }
 #simdwlgsxy .gt_indent_3 { text-indent: calc(5px * 3); }
 #simdwlgsxy .gt_indent_4 { text-indent: calc(5px * 4); }
 #simdwlgsxy .gt_indent_5 { text-indent: calc(5px * 5); }
 #simdwlgsxy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #simdwlgsxy .gt_row_group_first td { border-top-width: 2px; }
 #simdwlgsxy .gt_row_group_first th { border-top-width: 2px; }
 #simdwlgsxy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #simdwlgsxy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #simdwlgsxy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #simdwlgsxy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #simdwlgsxy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #simdwlgsxy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #simdwlgsxy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #simdwlgsxy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #simdwlgsxy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #simdwlgsxy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #simdwlgsxy .gt_left { text-align: left; }
 #simdwlgsxy .gt_center { text-align: center; }
 #simdwlgsxy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #simdwlgsxy .gt_font_normal { font-weight: normal; }
 #simdwlgsxy .gt_font_bold { font-weight: bold; }
 #simdwlgsxy .gt_font_italic { font-style: italic; }
 #simdwlgsxy .gt_super { font-size: 65%; }
 #simdwlgsxy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #simdwlgsxy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #simdwlgsxy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #simdwlgsxy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #simdwlgsxy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #simdwlgsxy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#neppfdjrzs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#neppfdjrzs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#neppfdjrzs p { margin: 0; padding: 0; }
 #neppfdjrzs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #neppfdjrzs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #neppfdjrzs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #neppfdjrzs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #neppfdjrzs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #neppfdjrzs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #neppfdjrzs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #neppfdjrzs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #neppfdjrzs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #neppfdjrzs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #neppfdjrzs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #neppfdjrzs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #neppfdjrzs .gt_spanner_row { border-bottom-style: hidden; }
 #neppfdjrzs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #neppfdjrzs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #neppfdjrzs .gt_from_md> :first-child { margin-top: 0; }
 #neppfdjrzs .gt_from_md> :last-child { margin-bottom: 0; }
 #neppfdjrzs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #neppfdjrzs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #neppfdjrzs .gt_indent_1 { text-indent: 5px; }
 #neppfdjrzs .gt_indent_2 { text-indent: calc(5px * 2); }
 #neppfdjrzs .gt_indent_3 { text-indent: calc(5px * 3); }
 #neppfdjrzs .gt_indent_4 { text-indent: calc(5px * 4); }
 #neppfdjrzs .gt_indent_5 { text-indent: calc(5px * 5); }
 #neppfdjrzs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #neppfdjrzs .gt_row_group_first td { border-top-width: 2px; }
 #neppfdjrzs .gt_row_group_first th { border-top-width: 2px; }
 #neppfdjrzs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #neppfdjrzs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #neppfdjrzs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #neppfdjrzs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #neppfdjrzs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #neppfdjrzs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #neppfdjrzs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #neppfdjrzs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #neppfdjrzs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #neppfdjrzs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #neppfdjrzs .gt_left { text-align: left; }
 #neppfdjrzs .gt_center { text-align: center; }
 #neppfdjrzs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #neppfdjrzs .gt_font_normal { font-weight: normal; }
 #neppfdjrzs .gt_font_bold { font-weight: bold; }
 #neppfdjrzs .gt_font_italic { font-style: italic; }
 #neppfdjrzs .gt_super { font-size: 65%; }
 #neppfdjrzs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #neppfdjrzs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #neppfdjrzs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #neppfdjrzs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #neppfdjrzs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #neppfdjrzs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xedottylxl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xedottylxl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xedottylxl p { margin: 0; padding: 0; }
 #xedottylxl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xedottylxl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xedottylxl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xedottylxl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xedottylxl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xedottylxl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xedottylxl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xedottylxl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xedottylxl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xedottylxl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xedottylxl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xedottylxl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xedottylxl .gt_spanner_row { border-bottom-style: hidden; }
 #xedottylxl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xedottylxl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xedottylxl .gt_from_md> :first-child { margin-top: 0; }
 #xedottylxl .gt_from_md> :last-child { margin-bottom: 0; }
 #xedottylxl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xedottylxl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xedottylxl .gt_indent_1 { text-indent: 5px; }
 #xedottylxl .gt_indent_2 { text-indent: calc(5px * 2); }
 #xedottylxl .gt_indent_3 { text-indent: calc(5px * 3); }
 #xedottylxl .gt_indent_4 { text-indent: calc(5px * 4); }
 #xedottylxl .gt_indent_5 { text-indent: calc(5px * 5); }
 #xedottylxl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xedottylxl .gt_row_group_first td { border-top-width: 2px; }
 #xedottylxl .gt_row_group_first th { border-top-width: 2px; }
 #xedottylxl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xedottylxl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xedottylxl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xedottylxl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xedottylxl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xedottylxl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xedottylxl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xedottylxl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xedottylxl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xedottylxl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xedottylxl .gt_left { text-align: left; }
 #xedottylxl .gt_center { text-align: center; }
 #xedottylxl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xedottylxl .gt_font_normal { font-weight: normal; }
 #xedottylxl .gt_font_bold { font-weight: bold; }
 #xedottylxl .gt_font_italic { font-style: italic; }
 #xedottylxl .gt_super { font-size: 65%; }
 #xedottylxl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xedottylxl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xedottylxl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xedottylxl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xedottylxl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xedottylxl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#izppugbufx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#izppugbufx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#izppugbufx p { margin: 0; padding: 0; }
 #izppugbufx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #izppugbufx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #izppugbufx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #izppugbufx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #izppugbufx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #izppugbufx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izppugbufx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #izppugbufx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #izppugbufx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #izppugbufx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #izppugbufx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #izppugbufx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #izppugbufx .gt_spanner_row { border-bottom-style: hidden; }
 #izppugbufx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #izppugbufx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #izppugbufx .gt_from_md> :first-child { margin-top: 0; }
 #izppugbufx .gt_from_md> :last-child { margin-bottom: 0; }
 #izppugbufx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #izppugbufx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #izppugbufx .gt_indent_1 { text-indent: 5px; }
 #izppugbufx .gt_indent_2 { text-indent: calc(5px * 2); }
 #izppugbufx .gt_indent_3 { text-indent: calc(5px * 3); }
 #izppugbufx .gt_indent_4 { text-indent: calc(5px * 4); }
 #izppugbufx .gt_indent_5 { text-indent: calc(5px * 5); }
 #izppugbufx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #izppugbufx .gt_row_group_first td { border-top-width: 2px; }
 #izppugbufx .gt_row_group_first th { border-top-width: 2px; }
 #izppugbufx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #izppugbufx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izppugbufx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #izppugbufx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #izppugbufx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izppugbufx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #izppugbufx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #izppugbufx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #izppugbufx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izppugbufx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #izppugbufx .gt_left { text-align: left; }
 #izppugbufx .gt_center { text-align: center; }
 #izppugbufx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #izppugbufx .gt_font_normal { font-weight: normal; }
 #izppugbufx .gt_font_bold { font-weight: bold; }
 #izppugbufx .gt_font_italic { font-style: italic; }
 #izppugbufx .gt_super { font-size: 65%; }
 #izppugbufx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izppugbufx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #izppugbufx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izppugbufx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #izppugbufx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #izppugbufx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#clapsitoun table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#clapsitoun thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#clapsitoun p { margin: 0; padding: 0; }
 #clapsitoun .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #clapsitoun .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #clapsitoun .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #clapsitoun .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #clapsitoun .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #clapsitoun .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #clapsitoun .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #clapsitoun .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #clapsitoun .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #clapsitoun .gt_column_spanner_outer:first-child { padding-left: 0; }
 #clapsitoun .gt_column_spanner_outer:last-child { padding-right: 0; }
 #clapsitoun .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #clapsitoun .gt_spanner_row { border-bottom-style: hidden; }
 #clapsitoun .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #clapsitoun .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #clapsitoun .gt_from_md> :first-child { margin-top: 0; }
 #clapsitoun .gt_from_md> :last-child { margin-bottom: 0; }
 #clapsitoun .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #clapsitoun .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #clapsitoun .gt_indent_1 { text-indent: 5px; }
 #clapsitoun .gt_indent_2 { text-indent: calc(5px * 2); }
 #clapsitoun .gt_indent_3 { text-indent: calc(5px * 3); }
 #clapsitoun .gt_indent_4 { text-indent: calc(5px * 4); }
 #clapsitoun .gt_indent_5 { text-indent: calc(5px * 5); }
 #clapsitoun .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #clapsitoun .gt_row_group_first td { border-top-width: 2px; }
 #clapsitoun .gt_row_group_first th { border-top-width: 2px; }
 #clapsitoun .gt_striped { color: #333333; background-color: #F4F4F4; }
 #clapsitoun .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #clapsitoun .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #clapsitoun .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #clapsitoun .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #clapsitoun .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #clapsitoun .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #clapsitoun .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #clapsitoun .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #clapsitoun .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #clapsitoun .gt_left { text-align: left; }
 #clapsitoun .gt_center { text-align: center; }
 #clapsitoun .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #clapsitoun .gt_font_normal { font-weight: normal; }
 #clapsitoun .gt_font_bold { font-weight: bold; }
 #clapsitoun .gt_font_italic { font-style: italic; }
 #clapsitoun .gt_super { font-size: 65%; }
 #clapsitoun .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #clapsitoun .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #clapsitoun .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #clapsitoun .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #clapsitoun .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #clapsitoun .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
