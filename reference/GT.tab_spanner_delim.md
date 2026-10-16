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
#jcbejetbdb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jcbejetbdb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jcbejetbdb p { margin: 0; padding: 0; }
 #jcbejetbdb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jcbejetbdb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jcbejetbdb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jcbejetbdb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jcbejetbdb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jcbejetbdb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jcbejetbdb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jcbejetbdb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jcbejetbdb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jcbejetbdb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jcbejetbdb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jcbejetbdb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jcbejetbdb .gt_spanner_row { border-bottom-style: hidden; }
 #jcbejetbdb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jcbejetbdb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jcbejetbdb .gt_from_md> :first-child { margin-top: 0; }
 #jcbejetbdb .gt_from_md> :last-child { margin-bottom: 0; }
 #jcbejetbdb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jcbejetbdb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jcbejetbdb .gt_indent_1 { text-indent: 5px; }
 #jcbejetbdb .gt_indent_2 { text-indent: calc(5px * 2); }
 #jcbejetbdb .gt_indent_3 { text-indent: calc(5px * 3); }
 #jcbejetbdb .gt_indent_4 { text-indent: calc(5px * 4); }
 #jcbejetbdb .gt_indent_5 { text-indent: calc(5px * 5); }
 #jcbejetbdb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jcbejetbdb .gt_row_group_first td { border-top-width: 2px; }
 #jcbejetbdb .gt_row_group_first th { border-top-width: 2px; }
 #jcbejetbdb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jcbejetbdb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jcbejetbdb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jcbejetbdb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jcbejetbdb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jcbejetbdb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jcbejetbdb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jcbejetbdb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jcbejetbdb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jcbejetbdb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jcbejetbdb .gt_left { text-align: left; }
 #jcbejetbdb .gt_center { text-align: center; }
 #jcbejetbdb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jcbejetbdb .gt_font_normal { font-weight: normal; }
 #jcbejetbdb .gt_font_bold { font-weight: bold; }
 #jcbejetbdb .gt_font_italic { font-style: italic; }
 #jcbejetbdb .gt_super { font-size: 65%; }
 #jcbejetbdb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jcbejetbdb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jcbejetbdb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jcbejetbdb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jcbejetbdb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jcbejetbdb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="4" id="province" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="colgroup">province</th>
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
<td class="gt_row gt_right" headers="province NL_ZH province.NL_ZH.pop">1</td>
<td class="gt_row gt_right" headers="province NL_ZH province.NL_ZH.gdp">4</td>
<td class="gt_row gt_right" headers="province NL_NH province.NL_NH.pop">7</td>
<td class="gt_row gt_right" headers="province NL_NH province.NL_NH.gdp">10</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="province NL_ZH province.NL_ZH.pop">2</td>
<td class="gt_row gt_right" headers="province NL_ZH province.NL_ZH.gdp">5</td>
<td class="gt_row gt_right" headers="province NL_NH province.NL_NH.pop">8</td>
<td class="gt_row gt_right" headers="province NL_NH province.NL_NH.gdp">11</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="province NL_ZH province.NL_ZH.pop">3</td>
<td class="gt_row gt_right" headers="province NL_ZH province.NL_ZH.gdp">6</td>
<td class="gt_row gt_right" headers="province NL_NH province.NL_NH.pop">9</td>
<td class="gt_row gt_right" headers="province NL_NH province.NL_NH.gdp">12</td>
</tr>
</tbody>
</table>


``` python
gt.tab_spanner_delim(limit=1)
```


<style>
#aiujejfves table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aiujejfves thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aiujejfves p { margin: 0; padding: 0; }
 #aiujejfves .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aiujejfves .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aiujejfves .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aiujejfves .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aiujejfves .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aiujejfves .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aiujejfves .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aiujejfves .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #aiujejfves .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aiujejfves .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aiujejfves .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aiujejfves .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aiujejfves .gt_spanner_row { border-bottom-style: hidden; }
 #aiujejfves .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aiujejfves .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aiujejfves .gt_from_md> :first-child { margin-top: 0; }
 #aiujejfves .gt_from_md> :last-child { margin-bottom: 0; }
 #aiujejfves .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aiujejfves .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #aiujejfves .gt_indent_1 { text-indent: 5px; }
 #aiujejfves .gt_indent_2 { text-indent: calc(5px * 2); }
 #aiujejfves .gt_indent_3 { text-indent: calc(5px * 3); }
 #aiujejfves .gt_indent_4 { text-indent: calc(5px * 4); }
 #aiujejfves .gt_indent_5 { text-indent: calc(5px * 5); }
 #aiujejfves .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #aiujejfves .gt_row_group_first td { border-top-width: 2px; }
 #aiujejfves .gt_row_group_first th { border-top-width: 2px; }
 #aiujejfves .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aiujejfves .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aiujejfves .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aiujejfves .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aiujejfves .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aiujejfves .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aiujejfves .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aiujejfves .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aiujejfves .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aiujejfves .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aiujejfves .gt_left { text-align: left; }
 #aiujejfves .gt_center { text-align: center; }
 #aiujejfves .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aiujejfves .gt_font_normal { font-weight: normal; }
 #aiujejfves .gt_font_bold { font-weight: bold; }
 #aiujejfves .gt_font_italic { font-style: italic; }
 #aiujejfves .gt_super { font-size: 65%; }
 #aiujejfves .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aiujejfves .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aiujejfves .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aiujejfves .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aiujejfves .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aiujejfves .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_right" headers="province.NL_ZH province.NL_ZH.pop">1</td>
