"""
Generate x_fontawesome.csv and x_fontawesome_aliases.csv from Font Awesome's icon metadata.

This script fetches `metadata/icons.json` for a tagged release of Font Awesome Free and writes
the SVG data of every icon (one row per icon and style) into a CSV file, along with a second CSV
that maps the icons' alias names to their canonical names. These files are used by `fmt_icon()`.
The approach (and the checks made before writing) follow `data-raw/fontawesome-update.R` in the
R fontawesome package.

Font Awesome source: https://github.com/FortAwesome/Font-Awesome
The icons are licensed under CC BY 4.0 (see great_tables/data/FONT_AWESOME_LICENSE.txt).

Usage:
    python scripts/generate_fontawesome_csv.py
"""

from __future__ import annotations

import csv
import json
import re
import urllib.request
from pathlib import Path

# The Font Awesome release to take the icons from (also noted in FONT_AWESOME_LICENSE.txt)
VERSION_TAG = "7.1.0"

ICONS_URL = (
    f"https://raw.githubusercontent.com/FortAwesome/Font-Awesome/{VERSION_TAG}/metadata/icons.json"
)

DATA_DIR = Path(__file__).parent.parent / "great_tables" / "data"

ICONS_COLUMNS = ["name", "style", "full_name", "label", "width", "path"]
ALIASES_COLUMNS = ["alias", "name"]

STYLE_PREFIXES = {"regular": "far", "solid": "fas", "brands": "fab"}


def fetch_icons() -> dict:
    print(f"Fetching {ICONS_URL}")
    with urllib.request.urlopen(ICONS_URL, timeout=60) as response:
        return json.load(response)


def tidy_icons(icons: dict) -> tuple[list[dict], list[dict]]:
    """Get one row per icon and style, and one row per alias name."""

    icon_rows = []
    alias_rows = []

    for name, info in icons.items():
        for style, svg in info["svg"].items():
            min_x, min_y, width, height = (int(x) for x in svg["viewBox"])

            # Only the width varies between icons; the other viewBox values are taken as fixed
            # (with a height of 512) when generating the SVGs
            if (min_x, min_y, height) != (0, 0, 512):
                raise ValueError(f"The '{name}' ({style}) icon has an unexpected viewBox.")

            icon_rows.append(
                {
                    "name": name,
                    "style": style,
                    "full_name": f"{STYLE_PREFIXES[style]} fa-{name}",
                    "label": info["label"],
                    "width": width,
                    "path": svg["path"],
                }
            )

        for alias in (info.get("aliases") or {}).get("names", []):
            alias_rows.append({"alias": alias, "name": name})

    return icon_rows, alias_rows


def validate(icon_rows: list[dict], alias_rows: list[dict]) -> None:
    """Check the icon data before it's written (these are the checks made by the R package)."""

    names = {row["name"] for row in icon_rows}
    full_names = [row["full_name"] for row in icon_rows]

    assert len(icon_rows) > 2000, "Expected more than 2000 icons"
    assert len(full_names) == len(set(full_names)), "Expected the full names to be distinct"
    assert all(row[col] not in (None, "") for row in icon_rows for col in ICONS_COLUMNS)
    assert all(re.fullmatch(r"[a-z0-9-]+", row["name"]) for row in icon_rows)
    assert all(re.fullmatch(r"fa[brs] fa-[a-z0-9-]+", name) for name in full_names)

    # An alias must never shadow an icon name, and each alias must point to a single icon
    aliases = [row["alias"] for row in alias_rows]
    assert len(aliases) == len(set(aliases)), "Expected each alias to belong to a single icon"
    assert not set(aliases) & names, "Expected no alias to also be an icon name"
    assert all(row["name"] in names for row in alias_rows)


def write_csv(fname: Path, rows: list[dict], columns: list[str]) -> None:
    with open(fname, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {fname}")


def main() -> None:
    icon_rows, alias_rows = tidy_icons(fetch_icons())
    validate(icon_rows, alias_rows)

    write_csv(DATA_DIR / "x_fontawesome.csv", icon_rows, ICONS_COLUMNS)
    write_csv(DATA_DIR / "x_fontawesome_aliases.csv", alias_rows, ALIASES_COLUMNS)


if __name__ == "__main__":
    main()
