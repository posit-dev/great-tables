# Data cleaning — get to ONE clean, correctly-typed DataFrame (Step 1)

Step 1 first *understands* the data; this file is the mechanical sub-step that comes
**before Step 2**: turn whatever you were handed (CSV, Excel, SQL result, a messy
DataFrame) into **one tidy DataFrame with the right dtype in every column**. Do this
first, because `great_tables` **formats numbers — it does not parse strings**, and
`data_color` needs real numerics. A currency string or an `object`-dtype column
silently breaks `fmt_*` / `data_color` downstream.

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

4. **Fix the header row.** If row 0 is a title / blank / merged cell rather than the
   real header (common in Excel exports), reload with the correct `header=`/`skiprows=`
   so column names are real, not `Unnamed: 0`.

5. **SQL / Decimal results → float.** Cast `decimal.Decimal` columns to `float`
   (`df["amt"] = df["amt"].astype(float)`) so gt's formatters accept them, and confirm
   NULL handling matches your missing-value convention (below). **Caution — exact money /
   large integers:** `float` has only ~15–16 significant digits (integers exact only up
   to 2^53). For values that must stay exact — cents-precise money, IDs, or magnitudes
   beyond 2^53 — do **not** cast to `float`: keep the `Decimal`, or `quantize` it to the
   display precision (e.g. `df["amt"] = df["amt"].map(lambda d: d.quantize(Decimal("0.01")))`),
   then format. gt can format `Decimal` values directly.

6. **Trim whitespace in string keys.** Leading/trailing spaces break exact matching for
   `groupname_col` labels and joins: `df["region"] = df["region"].str.strip()`.

7. **Name the missing-value meaning, then make it uniform.** "No data", "true zero",
   and "not applicable" are different claims — don't let them all collapse to a blank
   cell. Standardize to `NaN` where you mean missing, and render with
   `sub_missing(missing_text="—")` (an em dash reads as *intentionally blank*, not
   *broken*). This pairs with the NA-cell neutral in `small_color.md`.

## Do NOT fabricate

If cleaning reveals the data cannot answer the request (a needed column is absent or
unusable), stop — tell the user what is missing and emit a blank table (Step 1's
validate-request rule). Never invent values to fill a gap.
