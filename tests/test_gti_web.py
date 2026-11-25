"""Interactive tables in pages an app makes itself: `great_tables.web`, `as_raw_html(runtime=)`,
and a table's `__html__()`, in Jinja's, Django's and FastHTML's pages.

The pages are tested in a browser, served by Flask and FastHTML apps, in
packages/gti/e2e/hosts.spec.ts.
"""

from __future__ import annotations

import hashlib
import runpy
import shutil

import pandas as pd
import pytest

from great_tables import GT, GTI
from great_tables._gti._render import JS_DIR, _load_runtime
from great_tables.web import RUNTIME_FILES, runtime_tags, write_runtime
from tests.utils import DEMOS, docs_code

DATA = pd.DataFrame({"char": ["apricot", "banana"], "num": [1.0, 2.0]})

JS, CSS = _load_runtime()


def tables() -> list[GT]:
    """A `GTI` table, a `GT` table made interactive, and a static `GT` table (with ids, so that
    each renders the same each time)."""
    return [GTI(DATA, id="one"), GT(DATA, id="two").opt_interactive(), GT(DATA, id="three")]


def elements(page: str) -> int:
    """The `<gt-table>` elements in a page (each with its spec)."""
    return page.count("data-gti-spec>")


def version(name: str) -> str:
    return hashlib.sha256((JS_DIR / name).read_bytes()).hexdigest()[:12]


def test_runtime_tags_inline():
    tags = runtime_tags()
    assert tags == f"<style>\n{CSS}</style>\n<script>\n{JS}</script>\n"
    assert tags.__html__() == tags


def test_runtime_tags_nonce():
    tags = runtime_tags(nonce='a"b')
    assert tags.startswith('<style nonce="a&quot;b">\n')
    assert '<script nonce="a&quot;b">\n' in tags
    assert JS in tags


@pytest.mark.parametrize("url", ["/static/gti", "/static/gti/"])
def test_runtime_tags_url(url: str):
    tags = runtime_tags(url=url)
    assert tags == (
        f'<link rel="stylesheet" href="/static/gti/gti.css?v={version("gti.css")}"/>\n'
        f'<script src="/static/gti/gti.js?v={version("gti.js")}" defer></script>\n'
    )
    assert tags.__html__() == tags


def test_runtime_tags_url_escaped_with_nonce():
    tags = runtime_tags(url='https://cdn.example/?a=1&b="', nonce="n")
    assert 'href="https://cdn.example/?a=1&amp;b=&quot;/gti.css?v=' in tags
    assert f'gti.js?v={version("gti.js")}" defer nonce="n"></script>' in tags
    assert f'gti.css?v={version("gti.css")}" nonce="n"/>' in tags


def test_write_runtime(tmp_path):
    directory = tmp_path / "static" / "gti"
    paths = write_runtime(directory)
    assert paths == [directory / "gti.js", directory / "gti.css"]
    assert (directory / "gti.js").read_text(encoding="utf-8") == JS
    assert (directory / "gti.css").read_text(encoding="utf-8") == CSS
    # (Written again, over the old ones)
    (directory / "gti.js").write_text("old", encoding="utf-8")
    write_runtime(str(directory))
    assert (directory / "gti.js").read_text(encoding="utf-8") == JS


@pytest.mark.parametrize("make_page", [False, True])
def test_as_raw_html_runtime_none(make_page: bool):
    interactive, opt, static = tables()
    for table in (interactive, opt):
        html = table.as_raw_html(runtime="none", make_page=make_page)
        assert "<gt-table" in html
        assert JS not in html
        assert CSS not in html
        assert table.as_raw_html(make_page=make_page).startswith(html.split("</gt-table>")[0])
        assert JS in table.as_raw_html(runtime="inline", make_page=make_page)
    # (A static table has no runtime)
    assert static.as_raw_html(runtime="none") == static.as_raw_html()


@pytest.mark.parametrize("table", tables(), ids=["gti", "opt_interactive", "static"])
def test_as_raw_html_runtime_bad(table: GT):
    with pytest.raises(ValueError, match="`runtime=` must be"):
        table.as_raw_html(runtime="external")  # type: ignore[arg-type]


