#!/usr/bin/env python3
"""Validate required packaging resources and relative Markdown links (stdlib only)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent


def main():
    errors = []
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    if not match:
        errors.append("SKILL.md: missing YAML frontmatter")
    else:
        for key in ("name", "description"):
            if not re.search(r"^" + key + r":\s*\S", match.group(1), re.M):
                errors.append("SKILL.md: missing " + key)
        if not re.search(r"^name: top-venue-paper-writing$", match.group(1), re.M):
            errors.append("SKILL.md: unexpected skill name")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", content):
            if "://" in link or link.startswith(("#", "mailto:")):
                continue
            target = link.split("#", 1)[0]
            if target and not (path.parent / target).exists():
                errors.append(str(path.relative_to(ROOT)) + ": missing link target " + target)
        for resource in re.findall(r'`((?:references|templates|examples|scripts)/[\w./-]+\.(?:md|py))`', content):
            if not (ROOT / resource).is_file():
                errors.append(str(path.relative_to(ROOT)) + ": missing resource " + resource)
    for resource in ("LICENSE", "agents/openai.yaml", "assets/banner.png", "assets/icon.png", "assets/icon.svg"):
        if not (ROOT / resource).is_file():
            errors.append("Missing resource: " + resource)
    if errors:
        print("\n".join(errors))
        return 1
    print("Skill metadata, required resources and relative Markdown links: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
