# GT.fmt_index()


Format values as index characters.


Usage

``` python
GT.fmt_index(
    columns=None,
    rows=None,
    case="upper",
    index_algo="repeat",
    pattern="{x}",
    locale=None,
)
```


With numeric values in a **gt** table, we can transform those to index values, usually based on letters. These characters can be derived from a specified locale and they are intended for ordering (often leaving out characters with diacritical marks). For example, the value `1` would map to `"A"`, `2` to `"B"`, and so on. When the value exceeds the number of characters in the index set, the algorithm set by `index_algo` determines how to proceed: with `"repeat"`, characters are repeated (e.g., 27 becomes `"AA"`, 28 becomes `"BB"`); with `"excel"`, Excel-style column naming is used (e.g., 27 becomes `"AA"`, 28 becomes `"AB"`).


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`case: str = ``"upper"`  
The case of the resulting index characters. Use `"upper"` (the default) for uppercase letters or `"lower"` for lowercase.

`index_algo: str = ``"repeat"`  
The algorithm to use when values exceed the index character set size. `"repeat"` (the default) repeats characters (1→A, …, 27→AA, 28→BB). `"excel"` uses Excel-style column naming (1→A, …, 27→AA, 28→AB).

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by `{x}` and all other characters are interpreted as string literals.

