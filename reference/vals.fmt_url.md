# vals.fmt_url()


Format values as URL links.


Usage

``` python
vals.fmt_url(
    x,
    label=None,
    as_button=False,
    color="auto",
    show_underline="auto",
    button_fill="auto",
    button_width=None,
    button_outline=None,
    target="_blank",
)
```


The `val_fmt_url()` function lets you format string values as clickable URL links. This is the standalone version of [GT.fmt_url()](GT.fmt_url.md#great_tables.GT.fmt_url).


## Parameters


`x: X`  
A list of URL strings (or a single URL string) to be formatted.

`label: str | Callable[[str], str] | None = None`  
An optional label for the link. Can be a string or a callable.

`as_button: bool = ``False`  
Should the link be styled as a button? By default this is `False`.

`color: str = ``"auto"`  
The color of the link text. The default `"auto"` uses dark cyan for links and white for buttons.

`show_underline: str | bool = ``"auto"`  
Should the link be underlined? The default `"auto"` enables underlines for links and disables them for buttons.

`button_fill: str = ``"auto"`  
The background color for button-style links.

`button_width: str | None = None`  
The width of the button as a CSS width string.

`button_outline: str | None = None`  
The CSS outline for the button.

`target: str | None = ``"_blank"`  
The `target` attribute for the anchor element.


## Returns


`list[str]`  
A list of formatted values is returned.
