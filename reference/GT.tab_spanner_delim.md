# GT.tab_spanner_delim()


Insert spanners by splitting column names with a delimiter.


Usage

``` python
GT.tab_spanner_delim(
    delim=".",
    columns=None,
    split="last",
    limit=-1,
    reverse=False,
)
```


This generates one or more spanners (and sets column labels), by splitting the column name by the specified delimiter text (delim) and placing the fragments from top to bottom (i.e., higher-level spanners to the column labels) or vice versa.

For example, the three side-by-side column names rating_1, rating_2, and rating_3 will by default produce a spanner labeled "rating" above columns labeled "1", "2", and "3".


## Parameters


`delim: str = ``"."`  
Delimiter for splitting, default to `"."`.

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`split: Literal[``"first", `<span class="st">`"last"``]`</span>` = ``"last"`  
Should the delimiter splitting occur from the "last" instance of the delim character or from the "first"? The default here uses the "last" keyword, and splitting begins at the last instance of the delimiter in the column name. This option only has some consequence when there is a limit value applied that is lesser than the number of delimiter characters for a given column name (i.e., number of splits is not the maximum possible number).

`limit: int = ``-1`  
Limit for splitting. An optional limit to place on the splitting procedure. The default -1 means that a column name will be split as many times are there are delimiter characters. In other words, the default means there is no limit. If an integer value is given to limit then splitting will cease at the iteration given by limit. This works in tandem with split since we can adjust the number of splits from either the right side (split = "last") or left side (split = "first") of the column name.

`reverse: bool = ``False`  
Should the order of split names be reversed? By default, this is `False`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's create a table table that includes the column names province.NL_ZH.pop, province.NL_ZH.gdp, province.NL_NH.pop, and province.NL_NH.gdp, we can see that we have a naming system that has a well-defined structure. We start with the more general to the left ("province") and move to the more specific on the right ("pop"). If the columns are in the table in this exact order, then things are in an ideal state as the eventual spanner labels will form from this neighboring. When using tab_spanner_delim() here with delim set as "." we get the following table:


``` python
import polars as pl
import polars.selectors as cs
from great_tables import GT

data = {
    "province.NL_ZH.pop": [1, 2, 3],
    "province.NL_ZH.gdp": [4, 5, 6],
    "province.NL_NH.pop": [7, 8, 9],
    "province.NL_NH.gdp": [10, 11, 12],
}

gt = GT(pl.DataFrame(data))
gt.tab_spanner_delim()
```


<style>
#bdphkwrwwo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bdphkwrwwo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bdphkwrwwo p { margin: 0; padding: 0; }
 #bdphkwrwwo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bdphkwrwwo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bdphkwrwwo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bdphkwrwwo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bdphkwrwwo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bdphkwrwwo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bdphkwrwwo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bdphkwrwwo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bdphkwrwwo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bdphkwrwwo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bdphkwrwwo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bdphkwrwwo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bdphkwrwwo .gt_spanner_row { border-bottom-style: hidden; }
 #bdphkwrwwo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bdphkwrwwo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bdphkwrwwo .gt_from_md> :first-child { margin-top: 0; }
 #bdphkwrwwo .gt_from_md> :last-child { margin-bottom: 0; }
 #bdphkwrwwo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bdphkwrwwo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bdphkwrwwo .gt_indent_1 { text-indent: 5px; }
 #bdphkwrwwo .gt_indent_2 { text-indent: calc(5px * 2); }
 #bdphkwrwwo .gt_indent_3 { text-indent: calc(5px * 3); }
 #bdphkwrwwo .gt_indent_4 { text-indent: calc(5px * 4); }
 #bdphkwrwwo .gt_indent_5 { text-indent: calc(5px * 5); }
 #bdphkwrwwo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bdphkwrwwo .gt_row_group_first td { border-top-width: 2px; }
 #bdphkwrwwo .gt_row_group_first th { border-top-width: 2px; }
 #bdphkwrwwo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bdphkwrwwo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bdphkwrwwo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bdphkwrwwo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bdphkwrwwo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bdphkwrwwo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bdphkwrwwo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bdphkwrwwo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bdphkwrwwo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bdphkwrwwo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bdphkwrwwo .gt_left { text-align: left; }
 #bdphkwrwwo .gt_center { text-align: center; }
 #bdphkwrwwo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bdphkwrwwo .gt_font_normal { font-weight: normal; }
 #bdphkwrwwo .gt_font_bold { font-weight: bold; }
 #bdphkwrwwo .gt_font_italic { font-style: italic; }
 #bdphkwrwwo .gt_super { font-size: 65%; }
 #bdphkwrwwo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bdphkwrwwo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bdphkwrwwo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bdphkwrwwo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bdphkwrwwo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bdphkwrwwo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="4" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="colgroup">province</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="2" id="NL_ZH" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">NL_ZH</th>
