# GT.rm_footnotes()


Remove table footnotes.


Usage

``` python
GT.rm_footnotes(footnotes=None)
```


Footnotes are added to targeted locations with the <a href="GT.tab_footnote.html#great_tables.GT.tab_footnote" class="gdls-link"><code>tab_footnote()</code></a> method. With [rm_footnotes()](GT.rm_footnotes.md#great_tables.GT.rm_footnotes) we can remove all of them at once or, by supplying the `footnotes=` argument, only those at specific indices.


## Parameters


`footnotes: int | list[int] | None = None`  
The footnotes to remove. Supplied as a single index or a list of indices (`0`-based, in the order the footnotes were added). If `None` (the default), then all footnotes will be removed.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, let's create a table with two footnotes. We then remove all footnotes by calling [rm_footnotes()](GT.rm_footnotes.md#great_tables.GT.rm_footnotes) without any arguments.


``` python
from great_tables import GT
from great_tables.loc import body
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini)
    .tab_footnote(footnote="Manufacturer.", locations=body(columns="mfr", rows=[0]))
    .tab_footnote(footnote="Price.", locations=body(columns="msrp", rows=[0]))
    .rm_footnotes()
)
```


<style>
#vltbeonydn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vltbeonydn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vltbeonydn p { margin: 0; padding: 0; }
 #vltbeonydn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vltbeonydn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vltbeonydn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vltbeonydn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vltbeonydn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vltbeonydn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vltbeonydn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vltbeonydn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vltbeonydn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vltbeonydn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vltbeonydn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vltbeonydn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vltbeonydn .gt_spanner_row { border-bottom-style: hidden; }
 #vltbeonydn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vltbeonydn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vltbeonydn .gt_from_md> :first-child { margin-top: 0; }
 #vltbeonydn .gt_from_md> :last-child { margin-bottom: 0; }
 #vltbeonydn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vltbeonydn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vltbeonydn .gt_indent_1 { text-indent: 5px; }
 #vltbeonydn .gt_indent_2 { text-indent: calc(5px * 2); }
 #vltbeonydn .gt_indent_3 { text-indent: calc(5px * 3); }
 #vltbeonydn .gt_indent_4 { text-indent: calc(5px * 4); }
 #vltbeonydn .gt_indent_5 { text-indent: calc(5px * 5); }
 #vltbeonydn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vltbeonydn .gt_row_group_first td { border-top-width: 2px; }
 #vltbeonydn .gt_row_group_first th { border-top-width: 2px; }
 #vltbeonydn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vltbeonydn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vltbeonydn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vltbeonydn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vltbeonydn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vltbeonydn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vltbeonydn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vltbeonydn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vltbeonydn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vltbeonydn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vltbeonydn .gt_left { text-align: left; }
 #vltbeonydn .gt_center { text-align: center; }
 #vltbeonydn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vltbeonydn .gt_font_normal { font-weight: normal; }
 #vltbeonydn .gt_font_bold { font-weight: bold; }
 #vltbeonydn .gt_font_italic { font-style: italic; }
 #vltbeonydn .gt_super { font-size: 65%; }
 #vltbeonydn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vltbeonydn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vltbeonydn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vltbeonydn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vltbeonydn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vltbeonydn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| mfr     | model        | msrp     |
|---------|--------------|----------|
| Ford    | GT           | 447000.0 |
| Ferrari | 458 Speciale | 291744.0 |
| Ferrari | 458 Spider   | 263553.0 |
| Ferrari | 458 Italia   | 233509.0 |
| Ferrari | 488 GTB      | 245400.0 |


## See Also

<a href="GT.tab_footnote.html#great_tables.GT.tab_footnote" class="gdls-link"><code>tab_footnote()</code></a> to add a footnote to a table.
