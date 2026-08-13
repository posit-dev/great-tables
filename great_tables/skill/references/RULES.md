# RULES — per-data-type formatting rules

No flowchart here. Find the row below that matches your column's kind, then
open `scripts/house_table.py` and find the function/section it names — copy
and adapt that, not this file's prose.

## THE NON-NEGOTIABLE BASE — every table gets ALL of these, no exceptions

This is not a menu, and it is not conditional on whether a particular table
"seems to need it." Every table this skill produces — no matter how simple
the request looks — gets every item below. Treat this as a checklist to
run through immediately before you call `finalize()`: if any box below is
unchecked, the table isn't done yet.

1. **Title AND subtitle, both, always** — `tab_header(title=..., subtitle=...)`.
   A subtitle-less or title-less table is incomplete, full stop — there is
   no data shape simple enough to skip this.
2. **TWO source notes: an analytical caption stating the finding or the
   chosen definition, then a separate provenance note** — two
   `tab_source_note(source_note=...)` calls, caption first. If the actual
   provenance is unknown, write a generic-but-real provenance note
   ("Source: provided dataset.") rather than omitting it — an unstated
   source is still a gap, not a neutral default.
3. **The boxed frame, always** — `frame(gt)`.
4. **Big Color stays restrained, not capped at a fixed number** —
   `data_color`/`heatmap()` calls across the WHOLE table target only the
   measure(s) that are actually the point of the request, never "one per
   numeric column." There is no numeric cap on colored measures — color
   what the request is actually about, using the correct palette for
   each. Any measure that isn't part of what the request is about
   renders fully plain: no fill, no bold, no text-color treatment of any
   kind. This applies regardless of how many other measures already
   carry a color fill. See "Color restraint" below.
5. **Body-row hairlines pinned to the house tone, always** — `hairlines(gt)`.
   `great_tables` renders a hairline between body rows ON BY DEFAULT (a
   raw library gray, `#D3D3D3`) even without this call — the gap this
   closes is not "no line at all," it's "the wrong gray." This is a
   completely separate `great_tables` option family from item 3's outer
   `frame()` border, not a duplicate of it — calling `frame()` alone still
   leaves the body-row lines at the library default, unrelated to whatever
   the frame itself looks like. Small polish like this is not optional
   filler around the "real" work of Big Color — a table with a heatmap but
   the raw default hairline gray is still an unfinished table.
6. **`finalize(gt, path="table.png")`** — the mandatory render, always last.

Everything else in this file — a stub, a group, a spanner, a status chip,
a summary row, the striping/tint hierarchy — is genuinely conditional on
what the data and request actually call for, and stays that way. The six
items above are different in kind: they are the base every table stands
on, never something to selectively adopt. If you imported a helper
(`stripe`, `stub_tint`, `humanize_labels`, ...) and then don't end up
calling it, that's a sign you copied more of `house_table.py` than your
table needs — remove the unused import, but never let "I didn't get to
it" cost you an item on this list.

**Conditional does not mean skippable — it means "evaluate the gate every
time."** `stripe()` (apply UNLESS the body's visible non-stub/non-group
columns are already 100% covered by `data_color`/`heatmap` fills — a
heatmap that already paints every real cell is the one case where a
stripe has nothing left to show through on; row count is NOT part of this
gate anymore) and `stub_tint()` (a stub exists) are genuinely
data-dependent, not unconditional like the six items above — but that
means you check their gate condition on every table, not that you can
forget they exist. A 5-row table with a mostly-plain body that ships with
no striping and no stub tint isn't "keeping it simple," it's skipping two
items whose gate condition was clearly met — striping is the DEFAULT now,
not something reserved for long tables.

## Ambiguous measures / selection criteria — pick ONE definition, STATE it

A request like "Create a table showing **population growth trends** for
the top 15 fastest-growing Ontario towns, comparing their density changes
across all census years from 1996 to 2021, with the percentage changes
between each period" mixes two different questions: what to **rank/select
by** (which 15 towns make the list), and what to **display** for those
towns once selected (which columns appear). Conflating the two — e.g.
ranking by whichever measure happens to sit nearest the superlative
phrase, regardless of which one the request actually frames as the
subject — silently answers a different leaderboard than the one asked
for. None of the *display* choices below are wrong on their own, but
picking any of them **without saying so** is why the same prompt can
render a genuinely different table each time — a real inconsistency, not
a stylistic one.

