"""Interactive tables in pages an app makes itself, with a template (Flask's Jinja, Django's) or
with FastHTML: `runtime_tags()` gives the runtime that makes the tables interactive, for the page's
`<head>`, once however many tables it shows, and `write_runtime()` its files, for an app to serve.

A table (`GT` or `GTI`) has an `__html__()`, so it's shown as HTML where it's put in a Jinja
template or in FastHTML's components (Django makes a value a string first, so there it's given as
its HTML, marked safe); it's followed by the runtime, unless it's given as
`as_raw_html(runtime="none")`, as on a page with `runtime_tags()`. The runtime registers
`<gt-table>` once, however often it's on the page.
"""

from __future__ import annotations

__all__ = (
    "runtime_tags",
    "write_runtime",
)

import hashlib
from functools import cache
from html import escape
from pathlib import Path

from ._gti._render import JS_DIR, _load_runtime

# (The runtime's files, as `write_runtime()` writes them)
RUNTIME_FILES = ("gti.js", "gti.css")


class _HTML(str):
    """HTML, which a template (or FastHTML) shows as it is, rather than as text."""

    def __html__(self) -> str:
        return str(self)


def runtime_tags(url: str | None = None, nonce: str | None = None) -> str:
    """
    The tags that give a page the runtime its interactive tables need.

    An interactive table (a `GTI` table, or a `GT` table made with `opt_interactive()`) is a
    `<gt-table>` element, made interactive by the runtime, its JavaScript and CSS. Its HTML (from
    `as_raw_html()`, or as it's put in a template) is followed by the runtime, so that it works
    anywhere; but a page showing several tables needs it only once. These tags, put in the page's
    `<head>`, give it the runtime, and each table is then given without it, as
    `as_raw_html(runtime="none")`.

    The tags have the runtime itself, as a `<style>` and a `<script>`; or, given the `url=` the
    app serves the runtime's files at (as [`write_runtime()`](`great_tables.web.write_runtime`)
    writes them), they link to them, so that a browser keeps them as it does any other file, and
    a page whose Content Security Policy doesn't allow inline scripts can have them (the table's
    spec, in a `<script type="application/json">`, is data, which isn't run). The table's own CSS
    is inline, in a `<style>` (and its styles in `style=` attributes), so the policy's
    `style-src` must allow `'unsafe-inline'`.

    The tags are HTML (a `str` with an `__html__()`), which a template (Jinja's, as Flask has, or
    Django's) or FastHTML shows as it is. A table is put in a page as its HTML, from
    `as_raw_html(runtime="none")`, marked safe (with `|safe` in a template, as below, or Django's
    `mark_safe()`, or FastHTML's `NotStr()`).

    Parameters
    ----------
    url
        Where the app serves the runtime's files, `gti.js` and `gti.css` (e.g., `"/static/gti/"`).
        Each link has the file's version (`?v=`), so that a browser doesn't keep an old one. By
        default (`None`), the tags have the runtime itself.
    nonce
        A nonce for the page's Content Security Policy, which the tags are given (as their
        `nonce=` attribute), so that it allows them.

    Returns
    -------
    str
        The tags, as HTML (a `str` with an `__html__()`).

    Examples
    --------
    In a Flask app, with the runtime's files written to its `static/gti` folder (with
    `write_runtime("static/gti")`, once), and a page with two tables:

    ```python
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
    """
    attrs = f' nonce="{escape(nonce)}"' if nonce is not None else ""
    if url is None:
        js, css = _load_runtime()
        return _HTML(f"<style{attrs}>\n{css}</style>\n<script{attrs}>\n{js}</script>\n")
    base = url if url.endswith("/") else f"{url}/"
    css_url = escape(f"{base}gti.css?v={_version('gti.css')}")
    js_url = escape(f"{base}gti.js?v={_version('gti.js')}")
    return _HTML(
        f'<link rel="stylesheet" href="{css_url}"{attrs}/>\n'
        f'<script src="{js_url}" defer{attrs}></script>\n'
    )


def write_runtime(directory: str | Path) -> list[Path]:
    """
    Write the runtime's files, for an app to serve.

    The runtime that makes interactive tables interactive is two files, `gti.js` and `gti.css`,
    written to `directory` (made if it isn't there) for an app to serve as static files (as a
    Flask app serves its `static` folder, or Django its static files), and linked to by
    [`runtime_tags(url=)`](`great_tables.web.runtime_tags`). Write them again with each new
    version of Great Tables (as when the app starts, or is built), as a table needs the runtime of
    its own version.

    Parameters
    ----------
    directory
        The directory to write the files to.

    Returns
    -------
    list[Path]
        The files written.
    """
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for name in RUNTIME_FILES:
        path = directory / name
        path.write_bytes((JS_DIR / name).read_bytes())
        paths.append(path)
    return paths


@cache
def _version(name: str) -> str:
    """A file of the runtime's version: the start of its hash."""
    return hashlib.sha256((JS_DIR / name).read_bytes()).hexdigest()[:12]
