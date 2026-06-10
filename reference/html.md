## html()


Interpret input text as HTML-formatted text.


Usage

``` python
html(text)
```


For certain pieces of text (like in column labels or table headings) we may want to express them as raw HTML. In fact, with HTML, anything goes so it can be much more than just text. The [html()](html.md#great_tables.html) function will guard the input HTML against escaping, so, your HTML tags will come through as HTML when rendered.


## Parameters


`text: str`  
The text that is understood to contain HTML formatting.


## Examples

See <a href="GT.tab_header.html#great_tables.GT.tab_header" class="gdls-link"><code>GT.tab_header()</code></a>.
