# web.write_runtime()

Write the runtime's files, for an app to serve.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/web.py#L116-L144)

``` python
web.write_runtime(directory)
```

The runtime that makes interactive tables interactive is two files, `gti.js` and `gti.css`, written to `directory` (made if it isn't there) for an app to serve as static files (as a Flask app serves its `static` folder, or Django its static files), and linked to by [`runtime_tags(url=)`](../reference/web.runtime_tags.md#great_tables.web.runtime_tags). Write them again with each new version of Great Tables (as when the app starts, or is built), as a table needs the runtime of its own version.

## Parameters

`directory: str | Path`  
The directory to write the files to.

## Returns

`list[Path]`  
The files written.
