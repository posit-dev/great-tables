# Palettes — the single source of truth for every color hex

Load this whenever you pick a Big-Color fill, a heading-band hue, or any
Small-Color surface (Step 3, 4, or 5). Every hex the skill uses lives here.

There are **three tiers**: a fixed **branding tier** for the header band / stub tint /
row stripe (§0), the Dark Academia solids for other non-gradient Big-Color treatments
plus their washed tints (§1–§2), and the sequential/diverging palettes for a
heatmapped measure's own fill (§3). §1–§3 stay deliberately linked (the Small-Color
tints are washed-out versions of the Big-Color solids); §0 never varies by table.

---

## 0. Branding tier — fixed branding surfaces, every table

The heading band, stub tint, and row stripe are a **branding tier** (navy heading
band, pale-blue stub tint, neutral-grey row stripe): the same three hexes on every
table, always. Only the header band and stub tint are part of the Blues/navy family
— the row stripe (`#F6F6F6`) is a pure neutral grey (equal R/G/B), not a blue tint,
and should not be "corrected" toward one.

| Branding surface | Hex |
|---|---|
| Header band | `#08306B` |
| Stub tint | `#EAF0F6` |
| Row stripe | `#F6F6F6` |

These do **not** follow the same *data-driven, per-measure* hue selection used for a
heatmapped measure's own fill (§3 below): a heatmapped measure still resolves its own
hue by semantic — `Greens` for "more is better," `Reds` for "more is worse," `Blues`
for a neutral magnitude — but the branding surfaces around it always resolve to these
same fixed values regardless of what hue that measure ends up using. The header band
and stub tint default to Blues/navy specifically; the row stripe is a separate,
neutral-grey fixed value, not part of that hue family. None of the three is a
harmonization step that adapts per table, and a heatmap's own hue never overrides any
of them.

---

## 1. Dark Academia — SOLID Big-Color palette (Warm set)

Used for **every non-branding Big-Color treatment that is not a gradient / heatmap /
diverging fill**: full-column fills, full-row highlights, status fills, colored-text
anchors. (The heading band is the fixed branding surface in §0 above — it no longer
draws its hue from this table.) **White text on all solid members.**

| Member | Solid hex | Washed light tint | Use when… |
|---|---|---|---|
| **Navy** | `#22384F` | `#EAF0F6` | **Default** with no other cue |
| Forest | `#2F4A38` | `#EAF1EC` | Nature, growth, environment, money/finance |
| Oxblood | `#5C2E2E` | `#F5EBEB` | Risk, alerts, deficits, intensity (non-diverging) |
| Espresso | `#4A3A2C` | `#F1EADD` | Historical, literary, food/wine, vintage |
| Ochre (accent) | `#9A7B33` | `#F5EFDC` | Premium / awards / highlight |
| Tan (accent/mid) | `#8A7452` | `#EFE7D6` | Secondary warm accent (cream tint) |

### DA hue-selection rule (applies to any solid DA use — full-column fill, full-row highlight, status fill, colored-text anchor)

Resolve to **exactly one** hue — this is a deterministic lookup, **not** a
harmonization. **Default Navy.** Otherwise walk this priority order and **pick the
FIRST that applies**, then stop (do not blend hues):

1. any heatmap/gradient palette hue already present in the table — match its family,
2. the data source's subject — per the "Use when…" column of the table above,
3. any other color already used in the table.

If none applies, the hue **is Navy**. One coherent theme per table — the same table
cues resolve to the same hue on every run.

---

## 2. Small Color — light structural surfaces (neutrals)

Quiet surfaces that are **not** part of the branding tier (dividers, hairlines, empty
cells, group rules) draw from the neutral greys below — never a saturated color. The
heading band, stub tint, and row stripe are the fixed branding-tier values from §0,
not entries in this table.

| Neutral role | Default hex | Weight |
|---|---|---|
| Cell hairline (between rows) | `#E8E8E8` | 1px |
| Column-label bottom rule | `#CCCCCC` | 2px |
| Group / summary structural rule | `#BDBDBD` | — |
| Column-group vertical divider | `#D0D0D0` | light but easily noticeable |
| NA / empty cell | `#808080` | `na_color=` fill; `sub_missing("—")` text |

