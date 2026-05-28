"""
Generate x_durations.csv from Unicode CLDR JSON data.

This script fetches duration unit patterns (week, day, hour, minute, second)
from the cldr-json GitHub repo for all locales used by great-tables and writes
them into a CSV file suitable for locale-aware fmt_duration() formatting.

CLDR source: https://github.com/unicode-org/cldr-json
Package: cldr-units-full

Usage:
    python scripts/generate_durations_csv.py
"""

from __future__ import annotations

import csv
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# The base URL for CLDR units JSON files
CLDR_BASE_URL = (
    "https://raw.githubusercontent.com/unicode-org/cldr-json/main/"
    "cldr-json/cldr-units-full/main/{locale}/units.json"
)

# Duration units we care about
DURATION_UNITS = ["week", "day", "hour", "minute", "second"]

# CLDR unit length types mapped to our style names
# "long" in CLDR = "wide" in gt; "narrow" stays "narrow"
CLDR_TYPES = ["long", "narrow"]

# Plural forms we extract
PLURAL_FORMS = ["zero", "one", "two", "few", "many", "other"]

# Output CSV columns
# locale, type, then for each unit and plural form: {unit}_{plural}
# e.g., week_one, week_other, week_zero, day_one, day_other, ...


def get_gt_locales() -> list[str]:
    """Read the list of locales from x_locales.csv."""
    locales_csv = Path(__file__).parent.parent / "great_tables" / "data" / "x_locales.csv"
    locales = []
    with open(locales_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            locales.append(row["locale"])
    return locales


def normalize_locale_for_cldr(locale: str) -> str:
    """Convert gt locale format to CLDR path format.

    gt uses underscores (e.g., "en_US"), CLDR uses hyphens (e.g., "en-US").
    """
    return locale.replace("_", "-")


def fetch_cldr_units(locale: str) -> dict | None:
    """Fetch the CLDR units JSON for a locale. Returns None on failure."""
    cldr_locale = normalize_locale_for_cldr(locale)
    url = CLDR_BASE_URL.format(locale=cldr_locale)

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "great-tables-cldr-fetch/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        print(f"  HTTP {e.code} for {cldr_locale}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  Error fetching {cldr_locale}: {e}", file=sys.stderr)
        return None


def extract_duration_patterns(data: dict, locale: str) -> list[dict[str, str]]:
    """Extract duration patterns from CLDR JSON data for a locale.

    Returns a list of dicts (one per type: long/narrow), each containing
    the locale, type, and all duration unit patterns.
    """
    cldr_locale = normalize_locale_for_cldr(locale)

    # Navigate to the units section
    try:
        units = data["main"][cldr_locale]["units"]
    except KeyError:
        # Try with just the base locale key
        keys = list(data.get("main", {}).keys())
        if keys:
            units = data["main"][keys[0]]["units"]
        else:
            return []

    rows = []

    for cldr_type in CLDR_TYPES:
        # Map CLDR type to our type name
        gt_type = "wide" if cldr_type == "long" else "narrow"

        unit_data = units.get(cldr_type, {})
        row: dict[str, str] = {"locale": locale, "type": gt_type}

        for unit in DURATION_UNITS:
            cldr_key = f"duration-{unit}"
            unit_entry = unit_data.get(cldr_key, {})

            for plural in PLURAL_FORMS:
                pattern_key = f"unitPattern-count-{plural}"
                pattern = unit_entry.get(pattern_key, "")
                col_name = f"{unit}_{plural}"
                row[col_name] = pattern

        rows.append(row)

    return rows


def get_fallback_locale(locale: str) -> str | None:
    """Get fallback locale by stripping the last subtag."""
    parts = locale.split("_") if "_" in locale else locale.split("-")
    if len(parts) > 1:
        return "_".join(parts[:-1]) if "_" in locale else "-".join(parts[:-1])
    return None


def main():
    gt_locales = get_gt_locales()
    print(f"Processing {len(gt_locales)} locales from x_locales.csv...")

    # Build the CSV column list
    columns = ["locale", "type"]
    for unit in DURATION_UNITS:
        for plural in PLURAL_FORMS:
            columns.append(f"{unit}_{plural}")

    all_rows: list[dict[str, str]] = []
    fetched_cache: dict[str, dict | None] = {}
    success_count = 0
    fallback_count = 0
    missing_count = 0

    for i, locale in enumerate(gt_locales):
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i + 1}/{len(gt_locales)}...")

        # Try exact locale first
        cldr_locale = normalize_locale_for_cldr(locale)
        if cldr_locale not in fetched_cache:
            fetched_cache[cldr_locale] = fetch_cldr_units(locale)
            # Rate limiting: small delay to be nice to GitHub
            time.sleep(0.05)

        data = fetched_cache[cldr_locale]

        # If not found, try fallback (e.g., "fr-BE" -> "fr")
        if data is None:
            fallback = get_fallback_locale(locale)
            if fallback:
                fb_cldr = normalize_locale_for_cldr(fallback)
                if fb_cldr not in fetched_cache:
                    fetched_cache[fb_cldr] = fetch_cldr_units(fallback)
                    time.sleep(0.05)
                data = fetched_cache[fb_cldr]
                if data is not None:
                    fallback_count += 1

        if data is None:
            missing_count += 1
            # Add empty rows for this locale
            for gt_type in ["wide", "narrow"]:
                row = {"locale": locale, "type": gt_type}
                for unit in DURATION_UNITS:
                    for plural in PLURAL_FORMS:
                        row[f"{unit}_{plural}"] = ""
                all_rows.append(row)
            continue

        rows = extract_duration_patterns(data, locale)
        if rows:
            all_rows.extend(rows)
            success_count += 1
        else:
            missing_count += 1

    # Write output CSV
    output_path = Path(__file__).parent.parent / "great_tables" / "data" / "x_durations.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\nDone! Wrote {len(all_rows)} rows to {output_path}")
    print(f"  Successful: {success_count} locales")
    print(f"  Used fallback: {fallback_count} locales")
    print(f"  Missing/empty: {missing_count} locales")


if __name__ == "__main__":
    main()