<th colspan="2" id="NL_NH" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">NL_NH</th>
</tr>
<tr class="gt_col_headings">
<th id="province.NL_ZH.pop" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pop</th>
<th id="province.NL_ZH.gdp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">gdp</th>
<th id="province.NL_NH.pop" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pop</th>
<th id="province.NL_NH.gdp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">gdp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">7</td>
<td class="gt_row gt_right">10</td>
</tr>
<tr>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right">11</td>
</tr>
<tr>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">6</td>
<td class="gt_row gt_right">9</td>
<td class="gt_row gt_right">12</td>
</tr>
</tbody>
</table>


``` python
gt.tab_spanner_delim(limit=1)
```


<style>
#gwbqpjtqna table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gwbqpjtqna thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gwbqpjtqna p { margin: 0; padding: 0; }
 #gwbqpjtqna .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gwbqpjtqna .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gwbqpjtqna .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gwbqpjtqna .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gwbqpjtqna .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gwbqpjtqna .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gwbqpjtqna .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gwbqpjtqna .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gwbqpjtqna .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gwbqpjtqna .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gwbqpjtqna .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gwbqpjtqna .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gwbqpjtqna .gt_spanner_row { border-bottom-style: hidden; }
 #gwbqpjtqna .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gwbqpjtqna .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gwbqpjtqna .gt_from_md> :first-child { margin-top: 0; }
 #gwbqpjtqna .gt_from_md> :last-child { margin-bottom: 0; }
 #gwbqpjtqna .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gwbqpjtqna .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gwbqpjtqna .gt_indent_1 { text-indent: 5px; }
 #gwbqpjtqna .gt_indent_2 { text-indent: calc(5px * 2); }
 #gwbqpjtqna .gt_indent_3 { text-indent: calc(5px * 3); }
 #gwbqpjtqna .gt_indent_4 { text-indent: calc(5px * 4); }
 #gwbqpjtqna .gt_indent_5 { text-indent: calc(5px * 5); }
 #gwbqpjtqna .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gwbqpjtqna .gt_row_group_first td { border-top-width: 2px; }
 #gwbqpjtqna .gt_row_group_first th { border-top-width: 2px; }
 #gwbqpjtqna .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gwbqpjtqna .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gwbqpjtqna .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gwbqpjtqna .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gwbqpjtqna .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gwbqpjtqna .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gwbqpjtqna .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gwbqpjtqna .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gwbqpjtqna .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gwbqpjtqna .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gwbqpjtqna .gt_left { text-align: left; }
 #gwbqpjtqna .gt_center { text-align: center; }
 #gwbqpjtqna .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gwbqpjtqna .gt_font_normal { font-weight: normal; }
 #gwbqpjtqna .gt_font_bold { font-weight: bold; }
 #gwbqpjtqna .gt_font_italic { font-style: italic; }
 #gwbqpjtqna .gt_super { font-size: 65%; }
 #gwbqpjtqna .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gwbqpjtqna .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gwbqpjtqna .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gwbqpjtqna .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gwbqpjtqna .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gwbqpjtqna .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="2" id="province.NL_ZH" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">province.NL_ZH</th>
<th colspan="2" id="province.NL_NH" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">province.NL_NH</th>
</tr>
<tr class="gt_col_headings">
<th id="province.NL_ZH.pop" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pop</th>
<th id="province.NL_ZH.gdp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">gdp</th>
<th id="province.NL_NH.pop" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pop</th>
<th id="province.NL_NH.gdp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">gdp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">7</td>
<td class="gt_row gt_right">10</td>
</tr>
<tr>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right">11</td>
</tr>
<tr>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">6</td>
<td class="gt_row gt_right">9</td>
<td class="gt_row gt_right">12</td>
</tr>
</tbody>
</table>


