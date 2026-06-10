## style.css


A style specification for custom CSS rules.


Usage

``` python
style.css()
```


The [style.css()](style.css.md#great_tables.style.css) class is to be used with the [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) method, which itself allows for the setting of custom styles to one or more cells. With [style.css()](style.css.md#great_tables.style.css), you can specify any CSS rule that you would like to apply to the targeted cells.


## Parameters


`rule: str`  
The CSS rule to apply to the targeted cells. This can be any valid CSS rule, such as `background-color: red;` or `font-size: 14px;`.


## Returns


`CellStyleCss`  
A CellStyleCss object, which is used for a `styles` argument if specifying a custom CSS rule.


## Examples

See <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>GT.tab_style()</code></a>.
