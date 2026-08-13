"""house_table.py — the "house format" reference table AND its helper module.

This file is two things at once:

1. **A reusable helper module.** ``PALETTE`` and the functions below are meant
   to be imported into a real table script:

       from house_table import PALETTE, frame, hairlines, finalize, band, \
           stripe, stub_tint, heatmap, status_chip, summary_row, \
           group_emphasis, humanize_labels

2. **The one worked example.** Running this file directly
   (``python house_table.py``) builds a single synthetic "Regional Product
   Line Performance" table that exercises every generic formatting feature
   the skill covers — stub, groups, spanners, a sequential heatmap, a
   diverging heatmap, categorical status chips, a summary row, striping,
   stub tint, band, frame, hairlines, footnote, source note, and a missing
   value — and
   saves it to ``house_table.png`` next to this script.

THE NON-NEGOTIABLE BASE (see ``references/RULES.md`` for the full rule):
every table gets ALL of — (1) a title AND subtitle, (2) TWO source notes
(an analytical caption stating the finding or the chosen definition for an
ambiguous measure, THEN a separate provenance note — a generic provenance
note if the real one is unknown, never omitted), (3) the boxed frame
(``frame(gt)``), (4) Big Color kept restrained — the ``heatmap()``/
``data_color()`` calls target only the measure(s) the request is actually
about, never one heatmap per numeric column; there is no numeric cap on
colored measures, and any measure that isn't part of what the request is
about renders fully plain (no fill, no bold, no text-color treatment of
any kind), regardless of how many other measures already carry a color
fill (see ``references/RULES.md``'s "Color restraint"), (5) the body-row
``hairlines(gt)`` rule (a completely separate `great_tables` option family
from the outer ``frame()`` border — `great_tables` already renders a raw
gray hairline by default, so skipping this call leaves an otherwise
well-colored table in the wrong, unbranded gray rather than undivided),
and (6)
``finalize(gt, path="table.png")`` as the final call. These six are
unconditional, unlike the stub/group/spanner/status-chip/summary-row
choices below, which stay genuinely data-dependent — and unlike striping
(conditional on full heatmap coverage, see ``stripe()`` below), which
stays a gate you must evaluate every time, not skip. Importing a helper
(``stripe``, ``stub_tint``, ``humanize_labels``, ...) and then not calling
it is fine when its own gate doesn't fire; skipping one of the six items
above because your table "didn't seem to need it" is not — small polish
(hairlines, a stub tint, striping when its gate fires) matters just as
much as the big colored measures, and the demo below hits all six
unconditional items every time for exactly this reason.

Why a single script instead of a flowchart and per-shape reference files? That
design solves "same input -> same output" with a **procedure**: a numbered
decision sequence plus a directory of archetype examples to route to. This
skill solves the same problem with a **worked example**: read this file once,
find the block that matches your data's shape (a magnitude column, a
percent column, a status column, a group, a summary row, ...), copy/adapt
it, and look up the matching row in ``references/RULES.md`` for the one
formatting rule that block encodes. There is no router file and no
per-archetype directory — this script IS the one example, annotated in
place.

The ``solid`` / ``washed`` / ``neutral`` / ``sequential`` / ``diverging``
tiers of ``PALETTE`` below reuse an already-validated hue system, deliberately
rather than inventing a new one. The ``accent`` / ``accent_tint`` tiers are new
to THIS skill: a
brighter, more saturated pairing modeled on `great_tables`' own built-in
``opt_stylize()`` presets (styles 3 and 6 in particular) — a solid,
clearly "branded" header band and clean, clearly-differentiated status
colors, rather than a barely-there wash. ``accent`` backs the
column-label band's solid fill under the house-default
``band(gt, shade="dark")`` AND ``status_chip()``'s good/bad/neutral
fills; ``accent_tint`` backs the band's lighter fill under
``band(gt, shade="light")``. Neither tier is used by ``stub_tint()``
(always the quieter ``washed`` tier, so the stub stays subtler than the
band) or by ``group_emphasis()`` (bold weight + a neutral structural rule
only, no fill at all). See ``band()``/``stub_tint()``/``status_chip()``/
``group_emphasis()`` below for exactly how each tier is used.
"""

from __future__ import annotations

import pandas as pd
from great_tables import GT, loc, md, style

