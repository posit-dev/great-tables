from __future__ import annotations

import importlib.util
import json
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "packages" / "gti" / "test" / "make_colors.py"


def test_the_runtimes_colors_are_data_colors():
    # (The colors the runtime's are checked against are the ones `data_color()` makes now)
    spec = importlib.util.spec_from_file_location("make_colors", SCRIPT)
    assert spec is not None and spec.loader is not None
    make_colors = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(make_colors)

    made = json.loads(make_colors.OUT.read_text())
    assert made == json.loads(
        json.dumps(make_colors.make())
    ), "Run `python packages/gti/test/make_colors.py` to write test/colors.json again"
