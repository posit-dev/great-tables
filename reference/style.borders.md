## style.borders


A style specification for cell borders.


Usage

``` python
style.borders()
```


The `styles.borders()` class is to be used with the [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) method, which itself allows for the setting of custom styles to one or more cells. The [sides](style.borders.md#great_tables.style.borders.sides) argument is where we define which borders should be modified (e.g., `"left"`, `"right"`, etc.). With that selection, the [color](style.text.md#great_tables.style.text.color), [style](style.text.md#great_tables.style.text.style), and [weight](style.text.md#great_tables.style.text.weight) of the selected borders can then be modified.


## Parameters


`sides: (`  
`    Literal[``"all", `<span class="st">`"top"``, ``"bottom"``, ``"left"``, ``"right"``]`  
`    | list[Literal[``"all"``, ``"top"``, ``"bottom"``, ``"left"``, ``"right"``]]`  
`)`  
</span>` = ``"all"`  
The border sides to be modified. Options include `"left"`, `"right"`, `"top"`, and `"bottom"`. For all borders surrounding the selected cells, we can use the `"all"` option.

`color: str | ColumnExpr = ``"#000000"`  
The border [color](style.text.md#great_tables.style.text.color) can be defined with any valid CSS color value, such as a hex code, a named color, or an RGB value. The default [color](style.text.md#great_tables.style.text.color) value is `"#000000"` (black).

`style: str | ColumnExpr = ``"solid"`  
The border [style](style.text.md#great_tables.style.text.style) can be one of either `"solid"` (the default), `"dashed"`, `"dotted"`, `"hidden"`, or `"double"`.

`weight: str | ColumnExpr = ``"1px"`  
The default value for [weight](style.text.md#great_tables.style.text.weight) is `"1px"` and higher values will become more visually prominent.


## Returns


`CellStyleBorders`  
A CellStyleBorders object, which is used for a `styles` argument if specifying cell borders.


## Examples

See <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>GT.tab_style()</code></a>.