**"Pick one and state it" is not enough by itself** — two independent runs
can each honestly state a different pick and still diverge. Resolve the
pick with a deterministic precedence, in this order, then STATE the
result in the analytical caption note — the FIRST of the two
`tab_source_note()` calls, not the subtitle (see "TWO source notes" above)
— e.g. "ranked by overall population growth, 1996–2021":

1. **Find the ranking/selection metric FIRST, separately from the display
   columns** — it's usually the request's stated TOPIC (the noun phrase
   right after "a table showing/of...", typically at the very start),
   not whatever measure happens to sit nearest "top N"/"fastest-growing"
   in the sentence. In "showing **population growth trends** for the top
   15 fastest-growing... towns, comparing their **density changes**...",
   the topic clause names population growth — rank/select by population
   growth. "Comparing their density changes..." is a SEPARATE instruction
   about what to display for the towns already selected, not a competing
   ranking criterion, even though it sits right next to "fastest-growing."
   An explicitly named metric ("top 15 by revenue") always wins outright,
   full stop, no further judgment needed. **If the topic measure and the
   named display columns are different things** (population to rank by,
   density to display), show BOTH as columns, not just the display one —
   a table titled "population growth trends" that contains zero
   population data reads as incomplete regardless of how well it answers
   the density question.
2. **Entity/category scope: ALWAYS match the request's term to every data
   row it plausibly covers — never the narrower literal subset.**
   "Ontario towns" in ordinary usage means "Ontario municipalities"
   generically; if the data has a type/category column (e.g. `csd_type`
   with `town`/`city`/`township`/`municipality`/`village`), include every
   type, not just the rows whose type-value literally matches the
   request's word ("town-type records only" is NOT an acceptable
   alternative reading — it's the narrower literal subset this rule
   exists to rule out). State the scope in the analytical caption note
   (e.g. "all municipality types") so the choice is explicit, not because
   there are two valid options to pick between.
