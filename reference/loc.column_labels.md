# loc.column_labels


Target column labels.


Usage

``` python
loc.column_labels(columns=None)
```


With [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels), we can target the cells containing the column labels. This is useful for applying custom styling with the <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> method. That method has a `locations=` argument and this class should be used there to perform the targeting.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. If no columns are specified, all columns are targeted.


## Returns


`LocColumnLabels`  
A LocColumnLabels object, which is used for a `locations=` argument if specifying the table's column labels.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style all three of the column labels by using `locations=loc.column_labels()` within <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>. Note that no specification of `columns=` is needed here because we want to target all columns.


``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(gtcars[["mfr", "model", "msrp"]].head(5))
    .tab_style(
        style=style.text(color="blue", size="large", weight="bold"),
        locations=loc.column_labels()
    )
)
```


<style>
#srlconyzmq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#srlconyzmq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#srlconyzmq p { margin: 0; padding: 0; }
 #srlconyzmq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #srlconyzmq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #srlconyzmq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #srlconyzmq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #srlconyzmq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #srlconyzmq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #srlconyzmq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #srlconyzmq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #srlconyzmq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #srlconyzmq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #srlconyzmq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #srlconyzmq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #srlconyzmq .gt_spanner_row { border-bottom-style: hidden; }
 #srlconyzmq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #srlconyzmq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #srlconyzmq .gt_from_md> :first-child { margin-top: 0; }
 #srlconyzmq .gt_from_md> :last-child { margin-bottom: 0; }
 #srlconyzmq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #srlconyzmq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #srlconyzmq .gt_indent_1 { text-indent: 5px; }
 #srlconyzmq .gt_indent_2 { text-indent: calc(5px * 2); }
 #srlconyzmq .gt_indent_3 { text-indent: calc(5px * 3); }
 #srlconyzmq .gt_indent_4 { text-indent: calc(5px * 4); }
 #srlconyzmq .gt_indent_5 { text-indent: calc(5px * 5); }
 #srlconyzmq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #srlconyzmq .gt_row_group_first td { border-top-width: 2px; }
 #srlconyzmq .gt_row_group_first th { border-top-width: 2px; }
 #srlconyzmq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #srlconyzmq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #srlconyzmq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #srlconyzmq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #srlconyzmq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #srlconyzmq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #srlconyzmq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #srlconyzmq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #srlconyzmq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #srlconyzmq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #srlconyzmq .gt_left { text-align: left; }
 #srlconyzmq .gt_center { text-align: center; }
 #srlconyzmq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #srlconyzmq .gt_font_normal { font-weight: normal; }
 #srlconyzmq .gt_font_bold { font-weight: bold; }
 #srlconyzmq .gt_font_italic { font-style: italic; }
 #srlconyzmq .gt_super { font-size: 65%; }
 #srlconyzmq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #srlconyzmq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #srlconyzmq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #srlconyzmq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #srlconyzmq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #srlconyzmq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| mfr     | model        | msrp     |
|---------|--------------|----------|
| Ford    | GT           | 447000.0 |
| Ferrari | 458 Speciale | 291744.0 |
| Ferrari | 458 Spider   | 263553.0 |
| Ferrari | 458 Italia   | 233509.0 |
| Ferrari | 488 GTB      | 245400.0 |
