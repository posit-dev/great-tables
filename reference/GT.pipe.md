# GT.pipe()


Provide a structured way to chain a function for a GT object.


Usage

``` python
GT.pipe(
    func,
    *args,
    **kwargs,
)
```


This function accepts a function that receives a GT object along with optional positional and keyword arguments, returning a GT object. This allows users to easily integrate a function into the chained API offered by **Great Tables**.


## Parameters


`func: Callable[Concatenate[``"GT", P], `<span class="st">`"GT"``]`</span>  
A function that receives a GT object along with optional positional and keyword arguments, returning a GT object.

`*args: P.args`  
Optional positional arguments to be passed to the function.

`**kwargs: P.kwargs`  
Optional keyword arguments to be passed to the function.


## Returns


`gt`  
A GT object.


## Examples

Let's use the `name`, `land_area_km2`, and `density_2021` columns of the [towny](data.towny.md#great_tables.data.towny) dataset to create a table. First, we'll demonstrate using two consecutive calls to the `.tab_style()` method to highlight the maximum value of the `land_area_km2` column with `"lightgray"` and the maximum value of the `density_2021` column with `"lightblue"`.


``` python
import polars as pl
from great_tables import GT, loc, style
from great_tables.data import towny


towny_mini = pl.from_pandas(towny).head(10)

(
    GT(
        towny_mini[["name", "land_area_km2", "density_2021"]],
        rowname_col="name",
    )
    .tab_style(
        style=style.fill(color="lightgray"),
        locations=loc.body(
            columns="land_area_km2",
            rows=pl.col("land_area_km2").eq(pl.col("land_area_km2").max()),
        ),
    )
    .tab_style(
        style=style.fill(color="lightblue"),
        locations=loc.body(
            columns="density_2021",
            rows=pl.col("density_2021").eq(pl.col("density_2021").max()),
        ),
    )
)
```


<style>
#ojzppwsccr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ojzppwsccr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ojzppwsccr p { margin: 0; padding: 0; }
 #ojzppwsccr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ojzppwsccr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ojzppwsccr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ojzppwsccr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ojzppwsccr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ojzppwsccr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ojzppwsccr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ojzppwsccr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ojzppwsccr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ojzppwsccr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ojzppwsccr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ojzppwsccr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ojzppwsccr .gt_spanner_row { border-bottom-style: hidden; }
 #ojzppwsccr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ojzppwsccr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ojzppwsccr .gt_from_md> :first-child { margin-top: 0; }
 #ojzppwsccr .gt_from_md> :last-child { margin-bottom: 0; }
 #ojzppwsccr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ojzppwsccr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ojzppwsccr .gt_indent_1 { text-indent: 5px; }
 #ojzppwsccr .gt_indent_2 { text-indent: calc(5px * 2); }
 #ojzppwsccr .gt_indent_3 { text-indent: calc(5px * 3); }
 #ojzppwsccr .gt_indent_4 { text-indent: calc(5px * 4); }
 #ojzppwsccr .gt_indent_5 { text-indent: calc(5px * 5); }
 #ojzppwsccr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ojzppwsccr .gt_row_group_first td { border-top-width: 2px; }
 #ojzppwsccr .gt_row_group_first th { border-top-width: 2px; }
 #ojzppwsccr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ojzppwsccr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ojzppwsccr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ojzppwsccr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ojzppwsccr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ojzppwsccr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ojzppwsccr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ojzppwsccr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ojzppwsccr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ojzppwsccr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ojzppwsccr .gt_left { text-align: left; }
 #ojzppwsccr .gt_center { text-align: center; }
 #ojzppwsccr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ojzppwsccr .gt_font_normal { font-weight: normal; }
 #ojzppwsccr .gt_font_bold { font-weight: bold; }
 #ojzppwsccr .gt_font_italic { font-style: italic; }
 #ojzppwsccr .gt_super { font-size: 65%; }
 #ojzppwsccr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ojzppwsccr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ojzppwsccr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ojzppwsccr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ojzppwsccr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ojzppwsccr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                        | land_area_km2 | density_2021 |