3. **A stated date range always means the FULL span, not a sub-period** —
   "from 1996 to 2021" compares `value_2021` against `value_1996`, never a
   single interior period, unless the request names that period
   specifically. Compare them as a **percentage/relative change**
   (`(value_2021 - value_1996) / value_1996`), not an absolute difference,
   whenever the request says "growth," "fastest-growing," or "rate" —
   ordinary usage of "fastest-growing" means highest relative growth rate
   (a small town doubling in size is "faster-growing" than a large city
   adding the same absolute headcount), the same convention "fastest-
   growing companies/cities" lists use elsewhere. Use absolute change
   instead only when the request explicitly asks for a magnitude ("added
   the most residents," "grew by the largest number"). **Guard the
   baseline first, against the ACTUAL data, not the measure's type in the
   abstract**: check whether any eligible row's starting value is actually
   zero/negative before doing anything about it — a measure that could
   theoretically go negative (profit) but happens to be positive for
   every eligible row needs no special handling at all; don't fall back to
   absolute change just because the measure's category is capable of it.
   When a real zero/negative baseline IS present: if the request left the
   metric **unstated** (just "growth"/"fastest-growing"), fall back to
   absolute change for the whole table and say so in the analytical
   caption note. If the request **explicitly** asked for a rate/percentage
   specifically, don't silently swap the whole table to a different metric
   — instead **exclude only the rows with a non-positive baseline** from
   the ranking (a rate is genuinely undefined for them, not just
   inconvenient to compute) and note the exclusion, so the metric actually
   answers what was asked for the rows it can.
4. **"Show X across all periods, with changes between each period" means
   BOTH, not one or the other** — when a request separately names the
   per-checkpoint values ("density changes across all census years") AND
   the between-period deltas ("percentage changes between each period"),
   include both as separate columns rather than picking one representation
   to stand in for the other. This is a *display* choice — it never
   overrides the ranking metric found in step 1. The baseline guard from
   step 3 applies to EVERY individual period's delta too, not just the
   overall ranking figure — a period whose starting value is zero/negative
   makes that one cell's percentage undefined, and **not always in an
   obviously-broken way**: a zero baseline computes to `inf` (`sub_missing`
   does NOT catch this — confirmed by direct test: it only substitutes
   `None`/`NaN`, so an unmasked `inf` renders as the literal text
   `"inf%"`), but a *negative* baseline computes to a finite,
   sign-reversed, equally-meaningless value (confirmed: `(5 - (-10)) /
   (-10)` = `-1.5`, i.e. "-150%" — a plausible-looking number that passes
   right through `sub_missing` uncaught). Mask on the condition, not the
   symptom: compute with `np.where(start > 0, (end - start) / start,
   np.nan)` so both the zero-baseline (`inf`) and negative-baseline
   (finite-but-meaningless) cases become `np.nan` up front — confirmed by
   direct test to render `"—"` for both — THEN call `sub_missing`, without
   discarding the rest of that row. **Use `np.nan`, not `None`, as the
   `np.where` fallback** — `sub_missing` catches both identically, but
   `None` forces the whole column to `object` dtype (NumPy has no `None`
   scalar for a float array), while `np.nan` keeps it `float64`. The
   masked column is exactly the one this section tells you to rank/sort by
   next (step 3's "exclude only the rows with a non-positive baseline from
   the ranking") — an `object`-dtype column breaks `.nlargest()`/
   `.sort_values()` with a `TypeError`, so this isn't a cosmetic
   preference, it's what makes the very next step work.

This narrows the ambiguity considerably but — being a precedence over
natural-language phrasing, not a closed-form algorithm — does not
guarantee two runs land on byte-identical column choices for every
conceivable prompt; genuinely irreducible ambiguity still gets resolved by
judgment. STATING the resolved definition (not just making the same
mechanical pick) is still what makes an individual table's numbers
reproducible and defensible on its own. Do all of this BEFORE organizing
columns — it decides which columns (and which 15 rows) exist at all, not
just how they're formatted.

## Data-cleaning gotchas (fix these before any `fmt_*`/`data_color` call)

- A currency string like `"$1,200"` or a percent string like `"12%"` is
  still a *string* — `great_tables` formats numbers, it does not parse
  them. Strip the symbol/separators and cast to `float` first.
- A `Decimal` from a SQL result should be cast to `float` (or quantized)
  before formatting — `great_tables` doesn't know how to format `Decimal`.
- A non-zero header row (extra title/blank rows above the real header) in
  a CSV needs `header=`/`skiprows=` in the read call — check the first
  parsed row is real data, not a stray label.

## Financial (money / price / revenue / cost)

Round to 2 decimals for small amounts, 0 decimals for large/whole-dollar
figures. Always a currency symbol: `fmt_currency(columns=..., decimals=0|2)`.
A single neutral magnitude column is the sequential **Blues** heatmap hero —
`heatmap(gt, "revenue", kind="sequential", hue="neutral")` — see `revenue` in
`house_table.py` — **only** when it's the hero measure the request is
actually about. Otherwise leave it plain — no fill and no bold.

## Percent / rate / change

`fmt_percent(columns=..., decimals=1)`. Decide once whether the data is
fractional (`0.12`) or already-scaled (`12`, needs `scale_values=False`),
and stay consistent for that column. A **signed** percent (year-over-year,
above/below target) is the diverging **RdYlGn** measure —
`heatmap(gt, "yoy_change", kind="diverging", hue="default")` — see
`yoy_change` in `house_table.py`. `positive=good` is the default
orientation; pass `reverse=True` only when positive genuinely means worse
(cost overrun, error rate, latency, churn).

**Any percent or signed-number column whose real data crosses zero uses
`force_sign=True`** — this is a rule, not a stylistic option. Do NOT
hand-rewrite it with `pattern="{x:+.1f}%"`. `force_sign=True` is a plain
keyword on `fmt_number`/`fmt_percent`/`fmt_currency`/`fmt_integer` (the
formatters this skill actually uses); `fmt_scientific` is the one
exception, with separate `force_sign_m=`/`force_sign_n=` keywords instead
of a single `force_sign=`.

`pattern=`'s `{x}` is a **literal substitution token** that must appear
EXACTLY as `{x}` — it is not a Python format-spec slot, so
`great_tables` does a plain string-replace of the substring `{x}`, not an
f-string evaluation. Write `:+.1f` (or any format spec) inside the braces
and the substring no longer matches `{x}` at all, so **nothing gets
replaced and every cell renders the literal text `{x:+.1f}%`** — silently,
with no exception raised. Confirmed by direct test:
`fmt_number(columns="x", pattern="{x:+.1f}%")` renders literal
`{x:+.1f}%` in every cell. For a genuine **percent** column, fix it with
`fmt_percent`, not a `fmt_number` + manual `%` suffix (a `%`-suffixed
`fmt_number` call is cosmetically similar but semantically wrong for a
percent value — it skips `fmt_percent`'s scale handling and locale-aware
percent formatting, contradicting this section's own rule above):
`fmt_percent(columns="x", decimals=1, scale_values=False,
force_sign=True)` renders `+86.5%` / `−12.3%` correctly for already-scaled
inputs like `86.5` (`scale_values=True`, the default, is for fractional
inputs like `0.865`) — `decimals=` still needs to be passed explicitly (it
defaults to `2`, so omitting it here would render `+86.50%`, not
`+86.5%`); `pattern=` is only for wrapping the
already-formatted number in literal text (a unit suffix, parentheses,
etc.), never for a format spec.

## Ranking / rank / position

Plain integers, no decimals, no color — `fmt_integer(columns="rank")`, see
`rank` in `house_table.py`. A rank's information is its *order*, not its
magnitude: never `data_color`/`heatmap` a rank column.

## Categorical status / binary state

Never `data_color`. Use `status_chip(gt, column, meaning)` with an explicit
value → `"good"`/`"bad"`/`"neutral"` map — see `status` in
`house_table.py`. The rule made explicit: a red/green column always means
good/bad, whether it's continuous (a heatmap) or discrete (a status chip)
— color is never decorative.

## Row identifiers (name / date / ID)

Becomes the stub: `rowname_col=...`, default ON whenever a column holds
row identifiers. `tab_stubhead(label=...)` requires the stub to already
exist — see the `product` column / `tab_stubhead("Product")` call in
`house_table.py`.

## Natural grouping category

`groupname_col=...` + `group_emphasis(gt, hue=...)` when the prompt names
a grouping dimension, or a low-cardinality categorical is the organizing
story — see `region` / `group_emphasis` in `house_table.py`.

## Unified color theme — the band/stub/group/stripe hierarchy

Branding surfaces (the column-label band and the stub) are fixed to the
same navy/Blues family by default — this is a branding
decision, not the same data-driven, per-measure hue selection used for a
heatmapped measure's own fill color. Branding never adopts a heatmap's
semantic hue (a "more is better" green heatmap elsewhere never turns the
header green). `hue=` stays available as an escape hatch on
`band()`/`stub_tint()` for the rare table with an explicit reason to
diverge, but it is not a default decision point. Only ONE row deserves its
own distinct, highlighted treatment: a summary/total row (see below).
Column labels, the stub, and group headers are all quieter than that, and
quieter than each other:

1. **Column-label band** — `band(gt, hue=...)` — the house DEFAULT is now
   `shade="dark"` (a solid `accent` fill, `#08306B` for navy, + bold white
   text), ALWAYS, regardless of whether the table has a heatmap. This is a
   branding surface, not a data surface — it stays the same deep navy
   whether the table's own heatmap is Blues, Reds, RdYlGn, or nothing at
   all. (Earlier guidance reserved `shade="dark"` for a no-heatmap table
   and defaulted colored tables to the lighter `accent_tint` band instead;
   that's no longer the house convention — every current reference table
   uses the dark band, with or without a heatmap present.)
2. **Stub** — `stub_tint(gt, hue=...)` — the quieter `washed` tint of the
   SAME fixed navy/Blues family as the band. A narrower, secondary surface
   next to the more prominent band, so it stays subtler rather than
   competing with it.
3. **Group headers** — `group_emphasis(gt)` — bold weight + the `#BDBDBD`
   structural rule ONLY, deliberately **no background fill**. A group
   label is a section break, not a result worth its own highlight.
4. **Row stripe** — `stripe(gt)` — always the flat neutral grey, NEVER
   tinted to the table's hue (unlike band/stub) — an alternating tinted
   fill reads as busy across many rows in a way a single flat surface
   doesn't.

Pass the SAME hue to `band()`/`stub_tint()` so the theme reads as one
thing. This hierarchy is what keeps the heatmap the star: nothing in the
structural furniture is as loud as a heatmap's own gradient (pale to deep,
varying row by row), which stays the only element on the page that
visually "moves." See `house_table.py`'s `band(gt, hue="navy")` /
`stub_tint(gt, hue="navy")` / `group_emphasis(gt)` / `stripe(gt)` calls for
the worked example.

## Summary / total rows

Add **only** when the request implies totals/aggregates; don't invent one
otherwise. For a whole-table grand total, use `great_tables`' native
`gt.grand_summary_rows(fns={"Total": ...})` + `tab_style(...,
locations=loc.grand_summary())` — see the `Total` row in `house_table.py`.
It's structurally separate from any `groupname_col` section (no fake group
label needed) and it's excluded from `data_color`'s domain automatically.
Sum only the columns that are meaningfully summable (`units_sold`/`revenue`
in the demo; `yoy_change`/`status`/`rank` are left blank via `missing_text`
because summing them is meaningless). Reach for the `summary_row(gt,
row_index, bold=True)` helper only when a total must live inline as an
ordinary data row instead (e.g. a per-group subtotal positioned among that
group's own rows) — `grand_summary_rows` always places its total(s) at the
very top or bottom of the whole table, never inline.

## Missing values

Always `sub_missing(columns=..., missing_text="—")` — never a raw blank
cell. See the injected `yoy_change` gap on `Zeta Kit` and the blank
`Total` row cells in `house_table.py`.

## Color restraint — no numeric cap, and no bold/text-color step-down

An earlier version of this rule capped colored measures at a fixed count;
that numeric ceiling was rejected as arbitrary and is gone. There is no
numeric cap on colored measures — color what the request is actually
about, using the correct palette for each. Which measure(s) that is, when
2+ measures are named with no explicit ranking, is decided by `data.md`'s
tie-break section — this restraint rule doesn't re-decide that, it only
says what happens to whichever measure(s) that tie-break doesn't pick: no
fill, but also no bold or text-color consolation. Any measure that isn't part of
what the request is about renders fully plain: no fill, no bold, no
text-color treatment of any kind. This applies regardless of how many
other measures already carry a color fill — a table with 2, 3, or more
colored measures still leaves every remaining measure completely plain.

A still-earlier version of this rule tried to soften "plain" into "bold
text/text-color instead of a fill" for a measure that had lost a
fill-priority tie-break. That mechanic is wrong and is not part of this
skill, in any narrow or broad form: three of the six ground truths in
this corpus state explicitly, in the author's own words, that a
non-fill-winning measure renders plain, not bold —
`airquality_monthly_summary.py` ("Wind stays plain text -- no bold, no
fill -- by author direction"), `towny_growth_trends.py` ("Rank / Total
Growth % stay plain text -- no bold -- by author direction"), and
`sp500_monthly_performance.py` ("open / close stay plain, uncolored text
(not bold..."). `towny_growth_trends.py` keeps its ranking measure and
`rank` column plain even alongside 2 full heatmap blocks elsewhere in
that same table. Do not bold or tint any measure that isn't itself
getting a fill, no matter how many measures already have one and no
matter how plausible a fill candidate it was. `sp500_monthly_performance.py`'s
top-5/bottom-5 bold-text mechanic is a different, answer-key-specific
stretch goal this skill does not teach as a general rule — don't
generalize its *effect* (bolding a named subset) into this restraint
clause. A pure categorical/text table still gets no fill at all — its
anchor is the heading band, which is `band(gt, shade="dark", hue=...)`
regardless (see "Unified color theme" above — dark is the universal
default now, not a no-heatmap-only fallback). `house_table.py` uses 2
full heatmaps: `revenue` (sequential) and `yoy_change` (diverging);
`status` is a 3rd color story but a categorical chip, not a heatmap.

## Global constants

Frame/save/title/subtitle are covered by "THE NON-NEGOTIABLE BASE" at the
top of this file — this section is just the remaining fit-and-finish
constants:

- Header alignment: title + subtitle centered (`tab_header`'s default).
- Font size: shrink only as a last resort, in this order — bigger canvas
  (`gtsave(vwidth=..., vheight=...)`) → higher zoom (`gtsave(zoom=...)`) →
  smaller font.
- Column widths & padding: `cols_width(cases={...})` sized to each
  column's content plus a small buffer — don't let auto-layout stretch a
  narrow column; pair with the six pinned `tab_options` padding values
  (`heading_padding="6px"`, `column_labels_padding="6px"`,
  `column_labels_padding_horizontal="8px"`, `data_row_padding="5px"`,
  `data_row_padding_horizontal="8px"`, `source_notes_padding="6px"`) —
  see `house_table.py`'s `cols_width`/padding block.
- Column order: the primary heatmapped measure sits in the first value
  column or two, or last — never buried among trailing categorical/rank
  columns; which edge depends on narrative sequencing (context/input
  columns precede a derived-outcome column).