`locale: str | None = None`  
An optional locale ID. Currently reserved for future use; index characters default to the English A-Z set regardless of locale.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [towny](data.towny.md#great_tables.data.towny) dataset to create a table of the five smallest census subdivisions by population. The ranking column is formatted as index characters (A through E) and merged with the subdivision name.


``` python
import polars as pl
from great_tables import GT, md, data

towny_mini = (
    data.pl.towny
    .select("name", "census_div", "population_2021")
    .group_by("census_div")
    .agg(pl.col("population_2021").sum().alias("population"))
    .sort("population")
    .head(5)
    .with_row_index("ranking", offset=1)
    .select("ranking", "census_div", "population")
)

(
    GT(towny_mini)
    .fmt_integer(columns="population")
    .fmt_index(columns="ranking", pattern="{x}.")
    .cols_merge(columns=["ranking", "census_div"])
    .cols_align(align="left", columns="ranking")
    .cols_label(
        ranking=md("Census<br>Subdivision"),
        population=md("Population<br>in 2021"),
    )
    .tab_header(title=md("The Smallest<br>Census Subdivisions"))
    .tab_options(table_width="325px")
)
```


<style>
#wjzcnvpxqo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wjzcnvpxqo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wjzcnvpxqo p { margin: 0; padding: 0; }
 #wjzcnvpxqo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: 325px; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wjzcnvpxqo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wjzcnvpxqo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wjzcnvpxqo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wjzcnvpxqo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjzcnvpxqo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjzcnvpxqo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjzcnvpxqo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wjzcnvpxqo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wjzcnvpxqo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wjzcnvpxqo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wjzcnvpxqo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wjzcnvpxqo .gt_spanner_row { border-bottom-style: hidden; }
 #wjzcnvpxqo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wjzcnvpxqo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wjzcnvpxqo .gt_from_md> :first-child { margin-top: 0; }
 #wjzcnvpxqo .gt_from_md> :last-child { margin-bottom: 0; }
 #wjzcnvpxqo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wjzcnvpxqo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wjzcnvpxqo .gt_indent_1 { text-indent: 5px; }
 #wjzcnvpxqo .gt_indent_2 { text-indent: calc(5px * 2); }
 #wjzcnvpxqo .gt_indent_3 { text-indent: calc(5px * 3); }
 #wjzcnvpxqo .gt_indent_4 { text-indent: calc(5px * 4); }
 #wjzcnvpxqo .gt_indent_5 { text-indent: calc(5px * 5); }
 #wjzcnvpxqo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wjzcnvpxqo .gt_row_group_first td { border-top-width: 2px; }
 #wjzcnvpxqo .gt_row_group_first th { border-top-width: 2px; }
 #wjzcnvpxqo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wjzcnvpxqo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjzcnvpxqo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjzcnvpxqo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wjzcnvpxqo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjzcnvpxqo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjzcnvpxqo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wjzcnvpxqo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wjzcnvpxqo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjzcnvpxqo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjzcnvpxqo .gt_left { text-align: left; }
 #wjzcnvpxqo .gt_center { text-align: center; }
 #wjzcnvpxqo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wjzcnvpxqo .gt_font_normal { font-weight: normal; }
 #wjzcnvpxqo .gt_font_bold { font-weight: bold; }
 #wjzcnvpxqo .gt_font_italic { font-style: italic; }
 #wjzcnvpxqo .gt_super { font-size: 65%; }
 #wjzcnvpxqo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjzcnvpxqo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wjzcnvpxqo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjzcnvpxqo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjzcnvpxqo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wjzcnvpxqo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_title gt_font_normal">The Smallest<br />
Census Subdivisions</th>
</tr>
<tr class="gt_col_headings">
<th id="ranking" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Census<br />
Subdivision</th>
<th id="population" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Population<br />
in 2021</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">A. Manitoulin</td>
<td class="gt_row gt_right">8,906</td>
</tr>
<tr>
<td class="gt_row gt_left">B. Rainy River</td>
<td class="gt_row gt_right">15,769</td>
</tr>
<tr>
<td class="gt_row gt_left">C. Sudbury</td>
<td class="gt_row gt_right">18,606</td>
</tr>
<tr>
<td class="gt_row gt_left">D. Haliburton</td>
<td class="gt_row gt_right">20,571</td>
</tr>
<tr>
<td class="gt_row gt_left">E. Prince Edward</td>
<td class="gt_row gt_right">25,704</td>
</tr>
</tbody>
</table>


Using `index_algo="excel"` produces Excel-style column naming when values exceed 26. Here we show both algorithms side by side.


``` python
import polars as pl
from great_tables import GT

df = pl.DataFrame({
    "value": [1, 5, 13, 26, 27, 28, 52, 53, 100],
})

(
    GT(
        df.with_columns(
            repeat=pl.col("value"),
            excel=pl.col("value"),
        )
    )
    .fmt_index(columns="repeat", index_algo="repeat")
    .fmt_index(columns="excel", index_algo="excel")
    .cols_label(value="Value", repeat="Repeat", excel="Excel")
)
```


<style>
#letefkflwk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#letefkflwk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#letefkflwk p { margin: 0; padding: 0; }
 #letefkflwk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #letefkflwk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #letefkflwk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #letefkflwk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #letefkflwk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #letefkflwk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #letefkflwk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #letefkflwk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #letefkflwk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #letefkflwk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #letefkflwk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #letefkflwk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #letefkflwk .gt_spanner_row { border-bottom-style: hidden; }
 #letefkflwk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #letefkflwk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #letefkflwk .gt_from_md> :first-child { margin-top: 0; }
 #letefkflwk .gt_from_md> :last-child { margin-bottom: 0; }
 #letefkflwk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #letefkflwk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #letefkflwk .gt_indent_1 { text-indent: 5px; }
 #letefkflwk .gt_indent_2 { text-indent: calc(5px * 2); }
 #letefkflwk .gt_indent_3 { text-indent: calc(5px * 3); }
 #letefkflwk .gt_indent_4 { text-indent: calc(5px * 4); }
 #letefkflwk .gt_indent_5 { text-indent: calc(5px * 5); }
 #letefkflwk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #letefkflwk .gt_row_group_first td { border-top-width: 2px; }
 #letefkflwk .gt_row_group_first th { border-top-width: 2px; }
 #letefkflwk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #letefkflwk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #letefkflwk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #letefkflwk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #letefkflwk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #letefkflwk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #letefkflwk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #letefkflwk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #letefkflwk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #letefkflwk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #letefkflwk .gt_left { text-align: left; }
 #letefkflwk .gt_center { text-align: center; }
 #letefkflwk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #letefkflwk .gt_font_normal { font-weight: normal; }
 #letefkflwk .gt_font_bold { font-weight: bold; }
 #letefkflwk .gt_font_italic { font-style: italic; }
 #letefkflwk .gt_super { font-size: 65%; }
 #letefkflwk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #letefkflwk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #letefkflwk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #letefkflwk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #letefkflwk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #letefkflwk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Value | Repeat | Excel |
|-------|--------|-------|
| 1     | A      | A     |
| 5     | E      | E     |
| 13    | M      | M     |
| 26    | Z      | Z     |
| 27    | AA     | AA    |
| 28    | BB     | AB    |
| 52    | ZZ     | AZ    |
| 53    | AAA    | BA    |
| 100   | VVVV   | CV    |
