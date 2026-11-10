"""Write test/colors.json: the colors `data_color()` makes, which the runtime's (`src/color.ts`)
must match (see `test/color.test.ts`).

Each case is a spec's `colors` entry (from every row) and the colors `data_color()` gives the
rows kept when it colors them alone. Run it again when `data_color()`'s colors change (pytest's
`tests/test_gti_colors.py` checks that the file is up to date):

    python packages/gti/test/make_colors.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import polars as pl

from great_tables import GT, GTI
from great_tables._data_color.base import _ideal_fgnd_color, _resolve_palette
from great_tables._data_color.palettes import GradientPalette
from great_tables._gti._spec import build_spec
from great_tables._styles import CellStyleFill, CellStyleText

OUT = Path(__file__).parent / "colors.json"


def _colors(gt: GT) -> dict[int, list[str | None]]:
    found: dict[int, list[str | None]] = {}
    for info in gt._styles:
        fill = next((s.color for s in info.styles if isinstance(s, CellStyleFill)), None)
        text = next((s.color for s in info.styles if isinstance(s, CellStyleText)), None)
        found[info.rownum] = [fill, text]  # type: ignore[index]
    return found


def _case(name: str, values: list[Any], keep: list[int], **kwargs: Any) -> dict[str, Any]:
    df = pl.DataFrame({"x": values}, strict=False)
    gti = GTI(df).data_color(columns="x", **kwargs)
    spec = build_spec(gti.i_cols_controls(data_color="recompute")._build_data("html"))
    kept = _colors(GT(df[keep]).data_color(columns="x", **kwargs))
    missing = [x is None or (isinstance(x, float) and math.isnan(x)) for x in values]
    expected = {str(row): kept[i] for i, row in enumerate(keep) if not missing[row]}
    return {"name": name, "spec": spec["colors"][0], "keep": keep, "expected": expected}


def make() -> dict[str, Any]:
    cases = [
        _case("numbers", [1.5, 2, 30, 7, 11, 4.25, None, 19], [0, 2, 3, 5, 7]),
        _case(
            "numbers, viridis", [1.5, 2, 30, 7, 11, 4.25, 8, 19], [1, 3, 4, 6], palette="viridis"
        ),
        _case("infinities", [-math.inf, 3, 9, math.inf, 5, 1], [0, 2, 3, 4]),
        _case(
            "a midpoint",
            [-4, -1, 0, 2, 9, 3, -7],
            [0, 1, 3, 5],
            palette=["red", "white", "green"],
            midpoint=0,
        ),
        _case("only the midpoint", [0, 0, 2, 5], [0, 1], palette="RdBu", midpoint=0),
        _case(
            "alpha, and WCAG",
            [10, 20, 30, 40, 50, 60],
            [1, 2, 4],
            palette="Greens",
            alpha=0.6,
            contrast_algo="wcag",
        ),
        _case("one row", [10, 20, 30], [1]),
        _case("text", ["b", "a", "c", "b", "d", "e", "a"], [0, 2, 3, 5], palette="Set2"),
        # (The levels in the order they first come in the rows kept)
        _case("text, in a new order", ["b", "a", "c", "a", "b", "d"], [2, 3, 4]),
        _case("text, one level", ["b", "a", "c", "b"], [0, 3]),
        _case(
            "text, without text colors",
            ["b", "a", "c", "b", "d"],
            [1, 2, 4],
            palette="Blues",
            autocolor_text=False,
        ),
    ]
    # Each palette's colors at 41 places, and the text on each
    ramps = []
    for palette in [None, "viridis", "RdBu", "Blues", "Spectral", ["red", "white", "green"]]:
        colors = [color[:7] for color in _resolve_palette(palette)]
        made = GradientPalette(colors=colors)([i / 40 for i in range(41)])
        ramps.append(
            {
                "palette": colors,
                "colors": made,
                "apca": [_ideal_fgnd_color(color, algo="apca") for color in made],  # type: ignore[arg-type]
                "wcag": [_ideal_fgnd_color(color, algo="wcag") for color in made],  # type: ignore[arg-type]
                "alpha": [_ideal_fgnd_color(f"{color}66") for color in made],
            }
        )
    return {"cases": cases, "ramps": ramps}


if __name__ == "__main__":
    OUT.write_text(json.dumps(make(), indent=1) + "\n")
