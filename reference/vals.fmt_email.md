# vals.fmt_email()


Format values as email links.


Usage

``` python
vals.fmt_email(
    x,
    display_name=None,
    as_button=False,
    color="auto",
    show_underline="auto",
    button_fill="auto",
    button_width=None,
    button_outline=None,
    target="_blank",
)
```


The `val_fmt_email()` function lets you format string values as clickable `mailto:` links. This is the standalone version of [GT.fmt_email()](GT.fmt_email.md#great_tables.GT.fmt_email).


## Parameters


`x: X`  
A list of email address strings (or a single string) to be formatted.

`display_name: str | Callable[[str], str] | None = None`  
An optional display name for the link. Can be a string or a callable.

`as_button: bool = ``False`  
Should the link be styled as a button? By default this is `False`.

`color: str = ``"auto"`  
The color of the link text.

`show_underline: str | bool = ``"auto"`  
Should the link be underlined?

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
