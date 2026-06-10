## GT.opt_footnote_marks()


Option to modify the set of footnote marks.


Usage

``` python
GT.opt_footnote_marks(marks="numbers")
```


Alter the footnote marks for any footnotes that may be present in the table. Either a list of marks can be provided (including Unicode characters), or, a specific keyword could be used to signify a preset sequence. This method serves as a shortcut for using `tab_options(footnotes_marks=<marks>)`

We can supply a list of strings will represent the series of marks. The series of footnote marks is recycled when its usage goes beyond the length of the set. At each cycle, the marks are simply doubled, tripled, and so on (e.g., `*` -\> `**` -\> `***`). The option exists for providing keywords for certain types of footnote marks. The keywords are

- `"numbers"`: numeric marks, they begin from 1 and these marks are not subject to recycling behavior
- `"letters"`: lowercase alphabetic marks. Same as using the `gt.letters()` function which produces a list of 26 lowercase letters from the Roman alphabet
- `"LETTERS"`: uppercase alphabetic marks. Same as using the `gt.LETTERS()` function which produces a list of 26 uppercase letters from the Roman alphabet
- `"standard"`: symbolic marks, four symbols in total
- `"extended"`: symbolic marks, extends the standard set by adding two more symbols, making six


## Parameters


`marks: str | list[str] = ``"numbers"`  
Either a list of strings that will represent the series of marks or a keyword string that represents a preset sequence of marks. The valid keywords are: `"numbers"` (for numeric marks), `"letters"` and `"LETTERS"` (for lowercase and uppercase alphabetic marks), `"standard"` (for a traditional set of four symbol marks), and `"extended"` (which adds two more symbols to the standard set).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.
