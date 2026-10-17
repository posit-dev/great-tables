# Data cleaning — get to ONE clean, correctly-typed DataFrame (Step 1)

Step 1 first *understands* the data; this file is the mechanical sub-step that comes
**before Step 2**: turn whatever you were handed (CSV, Excel, SQL result, a messy
DataFrame) into **one tidy DataFrame with the right dtype in every column**. Do this
first, because `great_tables` **formats numbers — it does not parse strings**, and
`data_color` needs real numerics. A currency string or an `object`-dtype column
silently breaks `fmt_*` / `data_color` downstream.

**Anti-pattern: don't cast a numeric identifier column to string to suppress
thousands-separators.** A column like `Year` or an ID renders `1,996` instead of
`1996` once a broader `fmt_integer`/`fmt_number` pass (default `use_seps=True`)
touches it — not by default, and not until that pass runs — and it's tempting to
fix that with `df["Year"] = df["Year"].astype(str)` — don't. That silently converts
the column to `object` dtype: any later `fmt_*` call on it raises
`TypeError: '<' not supported between instances of 'str' and 'int'`, and a
`data_color`/heatmap pass on it doesn't crash but silently produces a different,
wrong color mapping. The column stays numeric; suppress the separators at format
time instead — `gt.fmt_integer(columns="Year", use_seps=False)` (here `gt` is the
`GT` instance you already built, e.g. `gt = GT(df)` — never
`import great_tables as gt`) — and apply that call *after* any
broader `fmt_integer`/`fmt_number` pass over multiple columns (or exclude this
column from it): the later matching format call wins, so a broader pass's default
`use_seps=True` would otherwise silently re-add the separators.

## The checklist — run it before you organize columns

1. **Strip number-like strings to real numbers.** Values imported as strings because of
   currency symbols, thousands separators, percent signs, or unit suffixes
   (`"$1,200"`, `"1,116.56"`, `"12%"`, `"5 kg"`) must become plain floats/ints
   **before** they reach gt. `fmt_currency`/`fmt_percent` format *numbers*; they will
   not parse `"$1,200"`.

   **Normalize accounting-negative parentheses FIRST.** A value wrapped in parentheses
   is a **negative** (`"($1,200)"` = −1200, `"(12%)"` = −12). The naïve strip
   `r"[^0-9.\-]"` deletes the parentheses and keeps only the digits, silently turning a
   loss into a positive number — **data corruption**. So detect the wrapping parentheses
   and convert them to a leading `-` *before* you strip symbols:
   ```python
   s = df["price"].astype(str).str.strip()
   s = s.str.replace(r"^\((.*)\)$", r"-\1", regex=True)  # (1,200) -> -1,200  BEFORE stripping
   s = s.str.replace(r"[^0-9.\-]", "", regex=True)       # now drop $ , % and unit text; keep leading -
   df["price"] = pd.to_numeric(s, errors="coerce")
   ```
   **Magnitude suffixes need an explicit multiplier — never the generic strip.** For
   abbreviated values (`"$1.2M"`, `"3K"`, `"4bn"`) the generic strip leaves `1.2`, `3`,
   `4` — dropping the ×1e6 / ×1e3 / ×1e9 multiplier, an order-of-magnitude corruption.
   Do **not** run the generic strip on a suffixed column; parse the suffix explicitly
   against a fixed multiplier table (deterministic — same string always maps to the same
   number):
   ```python
   import re
   _MULT = {"k": 1e3, "m": 1e6, "b": 1e9, "bn": 1e9, "t": 1e12}   # fixed, case-insensitive
   def parse_scaled(x):
       s = str(x).strip().lower().replace(",", "")
       s = re.sub(r"^\((.*)\)$", r"-\1", s)                       # accounting negative first
       m = re.match(r"^[^\d\-.]*(-?\d+(?:\.\d+)?)\s*(bn|k|m|b|t)?", s)  # bn before b
       if not m:
           return float("nan")
       return float(m.group(1)) * _MULT.get(m.group(2), 1.0)
   df["amount"] = df["amount"].map(parse_scaled)
   ```

2. **Coerce `object`-dtype numeric columns deliberately.** A column with numbers plus a
   stray `"N/A"`/`"-"` stays `object` and breaks `fmt_number`/`data_color`. Coerce it,
   don't leave it: `df["x"] = pd.to_numeric(df["x"], errors="coerce")` (bad values →
   `NaN`, which you then render with `sub_missing`).

3. **Percent scale — decide fraction vs. already-scaled.** `fmt_percent` expects the
   **fractional** form (`0.12` → `12%`). If the column is already `12` meaning "12%",
   either divide by 100 first or pass `scale_values=False` — otherwise it renders
   `1200%`. Pick one and be consistent across every percent column.

