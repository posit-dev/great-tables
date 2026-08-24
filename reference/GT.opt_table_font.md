# GT.opt_table_font()


Options to define font choices for the entire table.


Usage

``` python
GT.opt_table_font(
    font=None,
    stack=None,
    weight=None,
    style=None,
    add=True,
)
```


The [opt_table_font()](GT.opt_table_font.md#great_tables.GT.opt_table_font) method makes it possible to define fonts used for an entire table. Any font names supplied in `font=` will (by default, with `add=True`) be placed before the names present in the existing font stack (i.e., they will take precedence). You can choose to base the font stack on those provided by the [`system_fonts()`](%60system_fonts.md%60) helper function by providing a valid keyword for a themed set of fonts. Take note that you could still have entirely different fonts in specific locations of the table. To make that possible you would need to use <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> in conjunction with <a href="style.text.html#great_tables.style.text" class="gdls-link"><code>style.text()</code></a>.


## Parameters


`font: str | list[str] | dict[str, str] | GoogleFont | None = None`  
One or more font names available on the user's system. This can be provided as a string or a list of strings. Alternatively, you can specify font names using the [google_font()](google_font.md#great_tables.google_font) helper function. The default value is `None` since you could instead opt to use `stack` to define a list of fonts.

`stack: FontStackName | None = None`  
A name that is representative of a font stack (obtained via internally via the [system_fonts()](system_fonts.md#great_tables.system_fonts) helper function. If provided, this new stack will replace any defined fonts and any `font=` values will be prepended.

`style: str | None = None`  
An option to modify the text style. Can be one of either `"normal"`, `"italic"`, or `"oblique"`.

`weight: str | float | None = None`  
Option to set the weight of the font. Can be a text-based keyword such as `"normal"`, `"bold"`, `"lighter"`, `"bolder"`, or, a numeric value between `1` and `1000`. Please note that typefaces have varying support for the numeric mapping of weight.

`add: bool = ``True`  
Should fonts be added to the beginning of any already-defined fonts for the table? By default, this is `True` and is recommended since those fonts already present can serve as fallbacks when everything specified in `font` is not available. If a `stack=` value is provided, then `add` will automatically set to `False`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Possibilities For The `stack` Argument

There are several themed font stacks available via the [`system_fonts()`](%60system_fonts.md%60) helper function. That function can be used to generate all or a segment of a list supplied to the `font=` argument. However, using the `stack=` argument with one of the 15 keywords for the font stacks available in [`system_fonts()`](%60system_fonts.md%60), we could be sure that the typeface class will work across multiple computer systems. Any of the following keywords can be used with `stack=`:

- `"system-ui"`
- `"transitional"`
- `"old-style"`
- `"humanist"`
- `"geometric-humanist"`
- `"classical-humanist"`
- `"neo-grotesque"`
- `"monospace-slab-serif"`
- `"monospace-code"`
- `"industrial"`
- `"rounded-sans"`
- `"slab-serif"`
- `"antique"`
- `"didone"`
- `"handwritten"`


## Examples

Let's use a subset of the [sp500](data.sp500.md#great_tables.data.sp500) dataset to create a small table. With [opt_table_font()](GT.opt_table_font.md#great_tables.GT.opt_table_font) we can add some preferred font choices for modifying the text of the entire table. Here we'll use the `"Superclarendon"` and `"Georgia"` fonts (the second font serves as a fallback).


``` python
import polars as pl
from great_tables import GT
from great_tables.data import sp500

sp500_mini = pl.from_pandas(sp500).slice(0, 10).drop(["volume", "adj_close"])

(
    GT(sp500_mini, rowname_col="date")
    .fmt_currency(use_seps=False)
    .opt_table_font(font=["Superclarendon", "Georgia"])
)
```


<style>
#bhzccfnchi table {
          font-family: Superclarendon, Georgia, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bhzccfnchi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bhzccfnchi p { margin: 0; padding: 0; }
 #bhzccfnchi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bhzccfnchi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bhzccfnchi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bhzccfnchi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bhzccfnchi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhzccfnchi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhzccfnchi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhzccfnchi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bhzccfnchi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bhzccfnchi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bhzccfnchi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bhzccfnchi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bhzccfnchi .gt_spanner_row { border-bottom-style: hidden; }
 #bhzccfnchi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bhzccfnchi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bhzccfnchi .gt_from_md> :first-child { margin-top: 0; }
 #bhzccfnchi .gt_from_md> :last-child { margin-bottom: 0; }
 #bhzccfnchi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bhzccfnchi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bhzccfnchi .gt_indent_1 { text-indent: 5px; }
 #bhzccfnchi .gt_indent_2 { text-indent: calc(5px * 2); }
 #bhzccfnchi .gt_indent_3 { text-indent: calc(5px * 3); }
 #bhzccfnchi .gt_indent_4 { text-indent: calc(5px * 4); }
 #bhzccfnchi .gt_indent_5 { text-indent: calc(5px * 5); }
 #bhzccfnchi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bhzccfnchi .gt_row_group_first td { border-top-width: 2px; }
 #bhzccfnchi .gt_row_group_first th { border-top-width: 2px; }
 #bhzccfnchi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bhzccfnchi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhzccfnchi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhzccfnchi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bhzccfnchi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhzccfnchi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhzccfnchi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bhzccfnchi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bhzccfnchi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhzccfnchi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhzccfnchi .gt_left { text-align: left; }
 #bhzccfnchi .gt_center { text-align: center; }
 #bhzccfnchi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bhzccfnchi .gt_font_normal { font-weight: normal; }
 #bhzccfnchi .gt_font_bold { font-weight: bold; }
 #bhzccfnchi .gt_font_italic { font-style: italic; }
 #bhzccfnchi .gt_super { font-size: 65%; }
 #bhzccfnchi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhzccfnchi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bhzccfnchi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhzccfnchi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhzccfnchi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bhzccfnchi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|            | open      | high      | low       | close     |
|------------|-----------|-----------|-----------|-----------|
| 2015-12-31 | \$2060.59 | \$2062.54 | \$2043.62 | \$2043.94 |
| 2015-12-30 | \$2077.34 | \$2077.34 | \$2061.97 | \$2063.36 |
| 2015-12-29 | \$2060.54 | \$2081.56 | \$2060.54 | \$2078.36 |
| 2015-12-28 | \$2057.77 | \$2057.77 | \$2044.20 | \$2056.50 |
| 2015-12-24 | \$2063.52 | \$2067.36 | \$2058.73 | \$2060.99 |
| 2015-12-23 | \$2042.20 | \$2064.73 | \$2042.20 | \$2064.29 |
| 2015-12-22 | \$2023.15 | \$2042.74 | \$2020.49 | \$2038.97 |
| 2015-12-21 | \$2010.27 | \$2022.90 | \$2005.93 | \$2021.15 |
| 2015-12-18 | \$2040.81 | \$2040.81 | \$2005.33 | \$2005.55 |
| 2015-12-17 | \$2073.76 | \$2076.37 | \$2041.66 | \$2041.89 |


In practice, both of these fonts are not likely to be available on all systems. The [opt_table_font()](GT.opt_table_font.md#great_tables.GT.opt_table_font) method safeguards against this by prepending the fonts in the `font=` list to the existing font stack. This way, if both fonts are not available, the table will fall back to using the list of default table fonts. This behavior is controlled by the `add=` argument, which is `True` by default.

With the [sza](data.sza.md#great_tables.data.sza) dataset we'll create a two-column, eleven-row table. Within [opt_table_font()](GT.opt_table_font.md#great_tables.GT.opt_table_font), the `stack=` argument will be supplied with the "rounded-sans" font stack. This sets up a family of fonts with rounded, curved letterforms that should be locally available in different computing environments.


``` python
from great_tables.data import sza

sza_mini = (
    pl.from_pandas(sza)
    .filter((pl.col("latitude") == "20") & (pl.col("month") == "jan"))
    .drop_nulls()
    .drop(["latitude", "month"])
)

(
    GT(sza_mini)
    .opt_table_font(stack="rounded-sans")
    .opt_all_caps()
)
```


<style>
#lxbdagiwvj table {
          font-family: ui-rounded, 'Hiragino Maru Gothic ProN', Quicksand, Comfortaa, Manjari, 'Arial Rounded MT', 'Arial Rounded MT Bold', Calibri, source-sans-pro, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lxbdagiwvj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lxbdagiwvj p { margin: 0; padding: 0; }
 #lxbdagiwvj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lxbdagiwvj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lxbdagiwvj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lxbdagiwvj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lxbdagiwvj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lxbdagiwvj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lxbdagiwvj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lxbdagiwvj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lxbdagiwvj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lxbdagiwvj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lxbdagiwvj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lxbdagiwvj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lxbdagiwvj .gt_spanner_row { border-bottom-style: hidden; }
 #lxbdagiwvj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lxbdagiwvj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lxbdagiwvj .gt_from_md> :first-child { margin-top: 0; }
 #lxbdagiwvj .gt_from_md> :last-child { margin-bottom: 0; }
 #lxbdagiwvj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lxbdagiwvj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lxbdagiwvj .gt_indent_1 { text-indent: 5px; }
 #lxbdagiwvj .gt_indent_2 { text-indent: calc(5px * 2); }
 #lxbdagiwvj .gt_indent_3 { text-indent: calc(5px * 3); }
 #lxbdagiwvj .gt_indent_4 { text-indent: calc(5px * 4); }
 #lxbdagiwvj .gt_indent_5 { text-indent: calc(5px * 5); }
 #lxbdagiwvj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lxbdagiwvj .gt_row_group_first td { border-top-width: 2px; }
 #lxbdagiwvj .gt_row_group_first th { border-top-width: 2px; }
 #lxbdagiwvj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lxbdagiwvj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lxbdagiwvj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lxbdagiwvj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lxbdagiwvj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lxbdagiwvj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lxbdagiwvj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lxbdagiwvj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lxbdagiwvj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lxbdagiwvj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lxbdagiwvj .gt_left { text-align: left; }
 #lxbdagiwvj .gt_center { text-align: center; }
 #lxbdagiwvj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lxbdagiwvj .gt_font_normal { font-weight: normal; }
 #lxbdagiwvj .gt_font_bold { font-weight: bold; }
 #lxbdagiwvj .gt_font_italic { font-style: italic; }
 #lxbdagiwvj .gt_super { font-size: 65%; }
 #lxbdagiwvj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lxbdagiwvj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lxbdagiwvj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lxbdagiwvj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lxbdagiwvj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lxbdagiwvj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| tst  | sza  |
|------|------|
| 0700 | 84.9 |
| 0730 | 78.7 |
| 0800 | 72.7 |
| 0830 | 66.1 |
| 0900 | 61.5 |
| 0930 | 56.5 |
| 1000 | 52.1 |
| 1030 | 48.3 |
| 1100 | 45.5 |
| 1130 | 43.6 |
| 1200 | 43.0 |
