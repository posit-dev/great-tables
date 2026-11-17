# GTI.i_cols_pin()

Pin columns to a side of the table, so they stay in view as it scrolls sideways.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L1187-L1255)

``` python
GTI.i_cols_pin(
    columns=None,
    side="left",
)
```

A table wider than its container scrolls sideways, with its stub (and the row group column, if row groups are shown as one) pinned to the left, in view. This pins other columns too: to the left, after the stub, or to the right. Pinned columns have to be next to their side of the table (with only other columns pinned there between them and it), so a column further in has to be moved there first, with [`cols_move_to_start()`](../reference/GT.cols_move_to_start.md#great_tables.GT.cols_move_to_start) or [`cols_move_to_end()`](../reference/GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end); this is checked when the table is made, after any moves. Hidden columns don't count. A spanner over columns on both sides of a pinned edge isn't pinned, and neither is the footer.

Pinned columns can't take up more than half of the table's container: in a narrower one, only the stub stays pinned (until the container is wide enough again).

The sides are those of the columns' order: the left is the stub's side, and the right is the other. A table shown right to left (in a page that's written that way) has its stub on the right, and so its columns pinned to the "left" are on the right, by the stub.

Each call pins (or unpins) the columns it's given, so that some columns can be pinned to one side, and others to the other; a later call for a column replaces what an earlier one set.

## Parameters

`columns: SelectExpr = None`  
The columns to pin: a column name, a list of them, or a selector (e.g., Polars' `cs.numeric()`). With `None` (the default), every column but the stub. The stub and the row group column are always pinned (naming them does nothing).

`side: PinSide | None = "left"`  
The side to pin the columns to: `"left"` (the stub's) or `"right"`. With `None`, the columns are unpinned.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a wide table of Ontario's municipalities that keeps each one's status in view, by its name, and its latest population at the other side.

``` python
from great_tables import GTI
from great_tables.data import towny

(
    GTI(towny.drop(columns="website").head(10), rowname_col="name")
    .cols_move_to_end(columns="population_2021")
    .fmt_integer(columns=["population_1996", "population_2021"])
    .i_cols_pin(columns="status")
    .i_cols_pin(columns="population_2021", side="right")
)
```

|  | status | csd_type | census_div | latitude | longitude | land_area_km2 | population_1996 | population_2001 | population_2006 | population_2011 | population_2016 | density_1996 | density_2001 | density_2006 | density_2011 | density_2016 | density_2021 | pop_change_1996_2001_pct | pop_change_2001_2006_pct | pop_change_2006_2011_pct | pop_change_2011_2016_pct | pop_change_2016_2021_pct | population_2021 |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Addington Highlands | lower-tier | township | Lennox and Addington | 45.0 | -77.25 | 1293.99 | 2,429 | 2402 | 2512 | 2517 | 2318 | 1.88 | 1.86 | 1.94 | 1.95 | 1.79 | 1.96 | -0.0111 | 0.0458 | 0.002 | -0.0791 | 0.0932 | 2,534 |
| Adelaide Metcalfe | lower-tier | township | Middlesex | 42.95 | -81.7 | 331.11 | 3,128 | 3149 | 3135 | 3028 | 2990 | 9.45 | 9.51 | 9.47 | 9.14 | 9.03 | 9.09 | 0.0067 | -0.0044 | -0.0341 | -0.0125 | 0.007 | 3,011 |
| Adjala-Tosorontio | lower-tier | township | Simcoe | 44.133333 | -79.933333 | 371.53 | 9,359 | 10082 | 10695 | 10603 | 10975 | 25.19 | 27.14 | 28.79 | 28.54 | 29.54 | 29.58 | 0.0773 | 0.0608 | -0.0086 | 0.0351 | 0.0013 | 10,989 |
| Admaston/Bromley | lower-tier | township | Renfrew | 45.529167 | -76.896944 | 519.59 | 2,837 | 2824 | 2716 | 2844 | 2935 | 5.46 | 5.44 | 5.23 | 5.47 | 5.65 | 5.76 | -0.0046 | -0.0382 | 0.0471 | 0.032 | 0.0204 | 2,995 |
| Ajax | lower-tier | town | Durham | 43.858333 | -79.036389 | 66.64 | 64,430 | 73753 | 90167 | 109600 | 119677 | 966.84 | 1106.74 | 1353.05 | 1644.66 | 1795.87 | 1900.75 | 0.1447 | 0.2226 | 0.2155 | 0.0919 | 0.0584 | 126,666 |
| Alberton | single-tier | township | Rainy River | 48.6 | -93.533333 | 116.6 | 1,027 | 956 | 958 | 864 | 969 | 8.81 | 8.2 | 8.22 | 7.41 | 8.31 | 8.18 | -0.0691 | 0.0021 | -0.0981 | 0.1215 | -0.0155 | 954 |
| Alfred and Plantagenet | lower-tier | township | Prescott and Russell | 45.566667 | -74.916667 | 391.79 | 8,315 | 8593 | 8654 | 9196 | 9680 | 21.22 | 21.93 | 22.09 | 23.47 | 24.71 | 25.39 | 0.0334 | 0.0071 | 0.0626 | 0.0526 | 0.0278 | 9,949 |
| Algonquin Highlands | lower-tier | township | Haliburton | 45.4 | -78.75 | 999.69 | 1,687 | 1827 | 1976 | 2186 | 2351 | 1.69 | 1.83 | 1.98 | 2.19 | 2.35 | 2.59 | 0.083 | 0.0816 | 0.1063 | 0.0755 | 0.1008 | 2,588 |
| Alnwick/Haldimand | lower-tier | township | Northumberland | 44.083333 | -78.033333 | 398.25 | 5,528 | 5846 | 6435 | 6617 | 6869 | 13.88 | 14.68 | 16.16 | 16.62 | 17.25 | 18.76 | 0.0575 | 0.1008 | 0.0283 | 0.0381 | 0.0879 | 7,473 |
| Amaranth | lower-tier | township | Dufferin | 43.983333 | -80.233333 | 265.02 | 3,450 | 3770 | 3845 | 3963 | 4079 | 13.02 | 14.23 | 14.51 | 14.95 | 15.39 | 16.33 | 0.0928 | 0.0199 | 0.0307 | 0.0293 | 0.0608 | 4,327 |