4. **Guard a percent-CHANGE column against zero/negative baselines.** `(end - start) /
   start` silently produces two different kinds of garbage for the rows this doesn't
   work for: a zero baseline gives `inf` (renders as the literal text `"inf%"` — not
   caught by `sub_missing`, which only substitutes `None`/`NaN`), and a negative
   baseline gives a finite, sign-reversed, equally-meaningless value (`(5 - (-10)) /
   (-10)` = `-1.5`, i.e. a plausible-looking `"-150%"` that passes right through
   uncaught). Mask on the condition, not the symptom, and use `np.nan` — not `None` —
   as the fallback: `None` forces the whole column to `object` dtype (breaking any
   later `.nlargest()`/`.sort_values()` on it), while `np.nan` keeps it `float64` and
   `sub_missing` still catches it identically:
   ```python
   df["pct_change"] = np.where(df["start"] > 0, (df["end"] - df["start"]) / df["start"], np.nan)
   ```
   then render with `sub_missing(missing_text="—")` as usual, without discarding the
   rest of that row.

5. **Fix the header row.** If row 0 is a title / blank / merged cell rather than the
   real header (common in Excel exports), reload with the correct `header=`/`skiprows=`
   so column names are real, not `Unnamed: 0`.

6. **SQL / Decimal results → float.** Cast `decimal.Decimal` columns to `float`
   (`df["amt"] = df["amt"].astype(float)`) so gt's formatters accept them, and confirm
   NULL handling matches your missing-value convention (below). **Caution — exact money /
   large integers:** `float` has only ~15–16 significant digits (integers exact only up
   to 2^53). For values that must stay exact — cents-precise money, IDs, or magnitudes
   beyond 2^53 — do **not** cast to `float`: keep the `Decimal`, or `quantize` it to the
   display precision (e.g. `df["amt"] = df["amt"].map(lambda d: d.quantize(Decimal("0.01")))`),
   then format. gt can format `Decimal` values directly.

7. **Trim whitespace in string keys.** Leading/trailing spaces break exact matching for
   `groupname_col` labels and joins: `df["region"] = df["region"].str.strip()`.

8. **Name the missing-value meaning, then make it uniform.** "No data", "true zero",
   and "not applicable" are different claims — don't let them all collapse to a blank
   cell. Standardize to `NaN` where you mean missing, and render with
   `sub_missing(missing_text="—")` (an em dash reads as *intentionally blank*, not
   *broken*). This pairs with the NA-cell neutral in `small_color.md`.

## Grain & identifiers — does every row have a distinct stub label?

Before Step 2 turns a column into the stub, confirm the DataFrame's **grain** — what
one row actually represents — has an identifier that is genuinely unique at that
grain, not just present.

- **Single-column identifier.** A single existing column (name, ID, date) is enough
  when it alone is unique at the row's grain — use it directly as the stub.
- **Composite identifier — two distinct motivations, not one.** A composite (joining
  two or more columns into one stub label) can be built for either reason, and it's
  worth being clear about which one actually applies:
  - **Uniqueness** — a single column has duplicate values across rows, so a
    composite is *required* to disambiguate at all.
  - **Readability** — a single column is already unique on its own, but pairing it
    with another column produces a more self-describing label, so the reader isn't
    forced to cross-reference a second column to understand what the stub names.
    A column can pass the uniqueness test below and still be worth combining for
    this reason alone.

  A concrete case combining both motivations: `mfr` + `model` in a car dataset —
  `mfr` alone isn't unique (only 19 distinct manufacturers across 47 rows, e.g.
  multiple Aston Martins), so a composite is required just to disambiguate. `model`
  alone is in fact unique across all 47 rows in this dataset (zero duplicate
  values), and still isn't reliably recognizable on its own: "GT" alone is not a
  known car, "Ford GT" is.
  Combining both gives a stub that's unique *and* readable. Build the stub column
  yourself before stubbing:
  ```python
  df["car"] = df["mfr"] + " " + df["model"]
  ```
  then `rowname_col="car"`. Do this whenever the request's own language refers to
  rows by the combination ("the Bentley Continental GT," not "the Bentley").

  A hypothetical product-catalog dataset illustrates the readability motivation with
  no uniqueness requirement at all: suppose `sku_name` (e.g. "Trail Runner 3") is
  already unique across every row on its own (verified directly against the data),
  so uniqueness alone would not require a composite. A stub can still combine
  `brand + " " + sku_name` into one label anyway, because "Trail Runner 3" read
  alone doesn't say which brand makes it, while "Summit Trail Runner 3" is
  self-describing without a separate brand column:
  ```python
  df["display_name"] = df["brand"] + " " + df["sku_name"]
  ```
- **Constructed identifier.** When the grain is itself a combination of columns with
  no natural label (e.g. one row per region-quarter), build a display label from them
  rather than showing the raw parts side by side:
  ```python
  df["period_label"] = df["yr"].astype(str) + " Q" + df["qtr"].astype(str)  # -> "2010 Q1"
  ```

**The decidable test (uniqueness only):** would two different rows render an
**identical** stub label? If so, the identifier is incomplete for uniqueness —
extend it (add another column to the composite, or construct a finer label) until
every row's label is unique. This test only checks uniqueness, not readability — a
column can pass it (be unique on its own) and still benefit from a composite for the
readability reason above. Check the test against the actual data, the same way the
product-catalog case above is verified against every row before it's trusted, rather
than assuming a column "looks like" an identifier.

## Do NOT fabricate

If cleaning reveals the data cannot answer the request (a needed column is absent or
unusable), stop — tell the user what is missing and emit a blank table (Step 1's
validate-request rule). Never invent values to fill a gap.
