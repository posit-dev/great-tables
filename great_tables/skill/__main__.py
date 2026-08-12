from __future__ import annotations

import argparse
import sys

from . import DEFAULT_DEST, install


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m great_tables.skill",
        description="Install the bundled great-tables Agent Skill into a project.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    install_parser = subparsers.add_parser(
        "install", help="Copy the skill into a destination folder."
    )
    install_parser.add_argument(
        "dest",
        nargs="?",
        default=str(DEFAULT_DEST),
        help=f"where to copy the skill (default: {DEFAULT_DEST})",
    )
    install_parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite the destination if it already exists",
    )

    args = parser.parse_args(argv)

    if args.command == "install":
        try:
            dest = install(args.dest, force=args.force)
        except FileExistsError as e:
            print(str(e), file=sys.stderr)
            return 1
        print(f"Installed the great-tables skill to {dest}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