<td class="gt_row gt_right" headers="province.NL_ZH province.NL_ZH.gdp">4</td>
<td class="gt_row gt_right" headers="province.NL_NH province.NL_NH.pop">7</td>
<td class="gt_row gt_right" headers="province.NL_NH province.NL_NH.gdp">10</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="province.NL_ZH province.NL_ZH.pop">2</td>
<td class="gt_row gt_right" headers="province.NL_ZH province.NL_ZH.gdp">5</td>
<td class="gt_row gt_right" headers="province.NL_NH province.NL_NH.pop">8</td>
<td class="gt_row gt_right" headers="province.NL_NH province.NL_NH.gdp">11</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="province.NL_ZH province.NL_ZH.pop">3</td>
<td class="gt_row gt_right" headers="province.NL_ZH province.NL_ZH.gdp">6</td>
<td class="gt_row gt_right" headers="province.NL_NH province.NL_NH.pop">9</td>
<td class="gt_row gt_right" headers="province.NL_NH province.NL_NH.gdp">12</td>
</tr>
</tbody>
</table>


``` python
# the name "province" repeats in the styled table,
# because the first spanner is column names
gt.tab_spanner_delim(reverse=True)
```


<style>
#nptpspvdwf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nptpspvdwf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nptpspvdwf p { margin: 0; padding: 0; }
 #nptpspvdwf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nptpspvdwf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nptpspvdwf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nptpspvdwf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nptpspvdwf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nptpspvdwf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nptpspvdwf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nptpspvdwf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nptpspvdwf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nptpspvdwf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nptpspvdwf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nptpspvdwf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nptpspvdwf .gt_spanner_row { border-bottom-style: hidden; }
 #nptpspvdwf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nptpspvdwf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nptpspvdwf .gt_from_md> :first-child { margin-top: 0; }
 #nptpspvdwf .gt_from_md> :last-child { margin-bottom: 0; }
 #nptpspvdwf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nptpspvdwf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nptpspvdwf .gt_indent_1 { text-indent: 5px; }
 #nptpspvdwf .gt_indent_2 { text-indent: calc(5px * 2); }
 #nptpspvdwf .gt_indent_3 { text-indent: calc(5px * 3); }
 #nptpspvdwf .gt_indent_4 { text-indent: calc(5px * 4); }
 #nptpspvdwf .gt_indent_5 { text-indent: calc(5px * 5); }
 #nptpspvdwf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nptpspvdwf .gt_row_group_first td { border-top-width: 2px; }
 #nptpspvdwf .gt_row_group_first th { border-top-width: 2px; }
 #nptpspvdwf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nptpspvdwf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nptpspvdwf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nptpspvdwf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nptpspvdwf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nptpspvdwf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nptpspvdwf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nptpspvdwf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nptpspvdwf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nptpspvdwf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nptpspvdwf .gt_left { text-align: left; }
 #nptpspvdwf .gt_center { text-align: center; }
 #nptpspvdwf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nptpspvdwf .gt_font_normal { font-weight: normal; }
 #nptpspvdwf .gt_font_bold { font-weight: bold; }
 #nptpspvdwf .gt_font_italic { font-style: italic; }
 #nptpspvdwf .gt_super { font-size: 65%; }
 #nptpspvdwf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nptpspvdwf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nptpspvdwf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nptpspvdwf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nptpspvdwf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nptpspvdwf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th id="pop" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col">pop</th>
