#!/usr/bin/env python3
"""Validate the marketplace manifest and skill frontmatter.

Checks, with no third-party dependencies (stdlib only):

1. Every skill path listed under each plugin's ``skills`` array in
   ``.claude-plugin/marketplace.json`` exists and contains a ``SKILL.md``.
2. Every ``skills/*/SKILL.md`` has YAML frontmatter with non-empty ``name``
   and ``description`` fields, and its ``name`` matches its directory name.

Exits non-zero with a clear message if any check fails.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"
SKILLS_DIR = REPO_ROOT / "skills"


def parse_frontmatter(text):
    """Extract simple ``key: value`` pairs from a leading YAML frontmatter block.

    Returns a dict of the top-level scalar fields, or ``None`` if the file does
    not start with a ``---`` delimited frontmatter block. Only the flat
    ``name``/``description`` scalars we care about are needed, so this avoids a
    PyYAML dependency.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip("\"'")
    # No closing delimiter found.
    return None


def check_marketplace(errors):
    if not MARKETPLACE.exists():
        errors.append(f"manifest not found: {MARKETPLACE.relative_to(REPO_ROOT)}")
        return
    try:
        manifest = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{MARKETPLACE.relative_to(REPO_ROOT)}: invalid JSON: {exc}")
        return

    for plugin in manifest.get("plugins", []):
        name = plugin.get("name", "<unnamed>")
        for rel in plugin.get("skills", []):
            skill_dir = (REPO_ROOT / rel).resolve()
            label = f"plugin '{name}' -> {rel}"
            if not skill_dir.is_dir():
                errors.append(f"{label}: directory does not exist")
                continue
            if not (skill_dir / "SKILL.md").is_file():
                errors.append(f"{label}: missing SKILL.md")


def check_skill_frontmatter(errors):
    if not SKILLS_DIR.is_dir():
        errors.append(f"skills directory not found: {SKILLS_DIR.relative_to(REPO_ROOT)}")
        return
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        rel = skill_md.relative_to(REPO_ROOT)
        dir_name = skill_md.parent.name
        fields = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        if fields is None:
            errors.append(f"{rel}: missing or malformed YAML frontmatter block")
            continue
        for required in ("name", "description"):
            if not fields.get(required):
                errors.append(f"{rel}: frontmatter '{required}' is missing or empty")
        name = fields.get("name", "")
        if name and name != dir_name:
            errors.append(
                f"{rel}: frontmatter name '{name}' does not match directory name '{dir_name}'"
            )


def main():
    errors = []
    check_marketplace(errors)
    check_skill_frontmatter(errors)

    if errors:
        print("Skill validation FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Skill validation passed: marketplace paths and SKILL.md frontmatter are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
