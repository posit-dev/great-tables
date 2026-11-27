# GT.write_raw_html()

Write the table to an HTML file.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_export.py#L660-L734)

``` python
GT.write_raw_html(
    gt,
    filename,
    encoding="utf-8",
    inline_css=False,
    newline=None,
    make_page=False,
    all_important=False,
    runtime="inline",
)
```

This helper function saves the output of [GT.as_raw_html()](../reference/GT.as_raw_html.md#great_tables.GT.as_raw_html) to an HTML file specified by the user.

## Parameters

`gt: GT`  
A GT object.

`filename: str | Path`  
The name of the file to save the HTML. Can be a string or a `pathlib.Path` object.

`encoding: str = "utf-8"`  
The encoding used when writing the file. Defaults to 'utf-8'.

`inline_css: bool = False`  
An option to supply styles to table elements as inlined CSS styles. This is useful when including the table HTML as part of an HTML email message body, since inlined styles are largely supported in email clients over using CSS in a `<style>` block.

`newline: str | None = None`  
The newline character to use when writing the file. Defaults to `os.linesep`.

`make_page: bool = False`  
If `True`, the table is wrapped in a complete HTML page, with `<html>`, `<head>` and `<body>` tags.

`all_important: bool = False`  
If `True`, all CSS declarations are marked with `!important`.

`runtime: Literal["inline", "none"] = "inline"`  
Whether an interactive table's HTML is followed by the runtime that makes it interactive, its JavaScript and CSS: `"inline"` (the default) or `"none"`, for a page that has the runtime once, however many tables it shows (see [`runtime_tags()`](../reference/web.runtime_tags.md#great_tables.web.runtime_tags)). A static table has no runtime, so this doesn't change it.

## Returns

`None`  
An HTML file is written to the specified path and the method returns `None`. (A [GTI](../reference/GTI.md#great_tables.GTI) table with its rows as an asset, as [`i_scale()`](../reference/GTI.i_scale.md#great_tables.GTI.i_scale) sets it, has the rows past its first page written beside it, to a file named as the HTML file is, with `.gti.json` for its extension.)
