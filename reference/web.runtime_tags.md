# web.runtime_tags()

The tags that give a page the runtime its interactive tables need.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/web.py#L37-L113)

``` python
web.runtime_tags(
    url=None,
    nonce=None,
)
```

An interactive table (a [GTI](../reference/GTI.md#great_tables.GTI) table, or a [GT](../reference/GT.md#great_tables.GT) table made with [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive)) is a `<gt-table>` element, made interactive by the runtime, its JavaScript and CSS. Its HTML (from [as_raw_html()](../reference/GT.as_raw_html.md#great_tables.GT.as_raw_html), or as it's put in a template) is followed by the runtime, so that it works anywhere; but a page showing several tables needs it only once. These tags, put in the page's `<head>`, give it the runtime, and each table is then given without it, as `as_raw_html(runtime="none")`.

The tags have the runtime itself, as a `<style>` and a `<script>`; or, given the `url=` the app serves the runtime's files at (as [`write_runtime()`](../reference/web.write_runtime.md#great_tables.web.write_runtime) writes them), they link to them, so that a browser keeps them as it does any other file, and a page whose Content Security Policy doesn't allow inline scripts can have them (the table's spec, in a `<script type="application/json">`, is data, which isn't run). The table's own CSS is inline, in a `<style>` (and its styles in `style=` attributes), so the policy's `style-src` must allow `'unsafe-inline'`.

The tags are HTML (a `str` with an `__html__()`), which a template (Jinja's, as Flask has, or Django's) or FastHTML shows as it is. A table is put in a page as its HTML, from `as_raw_html(runtime="none")`, marked safe (with `|safe` in a template, as below, or Django's `mark_safe()`, or FastHTML's `NotStr()`).

## Parameters

`url: str | None = None`  
Where the app serves the runtime's files, `gti.js` and `gti.css` (e.g., `"/static/gti/"`). Each link has the file's version (`?v=`), so that a browser doesn't keep an old one. By default (`None`), the tags have the runtime itself.

`nonce: str | None = None`  
A nonce for the page's Content Security Policy, which the tags are given (as their `nonce=` attribute), so that it allows them.

## Returns

`str`  
The tags, as HTML (a `str` with an `__html__()`).

## Examples

In a Flask app, with the runtime's files written to its `static/gti` folder (with `write_runtime("static/gti")`, once), and a page with two tables:

``` python
from flask import Flask, render_template_string
from great_tables import GTI, exibble
from great_tables.web import runtime_tags

app = Flask(__name__)

PAGE = (
    "<html><head>{{ runtime }}</head>"
    "<body>{{ one|safe }}{{ two|safe }}</body></html>"
)

@app.route("/")
def index():
    return render_template_string(
        PAGE,
        runtime=runtime_tags(url="/static/gti/"),
        one=GTI(exibble).as_raw_html(runtime="none"),
        two=GTI(exibble).i_selection("multiple").as_raw_html(runtime="none"),
    )
```
