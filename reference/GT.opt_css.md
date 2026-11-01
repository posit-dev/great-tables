# GT.opt_css()

Option to add custom CSS for the table.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L1727-L1817)

``` python
GT.opt_css(
    css,
    add=True,
    allow_duplicates=False,
)
```

[opt_css()](../reference/GT.opt_css.md#great_tables.GT.opt_css) makes it possible to add extra CSS rules to a table. This CSS will be added after the compiled CSS that Great Tables generates automatically when the object is transformed to an HTML output table.

If you want to set CSS styles on a specific table location, use [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) with [style.css()](../reference/style.css.md#great_tables.style.css) instead.

## Parameters

`css: str`  
The CSS to include as part of the rendered table's `<style>` element.

`add: bool = True`  
If `True`, the default, the CSS is added to any already-defined CSS (typically from previous calls of [opt_css()](../reference/GT.opt_css.md#great_tables.GT.opt_css) or `tab_options(table_additional_css=...)`). If this is set to `False`, the CSS provided here will replace any previously-stored CSS.

`allow_duplicates: bool = False`  
When this is `False` (the default), the CSS provided here won't be added (provided that `add=True`) if it is seen in the already-defined CSS.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's use the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `num` and `currency` columns). Through use of the [opt_css()](../reference/GT.opt_css.md#great_tables.GT.opt_css) method, we can insert CSS rulesets as a string. We need to ensure that the table ID is set explicitly (we've done so here with the ID value of `"one"`, setting it up with `GT(id=)`).

``` python
from great_tables import GT, exibble
import polars as pl

exibble_mini = pl.from_pandas(exibble).select(["num", "currency"])

(
    GT(exibble_mini, id="one")
    .fmt_currency(columns="currency", currency="HKD")
    .fmt_scientific(columns="num")
    .opt_css(
        css='''
        #one .gt_table {
          background-color: skyblue;
        }
        #one .gt_row {
          padding: 20px 30px;
        }
        #one .gt_col_heading {
          text-align: center !important;
        }
        '''
    )
)
```

| num         | currency      |
|-------------|---------------|
| 1.11 × 10⁻¹ | HK\$49.95     |
| 2.22        | HK\$17.95     |
| 3.33 × 10¹  | HK\$1.39      |
| 4.44 × 10²  | HK\$65,100.00 |
| 5.55 × 10³  | HK\$1,325.81  |
| None        | HK\$13.26     |
| 7.77 × 10⁵  | None          |
| 8.88 × 10⁶  | HK\$0.44      |
