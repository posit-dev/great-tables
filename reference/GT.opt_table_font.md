## GT.opt_table_font()


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

`weight: str | int | float | None = None`  
Option to set the weight of the font. Can be a text-based keyword such as `"normal"`, `"bold"`, `"lighter"`, `"bolder"`, or, a numeric value between `1` and `1000`. Please note that typefaces have varying support for the numeric mapping of weight.

`add: bool = ``True`  
Should fonts be added to the beginning of any already-defined fonts for the table? By default, this is `True` and is recommended since those fonts already present can serve as fallbacks when everything specified in [font](style.text.md#great_tables.style.text.font) is not available. If a `stack=` value is provided, then `add` will automatically set to `False`.


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
