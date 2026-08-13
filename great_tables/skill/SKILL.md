---
name: great-tables
description: Use when building a table with `great_tables`, `gt.GT`, or `gtsave`, or turning tabular data (CSV, DataFrame, spreadsheet) into a rendered PNG — including requests that look simple (a plain list, one or two numeric columns), since the house style still applies. One worked reference script plus a short per-column-kind rules file and a short data/measure-definitions file — no flowchart, no archetype directory. Read the one annotated script, pattern-match the section that fits your data, adapt it, done. Invoke before reading the data or writing any Python.
license: MIT
compatibility: Requires Python >=3.10 and a launchable Chrome/Chromium install (gtsave() renders through headless Chrome).
metadata:
  author: hrudith-lakshminarasimman
  version: "2.0"
  tags:
    - tables
    - data-visualization
    - table-design
    - python
---

# Great Tables — House Format

The mechanism is deliberately thin: **one script, one rules file, one
data/measure-definitions file, no procedure.**

1. Read `scripts/house_table.py` once. It is both the worked example (run
   it directly to see `house_table.png`, the canonical reference render)
   and a helper module (`PALETTE` + `frame`/`finalize`/`band`/`stripe`/
   `stub_tint`/`heatmap`/`status_chip`/`summary_row`/`group_emphasis`/
   `humanize_labels`) you import into your own script.
2. **Before you read the data as anything more than a CSV**: open
   `references/data.md`. It answers three questions this skill has no
   flowchart step for otherwise — what is one row and what actually
   identifies it (often a composite/constructed column, not a literal
   one), what a named-but-not-literal measure ("gain," "growth") actually
   computes to, and how to tie-break when 2+ measures are named with no
   explicit ranking. Get these wrong and the table renders cleanly but
   stubs, colors, or ranks the wrong thing.
3. **Before organizing columns**: if the request's measure or selection
   criterion has more than one reasonable reading (e.g. "top N
   fastest-growing" — by what metric?), pick ONE definition and state it
   in the analytical caption note (the first of the two `tab_source_note()`
   calls, not the subtitle) — see `references/RULES.md`'s "Ambiguous
   measures" section. This decides which columns exist at all; do it
   before step 4.
4. Find the block in `house_table.py` that matches your data's shape — a
   plain magnitude, a currency hero measure, a signed percent, a
   categorical status column, a stub, a group, a summary row, a missing
   value — and copy/adapt it.
5. Open `references/RULES.md` for the one rule that applies to the
   column kind you just matched (it points back at the function/section
   in `house_table.py` by name — it does not duplicate the code).

That's the whole workflow. Nothing else to read beyond the three files above.

## The non-negotiable base — every table, no exceptions

Before you call `finalize()`, confirm every one of these is actually in
your script — they are not "pattern-match if it seems relevant," they are
unconditional, regardless of how simple the request looks:

1. **Title AND subtitle** — both, always.
2. **Two source notes** — an analytical caption (the finding, or the
   definition you picked for an ambiguous measure) first, then a
   provenance note; a generic provenance note ("Source: provided
   dataset.") beats none.
3. **The boxed frame** — `frame(gt)`.
4. **Big Color stays restrained** — `heatmap()`/`data_color()` targets only
   the measure(s) the request is actually about, never one heatmap per
   numeric column. There is no numeric cap on colored measures — color
   what the request is actually about, using the correct palette for
   each. Any measure that isn't part of what the request is about
   renders fully plain: no fill, no bold, no text-color treatment of any
   kind — regardless of how many other measures already carry a color
   fill.
5. **Body-row hairlines** — `hairlines(gt)`. A separate option family from
   item 3's frame, not covered by it — `great_tables` already renders a
   raw gray hairline by default, so skipping this call doesn't leave the
   table undivided, it leaves it in the wrong (unbranded) gray. Small
   polish counts as much as Big Color.
6. **`finalize(gt, path="table.png")`** as the final call.

Full detail and the reasoning for each lives in `references/RULES.md`'s
"THE NON-NEGOTIABLE BASE" section (read it — this list is the summary, not
the whole rule). Everything else — a stub, a group, a spanner, a status
chip, a summary row — stays genuinely conditional on the data; only the
six items above are unconditional. Conditional items (striping, stub
tint) still need their gate CHECKED every time, not skipped by default.

## What this skill deliberately does not have

- **No numbered flowchart and no reference-router file.** One script's
  worked example stands in for both the decision sequence and the
  per-shape lookup.
- **No per-archetype example directory** (`assets/examples/<shape>/`).
  `house_table.py` IS the one worked example; there is no second example
  to pick between.
- **No CI checker or run-until-pass loop.** The palette and helper
  functions in `house_table.py` are the only guardrail, and you're
  trusted to read the rendered PNG yourself.

## Rule 0 — the user's prompt overrides everything

Every rule in `references/RULES.md` and every pattern in
`house_table.py` is a **default**. An explicit instruction in the user's
prompt wins (a requested font, a column's format, "bold the totals,"
"show all rows"). Silently drop the conflicting default.

## The mandatory renderer

End every table with **`gt.gtsave("table.png", ...)`** — never `.save()`
(deprecated), never `.as_raw_html()` + a screenshot tool, never PIL/
imgkit/wkhtmltoimage/Playwright/Selenium. `finalize()` in
`house_table.py` wraps this with the house-format `expand=15, zoom=2.0`
defaults. If rendering fails, stop and surface the error verbatim — a
fallback produces a fake table.

## Imports

```python
from great_tables import GT, md, html, style, loc
```
