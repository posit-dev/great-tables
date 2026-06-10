## GT.write_raw_html()


Write the table to an HTML file.


Usage

``` python
GT.write_raw_html(
    gt,
    filename,
    encoding="utf-8",
    inline_css=False,
    newline=None,
    make_page=False,
    all_important=False
)
```


This helper function saves the output of [GT.as_raw_html()](GT.as_raw_html.md#great_tables.GT.as_raw_html) to an HTML file specified by the user.


## Parameters


`gt: GT`  
A GT object.

`filename: str | Path`  
The name of the file to save the HTML. Can be a string or a `pathlib.Path` object.

`encoding: str = ``"utf-8"`  
The encoding used when writing the file. Defaults to 'utf-8'.

`inline_css: bool = ``False`  
An option to supply styles to table elements as inlined CSS styles. This is useful when including the table HTML as part of an HTML email message body, since inlined styles are largely supported in email clients over using CSS in a `<style>` block.

`newline: str | None = None`  
The newline character to use when writing the file. Defaults to `os.linesep`.


## Returns


`None`  
An HTML file is written to the specified path and the method returns `None`.
