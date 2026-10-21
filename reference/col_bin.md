# col_bin()

Create a color-mapping function for numeric values cut into bins.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_data_color/col_fns.py#L225-L351)

``` python
col_bin(
    palette=None,
    domain=None,
    bins=7,
    na_color=None,
    right=False,
    reverse=False,
    truncate=False,
)
```

The [col_bin()](../reference/col_bin.md#great_tables.col_bin) helper returns a function that divides numeric values into bins and gives every value in a bin the same color. The bin colors are spaced evenly along the palette. The returned function is designed to be passed to the `fn=` argument of [`data_color()`](../reference/GT.data_color.md#great_tables.GT.data_color), but it can be called on any list of values.

## Parameters

`palette: str | list[str] | None = None`  
The colors to use. This can be a list of colors (as hexadecimal values or color names) or the name of a ColorBrewer or viridis palette (see [`data_color()`](../reference/GT.data_color.md#great_tables.GT.data_color) for the available names). If `None`, then a default palette will be used.

`domain: list[int] | list[float] | None = None`  
The range of values to divide into bins, given as `[min, max]`. This is only used when `bins=` is an integer. If `None`, then the domain is taken from the range of the (non-missing) values supplied to the returned function each time it is called.

`bins: int | list[int] | list[float] = 7`  
Either the number of equal-width bins to cut the domain into, or a list of two or more bin boundaries (e.g., `[0, 10, 50, 100]`). Values outside of the outermost boundaries receive the missing-value color (unless `truncate=True`).

`na_color: str | None = None`  
The color to use for missing values and values outside of the bins. If `None`, then the returned function gives `None` for those values, which lets [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) apply its own `na_color=` color.

`right: bool = False`  
Should the bins be closed on the right (and open on the left)? By default, bins include their lower boundary but not their upper one (the last bin includes both). With `right=True`, bins include their upper boundary but not their lower one (the first bin includes both).

`reverse: bool = False`  
Should the order of the palette colors be reversed?

`truncate: bool = False`  
If `True`, then values below the lowest boundary are placed in the first bin and values above the highest boundary are placed in the last bin. If `False` (the default), then they receive the missing-value color.

## Returns

`Callable[[list[Any]], list[str | None]]`  
A function that takes a list of numeric values and returns a list of hexadecimal colors.

## Examples

Let's color the `currency` column of the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset in three bins with explicit boundaries:

``` python
from great_tables import GT, col_bin
from great_tables.data import exibble

GT(exibble[["currency", "char"]]).data_color(
    columns="currency",
    fn=col_bin(palette="Blues", bins=[0, 10, 1000, 100000]),
    na_color="lightgray",
)
```

| currency | char       |
|----------|------------|
| 49.95    | apricot    |
| 17.95    | banana     |
| 1.39     | coconut    |
| 65100.0  | durian     |
| 1325.81  | None       |
| 13.255   | fig        |
| None     | grapefruit |
| 0.44     | honeydew   |
