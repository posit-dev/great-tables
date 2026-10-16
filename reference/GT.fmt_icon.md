# GT.fmt_icon()


Use icons within a table's body cells.


Usage

``` python
GT.fmt_icon(
    columns=None,
    rows=None,
    height=None,
    sep=" ",
    stroke_color=None,
    stroke_width=None,
    stroke_alpha=None,
    fill_color=None,
    fill_alpha=None,
    margin_left=None,
    margin_right=None,
)
```


We can draw from a library of thousands of icons and selectively insert them into a table. The [fmt_icon()](GT.fmt_icon.md#great_tables.GT.fmt_icon) method makes this possible by mapping input cell labels to an icon name. We are exclusively using Font Awesome icons here so the reference is the short icon name. Multiple icons can be included per cell by separating icon names with commas (e.g., `"hard-drive,clock"`). The `sep=` argument allows for a common separator to be applied between icons.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`height: str | None = None`  
The absolute height of the icon in the table cell. By default, this is set to "1em".

`sep: str = ``" "`  
In the output of icons within a body cell, `sep=` provides the separator between each icon.

`stroke_color: str | None = None`  
The icon stroke is essentially the outline of the icon. The color of the stroke can be modified by applying a single color here. If not provided then the default value of `"currentColor"` is applied so that the stroke color matches that of the parent HTML element's color attribute.

`stroke_width: str | int | None = None`  
The `stroke_width=` option allows for setting the color of the icon outline stroke. By default, the stroke width is very small at "1px" so a size adjustment here can sometimes be useful. If an integer value is provided then it is assumed to be in pixels.

`stroke_alpha: float | None = None`  
The level of transparency for the icon stroke can be controlled with a decimal value between `0` and `1`.

`fill_color: str | dict[str, str] | None = None`  
The fill color of the icon can be set with `fill_color=`; providing a single color here will change the color of the fill but not of the icon's 'stroke' or outline (use `stroke_color=` to modify that). A dictionary comprising the icon names with corresponding fill colors can alternatively be used here (e.g., `{"circle-check" = "green", "circle-xmark" = "red"}`. If nothing is provided then the default value of `"currentColor"` is applied so that the fill matches the color of the parent HTML element's color attribute.

`fill_alpha: float | None = None`  
The level of transparency for the icon fill can be controlled with a decimal value between `0` and `1`.

`margin_left: str | None = None`  
The length value for the margin that's to the left of the icon. By default, `"auto"` is used for this but if space is needed on the left-hand side then a length of `"0.2em"` is recommended as a starting point.

`margin_right: str | None = None`  
The length value for the margin right of the icon. By default, `"auto"` is used but if space is needed on the right-hand side then a length of `"0.2em"` is recommended as a starting point.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

For this first example of generating icons with [fmt_icon()](GT.fmt_icon.md#great_tables.GT.fmt_icon), let's make a simple DataFrame that has two columns of Font Awesome icon names. We separate multiple icons per cell with commas. By default, the icons are 1 em in height; we're going to make the icons slightly larger here (so we can see the fine details of them) by setting height = "4em".


``` python
import pandas as pd
from great_tables import GT

animals_foods_df = pd.DataFrame(
    {
        "animals": ["hippo", "fish,spider", "mosquito,locust,frog", "dog,cat", "kiwi-bird"],
        "foods": ["bowl-rice", "egg,pizza-slice", "burger,lemon,cheese", "carrot,hotdog", "bacon"],
    }
)

(
    GT(animals_foods_df)
    .fmt_icon(
        columns=["animals", "foods"],
        height="4em"
    )
    .cols_align(
        align="center",
        columns=["animals", "foods"]
    )
)
```


<style>
#ggjyprbqxp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ggjyprbqxp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ggjyprbqxp p { margin: 0; padding: 0; }
 #ggjyprbqxp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ggjyprbqxp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ggjyprbqxp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ggjyprbqxp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ggjyprbqxp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ggjyprbqxp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ggjyprbqxp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ggjyprbqxp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ggjyprbqxp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ggjyprbqxp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ggjyprbqxp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ggjyprbqxp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ggjyprbqxp .gt_spanner_row { border-bottom-style: hidden; }
 #ggjyprbqxp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ggjyprbqxp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ggjyprbqxp .gt_from_md> :first-child { margin-top: 0; }
 #ggjyprbqxp .gt_from_md> :last-child { margin-bottom: 0; }
 #ggjyprbqxp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ggjyprbqxp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ggjyprbqxp .gt_indent_1 { text-indent: 5px; }
 #ggjyprbqxp .gt_indent_2 { text-indent: calc(5px * 2); }
 #ggjyprbqxp .gt_indent_3 { text-indent: calc(5px * 3); }
 #ggjyprbqxp .gt_indent_4 { text-indent: calc(5px * 4); }
 #ggjyprbqxp .gt_indent_5 { text-indent: calc(5px * 5); }
 #ggjyprbqxp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ggjyprbqxp .gt_row_group_first td { border-top-width: 2px; }
 #ggjyprbqxp .gt_row_group_first th { border-top-width: 2px; }
 #ggjyprbqxp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ggjyprbqxp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ggjyprbqxp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ggjyprbqxp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ggjyprbqxp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ggjyprbqxp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ggjyprbqxp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ggjyprbqxp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ggjyprbqxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ggjyprbqxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ggjyprbqxp .gt_left { text-align: left; }
 #ggjyprbqxp .gt_center { text-align: center; }
 #ggjyprbqxp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ggjyprbqxp .gt_font_normal { font-weight: normal; }
 #ggjyprbqxp .gt_font_bold { font-weight: bold; }
 #ggjyprbqxp .gt_font_italic { font-style: italic; }
 #ggjyprbqxp .gt_super { font-size: 65%; }
 #ggjyprbqxp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ggjyprbqxp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ggjyprbqxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ggjyprbqxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ggjyprbqxp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ggjyprbqxp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| animals | foods |
|----|----|
| <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNjQwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjUuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik00MDcgNDdjOS40LTkuNCAyNC42LTkuNCAzMy45IDBsMTcuMiAxNy4yYzEuOS0uMSAzLjktLjIgNS44LS4yaDMyYzExLjIgMCAyMS45IDIuMyAzMS42IDYuNUw1NDMgNTVjOS40LTkuNCAyNC42LTkuNCAzMy45IDBzOS40IDI0LjYgMCAzMy45TDU2NCAxMDEuOWM3LjYgMTIuMiAxMiAyNi43IDEyIDQyLjFjMCAxMC4yIDcuNCAxOC44IDE2LjcgMjNjMjcuOSAxMi41IDQ3LjMgNDAuNSA0Ny4zIDczYzAgMjYuMi0xMi42IDQ5LjQtMzIgNjR2MzJjMCA4LjgtNy4yIDE2LTE2IDE2SDU2MGMtOC44IDAtMTYtNy4yLTE2LTE2VjMyMEg0ODB2MTZjMCA4LjgtNy4yIDE2LTE2IDE2SDQzMmMtOC44IDAtMTYtNy4yLTE2LTE2VjMxOC40Yy0xMS44LTIuNC0yMi43LTcuNC0zMi0xNC40Yy0xLjUtMS4xLTIuOS0yLjMtNC4zLTMuNWMtMTctMTQuNy0yNy43LTM2LjQtMjcuNy02MC41YzAtOC44LTcuMi0xNi0xNi0xNnMtMTYgNy4yLTE2IDE2YzAgNDQuNyAyNi4yIDgzLjIgNjQgMTAxLjJWMzUyYzAgMTcuNyAxNC4zIDMyIDMyIDMyaDMydjY0YzAgMTcuNy0xNC4zIDMyLTMyIDMySDM1MmMtMTcuNyAwLTMyLTE0LjMtMzItMzJWMzcyYy0xOS44IDcuNy00MS40IDEyLTY0IDEycy00NC4yLTQuMy02NC0xMnY3NmMwIDE3LjctMTQuMyAzMi0zMiAzMkg5NmMtMTcuNyAwLTMyLTE0LjMtMzItMzJWMzI5LjFMNDUuOSAzNjkuN2MtNS40IDEyLjEtMTkuNiAxNy42LTMxLjcgMTIuMlMtMy4zIDM2Mi40IDIuMSAzNTAuM0wyNCAzMDAuOWM1LjMtMTEuOSA4LTI0LjcgOC0zNy43QzMyIDE1NS43IDExNy4yIDY4IDIyMy44IDY0LjFsLjItLjFoNy4ySDI1NmgzMmM0MS43IDAgODMuNCAxMi4xIDExNy4yIDI1LjdjMS43LTEuOCAzLjUtMy42IDUuMy01LjJMNDA3IDgxYy05LjQtOS40LTkuNC0yNC42IDAtMzMuOXptNzMgMTg1YzAtMTMuMy0xMC43LTI0LTI0LTI0cy0yNCAxMC43LTI0IDI0czEwLjcgMjQgMjQgMjRzMjQtMTAuNyAyNC0yNHptODggMjRjMTMuMyAwIDI0LTEwLjcgMjQtMjRzLTEwLjctMjQtMjQtMjRzLTI0IDEwLjctMjQgMjRzMTAuNyAyNCAyNCAyNHpNNDgwIDE0NGMwLTguOC03LjItMTYtMTYtMTZzLTE2IDcuMi0xNiAxNnM3LjIgMTYgMTYgMTZzMTYtNy4yIDE2LTE2em00OCAxNmM4LjggMCAxNi03LjIgMTYtMTZzLTcuMi0xNi0xNi0xNnMtMTYgNy4yLTE2IDE2czcuMiAxNiAxNiAxNnoiIC8+PC9zdmc+" class="fa" /></span> | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0xNzYgNTZjMC0xMy4zIDEwLjctMjQgMjQtMjRoMTZjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMjAwYy0xMy4zIDAtMjQtMTAuNy0yNC0yNHptMjQgNDhoMTZjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMjAwYy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0ek01NiAxNzZINzJjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRINTZjLTEzLjMgMC0yNC0xMC43LTI0LTI0czEwLjctMjQgMjQtMjR6TTAgMjgzLjRDMCAyNjguMyAxMi4zIDI1NiAyNy40IDI1Nkg0ODQuNmMxNS4xIDAgMjcuNCAxMi4zIDI3LjQgMjcuNGMwIDcwLjUtNDQuNCAxMzAuNy0xMDYuNyAxNTQuMUw0MDMuNSA0NTJjLTIgMTYtMTUuNiAyOC0zMS44IDI4SDE0MC4yYy0xNi4xIDAtMjkuOC0xMi0zMS44LTI4bC0xLjgtMTQuNEM0NC40IDQxNC4xIDAgMzUzLjkgMCAyODMuNHpNMjI0IDIwMGMwLTEzLjMgMTAuNy0yNCAyNC0yNGgxNmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgyNDhjLTEzLjMgMC0yNC0xMC43LTI0LTI0em0tOTYgMGMwLTEzLjMgMTAuNy0yNCAyNC0yNGgxNmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgxNTJjLTEzLjMgMC0yNC0xMC43LTI0LTI0em0tMjQtOTZoMTZjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMTA0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0em0yMTYgOTZjMC0xMy4zIDEwLjctMjQgMjQtMjRoMTZjMTMuMyAwIDI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjRIMzQ0Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHptLTI0LTk2aDE2YzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDI5NmMtMTMuMyAwLTI0LTEwLjctMjQtMjRzMTAuNy0yNCAyNC0yNHptMTIwIDk2YzAtMTMuMyAxMC43LTI0IDI0LTI0aDE2YzEzLjMgMCAyNCAxMC43IDI0IDI0cy0xMC43IDI0LTI0IDI0SDQ0MGMtMTMuMyAwLTI0LTEwLjctMjQtMjR6bS0yNC05NmgxNmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgzOTJjLTEzLjMgMC0yNC0xMC43LTI0LTI0czEwLjctMjQgMjQtMjR6TTI5NiAzMmgxNmMxMy4zIDAgMjQgMTAuNyAyNCAyNHMtMTAuNyAyNC0yNCAyNEgyOTZjLTEzLjMgMC0yNC0xMC43LTI0LTI0czEwLjctMjQgMjQtMjR6IiAvPjwvc3ZnPg==" class="fa" /></span> |
| <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuNWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0xODAuNSAxNDEuNUMyMTkuNyAxMDguNSAyNzIuNiA4MCAzMzYgODBzMTE2LjMgMjguNSAxNTUuNSA2MS41YzM5LjEgMzMgNjYuOSA3Mi40IDgxIDk5LjhjNC43IDkuMiA0LjcgMjAuMSAwIDI5LjNjLTE0LjEgMjcuNC00MS45IDY2LjgtODEgOTkuOEM0NTIuMyA0MDMuNSAzOTkuNCA0MzIgMzM2IDQzMnMtMTE2LjMtMjguNS0xNTUuNS02MS41Yy0xNi4yLTEzLjctMzAuNS0yOC41LTQyLjctNDMuMUw0OC4xIDM3OS42Yy0xMi41IDcuMy0yOC40IDUuMy0zOC43LTQuOVMtMyAzNDguNyA0LjIgMzM2LjFMNTAgMjU2IDQuMiAxNzUuOWMtNy4yLTEyLjYtNS0yOC40IDUuMy0zOC42czI2LjEtMTIuMiAzOC43LTQuOWw4OS43IDUyLjNjMTIuMi0xNC42IDI2LjUtMjkuNCA0Mi43LTQzLjF6TTQ0OCAyNTZjMC0xNy43LTE0LjMtMzItMzItMzJzLTMyIDE0LjMtMzIgMzJzMTQuMyAzMiAzMiAzMnMzMi0xNC4zIDMyLTMyeiIgLz48L3N2Zz4=" class="fa" /> <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuNWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0xOTAuNCAzMi42YzQuOC0xMi40LTEuNC0yNi4zLTEzLjgtMzFzLTI2LjMgMS40LTMxIDEzLjhMMTEzLjEgMTAwYy03LjkgMjAuNy0zIDQ0LjEgMTIuNyA1OS43bDU3LjQgNTcuNC04MC40LTI2LjhjLTIuNC0uOC00LjMtMi43LTUuMS01LjFMNzguOCAxMjguNEM3NC42IDExNS44IDYxIDEwOSA0OC40IDExMy4yUzI5IDEzMSAzMy4yIDE0My42bDE4LjkgNTYuOGM1LjYgMTYuNyAxOC43IDI5LjggMzUuNCAzNS40TDE0OC4xIDI1NiA4Ny42IDI3Ni4yYy0xNi43IDUuNi0yOS44IDE4LjctMzUuNCAzNS40TDMzLjIgMzY4LjRDMjkgMzgxIDM1LjggMzk0LjYgNDguNCAzOTguOHMyNi4yLTIuNiAzMC40LTE1LjJsMTguOS01Ni44Yy44LTIuNCAyLjctNC4zIDUuMS01LjFsODAuNC0yNi44LTU3LjQgNTcuNGMtMTUuNiAxNS42LTIwLjYgMzktMTIuNyA1OS43bDMyLjUgODQuNmM0LjggMTIuNCAxOC42IDE4LjUgMzEgMTMuOHMxOC41LTE4LjYgMTMuOC0zMWwtMzIuNS04NC42Yy0xLjEtMy0uNC02LjMgMS44LTguNUwxOTIgMzUzLjljMSA1Mi4xIDQzLjYgOTQuMSA5NiA5NC4xczk1LTQxLjkgOTYtOTQuMWwzMi4zIDMyLjNjMi4yIDIuMiAyLjkgNS42IDEuOCA4LjVsLTMyLjUgODQuNmMtNC44IDEyLjQgMS40IDI2LjMgMTMuOCAzMXMyNi4zLTEuNCAzMS0xMy44TDQ2Mi45IDQxMmM3LjktMjAuNyAzLTQ0LjEtMTIuNy01OS43bC01Ny40LTU3LjQgODAuNCAyNi44YzIuNCAuOCA0LjMgMi43IDUuMSA1LjFsMTguOSA1Ni44YzQuMiAxMi42IDE3LjggMTkuNCAzMC40IDE1LjJzMTkuNC0xNy44IDE1LjItMzAuNGwtMTguOS01Ni44Yy01LjYtMTYuNy0xOC43LTI5LjgtMzUuNC0zNS40TDQyNy45IDI1Nmw2MC41LTIwLjJjMTYuNy01LjYgMjkuOC0xOC43IDM1LjQtMzUuNGwxOC45LTU2LjhjNC4yLTEyLjYtMi42LTI2LjItMTUuMi0zMC40cy0yNi4yIDIuNi0zMC40IDE1LjJsLTE4LjkgNTYuOGMtLjggMi40LTIuNyA0LjMtNS4xIDUuMWwtODAuNCAyNi44IDU3LjQtNTcuNGMxNS42LTE1LjYgMjAuNi0zOSAxMi43LTU5LjdMNDMwLjQgMTUuNEM0MjUuNiAzIDQxMS44LTMuMiAzOTkuNCAxLjZzLTE4LjUgMTguNi0xMy44IDMxbDMyLjUgODQuNmMxLjEgMyAuNCA2LjMtMS44IDguNUwzNjggMTc0LjFWMTYwYzAtMzEuOC0xOC42LTU5LjMtNDUuNS03Mi4yYy05LjEtNC40LTE4LjUgMy4zLTE4LjUgMTMuNFYxMTJjMCA4LjgtNy4yIDE2LTE2IDE2cy0xNi03LjItMTYtMTZWMTAxLjJjMC0xMC4xLTkuNC0xNy43LTE4LjUtMTMuNEMyMjYuNiAxMDAuNyAyMDggMTI4LjIgMjA4IDE2MHYxNC4xbC00OC4zLTQ4LjNjLTIuMi0yLjItMi45LTUuNi0xLjgtOC41bDMyLjUtODQuNnoiIC8+PC9zdmc+" class="fa" /></span> | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjMuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0xOTIgNDk2Qzg2IDQ5NiAwIDQxMCAwIDMwNEMwIDE5MiA5NiAxNiAxOTIgMTZzMTkyIDE3NiAxOTIgMjg4YzAgMTA2LTg2IDE5Mi0xOTIgMTkyek0xNTYuNSAxMzhsMCAwIDAgMCAwIDBjNS41LTYuOSA0LjQtMTctMi41LTIyLjVzLTE3LTQuNC0yMi41IDIuNUwxNDQgMTI4Yy0xMi41LTEwLTEyLjUtMTAtMTIuNS0xMGwwIDAgMCAwLS4xIC4xLS4yIC4yLS42IC44Yy0uNSAuNy0xLjMgMS43LTIuMiAzYy0xLjkgMi42LTQuNSA2LjMtNy43IDExYy02LjMgOS40LTE0LjYgMjMtMjMgMzkuN0M4MS4xIDIwNi4xIDY0IDI1Mi42IDY0IDMwNGMwIDguOCA3LjIgMTYgMTYgMTZzMTYtNy4yIDE2LTE2YzAtNDQuNiAxNC45LTg2LjEgMzAuMy0xMTYuOGM3LjYtMTUuMyAxNS4zLTI3LjcgMjEtMzYuM2MyLjgtNC4zIDUuMi03LjYgNi44LTkuOGMuOC0xLjEgMS40LTEuOSAxLjgtMi40bC40LS42IC4xLS4xIDAgMHoiIC8+PC9zdmc+" class="fa" /> <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0xNjkuNyAuOWMtMjIuOC0xLjYtNDEuOSAxNC00Ny41IDM0LjdMMTEwLjQgODBjLjUgMCAxLjEgMCAxLjYgMGMxNzYuNyAwIDMyMCAxNDMuMyAzMjAgMzIwYzAgLjUgMCAxLjEgMCAxLjZsNDQuNC0xMS44YzIwLjgtNS41IDM2LjMtMjQuNyAzNC43LTQ3LjVDNDk4LjUgMTU5LjUgMzUyLjUgMTMuNSAxNjkuNyAuOXpNMzk5LjggNDEwLjJjLjEtMy40IC4yLTYuOCAuMi0xMC4yYzAtMTU5LjEtMTI4LjktMjg4LTI4OC0yODhjLTMuNCAwLTYuOCAuMS0xMC4yIC4yTC41IDQ5MS45Yy0xLjUgNS41IC4xIDExLjQgNC4xIDE1LjRzOS45IDUuNiAxNS40IDQuMUwzOTkuOCA0MTAuMnpNMTc2IDI3MmMtMTcuNyAwLTMyLTE0LjMtMzItMzJzMTQuMy0zMiAzMi0zMnMzMiAxNC4zIDMyIDMycy0xNC4zIDMyLTMyIDMyem0xMjggNjRjMCAxNy43LTE0LjMgMzItMzIgMzJzLTMyLTE0LjMtMzItMzJzMTQuMy0zMiAzMi0zMnMzMiAxNC4zIDMyIDMyek0xNjAgMzg0YzAgMTcuNy0xNC4zIDMyLTMyIDMycy0zMi0xNC4zLTMyLTMyczE0LjMtMzIgMzItMzJzMzIgMTQuMyAzMiAzMnoiIC8+PC9zdmc+" class="fa" /></span> |
| <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNjQwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjUuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik00NjMuNyA1MDUuOWM5LjgtOC45IDEwLjctMjQuMyAyLjEtMzQuM2wtNDIuMS00OSAwLTU0LjdjMC01LjUtMS44LTEwLjgtNS4xLTE1LjFMMzUyIDI2Ni4zbDAtLjNMNDg1LjQgMzg3LjhDNTQyLjQgNDQ3LjYgNjQwIDQwNS4yIDY0MCAzMjAuNmMwLTQ3LjktMzQtODguMy03OS40LTk0LjJsLTE1My0yMy45IDQwLjgtNDAuOWM3LjgtNy44IDkuNC0yMC4xIDMuOS0yOS44TDQyOC41IDkwLjFsMzguMi01MC45YzgtMTAuNiA2LjEtMjUuOS00LjMtMzQuMXMtMjUuMi02LjMtMzMuMiA0LjRsLTQ4IDYzLjljLTUuOSA3LjktNi42IDE4LjYtMS43IDI3LjJMNDAyLjIgMTQwIDM1MiAxOTAuM2wwLTM4LjJjMC0xNC45LTEwLjItMjcuNC0yNC0zMWwwLTU3LjJjMC00LjQtMy42LTgtOC04cy04IDMuNi04IDhsMCA1Ny4yYy0xMy44IDMuNi0yNCAxNi4xLTI0IDMxbDAgMzguMUwyMzcuOCAxNDBsMjIuNi0zOS41YzQuOS04LjYgNC4yLTE5LjMtMS43LTI3LjJsLTQ4LTYzLjljLTgtMTAuNi0yMi44LTEyLjYtMzMuMi00LjRzLTEyLjIgMjMuNS00LjMgMzQuMWwzOC4yIDUwLjktMjMuOSA0MS43Yy01LjUgOS43LTMuOSAyMiAzLjkgMjkuOGw0MC44IDQwLjktMTUzIDIzLjlDMzQgMjMyLjMgMCAyNzIuNyAwIDMyMC42YzAgODQuNiA5Ny42IDEyNyAxNTQuNiA2Ny4xTDI4OCAyNjZsMCAuMy02Ni41IDg2LjRjLTMuMyA0LjMtNS4xIDkuNi01LjEgMTUuMWwwIDU0LjctNDIuMSA0OWMtOC42IDEwLjEtNy43IDI1LjUgMi4xIDM0LjNzMjQuNyA3LjkgMzMuNC0yLjFsNDgtNTUuOWMzLjgtNC40IDUuOS0xMC4yIDUuOS0xNi4xbDAtNTUuNEwyODggMzQ0LjdsMCA2My4xYzAgMTcuNyAxNC4zIDMyIDMyIDMyczMyLTE0LjMgMzItMzJsMC02My4xIDI0LjMgMzEuNiAwIDU1LjRjMCA1LjkgMi4xIDExLjcgNS45IDE2LjFsNDggNTUuOWM4LjYgMTAuMSAyMy42IDExIDMzLjQgMi4xeiIgLz48L3N2Zz4=" class="fa" /> <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNjQwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjUuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0zNDQgMzJjLTEzLjMgMC0yNCAxMC43LTI0IDI0czEwLjcgMjQgMjQgMjRoMTZjOTguNyAwIDE4MC42IDcxLjQgMTk3IDE2NS40Yy05LTMuNS0xOC44LTUuNC0yOS01LjRINDYzLjhsLTQxLjgtOTcuNWMtMy40LTcuOS0xMC44LTEzLjQtMTkuMy0xNC40cy0xNyAyLjctMjIuMSA5LjZsLTQwLjkgNTUuNS0yMS43LTUwLjdjLTMuMy03LjgtMTAuNS0xMy4yLTE4LjktMTQuM3MtMTYuNyAyLjMtMjIgOC45bC0yNDAgMzA0Yy04LjIgMTAuNC02LjQgMjUuNSA0IDMzLjdzMjUuNSA2LjQgMzMuNy00bDc5LjQtMTAwLjUgNDMgMTYuNC00MC41IDU1Yy03LjkgMTAuNy01LjYgMjUuNyA1LjEgMzMuNnMyNS43IDUuNiAzMy42LTUuMUwyNDcuMSA0MDBoNzQuNWwtMjkuMyA0Mi4zYy03LjUgMTAuOS00LjggMjUuOCA2LjEgMzMuNHMyNS44IDQuOCAzMy40LTYuMUwzODAgNDAwaDgwLjRsMzguOCA2Ny45YzYuNiAxMS41IDIxLjIgMTUuNSAzMi43IDguOXMxNS41LTIxLjIgOC45LTMyLjdMNTE1LjYgNDAwSDUyOGM0NC4xIDAgNzkuOC0zNS43IDgwLTc5LjdjMC0uMSAwLS4yIDAtLjNWMjgwQzYwOCAxNDMgNDk3IDMyIDM2MCAzMkgzNDR6bTUwLjUgMTY4bDE3LjEgNDBIMzY1bDI5LjUtNDB6bS04Ny43IDM4LjFsLTEuNCAxLjlIMjU3LjFsMzIuNy00MS41IDE2LjkgMzkuNXpNMTIwLjggMjQwQzg5LjQgMjQwIDY0IDI2NS40IDY0IDI5Ni44YzAgMTUuNSA2LjMgMzAgMTYuOSA0MC40TDE1OC43IDI0MEgxMjAuOHpNNTI4IDMyMGMtOC44IDAtMTYtNy4yLTE2LTE2czcuMi0xNiAxNi0xNnMxNiA3LjIgMTYgMTZzLTcuMiAxNi0xNiAxNnoiIC8+PC9zdmc+" class="fa" /> <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuNWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0zNjggMzJjNDEuNyAwIDc1LjkgMzEuOCA3OS43IDcyLjVsODUuNiAyNi4zYzI1LjQgNy44IDQyLjggMzEuMyA0Mi44IDU3LjljMCAyMS44LTExLjcgNDEuOS0zMC43IDUyLjdMNDAwLjggMzIzLjUgNDkzLjMgNDE2SDU0NGMxNy43IDAgMzIgMTQuMyAzMiAzMnMtMTQuMyAzMi0zMiAzMkg0ODBjLTguNSAwLTE2LjYtMy40LTIyLjYtOS40TDM0Ni45IDM2MC4yYzExLjctMzYgMy4yLTc3LjEtMjUuNC0xMDUuN2MtNDAuNi00MC42LTEwNi4zLTQwLjYtMTQ2LjktLjFMMTAxIDMyNC40Yy02LjQgNi4xLTYuNyAxNi4yLS42IDIyLjZzMTYuMiA2LjYgMjIuNiAuNmw3My44LTcwLjIgLjEtLjEgLjEtLjFjMy41LTMuNSA3LjMtNi42IDExLjMtOS4yYzI3LjktMTguNSA2NS45LTE1LjQgOTAuNSA5LjJjMjQuNyAyNC43IDI3LjcgNjIuOSA5IDkwLjljLTIuNiAzLjgtNS42IDcuNS05IDEwLjlMMjYxLjggNDE2SDM1MmMxNy43IDAgMzIgMTQuMyAzMiAzMnMtMTQuMyAzMi0zMiAzMkg2NGMtMzUuMyAwLTY0LTI4LjctNjQtNjRDMCAyNDkuNiAxMjcgMTEyLjkgMjg5LjMgOTcuNUMyOTYuMiA2MC4yIDMyOC44IDMyIDM2OCAzMnptMCAxMDRjMTMuMyAwIDI0LTEwLjcgMjQtMjRzLTEwLjctMjQtMjQtMjRzLTI0IDEwLjctMjQgMjRzMTAuNyAyNCAyNCAyNHoiIC8+PC9zdmc+" class="fa" /></span> | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik02MS4xIDIyNEM0NSAyMjQgMzIgMjExIDMyIDE5NC45YzAtMS45IC4yLTMuNyAuNi01LjZDMzcuOSAxNjguMyA3OC44IDMyIDI1NiAzMnMyMTguMSAxMzYuMyAyMjMuNCAxNTcuM2MuNSAxLjkgLjYgMy43IC42IDUuNmMwIDE2LjEtMTMgMjkuMS0yOS4xIDI5LjFINjEuMXpNMTQ0IDEyOGMwLTguOC03LjItMTYtMTYtMTZzLTE2IDcuMi0xNiAxNnM3LjIgMTYgMTYgMTZzMTYtNy4yIDE2LTE2em0yNDAgMTZjOC44IDAgMTYtNy4yIDE2LTE2cy03LjItMTYtMTYtMTZzLTE2IDcuMi0xNiAxNnM3LjIgMTYgMTYgMTZ6TTI3MiA5NmMwLTguOC03LjItMTYtMTYtMTZzLTE2IDcuMi0xNiAxNnM3LjIgMTYgMTYgMTZzMTYtNy4yIDE2LTE2ek0xNiAzMDRjMC0yNi41IDIxLjUtNDggNDgtNDhINDQ4YzI2LjUgMCA0OCAyMS41IDQ4IDQ4cy0yMS41IDQ4LTQ4IDQ4SDY0Yy0yNi41IDAtNDgtMjEuNS00OC00OHptMTYgOTZjMC04LjggNy4yLTE2IDE2LTE2SDQ2NGM4LjggMCAxNiA3LjIgMTYgMTZ2MTZjMCAzNS4zLTI4LjcgNjQtNjQgNjRIOTZjLTM1LjMgMC02NC0yOC43LTY0LTY0VjQwMHoiIC8+PC9zdmc+" class="fa" /> <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjMuNWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik00NDggOTZjMC0zNS4zLTI4LjctNjQtNjQtNjRjLTYuNiAwLTEzIDEtMTkgMi45Yy0yMi41IDctNDguMSAxNC45LTcxIDljLTc1LjItMTkuMS0xNTYuNCAxMS0yMTMuNyA2OC4zUy03LjIgMjUwLjggMTEuOSAzMjZjNS44IDIyLjktMiA0OC40LTkgNzFDMSA0MDMgMCA0MDkuNCAwIDQxNmMwIDM1LjMgMjguNyA2NCA2NCA2NGM2LjYgMCAxMy0xIDE5LjEtMi45YzIyLjUtNyA0OC4xLTE0LjkgNzEtOWM3NS4yIDE5LjEgMTU2LjQtMTEgMjEzLjctNjguM3M4Ny41LTEzOC41IDY4LjMtMjEzLjdjLTUuOC0yMi45IDItNDguNCA5LTcxYzEuOS02IDIuOS0xMi40IDIuOS0xOS4xek0yMTIuNSAxMjcuNGMtNTQuNiAxNi0xMDEuMSA2Mi41LTExNy4xIDExNy4xQzkyLjkgMjUzIDg0IDI1Ny44IDc1LjUgMjU1LjRTNjIuMiAyNDQgNjQuNiAyMzUuNWMxOS4xLTY1LjEgNzMuNy0xMTkuOCAxMzguOS0xMzguOWM4LjUtMi41IDE3LjQgMi40IDE5LjkgMTAuOXMtMi40IDE3LjQtMTAuOSAxOS45eiIgLz48L3N2Zz4=" class="fa" /> <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik01MTIgMjQwLjJWMjU2SDBjMC0yMCAxMC0zOC43IDI2LjYtNDkuOEwyNzQuOSA0MC43YzguNi01LjcgMTguNi04LjcgMjguOS04LjdDNDE4LjggMzIgNTEyIDEyNS4yIDUxMiAyNDAuMnptMCA0Ny44VjQxNmMwIDM1LjMtMjguNyA2NC02NCA2NEg2NGMtMzUuMyAwLTY0LTI4LjctNjQtNjRWMjg4SDUxMnoiIC8+PC9zdmc+" class="fa" /></span> |
| <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuNWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0zMDkuNiAxNTguNUwzMzIuNyAxOS44QzMzNC42IDguNCAzNDQuNSAwIDM1Ni4xIDBjNy41IDAgMTQuNSAzLjUgMTkgOS41TDM5MiAzMmg1Mi4xYzEyLjcgMCAyNC45IDUuMSAzMy45IDE0LjFMNDk2IDY0aDU2YzEzLjMgMCAyNCAxMC43IDI0IDI0djI0YzAgNDQuMi0zNS44IDgwLTgwIDgwSDQ2NCA0NDggNDI2LjdsLTUuMSAzMC41LTExMi02NHpNNDE2IDI1Ni4xTDQxNiA0ODBjMCAxNy43LTE0LjMgMzItMzIgMzJIMzUyYy0xNy43IDAtMzItMTQuMy0zMi0zMlYzNjQuOGMtMjQgMTIuMy01MS4yIDE5LjItODAgMTkuMnMtNTYtNi45LTgwLTE5LjJWNDgwYzAgMTcuNy0xNC4zIDMyLTMyIDMySDk2Yy0xNy43IDAtMzItMTQuMy0zMi0zMlYyNDkuOGMtMjguOC0xMC45LTUxLjQtMzUuMy01OS4yLTY2LjVMMSAxNjcuOGMtNC4zLTE3LjEgNi4xLTM0LjUgMjMuMy0zOC44czM0LjUgNi4xIDM4LjggMjMuM2wzLjkgMTUuNUM3MC41IDE4MiA4My4zIDE5MiA5OCAxOTJoMzAgMTZIMzAzLjhMNDE2IDI1Ni4xek00NjQgODBjMC04LjgtNy4yLTE2LTE2LTE2cy0xNiA3LjItMTYgMTZzNy4yIDE2IDE2IDE2czE2LTcuMiAxNi0xNnoiIC8+PC9zdmc+" class="fa" /> <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yODggMTkyaDE3LjFjMjIuMSAzOC4zIDYzLjUgNjQgMTEwLjkgNjRjMTEgMCAyMS44LTEuNCAzMi00djQgMzJWNDgwYzAgMTcuNy0xNC4zIDMyLTMyIDMycy0zMi0xNC4zLTMyLTMyVjMzOS4yTDI0OCA0NDhoNTZjMTcuNyAwIDMyIDE0LjMgMzIgMzJzLTE0LjMgMzItMzIgMzJIMTYwYy01MyAwLTk2LTQzLTk2LTk2VjE5Mi41YzAtMTYuMS0xMi0yOS44LTI4LTMxLjhsLTcuOS0xQzEwLjUgMTU3LjYtMS45IDE0MS42IC4yIDEyNHMxOC4yLTMwIDM1LjctMjcuOGw3LjkgMWM0OCA2IDg0LjEgNDYuOCA4NC4xIDk1LjN2ODUuM2MzNC40LTUxLjcgOTMuMi04NS44IDE2MC04NS44em0xNjAgMjYuNXYwYy0xMCAzLjUtMjAuOCA1LjUtMzIgNS41Yy0yOC40IDAtNTQtMTIuNC03MS42LTMyaDBjLTMuNy00LjEtNy04LjUtOS45LTEzLjJDMzI1LjMgMTY0IDMyMCAxNDYuNiAzMjAgMTI4djBWMzIgMTIgMTAuN0MzMjAgNC44IDMyNC43IC4xIDMzMC42IDBoLjJjMy4zIDAgNi40IDEuNiA4LjQgNC4ybDAgLjFMMzUyIDIxLjNsMjcuMiAzNi4zTDM4NCA2NGg2NGw0LjgtNi40TDQ4MCAyMS4zIDQ5Mi44IDQuM2wwLS4xYzItMi42IDUuMS00LjIgOC40LTQuMmguMkM1MDcuMyAuMSA1MTIgNC44IDUxMiAxMC43VjEyIDMydjk2YzAgMTcuMy00LjYgMzMuNi0xMi42IDQ3LjZjLTExLjMgMTkuOC0yOS42IDM1LjItNTEuNCA0Mi45ek00MDAgMTI4YzAtOC44LTcuMi0xNi0xNi0xNnMtMTYgNy4yLTE2IDE2czcuMiAxNiAxNiAxNnMxNi03LjIgMTYtMTZ6bTQ4IDE2YzguOCAwIDE2LTcuMiAxNi0xNnMtNy4yLTE2LTE2LTE2cy0xNiA3LjItMTYgMTZzNy4yIDE2IDE2IDE2eiIgLz48L3N2Zz4=" class="fa" /></span> | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0zNDYuNyA2QzMzNy42IDE3IDMyMCA0Mi4zIDMyMCA3MmMwIDQwIDE1LjMgNTUuMyA0MCA4MHM0MCA0MCA4MCA0MGMyOS43IDAgNTUtMTcuNiA2Ni0yNi43YzQtMy4zIDYtOC4yIDYtMTMuM3MtMi0xMC02LTEzLjJjLTExLjQtOS4xLTM4LjMtMjYuOC03NC0yNi44Yy0zMiAwLTQwIDgtNDAgOHM4LTggOC00MGMwLTM1LjctMTcuNy02Mi42LTI2LjgtNzRDMzcwIDIgMzY1LjEgMCAzNjAgMHMtMTAgMi0xMy4zIDZ6TTI0NC42IDEzNmMtNDAgMC03Ny4xIDE4LjEtMTAxLjcgNDguMmw2MC41IDYwLjVjNi4yIDYuMiA2LjIgMTYuNCAwIDIyLjZzLTE2LjQgNi4yLTIyLjYgMGwtNTUuMy01NS4zIDAgLjFMMi4yIDQ3Ny45Qy0yIDQ4Ny0uMSA0OTcuOCA3IDUwNXMxNy45IDkgMjcuMSA0LjhsMTM0LjctNjIuNC01Mi4xLTUyLjFjLTYuMi02LjItNi4yLTE2LjQgMC0yMi42czE2LjQtNi4yIDIyLjYgMEwxOTkuNyA0MzNsMTAwLjItNDYuNGM0Ni40LTIxLjUgNzYuMi02OCA3Ni4yLTExOS4yQzM3NiAxOTQuOCAzMTcuMiAxMzYgMjQ0LjYgMTM2eiIgLz48L3N2Zz4=" class="fa" /> <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik00ODguNiAyMy40YzMxLjIgMzEuMiAzMS4yIDgxLjkgMCAxMTMuMWwtMzUyIDM1MmMtMzEuMiAzMS4yLTgxLjkgMzEuMi0xMTMuMSAwcy0zMS4yLTgxLjkgMC0xMTMuMWwzNTItMzUyYzMxLjItMzEuMiA4MS45LTMxLjIgMTEzLjEgMHpNNDQzLjMgOTIuN2MtNi4yLTYuMi0xNi40LTYuMi0yMi42IDBjLTEyLjUgMTIuNS0yMy44IDE1LjEtMzcuNSAxNy42bC0yLjUgLjRjLTEzLjggMi41LTMxLjYgNS42LTQ4IDIyYy0xNi43IDE2LjctMjAuOSAzNi0yNC4xIDUwLjlsMCAwdjBsLS4yIDFjLTMuNCAxNS42LTYgMjYuNC0xNS43IDM2LjFzLTIwLjUgMTIuMy0zNi4xIDE1LjdsLTEgLjJjLTE0LjkgMy4yLTM0LjIgNy40LTUwLjkgMjQuMXMtMjAuOSAzNi0yNC4xIDUwLjlsLS4yIDFjLTMuNCAxNS42LTYgMjYuNC0xNS43IDM2LjFjLTkuMiA5LjItMTggMTAuOC0zMi43IDEzLjRsMCAwLS45IC4yYy0xNS42IDIuOC0zNC45IDYuOS01NC40IDI2LjRjLTYuMiA2LjItNi4yIDE2LjQgMCAyMi42czE2LjQgNi4yIDIyLjYgMGMxMi41LTEyLjUgMjMuOC0xNS4xIDM3LjUtMTcuNmwyLjUtLjRjMTMuOC0yLjUgMzEuNi01LjYgNDgtMjJjMTYuNy0xNi43IDIwLjktMzYgMjQuMS01MC45bC4yLTFjMy40LTE1LjYgNi0yNi40IDE1LjctMzYuMXMyMC41LTEyLjMgMzYuMS0xNS43bDEtLjJjMTQuOS0zLjIgMzQuMi03LjQgNTAuOS0yNC4xczIwLjktMzYgMjQuMS01MC45bC4yLTFjMy40LTE1LjYgNi0yNi40IDE1LjctMzYuMWM5LjItOS4yIDE4LTEwLjggMzIuNy0xMy40bC45LS4yYzE1LjYtMi44IDM0LjktNi45IDU0LjQtMjYuNGM2LjItNi4yIDYuMi0xNi40IDAtMjIuNnpNMTkxLjIgNDc5LjJsMjg4LTI4OEw0OTUgMjA3YzEwLjkgMTAuOSAxNyAyNS42IDE3IDQxcy02LjEgMzAuMS0xNyA0MUwyODkgNDk1Yy0xMC45IDEwLjktMjUuNiAxNy00MSAxN3MtMzAuMS02LjEtNDEtMTdsLTE1LjgtMTUuOHpNMTcgMzA1QzYuMSAyOTQuMSAwIDI3OS40IDAgMjY0czYuMS0zMC4xIDE3LTQxTDIyMyAxN0MyMzMuOSA2LjEgMjQ4LjYgMCAyNjQgMHMzMC4xIDYuMSA0MSAxN2wxNS44IDE1LjgtMjg4IDI4OEwxNyAzMDV6IiAvPjwvc3ZnPg==" class="fa" /></span> |
| <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuNWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yOTEuMiAzODguNGMzMS4yLTE4LjggNjQuNy0zNi40IDEwMS4xLTM2LjRINDQ4YzQuNiAwIDkuMS0uMiAxMy42LS43bDg1LjMgMTIxLjljNCA1LjcgMTEuMyA4LjIgMTcuOSA2LjFzMTEuMi04LjMgMTEuMi0xNS4zVjIyNGMwLTcwLjctNTcuMy0xMjgtMTI4LTEyOEgzOTIuM2MtMzYuNCAwLTY5LjktMTcuNi0xMDEuMS0zNi40QzI2Mi4zIDQyLjEgMjI4LjMgMzIgMTkyIDMyQzg2IDMyIDAgMTE4IDAgMjI0YzAgNzEuMSAzOC42IDEzMy4xIDk2IDE2Ni4zVjQ1NmMwIDEzLjMgMTAuNyAyNCAyNCAyNHMyNC0xMC43IDI0LTI0VjQxMGMxNS4zIDMuOSAzMS40IDYgNDggNmM1LjQgMCAxMC43LS4yIDE2LS43VjQ1NmMwIDEzLjMgMTAuNyAyNCAyNCAyNHMyNC0xMC43IDI0LTI0VjQwNS4xYzEyLjQtNC40IDI0LjItMTAgMzUuMi0xNi43ek00NDggMjQ4Yy0xMy4zIDAtMjQtMTAuNy0yNC0yNHMxMC43LTI0IDI0LTI0czI0IDEwLjcgMjQgMjRzLTEwLjcgMjQtMjQgMjR6IiAvPjwvc3ZnPg==" class="fa" /></span> | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6NGVtO3dpZHRoOjQuNWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik00MzkuMiAxLjJjMTEuMi0zLjIgMjMuMi0uMSAzMS40IDguMUw1MTggNTYuN2wtMjYuNSA3LjljLTU4IDE2LjYtOTguMSAzOS42LTEyOS42IDY3LjRjLTMxLjIgMjcuNS01My4yIDU5LjEtNzUuMSA5MC45bC0yLjMgMy4zQzI0MS42IDI4OC43IDE5NSAzNTYuNiA3Mi44IDQxNy43TDM3LjkgNDM1LjIgOS40IDQwNi42Yy03LjMtNy4zLTEwLjYtMTcuNi05LTI3LjhzOC4xLTE4LjkgMTcuMy0yMy41QzEzNi4xIDI5Ni4yIDE4MC45IDIzMSAyMjMuMyAxNjkuM2wyLjMtMy40YzIxLjgtMzEuOCA0NC45LTY0LjkgNzcuNy05My45YzMzLjQtMjkuNSA3NS44LTUzLjYgMTM1LjktNzAuOHpNNjEuOCA0NTlsMjUuNC0xMi43YzEyOS41LTY0LjcgMTc5LjktMTM4LjEgMjIzLjgtMjAybDIuMi0zLjNjMjIuMS0zMi4xIDQyLjEtNjAuNSA2OS45LTg1LjFjMjcuNS0yNC4zIDYzLjQtNDUuMiAxMTcuMy02MC42bDAgMCAuMi0uMSA0My4xLTEyLjkgMjMgMjNjOCA4IDExLjIgMTkuNyA4LjMgMzAuN3MtMTEuMyAxOS42LTIyLjIgMjIuN2MtNTEuOSAxNC44LTg1LjYgMzQuNy0xMTEuMSA1Ny4yYy0yNi4xIDIzLTQ1LjEgNDkuOS02Ny4zIDgyLjFsLTIuMiAzLjJDMzI3LjggMzY1LjkgMjc1LjUgNDQyIDE0Mi4zIDUwOC42Yy0xMi4zIDYuMi0yNy4yIDMuNy0zNi45LTZMNjEuOCA0NTl6IiAvPjwvc3ZnPg==" class="fa" /></span> |


Let's take a few rows from the towny dataset and make it so the `csd_type` column contains *Font Awesome* icon names (we want only the `"city"` and `"house-chimney"` icons here). After using [fmt_icon()](GT.fmt_icon.md#great_tables.GT.fmt_icon) to format the `csd_type` column, we get icons that are representative of the two categories of municipality for this subset of data.


``` python
import polars as pl
from great_tables.data import towny

towny_mini = (
    pl.from_pandas(towny.loc[[323, 14, 26, 235]])
    .select(["name", "csd_type", "population_2021"])
    .with_columns(
       csd_type = pl.when(pl.col("csd_type") == "town")
       .then(pl.lit("house-chimney"))
       .otherwise(pl.lit("city"))
    )
)

(
   GT(towny_mini)
   .fmt_integer(columns="population_2021")
   .fmt_icon(columns="csd_type")
   .cols_label(
       csd_type="",
       name="City/Town",
       population_2021="Population"
   )
)
```


<style>
#adaocvocvx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#adaocvocvx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#adaocvocvx p { margin: 0; padding: 0; }
 #adaocvocvx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #adaocvocvx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #adaocvocvx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #adaocvocvx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #adaocvocvx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #adaocvocvx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #adaocvocvx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #adaocvocvx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #adaocvocvx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #adaocvocvx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #adaocvocvx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #adaocvocvx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #adaocvocvx .gt_spanner_row { border-bottom-style: hidden; }
 #adaocvocvx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #adaocvocvx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #adaocvocvx .gt_from_md> :first-child { margin-top: 0; }
 #adaocvocvx .gt_from_md> :last-child { margin-bottom: 0; }
 #adaocvocvx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #adaocvocvx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #adaocvocvx .gt_indent_1 { text-indent: 5px; }
 #adaocvocvx .gt_indent_2 { text-indent: calc(5px * 2); }
 #adaocvocvx .gt_indent_3 { text-indent: calc(5px * 3); }
 #adaocvocvx .gt_indent_4 { text-indent: calc(5px * 4); }
 #adaocvocvx .gt_indent_5 { text-indent: calc(5px * 5); }
 #adaocvocvx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #adaocvocvx .gt_row_group_first td { border-top-width: 2px; }
 #adaocvocvx .gt_row_group_first th { border-top-width: 2px; }
 #adaocvocvx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #adaocvocvx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #adaocvocvx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #adaocvocvx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #adaocvocvx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #adaocvocvx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #adaocvocvx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #adaocvocvx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #adaocvocvx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #adaocvocvx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #adaocvocvx .gt_left { text-align: left; }
 #adaocvocvx .gt_center { text-align: center; }
 #adaocvocvx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #adaocvocvx .gt_font_normal { font-weight: normal; }
 #adaocvocvx .gt_font_bold { font-weight: bold; }
 #adaocvocvx .gt_font_italic { font-style: italic; }
 #adaocvocvx .gt_super { font-size: 65%; }
 #adaocvocvx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #adaocvocvx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #adaocvocvx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #adaocvocvx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #adaocvocvx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #adaocvocvx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| City/Town |  | Population |
|----|----|----|
| Sarnia | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNjQwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjEuMjVlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNNDgwIDQ4YzAtMjYuNS0yMS41LTQ4LTQ4LTQ4SDMzNmMtMjYuNSAwLTQ4IDIxLjUtNDggNDhWOTZIMjI0VjI0YzAtMTMuMy0xMC43LTI0LTI0LTI0cy0yNCAxMC43LTI0IDI0Vjk2SDExMlYyNGMwLTEzLjMtMTAuNy0yNC0yNC0yNFM2NCAxMC43IDY0IDI0Vjk2SDQ4QzIxLjUgOTYgMCAxMTcuNSAwIDE0NHY5NlY0NjRjMCAyNi41IDIxLjUgNDggNDggNDhIMzA0aDMyIDk2SDU5MmMyNi41IDAgNDgtMjEuNSA0OC00OFYyNDBjMC0yNi41LTIxLjUtNDgtNDgtNDhINDgwVjQ4em05NiAzMjB2MzJjMCA4LjgtNy4yIDE2LTE2IDE2SDUyOGMtOC44IDAtMTYtNy4yLTE2LTE2VjM2OGMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2ek0yNDAgNDE2SDIwOGMtOC44IDAtMTYtNy4yLTE2LTE2VjM2OGMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2djMyYzAgOC44LTcuMiAxNi0xNiAxNnpNMTI4IDQwMGMwIDguOC03LjIgMTYtMTYgMTZIODBjLTguOCAwLTE2LTcuMi0xNi0xNlYzNjhjMC04LjggNy4yLTE2IDE2LTE2aDMyYzguOCAwIDE2IDcuMiAxNiAxNnYzMnpNNTYwIDI1NmM4LjggMCAxNiA3LjIgMTYgMTZ2MzJjMCA4LjgtNy4yIDE2LTE2IDE2SDUyOGMtOC44IDAtMTYtNy4yLTE2LTE2VjI3MmMwLTguOCA3LjItMTYgMTYtMTZoMzJ6TTI1NiAxNzZ2MzJjMCA4LjgtNy4yIDE2LTE2IDE2SDIwOGMtOC44IDAtMTYtNy4yLTE2LTE2VjE3NmMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2ek0xMTIgMTYwYzguOCAwIDE2IDcuMiAxNiAxNnYzMmMwIDguOC03LjIgMTYtMTYgMTZIODBjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDMyek0yNTYgMzA0YzAgOC44LTcuMiAxNi0xNiAxNkgyMDhjLTguOCAwLTE2LTcuMi0xNi0xNlYyNzJjMC04LjggNy4yLTE2IDE2LTE2aDMyYzguOCAwIDE2IDcuMiAxNiAxNnYzMnpNMTEyIDMyMEg4MGMtOC44IDAtMTYtNy4yLTE2LTE2VjI3MmMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2djMyYzAgOC44LTcuMiAxNi0xNiAxNnptMzA0LTQ4djMyYzAgOC44LTcuMiAxNi0xNiAxNkgzNjhjLTguOCAwLTE2LTcuMi0xNi0xNlYyNzJjMC04LjggNy4yLTE2IDE2LTE2aDMyYzguOCAwIDE2IDcuMiAxNiAxNnpNNDAwIDY0YzguOCAwIDE2IDcuMiAxNiAxNnYzMmMwIDguOC03LjIgMTYtMTYgMTZIMzY4Yy04LjggMC0xNi03LjItMTYtMTZWODBjMC04LjggNy4yLTE2IDE2LTE2aDMyem0xNiAxMTJ2MzJjMCA4LjgtNy4yIDE2LTE2IDE2SDM2OGMtOC44IDAtMTYtNy4yLTE2LTE2VjE3NmMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIgLz48L3N2Zz4=" class="fa" /></span> | 72,047 |
| Arnprior | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjEuMTJlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNNTQzLjggMjg3LjZjMTcgMCAzMi0xNCAzMi0zMi4xYzEtOS0zLTE3LTExLTI0TDUxMiAxODVWNjRjMC0xNy43LTE0LjMtMzItMzItMzJINDQ4Yy0xNy43IDAtMzIgMTQuMy0zMiAzMnYzNi43TDMwOS41IDdjLTYtNS0xNC03LTIxLTdzLTE1IDEtMjIgOEwxMCAyMzEuNWMtNyA3LTEwIDE1LTEwIDI0YzAgMTggMTQgMzIuMSAzMiAzMi4xaDMydjY5LjdjLS4xIC45LS4xIDEuOC0uMSAyLjhWNDcyYzAgMjIuMSAxNy45IDQwIDQwIDQwaDE2YzEuMiAwIDIuNC0uMSAzLjYtLjJjMS41IC4xIDMgLjIgNC41IC4ySDE2MGgyNGMyMi4xIDAgNDAtMTcuOSA0MC00MFY0NDggMzg0YzAtMTcuNyAxNC4zLTMyIDMyLTMyaDY0YzE3LjcgMCAzMiAxNC4zIDMyIDMydjY0IDI0YzAgMjIuMSAxNy45IDQwIDQwIDQwaDI0IDMyLjVjMS40IDAgMi44IDAgNC4yLS4xYzEuMSAuMSAyLjIgLjEgMy4zIC4xaDE2YzIyLjEgMCA0MC0xNy45IDQwLTQwVjQ1NS44Yy4zLTIuNiAuNS01LjMgLjUtOC4xbC0uNy0xNjAuMmgzMnoiIC8+PC9zdmc+" class="fa" /></span> | 9,629 |
| Barrie | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNjQwIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjEuMjVlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNNDgwIDQ4YzAtMjYuNS0yMS41LTQ4LTQ4LTQ4SDMzNmMtMjYuNSAwLTQ4IDIxLjUtNDggNDhWOTZIMjI0VjI0YzAtMTMuMy0xMC43LTI0LTI0LTI0cy0yNCAxMC43LTI0IDI0Vjk2SDExMlYyNGMwLTEzLjMtMTAuNy0yNC0yNC0yNFM2NCAxMC43IDY0IDI0Vjk2SDQ4QzIxLjUgOTYgMCAxMTcuNSAwIDE0NHY5NlY0NjRjMCAyNi41IDIxLjUgNDggNDggNDhIMzA0aDMyIDk2SDU5MmMyNi41IDAgNDgtMjEuNSA0OC00OFYyNDBjMC0yNi41LTIxLjUtNDgtNDgtNDhINDgwVjQ4em05NiAzMjB2MzJjMCA4LjgtNy4yIDE2LTE2IDE2SDUyOGMtOC44IDAtMTYtNy4yLTE2LTE2VjM2OGMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2ek0yNDAgNDE2SDIwOGMtOC44IDAtMTYtNy4yLTE2LTE2VjM2OGMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2djMyYzAgOC44LTcuMiAxNi0xNiAxNnpNMTI4IDQwMGMwIDguOC03LjIgMTYtMTYgMTZIODBjLTguOCAwLTE2LTcuMi0xNi0xNlYzNjhjMC04LjggNy4yLTE2IDE2LTE2aDMyYzguOCAwIDE2IDcuMiAxNiAxNnYzMnpNNTYwIDI1NmM4LjggMCAxNiA3LjIgMTYgMTZ2MzJjMCA4LjgtNy4yIDE2LTE2IDE2SDUyOGMtOC44IDAtMTYtNy4yLTE2LTE2VjI3MmMwLTguOCA3LjItMTYgMTYtMTZoMzJ6TTI1NiAxNzZ2MzJjMCA4LjgtNy4yIDE2LTE2IDE2SDIwOGMtOC44IDAtMTYtNy4yLTE2LTE2VjE3NmMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2ek0xMTIgMTYwYzguOCAwIDE2IDcuMiAxNiAxNnYzMmMwIDguOC03LjIgMTYtMTYgMTZIODBjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDMyek0yNTYgMzA0YzAgOC44LTcuMiAxNi0xNiAxNkgyMDhjLTguOCAwLTE2LTcuMi0xNi0xNlYyNzJjMC04LjggNy4yLTE2IDE2LTE2aDMyYzguOCAwIDE2IDcuMiAxNiAxNnYzMnpNMTEyIDMyMEg4MGMtOC44IDAtMTYtNy4yLTE2LTE2VjI3MmMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2djMyYzAgOC44LTcuMiAxNi0xNiAxNnptMzA0LTQ4djMyYzAgOC44LTcuMiAxNi0xNiAxNkgzNjhjLTguOCAwLTE2LTcuMi0xNi0xNlYyNzJjMC04LjggNy4yLTE2IDE2LTE2aDMyYzguOCAwIDE2IDcuMiAxNiAxNnpNNDAwIDY0YzguOCAwIDE2IDcuMiAxNiAxNnYzMmMwIDguOC03LjIgMTYtMTYgMTZIMzY4Yy04LjggMC0xNi03LjItMTYtMTZWODBjMC04LjggNy4yLTE2IDE2LTE2aDMyem0xNiAxMTJ2MzJjMCA4LjgtNy4yIDE2LTE2IDE2SDM2OGMtOC44IDAtMTYtNy4yLTE2LTE2VjE3NmMwLTguOCA3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIgLz48L3N2Zz4=" class="fa" /></span> | 147,829 |
| Milton | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjEuMTJlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNNTQzLjggMjg3LjZjMTcgMCAzMi0xNCAzMi0zMi4xYzEtOS0zLTE3LTExLTI0TDUxMiAxODVWNjRjMC0xNy43LTE0LjMtMzItMzItMzJINDQ4Yy0xNy43IDAtMzIgMTQuMy0zMiAzMnYzNi43TDMwOS41IDdjLTYtNS0xNC03LTIxLTdzLTE1IDEtMjIgOEwxMCAyMzEuNWMtNyA3LTEwIDE1LTEwIDI0YzAgMTggMTQgMzIuMSAzMiAzMi4xaDMydjY5LjdjLS4xIC45LS4xIDEuOC0uMSAyLjhWNDcyYzAgMjIuMSAxNy45IDQwIDQwIDQwaDE2YzEuMiAwIDIuNC0uMSAzLjYtLjJjMS41IC4xIDMgLjIgNC41IC4ySDE2MGgyNGMyMi4xIDAgNDAtMTcuOSA0MC00MFY0NDggMzg0YzAtMTcuNyAxNC4zLTMyIDMyLTMyaDY0YzE3LjcgMCAzMiAxNC4zIDMyIDMydjY0IDI0YzAgMjIuMSAxNy45IDQwIDQwIDQwaDI0IDMyLjVjMS40IDAgMi44IDAgNC4yLS4xYzEuMSAuMSAyLjIgLjEgMy4zIC4xaDE2YzIyLjEgMCA0MC0xNy45IDQwLTQwVjQ1NS44Yy4zLTIuNiAuNS01LjMgLjUtOC4xbC0uNy0xNjAuMmgzMnoiIC8+PC9zdmc+" class="fa" /></span> | 132,979 |


A fairly common thing to do with icons in tables is to indicate whether a quantity is either higher or lower than another. Up and down arrow symbols can serve as good visual indicators for this purpose. We can make use of the `"up-arrow"` and `"down-arrow"` icons here. As those strings are available in the `dir` column of the table derived from the [sp500](data.sp500.md#great_tables.data.sp500) dataset, [fmt_icon()](GT.fmt_icon.md#great_tables.GT.fmt_icon) can be used. We set the `fill_color` argument with a dictionary that indicates which color should be used for each icon.


``` python
from great_tables.data import sp500

sp500_mini = (
    pl.from_pandas(sp500)
    .head(10)
    .select(["date", "open", "close"])
    .sort("date", descending=False)
    .with_columns(
        dir = pl.when(pl.col("close") >= pl.col("open")).then(
            pl.lit("arrow-up")).otherwise(pl.lit("arrow-down"))
    )
)

(
    GT(sp500_mini, rowname_col="date")
    .fmt_icon(
        columns="dir",
        fill_color={"arrow-up": "green", "arrow-down": "red"}
    )
    .cols_label(
        open="Opening Value",
        close="Closing Value",
        dir=""
    )
    .opt_stylize(style=1, color="gray")
)
```


<style>
#hvuhrteiea table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hvuhrteiea thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hvuhrteiea p { margin: 0; padding: 0; }
 #hvuhrteiea .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #000000; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #000000; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hvuhrteiea .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hvuhrteiea .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hvuhrteiea .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hvuhrteiea .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hvuhrteiea .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #hvuhrteiea .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hvuhrteiea .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hvuhrteiea .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hvuhrteiea .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hvuhrteiea .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hvuhrteiea .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hvuhrteiea .gt_spanner_row { border-bottom-style: hidden; }
 #hvuhrteiea .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hvuhrteiea .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: middle; }
 #hvuhrteiea .gt_from_md> :first-child { margin-top: 0; }
 #hvuhrteiea .gt_from_md> :last-child { margin-bottom: 0; }
 #hvuhrteiea .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: none; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #hvuhrteiea .gt_stub { color: #FFFFFF; background-color: #5F5F5F; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #hvuhrteiea .gt_indent_1 { text-indent: 5px; }
 #hvuhrteiea .gt_indent_2 { text-indent: calc(5px * 2); }
 #hvuhrteiea .gt_indent_3 { text-indent: calc(5px * 3); }
 #hvuhrteiea .gt_indent_4 { text-indent: calc(5px * 4); }
 #hvuhrteiea .gt_indent_5 { text-indent: calc(5px * 5); }
 #hvuhrteiea .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hvuhrteiea .gt_row_group_first td { border-top-width: 2px; }
 #hvuhrteiea .gt_row_group_first th { border-top-width: 2px; }
 #hvuhrteiea .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hvuhrteiea .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #hvuhrteiea .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hvuhrteiea .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hvuhrteiea .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvuhrteiea .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hvuhrteiea .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hvuhrteiea .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hvuhrteiea .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvuhrteiea .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hvuhrteiea .gt_left { text-align: left; }
 #hvuhrteiea .gt_center { text-align: center; }
 #hvuhrteiea .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hvuhrteiea .gt_font_normal { font-weight: normal; }
 #hvuhrteiea .gt_font_bold { font-weight: bold; }
 #hvuhrteiea .gt_font_italic { font-style: italic; }
 #hvuhrteiea .gt_super { font-size: 65%; }
 #hvuhrteiea .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvuhrteiea .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hvuhrteiea .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvuhrteiea .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hvuhrteiea .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hvuhrteiea .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | Opening Value | Closing Value |  |
|----|----|----|----|
| 2015-12-17 | 2073.76 | 2041.89 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpyZWQ7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjAuNzVlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNMTY5LjQgNDcwLjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBsMTYwLTE2MGMxMi41LTEyLjUgMTIuNS0zMi44IDAtNDUuM3MtMzIuOC0xMi41LTQ1LjMgMEwyMjQgMzcwLjggMjI0IDY0YzAtMTcuNy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMybDAgMzA2LjdMNTQuNiAyNjUuNGMtMTIuNS0xMi41LTMyLjgtMTIuNS00NS4zIDBzLTEyLjUgMzIuOCAwIDQ1LjNsMTYwIDE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
| 2015-12-18 | 2040.8101 | 2005.55 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpyZWQ7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjAuNzVlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNMTY5LjQgNDcwLjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBsMTYwLTE2MGMxMi41LTEyLjUgMTIuNS0zMi44IDAtNDUuM3MtMzIuOC0xMi41LTQ1LjMgMEwyMjQgMzcwLjggMjI0IDY0YzAtMTcuNy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMybDAgMzA2LjdMNTQuNiAyNjUuNGMtMTIuNS0xMi41LTMyLjgtMTIuNS00NS4zIDBzLTEyLjUgMzIuOCAwIDQ1LjNsMTYwIDE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
| 2015-12-21 | 2010.27 | 2021.15 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpncmVlbjtzdHJva2Utd2lkdGg6MXB4O2hlaWdodDoxZW07d2lkdGg6MC43NWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMTQuNiA0MS40Yy0xMi41LTEyLjUtMzIuOC0xMi41LTQ1LjMgMGwtMTYwIDE2MGMtMTIuNSAxMi41LTEyLjUgMzIuOCAwIDQ1LjNzMzIuOCAxMi41IDQ1LjMgMEwxNjAgMTQxLjJWNDQ4YzAgMTcuNyAxNC4zIDMyIDMyIDMyczMyLTE0LjMgMzItMzJWMTQxLjJMMzI5LjQgMjQ2LjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBzMTIuNS0zMi44IDAtNDUuM2wtMTYwLTE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
| 2015-12-22 | 2023.15 | 2038.97 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpncmVlbjtzdHJva2Utd2lkdGg6MXB4O2hlaWdodDoxZW07d2lkdGg6MC43NWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMTQuNiA0MS40Yy0xMi41LTEyLjUtMzIuOC0xMi41LTQ1LjMgMGwtMTYwIDE2MGMtMTIuNSAxMi41LTEyLjUgMzIuOCAwIDQ1LjNzMzIuOCAxMi41IDQ1LjMgMEwxNjAgMTQxLjJWNDQ4YzAgMTcuNyAxNC4zIDMyIDMyIDMyczMyLTE0LjMgMzItMzJWMTQxLjJMMzI5LjQgMjQ2LjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBzMTIuNS0zMi44IDAtNDUuM2wtMTYwLTE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
| 2015-12-23 | 2042.2 | 2064.29 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpncmVlbjtzdHJva2Utd2lkdGg6MXB4O2hlaWdodDoxZW07d2lkdGg6MC43NWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMTQuNiA0MS40Yy0xMi41LTEyLjUtMzIuOC0xMi41LTQ1LjMgMGwtMTYwIDE2MGMtMTIuNSAxMi41LTEyLjUgMzIuOCAwIDQ1LjNzMzIuOCAxMi41IDQ1LjMgMEwxNjAgMTQxLjJWNDQ4YzAgMTcuNyAxNC4zIDMyIDMyIDMyczMyLTE0LjMgMzItMzJWMTQxLjJMMzI5LjQgMjQ2LjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBzMTIuNS0zMi44IDAtNDUuM2wtMTYwLTE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
| 2015-12-24 | 2063.52 | 2060.99 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpyZWQ7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjAuNzVlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNMTY5LjQgNDcwLjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBsMTYwLTE2MGMxMi41LTEyLjUgMTIuNS0zMi44IDAtNDUuM3MtMzIuOC0xMi41LTQ1LjMgMEwyMjQgMzcwLjggMjI0IDY0YzAtMTcuNy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMybDAgMzA2LjdMNTQuNiAyNjUuNGMtMTIuNS0xMi41LTMyLjgtMTIuNS00NS4zIDBzLTEyLjUgMzIuOCAwIDQ1LjNsMTYwIDE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
| 2015-12-28 | 2057.77 | 2056.5 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpyZWQ7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjAuNzVlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNMTY5LjQgNDcwLjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBsMTYwLTE2MGMxMi41LTEyLjUgMTIuNS0zMi44IDAtNDUuM3MtMzIuOC0xMi41LTQ1LjMgMEwyMjQgMzcwLjggMjI0IDY0YzAtMTcuNy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMybDAgMzA2LjdMNTQuNiAyNjUuNGMtMTIuNS0xMi41LTMyLjgtMTIuNS00NS4zIDBzLTEyLjUgMzIuOCAwIDQ1LjNsMTYwIDE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
| 2015-12-29 | 2060.54 | 2078.3601 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpncmVlbjtzdHJva2Utd2lkdGg6MXB4O2hlaWdodDoxZW07d2lkdGg6MC43NWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0yMTQuNiA0MS40Yy0xMi41LTEyLjUtMzIuOC0xMi41LTQ1LjMgMGwtMTYwIDE2MGMtMTIuNSAxMi41LTEyLjUgMzIuOCAwIDQ1LjNzMzIuOCAxMi41IDQ1LjMgMEwxNjAgMTQxLjJWNDQ4YzAgMTcuNyAxNC4zIDMyIDMyIDMyczMyLTE0LjMgMzItMzJWMTQxLjJMMzI5LjQgMjQ2LjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBzMTIuNS0zMi44IDAtNDUuM2wtMTYwLTE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
| 2015-12-30 | 2077.3401 | 2063.3601 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpyZWQ7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjAuNzVlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNMTY5LjQgNDcwLjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBsMTYwLTE2MGMxMi41LTEyLjUgMTIuNS0zMi44IDAtNDUuM3MtMzIuOC0xMi41LTQ1LjMgMEwyMjQgMzcwLjggMjI0IDY0YzAtMTcuNy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMybDAgMzA2LjdMNTQuNiAyNjUuNGMtMTIuNS0xMi41LTMyLjgtMTIuNS00NS4zIDBzLTEyLjUgMzIuOCAwIDQ1LjNsMTYwIDE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
| 2015-12-31 | 2060.5901 | 2043.9399 | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpyZWQ7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjAuNzVlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNMTY5LjQgNDcwLjZjMTIuNSAxMi41IDMyLjggMTIuNSA0NS4zIDBsMTYwLTE2MGMxMi41LTEyLjUgMTIuNS0zMi44IDAtNDUuM3MtMzIuOC0xMi41LTQ1LjMgMEwyMjQgMzcwLjggMjI0IDY0YzAtMTcuNy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMybDAgMzA2LjdMNTQuNiAyNjUuNGMtMTIuNS0xMi41LTMyLjgtMTIuNS00NS4zIDBzLTEyLjUgMzIuOCAwIDQ1LjNsMTYwIDE2MHoiIC8+PC9zdmc+" class="fa" /></span> |
