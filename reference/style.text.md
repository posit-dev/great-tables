## style.text


A style specification for cell text.


Usage

``` python
style.text()
```


The [style.text()](style.text.md#great_tables.style.text) class is to be used with the [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) method, which itself allows for the setting of custom styles to one or more cells. With it, you can specify the color of the text, the font family, the font size, and the horizontal and vertical alignment of the text and more.


## Parameters


`color: str | ColumnExpr | None = None`  
The text color can be modified through the [color](style.text.md#great_tables.style.text.color) argument.

`font: str | ColumnExpr | GoogleFont | None = None`  
The font or collection of fonts (subsequent font names are) used as fallbacks.

`size: str | ColumnExpr | None = None`  
The size of the font. Can be provided as a number that is assumed to represent `px` values (or could be wrapped in the `px()` helper function). We can also use one of the following absolute size keywords: `"xx-small"`, `"x-small"`, `"small"`, `"medium"`, `"large"`, `"x-large"`, or `"xx-large"`.

`align: Literal[``"center", `<span class="st">`"left"``, ``"right"``, ``"justify"``] | ColumnExpr | None`</span>` = None`  
The text in a cell can be horizontally aligned though one of the following options: `"center"`, `"left"`, `"right"`, or `"justify"`.

`v_align: Literal[``"middle", `<span class="st">`"top"``, ``"bottom"``] | ColumnExpr | None`</span>` = None`  
The vertical alignment of the text in the cell can be modified through the options `"middle"`, `"top"`, or `"bottom"`.

`style: Literal[``"normal", `<span class="st">`"italic"``, ``"oblique"``] | ColumnExpr | None`</span>` = None`  
Can be one of either `"normal"`, `"italic"`, or `"oblique"`.

`weight: Literal[``"normal", `<span class="st">`"bold"``, ``"bolder"``, ``"lighter"``] | ColumnExpr | None`</span>` = None`  
The weight of the font can be modified thorough a text-based option such as `"normal"`, `"bold"`, `"lighter"`, `"bolder"`, or, a numeric value between `1` and `1000`, inclusive. Note that only variable fonts may support the numeric mapping of weight.

`stretch: (`  
`    Literal[`  
`        `<span class="st">`"normal",`  
`        ``"condensed"``,`  
`        ``"ultra-condensed"``,`  
`        ``"extra-condensed"``,`  
`        ``"semi-condensed"``,`  
`        ``"semi-expanded"``,`  
`        ``"expanded"``,`  
`        ``"extra-expanded"``,`  
`        ``"ultra-expanded"``,`  
`    ]`  
`    | ColumnExpr`  
`    | None`  
`)`  
</span>` = None`  
Allows for text to either be condensed or expanded. We can use one of the following text-based keywords to describe the degree of condensation/expansion: `"ultra-condensed"`, `"extra-condensed"`, `"condensed"`, `"semi-condensed"`, `"normal"`, `"semi-expanded"`, `"expanded"`, `"extra-expanded"`, or `"ultra-expanded"`. Alternatively, we can supply percentage values from `0%` to `200%`, inclusive. Negative percentage values are not allowed.

`decorate: (`  
`    Literal[``"overline", `<span class="st">`"line-through"``, ``"underline"``, ``"underline overline"``]`  
`    | ColumnExpr`  
`    | None`  
`)`  
</span>` = None`  
Allows for text decoration effect to be applied. Here, we can use `"overline"`, `"line-through"`, or `"underline"`.

`transform: Literal[``"uppercase", `<span class="st">`"lowercase"``, ``"capitalize"``] | ColumnExpr | None`</span>` = None`  
Allows for the transformation of text. Options are `"uppercase"`, `"lowercase"`, or `"capitalize"`.

`whitespace: (`  
`    Literal[``"normal", `<span class="st">`"nowrap"``, ``"pre"``, ``"pre-wrap"``, ``"pre-line"``, ``"break-spaces"``]`  
`    | ColumnExpr`  
`    | None`  
`)`  
</span>` = None`  
A white-space preservation option. By default, runs of white-space will be collapsed into single spaces but several options exist to govern how white-space is collapsed and how lines might wrap at soft-wrap opportunities. The options are `"normal"`, `"nowrap"`, `"pre"`, `"pre-wrap"`, `"pre-line"`, and `"break-spaces"`.


## Returns


`CellStyleText`  
A CellStyleText object, which is used for a `styles` argument if specifying any cell text properties.


## Examples

See <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>GT.tab_style()</code></a>.