# ---------------------------------------------------------------------------
# PALETTE — the single source of truth for every color this skill uses. Do
# not invent new colors elsewhere; change a hex here if it needs to change.
# ---------------------------------------------------------------------------
PALETTE = {
    # Dark Academia SOLID Big-Color palette (white text on every solid). Each
    # hue exists for a specific subject-matter cue, not decoration — see the
    # "Use when..." comment on each entry. Navy is also the fixed default for
    # BRANDING surfaces (band()/stub_tint()) specifically, because Blues/navy
    # is the standard house hue for branding — not because it's re-derived by
    # matching whichever hue a heatmapped measure elsewhere in the table
    # happens to use (see references/RULES.md's "Unified color theme").
    "solid": {
        "navy": "#22384F",  # default with no other cue
        "forest": "#2F4A38",  # nature, growth, environment, money/finance
        "oxblood": "#5C2E2E",  # risk, alerts, deficits, intensity
        "espresso": "#4A3A2C",  # historical, literary, food/wine, vintage
        "ochre": "#9A7B33",  # premium / awards / highlight (accent)
        "tan": "#8A7452",  # secondary warm accent / mid (cream tint)
    },
    # The washed light tint paired with each solid above (same keys). Used
    # for the stub's quiet tint (`stub_tint()`) — navy/Blues is the fixed
    # branding default here because Blues is the standard house hue for
    # branding, not a tint re-derived by matching whichever solid hue a
    # heatmapped measure elsewhere in the table happens to use.
    "washed": {
        "navy": "#EAF0F6",
        "forest": "#EAF1EC",
        "oxblood": "#F5EBEB",
        "espresso": "#F1EADD",
        "ochre": "#F5EFDC",
        "tan": "#EFE7D6",  # cream
    },
    # Brighter, more saturated pairing used for the column-label band's solid
    # fill under the house-default `band(gt, shade="dark")` AND for
    # `status_chip()`'s good/bad/neutral fills — modeled on great_tables' own
    # opt_stylize() styles 3/6 (a solid, clearly-branded header band, paired
    # with clean, clearly-differentiated status colors, not a barely-there
    # wash). NOT used by `stub_tint()` (always the quieter "washed" tier
    # below, so the stub stays subtler than the band) or by
    # `group_emphasis()` (bold weight + a neutral structural rule only, no
    # fill at all).
    "accent": {
        "navy": "#08306B",
        "forest": "#2E7350",
        "oxblood": "#A23A3A",
        "espresso": "#8A6238",
        "ochre": "#B8912E",
        "tan": "#9C8258",
    },
    # The visibly-tinted (not barely-there) light pairing for "accent" above —
    # used for the column-label band when `band(gt, shade="light")` is
    # chosen (the house DEFAULT is `shade="dark"`, which paints the band with
    # the solid "accent" tier itself instead — see band()'s docstring). NOT
    # used for the stub (`stub_tint()` always uses the quieter "washed" tier
    # below) or for group headers (`group_emphasis()` applies bold + a rule
    # only, no fill at all). The row stripe is a third, separate tier
    # entirely — the flat, never-tinted "neutral" grey (see stripe()).
    "accent_tint": {
        "navy": "#C9E0F0",
        "forest": "#CFEAD9",
        "oxblood": "#F4D6D6",
        "espresso": "#EEDFC7",
        "ochre": "#F6E8BE",
        "tan": "#EFE3CE",
    },
    # Neutral structural surfaces (light greys) — the default for every quiet
    # surface when there's no Big-Color hue to harmonize to.
    "neutral": {
        "label_band": "#F0F0F0",  # light label band
        "row_stripe": "#F6F6F6",  # row stripe
        "hairline": "#E8E8E8",  # cell hairline between rows, 1px
        "column_label_rule": "#CCCCCC",  # column-label bottom rule, 2px; also the frame border
        "structural_rule": "#BDBDBD",  # group / summary structural rule
        "vertical_divider": "#D0D0D0",  # column-group vertical divider
        "na_cell": "#808080",  # NA / empty cell fill
    },
    # Sequential palette NAMES (matplotlib/brewer), keyed by semantic
    # meaning — passed to data_color(palette=...), never a fixed hex. A
    # single neutral magnitude (money/price/volume/count) is always "Blues";
    # Greens/Reds are reserved for measures with an explicit direction.
    "sequential": {
        "positive": "Greens",  # growth / "more is better"
        "warning": "Reds",  # worse / "more is worse"
        "warning_alt": "Oranges",
        "neutral": "Blues",  # volume / count / price / population
    },
    # Diverging palette NAMES for signed values. RdYlGn is the default
    # (green = good); reverse it only when positive genuinely means worse.
    "diverging": {
        "default": "RdYlGn",
        "colorblind_safe": ["RdBu", "PuOr"],
    },
}


# ---------------------------------------------------------------------------
# Reusable helpers. Every helper takes the DECISION as an argument (which
# columns, which hue, light vs dark, good/bad/neutral, ...) — none of them
# choose anything themselves. That mirrors gt_consistency.py's philosophy:
# the model decides *what*, the helper only guarantees *how* it's executed
# is identical every time it's called with the same arguments.
# ---------------------------------------------------------------------------


def humanize_labels(gt, df, overrides=None):
    """Turn snake_case column names into Title Case via ``cols_label``.

    WHAT: relabels every column of ``df`` from its snake_case name (e.g.
    ``yoy_change``) to a human Title Case label (``Yoy Change``), then
    applies ``overrides`` on top for anything the naive rule gets wrong —
    an acronym that shouldn't title-case letter-by-letter ("YoY", not
    "Yoy"), a currency/unit suffix, or any label an explicit request names.

    WHY: naive Title Case is right often enough to not deserve a decision
    every time, but wrong often enough (acronyms, units) that it needs an
    escape hatch — ``overrides`` is that hatch, applied last so it always
    wins.
    """
    overrides = overrides or {}
    labels = {}
    for col in df.columns:
        labels[col] = overrides.get(col, col.replace("_", " ").title())
    return gt.cols_label(**labels)


