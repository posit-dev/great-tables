## vals.fmt_roman()


Format values as Roman numerals.


Usage

``` python
vals.fmt_roman(
    x,
    case="upper",
    pattern="{x}",
)
```


With numeric values we can transform those to Roman numerals, rounding values as necessary.


## Parameters


`x: X`  
A list of values to be formatted.

`case: str = ``"upper"`  
Should Roman numerals should be rendered as uppercase (`"upper"`) or lowercase (`"lower"`) letters? By default, this is set to `"upper"`.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_roman([3, 5])
```


    ['III', 'V']
