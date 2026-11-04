# GTI

The source of `<gt-table>`, the custom element behind Great Tables' interactive tables. It
hydrates the static HTML that Great Tables renders (the static table *is* the interactive table)
and has no runtime dependencies.

This package is for working on the component itself. Using Great Tables, including its interactive
tables, never needs Node: the built runtime is committed to `great_tables/js/gti.{js,css}` and
ships in the wheel. This directory isn't part of the Python package.

## Setup

Node 24 (other recent versions should work).

```bash
cd packages/gti
npm ci
npx playwright install chromium   # for the browser tests
```

## Commands

| Command | What it does |
|---|---|
| `npm run build` | Builds `great_tables/js/gti.{js,css}` (minified) and prints their gzipped sizes |
| `npm run check` | Type-checks, then fails if the committed bundle is stale or the runtime is over its 50 KB (min+gzip) budget |
| `npm test` | Unit tests (Vitest, happy-dom) |
| `npm run test:e2e` | Browser tests (Playwright, Chromium) on pages built from real Great Tables output |

After changing anything in `src/`, run `npm run build` and commit the rebuilt
`great_tables/js/gti.*` along with the source; CI runs `npm run check`.

The build shortens the names of `private` members (TypeScript's `private` is gone in the bundle,
so minifying alone keeps them), where that can't break anything: see `scripts/mangle.mjs`. A
private member that the browser tests read, as `(node as any).name`, keeps its name; one read any
other way from outside the bundle (by a host page, say) should be made public instead.

The browser tests write their pages with `e2e/make_fixtures.py`, which needs a Python with
`great_tables` installed. They use `$PYTHON` if set, otherwise the repo's `.venv`, otherwise
`python3`.

Great Tables' differential tests of its view queries (`tests/test_gti_query.py`) run tables
through the built runtime with `scripts/engine.mjs`, so they need `npm ci` here too (they're
skipped without it).

## Layout

```
src/        TypeScript source (index.ts is the bundle entry) and gti.css
test/       Vitest unit tests
e2e/        Playwright tests, and the script that writes their fixture pages
scripts/    build.mjs (build, staleness check, size budget), mangle.mjs (the private names it
            shortens), engine.mjs (the runtime under Node, for Python's differential tests)
```

The npm package name is undecided, so the package is marked private for now.
