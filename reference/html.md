# html()

Interpret input text as HTML-formatted text.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_helpers.py#L297-L314)

``` python
html(text)
```

For certain pieces of text (like in column labels or table headings) we may want to express them as raw HTML. In fact, with HTML, anything goes so it can be much more than just text. The [html()](../reference/html.md#great_tables.md) function will guard the input HTML against escaping, so, your HTML tags will come through as HTML when rendered.

## Parameters

`text: str`  
The text that is understood to contain HTML formatting.

## Examples

See [`GT.tab_header()`](../reference/GT.tab_header.md#great_tables.GT.tab_header).
