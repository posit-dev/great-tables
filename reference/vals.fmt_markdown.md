## vals.fmt_markdown()


Format Markdown text.


Usage

``` python
vals.fmt_markdown(x)
```


Any Markdown-formatted text can be transformed to HTML when using the [fmt_markdown()](GT.fmt_markdown.md#great_tables.GT.fmt_markdown) function.


## Parameters


`x: X`  
A list of values to be formatted.


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

text_1 = """
### This is Markdown.

Markdown's syntax is comprised entirely of
punctuation characters, which punctuation
characters have been carefully chosen so as
to look like what they mean... assuming
you've ever used email.
"""

text_2 = """
Info on Markdown syntax can be found
[here](https://daringfireball.net/projects/markdown/).
"""

vals.fmt_markdown([text_1, text_2])
```


    ['<h3>This is Markdown.</h3>\n<p>Markdown's syntax is comprised entirely of\npunctuation characters, which punctuation\ncharacters have been carefully chosen so as\nto look like what they mean... assuming\nyou've ever used email.',
     'Info on Markdown syntax can be found\n[here](https://daringfireball.net/projects/markdown/).']
