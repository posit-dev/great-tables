---
name: great-tables
description: Use when the user's request involves building any table with `great_tables`, `gt.GT`, `gtsave`, or turning tabular data (CSV, DataFrame, spreadsheet) into a rendered PNG. Drives every table through one deterministic 7-step flowchart — understand data, organize columns, Big Color (which measures earn fill), heading band, Small-Color checklist, titles/annotations, render+verify — a deterministic flowchart for nearly every design decision. Before writing any Python, read `references/REFERENCE.md`: it routes every color, band, polish, and API decision to the exact reference file that pins its value. The mandatory renderer is `gt.gtsave("table.png")`. Invoke before reading the data or writing any Python — the flowchart shapes the whole script.
---

# Great Tables Skill

Build publication-ready display tables in Python with `great_tables`. This skill is
a **flowchart, not a menu**: for most parts of a table there is one deterministic
rule (or one explicit, data-driven branch); the exception is which measures earn a
color fill when several are named, which is a judgment call about redundancy, not a
fixed formula — so most of a table's design should reproduce identically across
runs, with that one exception. **Every table reads as one product.**

## Read this before you write ANY Python

Before you write **any** Python, read **`references/REFERENCE.md`**. It is the single
doorway that routes every decision below to the exact reference file holding its
pinned value — palette, hex, domain rule, polish checklist, method signature, worked
example. **Do not skip it.** SKILL.md carries the *procedure and the decision points*;
it deliberately holds **zero** pinned values. Those live only in the references that
`REFERENCE.md` points you to.

## Rule 0 — the user's prompt overrides everything