@pytest.mark.parametrize("table", tables(), ids=["gti", "opt_interactive", "static"])
def test_html_dunder(table: GT):
    assert table.__html__() == table.as_raw_html()


def test_jinja():
    jinja2 = pytest.importorskip("jinja2")
    env = jinja2.Environment(autoescape=True)
    interactive, _, static = tables()
    page = env.from_string("{{ runtime }}{{ one }}{{ two }}").render(
        runtime=runtime_tags(url="/gti/"), one=interactive, two=static
    )
    assert page.startswith('<link rel="stylesheet" href="/gti/gti.css?v=')
    assert elements(page) == 1
    assert page.count(JS) == 1
    assert page.count('<table class="gt_table"') == 2


def test_django():
    pytest.importorskip("django")
    from django.conf import settings
    from django.template import Context, Engine

    if not settings.configured:
        settings.configure()
    interactive, opt, _ = tables()
    # (Django makes a value a string before it's escaped, so a table's given as its HTML, marked
    # safe; the runtime's tags are a string already)
    page = (
        Engine()
        .from_string("{{ runtime }}{{ one|safe }}{{ two|safe }}")
        .render(
            Context(
                {
                    "runtime": runtime_tags(),
                    "one": interactive.as_raw_html(runtime="none"),
                    "two": opt.as_raw_html(runtime="none"),
                }
            )
        )
    )
    assert page.startswith(f"<style>\n{CSS}</style>")
    assert elements(page) == 2
    assert page.count(JS) == 1


def test_fasthtml():
    pytest.importorskip("fasthtml")
    from fasthtml.common import Div, Head, Html, to_xml

    interactive, _, static = tables()
    page = to_xml(Html(Head(runtime_tags(url="/gti")), Div(interactive), Div(static)))
    assert '<link rel="stylesheet" href="/gti/gti.css?v=' in page
    assert elements(page) == 1
    assert page.count(JS) == 1
    assert page.count('<table class="gt_table"') == 2
    assert "&lt;" not in page.split("<body>")[0]


def test_fasthtml_route_returns_a_table():
    pytest.importorskip("fasthtml")
    pytest.importorskip("httpx")
    from fasthtml.common import Div, FastHTML
    from starlette.testclient import TestClient

    interactive, gt_interactive, static = tables()
    app = FastHTML(secret_key="test")  # (Without writing a .sesskey file)
    app.get("/one")(lambda: interactive)
    app.get("/two")(lambda: (gt_interactive, Div("After")))
    app.get("/three")(lambda: static)

    # (Each in a page, as its HTML, as a component is: not its repr, nor escaped)
    client = TestClient(app)
    for path, table in [("/one", interactive), ("/two", gt_interactive), ("/three", static)]:
        page = client.get(path).text
        assert page.startswith("<!doctype html>")
        assert table.as_raw_html() in page
        assert "&lt;" not in page and "GT(" not in page
    assert elements(client.get("/one").text) == 1
    assert "<div>After</div>" in client.get("/two").text
    assert interactive.__ft__() == interactive.__html__() == interactive.as_raw_html()


DEMO = DEMOS / "flask" / "app.py"


def test_demo_app(tmp_path, monkeypatch):
    # (The docs' demo, run from another folder than its own: its runtime is written where Flask
    # serves it from, beside the app, and linked to once for both tables)
    pytest.importorskip("flask")
    shutil.copy(DEMO, tmp_path / "app.py")
    monkeypatch.chdir(tmp_path.parent)
    client = runpy.run_path(str(tmp_path / "app.py"))["app"].test_client()
    page = client.get("/").text
    assert runtime_tags(url="/static/gti/") in page
    assert elements(page) == 2 and JS not in page
    assert "Ford" in page and "$447,000" in page
    for name in RUNTIME_FILES:
        assert client.get(f"/static/gti/{name}").data == (JS_DIR / name).read_bytes()


def test_demo_app_is_the_docs():
    # (The code shown is the app that's run)
    (code,) = docs_code("27-gti-in-python-and-apps.qmd", "Using the table in a page an app makes")
    assert code == DEMO.read_text(encoding="utf-8")
