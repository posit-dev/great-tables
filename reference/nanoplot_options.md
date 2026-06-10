## nanoplot_options()


Helper for setting the options for a nanoplot.


Usage

``` python
nanoplot_options(
    data_point_radius=None,
    data_point_stroke_color=None,
    data_point_stroke_width=None,
    data_point_fill_color=None,
    data_line_type=None,
    data_line_stroke_color=None,
    data_line_stroke_width=None,
    data_area_fill_color=None,
    data_bar_stroke_color=None,
    data_bar_stroke_width=None,
    data_bar_fill_color=None,
    data_bar_negative_stroke_color=None,
    data_bar_negative_stroke_width=None,
    data_bar_negative_fill_color=None,
    reference_line_color=None,
    reference_area_fill_color=None,
    vertical_guide_stroke_color=None,
    vertical_guide_stroke_width=None,
    show_data_points=None,
    show_data_line=None,
    show_data_area=None,
    show_reference_line=None,
    show_reference_area=None,
    show_vertical_guides=None,
    show_y_axis_guide=None,
    interactive_data_values=None,
    y_val_fmt_fn=None,
    y_axis_fmt_fn=None,
    y_ref_line_fmt_fn=None,
    currency=None
)
```


When using `cols_nanoplot()`, the defaults for the generated nanoplots can be modified with [nanoplot_options()](nanoplot_options.md#great_tables.nanoplot_options) within the `options=` argument.


## Parameters


`data_point_radius: int | list[int] | None = None`  
The `data_point_radius=` option lets you set the radius for each of the data points. By default this is set to `10`. Individual radius values can be set by using a list of numeric values; however, the list provided must match the number of data points.

`data_point_stroke_color: str | list[str] | None = None`  
The default stroke color of the data points is `"#FFFFFF"` (`"white"`). This works well when there is a visible data line combined with data points with a darker fill color. The stroke color can be modified with `data_point_stroke_color=` for all data points by supplying a single color value. With a list of colors, each data point's stroke color can be changed (ensure that the list length matches the number of data points).

`data_point_stroke_width: int | list[int] | None = None`  
The width of the outside stroke for the data points can be modified with the `data_point_stroke_width=` option. By default, a value of `4` (as in '4px') is used.

`data_point_fill_color: str | list[str] | None = None`  
By default, all data points have a fill color of `"#FF0000"` (`"red"`). This can be changed for all data points by providing a different color to `data_point_fill_color=`. And, a list of different colors can be supplied so long as the length is equal to the number of data points; the fill color values will be applied in order of left to right.

`data_line_type: str | None = None`  
This can accept either `"curved"` or `"straight"`. Curved lines are recommended when the nanoplot has less than 30 points and data points are evenly spaced. In most other cases, straight lines might present better.

`data_line_stroke_color: str | None = None`  
The color of the data line can be modified from its default `"#4682B4"` (`"steelblue"`) color by supplying a color to the `data_line_stroke_color=` option.

`data_line_stroke_width: int | None = None`  
The width of the connecting data line can be modified with `data_line_stroke_width=`. By default, a value of `4` (as in '4px') is used.

`data_area_fill_color: str | None = None`  
The fill color for the area that bounds the data points in line plot. The default is `"#FF0000"` (`"red"`) but can be changed by providing a color value to `data_area_fill_color=`.

`data_bar_stroke_color: str | list[str] | None = None`  
The color of the stroke used for the data bars can be modified from its default `"#3290CC"` color by supplying a color to `data_bar_stroke_color=`.

`data_bar_stroke_width: int | list[int] | None = None`  
The width of the stroke used for the data bars can be modified with the `data_bar_stroke_width=` option. By default, a value of `4` (as in '4px') is used.

`data_bar_fill_color: str | list[str] | None = None`  
By default, all data bars have a fill color of `"#3FB5FF"`. This can be changed for all data bars by providing a different color to `data_bar_fill_color=`. And, a list of different colors can be supplied so long as the length is equal to the number of data bars; the fill color values will be applied in order of left to right.

`data_bar_negative_stroke_color: str | None = None`  
The color of the stroke used for the data bars that have negative values. The default color is `"#CC3243"` but this can be changed by supplying a color value to the `data_bar_negative_stroke_color=` option.

`data_bar_negative_stroke_width: int | None = None`  
The width of the stroke used for negative value data bars. This has the same default as `data_bar_stroke_width=` with a value of `4` (as in '4px'). This can be changed by giving a numeric value to the `data_bar_negative_stroke_width=` option.

`data_bar_negative_fill_color: str | None = None`  
By default, all negative data bars have a fill color of `"#D75A68"`. This can however be changed by providing a color value to `data_bar_negative_fill_color=`.

`reference_line_color: str | None = None`  
The reference line will have a color of `"#75A8B0"` if it is set to appear. This color can be changed by providing a single color value to `reference_line_color=`.

`reference_area_fill_color: str | None = None`  
If a reference area has been defined and is visible it has by default a fill color of `"#A6E6F2"`. This can be modified by declaring a color value in the `reference_area_fill_color=` option.

`vertical_guide_stroke_color: str | None = None`  
Vertical guides appear when hovering in the vicinity of data points. Their default color is `"#911EB4"` (a strong magenta color) and a fill opacity value of `0.4` is automatically applied to this. However, the base color can be changed with the `vertical_guide_stroke_color=` option.

`vertical_guide_stroke_width: int | None = None`  
The vertical guide's stroke width, by default, is relatively large at `12` (this is '12px'). This is modifiable by setting a different value with `vertical_guide_stroke_width=`.

`show_data_points: bool | None = None`  
By default, all data points in a nanoplot are shown but this layer can be hidden by setting `show_data_points=` to `False`.

`show_data_line: bool | None = None`  
The data line connects data points together and it is shown by default. This data line layer can be hidden by setting `show_data_line=` to `False`.

`show_data_area: bool | None = None`  
The data area layer is adjacent to the data points and the data line. It is shown by default but can be hidden with `show_data_area=False`.

`show_reference_line: bool | None = None`  
The layer with a horizontal reference line appears underneath that of the data points and the data line. Like vertical guides, hovering over a reference will show its value. The reference line (if available) is shown by default but can be hidden by setting `show_reference_line=` to `False`.

`show_reference_area: bool | None = None`  
The reference area appears at the very bottom of the layer stack, if it is available (i.e., defined in `cols_nanoplot()`). It will be shown in the default case but can be hidden by using `show_reference_area=False`.

`show_vertical_guides: bool | None = None`  
Vertical guides appear when hovering over data points. This hidden layer is active by default but can be deactivated by using `show_vertical_guides=False`.

`show_y_axis_guide: bool | None = None`  
The *y*-axis guide will appear when hovering over the far left side of a nanoplot. This hidden layer is active by default but can be deactivated by using `show_y_axis_guide=False`.

`interactive_data_values: bool | None = None`  
By default, numeric data values will be shown only when the user interacts with certain regions of a nanoplot. This is because the values may be numerous (i.e., clutter the display when all are visible) and it can be argued that the values themselves are secondary to the presentation. However, for some types of plots (like horizontal bar plots), a persistent display of values alongside the plot marks may be desirable. By setting `interactive_data_values=False` we can opt for always displaying the data values alongside the plot components.

`y_val_fmt_fn: Callable[…, str] | None = None`  
If providing a function to `y_val_fmt_fn=`, customized formatting of the *y* values associated with the data points/bars is possible.

`y_axis_fmt_fn: Callable[…, str] | None = None`  
A function supplied to `y_axis_fmt_fn=` will result in customized formatting of the *y*-axis label values.

`y_ref_line_fmt_fn: Callable[…, str] | None = None`  
Providing a function for `y_ref_line_fmt_fn=` yields customized formatting of the reference line (if present).

`currency: str | None = None`  
If the values are to be displayed as currency values, supply either: (1) a 3-letter currency code (e.g., `"USD"` for U.S. Dollars, `"EUR"` for the Euro currency), or (2) a common currency name (e.g., `"dollar"`, `"pound"`, `"yen"`, etc.).


## Examples

See <a href="GT.fmt_nanoplot.html#great_tables.GT.fmt_nanoplot" class="gdls-link"><code>fmt_nanoplot()</code></a>.
