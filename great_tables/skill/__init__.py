from __future__ import annotations

import shutil
from pathlib import Path

from importlib_resources import as_file, files

SKILL_MOD = files("great_tables.skill")

DEFAULT_DEST = Path(".claude/skills/great-tables")

# Only this installer's own module files (and any bytecode cache) are excluded
# from the copy -- everything else under great_tables/skill/ is the skill's
# actual content and ships as-is, whatever that content happens to be.
_NOT_SKILL_CONTENT = shutil.ignore_patterns("__init__.py", "__main__.py", "__pycache__")


def install(dest: str | Path = DEFAULT_DEST, *, force: bool = False) -> Path:
    """Copy the bundled `great-tables` Agent Skill to `dest`.

    The skill teaches an AI coding agent the same house table-design rules on
    every run, so tables built by an agent look consistent from one run to the
    next. This copies the skill's own files (`SKILL.md`, `references/`,
    `scripts/`), unmodified, out of the installed `great_tables` package.

    Parameters
    ----------
    dest
        Where to copy the skill folder. Defaults to `.claude/skills/great-tables`,
        relative to the current working directory.
    force
        Overwrite `dest` if it already exists. By default, an existing `dest`
        raises `FileExistsError` rather than silently overwriting it.

    Returns
    -------
    Path
        The resolved destination path the skill was copied to.
    """
    dest_path = Path(dest)

    if dest_path.exists():
        if not force:
            raise FileExistsError(
                f"{dest_path} already exists. Pass force=True "
                "(or --force on the command line) to overwrite it."
            )
        shutil.rmtree(dest_path)

    with as_file(SKILL_MOD) as src_path:
        shutil.copytree(src_path, dest_path, ignore=_NOT_SKILL_CONTENT)

    return dest_path.resolve()