def frame(gt, color=None, width="1px", style="solid"):
    """Apply the boxed enclosing border on all four sides.

    WHAT: sets the table's top/bottom/left/right border color, width, and
    style identically.

    WHY: ``great_tables`` defaults the *left/right* border style to
    ``"none"`` — setting only ``color``/``width`` would leave the side
    borders invisible and render only top/bottom rules, not a box. The
    style must be set explicitly on all four sides to get an actual frame.
    Defaults to the neutral ``#CCCCCC`` used as the frame color everywhere
    in this skill (see ``references/RULES.md``'s "Global constants").
    """
    if color is None:
        color = PALETTE["neutral"]["column_label_rule"]
    return gt.tab_options(
        table_border_top_style=style,
        table_border_top_color=color,
        table_border_top_width=width,
        table_border_bottom_style=style,
        table_border_bottom_color=color,
        table_border_bottom_width=width,
        table_border_left_style=style,
        table_border_left_color=color,
        table_border_left_width=width,
        table_border_right_style=style,
        table_border_right_color=color,
        table_border_right_width=width,
    )


def hairlines(gt, color=None, width="1px", style="solid"):
    """Pin the body-row hairline to the house palette's neutral hex.

    WHAT: sets ``table_body_hlines_style``/``_color``/``_width`` — the thin
    rule BETWEEN ordinary rows. `great_tables` renders this line ON BY
    DEFAULT (``style="solid"``, ``color="#D3D3D3"``) even if nothing ever
    calls this helper — the gap this closes is not "no line at all," it's
    "the raw library default gray instead of the house palette's specific
    washed neutral" (``PALETTE["neutral"]["hairline"]``, ``#E8E8E8``).

    WHY this is its own helper, not folded into ``frame()``: a hairline is a
    body-row separator, a completely different `great_tables` option family
    from ``frame()``'s outer table border — conflating the two, or assuming
    `frame()` already covers it, is how a table ends up with a boxed
    outline and the library's raw default gray between rows instead of a
    deliberately-chosen house tone. This is UNCONDITIONAL — every table
    gets it, the same as `frame()` and the heading band's bottom rule,
    regardless of row count or whether the table has Big Color. See
    ``references/RULES.md``'s "THE NON-NEGOTIABLE BASE".
    """
    if color is None:
        color = PALETTE["neutral"]["hairline"]
    return gt.tab_options(
        table_body_hlines_style=style,
        table_body_hlines_color=color,
        table_body_hlines_width=width,
    )


def finalize(gt, path="table.png", **overrides):
    """Save the table with the house-format ``gtsave`` defaults.

    WHAT: calls ``gt.gtsave(path, expand=15, zoom=2.0, **overrides)`` — a
    raised outer margin and a retina zoom, with any keyword in
    ``overrides`` (e.g. ``vwidth``/``vheight``) taking precedence.

    WHY ``path`` defaults to ``"table.png"``: that's the mandatory renderer
    target this skill (and the harness that runs it) expects — see
    ``SKILL.md``'s "The mandatory renderer" section. A real table script
    that imports this helper and calls ``finalize(gt)`` with no explicit
    path should produce the expected file, not silently write something
    else. The demo below passes an explicit ``path="house_table.png"`` to
    override this default, since its output is the reference render, not a
    generated table.

    WHY the other defaults: the default 5px ``gtsave`` margin crowds the
    frame border against the image edge; ``zoom=2.0`` keeps text crisp at
    normal viewing sizes. If a table renders too big, grow room/zoom before
    ever shrinking font size (see ``references/RULES.md``'s font-size fit
    order).
    """
    opts = {"expand": 15, "zoom": 2.0}
    opts.update(overrides)
    return gt.gtsave(path, **opts)


