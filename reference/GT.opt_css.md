# GT.opt_css()


Option to add custom CSS for the table.


Usage

``` python
GT.opt_css(
    css,
    add=True,
    allow_duplicates=False,
)
```


[opt_css()](GT.opt_css.md#great_tables.GT.opt_css) makes it possible to add extra CSS rules to a table. This CSS will be added after the compiled CSS that Great Tables generates automatically when the object is transformed to an HTML output table.

If you want to set CSS styles on a specific table location, use [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) with [style.css()](style.css.md#great_tables.style.css) instead.


## Parameters


`css: str`  
The CSS to include as part of the rendered table's `<style>` element.

`add: bool = ``True`  
If `True`, the default, the CSS is added to any already-defined CSS (typically from previous calls of [opt_css()](GT.opt_css.md#great_tables.GT.opt_css) or `tab_options(table_additional_css=...)`). If this is set to `False`, the CSS provided here will replace any previously-stored CSS.

`allow_duplicates: bool = ``False`  
When this is `False` (the default), the CSS provided here won't be added (provided that `add=True`) if it is seen in the already-defined CSS.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `num` and `currency` columns). Through use of the [opt_css()](GT.opt_css.md#great_tables.GT.opt_css) method, we can insert CSS rulesets as a string. We need to ensure that the table ID is set explicitly (we've done so here with the ID value of `"one"`, setting it up with `GT(id=)`).


``` python
from great_tables import GT, exibble
import polars as pl

exibble_mini = pl.from_pandas(exibble).select(["num", "currency"])

(
    GT(exibble_mini, id="one")
    .fmt_currency(columns="currency", currency="HKD")
    .fmt_scientific(columns="num")
    .opt_css(
        css='''
        #one .gt_table {
          background-color: skyblue;
        }
        #one .gt_row {
          padding: 20px 30px;
        }
        #one .gt_col_heading {
          text-align: center !important;
        }
        '''
    )
)
```


<style>
#one table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#one thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#one p { margin: 0; padding: 0; }
 #one .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #one .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #one .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #one .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #one .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #one .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #one .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #one .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #one .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #one .gt_column_spanner_outer:first-child { padding-left: 0; }
 #one .gt_column_spanner_outer:last-child { padding-right: 0; }
 #one .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #one .gt_spanner_row { border-bottom-style: hidden; }
 #one .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #one .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #one .gt_from_md> :first-child { margin-top: 0; }
 #one .gt_from_md> :last-child { margin-bottom: 0; }
 #one .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #one .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #one .gt_indent_1 { text-indent: 5px; }
 #one .gt_indent_2 { text-indent: calc(5px * 2); }
 #one .gt_indent_3 { text-indent: calc(5px * 3); }
 #one .gt_indent_4 { text-indent: calc(5px * 4); }
 #one .gt_indent_5 { text-indent: calc(5px * 5); }
 #one .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #one .gt_row_group_first td { border-top-width: 2px; }
 #one .gt_row_group_first th { border-top-width: 2px; }
 #one .gt_striped { color: #333333; background-color: #F4F4F4; }
 #one .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #one .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #one .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #one .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #one .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #one .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #one .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #one .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #one .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #one .gt_left { text-align: left; }
 #one .gt_center { text-align: center; }
 #one .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #one .gt_font_normal { font-weight: normal; }
 #one .gt_font_bold { font-weight: bold; }
 #one .gt_font_italic { font-style: italic; }
 #one .gt_super { font-size: 65%; }
 #one .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #one .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #one .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #one .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #one .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #one .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
#one .gt_table {
          background-color: skyblue;
        }
        #one .gt_row {
          padding: 20px 30px;
        }
        #one .gt_col_heading {
          text-align: center !important;
        }

</style>

| num                    | currency      |
|------------------------|---------------|
| 1.11 × 10<sup>−1</sup> | HK\$49.95     |
| 2.22                   | HK\$17.95     |
| 3.33 × 10<sup>1</sup>  | HK\$1.39      |
| 4.44 × 10<sup>2</sup>  | HK\$65,100.00 |
| 5.55 × 10<sup>3</sup>  | HK\$1,325.81  |
| None                   | HK\$13.26     |
| 7.77 × 10<sup>5</sup>  | None          |
| 8.88 × 10<sup>6</sup>  | HK\$0.44      |