Every rule below is a **default**. Any explicit instruction in the user's prompt wins
(a requested font, a column's format, "bold the totals," "show all rows"). The
flowchart decides what to do *in the absence of* an instruction; it never overrides
one. When a user instruction conflicts with a default, follow the user and drop the
conflicting default silently — do not fight it or add it back later.

## The 7-step flowchart

```
1. UNDERSTAND THE DATA   grain? identifiers? measures? categories? units? quality?
                         clean → ONE correctly-typed DataFrame (references/data.md)
                         validate request vs data (blank table if unanswerable)
2. ORGANIZE COLUMNS      show/hide · limit rows · stub (default) · groups (gated)
                         spanners (column groups) · name the hero column · primary
                         heatmapped measure prefers an outer edge (strong default,
                         not absolute)
3. BIG COLOR             which measure(s) earn fill (the hero if only 1); encoding
                         by data shape; gradients use sequential/diverging, everything
                         else uses Dark Academia solids
4. HEADING BAND          unconditional: dark navy band, bold labels, white text —
                         every table, regardless of Big Color
5. SMALL COLOR           fixed checklist: borders · dividers · striping · stub tint ·
                         fmt_* per column · row-group rule (bold + border, no fill)
6. TITLES & ANNOTATIONS  title + subtitle (both required) · caption (≥5 rows) +
                         source (when known), stacked footer notes
7. RENDER & VERIFY       gt.gtsave("table.png") · read it back · audit every rule
```

The order is fixed: color intent (Step 3) is decided before the quiet polish (Step 5).
The heading band (Step 4) is a fixed branding constant, not a decision — it renders the
same way whether or not Step 3 produced any Big Color.

## Step 7 is an audit against a checklist, not a vibe check

"Read it back and audit every rule" is not one vague pass — it means going through
every item below **against the actual code you wrote**, not against your memory of
what you intended. Big Color (Step 3) gets attention because it's the visible,
interesting decision; these are the small, boring items that are just as easy to
silently skip — and skipping them is what makes an otherwise well-colored table read
as bare or half-finished. Before you consider the table done:

1. **Title AND subtitle** — both set (Step 6).
2. **Frame** — a boxed border on all four sides, not flat/edge-to-edge (Global
   constants above).
3. **Body-row hairlines** — `table_body_hlines_style` set to a visible style
   (`small_color.md` (a)). Unconditional, every table, never gated on row count or
   Big Color.
4. **Footer: TWO separate `tab_source_note(...)` calls**, not one combined line, on
   any table with ≥5 rows (`small_color.md` (f)) — an analytical caption (a finding
   or a definition you had to pick) AND a separate source/provenance note.
5. **Striping gate — apply by default, always.** Skip **only** when every visible
   non-stub/non-group column in the body is already 100% covered by color (e.g. a
   single fully-heatmapped measure column next to a stub, nothing else) —
   `opt_row_striping()` is REQUIRED otherwise, not a nice-to-have. Row count is not a
   factor: a 5-row table stripes exactly like a 500-row table. If you haven't actually
   checked whether the body is fully color-covered, check now before answering this
   item.
6. **Stub tint gate — independent of item 5, not either/or.** If a stub
   (`rowname_col`) exists, it needs the fixed pale-blue tint, `#EAF0F6`,
   unconditionally (`small_color.md` (d)) — striping being on doesn't excuse skipping
   it; stripes still show on an unfilled stub (`small_color.md` (c)).
7. **Every unselected measure stays fully plain at the measure level — no
   consolation bold, no numeric cap either way.** Recount every `data_color`/`heatmap`
   call now: each fill should still be earning its place for this data — there is no
   fixed count, so don't cut a fill just to hit a number, and don't keep one just
   because it's already there. Any measure that doesn't carry a fill — because it
   never qualified, or because it turned out to be a near-redundant restatement of
   another colored measure (`small_color.md`'s redundancy check) — renders as an
   ordinary, unstyled value column at the MEASURE level: no whole-column
   `style.text(weight="bold")`, no whole-column text-color treatment, no fill. Plain
   text is the correct, final treatment for that measure, not a placeholder for a
   missing color. (This does not forbid the separate, narrower
   `bold_colored_number.md` technique of bolding a small number of individual outlier
   CELLS within an otherwise-plain column when the request specifically calls for
   highlighting extremes — that's a distinct technique for a few cells, not a
   consolation treatment for a whole measure that lost a fill.)

An item you can't check off because you never evaluated its gate (didn't check
whether the table has ≥5 rows for the caption gate, didn't check whether a stub
exists) is not "not applicable" — go compute the gate condition, then check the item
for real.

## Withhold values, forbid guessing — open the file the action needs

SKILL.md names *what* to decide; the *value* you type lives only in a reference file.
Before you type the code below, open the file `REFERENCE.md` routes you to and **copy
the value out of it. Do NOT guess a palette, a hex, a domain, or a signature from
memory.**

- **Before you organize columns** (right after Step 1): open `data.md` and get to
  **one clean, correctly-typed DataFrame** — strip currency/percent strings to floats,
  coerce `object`-dtype numeric columns, fix a non-zero header row, cast SQL `Decimal`s.
  `great_tables` *formats* numbers; it does **not** parse strings, so a `"$1,200"` value
  silently breaks `fmt_*` / `data_color`.
- **Before you finalize column order** (Step 2): the column (or column-group) carrying
  the primary/most-important heatmap fill should prefer an outer edge — right after
  the stub, or as the last column(s). This is a strong preference, not an absolute; a
  table with multiple qualifying measures may reasonably place one a column or two
  inside the edge if that better serves the table's narrative order — don't force a
  reordering that fights the data's natural grouping just to satisfy it. Columns
  providing context/inputs a reader needs first precede columns reporting a
  derived/resulting outcome, so an outcome-type measure naturally lands at the right
  edge while a measure that IS the subject's defining fact lands at the left edge. Use
  `cols_move`/`cols_move_to_start`/`cols_move_to_end` (`api.md`) to place it.
- **Before you write any `data_color(...)`** (Step 3): the exact palette name, hexes,
  and domain live ONLY in the `big_color/<shape>.md` file `REFERENCE.md` names for your
  data shape. Open that file (plus `palettes.md`) and copy them. Do not invent a
  palette or a hex.
- **Before you set the heading band** (Step 4): open `palettes.md`'s branding tier and
  copy the exact band hex, weight, and label text color — a fixed value, the same on
  every table, independent of whether the body has Big Color. Do not improvise a band
  color.
- **Before you run the Small-Color polish** (Step 5): open `small_color.md` and run its
  fixed checklist top to bottom. Every neutral hex, the striping gate, the stub tint,
  and the fmt-per-type rules are there. Do not improvise a grey.
- **Before you call any method you are unsure of** (any step): open `api.md` for the
  exact signature, arguments, and defaults. Do not guess an argument name.

If SKILL.md cannot answer it and you may not invent it, the reference **has** to be
opened.

## Global constants (true for every table)

Set once, never vary unless Rule 0 fires. These are **named rules**; their exact
numeric values live in the references.

- **Frame.** A boxed enclosing light border on all four sides + a margin around the
  whole table (never flat/edge-to-edge). The exact border color/width and the `gtsave`
  margin value are in `references/small_color.md`. Rounded corners preferred; a square
  light border is acceptable — the enclosing border + margin is the non-negotiable.
- **Header alignment.** Title + subtitle centered (the default).
- **Font family.** great-tables default. Do **not** set the font unless the user asks.
- **Font size.** Default; shrink as little as possible, only when forced.
- **Font-size fit rule.** When a table renders too big, in this order: (1) give it room
  — raise the `gtsave` width/height; (2) keep it crisp — raise the `gtsave` zoom;
  (3) **only then** reduce font size, by the smallest amount that restores clarity. The
  default zoom and the margin value are in `references/small_color.md`. Relative scale:
  title > subtitle > body > source/caption.
- **Compact layout.** Every table sizes each column with `cols_width(cases={...})` to
  its own content plus a small buffer, and pins six padding values via
  `tab_options(...)`. Widths are content-dependent (pick per table); the padding
  literals are pinned in `references/small_color.md`. A consistency addition, not
  currently mechanically checked.

## Correctness gotchas (named rules — the values live in the references)

- **`data_color` domain.** Always set `domain=` to cover the full data range; a
  **signed/diverging** measure's domain must be **symmetric about 0** with
  `truncate=False`. The exact rule and the data-driven bound are in
  `references/big_color/diverging_fill.md`.
- **`fmt_percent` scale.** It expects values in decimal form (`0.15` renders as `15%`);
  if your data is already on a 0–100 scale, pass `scale_values=False`. See `api.md`.
- **Original column names** in `fmt_*` / `data_color` — not the `cols_label` display text.
- **Row indices in `loc.body()`** are 0-based display positions, not the DataFrame index.
- **Method chaining.** Build the whole table in one chained expression; collect row
  indices into lists rather than looping `tab_style` per row.
- **Renderer.** End with **`gt.gtsave("table.png")`** only. `gtsave()` renders
  through headless Chrome, so a launchable **Chrome/Chromium is a prerequisite**
  (assume one is installed; do not provision it). Never fall back to `gt.save()`
  (deprecated), `.as_raw_html()` + a screenshot tool, PIL/Pillow,
  imgkit/wkhtmltoimage/weasyprint, Playwright/Selenium/headless-chrome, or writing
  `table.html`. If rendering fails, **stop and surface the error verbatim** — a
  fallback produces a fake table.
- **Imports.** `from great_tables import GT, md, html, style, loc`.