def band(gt, *, shade="dark", hue):
    """Apply the heading band (light tint or dark solid) + the mandatory rule.

    WHAT: ``shade="dark"`` (the house DEFAULT) paints the column-label
    background with the ``accent`` solid for ``hue`` and whitens the
    column-label (and spanner-label, if any) text — a fully "branded"
    look. ``shade="light"`` instead paints it with the ``accent_tint`` of
    ``hue`` (or the neutral grey band when ``hue="grey"``) — a
    clearly-visible but not solid surface; no white-text override needed.
    Either way, the 2px ``#CCCCCC`` column-label bottom rule AND bold
    column-label text are ALWAYS applied, regardless of shade.

    WHY dark is the default: every current reference table uses the same
    deep, branded navy header regardless of whether the body has a
    heatmap — the header is a fixed branding surface, not something that
    should fade into a lighter tint just because a heatmap is also present
    elsewhere on the table. (An earlier version of this skill defaulted to
    ``shade="light"`` specifically so the header wouldn't compete with a
    heatmap; that reasoning no longer matches the house convention. Reach
    for ``shade="light"`` only if you have an explicit reason to want the
    quieter tint instead.)

    NOTE the default ``shade="dark"`` band uses the solid ``accent`` tier
    (the most visible option) while ``stub_tint()`` always uses the quieter
    ``washed`` tier. The band is the more prominent surface (it spans every
    column and sits right under the title), so it carries the most-visible
    fill; the stub is a narrower, secondary surface and stays quieter so it
    doesn't out-compete the band above it. (``shade="light"`` paints the
    band with the lighter ``accent_tint`` tier instead of the default's
    solid ``accent`` — still more visible than the stub's ``washed`` tint
    either way.)
    """
    rule = PALETTE["neutral"]["column_label_rule"]
    options = {
        "column_labels_border_bottom_color": rule,
        "column_labels_border_bottom_width": "2px",
        "column_labels_border_bottom_style": "solid",
        # Bold column labels, always, regardless of shade -- every current
        # ground truth sets this alongside the background color; it was
        # missing here entirely, so a candidate relying on this helper
        # ALONE (no separate explicit `column_labels_font_weight=`) never
        # actually got the bold header every ground truth has.
        "column_labels_font_weight": "bold",
    }
    if shade == "light":
        if hue == "grey":
            options["column_labels_background_color"] = PALETTE["neutral"]["label_band"]
        else:
            options["column_labels_background_color"] = PALETTE["accent_tint"][hue]
        return gt.tab_options(**options)
    if shade == "dark":
        options["column_labels_background_color"] = PALETTE["accent"][hue]
        gt = gt.tab_options(**options)
        locations = [loc.column_labels()]
        spanners = getattr(gt, "_spanners", None)
        if spanners:
            spanner_ids = [s.spanner_id for s in spanners]
            if spanner_ids:
                locations.append(loc.spanner_labels(ids=spanner_ids))
        return gt.tab_style(style=style.text(color="white"), locations=locations)
    raise ValueError("band(): shade must be 'light' or 'dark', got %r" % (shade,))


def stripe(gt):
    """Apply zebra row striping in the flat neutral stripe hex — always grey.

    Deliberately NOT tinted to the table's hue, even when the table has a
    unified color theme elsewhere (band/stub) — an alternating tint reads
    as busy across many rows in a way a single flat band/stub surface
    doesn't, and grey is quiet enough to never compete with a heatmap.

    THE GATE (this function does not check it — the caller must): apply
    striping by DEFAULT, regardless of row count. Skip it only when the
    body's visible non-stub/non-group columns are ALREADY 100% covered by
    `data_color`/`heatmap` fills — a heatmap that paints every real cell
    leaves no plain cell for a stripe to ever show through on. A row-count
    floor is NOT part of this gate (a 5-row table still stripes).
    """
    return gt.opt_row_striping().tab_options(
        row_striping_background_color=PALETTE["neutral"]["row_stripe"],
    )


def stub_tint(gt, *, hue):
    """Tint the stub background so row labels separate from the value columns.

    ``hue="grey"`` uses the neutral label-band grey (the default with no
    Big Color). Any other hue key (``navy``/``forest``/``oxblood``/
    ``espresso``/``ochre``/``tan``) uses that hue's ``washed`` tint — the
    quieter tier (NOT ``accent``, which ``band()`` uses by default under
    ``shade="dark"`` — or ``accent_tint``, which ``band()`` uses under
    ``shade="light"``): the stub is a narrower, secondary surface next to
    the more prominent column-label band, so it stays subtler than the
    band rather than competing with it.
    Pass the SAME hue as ``band()`` — branding surfaces default to the
    fixed navy/Blues family regardless of which hue a heatmap elsewhere on
    the table happens to use; this is a branding decision, not something
    re-derived from the body's own data-driven color.
    """
    if hue == "grey":
        color = PALETTE["neutral"]["label_band"]
    else:
        color = PALETTE["washed"][hue]
    return gt.tab_style(style=style.fill(color=color), locations=loc.stub())


def _is_missing(value):
    """True if ``value`` is a missing scalar — ``None`` / NaN / ``pd.NA`` / null.

    ``value != value`` is ``True`` for float NaN, but pandas' *nullable*
    dtypes (``pd.NA``) make ``pd.NA != pd.NA`` return ``pd.NA`` itself, and
    ``bool(pd.NA)`` raises (its truth value is ambiguous) rather than
    returning ``False`` — so a bare ``value != value`` check silently
    crashes on nullable columns instead of just being wrong. The ``except``
    below treats that ambiguity as "yes, missing."
    """
    if value is None:
        return True
    try:
        return bool(value != value)
    except (TypeError, ValueError):
        return True


def _column_min_max(data, cols):
    """Return ``(lo, hi)`` as floats across every column in ``cols``, skipping NaN/NA.

    A column that is entirely missing yields NaN (float dtype) or ``pd.NA``
    (nullable dtype) from ``.min()``/``.max()`` — never a plain Python
    ``None`` — so a naive ``is None`` guard lets a ``[nan, nan]`` domain
    through, and ``float(pd.NA)`` raises outright. Skip any column whose
    min/max is missing; raise a clear error only if EVERY selected column is
    entirely missing (no numeric extent exists to build a domain from at
    all), rather than an opaque numpy/pandas crash.
    """
    lo = None
    hi = None
    for col in cols:
        series = data[col]
        c_min, c_max = series.min(), series.max()
        if _is_missing(c_min) or _is_missing(c_max):
            continue
        c_min, c_max = float(c_min), float(c_max)
        lo = c_min if lo is None else min(lo, c_min)
        hi = c_max if hi is None else max(hi, c_max)
    if lo is None or hi is None:
        raise ValueError(
            "heatmap(): every selected column %r is all-missing (no numeric "
            "values to build a domain from)" % (cols,)
        )
    return lo, hi