<th id="gdp" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col">gdp</th>
<th id="pop" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col">pop</th>
<th id="gdp" class="gt_center gt_columns_bottom_border gt_columns_top_border gt_column_spanner_outer" scope="col">gdp</th>
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
<td class="gt_row gt_right" headers="pop NL_ZH province.NL_ZH.pop">1</td>
<td class="gt_row gt_right" headers="gdp NL_ZH province.NL_ZH.gdp">4</td>
<td class="gt_row gt_right" headers="pop NL_NH province.NL_NH.pop">7</td>
<td class="gt_row gt_right" headers="gdp NL_NH province.NL_NH.gdp">10</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="pop NL_ZH province.NL_ZH.pop">2</td>
<td class="gt_row gt_right" headers="gdp NL_ZH province.NL_ZH.gdp">5</td>
<td class="gt_row gt_right" headers="pop NL_NH province.NL_NH.pop">8</td>
<td class="gt_row gt_right" headers="gdp NL_NH province.NL_NH.gdp">11</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="pop NL_ZH province.NL_ZH.pop">3</td>
<td class="gt_row gt_right" headers="gdp NL_ZH province.NL_ZH.gdp">6</td>
<td class="gt_row gt_right" headers="pop NL_NH province.NL_NH.pop">9</td>
<td class="gt_row gt_right" headers="gdp NL_NH province.NL_NH.gdp">12</td>
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
#vjcbswlemm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vjcbswlemm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vjcbswlemm p { margin: 0; padding: 0; }
 #vjcbswlemm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vjcbswlemm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vjcbswlemm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vjcbswlemm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vjcbswlemm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vjcbswlemm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vjcbswlemm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vjcbswlemm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vjcbswlemm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vjcbswlemm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vjcbswlemm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vjcbswlemm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vjcbswlemm .gt_spanner_row { border-bottom-style: hidden; }
 #vjcbswlemm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vjcbswlemm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vjcbswlemm .gt_from_md> :first-child { margin-top: 0; }
 #vjcbswlemm .gt_from_md> :last-child { margin-bottom: 0; }
 #vjcbswlemm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vjcbswlemm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vjcbswlemm .gt_indent_1 { text-indent: 5px; }
 #vjcbswlemm .gt_indent_2 { text-indent: calc(5px * 2); }
 #vjcbswlemm .gt_indent_3 { text-indent: calc(5px * 3); }
 #vjcbswlemm .gt_indent_4 { text-indent: calc(5px * 4); }
 #vjcbswlemm .gt_indent_5 { text-indent: calc(5px * 5); }
 #vjcbswlemm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vjcbswlemm .gt_row_group_first td { border-top-width: 2px; }
 #vjcbswlemm .gt_row_group_first th { border-top-width: 2px; }
 #vjcbswlemm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vjcbswlemm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vjcbswlemm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vjcbswlemm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vjcbswlemm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vjcbswlemm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vjcbswlemm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vjcbswlemm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vjcbswlemm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vjcbswlemm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vjcbswlemm .gt_left { text-align: left; }
 #vjcbswlemm .gt_center { text-align: center; }
 #vjcbswlemm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vjcbswlemm .gt_font_normal { font-weight: normal; }
 #vjcbswlemm .gt_font_bold { font-weight: bold; }
 #vjcbswlemm .gt_font_italic { font-style: italic; }
 #vjcbswlemm .gt_super { font-size: 65%; }
 #vjcbswlemm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vjcbswlemm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vjcbswlemm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vjcbswlemm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vjcbswlemm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vjcbswlemm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left" headers="name">Addington Highlands</td>
<td class="gt_row gt_right" headers="population population_1996">2429</td>
<td class="gt_row gt_right" headers="population population_2001">2402</td>
<td class="gt_row gt_right" headers="population population_2006">2512</td>
<td class="gt_row gt_right" headers="population population_2011">2517</td>
<td class="gt_row gt_right" headers="population population_2016">2318</td>
<td class="gt_row gt_right" headers="population population_2021">2534</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="name">Adelaide Metcalfe</td>
<td class="gt_row gt_right" headers="population population_1996">3128</td>
<td class="gt_row gt_right" headers="population population_2001">3149</td>
<td class="gt_row gt_right" headers="population population_2006">3135</td>
<td class="gt_row gt_right" headers="population population_2011">3028</td>
<td class="gt_row gt_right" headers="population population_2016">2990</td>
<td class="gt_row gt_right" headers="population population_2021">3011</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="name">Adjala-Tosorontio</td>
<td class="gt_row gt_right" headers="population population_1996">9359</td>
<td class="gt_row gt_right" headers="population population_2001">10082</td>
<td class="gt_row gt_right" headers="population population_2006">10695</td>
<td class="gt_row gt_right" headers="population population_2011">10603</td>
<td class="gt_row gt_right" headers="population population_2016">10975</td>
<td class="gt_row gt_right" headers="population population_2021">10989</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="name">Admaston/Bromley</td>
<td class="gt_row gt_right" headers="population population_1996">2837</td>
<td class="gt_row gt_right" headers="population population_2001">2824</td>
<td class="gt_row gt_right" headers="population population_2006">2716</td>
<td class="gt_row gt_right" headers="population population_2011">2844</td>
<td class="gt_row gt_right" headers="population population_2016">2935</td>
<td class="gt_row gt_right" headers="population population_2021">2995</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="name">Ajax</td>
<td class="gt_row gt_right" headers="population population_1996">64430</td>
<td class="gt_row gt_right" headers="population population_2001">73753</td>
<td class="gt_row gt_right" headers="population population_2006">90167</td>
<td class="gt_row gt_right" headers="population population_2011">109600</td>
<td class="gt_row gt_right" headers="population population_2016">119677</td>
<td class="gt_row gt_right" headers="population population_2021">126666</td>
</tr>
</tbody>
</table>
