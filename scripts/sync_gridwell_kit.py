"""
Sync gridwell's conformance kit into `tests/gridwell_kit/`.

`GT.as_gridwell()` writes gridwell's IR, and its tests check that IR against gridwell's
conformance kit: the conformance cases (`conformance/cases.py`), each case's expected grid for
Great Tables (`conformance/expected/great_tables/`), the HTML grid reader the other tables are
checked with (`conformance/html_grid.py`) and the IR's JSON Schema. This script copies them from a
gridwell checkout (https://github.com/rich-iannone/gridwell), removes expected grids that gridwell
no longer has, and records the gridwell commit in `tests/gridwell_kit/SYNCED_FROM`. The copies
aren't edited here: change them in gridwell and sync again.

Usage:
    python scripts/sync_gridwell_kit.py ../gridwell          # copy the kit from a checkout
    python scripts/sync_gridwell_kit.py --check ../gridwell  # only check the copy is current

The gridwell checkout can also be given with the `GRIDWELL_DIR` environment variable. With
`--check`, the exit status is `1` when any file differs (`SYNCED_FROM` isn't compared).
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KIT = REPO_ROOT / "tests" / "gridwell_kit"

# Each file of the kit, by its path in gridwell
FILES = {
    "cases.py": "conformance/cases.py",
    "html_grid.py": "conformance/html_grid.py",
    "ir-1.0.schema.json": "crates/gridwell-ir/schema/ir-1.0.schema.json",
}
EXPECTED = "conformance/expected/great_tables"


def kit_files(gridwell: Path) -> dict[str, Path]:
    """The kit's files (relative to `tests/gridwell_kit/`) and where they are in gridwell."""
    files = {name: gridwell / src for name, src in FILES.items()}
    for path in sorted((gridwell / EXPECTED).glob("*.json")):
        files[f"expected/{path.name}"] = path
    missing = [str(path) for path in files.values() if not path.is_file()]
    if missing or not any(name.startswith("expected/") for name in files):
        raise SystemExit(f"{gridwell} isn't a gridwell checkout with the kit (missing: {missing})")
    return files


def stale_files(files: dict[str, Path]) -> list[Path]:
    """Expected grids in the copy that gridwell no longer has."""
    return [
        path
        for path in sorted((KIT / "expected").glob("*.json"))
        if f"expected/{path.name}" not in files
    ]


def gridwell_commit(gridwell: Path) -> str:
    """The checkout's commit, and whether the kit's files have changes not committed."""
    try:
        commit = subprocess.run(
            ["git", "-C", str(gridwell), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        changed = subprocess.run(
            ["git", "-C", str(gridwell), "status", "--porcelain", "--", *FILES.values(), EXPECTED],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown (not a git checkout)"
    return f"{commit} (with changes not committed)" if changed else commit


def check(files: dict[str, Path]) -> list[str]:
    """What differs between the copy and gridwell's kit."""
    problems: list[str] = []
    for name, src in files.items():
        copy = KIT / name
        if not copy.is_file():
            problems.append(f"missing: {name}")
        elif copy.read_bytes() != src.read_bytes():
            problems.append(f"differs: {name}")
    problems += [f"not in gridwell: expected/{path.name}" for path in stale_files(files)]
    return problems


def sync(files: dict[str, Path], gridwell: Path) -> None:
    for path in stale_files(files):
        path.unlink()
        print(f"removed {path.relative_to(REPO_ROOT)}")
    for name, src in files.items():
        copy = KIT / name
        copy.parent.mkdir(parents=True, exist_ok=True)
        if not copy.is_file() or copy.read_bytes() != src.read_bytes():
            shutil.copyfile(src, copy)
            print(f"copied {copy.relative_to(REPO_ROOT)}")
    (KIT / "SYNCED_FROM").write_text(f"gridwell {gridwell_commit(gridwell)}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0].strip())
    parser.add_argument(
        "gridwell",
        nargs="?",
        default=os.environ.get("GRIDWELL_DIR"),
        help="a gridwell checkout (default: $GRIDWELL_DIR)",
    )
    parser.add_argument("--check", action="store_true", help="only check that the copy is current")
    args = parser.parse_args()
    if not args.gridwell:
        parser.error("give a gridwell checkout (or set GRIDWELL_DIR)")

    gridwell = Path(args.gridwell).resolve()
    files = kit_files(gridwell)
    if args.check:
        problems = check(files)
        for problem in problems:
            print(problem)
        if problems:
            print(f"tests/gridwell_kit/ isn't current: run scripts/sync_gridwell_kit.py {gridwell}")
            return 1
        print("tests/gridwell_kit/ is current")
        return 0
    sync(files, gridwell)
    return 0


if __name__ == "__main__":
    sys.exit(main())