### The grey-budget rule — retired

This rule used to promote the stub tint or the heading band to a washed tint of the
table's own Big-Color hue when several grey surfaces stacked up and looked
monotonous. It no longer applies: the heading band, stub tint, and row stripe are now
the fixed branding constants in §0 — they never vary by table, so there is nothing
left to harmonize or re-balance.

---

## 3. Sequential / Diverging — for a heatmapped MEASURE's own fill

Used when a measure is a magnitude / trend / signed story. These are matplotlib /
brewer palette **names** passed to `data_color(palette=…)`, not fixed hexes. This is
the per-measure, data-driven hue selection that the branding tier (§0) is
specifically exempt from.

### Sequential — fixed hue per semantic (F-deterministic-branch)

This is a **lookup, not a menu.** Read the measure's semantic, take that row's
palette. There is **no choice** and no coin-flip — the same semantic resolves to the
same hue on every run.

| Measure semantic | Palette |
|---|---|
| money · price · revenue · cost · volume · count · population · size — any **neutral magnitude** with no inherent good/bad direction | **`Blues`** — always |
| growth · gain · improvement · "more is better" | **`Greens`** |
| loss · risk · warning · worse · error rate — "more is worse" | **`Reds`** (`Oranges` = documented alternate only, when `Reds` clashes with another hue already in the table) |

A **single** neutral magnitude (money/price/volume/count/population) is **always
`Blues`** — never Greens. `Greens`/`Reds` are reserved for measures that carry an
explicit direction. This removes the Blues-vs-Greens coin-flip. (For the case of **two**
neutral magnitudes in one table, which would both want `Blues`, see the neutral
tie-breaker under "Rules for the colored measures" below.)

### Diverging (signed values)

`RdYlGn` **default**. Orientation is computable, not assumed: positive = good ⇒
`RdYlGn` (green = positive); **positive = bad** (cost/variance-over-budget, error,
defect, latency, delay, downtime, churn — "more is worse") ⇒ `RdYlGn` with
`reverse=True` (green = negative). `RdBu` / `PuOr` colorblind-safe alternatives. The
symmetric domain `[-M, M]` is identical in both orientations — see
`big_color/diverging_fill.md` for the full test.

### Rules for the colored measures

- **Consistency within a measure:** every column of a measure shares the **same
  palette and the same `domain`** — one `data_color` domain spanning all facet
  columns, not per-column domains.
- **Diverging domain:** **symmetric around 0**, covering the full data range, with
  `truncate=False` so out-of-range values keep the most extreme color rather than
  disappearing. (e.g. data −30 → +40 ⇒ `domain=[-40, 40]`.)
- **Two sequential measures:** give them **two distinct semantic hue families —
  never the same** (e.g. `Greens` + `Blues`, not `Blues` + `Blues`). When each measure
  carries its own direction, the semantic lookup already yields distinct hues.
- **Two NEUTRAL measures (the tie-breaker):** two same-semantic neutral magnitudes
  (e.g. price + volume, horsepower + price) both resolve to `Blues` by the lookup, which
  would violate "distinct hues". Resolve deterministically: the **primary** neutral
  measure keeps **`Blues`**; the **secondary** takes the next entry from the pinned
  ordered fallback ladder **`Blues → Greens → Oranges`** (i.e. the second neutral →
  `Greens`; a third — reached only if a table gives three neutral measures a full fill
  at once, which is unusual but not disallowed — → `Oranges`). `Reds` is excluded from
  this ladder (reserved for a directional "worse" measure). The ladder is applied for
  **distinctness only**; the fallback hue carries no good/bad meaning here.
  - **Which measure is "primary" (total, computable order):** (1) the measure the
    prompt names/emphasises first, in prompt order; else (2) leftmost-first by DataFrame
    column order. This is the SAME priority order used to rank which measures earn a
    full heatmap fill first (`big_color/column_gradient_fill.md`), so both runs assign
    the same palettes to the same columns.
- **Non-gradient Big Color uses the Dark Academia solids** (§1), hue per the
  DA hue-selection rule — never these sequential/diverging palettes.
