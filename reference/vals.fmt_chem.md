# vals.fmt_chem()


Format chemical formulas.


Usage

``` python
vals.fmt_chem(x)
```


With string values in a list, we can transform chemical formula notation into properly typeset HTML with subscripted numbers, superscripted charges, reaction arrows, and more. The input text should conform to the chemistry notation described in `fmt_chem()`.


## Parameters


`x: X`  
A list of string values to be formatted as chemical formulas.


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_chem(["C6H12O6", "H2O", "CH4 + 2 O2 -> CO2 + 2 H2O"])
```


    ['C<span style="white-space:nowrap;"><sub style="line-height:0;">6</sub></span>H<span style="white-space:nowrap;"><sub style="line-height:0;">12</sub></span>O<span style="white-space:nowrap;"><sub style="line-height:0;">6</sub></span>',
     'H<span style="white-space:nowrap;"><sub style="line-height:0;">2</sub></span>O',
     'CH<span style="white-space:nowrap;"><sub style="line-height:0;">4</sub></span> + 2 O<span style="white-space:nowrap;"><sub style="line-height:0;">2</sub></span> → CO<span style="white-space:nowrap;"><sub style="line-height:0;">2</sub></span> + 2 H<span style="white-space:nowrap;"><sub style="line-height:0;">2</sub></span>O']
