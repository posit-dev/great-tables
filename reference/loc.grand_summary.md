# loc.grand_summary


Target the data cells in grand summary rows.


Usage

``` python
loc.grand_summary(
    columns=None,
    rows=None,
    mask=None,
)
```


With [loc.grand_summary()](loc.grand_summary.md#great_tables.loc.grand_summary) we can target the cells containing the grand summary data. This is useful for applying custom styling with the <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> method. That method has a `locations=` argument and this class should be used there to perform the targeting.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
The rows to target. Can either be a single row name or a series of row names provided in a list. Note that if rows are targeted by index, top and bottom grand summary rows are indexed as one combined list starting with the top rows.


## Returns


`LocGrandSummary`  
A LocGrandSummary object, which is used for a `locations=` argument if specifying the table's grand summary rows.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style all of the grand summary cells by using `locations=loc.grand_summary()` within <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>.


``` python
from great_tables import GT, style, loc, vals
from great_tables.data import gtcars

(
    GT(
        gtcars[["mfr", "model", "hp", "trq", "mpg_c"]].head(6),
        rowname_col="model",
    )
    .fmt_integer(columns=["hp", "trq", "mpg_c"])
    .grand_summary_rows(
        fns={
            "Min": lambda df: df.min(numeric_only=True),
            "Max": lambda x: x.max(numeric_only=True),
        },
        side="top",
        fmt=vals.fmt_integer,
    )
    .tab_style(
        style=[style.text(color="crimson", weight="bold"), style.fill(color="lightgray")],
        locations=loc.grand_summary(),
    )
)
```


<style>
#xpfstvssie table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xpfstvssie thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xpfstvssie p { margin: 0; padding: 0; }
 #xpfstvssie .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xpfstvssie .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xpfstvssie .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xpfstvssie .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xpfstvssie .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xpfstvssie .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xpfstvssie .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xpfstvssie .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xpfstvssie .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xpfstvssie .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xpfstvssie .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xpfstvssie .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xpfstvssie .gt_spanner_row { border-bottom-style: hidden; }
 #xpfstvssie .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xpfstvssie .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xpfstvssie .gt_from_md> :first-child { margin-top: 0; }
 #xpfstvssie .gt_from_md> :last-child { margin-bottom: 0; }
 #xpfstvssie .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xpfstvssie .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xpfstvssie .gt_indent_1 { text-indent: 5px; }
 #xpfstvssie .gt_indent_2 { text-indent: calc(5px * 2); }
 #xpfstvssie .gt_indent_3 { text-indent: calc(5px * 3); }
 #xpfstvssie .gt_indent_4 { text-indent: calc(5px * 4); }
 #xpfstvssie .gt_indent_5 { text-indent: calc(5px * 5); }
 #xpfstvssie .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xpfstvssie .gt_row_group_first td { border-top-width: 2px; }
 #xpfstvssie .gt_row_group_first th { border-top-width: 2px; }
 #xpfstvssie .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xpfstvssie .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xpfstvssie .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xpfstvssie .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xpfstvssie .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xpfstvssie .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xpfstvssie .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xpfstvssie .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xpfstvssie .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xpfstvssie .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xpfstvssie .gt_left { text-align: left; }
 #xpfstvssie .gt_center { text-align: center; }
 #xpfstvssie .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xpfstvssie .gt_font_normal { font-weight: normal; }
 #xpfstvssie .gt_font_bold { font-weight: bold; }
 #xpfstvssie .gt_font_italic { font-style: italic; }
 #xpfstvssie .gt_super { font-size: 65%; }
 #xpfstvssie .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xpfstvssie .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xpfstvssie .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xpfstvssie .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xpfstvssie .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xpfstvssie .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|              | mfr     | hp  | trq | mpg_c |
|--------------|---------|-----|-----|-------|
| Min          | ---     | 553 | 398 | 11    |
| Max          | ---     | 661 | 561 | 16    |
| GT           | Ford    | 647 | 550 | 11    |
| 458 Speciale | Ferrari | 597 | 398 | 13    |
| 458 Spider   | Ferrari | 562 | 398 | 13    |
| 458 Italia   | Ferrari | 562 | 398 | 13    |
| 488 GTB      | Ferrari | 661 | 561 | 15    |
| California   | Ferrari | 553 | 557 | 16    |
