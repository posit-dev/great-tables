# DATA — grain, identifiers, and measure definitions (read before house_table.py)

House format has no numbered flowchart, but every table still needs three
questions answered **before** you go pattern-match a block in
`house_table.py`: what is one row, what actually identifies it, and what
does each measure mean. Skip these and the table still renders cleanly —
it just stubs, colors, or ranks the wrong thing. `RULES.md`'s per-type
rules (financial, percent, categorical, ...) only work once you've picked
the right column(s) for each role; they don't tell you how to pick.

## 1. Find the grain, then find the identifier — it is often NOT one column

"A row identifier" in `RULES.md`'s stub rule usually is not the single
column whose name sounds like an ID. Three shapes show up in real data:

- **Single column** — an obvious ID/name/date column. Stub it directly.
- **Composite** — no single column is unique or meaningful alone, but two
  or more together are (`mfr` + `model` in a car dataset: "Toyota" alone
  isn't a row identity, "Toyota Camry" is). Build the stub column yourself
  — `df["car"] = df["mfr"] + " " + df["model"]` — then `rowname_col="car"`.
  Do this whenever the request's own language refers to rows by the
  combination ("the Bentley Continental GT," not "the Bentley").
- **Constructed** — the identity is a transformation of other columns
  (`year` + `month` -> "Jan 2020"; a fiscal quarter from a date). Build the
  display label the same way before stubbing it.

**The test, not a vibe check:** would two different rows in this dataset
ever render the identical stub label? If yes, you haven't found the real
grain yet — go one level more specific (add the composite/constructed
column) before you call `rowname_col=`. A table with no stub at all is
only correct when the request's own subject genuinely has no natural row
identity (e.g. "compare these 3 named metrics side by side").

## 2. Name every derived measure explicitly, BEFORE deciding its color kind

A request often names a comparison that isn't a literal column — "gain,"
"loss," "growth," "performance," "change." Before it can go through
`heatmap()`, pin down which of these two it actually is, because they get
opposite color treatment:

- **An absolute magnitude** (`close - open` in dollars, `2021 - 1996` in
  raw units) is a **sequential** measure at best (Blues/neutral, or plain
  text — no fill, no bold — if it's not the hero) — dollars and raw-unit
  deltas do not have a natural "this is bad, this is good" symmetric
  center, and a diverging red/green scale on them reads as a claim you
  haven't earned.
- **A relative/percent change** (`(close - open) / open`, `pct_change()`,
  year-over-year `%`) is the genuinely **signed** measure — this is what
  `heatmap(kind="diverging")` in `RULES.md`'s percent section is for.

Compute the one the request actually means (usually the % form when the
prompt says "growth"/"gain"/"performance" without naming a currency), and
say which you picked in the analytical caption note (the first
`tab_source_note()` call, not the subtitle). Never color a raw
dollar/unit delta with a diverging palette just because it can be negative
— check whether it's a *rate* first, not just whether it has a sign.

## 3. When 2+ measures are named with no explicit ranking, tie-break like this

A prompt naming two measures ("Horsepower and Price," "trends... comparing
density changes") does not mean both are equally the hero for coloring.
Resolve in this order, and state the pick:

1. An explicitly named ranking/selection metric ("top 10 by revenue")
   always wins outright.
2. Otherwise, the measure in the request's **topic clause** — the noun
   phrase right after "a table of/showing ..." — is the hero; a measure
   named later as a secondary comparison is displayed but stays plain
   text — no fill and no bold — not a second heatmap.
3. Still genuinely tied? Pick the one with the wider real spread across
   the selected rows (more of the story is visible in its color) and say
   so — never split color across both, and never default to whichever
   column happens to be numerically first in the source data.

## 4. Mechanical cleaning is a separate, already-solved problem

Currency/percent strings to floats, `Decimal` casts, header-row fixes,
missing-value conventions — see `RULES.md`'s "Data-cleaning gotchas"
section. Do that pass first; it's a prerequisite for steps 1-3 above
(you can't compute a percent-change measure correctly from a column
that's still a `"$1,200"` string).

## 5. Color/heatmap follows the measure's MEANING, never its column name

Once grain and measure definitions are pinned (steps 1-2), the color
choice in `RULES.md` is close to mechanical — but the input to that
choice is the semantic type you just decided (magnitude vs. rate vs.
category), not whatever the column happens to be called. A column named
`score` that's actually a 1-5 categorical rating is `status_chip`
territory, not a sequential heatmap; a column named `delta` that's
actually a fractional rate is the diverging candidate from step 2, not a
sequential one. When in doubt, re-derive the type from the values
(`df[col].nunique()` small and non-numeric-feeling -> categorical; can go
negative and is a rate -> diverging; strictly non-negative magnitude ->
sequential) rather than from the name.
