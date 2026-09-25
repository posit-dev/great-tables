# vals.fmt_index()


Format values as index characters.


Usage

``` python
vals.fmt_index(
    x,
    case="upper",
    index_algo="repeat",
    pattern="{x}",
    locale=None,
)
```


With numeric values in a list, we can transform those to index values based on letters. The value `1` maps to `"A"`, `2` to `"B"`, and so on through the alphabet. When values exceed 26, the `index_algo` parameter controls how additional characters are generated.


## Parameters


`x: X`  
A list of numeric values to be formatted as index characters.

`case: str = ``"upper"`  
The case of the resulting characters. `"upper"` (default) or `"lower"`.

`index_algo: str = ``"repeat"`  
The algorithm for values exceeding the character set size. `"repeat"` (default) repeats characters whereas `"excel"` uses Excel-style column naming.

`pattern: str = ``"{x}"`  
A formatting pattern; `{x}` is the formatted value placeholder.

`locale: str | None = None`  
An optional locale ID. Currently reserved for future use.


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_index([1, 2, 3, 26, 27])
```


    ['A', 'B', 'C', 'Z', 'AA']
