# google_font()


Specify a font from the *Google Fonts* service.


Usage

``` python
google_font(name)
```


The [google_font()](google_font.md#great_tables.google_font) helper function can be used wherever a font name might be specified. There are two instances where this helper can be used:

1.  `opt_table_font(font=...)` (for setting a table font)
2.  `style.text(font=...)` (itself used in <a href="../reference/GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>)


## Parameters


`name: str`  
The name of the Google Font to use.


## Returns


`GoogleFont`  
A GoogleFont object, which contains the name of the font and methods for incorporating the font in HTML output tables.


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a table of two columns and eight rows. We'll replace missing values with em dashes using <a href="../reference/GT.sub_missing.html#great_tables.GT.sub_missing" class="gdls-link"><code>sub_missing()</code></a>. For text in the time column, we will use the font called `"IBM Plex Mono"` which is available from Google Fonts. This is defined inside the [google_font()](google_font.md#great_tables.google_font) call, itself within the <a href="../reference/style.text.html#great_tables.style.text" class="gdls-link"><code>style.text()</code></a> method that's applied to the `style=` parameter of <a href="../reference/GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>.


``` python
from great_tables import GT, exibble, style, loc, google_font

(
    GT(exibble[["char", "time"]])
    .sub_missing()
    .tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body(columns="time")
    )
)
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
#projzxgtof table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#projzxgtof thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#projzxgtof p { margin: 0; padding: 0; }
 #projzxgtof .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #projzxgtof .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #projzxgtof .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #projzxgtof .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #projzxgtof .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #projzxgtof .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #projzxgtof .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #projzxgtof .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #projzxgtof .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #projzxgtof .gt_column_spanner_outer:first-child { padding-left: 0; }
 #projzxgtof .gt_column_spanner_outer:last-child { padding-right: 0; }
 #projzxgtof .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #projzxgtof .gt_spanner_row { border-bottom-style: hidden; }
 #projzxgtof .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #projzxgtof .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #projzxgtof .gt_from_md> :first-child { margin-top: 0; }
 #projzxgtof .gt_from_md> :last-child { margin-bottom: 0; }
 #projzxgtof .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #projzxgtof .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #projzxgtof .gt_indent_1 { text-indent: 5px; }
 #projzxgtof .gt_indent_2 { text-indent: calc(5px * 2); }
 #projzxgtof .gt_indent_3 { text-indent: calc(5px * 3); }
 #projzxgtof .gt_indent_4 { text-indent: calc(5px * 4); }
 #projzxgtof .gt_indent_5 { text-indent: calc(5px * 5); }
 #projzxgtof .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #projzxgtof .gt_row_group_first td { border-top-width: 2px; }
 #projzxgtof .gt_row_group_first th { border-top-width: 2px; }
 #projzxgtof .gt_striped { color: #333333; background-color: #F4F4F4; }
 #projzxgtof .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #projzxgtof .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #projzxgtof .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #projzxgtof .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #projzxgtof .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #projzxgtof .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #projzxgtof .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #projzxgtof .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #projzxgtof .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #projzxgtof .gt_left { text-align: left; }
 #projzxgtof .gt_center { text-align: center; }
 #projzxgtof .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #projzxgtof .gt_font_normal { font-weight: normal; }
 #projzxgtof .gt_font_bold { font-weight: bold; }
 #projzxgtof .gt_font_italic { font-style: italic; }
 #projzxgtof .gt_super { font-size: 65%; }
 #projzxgtof .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #projzxgtof .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #projzxgtof .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #projzxgtof .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #projzxgtof .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #projzxgtof .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| char       | time  |
|------------|-------|
| apricot    | 13:35 |
| banana     | 14:40 |
| coconut    | 15:45 |
| durian     | 16:50 |
| --          | 17:55 |
| fig        | --     |
| grapefruit | 19:10 |
| honeydew   | 20:20 |


We can use a subset of the [sp500](data.sp500.md#great_tables.data.sp500) dataset to create a small table. With <a href="../reference/GT.fmt_currency.html#great_tables.GT.fmt_currency" class="gdls-link"><code>fmt_currency()</code></a>, we can display values as monetary values. Then, we'll set a larger font size for the table and opt to use the `"Merriweather"` font by calling [google_font()](google_font.md#great_tables.google_font) within <a href="../reference/GT.opt_table_font.html#great_tables.GT.opt_table_font" class="gdls-link"><code>opt_table_font()</code></a>. In cases where that font may not materialize, we include two font fallbacks: `"Cochin"` and the catchall `"Serif"` group.


``` python
from great_tables import GT, google_font
from great_tables.data import sp500

(
    GT(sp500.drop(columns=["volume", "adj_close"]).head(10))
    .fmt_currency(columns=["open", "high", "low", "close"])
    .tab_options(table_font_size="20px")
    .opt_table_font(font=[google_font(name="Merriweather"), "Cochin", "Serif"])
)
```


<style>
@import url('https://fonts.googleapis.com/css2?family=Merriweather&display=swap');
#cqajcmmhmi table {
          font-family: Merriweather, Cochin, Serif, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cqajcmmhmi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cqajcmmhmi p { margin: 0; padding: 0; }
 #cqajcmmhmi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 20px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cqajcmmhmi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cqajcmmhmi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cqajcmmhmi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cqajcmmhmi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cqajcmmhmi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cqajcmmhmi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cqajcmmhmi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cqajcmmhmi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cqajcmmhmi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cqajcmmhmi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cqajcmmhmi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cqajcmmhmi .gt_spanner_row { border-bottom-style: hidden; }
 #cqajcmmhmi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cqajcmmhmi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cqajcmmhmi .gt_from_md> :first-child { margin-top: 0; }
 #cqajcmmhmi .gt_from_md> :last-child { margin-bottom: 0; }
 #cqajcmmhmi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cqajcmmhmi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cqajcmmhmi .gt_indent_1 { text-indent: 5px; }
 #cqajcmmhmi .gt_indent_2 { text-indent: calc(5px * 2); }
 #cqajcmmhmi .gt_indent_3 { text-indent: calc(5px * 3); }
 #cqajcmmhmi .gt_indent_4 { text-indent: calc(5px * 4); }
 #cqajcmmhmi .gt_indent_5 { text-indent: calc(5px * 5); }
 #cqajcmmhmi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cqajcmmhmi .gt_row_group_first td { border-top-width: 2px; }
 #cqajcmmhmi .gt_row_group_first th { border-top-width: 2px; }
 #cqajcmmhmi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cqajcmmhmi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cqajcmmhmi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cqajcmmhmi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cqajcmmhmi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cqajcmmhmi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cqajcmmhmi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cqajcmmhmi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cqajcmmhmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cqajcmmhmi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cqajcmmhmi .gt_left { text-align: left; }
 #cqajcmmhmi .gt_center { text-align: center; }
 #cqajcmmhmi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cqajcmmhmi .gt_font_normal { font-weight: normal; }
 #cqajcmmhmi .gt_font_bold { font-weight: bold; }
 #cqajcmmhmi .gt_font_italic { font-style: italic; }
 #cqajcmmhmi .gt_super { font-size: 65%; }
 #cqajcmmhmi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cqajcmmhmi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cqajcmmhmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cqajcmmhmi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cqajcmmhmi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cqajcmmhmi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | open       | high       | low        | close      |
|------------|------------|------------|------------|------------|
| 2015-12-31 | \$2,060.59 | \$2,062.54 | \$2,043.62 | \$2,043.94 |
| 2015-12-30 | \$2,077.34 | \$2,077.34 | \$2,061.97 | \$2,063.36 |
| 2015-12-29 | \$2,060.54 | \$2,081.56 | \$2,060.54 | \$2,078.36 |
| 2015-12-28 | \$2,057.77 | \$2,057.77 | \$2,044.20 | \$2,056.50 |
| 2015-12-24 | \$2,063.52 | \$2,067.36 | \$2,058.73 | \$2,060.99 |
| 2015-12-23 | \$2,042.20 | \$2,064.73 | \$2,042.20 | \$2,064.29 |
| 2015-12-22 | \$2,023.15 | \$2,042.74 | \$2,020.49 | \$2,038.97 |
| 2015-12-21 | \$2,010.27 | \$2,022.90 | \$2,005.93 | \$2,021.15 |
| 2015-12-18 | \$2,040.81 | \$2,040.81 | \$2,005.33 | \$2,005.55 |
| 2015-12-17 | \$2,073.76 | \$2,076.37 | \$2,041.66 | \$2,041.89 |
