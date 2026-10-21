# col_factor()

Create a color-mapping function for categorical values.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_data_color/col_fns.py#L354-L443)

``` python
col_factor(
    palette=None,
    domain=None,
    na_color=None,
    reverse=False,
)
```

The [col_factor()](../reference/col_factor.md#great_tables.col_factor) helper returns a function that gives each distinct value (or level) its own color. If the palette has at least as many colors as there are levels, then the levels take the palette colors in order; otherwise, colors are interpolated along the palette. The returned function is designed to be passed to the `fn=` argument of [`data_color()`](../reference/GT.data_color.md#great_tables.GT.data_color), but it can be called on any list of values.

## Parameters

`palette: str | list[str] | None = None`  
The colors to use. This can be a list of colors (as hexadecimal values or color names) or the name of a ColorBrewer or viridis palette (see [`data_color()`](../reference/GT.data_color.md#great_tables.GT.data_color) for the available names). If `None`, then a default palette will be used.

`domain: list[Any] | None = None`  
The levels to map to colors, in order. Values that aren't in the domain receive the missing-value color. If `None`, then the levels are the distinct (non-missing) values supplied to the returned function each time it is called, in their order of appearance.

`na_color: str | None = None`  
The color to use for missing values and values not in the domain. If `None`, then the returned function gives `None` for those values, which lets [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) apply its own `na_color=` color.

`reverse: bool = False`  
Should the order of the palette colors be reversed?

## Returns

`Callable[[list[Any]], list[str | None]]`  
A function that takes a list of values and returns a list of hexadecimal colors.

## Examples

Setting the `domain=` fixes the color of each level, no matter which levels are present in the column or in what order they appear:

``` python
import pandas as pd
from great_tables import GT, col_factor

df = pd.DataFrame(
    {
        "ticket": [101, 102, 103, 104, 105],
        "priority": ["low", "high", "medium", "high", "urgent"],
    }
)

GT(df).data_color(
    columns="priority",
    fn=col_factor(
        palette=["#FEF0D9", "#FDCC8A", "#FC8D59"],
        domain=["low", "medium", "high"],
        na_color="#D7301F",
    ),
)
```

| ticket | priority |
|--------|----------|
| 101    | low      |
| 102    | high     |
| 103    | medium   |
| 104    | high     |
| 105    | urgent   |
