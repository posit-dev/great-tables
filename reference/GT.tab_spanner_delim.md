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
#slhlwvrhro table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#slhlwvrhro thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#slhlwvrhro p { margin: 0; padding: 0; }
 #slhlwvrhro .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #slhlwvrhro .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #slhlwvrhro .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #slhlwvrhro .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #slhlwvrhro .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #slhlwvrhro .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #slhlwvrhro .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #slhlwvrhro .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #slhlwvrhro .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #slhlwvrhro .gt_column_spanner_outer:first-child { padding-left: 0; }
 #slhlwvrhro .gt_column_spanner_outer:last-child { padding-right: 0; }
 #slhlwvrhro .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #slhlwvrhro .gt_spanner_row { border-bottom-style: hidden; }
 #slhlwvrhro .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #slhlwvrhro .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #slhlwvrhro .gt_from_md> :first-child { margin-top: 0; }
 #slhlwvrhro .gt_from_md> :last-child { margin-bottom: 0; }
 #slhlwvrhro .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #slhlwvrhro .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #slhlwvrhro .gt_indent_1 { text-indent: 5px; }
 #slhlwvrhro .gt_indent_2 { text-indent: calc(5px * 2); }
 #slhlwvrhro .gt_indent_3 { text-indent: calc(5px * 3); }
 #slhlwvrhro .gt_indent_4 { text-indent: calc(5px * 4); }
 #slhlwvrhro .gt_indent_5 { text-indent: calc(5px * 5); }
 #slhlwvrhro .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #slhlwvrhro .gt_row_group_first td { border-top-width: 2px; }
 #slhlwvrhro .gt_row_group_first th { border-top-width: 2px; }
 #slhlwvrhro .gt_striped { color: #333333; background-color: #F4F4F4; }
 #slhlwvrhro .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #slhlwvrhro .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #slhlwvrhro .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #slhlwvrhro .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #slhlwvrhro .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #slhlwvrhro .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #slhlwvrhro .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #slhlwvrhro .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #slhlwvrhro .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #slhlwvrhro .gt_left { text-align: left; }
 #slhlwvrhro .gt_center { text-align: center; }
 #slhlwvrhro .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #slhlwvrhro .gt_font_normal { font-weight: normal; }
 #slhlwvrhro .gt_font_bold { font-weight: bold; }
 #slhlwvrhro .gt_font_italic { font-style: italic; }
 #slhlwvrhro .gt_super { font-size: 65%; }
 #slhlwvrhro .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #slhlwvrhro .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #slhlwvrhro .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #slhlwvrhro .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #slhlwvrhro .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #slhlwvrhro .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#myunissagb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#myunissagb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#myunissagb p { margin: 0; padding: 0; }
 #myunissagb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #myunissagb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #myunissagb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #myunissagb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #myunissagb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #myunissagb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #myunissagb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #myunissagb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #myunissagb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #myunissagb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #myunissagb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #myunissagb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #myunissagb .gt_spanner_row { border-bottom-style: hidden; }
 #myunissagb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #myunissagb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #myunissagb .gt_from_md> :first-child { margin-top: 0; }
 #myunissagb .gt_from_md> :last-child { margin-bottom: 0; }
 #myunissagb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #myunissagb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #myunissagb .gt_indent_1 { text-indent: 5px; }
 #myunissagb .gt_indent_2 { text-indent: calc(5px * 2); }
 #myunissagb .gt_indent_3 { text-indent: calc(5px * 3); }
 #myunissagb .gt_indent_4 { text-indent: calc(5px * 4); }
 #myunissagb .gt_indent_5 { text-indent: calc(5px * 5); }
 #myunissagb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #myunissagb .gt_row_group_first td { border-top-width: 2px; }
 #myunissagb .gt_row_group_first th { border-top-width: 2px; }
 #myunissagb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #myunissagb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #myunissagb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #myunissagb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #myunissagb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #myunissagb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #myunissagb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #myunissagb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #myunissagb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #myunissagb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #myunissagb .gt_left { text-align: left; }
 #myunissagb .gt_center { text-align: center; }
 #myunissagb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #myunissagb .gt_font_normal { font-weight: normal; }
 #myunissagb .gt_font_bold { font-weight: bold; }
 #myunissagb .gt_font_italic { font-style: italic; }
 #myunissagb .gt_super { font-size: 65%; }
 #myunissagb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #myunissagb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #myunissagb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #myunissagb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #myunissagb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #myunissagb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ghfviqwhum table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ghfviqwhum thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ghfviqwhum p { margin: 0; padding: 0; }
 #ghfviqwhum .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ghfviqwhum .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ghfviqwhum .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ghfviqwhum .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ghfviqwhum .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ghfviqwhum .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghfviqwhum .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ghfviqwhum .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ghfviqwhum .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ghfviqwhum .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ghfviqwhum .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ghfviqwhum .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ghfviqwhum .gt_spanner_row { border-bottom-style: hidden; }
 #ghfviqwhum .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ghfviqwhum .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ghfviqwhum .gt_from_md> :first-child { margin-top: 0; }
 #ghfviqwhum .gt_from_md> :last-child { margin-bottom: 0; }
 #ghfviqwhum .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ghfviqwhum .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ghfviqwhum .gt_indent_1 { text-indent: 5px; }
 #ghfviqwhum .gt_indent_2 { text-indent: calc(5px * 2); }
 #ghfviqwhum .gt_indent_3 { text-indent: calc(5px * 3); }
 #ghfviqwhum .gt_indent_4 { text-indent: calc(5px * 4); }
 #ghfviqwhum .gt_indent_5 { text-indent: calc(5px * 5); }
 #ghfviqwhum .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ghfviqwhum .gt_row_group_first td { border-top-width: 2px; }
 #ghfviqwhum .gt_row_group_first th { border-top-width: 2px; }
 #ghfviqwhum .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ghfviqwhum .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghfviqwhum .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ghfviqwhum .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ghfviqwhum .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghfviqwhum .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ghfviqwhum .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ghfviqwhum .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ghfviqwhum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghfviqwhum .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ghfviqwhum .gt_left { text-align: left; }
 #ghfviqwhum .gt_center { text-align: center; }
 #ghfviqwhum .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ghfviqwhum .gt_font_normal { font-weight: normal; }
 #ghfviqwhum .gt_font_bold { font-weight: bold; }
 #ghfviqwhum .gt_font_italic { font-style: italic; }
 #ghfviqwhum .gt_super { font-size: 65%; }
 #ghfviqwhum .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghfviqwhum .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ghfviqwhum .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghfviqwhum .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ghfviqwhum .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ghfviqwhum .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#chzrrbkwrc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#chzrrbkwrc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#chzrrbkwrc p { margin: 0; padding: 0; }
 #chzrrbkwrc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #chzrrbkwrc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #chzrrbkwrc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #chzrrbkwrc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #chzrrbkwrc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #chzrrbkwrc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #chzrrbkwrc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #chzrrbkwrc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #chzrrbkwrc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #chzrrbkwrc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #chzrrbkwrc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #chzrrbkwrc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #chzrrbkwrc .gt_spanner_row { border-bottom-style: hidden; }
 #chzrrbkwrc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #chzrrbkwrc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #chzrrbkwrc .gt_from_md> :first-child { margin-top: 0; }
 #chzrrbkwrc .gt_from_md> :last-child { margin-bottom: 0; }
 #chzrrbkwrc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #chzrrbkwrc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #chzrrbkwrc .gt_indent_1 { text-indent: 5px; }
 #chzrrbkwrc .gt_indent_2 { text-indent: calc(5px * 2); }
 #chzrrbkwrc .gt_indent_3 { text-indent: calc(5px * 3); }
 #chzrrbkwrc .gt_indent_4 { text-indent: calc(5px * 4); }
 #chzrrbkwrc .gt_indent_5 { text-indent: calc(5px * 5); }
 #chzrrbkwrc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #chzrrbkwrc .gt_row_group_first td { border-top-width: 2px; }
 #chzrrbkwrc .gt_row_group_first th { border-top-width: 2px; }
 #chzrrbkwrc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #chzrrbkwrc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #chzrrbkwrc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #chzrrbkwrc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #chzrrbkwrc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #chzrrbkwrc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #chzrrbkwrc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #chzrrbkwrc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #chzrrbkwrc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #chzrrbkwrc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #chzrrbkwrc .gt_left { text-align: left; }
 #chzrrbkwrc .gt_center { text-align: center; }
 #chzrrbkwrc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #chzrrbkwrc .gt_font_normal { font-weight: normal; }
 #chzrrbkwrc .gt_font_bold { font-weight: bold; }
 #chzrrbkwrc .gt_font_italic { font-style: italic; }
 #chzrrbkwrc .gt_super { font-size: 65%; }
 #chzrrbkwrc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #chzrrbkwrc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #chzrrbkwrc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #chzrrbkwrc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #chzrrbkwrc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #chzrrbkwrc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
