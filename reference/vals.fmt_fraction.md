# vals.fmt_fraction()


Format values as mixed fractions.


Usage

``` python
vals.fmt_fraction(
    x,
    accuracy="low",
    simplify=True,
    layout="inline",
    use_seps=True,
    pattern="{x}",
    sep_mark=",",
    locale=None,
)
```


With numeric values we can perform mixed-fraction-based formatting. The `accuracy` parameter controls the type of fractions generated: use a keyword (`"low"`, `"med"`, `"high"`) to get denominators of up to 1, 2, or 3 digits, or supply a positive integer to fix the denominator (e.g., `2` for halves, `4` for quarters).


## Parameters


`x: X`  
A list of values to be formatted.

`accuracy: str | int = ``"low"`  
The accuracy of the fraction. Use `"low"` for denominators up to 1 digit (e.g., halves, thirds, quarters, etc.), `"med"` for up to 2-digit denominators, `"high"` for up to 3-digit denominators, or a positive integer for a fixed denominator. The default is `"low"`.

`simplify: bool = ``True`  
When `accuracy` is an integer, should the fraction be simplified via GCD reduction? For example, with `accuracy=4` and a value of `0.5`, `simplify=True` yields `"1/2"` while `simplify=False` yields `"2/4"`. The default is `True`.

`layout: str = ``"inline"`  
`"inline"` for baseline fractions with a standard slash (e.g., `3/4`), `"diagonal"` for raised/lowered numerals with a fraction slash character (HTML only). The default is `"inline"`.

`use_seps: bool = ``True`  
Whether to use digit grouping separators in the whole-number part. The default is `True`.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` and all other characters are interpreted as string literals.

`sep_mark: str = ``","`  
The mark to use as a thousands separator. The default is `","`.

`locale: str | None = None`  
An optional locale ID that can be used for applying a locale-specific thousands separator.


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_fraction([1.5, 0.25, 3.75])
```


    ['1 1/2', '1/4', '3 3/4']
