# md()

Interpret input text as Markdown-formatted text.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_helpers.py#L278-L294)

``` python
md(text)
```

Markdown can be used in certain places (e.g., source notes, table title/subtitle, etc.) and we can expect it to render to HTML. There is also the [`html()`](../reference/html.md#great_tables.md) helper function that allows you to use raw HTML text.

## Parameters

`text: str`  
The text that is understood to contain Markdown formatting.

## Examples

See [`GT.tab_header()`](../reference/GT.tab_header.md#great_tables.GT.tab_header).