def heatmap(gt, columns, *, kind, hue, domain=None, reverse=False):
    """Color one measure's column(s) by value — the mechanical half of Big Color.

    ``columns``: str or list of column names colored together under one
    shared domain/palette, so multi-column facets of the same measure stay
    comparable.

    ``kind``: ``"sequential"`` (a plain magnitude, no inherent direction) or
    ``"diverging"`` (a signed value where negative/positive both matter).
    This function does NOT infer ``kind`` from the data's sign — that is
    the model's decision.

    ``hue``: a semantic key resolved against ``PALETTE["sequential"]`` /
    ``PALETTE["diverging"]`` (e.g. ``"neutral"`` -> Blues, ``"default"`` ->
    RdYlGn), or any other string, passed straight through as an explicit
    palette NAME.

    ``domain``: when ``None``, computed from ``columns`` across the GT's own
    data (missing-only columns are skipped rather than crashing — see
    ``_column_min_max``) — sequential gets the full ``[min, max]``;
    diverging gets a **symmetric** ``[-M, M]`` with ``M = max(abs(min),
    abs(max))``. Pass an explicit ``domain`` to override (e.g. to exclude a
    summary/total row from the color scale so it doesn't compress the real
    data's range — see ``revenue`` in ``build_house_table`` below for
    exactly this case).

    ``reverse``: for a **diverging** measure where positive genuinely means
    *worse* (cost overrun, error rate, latency, churn — "more is worse"),
    pass ``reverse=True`` so the palette's low/high ends swap (green stays
    "good" = negative, red stays "bad" = positive) instead of literally
    reversing the color list. Actually ignored (forced ``False``) for
    ``kind="sequential"`` — a plain magnitude has no good/bad orientation to
    flip, so passing ``True`` there would silently flip the intended
    light-to-dark magnitude encoding instead of doing nothing. This is the
    parameter ``references/RULES.md``'s "Percent / rate / change" rule tells
    callers to pass.

    THE GOTCHA this function exists to prevent: ``fmt_percent`` expects
    *fractional* values (``0.12`` renders as ``12%``) — a percent column
    stored as already-scaled ``12`` needs ``scale_values=False`` wherever
    it's formatted, and the same fractional-vs-scaled question applies to
    the domain passed here. A bare ``data_color(...)`` call with no
    explicit ``domain`` is a **correctness bug**, not a style nit: without
    a pinned domain, the color a given value renders as can shift between
    runs (or between two tables) depending on what else happens to be in
    the column at that moment.
    """
    cols = [columns] if isinstance(columns, str) else list(columns)
    if domain is None:
        lo, hi = _column_min_max(gt._tbl_data, cols)
        if kind == "diverging":
            m = max(abs(lo), abs(hi))
            domain = [-m, m] if m != 0 else [-1.0, 1.0]
        elif kind == "sequential":
            domain = [lo, hi]
        else:
            raise ValueError(
                "heatmap(): kind must be 'sequential' or 'diverging', got %r" % (kind,)
            )
    if kind == "sequential":
        palette = PALETTE["sequential"].get(hue, hue)
    elif kind == "diverging":
        resolved = PALETTE["diverging"].get(hue, hue)
        palette = resolved[0] if isinstance(resolved, (list, tuple)) else resolved
    else:
        raise ValueError("heatmap(): kind must be 'sequential' or 'diverging', got %r" % (kind,))
    return gt.data_color(
        columns=cols,
        palette=palette,
        domain=domain,
        na_color=PALETTE["neutral"]["na_cell"],
        truncate=False,
        autocolor_text=True,
        reverse=reverse if kind == "diverging" else False,
    )


