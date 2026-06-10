## GT.fmt_flag()


Generate flag icons for countries from their country codes.


Usage

``` python
GT.fmt_flag(
    columns=None,
    rows=None,
    height="1em",
    sep=" ",
    use_title=True,
)
```


While it is fairly straightforward to insert images into body cells (using [fmt_image()](GT.fmt_image.md#great_tables.GT.fmt_image) is one way to it), there is often the need to incorporate specialized types of graphics within a table. One such group of graphics involves iconography representing different countries, and the [fmt_flag()](GT.fmt_flag.md#great_tables.GT.fmt_flag) method helps with inserting a flag icon (or multiple) in body cells. To make this work seamlessly, the input cells need to contain some reference to a country, and this can be in the form of a 2- or 3-letter ISO 3166-1 country code (e.g., Egypt has the `"EG"` country code). This method will parse the targeted body cells for those codes and insert the appropriate flag graphics.

Multiple flags can be included per cell by separating country codes with commas (e.g., `"GB,TT"`). The `sep=` argument allows for a common separator to be applied between flag icons.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`height: str | int | float | None = ``"1em"`  
The height of the flag icons. The default value is `"1em"`. If given as a number, it is assumed to be in pixels.

`sep: str = ``" "`  
In the output of multiple flag icons within a body cell, `sep=` provides the separator between each of the flag icons.

`use_title: bool = ``True`  
The option to include a title attribute with the country name when hovering over the flag icon. The default is `True`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a new table with flag icons. We will only include a few columns and rows from that table. The `country_code_2` column has 2-letter country codes in the format required for [fmt_flag()](GT.fmt_flag.md#great_tables.GT.fmt_flag) and using that method transforms the codes to circular flag icons.


``` python
from great_tables import GT
from great_tables.data import countrypops
import polars as pl

countrypops_mini = (
    pl.from_pandas(countrypops)
    .filter(pl.col("year") == 2021)
    .filter(pl.col("country_name").str.starts_with("S"))
    .sort("country_name")
    .head(10)
    .drop(["year", "country_code_3"])
)

(
    GT(countrypops_mini)
    .fmt_integer(columns="population")
    .fmt_flag(columns="country_code_2")
    .cols_label(
        country_code_2="",
        country_name="Country",
        population="Population (2021)"
    )
    .cols_move_to_start(columns="country_code_2")
)
```


|  | Country | Population (2021) |
|----|----|----|
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2Ftb2E8L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0wIDI1NiAyNTYgMGgyNTZ2NTEySDB6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMjU2djI1NkgweiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJtMjA1IDE2NyA0LjIgMTIuN2gxMy40bC0xMC44IDcuOSA0LjEgMTIuNy0xMC44LTcuOC0xMC45IDcuOCA0LjEtMTIuNy0xMC44LTcuOWgxMy40ek0xMzcuOCA2Ni44bDcgMjEuMkgxNjdsLTE4LjEgMTMuMiA2LjkgMjEuMi0xOC4xLTEzLjEtMTggMTMuMSA2LjgtMjEuMi0xOC0xMy4yaDIyLjN6TTIwNC41IDg5bDYuOSAyMS4zaDIyLjNsLTE4IDEzLjEgNi45IDIxLjMtMTguMS0xMy4xLTE4LjEgMTMuMSA3LTIxLjMtMTguMi0xMy4xaDIyLjR6bS01Mi44IDg5IDYuOSAyMS4zSDE4MWwtMTguMSAxMy4yIDYuOSAyMS4yLTE4LjEtMTMuMS0xOCAxMy4xIDYuOC0yMS4yLTE4LTEzLjJoMjIuM3ptLTU4LjUtNTUuNiA2LjkgMjEuM2gyMi4zbC0xOCAxMy4xIDYuOSAyMS4zLTE4LjEtMTMuMkw3NSAxNzguMWw2LjktMjEuMy0xOC0xMy4xaDIyLjN6IiAvPjwvZz48L3N2Zz4=)</span> | Samoa | 218,764 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2FuIE1hcmlubzwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iIzMzOGFmMyIgZD0ibTAgMjU2IDI1Ni01Mi4zTDUxMiAyNTZ2MjU2SDB6IiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDBoNTEydjI1NkgweiIgLz48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMzU3LjYgMTc2LjYgMjU2IDI3OC4zIDE1NC40IDE3Ni42YTEyMS43IDEyMS43IDAgMCAwLTIwLjggNjguM3YzMy40YzAgNTMuNiAzNC42IDk5LjIgODIuNyAxMTUuOGEzNyAzNyAwIDAgMCA0IDQwbDM2LjQtMjkuMiAzNi40IDI5LjJhMzcgMzcgMCAwIDAgMy45LTQwLjUgMTIyLjYgMTIyLjYgMCAwIDAgODEuNC0xMTUuM3YtMzMuNGMwLTI1LjMtNy42LTQ4LjctMjAuOC02OC4zeiIgLz48cGF0aCBmaWxsPSIjZmZkYTQ0IiBkPSJNMjU2IDM2Ny4zYy00OS4xIDAtODktNDAtODktODl2LTMzLjRhODkuMSA4OS4xIDAgMCAxIDE3OCAwdjMzLjRjMCA0OS0zOS45IDg5LTg5IDg5eiIgLz48cGF0aCBmaWxsPSIjMzM4YWYzIiBkPSJNMzExLjcgMjc4LjN2LTMzLjRhNTUuNyA1NS43IDAgMCAwLTExMS40IDB2MzMuNGw1NS43IDExeiIgLz48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMjAwLjMgMjc4LjNhNTUuNyA1NS43IDAgMCAwIDExMS40IDB6IiAvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Ik0zMjIuOCAxNTUuOEEzMy40IDMzLjQgMCAwIDAgMjY3IDEzMXYtMTkuNmgxMS4yVjg5SDI2N1Y3OGgtMjJ2MTFoLTExLjJ2MjIuM0gyNDV2MTkuNmEzMy40IDMzLjQgMCAwIDAtNDQuNSA0OS44djE5LjZoMTExLjN2LTE5LjZjNi44LTYuMSAxMS0xNSAxMS0yNC45eiIgLz48L2c+PC9zdmc+)</span> | San Marino | 33,745 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2FvIFRvbWUgYW5kIFByaW5jaXBlPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMCAwaDUxMnYxNjdsLTUyLjYgODMuOEw1MTIgMzQ1djE2N0gwbDcyLTI2NC4zeiIgLz48cGF0aCBmaWxsPSIjZmZkYTQ0IiBkPSJNMTE0LjkgMTY2LjlINTEydjE3OEgxMTQuOXoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMHY1MTJsMjU2LTI1NnoiIC8+PHBhdGggZmlsbD0iIzMzMyIgZD0ibTMyNSAyMTEuNSAxMS4xIDM0SDM3MmwtMjkgMjEgMTEuMSAzNC0yOS0yMS0yOC45IDIxIDExLTM0LTI4LjgtMjFIMzE0em0xMTEuNCAwIDExIDM0aDM1LjhsLTI5IDIxIDExLjEgMzQtMjktMjEtMjguOSAyMSAxMS4xLTM0LTI5LTIxaDM1Ljh6IiAvPjwvZz48L3N2Zz4=)</span> | Sao Tome and Principe | 223,107 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2F1ZGkgQXJhYmlhPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjNDk2ZTJkIiBkPSJNMCAwaDUxMnY1MTJIMHoiIC8+PGcgZmlsbD0iI2VlZSI+PHBhdGggZD0iTTE0NC43IDMwNmMwIDE4LjUgMTUgMzMuNSAzMy40IDMzLjVoMTAwLjJhMjcuOCAyNy44IDAgMCAwIDI3LjggMjcuOGgzMy40YTI3LjggMjcuOCAwIDAgMCAyNy44LTI3LjhWMzA2em0yMjUuNC0xNjEuM3Y3OGMwIDEyLjItMTAgMjIuMi0yMi4zIDIyLjJ2MzMuNGMzMC43IDAgNTUuNy0yNSA1NS43LTU1Ljd2LTc3LjlIMzcwem0tMjM5LjMgNzhjMCAxMi4yLTEwIDIyLjItMjIuMyAyMi4ydjMzLjRjMzAuNyAwIDU1LjctMjUgNTUuNy01NS43di03Ny45aC0zMy40eiIgLz48cGF0aCBkPSJNMzIwIDE0NC43aDMzLjR2NzhIMzIwem0tNTAgNDQuNWE1LjYgNS42IDAgMCAxLTExLjIgMHYtNDQuNWgtMzMuNHY0NC41YTUuNiA1LjYgMCAwIDEtMTEuMSAwdi00NC41aC0zMy40djQ0LjVhMzkgMzkgMCAwIDAgMzkgMzkgMzguNyAzOC43IDAgMCAwIDIyLjItNyAzOC43IDM4LjcgMCAwIDAgMjIuMiA3YzEuNyAwIDMuNC0uMSA1LS4zYTIyLjMgMjIuMyAwIDAgMS0yMS42IDE3djMzLjRjMzAuNiAwIDU1LjYtMjUgNTUuNi01NS43di03Ny45SDI3MHoiIC8+PHBhdGggZD0iTTE4MC45IDI0NC45aDUwdjMzLjRoLTUweiIgLz48L2c+PC9nPjwvc3ZnPg==)</span> | Saudi Arabia | 35,950,396 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2VuZWdhbDwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0iTTE0NC44IDBoMjIyLjRsMzIgMjYwLTMyIDI1MkgxNDQuOGwtMzIuMS0yNTZ6IiAvPjxwYXRoIGZpbGw9IiM0OTZlMmQiIGQ9Ik0wIDBoMTQ0Ljh2NTEySDB6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0zNjcuMiAwSDUxMnY1MTJIMzY3LjJ6IiAvPjxwYXRoIGZpbGw9IiM0OTZlMmQiIGQ9Im0yNTYuMSAxNjcgMjIuMSA2OGg3MS41TDI5MiAyNzdsMjIgNjgtNTcuOC00Mi01Ny45IDQyIDIyLjEtNjgtNTcuOC00MkgyMzR6IiAvPjwvZz48L3N2Zz4=)</span> | Senegal | 16,876,720 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2VyYmlhPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjMDA1MmI0IiBkPSJtMCAxNjcgMjUzLjgtMTkuM0w1MTIgMTY3djE3OGwtMjU0LjkgMzIuM0wwIDM0NXoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MTY3SDB6IiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDM0NWg1MTJ2MTY3SDB6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik02Ni4yIDE0NC43djEyNy43YzAgNzIuNiA5NC45IDk1IDk0LjkgOTVzOTQuOS0yMi40IDk0LjktOTVWMTQ0Ljd6IiAvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Ik0xMDUuNCAxNjdoMTExLjR2LTQ0LjZsLTIyLjMgMTEuMi0zMy40LTMzLjQtMzMuNCAzMy40LTIyLjMtMTEuMnptMTI4LjMgMTIzLjItNzIuMy03Mi40TDg5IDI5MC4ybDIzLjcgMjMuNiA0OC43LTQ4LjcgNDguNyA0OC43eiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMjMzLjcgMjIyLjZIMjAwYTIyLjEgMjIuMSAwIDAgMCAzLTExLjEgMjIuMyAyMi4zIDAgMCAwLTQyLTEwLjUgMjIuMyAyMi4zIDAgMCAwLTQxLjkgMTAuNSAyMi4xIDIyLjEgMCAwIDAgMyAxMS4xSDg5YTIzIDIzIDAgMCAwIDIzIDIyLjNoLS43YzAgMTIuMyAxMCAyMi4yIDIyLjMgMjIuMiAwIDExIDcuOCAyMCAxOC4xIDIxLjlsLTE3LjUgMzkuNmE3Mi4xIDcyLjEgMCAwIDAgMjcuMiA1LjMgNzIuMSA3Mi4xIDAgMCAwIDI3LjItNS4zTDE3MS4xIDI4OWMxMC4zLTIgMTguMS0xMSAxOC4xLTIxLjkgMTIuMyAwIDIyLjMtMTAgMjIuMy0yMi4yaC0uOGEyMyAyMyAwIDAgMCAyMy0yMi4zeiIgLz48L2c+PC9zdmc+)</span> | Serbia | 6,834,326 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2V5Y2hlbGxlczwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTAgMHYzMzJsMTUwLjktMTM4LjVMMjI1LjIgMHoiIC8+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0iTTI3My4xIDI1My4zIDUxMiAwSDIyNS4yTDAgMzMydjgwLjJ6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik01MTIgMCAwIDQxMi4ydjUwLjRMMjc3LjkgMzkwIDUxMiAyNTZ6IiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDQ2Mi42IDUxMiAyNTZ2MTMzLjVsLTIyMy45IDc4LjhMMCA0ODguNHoiIC8+PHBhdGggZmlsbD0iIzZkYTU0NCIgZD0ibTUxMiAzODkuNS01MTIgOTlWNTEyaDUxMnoiIC8+PC9nPjwvc3ZnPg==)</span> | Seychelles | 99,258 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2llcnJhIExlb25lPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJtMCAxNjcgMjUzLjgtMTkuM0w1MTIgMTY3djE3OGwtMjU0LjkgMzIuM0wwIDM0NXoiIC8+PHBhdGggZmlsbD0iIzZkYTU0NCIgZD0iTTAgMGg1MTJ2MTY3SDB6IiAvPjxwYXRoIGZpbGw9IiMzMzhhZjMiIGQ9Ik0wIDM0NWg1MTJ2MTY3SDB6IiAvPjwvZz48L3N2Zz4=)</span> | Sierra Leone | 8,420,641 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2luZ2Fwb3JlPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJtMCAyNTYgMjU3LjctNTFMNTEyIDI1NnYyNTZIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MjU2SDB6IiAvPjxnIGZpbGw9IiNlZWUiPjxwYXRoIGQ9Ik0xNTUuOCAxMzMuNkE3OCA3OCAwIDAgMSAyMTcgNTcuNWE3OC4yIDc4LjIgMCAwIDAtMTYuNy0xLjggNzggNzggMCAxIDAgMTYuNyAxNTQgNzggNzggMCAwIDEtNjEuMi03Ni4xek0yNTYgNjEuMmw1LjUgMTdoMThsLTE0LjYgMTAuNSA1LjYgMTdMMjU2IDk1LjJsLTE0LjUgMTAuNSA1LjYtMTctMTQuNS0xMC41aDE3Ljl6IiAvPjxwYXRoIGQ9Im0yMTIuNiA5NC42IDUuNiAxN0gyMzZsLTE0LjQgMTAuNSA1LjUgMTctMTQuNS0xMC41LTE0LjQgMTAuNSA1LjUtMTctMTQuNS0xMC41aDE3Ljl6bTg2LjggMCA1LjUgMTdoMTcuOWwtMTQuNSAxMC41IDUuNSAxNy0xNC40LTEwLjUtMTQuNSAxMC41IDUuNS0xNy0xNC40LTEwLjVoMTcuOHptLTE2LjcgNTAuMSA1LjUgMTdoMTcuOWwtMTQuNSAxMC41IDUuNSAxNy0xNC40LTEwLjUtMTQuNSAxMC41IDUuNS0xNy0xNC40LTEwLjVoMTcuOXptLTUzLjQgMCA1LjUgMTdoMThsLTE0LjUgMTAuNSA1LjUgMTctMTQuNS0xMC41LTE0LjQgMTAuNSA1LjUtMTctMTQuNS0xMC41aDE3Ljl6IiAvPjwvZz48L2c+PC9zdmc+)</span> | Singapore | 5,453,566 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2ludCBNYWFydGVuIChEdXRjaCBwYXJ0KTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MjU2bC0yNjUgNDUuMnoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTIxMCAyNTZoMzAydjI1NkgweiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMCAwdjUxMmwyNTYtMjU2eiIgLz48ZyBmaWxsPSIjZmZkYTQ0Ij48cGF0aCBkPSJNMjggMjU2YTczLjEgNzMuMSAwIDAgMC0uMiA1LjYgNzIuMyA3Mi4zIDAgMSAwIDE0NC41LTUuNnoiIC8+PGNpcmNsZSBjeD0iMTAwLjIiIGN5PSIyMDAuMyIgcj0iMjIuMyI+PC9jaXJjbGU+PC9nPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik01MCAxOTQuOFYyNjdjMCAzOC40IDUwLjIgNTAgNTAuMiA1MHM1MC0xMS42IDUwLTUwdi03Mi4zaC0xMDB6IiAvPjxwYXRoIGZpbGw9IiMzMzhhZjMiIGQ9Ik0xMDAuMiAyOTRjLTkuMy0zLjQtMjgtMTItMjgtMjd2LTUwSDEyOHY1MGMwIDE1LTE4LjYgMjMuNi0yNy44IDI2Ljl6IiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0xMTEuMyAyNDQuOXYtMTEuMmwtMTEuMS01LjUtMTEuMiA1LjVWMjQ1bC01LjUgNS41djIyLjNoMzMuNHYtMjIuM3oiIC8+PC9nPjwvc3ZnPg==)</span> | Sint Maarten (Dutch part) | 42,846 |