``` python
# the name "province" repeats in the styled table,
# because the first spanner is column names
gt.tab_spanner_delim(reverse=True)
```


<style>
#dnpphrwjtg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dnpphrwjtg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dnpphrwjtg p { margin: 0; padding: 0; }
 #dnpphrwjtg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dnpphrwjtg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dnpphrwjtg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dnpphrwjtg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dnpphrwjtg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dnpphrwjtg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnpphrwjtg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dnpphrwjtg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dnpphrwjtg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dnpphrwjtg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dnpphrwjtg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dnpphrwjtg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dnpphrwjtg .gt_spanner_row { border-bottom-style: hidden; }
 #dnpphrwjtg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dnpphrwjtg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dnpphrwjtg .gt_from_md> :first-child { margin-top: 0; }
 #dnpphrwjtg .gt_from_md> :last-child { margin-bottom: 0; }
 #dnpphrwjtg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dnpphrwjtg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dnpphrwjtg .gt_indent_1 { text-indent: 5px; }
 #dnpphrwjtg .gt_indent_2 { text-indent: calc(5px * 2); }
 #dnpphrwjtg .gt_indent_3 { text-indent: calc(5px * 3); }
 #dnpphrwjtg .gt_indent_4 { text-indent: calc(5px * 4); }
 #dnpphrwjtg .gt_indent_5 { text-indent: calc(5px * 5); }
 #dnpphrwjtg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dnpphrwjtg .gt_row_group_first td { border-top-width: 2px; }
 #dnpphrwjtg .gt_row_group_first th { border-top-width: 2px; }
 #dnpphrwjtg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dnpphrwjtg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnpphrwjtg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dnpphrwjtg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dnpphrwjtg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnpphrwjtg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dnpphrwjtg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dnpphrwjtg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dnpphrwjtg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnpphrwjtg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dnpphrwjtg .gt_left { text-align: left; }
 #dnpphrwjtg .gt_center { text-align: center; }
 #dnpphrwjtg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dnpphrwjtg .gt_font_normal { font-weight: normal; }
 #dnpphrwjtg .gt_font_bold { font-weight: bold; }
 #dnpphrwjtg .gt_font_italic { font-style: italic; }
 #dnpphrwjtg .gt_super { font-size: 65%; }
 #dnpphrwjtg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnpphrwjtg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dnpphrwjtg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnpphrwjtg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dnpphrwjtg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dnpphrwjtg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col">pop</th>
<th class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col">gdp</th>
<th class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col">pop</th>
<th class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col">gdp</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="2" id="NL_ZH" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">NL_ZH</th>
<th colspan="2" id="NL_NH" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">NL_NH</th>
</tr>
<tr class="gt_col_headings">
<th id="province.NL_ZH.pop" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">province</th>
<th id="province.NL_ZH.gdp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">province</th>
<th id="province.NL_NH.pop" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">province</th>
<th id="province.NL_NH.gdp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">province</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">7</td>
<td class="gt_row gt_right">10</td>
</tr>
<tr>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right">11</td>
</tr>
<tr>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">6</td>
<td class="gt_row gt_right">9</td>
<td class="gt_row gt_right">12</td>
</tr>
</tbody>
</table>


``` python
from great_tables.data import towny

lil_towny = (
    pl.DataFrame(towny)
    .select("name", cs.starts_with("population"))
    .head()
)

GT(lil_towny).tab_spanner_delim(delim="_")
```


