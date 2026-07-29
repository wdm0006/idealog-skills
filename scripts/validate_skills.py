#!/usr/bin/env python3
"""Validate the marketplace manifest and skill frontmatter.

Checks, with no third-party dependencies (stdlib only):

1. Every skill path listed under each plugin's ``skills`` array in
   ``.claude-plugin/marketplace.json`` exists and contains a ``SKILL.md``.
2. Every ``skills/*/SKILL.md`` has YAML frontmatter with non-empty ``name``
   and ``description`` fields, and its ``name`` matches its directory name.
3. The ``idealog-complete`` plugin lists every ``skills/*/SKILL.md`` directory
   exactly once. Curated bundles are free to ship a subset.

Exits non-zero with a clear message if any check fails.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_REL = Path(".claude-plugin") / "marketplace.json"
SKILLS_REL = Path("skills")
COMPLETE_PLUGIN = "idealog-complete"


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


def load_manifest(repo_root, errors):
    """Read and parse the marketplace manifest, or return ``None`` on failure."""
    manifest_path = repo_root / MANIFEST_REL
    if not manifest_path.exists():
        errors.append(f"manifest not found: {MANIFEST_REL}")
        return None
    try:
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{MANIFEST_REL}: invalid JSON: {exc}")
        return None


def discover_skill_dirs(repo_root):
    """Return the on-disk ``skills/*`` directories that contain a ``SKILL.md``."""
    return sorted(md.parent for md in (repo_root / SKILLS_REL).glob("*/SKILL.md"))


def check_marketplace(repo_root, manifest, errors):
    for plugin in manifest.get("plugins", []):
        name = plugin.get("name", "<unnamed>")
        for rel in plugin.get("skills", []):
            skill_dir = (repo_root / rel).resolve()
            label = f"plugin '{name}' -> {rel}"
            if not skill_dir.is_dir():
                errors.append(f"{label}: directory does not exist")
                continue
            if not (skill_dir / "SKILL.md").is_file():
                errors.append(f"{label}: missing SKILL.md")


def check_complete_coverage(repo_root, manifest, errors):
    """Require the ``idealog-complete`` bundle to list every skill exactly once."""
    complete = [p for p in manifest.get("plugins", []) if p.get("name") == COMPLETE_PLUGIN]
    if not complete:
        errors.append(
            f"{MANIFEST_REL}: no plugin named '{COMPLETE_PLUGIN}'; "
            "it must exist and distribute every skill"
        )
        return

    for plugin in complete:
        declared = {}
        for rel in plugin.get("skills", []):
            declared.setdefault((repo_root / rel).resolve(), []).append(rel)

        for paths in declared.values():
            if len(paths) > 1:
                listed = ", ".join(paths)
                errors.append(
                    f"plugin '{COMPLETE_PLUGIN}': skill listed {len(paths)} times ({listed}); "
                    "each skill must appear exactly once"
                )

        for skill_dir in discover_skill_dirs(repo_root):
            if skill_dir.resolve() not in declared:
                rel = skill_dir.relative_to(repo_root).as_posix()
                errors.append(
                    f"plugin '{COMPLETE_PLUGIN}': missing ./{rel}; "
                    f"add it so installing '{COMPLETE_PLUGIN}' ships every skill"
                )


def check_skill_frontmatter(repo_root, errors):
    skills_dir = repo_root / SKILLS_REL
    if not skills_dir.is_dir():
        errors.append(f"skills directory not found: {SKILLS_REL}")
        return
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        rel = skill_md.relative_to(repo_root)
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


def collect_errors(repo_root):
    errors = []
    manifest = load_manifest(repo_root, errors)
    if manifest is not None:
        check_marketplace(repo_root, manifest, errors)
        check_complete_coverage(repo_root, manifest, errors)
    check_skill_frontmatter(repo_root, errors)
    return errors


def main():
    errors = collect_errors(REPO_ROOT)

    if errors:
        print("Skill validation FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(
        "Skill validation passed: marketplace paths, bundle coverage, "
        "and SKILL.md frontmatter are valid."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
