## style.fill


A style specification for the background fill of targeted cells.


Usage

``` python
style.fill()
```


The [style.fill()](style.fill.md#great_tables.style.fill) class is to be used with the [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) method, which itself allows for the setting of custom styles to one or more cells. Specifically, the call to [style.fill()](style.fill.md#great_tables.style.fill) should be bound to the `styles` argument of [tab_style()](GT.tab_style.md#great_tables.GT.tab_style).


## Parameters


`color: str | ColumnExpr`  
The color to use for the cell background fill. This can be any valid CSS color value, such as a hex code, a named color, or an RGB value.


## Returns


`CellStyleFill`  
A CellStyleFill object, which is used for a `styles` argument if specifying a cell fill value.


## Examples

See <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>GT.tab_style()</code></a>.
