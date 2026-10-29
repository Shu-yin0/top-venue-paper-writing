#!/usr/bin/env python3
"""Copy the skill into a fresh agent skill folder. Python 3.8+, no dependencies."""
import argparse
import os
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
NAME = "top-venue-paper-writing"
FILES = ("SKILL.md", "LICENSE", "scripts/paperlint.py")
DIRS = ("agents", "assets", "references", "templates", "examples")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--agent", choices=("codex", "claude"))
    choice.add_argument("--dest", type=Path, help="Complete destination skill directory")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.dest is not None:
        dest = args.dest.expanduser().resolve()
    elif args.agent == "codex":
        dest = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / "skills" / NAME
    else:
        dest = Path.home() / ".claude" / "skills" / NAME
    dest = dest.expanduser().resolve()
    if dest.exists():
        parser.error("Destination already exists; preserve or move it before installing: " + str(dest))
    if ROOT == dest or ROOT in dest.parents:
        parser.error("Choose a destination outside this repository to avoid recursive copies.")
    for name in FILES + DIRS:
        if not (ROOT / name).exists():
            parser.error("Missing source resource: " + name)
    print("Destination: " + str(dest))
    if args.dry_run:
        print("Dry run: no files written.")
        return
    try:
        dest.mkdir(parents=True, exist_ok=False)
        for name in FILES:
            target = dest / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, target)
        for name in DIRS:
            shutil.copytree(ROOT / name, dest / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    except OSError as exc:
        parser.error("Installation incomplete; inspect the printed destination before retrying: " + str(exc))
    print("Installed " + NAME + ". Ask your agent to use it; start a new session if discovery has not refreshed.")


if __name__ == "__main__":
    main()