<style>
#titfkkmcls table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#titfkkmcls thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#titfkkmcls p { margin: 0; padding: 0; }
 #titfkkmcls .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #titfkkmcls .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #titfkkmcls .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #titfkkmcls .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #titfkkmcls .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #titfkkmcls .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #titfkkmcls .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #titfkkmcls .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #titfkkmcls .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #titfkkmcls .gt_column_spanner_outer:first-child { padding-left: 0; }
 #titfkkmcls .gt_column_spanner_outer:last-child { padding-right: 0; }
 #titfkkmcls .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #titfkkmcls .gt_spanner_row { border-bottom-style: hidden; }
 #titfkkmcls .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #titfkkmcls .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #titfkkmcls .gt_from_md> :first-child { margin-top: 0; }
 #titfkkmcls .gt_from_md> :last-child { margin-bottom: 0; }
 #titfkkmcls .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #titfkkmcls .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #titfkkmcls .gt_indent_1 { text-indent: 5px; }
 #titfkkmcls .gt_indent_2 { text-indent: calc(5px * 2); }
 #titfkkmcls .gt_indent_3 { text-indent: calc(5px * 3); }
 #titfkkmcls .gt_indent_4 { text-indent: calc(5px * 4); }
 #titfkkmcls .gt_indent_5 { text-indent: calc(5px * 5); }
 #titfkkmcls .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #titfkkmcls .gt_row_group_first td { border-top-width: 2px; }
 #titfkkmcls .gt_row_group_first th { border-top-width: 2px; }
 #titfkkmcls .gt_striped { color: #333333; background-color: #F4F4F4; }
 #titfkkmcls .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #titfkkmcls .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #titfkkmcls .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #titfkkmcls .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #titfkkmcls .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #titfkkmcls .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #titfkkmcls .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #titfkkmcls .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #titfkkmcls .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #titfkkmcls .gt_left { text-align: left; }
 #titfkkmcls .gt_center { text-align: center; }
 #titfkkmcls .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #titfkkmcls .gt_font_normal { font-weight: normal; }
 #titfkkmcls .gt_font_bold { font-weight: bold; }
 #titfkkmcls .gt_font_italic { font-style: italic; }
 #titfkkmcls .gt_super { font-size: 65%; }
 #titfkkmcls .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #titfkkmcls .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #titfkkmcls .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #titfkkmcls .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #titfkkmcls .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #titfkkmcls .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">name</th>
<th colspan="6" id="population" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">population</th>
</tr>
<tr class="gt_col_headings">
<th id="population_1996" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1996</th>
<th id="population_2001" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2001</th>
<th id="population_2006" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2006</th>
<th id="population_2011" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2011</th>
<th id="population_2016" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2016</th>
<th id="population_2021" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2021</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Addington Highlands</td>
<td class="gt_row gt_right">2429</td>
<td class="gt_row gt_right">2402</td>
<td class="gt_row gt_right">2512</td>
<td class="gt_row gt_right">2517</td>
<td class="gt_row gt_right">2318</td>
<td class="gt_row gt_right">2534</td>
</tr>
<tr>
<td class="gt_row gt_left">Adelaide Metcalfe</td>
<td class="gt_row gt_right">3128</td>
<td class="gt_row gt_right">3149</td>
<td class="gt_row gt_right">3135</td>
<td class="gt_row gt_right">3028</td>
<td class="gt_row gt_right">2990</td>
<td class="gt_row gt_right">3011</td>
</tr>
<tr>
<td class="gt_row gt_left">Adjala-Tosorontio</td>
<td class="gt_row gt_right">9359</td>
<td class="gt_row gt_right">10082</td>
<td class="gt_row gt_right">10695</td>
<td class="gt_row gt_right">10603</td>
<td class="gt_row gt_right">10975</td>
<td class="gt_row gt_right">10989</td>
</tr>
<tr>
<td class="gt_row gt_left">Admaston/Bromley</td>
<td class="gt_row gt_right">2837</td>
<td class="gt_row gt_right">2824</td>
<td class="gt_row gt_right">2716</td>
<td class="gt_row gt_right">2844</td>
<td class="gt_row gt_right">2935</td>
<td class="gt_row gt_right">2995</td>
</tr>
<tr>
<td class="gt_row gt_left">Ajax</td>
<td class="gt_row gt_right">64430</td>
<td class="gt_row gt_right">73753</td>
<td class="gt_row gt_right">90167</td>
<td class="gt_row gt_right">109600</td>
<td class="gt_row gt_right">119677</td>
<td class="gt_row gt_right">126666</td>
</tr>
</tbody>
</table>