Here's another example (again using [countrypops](data.countrypops.md#great_tables.data.countrypops)) where we generate a table providing populations every five years for the Benelux countries (`"BEL"`, `"NLD"`, and `"LUX"`). After some filtering and a pivot, the [fmt_flag()](GT.fmt_flag.md#great_tables.GT.fmt_flag) method is used to obtain flag icons from 3-letter country codes present in the `country_code_3` column.


``` python
import polars.selectors as cs

countrypops_mini = (
    pl.from_pandas(countrypops)
    .filter(pl.col("country_code_3").is_in(["BEL", "NLD", "LUX"]))
    .filter((pl.col("year") % 10 == 0) & (pl.col("year") >= 1960))
    .pivot("year", index = ["country_code_3", "country_name"], values="population")
)

(
    GT(countrypops_mini)
    .tab_header(title="Populations of the Benelux Countries")
    .tab_spanner(label="Year", columns=cs.numeric())
    .fmt_integer(columns=cs.numeric())
    .fmt_flag(columns="country_code_3")
    .cols_label(
        country_code_3="",
        country_name="Country"
    )
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="9" class="gt_heading gt_title gt_font_normal">Populations of the Benelux Countries</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="country_code_3" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th rowspan="2" id="country_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Country</th>
<th colspan="7" id="Year" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Year</th>
</tr>
<tr class="gt_col_headings">
<th id="1960" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1960</th>
<th id="1970" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1970</th>
<th id="1980" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1980</th>
<th id="1990" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1990</th>
<th id="2000" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2000</th>
<th id="2010" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2010</th>
<th id="2020" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2020</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QmVsZ2l1bTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iIzMzMyIgZD0iTTAgMGgxNjdsMzguMiAyNTIuNkwxNjcgNTEySDB6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0zNDUgMGgxNjd2NTEySDM0NWwtMzYuNy0yNTZ6IiAvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Ik0xNjcgMGgxNzh2NTEySDE2N3oiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left">Belgium</td>
<td class="gt_row gt_right">9,153,489</td>
<td class="gt_row gt_right">9,655,549</td>
<td class="gt_row gt_right">9,859,242</td>
<td class="gt_row gt_right">9,967,379</td>
<td class="gt_row gt_right">10,251,250</td>
<td class="gt_row gt_right">10,895,586</td>
<td class="gt_row gt_right">11,538,604</td>
</tr>
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+THV4ZW1ib3VyZzwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0ibTAgMTY3IDI1My44LTE5LjNMNTEyIDE2N3YxNzhsLTI1NC45IDMyLjNMMCAzNDV6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48cGF0aCBmaWxsPSIjMzM4YWYzIiBkPSJNMCAzNDVoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+" /></span></td>
<td class="gt_row gt_left">Luxembourg</td>
<td class="gt_row gt_right">313,970</td>
<td class="gt_row gt_right">339,171</td>
<td class="gt_row gt_right">364,150</td>
<td class="gt_row gt_right">381,850</td>
<td class="gt_row gt_right">436,300</td>
<td class="gt_row gt_right">506,953</td>
<td class="gt_row gt_right">630,419</td>
</tr>
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+TmV0aGVybGFuZHM8L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Im0wIDE2NyAyNTMuOC0xOS4zTDUxMiAxNjd2MTc4bC0yNTQuOSAzMi4zTDAgMzQ1eiIgLz48cGF0aCBmaWxsPSIjYTIwMDFkIiBkPSJNMCAwaDUxMnYxNjdIMHoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTAgMzQ1aDUxMnYxNjdIMHoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left">Netherlands</td>
<td class="gt_row gt_right">11,486,631</td>
<td class="gt_row gt_right">13,038,526</td>
<td class="gt_row gt_right">14,149,800</td>
<td class="gt_row gt_right">14,951,510</td>
<td class="gt_row gt_right">15,925,513</td>
<td class="gt_row gt_right">16,615,394</td>
<td class="gt_row gt_right">17,441,500</td>
</tr>
</tbody>
</table>