def status_chip(gt, column, meaning):
    """Fill a DISCRETE categorical column's cells by a value -> meaning map.

    ``meaning`` maps each cell VALUE (e.g. ``"On Track"``) to one of
    ``"good"`` / ``"bad"`` / ``"neutral"``. Fills from the ``accent`` tier
    (the same brighter, more saturated tier ``band(shade="dark")`` uses --
    NOT ``stub_tint()``, which always uses the quieter ``washed`` tier)
    rather than the muted ``solid`` DA tier: ``good`` -> accent forest
    (a clean green), ``bad`` -> accent oxblood (a clean red, not the muted
    ``solid`` oxblood's muddy brown-red), ``neutral`` -> accent ochre (a
    warm, legible amber — not accent/solid ``tan``, which reads as a flat,
    muddy khaki next to the other two rather than a distinct third color).
    All three get white text. The category is what matters here — status
    is a discrete red/green/amber signal, not a magnitude, so it wants
    clean, clearly-differentiated colors more than restraint.

    THE POINT of this function: a red/green column is not always a
    continuous heatmap. When the column's values are a small fixed set of
    categories (status, state, pass/fail) rather than a magnitude, use THIS
    function, never ``data_color``/``heatmap`` — the good/bad resolution
    must land on the exact same two solids either way (continuous heatmap
    or discrete chip), because the meaning is the same: color here is never
    decorative, it always encodes good/bad/neutral, resolved the same
    deterministic way regardless of whether the underlying data is
    continuous or discrete.

    A missing cell (``None``/NaN/``pd.NA`` — e.g. a nullable pandas string
    dtype) is skipped rather than compared: ``v == value`` on a ``pd.NA``
    scalar returns ``pd.NA`` itself, and ``bool(pd.NA)`` raises (ambiguous
    truth value) instead of being simply ``False``, which would otherwise
    crash this function on the exact kind of missing status cell
    ``sub_missing(missing_text="—")`` is meant to handle gracefully
    elsewhere.

    ``loc.body(rows=...)`` interprets a list of INTEGERS as **display**
    positions — but with ``groupname_col=`` set, ``great_tables`` renders
    rows grouped into sections, which can reorder them relative to the
    underlying data's original row order (this table's own demo rows
    happen to already be sorted by group, so it wouldn't show the bug, but
    a caller whose source rows interleave groups would silently color the
    wrong cells). An earlier version of this function targeted rows by
    their stub row NAME instead of position to sidestep that — but a stub
    label is not guaranteed unique across groups (two different groups can
    each have a row named "Large"), and ``loc.body(rows=[name])`` matches
    EVERY row sharing that name, so a repeated label could still pick up
    the wrong fill. The actually-correct fix is ``gt._stub.group_indices_map()``:
    it returns ``(original_row_index, group_info)`` tuples in the exact
    order ``great_tables`` will render them (grouped if ``groupname_col=``
    is set, identity order otherwise) — enumerating it gives a
    ``original_index -> display_position`` mapping that is correct
    regardless of grouping AND regardless of whether stub labels repeat,
    since it never relies on row identity being unique at all.
    """
    fills = {
        "good": PALETTE["accent"]["forest"],
        "bad": PALETTE["accent"]["oxblood"],
        "neutral": PALETTE["accent"]["ochre"],
    }
    values = gt._tbl_data[column]
    display_order = [int(orig_idx) for orig_idx, _group in gt._stub.group_indices_map()]
    display_position_of = {orig_idx: pos for pos, orig_idx in enumerate(display_order)}
    for value, state in meaning.items():
        if state not in fills:
            raise ValueError(
                "status_chip(): meaning must map to 'good'/'bad'/'neutral', got %r" % (state,)
            )
        selector = [
            display_position_of[i]
            for i, v in enumerate(values)
            if not _is_missing(v) and v == value
        ]
        if not selector:
            continue
        gt = gt.tab_style(
            style=[style.fill(color=fills[state]), style.text(color="white")],
            locations=loc.body(columns=column, rows=selector),
        )
    return gt


def summary_row(gt, row_index, *, bold=True):
    """Mark one ORDINARY DATA row as a totals/summary row, distinct from a plain row.

    For a **whole-table grand total**, prefer ``gt.grand_summary_rows(...)``
    (native to `great_tables`) + ``tab_style(..., locations=loc.grand_summary())``
    — see the "Total" row in ``build_house_table()`` below. That native
    mechanism keeps the total structurally separate from any
    ``groupname_col`` section (no fake group label needed) and it's excluded
    from `data_color`'s domain automatically. Reach for THIS helper only for
    a row that must live inline as an actual data row instead (e.g. a
    per-group subtotal you want positioned among that group's own rows,
    which ``grand_summary_rows`` cannot do — it always places the total(s)
    at the very top or bottom of the whole table).

    Applies a stronger — but still restrained — top border rule
    (``#BDBDBD``, ~1.5px, vs. the default hairline between ordinary rows)
    and, by default, bold text weight to ``row_index`` (a 0-based display
    position, per ``loc.body()``'s indexing — not a DataFrame index).

    Applies to **both** ``loc.body()`` (the value cells) AND ``loc.stub()``
    (the row label) — a table with ``rowname_col=`` set has its row label
    live in a structurally separate stub column, and styling only the body
    would leave the summary row's own label unbolded and un-ruled, which
    reads as an inconsistent, half-applied treatment. ``loc.stub(rows=...)``
    is harmless to call even when the table has no stub at all (it simply
    matches nothing).
    """
    styles = [
        style.borders(sides="top", color=PALETTE["neutral"]["structural_rule"], weight="1.5px")
    ]
    if bold:
        styles.append(style.text(weight="bold"))
    gt = gt.tab_style(style=styles, locations=loc.body(rows=[row_index]))
    return gt.tab_style(style=styles, locations=loc.stub(rows=[row_index]))


