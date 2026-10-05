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

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

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
#vgfxazrpdc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vgfxazrpdc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vgfxazrpdc p { margin: 0; padding: 0; }
 #vgfxazrpdc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: 325px; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vgfxazrpdc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vgfxazrpdc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vgfxazrpdc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vgfxazrpdc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vgfxazrpdc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vgfxazrpdc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vgfxazrpdc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vgfxazrpdc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vgfxazrpdc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vgfxazrpdc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vgfxazrpdc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vgfxazrpdc .gt_spanner_row { border-bottom-style: hidden; }
 #vgfxazrpdc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vgfxazrpdc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vgfxazrpdc .gt_from_md> :first-child { margin-top: 0; }
 #vgfxazrpdc .gt_from_md> :last-child { margin-bottom: 0; }
 #vgfxazrpdc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vgfxazrpdc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vgfxazrpdc .gt_indent_1 { text-indent: 5px; }
 #vgfxazrpdc .gt_indent_2 { text-indent: calc(5px * 2); }
 #vgfxazrpdc .gt_indent_3 { text-indent: calc(5px * 3); }
 #vgfxazrpdc .gt_indent_4 { text-indent: calc(5px * 4); }
 #vgfxazrpdc .gt_indent_5 { text-indent: calc(5px * 5); }
 #vgfxazrpdc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vgfxazrpdc .gt_row_group_first td { border-top-width: 2px; }
 #vgfxazrpdc .gt_row_group_first th { border-top-width: 2px; }
 #vgfxazrpdc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vgfxazrpdc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vgfxazrpdc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vgfxazrpdc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vgfxazrpdc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vgfxazrpdc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vgfxazrpdc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vgfxazrpdc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vgfxazrpdc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vgfxazrpdc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vgfxazrpdc .gt_left { text-align: left; }
 #vgfxazrpdc .gt_center { text-align: center; }
 #vgfxazrpdc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vgfxazrpdc .gt_font_normal { font-weight: normal; }
 #vgfxazrpdc .gt_font_bold { font-weight: bold; }
 #vgfxazrpdc .gt_font_italic { font-style: italic; }
 #vgfxazrpdc .gt_super { font-size: 65%; }
 #vgfxazrpdc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vgfxazrpdc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vgfxazrpdc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vgfxazrpdc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vgfxazrpdc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vgfxazrpdc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#urdqahguiy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#urdqahguiy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#urdqahguiy p { margin: 0; padding: 0; }
 #urdqahguiy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #urdqahguiy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #urdqahguiy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #urdqahguiy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #urdqahguiy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #urdqahguiy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #urdqahguiy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #urdqahguiy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #urdqahguiy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #urdqahguiy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #urdqahguiy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #urdqahguiy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #urdqahguiy .gt_spanner_row { border-bottom-style: hidden; }
 #urdqahguiy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #urdqahguiy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #urdqahguiy .gt_from_md> :first-child { margin-top: 0; }
 #urdqahguiy .gt_from_md> :last-child { margin-bottom: 0; }
 #urdqahguiy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #urdqahguiy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #urdqahguiy .gt_indent_1 { text-indent: 5px; }
 #urdqahguiy .gt_indent_2 { text-indent: calc(5px * 2); }
 #urdqahguiy .gt_indent_3 { text-indent: calc(5px * 3); }
 #urdqahguiy .gt_indent_4 { text-indent: calc(5px * 4); }
 #urdqahguiy .gt_indent_5 { text-indent: calc(5px * 5); }
 #urdqahguiy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #urdqahguiy .gt_row_group_first td { border-top-width: 2px; }
 #urdqahguiy .gt_row_group_first th { border-top-width: 2px; }
 #urdqahguiy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #urdqahguiy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #urdqahguiy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #urdqahguiy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #urdqahguiy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #urdqahguiy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #urdqahguiy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #urdqahguiy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #urdqahguiy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #urdqahguiy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #urdqahguiy .gt_left { text-align: left; }
 #urdqahguiy .gt_center { text-align: center; }
 #urdqahguiy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #urdqahguiy .gt_font_normal { font-weight: normal; }
 #urdqahguiy .gt_font_bold { font-weight: bold; }
 #urdqahguiy .gt_font_italic { font-style: italic; }
 #urdqahguiy .gt_super { font-size: 65%; }
 #urdqahguiy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #urdqahguiy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #urdqahguiy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #urdqahguiy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #urdqahguiy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #urdqahguiy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