|------------------------|---------------|--------------|
| Addington Highlands    | 1293.99       | 1.96         |
| Adelaide Metcalfe      | 331.11        | 9.09         |
| Adjala-Tosorontio      | 371.53        | 29.58        |
| Admaston/Bromley       | 519.59        | 5.76         |
| Ajax                   | 66.64         | 1900.75      |
| Alberton               | 116.6         | 8.18         |
| Alfred and Plantagenet | 391.79        | 25.39        |
| Algonquin Highlands    | 999.69        | 2.59         |
| Alnwick/Haldimand      | 398.25        | 18.76        |
| Amaranth               | 265.02        | 16.33        |


Next, we'll demonstrate how to achieve the same result using the `.pipe()` method to programmatically style each column.


``` python
columns = ["land_area_km2", "density_2021"]
colors = ["lightgray", "lightblue"]


def tbl_style(gtbl: GT, columns: list[str], colors: list[str]) -> GT:
    for column, color in zip(columns, colors):
        gtbl = gtbl.tab_style(
            style=style.fill(color=color),
            locations=loc.body(columns=column, rows=pl.col(column).eq(pl.col(column).max())),
        )
    return gtbl


(
    GT(
        towny_mini[["name", "land_area_km2", "density_2021"]],
        rowname_col="name",
    ).pipe(tbl_style, columns, colors)
)
```


<style>
#mnbcclfktz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mnbcclfktz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mnbcclfktz p { margin: 0; padding: 0; }
 #mnbcclfktz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mnbcclfktz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mnbcclfktz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mnbcclfktz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mnbcclfktz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mnbcclfktz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mnbcclfktz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mnbcclfktz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mnbcclfktz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mnbcclfktz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mnbcclfktz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mnbcclfktz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mnbcclfktz .gt_spanner_row { border-bottom-style: hidden; }
 #mnbcclfktz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mnbcclfktz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mnbcclfktz .gt_from_md> :first-child { margin-top: 0; }
 #mnbcclfktz .gt_from_md> :last-child { margin-bottom: 0; }
 #mnbcclfktz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mnbcclfktz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mnbcclfktz .gt_indent_1 { text-indent: 5px; }
 #mnbcclfktz .gt_indent_2 { text-indent: calc(5px * 2); }
 #mnbcclfktz .gt_indent_3 { text-indent: calc(5px * 3); }
 #mnbcclfktz .gt_indent_4 { text-indent: calc(5px * 4); }
 #mnbcclfktz .gt_indent_5 { text-indent: calc(5px * 5); }
 #mnbcclfktz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mnbcclfktz .gt_row_group_first td { border-top-width: 2px; }
 #mnbcclfktz .gt_row_group_first th { border-top-width: 2px; }
 #mnbcclfktz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mnbcclfktz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mnbcclfktz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mnbcclfktz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mnbcclfktz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mnbcclfktz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mnbcclfktz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mnbcclfktz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mnbcclfktz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mnbcclfktz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mnbcclfktz .gt_left { text-align: left; }
 #mnbcclfktz .gt_center { text-align: center; }
 #mnbcclfktz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mnbcclfktz .gt_font_normal { font-weight: normal; }
 #mnbcclfktz .gt_font_bold { font-weight: bold; }
 #mnbcclfktz .gt_font_italic { font-style: italic; }
 #mnbcclfktz .gt_super { font-size: 65%; }
 #mnbcclfktz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mnbcclfktz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mnbcclfktz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mnbcclfktz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mnbcclfktz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mnbcclfktz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                        | land_area_km2 | density_2021 |
|------------------------|---------------|--------------|
| Addington Highlands    | 1293.99       | 1.96         |
| Adelaide Metcalfe      | 331.11        | 9.09         |
| Adjala-Tosorontio      | 371.53        | 29.58        |
| Admaston/Bromley       | 519.59        | 5.76         |
| Ajax                   | 66.64         | 1900.75      |
| Alberton               | 116.6         | 8.18         |
| Alfred and Plantagenet | 391.79        | 25.39        |
| Algonquin Highlands    | 999.69        | 2.59         |
| Alnwick/Haldimand      | 398.25        | 18.76        |
| Amaranth               | 265.02        | 16.33        |