def group_emphasis(gt):
    """Emphasize every ``groupname_col`` header row so section breaks read clearly.

    Bold weight + the ``#BDBDBD`` structural rule above and below the group
    label — deliberately NO background fill. A summary/total row is the one
    row that earns its own distinct, subtly-highlighted treatment (see
    ``summary_row()`` / the ``grand_summary_rows()`` styling below); a group
    label is a section break, not a result worth calling out the same way,
    and a fill there reads as one more saturated surface competing with the
    heatmap. Bold + rule alone is enough for the section break to read
    clearly.
    """
    rule = PALETTE["neutral"]["structural_rule"]
    return gt.tab_options(
        row_group_font_weight="bold",
        row_group_border_top_color=rule,
        row_group_border_bottom_color=rule,
        row_group_padding="6px",
    )


# ---------------------------------------------------------------------------
# The demo: "Regional Product Line Performance" — 12 products, 3 region
# groups of 4, exercising every helper above at once. This is the ONE worked
# example the whole skill points at; pattern-match the piece of it (and the
# matching row in references/RULES.md) that fits your actual data.
# ---------------------------------------------------------------------------


def build_house_table():
    """Build and render the house-format reference table.

    Column roles (walk through references/RULES.md alongside this):

    - ``product``    -> stub (rowname_col) — a row identifier.
    - ``region``     -> groupname_col — the organizing category.
    - ``units_sold`` -> plain magnitude, thousands separator, UNCOLORED.
    - ``revenue``    -> the sequential heatmap HERO measure (Blues/neutral).
    - ``yoy_change`` -> the diverging heatmap measure (RdYlGn/default) — the
                        2nd full-heatmap measure in this demo (Big Color
                        stays restrained, not capped at a fixed count).
    - ``status``     -> categorical good/bad/neutral via status_chip, NOT a
                        heatmap — it is 3 discrete states, not a magnitude.
    - ``rank``       -> plain integer, no color, no decimals — a rank's
                        information is its order, not its size.

    Column order: `revenue`, the primary heatmapped measure, sits in the
    first value column or two — right after its lone context column
    (`units_sold`), not literally the very first column — never buried
    among trailing categorical/rank columns; this demo already satisfies
    that, no reordering needed.
    """
    products = pd.DataFrame(
        [
            # product,           region,          units_sold, revenue, yoy_change, status,      rank
            ("Alpha Widget", "North America", 1240, 482000, 0.18, "On Track", 1),
            ("Beta Gadget", "North America", 860, 305000, -0.07, "Watch", 4),
            ("Gamma Tool", "North America", 430, 178500, 0.05, "On Track", 7),
            ("Delta Device", "North America", 210, 64000, -0.22, "At Risk", 11),
            ("Epsilon Unit", "Europe", 980, 410000, 0.12, "On Track", 2),
            ("Zeta Kit", "Europe", 560, 239000, None, "Watch", 6),
            ("Eta Module", "Europe", 340, 142000, -0.15, "At Risk", 9),
            ("Theta Part", "Europe", 125, 38500, 0.02, "Watch", 12),
            ("Iota Component", "Asia-Pacific", 915, 396000, 0.27, "On Track", 3),
            ("Kappa Assembly", "Asia-Pacific", 705, 298000, 0.09, "On Track", 5),
            ("Lambda System", "Asia-Pacific", 388, 165000, -0.11, "At Risk", 8),
            ("Mu Product", "Asia-Pacific", 245, 71500, -0.04, "Watch", 10),
        ],
        columns=["product", "region", "units_sold", "revenue", "yoy_change", "status", "rank"],
    )

    kappa_row_index = products.index[products["product"] == "Kappa Assembly"][0]  # footnote target

    gt = (
        GT(products, rowname_col="product", groupname_col="region")
        .tab_header(
            title="Regional Product Line Performance",
            subtitle=md("Full-year revenue, volume, and trend by product — grouped by region"),
        )
        .tab_stubhead(label="Product")
        .tab_spanner(label="Volume & Revenue", columns=["units_sold", "revenue"])
        .tab_spanner(label="Trend", columns=["yoy_change", "status"])
        # spanner-seam vertical divider — right edge of the LAST column in the
        # first group, applied to both the body and the column-labels row so
        # the seam runs the full height of the table (small_color.md (b)).
        .tab_style(
            style=style.borders(
                sides="right", color=PALETTE["neutral"]["vertical_divider"], weight="1px"
            ),
            locations=loc.body(columns="revenue"),
        )
        .tab_style(
            style=style.borders(
                sides="right", color=PALETTE["neutral"]["vertical_divider"], weight="1px"
            ),
            locations=loc.column_labels(columns="revenue"),
        )
        .fmt_number(columns="units_sold", decimals=0, use_seps=True)
        .fmt_currency(columns="revenue", decimals=0)
        .fmt_percent(columns="yoy_change", decimals=1, force_sign=True)
        .fmt_integer(columns="rank")
        .sub_missing(columns=["yoy_change", "status", "rank"], missing_text="—")
    )
    gt = humanize_labels(
        gt,
        products,
        overrides={"units_sold": "Units Sold", "yoy_change": "YoY Change"},
    )

    # Column widths + padding: size each column to its content plus a
    # small buffer; don't let auto-layout stretch narrow columns (`rank`)
    # to match the widest label elsewhere. Padding values are the six
    # pinned house constants (see references/RULES.md's "Global constants").
    gt = gt.cols_width(
        cases={
            "product": "150px",
            "units_sold": "110px",
            "revenue": "110px",
            "yoy_change": "110px",
            "status": "100px",
            "rank": "70px",
        }
    )
    gt = gt.tab_options(
        heading_padding="6px",
        column_labels_padding="6px",
        column_labels_padding_horizontal="8px",
        data_row_padding="5px",
        data_row_padding_horizontal="8px",
        source_notes_padding="6px",
    )

    # Big Color, kept restrained: 2 full heatmaps in this demo (no fixed
    # cap — see references/RULES.md's "Color restraint"). `revenue` is the
    # sequential hero (a neutral magnitude -> Blues); `yoy_change` is the
    # diverging 2nd measure (signed, positive=good -> RdYlGn default
    # orientation, no reverse). `status` is a categorical good/bad/
    # neutral column, NOT a heatmap — status_chip, not data_color. The
    # domain for each is computed from `products` alone (heatmap()'s default
    # when domain=None) — safe because the grand-summary Total added below
    # is NOT part of `gt._tbl_data`; unlike a manually appended total ROW, it
    # can never stretch/compress the color scale.
    gt = heatmap(gt, "revenue", kind="sequential", hue="neutral")
    gt = heatmap(gt, "yoy_change", kind="diverging", hue="default")
    gt = status_chip(gt, "status", {"On Track": "good", "At Risk": "bad", "Watch": "neutral"})

    # Heading band: the house DEFAULT (shade="dark") is a solid, branded
    # navy fill (`accent["navy"]`, #08306B) with bold white text. Branding
    # surfaces are fixed to this navy/Blues family always — navy here is
    # NOT re-derived by matching the heatmap's own hue elsewhere in the
    # table (a heatmap could be Blues, Reds, or RdYlGn and the band stays
    # navy regardless); see references/RULES.md's "Unified color theme".
    gt = band(gt, hue="navy")

    # Small-Color polish: striping applies by DEFAULT regardless of row
    # count — the real gate is whether the body's visible cells are
    # already 100% heatmap-covered. Only 2 of 6 columns here carry
    # continuous color (revenue, yoy_change), so plenty of plain cells
    # remain for a stripe to show through on. Stub tint harmonizes to the
    # same navy family as the band, at the quieter "washed" tier (the band
    # is the louder of the two). The stripe is always flat grey, never
    # tinted — an alternating fill reads as busy in a way a single flat
    # surface doesn't. Group headers get bold + a rule ONLY (no fill) —
    # the one row that earns its own distinct highlight is the
    # summary/total row below, not a section break.
    gt = stripe(gt)
    gt = stub_tint(gt, hue="navy")
    gt = group_emphasis(gt)

    # Grand summary "Total" row — the NATIVE mechanism for a whole-table
    # total (great_tables' own `grand_summary_rows`), not a manually
    # appended data row. This is deliberately NOT the `summary_row()`
    # helper above: grand_summary_rows() places the total in its own
    # structural section below every groupname_col group, with no fake
    # group label required (a manually appended row needs SOME value in
    # the `region` column, and `None`/NaN renders as the literal text
    # "nan" — grand_summary_rows sidesteps the whole problem). Only
    # `units_sold`/`revenue` are meaningfully summable — `yoy_change`,
    # `status`, and `rank` have no sensible total, so the aggregation
    # function only returns the two summable columns and the rest render
    # via `missing_text="—"` (overriding the `"---"` default so it matches
    # this table's `sub_missing` em dash elsewhere).
    #
    # `fns` values must return a `pandas.Series`; `grand_summary_rows`
    # applies at most ONE `fmt=` formatter to every summarized column, so
    # with two columns needing different formats (thousands-separated
    # integer vs. currency) the values are pre-formatted as display
    # strings inside the function itself instead of using `fmt=`.
    def _totals(d):
        return pd.Series(
            {
                "units_sold": f"{int(d['units_sold'].sum()):,}",
                "revenue": f"${int(d['revenue'].sum()):,}",
            }
        )

    gt = gt.grand_summary_rows(fns={"Total": _totals}, missing_text="—")
    gt = gt.tab_style(
        style=[
            style.text(weight="bold"),
            style.borders(sides="top", color=PALETTE["neutral"]["structural_rule"], weight="1.5px"),
        ],
        locations=loc.grand_summary(),
    )
    gt = gt.tab_style(
        style=style.text(weight="bold"),
        locations=loc.grand_summary_stub(),
    )

    gt = (
        gt.tab_footnote(
            footnote="Restated to include a distributor rebate posted in Q4.",
            locations=loc.body(columns="revenue", rows=[kappa_row_index]),
        )
        # Two source notes, analytical caption FIRST: "YoY Change" is a
        # derived, potentially ambiguous measure (revenue growth vs. unit
        # growth) — state the chosen definition here, not in the subtitle.
        .tab_source_note(
            source_note="YoY Change is the year-over-year percent change in revenue, not unit volume."
        )
        .tab_source_note(source_note="Source: internal sales ledger, FY close. Figures in USD.")
    )

    gt = hairlines(gt)
    gt = frame(gt)
    finalize(gt, path="house_table.png")
    return gt


if __name__ == "__main__":
    build_house_table()
