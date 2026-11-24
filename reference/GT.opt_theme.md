# GT.opt_theme()

Apply a theme to the table and choose its color mode.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_theme.py#L443-L516)

``` python
GT.opt_theme(
    theme=None,
    mode=None,
)
```

The [opt_theme()](../reference/GT.opt_theme.md#great_tables.GT.opt_theme) method stores a [Theme](../reference/Theme.md#great_tables.Theme) and a color mode on the table. The theme gives the table its colors, fonts and other options, and can hold a separate set of colors for dark mode through its `dark=` argument. The mode picks which colors are used: `"light"` always uses the light colors, `"dark"` always uses the dark colors, and `"auto"` (the default) follows the color scheme of the page the table is shown in.

## Parameters

`theme: Theme | Literal[False] | None = None`  
The [Theme](../reference/Theme.md#great_tables.Theme) to apply. If `None`, the theme already on the table is left as it is, and if `False`, it is removed (the mode stays as it is unless `mode=` is given).

`mode: ThemeMode | None = None`  
The color mode, one of `"auto"`, `"light"` or `"dark"`. If `None`, the mode already on the table is left as it is. An `"auto"` table stays light when a background color is set for light mode only (with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options), [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize), or a theme option with no value in the theme's `dark=`).

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using select columns from the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset, let's create a table and choose its color mode with [opt_theme()](../reference/GT.opt_theme.md#great_tables.GT.opt_theme).

``` python
from great_tables import GT, Theme, data

gt_tbl = GT(data.pl.exibble.select("num", "char", "currency", "row"), rowname_col="row")

gt_tbl.opt_theme(mode="dark")
```

|       | num       | char       | currency |
|-------|-----------|------------|----------|
| row_1 | 0.1111    | apricot    | 49.95    |
| row_2 | 2.222     | banana     | 17.95    |
| row_3 | 33.33     | coconut    | 1.39     |
| row_4 | 444.4     | durian     | 65100.0  |
| row_5 | 5550.0    | None       | 1325.81  |
| row_6 | None      | fig        | 13.255   |
| row_7 | 777000.0  | grapefruit | None     |
| row_8 | 8880000.0 | honeydew   | 0.44     |

A custom [Theme](../reference/Theme.md#great_tables.Theme) sets the tokens and options that should differ from the defaults.

``` python
gt_tbl.opt_theme(Theme(border="#9AA5B1", font="Georgia", data_row_padding=4))
```

|       | num       | char       | currency |
|-------|-----------|------------|----------|
| row_1 | 0.1111    | apricot    | 49.95    |
| row_2 | 2.222     | banana     | 17.95    |
| row_3 | 33.33     | coconut    | 1.39     |
| row_4 | 444.4     | durian     | 65100.0  |
| row_5 | 5550.0    | None       | 1325.81  |
| row_6 | None      | fig        | 13.255   |
| row_7 | 777000.0  | grapefruit | None     |
| row_8 | 8880000.0 | honeydew   | 0.44     |

Use the `dark=` argument of [Theme](../reference/Theme.md#great_tables.Theme) to give the table its own colors in dark mode.

``` python
gt_tbl.opt_theme(
    Theme(border="#9AA5B1", dark=Theme(background="#101418", border="#2A3038")),
    mode="dark",
)
```

|       | num       | char       | currency |
|-------|-----------|------------|----------|
| row_1 | 0.1111    | apricot    | 49.95    |
| row_2 | 2.222     | banana     | 17.95    |
| row_3 | 33.33     | coconut    | 1.39     |
| row_4 | 444.4     | durian     | 65100.0  |
| row_5 | 5550.0    | None       | 1325.81  |
| row_6 | None      | fig        | 13.255   |
| row_7 | 777000.0  | grapefruit | None     |
| row_8 | 8880000.0 | honeydew   | 0.44     |
