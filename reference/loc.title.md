# loc.title

Target the table title.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_locations.py#L135-L173)

``` python
loc.title()
```

With [loc.title()](../reference/loc.title.md#great_tables.loc.title), we can target the part of table containing the title (within the table header). This is useful for applying custom styling with the [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style) method. That method has a `locations=` argument and this class should be used there to perform the targeting.

## Returns

`LocTitle`  
A LocTitle object, which is used for a `locations=` argument if specifying the title of the table.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style only the 'title' part of the table header (leaving the 'subtitle' part unaffected). This can be done by using `locations=loc.title()` within [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style).

``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(gtcars[["mfr", "model", "msrp"]].head(5))
    .tab_header(
        title="Select Cars from the gtcars Dataset",
        subtitle="Only the first five cars are displayed"
    )
    .tab_style(
        style=style.text(color="blue", size="large", weight="bold"),
        locations=loc.title()
    )
    .fmt_currency(columns="msrp", decimals=0)
)
```

| Select Cars from the gtcars Dataset    |              |           |
|----------------------------------------|--------------|-----------|
| Only the first five cars are displayed |              |           |
| mfr                                    | model        | msrp      |
| Ford                                   | GT           | \$447,000 |
| Ferrari                                | 458 Speciale | \$291,744 |
| Ferrari                                | 458 Spider   | \$263,553 |
| Ferrari                                | 458 Italia   | \$233,509 |
| Ferrari                                | 488 GTB      | \$245,400 |
